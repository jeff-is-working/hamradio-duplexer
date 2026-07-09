---
title: 70cm UHF Duplexer Build
scope: Working folder for the 70cm (440-450) repeater duplexer build
last_updated: 2026-07-09
---

# 70cm UHF Duplexer (T1500 series)

Hardware: **Motorola T1500 series, UHF (406-512 MHz)**. A 5 MHz split gives a
4-cavity UHF set ample margin - this is an easy build.

## Band plan (tunable placeholders)

| Parameter | Value |
|-----------|-------|
| Band | 70cm, 440-450 MHz |
| Repeater output (TX) | 444.150 MHz (placeholder) |
| Repeater input (RX) | 449.150 MHz (placeholder) |
| Split | 5 MHz |
| CTCSS/PL | TBD |
| Target isolation | 80+ dB |
| Target insertion loss | 1.0-1.6 dB |

Harness: use the **430-470 MHz** row lengths in
`docs/reference/motorola-t1500-uhf.md`. Silver-plated connectors only.
Phasing: lower freq (TX, 444) -> loop pair; higher freq (RX, 449) -> probe pair.

## Procedure links

- Cabling: `docs/procedures/cabling-harness.md`
- Tuning: `docs/procedures/tuning-nanovna.md`, `docs/procedures/tuning-tinysa-ultra.md`
- Commissioning: `docs/procedures/commissioning.md`
- Reference: `docs/reference/motorola-t1500-uhf.md`

## Build log

| Date | Step | NanoVNA / tinySA reading | Notes |
|------|------|--------------------------|-------|
| YYYY-MM-DD | | | |
