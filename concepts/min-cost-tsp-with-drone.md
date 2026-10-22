---
title: >-
  Min-cost TSP with Drone (min-cost TSP-D)
category: concepts
tags: [tsp, drones, objective-design, operations-research]
relationships:
  - target: "[[references/ha2018-min-cost-tsp-d]]"
    type: derived_from
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: related_to
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
sources:
  - _papers/ha2018mincost/ha2018mincost-extracted.md
  - _papers/ha2018mincost/ha2018mincost.md
summary: >-
  A TSP-D variant that optimizes transportation and synchronization waiting costs, exposing trade-offs between route cost quality, delivery time, and drone usage frequency.
provenance:
  extracted: 0.84
  inferred: 0.13
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:52:03Z
updated: 2026-10-22T09:52:03Z
---

# Min-cost TSP with Drone (min-cost TSP-D)

Min-cost TSP-D is a truck-drone routing formulation where objective value emphasizes **operational economics** instead of only completion time.

## Key Ideas

- Objective combines transport cost with synchronization waiting penalties.
- Cost-aware solutions can deliberately accept longer completion times if monetary savings are large.
- Split-based construction plus local search can produce higher-quality min-cost solutions than direct tour-conversion heuristics.
- Drone utilization under min-cost objectives is often higher than under min-time objectives in the same benchmark families.

A practical implication is that objective choice can dominate algorithm choice: two methods with similar route structure may be ranked differently once waiting penalties are priced. ^[inferred]

Related pages: [[references/ha2018-min-cost-tsp-d]], [[concepts/drone-speed-selection-in-routing]], [[concepts/k-multi-visit-drone-routing-problem]], [[references/tamke2023-vrpd-dss]].

## Open Questions

- How should waiting penalties be calibrated to represent real labor/asset costs across regions and operators?
- Does min-cost objective behavior remain stable when extending from single-truck TSP-D to multi-truck/multi-station settings? ^[inferred]

## Sources

- [[_papers/ha2018mincost/ha2018mincost-extracted.md]]
- [[_papers/ha2018mincost/ha2018mincost.md]]
