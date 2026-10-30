---
title: >-
  Iterated Local Search: Framework and Applications (Lourenço, Martin & Stützle, 2019)
category: references
tags: [paper, metaheuristic, iterated-local-search, local-search, perturbation, acceptance-criterion, double-bridge, tsp, qap, pfsp, job-shop, handbook, chapter, framework]
relationships:
  - target: "[[concepts/iterated-local-search]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: derived_from
  - target: "[[references/mbiadousaleu2022parallel]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/tabu-search]]"
    type: related_to
  - target: "[[references/wang2019routing]]"
    type: related_to
sources:
  - _papers/lourenco2019iterated/lourenco2019iterated-extracted.md
  - _papers/lourenco2019iterated/lourenco2019iterated.md
  - _papers/lourenco2019iterated/images/page_3_image_0.jpg
  - _papers/lourenco2019iterated/images/page_6_image_0.jpg
  - _papers/lourenco2019iterated/images/page_9_chart_0.jpg
  - _papers/lourenco2019iterated/images/page_9_chart_1.jpg
  - _papers/lourenco2019iterated/images/page_11_image_0.jpg
summary: >-
  Handbook chapter defining ILS: walk over local optima via perturbation + acceptance; design rules for the four modules, speed advantage, applications, relations to other metaheuristics.
provenance:
  extracted: 0.94
  inferred: 0.03
  ambiguous: 0.03
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-29
tier: core
created: 2026-10-26T00:51:06Z
updated: 2026-10-30T14:39:22Z
---

# Iterated Local Search: Framework and Applications (Lourenço, Martin & Stützle, 2019)

> [!tldr] The canonical ILS chapter: ILS walks the reduced space `S*` of local optima by perturbing the incumbent, re-running the embedded local search, and accepting by a rule; quality hinges on perturbation strength and acceptance criterion, and ILS samples far more local optima per CPU second than random restart.

## Problem & Motivation

The chapter is chapter 5 of the Handbook of Metaheuristics (Springer, 2019, DOI 10.1007/978-3-319-91086-4_5). The chapter authors are Helena Ramalhinho Lourenço (Universitat Pompeu Fabra), Olivier C. Martin (INRA, Université Paris-Sud) and Thomas Stützle (ULB); the sidecar's creators list also contains the volume editors Michel Gendreau and Jean-Yves Potvin. `^[ambiguous]` Two points make an algorithm ILS: (i) a single chain is followed (population methods excluded); (ii) the search happens in the reduced space defined by the output of a black-box heuristic. Names with the same essence include iterated descent, large-step Markov chains (LSMC), iterated Lin-Kernighan, chained local optimization.

![[_papers/lourenco2019iterated/images/page_3_image_0.jpg]]
*Fig. 1 Probability densities of costs. The curve labeled s indicates the left tail of the cost density function for all solutions, while the curve labeled $s ^ {* }$ indicates the cost density function for the solutions that are local optima.* — the cost distribution for local optima has a much smaller mean/variance, so local search beats random sampling; random restart collapses on large instances.

## Method / Architecture

![[_papers/lourenco2019iterated/images/page_6_image_0.jpg]]
*Fig. 2 Pictorial representation of iterated local search. Starting with a local minimum $s ^ { * }$ we apply a perturbation leading to a solution $s ^ { \prime } .$ After applying LocalSearch, we find a new local minimum $s ^ { * \prime }$ that may be better than $s ^ { * }$*

The framework (Algorithm 1):

```
s_0 = GenerateInitialSolution
s* = LocalSearch(s_0)
repeat
    s' = Perturbation(s*, history)
    s*' = LocalSearch(s')
    s* = AcceptanceCriterion(s*, s*', history)
until termination condition met
```

Neighborhoods on `S*` are induced by intersecting basins of attraction, but listing them is intractable, so ILS samples `S*` by perturbing. Perturbations must be neither too small (fall back to `s*`) nor too large (becomes random restart). The canonical perturbation for the TSP is the **double-bridge** move: four edges cut, four reconnected, undoable by neither 2-opt, 3-opt nor most Lin-Kernighan searches.

![[_papers/lourenco2019iterated/images/page_11_image_0.jpg]]
*Fig. 4 Schematic representation of the double-bridge move. The four dotted edges are removed and the remaining parts A, B, $\mathrm { C } ,$ D are reconnected by the dashed edges.*

Acceptance criteria form a spectrum between the two extremes:

$$
\text{Better}(s^*, s^{*\prime}) = \begin{cases} s^{*\prime} & \text{if } \mathcal{C}(s^{*\prime}) < \mathcal{C}(s^*) \\ s^* & \text{otherwise} \end{cases}
\qquad
\text{RW}(s^*, s^{*\prime}) = s^{*\prime}
$$

