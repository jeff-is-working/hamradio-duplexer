---
title: Procedure - Tuning and Verifying with a tinySA Ultra
scope: Using the tinySA Ultra as tracking source / spectrum analyzer for cavities
last_updated: 2026-07-09
last_reviewed: 2026-07-09
---

# Tuning and Verifying with a tinySA Ultra

The tinySA Ultra complements the NanoVNA. It has a built-in signal generator and
a spectrum-analyzer input, so it can drive one side of a cavity and measure the
level that comes through - a scalar equivalent of an S21 sweep. Use it to
cross-check the NanoVNA and to observe real signals.

## Two useful modes

### 1. Scalar tracking sweep (generator + analyzer)

- Use the tinySA Ultra's **signal generator output** as the source into the
  cavity/duplexer input.
- Feed the cavity output into the **SA input**.
- Sweep the generator across the band and watch the received level: the **pass**
  is a peak, the **reject notch** is a deep dip.

This gives you pass frequency, notch frequency, and relative notch depth without
a VNA. It is scalar (magnitude only, no phase), so use it for verification and
for measuring notch depth, and rely on the NanoVNA for the precise interacting
tune.

Success looks like: a level peak at the wanted frequency and a sharp level dip
(notch) at the unwanted frequency.

### 2. Passive spectrum monitoring

- Watch for the transmitter's carrier leaking to the receive port, on-air
  interference, or spurious products. Useful during commissioning to confirm the
  notch actually suppresses the TX carrier at the RX port in the real system.

## Guardrails (read before connecting)

- The tinySA Ultra SA input is **low-level**. Do **NOT** connect it directly to a
  transmitter or any high-power port. Use the built-in generator for tuning, or a
  proper **attenuator / directional coupler** when observing a live transmitter.
  Exceeding the input rating destroys the front end.
- Confirm the generator output level and the SA input limit in the tinySA docs
  before each new hookup.
- Terminate unused ports in 50 ohms.

## Suggested workflow

1. Do the precise tune on the **NanoVNA** (interacting cavities, phase-accurate).
2. **Cross-check** pass/notch frequency and depth on the tinySA Ultra tracking
   sweep - the two instruments should agree within a dB or two.
3. At commissioning, use the tinySA Ultra in **spectrum mode** (through an
   attenuator/coupler) to confirm TX carrier suppression at the RX port under
   real low power.

Record any tinySA-measured numbers alongside the NanoVNA numbers in the unit's
inventory YAML so discrepancies are visible.
