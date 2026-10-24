---
title: >-
  Handbook of Metaheuristics (Gendreau & Potvin, 2019)
category: references
tags: [book, metaheuristics, operations-research, optimization]
relationships:
  - target: "[[concepts/tabu-search]]"
    type: uses
  - target: "[[concepts/variable-neighborhood-search]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: uses
  - target: "[[concepts/parallel-metaheuristics-cooperative-search]]"
    type: uses
  - target: "[[concepts/hyper-heuristics]]"
    type: uses
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
  - _papers/gendreau2019handbook/images/page_20_image_3.jpg
  - _papers/gendreau2019handbook/images/page_20_image_4.jpg
  - _papers/gendreau2019handbook/images/page_26_image_2.jpg
  - _papers/gendreau2019handbook/images/page_47_image_7.jpg
  - _papers/gendreau2019handbook/images/page_85_image_2.jpg
  - _papers/gendreau2019handbook/images/page_123_image_2.jpg
  - _papers/gendreau2019handbook/images/page_257_image_2.jpg
  - _papers/gendreau2019handbook/images/page_115_image_2.jpg
  - _papers/gendreau2019handbook/images/page_117_image_2.jpg
summary: >-
  Distilled handbook-level patterns for tabu search, VNS, LNS/ALNS, cooperative parallel search, and hyper-heuristics used in routing and combinatorial optimization.
provenance:
  extracted: 0.74
  inferred: 0.23
  ambiguous: 0.03
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-22T08:35:02Z
updated: 2026-10-24T12:55:00Z
---

# Handbook of Metaheuristics (Gendreau & Potvin, 2019)

This handbook consolidates core metaheuristic design patterns and compares how they are applied across combinatorial optimization domains, including routing and scheduling.

## Key Ideas

- Metaheuristics differ mainly by how they balance intensification and diversification under fixed compute budgets.
- Memory-based control (e.g., tabu search), neighborhood-change control (VNS), and destroy/repair control (LNS/ALNS) are reusable design families.
- Cooperative parallel search improves robustness and often solution quality when exchanges preserve diversity and avoid premature convergence.
- Hyper-heuristics move control one level up: they search over heuristics instead of directly searching over candidate solutions.
- Together, these families provide a shared vocabulary for designing routing solvers across truck-only and truck-drone settings. ^[inferred]

## Chapter Signals Relevant to Routing

- **Tabu Search (Chapter 2):** explicit treatment of tabu tenure, aspiration, and candidate-list strategies.
- **Variable Neighborhood Search (Chapter 3):** formal neighborhood-change logic (VND, RVNS, BVNS).
- **Large Neighborhood Search (Chapter 4):** destroy/repair framing and ALNS-style adaptive operator control.
- **Parallel Metaheuristics (Chapter 13):** cooperative multi-search taxonomies and communication design trade-offs.
- **Hyper-Heuristics (Chapter 14):** updated classification by selection/generation and online/offline/no learning.

![[_papers/gendreau2019handbook/images/page_115_image_2.jpg]]
![[_papers/gendreau2019handbook/images/page_117_image_2.jpg]]
*Fig. 4.1 (paper): a 100-customer CVRP solution with 15 customers removed (43 vehicles); Fig. 4.2 (paper): the LNS destroy-and-repair process with the accept() step.*

## LNS Chapter Numbers (Pisinger & Ropke, Chapter 4)

- LNS was proposed by Shaw, based on the ruin-and-recreate approach, and belongs to the **VLSN** class: the neighborhood is defined implicitly by the destroy and repair methods and is **sampled**, never searched exhaustively.
- Census: a 15% destroy on 100 customers gives $C(100,15)=2.5\times10^{17}$ removal choices; a 20% destroy on 1000 customers gives $4.2\times10^{208}$. Very large-scale neighborhoods are defined as $f(n)=O(n^k)$, $k\le 3$ — 2-opt, relocate, swap ($O(n^2)$); exchange is $O(n^3)$.
- VLSN motivation, stated as an observation: a large neighborhood gives a higher-quality local optimum and a more promising search path; filtering limits the subset searched, and random removal with capacity-respecting repair gives a fast heuristic with a large neighborhood.
- With simulated-annealing acceptance (accept improving; else accept $x^t$ with probability $\exp(-(c(x^t)-c(x))/T)$, $T_{new}=\alpha T_{old}$, $0<\alpha<1$) LNS becomes standard simulated annealing with a complex neighborhood. The original LNS accepted improving solutions only, i.e. a hill-climber.
- Stated advantage: the large neighborhood lets the method navigate easily on tightly constrained instances, whereas small-scale neighborhoods struggle to reach distant regions of the search space.
- Chapter 4 prescribes randomized destroy methods (customer removal, related removal, route removal) paired with constructive/repair heuristics; the ship-pair variant used in industry is [[concepts/large-neighborhood-ship-pair-destroy-repair]].

