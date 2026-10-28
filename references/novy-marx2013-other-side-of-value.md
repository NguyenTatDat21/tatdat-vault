---
title: >-
  The Other Side of Value: The Gross Profitability Premium
category: references
tags: [asset-pricing, profitability, value-premium, factor-models, quality-investing, gross-profitability, anomalies, fama-french, investing-strategy, cross-sectional-regression]
relationships:
  - target: "[[concepts/fama-macbeth-two-stage-cross-sectional-regression]]"
    type: uses
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: extends
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: related_to
  - target: "[[references/kim2020-profitability-asean-stocks]]"
    type: related_to
  - target: "[[references/brown2007-negative-book-equity-stocks]]"
    type: related_to
  - target: "[[references/ball2016-accruals-cash-flows-operating-profitability]]"
    type: related_to
  - target: "[[references/fama1973-risk-return-equilibrium-empirical-tests]]"
    type: related_to
  - target: "[[concepts/gross-profitability-premium]]"
    type: related_to
  - target: "[[concepts/leximax-leximin-fairness-principles]]"
    type: related_to
sources:
  - _papers/novy-marx2013other/novy-marx2013other-extracted.md
  - _papers/novy-marx2013other/novy-marx2013other.md
  - _papers/novy-marx2013other/images/page_1_equation_10.jpg
  - _papers/novy-marx2013other/images/page_3_table_5.jpg
  - _papers/novy-marx2013other/images/page_4_table_5.jpg
  - _papers/novy-marx2013other/images/page_5_chart_6.jpg
  - _papers/novy-marx2013other/images/page_6_table_4.jpg
  - _papers/novy-marx2013other/images/page_7_table_5.jpg
  - _papers/novy-marx2013other/images/page_7_table_7.jpg
  - _papers/novy-marx2013other/images/page_8_table_5.jpg
  - _papers/novy-marx2013other/images/page_9_table_5.jpg
  - _papers/novy-marx2013other/images/page_9_table_7.jpg
  - _papers/novy-marx2013other/images/page_10_table_5.jpg
  - _papers/novy-marx2013other/images/page_11_table_5.jpg
  - _papers/novy-marx2013other/images/page_12_table_10.jpg
  - _papers/novy-marx2013other/images/page_13_table_5.jpg
  - _papers/novy-marx2013other/images/page_15_table_14.jpg
  - _papers/novy-marx2013other/images/page_16_equation_10.jpg
  - _papers/novy-marx2013other/images/page_16_table_5.jpg
  - _papers/novy-marx2013other/images/page_17_table_5.jpg
  - _papers/novy-marx2013other/images/page_18_table_5.jpg
  - _papers/novy-marx2013other/images/page_19_table_5.jpg
  - _papers/novy-marx2013other/images/page_20_chart_6.jpg
  - _papers/novy-marx2013other/images/page_20_table_5.jpg
  - _papers/novy-marx2013other/images/page_21_table_3.jpg
  - _papers/novy-marx2013other/images/page_22_table_0.jpg
  - _papers/novy-marx2013other/images/page_23_table_5.jpg
  - _papers/novy-marx2013other/images/page_23_table_8.jpg
  - _papers/novy-marx2013other/images/page_24_table_6.jpg
  - _papers/novy-marx2013other/images/page_24_table_9.jpg
  - _papers/novy-marx2013other/images/page_25_table_6.jpg
  - _papers/novy-marx2013other/images/page_26_table_8.jpg
summary: >-
  Novy-Marx (JFE 2013): gross profits-to-assets predicts returns like B/M, hedges value, and a four-factor model cuts anomaly pricing error to 0.22% per month.
provenance:
  extracted: 0.76
  inferred: 0.02
  ambiguous: 0.22
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T07:13:34Z
tier: core
created: 2026-10-26T07:13:34Z
updated: 2026-10-27T06:00:00Z
---

# The Other Side of Value: The Gross Profitability Premium

> [!tldr] **Robert Novy-Marx, Journal of Financial Economics (2013), DOI 10.1016/j.jfineco.2013.01.003** (sidecar; extracted text confirms sole author, Rochester, JEL G12; volume/issue are not in the extracted md ^[ambiguous]). Profitability measured by **gross profits-to-assets (GP/A = (REVT − COGS)/AT)** has roughly the same power as book-to-market predicting the cross section of average returns. Profitable firms earn significantly higher returns despite *higher* valuation ratios; the profitability strategy is a growth strategy that **hedges value** (return correlation −0.57), and a four-factor model (market + industry-adjusted value, momentum, profitability) prices most earnings-related and seemingly unrelated anomalies, cutting root mean squared pricing error from 0.54% to 0.22% per month.

