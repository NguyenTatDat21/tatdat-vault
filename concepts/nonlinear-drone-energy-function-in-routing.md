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
sources:
  - _papers/cheng2020drone/cheng2020drone-extracted.md
  - _papers/cheng2020drone/cheng2020drone.md
  - _papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery-extracted.md
  - _papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery.md
summary: >-
  Models payload-aware convex drone energy and extends routing formulations to arbitrary energy functions while preserving tractable optimization structure.
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:29:44Z
updated: 2026-10-22T23:50:19Z
---

# Nonlinear Drone Energy Function in Routing

Drone-routing models often need energy feasibility, not just distance minimization. A nonlinear payload-aware energy function captures this better than simple linear approximations.

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

## Algorithmic Pattern

For exact optimization, combine:

1. base route MILP variables,
2. nonlinear/convex energy representation (or valid under-estimators),
3. explicit feasibility controls for battery-capacity violations,
4. formulation choices that preserve a strong relaxation.

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

## Sources

- [[_papers/cheng2020drone/cheng2020drone-extracted.md]]
- [[_papers/cheng2020drone/cheng2020drone.md]]
- [[_papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery-extracted.md]]
- [[_papers/ahmadi-javid2022delivery/ahmadi-javid2022delivery.md]]
