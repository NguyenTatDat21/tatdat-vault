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
  extracted: 0.77
  inferred: 0.2
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:12:13Z
updated: 2026-10-22T09:12:13Z
---

# Drone Speed Selection in Truck-Drone Routing

Drone speed selection models do not assume a fixed cruising speed; they optimize speed per sortie (or per operation) under battery and timing constraints.

## Key Ideas

- Speed choices change both flight time and energy burn, so faster is not always better.
- In cost-based formulations, speed can shift the balance between truck-driver time savings and drone energy use.
- Dominated-speed filtering can reduce model size before branch-and-cut/branch-and-bound.
- This concept is central in [[references/tamke2023-vrpd-dss]] and complements route-structure models such as [[references/poikonen2020-k-mvdrp]].

In practice, the largest gains often come from shortening total completion time while keeping drone energy within feasible range envelopes. ^[inferred]

Related pages: [[references/tamke2023-vrpd-dss]], [[concepts/k-multi-visit-drone-routing-problem]], [[references/poikonen2020-k-mvdrp]], [[references/montemanni2024-pdsvrp-collective-drones]].

## Open Questions

- How stable are optimal speed profiles when weather-dependent energy models are introduced?
- Which speed-discretization granularity gives most of the value without exploding MILP size? ^[inferred]

## Sources

- [[_papers/tamke2023vehicle/tamke2023vehicle-extracted.md]]
- [[_papers/tamke2023vehicle/tamke2023vehicle.md]]
