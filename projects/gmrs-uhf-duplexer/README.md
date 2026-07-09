---
title: GMRS UHF Duplexer Build
scope: Working folder for the GMRS (462/467) repeater duplexer build
last_updated: 2026-07-09
---

# GMRS UHF Duplexer (T1500 series)

Hardware: **Motorola T1500 series, UHF (406-512 MHz)**. Same UHF cavities and
5 MHz split margin as 70cm - the easiest of the three to commission.

## Band plan (tunable placeholders)

| Parameter | Value |
|-----------|-------|
| Band | GMRS, 462/467 MHz |
| Repeater output (TX) | 462.550 MHz (placeholder - one of 8 GMRS repeater pairs) |
| Repeater input (RX) | 467.550 MHz (placeholder) |
| Split | 5 MHz |
| CTCSS/PL | TBD |
| Target isolation | 80+ dB |
| Target insertion loss | 1.0-1.6 dB |

Regulatory: GMRS repeaters (FCC Part 95E) are allowed only on the **8 designated
462.xxx output / 467.xxx input pairs**. Pick a real pair when configuring;
placeholders above use the 462.550/467.550 pair for illustration.

Harness: **430-470 MHz** row in `docs/reference/motorola-t1500-uhf.md`.
Silver-plated connectors only. Phasing: lower freq (TX, 462) -> loop pair; higher
freq (RX, 467) -> probe pair.

## Procedure links

- Cabling: `docs/procedures/cabling-harness.md`
- Tuning: `docs/procedures/tuning-nanovna.md`, `docs/procedures/tuning-tinysa-ultra.md`
- Commissioning: `docs/procedures/commissioning.md`
- Reference: `docs/reference/motorola-t1500-uhf.md`

## Build log

| Date | Step | NanoVNA / tinySA reading | Notes |
|------|------|--------------------------|-------|
| YYYY-MM-DD | | | |
