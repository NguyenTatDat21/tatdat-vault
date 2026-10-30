---
title: Entropy Coefficient Adjustment Schemes
summary: Three ways to set the entropy coefficient in an actor-critic design agent — fixed, linear decay, and a neural-network learned scheme — differ in final cost, speed, and how late they keep exploring.
tags: [reinforcement-learning, hyper-heuristics]
provenance:
  extracted_paper_extracted_md: 0.85
  extracted_paper_sidecar: 0.05
  author_synthesis: 0.10
base_confidence: 0.87
tier: supporting
category: concepts
created: 2026-10-29T18:10:00Z
updated: 2026-10-30T17:41:00Z
lifecycle: draft
lifecycle_changed: 2026-10-29
relationships:
  - target: '[[references/yi2023-ace-gsf-automated-design-cvrptw]]'
    type: related_to
  - target: '[[references/yang2022-vrpd-bilevel-heuristic]]'
    type: related_to
  - target: '[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]'
    type: related_to
  - target: '[[concepts/actor-critic-entropy-automated-algorithm-design]]'
    type: related_to
sources:
  - "[[_papers/yi2023automated/yi2023automated-extracted.md]]"
  - "[[_papers/yi2023automated/yi2023automated.md]]"
  - "[[_papers/yang2022solving/yang2022solving-extracted.md]]"
  - "[[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md]]"

---

# Entropy Coefficient Adjustment Schemes

## The schemes
- **FS (fixed scheme)** — `α = 0.5` constant. ^[extracted, p. 12]  #max-entropy
- **LAS (linear adjustment scheme)** — `α_t+1 = α_t · 0.9998` over 10^4 steps, so α reaches ≈3.7 at step 10^4.  ^[extracted, p. 12]  #schedules
- **NLAS (non-linear adjustment scheme)** — a NN with two hidden layers adjusts the coefficient, using the entropy of the last 30 steps as input. ^[extracted, p. 12]  #learning
- NLAS is a two-hidden-layer NN that adjusts the coefficient from the entropy of the last 30 steps, using the ACE feature set as its input.  #learning
## Measured behaviour
- NLAS reaches the lowest training cost in the fewest iterations, then FS, then LAS; the final performance of FS, LAS and NLAS is close. ^[extracted, p. 17]  #entropy
- NLAS keeps exploring for more iterations than LAS, i.e. its entropy drops later (p. 17, Figure 7), so the high-entropy phase is longer. ^[extracted, p. 17]  #exploration
- In the 10,000-step training plots the entropy curves for the three schemes look similar and are not interpreted, i.e. no entropy analysis.  #entropy
- The entropy term is `r_π = r + α·H[π]` (Eq. 1), so the coefficient trades exploration against exploitation. ^[extracted, p. 12]  #max-entropy
- Yang & Ha (2022) `ε = 1.0 → 0.1` over 600,000 iterations, 375,000 in the first phase, 200,000 in the second; `ε_t = 1.0 − 0.9·(t−1)/180000` (Eq. 13). ^[extracted, p. 5]  #schedules
- Ganjia et al. (2026) `ε = 0.9 → 0.1`, `α = 0.01 → 0.03`, 470 episodes. ^[extracted, p. 17]  #schedules
- Chen & Hooker (2023) `references/xinyingchen2023guide` treat schedules as hyperparameter choices in its ML track. ^[synthesized, Q007]  #hyperparameters
## Related pages
- [[references/yi2023-ace-gsf-automated-design-cvrptw]] — ACE's three schemes.
- [[references/yang2022-vrpd-bilevel-heuristic]] — the ε-schedule.
- [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]] — ε and α schedules.

## Sources

- `_papers/yi2023automated/yi2023automated-extracted.md`
- `_papers/yang2022solving/yang2022solving-extracted.md`
- `_papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md`
