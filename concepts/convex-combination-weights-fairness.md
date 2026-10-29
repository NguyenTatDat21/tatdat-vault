---
title: Convex combination weights for fairness
summary: "Convex combination SWFs, λ interpretation, product SWF λ=1/2, Gini μ/(1+μ), decreasing weights, dominance constraints, elicitation, utilitarian↔maximin."
tags: fairness, optimization, convex-combination
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0
base_confidence: 0.67
tier: core
created: 2026-10-29T17:37:00Z
updated: 2026-10-29T17:37:00Z
sources:
- _papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md
relationships:
- {target: "references/xinyingchen2023guide", type: "related_to"}
- {target: "concepts/alpha-fairness-proportional-fairness", type: "related_to"}
- {target: "concepts/maximin-leximax-fairness", type: "related_to"}
- {target: "concepts/welfare-social-function-fairness-formulations", type: "related_to"}
lifecycle: draft
lifecycle_changed: 2026-10-29T17:37:00Z
---

> [!tldr] Convex combination weights for fairness.

## Key claims
- Convex combinations `W(u)=(1−λ)Σu_i+λΦ(u)`, λ interpretation problem; Eisenhandler & Tzur 2019 `Σu_i−(1/n)Σ_{i<j}|u_j−u_i|` λ=1/2, Mostajabdaveh et al. 2019 `Σu_i+μ(1−G)Σu_i`, λ=μ/(1+μ); convex-combo maximin eq. 10, decreasing weights eq. 11. ^[inferred]
- Multi-criteria Yager 1997, Ogryczak & Śliwiński 2003, Hu & Chen 2020 ML classifier correspondence, stakeholder elicitation Gralla 2014, Carland 2018, Yilmaz & Kabak 2020, Hasnain 2021; Argyris et al. 2022 welfare-based dominance constraints MILP, weighted ordered averages continuum utilitarian↔maximin, Rea et al. 2021 request-vs-allocation deviations. ^[inferred]

## Related
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — source.
- [[concepts/alpha-fairness-proportional-fairness]] — alpha fairness, convex-combination continuum.
- [[concepts/maximin-leximax-fairness]] — convex-combo maximin eq. 10, leximax remedy.
- [[concepts/welfare-social-function-fairness-formulations]] — convex-combination SWFs as models.