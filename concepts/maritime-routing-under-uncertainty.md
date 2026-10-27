---
title: Maritime Routing Under Uncertainty
category: concepts
tags: [maritime, uncertainty, routing, planning]
relationships:
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: derived_from
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: extends
  - target: "[[references/christiansen2020-liner-shipping-network-design]]"
    type: related_to
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
sources:
  - _papers/ksciuk2023uncertainty/ksciuk2023uncertainty-extracted.md
  - _papers/christiansen2013ship/christiansen2013ship-extracted.md
  - _papers/christiansen2020liner/christiansen2020liner-extracted.md
  - _papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md
summary: >-
  A planning-level concept for uncertainty in maritime routing, spanning demand, travel time, fuel and disruption risk, plus robust and rolling-horizon mitigation strategies.
provenance:
  extracted: 0.82
  inferred: 0.15
  ambiguous: 0.03
base_confidence: 0.97
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:12:13Z
updated: 2026-10-27T06:00:00Z
---

# Maritime Routing Under Uncertainty

Maritime routing and scheduling are uncertainty-sensitive across planning horizons, but uncertainty sources and control levers differ by decision level.

## Key Ideas

- **Strategic uncertainty**: long-horizon demand shifts, fleet/technology transitions, and network design assumptions.
- **Tactical uncertainty**: schedule reliability, inventory-routing feasibility, speed/bunkering policy, and transshipment delays.
- **Operational uncertainty**: weather, port congestion, disruptions, and short-horizon network imbalance.
- In practice, robust buffers, decomposition, and rolling-horizon replanning are often preferred over fully stochastic monoliths when deployment constraints dominate. ^[inferred]
- In maritime inventory routing specifically, uncertainty modeling is still in its infancy: the 2013–2023 survey counts few stochastic MIRP studies and calls for a standardized instance set plus an open-source simulation framework to compare stochastic policies — see [[references/fagerholt2023-maritime-inventory-routing-survey]].

The central tension is realism vs deployability: richer stochastic models can improve policy quality, but adoption depends on data quality, computation time, and planner trust.

## Maritime Context Signals

| Signal | Practical implication |
|---|---|
| Frequent disruptions and weather effects | Plans require recourse and slack mechanisms |
| High transshipment and schedule coupling | Uncertainty propagates across service network layers |
| Inventory-linked shipping (e.g., LNG/MIRP) | Routing errors create stockout/overflow risk, not just delay |

## Open Questions

- Which uncertainty representations are most robust under sparse historical maritime data?
- How should robust/stochastic plans be blended with rolling-horizon replanning in production systems? ^[inferred]
- Which uncertainty components should be priced directly in network-design objectives versus handled as operational recourse? ^[inferred]

## Related

- [[references/ksciuk2023-maritime-uncertainty-review]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/christiansen2020-liner-shipping-network-design]]
- [[concepts/maritime-inventory-routing-problem]]
- [[references/fagerholt2023-maritime-inventory-routing-survey]]
- [[concepts/mirp-modeling-continuous-vs-discrete-time]]
- [[concepts/liner-shipping-network-design]]

## Sources

- [[_papers/ksciuk2023uncertainty/ksciuk2023uncertainty-extracted.md]]
- [[_papers/christiansen2013ship/christiansen2013ship-extracted.md]]
- [[_papers/christiansen2020liner/christiansen2020liner-extracted.md]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted.md]]
- [[_papers/fagerholt2023maritime/images/page_22_image_2.jpg]]
