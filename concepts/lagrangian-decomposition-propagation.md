---
title: Lagrangian Decomposition Propagation
summary: "Lagrangian relaxation propagates bounds between constraint groups as penalties, gives valid bounds for global constraints, and decision-variable-induced bounds strengthen the model."
tags: [lagrangian-relaxation, bound-computation, constraint-propagation, subgradient, duality]
provenance:
  extracted: 0.72
  inferred: 0.18
  ambiguous: 0.10
base_confidence: 0.67
tier: core
category: concepts
created: 2026-10-29T15:46:00Z
updated: 2026-10-30T14:38:55Z
sources:
  - _papers/pesant2015principles/pesant2015principles.md
  - _papers/pesant2015principles/pesant2015principles-extracted.md
relationships:
  - target: references/pesant2015-cp2015-proceedings
    type: related_to
  - target: concepts/bound-tightening-relaxation-networks
    type: related_to
  - target: concepts/cumulative-volume-lower-bound-cp-search
    type: related_to
  - target: concepts/large-neighborhood-search
    type: related_to
  - target: "[[concepts/auxiliary-decision-variable-model-strengthening]]"
    type: related_to
    note: "Reciprocal - concepts/auxiliary-decision-variable-model-strengthening references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/decision-diagrams-optimization]]"
    type: related_to
    note: "Reciprocal - concepts/decision-diagrams-optimization references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
lifecycle: draft
lifecycle_changed: 2026-10-29T15:46:00Z
---

# Lagrangian Decomposition Propagation

> [!tldr] Lagrangian decomposition turns a CP program into subproblems joined by dualized copies of shared variables. The multipliers are both a bound (the dual is a valid objective bound) and a propagator (the penalty cost prunes values). CP 2015 shows both uses: cost propagation between constraint pairs, and an automatic bounding mechanism for constraint programs.

## Summary

The ILP form `max{f x | Ax ≤ b, Cx ≤ d, x ∈ X}` is reformulated with a y-copy and the equality `x = y`, dualized with multipliers `λ ∈ R^n`, giving `L_P(λ) = max{(f−λ)x | Cx ≤ d, x∈X} + max{λy | Ay ≤ b, y∈Y}` (idx 11, chapter 3, pp. 30-38). The same variable-splitting scheme, Lagrangian decomposition of Guignard & Kim, is the basis of a general bounding mechanism for constraint programs, solved by the subgradient method (idx 20, chapter 12, pp. 158-172).

## Key ideas

- **Penalty propagation** — adding Lagrangian penalty costs between pairs of constraints, forcing duplicate variable copies to agree, makes CP constraints communicate; propagating the Lagrangian cost information improves overall bound computation and solution time (idx 11, chapter 3, pp. 30-38).
- **Dual form** — the decomposition is the sum of two maxima, `max{(f−λ)x | Cx ≤ d, x∈X}` and `max{λy | Ay ≤ b, y∈Y}`, so each term is a subproblem whose objective carries the penalty (idx 11, chapter 3, pp. 30-38).
- **Bounding, not just relaxing** — the abstract states Lagrangian decomposition is useful not only to improve the objective bound, and the paper's claim is that propagating the cost is what pays (idx 11, chapter 3, pp. 30-38).
- **CP's bounding gap** — CP has no easy way to automatically derive a good objective bound the way IP solvers do from linear relaxation; Lagrangian relaxation coupled with CP loses the original structure, so variable splitting keeps it (idx 20, chapter 12, pp. 158-172).
- **Subgradient update** — the dual is solved by the subgradient method of Shor et al.: `u^{k+1} = u^k + t_k(y^k − x^k)` (Eq. 9), with step `t_k = λ(Z^{k−1} − Z*)/‖y^{k−1} − x^{k−1}‖²` and `0 ≤ λ ≤ 2` (Eq. 10) (idx 20, chapter 12, pp. 158-172).
- **Multiplier as graph cost** — on the regular constraint graph, the multiplier `u(i,j,a)` for a binary variable `X_j = a` makes an edge `(q₁, a, q₂)` cost `p_aj + Σ_{l=2..m} u(l,j,a)` for constraint 1 and `−u(i,j,a)` for constraint i (idx 20, chapter 12, pp. 158-172).
- **Measured effect** — algorithms built around CP Optimizer 12.6 with depth-first search, criteria of search-tree nodes, time, and instances solved; root-node bounds against CPLEX LP and ILP relaxations average 1.03 % for LD against 0.79 % for LP (idx 20, chapter 12, pp. 158-172).

## Related

- [[references/pesant2015-cp2015-proceedings]] — the volume these papers are drawn from
- [[concepts/bound-tightening-relaxation-networks]] — the relaxation-side counterpart
- [[concepts/cumulative-volume-lower-bound-cp-search]] — bound computation inside CP search
- [[concepts/large-neighborhood-search]] — LNS needs a bound to accept neighbourhoods

## Sources

- `_papers/pesant2015principles/pesant2015principles-extracted.md` (18,510 lines), chapters 3 and 12.
