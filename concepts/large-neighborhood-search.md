---
title: >-
  Large Neighborhood Search (LNS)
category: concepts
tags: [metaheuristics, lns, alns, routing]
relationships:
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[concepts/tabu-search]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: derived_from
  - target: "[[references/pisinger2019-large-neighborhood-search]]"
    type: related_to
  - target: "[[references/pham2023-efficient-ga-quadratic-tsp]]"
    type: related_to
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: related_to
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
  - _papers/gendreau2019handbook/images/page_117_image_2.jpg
  - _papers/goel2012large/goel2012large-extracted.md
  - _papers/goel2012large/goel2012large.md
  - _papers/goel2012large/images/page_22_chart_2.jpg
  - _papers/pisinger2019large/pisinger2019large-extracted.md
  - _papers/pisinger2019large/pisinger2019large.md
  - _papers/ha2020new/ha2020new-extracted.md
  - _papers/ha2020new/ha2020new.md
summary: >-
  LNS improves solutions by repeatedly destroying and repairing large parts of a solution; ALNS adapts operator choice based on observed performance.
provenance:
  extracted: 0.84
  inferred: 0.14
  ambiguous: 0.02
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-22T08:35:02Z
updated: 2026-10-25T19:48:00Z
---

# Large Neighborhood Search (LNS)

LNS is a destroy-and-repair metaheuristic: remove a substantial part of a current solution, then rebuild it with a repair heuristic and keep improvements under an acceptance policy.

## Key Ideas

- Large neighborhoods can offer better-quality moves per iteration than small local neighborhoods.
- Explicit neighborhood enumeration is often intractable, so LNS explores neighborhoods implicitly via destroy/repair operators.
- **ALNS** (Adaptive LNS) learns operator usefulness and shifts selection probabilities over time.
- Ropke & Pisinger formalized ALNS (Transportation Science 40(4):455-472, 2006) for PDPTW; their handbook chapter systematizes the operator inventories, psi-score/lambda-decay weight adaptation, and the VLSN families; see [[references/pisinger2019-large-neighborhood-search]].
- The handbook defines small neighborhood search as $f(n)=O(n^k)$ with low $k$ ($k\le 3$; 2-opt, relocate, swap are $O(n^2)$), while very-large-scale neighborhoods grow exponentially and are too large to search explicitly.
- In routing, LNS-style methods are attractive when exact neighborhood scans are too expensive.

![[_papers/gendreau2019handbook/images/page_117_image_2.jpg]]
*Fig. 4.2 (Handbook of Metaheuristics, Ch. 4, verbatim): "Destroy and repair example. The top left figure shows a CVRP solution before the destroy operation. The top right figure shows the solution after a destroy operation that removed six customers (now disconnected from the routes). The bottom figure shows the solution obtained after reinsertion of the customers by the repair operation." The accept() step is the chapter's terminology for the acceptance stage of the LNS loop, not part of this caption.*

## Census, Acceptance, and an Industrial Instance

- Destroy size: the chapter's example destroy method for the CVRP removes, say, 15% of the customers in the current solution (selecting them at random), and a repair method rebuilds by inserting removed customers with a greedy heuristic.
- LNS was proposed by Shaw, based on ideas similar to the ruin-and-recreate method of Schrimpf et al.; destroy methods contain stochasticity, so LNS **samples** the neighborhood rather than searching it. Shaw gradually increases the degree of destruction; Ropke and Pisinger choose it randomly each iteration from a range dependent on instance size.
- Acceptance: the original LNS accepted improving solutions only, i.e. a hill-climber. With simulated-annealing acceptance — accept if $c(x^t)\le c(x)$, otherwise accept $x^t$ with probability $\exp(-(c(x^t)-c(x))/T)$, $T_{new}=\alpha T_{old}$ with $0<\alpha<1$ and $T_0$ high, decaying — LNS becomes standard simulated annealing with a complex neighborhood.
- Stated advantage: a large neighborhood lets the method navigate easily on tightly constrained instances where small-scale neighborhoods struggle to reach distant regions of the search space.
- Industrial instance: Goel et al. (2012) destroy **all voyages of two ships** in a time-space MIP and repair by re-solving with the other ships' schedules fixed, in a variable-neighborhood loop. Table 11 defines speed-up as the ratio of CPU time CPLEX needs to generate a solution at least as good as the heuristic's, relative to the heuristic's own CPU time; geometric means over solvable instances are 13.61 (lexicographic), 13.60 (random pair), 14.47 (metrics), 15.72 (LP-selected pair) on LNG inventory-routing instances with up to 232,856 binary variables. See [[concepts/large-neighborhood-ship-pair-destroy-repair]].

![[_papers/goel2012large/images/page_22_chart_2.jpg]]
*Fig. 2 (Goel et al. 2012, verbatim): "Cumulative frequency distribution for total CPU time for H-Randm on P11. CPU time for H-Model is indicated by vertical line" — over the 100 randomized runs on P11, 77% take more CPU time than H-Model.*

LNS and ALNS can also be viewed as low-level heuristic families that a higher-level hyper-heuristic can orchestrate. ^[inferred]

- Hà et al. (2020) replaced CP-based insertion feasibility with linear programs in an ALNS for VRP with synchronization: maximize the delay allowed on each route arc under time windows and sync (F1), probe all arcs in one LP (F2), validate O(1) from stored earliest/latest arrivals, final LP check (F3) — 20× speedup on 50-customer instances, dominating all prior heuristics; see [[references/ha2020-vrp-synchronization-lp-alns]]. ^[inferred]

Related pages: [[concepts/variable-neighborhood-search]], [[concepts/hyper-heuristics]], [[concepts/tabu-search]], [[concepts/large-neighborhood-ship-pair-destroy-repair]], [[references/gendreau2019-handbook-metaheuristics]], [[references/goel2012-large-neighborhood-search-lng-inventory-routing]], [[references/montemanni2024-pdsvrp-collective-drones]], [[references/pisinger2019-large-neighborhood-search]], and [[references/pham2023-efficient-ga-quadratic-tsp]], [[references/ha2020-vrp-synchronization-lp-alns]].

## Open Questions

- Which destroy/repair operator portfolios transfer cleanly from CVRP to collaborative truck-drone variants?
- How aggressively should ALNS adaptation respond to short-term operator performance volatility? ^[inferred]

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
- [[_papers/gendreau2019handbook/gendreau2019handbook.md]]
- [[_papers/gendreau2019handbook/images/page_117_image_2.jpg]]
- [[_papers/goel2012large/goel2012large-extracted.md]]
- [[_papers/goel2012large/goel2012large.md]]
- [[_papers/goel2012large/images/page_22_chart_2.jpg]]
- [[_papers/ha2020new/ha2020new-extracted.md]]
- [[_papers/ha2020new/ha2020new.md]]
