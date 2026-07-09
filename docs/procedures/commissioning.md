---
title: Procedure - Commissioning a Duplexer
scope: Final acceptance measurements and on-air checklist before service
last_updated: 2026-07-09
---

# Commissioning

A set is **commissioned** only after it passes measured acceptance criteria at
its real operating frequencies. The inventory validator refuses
`status: commissioned` unless measured `insertion_loss_db` and `isolation_db` are
recorded - so this checklist and the log stay in sync.

## Acceptance criteria

Measure at the **actual** RX/TX frequencies for the band (not band center):

| Band | Split | Target isolation | Target insertion loss |
|------|-------|------------------|-----------------------|
| 2m | 0.6 MHz | 70 dB floor, chase higher | ~1.5 dB (4-cav) |
| 70cm | 5 MHz | 80+ dB | 1.0-1.6 dB |
| GMRS | 5 MHz | 80+ dB | 1.0-1.6 dB |

Isolation is read as S21 TX-port-to-RX-port at both the TX and RX frequencies,
antenna port terminated (see `docs/procedures/tuning-nanovna.md`, Step 4).

## Bench acceptance checklist

- [ ] Harness rebuilt/verified to correct lengths; `cable_state` logged.
- [ ] Pass loss minimized on both TX and RX paths, within spec for cavity count.
- [ ] Isolation at TX freq meets target.
- [ ] Isolation at RX freq meets target.
- [ ] Tuning locknuts locked; re-swept after locking (no significant shift).
- [ ] Numbers cross-checked NanoVNA vs tinySA within a couple dB.
- [ ] Final `insertion_loss_db` and `isolation_db` recorded in inventory YAML.

## Low-power RF verification

- [ ] Terminate antenna port; drive TX at **low power** through the duplexer.
- [ ] With tinySA Ultra (via attenuator/coupler), confirm TX carrier is
      suppressed at the RX port by the expected notch depth.
- [ ] No overheating, no arcing, connectors cool.

## On-air commissioning

- [ ] Confirm licensing/coordination for the band (2m/70cm repeater
      coordination as applicable; GMRS per FCC Part 95 - GMRS repeaters allowed
      on the 8 designated 462.xxx output / 467.xxx input pairs only).
- [ ] Correct CTCSS/PL configured on the repeater (logged in the project folder).
- [ ] Full-duplex on-air test: transmit while receiving a weak signal; confirm no
      receiver desense.
- [ ] Range/coverage sanity check.
- [ ] Set `status: commissioned` in inventory and write the project build-log
      entry with final numbers and date.

## If it will not pass

Do not fudge the log. If isolation cannot reach target without excessive loss,
record the best achieved numbers, keep `status: tuning`, and note the likely
cause (too few cavities for the split, harness length, or a bad cavity). See
`docs/theory/split-vs-isolation.md`.
