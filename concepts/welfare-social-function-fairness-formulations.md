---
title: Welfare social function fairness formulations
summary: "Welfare social function models for fairness in optimization: welfare maximizing, welfare constraining, utilities u=U(x), linear/nonlinear/MILP, triage, mortgage."
tags: [fairness, optimization]
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T17:37:00Z
updated: 2026-10-30T17:41:00Z
sources:
- _papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md
relationships:
  - target: references/xinyingchen2023guide
    type: related_to
  - target: concepts/maximin-leximax-fairness
    type: related_to
  - target: concepts/utility-fairness-thresholds
    type: related_to
  - target: concepts/alpha-fairness-proportional-fairness
    type: related_to
  - target: "[[concepts/convex-combination-weights-fairness]]"
    type: related_to
  - target: "[[concepts/group-parity-fairness-metrics]]"
    type: related_to
  - target: "[[concepts/inequality-measures-fairness-formulations]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T17:37:00Z
---

> [!tldr] Welfare social function fairness formulations.

## Key claims
- Welfare maximizing models eq. 1 `max{W(u) | u=U(x), x∈S_x}` and eq. 3 `max{W(u) | (u,x)∈S}`, utility vector u=U(x), welfare social function W trades off utilities. ^[inferred]
- Welfare constraining models eq. 2 `max{f(x) | W(u)≥LB, u=U(x), x∈S_x}` and eq. 4 `max{f(x) | W(u)≥LB, (u,x)∈S}`, minimum fairness lower bound, triage budget B, utilities a_i+b_i x_i QALYs. ^[inferred]
- Mortgage approval `min ΣR_i(x_i)`, `u_i=p_i x_i`, 0/1 decisions, upper bounds x_i≤a_i; advantages: welfare maximizing regulates efficiency-fairness tradeoff, welfare constraining when no suitable SWF. ^[inferred]

## Related
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — source.
- [[concepts/maximin-leximax-fairness]] — maximin/leximax as SWF choices.
- [[concepts/utility-fairness-thresholds]] — threshold SWFs as welfare constraints.
- [[concepts/alpha-fairness-proportional-fairness]] — alpha fairness, convex-combination SWFs.

## Sources

- `_papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md`
