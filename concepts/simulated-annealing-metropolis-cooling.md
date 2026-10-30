---
title: >-
  Simulated Annealing: Metropolis Acceptance and Cooling
category: concepts
tags: [simulated-annealing, metaheuristics, acceptance-criterion, markov-chains, cooling-schedules]
relationships:
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: derived_from
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[concepts/drone-swarm-synchronization]]"
    type: related_to
    note: "Reciprocal - concepts/drone-swarm-synchronization references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[concepts/iterated-local-search]]"
    type: related_to
    note: "Reciprocal - concepts/iterated-local-search references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/li2024drone]]"
    type: related_to
    note: "Reciprocal - references/li2024drone references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/lourenco2019iterated]]"
    type: related_to
    note: "Reciprocal - references/lourenco2019iterated references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/nguyen2025set]]"
    type: related_to
    note: "Reciprocal - references/nguyen2025set references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
    note: "Reciprocal - references/ropke2006-adaptive-large-neighborhood-search-pdptw references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: related_to
    note: "Reciprocal - references/sacramento2019-vrp-d-truck-drone-alns-cost references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/santini2018-alns-acceptance-criteria]]"
    type: related_to
    note: "Reciprocal - references/santini2018-alns-acceptance-criteria references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/shaabani2023-multiproduct-mirp-matheuristic]]"
    type: related_to
    note: "Reciprocal - references/shaabani2023-multiproduct-mirp-matheuristic references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
summary: >-
  Simulated annealing as the handbook frames it: Metropolis acceptance as a probability, control-parameter cooling as the exploration dial, and acceptance-rate monitoring as the practical tuning signal.
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-24T04:37:31Z
updated: 2026-10-30T14:38:55Z
---

# Simulated Annealing: Metropolis Acceptance and Cooling

Chapter 1 (Delahaye, Chaimatanan & Mongeau) treats SA as the method for **black-box global optimization** where the objective can only be evaluated through costly simulation — the case where population-based algorithms are inapplicable because evaluating a full population over a large-dimension state space is too expensive. SA's main advantage is simplicity; it escapes the local-minimum trapping of the Monte-Carlo approach via the Metropolis acceptance criterion, in analogy with physical annealing.

## Core Structure

- **Notation** $(S, f)$: $S$ = set of feasible solutions, $f$ = objective to minimize; in the SA analogy $f$ plays the role of the solid's energy, and a **control parameter** $c$ with the same units as $f$ acts as a temperature. The physical Boltzmann probability $p_i = e^{-E_i/(k_b T)} / Z(T)$, $Z(T) = \sum_{j \in S} e^{-E_j/(k_b T)}$, motivates the acceptance rule.
- **Boltzmann distribution** gives the probability of a state $i$ with energy $E_i$ at temperature $T$.
- **Definition 5 — acceptance criterion:** for current $i$ and neighbor $j$, $\Pr\{accept\, j\} = 1$ if $f(j) < f(i)$, else $e^{(f(i)-f(j))/c}$ (Metropolis criterion).
- **Definition 6 — transition:** generation + acceptance. A Markov-chain transition corresponds to a **move** in the state space.
- **Control parameter $c$:** high $c$ accepts high degradation and explores thoroughly; as $c$ decreases, only improving and low-degradation transitions are accepted; as $c \to 0$, SA behaves like Monte Carlo.
- **Definition 9 — acceptance rate** $\chi(c)$ = accepted transitions / proposed transitions. $\chi(c)\approx 1$ at high $c$; it falls to 0 as $c$ decreases, and **$\chi(c) \approx 0.5$ as $c$ approaches the target $c_t$** — the practical tuning signal.
- **Theorem 1 (statistical equilibrium):** after a sufficient number of transitions at fixed $c$, the state distribution matches the Boltzmann distribution — i.e. the chain reaches equilibrium.
- **Asymptotic convergence** (§1.3.2) is proved with Markov chain theory; §1.4 covers practical issues: finite-time approximation, geometric cooling, cooling in polynomial time (initial temperature, decay of $c$, length of Markov chains, stopping criterion), and simulation-based evaluations.
- **§1.5–1.6** apply SA to the knapsack problem, the TSP, then deploy it on a real large-scale aircraft trajectory-planning problem involving **nearly 30,000 flights at European continental scale** — the case where the objective is a simulation.
- **Objective-value distribution $q(c)$:** at large $c$ this equals the objective distribution; at lower $c$ some transitions are not accepted, shifting $q(c)$ toward lower objective values (Fig. 1.2, verbatim: "Distribution of the objective function values at some high temperature $c_1$ and at a lower temperature $c_2$").

