---
title: >-
  Solving Vehicle Routing with Drones via Bi-level Heuristic (Yang et al., 2022)
category: references
tags: [paper, drones, vehicle-routing, heuristics, bilevel-optimization, alns]
relationships:
  - target: "[[concepts/bilevel-vrpd-task-assignment-routing]]"
    type: related_to
  - target: "[[references/yi2023-ace-gsf-automated-design-cvrptw]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: related_to
  - target: "[[references/hendel2022-adaptive-lns-for-mip]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
sources:
  - _papers/yang2022solving/yang2022solving-extracted.md
  - _papers/yang2022solving/yang2022solving.md
  - _papers/yang2022solving/images/page_1_image_6.jpg
  - _papers/yang2022solving/images/page_2_image_0.jpg
  - _papers/yang2022solving/images/page_4_image_8.jpg
  - _papers/yang2022solving/images/page_5_chart_0.jpg
  - _papers/yang2022solving/images/page_5_chart_2.jpg
summary: >-
  Introduces a bi-level VRPD heuristic that combines BSO assignment and ALNS routing to reduce customer waiting time in multi-truck, multi-station drone delivery.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T09:52:03Z
updated: 2026-10-30T14:08:41Z
---

# Solving Vehicle Routing with Drones via Bi-level Heuristic (Yang et al., 2022)

> [!tldr] The paper models a multi-truck/multi-UAV-station VRPD and solves it with a bi-level heuristic: BSO for assignment plus ALNS-SA for route/schedule refinement.

## Problem & Objective

The paper studies a VRPD variant with:
- one depot,
- multiple trucks,
- multiple UAV stations,
- and UAV-serviceable vs truck-only customers.

Assumptions: UAV stations are placed in densely populated communities, trucks unload parcels at stations so they need not visit every customer, and each customer is served exactly once by truck or drone. Flight-range areas of different stations do not overlap, so each UAV-serviceable customer maps to one station, and each UAV carries one parcel per trip, returning to its station before the next customer. Customers outside any station range are Truck-Only Customers (TOC), the rest are UAV-Serviceable Customers (USC), and become Truck-Responsible (TRC) or UAV-Responsible (URC) once assigned.

![[_papers/yang2022solving/images/page_1_image_6.jpg]]

*Fig. 1 (paper): A delivery scenario*

The objective is the sum of all customer waiting times, chosen for customer satisfaction rather than the usual tour length defined as the latest return time of all vehicles at the depot (Eq. 1):

$$
t = \sum_{toc \in L^{toc}} t_{toc} + \sum_{s \in L^{s}} \sum_{usc \in L_{s}^{usc}} t_{usc}
$$

where $t_{toc}$ is the waiting time of a truck-only customer and $t_{usc}$ the waiting time of a UAV-serviceable customer of station $s$. The paper extends the TSP-DS model to multiple trucks and multiple drone stations.

![[_papers/yang2022solving/images/page_2_image_0.jpg]]

*Fig. 2 (paper): Calculation of the sum of customer waiting times*
## Method / Architecture

The proposed method uses two coordinated levels:

1. **Upper level (assignment):** Brain Storm Optimization (BSO) searches customer assignment strings (`s_a`) where each UAV-serviceable customer is assigned to truck or drone service.
2. **Lower level (planning):** route planning + drone scheduling are rebuilt from `s_a`, with truck routing refined by ALNS under simulated annealing. The outer level runs in two variants: the original BSO with K-Means clustering, and BSO-OS, which clusters by objective value and keeps the top solutions as elitists.

A structural formulation in the paper is:

$$
s_a^* = \arg\min_{s_a} f\big(s_a, \operatorname{PathPlanning}(s_a)\big)
$$

Key mechanics reported:
- assignment operators include bit-flip and two-parent merge rules,
- parent-route reuse is distance-guided: when a solution is generated from two parents, the parent route with the shorter Hamming distance to the new assignment is reused, and customers that switch between drone and truck service are handled as drone-to-truck and truck-to-drone nodes,
- drone scheduling at each station prioritizes nearer UAV customers to reduce cumulative waiting,
- tuned parameters (Table I): original BSO $K = 5$ for K-Means with 10 clustering repeats, $p_{best} = 45\%$ parent-selection probability and $p_{one} = 80\%$ single-parent generation; BSO-OS elitist share $perc_e = 20\%$, $p_e = 80\%$, $p_{one} = 80\%$; ALNS-SA accepts a solution 10% worse than the current one with initial probability 50%, with temperature exponentially decreasing to 0.1% of the initial value.

