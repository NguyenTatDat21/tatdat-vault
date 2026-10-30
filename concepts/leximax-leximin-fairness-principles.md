---
title: >-
  Leximax and Leximin Fairness Principles
category: concepts
tags: [fairness, max-min-fairness, lexicographic-ordering, resource-allocation]
relationships:
  - target: "[[references/ogryczak2014-fair-optimization-networks-survey]]"
    type: derived_from
  - target: "[[concepts/fuzzy-weighted-max-min-scalarization]]"
    type: related_to
  - target: "[[references/hartman2023-leximin-approximation]]"
    type: related_to
  - target: "[[references/phanduc2025-pareto-front-grid-fairness-dpdptw]]"
    type: related_to
  - target: "[[concepts/periodic-scheduling-under-capacity-constraints]]"
    type: related_to
  - target: "[[references/richards1996-scheduling-to-maximize-customer-satisfaction]]"
    type: related_to
  - target: "[[concepts/gross-profitability-premium]]"
    type: related_to
  - target: "[[concepts/maximin-leximax-fairness]]"
    type: related_to
  - target: "[[concepts/sequential-leximax-threshold-models]]"
    type: related_to
  - target: "[[references/novy-marx2013-other-side-of-value]]"
    type: related_to
  - target: "[[references/xinyingchen2023guide]]"
    type: related_to
sources:
  - _papers/ogryczak2014fair/ogryczak2014fair-extracted.md
  - _papers/ogryczak2014fair/ogryczak2014fair.md
summary: >-
  Definition and properties of lexicographic maximin (leximin) and leximax orderings: Pigou-Dalton fairness axioms, fair dominance, OWA limits, alpha-fairness, water-filling, and complexity.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T07:13:34Z
tier: core
created: 2026-10-26T07:13:34Z
updated: 2026-10-30T14:38:55Z
---

# Leximax and Leximin Fairness Principles

> [!tldr]
> **Definition:** a solution is **leximin-optimal** (lexicographic maximin, MMF) if, after sorting its outcome vector ascending, the sorted vector is lexicographically maximal; equivalently improve the worst-off outcome first, then the next-worst, and so on. **Leximax** is the mirror ordering on descending-sorted vectors, used for minimax-type objectives.
> **Why it is the right fairness criterion:** max-min alone is degenerate — many solutions share the same worst-off value. Lexicographic regularization breaks those ties; the survey calls the resulting procedure "the leximin approach" rooted in Rawls' maximin, Tchebycheff approximation, and the **nucleolus of a matrix game** (Dresher; Schmeidler, generalized by Potters & Tijs).
> **Headline numbers:** lexicographic maximin resource allocation with linear/exponential outcome functions is polynomial at `O(mn)` / `O(m²n)` closed-form manipulations; `barθ_k = max_t (k t − Σ_i max{t − y_i, 0})` makes "sum of the k smallest outcomes" an LP with no binary variables; price of max-min fairness is at most `1 − 4m/(m+1)²`, tight for every `m`.

## Axioms Behind the Ordering

- **Impartiality (anonymity):** any permutation of an outcome vector is indifferent — the criterion depends only on the sorted vector.
- **Pigou-Dalton principle of transfers:** taking `ε` from a better-off service `i` and giving it to a worse-off service `k` (`0 < ε < y_i − y_k`) is preferred. Every strictly Schur-concave, symmetric aggregation satisfies these axioms, so its optima are fairly efficient.
- **Fair dominance:** `y'` fairly dominates `y''` when a finite sequence of permutations, equitable transfers and coordinate increases transforms `y''` into `y'`. A **fairly efficient** solution is one whose outcome vector is not fairly dominated; every fairly efficient solution is Pareto-optimal, not conversely.
- Max-min fairness is the limit of the **α-fairness** utility family `u(y, α) = y^{1−α}/(1−α)` (`α ≠ 1`) and `log y` (`α = 1`): `α = 1` is proportional fairness, `α → ∞` approaches max-min fairness, and for discrete problems a sufficiently large `α` yields exact max-min fairness.

## Equivalence Classes and Scalarizations

- **Cumulative criteria** `barθ_k` (the sum of the `k` smallest outcomes, `k = 1..m`) characterize fair dominance pointwise. Lexicographic maximization of `(barθ_1, …, barθ_m)` = leximin.
- **OWA weights** `ω_1 > ω_2 > … > ω_m > 0` give fair ordered weighted averaging: as weight differences grow the OWA becomes lexicographic maximin; as they shrink it approaches mean maximization. Yager's **andness** measures the position: min aggregation = 1, mean = 1/2, max aggregation = 0; OWA with andness > 1/2 counts as fair.
- **Shortfall duality:** minimizing mean shortfalls `δ_τ(y) = (1/m)Σ(τ − y_i)_+` pointwise over targets is the increasing concave order (Second Stochastic Dominance); maximizing a concave increasing utility is equivalent to minimizing a weighted aggregation of shortfalls with weights `w(ξ) = −u''(ξ)`.
- [[concepts/fuzzy-weighted-max-min-scalarization]] is the fuzzy/OWA-style scalarization of the same max-min family, with a weighted fuzzy membership function.

