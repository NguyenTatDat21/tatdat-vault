---
title: >-
  Maritime Routing Under Uncertainty
category: concepts
tags: [maritime, uncertainty, routing, planning]
relationships:
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: derived_from
  - target: "[[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted]]"
    type: related_to
  - target: "[[_papers/christiansen2013ship/christiansen2013ship-extracted]]"
    type: related_to
sources:
  - _papers/ksciuk2023uncertainty/ksciuk2023uncertainty-extracted.md
  - _papers/ksciuk2023uncertainty/ksciuk2023uncertainty.md
summary: >-
  A planning-level view of uncertainty in maritime routing and scheduling, emphasizing demand/travel-time/fuel volatility and practical mitigation patterns in industry.
provenance:
  extracted: 0.78
  inferred: 0.19
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:12:13Z
updated: 2026-10-22T09:12:13Z
---

# Maritime Routing Under Uncertainty

Maritime routing and scheduling decisions are uncertainty-sensitive across all planning horizons, but the uncertainty type and control levers differ by level.

## Key Ideas

- Strategic uncertainty often appears in demand and technology-transition assumptions.
- Tactical uncertainty strongly affects vessel schedules, inventory-routing plans, and bunker policies.
- Operational uncertainty appears in weather, disruptions, and short-horizon network imbalance (e.g., empty repositioning).
- Practice often relies on buffers and decomposition when full stochastic optimization is hard to deploy.

The central tension is between model realism and deployability: richer stochastic models can improve policy quality, but operational adoption depends on data pipelines and planner trust. ^[inferred]

Related pages: [[references/ksciuk2023-maritime-uncertainty-review]], [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted]], [[_papers/christiansen2013ship/christiansen2013ship-extracted]], [[_papers/gronhaug2010branchandprice/gronhaug2010branchandprice-extracted]].

## Open Questions

- Which uncertainty representations are most robust under sparse historical maritime data?
- How should robust/stochastic plans be blended with rolling-horizon replanning in production systems? ^[inferred]

## Sources

- [[_papers/ksciuk2023uncertainty/ksciuk2023uncertainty-extracted.md]]
- [[_papers/ksciuk2023uncertainty/ksciuk2023uncertainty.md]]
