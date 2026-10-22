---
title: Ship Routing and Scheduling in the New Millennium (Christiansen et al., 2013)
category: references
tags: [maritime, ship-routing-scheduling, review, liner-shipping]
relationships:
  - target: "[[references/christiansen2007-maritime-transportation-operations-research]]"
    type: extends
  - target: "[[references/christiansen2020-liner-shipping-network-design]]"
    type: related_to
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[concepts/liner-shipping-network-design]]"
    type: related_to
sources:
  - _papers/christiansen2013ship/christiansen2013ship-extracted.md
  - _papers/christiansen2013ship/christiansen2013ship.md
summary: >-
  Reviews 2002–2011 ship routing and scheduling research, providing canonical liner network-design and fleet-deployment formulations and highlighting growth, decomposition trends, and open maritime optimization gaps.
provenance:
  extracted: 0.89
  inferred: 0.09
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T23:17:15Z
updated: 2026-10-22T23:17:15Z
---

# Ship Routing and Scheduling in the New Millennium (Christiansen et al., 2013)

> [!tldr] A landmark review of maritime OR in 2002–2011 that formalizes liner network design and fleet deployment, then maps how methods evolved toward decomposition and richer planning scope.

## Problem & Contribution

This invited review updates earlier maritime surveys and analyzes over one hundred new refereed papers from 2002–2011. It shows that research volume has roughly doubled by decade and that model scope expanded from narrow routing tasks to integrated network, deployment, inventory-routing, LNG, speed, and emissions decisions.

The paper contributes:
- a planning-structure map for liner, tramp, and industrial modes,
- canonical optimization models for liner network design and fleet deployment,
- trend analysis by method class and application area,
- explicit research gaps for unresolved practical-scale problems.

## Core Models (Representative Equations)

### Liner network design objective (simplified review model)

$$
\max \Big(\text{transport revenue} - \sum_{(o,d,i)\in\mathcal W}\sum_{a\in\mathcal A} C_a^C y_a^{(o,d,i)} - \sum_{v\in\mathcal V}\sum_{r\in\mathcal R} C_{vr}^V x_{vr}\Big)
$$

subject to flow conservation, ship-capacity coupling on arcs, demand bounds, and ship-availability constraints.

### Fleet deployment model (reviewed template)

$$
\min \sum_{v\in\mathcal V}\sum_{r\in\mathcal R}\left(C_{vr}x_{vr}+C_v^I n_{vr}^I\right)+\sum_{v\in\mathcal V}\left(C_v^L d_v-C_v^O n_v^O\right)
$$

with demand satisfaction, frequency, vessel-availability, voyage-time, and lay-up constraints.

## Key Evidence

| Signal from review | Reported value / implication |
|---|---|
| Fleet growth in 2000–2010 decade | Oil tankers +60%, dry bulk +65%, containership capacity +164% |
| Seaborne trade growth (2000→2010) | ~40% increase |
| Method trend | More decomposition/heuristic hybrids for practical-scale instances |
| Topic trend | Increased focus on MIR, LNG logistics, speed/bunkering, emissions |

## Practical Insights

- Integrated maritime planning is increasingly necessary because network design, deployment, and cargo/inventory decisions interact strongly.
- Pure monolithic formulations often face scalability limits, motivating decomposition and matheuristic pipelines. ^[inferred]
- Data/model realism grew (e.g., transshipment costs, speed decisions, uncertainty), but unresolved critical problems remained open in 2013.

## Limitations

- As a review, conclusions depend on coverage choices (English refereed outlets, 2002–2011 window).
- Reported computational comparisons are not based on a single unified benchmark across all subtopics.

## Related

- [[references/christiansen2007-maritime-transportation-operations-research]]
- [[references/christiansen2020-liner-shipping-network-design]]
- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/liner-shipping-network-design]]
- [[concepts/maritime-routing-under-uncertainty]]

## Bibliographic Record

- Citation key: `christiansen2013ship`
- DOI: `10.1016/j.ejor.2012.12.002`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S037722171300003X>
- Publication: *European Journal of Operational Research* (2013)
- Authors: Marielle Christiansen; Kjetil Fagerholt; Bjørn Nygreen; David Ronen
- Companion metadata note: [[_papers/christiansen2013ship/christiansen2013ship.md]]

## Sources

- [[_papers/christiansen2013ship/christiansen2013ship-extracted.md]]
- [[_papers/christiansen2013ship/christiansen2013ship.md]]
