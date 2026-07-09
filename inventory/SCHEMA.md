---
title: Inventory Unit Schema
scope: Fields for per-filterset YAML logs and validation rules
last_updated: 2026-07-09
---

# Inventory Unit Schema

One YAML file per physical filterset lives in `inventory/units/`. Each is
validated by `tools/validate_inventory.py` (run locally and in CI).

## Fields

| Field | Required | Type | Notes |
|-------|----------|------|-------|
| `id` | yes | string | Unique slug, e.g. `t1480-4cav-a`. |
| `model` | yes | string | Stamped model, e.g. `T1480`, `T1504A`. Prefix must match band RF (T148x=VHF, T150x=UHF). |
| `band` | yes | enum | `2m`, `70cm`, or `gmrs`. |
| `cavities` | yes | int >=1 | Number of cavities. |
| `cable_state` | yes | enum | `intact`, `cut`, `partial`, `rebuilt`. |
| `rx_freq_mhz` | yes | number | Repeater receive freq; must be in band. |
| `tx_freq_mhz` | yes | number | Repeater transmit freq; must be in band. |
| `status` | yes | enum | `planned`, `cabling`, `tuning`, `commissioned`, `retired`. |
| `ctcss_hz` | no | number | PL tone if used. |
| `insertion_loss_db` | conditional | number | **Required when `status: commissioned`.** |
| `isolation_db` | conditional | number | **Required when `status: commissioned`.** |
| `harness_lengths_in` | no | list/map | Recorded tip-to-tip jumper lengths. |
| `notes` | no | string | Free text. |

## Validation rules (enforced)

- All required fields present and non-empty.
- `band` is one of the known bands.
- `cavities` is a positive integer.
- `cable_state` and `status` are from the allowed sets.
- Model RF class matches band RF (T148x VHF cannot be on a UHF band; T150x UHF
  cannot be on 2m).
- `rx_freq_mhz` and `tx_freq_mhz` are numeric and within the band edges.
- TX/RX split falls in the plausible window for the band (typo/swap guard):
  2m 0.5-0.7 MHz; 70cm and GMRS 4.5-5.5 MHz.
- `status: commissioned` requires numeric `insertion_loss_db` and `isolation_db`.

## Running the validator

```bash
python tools/validate_inventory.py            # all units, human-readable
python tools/validate_inventory.py --json     # machine-readable
python tools/validate_inventory.py inventory/units/foo.yaml   # one file
```

Exit code is non-zero if any unit fails, so CI blocks a bad log.
