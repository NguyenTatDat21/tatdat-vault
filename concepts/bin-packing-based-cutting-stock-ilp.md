---
title: >-
  Bin-Packing-Based Cutting Stock ILP
category: concepts
tags: [integer-programming, cutting-stock, bin-packing, symmetry-breaking, cutting-planes]
relationships:
  - target: "[[references/hadjsalem2023-2d-variable-sized-cutting-stock-textile]]"
    type: derived_from
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
  - target: "[[references/clautiaux2018-hypergraph-guillotine-knapsack]]"
    type: related_to
  - target: "[[concepts/four-stage-guillotine-cut-bounded-knapsack]]"
    type: related_to
  - target: "[[concepts/plate-cut-position-guillotine-mip]]"
    type: related_to
sources:
  - _papers/hadjsalem2023mathematical/hadjsalem2023mathematical-extracted.md
  - _papers/hadjsalem2023mathematical/hadjsalem2023mathematical.md
summary: >-
  Encode cutting as 1D bin packing: pieces as items, patterns as bins, strips as item+bin; compact size-indexed-free ILP plus precedence symmetry breakers beats index models at low per-type demand.
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25T19:48:00Z
tier: supporting
created: 2026-10-25T19:48:00Z
updated: 2026-10-25T19:48:00Z
---

# Bin-Packing-Based Cutting Stock ILP

> [!tldr] When per-type item demand is small (below ~10 pieces), the cutting stock problem collapses to bin packing: every piece is an item, every pattern a bin, every strip an item+bin pair. The model loses the pattern/strip index product of CSP formulations and becomes tractable for a general solver.

## Core Idea

From Hadj Salem et al. (2023, ILP-4): flatten all $|I'|=\sum_i d_i$ pieces into items and encode the three guillotine layers through item-to-bin assignments:

$$
\sum_j\sum_{i'\le i}\alpha^j_{i,i'}=1\ \ \forall i\in I',\qquad
\sum_j\sum_{i'\le i}\beta^j_{i,i'}\le 1\ \ \forall i\in I'
$$

($\alpha^j_{i,i'}$ = piece $i$ in a strip that starts at piece $i'$ in roll $j$; $\beta^j_{i,i'}$ = piece $i$ starts a strip of pattern $i'$), with roll length $x_j\ge\sum_i y_i^j$, strip length $\sum l_i\alpha\le y+P_{max}(1-\beta)$, width $\sum w_i\beta\le W_j\beta$, and big-M replaced by industrial parameter bounds.

Variable counts: $2J|I'|^2$ binaries, $O(J|I'|^2)$ constraints — no dependence on the pattern-length grid $P$ that bloats the CSP-indexed models ($J\cdot P$ products).

## Why It Beats the Index Models

- Symmetry breakers S1.α/S2.α/S1.β (precedence inequalities) are the decisive lever: ILP-4 alone was unsolved, ILP-4+S solved 97/160 instances with avg CPU 10.32 s vs 71–318 s for the Lodi & Monaci-indexed ILP-1/2/3. ^[inferred]
- Cutting planes C1.α ($\sum_{k<i'}\alpha_{i',k}+\alpha_{i,i'}\le 1$) dominate the O(I'³) C2 planes (Props 5.1–5.7), and add nothing measurable on top of S — the symmetry structure, not extra cuts, carries the model. ^[inferred]
- The pattern count $f_2(\beta)=\sum\beta_{i,i}$ becomes directly readable, enabling exact bi-objective ε-constraint Pareto fronts (textile area vs patterns). ^[inferred]

## Limits

- Valid only when demand per type is small: BPP bin count $|I'|$ grows linearly with total demand; real cutting instances with demand in the hundreds make it intractable. ^[inferred]
- Two-stage guillotine, non-exact cuts (trimming); the encoding does not cover $n$-stage guillotine families such as [[concepts/four-stage-guillotine-cut-bounded-knapsack]]. ^[inferred]
- Bounds quality is weaker than the pattern-indexed ILP-1 (best bounds per the paper's profile comparison).

## Related

- [[references/hadjsalem2023-2d-variable-sized-cutting-stock-textile]]
- [[concepts/plate-cut-position-guillotine-mip]] — position-indexed MIP for fixed panels
- [[concepts/four-stage-guillotine-cut-bounded-knapsack]]
- [[references/furini2016-two-dimensional-guillotine-cutting-ip]]
- [[references/clautiaux2018-hypergraph-guillotine-knapsack]]

## Sources

- [[_papers/hadjsalem2023mathematical/hadjsalem2023mathematical-extracted.md]]
- [[_papers/hadjsalem2023mathematical/hadjsalem2023mathematical.md]]
