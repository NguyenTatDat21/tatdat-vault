---
title: Min-cost Parallel Drone Scheduling VRP (PDSVRP)
category: concepts
tags: [vrp, drones, cost-optimization, scheduling]
relationships:
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: derived_from
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: extends
  - target: "[[concepts/pdsvrp-c]]"
    type: related_to
  - target: "[[concepts/bilevel-vrpd-task-assignment-routing]]"
    type: related_to
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: related_to
  - target: "[[references/torabbeigi2020-payload-bcr-drone-scheduling]]"
    type: derived_from
  - target: "[[concepts/dag-topological-sort-scheduling-move-evaluation]]"
    type: related_to
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: derived_from
  - target: "[[concepts/multiple-flying-sidekicks-traveling-salesman-problem]]"
    type: related_to
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: related_to
  - target: "[[concepts/transformer-seq2seq-routing-solver]]"
    type: related_to
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: related_to
  - target: "[[references/dinh2021-haco-pdstsp]]"
    type: related_to
  - target: "[[references/mbiadousaleu2022parallel]]"
    type: related_to
  - target: "[[references/song2018-persistent-uav-delivery-milp-rhta]]"
    type: related_to
sources:
  - _papers/nguyen2022mincost/nguyen2022mincost-extracted.md
  - _papers/nguyen2022mincost/nguyen2022mincost.md
  - _papers/montemanni2023constraint/montemanni2023constraint-extracted.md
  - _papers/montemanni2023constraint/montemanni2023constraint.md
summary: PDSVRP minimizes total truck+drone operating cost with multiple trucks and parallel drones under capacity and time constraints.
provenance:
  extracted: 0.83
  inferred: 0.17
  ambiguous: 0.0
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-22T11:13:25Z
updated: 2026-10-30T14:38:55Z
---

# Min-cost Parallel Drone Scheduling VRP (PDSVRP)

Min-cost PDSVRP is a truck-drone routing model where multiple trucks and multiple depot-based drones are coordinated to serve customers at minimum transportation cost.

## Key Ideas

- Customer set is partitioned into:
  - truck-only customers,
  - mode-flexible customers (truck or drone).
- Drones execute one-customer back-and-forth flights from the depot.
- Both fleet layers are constrained by working-time limits; trucks also obey route-capacity constraints.
- Objective is total operating cost, which differs structurally from min-time objectives and changes local-search move usefulness.
- Slack-inducing [[concepts/dag-topological-sort-scheduling-move-evaluation|ruin-and-recreate]] patterns (e.g., sweep/string removals) are effective for this objective. ^[inferred]
- Constraint-programming formulations with per-truck Circuit constraints plus giant-tour models carrying time and weight counters (Montemanni & Dell'Amico 2023) produced the first lower bounds ever on the published min-cost benchmark instances; the giant-tour model scales to 400-customer instances for bounds, while the 3-index model often fails to bound large ones.

Reported sensitivity results indicate drone value is most governed by battery endurance and truck-drone cost ratio, with notable scenario interactions rather than one-factor effects.

Related pages: [[references/nguyen2022-min-cost-pdsvrp]], [[concepts/min-cost-tsp-with-drone]], [[concepts/pdsvrp-c]], [[concepts/bilevel-vrpd-task-assignment-routing]], [[references/montemanni2024-pdsvrp-collective-drones]], [[references/montemanni2023-cp-pdsvrp]].

## Open Questions

- How should min-cost PDSVRP be reformulated when payload-dependent drone energy is explicit instead of preprocessed eligibility?
- Which robust/stochastic extensions best preserve solution quality under uncertain travel times and demand? ^[inferred]


## Related

- [[references/torabbeigi2020-payload-bcr-drone-scheduling]] — shares drones + scheduling tags with this page
- [[concepts/dag-topological-sort-scheduling-move-evaluation]] — exact insertion cost under drone synchronization
- [[references/song2018-persistent-uav-delivery-milp-rhta]] — persistent UAV delivery with payload-weighted flight time, solved by a receding-horizon petal heuristic in under 0.4 s
- [[references/sacramento2019-vrp-d-truck-drone-alns-cost]] — shares drones + vrp tags with this page
## Sources

- [[_papers/nguyen2022mincost/nguyen2022mincost-extracted.md]]
- [[_papers/nguyen2022mincost/nguyen2022mincost.md]]
- [[_papers/montemanni2023constraint/montemanni2023constraint-extracted.md]]
- [[_papers/montemanni2023constraint/montemanni2023constraint.md]]
