---
title: From Predictive to Prescriptive Analytics
category: references
tags: [prescriptive-analytics, machine-learning, stochastic-optimization, data-driven-decision]
relationships:
  - target: "[[concepts/predictive-to-prescriptive-analytics]]"
    type: derived_from
  - target: "[[references/bertsimas2022-bootstrap-robust-prescriptive-analytics]]"
    type: extends
  - target: "[[concepts/ordering-information-portfolio-selection]]"
    type: related_to
  - target: "[[concepts/inverse-soft-q-imitation-learning]]"
    type: related_to
    note: "Reciprocal - concepts/inverse-soft-q-imitation-learning references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/statistical-investigation-lifecycle]]"
    type: related_to
    note: "Reciprocal - concepts/statistical-investigation-lifecycle references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/chatfield1995-problem-solving-statisticians-guide]]"
    type: related_to
    note: "Reciprocal - references/chatfield1995-problem-solving-statisticians-guide references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/garg2022-iq-learn-inverse-soft-q]]"
    type: related_to
    note: "Reciprocal - references/garg2022-iq-learn-inverse-soft-q references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/bertsimas2020predictive/bertsimas2020predictive-extracted.md
  - _papers/bertsimas2020predictive/bertsimas2020predictive.md
summary: >-
  Introduces a contextual decision framework that converts predictive features into optimized prescriptions and evaluates value with the coefficient of prescriptiveness.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T20:40:00Z
updated: 2026-10-30T14:38:55Z
---

# From Predictive to Prescriptive Analytics

> [!tldr] Reframes ML outputs as inputs to optimization, producing decisions directly from contextual data instead of separating forecasting and optimization.

## Problem & Motivation

Classical stochastic optimization ignores contextual covariates $X$, while pure prediction does not optimize downstream decisions. The paper builds a bridge: use data-rich prediction structure to make context-conditioned prescriptions.

## Method / Architecture

The approach learns local decision rules from historical pairs $(x^i, y^i)$ and solves a weighted optimization per query context $x$.

```mermaid
flowchart LR
  A[Historical data (x,y)] --> B[Local weighting model]
  B --> C[Context-conditioned objective]
  C --> D[Optimization over feasible decisions]
  D --> E[Prescriptive decision z(x)]
  E --> F[Out-of-sample performance + prescriptiveness P]
```

## Key Equations

Classical and contextual targets:

$$
v^{\text{stoch}} = \min_{z\in\mathcal{Z}} \mathbb{E}[c(z;Y)]
$$

$$
v^*(x)=\min_{z\in\mathcal{Z}} \mathbb{E}[c(z;Y)\mid X=x]
$$

Predictive prescription:

$$
\hat z_N(x) \in \arg\min_{z\in\mathcal{Z}} \sum_{i=1}^{N} w_{N,i}(x)c(z;y^i)
$$

Coefficient of prescriptiveness:

$$
P = 1 - \frac{\hat R_{N_v}(\hat z_N)-\hat R^*_{N_v}}{\hat R_{N_v}(z_N^{\mathrm{SAA}})-\hat R^*_{N_v}}
$$

## Results

| Setting | Result |
|---|---|
| Synthetic decision settings | Local-learning prescriptions outperform data-poor baselines once sample size is sufficient |
| Theoretical guarantees | Theorems 5–10 prove asymptotic optimality/consistency for kNN, kernel, recursive kernel, LOESS, local linear, and nonnegative local linear regression; the abstract names LOESS, CART, and random forests as asymptotically optimal under mild conditions |
| Real inventory case | Reported out-of-sample $P = 0.88$, i.e., 88% of the gap to perfect foresight closed |

## Limitations

- Gains depend strongly on quality and relevance of contextual features.
- Assumption sets for asymptotic optimality may be hard to verify in production pipelines. ^[inferred]
- Real-world result is from one operational context; transportability across industries is not guaranteed. ^[inferred]

## Related

- [[concepts/predictive-to-prescriptive-analytics]]
- [[references/bertsimas2022-bootstrap-robust-prescriptive-analytics]]
- [[concepts/ordering-information-portfolio-selection]]
- [[concepts/adaptive-large-neighborhood-search-for-mip]]

## Sources

- [[_papers/bertsimas2020predictive/bertsimas2020predictive-extracted.md]]
- [[_papers/bertsimas2020predictive/bertsimas2020predictive.md]]
