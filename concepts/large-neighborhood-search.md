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
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
  - _papers/gendreau2019handbook/images/page_117_image_2.jpg
  - _papers/goel2012large/goel2012large-extracted.md
  - _papers/goel2012large/goel2012large.md
  - _papers/goel2012large/images/page_22_chart_2.jpg
summary: >-
  LNS improves solutions by repeatedly destroying and repairing large parts of a solution; ALNS adapts operator choice based on observed performance.
provenance:
  extracted: 0.82
  inferred: 0.15
  ambiguous: 0.03
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-22T08:35:02Z
updated: 2026-10-24T03:00:25Z
---

# Large Neighborhood Search (LNS)

LNS is a destroy-and-repair metaheuristic: remove a substantial part of a current solution, then rebuild it with a repair heuristic and keep improvements under an acceptance policy.

## Key Ideas

- Large neighborhoods can offer better-quality moves per iteration than small local neighborhoods.
- Explicit neighborhood enumeration is often intractable, so LNS explores neighborhoods implicitly via destroy/repair operators.
- **ALNS** (Adaptive LNS) learns operator usefulness and shifts selection probabilities over time.
- LNS sits within the broader very-large-scale neighborhood (VLSN) family, defined in the handbook as $f(n)=O(n^k)$ with $k\le 3$ (2-opt, relocate, swap are $O(n^2)$; exchange is $O(n^3)$).
- In routing, LNS-style methods are attractive when exact neighborhood scans are too expensive.

![[_papers/gendreau2019handbook/images/page_117_image_2.jpg]]
*Fig. 4.2 (Handbook of Metaheuristics, Ch. 4): the destroy-and-repair process with the accept() step.*

## Census, Acceptance, and an Industrial Instance

- Destroy size: a 15% destroy on 100 customers gives $C(100,15)=2.5\times10^{17}$ removal choices; a 20% destroy on 1000 customers gives $4.2\times10^{208}$.
- LNS was proposed by Shaw, based on ruin-and-recreate; destroy methods are stochastic, so LNS **samples** the neighborhood rather than searching it. The handbook pairs randomized removal of customers (satisfaction-based), related removal, and route removal with constructive/repair heuristics.
- Acceptance: the original LNS accepted improving solutions only, i.e. a hill-climber. With simulated-annealing acceptance — accept if $c(x^t)\le c(x)$, otherwise accept $x^t$ with probability $\exp(-(c(x^t)-c(x))/T)$, $T_{new}=\alpha T_{old}$ with $0<\alpha<1$ and $T_0$ high, decaying — LNS becomes standard simulated annealing with a complex neighborhood.
- Stated advantage: a large neighborhood lets the method navigate easily on tightly constrained instances where small-scale neighborhoods struggle to reach distant regions of the search space.
- Industrial instance: Goel et al. (2012) destroy **all voyages of two ships** in a time-space MIP and repair by re-solving with the other ships' schedules fixed, in a variable-neighborhood loop; the geometric-mean speed-up over CPLEX's first feasible solution is 13.60 (random pair) to 15.72 (LP-selected pair) on LNG inventory-routing instances with 232,856 binaries. See [[concepts/large-neighborhood-ship-pair-destroy-repair]].

![[_papers/goel2012large/images/page_22_chart_2.jpg]]
*Fig. 2 (Goel et al. 2012 paper): cumulative frequency of CPU time over 100 random-pair runs on instance P13.*

LNS and ALNS can also be viewed as low-level heuristic families that a higher-level hyper-heuristic can orchestrate. ^[inferred]

Related pages: [[concepts/variable-neighborhood-search]], [[concepts/hyper-heuristics]], [[concepts/tabu-search]], [[concepts/large-neighborhood-ship-pair-destroy-repair]], [[references/gendreau2019-handbook-metaheuristics]], [[references/goel2012-large-neighborhood-search-lng-inventory-routing]], and [[references/montemanni2024-pdsvrp-collective-drones]].

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
