---
title: >-
  Annual LNG Delivery Program (ADP)
category: concepts
tags: [maritime, lng, inventory-routing, tactical-planning]
relationships:
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: derived_from
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: related_to
sources:
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive.md
summary: >-
  Tactical LNG planning framework that jointly optimizes production-linked inventory and vessel delivery schedules under contract constraints over an annual horizon.
provenance:
  extracted: 0.82
  inferred: 0.15
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:52:03Z
updated: 2026-10-22T09:52:03Z
---

# Annual LNG Delivery Program (ADP)

Annual Delivery Program (ADP) is a tactical planning problem for LNG suppliers that couples maritime routing with production, storage, and contract satisfaction decisions.

## Key Ideas

- Planning horizon is long (roughly one year), with periodic shipment decisions.
- Decisions must respect vessel availability, maintenance windows, berth capacity, and customer contract terms.
- Inventory-production balance at loading terminals is tightly coupled to routing feasibility.
- Split-delivery policies can improve total cost when demand/capacity patterns are imbalanced.
- Heuristic routing layers can be materially more practical than pure exact MIP on realistic large instances.

ADP is a load-bearing bridge between strategic network design and short-horizon operational replanning in LNG supply chains. ^[inferred]

Related pages: [[references/mutlu2016-lng-annual-delivery-program]], [[concepts/maritime-routing-under-uncertainty]], [[references/ksciuk2023-maritime-uncertainty-review]], [[_papers/andersson2017creating/andersson2017creating-extracted]].

## Open Questions

- Which uncertainty structures (demand, weather, spot market price) should be integrated directly into annual ADP optimization?
- How should ADP plans be re-optimized in rolling horizons without destabilizing contractual commitments? ^[inferred]

## Sources

- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md]]
- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive.md]]