## VNS and Tabu Search Chapter Additions

- **VNS (Chapter 3):** proposed ~20 years before 2019; schemes VND, RVNS, BVNS, GVNS plus Skewed VNS and VNDS (two-level VNS on a problem decomposition, solving a sequence of reduced problems from LP relaxations with variables fixed by VNDS rules, producing sequences of upper and lower bounds). Neighborhood-change rule: if $f(x')<f(x)$, set $x\leftarrow x'$ and return $k$ to the initial neighborhood, otherwise move to the next. Three motivating facts: a local minimum in one neighborhood need not be one in another; a global minimum is a local minimum for all neighborhoods; local minima with respect to several $N_k$ are often close. Extensions: Formulation Space Search / variable formulation search; VNS for automatic programming and AI; AutoGraphiX graph-theory discovery (>1500 conjectures, more than half proved automatically, compared with about 400 by human efforts); VNS combined with local branching for MILP solution generation, and with exact solvers for very large MILP instances.
- **Tabu Search (Chapter 2):** hybridization is pervasive — TS with ALNS (order-batching, Žulj/Kramer/Schneider, EJOR 264:653–664, 2018), GA, CP and IP; multi-objective TS for continuous problems (Jaeggi/Parks/Kipouros/Clarkson, EJOR 185:1192–1212, 2008) and on GPUs (Tsitskas/Kipouros/Savill, 2014).
- The handbook's third edition has 18 chapters (the second 21, the first 19); the edition change drops the "future directions" framing in favor of "recent and emerging" methods.

## Bibliographic Record

- Citation key: `gendreau2019handbook`
- DOI: `10.1007/978-3-319-91086-4`
- Canonical URL: <http://link.springer.com/10.1007/978-3-319-91086-4>
- Publication: *Springer International Publishing* (2019)
- Authors: Michel Gendreau; Jean-Yves Potvin
- Companion metadata note: [[_papers/gendreau2019handbook/gendreau2019handbook.md]]

## Related

- [[concepts/tabu-search]]
- [[concepts/variable-neighborhood-search]]
- [[concepts/large-neighborhood-search]]
- [[concepts/parallel-metaheuristics-cooperative-search]]
- [[concepts/hyper-heuristics]]
- [[references/montemanni2024-pdsvrp-collective-drones]]
- [[concepts/pdsvrp-c]]
- [[_papers/ropke2006adaptive/ropke2006adaptive-extracted]]
- [[_papers/lourenco2019iterated/lourenco2019iterated-extracted]]
- [[_papers/pisinger2019large/pisinger2019large-extracted]]
- [[concepts/large-neighborhood-ship-pair-destroy-repair]]
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]]
- [[references/goel2015-constraint-programming-lng-ship-scheduling]]

## Open Questions

- Which handbook patterns transfer best to collaborative truck-drone routing without heavy retuning?
- What communication policy gives the best robustness/compute trade-off in cooperative search for large VRP variants?

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
- [[_papers/gendreau2019handbook/gendreau2019handbook.md]]
- [[_papers/gendreau2019handbook/images/page_20_image_3.jpg]]
- [[_papers/gendreau2019handbook/images/page_20_image_4.jpg]]
- [[_papers/gendreau2019handbook/images/page_26_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_47_image_7.jpg]]
- [[_papers/gendreau2019handbook/images/page_85_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_123_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_257_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_115_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_117_image_2.jpg]]
