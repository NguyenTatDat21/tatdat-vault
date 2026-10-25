---
title: Vehicle Routing with Synchronization Constraints (VRPMS)
category: concepts
tags: [vrp, synchronization, constraint-programming, alns]
relationships:
  - target: "[[references/hojabri2018-vrp-synchronization-alns-cp]]"
    type: derived_from
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: derived_from
sources:
  - _papers/hojabri2018large/hojabri2018large-extracted.md
  - _papers/hojabri2018large/hojabri2018large.md
summary: VRPMS couples route design with temporal synchronization windows between service layers, requiring specialized repair and feasibility handling.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T10:00:17Z
updated: 2026-10-24T18:36:02Z
---

# Vehicle Routing with Synchronization Constraints (VRPMS)

VRPMS extends VRPTW by requiring time-consistent coordination between at least two service layers (e.g., regular and special vehicles).

## Key Ideas

- Synchronization constraints bind service start times across routes, not just within a route.
- A common form enforces:

\[
t - \delta \le t'_i \le t + \gamma
\]

where \(t\) is the delivery time at the regular vertex of a special customer and \(t'_i\) is the start time of its special service; \(\delta\) and \(\gamma\) are model parameters. The paper writes a single pair $\delta$, $\gamma$ for all customers.

- Even a small number of synchronization constraints can alter route structure and search difficulty.
- Hybrid solve patterns (metaheuristic destroy/repair + CP feasibility reconstruction) are effective for these tightly coupled constraints.

VRPMS is a representative case where feasibility structure, not only objective value, drives algorithm design. ^[inferred]

Related pages: [[references/hojabri2018-vrp-synchronization-alns-cp]], [[concepts/exact-multitrip-vrptw-framework]], [[concepts/large-neighborhood-search]], [[concepts/variable-neighborhood-search]], [[references/paradiso2020-esf-multitrip-vrptw]].

## Open Questions

- Which synchronization-rich domains benefit most from exact CP-based reinsertion versus faster heuristic repairs?
- How should robustness to stochastic delays be layered onto deterministic synchronization windows? ^[inferred]


## Related

- [[references/montemanni2024-pdsvrp-collective-drones]] — shares constraint-programming + vrp tags with this page
## Sources

- [[_papers/hojabri2018large/hojabri2018large-extracted.md]]
- [[_papers/hojabri2018large/hojabri2018large.md]]
