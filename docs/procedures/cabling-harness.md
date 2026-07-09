---
title: Procedure - Cabling and Rebuilding the Phasing Harness
scope: Restoring cut interconnect jumpers to correct electrical length
last_updated: 2026-07-09
---

# Cabling and Harness Rebuild

Some of the filtersets have intact cabling; others have the jumpers **cut between
the cavities**. The jumpers are electrical-length phasing sections, not plain
patch cables (see `docs/theory/pass-notch-cavities.md`). Restore them to the
correct length or the duplexer will not tune, no matter how good the cavities.

## Safety first

- RF exposure: never key a transmitter into an unterminated or half-built
  duplexer. Terminate every open port with a 50-ohm load during bench work.
- Torque: hand-tighten then snug PL-259/N connectors; do not overtighten and
  crack a cavity fitting.
- Label everything before disconnecting. Photograph the intact sets first.

## Golden rule for intact sets

**Measure and record before you cut anything.** For any set that still has its
original jumpers, log each jumper's exact **tip-to-tip** (connector-tip to
connector-tip) length and routing in that unit's inventory YAML before
disturbing it. An intact reference set is your ground truth for the cut ones.

## T1500 UHF documented lengths (Source 2)

Rebuild cut UHF jumpers to these PL-259 tip-to-tip lengths:

| Freq range | Cable #1 | Cable #2 | Cable #3 | Cable #4 |
|------------|----------|----------|----------|----------|
| 406-430 MHz | 9-3/8" | 9-3/4" | 6-3/4" | 10-1/2" |
| 430-470 MHz | 8-1/2" | 8-3/4" | 5-3/4" | 9-3/4" |

70cm (440-450) and GMRS (462/467) both use the **430-470 MHz** row.

### Connector / cable requirement (T1500)

- **Silver-plated, double-shielded coax and silver-plated connectors only.**
- No nickel or chrome plating - it degrades the notch.

## T1480 VHF lengths (not yet documented)

The authoritative VHF harness lengths are in the Source 1 PDF, which needs OCR.
Until recovered, use one of:

1. Copy from an intact reference T1480 of the same model.
2. Compute the electrical length and verify by tuning (below).

## Computing electrical length when no figure exists

The phasing sections are odd multiples of a quarter wavelength in the cable.

```
lambda_free (in) = 11802.9 / f_MHz          # speed of light in inches/us basis
quarter_wave_electrical (in) = (11802.9 / f_MHz) / 4 * VF
```

- `VF` is the cable **velocity factor** (solid-PE RG-8/213 ~0.66; foam ~0.80-0.84;
  check the exact coax datasheet - this matters).
- Motorola's tip-to-tip figures include the connector bodies, so a computed bare
  cable length must be adjusted for connector length. Treat computed values as a
  **starting point**, then confirm by sweeping the notch position on the NanoVNA.

Worked example, 445 MHz, VF 0.66:
`11802.9 / 445 = 26.52 in` free-space wavelength;
quarter-wave electrical `= 26.52 / 4 * 0.66 = 4.38 in` bare cable.
(Motorola's shortest 430-470 jumper is 5-3/4" tip-to-tip, i.e. this quarter-wave
class length plus connector bodies - the documented figures are still preferred.)

## Rebuild checklist

- [ ] Intact reference lengths recorded in the unit's inventory YAML.
- [ ] Correct plating (silver) coax and connectors on hand for UHF.
- [ ] Jumpers cut/assembled to documented tip-to-tip length (+/- 1/16").
- [ ] Continuity and short checks on each new jumper before installing.
- [ ] Cavities connected per the loop/probe phasing rule (T1500).
- [ ] Every open port terminated in 50 ohms before any RF is applied.
- [ ] Set marked `cable_state: rebuilt` in inventory, ready for tuning.
