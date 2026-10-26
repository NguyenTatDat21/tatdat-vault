---
title: Large Neighborhood Search (Handbook of Metaheuristics chapter)
category: references
tags: [metaheuristics, lns, alns, vlsn, variable-neighborhood-search, hyper-heuristics, vehicle-routing, adaptive-weights]
relationships:
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: derived_from
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[references/pham2023-efficient-ga-quadratic-tsp]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
sources:
  - _papers/pisinger2019large/pisinger2019large-extracted.md
  - _papers/pisinger2019large/pisinger2019large.md
  - _papers/pisinger2019large/images/page_3_image_2.jpg
  - _papers/pisinger2019large/images/page_5_image_2.jpg
  - _papers/pisinger2019large/images/page_8_image_2.jpg
  - _papers/pisinger2019large/images/page_14_image_2.jpg
summary: >-
  The canonical LNS/ALNS chapter: LNS pseudocode, destroy-repair design principles, very-large-scale neighborhood classes, adaptive operator weights with roulette-wheel selection, and a survey of VRP, scheduling, and parallel-LNS applications.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T14:33:00Z
updated: 2026-10-26T12:26:00Z
---

# Large Neighborhood Search (Handbook of Metaheuristics chapter)

> [!tldr] LNS samples a destroy-and-repair neighborhood instead of searching it; ALNS adapts destroy/repair selection with scored weights; VLSN neighborhoods (variable-depth, network-flow, polynomial special cases) are the three families of very-large neighborhoods, and the chapter warns that small neighborhoods searched often can match large ones searched rarely.

## Problem & Motivation

Neighborhood search on local structures (2-opt, O(n²)) cannot reach distant regions of a constrained search space. Shaw (1998) proposed LNS: destroy part of a solution, repair it, implicitly defining a neighborhood N(x) = all solutions reachable from x by one destroy followed by one repair. Very-large-scale neighborhood (VLSN) methods (Ahuja et al. 2002, Discrete Applied Mathematics 123:75-102) exploit neighborhoods that grow exponentially, defined by structures whose best solution can be found in polynomial time. The chapter is the canonical reference for destroy/repair design, the ALNS adaptive mechanism, and the VLSN taxonomy.

![[_papers/pisinger2019large/images/page_3_image_2.jpg]]

*Fig. 1 Left: a TSP solution. Right: A CVRP solution. In the CVRP the depot is marked with a square and the customers i are marked with nodes each having a demand q_i*

## Method / Architecture

LNS loop (Algorithm 1): x^b = x; repeat x^t = r(d(x)); if accept(x^t, x) then x = x^t; if c(x^t) < c(x^b) then x^b = x^t; until stop; return x^b.

