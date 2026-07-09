---
title: Procedure - Tuning with a NanoVNA
scope: Step-by-step pass-notch cavity tuning using NanoVNA S21/S11
last_updated: 2026-07-09
---

# Tuning with a NanoVNA

The NanoVNA is the primary tuning instrument. You tune each cavity for a **pass**
at its own frequency and a **deep reject notch** at the opposite leg's frequency,
then verify overall TX-to-antenna and antenna-to-RX isolation.

## Gear and setup

- NanoVNA (two ports: CH0/S11 source, CH1/S21 through).
- Two short known-good test jumpers, plus 50-ohm loads for unused ports.
- Calibration kit (open/short/load, and a through for S21).

Success looks like: a clean S21 pass curve at the wanted frequency and a sharp,
deep S21 null (notch) at the unwanted frequency, at the target depth from
`docs/theory/split-vs-isolation.md`.

## Step 0 - Calibrate

1. Set the sweep to span both legs with margin (e.g. 2m: 144-148 MHz; UHF:
   440-470 MHz).
2. **SOLT calibrate at the ends of your test jumpers**, not at the NanoVNA
   connectors - you want the cables in the calibration reference plane.
3. Save the calibration slot.

## Step 1 - Characterize each cavity (S21 through)

For one cavity at a time, port-to-port through the cavity:

1. Connect CH0 -> cavity in, cavity out -> CH1, unused coupling port terminated.
2. Read the **pass** (minimum insertion loss) frequency and the **notch**
   (maximum rejection) frequency and depth.
3. Adjust the **tuning rod** to move the pass frequency onto that cavity's leg.
4. The notch offset is set by the coupling and the phasing jumper; if the notch
   is at the wrong offset, the jumper length is wrong (see cabling procedure),
   not the rod.

Record pass freq, notch freq, and notch depth per cavity.

## Step 2 - Tune the TX side (protect RX)

The TX-side cavities must **notch deeply at the RX frequency** while passing TX.

1. Sweep S21 from the TX input through the TX cavities to the antenna junction.
2. Peak the pass at the **TX frequency** (lowest insertion loss).
3. Confirm a deep null at the **RX frequency**. Iterate the rods - moving one
   cavity slightly detunes the interaction, so tune in small steps and re-check.

## Step 3 - Tune the RX side (protect against TX)

The RX-side cavities must **notch deeply at the TX frequency** while passing RX.

1. Sweep S21 from the antenna junction through the RX cavities to the RX port.
2. Peak the pass at the **RX frequency**.
3. Confirm a deep null at the **TX frequency**.

## Step 4 - Measure end-to-end isolation

1. S21 from **TX port to RX port** with the antenna port terminated in 50 ohms.
2. Read isolation at the **TX frequency** and at the **RX frequency** - both
   must meet target (2m: aim 70+ dB; UHF: 80+ dB is readily achievable).
3. Read insertion loss on each pass path; confirm it is within spec for the
   cavity count (see cross-reference).

## Step 5 - Iterate

Tuning interacts. Repeat Steps 2-4 in small increments until:

- Pass loss is minimized on both paths, AND
- Notch depth at the opposite frequency meets target on both paths.

When you cannot reach the isolation target without unacceptable insertion loss,
the set likely has too few cavities for that split - see
`docs/theory/split-vs-isolation.md`. Log final numbers in the unit's inventory
YAML, then proceed to `docs/procedures/commissioning.md`.

## Notes

- Lock each tuning rod's locknut after final tune and re-sweep - locking can
  shift the tune slightly.
- The NanoVNA source level is tiny, so this is done at **no RF power** - safe and
  accurate. Verify at low power only during commissioning.
