---
title: >-
  Simulated Annealing: Metropolis Acceptance and Cooling
category: concepts
tags: [simulated-annealing, metaheuristics, acceptance-criterion, markov-chains, cooling-schedules]
relationships:
  - target: "[[references/gendreau2019-handbook-metaheuristics.md]]"
    type: derived_from
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
summary: >-
  Simulated annealing as the handbook frames it: Metropolis acceptance as a probability, control-parameter cooling as the exploration dial, and acceptance-rate monitoring as the practical tuning signal.
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-24T04:37:31Z
updated: 2026-10-24T04:37:31Z
---

# Simulated Annealing: Metropolis Acceptance and Cooling

Chapter 1 (Vanier, Melonim & Taieb) treats SA as the method for **black-box global optimization** where the objective can only be evaluated through costly simulation — the case where population-based algorithms are inapplicable because evaluating a full population is too expensive. SA's main advantage is simplicity; it escapes Monte-Carlo local-minimum trapping via the Metropolis acceptance criterion, in analogy with physical annealing.

## Core Structure

- **State space** $U$ of feasible states, $E$ energy = objective, $u^*$ optimal state ($E(u^*) \le E(u)$ for all $u$).
- **Boltzmann distribution** gives the probability of a state $i$ with energy $E_i$ at temperature $T$.
- **Definition 5 — acceptance criterion:** accepting solution $j$ from current $i$ is a **probability** (Metropolis criterion).
- **Definition 6 — transition:** generation + acceptance. A Markov-chain transition corresponds to a **move** in the state space.
- **Control parameter $c$:** high $c$ accepts high degradation and explores thoroughly; as $c$ decreases, only improving and low-degradation transitions are accepted; as $c \to 0$, SA behaves like Monte Carlo.
- **Definition 9 — acceptance rate** $\chi(c)$ = accepted transitions / proposed transitions. $\chi(c)\approx 1$ at high $c$; it falls to 0 as $c$ decreases, and **$\chi(c) \approx 0.5$ as $c$ approaches the target $c_t$** — the practical tuning signal.
- **Theorem 1 (statistical equilibrium):** after a sufficient number of transitions at fixed $c$, the state distribution matches the Boltzmann distribution — i.e. the chain reaches equilibrium.
- **Asymptotic convergence** (S2) is proved with Markov chain theory; **S3** covers practical issues: finite-time approximation, polynomial-time cooling, Markov chain length, stopping criteria, and simulation-based evaluations.
- **S4** applies SA to the knapsack problem, the TSP, and a **real aircraft trajectory-planning problem at European continental scale with nearly 30,000 flights** — the case where the objective is a simulation.
- **Objective-value distribution $q(c)$** shifts as transitions are rejected at lower temperature (Fig. 1.2): the population of accepted values tightens around improvements.

```
SA loop:
  propose move (generation)
  accept with probability p(j from i)     # Metropolis
  track chi(c) = accepted / proposed
  cool c; stop when chi(c) collapses toward 0 near c_t
```

The LNS + SA combination is this acceptance rule applied to a **complex neighborhood**: the destroy/repair step proposes a large jump, and SA decides acceptance. The handbook's LNS chapter notes this hybrid (and the Goel LNG LNS uses SA acceptance in the same way). ^[extracted]

![[_papers/gendreau2019handbook/images/page_20_image_3.jpg]]
*Fig. 1.2 (handbook, PDF p. 21): the objective-value distribution $q(c)$ shifting as transitions are rejected at lower temperature — the annealing curve, quoted in the chapter's SA introduction.*

## Why It Matters

- Acceptance rate is the measurable dial: $\chi(c)\approx 0.5$ near the target temperature gives a concrete schedule-tuning target, so cooling schedules can be validated empirically instead of copied. ^[extracted]
- It frames SA as the *simulation-cost* method: when evaluating one solution is expensive, population methods are unusable, and SA is the standard choice. ^[extracted]
- The equilibrium + convergence theory separates what SA guarantees (asymptotic) from what it delivers in finite time (approximation), which is exactly the gap LNS+SA operates in.
- It gives the vocabulary for comparing acceptance rules in ALNS (Simou/Arese/Temp) against the Metropolis criterion. ^[inferred]
- It sets expectations for real applications: SA is validated on continental-scale trajectory planning, so "SA is too simple for industrial problems" is not a supported claim.
- The Markov-chain view (transition = generation + acceptance) makes the chain length a tunable parameter per temperature, not an implementation detail.

## Related

- [[references/gendreau2019-handbook-metaheuristics.md]]
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