```
SA loop:
  propose move (generation)
  accept with probability p(j from i)     # Metropolis
  track chi(c) = accepted / proposed
  cool c; stop when chi(c) collapses toward 0 near c_t
```

The LNS + SA combination is this acceptance rule applied to a **complex neighborhood**: the destroy/repair step proposes a large jump, and SA decides acceptance. The handbook's LNS chapter notes this hybrid (and the Goel LNG LNS uses SA acceptance in the same way). ^[extracted]
The LNS + SA combination is this acceptance rule applied to a **complex neighborhood**: the destroy/repair step proposes a large jump, and SA decides acceptance — the handbook's LNS chapter says LNS with SA acceptance is standard SA with a complex neighborhood. Goel et al.'s ship-pair LNS keeps improving solutions only, i.e. the original hill-climber acceptance. ^[extracted]
![[_papers/gendreau2019handbook/images/page_20_image_3.jpg]]
*Fig. 1.1 (handbook, PDF p. 21, verbatim): "When the temperature is high, the material is in a liquid state (left). For a hardening process, the material reaches a solid state with non-minimal energy (metastable state; top right). In this case, the structure of the atoms has no symmetry. During a slow annealing process, the material reaches also a solid state but for which atoms are organized with symmetry (crystal; bottom right)" — the physical-annealing analogy behind SA.*

## Why It Matters

- Acceptance rate is the measurable dial: $\chi(c)\approx 0.5$ near the target temperature gives a concrete schedule-tuning target, so cooling schedules can be validated empirically instead of copied. ^[extracted]
- It frames SA as the *simulation-cost* method: when evaluating one solution is expensive, population methods are unusable, and SA is the standard choice. ^[extracted]
- The equilibrium + convergence theory separates what SA guarantees (asymptotic) from what it delivers in finite time (approximation), which is exactly the gap LNS+SA operates in.
- It gives the vocabulary for comparing acceptance rules in ALNS (Simou/Arese/Temp) against the Metropolis criterion. ^[inferred]
- It sets expectations for real applications: SA is validated on continental-scale trajectory planning, so "SA is too simple for industrial problems" is not a supported claim.
- The Markov-chain view (transition = generation + acceptance) makes the chain length a tunable parameter per temperature, not an implementation detail.

## Related

- [[references/gendreau2019-handbook-metaheuristics]]
- [[concepts/large-neighborhood-search]]
- [[concepts/adaptive-large-neighborhood-search-for-mip]]
- [[concepts/hyper-heuristics]]
- [[concepts/metaheuristic-hybridization]]
- [[concepts/large-neighborhood-ship-pair-destroy-repair]]

## Open Questions

- What Markov-chain length per temperature is enough, given finite-time approximation is the practical mode?
- Does $\chi(c)\approx 0.5$ at $c_t$ remain the right target for large-neighborhood proposals, where degradation magnitudes differ by orders of magnitude from local moves? ^[inferred]
- How much of the SA chapter's content is simulation-specific (costly objective), and how much transfers to cheap-objective routing? ^[ambiguous]

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
- [[_papers/gendreau2019handbook/gendreau2019handbook.md]]
- [[_papers/gendreau2019handbook/images/page_20_image_3.jpg]]
