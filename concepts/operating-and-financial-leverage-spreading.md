---
title: >-
  Operating and Financial Leverage Spreading (ROCE Decomposition)
category: concepts
aliases: [spread, financial leverage, operating liability leverage, FLEV, OLLEV, net borrowing cost, asset turnover]
tags: [profitability, asset-allocation]
relationships:
  - target: "[[concepts/residual-earnings-equity-valuation]]"
    type: related_to
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[concepts/negative-book-equity-style-classification]]"
    type: related_to
  - target: "[[references/brown2007-negative-book-equity-stocks]]"
    type: related_to
  - target: "[[references/kim2020-profitability-asean-stocks]]"
    type: related_to
  - target: "[[references/beatty2014-financial-accounting-in-banking]]"
    type: related_to
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: derived_from
  - target: "[[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]]"
    type: related_to
sources:
  - _papers/nissim2001ratio/nissim2001ratio-extracted.md
  - _papers/nissim2001ratio/nissim2001ratio.md
summary: >-
  ROCE = RNOA + FLEV·SPREAD = PM·ATO + FLEV·SPREAD, and RNOA = ROOA + OLLEV·OLSPREAD; median 1963–1999 FLEV 0.40, OLLEV 0.35, SPREAD 3.9%, OLSPREAD 3.4%.
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: core
created: 2026-10-26T05:12:09Z
updated: 2026-10-30T17:41:00Z
---

# Operating and Financial Leverage Spreading

> [!tldr] Return on capital is **profit margin × asset turnover plus the spread earned on [[concepts/ratio-hierarchy-for-profitability-and-growth|leverage]]**. Two levers are separated: **financial leverage** (net debt on equity, financed at the borrowing cost) and **operating liability leverage** (free trade credit from customers and employees). Leverage is measured as **net** debt, and the second lever is invisible in conventional analysis.

## Financial leverage and the spread

$$ROCE=RNOA+FLEV\cdot SPREAD,\qquad FLEV=\frac{NFO}{CSE},\quad SPREAD=RNOA-NBC$$

$$ROCE=PM\cdot ATO+FLEV\cdot SPREAD,\qquad PM=\frac{OI}{Sales},\quad ATO=\frac{Sales}{NOA}$$

$$ROCE=Sales\ PM\cdot ATO+\frac{Other\ Items}{NOA}+FLEV\cdot SPREAD$$

$FLEV$ is net financial obligations per unit of equity, so firms that are **net holders of financial assets** have negative financial leverage — about **20% of U.S. firm-years**. $NBC$ is the net after-tax borrowing cost. The median values over 1963–1999 make the mechanism concrete: median $RNOA$ 10.0%, median $NBC$ 5.2% after tax, so the median $SPREAD$ is positive; median $FLEV$ is **0.40**, and the median $ROCE$ (12.2%) exceeds the median $RNOA$ (10.0%) — leverage amplifies operating performance. Median $SPREAD$ 3.9% with $SD$ 20.3%, negative in about 30% of firm-years. The conventional leverage measure (Debt/Equity, median 1.19) is **larger** than $FLEV$, and the difference is largely induced by operating liability leverage (debt is used to buy financial assets).

Firms with more operating liability leverage have less financial leverage (Spearman $FLEV$–$OLLEV$ $-0.26$), consistent with the view that operating liabilities are attractive financing; operating liabilities are also cheaper as the firm earns more (median $OLSPREAD$ 3.4%). $FLEV$ and $SPREAD$ are negatively related (rank correlation $-0.38$; $FLEV$–$RNOA$ $-0.42$): the paper conjectures that firms with high operating returns accept more business risk and therefore choose lower financing risk, that higher leverage drives up borrowing cost and shrinks the spread, and that profitable firms generate cash and reduce leverage.

## Operating liability leverage

$$RNOA=ROOA+OLLEV\cdot OLSPREAD,\qquad OLLEV=\frac{OL}{NOA},\quad OLSPREAD=ROOA-\frac{io}{OL}$$

