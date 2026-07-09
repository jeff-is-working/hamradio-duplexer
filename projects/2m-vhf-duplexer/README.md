---
title: 2m VHF Duplexer Build
scope: Working folder for the 2m (144-148) repeater duplexer build
last_updated: 2026-07-09
---

# 2m VHF Duplexer (T1480 series)

Hardware: **Motorola T1480 series, VHF High Band (132-174 MHz)**. This is the
**hard case** - a 600 kHz split is near a 4-cavity set's limit. Use your
most-cavity VHF set here.

## Band plan (tunable placeholders)

| Parameter | Value |
|-----------|-------|
| Band | 2m, 144-148 MHz |
| Repeater output (TX) | 145.750 MHz (placeholder) |
| Repeater input (RX) | 145.150 MHz (placeholder) |
| Split | 600 kHz |
| CTCSS/PL | TBD |
| Target isolation | 70 dB floor, chase higher |
| Target insertion loss | ~1.5 dB (4-cavity) |

Set real frequencies when coordinated; update the unit YAML in
`inventory/units/`.

## Procedure links

- Theory: `docs/theory/pass-notch-cavities.md`, `docs/theory/split-vs-isolation.md`
- Cabling: `docs/procedures/cabling-harness.md` (VHF lengths pending OCR)
- Tuning: `docs/procedures/tuning-nanovna.md`, `docs/procedures/tuning-tinysa-ultra.md`
- Commissioning: `docs/procedures/commissioning.md`
- Reference: `docs/reference/motorola-t1480-vhf.md`

## Build log

| Date | Step | NanoVNA / tinySA reading | Notes |
|------|------|--------------------------|-------|
| YYYY-MM-DD | (e.g. recorded harness lengths) | | |