![[_papers/novy-marx2013other/images/page_1_equation_10.jpg]]

*Equation on page 1 (the dividend-discount/clean-surplus starting point, Eq. 1 in text).* ^[ambiguous]

## Problem & motivation

Popular work (Fama & French 2006) finds earnings has power in [[concepts/fama-macbeth-two-stage-cross-sectional-regression|Fama-MacBeth]] regressions, but Fama & French (2008, p. 1663) concluded that "profitability sorts produce the weakest average hedge portfolio returns" and provide little basis for a profitability return relation once size and B/M are controlled. This paper shows the opposite when profitability is measured **gross**: revenues minus cost of goods sold, scaled by book assets. Earnings are a polluted proxy — R&D, advertising, and human-capital investments are expensed, reducing earnings without reducing true economic profitability. Gross profits are "the cleanest accounting measure of true economic profitability": not reduced by interest, hence independent of leverage; scaling by book assets (not equity, not market) avoids conflating the productivity proxy with B/M.

The economic logic: value strategies buy inexpensive assets by selling expensive ones; profitability strategies buy **productive** assets by selling unproductive ones. Both acquire productive capacity cheaply — the same philosophy, "the other side of value."

## Method / formulation

Under the dividend discount model with clean surplus accounting, market value of equity (cum dividend) is

$$M_t = \sum_{\tau=0}^{\infty} \frac{E_t[Y_{t+\tau} - dB_{t+\tau}]}{(1+r)^{\tau}} \tag{1}$$

where $Y_t$ is earnings, $dB_t = B_t - B_{t-1}$ is the change in book equity, $r$ the required return. Higher expected earnings ⇒ higher expected returns; higher valuations ⇒ lower expected returns. The Du Pont decomposition of the proxy:

$$\frac{\text{Gross profits}}{\text{Assets}} = \underbrace{\frac{\text{Sales}}{\text{Assets}}}_{\text{Asset turnover}} \times \underbrace{\frac{\text{Gross profits}}{\text{Sales}}}_{\text{Gross margins}} \tag{2}$$

Sample: Compustat starting 1962 (Amex inclusion year); accounting data usable from end of June of the following calendar year; asset pricing tests cover **July 1963–December 2010**; financial firms (one-digit SIC 6) excluded; independent variables trimmed at 1%/99%; annual rebalancing at end of June; NYSE breakpoints; value-weighted portfolios. Free cash flow = NI + DP − WCAPCH − CAPX; book equity via tiered definitions matching Fama & French's HML construction. Spearman rank correlation between GP/A and B/M is **−18%** (highly significant), so profitability sorts are growth strategies. ^[inferred]

![[_papers/novy-marx2013other/images/page_3_table_5.jpg]]
![[_papers/novy-marx2013other/images/page_4_table_5.jpg]]

*Table 1. Fama and MacBeth regressions of returns on measures of profitability (Panel A: straight variables; Panel B: industry-demeaned).*

**Table 1 (slope coefficients ×10², [t]):** GP/A `0.75[5.49]`; earnings IB/BE `0.22[0.84]`; FCF/BE `0.27[2.28]`; log(B/M) `0.35[5.98]`; log(ME) `−0.09[−2.29]`; $r_{1,0}$ `−5.57[−13.8]`; $r_{12,2}$ `0.76[3.87]`. Industry-demeaned (Panel B): GP/A `1.00[8.99]`, earnings `0.28[1.86]`, FCF `0.16[2.54]`. GP/A subsumes earnings and FCF; FCF subsumes earnings; FCF keeps incremental power over GP/A only after controlling for earnings. With industry demeaning the GP/A t-statistic is more than 1.5× the B/M coefficient and ~2.5× the momentum coefficient. EBITDA/A and XSGA/A each have power, individually and jointly, but GP/A subsumes them; asset turnover and gross margins likewise lose power jointly with GP/A. GP/A keeps its power after controlling for accruals (Sloan 1996) and R&D (Chan, Lakonishok & Sougiannis 2001).

