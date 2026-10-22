---
title: >-
  Ordering-Information Portfolio Selection
category: concepts
tags: [portfolio-optimization, decision-theory, risk, preference-modeling]
relationships:
  - target: "[[references/almgren2004-optimal-portfolios-ordering-information]]"
    type: derived_from
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: related_to
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
sources:
  - _papers/almgren2004optimal/almgren2004optimal-extracted.md
  - _papers/almgren2004optimal/almgren2004optimal.md
summary: >-
  Portfolio-construction paradigm that uses ranking beliefs about expected returns, rather than precise return forecasts, while retaining explicit risk controls.
provenance:
  extracted: 0.84
  inferred: 0.13
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T19:23:44Z
updated: 2026-10-22T19:23:44Z
---

# Ordering-Information Portfolio Selection

Ordering-information portfolio selection replaces point estimates of expected returns with ordinal beliefs (which assets are likely better than others), then optimizes portfolios under risk constraints.

## Key Ideas

- Investor beliefs are expressed as linear inequality relations over expected returns.
- Preference between portfolios is defined geometrically via feasible return cones/half-spaces.
- Efficient portfolios are selected by maximizing this preference relation subject to covariance-based risk control.
- The framework recovers classical mean-variance behavior when full return vectors are known.

## Why It Matters

- In practice, relative rankings may be more stable than absolute expected-return forecasts.
- The method offers a bridge between strict Markowitz assumptions and rank/characteristic-driven investment workflows.
- Similar "optimize under partial information" structure appears in other planning domains. ^[inferred]

## Related

- [[references/almgren2004-optimal-portfolios-ordering-information]]
- [[concepts/annual-lng-delivery-program]]
- [[concepts/set-orienteering-problem]]

## Open Questions

- How robust is performance under noisy or conflicting rank signals across sectors?
- What is the best way to combine ordering-belief models with transaction-cost-aware rebalancing? ^[inferred]

## Sources

- [[_papers/almgren2004optimal/almgren2004optimal-extracted.md]]
- [[_papers/almgren2004optimal/almgren2004optimal.md]]
