---
title: >-
  Annual LNG Delivery Program (ADP)
category: concepts
tags: [maritime, lng, inventory-routing, tactical-planning]
relationships:
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: derived_from
  - target: "[[references/al-haidous2016-optimal-lng-deliveries]]"
    type: extends
  - target: "[[references/andersson2017-creating-annual-lng-delivery-programs]]"
    type: extends
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
sources:
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive.md
  - _papers/al-haidous2016optimal/al-haidous2016optimal-extracted.md
  - _papers/al-haidous2016optimal/al-haidous2016optimal.md
  - _papers/andersson2017creating/andersson2017creating-extracted.md
  - _papers/andersson2017creating/andersson2017creating.md
summary: >-
  Tactical LNG planning problem that coordinates inventory, vessel schedules, contract obligations, and optional spot-market actions over annual horizons.
provenance:
  extracted: 0.85
  inferred: 0.13
  ambiguous: 0.02
base_confidence: 0.90
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:52:03Z
updated: 2026-10-22T19:23:44Z
---

# Annual LNG Delivery Program (ADP)

Annual Delivery Program (ADP) is a tactical planning problem for LNG suppliers that couples maritime routing with production, storage, and contract satisfaction decisions.

## Key Ideas

- Planning horizon is long (roughly one year), with periodic shipment decisions.
- Decisions must respect vessel availability, maintenance windows, berth capacity, and customer contract terms.
- Inventory-production balance at loading terminals is tightly coupled to routing feasibility.
- Al-Haidous et al. formulate ADP with a compact arc-flow MIP that minimizes required fleet size while preserving operational detail.
- Andersson et al. extend the annual LNG setup with explicit spot-market economics and branch-and-cut valid inequalities that tighten the model.

ADP is a load-bearing bridge between strategic network design and short-horizon operational replanning in LNG supply chains. ^[inferred]

## Related

- [[references/mutlu2016-lng-annual-delivery-program]]
- [[references/al-haidous2016-optimal-lng-deliveries]]
- [[references/andersson2017-creating-annual-lng-delivery-programs]]
- [[concepts/maritime-routing-under-uncertainty]]
- [[references/ksciuk2023-maritime-uncertainty-review]]

## Open Questions

- Which uncertainty structures (demand, weather, spot-market price) should be integrated directly into annual ADP optimization?
- How should ADP plans be re-optimized in rolling horizons without destabilizing contractual commitments? ^[inferred]

## Sources

- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md]]
- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive.md]]
- [[_papers/al-haidous2016optimal/al-haidous2016optimal-extracted.md]]
- [[_papers/al-haidous2016optimal/al-haidous2016optimal.md]]
- [[_papers/andersson2017creating/andersson2017creating-extracted.md]]
- [[_papers/andersson2017creating/andersson2017creating.md]]
