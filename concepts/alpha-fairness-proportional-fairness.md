---
title: Alpha fairness and proportional fairness
summary: "Alpha fairness family W_α, α=0 utilitarian, α→∞ maximin; proportional fairness α=1 Nash product; bandwidth Kelly 1998, α≥1 anomaly, partition axiom."
tags: [fairness, optimization, alpha-fairness]
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T17:37:00Z
updated: 2026-10-30T14:38:55Z
sources:
- _papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md
relationships:
  - target: references/xinyingchen2023guide
    type: related_to
  - target: concepts/nash-bargaining-solution-axioms
    type: related_to
  - target: concepts/inequality-measures-fairness-formulations
    type: related_to
  - target: concepts/maximin-leximax-fairness
    type: related_to
  - target: "[[concepts/convex-combination-weights-fairness]]"
    type: related_to
  - target: "[[concepts/kalai-smorodinsky-bargaining-solution]]"
    type: related_to
  - target: "[[concepts/welfare-social-function-fairness-formulations]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T17:37:00Z
---

> [!tldr] Alpha fairness and proportional fairness.

## Key claims
- Alpha fairness Mo & Walrand 2000, Verloop et al. 2010 `W_α=(1/(1−α))Σu_i^{1−α}` α≥0, α≠1, `Σlog(u_i)` α=1; α=0 utilitarian, α→∞ maximin, Bertsimas et al. 2012 worst-case trade-offs, α interpretation u_j reduced by (u_j/u_i)^α compensating unit increase in u_i. ^[inferred]
- Lan & Chiang 2011 partition axiom eq. 12, Kolmogorov mean h, geometric/power mean, ratio-scale comparability Roberts 1980 φ_i=β_i u_i, Lan et al. 2010, unnormalized Theil/Atkinson logarithmic. ^[inferred]
- Proportional fairness α=1 product Πu_i vs log, Nash bargaining hyperrectangle volume Fig. 1a, bandwidth Kelly et al. 1998, Mazumdar et al. 1991; α anomaly α≥1 (1,1) vs (t,T), t=1/T α=1, t=(2−T^{1−α})^{1/(1−α)} α>1, T^{1−α}<2, α<1 no anomaly. ^[inferred]

## Related
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — source.
- [[concepts/nash-bargaining-solution-axioms]] — α=1 proportional fairness Nash bargaining.
- [[references/ogryczak2014-fair-optimization-networks-survey]] — alpha fairness, fair dominance, survey.
- [[concepts/maximin-leximax-fairness]] — alpha continuum utilitarian→maximin.

## Sources

- `_papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md`
