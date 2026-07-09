---
title: hamradio-duplexer README
scope: Notes, procedures, and logs for tuning Motorola cavity duplexers
last_updated: 2026-07-09
---

# hamradio-duplexer

Notes, reference material, procedures, and per-unit logs for **cabling, tuning,
and commissioning Motorola cavity filtersets** into working duplexers for
amateur (2m, 70cm) and GMRS repeater use.

Test gear assumed: **NanoVNA** (S21/S11) and **tinySA Ultra** (spectrum +
tracking source).

## Hardware -> band map

| Motorola family | Band | Repeater use | Split | Difficulty |
|-----------------|------|--------------|-------|-----------|
| **T1480 series** (VHF 132-174) | 2m | 144-148 | 600 kHz | Hard (near 4-cav limit) |
| **T1500 series** (UHF 406-512) | 70cm | 440-450 | 5 MHz | Easy |
| **T1500 series** (UHF 406-512) | GMRS | 462/467 | 5 MHz | Easy |

Important: **T1480 = VHF, T1500 = UHF.** They are different bands. See
`docs/reference/cross-reference.md`.

## Where things are

```
docs/reference/    # Motorola specs, cross-ref, cited sources
docs/theory/       # how pass-notch cavities and the split/isolation tradeoff work
docs/procedures/   # cabling harness, NanoVNA tuning, tinySA tuning, commissioning
docs/status/       # dated session status files
projects/          # one folder per band build (2m, 70cm, gmrs) with band plans + logs
inventory/         # per-filterset YAML logs + validator schema
tools/             # validate_inventory.py
tests/             # pytest for the validator
```

## Quick start

1. Read `docs/theory/pass-notch-cavities.md` and
   `docs/theory/split-vs-isolation.md`.
2. Identify each physical set by its stamped model
   (`docs/reference/cross-reference.md`).
3. Copy `inventory/filterset-template.yaml` to `inventory/units/<id>.yaml` and
   fill it in. Validate:
   ```bash
   pip install -r requirements.txt
   python tools/validate_inventory.py
   ```
4. Rebuild cut harnesses (`docs/procedures/cabling-harness.md`), tune
   (`docs/procedures/tuning-nanovna.md`), commission
   (`docs/procedures/commissioning.md`).

## Safety

Radio frequency energy and transmit power are involved. Never key a transmitter
into an unterminated or half-built duplexer; terminate open ports in 50 ohms.
Do not connect the tinySA Ultra input directly to transmit power - use an
attenuator or coupler. Follow all licensing/coordination rules (amateur band
coordination; FCC Part 95E for GMRS).

## Accessibility

See [ACCESSIBILITY.md](ACCESSIBILITY.md). Docs use plain language, real tables
(not ASCII art), and never rely on color alone.

## License

MIT (see [LICENSE](LICENSE)). Third-party specs are cited to their sources in
`docs/reference/sources.md` and archived for personal, non-commercial study.
