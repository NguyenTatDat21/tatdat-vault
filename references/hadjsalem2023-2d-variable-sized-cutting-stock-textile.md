---
title: >-
  Mathematical Models for the Two-Dimensional Variable-Sized Cutting Stock Problem in the Home Textile Industry
category: references
tags: [paper, cutting-stock, two-dimensional-packing, integer-programming, bi-objective-optimization, bin-packing, pareto-front]
relationships:
  - target: "[[concepts/bin-packing-based-cutting-stock-ilp]]"
    type: uses
  - target: "[[concepts/plate-cut-position-guillotine-mip]]"
    type: related_to
  - target: "[[concepts/four-stage-guillotine-cut-bounded-knapsack]]"
    type: related_to
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
  - target: "[[references/clautiaux2018-hypergraph-guillotine-knapsack]]"
    type: related_to
sources:
  - _papers/hadjsalem2023mathematical/hadjsalem2023mathematical-extracted.md
  - _papers/hadjsalem2023mathematical/hadjsalem2023mathematical.md
  - _papers/hadjsalem2023mathematical/images/page_5_image_2.jpg
  - _papers/hadjsalem2023mathematical/images/page_11_chart_4.jpg
  - _papers/hadjsalem2023mathematical/images/page_13_chart_5.jpg
summary: >-
  Four ILP models for 2D variable-sized fabric-roll cutting in home textile; BPP-based ILP-4+S solves 97/160 instances in ~10 s avg; ε-constraint gives exact Pareto textile-vs-patterns fronts.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25T19:48:00Z
tier: supporting
created: 2026-10-25T19:48:00Z
updated: 2026-10-25T19:48:00Z
---

# Mathematical Models for the Two-Dimensional Variable-Sized Cutting Stock Problem in the Home Textile Industry

> [!tldr] Hadj Salem, Silva, Oliveira & Carravilla (2023, *EJOR*, DOI 10.1016/j.ejor.2022.08.018) model the home-textile cutting problem as a **2D variable-sized cutting stock problem with two-stage (non-exact) guillotine cuts**: decide the widths and lengths of fabric rolls to produce *and* the cutting patterns. Four ILP models are compared; a bin-packing-based model (ILP-4) with symmetry breakers wins decisively, and an ε-constraint method gives the first exact Pareto front minimizing both textile area and number of patterns.

![[_papers/hadjsalem2023mathematical/images/page_5_image_2.jpg]]
*Fig. 5. An optimal solution of the example that contains (a) two cutting patterns from a fabric roll of width W_1 = 160 cm and (b) two cutting patterns from a fabric roll of width W_3 = 225 cm.*

## Problem & Novelty

The home textile cutting-and-production (C&P) process: rolls of fixed discrete widths $W_j$ are produced; on the cutting table, pieces $(l_i,w_i)$ are cut in two-stage guillotine patterns, cuts **not required to be exact** (trimming allowed). The problem generalizes the multi-sized stock cutting problem: the lengths $x_j$ of produced rolls are continuous decision variables bounded by $L_{min}$ and $ub_p$; the objective minimizes the total fabric area $\sum_j W_jx_j$. Strongly NP-hard; industrial demand is below 10 pieces per type, which makes a **bin-packing reformulation** viable — the novel model ILP-4. The paper also claims the first incorporation of pattern-count reduction in an exact multi-objective cutting-stock framework. ^[inferred]

![[_papers/hadjsalem2023mathematical/images/page_11_chart_4.jpg]]
*Fig. 6. Gurobi gap GGap profile (expressed in percentage, log_10 scale).*

## Method / Pipeline

- **ILP-1**: extension of Lodi & Monaci (2003) CSP model with continuous roll lengths, pattern/strip precedence, width capacity, stage-2 length constraints, demand in $[d_i,d_i^{ub}]$, symmetry breakers S1 (patterns sorted by decreasing length), S2 (strips by decreasing item width), S3 (stage-2 cuts by decreasing length).
- **ILP-2 / ILP-3**: width-indexed and piece-indexed variants in the appendix; ILP-2 is the symmetry ILP of ILP-1 and ILP-3.
- **ILP-4 (bin-packing)**: all $|I'|=\sum d_i$ pieces are items; each pattern is a bin; each strip is an item + a bin. Assignment constraints

$$
\sum_j\sum_{i'\le i}\alpha^j_{i,i'}=1\ \ \forall i\in I',\qquad
\sum_j\sum_{i'\le i}\beta^j_{i,i'}\le 1\ \ \forall i\in I'
$$

