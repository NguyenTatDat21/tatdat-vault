---
title: Global Portfolio Optimization
category: references
tags: [portfolio-optimization, black-litterman, capm, asset-allocation]
relationships:
  - target: "[[concepts/ordering-information-portfolio-selection]]"
    type: related_to
  - target: "[[references/fama1973-risk-return-equilibrium-empirical-tests]]"
    type: related_to
  - target: "[[references/almgren2004-optimal-portfolios-ordering-information]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[concepts/mmse-covariance-shrinkage]]"
    type: uses
sources:
  - _papers/black1992global/black1992global-extracted.md
  - _papers/black1992global/black1992global.md
summary: >-
  Uses CAPM equilibrium returns as a neutral prior and blends investor views by confidence, yielding more stable global asset-allocation portfolios than naive mean assumptions.
provenance:
  extracted: 0.83
  inferred: 0.15
  ambiguous: 0.02
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T20:40:00Z
updated: 2026-10-25T01:47:51Z
---

# Global Portfolio Optimization

> [!tldr] Introduces the equilibrium-plus-views construction (later known as Black–Litterman) to tame unstable mean-variance portfolios.

## Problem & Motivation

Classical mean-variance optimization is highly sensitive to expected-return inputs and often produces extreme, unintuitive positions. The paper proposes using equilibrium risk premiums as a neutral center, then tilting by explicit investor views with confidence.

## Method / Architecture

1. Compute equilibrium excess-return vector $\pi$ from global CAPM assumptions.
2. Treat expected returns as uncertain around this center: prior covariance proportional to $\tau\Sigma$.
3. Encode investor views as linear constraints $P\,E[R]' = Q$.
4. Combine equilibrium and views to derive posterior expected returns used in optimization.

```mermaid
flowchart LR
  A[Market cap + covariance data] --> B[Equilibrium prior π]
  B --> C[Prior over expected returns N(π, τΣ)]
  D[Investor views (P,Q,confidence)] --> E[View likelihood]
  C --> F[Posterior expected returns]
  E --> F
  F --> G[Mean-variance optimization]
```

## Key Equations

Mean-variance objective (standard form implied by the paper's "maximize expected return for a given level of risk"; the paper's own λ is the universal hedging constant, not this objective's risk aversion): ^[inferred]

$$
\max_w\; w'\mu - \frac{\lambda}{2}w'\Sigma w
$$

Equilibrium prior over expected returns:

$$
E[R] \sim \mathcal{N}(\pi,\tau\Sigma)
$$

Linear view system:

$$
P\,E[R]' = Q
$$

Posterior mean update (confidence-weighted tilt):

$$
\mu_{\text{post}} = \pi + \tau\Sigma P'\left(P\tau\Sigma P'\right)^{-1}\left(Q - P\pi\right)
$$

## Results

| Setting | Result |
|---|---|
| Naive return assumptions | Produces unstable and often unreasonable long/short portfolios |
| Equilibrium neutral point | Gives a stable baseline portfolio tied to market structure |
| Global currency hedging | Universal hedge ratio argued to be plausible in the 75–85% range; examples use ~80% |
| View integration | Small/moderate views can be expressed directly with explicit confidence control |

## Limitations

- Equilibrium assumptions and confidence calibration still require judgment.
- Practical outputs remain sensitive to [[concepts/mmse-covariance-shrinkage|covariance estimates]] and view specification.
- Original exposition is partly heuristic and uses illustrative examples rather than one unified empirical testbed. ^[inferred]
- The efficiency of the value-weighted market portfolio under homogeneous expectations and unrestricted short selling is Black (1972)'s argument, used by Fama & MacBeth (1973) to justify testing the two-parameter model on the observed market; it is not part of this 1992 paper's argument, which takes equilibrium value weights as given — see [[references/fama1973-risk-return-equilibrium-empirical-tests]]. ^[inferred]

## Related

- [[concepts/ordering-information-portfolio-selection]]
- [[references/almgren2004-optimal-portfolios-ordering-information]]
- [[concepts/cash-based-operating-profitability]]
- [[references/ball2016-accruals-cash-flows-operating-profitability]]
- [[references/fama1973-risk-return-equilibrium-empirical-tests]]
- [[concepts/fama-macbeth-two-stage-cross-sectional-regression]]

## Sources

- [[_papers/black1992global/black1992global-extracted.md]]
- [[_papers/black1992global/black1992global.md]]
- [[_papers/fama1973risk/fama1973risk-extracted.md]]
