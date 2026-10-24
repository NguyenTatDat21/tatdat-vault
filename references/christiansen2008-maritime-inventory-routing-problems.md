---
title: Maritime Inventory Routing Problems (Christiansen & Fagerholt, 2008)
category: references
tags: [maritime, inventory-routing, ship-routing-scheduling, review]
relationships:
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: uses
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: related_to
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: related_to
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
  - target: "[[references/deshpande2023-lng-adp-inventory-berth]]"
    type: related_to
sources:
  - _papers/christiansen2008maritime/christiansen2008maritime-extracted.md
  - _papers/christiansen2008maritime/christiansen2008maritime.md
summary: >-
  Defines the basic maritime inventory routing problem (ISRP) and its main extensions, integrating ship routing/scheduling with inventory dynamics at production and consumption ports.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T23:17:15Z
updated: 2026-10-23T00:04:12Z
---

# Maritime Inventory Routing Problems (Christiansen & Fagerholt, 2008)

> [!tldr] The paper frames maritime inventory routing as one integrated optimization problem where routing and scheduling choices must co-evolve with port inventory feasibility.

## Problem & Contribution

The work defines the **Inventory Ship Routing Problem (ISRP)** as a combined:
1. ship routing and scheduling problem, and
2. inventory management problem at loading/production and unloading/consumption ports.

Its key contribution is a clean baseline formulation that later MIR/LNG studies extend.

![[_papers/christiansen2008maritime/images/page_2_image_9.jpg]]
*Figure 2: A simplified planning situation with seven ports and two ships (cement producer in Norway: two production factories, five consumption ports, fleet of two ships).*


## Core Formulation (Basic ISRP)

A representative objective is transportation-cost minimization:

$$
\min \sum_{v \in \mathcal{V}} \sum_{(i,m,j,n) \in \mathcal{A}_v} C_{ijv}\, x_{imjnv}
$$

with coupled inventory balance at each port call:

$$
s_{i,m} = s_{i,m-1} - \sum_{v \in \mathcal{V}} I_i\, q_{i(m-1),v} + R_i (t_{i,m} - t_{i,m-1}) \quad \forall i \in \mathcal{N},\ m \in \mathcal{M}_i \setminus \{1\}
$$

and inventory safety bounds:

$$
S_{MN,i} \le s_{i,m} \le S_{MX,i} \quad \forall i \in \mathcal{N},\ m \in \mathcal{M}_i
$$

The paper also details routing flow constraints, ship-capacity constraints, service-time/scheduling constraints, and inventory-feasibility constraints over time.

## Extensions Highlighted

The article identifies major practical extensions beyond the basic ISRP:
- one-sided inventory constraints (only production or only consumption side),
- variable production/consumption rates,
- multi-product and compartment/stowage effects,
- spot charter integration,
- hybrid inventory-routing + cargo-routing settings,
- broader supply-chain coupling (production and downstream logistics).

## Evidence & Practical Notes

| Observation | Implication |
|---|---|
| ISRP is harder than standard VRP due to inventory state coupling | Exact methods scale poorly without decomposition ^[inferred] |
| Real cases frequently combine several extensions at once | Single-purpose models are often insufficient in deployment |
| Maritime operations include weather and production/consumption uncertainty | Deterministic plans can degrade under disturbances ^[inferred] |
## Limitations

- This is a survey/introductory synthesis, so numerical comparison across all extension classes is limited.
- Several formulation details depend on case assumptions (e.g., loading policy, berth restrictions, stowage granularity). ^[inferred]

## Related

- [[concepts/maritime-inventory-routing-problem]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/mutlu2016-lng-annual-delivery-program]]
- [[references/deshpande2023-lng-adp-inventory-berth]]
- [[concepts/annual-lng-delivery-program]]
- [[concepts/maritime-routing-under-uncertainty]]

## Bibliographic Record

- Citation key: `christiansen2008maritime`
- DOI: `10.1007/978-0-387-74759-0_352`
- Canonical URL: <https://link.springer.com/rwe/10.1007/978-0-387-74759-0_352>
- Publication: *Encyclopedia of Optimization* (2008)
- Authors: Marielle Christiansen; Kjetil Fagerholt
- Companion metadata note: [[_papers/christiansen2008maritime/christiansen2008maritime.md]]

## Sources

- [[_papers/christiansen2008maritime/christiansen2008maritime-extracted.md]]
- [[_papers/christiansen2008maritime/christiansen2008maritime.md]]
