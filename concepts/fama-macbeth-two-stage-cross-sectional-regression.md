---
title: >-
  Fama-MacBeth Two-Stage Cross-Sectional Regression
category: concepts
tags: [asset-pricing, empirical-method, cross-sectional-regression, beta, finance]
relationships:
  - target: "[[references/fama1973-risk-return-equilibrium-empirical-tests]]"
    type: derived_from
  - target: "[[concepts/ordering-information-portfolio-selection]]"
    type: related_to
  - target: "[[concepts/mmse-covariance-shrinkage]]"
    type: related_to
  - target: "[[references/black1992-global-portfolio-optimization]]"
    type: related_to
sources:
  - _papers/fama1973risk/fama1973risk-extracted.md
  - _papers/fama1973risk/fama1973risk.md
summary: >-
  The portfolio-formation plus monthly cross-sectional regression design that turns noisy security-level
  betas into clean tests of whether beta risk is priced.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-24T00:32:00Z
updated: 2026-10-24T12:28:15Z
---

# Fama-MacBeth Two-Stage Cross-Sectional Regression

The design that made asset-pricing tests possible: estimate the risk characteristic from one window of data, test it in a non-overlapping window, and average the test statistics over time. It is the pattern most empirical asset-pricing papers still copy.

## Core Structure

- **Stage 1 — form portfolios on the characteristic.** Rank securities by an estimated β from a formation window (4 years), sort into 20 portfolios.
- **Stage 2 — re-estimate the characteristic on fresh data.** Recompute portfolio β over the next 5 years, and update it monthly during the testing period. The key move: the β used in the test comes from data not used for formation, which kills the "regression phenomenon" (extreme-β portfolios re-forming toward the middle) that had plagued earlier tests. ^[extracted]
- **Stage 3 — per-period cross-sectional regression.** Each month regress the 20 portfolio returns on the characteristic(s):

$$
R_{pt} = \hat\gamma_0 + \hat\gamma_1\hat\beta_{p,t-1} + \hat\gamma_2\hat\beta_{p,t-1}^2 + \hat\gamma_3\bar s_{p,t-1} + \hat\eta_{pt}
$$

- **Stage 4 — aggregate over time.** Mean coefficients, t-statistics $t(\bar\gamma_j) = \bar\gamma_j / (s(\gamma_j)/\sqrt{n})$, and serial correlations of the per-month estimates (fair-game / market-efficiency test).
- **Non-β risk measure**: standard deviation of market-model residuals $\epsilon_{it}$ from $R_{it} = a_i + \beta_i R_{mt} + \epsilon_{it}$, aggregated as the mean residual deviation $\bar s_p$ inside each portfolio.
- **Panels** A (β), B (β, β²), C (β, $s$), D (all three) let each hypothesis be isolated.
- Rolling windows are essential: nine windows with formation → estimation → testing periods, 435–845 securities meeting data requirements.
- **Variance logic**: the variance of a per-month coefficient decomposes as $s^2(\hat\gamma_j) = s^2(\tilde\gamma_j) + s^2(\tilde\phi_j)$ (estimation-noise + sampling-error components), so $F = s^2(\hat\gamma_j)/s^2(\tilde\phi_j)$ tells whether the month-to-month coefficient has real variation; adding regressors inflates noise on the intercept and slope. ^[extracted]
- **Gauss-Markov reading**: $\hat\gamma_0$ is the return on the minimum-variance portfolio with zero fitted β. ^[extracted]

## Why It Matters

- It is the standard template for testing any cross-sectional predictor (value, size, momentum): form portfolios on the signal, regress returns on it, average the slopes. Modern factor zoo papers use the same skeleton. ^[inferred]
- The design exposes estimation noise explicitly, which is what makes the "is the market efficient?" claim falsifiable at all.
- It separates two hypotheses that earlier tests mixed: linearity in β, and pricing of non-β risk.
- The two-factor form $R_{it} = \hat\gamma_0(1-\hat\beta_i) + \hat\beta_i R_{mt} + \hat\eta_{it}$ improves event studies: one-factor market-model residuals carry the market factors γ₀, γ₂, γ₃, with residual-variance reduction proportional to $(1-\hat\beta)^2$.
- It shows how covariance-estimation error propagates into risk estimates — the same problem shrinkage estimators address in portfolio construction. ^[inferred]
- The design does not solve the estimation problem, it measures it: extreme portfolios carry the largest residual interdependence, so the paper reports evidence of multifactor structure inside a single-index test. ^[inferred]

## Related

- [[references/fama1973-risk-return-equilibrium-empirical-tests]]
- [[concepts/ordering-information-portfolio-selection]]
- [[concepts/mmse-covariance-shrinkage]]
- [[references/black1992-global-portfolio-optimization]]
- [[references/chen2010-shrinkage-mmse-covariance-estimation]]

## Open Questions

- Does the design have enough power for small nonlinearity, given thick-tailed returns make normal-based levels overestimates?
- What does the design conclude under modern high-dimensional covariance estimation, where β noise is far larger than in a 20-portfolio, monthly scheme? ^[inferred]
- Is γ₀ a risk-free rate, a zero-β portfolio return, or the intercept of a multifactor model? The paper cannot separate the interpretations. ^[ambiguous]

## Sources

- [[_papers/fama1973risk/fama1973risk-extracted.md]]
- [[_papers/fama1973risk/fama1973risk.md]]
