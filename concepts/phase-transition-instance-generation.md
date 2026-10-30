---
title: "Phase Transition in Instance Generation"
summary: "Phase transition in instance generation: clustered IRP instances cross the threshold where B&C finds few feasible solutions, with TSP cluster-ratio evidence."
type: concept
tags: [paper, branch-and-cut, lower-bounds, vehicle-routing]
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.00
base_confidence: 0.67
created: 2026-10-28T15:52:00Z
updated: 2026-10-30T17:41:00Z
tier: core
category: concepts
lifecycle: draft
lifecycle_changed: "2026-10-28"
sources:
  - "[[_papers/skalnes2024new/skalnes2024new-extracted.md]]"
  - "[[_papers/skalnes2024new/skalnes2024new.md]]"
relationships:
  - target: "[[concepts/benchmark-instance-design]]"
    type: related_to
  - target: "[[concepts/branch-and-cut]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: derived_from
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: derived_from
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: derived_from
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: derived_from
  - target: "[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]"
    type: derived_from
  - target: "[[references/paradiso2020-esf-multitrip-vrptw]]"
    type: derived_from

---
> [!tldr] Clustered instances cross a phase transition: the B&C finds few feasible solutions on clustered instances, finds the most in random-clustered ones, and clustered gaps are smaller than random gaps, consistent with the TSP cluster-ratio literature.

Phase transition is defined by Gent & Walsh 1996 as a threshold where hard problems become easy on the tractable side, and the paper reads the B&C behavior on clustered instances as crossing it: B&C struggles to find feasible solutions on clustered instances, and finds the most in random-clustered instances. TSP evidence includes Zhang 2004 on distinct distance values, van Hemert & Urquhart 2004 on cluster-based TSP difficulty, and Smith-Miles et al. 2010 on cluster-to-node ratios.

Clustered instances have smaller average gaps than random and mixed for both matheuristic and B&C, explained by cost drivers being the arcs between clusters: once inter-cluster arcs are fixed, the lower bound is strong, and the sequence inside a cluster barely affects cost. Feasible-solution counts support this: B&C finds 18 of 50 instances at 50 customers, split 5 random, 3 clustered, 10 random-clustered, 7 of 100 customers split 3 random, 4 random-clustered, zero at 200; the matheuristic finds 108 feasible solutions, all 10- and 25-customer instances, zero at 50, 100, 200. ^[inferred]

The constructive feasibility heuristic, running before the methods, found feasible solutions on all 270 instances, so instance hardness is not a feasibility issue; the phase transition is read as the exact method losing traction on clustered instances, not as feasibility failure. Instance generation with clustered positioning, exponential decay λ = 50, mixed random-clustered 50/50 placement, and fleet scaling by customers rather than capacity produces the crossing behavior.

## Related

- [[concepts/benchmark-instance-design]] - the feature-space generation that produces clustered, random and mixed instances.
- [[concepts/branch-and-cut]] - the exact method whose feasibility behavior marks the transition.
- [[concepts/large-neighborhood-search]] - the heuristic whose gaps stay small on clustered instances.
- [[references/poikonen2020-k-mvdrp]] — shares paper + vehicle-routing tags with this page
- [[references/tamke2023-vrpd-dss]] — shares paper + vehicle-routing tags with this page
- [[references/cheng2020-drone-routing-energy-function]] — shares branch-and-cut + paper tags with this page
- [[references/montemanni2023-cp-pdsvrp]] — shares lower-bounds + vehicle-routing tags with this page
- [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]] — shares paper + vehicle-routing tags with this page
- [[references/paradiso2020-esf-multitrip-vrptw]] — shares paper + vehicle-routing tags with this page

## Sources

- `[[_papers/skalnes2024new/skalnes2024new-extracted.md]]`
- `[[_papers/skalnes2024new/skalnes2024new.md]]`
