---
title: Motorola T1500 (UHF) Reference
scope: T1500-series UHF duplexer facts, harness lengths, connector rules
last_updated: 2026-07-09
---

# Motorola T1500 Series (UHF 406-512 MHz)

Source: https://www.repeater-builder.com/motorola/t1500/t1500.html (Source 2),
original manual 6881102E96 rev G (1983-01-25).

## Configuration

- Band: **UHF, 406-512 MHz**.
- Four cavities in two pairs:
  - **Two loop cavities** - used for the **lower** frequency.
  - **Two probe cavities** - used for the **higher** frequency.

## Phasing rule (do not get this backwards)

- Connect the **lower** of the two frequencies to a **loop** cavity.
- Connect the **higher** frequency to a **probe** cavity.

For a repeater, RX (receive) and TX (transmit) are the two frequencies; assign
each to loop or probe by which is numerically lower/higher, not by whether it is
RX or TX. Example (70cm, RX high / TX low): TX is lower -> loop pair; RX is
higher -> probe pair.

## Interconnect cable lengths (PL-259 tip-to-tip)

These are the phasing harness lengths. If your jumpers are cut, rebuild to these
exact tip-to-tip dimensions. See `docs/procedures/cabling-harness.md`.

| Freq range | Cable #1 | Cable #2 | Cable #3 | Cable #4 |
|------------|----------|----------|----------|----------|
| 406-430 MHz | 9-3/8" | 9-3/4" | 6-3/4" | 10-1/2" |
| 430-470 MHz | 8-1/2" | 8-3/4" | 5-3/4" | 9-3/4" |

Both 70cm (440-450) and GMRS (462/467) fall in the **430-470 MHz** row.

## Connectors and cable (explicit requirement)

- Use only **silver-plated double-shielded cable and silver-plated connectors**.
- Do **NOT** use nickel- or chrome-plated connectors - they degrade notch depth.

## Parts notes

- Original tuning knobs P/N 36-84458A01 are NLA (no longer available).
- Replacement locknuts: McMaster-Carr 94830A550.

## Per-model specs (from Source 5)

| Model | Cavities / type | Min split | Insertion loss | Isolation |
|-------|-----------------|-----------|----------------|-----------|
| T1503A | 2 cavity, pass-reject | 5 MHz | 0.7-0.8 dB | 55 dB |
| T1504A | 4 cavity | 2 MHz | 1.3-1.6 dB | 80-85 dB |
| T1507A | 4 cavity, bandpass only | 5 MHz | 2.0 dB | 55 dB |

Note T1507A is **bandpass only** (no reject notch) - useful as a preselector or
in a Bp/Br chain, but on its own it will not give TX/RX isolation the way a
pass-reject unit does.