## Results

Experimental setup:
Experimental setup:
- 3 scenarios: 60 / 100 / 150 customers,
- 30 runs per method,
- compared: **BSO-Original + ALNS**, **BSO-OS + ALNS**, and **single-level ALNS**,
- population of 50 solutions, at most 100 outer iterations with mostly 400 inner iterations for the bi-level methods, $2 \times 10^6$ iterations for single-level ALNS, and early stopping when the best objective has not improved for 20% of the maximum iterations.

From Table II, the BSO-OS + ALNS variant produced the best average objective in all three scenarios:

| Customers | BSO-Original + ALNS (avg) | BSO-OS + ALNS (avg) | ALNS (avg) |
|---|---:|---:|---:|
| 60 | 2841.635 | **2821.592** | 2831.037 |
| 100 | 5915.287 | **5817.652** | 5978.271 |
| 150 | 9767.243 | **9532.052** | 9929.743 |

Standard deviations (same order): 10.523 / **3.782** / 24.208 at 60, 24.434 / **9.607** / 191.254 at 100, 39.888 / **22.540** / 306.900 at 150. Minimum objectives per scenario: 2820.556 / 2820.041 / 2820.041, 5849.222 / 5809.648 / 5809.648, 9694.211 / 9503.725 / 9601.444.

The best value of each row is printed in bold in Table II, so BSO-OS + ALNS behaves better than the other two methods, and the single-level ALNS ties the BSO-OS minimum at 60 and 100 customers while being worse on average. Convergence curves (Fig. 5) show better exploration for BSO-OS than BSO-Original. Route visualizations show trucks assigned to depot directions and trucks preferring to reach UAV stations early, leaving many UAV-responsible customers waiting less.

## Limitations

- Evidence is from one benchmark setup with fixed parameterization; generalization to other geographies and constraints is unproven.
- The paper demonstrates heuristic effectiveness, not optimality guarantees.
- UAV stations are assumed non-overlapping with single-parcel UAV trips and no recharging model, so denser service areas and battery constraints are outside the model. ^[inferred]
- The paper demonstrates heuristic effectiveness, not optimality guarantees.
No mathematical model is built for the extended problem, so exact methods such as mixed integer programming are left open, and the authors state that comparisons with more advanced methods and wider parameter ranges are future work. ^[extracted]

## Related

- [[concepts/bilevel-vrpd-task-assignment-routing]]
- [[references/yi2023-ace-gsf-automated-design-cvrptw]] — ACE learns the operators and heuristics this paper fixed by hand.
- [[concepts/large-neighborhood-search]]
- [[references/hendel2022-adaptive-lns-for-mip]]
- [[references/dorling2017-drone-delivery-vrp]]
- [[references/tamke2023-vrpd-dss]]
- [[references/poikonen2020-k-mvdrp]]
- [[_papers/windrasmara2022adaptive/windrasmara2022adaptive-extracted]]
- [[_papers/raj2020multiple/raj2020multiple-extracted]]
- [[_papers/mbiadousaleu2022parallel/mbiadousaleu2022parallel-extracted]]

## Bibliographic Record

- Citation key: `yang2022solving`
- DOI: `10.1109/SMC53654.2022.9945266`
- Canonical URL: <https://doi.org/10.1109/SMC53654.2022.9945266>
- Publication: *2022 IEEE International Conference on Systems, Man, and Cybernetics (SMC)*
- Authors: Jian Yang; Haobin Yang; Zonghan He; Qi Zhao; Yuhui Shi
- Companion metadata note: [[_papers/yang2022solving/yang2022solving.md]]

## Sources

- [[_papers/yang2022solving/yang2022solving-extracted.md]]
- [[_papers/yang2022solving/yang2022solving.md]]
- [[_papers/yang2022solving/images/page_2_image_0.jpg]]
- [[_papers/yang2022solving/images/page_4_image_8.jpg]]
- [[_papers/yang2022solving/images/page_5_chart_0.jpg]]
- [[_papers/yang2022solving/images/page_5_chart_2.jpg]]
