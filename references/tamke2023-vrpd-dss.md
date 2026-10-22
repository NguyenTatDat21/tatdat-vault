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
sources:
  - _papers/tamke2023vehicle/tamke2023vehicle-extracted.md
  - _papers/tamke2023vehicle/tamke2023vehicle.md
summary: >-
  Introduces VRPD-DSS with discrete drone-speed decisions and payload-aware energy costs, showing that adaptive speed choices beat constant-speed operations in truck-drone delivery.
provenance:
  extracted: 0.82
  inferred: 0.15
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:12:13Z
updated: 2026-10-22T09:12:13Z
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

The study reports that always flying at maximum drone speed is often suboptimal once realistic energy effects are included.

Main findings:
- adaptive speed selection improves objective quality versus fixed-speed baselines;
- a substantial share of savings comes from reduced driver/truck active time;
- drone energy cost contributes less than labor and truck-time effects in the studied setting.

This supports the broader claim that operationally realistic energy models reduce overoptimistic savings reported in simplified truck-drone studies. ^[inferred]

## Limitations

- Evidence is generated on one benchmarked rural context and may not transfer directly to dense urban settings.
- The extraction source includes formatting artifacts (binary/NUL corruption in one export), so a few equation-level details may be under-resolved. ^[ambiguous]

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
