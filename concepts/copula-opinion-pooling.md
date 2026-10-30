---
title: 'Copula Opinion Pooling (COP)'
category: concepts
tags: [portfolio-optimization]
relationships:
  - target: "[[references/meucci2006-beyond-black-litterman-copula]]"
    type: derived_from
  - target: "[[references/meucci2010-fully-flexible-views]]"
    type: related_to
  - target: "[[references/black1992-global-portfolio-optimization]]"
    type: related_to
sources:
  - _papers/meucci2006blacklitterman/meucci2006blacklitterman-extracted.md
  - _papers/meucci2006blacklitterman/meucci2006blacklitterman.md
  - _papers/meucci2010fully/meucci2010fully-extracted.md
  - _papers/meucci2010fully/meucci2010fully.md
  - _papers/meucci2006blacklitterman/images/page_8_chart_0.jpg
summary: >-
  COP updates a non-normal prior market to subjective marginal views by pooling each view's cdf with the prior-implied cdf and inheriting the prior copula for the joint posterior.
provenance:
  extracted: 0.85
  inferred: 0.1
  ambiguous: 0.05
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T10:55:07Z
updated: 2026-10-30T17:41:00Z
---

# Copula Opinion Pooling (COP)

> [!tldr] COP separates a market's marginal distributions from its dependence structure (copula), opinion-pools each marginal with a subjective view cdf using a confidence weight, and keeps the prior copula as the posterior dependence structure. It is the distribution-level generalization of Black-Litterman for non-normal markets.

## Core Idea

- Market vector M ~ f_M is rotated into view coordinates V = P̄M via a pick matrix P and complementary P⊥ (rows of P⊥ orthonormal); views live on K ≤ N combinations.
- Each view is a subjective marginal cdf F̂_k; the prior-implied marginal is F_k; opinion pooling gives the posterior marginal F̃_k = c_k F̂_k + (1−c_k) F_k with confidence c_k ∈ [0,1].
- Posterior joint: transform each posterior marginal through its prior copula grade, V_k = F̃_k⁻¹(C_k(F_k(V_k))), then rotate back M = P̄⁻¹V. The dependence structure is inherited from the prior, so copulas and tail co-dependence are preserved.
- Practical implementation (five-step Monte Carlo recipe): rotate a J × N panel, sort columns (rank cdf j/(J+1) is the prior marginal, sorted panel is the copula), pool cdf entries, interpolate copula realizations through pooled cdfs, rotate back. All steps run in a fraction of a second even for J = 100,000.
- Confidence is a sensitive parameter; posterior means move toward views while volatilities, kurtoses, and copulas change little.
- The five-step recipe works in real time on any number of risk factors because Monte Carlo is not cursed by dimensionality, while closed-form marginalization is infeasible outside trivial cases.

![[_papers/meucci2006blacklitterman/images/page_8_chart_0.jpg]]
"Figure 2: Cdf of the steepening view: as implied by the market (prior); as stated by the manager (view); and the posterior"

## Limits and the Entropy-Pooling Successor

- COP handles marginal views and multi-user weighted pooling, but not correlation stress-tests as views, non-linear views, lax ranking constraints, or views applied through a trading-desk pricing function.
- Entropy pooling replaces the copula-inheritance mechanism with relative-entropy minimization over posterior distributions subject to the same view constraints, generalizing COP: with a normal prior and linear moment views, the EP posterior is a normal mixture N(μ,Σ)/N(μ̃,Σ̃) with weights 1−c, c, and confidence-weighted multi-user pooling becomes p̃_c = Σ_s c_s p̃^(s).
- Both share the same view inputs (location, ranking, volatility, tail statements) and the confidence machinery (seniority and past-view correlation), so COP is the special case of EP in which the posterior dependence is forced to equal the prior copula. ^[inferred]

## Related

- [[references/meucci2006-beyond-black-litterman-copula]] — the paper that defines and implements COP
- [[references/meucci2010-fully-flexible-views]] — entropy pooling generalizes COP
- [[references/black1992-global-portfolio-optimization]] — the normal-markets framework COP extends
- [[concepts/ordering-information-portfolio-selection]] — ranking views supported by COP/EP inputs

## Sources

- [[_papers/meucci2006blacklitterman/meucci2006blacklitterman-extracted.md]]
- [[_papers/meucci2006blacklitterman/meucci2006blacklitterman.md]]
- [[_papers/meucci2010fully/meucci2010fully-extracted.md]]
- [[_papers/meucci2010fully/meucci2010fully.md]]
- [[_papers/meucci2006blacklitterman/images/page_8_chart_0.jpg]]
