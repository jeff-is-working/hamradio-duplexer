---
title: Source Index
scope: Every external reference used in this repo, with fetch dates and citations
last_updated: 2026-07-09
---

# Sources

All specifications in this repo trace back to the sources below. Fetched
2026-07-09 unless noted. These are third-party references archived for personal,
non-commercial study of hardware the owner physically possesses.

| # | Source | URL | Status |
|---|--------|-----|--------|
| 1 | Motorola T1480-series VHF duplexers (PDF) | https://www.repeater-builder.com/antenna/pdf/motorola-t1480-series-vhf-duplexers.pdf | Scanned image PDF, no text layer - needs OCR |
| 2 | Motorola T1500 (UHF) page | https://www.repeater-builder.com/motorola/t1500/t1500.html | Extracted |
| 3 | Motorola UHF duplexer (PDF) | https://www.repeater-builder.com/antenna/pdf/motorola-uhf-duplexer.pdf | Scanned image PDF, no text layer - needs OCR |
| 4 | Motorola duplexer cross-reference | https://www.repeater-builder.com/antenna/motorola-duplexer-cross-ref.html | Extracted |
| 5 | Duplexer specifications | https://www.repeater-builder.com/antenna/duplexer-specs.html | Extracted |
| 6 | Antenna systems index | https://www.repeater-builder.com/antenna/ant-sys-index.html | Extracted (index) |

## Additional tuning/theory references (linked from Source 6)

- "Why are there quarter-wave coax cables between my duplexer's cavities?" - Gary Schafer K4FMX. Explains the electrical role of the interconnect jumpers.
- "How to Tune a Pass Cavity" - Telewave (video).
- Sinclair "Tuning Instructions for 'P' and 'Q' series cavity duplexers".
- TX-RX "Tuning and Adjusting Vari-Notch Duplexers".
- "Methods of Tuning Cavity Resonators According to Application" - W.F. Lieske.
- "Duplexer Theory and Tuning" - Dave Metz WA0AUQ.
- "A Guide to Duplexer Specifications" - Paul Kelley N1BUG (130+ models).
- "When Band-Pass/Band-Reject (Bp/Br) Duplexers Really Aren't Band-Pass" - KA7OEI.

## Known gaps (OCR follow-up)

Sources 1 and 3 (the two authoritative Motorola PDFs) are JBIG2-encoded scans
with no selectable text. They hold the **T1480 VHF harness cut-lengths** and the
**step-by-step Motorola tuning procedure**, which are NOT recoverable without
OCR. Tracked as a follow-up task. Until then, VHF harness lengths must be
measured empirically (see `docs/procedures/cabling-harness.md`) or taken from an
intact reference unit.
