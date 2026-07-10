---
title: Session Status - OSINT Source List + Community Reply Draft
scope: GMRS-repurpose source research and a Reddit reply draft
last_updated: 2026-07-09
---

# 2026-07-09 - OSINT Sources + Community Reply

## What was done

- Merged PR #8; `main` now carries the full repo scaffold (issues #3-#7 closed).
- Ran an OSINT collection pass (public sources only) for documented cases of
  people repurposing/retuning Motorola cavity duplexers for GMRS. Produced a
  tiered, source-reliability-rated list (delivered in chat).
- Drafted a mentor-voice ("Elmer") Reddit reply for a newcomer who bought a
  two-can UHF pass-notch duplexer for $20 (bundled with an MSF5000), with the
  interconnect harness missing. Final draft stays general, points to the
  repeater-builder docs and a few GMRS/NanoVNA tuning threads, no bespoke
  hand-holding.

## Key facts confirmed this session

- GMRS is UHF, so only the T1500-series (UHF) hardware applies; T1480 (VHF)
  cannot be tuned to GMRS. Confirming null result, not a gap.
- A 2-cavity pass-notch set gives ~50-something dB isolation - light for tight
  duplex at power; wants a wide split and antenna separation.
- Each cavity is an independent 2-port device, so it can be characterized (pass
  peak + reject notch) individually on a NanoVNA without the phasing harness.
  The harness is only required to run the set as a system.

## Best GMRS-repurpose sources found

- KK4ICE "Finished Up The Motorola T-1504 UHF Duplexers" (refurb, ~102 dB
  isolation / 1.1 dB IL) - http-only, broken TLS cert; use Wayback.
- repeater-builder groups.io "Motorola T1504 Duplexer" and "GMRS Repeater Build"
  threads.
- myGMRS topics 483 (T1504A), 4432 (tuning a duplexer), 5259 (beginner build).
- RadioReference NanoVNA V2 PLUS4 duplexer-tuning thread; nanorfe.com tuning
  notes; YouTube "How to Tune a UHF Duplexer for Ham Radio and GMRS".

## Open follow-ups (unchanged / new)

- OCR the two Motorola PDFs for T1480 VHF harness lengths + stock tuning steps.
- Optional: commit the GMRS-repurpose source list as
  `docs/reference/gmrs-repurpose-sources.md` (would want its own issue + PR).
- Replace the example inventory unit with the user's real filtersets.
