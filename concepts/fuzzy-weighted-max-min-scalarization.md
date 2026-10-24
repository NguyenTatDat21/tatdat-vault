---
title: >-
  Fuzzy Weighted Max-Min Scalarization for Multi-Objective MIP
category: concepts
tags: [multi-objective-optimization, scalarization, fuzzy-logic, mixed-integer-programming, pareto-fronts]
relationships:
  - target: "[[references/dossantos2024-multiobjective-maritime-cargo-routing]]"
    type: derived_from
  - target: "[[concepts/multi-objective-maritime-cargo-routing-scheduling]]"
    type: uses
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
sources:
  - target: "[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]"
    type: related_to
  - _papers/dossantos2024multiobjective/dossantos2024multiobjective-extracted.md
  - _papers/dossantos2024multiobjective/dossantos2024multiobjective.md
summary: >-
  Scalarize several objectives by maximizing a weighted minimum of fuzzy membership values, so one MIP solve
  per weight vector traces out a Pareto approximation without an evolutionary algorithm.
provenance:
  extracted: 0.75
  inferred: 0.20
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-24T00:32:00Z
updated: 2026-10-24T04:15:00Z
---

# Fuzzy Weighted Max-Min Scalarization for Multi-Objective MIP

A scalarization scheme for multi-objective MIP: turn each objective into a fuzzy membership value and maximize the **weighted minimum** of them. It suits MIP solvers because it keeps the problem a single optimization, and the max-min form prevents one objective from being satisfied at the expense of another.

## Core Structure

- Each objective $Z_l$ (a minimization) becomes a membership value scaled between its best and worst attainable values:

$$
\mu_{Z_l}(x) = \frac{Z_l^+ - Z_l(x)}{Z_l^+ - Z_l^-}
$$

- $Z_l^+$ comes from the single-objective optimum (in the maritime case, a matheuristic run on that objective); $Z_l^-$ is the **nadir** value from the full solution.
- Decision-maker weights $\theta_k$ with $\sum_k \theta_k = 1$, $\theta_k \ge 0$; solve:

$$
\max \lambda \quad \text{s.t.} \quad \theta_k\lambda \le \mu_{Z_k}(x)\ \ \forall k
$$

- A weight sweep ($\theta_k \in \{0, 0.05, \dots, 1\}$, all weight combinations summing to 1) produces a set of solutions, which is the Pareto approximation.
- The max-min form is what distinguishes it from a weighted sum: the solution is judged by its **worst** normalized objective, so a weight of zero for an objective removes it from the comparison entirely.
- Evaluation must be relative when no true Pareto front is known: C-metric and hypervolume of one algorithm's set against the other's, plus convergence/diversity metrics.
- A weight of zero for an objective means that objective is not considered in the solution, so sweeps that include zeros generate solutions that are not comparable.

## Why It Matters

- It keeps multi-objective work inside the MIP machinery: one solve per weight vector, so an exact solver's bounds and cuts still apply.
- The best/worst anchors ($Z^+$, $Z^-$) make objectives comparable on one scale, which is what lets non-cost objectives (makespan, delay) trade off against money.
- It requires the extremes, so the scheme pushes you to run single-objective optimizations first — that is where the matheuristic for each objective earns its keep.
- It exposes weights as an explicit, interpretable policy dial: business preferences enter as $\theta$, not as hidden cost conversions. ^[inferred]
- The scheme is deterministic and reproducible, unlike evolutionary multi-objective methods. ^[inferred]
- It does not deliver a certified Pareto front: the quality of the approximation depends on the anchors, so gaps between weight vectors are not quantified. ^[inferred]
- The scheme is used on maritime cargo routing, multi-objective energy-military logistics, power generation and product-line planning — it is the standard scalarization when the solver is a MIP.

- **Anchoring evidence from ganjia**: its economic / customer / compromise orientations reproduce the frontier endpoints from single-objective extremes (74.52 MLCU & 9.43 h vs 2.17 h & 245.11 MLCU), exactly the $Z^+/Z^-$ anchor roles the membership function needs. The tuned NSGA-II sits within 0.002% of the $\varepsilon$-constraint cost front, MOPSO within 0.020%. ^[inferred]
- **Ganjia 2026 instantiation** (cost + tardiness, production-scheduling / due-date / batch-delivery / heterogeneous VRPTW MINLP): ganjia does **not** use fuzzy max-min — it builds the front with the $\varepsilon$-constraint method, tunes NSGA-II / MOPSO parameters by Taguchi L27 (smaller-the-better S/N), and lists fuzzy approaches as future work. The Taguchi dial is a *parameter* analogue of the $\theta$ sweep, and due-date setting is part of the objective. ^[inferred] [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]
## Related

- [[references/dossantos2024-multiobjective-maritime-cargo-routing]]
- [[concepts/multi-objective-maritime-cargo-routing-scheduling]]
- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/adaptive-large-neighborhood-search-for-mip]]
- [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]

## Open Questions

- How dense must the weight sweep be for the approximation to be usable, and how far apart are consecutive weight vectors in solution space?
- Can the anchors be computed cheaply for a new objective (e.g. CO₂ emissions) without a full single-objective run?
- Does a max-min scheme ever produce solutions that a weighted-sum sweep misses, and how often? ^[inferred]
- Do Taguchi-tuned algorithm parameters produce the same front as a fuzzy $\theta$ sweep on a bi-objective scheduling MINLP (the ganjia cost + tardiness case)? ^[inferred]

## Sources

- [[_papers/dossantos2024multiobjective/dossantos2024multiobjective-extracted.md]]
- [[_papers/dossantos2024multiobjective/dossantos2024multiobjective.md]]
  - _papers/ganjia2026multiobjective/ganjia2026multiobjective-extracted.md
  - _papers/ganjia2026multiobjective/ganjia2026multiobjective.md
  - _papers/ganjia2026multiobjective/images/page_3_chart_1.jpg
  - _papers/ganjia2026multiobjective/images/page_4_chart_1.jpg