## Results

**Univariate quintile sorts (Table 2, Panel A, sorted on GP/A; monthly value-weighted excess returns):** Low `0.31[1.65]` → High `0.62[3.12]`; high−low `0.31[2.49]` with alpha `0.52[4.49]` and HML loading `−0.44[−10.8]`. Portfolio GP/A runs 0.10→0.68, B/M 1.10→0.33, ME $748M→$1,096M, n 771→938. Panel B (B/M sorts): Low `0.39` → High `0.80[3.88]`, high−low `0.41[2.95]`, HML `0.91[30.0]`; high B/M portfolio ME $367M, B/M 5.47.

**The hedge:** profitability strategy 0.31%/month (SD 2.94%), value 0.41%/month (SD 3.27%), return correlation **−0.57**. A 50/50 mix earns 0.71%/month with SD 2.89% — positions twice as large, *less* risk; t-statistic 5.87; realized annual **Sharpe 0.85 vs 0.34 for the market**. Orthogonal to momentum.

![[_papers/novy-marx2013other/images/page_5_chart_6.jpg]]

*Fig. 1. Performance over time of profitability and value strategies. Trailing five-year Sharpe ratios of profitability (dashed) and value (dotted) and a 50/50 mix (solid). Long–short extreme value-weighted quintiles from sorts on gross profits-to-assets and book-to-market; sample excludes financial firms, June 1963 to December 2010.*

Profitability performed poorly mid-1970s to early-1980s and mid-2000s; value performed poorly in the 1990s; the 50/50 mix **never had a losing five-year period** over July 1963–December 2010.

**Size (Table 3):** small quintile has 2,427 firms (54.2% of firms) but 2.43% of total capitalization; large quintile 335 firms, 75.1% of capitalization ($3,652B); average capitalization $39.6M → $9,494M; B/M 2.64 → 0.61; GP/A is flat across size (0.27, 0.28, 0.26, 0.25, 0.27).

![[_papers/novy-marx2013other/images/page_6_table_4.jpg]]

*Table 3. Size portfolio time series average characteristics.*

**Double sorts size × GP/A (Table 4):** profitability spreads 0.67[4.59] (small) to 0.26[1.88] (big) per month; alphas 0.63[4.27] to 0.50[3.90]; HML loadings increase in magnitude with size (0.13 → −0.51[−11.3]). Among the largest stocks the profitability spread (26 bp, t 1.88) exceeds the value spread (14 bp, t 0.95, untabulated); the two strategies correlate −0.58 and a 50/50 mix in the Fortune 500 universe earns Sharpe 0.44 (strategies alone: 0.27, 0.14).

![[_papers/novy-marx2013other/images/page_7_table_5.jpg]]
![[_papers/novy-marx2013other/images/page_7_table_7.jpg]]
![[_papers/novy-marx2013other/images/page_8_table_5.jpg]]

*Table 4. Double sorts on gross profits-to-assets and market equity (Panel A returns/loadings; Panel B firm counts and book-to-markets).*

**International evidence (Table 5, 19 developed markets outside North America, Compustat Global, July 1990–October 2009):** GP/A high−low `0.76[2.25]` with alpha `0.99[2.97]`; B/M high−low `0.51[2.12]` — the profitability spread is significant and *larger* than the international value spread.

![[_papers/novy-marx2013other/images/page_9_table_5.jpg]]
![[_papers/novy-marx2013other/images/page_9_table_7.jpg]]
![[_papers/novy-marx2013other/images/page_10_table_5.jpg]]

*Table 5. Excess returns to portfolios sorted on profitability, international evidence.*

**Double sorts GP/A × B/M (Table 6):** average value spread across profitability quintiles `0.68%` per month — in every B/M quintile exceeds the unconditional 0.41%; average profitability spread across B/M quintiles `0.54%` — in every quintile exceeds the unconditional 0.31%. Panel B pattern: profitable growth firms are large, profitable **value** firms are small (High-B/M/High-GP/A cell: 108 firms, average size $102M).

![[_papers/novy-marx2013other/images/page_11_table_5.jpg]]
![[_papers/novy-marx2013other/images/page_12_table_10.jpg]]

*Table 6. Double sorts on gross profits-to-assets and book-to-market.*

