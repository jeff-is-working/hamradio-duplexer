---
title: Session Status - Repo Scaffold
scope: Initial build-out of the duplexer notes/tuning repo
last_updated: 2026-07-09
---

# 2026-07-09 - Repo Scaffold

## What was done

- Created public GitHub repo `jeff-is-working/hamradio-duplexer` from the org
  project template.
- Filed issues #3-#7 (scaffold, reference, theory+procedures, inventory
  validator, per-band folders), each with acceptance criteria.
- Fetched and summarized the repeater-builder sources; wrote cited reference
  docs. Two Motorola PDFs are un-OCR'd scans (follow-up).
- Wrote theory, procedure (cabling/NanoVNA/tinySA/commissioning), and per-band
  project docs (2m, 70cm, GMRS) with tunable-placeholder frequency plans.
- TDD: inventory YAML schema + `tools/validate_inventory.py` (test-first, 11
  tests). Validator gates `commissioned` on measured IL/isolation.
- Opened PR #8 closing #3-#7.

## Key decision / correction

- **T1480 series = VHF (132-174 MHz) -> 2m. T1500 series = UHF (406-512 MHz) ->
  70cm and GMRS.** This corrected the initial assumption that both were VHF and
  drove the validator's model-RF check and all band mapping.

## Validation evidence

- `pytest`: 11 passed. `ruff check .`: clean. `validate_inventory.py`: 1/1 valid.

## What's left

- **OCR the two Motorola PDFs** (Sources 1 and 3) to recover VHF T1480 harness
  tip-to-tip lengths and the stock step-by-step tuning procedure.
- Replace the example inventory unit with the user's real filtersets (stamped
  model numbers, cavity counts, cable states, coordinated frequencies).
- Record intact reference-set harness lengths before cutting anything.
- Merge PR #8 after CI passes.

## Lessons learned

- Bare `pytest`/`find` get rewritten by the rtk shell hook and can misreport
  (e.g. "No tests collected"); run via `rtk proxy ...` or `python3 -m pytest` to
  get true results.
- The template CI auto-detects Python via `requirements.txt` and runs
  ruff + pytest, so the validator is exercised in CI with no extra workflow.
