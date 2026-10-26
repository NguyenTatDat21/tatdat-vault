---
title: "Leximin Approximation: From Single-Objective to Multi-Objective"
category: references
tags: [paper, multi-objective-optimization, leximin, fair-division, approximation-algorithms, polynomial-time, leximin-order, multi-objective-mip, social-choice, algorithm-design, subproblem-formulation, randomized-boosting, theoretical-computer-science, scheduling]
relationships:
  - target: "[[concepts/fuzzy-weighted-max-min-scalarization]]"
    type: related_to
  - target: "[[concepts/multi-objective-maritime-cargo-routing-scheduling]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[concepts/leximax-leximin-fairness-principles]]"
    type: related_to
sources:
  - _papers/hartman2023leximin/hartman2023leximin-extracted.md
  - _papers/hartman2023leximin/hartman2023leximin.md
summary: >-
  Polynomial-time algorithm converts any (α,ε)-approximate single-objective solver into an
  (α²/(1−α+α²), ε/(1−α+α²))-leximin approximation, independent of the number of objectives.
provenance:
  extracted: 0.79
  inferred: 0.21
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T10:50:35Z
updated: 2026-10-25T21:41:00Z
---

# Leximin Approximation: From Single-Objective to Multi-Objective

> [!tldr] Hartman et al. define (α,ε)-leximin approximation and give one polynomial-time algorithm that converts any (α,ε)-approximate single-objective solver into an (α²/(1−α+α²), ε/(1−α+α²))-leximin approximation, regardless of the number of objectives.

## Problem & Contribution

- [[concepts/leximax-leximin-fairness-principles|Leximin]]: maximize the smallest objective, then the second-smallest, and so on; the exact saturation-based algorithms fail with approximate solvers — for lexmaxmin over {x1,x2} subject to x1+x2 ≤ 1, a solver returning 0.49 saturates no objective, so the procedure never terminates correctly (lines 25-31).
- Contributions: a definition of (α,ε)-leximin approximation combining a multiplicative factor α∈(0,1] and an additive factor ε≥0; a polynomial algorithm built from a single-objective approximate oracle; and an approximation-factor degradation mapping independent of the number of objectives.
- Aggregation functions for leximin do not exist (the OWA/Yager context, line 57), so scalarization methods cannot inherit single-objective approximation guarantees; this paper closes that gap with an iterative oracle scheme. ^[inferred]

## Method

Approximate leximin order (lines 127-131): y ≻₍α,ε₎ x iff there is k such that V_j(x) ≤ V_j(y) for all j < k and

$$
V_k(y) > \tfrac{1}{\alpha}\left(V_k(x)+\varepsilon\right)
$$

Algorithm 1 "Ordered Outcomes" (lines 210-216): for t = 1..n, call the oracle OP(z₁..z_{t−1}) to obtain (x_t, z_t); return x_n.

```mermaid
flowchart LR
  A[t = 1] --> B[OP: optimize with prior z_1..z_{t-1}]
  B --> C["(x_t, z_t)"]
  C --> D{t = n?}
  D -- no --> A
  D -- yes --> E[return x_n]
```

Exact subprograms per iteration: P1 maximizes z_t subject to V_ℓ(x) ≥ z_ℓ for ℓ < t (not linear, lines 222-224); P2 replaces them with subset-sum constraints over all subsets of objectives, exponentially many constraints (lines 234-240); P3 linearizes P2 with auxiliary variables y_ℓ, m_{ℓ,j}:

$$
\ell\,y_\ell - \textstyle\sum_j m_{\ell,j} \;\ge\; \textstyle\sum_{i=1}^{\ell} z_i
$$

(lines 248-250).

Order fundamentals: y ≻ x iff y ≻₍₁,₀₎ x (Lemma 1); a (1,0)-approximation is exactly a leximin optimum (Lemma 3); a leximin optimum is an (α,ε)-approximation for every factor (Lemma 5); and a leximin approximation also approximates optimal egalitarian welfare min_i f_i (Observation 6, lines 127-165).

## Results

| Setting | Guarantee (evidence) |
|---|---|
| Exact solver for P2/P3 in Algorithm 1 | Leximin-optimal output (Theorem, line 256, combining Ogryczak-Piòro-Tomaszewski Thm 4 + Ogryczak-Sliwinski Thm 1) |
| (α,ε)-approximate solver for P2/P3 | (α²/(1−α+α²), ε/(1−α+α²))-leximin approximation (Theorem 9, line 300) |
| α = 0.9, ε = 0 | (81/91, 0) ≈ (0.89, 0) (line 302) |
| ε = 0 | Output carries only the multiplicative factor; α = 1 carries only additive ε (line 312) |
| p-randomized solver, n independent activations | Same-factor leximin approximation with probability pⁿ; output always feasible (Corollary 10, lines 316-320) |
| Approximate solver, no factor mapping | Can fail: max{x1,x2} s.t. x1 ≤ 100, x1+x2 ≤ 200 with a (0.9,0)-solver returns (94.5, 94.5), which is not (0.9,0)-leximin-approximate; it is 0.896-good (Theorem 8, lines 280-298) |
| Relation sets R₍α,ε₎ (Table 1, lines 167-174) | Shrink as factors loosen: for x=(1,10,15), y=(1,40,60), z=(2,20,30), R₍₁,₀₎={(z,x),(z,y),(y,x)}; at (1,45) the set is empty |

## Limitations

- The approximate leximin order is partial: not every pair of outcome vectors is comparable (e.g. (1,2) vs (1,3), Section 4).
- The guarantee needs the oracle to return feasible solutions, and P2's exponentially many constraints make P3's linearization assumption-dependent.
- No computational experiments in the paper — the guarantees are theoretical, and runtime behavior of approximate solvers is not measured. ^[inferred]
- Future work targets computational-hardness settings, integer and exponential-LP egalitarian models, and improved factors (lines 328-332).
- The extracted markdown contains NUL bytes; the page content was read through a NUL-stripped in-memory decode (skill: wiki-ingest-strict-batch-fallbacks). ^[inferred]
- The only inline image (page_13_image_1.jpg, caption "Structure of processes running on each transputer") is an extraction artifact unrelated to the paper content, so no figure is embedded. ^[inferred]

## Related

- [[concepts/fuzzy-weighted-max-min-scalarization]]
- [[concepts/multi-objective-maritime-cargo-routing-scheduling]]
- [[concepts/adaptive-large-neighborhood-search-for-mip]]

## Bibliographic Record

- Citation key: `hartman2023leximin`
- DOI: 10.48550/arXiv.2303.12506
- URL: http://arxiv.org/abs/2303.12506
- Publication: preprint (arXiv), 2023-09-28
- Authors: Eden Hartman, Avinatan Hassidim, Yonatan Aumann, Erel Segal-Halevi
- Companion metadata: [[../_papers/hartman2023leximin/hartman2023leximin.md|hartman2023leximin metadata]]
- Funding: Israeli Science Foundation grants 712/20, 2697/22 (line 338)

## Sources

- [[_papers/hartman2023leximin/hartman2023leximin-extracted.md]]
- [[_papers/hartman2023leximin/hartman2023leximin.md]]