**Fortune 500 strategy (Table 7):** rank the 500 largest nonfinancial stocks on GP/A and B/M; each June buy $1 of the 150 stocks with the highest combined ranks, short $1 of the 150 lowest. High−low combined-rank spread `0.62%`/month `t[5.11]`, alpha `0.37[3.67]`, realized annual Sharpe **0.74**; only one-third of each side turns over per year; average excess returns "almost 8% per year." Long side contributes 0.28%/month, short side 0.34%. The long side hedged with the market: abnormal returns `18 bp`/month `t[3.46]`, Sharpe 0.75 when run at market volatility. Notable July–December 2010 top-rank names: AstraZeneca, GlaxoSmithKline, JC Penney, Sears, Nokia.

![[_papers/novy-marx2013other/images/page_13_table_5.jpg]]

*Table 7. Performance of large stock profitability and value strategies (tertile sorts on GP/A, B/M, and the sum of ranks).*

**Conditional factors (Table 8):** tertile sorts *within* deciles, HML construction. **HML|GP** earns `0.54%`/month `t[5.01]` vs HML `0.40[3.25]`; abnormal relative to HML `0.23[4.55]`, relative to FF3 + UMD `0.23[4.52]` — essentially orthogonal to momentum. **PMU|BM** earns `0.48%`/month `t[5.35]`; abnormal relative to FF3 `0.48[5.23]`, relative to FF3+UMD `0.51[5.54]` — a larger information ratio than UMD (5.11). HML loads `1.04[47.6]` on HML|GP and `−0.18[−6.73]` on PMU|BM (adj. R² 79.9%), so HML is inside the span of the two conditional factors. The unconditional PMU loads `0.98[57.2]` on PMU|BM and `−0.33[−22.7]` on HML|GP: long real profitability, short real value.

![[_papers/novy-marx2013other/images/page_15_table_14.jpg]]

*Table 8. High-minus-low factor (HML) constructed conditioning on gross profitability (HML|GP and PMU|BM).*

**Industry-adjusted factors (Table 9, July 1973–December 2010):** HMLⁿ `0.47[6.42]`, alpha `0.25[5.41]`; UMDⁿ `0.58[4.17]`, alpha `0.28[6.51]`; PMUⁿ `0.27[4.88]`, alpha `0.35[6.90]`. All three have Sharpe ratios exceeding any Fama-French factor, and FF4 (MKT, SMB, HML, UMD) does not significantly reduce their information ratios.

![[_papers/novy-marx2013other/images/page_16_equation_10.jpg]]

*Equation region on page 16 (Table 9 header region).* ^[ambiguous]

**Anomalies (Table 10, 15 long–short extreme-decile strategies, July 1973–December 2010):** mean excess returns vs FF4 alphas vs the alternative model (MKT, HMLⁿ, UMDⁿ, PMUⁿ) alphas — Market equity `0.35[1.53] / −0.19[−1.60] / 0.38[1.54]` (PMUⁿ loading −1.35[−6.42]); Book-to-market `0.58[3.13] / 0.05 / −0.03`; Prior performance `1.43[4.28] / 0.52[3.99] / −0.14`; Industry-adjusted profitability `0.21[2.34] / 0.32[4.01] / −0.04` (PMUⁿ 1.01[16.8]); Return on assets `0.67[2.81] / 0.84[4.63] / −0.15` (PMUⁿ 2.33[13.6]); Return on equity `1.02[4.47] / 0.82 / 0.07` (PMUⁿ 1.52[8.23]); Asset turnover `0.54[2.92] / 0.47 / −0.15` (PMUⁿ 2.05[13.5]); Gross margins `0.02[0.15] / 0.42[3.33] / 0.01` (PMUⁿ 1.00[7.78], HMLⁿ −0.46[−4.97]); SUE `0.69[4.00] / 0.54 / 0.36[2.20]` (only ~half explained); Failure probability `0.76[2.09] / 0.94[4.44] / −0.26` (PMUⁿ 2.19[9.93]); Ohlson O-score `0.11[0.58] / 0.59[4.55] / 0.09` (PMUⁿ 0.85[5.40]); Net stock issuance `0.73[5.15] / 0.62 / 0.21`; Total accruals `0.37[2.35] / 0.37 / 0.39[2.16]` — the only anomaly the alternative model fails; Asset growth `0.70[4.17] / 0.30 / 0.23`; Organizational capital (Eisfeldt & Papanikolaou, SG&A stock depreciating 15%/yr) `0.46[3.73] / 0.30 / 0.27` (PMUⁿ 0.25[2.11]).

