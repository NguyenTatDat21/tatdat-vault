---
title: >-
  Min-cost Traveling Salesman Problem with Drone (Ha et al., 2018)
category: references
tags: [paper, drones, tsp, optimization]
relationships:
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: uses
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: related_to
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: related_to
sources:
  - _papers/ha2018mincost/ha2018mincost-extracted.md
  - _papers/ha2018mincost/ha2018mincost.md
  - _papers/ha2018mincost/images/page_8_image_2.jpg
  - _papers/ha2018mincost/images/page_8_image_4.jpg
  - _papers/ha2018mincost/images/page_23_image_6.jpg
  - _papers/ha2018mincost/images/page_29_image_0.jpg
summary: >-
  Defines min-cost TSP-D with transportation and waiting penalties, and shows split-based GRASP consistently beats TSP-LS in cost quality with acceptable runtime.
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-29T17:15:00Z
tier: core
created: 2026-10-22T09:52:03Z
updated: 2026-10-27T06:00:00Z
---

# Min-cost Traveling Salesman Problem with Drone (Ha et al., 2018)

> [!tldr] The paper reframes TSP-D around **operational cost minimization** (transport + waiting penalties), and introduces a split-based GRASP that outperforms a TSP-LS baseline in solution quality.

## Problem & Objective

Unlike earlier min-time focus, this work defines **min-cost TSP-D** where truck and drone must synchronize while minimizing:
- transportation costs,
- and waiting penalties when one vehicle waits for the other.

The framing emphasizes cost-aware coordination rather than pure completion-time minimization. ^[inferred]

![[_papers/ha2018mincost/images/page_8_image_2.jpg]]
![[_papers/ha2018mincost/images/page_8_image_4.jpg]]
*Figure 1: Optimal solution: TSP vs. min-cost TSP-D. TSP Objective = 1500, min-cost TSP-D Objective = 1000.82. The solid arcs are truck’s path. The dash arcs are drone’s path*


## Method / Architecture

The paper contributes:

1. **MILP formulation** for min-cost TSP-D,
2. **TSP-LS** baseline (adapted from earlier work),
3. **GRASP** with a split algorithm and local search.

GRASP structure:
- generate a giant tour (TSP construction heuristic),
- apply a shortest-path-based split on an auxiliary graph,
- improve via local operators (truck relocation, drone relocation, drone removal, two-exchange).

![[_papers/ha2018mincost/images/page_29_image_0.jpg]]
*Figure 3: A truck relocation move operator : relocate$_T$((TD, DD), 1, 2)*


The split procedure is the central design element enabling scalable solution construction.

![[_papers/ha2018mincost/images/page_23_image_6.jpg]]
*Figure 2: Auxiliary graph for TSP tour in Figure 1*


## Results

### Small instances (10 customers)

- MILP could not solve instances with >10 customers to optimality under 1-hour limit.
- On 10-customer tests, GRASP reached all optimal min-cost TSP-D solutions reported in that set, while TSP-LS found only one.
- Using drones reduced operational cost by **more than 20% and up to 53%** compared with truck-only TSP on this benchmark.

### Larger min-cost instances

Reported geometric means (relative to TSP baseline): ^[inferred]

| Instance size | GRASP ρ_avg | TSP-LS ρ_avg | GRASP T_avg | TSP-LS T_avg |
|---|---:|---:|---:|---:|
| 50 customers | **74.09** | 81.80 | 13.46 min | 0.15 min |
| 100 customers | **74.87** | 79.36 | 158.77 min | 1.79 min |

Interpretation: GRASP improves cost quality but with higher runtime.

### Objective trade-off (min-cost vs min-time)

From the paper’s aggregate comparison:
- min-time solutions improve completion time more,
- min-cost solutions save more operational cost (about 30% average vs about 20% for min-time in their summary table).

The authors also report that min-cost solutions use drones for up to 40% of customers, whereas min-time solutions use drones for up to 22% (higher drone speed raises the frequency).

## Limitations

- Single-truck TSP-D setting; direct transfer to multi-truck/multi-drone-station variants is non-trivial. ^[inferred]
- Runtime for high-quality GRASP solutions on 100-customer instances is materially higher than TSP-LS. ^[inferred]
- Extraction includes noisy table formatting, so some table-level fields may require PDF-level verification for audit use. ^[ambiguous]

## Related

- [[concepts/min-cost-tsp-with-drone]]
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — ALNS benchmarked against the Ha et al. dataset.
- [[references/poikonen2020-k-mvdrp]]
- [[references/tamke2023-vrpd-dss]]
- [[_papers/nguyen2022mincost/nguyen2022mincost-extracted]]
- [[_papers/sacramento2019adaptive/sacramento2019adaptive-extracted]]
- [[_papers/dellamico2020matheuristic/dellamico2020matheuristic-extracted]]
- [[references/dellamico2020-matheuristics-pdstsp]]

## Bibliographic Record

- Citation key: `ha2018mincost`
- DOI: `10.1016/j.trc.2017.11.015`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S0968090X17303327>
- Publication: *Transportation Research Part C: Emerging Technologies* (2018)
- Authors: Quang Minh Ha; Yves Deville; Quang Dung Pham; Minh Hoàng Hà
- Companion metadata note: [[_papers/ha2018mincost/ha2018mincost.md]]

## Sources

- [[_papers/ha2018mincost/ha2018mincost-extracted.md]]
- [[_papers/ha2018mincost/ha2018mincost.md]]
- [[_papers/ha2018mincost/images/page_8_image_2.jpg]]
- [[_papers/ha2018mincost/images/page_8_image_4.jpg]]
- [[_papers/ha2018mincost/images/page_23_image_6.jpg]]
- [[_papers/ha2018mincost/images/page_29_image_0.jpg]]
