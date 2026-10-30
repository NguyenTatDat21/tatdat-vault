---
title: >-
  Vehicle Routing Problem with Drones and Drone Speed Selection (Tamke & Buscher, 2023)
category: references
tags: [paper, drones, vehicle-routing, energy-modeling]
relationships:
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: uses
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
  - target: "[[concepts/benchmark-instance-design]]"
    type: related_to
  - target: "[[concepts/exact-multitrip-vrptw-framework]]"
    type: related_to
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
  - target: "[[concepts/phase-transition-instance-generation]]"
    type: related_to
  - target: "[[references/ha2018-min-cost-tsp-d]]"
    type: related_to
  - target: "[[references/paradiso2020-esf-multitrip-vrptw]]"
    type: related_to
  - target: "[[references/torabbeigi2020-payload-bcr-drone-scheduling]]"
    type: related_to
  - target: "[[references/yang2022-vrpd-bilevel-heuristic]]"
    type: related_to
sources:
  - _papers/tamke2023vehicle/tamke2023vehicle-extracted.md
  - _papers/tamke2023vehicle/tamke2023vehicle.md
  - _papers/tamke2023vehicle/images/page_7_chart_0.jpg
  - _papers/tamke2023vehicle/images/page_7_chart_2.jpg
  - _papers/tamke2023vehicle/images/page_7_chart_4.jpg
  - _papers/tamke2023vehicle/images/page_10_chart_0.jpg
summary: >-
  Introduces VRPD-DSS with discrete drone-speed decisions and payload-aware energy costs, showing that adaptive speed choices beat constant-speed operations in truck-drone delivery.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T09:12:13Z
updated: 2026-10-30T14:38:55Z
---

# Vehicle Routing Problem with Drones and Drone Speed Selection (Tamke & Buscher, 2023)

> [!tldr] The paper formulates VRPD-DSS as a cost-minimizing mixed-integer model where each drone flight selects a speed from a discrete set under speed-dependent energy consumption.

## Problem & Motivation

The paper targets truck-drone parcel delivery settings where drone speed materially changes battery usage and thus feasible routing decisions.

Unlike constant-speed assumptions, the model treats speed as a first-class routing decision and optimizes total operating cost (truck fuel, driver labor, drone energy).

## Method / Architecture

The authors formulate a comprehensive MIP for the **vehicle routing problem with drones and drone speed selection (VRPD-DSS)**.

Key modeling elements:
- each drone flight selects one speed from a discrete candidate set;
- drone energy consumption depends on speed and load;
- charging/recharging dynamics are modeled at the truck;
- preprocessing removes dominated speed choices;
- additional valid inequalities tighten the formulation.

The preprocessing and cuts are presented as practical enablers for solving larger instances than a direct formulation would allow.

## Results

The re-extracted paper reports concrete computational effects across the rural test set:

- Preprocessing removed an average **23.10%** of candidate drone operations in 20-customer instances and substantially shrank MILP size.
- Across tested speed sets, preprocessing reduced nonzero matrix elements by roughly **37%–63%** and runtime by about **52%–80%** (with identical optimal costs).
- In single-speed VRPD runs, the best average fixed speed was **12 m/s**; both slower and faster fixed speeds were usually worse.
- Relative to VRPD-DSS, the best fixed-speed VRPD (12 m/s) was still on average **0.59%** worse (1 drone) and **0.78%** worse (2 drones), with larger gaps in some instances. ^[inferred]
- For larger instances (30/40/50 customers), the MILP setup behaved effectively as a heuristic: average RPD after 1 hour ranged from about **0.13%** to **1.50%** depending on instance size and drone count.

Savings against truck-only delivery remained significant, and most savings were associated with reduced truck-driver time rather than drone electricity cost.
## Limitations

- Evidence comes from one rural benchmark region and may not transfer directly to dense urban contexts. ^[inferred]
- The energy model assumes ideal ambient conditions (e.g., no wind), so real operations may show different feasible-speed envelopes. ^[inferred]
- For larger instances, the solver is used mainly as a high-quality heuristic and many cases are not proven optimal within practical runtimes.
## Related

- [[concepts/drone-speed-selection-in-routing]]
- [[concepts/k-multi-visit-drone-routing-problem]]
- [[references/poikonen2020-k-mvdrp]]
- [[_papers/zhang2021energy/zhang2021energy-extracted]]
- [[_papers/dorling2017vehicle/dorling2017vehicle]]
- [[_papers/raj2020multiple/raj2020multiple-extracted]]

## Bibliographic Record

- Citation key: `tamke2023vehicle`
- DOI: `10.1016/j.cor.2022.106112`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S0305054822003422>
- Publication: *Computers & Operations Research* (2023)
- Authors: Felix Tamke; Udo Buscher
- Companion metadata note: [[_papers/tamke2023vehicle/tamke2023vehicle.md]]

## Sources

- [[_papers/tamke2023vehicle/tamke2023vehicle-extracted.md]]
- [[_papers/tamke2023vehicle/tamke2023vehicle.md]]
- [[_papers/tamke2023vehicle/images/page_7_chart_0.jpg]]
- [[_papers/tamke2023vehicle/images/page_7_chart_2.jpg]]
- [[_papers/tamke2023vehicle/images/page_7_chart_4.jpg]]
- [[_papers/tamke2023vehicle/images/page_10_chart_0.jpg]]