$ROOA=(OI+io)/OA$ is return on operating assets, where $io$ is **implicit interest** on operating liabilities — trade credit is not interest-bearing, so the borrowing rate (net of the interest earned on assets in the same liabilities) is not observable and must be estimated, conventionally with the short-term borrowing rate plus the net interest cost on pension liabilities. Because liabilities are measured as gross amounts, **asset turnover is overstated** when operating liabilities are large; the source's remedy is an asset-base turnover $ATO^{*}=Sales/OA$ with a correspondingly adjusted margin. Economically, firms earn free financing from customers (deferred delivery), employees (deferred wages, pension liabilities, employee stock options), and the government (deferred taxes); recognising the **liability** side of these transactions — deferred taxes, deferred investment tax credits, pension liabilities, employee stock options — is the accounting requirement, and the leverage from employee obligations is substantial. Median $OLLEV$ 0.44, median $OLSPREAD$ 3.4%, with $FLEV$–$OLLEV$ correlation $-0.26$ and $OLLEV$–$ATO$ 0.60, $OLLEV$–$PM$ $-0.21$ (low-margin firms carry more trade credit). ^[inferred]

## Ratio hygiene the decomposition implies

- $RNOA$ (= return on invested capital) is not $ROTA$: $ROTA$ mixes financial assets into the denominator and ignores operating liabilities. Median $ROTA$ 6.8% vs median $RNOA$ 10.0%; $RNOA>ROTA$ at mean and median, and for almost half of firm-years $|RNOA-ROTA|>3\%$ (rank correlation 0.94, so the two move together but at different levels).
- $ROCE$ on total capital (including minority interest) is $ROTCE$; $ROCE=ROTCE\cdot MSR$ with median $MSR$ 1.00, so the minority adjustment is small for the median firm.
- The **core** version of each driver separates items expected to repeat from unusual items (currency gains, pension non-service income, nonrecurring gains/losses, revaluation, restructuring, goodwill amortization); core ratios are the forecasting objects (median Core Sales PM 5.1% vs Sales PM 5.4%; median Core RNOA 9.4% vs RNOA 10.0%). ^[inferred]
- Book value is driven by sales, asset turnover and leverage: $CSE=Sales\cdot(1/ATO)\cdot(1/(1+FLEV))$, so growth in book value is growth in sales scaled by turnover and leverage — asset turnover in turn drives asset growth (and inflation-adjusted historical cost understates assets of high-turnover firms, so high-turnover firms show higher measured asset growth). ^[inferred]
- Seven drivers of $ROCE$: Sales PM, ATO, Other Items/NOA, FLEV, NBC (SPREAD), OLLEV, MSR; three drivers of growth in book value: Sales, ATO, FLEV.
- The **unlevered** reduction ($ReOI$ with $\rho_W$) collapses the driver set to Sales PM, ATO, Other Items/NOA, OLLEV plus Sales and ATO, and is valid only when financial items are at fair value.

## Related

- [[concepts/residual-earnings-equity-valuation]] — the valuation model these drivers feed
- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — the full hierarchy this equation realizes
- [[concepts/cash-based-operating-profitability]] — cash-based complement on the profit-margin side
- [[concepts/negative-book-equity-style-classification]] — leverage and profitability in cross-sectional style work
- [[references/brown2007-negative-book-equity-stocks]] — profit-margin and leverage classes in the cross section
- [[references/kim2020-profitability-asean-stocks]] — profitability ratios in international stock analysis
- [[references/beatty2014-financial-accounting-in-banking]] — the financial/institutional boundary that this operating-financial split is designed for
- [[references/nissim2001-ratio-analysis-equity-valuation]] — the source paper for FLEV/SPREAD and OLLEV/OLSPREAD

## Sources

- [[_papers/nissim2001ratio/nissim2001ratio-extracted.md]]
- [[_papers/nissim2001ratio/nissim2001ratio.md]]
