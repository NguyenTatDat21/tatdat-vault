---
title: "Empirical Profitability Anomalies in Thailand"
category: references
tags: [asset-pricing, profitability, emerging-markets, thailand, famamacbeth, carhart]
relationships:
  - target: "[[concepts/fama-macbeth-two-stage-cross-sectional-regression]]"
    type: derived_from
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: derived_from
  - target: "[[references/ball2016-accruals-cash-flows-operating-profitability]]"
    type: related_to
  - target: "[[references/fama1973-risk-return-equilibrium-empirical-tests]]"
    type: related_to
  - target: "[[concepts/gross-profitability-premium]]"
    type: uses
sources:
  - _papers/kakinuma2020empirical/kakinuma2020empirical-extracted.md
  - _papers/kakinuma2020empirical/kakinuma2020empirical.md
  - _papers/kakinuma2020empirical/images/page_9_chart_2.jpg
summary: >-
  In Thailand 2002-2019 gross profit and cash-flow-to-price profitability predict returns; top quintiles beat the market Sharpe, operating income alone does not.
provenance:
  extracted: 0.80
  inferred: 0.13
  ambiguous: 0.07
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-25T11:47:49Z
updated: 2026-10-30T14:39:22Z
---

# Empirical Profitability Anomalies in Thailand

> [!tldr] Kakinuma tests three profitability measures on 17 years of Thai stocks: gross profit (GP) and cash flow over market cap (C/P) predict future returns with robust high-quintile performance, while operating income (OP) is less reliable.

## Problem & Contribution

- Stock Exchange of Thailand, June 2002 - June 2019 (17 years), Datastream; the longest emerging-market profitability window claimed in the paper, where "the market is not fully efficient".
- Three measures: GP = gross profit / total assets, OP = operating income / total assets, FCF = C/P = annual cash flow from operating activities / market capitalization.
- Accounting data of year t-1 is matched to returns from June t to June t+1, the Ball et al. cash-flow alignment, so accounting reflects cash already earned before the return period. ^[inferred]
- Exclusions: ICB financial firms (real estate kept), REITs/property funds, bottom 3% market cap, missing data; accounting ratios winsorized at 0.1%/99.9%.

## Method

$$R_{j,t} = \beta_0 + \beta' x + \beta_2 \mathrm{Ln}(ME) + \beta_3 \mathrm{Ln}(B/M) + \beta_4 r_{1,0} + \beta_5 r_{12,1} + \varepsilon_{j,t}$$

Fama-MacBeth cross-sectional regression per month (Eq. 1): regress monthly returns on each profitability measure plus size, book-to-market and past-return controls; average the coefficients over time.

$$R_{i,t} - R_{F,t} = \alpha_i + \beta_1(MKT_t - R_{F,t}) + \beta_2 SMB_t + \beta_3 HML_t + \beta_4 WML_t + \varepsilon_{i,t}$$

Carhart four-factor regression (Eq. 2) on quintile portfolios formed June t to June t+1; factors from the Ken French data library.

## Results

| Measure | FM coef (t-stat) | Carhart top-quintile alpha (t) | High−Low alpha (t) | Top-quintile annual return / Sharpe |
|---|---|---|---|---|
| GP | 0.399 (32.33) | 0.065 (8.29) | 0.074 (5.98) | 18.34% / 0.62 |
| OP | 0.324 (23.96) | 0.024 (2.46) | −0.015 (ns) | 18.69% / 0.48 |
| FCF (C/P) | 0.226 (7.75) | 0.071 (9.38) | 0.066 (6.01) | 25.41% / 0.61 |
| Market index | — | — | — | 10.80% / 0.32 |

- Top-quintile GP portfolio: max drawdown 17.06% vs 43.77% for the market; information ratio 1.68. FCF: IR 2.45, tracking error 46.17%.
- Trailing five-year Sharpe is never negative for GP and C/P portfolios; OP and the market go negative around the 2008 crisis.

![[_papers/kakinuma2020empirical/images/page_9_chart_2.jpg]]
*"Figure 1 Trailing Five-Year Trailing Sharpe Ratios" (verbatim).* The figure illustrates the trailing five-year Sharpe ratio for the highest quintile portfolios for each profitability measure reported in Table 4. The data is from June 2007 to June 2019.

## Limitations

- OP is significant in the Table 3 FM regressions but its quintile alphas in Table 4 are non-monotonic (quintile 3 peaks, top-bottom spread insignificant); the paper attributes the contradiction to extreme observations in the top/bottom quintiles. ^[ambiguous]
- Thailand's listing universe is dominated by microcaps; the paper notes the market is "small, immature, inefficient".
- Sharpe and information ratios ignore trading costs; GP dominance in Thailand mirrors US Novy-Marx/Ball et al. results, suggesting the cash-flow mechanism transfers across markets. ^[inferred]

## Related

- [[concepts/fama-macbeth-two-stage-cross-sectional-regression]]
- [[concepts/cash-based-operating-profitability]]
- [[references/ball2016-accruals-cash-flows-operating-profitability]]
- [[concepts/gross-profitability-premium]] — shares asset-pricing + profitability tags with this page

## Bibliographic Record

- Citation key: kakinuma2020empirical — Kakinuma, Yosuke, "Empirical Profitability Anomalies in Thailand", Journal of International Studies, 2020.
- DOI: 10.14254/2071-8330.2020/13-4/6 (in the extracted text; the Zotero sidecar has no DOI field).
- Canonical URL: https://ceeol.com (article id 978575, per sidecar).
- Companion metadata: [[_papers/kakinuma2020empirical/kakinuma2020empirical.md|kakinuma2020empirical metadata]]

## Sources

- [[_papers/kakinuma2020empirical/kakinuma2020empirical-extracted.md]]
- [[_papers/kakinuma2020empirical/kakinuma2020empirical.md]]
- [[_papers/kakinuma2020empirical/images/page_9_chart_2.jpg]]
