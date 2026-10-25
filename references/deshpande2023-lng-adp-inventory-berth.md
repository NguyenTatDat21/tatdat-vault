---
title: >-
  Optimal LNG ADP with Customer Inventory and Berth Management (Deshpande et
  al., 2023)
category: references
tags: [paper, lng, maritime, mixed-integer-programming]
relationships:
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: uses
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: extends
  - target: "[[references/al-haidous2016-optimal-lng-deliveries]]"
    type: extends
  - target: "[[references/andersson2017-creating-annual-lng-delivery-programs]]"
    type: extends
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: extends
  - target: "[[concepts/time-space-network-ship-flow-model]]"
    type: uses
sources:
  - _papers/deshpande2023optimal/deshpande2023optimal-extracted.md
  - _papers/deshpande2023optimal/deshpande2023optimal.md
summary: >-
  Profit-maximizing LNG annual delivery model that adds explicit customer
  inventory and berth constraints, showing these constraints prevent operationally
  infeasible ADPs.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T23:45:17Z
updated: 2026-10-24T19:52:48Z
---

# Optimal LNG ADP with Customer Inventory and Berth Management (Deshpande et al., 2023)

> [!tldr] This paper extends LNG annual-delivery optimization by explicitly modeling customer inventory and berth operations, and shows those constraints are necessary to avoid physically infeasible plans.

## Problem & Contribution

The paper studies annual LNG delivery planning for suppliers serving LTC customers plus a spot market. Unlike several earlier ADP models, it explicitly enforces:
- customer-side inventory feasibility,
- customer/supplier berth limits,
- maintenance and ship-availability coupling,
- oversupply penalties with spot-market revenue trade-off.

## Mathematical Program

Objective (L271–277): minimize oversupply, maximize spot-market sales, minimize transport cost. LTC revenue is **removed** from the objective because LTC volumes are fixed by the signed contracts.

$$
\max \; (\text{spot revenue} - \text{transport cost} - \text{oversupply penalty})
$$

The formulation is slot-based and integrates:
- ship scheduling/loading constraints,
- supplier inventory balance and berth capacity,
- customer inventory balance and berth compatibility,
- maintenance timing constraints,
- oversupply accounting.

## Results

- Illustrative and case-study runs produce near-optimal ADPs while keeping oversupply below about **1%**.
- Comparative case analysis indicates that removing customer inventory/berth constraints creates plans with large inventory-limit violations over many days.
- The model supports single-grade and multi-grade planning and captures spot-market decisions.

## Limitations

- Split delivery is not modeled (one ship does not serve multiple customers within one voyage).
- Several parameters are deterministic (transport time/cost, spot price), so robustness to stochastic variation remains future work. ^[inferred]

## Related

- [[concepts/annual-lng-delivery-program]]
- [[concepts/maritime-inventory-routing-problem]]
- [[references/al-haidous2016-optimal-lng-deliveries]]
- [[references/andersson2017-creating-annual-lng-delivery-programs]]
- [[references/mutlu2016-lng-annual-delivery-program]]
- [[concepts/time-space-network-ship-flow-model]] — shares lng + maritime + mixed-integer-programming tags with this page

## Bibliographic Record

- Citation key: `deshpande2023optimal`
- DOI: `10.1021/acs.iecr.3c01769`
- Canonical URL: <https://doi.org/10.1021/acs.iecr.3c01769>
- Publication: *Industrial & Engineering Chemistry Research* (2023)
- Authors: Dnyanesh Deshpande; Mohd Shahrukh; Rajagopalan Srinivasan; Iftekhar A. Karimi
- Companion metadata note: [[_papers/deshpande2023optimal/deshpande2023optimal.md]]

## Sources

- [[_papers/deshpande2023optimal/deshpande2023optimal-extracted.md]]
- [[_papers/deshpande2023optimal/deshpande2023optimal.md]]
