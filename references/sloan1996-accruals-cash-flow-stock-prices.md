---
title: "Sloan 1996 – Do Stock Prices Fully Reflect Information in Accruals and Cash Flows?"
category: references
tags:
  - accruals
  - earnings-quality
  - post-earnings-announcement-drift
  - factor-investing
  - cash-flow
  - market-efficiency
  - paper
aliases:
  - Sloan accruals anomaly
sources:
  - "[[_papers/sloan1996stock/sloan1996stock-extracted.md]]"
  - "[[_papers/sloan1996stock/sloan1996stock.md]]"
  - "[[_papers/sloan1996stock/images/page_13_chart_6.jpg]]"
  - "[[_papers/sloan1996stock/images/page_13_chart_8.jpg]]"
relationships:
  - target: "[[references/pincus2007-accrual-anomaly-international-evidence]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[concepts/residual-earnings-equity-valuation]]"
    type: related_to
  - target: "[[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]]"
    type: related_to
summary: "Sloan (The Accounting Review 1996): accruals persist 0.765 vs cash flows 0.855, yet prices weight accruals 0.911 over cash flows 0.826. A long-low/short-high accrual hedge earns 10.4% in year one."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T07:25:00Z
updated: 2026-10-27T07:25:00Z
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
---

> [!tldr] Accruals are priced like cash flows, but they do not persist like cash flows
> Across 40,679 NYSE/AMEX firm-years from 1962 to 1991, earnings predict next year's earnings with coefficient 0.841; split into components, accruals persist 0.765 and cash flows 0.855. Stock prices price accruals at 0.911 and cash flows at 0.826 — the reverse of their true persistence. A hedge that is long the lowest-accrual decile and short the highest earns 10.4% in the first year (t = 4.71).

## Definitions and sample

- Earnings = operating income after depreciation (Compustat item 178) divided by average total assets (item 6); non-recurring items are excluded because Compustat cannot decompose them into cash and accrual parts.
- Accruals = (ΔCA − ΔCash) − (ΔCL − ΔSTD − ΔTP) − Dep, with current assets (item 4), cash (item 1), current liabilities (item 5), debt in current liabilities (item 34), income taxes payable (item 71), depreciation (item 14). Cash flow component = earnings − accruals.
- Sample 40,679 firm-years, 30 years 1962–1991; pre-1962 dropped for survivorship bias, post-1991 for missing future returns, banks and insurers for missing accrual data.
- Stock-return window starts **four months** after fiscal year-end (Alford et al. 1994 on public availability), cumulated for three future years, with a −100% delisting return assumed when CRSP codes it missing. Abnormal returns measured two ways: size-matched buy-hold and portfolio Jensen alphas (Ibbotson 1975), the alpha version restricted to December year-ends, 24,209 firm-years.

## Persistence: H1

- Pooled `Earnings_{t+1} = α0 + α1 Earnings_t` gives α1 = 0.841 (t = 303.98; random walk rejected at t = −57.47); industry-level mean 0.773, interquartile 0.708–0.863; rank regressions 0.783 pooled.
- Split specification `Earnings_{t+1} = γ0 + γ1 Accruals + γ2 Cash Flows`: **γ1 = 0.765, γ2 = 0.855**, equality rejected F = 614.01; γ1 < γ2 in 86% of industries. Rank version: γ1 = 0.565 vs γ2 = 0.838, F = 4894.24, γ1 smaller in 99% of industries.
- Table 1 deciles: cash flow falls from 0.22 (0.23) in the lowest-accrual portfolio to 0.00 (0.00) in the highest; earnings rises from 0.07 (0.07) to 0.15 (0.13); betas 1.25 → 0.86 (portfolio 4) → 1.23, so an equal-weight 1–10 hedge has beta 0.02. Rank correlation accruals–cash flows −0.53, accruals–accruals/earnings ratio 0.94. Variation in accruals is mostly the current-asset component (−0.08 to 0.21).

## Pricing: H2

- Market-efficiency likelihood test on the earnings-only system: 0.007, marginal significance 0.933 — prices do anticipate the *average* persistence of annual earnings, so the annual-earnings drift is absent; the Bernard & Thomas drift is a quarterly phenomenon.
- On the components system, the pricing coefficients invert: γ1* = 0.911 for accruals and γ2* = 0.826 for cash flows.
- Size-adjusted hedge returns: year 1 **10.4%** (t 4.71), year 2 4.8% (t 3.15), year 3 2.9% (t 1.64); Jensen alphas 10.4% (4.42), 4.8% (2.41), 3.8% (1.62). Individual extremes in year 1: +4.9% (t 2.65) low accrual, −5.5% (t −3.98) high accrual.
- Stability: the hedge is positive in 28 of 30 years; exceptions 1966 (−19.5%) and 1981 (−2.2%).
- Cross-sectional returns on accruals: −0.32 (t −4.60) for year t+1, −0.16 (−2.75) for t+2, −0.14 (−2.61) for t+3.
- Timing (16,795 firm-years, 1973–1991): hedge announcement-period return 4.5% vs non-announcement 6.0%, so **over 40% of the predictable return lands in 12 trading days** out of ~254. The good-news (low-accrual) portfolio concentrates over 80% around announcements (4.5% vs 0.9%); the bad-news (high-accrual) portfolio shows 0.0% in announcements and −5.1% outside, consistent with preemption of bad-news announcements — 34.5% late reporters in the highest-accrual decile vs 28.5% in the lowest.

![[_papers/sloan1996stock/images/page_13_chart_6.jpg]]
*Figure 1 illustrates the lower persistence of earnings performance attributable to the accrual component of earnings relative to earnings performance attributable to the cash flow component of earnings. The figure provides time-series plots of earnings performance for firm-years in the extreme deciles when ranked by earnings, accruals and cash flows, respectively.* (Panel identified from the extractor legend order: the six page-13 charts pair high/low for earnings, accruals, cash flows.)

![[_papers/sloan1996stock/images/page_13_chart_8.jpg]]
*Figure 1 illustrates the lower persistence of earnings performance attributable to the accrual component of earnings relative to earnings performance attributable to the cash flow component of earnings. The figure provides time-series plots of earnings performance for firm-years in the extreme deciles when ranked by earnings, accruals and cash flows, respectively.* (Cash-flow panel, same legend order.)

## Related

- [[references/pincus2007-accrual-anomaly-international-evidence]] — tests the accrual anomaly in Australia, Canada, the UK and the US, citing Sloan as the origin.
- [[concepts/cash-based-operating-profitability]] — cash-based profitability is the "good news" side of Sloan's split.
- [[concepts/residual-earnings-equity-valuation]] — accruals and earnings are the inputs its valuation model runs on.
- [[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]] — same mean-reversion logic, applied to accounting ratios.

## Limitations

- NYSE/AMEX only, 1962–1991; the announcement timing test covers 1973–1991 because Compustat quarterly announcement dates begin in the early 1970s.
- Balance-sheet accruals are used before SFAS No. 95 (1987) made cash-flow statements available, so the measure is reconstructed from balance-sheet and income-statement changes.
- The model cannot inspect images; panel assignments follow extractor legend order, not pixel inspection.

## Sources

- [[_papers/sloan1996stock/sloan1996stock-extracted.md]] — Sloan, *The Accounting Review*, July 1996, zotero-key G9HPTLK4, DOI 10.2308/TAR-9608042309; submitted February 1995, accepted February 1996.