![[_papers/novy-marx2013other/images/page_16_table_5.jpg]]
![[_papers/novy-marx2013other/images/page_17_table_5.jpg]]

*Table 10. Anomaly strategy average excess returns and abnormal performance.*

**Root mean squared pricing error across the 15 anomalies:** raw excess returns 0.67%/month; FF4 0.54; the alternative four-factor model **0.22** — less than half FF4. Intermediate models: FF4 + PMUⁿ `0.36`, MKT + HMLⁿ + UMDⁿ `0.44`: roughly **two-thirds** of the improvement is the profitability factor, one-third the industry adjustments.

## Interpretation and conclusion

Gross profitability is "the other side of value": both strategies acquire productive capacity cheaply. Profitable firms are *good growth firms* — low B/M, negative HML loadings, yet high returns. The findings collide with the Fama & French (1993) earnings-risk interpretation ("the value premium is emphatically not driven by unprofitable stocks"), the operating-leverage hypothesis (Carlson, Fisher & Giammarino 2004; Zhang 2005; Novy-Marx 2009, 2011), and the Lettau & Wachter (2007) duration explanation — profitable firms have *longer* durations, lower operating leverage, less distress. A value investor can capture the full profitability premium with **no additional risk**: adding profitability to value reduces volatility while doubling exposure to risky assets.

## Appendix highlights

![[_papers/novy-marx2013other/images/page_18_table_5.jpg]]

*Table A1. Spearman rank correlations between independent variables (A.1).*

**A.1** GP/A–IB/A 0.45[58.7], GP/A–FCF/A 0.31[17.9], GP/A–B/M −0.18[−17.2], GP/A–ME −0.03[−2.51], GP/A–$r_{12,2}$ 0.09[7.00]; earnings and FCF are positively correlated with size (0.36, 0.20), GP/A is not.

![[_papers/novy-marx2013other/images/page_19_table_5.jpg]]

*Table A2. Fama and MacBeth regressions employing EBITDA and XSGA (A.2).*

EBITDA/A `1.42[4.28]`, XSGA/A `0.65[4.07]`; jointly GP/A `0.53[3.76]`, EBITDA `1.07[3.03]`, XSGA `−0.69[−2.05]`; EBITDA keeps incremental power over GP/A, XSGA does not. Spearman GP/A–EBITDA 0.51, GP/A–XSGA 0.77; asset turnover–gross margins 0.27, GP/A–turnover 0.67, GP/A–margins 0.43.

![[_papers/novy-marx2013other/images/page_20_table_5.jpg]]

*Table A3. Fama and MacBeth regressions with asset turnover and gross margins (A.2/A.3 crop region).* ^[ambiguous]

![[_papers/novy-marx2013other/images/page_21_table_3.jpg]]

*Table A4 (crop is rotated in the extraction): Excess returns to portfolios sorted on asset turnover and gross margins (A.3).* ^[ambiguous]

Asset-turnover sorts: high−low `0.34[2.51]` with alpha `0.26[1.94]`; gross-margin sorts: high−low excess `0.01[0.13]` but alpha `0.37[4.35]` (HML loading −0.52[−17.6]) — high-margin firms are growth firms that outperform their peers.

![[_papers/novy-marx2013other/images/page_22_table_0.jpg]]

*Table A5 (crop orientation stripped): Fama and MacBeth regressions with accruals and R&D expenditures (A.3), July 1973–December 2010.* ^[ambiguous]

GP/A `0.85[5.21]` alone; accruals `−1.35[−4.67]`, R&D-to-market `2.31[4.22]`; with GP/A: `0.78[4.75]`, `0.86[5.17]`, `0.68[3.59]` — GP/A's power survives controls for both.

![[_papers/novy-marx2013other/images/page_23_table_5.jpg]]

*Table A6. Spigot the high frequency profitability strategy (garbled caption in extraction; low vs high frequency PMU time-series regressions, Jan 1972–Dec 2010).* ^[ambiguous]

![[_papers/novy-marx2013other/images/page_23_table_8.jpg]]

