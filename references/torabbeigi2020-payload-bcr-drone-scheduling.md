---
title: Payload-induced Battery Consumption in Drone Delivery Scheduling (Torabbeigi et al., 2020)
category: references
tags: [paper, drones, energy-modeling, scheduling]
relationships:
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: uses
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: related_to
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: related_to
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
sources:
  - _papers/torabbeigi2020drone/torabbeigi2020drone-extracted.md
  - _papers/torabbeigi2020drone/torabbeigi2020drone.md
  - _papers/torabbeigi2020drone/images/page_2_chart_2.jpg
  - _papers/torabbeigi2020drone/images/page_3_chart_1.jpg
  - _papers/torabbeigi2020drone/images/page_9_chart_1.jpg
  - _papers/torabbeigi2020drone/images/page_0_image_2.jpg
  - _papers/torabbeigi2020drone/images/page_6_image_9.jpg
  - _papers/torabbeigi2020drone/images/page_10_image_1.jpg
summary: Introduces payload-dependent battery-consumption modeling for drone delivery and shows that ignoring it can make planned routes infeasible.
provenance:
  extracted: 0.89
  inferred: 0.09
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T10:00:17Z
updated: 2026-10-23T00:04:12Z
---

# Payload-induced Battery Consumption in Drone Delivery Scheduling (Torabbeigi et al., 2020)

> [!tldr] The paper adds payload-sensitive battery draw to drone scheduling and demonstrates that this single modeling change materially alters route feasibility and fleet sizing outcomes.

## Problem & Scope

The study focuses on delivery network planning where drones carry heterogeneous payloads, making energy use non-constant across missions.

It decomposes planning into:
- **Strategic Planning (SP):** selecting depot locations,
- **Operational Planning (OP):** scheduling and routing drones to satisfy delivery demand with minimal drone count.

## Method / Architecture

The central technical component is a linear payload-to-battery-consumption model:

\[
\text{BCR} = \alpha \cdot \text{payload} + \beta
\]

with estimated coefficients:
- \(\alpha = 2.297\)
- \(\beta = 3.879\)

The OP stage is formulated as an optimization model with preprocessing and bound-tightening strategies (including infeasible-arc elimination and bound-generation components) to improve solvability.

## Results

- Controlled flight experiments (payloads from 0 to 0.882 lb) support the linear BCR model fit.
- Statistical tests in the paper indicate strong significance for payload effects on battery consumption.
- In the reported example, ignoring payload-aware BCR would leave **3 of 5 paths (60%) infeasible**.
- The case study demonstrates that infrastructure and scheduling choices are sensitive to whether payload-aware energy constraints are modeled.

## Limitations

- Coefficients are estimated from a specific drone setup; transfer to other airframes/batteries likely needs recalibration.
- Multi-objective service metrics (lateness, fairness, resilience) are not the primary optimization target in this formulation. ^[inferred]
- Some extracted lines are oversized due embedded image payloads; fine-grained figure/table details should be verified from the PDF when needed. ^[ambiguous]

## Related

- [[concepts/payload-induced-drone-battery-consumption-rate]]
- [[references/dorling2017-drone-delivery-vrp]]
- [[concepts/min-cost-tsp-with-drone]]
- [[concepts/drone-speed-selection-in-routing]]
- [[references/tamke2023-vrpd-dss]]
- [[references/poikonen2020-k-mvdrp]]
- [[_papers/torabbeigi2020drone/torabbeigi2020drone-extracted]]

## Bibliographic Record

- Citation key: `torabbeigi2020drone`
- DOI: `10.1007/s10846-019-01034-w`
- Canonical URL: <https://doi.org/10.1007/s10846-019-01034-w>
- Publication: *Journal of Intelligent & Robotic Systems* (2020)
- Authors: Masoud Torabbeigi; Ali Lim; Teo Chung-Piaw
- Companion metadata note: [[_papers/torabbeigi2020drone/torabbeigi2020drone.md]]

## Sources

- [[_papers/torabbeigi2020drone/torabbeigi2020drone-extracted.md]]
- [[_papers/torabbeigi2020drone/torabbeigi2020drone.md]]
- [[_papers/torabbeigi2020drone/images/page_2_chart_2.jpg]]
- [[_papers/torabbeigi2020drone/images/page_3_chart_1.jpg]]
- [[_papers/torabbeigi2020drone/images/page_9_chart_1.jpg]]
- [[_papers/torabbeigi2020drone/images/page_0_image_2.jpg]]
- [[_papers/torabbeigi2020drone/images/page_6_image_9.jpg]]
- [[_papers/torabbeigi2020drone/images/page_10_image_1.jpg]]
