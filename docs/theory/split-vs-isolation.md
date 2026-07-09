---
title: Split vs Isolation vs Insertion Loss
scope: The core tradeoff that governs every duplexer tuning decision
last_updated: 2026-07-09
---

# Split vs Isolation vs Insertion Loss

Every duplexer tuning decision trades three quantities against each other:

- **Split** - the TX/RX frequency separation you must support.
- **Isolation** - notch depth (dB) protecting the receiver from the transmitter.
- **Insertion loss** - signal lost passing through the duplexer (dB).

You cannot maximize all three. More cavities and a wider split buy isolation and
low loss; a tight split forces a compromise.

## The rule

| More cavities | Tighter split possible | Insertion loss | Isolation |
|---------------|------------------------|----------------|-----------|
| 4-cavity | moderate (0.5+ MHz VHF, 3-5 MHz UHF) | ~1.0-1.6 dB | 70-95 dB |
| 6-cavity | tight (0.3-0.4 MHz VHF) | ~2.0-2.2 dB | 95-120 dB |

At a fixed cavity count, pushing the notch closer to the passband (tighter split)
**raises insertion loss and/or lowers achievable isolation**. This is physics,
not a tuning skill issue.

## Applied to the three target bands

### 2m amateur - 600 kHz split (the hard case)

- 144-148 MHz, standard repeater split **0.6 MHz**.
- A 4-cavity T1480 is **at the edge** of its comfortable range at 0.6 MHz.
  Expect ~1.5 dB loss and target the most isolation tuning allows.
- If you have a 6-cavity VHF set, use it here - it is the right tool for 0.6 MHz.
- Minimum acceptable isolation depends on TX power and RX front-end, but treat
  **70 dB as a floor** and chase more. Low-power (a few watts) is far more
  forgiving than 50 W.

### 70cm amateur - 5 MHz split (easy)

- 440-450 MHz, standard split **5 MHz**.
- A 4-cavity T1500 UHF set has **ample margin** at 5 MHz. Expect low loss
  (~1.0-1.6 dB) and 80+ dB isolation with straightforward tuning.

### GMRS - 5 MHz split (easy)

- Repeater output 462.xxx, input 467.xxx, split **5 MHz**.
- Same UHF hardware and margin as 70cm. Easiest of the three to commission.

## Practical takeaway

- Put your **best/most-cavity VHF set on 2m**; it needs the help.
- UHF 70cm and GMRS are forgiving - a healthy 4-cavity T1500 will do well.
- When a 2m tune will not reach target isolation without unacceptable loss, the
  honest answer is often "this set has too few cavities for a 0.6 MHz split,"
  not "tune harder."
