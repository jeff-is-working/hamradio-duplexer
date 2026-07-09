---
title: Pass-Notch (Band-Reject) Cavity Theory
scope: How Motorola pass-notch cavities and their phasing harness work
last_updated: 2026-07-09
---

# Pass-Notch (Band-Reject) Cavities

The Motorola T1480 (VHF) and T1500 (UHF) duplexers are **pass-notch** cavities,
also called **band-reject** or **band-pass/band-reject (Bp/Br)**. Understanding
what each cavity does makes tuning predictable instead of guesswork.

## The job of a duplexer

A repeater transmits and receives at the same time on one antenna, on two
frequencies separated by the "split" (0.6 MHz on 2m, 5 MHz on UHF). The duplexer
must:

1. Pass the TX signal to the antenna with low loss, while **deeply notching**
   the TX energy that would otherwise reach the receiver.
2. Pass the RX signal from the antenna to the receiver with low loss, while
   **notching** the receiver's sensitivity at the TX frequency.

The notch (reject) is what protects the receiver from being desensed by the
co-located transmitter.

## What one cavity does

Each cavity is a tuned resonator. A single pass-notch cavity produces:

- A **pass** response near its resonant frequency (low insertion loss), and
- A sharp **reject notch** offset from resonance. The offset direction and depth
  are set by the **coupling loop/probe** and the **phasing cable** length.

The tuning rod moves the resonant frequency. The loop/probe orientation and the
interconnect cable length place the notch at the *other* leg's frequency.

## Loop vs probe cavities (T1500)

The T1500 UHF set uses two cavity types:

- **Loop cavities** carry the **lower** frequency leg.
- **Probe cavities** carry the **higher** frequency leg.

This is a hardware distinction - do not swap them. See
`docs/reference/motorola-t1500-uhf.md` for the phasing rule.

## Why there are coax jumpers between cavities

The interconnect coax jumpers are **not just wires** - they are electrical-length
(quarter-wave-class) phasing sections. Their length transforms the cavity's
impedance so the notch lands at the correct offset frequency and combines
correctly with the other cavities. Cut a jumper to the wrong length and the notch
moves, shrinks, or the insertion loss rises - even if every cavity is perfectly
tuned.

This is why a set with **cut jumpers** cannot simply be reconnected with random
coax. The lengths must be restored to the documented tip-to-tip dimensions (or
the correct electrical length for the band). See
`docs/procedures/cabling-harness.md`.

Reference: "Why are there quarter-wave coax cables between my duplexer's
cavities?" - Gary Schafer K4FMX (linked from Source 6).

## Bandpass-only caveat

Some models (e.g. T1507A) are **bandpass only** - they pass a band but do not
produce a reject notch. On their own they will not give TX/RX isolation. They are
used as preselectors or combined with reject cavities in a Bp/Br chain.
Reference: "When Bp/Br Duplexers Really Aren't Band-Pass" - KA7OEI.
