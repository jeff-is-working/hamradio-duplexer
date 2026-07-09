---
title: Motorola Duplexer Cross-Reference and Specs
scope: Model -> band -> configuration decode tables with citations
last_updated: 2026-07-09
---

# Motorola Duplexer Cross-Reference

Decode your cavities by the model / part number stamped on the casting, then read
across to band, cavity count, minimum usable split, insertion loss, and isolation.
This is the table to consult before assigning a filterset to a band.

> Key correction: **T1480 series = VHF (High Band, 132-174 MHz). T1500 series =
> UHF (406-512 MHz).** They are different bands, not two VHF families. Source 2
> and Source 6.

## Motorola family map (Source 6)

| Family | Band | Cavities | Member models |
|--------|------|----------|---------------|
| T1480 | VHF 132-174 MHz | 2-4 | T1481, T1482, T1485A, T1485AF, T1487A, T1487AF |
| T1500 | UHF 406-512 MHz | 4 (2 loop + 2 probe) | T1500-T1507 (incl. T1503A, T1504A, T1507A) |
| T4084A / T4085A / T5002A | UHF | 4-can | - |

Some Motorola units are relabeled Sinclair (P/Ns 0185417U01/U02/U03).

## Motorola UHF pass-notch specs (Source 5)

| Model | Band | Cavities / type | Min split | Insertion loss | Isolation |
|-------|------|-----------------|-----------|----------------|-----------|
| T1503A | UHF | 2 cavity, pass-reject | 5 MHz | 0.7-0.8 dB | 55 dB |
| T1504A | UHF | 4 cavity | 2 MHz | 1.3-1.6 dB | 80-85 dB |
| T1507A | UHF | 4 cavity, bandpass only | 5 MHz | 2.0 dB | 55 dB |

## Motorola cross-reference to OEM (Source 4)

"Min split" = minimum usable TX/RX separation. "Isolation" = TX/RX notch depth (dB).

### VHF 132-174 MHz

| Motorola | OEM | Freq (MHz) | Ins. loss | Min split (MHz) | Isolation (dB) | Cavities |
|----------|-----|-----------|-----------|-----------------|----------------|----------|
| TDD6200 | Sinclair Q202GC-U | 132-174 | 1.5 | 0.5 | 80 / 95 | 4 |
| TDD6459 | Sinclair Q202GC-N | 132-174 | 1.5 | 0.5 | 80 / 95 | 4 |
| TDD6830 | Decibel DB4060WC | 144-174 | 1.5 | 0.5 | 80 / 80 | 4 |
| TDD7110 | Decibel DB4060WOC | 144-174 | 1.5 | 0.5 | 80 / 80 | 4 |
| TDD6840 | Decibel DB4062WC | 144-174 | 2.2 | 0.3 | 100 / 100 | 6 |
| TDD7200 | Decibel DB4062WOC | 144-174 | 2.2 | 0.3 | 100 / 100 | 6 |
| TDD7040 | Sinclair Q2222E | 138-174 | 1.25 | 1.0 | 75 / 85 | 4 |

### UHF 406-512 MHz

| Motorola | OEM | Freq (MHz) | Ins. loss | Min split (MHz) | Isolation (dB) | Cavities |
|----------|-----|-----------|-----------|-----------------|----------------|----------|
| TDE7060 | Decibel DB4068 | 406-430 | 1.3 | 2.75 | 70 / 75 | 6 |
| TDE6740 | Celwave PD5264 | 406-470 | 1.0 | 5.0 | 120 / 120 | 4 |
| TDE6960 | Sinclair Q3220E | 406-512 | 0.8 | 3.0 / 10 | 75 / 90 | 4 |
| TDE6660 | Celwave PD6336A | 406-470 | 1.2 | 10 | 80 | 6 |
| 0185417U05 | Celwave PD526-4-2 | 430-470 | 1.3 | 3 / 5 | 100 / 120 | 6 |

## Reading the tradeoff

The pattern that governs every tuning decision (Source 5):

- **4-cavity**: wider min split (0.5+ MHz VHF, 3-5 MHz UHF), ~1.0-1.6 dB loss,
  70-95 dB isolation.
- **6-cavity**: tighter min split possible (0.3-0.4 MHz VHF), ~2.0-2.2 dB loss,
  95-120 dB isolation.

More cavities buy isolation and tighter split at the cost of insertion loss.
For **2m at a 600 kHz (0.6 MHz) split**, a 4-cavity VHF set is at the edge of its
comfortable range; 6-cavity is preferred if you have it. For **UHF at 5 MHz**
(70cm and GMRS), a 4-cavity set has ample margin.
