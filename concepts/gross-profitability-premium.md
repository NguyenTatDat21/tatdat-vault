---
title: Gross Profitability Premium
category: concepts
tags: [asset-pricing, profitability, value-premium, factor-investing, quality-investing, gross-profitability]
relationships:
  - target: "[[references/novy-marx2013-other-side-of-value]]"
    type: derived_from
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: related_to
  - target: "[[concepts/leximax-leximin-fairness-principles]]"
    type: related_to
sources:
  - _papers/novy-marx2013other/novy-marx2013other-extracted.md
  - _papers/novy-marx2013other/novy-marx2013other.md
summary: >-
  GP/A (revenues minus COGS over book assets) predicts average returns like B/M, hedges value at correlation -0.57, and explains most earnings-related anomalies.
provenance:
  extracted: 0.80
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T07:13:34Z
tier: supporting
created: 2026-10-26T07:13:34Z
updated: 2026-10-26T07:13:34Z
---

# Gross Profitability Premium

The **gross profitability premium**: firms with high gross profits-to-assets (GP/A = (REVT − COGS)/AT, revenues minus cost of goods sold over book assets) earn significantly higher average returns than unprofitable firms, *despite* lower book-to-markets and higher market capitalizations. Established in [[references/novy-marx2013-other-side-of-value|Novy-Marx (2013)]]; GP/A has roughly the same power as book-to-market predicting the cross section of average returns, and far more power than earnings or free cash flow (Fama-MacBeth slope 0.75 [t 5.49] vs 0.22 and 0.27; industry-demeaned GP/A 1.00 [8.99]). ^[extracted]

## Key ideas

- **Why gross, not earnings:** expensed R&D, advertising, and human capital cut earnings without cutting true economic profitability; gross profits are the cleanest accounting measure of economic profitability, are not reduced by interest (independent of leverage), and scaling by *book assets* keeps the proxy from being conflated with B/M. ^[extracted]
- **It is a growth strategy that pays:** high-GP/A quintile earns 0.62%/month, low 0.31% (spread 0.31 [2.49], alpha 0.52 [4.49]); the strategy loads −0.44 [−10.8] on HML — a growth strategy in characteristics and covariances. ^[extracted]
- **The value hedge:** profitability and value strategy returns correlate **−0.57**; a 50/50 mix earns 0.71%/month at SD 2.89% (less risk than either leg alone), annual Sharpe **0.85 vs market 0.34**; the mix never had a losing five-year window over 1963–2010. ^[extracted]
- **Controlling works both ways:** value spreads across GP/A quintiles average 0.68%/month (every cell beats the unconditional 0.41%); profitability spreads across B/M quintiles average 0.54% (every cell beats 0.31%). The conditional factors HML|GP (0.54 [5.01]) and PMU|BM (0.48 [5.35]) dominate standard HML (0.40 [3.25]); HML loads 1.04 on HML|GP and −0.18 on PMU|BM — it is inside their span. ^[extracted]
- **Industry adjustment matters:** the industry-demeaned, industry-hedged profitability factor PMUⁿ (0.27 [4.88], alpha 0.35 [6.90]) with Sharpe 0.79 beats standard PMU (0.23 [2.41], Sharpe 0.35); industry exposure drives 80%+ of PMU's variation but only 34% of its mean. ^[extracted]
- **Anomaly commonalities:** the four-factor model (MKT + HMLⁿ + UMDⁿ + PMUⁿ) prices 14 of 15 long–short decile anomalies (only total accruals survive); root mean squared pricing error 0.22%/month vs 0.54 for Fama-French 4, raw 0.67; ~2/3 of the gain is the profitability factor. ^[extracted]
- **Theory conflicts:** the premium contradicts the Fama-French (1993) earnings-risk story, the operating-leverage hypothesis (Carlson-Fisher-Giammarino, Zhang 2005), and the Lettau-Wachter (2007) duration model, because profitable firms are *less* distressed, *lower* operating leverage, and *longer* duration. ^[extracted]

## Why it matters

- A value investor can capture the premium **with no additional risk** — adding profitability to value cuts volatility while doubling exposure.
- The largest, most liquid stocks carry it too: big-cap profitability spread 26 bp [1.88] with alpha 0.50 [3.90]; the Fortune 500 combined-rank strategy earns 0.62%/month, Sharpe 0.74, with only one-third annual turnover. ^[extracted]
- GP/A is a predictor of long-run growth: 3-year gross-profit growth coefficient 0.31 [13.3], 10-year 1.60 [6.40]. ^[extracted]

## Related

- [[references/novy-marx2013-other-side-of-value]] — the source establishing the premium and all numbers above
- [[concepts/cash-based-operating-profitability]] — cash-flow-based profitability signals; GP/A retains power after controlling for accruals and R&D
- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — asset turnover × gross margins (Du Pont) is the same proxy decomposition
- [[concepts/leximax-leximin-fairness-principles]] — inequality-averse objectives in this vault; cross-cluster link added by the cross-linker pass ^[inferred]
- [[references/wahal2020-joint-value-profitability-international]] — cash-based operating profitability × book-to-market grids in 49 non-US markets

## Sources

- `_papers/novy-marx2013other/novy-marx2013other-extracted.md` — full extracted text (660 lines, read in full)
- `_papers/novy-marx2013other/novy-marx2013other.md` — Zotero sidecar (bibliographic authority)
