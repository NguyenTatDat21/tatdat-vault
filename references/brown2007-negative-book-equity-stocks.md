---
title: Going Negative — What to Do with Negative Book Equity Stocks
category: references
tags: [asset-pricing, factor-investing]
relationships:
  - target: "[[concepts/negative-book-equity-style-classification]]"
    type: derived_from
  - target: "[[references/ball2016-accruals-cash-flows-operating-profitability]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[references/beatty2014-financial-accounting-in-banking]]"
    type: related_to
  - target: "[[references/pincus2007-accrual-anomaly-international-evidence]]"
    type: related_to
  - target: "[[concepts/operating-and-financial-leverage-spreading]]"
    type: related_to
  - target: "[[references/novy-marx2013-other-side-of-value]]"
    type: related_to
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: related_to
sources:
  - _papers/brown2007going/brown2007going-extracted.md
  - _papers/brown2007going/brown2007going.md
  - _papers/brown2007going/images/page_5_chart_2.jpg
  - _papers/brown2007going/images/page_13_chart_3.jpg
summary: >-
  Shows that excluding negative-book-equity stocks from value-growth sorting loses systematic return information, and proposes returns-based style classification to reintegrate them.
provenance:
  extracted: 0.90
  inferred: 0.07
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T21:10:00Z
updated: 2026-10-30T17:41:00Z
---

# Going Negative — What to Do with Negative Book Equity Stocks

> [!tldr] Negative book-equity stocks are economically meaningful in value-growth spreads; dropping them understates HML-like premiums.

## Problem & Motivation

Traditional Fama-French value sorting excludes firms with negative book equity (BE), even though these firms increasingly appear in public markets: the number of negative-BE stocks stays below 100 until 1985 and rises sharply from 1986, reaching roughly 5% of all listed stocks. The paper tests whether this exclusion biases style-factor construction and return estimates.
![[_papers/brown2007going/images/page_5_chart_2.jpg]]

*Fig. 1 (paper): Number of negative BE Stocks.* Shaded areas denote recession periods as defined by the NBER.

## Method / Architecture

Positive-BE stocks are first placed in the six Fama-French size/value portfolios: NYSE market-cap rankings in June of year $t$ give the median NYSE size that splits NYSE, AMEX and NASDAQ stocks into small (S) and big (B), and NYSE breakpoints for the bottom 30% (L), middle 40% (M) and top 30% (H) of BE/ME give the three value groups, with portfolios running from July of year $t$ to June of year $t+1$. Each negative-BE stock is then assigned to one of these six groups by generalized style classification (GSC), which compares its historical return history with the returns of stocks already in each group. GSC is a quasi-k-means algorithm that adjusts for heteroskedasticity using both time-series and cross-sectional variances, which reduces the effect of outliers, and it comes from the mutual-fund and hedge-fund style literature (Brown and Goetzmann 1992/1997/2003; Brown, Goetzmann and Grinblatt 1998; Ahn, Conrad and Dittmar 2007). BE follows Fama and French: COMPUSTAT stockholders' equity plus balance-sheet deferred taxes and investment tax credit minus the book value of preferred stock (redemption, liquidation or par value, in that order).

Fama-French HML baseline:

$$
HML_t = \frac{1}{2}(R_{SH,t}+R_{BH,t}) - \frac{1}{2}(R_{SL,t}+R_{BL,t})
$$

The sample is merged CRSP/COMPUSTAT monthly data for NYSE, AMEX and NASDAQ from 1986 to 2004, with the Fama-French filters: CRSP prices in December of $t-1$ and June of $t$, COMPUSTAT book common equity for $t-1$, shares outstanding, at least two years on COMPUSTAT to limit survivorship bias, and CRSP share type 10 or 11, which excludes ADRs, REITs and units of beneficial interest. The authors keep financial firms (unlike Fama and French) and report the financial-excluded variant. Drop the financials: the stock count falls 17% while the negative-BE count falls only 7%, so negative-BE stocks matter more in the non-financial sample.

## Results

| Finding | Reported effect |
|---|---|
| Frequency of negative-BE firms | 3.5%–5.7% of stocks equal-weighted with financials included (Table 1 Panel B, 1986–2004); 3.6%–6.2% when financial firms are excluded |
| Value-weight footprint | 0.38%–1.57% of capitalization with financials, 0.38%–1.79% without; median negative-BE size is about one-third of positive-BE size |
| HML impact including negative-BE firms | Average annualized HML_new − HML_old of 0.9% (value-weighted, financials included) and 1.1% (financials excluded), Table 3 |
| Cumulative effect | 17% (financials included) and 20% (excluded) cumulative HML difference over the 18-year period, with t-values of 2.4 and 2.8 — significant at 95% |
| Portfolio composition (Table 2) | Negative-BE stocks move SL portfolio capitalization by more than 10% in 1992, 1994, 1997 and 2004, and change the HML composition by at least 10% in half the sample years (1988–1989, 1992, 1994, 1997–2000, 2004) |
| Where negative-BE stocks sit | 77% are NASDAQ-listed, 11% NYSE, 12% AMEX; top three industries are Computer Programming (10%), Pharmaceutical (5%) and Oil and Gas extraction (5%) |

![[_papers/brown2007going/images/page_13_chart_3.jpg]]

*Fig. 2 (paper): Accumulative HML with and without inclusion of negative BE Stocks.*

## Interpretation

- Negative-BE stocks are not merely noise; they systematically tilt style-factor returns, and most of them do not fall into the highest-growth group — they are more similar to value stocks.
- The enhancement is a default premium: in related work (Li et al. 2007) the negative-BE stocks with the highest probability of default, measured with an option-based bankruptcy model, earn higher average returns than all positive-BE stocks, and they sort into portfolios in a way that raises HML, consistent with Fama and French's reading of value as a distress factor.
- Practical implication stated by the authors: any strategy built to exploit the value premium should carry a default-risk screen. ^[extracted]
- Portfolio construction rules that discard these stocks can miss priced variation in distress/growth transitions. ^[inferred]
- Portfolio construction rules that discard them can miss priced variation in distress/growth transitions. ^[inferred]

## Related

- [[concepts/negative-book-equity-style-classification]]
- [[references/ball2016-accruals-cash-flows-operating-profitability]]
- [[concepts/cash-based-operating-profitability]]
- [[concepts/ordering-information-portfolio-selection]]
- [[references/beatty2014-financial-accounting-in-banking]]
- [[references/pincus2007-accrual-anomaly-international-evidence]] — pincus2007 builds zero-investment accrual decile portfolios in the same cross-sectional style; its OCF-underweighting result parallels the value effects style classification recovers here.
- [[concepts/operating-and-financial-leverage-spreading]] — leverage and spread measures in the same accounting frame

## Open Questions

- Do modern accounting standards and intangibles-heavy balance sheets amplify this effect out of sample? The paper's own list of non-distress causes — goodwill impairments (the AOL/Time Warner $126.9bn goodwill and the $54.24bn 2002 write-off under SFAS 142), start-ups burning capital, deferred-tax adjustments, preferred stock with redemption values above book — predicts that intangibles and preferred capital keep generating negative BE.
- How stable is GSC assignment for negative-BE firms during regime shifts? ^[inferred]
- The authors use the same Fama-French factor recipe and 1986–2004 U.S. data, so the numbers do not transfer directly to markets where listing standards, delisting rules and accounting regimes differ. ^[inferred]
- How stable is style assignment for negative-BE firms during regime shifts? ^[inferred]

## Sources

- [[_papers/brown2007going/brown2007going-extracted.md]]
- [[_papers/brown2007going/brown2007going.md]]
