---
title: Vehicle Routing Problems for Drone Delivery (Dorling et al., 2017)
category: references
tags: [paper, drones, vehicle-routing, energy-modeling]
relationships:
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: uses
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: related_to
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
sources:
  - _papers/dorling2017vehicle/dorling2017vehicle-extracted.md
  - _papers/dorling2017vehicle/dorling2017vehicle.md
summary: >-
  Defines multi-trip drone-delivery VRPs with battery/payload-aware energy,
  derives a practical linear power model, and combines MILP and simulated
  annealing for cost/time objectives.
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T23:45:17Z
updated: 2026-10-22T23:45:17Z
---

# Vehicle Routing Problems for Drone Delivery (Dorling et al., 2017)

> [!tldr] This paper formulates drone-only multi-trip delivery VRPs that explicitly model payload/battery effects on energy, then solves minimum-cost and minimum-time variants with MILP and simulated annealing.

## Problem & Contribution

The paper argues classical VRPs miss key drone-delivery realities:
- multiple depot returns and vehicle reuse,
- payload- and battery-dependent energy draw,
- tight coupling between route choice, battery size, and feasibility.

It introduces two variants:
- **MC-DDP** (minimum cost),
- **MT-DDP** (minimum overall delivery time).

## Energy Model

A practical linear approximation for multirotor power is used:

$$
p(m)=\alpha m + \beta
$$

where `m` is battery+payload mass, `\alpha` is marginal power-per-kg, and `\beta` is baseline hover power.

The paper reports fitted values (hexacopter setting) around:
- `\alpha \approx 46.7 W/kg`
- `\beta \approx 26.9 W`

and low approximation error in the tested mass range.

## Optimization Pattern

- MILP captures routing, reuse, timing, energy, capacity, and budget constraints.
- Simulated annealing is proposed for larger instances where MILP runtime is high.
- Cost functions penalize infeasible solutions and account for route-level battery/energy coupling.

## Results

- Experiments validate that battery and payload weight materially affect feasible route plans.
- Allowing drone reuse can reduce total fleet cost substantially versus one-trip assumptions.
- Sensitivity analyses show battery assumptions materially shift optimal route structure.

## Limitations

- Assumptions simplify weather, takeoff/landing dynamics, and charging logistics.
- Source extraction required NUL-byte cleanup for reading; exact table values should be rechecked against PDF for audit-critical use. ^[ambiguous]

## Related

- [[concepts/payload-induced-drone-battery-consumption-rate]]
- [[concepts/nonlinear-drone-energy-function-in-routing]]
- [[references/cheng2020-drone-routing-energy-function]]
- [[concepts/exact-multitrip-vrptw-framework]]
- [[references/tamke2023-vrpd-dss]]

## Bibliographic Record

- Citation key: `dorling2017vehicle`
- DOI: `10.1109/TSMC.2016.2582745`
- Canonical URL: <https://doi.org/10.1109/TSMC.2016.2582745>
- Publication: *IEEE Transactions on Systems, Man, and Cybernetics: Systems* (2017)
- Authors: Kevin Dorling; Jeremy Heinrichs; Geoff G. Messier; Sébastien Magierowski
- Companion metadata note: [[_papers/dorling2017vehicle/dorling2017vehicle.md]]

## Sources

- [[_papers/dorling2017vehicle/dorling2017vehicle-extracted.md]]
- [[_papers/dorling2017vehicle/dorling2017vehicle.md]]
