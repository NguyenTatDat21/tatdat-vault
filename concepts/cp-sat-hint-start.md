---
title: >-
  CP-SAT Hint-Start for Truck-and-Drone Routing
category: concepts
tags: [constraint-programming, cp-sat, vrp, warm-start]
relationships:
  - target: "[[concepts/pdsvrp-c]]"
    type: uses
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: derived_from
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: derived_from
  - target: "[[references/montemanni2024-parallel-collective-drones]]"
    type: derived_from
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: derived_from
  - target: "[[concepts/cumulative-volume-lower-bound-cp-search]]"
    type: related_to
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: related_to
sources: [_papers/montemanni2024combining/montemanni2024combining-extracted.md]
summary: >-
  A warm-start pattern where a truck-only VRP solution is injected as CP-SAT hints, improving bound quality and final solutions in collaborative drone routing models.
provenance:
  extracted: 0.68
  inferred: 0.28
  ambiguous: 0.04
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T08:07:13Z
updated: 2026-10-30T14:38:55Z
---

# CP-SAT Hint-Start for Truck-and-Drone Routing

Hint-start uses CP-SAT's ability to accept partial variable assignments before search. In this paper's setting, the hinted assignment comes from a truck-only min-max VRP solve.

## Key Ideas

- Build a feasible, structured baseline by solving truck-only VRP first.
- Feed that baseline into CP-SAT as hints instead of starting from scratch.
- Let CP-SAT optimize around the hint by moving selected customers to drones while preserving useful truck-tour structure.
- This pattern can improve both lower bounds and upper bounds under fixed time limits.
- The gains are notable even though the hint ignores drones entirely, suggesting search guidance is more important than full feature coverage in early search. ^[inferred]

In the PDSVRP-c experiments, this strategy improved heuristic outcomes and tightened bounds in both M2 and M3 compared with non-hinted runs.

Related pages: [[concepts/pdsvrp-c]] and [[references/montemanni2024-pdsvrp-collective-drones]].

## Open Questions

- Which variable subsets are most valuable to hint (routing arcs, timing, or assignment) for CP-SAT in mixed truck/drone models?
- Does hint quality correlate linearly with final gap closure, or are there threshold effects? ^[inferred]


## Related

- [[references/montemanni2023-cp-pdsvrp]] — shares constraint-programming + cp-sat tags with this page
- [[references/montemanni2024-parallel-collective-drones]] — shares constraint-programming + cp-sat tags with this page
- [[references/ha2020-vrp-synchronization-lp-alns]] — shares constraint-programming + vrp tags with this page
## Sources

- [[_papers/montemanni2024combining/montemanni2024combining-extracted.md]]
