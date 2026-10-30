---
title: >-
  Peukert's Law for Drone Battery Discharge (Current-Dependent Usable Capacity)
category: concepts
aliases: [Peukert effect, Peukert exponent, discharge current limit, battery efficiency loss]
tags: [battery, peukert-law, discharge-current, lifepo4, energy-consumption, drone-delivery, feasibility, lifespan, capacity-weight-tradeoff]
relationships:
  - target: "[[references/nguyen2023-pdstsp-collective-drones]]"
    type: derived_from
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
  - target: "[[concepts/multirotor-power-model-components]]"
    type: related_to
  - target: "[[references/liu2017power]]"
    type: related_to
  - target: "[[concepts/collective-drone-delivery]]"
    type: related_to
  - target: "[[concepts/uav-payload-bottleneck]]"
    type: related_to
sources:
  - _papers/nguyen2023parallel/nguyen2023parallel-extracted.md
  - _papers/nguyen2023parallel/nguyen2023parallel.md
summary: >-
  Peukert's law makes usable battery capacity shrink with discharge current: C_d = Σ I_i(I_i/I_nom)^(p-1)Δt_i with p=1.1, gated by I_max per phase and C_d ≥ 0.9·C_nom.
provenance:
  extracted: 0.95
  inferred: 0.05
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: core
created: 2026-10-26T05:12:09Z
updated: 2026-10-30T14:38:55Z
---

# Peukert's Law for Drone Battery Discharge

> [!tldr] A drone battery's **usable** capacity is not its nameplate capacity: drawing current faster empties it faster than the Ah rating predicts. Peukert's law models this as a current-dependent effective discharge, and in scheduling models it turns "can this drone fly this sortie?" into two tests — a **per-phase current ceiling** (lifespan) and a **Peukert-corrected energy budget** with an efficiency-loss factor.

## Formulation

Per flight phase $i$, the discharge current is obtained from the [[concepts/multirotor-power-model-components|power model]], $I_i = P_i / V_{nom}$ ($V_{nom}$ = nominal voltage, 12.8 V in the reference battery family). Peukert's law, as applied in the PDSTSP-c paper citing Doerffel & Sharkh (2006):

$$C_d=\sum_{i=1}^{6} I_{eff,i}\,\Delta t_i=\sum_{i=1}^{6}\left[I_i\left(\frac{I_i}{I_{nom}}\right)^{p-1}\Delta t_i\right],\qquad p>1$$

- $p$ = **Peukert exponent** (set to 1.1 in the experiments; Table 5 lists "Peukert constant 1.1").
- $I_{nom}$ = nominal current of the manufacturer capacity, i.e. the 1C rate.
- The sum runs over the six sortie phases (takeoff, cruise in, landing, parcel delivery, takeoff, cruise out, landing), so vertical and cruise phases contribute with their own currents and durations.

Two gates then decide feasibility:

1. **Current ceiling (constraint 2):** $I_i \le I_{max}$ for every phase $1\le i\le 6$. This protects battery lifespan. It blocks overloaded parcels and excessive speeds; in Algorithm 2 the four vertical takeoff/landing phases are tested **first** (loaded outbound leg, empty return leg) and the configuration is rejected before cruising speeds are even considered if a vertical phase is infeasible.
2. **Energy budget with efficiency loss (constraint 4):** $C_d \ge \beta\,C_{nom}$ with $\beta<1$ (set to 0.9), modelling wind resistance and battery degradation. If either gate fails, the drone configuration cannot transport the parcel.

## Reference LiFePO4 battery family (Power Tech PowerBrick+, 2022)

| Model ID | Capacity (Ah) | Weight (kg) | Max discharge current (A) | Nominal voltage (V) |
|---|---|---|---|---|
| 0 | 7.5 | 1.08 | 15 | 12.8 |
| 1 | 12 | 1.55 | 24 | 12.8 |
| 2 | 20 | 2.80 | 40 | 12.8 |
| 3 | 30 | 3.44 | 45 | 12.8 |

The $I_{max}$ column is what the current ceiling checks, so a heavier battery raises the ceiling along with the capacity. ^[inferred]

## The weight feedback loop

The measured consequence: aggregate c-drone gain by battery model at Node 10 ($m>12$) is 7.5 Ah → **26.68%**, 12 Ah → **29.69%**, 20 Ah → **27.95%**, 30 Ah → **25.05%**. Going 7.5 → 12 Ah helps; from 20 Ah upward the gain falls **and** the variance grows (lower average, lower whisker, taller box, longer tails). Extra battery weight enters $W$ (drone frame + battery) in the power model, raising current draw and therefore the Peukert-corrected demand, which neutralises the longer life. Under a 25 kg combined-weight cap, a 30-Ah drone weighing 4.64 kg leaves a 4-unit c-drone at most **6.44 kg** of payload and a 5-unit c-drone at most **1.8 kg**. The conclusion drawn in the source: **12 Ah is the most consistent choice** from a cost/effectiveness perspective.

## Modeling implications

- Peukert's law makes speed and payload **nonlinearly** coupled to endurance: a faster flight is shorter in time but demands a higher current, and the $(I/I_{nom})^{p-1}$ factor punishes it superlinearly.
- Adding capacity is not free: capacity, weight, current ceiling, and payload cap interact, so battery selection is a design decision, not a specification detail.
- Testing feasibility per phase, and testing the vertical phases first, is a cheap pruning rule: it rejects impossible configurations before enumerating cruise speeds.
- Battery assumptions in the source are strong: fully charged before every launch, negligible battery-swap/loading time, fixed $p=1.1$ and $\beta=0.9$, and one commercial product family as the battery population. Temperature, aging, depth-of-discharge, and recharge scheduling are not modelled.

## Related

- [[references/nguyen2023-pdstsp-collective-drones]] — constraints (2)–(4), Algorithm 2, and the battery-gain numbers
- [[concepts/payload-induced-drone-battery-consumption-rate]] — payload-dependent consumption without the current-dependent term
- [[concepts/multirotor-power-model-components]] — supplies $P_i$ that becomes $I_i$
- [[references/liu2017power]] — the power model whose coefficients feed the current calculation
- [[concepts/collective-drone-delivery]] — eligibility decisions that these gates drive

## Sources

- [[_papers/nguyen2023parallel/nguyen2023parallel-extracted.md]]
- [[_papers/nguyen2023parallel/nguyen2023parallel.md]]