## Algorithms and Complexity

- **Convex problems (LP-representable outcomes):** lexicographic maximin is a sequence of LPs / recursive max-min steps, polynomial, with **water-filling** as the fixed-path network version — increase all allocations uniformly until a link congests, remove the blocked connections and their capacity, repeat. The same sequence-of-LPs threshold sweep appears in a student-seminar assignment model, where the threshold is a preference score and the LP is re-solved at each candidate level: [[references/richards1996-scheduling-to-maximize-customer-satisfaction]].
- **Nonconvex (0-1) problems with few distinct targets:** counting functions with big-M binary variables `z_ki` and lexicographic minimization of `(Σ_i z_1i, …, Σ_i z_{r−1,i})`. Binary variables can be replaced by auxiliary continuous ones in many formulations.
- **Complexity bounds** (verbatim from the survey): `O(mn)` and `O(m²n)` closed-form lexicographic maximin for linear/exponential outcome functions; `O(|V|⁵)` load-balancing max-min fairness with linear costs; polynomial single-source splittable-flow max-min fairness (Megiddo); `O(pm⁸)` general / `O(pm⁴)` node-restricted ordered-median dynamic programs; `O(m³ log² m)` single-facility ordered median on trees; NP-hard for unsplittable single-path flows, multifacility ordered median on general networks, modular (granular) flows, and `n`-job `m`-machine job-shop.
- **Degeneracy of plain maximin:** the example `(1, 1, 1)`, `(8, 1, 1)`, `(1, 8, 1)`, `(8, 8, 1)` shows all four are max-min optimal when the third outcome is capped at 1 — lexicographic regularization is what selects among them.
- Approximation work continues on leximin itself: [[references/hartman2023-leximin-approximation]] studies approximation algorithms for the leximin objective.

## Fairness in Practice

- **Price of fairness (POF)** compares the total-outcome-maximizing solution with the fair solution: POF(MMF) ≤ `1 − 4m/(m+1)²` (tight), POF(proportional fairness) ≤ `1 − 2√m/m` (tight iff `√m` is integer), α-fairness ≈ `1 − O(m^{−α/(α+1)})`. Reference [75] constructs networks where a fairer allocation is always more efficient, so POF can be zero.
- **Network bandwidth allocation** (max-min fairness, proportional fairness, Nash utilities) is the standard application, including [[concepts/periodic-scheduling-under-capacity-constraints]] where periodic bandwidth allocation under link capacity constraints is a max-min bottleneck problem, and [[references/bar-noy2004-efficient-algorithms-periodic-scheduling]] for scheduling under resource constraints.
- **Applied ordering in combinatorial optimization:** [[references/phanduc2025-pareto-front-grid-fairness-dpdptw]] applies Pareto-front grid fairness to dial-a-ride with time windows, i.e. fairness among passenger outcomes rather than network bandwidth.
- **Inequality indices as substitutes are risky:** minimizing relative inequality measures (variance, Gini index `D(y)/μ(y)`, mean absolute difference) can reward a facility far from all clients — with distances `d_12 = 2`, `d_13 = d_23 = 100` and weights `w_1 = w_2 = (1 − ε)/2`, `w_3 = ε`, the mean-absolute-difference minimizer is the remote node `ν_3` for every `ε < 1/200`.

## Related

- [[references/ogryczak2014-fair-optimization-networks-survey]] — the source of this concept.
- [[concepts/fuzzy-weighted-max-min-scalarization]]
- [[references/hartman2023-leximin-approximation]]
- [[references/phanduc2025-pareto-front-grid-fairness-dpdptw]]
- [[concepts/periodic-scheduling-under-capacity-constraints]]
- [[references/bar-noy2004-efficient-algorithms-periodic-scheduling]]

## Sources

- `_papers/ogryczak2014fair/ogryczak2014fair-extracted.md` — the extracted full text (1073 lines), read in full: axioms, definitions, complexity bounds, POF bounds and the examples above are verbatim from it.
- `_papers/ogryczak2014fair/ogryczak2014fair.md` — Zotero sidecar (bibliographic authority: title, 5 authors, Journal of Applied Mathematics 2014, DOI 10.1155/2014/612018).
- `references/ogryczak2014-fair-optimization-networks-survey.md` — the reference page distilled from the same source in this wave.
- Cross-referenced vault pages (`concepts/fuzzy-weighted-max-min-scalarization.md`, `references/hartman2023-leximin-approximation.md`, `references/phanduc2025-pareto-front-grid-fairness-dpdptw.md`, `concepts/periodic-scheduling-under-capacity-constraints.md`, `references/bar-noy2004-efficient-algorithms-periodic-scheduling.md`) are cited as related context, not as sources of the numbers above. ^[inferred]
