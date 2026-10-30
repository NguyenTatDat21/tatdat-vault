---
title: Utility and fairness threshold schemes
summary: "Utility/fairness threshold SWFs combine utilitarian with maximin/leximax: Δ parameter, efficiency threshold, fairness threshold, hooker-wills, Elçi, groups, MILP/LP."
tags: [fairness, optimization, thresholds]
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0
base_confidence: 0.67
tier: supporting
category: concepts
created: 2026-10-29T17:37:00Z
updated: 2026-10-30T14:08:41Z
sources:
- _papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md
relationships:
  - target: references/xinyingchen2023guide
    type: related_to
  - target: concepts/maximin-leximax-fairness
    type: related_to
  - target: concepts/sequential-leximax-threshold-models
    type: related_to
  - target: concepts/welfare-social-function-fairness-formulations
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T17:37:00Z
---

> [!tldr] Utility and fairness threshold schemes.

## Key claims
- Δ parameter easier than α, groups of different sizes, no axiomatic/bargaining justification, inherit maximin limitations; Hooker & Williams 2012 n-person efficiency-threshold MILP polyhedral healthcare, Elçi et al. 2022 fairness-threshold LP; parties within Δ of worst-off priority, parties >Δ above lowest no benefit. ^[inferred]
- 2-person efficiency-threshold SWF: `u_1+u_2` if |u_1−u_2|≥Δ, `2min{u_1,u_2}+Δ` otherwise, Fig. 2, continuity; hooker-wills `W(u)=(n−1)Δ+Σmax{u_i−Δ,u_min}` eq. 13, fair region u_i−u_min≤Δ, Δ=0 utilitarian/∞ maximin, groups `W^g=(Σs_i−1)Δ+Σs_i max{u_i−Δ,u_min}` eq. 14, Gerdessen et al. 2018 Pareto frontier. ^[inferred]
- Fairness-threshold 2-person SWF `2min+Δ` if |u1−u2|≥Δ, `u1+u2` otherwise, Fig. 3, utilitarian open dot, welfare-maximizing black dot, Elçi `W(u)=nΔ+Σmin{u_i−Δ,u_min}` eq. 15, groups `W^g=(Σs_i)Δ+Σs_i min{u_i−Δ,u_min}` eq. 16, equate solutions with very different fairness. ^[inferred]

## Related
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — source.
- [[concepts/maximin-leximax-fairness]] — threshold criteria inherit maximin limitations.
- [[concepts/sequential-leximax-threshold-models]] — leximax threshold, sequential SWFs.
- [[references/ogryczak2014-fair-optimization-networks-survey]] — inequality-averse fair optimization.

## Sources

- `_papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md`