LSMC accepts worse solutions with probability `exp((C(s*) − C(s*′))/T)` (simulated annealing on `S*`); Restart adds `s` from a new initial solution if no improvement for `i_r` iterations. Rule of thumb: "a good perturbation transforms one excellent solution into an excellent starting point for a local search", and prefer accepting numerous small perturbations over one large one when diversification is needed.

## Key Equations

- Acceptance Better (Eq. 1), RW (Eq. 2), Restart (Eq. 3) above; LSMC probability `exp{(C(s*) − C(s*′))/T}`.
- Speed effect: from a random start, `O(n)` local changes are needed to reach a local optimum, while after a double-bridge perturbation a nearly constant number of changes suffices — so ILS samples many more local optima per CPU second.
- Perturbation strength for QAP is instance-dependent: best sizes up to 75% of solution components altered; strength `n` equals random restart.
- Basic VNS = ILS with Better acceptance and systematically varying perturbation strength over ordered neighborhoods `N_1,…,N_m`.

## Results

- **Speed factor (Table 2)**, local searches per 120 s, 3-opt with don't-look bits, single double-bridge: kroA100 17,507 (random restart) vs 56,186 (ILS); rl5915 34 vs 8,820 — 260× more local searches on the largest instance; five simultaneous double-bridges sit between.
- **TSP acceptance quality (Table 3)**, average % over optimum: fl3795 — RR 38.8, RW 1.87, Better 0.58; rl5915 — RR 6.90, RW 2.13, Better 0.66; Better beats RW, both crush random restart.
- **QAP (Tables 1, 4)**: with Better only, a weak perturbation can be worse than random restart; adding RW/Restart acceptance rescues ILS (e.g. tai60b, n/2: Better 0.50, RW 0.14, Restart 0.07).
- **Initial solution (Fig. 3, PFSP instances ta051/ta056)**: NEH greedy starts win for short runs; over long runs the dependence fades; persistent dependence means the walk struggles to explore `S*`. ^[inferred]
- Applications surveyed: TSP (iterated Lin-Kernighan, Concorde chained LK, Helsgaun LKH, Merz–Huhse for millions of cities), VRP family (prize-collecting, time-penalty, heterogeneous fleet, backhauls, split delivery, multi-commodity multi-trip, two-echelon LRP, bike rebalancing, matheuristic + column generation), scheduling (SMTWTP dynasearch, PFSP/iterated greedy, job shop with subproblem re-optimization perturbations, shifting-bottleneck GLS), QAP population-based ILS as state of the art, MAX-SAT reactive search, graph bipartitioning (Kernighan–Lin with island exchanges), coloring, continuous optimization (Powell's method; Liao–Stützle competition winner), SimILS for stochastic problems, and ParamILS itself being an ILS over parameter space.

![[_papers/lourenco2019iterated/images/page_9_chart_0.jpg]]
![[_papers/lourenco2019iterated/images/page_9_chart_1.jpg]]
*Fig. 3 The plots show the average solution cost (makespan on the y-axis) as a function of CPU time (given on the x-axis) for an ILS algorithm applied to the PFSP on instances ta051 and ta056.*

## Limitations

Interdependencies between perturbation strength and acceptance criterion are "rarely completely understood"; the chapter calls for more work on memory, explicit intensification/diversification switching, and problem-specific tuning. Global optimization is approximated by successively optimizing each module; configurators (irace, ParamILS, SMAC) automate it.

## Related

- [[concepts/iterated-local-search]] — the distilled framework page
- [[references/gendreau2019-handbook-metaheuristics]] — the handbook volume this chapter belongs to
- [[references/mbiadousaleu2022parallel]] — ILS applied to PDSMTSP, citing this chapter [25]
- [[concepts/simulated-annealing-metropolis-cooling]] — LSMC acceptance is SA on `S*`
- [[concepts/variable-neighborhood-search]] — basic VNS as ILS with varying perturbation strength
- [[concepts/tabu-search]] — shakeup = perturbation, memory inspiration
- [[references/wang2019routing]] — HTDD uses ILS with segment-node abstraction, inter-route insertion/swap/2-opt*, accept-if-improved objective. ^[extracted]

## Sources

- [[_papers/lourenco2019iterated/lourenco2019iterated-extracted.md]]
- [[_papers/lourenco2019iterated/lourenco2019iterated.md]]
- [[_papers/lourenco2019iterated/images/page_3_image_0.jpg]]
- [[_papers/lourenco2019iterated/images/page_6_image_0.jpg]]
- [[_papers/lourenco2019iterated/images/page_9_chart_0.jpg]]
- [[_papers/lourenco2019iterated/images/page_9_chart_1.jpg]]
- [[_papers/lourenco2019iterated/images/page_11_image_0.jpg]]
