---
title: Sequential leximax threshold models
summary: "Sequential leximax threshold SWFs: Chen & Hooker 2022 W_k sequence, fair-region weight, kidney exchange, valid inequalities, healthcare, earthquake shelter."
tags: [fairness, optimization, leximax]
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
  - target: concepts/utility-fairness-thresholds
    type: related_to
  - target: concepts/maximin-leximax-fairness
    type: related_to
  - target: concepts/leximax-leximin-fairness-principles
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T17:37:00Z
---

> [!tldr] Sequential leximax threshold models.

## Key claims
- Maximin threshold ignores disadvantaged other than worst-off, constraint-set cap; McElfresh & Dickerson 2020 kidney exchange preference ordering, fair region max−min≤Δ, eq. 17 `W=n u_1` if all |u_i−u_j|≤Δ, `Σu_i+sgn(u_1−u_i)Δ` otherwise; continuity claim false n>2 counterexample W(0,0,Δ+ε)=ε, W(0,ε,Δ+ε)=2ε−Δ. ^[inferred]
- Chen & Hooker 2022 sequence `W_1=` Hooker-Wills, `W_k=Σ_{i=1}^{k-1}(n−i+1)u_⟨i⟩+(n−k+1)min{u_⟨1⟩+Δ,u_⟨k⟩}+Σ_{i=k}^n(u_⟨i⟩−u_⟨1⟩−Δ)^+ k=2..n`, γ^+=max{0,γ}, u_⟨i⟩ nondecreasing; fair-region weight = number with same/greater utility, utilitarian unit weight, value independence continuity, socially optimal u*_⟨i⟩, valid inequalities, healthcare, earthquake shelter seconds for Δ. ^[inferred]

## Related
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — source.
- [[concepts/utility-fairness-thresholds]] — threshold criteria, continuity, Fig. 2-3.
- [[concepts/maximin-leximax-fairness]] — maximin/leximax, leximax threshold.
- [[concepts/leximax-leximin-fairness-principles]] — lexicographic maximin, leximax principles.

## Sources

- `_papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md`
