---
title: Predictive-to-Prescriptive Analytics
category: concepts
tags: [prescriptive-analytics, decision-optimization, machine-learning, robustness]
relationships:
  - target: "[[references/bertsimas2020-predictive-to-prescriptive-analytics]]"
    type: derived_from
  - target: "[[references/bertsimas2022-bootstrap-robust-prescriptive-analytics]]"
    type: extends
  - target: "[[concepts/ordering-information-portfolio-selection]]"
    type: related_to
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: related_to
  - target: "[[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]]"
    type: related_to
    note: "Reciprocal - concepts/ratio-mean-reversion-and-continuing-value-benchmarks references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/residual-earnings-equity-valuation]]"
    type: related_to
    note: "Reciprocal - concepts/residual-earnings-equity-valuation references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/statistical-investigation-lifecycle]]"
    type: related_to
    note: "Reciprocal - concepts/statistical-investigation-lifecycle references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: related_to
    note: "Reciprocal - references/nissim2001-ratio-analysis-equity-valuation references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/bertsimas2020predictive/bertsimas2020predictive-extracted.md
  - _papers/bertsimas2020predictive/bertsimas2020predictive.md
  - _papers/bertsimas2022bootstrap/bertsimas2022bootstrap-extracted.md
  - _papers/bertsimas2022bootstrap/bertsimas2022bootstrap.md
summary: >-
  Framework that uses contextual features to optimize decisions directly and evaluates value against data-poor baselines, with optional bootstrap-based robustness.
provenance:
  extracted: 0.87
  inferred: 0.11
  ambiguous: 0.02
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T20:40:00Z
updated: 2026-10-30T14:38:55Z
---

# Predictive-to-Prescriptive Analytics

Predictive-to-prescriptive analytics turns contextual data into optimization decisions instead of stopping at forecasts.

## Key Ideas

- Replace unconditional stochastic objectives with context-conditioned decision objectives.
- Learn local structure from historical $(x,y)$ data and optimize decision $z(x)$ directly.
- Evaluate incremental decision value with the **coefficient of prescriptiveness** relative to data-poor baselines.
- Add bootstrap/distributional robustness when finite-sample overfitting risk is material.

## Why It Matters

- Connects machine learning signals to operational decisions in one loop.
- Supports practical decisions where demand/returns depend on rich covariates.
- Provides a clearer benchmark of decision quality than prediction error alone. ^[inferred]

## Related

- [[references/bertsimas2020-predictive-to-prescriptive-analytics]]
- [[references/bertsimas2022-bootstrap-robust-prescriptive-analytics]]
- [[concepts/ordering-information-portfolio-selection]]
- [[concepts/adaptive-large-neighborhood-search-for-mip]]
- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — the ratio hierarchy that turns forecasts into valuation inputs

## Open Questions

- How should practitioners set robustness level to balance conservatism and realized value?
- Which feature and model governance checks are sufficient when prescriptions drive high-cost actions? ^[inferred]

## Sources

- [[_papers/bertsimas2020predictive/bertsimas2020predictive-extracted.md]]
- [[_papers/bertsimas2020predictive/bertsimas2020predictive.md]]
- [[_papers/bertsimas2022bootstrap/bertsimas2022bootstrap-extracted.md]]
- [[_papers/bertsimas2022bootstrap/bertsimas2022bootstrap.md]]