*Table A6, lower panel rows (caption stripped in extraction).* ^[ambiguous]

![[_papers/novy-marx2013other/images/page_24_table_6.jpg]]

*Table A7 (crop region; garbled caption in extraction): Profitability and profitability growth, Fama-MacBeth regressions of three- and 10-year growth on current profitability (A.5).* ^[ambiguous]

![[_papers/novy-marx2013other/images/page_24_table_9.jpg]]

*Table A7 continuation panels (caption stripped).* ^[ambiguous]

**A.4/A.5 numbers:** the high-frequency PMU (quarterly REVTQ/COGSQ/ATQ, rebalanced monthly, available at end of month after report date RDQ) intercept `0.63[3.73]`, alpha vs FF3 `0.78[4.61]`; the annual PMU `0.33[2.06]`; PMU explains PMU^hf with slope `0.64[16.3]` (adj. R² 36.2%), the reverse `0.57[16.3]`. High-frequency profitability is almost twice as profitable, ~8% per year, and persists more than three years. GP/A predicts 3-year gross-profit growth `0.31[13.3]` and 10-year `1.60[6.40]`; regressions exclude firms under $25M market cap, Newey-West t-statistics with 2/9 lags, fiscal years 1962–2010.

![[_papers/novy-marx2013other/images/page_20_chart_6.jpg]]

*Fig. A1. Persistence of profitability strategy performance. This figure shows the average cumulative returns to the high frequency gross profitability strategy considered in Table A6 from one to 60 months after portfolio formation. The sample excludes financial firms, and covers January 1972 to December 2010.*

![[_papers/novy-marx2013other/images/page_25_table_6.jpg]]

*Table A8 (crop region, caption anchor stripped in extraction): Double sorts on gross profits-to-assets and book-to-market, large stocks (A.6).* ^[ambiguous]

![[_papers/novy-marx2013other/images/page_26_table_8.jpg]]

*Table A9 (crop region, caption anchor stripped): Double sorts on gross profits-to-assets and book-to-market, small stocks (A.6).* ^[ambiguous]

**A.6 numbers:** large cap — average value spread across GP/A quintiles `0.59%` vs unconditional `0.30%`; average profitability spread `0.45%` vs unconditional `0.29%`; the high-profitability/high-B/M corner is very thin (4–8 firms per cell). Small cap — value spread `0.81%` vs `0.72%`, profitability spread `0.54%` vs `0.57%`: controlling matters little; the value effect is stronger among unprofitable stocks, the profitability effect among growth stocks.

**A.7 industry controls (Table A10):** standard HML `0.40[3.25]` Sharpe 0.47, UMD `0.72[3.94]` Sharpe 0.57, PMU `0.23[2.41]` Sharpe 0.35. Hedging industry exposure lowers returns (0.36/0.62/0.15) but raises Sharpes to **0.88/0.79/0.52**; industry exposure contributes only 10% (0.04/0.40) of HML's mean and 34% (0.08/0.23) of PMU's mean, but 80%+ of their variation. Industry-adjusted sorting raises PMU's mean to `0.27[4.42]` with Sharpe 0.64 — adjusted profitability is truly more associated with expected returns. Adjusted **and** hedged strategies reach Sharpe 0.97 (B/M), 0.77 (momentum), 0.79 (GP/A).


## Related

- [[concepts/gross-profitability-premium]] — the premium this paper establishes and its hedging properties
- [[concepts/cash-based-operating-profitability]] — cash-flow-based profitability signals in the same literature lineage
- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — the Du Pont-style driver hierarchy the paper's decomposition anticipates
- [[concepts/leximax-leximin-fairness-principles]] — the fairness/inequality-aversion page in this vault (cross-linker pass)
- [[references/wahal2020-joint-value-profitability-international]] — tests the US value×profitability result out of sample in 49 non-US markets

## Sources

- `_papers/novy-marx2013other/novy-marx2013other-extracted.md` — full extracted text (660 lines, read in full)
- `_papers/novy-marx2013other/novy-marx2013other.md` — Zotero sidecar (bibliographic authority)
- 29 image crops under `_papers/novy-marx2013other/images/` (all listed in frontmatter `sources:`; caption-to-crop mapping for the appendix tables is inferred from page order and marked ^[ambiguous] where the extracted md's caption anchors were garbled)
