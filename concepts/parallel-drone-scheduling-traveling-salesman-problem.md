---
title: Parallel Drone Scheduling Traveling Salesman Problem (PDSTSP)
category: concepts
tags: [drones, pdstsp, scheduling, truck-drone-routing]
relationships:
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: derived_from
  - target: "[[references/dinh2021-haco-pdstsp]]"
    type: derived_from
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: extends
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: related_to
  - target: "[[references/montemanni2024-parallel-collective-drones]]"
    type: related_to
sources:
  - _papers/dellamico2020matheuristic/dellamico2020matheuristic-extracted.md
  - _papers/dellamico2020matheuristic/dellamico2020matheuristic.md
  - _papers/dinh2021ants/dinh2021ants-extracted.md
  - _papers/dinh2021ants/dinh2021ants.md
  - _papers/montemanni2024parallel/montemanni2024parallel-extracted.md
  - _papers/montemanni2024parallel/montemanni2024parallel.md
  - _papers/montemanni2024parallel/images/page_3_image_0.jpg
summary: >-
  Truck-and-parallel-drone routing problem minimizing makespan, typically solved
  via giant-tour decomposition plus MILP/DP split assignment and local search.
provenance:
  extracted: 0.87
  inferred: 0.11
  ambiguous: 0.02
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T23:45:17Z
updated: 2026-10-22T23:45:17Z
---

# Parallel Drone Scheduling Traveling Salesman Problem (PDSTSP)

PDSTSP coordinates one truck and multiple depot-based drones to serve customers while minimizing overall completion time.

## Key Ideas

- Customers are partitioned into truck-served and drone-served subsets.
- Truck route sequencing and drone assignment/scheduling are tightly coupled.
- A common pattern is **giant-tour first, split second**:
  1. build/improve a truck-oriented sequence,
  2. decode into truck/drone operations via MILP or DP-based split.
- Local search then refines assignment and sequencing decisions.

## Why It Matters

- It is a load-bearing benchmark between simple TSP-D variants and richer multi-truck VRP-with-drones models.
- Method families developed on PDSTSP (branch-and-cut, split decoders, ant-colony/metaheuristics) transfer to broader truck-drone settings. ^[inferred]

## Typical Method Families

1. **Exact / branch-and-cut MILP** for small/medium instances.
2. **Matheuristics** combining TSP-based sequence generation with restricted MILP refinement.
3. **Metaheuristics** (e.g., HACO) with dual decision-layer search and split decoding.

## Related

- [[references/dellamico2020-matheuristics-pdstsp]]
- [[references/dinh2021-haco-pdstsp]]
- [[concepts/min-cost-parallel-drone-scheduling-vrp]]
- [[concepts/min-cost-tsp-with-drone]]
- [[references/nguyen2022-min-cost-pdsvrp]]

## Open Questions

- Which decomposition remains most robust as drone count and eligibility ratio scale up?
- How should uncertainty in travel times and launch turnaround be integrated without collapsing tractability? ^[inferred]

## Sources

- [[_papers/dellamico2020matheuristic/dellamico2020matheuristic-extracted.md]]
- [[_papers/dellamico2020matheuristic/dellamico2020matheuristic.md]]
- [[_papers/dinh2021ants/dinh2021ants-extracted.md]]
- [[_papers/dinh2021ants/dinh2021ants.md]]
