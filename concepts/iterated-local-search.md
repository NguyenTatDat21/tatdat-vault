---
title: >-
  Iterated Local Search (ILS)
category: concepts
tags: [metaheuristic, iterated-local-search, local-search, perturbation, acceptance-criterion, double-bridge, tsp, qap, pfsp, framework, vns, matheuristic]
relationships:
  - target: "[[references/lourenco2019iterated]]"
    type: derived_from
  - target: "[[references/mbiadousaleu2022parallel]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/tabu-search]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
sources:
  - _papers/lourenco2019iterated/lourenco2019iterated-extracted.md
  - _papers/lourenco2019iterated/lourenco2019iterated.md
summary: >-
  ILS: walks the reduced space of local optima by perturbing the incumbent, re-running local search, and accepting by a rule; quality hinges on perturbation strength and acceptance criterion.
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T00:51:06Z
tier: supporting
created: 2026-10-26T00:51:06Z
updated: 2026-10-27T06:00:00Z
---

# Iterated Local Search (ILS)

> [!tldr] ILS is a single-chain metaheuristic that walks the reduced space `S*` of local optima produced by a black-box local search: perturb the incumbent, re-run local search, accept by a rule. Two points make an algorithm ILS: a single chain is followed (population methods excluded), and the search happens in the reduced space defined by the output of the heuristic.

## Framework

```
s_0 = GenerateInitialSolution
s* = LocalSearch(s_0)
repeat
    s' = Perturbation(s*, history)
    s*' = LocalSearch(s')
    s* = AcceptanceCriterion(s*, s*', history)
until termination condition met
```

Perturbations must be neither too small (the local search falls back to `s*`) nor too large (the method degenerates into random restart). The canonical TSP perturbation is the **double-bridge** move — four edges cut and reconnected, undoable by neither 2-opt, 3-opt, nor most Lin–Kernighan searches. Acceptance criteria span a spectrum: **Better** (accept only improvements), **Random Walk (RW)** (accept always), **LSMC** (accept worse with probability `exp((C(s*) − C(s*′))/T)` — simulated annealing on `S*`, see [[concepts/simulated-annealing-metropolis-cooling]]), and **Restart** (start from a new initial solution after `i_r` non-improving iterations).

## Speed effect

From a random start, `O(n)` local changes are needed to reach a local optimum, while after a double-bridge perturbation a nearly constant number of changes suffices — so ILS samples far more local optima per CPU second. Table 2 of [[references/lourenco2019iterated]] (3-opt with don't-look bits, 120 s): kroA100 17,507 local searches with random restart vs 56,186 with ILS; on rl5915, 34 vs 8,820 — 260× more. Acceptance quality (average % above optimum, fl3795): random restart 38.8, RW 1.87, Better 0.58; on rl5915: 6.90 / 2.13 / 0.66.

## Design rules and variants

- Perturbation strength for QAP is instance-dependent; best sizes alter up to 75% of solution components; strength `n` equals random restart.
- Basic VNS ([[concepts/variable-neighborhood-search]]) = ILS with Better acceptance and systematically varying perturbation strength over ordered neighborhoods `N_1,…,N_m`.
- The tabu-search "shakeup" ([[concepts/tabu-search]]) plays the same perturbation role.
- Rule of thumb: "a good perturbation transforms one excellent solution into an excellent starting point for a local search"; prefer many small perturbations over one large one for diversification.
- Names with the same essence: iterated descent, large-step Markov chains (LSMC), iterated Lin-Kernighan, chained local optimization.

## Applications

TSP (iterated Lin-Kernighan, Concorde's chained LK, Helsgaun's LKH, Merz–Huhse for millions of cities), the VRP family (prize-collecting, time-penalty, heterogeneous fleets, backhauls, split delivery, two-echelon LRP, bike rebalancing, matheuristic + column generation), scheduling (SMTWTP dynasearch, PFSP/iterated greedy, job shop, shifting-bottleneck GLS), QAP population-based ILS, MAX-SAT reactive search, Kernighan–Lin bipartitioning, continuous optimization, SimILS for stochastic problems, and ParamILS itself (an ILS over parameter space). A concrete ILS instantiation for vehicle-drone delivery is the PDSMTSP heuristic of [[references/mbiadousaleu2022parallel]] (improved-only acceptance, tie-break by sum of resource durations, giant-tour rebuild as learning mechanism).

## Related

- [[references/lourenco2019iterated]] — the canonical framework chapter (Handbook of Metaheuristics, chapter 5, DOI 10.1007/978-3-319-91086-4_5)
- [[references/gendreau2019-handbook-metaheuristics]] — the volume hosting the chapter
- [[references/mbiadousaleu2022parallel]] — ILS applied to PDSMTSP, citing the chapter
- [[concepts/variable-neighborhood-search]] — VNS as ILS with varying neighborhoods
- [[concepts/tabu-search]] — shakeup as perturbation
- [[references/stalhane2012-construction-improvement-lng-adp]] — five-operator first-improvement local search inside a deterministic multi-start construction of an LNG delivery program
- [[concepts/simulated-annealing-metropolis-cooling]] — LSMC acceptance

## Sources

- [[_papers/lourenco2019iterated/lourenco2019iterated-extracted.md]]
- [[_papers/lourenco2019iterated/lourenco2019iterated.md]]
