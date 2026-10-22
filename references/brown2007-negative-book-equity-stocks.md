---
title: Going Negative — What to Do with Negative Book Equity Stocks
category: references
tags: [asset-pricing, value-factor, negative-book-equity, style-classification]
relationships:
  - target: "[[concepts/negative-book-equity-style-classification]]"
    type: derived_from
  - target: "[[references/ball2016-accruals-cash-flows-operating-profitability]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
sources:
  - _papers/brown2007going/brown2007going-extracted.md
  - _papers/brown2007going/brown2007going.md
summary: >-
  Shows that excluding negative-book-equity stocks from value-growth sorting loses systematic return information, and proposes returns-based style classification to reintegrate them.
provenance:
  extracted: 0.88
  inferred: 0.1
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T21:10:00Z
updated: 2026-10-22T21:10:00Z
---

# Going Negative — What to Do with Negative Book Equity Stocks

> [!tldr] Negative book-equity stocks are economically meaningful in value-growth spreads; dropping them understates HML-like premiums.

## Problem & Motivation

Traditional Fama-French value sorting excludes firms with negative book equity (BE), even though these firms increasingly appear in public markets. The paper tests whether this exclusion biases style-factor construction and return estimates.

## Method / Architecture

The authors assign negative-BE firms to value-growth buckets using a generalized style classification based on return covariances with benchmark value-growth portfolios.

Fama-French HML baseline:

$$
HML_t = \frac{1}{2}(R_{SH,t}+R_{BH,t}) - \frac{1}{2}(R_{SL,t}+R_{BL,t})
$$

Then they compare HML series with and without negative-BE stocks by financial/non-financial segmentation and weighting choices.

## Results

| Finding | Reported effect |
|---|---|
| Frequency of negative-BE firms | ~3.5% to ~5.7% of listed firms in sample periods |
| Value-weight footprint | Around 0.8% to 1.6% of market capitalization |
| HML impact including negative-BE firms | About +0.9% to +1.1% annualized mean increase |
| Cumulative effect | Material long-horizon spread differences (roughly high-teens percentages) |

## Interpretation

- Negative-BE stocks are not merely noise; they systematically tilt style-factor returns.
- Portfolio construction rules that discard them can miss priced variation in distress/growth transitions. ^[inferred]

## Related

- [[concepts/negative-book-equity-style-classification]]
- [[references/ball2016-accruals-cash-flows-operating-profitability]]
- [[concepts/cash-based-operating-profitability]]
- [[concepts/ordering-information-portfolio-selection]]

## Open Questions

- Do modern accounting standards and intangibles-heavy balance sheets amplify this effect out of sample?
- How stable is style assignment for negative-BE firms during regime shifts? ^[inferred]

## Sources

- [[_papers/brown2007going/brown2007going-extracted.md]]
- [[_papers/brown2007going/brown2007going.md]]
