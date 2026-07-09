#!/usr/bin/env python3
"""Validate per-filterset inventory YAML logs.

Each file in inventory/units/*.yaml describes one physical Motorola cavity
filterset and its tuning state. This tool enforces that logs are internally
consistent BEFORE a unit can be marked commissioned, so a "done" unit always
carries real measured numbers.

Usage:
    python tools/validate_inventory.py                 # validate inventory/units/*.yaml
    python tools/validate_inventory.py path/to/*.yaml  # validate specific files
    python tools/validate_inventory.py --json          # machine-readable report

Exit code is non-zero if any file fails validation.
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

import yaml

# Amateur/GMRS band edges (MHz) and the plausible repeater split window (MHz).
# split_min/split_max guard against typos (e.g. rx and tx swapped or a decimal
# slip) rather than encoding a hard regulatory rule.
BANDS = {
    "2m":   {"lo": 144.0, "hi": 148.0,  "rf": "vhf", "split_min": 0.5,  "split_max": 0.7},
    "70cm": {"lo": 440.0, "hi": 450.0,  "rf": "uhf", "split_min": 4.5,  "split_max": 5.5},
    "gmrs": {"lo": 462.0, "hi": 467.75, "rf": "uhf", "split_min": 4.5,  "split_max": 5.5},
}

# Model-number prefix -> RF range. Per repeater-builder: the T1480 series is
# Motorola High Band (VHF 132-174 MHz); the T1500 series is UHF (406-512 MHz).
# Used to catch a "VHF cavity declared on a UHF band" (or vice-versa) typo.
VHF_MODEL_PREFIXES = ("T148",)
UHF_MODEL_PREFIXES = ("T150", "T4084", "T4085", "T5002")

REQUIRED_FIELDS = (
    "id", "model", "band", "cavities", "cable_state",
    "rx_freq_mhz", "tx_freq_mhz", "status",
)
VALID_CABLE_STATES = {"intact", "cut", "partial", "rebuilt"}
VALID_STATUSES = {"planned", "cabling", "tuning", "commissioned", "retired"}


class ValidationError(Exception):
    """Raised when a unit log fails validation."""


def _model_rf(model: str) -> str | None:
    m = str(model).upper()
    if m.startswith(UHF_MODEL_PREFIXES):
        return "uhf"
    if m.startswith(VHF_MODEL_PREFIXES):
        return "vhf"
    return None


def validate_unit(path: str | Path) -> dict:
    """Load and validate one unit YAML file. Returns the parsed dict on success.

    Raises ValidationError with a message naming the file and problem on failure.
    """
    path = Path(path)
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValidationError(f"{path}: invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: top-level YAML must be a mapping")

    def err(msg: str) -> ValidationError:
        return ValidationError(f"{path}: {msg}")

    # Required fields present
    missing = [f for f in REQUIRED_FIELDS if data.get(f) in (None, "")]
    if missing:
        raise err(f"missing required field(s): {', '.join(missing)}")

    band = data["band"]
    if band not in BANDS:
        raise err(f"unknown band {band!r}; expected one of {sorted(BANDS)}")
    spec = BANDS[band]

    # Cavities: positive integer
    cavities = data["cavities"]
    if not isinstance(cavities, int) or isinstance(cavities, bool) or cavities < 1:
        raise err(f"cavities must be a positive integer, got {cavities!r}")

    if data["cable_state"] not in VALID_CABLE_STATES:
        raise err(f"cable_state must be one of {sorted(VALID_CABLE_STATES)}")

    if data["status"] not in VALID_STATUSES:
        raise err(f"status must be one of {sorted(VALID_STATUSES)}")

    # Model band matches declared band
    rf = _model_rf(data["model"])
    if rf is not None and rf != spec["rf"]:
        raise err(
            f"model {data['model']!r} is {rf.upper()} but band {band!r} is "
            f"{spec['rf'].upper()}; T1480/T1500 are VHF-only"
        )

    # Frequencies numeric and in band
    for key in ("rx_freq_mhz", "tx_freq_mhz"):
        f = data[key]
        if not isinstance(f, (int, float)) or isinstance(f, bool):
            raise err(f"{key} must be a number, got {f!r}")
        if not (spec["lo"] <= f <= spec["hi"]):
            raise err(
                f"{key}={f} MHz out of {band} band ({spec['lo']}-{spec['hi']} MHz)"
            )

    # Split plausibility
    split = abs(float(data["rx_freq_mhz"]) - float(data["tx_freq_mhz"]))
    if not (spec["split_min"] <= split <= spec["split_max"]):
        raise err(
            f"TX/RX split {split:.3f} MHz outside plausible {band} window "
            f"({spec['split_min']}-{spec['split_max']} MHz); check for typo or swap"
        )

    # Commissioning gate: real measurements required
    if data["status"] == "commissioned":
        for key in ("insertion_loss_db", "isolation_db"):
            v = data.get(key)
            if not isinstance(v, (int, float)) or isinstance(v, bool):
                raise err(
                    f"status=commissioned requires measured {key} (a number)"
                )

    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="unit YAML files (default: inventory/units/*.yaml)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)

    paths = args.paths or sorted(glob.glob("inventory/units/*.yaml"))
    results = []
    ok = True
    for p in paths:
        try:
            unit = validate_unit(p)
            results.append({"file": p, "ok": True, "id": unit.get("id"), "status": unit.get("status")})
        except ValidationError as exc:
            ok = False
            results.append({"file": p, "ok": False, "error": str(exc)})

    if args.json:
        print(json.dumps({"ok": ok, "count": len(results), "results": results}, indent=2))
    else:
        if not paths:
            print("[OK] no unit files found (inventory/units/*.yaml empty)")
        for r in results:
            if r["ok"]:
                print(f"[OK]    {r['file']}  ({r['id']}, {r['status']})")
            else:
                print(f"[ERROR] {r['error']}")
        print(f"\n{sum(1 for r in results if r['ok'])}/{len(results)} valid")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
