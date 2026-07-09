---
title: Motorola T1480 (VHF) Reference
scope: T1480-series VHF High Band duplexer facts and known gaps
last_updated: 2026-07-09
---

# Motorola T1480 Series (VHF High Band, 132-174 MHz)

Sources: index page (Source 6) and the T1480 VHF PDF (Source 1). The PDF is a
scanned image with no text layer, so harness cut-lengths and the step-by-step
tuning procedure are **not yet recovered** (OCR follow-up tracked in
`docs/reference/sources.md`).

## What is known

- Band: **VHF High Band, 132-174 MHz** (covers 2m amateur, 144-148).
- Offered in **2-4 cavity** configurations.
- Member models: **T1481, T1482, T1485A, T1485AF, T1487A, T1487AF**.
- Pass-notch (band-reject) cavities, same family behavior as the UHF T1500.

## Expected specs by cavity count (from comparable VHF units, Source 4/5)

The T1480 spec sheet numbers are pending OCR. Until then, use these
same-class VHF pass-notch figures as planning targets:

| Cavities | Typical min split | Insertion loss | Isolation |
|----------|-------------------|----------------|-----------|
| 4 | 0.5-0.6 MHz | 1.5 dB | 80-95 dB |
| 6 | 0.3-0.4 MHz | 2.0-2.2 dB | 95-120 dB |

For **2m at a 600 kHz split**, a 4-cavity T1480 is workable but near its edge;
expect roughly 1.5 dB insertion loss and target as much isolation as tuning
allows (aim 70+ dB minimum, more is better). See
`docs/theory/split-vs-isolation.md`.

## Harness cut-lengths (UNKNOWN - measure or OCR)

No VHF T1480 tip-to-tip harness dimensions were recoverable from text sources.
Options:
1. OCR the Source 1 PDF (preferred - it is the authoritative figure).
2. Measure an intact reference unit's jumpers exactly before cutting anything.
3. Compute the quarter-wave electrical length for the band and cable velocity
   factor (see `docs/procedures/cabling-harness.md`), then verify by tuning.

Do not discard or shorten any intact VHF jumper until its length is recorded.