with pattern-length, roll-length ($x_j\ge\sum_i y_i^j$), strip-length ($\sum l_i\alpha\le y+P_{max}(1-\beta)$), and width ($\sum w_i\beta\le W_j\beta$) constraints (4.1)–(4.15); big-M replaced by industrial parameter bounds.
- **Symmetry breakers S1.α/S2.α/S1.β** (precedence inequalities) and cutting planes **C1.α/C1.β**: $\sum_{k<i'}\alpha^j_{i',k}+\alpha^j_{i,i'}\le1$ (O(I'²)), provably stronger than C2.α/C2.β (O(I'³)) (Props 5.1–5.7) — favor C1.
- **Bi-objective**: $f_1(x)=\sum_j W_jx_j$ (textile area, 6a), $f_2(\beta)=\sum_j\sum_i\beta^j_{i,i}$ (number of patterns, 6b); ε-constraint method $\min f_1$ s.t. ILP-4+(S)-constraints and $f_2(\beta)\le\epsilon_2$ (7a), $\epsilon_2$ decreasing by $\rho$ from $\bar f_2$; $\rho=1$ gives the exact Pareto front.

## Setup & Headline Results

160 instances (16 classes × 10, groups S/M/L; $|I|\in\{5,10\}$, $|J|\in\{3,6\}$, $|I'|\in\{15,20,25,30\}$), Gurobi 9.1 single-thread, TimeLimit 3600 s, performance profiles.

| Model | Solved (of 160) | Avg CPU (s) | Avg GGap S/M/L |
|---|---|---|---|
| ILP-1+S | 46 | 318.4 | 6.88 / 6.33 / 5.29 |
| ILP-2+S | 80 | 71.41 | 0.17 / 0.75 / 1.66 |
| ILP-3+S | 90 | 117.79 | 0.19 / 0.51 / 2.12 |
| **ILP-4+S** | **97** | **10.32** | **0 / 1.6 / 5.47** |
| ILP-4+S+C1 | 97 | 10.35 | ≈ ILP-4+S |
| ILP-4+S+C2 | 98 | 19.44 | slightly worse except L |

ILP-4+S solves group S with GGap < 0.01%; its max GGap ≈ 13.5% at $|I'|=25$; ILP-2+S has the smallest max GGap (< 11%) on Large. Bi-objective results (classes 1–8, $P_{max}\in\{500,1000,1500\}$, 360 s/iteration): 8 instances unsolved; Pareto front size 2–4 for 70–80% of instances, up to 10 patterns; $Gap_{PF}<20\%$ average; CPU per iteration < 7 s for (S); $Gap_{iter}$ rises ~60% (Fig. 12).

![[_papers/hadjsalem2023mathematical/images/page_13_chart_5.jpg]]
*Fig. 8. Pareto front from the --constraint method (min f_1 (x) s.t. f_2 (β) ≤ ε_2) for instances (a) inst_3_5_15_9 from class (S)-1 and (b) inst_6_5_20_1 from class (M)-6.*

## Ablations & Limitations

- Symmetry breakers alone move ILP-4 from unsolved to 97 solved; C1 ≈ baseline, C2 adds one instance at 2x cost.
- BPP-based ILP-4 is competitive **only at low per-type demand** (< 10 pieces/item, the home-textile regime); scaling to real CSP demand levels is untested. ^[inferred]
- Two-stage guillotine only; stochastic/defect-aware production versions are named as future work. ^[extracted]
- The "first exact pattern-reduction multi-objective framework" claim is the authors' own; Lodi & Monaci's models remain stronger on bounds. ^[inferred]

## Bibliographic Record

- Publication: *European Journal of Operational Research*, Vol. 266, No. 2, pp. 514–529, April 16, 2023
- Authors: Khadija Hadj Salem; Elsa Silva; José Fernando Oliveira; Maria Antónia Carravilla (CETCOP, University of Lisbon)
- DOI: 10.1016/j.ejor.2022.08.018
- Companion metadata note: [[_papers/hadjsalem2023mathematical/hadjsalem2023mathematical.md]]

## Related

- [[concepts/bin-packing-based-cutting-stock-ilp]] — pattern page distilled from ILP-4
- [[concepts/plate-cut-position-guillotine-mip]] — guillotine MIP family for the fixed-panel variant
- [[concepts/four-stage-guillotine-cut-bounded-knapsack]] — deeper guillotine hierarchy
- [[references/furini2016-two-dimensional-guillotine-cutting-ip]]
- [[references/clautiaux2018-hypergraph-guillotine-knapsack]]
- Lodi & Monaci (2003), Tackling large instances of the two-dimensional cutting stock problem (EJOR 147:222–238) — base CSP models this paper extends; no vault page yet

## Sources

- [[_papers/hadjsalem2023mathematical/hadjsalem2023mathematical-extracted.md]]
- [[_papers/hadjsalem2023mathematical/hadjsalem2023mathematical.md]]
- [[_papers/hadjsalem2023mathematical/images/page_5_image_2.jpg]]
- [[_papers/hadjsalem2023mathematical/images/page_11_chart_4.jpg]]
- [[_papers/hadjsalem2023mathematical/images/page_13_chart_5.jpg]]
