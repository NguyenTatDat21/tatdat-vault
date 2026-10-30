---
title: Nonlinear Drone Energy Function in Routing
category: concepts
tags: [drone-routing, energy-modeling, optimization, nonlinear]
relationships:
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: derived_from
  - target: "[[references/ahmadi-javid2022-drone-delivery-energy-formulation]]"
    type: extends
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
  - target: "[[references/fuertes2023-transformer-multi-uav-routing]]"
    type: related_to
  - target: "[[references/raj2020multiple-variable-drone-speed-mfstsp]]"
    type: uses
  - target: "[[references/murray2015flying]]"
    type: derived_from
  - target: "[[references/mbiadousaleu2022parallel]]"
    type: derived_from
  - target: "[[concepts/drone-delivery-energy-and-range-parameters]]"
    type: related_to
    note: "Reciprocal - concepts/drone-delivery-energy-and-range-parameters references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/multirotor-power-model-components]]"
    type: related_to
    note: "Reciprocal - concepts/multirotor-power-model-components references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/li2024drone]]"
    type: related_to
    note: "Reciprocal - references/li2024drone references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/liu2017power]]"
    type: related_to
    note: "Reciprocal - references/liu2017power references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/wang2019routing]]"
    type: related_to
    note: "Reciprocal - references/wang2019routing references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/cheng2020drone/cheng2020drone-extracted.md
  - _papers/cheng2020drone/cheng2020drone.md
  - _papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery-extracted.md
  - _papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery.md
  - _papers/fuertes2023solving/fuertes2023solving-extracted.md
  - _papers/fuertes2023solving/fuertes2023solving.md
  - _papers/fuertes2023solving/images/page_4_image_3.jpg
summary: >-
  Models payload-aware convex drone energy and extends routing formulations to arbitrary energy functions while preserving tractable optimization structure.
provenance:

  extracted: 0.82
  inferred: 0.14
  ambiguous: 0.04
base_confidence: 0.87
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-22T11:29:44Z
updated: 2026-10-30T14:38:55Z
---

# Nonlinear Drone Energy Function in Routing

Drone-routing models often need energy feasibility, not just distance minimization. A nonlinear payload-aware energy function captures this better than simple linear approximations.

Raj & Murray's mFSTSP-VDS ([[references/raj2020multiple-variable-drone-speed-mfstsp]]) applies this idea with Liu et al.'s phase-specific power functions, making UAV endurance depend on cruise speed and payload.

## Core Model Idea

A representative convex form is:

`P(q) = k (W + m + q)^(3/2)`

where payload `q` increases power use nonlinearly.

Ahmadi-Javid and Meskar broaden this idea by allowing a general arc-level energy model `ed_a = F_a(w_a, t_a)` inside an exact routing formulation, rather than fixing one specific curve family.

## Why It Matters

- Linear approximations can underestimate consumption on heavier payload segments.
- That can produce route plans that appear feasible in a linear model but violate battery limits under nonlinear recalculation.
- General-energy formulations keep feasibility logic realistic while remaining optimization-friendly through stronger modeling structure.
- On benchmark sets, the generalized formulation reports major exact-solve speedups over prior branch-and-cut baselines.
- In Fuertes et al.'s multi-UAV mission planning, energy and range constraints are the motivation for cooperation, not a modeled mechanism: $t_{max}$ is set so each UAV can reach about half the nodes, cooperation is introduced because shared regions stay reachable when agents are lost to battery depletion, and the model itself uses Euclidean distances, zero service time, and one shared fleet speed — so a payload- and battery-aware energy function never enters the objective. ^[inferred] [[references/fuertes2023-transformer-multi-uav-routing]]

## Algorithmic Pattern

For exact optimization, combine:

1. base route MILP variables,
2. nonlinear/convex energy representation (or valid under-estimators),
3. explicit feasibility controls for battery-capacity violations,
4. formulation choices that preserve a strong relaxation.

In a learned solver the decoder state is the current node plus remaining time, so nonlinear fuel-consumption functions must enter that state for the policy to respect energy feasibility. ^[inferred] [[concepts/transformer-seq2seq-routing-solver]]
## Open Questions

- How much additional realism is gained by adding takeoff/landing and wind-state terms beyond payload-only convex models?
- What approximation error is acceptable for planning when recharging infrastructure is dense? ^[inferred]

## Related

- [[references/cheng2020-drone-routing-energy-function]]
- [[references/ahmadi-javid2022-drone-delivery-energy-formulation]]
- [[references/dorling2017-drone-delivery-vrp]]
- [[concepts/payload-induced-drone-battery-consumption-rate]]
- [[concepts/exact-multitrip-vrptw-framework]]
- [[references/tamke2023-vrpd-dss]]
- [[references/fuertes2023-transformer-multi-uav-routing]]
- [[concepts/cooperative-multi-agent-uav-routing]]
- [[concepts/transformer-seq2seq-routing-solver]]
- [[references/murray2015flying]] — shares drone-routing + optimization tags with this page
- [[references/mbiadousaleu2022parallel]] — shares drone-routing + optimization tags with this page

## Sources

- [[_papers/cheng2020drone/cheng2020drone-extracted.md]]
- [[_papers/cheng2020drone/cheng2020drone.md]]
- [[_papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery-extracted.md]]
- [[_papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery.md]]
- [[_papers/fuertes2023solving/fuertes2023solving-extracted.md]]
- [[_papers/fuertes2023solving/fuertes2023solving.md]]
- [[_papers/fuertes2023solving/images/page_4_image_3.jpg]]
