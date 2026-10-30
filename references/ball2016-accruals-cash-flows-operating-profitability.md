---
title: Accruals, cash flows, and operating profitability in the cross section of stock returns
category: references
tags: [asset-pricing, accruals, profitability, empirical-finance]
relationships:
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: derived_from
  - target: "[[concepts/ordering-information-portfolio-selection]]"
    type: related_to
  - target: "[[references/almgren2004-optimal-portfolios-ordering-information]]"
    type: related_to
  - target: "[[references/beatty2014-financial-accounting-in-banking]]"
    type: related_to
  - target: "[[references/pincus2007-accrual-anomaly-international-evidence]]"
    type: related_to
  - target: "[[concepts/gross-profitability-premium]]"
    type: related_to
  - target: "[[concepts/negative-book-equity-style-classification]]"
    type: related_to
  - target: "[[references/brown2007-negative-book-equity-stocks]]"
    type: related_to
  - target: "[[references/kakinuma2020-empirical-profitability-thailand]]"
    type: related_to
  - target: "[[references/kim2020-profitability-asean-stocks]]"
    type: related_to
  - target: "[[references/novy-marx2013-other-side-of-value]]"
    type: related_to
sources:
  - _papers/ball2016accruals/ball2016accruals-extracted.md
  - _papers/ball2016accruals/ball2016accruals.md
summary: >-
  Shows cash-based operating profitability predicts stock returns better than accrual-inclusive profitability and largely subsumes the accrual anomaly in cross-sectional tests.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T19:33:55Z
updated: 2026-10-30T14:38:55Z
---

# Accruals, cash flows, and operating profitability in the cross section of stock returns

> [!tldr] Cash-based operating profitability (CbOP) carries stronger return-prediction signal than accrual-inclusive profitability, and makes standalone accruals weak in joint tests.

## Problem & Motivation

Prior asset-pricing anomalies suggested that expected returns increase with profitability and decrease with accruals — the profitability leg is the gross-profitability premium of [[references/novy-marx2013-other-side-of-value|Novy-Marx 2013]]. This paper tests whether accruals add information once profitability is measured on a cash basis.

## Method / Architecture

The paper runs cross-sectional return tests using profitability, accruals, and cash-based profitability variants, with long-horizon US equity data.

## Key Equations

$$
r_{i,t+1} = \alpha + \beta_1 OP_{i,t} + \beta_2 ACC_{i,t} + \varepsilon_{i,t+1}
$$

$$
r_{i,t+1} = \alpha + \beta_1 CbOP_{i,t} + \beta_2 ACC_{i,t} + \varepsilon_{i,t+1}
$$

Regression forms summarize the empirical specification family described in the extracted text. ^[inferred]

## Results

| Signal test | Reported statistic |
|---|---|
| OP alone (cross-section) | t-value 7.04 |
| Accruals alone | t-value -3.90 |
| CbOP alone | t-value 9.69 |
| CbOP + accruals joint test | CbOP t-value 7.40; accruals t-value 0.34 |
| Portfolio implication | Annualized Sharpe ratio of the profitability strategy increases by almost 40% (t-value 4.6) when moving from accruals-based OP to CbOP; in opportunity-set tests, CbOP alone beats adding both accruals and OP factors (1.67 vs 1.54) |

## Limitations

- Evidence is estimated from historical market data and model choices; out-of-sample stability is not guaranteed.
- Reported effects depend on accounting definitions and sample construction choices. ^[inferred]

## Related

- [[concepts/cash-based-operating-profitability]]
- [[concepts/ordering-information-portfolio-selection]]
- [[references/almgren2004-optimal-portfolios-ordering-information]]
- [[references/beatty2014-financial-accounting-in-banking]] — same accrual-versus-cash valuation question in a regulated bank setting: Beatty/Harris/Holthausen/Zull (2014) shows loan-loss reporting lets managers manage earnings via loan-loss provisions and general reserves, so bank accruals carry information beyond cash flows, exactly the accruals-versus-cash-flows valuation gap CbOP exploits for stocks.
- [[references/pincus2007-accrual-anomaly-international-evidence]] — pincus2007 tests the accrual-versus-cash valuation gap in 20 countries: adding OCF deciles subsumes the accrual coefficient exactly in the four anomaly countries, the same subsumption ball2016 documents for CbOP in the US.

## Sources

- [[_papers/ball2016accruals/ball2016accruals-extracted.md]]
- [[_papers/ball2016accruals/ball2016accruals.md]]
