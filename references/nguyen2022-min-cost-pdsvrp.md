---
title: The Min-cost Parallel Drone Scheduling Vehicle Routing Problem (Nguyen et al., 2022)
category: references
tags: [paper, vrp, drones, metaheuristics]
relationships:
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: uses
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: related_to
  - target: "[[concepts/pdsvrp-c]]"
    type: related_to
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: related_to
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: uses
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: related_to
  - target: "[[references/dinh2021-haco-pdstsp]]"
    type: related_to
  - target: "[[concepts/dag-topological-sort-scheduling-move-evaluation]]"
    type: related_to
sources:
  - _papers/nguyen2022mincost/nguyen2022mincost-extracted.md
  - _papers/nguyen2022mincost/nguyen2022mincost.md
  - _papers/nguyen2022mincost/images/page_0_image_10.jpg
  - _papers/nguyen2022mincost/images/page_3_image_8.jpg
  - _papers/nguyen2022mincost/images/page_5_image_2.jpg
  - _papers/nguyen2022mincost/images/page_6_image_2.jpg
  - _papers/nguyen2022mincost/images/page_16_chart_4.jpg
  - _papers/nguyen2022mincost/images/page_18_chart_2.jpg
  - _papers/nguyen2022mincost/images/page_18_chart_4.jpg
summary: Introduces the min-cost PDSVRP, a MILP and SISSRs heuristic, with strong performance on instances up to 400 customers and state-of-the-art PDSTSP adaptation.
provenance:
  extracted: 0.91
  inferred: 0.07
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:13:25Z
updated: 2026-10-23T00:04:12Z
---

# The Min-cost Parallel Drone Scheduling Vehicle Routing Problem (Nguyen et al., 2022)

> [!tldr] This paper defines min-cost PDSVRP (multi-truck + parallel drones), proposes a MILP and a tailored SISSRs [[concepts/dag-topological-sort-scheduling-move-evaluation|ruin-and-recreate]] metaheuristic, and reports strong solution quality plus a state-of-the-art PDSTSP adaptation.

## Problem & Scope

The paper studies a mixed fleet where trucks run route tours and drones run depot-customer-depot trips, under capacity and working-time constraints.

Unlike min-time formulations, the objective is total transportation cost minimization, which changes neighborhood-search behavior and assignment logic.

## Method / Architecture

Two layers are proposed:

1. **MILP model** for exact solving of small instances;
2. **SISSRs heuristic** (Slack Induction by String and Sweep Removals), a ruin-and-recreate method with:
   - sweep removal,
   - random drone-customer removal,
   - adjacent string removal,
   - greedy insertion with blinks,
   - local search, perturbation, and threshold acceptance.

The design explicitly targets slack creation in ruined solutions to improve recreate-phase quality.

## Results

Key reported outcomes include:

- On small instances, SISSRs recovered all CPLEX optima found and improved CPLEX on additional hard cases.
- CPLEX solved 15/27 thirty-customer instances to optimality quickly, but only 5/27 fifty-customer instances, with multiple out-of-memory/failed-feasible cases.
- On 100/200/400-customer sets, SISSRs remained stable with average gaps reported below about 5.59% and runtimes generally below 10 minutes.
- Component study shows **full SISSRs configuration** is strongest; local search and threshold acceptance contribute most.
- Sensitivity analysis (CART over 1000 generated instances) reports average drone-enabled cost saving around **20.42%**, with battery endurance and truck-drone cost ratio as dominant factors.
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem|PDSTSP]] adaptation produced **26 new best-known solutions**, outperforming compared metaheuristics in solution quality.

## Limitations

- Results are primarily based on synthetic instance generators and selected benchmark families; operational transfer depends on calibration. ^[inferred]
- Threshold values from CART (e.g., endurance and cost-ratio split points) are scenario-dependent, not universal engineering constants. ^[inferred]
- Some extracted lines are oversized/truncated (embedded figures/tables), so fine-grained table cells may require PDF verification. ^[ambiguous]

## Related

- [[concepts/min-cost-parallel-drone-scheduling-vrp]]
- [[concepts/min-cost-tsp-with-drone]]
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]]
- [[references/dellamico2020-matheuristics-pdstsp]]
- [[references/dinh2021-haco-pdstsp]]
- [[concepts/pdsvrp-c]]
- [[references/montemanni2024-pdsvrp-collective-drones]]
- [[references/yang2022-vrpd-bilevel-heuristic]]
- [[_papers/nguyen2022mincost/nguyen2022mincost-extracted]]
- [[concepts/dag-topological-sort-scheduling-move-evaluation]] — the DAG move evaluation that the RnR insertion uses

## Bibliographic Record

- Citation key: `nguyen2022mincost`
- DOI: `10.1016/j.ejor.2021.07.008`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S0377221721006032>
- Publication: *European Journal of Operational Research* (2022)
- Authors: Minh Anh Nguyen; Giang Thi-Huong Dang; Minh Hoàng Hà; Minh-Trien Pham
- Companion metadata note: [[_papers/nguyen2022mincost/nguyen2022mincost.md]]

## Sources

- [[_papers/nguyen2022mincost/nguyen2022mincost-extracted.md]]
- [[_papers/nguyen2022mincost/nguyen2022mincost.md]]
- [[_papers/nguyen2022mincost/images/page_0_image_10.jpg]]
- [[_papers/nguyen2022mincost/images/page_3_image_8.jpg]]
- [[_papers/nguyen2022mincost/images/page_5_image_2.jpg]]
- [[_papers/nguyen2022mincost/images/page_6_image_2.jpg]]
- [[_papers/nguyen2022mincost/images/page_16_chart_4.jpg]]
- [[_papers/nguyen2022mincost/images/page_18_chart_2.jpg]]
- [[_papers/nguyen2022mincost/images/page_18_chart_4.jpg]]
