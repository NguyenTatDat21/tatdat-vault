---
title: Inequality measures as fairness formulations
summary: "Inequality fairness SWFs for optimization models: relative range, relative mean deviation, CV, Jain index, Gini, Hoover, Lorenz, linear fractional, Charnes-Cooper, MILP."
tags: [fairness, optimization]
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T17:37:00Z
updated: 2026-10-30T18:52:00Z
sources:
- _papers/xinyingchen2023guide/xinyingchen2023guide.md
relationships:
  - target: references/xinyingchen2023guide
    type: related_to
  - target: concepts/maximin-leximax-fairness
    type: related_to
  - target: concepts/alpha-fairness-proportional-fairness
    type: related_to
  - target: concepts/welfare-social-function-fairness-formulations
    type: related_to
  - target: "[[concepts/group-parity-fairness-metrics]]"
    type: related_to
lifecycle: draft
lifecycle_changed: 2026-10-29T17:37:00Z
---

> [!tldr] Inequality measures as fairness formulations.

## Key claims
- Relative range `W(u)=−(1/ū)(u_max−u_min)` with ū=(1/n)Σu_i, linear fractional Charnes & Cooper 1962; relative mean deviation `W(u)=−(1/ū)Σ|u_i−ū|` linearizable. ^[inferred]
- Coefficient of variation convex nonaffine; Jain index `W(u)=ū²((1/n)Σu_i²)⁻¹=1/(1+c_v²)`, 1 equality, 1/n perfect inequality, strictly monotone in CV, QoE fairness Georgopoulos 2013, Hoßfeld 2018, TCP fairness Pokhrel 2016, G, Bossaert Mehta 2020. ^[inferred]
- Gini `G(u)=(1/2ūn²)ΣΣ|u_i−u_j|`, Lorenz, linear fractional; Hoover `W(u)=−(1/2nū)Σ|u_i−ū|` proportional to relative mean deviation; metrics measure relative not absolute levels, relative range outliers. ^[inferred]

## Related
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — source.
- [[concepts/maximin-leximax-fairness]] — maximin family complements inequality measures.
- [[concepts/alpha-fairness-proportional-fairness]] — Jain, unnormalized Theil/Atkinson logarithmic.
- [[references/ogryczak2014-fair-optimization-networks-survey]] — inequality-averse fair optimization survey.

## Sources

- `_papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md`
