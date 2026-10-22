---
title: >-
  Solving Vehicle Routing with Drones via Bi-level Heuristic (Yang et al., 2022)
category: references
tags: [paper, drones, vehicle-routing, heuristics]
relationships:
  - target: "[[concepts/bilevel-vrpd-task-assignment-routing]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: related_to
sources:
  - _papers/yang2022solving/yang2022solving-extracted.md
  - _papers/yang2022solving/yang2022solving.md
  - _papers/yang2022solving/images/page_2_image_0.jpg
  - _papers/yang2022solving/images/page_4_image_8.jpg
  - _papers/yang2022solving/images/page_5_chart_0.jpg
  - _papers/yang2022solving/images/page_5_chart_2.jpg
summary: >-
  Introduces a bi-level VRPD heuristic that combines BSO assignment and ALNS routing to reduce customer waiting time in multi-truck, multi-station drone delivery.
provenance:
  extracted: 0.84
  inferred: 0.13
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:52:03Z
updated: 2026-10-22T18:14:03Z
---

# Solving Vehicle Routing with Drones via Bi-level Heuristic (Yang et al., 2022)

> [!tldr] The paper models a multi-truck/multi-UAV-station VRPD and solves it with a bi-level heuristic: BSO for assignment plus ALNS-SA for route/schedule refinement.

## Problem & Objective

The paper studies a VRPD variant with:
- one depot,
- multiple trucks,
- multiple UAV stations,
- and UAV-serviceable vs truck-only customers.

The optimization objective is to minimize the sum of customer waiting times.

$$
\min \sum_{c \in C} T_c^{wait}
$$

## Method / Architecture

The proposed method uses two coordinated levels:

1. **Upper level (assignment):** Brain Storm Optimization (BSO) searches customer assignment strings (`s_a`) where each UAV-serviceable customer is assigned to truck or drone service.
2. **Lower level (planning):** route planning + drone scheduling are rebuilt from `s_a`, with truck routing refined by ALNS under simulated annealing.

A structural formulation in the paper is:

$$
s_a^* = \arg\min_{s_a} f\big(s_a, \operatorname{PathPlanning}(s_a)\big)
$$

Key mechanics reported:
- assignment operators include bit-flip and two-parent merge rules,
- parent-route reuse is distance-guided (Hamming distance),
- drone scheduling at each station prioritizes nearer UAV customers to reduce cumulative waiting.

## Results

Experimental setup:
- 3 scenarios: 60 / 100 / 150 customers,
- 30 runs per method,
- compared: **BSO-Original + ALNS**, **BSO-OS + ALNS**, and **single-level ALNS**.

From Table II, the BSO-OS + ALNS variant produced the best average objective in all three scenarios:

| Customers | BSO-Original + ALNS (avg) | BSO-OS + ALNS (avg) | ALNS (avg) |
|---|---:|---:|---:|
| 60 | 2841.635 | **2821.592** | 2831.037 |
| 100 | 5915.287 | **5817.652** | 5978.271 |
| 150 | 9767.243 | **9532.052** | 9929.743 |

The paper also reports lower variance for BSO-OS than the other two methods across tested scales.

## Limitations

- Evidence is from one benchmark setup with fixed parameterization; generalization to other geographies and constraints is unproven.
- The paper demonstrates heuristic effectiveness, not optimality guarantees.
- Large embedded figure/table artifacts in the extraction limit direct reproduction of all visual diagnostics. ^[ambiguous]

## Related

- [[concepts/bilevel-vrpd-task-assignment-routing]]
- [[concepts/large-neighborhood-search]]
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
