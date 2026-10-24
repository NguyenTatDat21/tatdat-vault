---
title: Drone Routing with Nonlinear Energy Function (Cheng et al.)
category: references
tags: [paper, drone-routing, branch-and-cut, energy-modeling]
relationships:
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: uses
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: uses
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
  - target: "[[references/ahmadi-javid2022-drone-delivery-energy-formulation]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
sources:
  - _papers/cheng2020drone/cheng2020drone-extracted.md
  - _papers/cheng2020drone/cheng2020drone.md
  - _papers/cheng2020drone/images/page_0_image_9.jpg
  - _papers/cheng2020drone/images/page_5_chart_2.jpg
  - _papers/cheng2020drone/images/page_7_chart_2.jpg
summary: Formulates multi-trip drone routing with nonlinear payload-dependent energy and solves it via branch-and-cut with logical and subgradient cuts.
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:29:44Z
updated: 2026-10-23T00:04:12Z
---

# Drone Routing with Nonlinear Energy Function (Cheng et al.)

> [!tldr] This paper introduces a multi-trip drone routing model with time windows and nonlinear payload-dependent energy, then solves it using a cut-enhanced branch-and-cut approach.

## Problem & Contribution

The paper studies a **multi-trip drone routing problem (MTDRP)** where each customer must be visited once and routes must satisfy payload, battery, and time-window constraints.

Key contribution: replacing linearized energy assumptions with an explicit nonlinear model and showing that linear approximations can produce energy-infeasible routes.

## Method

- 2-index mixed-integer formulation for route/trip linkage.
- Nonlinear energy function based on payload-dependent power:
  - `P(q) = k (W + m + q)^(3/2)`
- Two custom cut families for nonlinear handling:
  1. **Logical infeasibility cuts** (remove energy-violating customer sequences).
  2. **Subgradient cuts** (tangent under-estimators for convex energy term).
- Additional valid inequalities and SEC separation integrated in branch-and-cut.

## Results

Reported findings include:

- Using logical + subgradient cuts + valid inequalities + SECs gives the strongest overall performance among tested cut configurations.
- Linear energy approximation is computationally faster but materially risky:
  - infeasible routes under nonlinear recalculation appear in `20/50` instances for model `R` and `18/50` for model `R+E`.
  - average energy gap between linear and nonlinear evaluation is around `9%`.
- On extended Solomon set B:
  - all 25-customer instances solved to optimality,
  - for 40-customer instances, solved counts are 19/27 (`R_e`), 14/27 (`E_e`), and 18/27 (`R+E_e`) within the time limit.

## Limitations

The paper notes that the energy model omits some effects (e.g., takeoff/landing detail, wind/speed factors) and uses small-drone parameterization, which may underrepresent newer production delivery platforms.

## Bibliographic Record

- Citation key: `cheng2020drone`
- DOI: `10.1016/j.trb.2020.06.011`
- Canonical URL: https://www.sciencedirect.com/science/article/pii/S019126152030360X
- Publication: *Transportation Research Part B: Methodological* (2020)
- Authors: Chun Cheng, Yossiri Adulyasak, Louis-Martin Rousseau
- Companion metadata note: [[_papers/cheng2020drone/cheng2020drone.md]]

## Related

- [[concepts/nonlinear-drone-energy-function-in-routing]]
- [[concepts/payload-induced-drone-battery-consumption-rate]]
- [[concepts/exact-multitrip-vrptw-framework]]
- [[references/poikonen2020-k-mvdrp]]
- [[references/ahmadi-javid2022-drone-delivery-energy-formulation]]
- [[references/dorling2017-drone-delivery-vrp]]
- [[_papers/cheng2020drone/cheng2020drone-extracted]]

## Sources

- [[_papers/cheng2020drone/cheng2020drone-extracted.md]]
- [[_papers/cheng2020drone/cheng2020drone.md]]
- [[_papers/cheng2020drone/images/page_0_image_9.jpg]]
- [[_papers/cheng2020drone/images/page_5_chart_2.jpg]]
- [[_papers/cheng2020drone/images/page_7_chart_2.jpg]]
