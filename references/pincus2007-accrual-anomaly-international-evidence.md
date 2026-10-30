---
title: The Accrual Anomaly — International Evidence
category: references
tags: [asset-pricing, accruals, cash-flows, international-accounting, legal-traditions, earnings-management]
relationships:
  - target: "[[references/ball2016-accruals-cash-flows-operating-profitability]]"
    type: related_to
  - target: "[[references/beatty2014-financial-accounting-in-banking]]"
    type: related_to
  - target: "[[references/brown2007-negative-book-equity-stocks]]"
    type: related_to
  - target: "[[concepts/fama-macbeth-two-stage-cross-sectional-regression]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[concepts/residual-earnings-equity-valuation]]"
    type: related_to
  - target: "[[references/ozili2017-bank-loan-loss-provisions-review]]"
    type: related_to
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: related_to
    note: "Reciprocal - references/nissim2001-ratio-analysis-equity-valuation references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/sloan1996-accruals-cash-flow-stock-prices]]"
    type: related_to
    note: "Reciprocal - references/sloan1996-accruals-cash-flow-stock-prices references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/pincus2007accrual/pincus2007accrual-extracted.md
  - _papers/pincus2007accrual/pincus2007accrual.md
summary: >-
  Across 20 countries and 62,027 firm-years, the accrual anomaly concentrates in common-law markets (AU, CA, UK, US) plus ADRs, best explained by earnings management and limits to arbitrage.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-25T14:33:00Z
updated: 2026-10-30T14:38:55Z
---

# The Accrual Anomaly — International Evidence

> [!tldr] Sloan's US accrual anomaly is not universal: Mishkin tests detect accruals overweighting only in Australia, Canada, the UK, the US, and in ADRs of firms from anomaly-absent countries; earnings management explains occurrence, limits to arbitrage explain [[concepts/ratio-mean-reversion-and-continuing-value-benchmarks|persistence]].

## Problem & Motivation

Sloan (1996) showed that a long-low-accrual / short-high-accrual strategy earns significant abnormal returns in the US, and that investors weight accruals more than accrual persistence warrants. Pincus, Rajgopal & Venkatachalam ask three things: (1) does the anomaly generalize beyond the US; (2) is its occurrence tied to country-level accounting and institutional structures; (3) which of four proposed explanations survives — earnings management (Xie 2001), limits to arbitrage (Mashruwala et al. 2006), unreliable accrual components (Richardson et al. 2005), and the value-glamour anomaly (Desai et al. 2004).

## Method / Architecture

Sample: 62,027 firm-years, 1994-2002, 20 countries, from Global Vantage Industrial/Commercial + Global Vantage Issues; financial firms excluded; 19,039 US firm-years, Japan 13,822, UK 6,482, down to Denmark 504. Income = NI before extraordinary items (GVIC 32); operating cash flow OCF = NI + depreciation (11) − Δ noncash current assets (75−60) + Δ current liabilities ex current LTD (104−94); accruals ACC = NI − OCF; all scaled by average total assets (89). Abnormal return = holding-period return incl. dividends minus Morgan Stanley country index, accumulated from each country's filing deadline. Winsorize at 5/95 percentiles; rank-based robustness checks give similar inferences.

Mishkin (1983) design: Eq. (1) \(NI_{t+1}=\gamma_0+\gamma_1 ACC_t+\gamma_2 OCF_t+\varepsilon_{t+1}\) forecasts next-year earnings; Eq. (2) \(AR_{t+1}=\beta_0+\beta_1(NI_{t+1}-\gamma_0^*-\gamma_1^*ACC_t-\gamma_2^*OCF_t)+\nu_{t+1}\) prices it; market efficiency requires \(\gamma_1^*=\gamma_1\); the anomaly is \(\gamma_1<\gamma_1^*\) (overweighting). Estimated by iterative weighted nonlinear least squares; test statistic \(2n\ln(SSR^c/SSR^u)\), Chi-square. Note the design's logic: earnings can be correctly weighted while its components are misweighted.

Abnormal returns tests (Section IV) follow Fama & MacBeth (1973): zero-investment decile portfolios on scaled ACC ranks, positions opened the month after each country's filing deadline and held one year; Eq. (6) \(AR_{t+1}=\delta_0+\delta_1 ACCdec+\delta_2 SIZEdec+\delta_3 EPdec+\delta_4 BMdec\), GMM with Newey-West (1987) correction.

## Key Equations

- Eqs. (1)-(3): Mishkin system and test statistic as above.
- Eqs. (4)-(5): country-level OLS of the anomaly dummy AccAnom (1 for AU/CA/UK/US) on ComLaw and institutional factors: AccIndex (Hung 2001, extent of accrual accounting permitted; US 0.86 highest, median 0.59), InvRights/LegEnforce (La Porta 1998 anti-director rights 0-5, enforcement 0-10), ImpEquity (La Porta 1997 equity-market importance), OwnConcen (La Porta 1998 top-3 ownership; US 12% lowest, median 41.5), InsiderTrad (Bhattacharya & Daouk 2002 prosecutions before 1996).
- Eq. (6b): Jones (1991) country-year accruals model \(ACC=\alpha_1+\alpha_2\Delta REV+\alpha_3 PPE\) splits discretionary (DACC) and non-discretionary accruals, tested in deciles inside Eq. (6).
- Eq. (7): arbitrage-risk interaction — ACCdec × ARBdec, ARB = idiosyncratic residual variance of a market model over 36 months, min 6 observations (sample drops to 60,695).

## Results