- **Destroy degree is the key knob**: too small loses exploration, too large degrades to repeated re-optimization. Shaw increases the degree gradually; Ropke & Pisinger ([[references/ropke2006-adaptive-large-neighborhood-search-pdptw|2006, Transportation Science 40(4):455-472]]) choose it randomly in a range that depends on instance size. Destroy must be able to reach the whole search space; e.g., removing 15% of 100 CVRP customers = C(100,15) ≈ 2.5×10¹⁷ removal choices.
- **Acceptance**: Shaw accepted improving solutions only; Ropke & Pisinger and Schrimpf add simulated annealing — accept if c(x^t) ≤ c(x), else with probability exp(−(c(x^t)−c(x))/T), T_new = αT_old, 0 < α < 1 — making LNS standard SA on a complex neighborhood.
- **Repair** can be optimal (slow, weak diversification) or heuristic; MIP/CP solvers act as general repair; the fix/optimize reading: destroy fixes a partial solution, repair re-optimizes; decomposable problems (master + subproblems) suit LNS, echoing Dantzig-Wolfe candidate generation. Ruin-and-recreate (Schrimpf et al. 2000, J. Comput. Phys. 159(2):139-171) is the near-identical framework.
- **ALNS** selects destroy methods from Ω⁻ and repair methods from Ω⁺ by roulette wheel, weights ρ init 1, \(\phi_j^- = \rho_j^-/\sum_k \rho_k^-\); per-iteration score ψ = max{ω1 global best, ω2 better than current, ω3 accepted, ω4 rejected} (Eq. 1, ω1≥ω2≥ω3≥ω4≥0); Eq. (2) update \(\rho_a^- = \lambda\rho_a^- + (1-\lambda)\psi\), λ ∈ [0,1]; unused weights unchanged; normalize ψ by time consumption for slow operators.
- **VLSN classes**: (1) variable-depth search (Lin-Kernighan TSP: alternating edge insert/delete with greedy gain and freeze, no cycling; ejection chains, Glover 1992 domino cascades); (2) network-flow-based (cyclic-exchange neighborhood = negative-cost cycle in Thompson's improvement graph, NP-hard subset-disjoint cycle; path exchanges = compounded swaps solvable in O(n²) as shortest paths; assignment neighborhood Sarvanov & Doroshko 1981 for TSP, k = n/2; Franceschi et al. 2006 distance-constrained CVRP, 13 improved best-known solutions); (3) polynomially solvable special cases (Halin-graph TSP in linear time, Cornuejols et al. 1983; bottleneck TSP; Steiner).
- **Design inventory**: destroy families — random (diversification), worst/critical (intensification), related (Shaw's distance+demand relatedness), history-based (Pisinger & Ropke: count how often setting a variable leads to bad solutions); repair families — greedy, approximation, relaxed exact algorithms; noising/randomization for diversification; sequential vs parallel subproblem heuristics; coupled neighborhoods K_i ⊆ Ω⁺ per destroy, K_i = ∅ means one neighborhood doing both destroy and repair; equal-probability operators without adaptive weights are robust and need fewer parameters.
- **Properties**: ALNS is robust and instance-adaptive, seldom trapped in local optima, needs limited calibration. It is related to VNS (VNS orders predefined neighborhoods by complexity; ALNS picks from parameterized families with adaptive probabilities) and to hyper-heuristics (Ross: heuristics to choose heuristics — ALNS's adaptive layer is exactly that). Prior adaptive frameworks: Rousseau et al. 2002 (two LNS neighborhoods, VND switching), Perron 2003 (repair portfolios), Laborie & Godard 2007 (self-adapting LNS tuning sub-heuristic parameters), Palpant et al. 2004 (LSSPER), outer metaheuristics: descent, ILS, SA; parallel LNS: Perron & Shaw 2003, Ropke 2009 parallel ALNS tested on CVRP and TSP-PD.
- **Applications**: VRPTW is LNS's most-studied domain; Bent & Hentenryck (2004) two-stage — SA minimizing number of routes, then LNS with related destroy and truncated branch-and-bound repair minimizing lengths, improving-only acceptance, removal size reset to 1 periodically; same pattern for PDPTW. Ropke & Pisinger's ALNS for PDPTW is state-of-the-art, and CVRP/VRPTW transform into PDPTW, so ALNS carries across VRP variants; Prescott-Gagnon et al. (2007) branch-and-price with LNS repair, 4 destroy methods, beats previous LNS. Best VRPTW at time of writing: Nagata & Bräysy 2009, a non-LNS route minimization heuristic. Few LNS applications to TSP variants — LNS suits partitioning problems (VRP, bin packing, generalized assignment) better. Scheduling: Laborie & Godard single-mode, Godard/Laborie/Nuijten cumulative, Carchrae & Beck job-shop, Cordeau et al. 2009 technician scheduling (hundreds of tasks in <15 minutes), Muller 2009 RCPSP ALNS among three best on PSPLIB, ALNS for multi-item capacitated lot sizing with setup times.

![[_papers/pisinger2019large/images/page_5_image_2.jpg]]

*Fig. 2 Illustration of the neighborhoods used by VDNS and VNS. The current solution is marked x. VDNS typically operates on one type of neighborhood with variable depth, while VNS operates on structurally different neighborhoods N_1, ..., N_k*

![[_papers/pisinger2019large/images/page_8_image_2.jpg]]

*Fig. 3 Destroy and repair example. The top left figure shows a CVRP solution before the destroy operation. The top right figure shows the solution after a destroy operation that removed 6 customers (now disconnected from the routes). The bottom figure shows the solution after the repair operation has reinserted the customers.*

![[_papers/pisinger2019large/images/page_14_image_2.jpg]]

*Fig. 4 Illustration of neighborhoods used by ALNS. The current solution is marked with x. ALNS operates on structurally different neighborhoods N_1, ..., N_k defined by the corresponding search heuristics. All neighborhoods N_1, ..., N_k in ALNS are a subset of the neighborhood N* defined by modifying q variables, where q is a measure of the maximum degree of destruction.*

## Key Equations

- Eq. (1): operator score \(\psi=\max\{\omega_1,\omega_2,\omega_3,\omega_4\}\) mapped to outcome quality.
- Eq. (2): adaptive weight update \(\rho_a^- \leftarrow \lambda\rho_a^-+(1-\lambda)\psi\), \(\rho_b^+ \leftarrow \lambda\rho_b^++(1-\lambda)\psi\).
- Neighborhood definitions: x is a local optimum iff c(x) ≤ c(x′) ∀x′ ∈ N(x); the 2-opt neighborhood (Flood 1956) has size O(n²).

## Results / Conclusions

The chapter's synthesis: LNS is quick to assemble from existing components and good for benchmarking; it works best on problems with partitioning decisions (VRP, bin packing, generalized assignment); large neighborhoods give no guarantee, and fewer iterations per unit time must be paid for their reach; VLSN is not a magic bullet — small neighborhoods searched fast can match large ones (Brueggemann & Hurink; Hurink); Gutin & Karapetyan's multidimensional-assignment experiments show combining small and large neighborhoods beats either alone, so hybrid neighborhoods are the promising direction stated in the conclusion.

## Limitations

- **Date ambiguity**: the sidecar cites Pisinger & Ropke (2019), DOI 10.1007/978-3-319-91086-4_4, Handbook of Metaheuristics 3rd ed. (Gendreau ed., Springer); the extracted header cites Pisinger & Røpke (2010), 2nd ed., pp. 399-420. Same chapter, two editions; page facts follow the extracted text. ^[ambiguous]
- "State-of-the-art" claims in the applications section are frozen at the chapter's publication date.
- The chapter asserts design principles from experience (refs 40, 46), not from systematic comparison.

## Related

- [[concepts/large-neighborhood-search]] — the vault concept page is this chapter's core; this page carries the design inventory, applications, and VLSN families.
- [[references/gendreau2019-handbook-metaheuristics]] — the handbook volume containing this chapter.
- [[concepts/variable-neighborhood-search]] — VNS ordering vs ALNS roulette-wheel adaptation, the comparison the chapter makes explicit.
- [[concepts/hyper-heuristics]] — Ross's "heuristics to choose heuristics"; the ALNS adaptive layer is a hyper-heuristic.
- [[references/pham2023-efficient-ga-quadratic-tsp]] — ruin-and-recreate LNS operators embedded in a genetic algorithm for the QTSP; cites Ropke & Pisinger 2006.
- [[concepts/large-neighborhood-ship-pair-destroy-repair]] — LNS destroy defined by removing whole ship schedules, repair by re-solving a time-space MIP.
- [[concepts/adaptive-large-neighborhood-search-for-mip]] — the ALNS-for-MIP pattern this chapter underwrites.
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] — the PDPTW paper whose ALNS scheme the chapter systematizes.

## Sources

- [[_papers/pisinger2019large/pisinger2019large-extracted.md]]
- [[_papers/pisinger2019large/pisinger2019large.md]]
- Bibliographic record: Pisinger & Røpke, "Large Neighborhood Search", Handbook of Metaheuristics, Springer; sidecar DOI 10.1007/978-3-319-91086-4_4 (2019, 3rd ed.), extracted header pp. 399-420 (2010, 2nd ed., Gendreau ed.), DTU Orbit. Zotero PDF key 6ACZYHAX.