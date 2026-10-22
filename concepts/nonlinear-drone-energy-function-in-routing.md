---
title: Nonlinear Drone Energy Function in Routing
category: concepts
tags: [drone-routing, energy-modeling, optimization, nonlinear]
relationships:
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: derived_from
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
sources:
  - _papers/cheng2020drone/cheng2020drone-extracted.md
  - _papers/cheng2020drone/cheng2020drone.md
summary: Models drone power as a convex payload-dependent function and integrates it into routing optimization to prevent energy-infeasible route plans.
provenance:
  extracted: 0.87
  inferred: 0.1
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:29:44Z
updated: 2026-10-22T11:29:44Z
---

# Nonlinear Drone Energy Function in Routing

Drone-routing models often need energy feasibility, not just distance minimization. A nonlinear payload-aware energy function captures this better than simple linear approximations.

## Core Model Idea

A representative form is:

`P(q) = k (W + m + q)^(3/2)`

where payload `q` increases power use nonlinearly.

In routing formulations, this changes feasibility and route choice because different customer orders imply different payload profiles per arc.

## Why It Matters

- Linear approximations can underestimate consumption on heavier payload segments.
- That can produce route plans that appear feasible in the linear model but violate battery limits under nonlinear recalculation.
- In Cheng et al., this mismatch appears repeatedly (around 9% average energy gap; multiple infeasible linear-derived routes).

## Algorithmic Pattern

For exact optimization, combine:

1. base route MILP variables,
2. convex-energy under-estimation cuts (subgradient/tangent cuts),
3. explicit infeasibility cuts when a candidate trip violates battery capacity.

This pattern keeps tractability while preserving energy realism.

## Open Questions

- How much additional realism is gained by adding takeoff/landing and wind-state terms beyond payload-only convex models?
- What approximation error is acceptable for planning when recharging infrastructure is dense? ^[inferred]

## Related

- [[references/cheng2020-drone-routing-energy-function]]
- [[concepts/payload-induced-drone-battery-consumption-rate]]
- [[concepts/exact-multitrip-vrptw-framework]]
- [[references/tamke2023-vrpd-dss]]

## Sources

- [[_papers/cheng2020drone/cheng2020drone-extracted.md]]
- [[_papers/cheng2020drone/cheng2020drone.md]]
