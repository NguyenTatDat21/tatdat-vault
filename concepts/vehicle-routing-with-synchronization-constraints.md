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
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: related_to
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: derived_from
  - target: "[[concepts/drone-swarm-synchronization]]"
    type: related_to
  - target: "[[concepts/ellipse-based-flight-segment-geometry]]"
    type: related_to
  - target: "[[concepts/green-vehicle-routing-problem-taxonomy]]"
    type: related_to
  - target: "[[concepts/hybrid-truck-drone-delivery]]"
    type: related_to
  - target: "[[references/asghari2021-green-vrp-state-of-the-art-review]]"
    type: related_to
  - target: "[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]"
    type: related_to
  - target: "[[references/li2024drone]]"
    type: related_to
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[references/murray2020-multiple-flying-sidekicks-tsp]]"
    type: related_to
  - target: "[[references/nguyen2023-pdstsp-collective-drones]]"
    type: related_to
  - target: "[[references/phanduc2025-pareto-front-grid-fairness-dpdptw]]"
    type: related_to
  - target: "[[references/raj2020multiple-variable-drone-speed-mfstsp]]"
    type: related_to
  - target: "[[references/wang2019routing]]"
    type: related_to
sources:
  - _papers/hojabri2018large/hojabri2018large-extracted.md
  - _papers/hojabri2018large/hojabri2018large.md
  - _papers/ha2020new/ha2020new-extracted.md
  - _papers/ha2020new/ha2020new.md
summary: VRPMS couples route design with temporal synchronization windows between service layers, requiring specialized repair and feasibility handling.
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-29
tier: core
created: 2026-10-22T10:00:17Z
updated: 2026-10-30T19:12:06Z
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

- Hà et al. (2020) showed LP-based insertion feasibility (maximize arc delay under time windows and sync, plus O(1) checks from stored earliest/latest arrivals) beats CP-based repair: 128 of 135 comparisons at 25 customers, 620 of 681 new best-known solutions, 4 new VRPTWSyn bests, 20× speedup from the O(1) checks; see [[references/ha2020-vrp-synchronization-lp-alns]]. ^[inferred]

Related pages: [[references/hojabri2018-vrp-synchronization-alns-cp]], [[concepts/exact-multitrip-vrptw-framework]], [[concepts/large-neighborhood-search]], [[concepts/variable-neighborhood-search]], [[references/paradiso2020-esf-multitrip-vrptw]].

## Open Questions

- Which synchronization-rich domains benefit most from exact CP-based reinsertion versus faster heuristic repairs?
- How should robustness to stochastic delays be layered onto deterministic synchronization windows? ^[inferred]


## Related

- [[references/montemanni2024-pdsvrp-collective-drones]] — shares constraint-programming + vrp tags with this page
- [[references/ha2020-vrp-synchronization-lp-alns]] — first MIP/CP models for VRPSC and the lp-ALNS heuristic
- [[references/sacramento2019-vrp-d-truck-drone-alns-cost]] — shares alns + vrp tags with this page
- [[references/wang2019routing]] — Wang et al. 2019: truck/UAV launch-recover rendezvous arcs as synchronization constraints. ^[extracted]
## Sources

- [[_papers/hojabri2018large/hojabri2018large-extracted.md]]
- [[_papers/hojabri2018large/hojabri2018large.md]]
- [[_papers/ha2020new/ha2020new-extracted.md]]
- [[_papers/ha2020new/ha2020new.md]]
