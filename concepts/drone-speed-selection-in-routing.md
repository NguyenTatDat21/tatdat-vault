---
title: >-
  Drone Speed Selection in Truck-Drone Routing
category: concepts
tags: [drones, optimization, energy, routing]
relationships:
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: derived_from
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
sources:
  - _papers/tamke2023vehicle/tamke2023vehicle-extracted.md
  - _papers/tamke2023vehicle/tamke2023vehicle.md
summary: >-
  Treats drone speed as an explicit optimization variable, balancing delivery speed against energy range and synchronization costs in truck-drone routes.
provenance:
  extracted: 0.84
  inferred: 0.14
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:12:13Z
updated: 2026-10-22T09:27:38Z
---

# Drone Speed Selection in Truck-Drone Routing

Drone speed selection models do not assume a fixed cruising speed; they optimize speed per sortie (or per operation) under battery and timing constraints.

## Key Ideas

- Speed directly controls both sortie duration and energy burn, creating a non-trivial range–time trade-off.
- In Tamke & Buscher’s VRPD experiments, the best average fixed speed was **12 m/s**; both lower and higher fixed speeds were often worse.
- Allowing speed selection (VRPD-DSS) outperformed fixed-speed VRPD on average; even the best fixed-speed baseline (12 m/s) was still about **0.59%** (1 drone) and **0.78%** (2 drones) worse on 20-customer tests.
- Dominance-based preprocessing is operationally important: roughly **23.10%** of candidate operations were removed and solve times dropped substantially while preserving optimal costs.

In practice, speed selection matters more as fleet/drone coordination complexity grows, because fixed-speed choices become harder to tune across diverse route patterns. ^[inferred]
Related pages: [[references/tamke2023-vrpd-dss]], [[concepts/k-multi-visit-drone-routing-problem]], [[references/poikonen2020-k-mvdrp]], [[references/montemanni2024-pdsvrp-collective-drones]].

## Open Questions

- How stable are optimal speed profiles when weather-dependent energy models are introduced?
- Which speed-discretization granularity gives most of the value without exploding MILP size? ^[inferred]

## Sources

- [[_papers/tamke2023vehicle/tamke2023vehicle-extracted.md]]
- [[_papers/tamke2023vehicle/tamke2023vehicle.md]]