- Pooled Mishkin (non-US, n=42,988): accruals overweighted \(\gamma_1=0.583<\gamma_1^*=0.743\), F=17.44; OCF underweighted (F=8.72). Common-law pooled: 0.572 vs 0.860, F=23.11; code-law pooled: 0.596 vs 0.561, F=0.48 — no anomaly. Earnings-level Mishkin shows no misweighting pooled, code-law underweighting of earnings (F=15.98).
- Country-by-country accrual Mishkin: significant F-values for Australia 9.29, Canada 4.41, UK 24.81, US 33.38 — the anomaly's four countries; Malaysia/Singapore/Germany/Spain/Indonesia show *underweighting* (γ1* far below γ1). OCF underweighting in 12 countries, earnings underweighting in 11 (11 of the 12); accrual over/underweighting does not mirror OCF (Houge & Loughran 2000).
- Abnormal returns: next-year AR of −8.4% (US), −17.9% (AU), −8.3% (CA), −9.9% (UK) for the low-minus-high accrual position; significant Mishkin AND returns only for the four countries. When OCFdec is added to Eq. (6), significant accrual coefficients remain only for AU/CA/UK/US.
- Country-level regressions: ComLaw +0.44** in every specification; AccIndex +1.38**; OwnConcen −1.27**; in the full model OwnConcen −1.47*, InvRights −0.17*; adjusted R² 23%-69%; condition indices show heavy multicollinearity (Belsley et al. 1980 reading). The anomaly is more likely in common-law countries that permit extensive accrual accounting with dispersed ownership, possibly with weaker outside shareholder rights.
- Alternative explanations: earnings management — DACCdec significantly negative for AU/CA/UK/US, NDACCdec not — supports Xie (2001). Limits to arbitrage — no country's ACCdec is reliably negative once ARBdec is controlled — the anomaly vanishes under arbitrage risk, generalizing Mashruwala et al. (2006). Richardson et al. (2005): accrual reliability explains part of it (changes in current liabilities and noncurrent assets significant in AU/UK only). Desai et al. (2004): in the US the accrual coefficient is subsumed by OCF/price, but not in AU/CA/UK. Khan (2005) bankruptcy-risk explanation not supported.
- ADR sample (893 firm-years, firms domiciled in 14 anomaly-absent countries, ~22% Japan): Mishkin F=21.03 for accruals overweighting, and abnormal returns test gives ACCdec −0.041** — the anomaly shows up where the stock trades (US), not where the firm is domiciled, consistent with the legal-tradition and disclosure/monitoring interpretation.

## Limitations

- Country-level regressions have severe multicollinearity among institutional factors; Logit/probit models failed to converge on 17 countries; the analysis is exploratory (Bushman & Smith 2001: cross-country designs are descriptive, causal claims problematic).
- Power varies: Sweden needs a doubling, India/Switzerland a quadrupling of samples to detect their (negative, significant) abnormal-return coefficients. ^[inferred]
- Balance-sheet accruals carry measurement error (Hribar & Collins 2002, SFAS 95); robustness samples dropping acquisition-method years leave results virtually unchanged.
- OCF and earnings underweighting are left to future research; earnings management via transaction structuring (Jian & Wong 2004) is offered as a conjecture, not tested.

## Images extracted from source PDF

The extracted markdown has zero image embeds; images/ holds 37 table/equation crops (Table 1, Table 2, the Table 3 Mishkin panels, Table 5 country-level statistics, Table 6 abnormal returns, Table 8 ADR panels, equation crops on pages 5-9, 15, 19, 21-23, 25-27, 30). Tables reported in this page were reconstructed from the extracted text.

## Related

- [[references/sloan1996-accruals-cash-flow-stock-prices]] — the accrual anomaly this evidence tests across countries, with the 10.4% first-year hedge as its benchmark

- [[references/ball2016-accruals-cash-flows-operating-profitability]] — ball2016 tests CbOP against the accrual anomaly the same way pincus2007 tests OCF; the OCF subsumption here is the same finding in a 20-country setting. ^[inferred]
- [[references/beatty2014-financial-accounting-in-banking]] — earnings management via discretionary reporting, the same mechanism pincus2007 identifies for accruals, in the regulated bank setting.
- [[references/brown2007-negative-book-equity-stocks]] — style-portfolio construction from merged CRSP/COMPUSTAT data, using the Fama-French sorting machinery this paper's zero-investment portfolios parallel.
- [[concepts/fama-macbeth-two-stage-cross-sectional-regression]] — the portfolio-formation + cross-sectional-regression template pincus2007 applies country-by-country (Eq. 6, GMM).
- [[concepts/cash-based-operating-profitability]] — the cash-versus-accrual valuation gap that OCF underweighting measures directly. ^[inferred]
- [[concepts/residual-earnings-equity-valuation]] — the accrual-valuation model behind the anomaly
- [[references/ozili2017-bank-loan-loss-provisions-review]] — ozili2017 reviews earnings-management-driven loan loss provisioning in banks, the bank-side analogue of pincus2007's earnings-management explanation for the accrual anomaly.

## Sources

- [[_papers/pincus2007accrual/pincus2007accrual-extracted.md]]
- [[_papers/pincus2007accrual/pincus2007accrual.md]]
- Bibliographic record: Pincus, Rajgopal & Venkatachalam (2007), The Accounting Review 82(1):169-202, "The Accrual Anomaly: International Evidence", DOI 10.2308/accr.2007.82.1.169, https://doi.org/10.2308/accr.2007.82.1.169. Zotero: PDF key WBHSYGI6, html attachment KJXZIPNS.
