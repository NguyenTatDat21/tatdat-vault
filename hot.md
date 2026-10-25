---
title: Hot Cache
updated: 2026-10-25T16:35:57Z
pages: 365
generated_by: obsidian-wiki memory hot
---

# Hot Cache

*Generated snapshot of recent vault activity. Rebuilt by `obsidian-wiki memory hot` — edits to the generated sections are overwritten, so put durable prose in `## Key Takeaways`, which survives every rebuild.*

## Recent Activity

- [2026-10-25] INGEST source=_papers/kakinuma2020empirical/kakinuma2020empirical-extract... pages_created=1 pages_updated=2 ...
- [2026-10-25] INGEST source=_papers/kim2020profitability/kim2020profitability-extracted... pages_created=1 pages_updated=2 ...
- [2026-10-25] INGEST source=_papers/ku2016mixed/ku2016mixed-extracted.md pages_created=1 pages_updated=2 ...

## Active Threads

*No open threads.*

## Key Takeaways

Pisinger & Røpke's LNS chapter is the canonical source for destroy/repair design: destroy degree is the key knob (random in a size-dependent range), SA acceptance turns LNS into SA-on-a-complex-neighborhood, ALNS weights update as rho = lambda*rho + (1-lambda)*psi with time-normalized scores; the chapter warns VLSN is not a magic bullet and concludes small+large hybrid neighborhoods are the promising direction. Pham et al. 2023 HGA: the double-bridge gain of Pacheco et al. 2022 is wrong for QTSP when indices are adjacent (missing the c_{sigma(j1),sigma(i1+1),sigma(j2+1)} term); their restricted O(n^2) case-split fixes it and finds new best-knowns on 437/450 instances. Phan Duc et al. 2025 PFG-2F: two-level random keys + Pareto Front Grid (ideal/nadir segmentation) cut IGD ~10x vs MOEA/D on four-objective dynamic PDPTW; the permutation variant converges faster early on RC data. Pincus et al. 2007: accrual overweighting exists only in Australia/Canada/UK/US (Mishkin F=9.29/4.41/24.81/33.38) plus the ADR market (F=21.03); earnings management (DACC deciles negative) drives occurrence, arbitrage risk (ARB interaction kills significance) drives persistence. Qian & Gorman 2001: conditional covariance Sigma~ = Sigma + SigmaP^t(Sigma~v^-1 - Sigma_v^-1)P Sigma is the new result; Theorem 2 shows views move only viewed assets' weights, and views have zero allocation impact when Sigma~v^-1 mu~v = Sigma_v^-1 mu_v.

Modern MIP proves moderate job-shop instances quickly with Manne's disjunctive model in CPLEX/GUROBI, but SCIP's presolve flips the model ranking, and off-the-shelf CP dominates large instances — model size is a poor predictor of solver performance.

## Flagged Contradictions

*None flagged.*
