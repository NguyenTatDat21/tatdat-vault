---
title: Multiple Flying Sidekicks Traveling Salesman Problem (Murray & Raj, 2020)
category: references
tags: [paper, truck-drone-routing, heuristics, milp]
relationships:
  - target: "[[concepts/multiple-flying-sidekicks-traveling-salesman-problem]]"
    type: uses
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
sources:
  - _papers/murray2020multiple/murray2020multiple-extracted.md
  - _papers/murray2020multiple/murray2020multiple.md
  - _papers/murray2020multiple/images/page_2_chart_7.jpg
  - _papers/murray2020multiple/images/page_2_image_0.jpg
  - _papers/murray2020multiple/images/page_2_image_2.jpg
  - _papers/murray2020multiple/images/page_2_image_4.jpg
  - _papers/murray2020multiple/images/page_6_image_1.jpg
  - _papers/murray2020multiple/images/page_6_image_3.jpg
  - _papers/murray2020multiple/images/page_6_image_5.jpg
  - _papers/murray2020multiple/images/page_6_image_7.jpg
summary: Defines mFSTSP for one truck with multiple heterogeneous drones and proposes a three-phase heuristic with timing MILP to solve practical-scale instances.
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:39:28Z
updated: 2026-10-22T18:14:03Z
---

# Multiple Flying Sidekicks Traveling Salesman Problem (Murray & Raj, 2020)

> [!tldr] Extends truck-drone last-mile routing to multiple UAVs with heterogeneous endurance and launch/retrieval synchronization, then solves it with a three-phase heuristic plus timing MILP.

## Problem & Scope

The paper defines the **multiple flying sidekicks traveling salesman problem (mFSTSP)** for parcel delivery:

- one truck and multiple UAVs coordinate from a single depot,
- each customer is served exactly once by truck or UAV,
- UAV sorties launch from and return to the truck,
- objective is minimum completion time (makespan, including return to depot).

Compared with the earlier FSTSP setting, this version models multiple drones and operational synchronization at launch/retrieval events.

## Method / Architecture

The authors formulate mFSTSP as a MILP, but solve practical instances with a **three-phase heuristic**:

1. **Phase I – initial customer assignment** between truck and UAV service.
2. **Phase II – sortie construction** using candidate-generation and feasibility filtering.
3. **Phase III – timing optimization** via a reduced MILP that schedules truck/UAV timing and synchronization.

A lower-truck-limit control is used in the iterative search:

$$
LTL_0 = \left\lceil \frac{|C|-|V|}{|V|+1} \right\rceil
$$

where \(|C|\) is customer count and \(|V|\) is UAV count.

The model also evaluates endurance assumptions and automation variants (truck/depot automation effects).

## Results

Reported computational findings include:

- For 8-customer exact tests (320 cases), 220 solved to optimality within 1 hour by full MILP.
- Heuristic runtime is dramatically lower (e.g., average 0.08s in 8-customer set) with an average 4.5% gap to known optimum in that set.
- Relative to truck-only TSP baselines, average delivery-time improvements are substantial in larger cases (about 14% at 10 customers, 23% at 25, 21% at 50, 18% at 100).
- Additional UAVs yield **diminishing marginal benefit** in time savings.
- Automation scenarios further improve outcomes; reported average gains versus default range from 4.5% up to 13.0% depending on automation variant.

## Limitations

The study highlights that several realistic dimensions remain simplified (e.g., richer dynamic demand and broader operational constraints), leaving room for future stochastic and real-time extensions.

## Bibliographic Record

- Citation key: `murray2020multiple`
- DOI: `10.1016/j.trc.2019.11.003`
- Canonical URL: https://www.sciencedirect.com/science/article/pii/S0968090X19302505
- Publication: *Transportation Research Part C: Emerging Technologies* (2020)
- Authors: Chase C. Murray, Ritwik Raj
- Companion metadata note: [[_papers/murray2020multiple/murray2020multiple.md]]

## Related

- [[concepts/multiple-flying-sidekicks-traveling-salesman-problem]]
- [[concepts/k-multi-visit-drone-routing-problem]]
- [[concepts/min-cost-parallel-drone-scheduling-vrp]]
- [[references/poikonen2020-k-mvdrp]]
- [[references/tamke2023-vrpd-dss]]
- [[_papers/raj2020multiple/raj2020multiple-extracted]]

## Sources

- [[_papers/murray2020multiple/murray2020multiple-extracted.md]]
- [[_papers/murray2020multiple/murray2020multiple.md]]
- [[_papers/murray2020multiple/images/page_2_chart_7.jpg]]
- [[_papers/murray2020multiple/images/page_2_image_0.jpg]]
- [[_papers/murray2020multiple/images/page_2_image_2.jpg]]
- [[_papers/murray2020multiple/images/page_2_image_4.jpg]]
- [[_papers/murray2020multiple/images/page_6_image_1.jpg]]
- [[_papers/murray2020multiple/images/page_6_image_3.jpg]]
- [[_papers/murray2020multiple/images/page_6_image_5.jpg]]
- [[_papers/murray2020multiple/images/page_6_image_7.jpg]]
