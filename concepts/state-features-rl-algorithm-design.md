---
title: State Features for RL-Based Algorithm Design
summary: The state an RL design agent observes — search-dependent and instance-dependent features — is the interface that lets a policy pick operators and heuristics per instance.
tags: [reinforcement-learning, state-features, instance-features, automated-algorithm-design, hyper-heuristics, representation]
provenance:
  extracted_paper_extracted_md: 0.80
  extracted_paper_sidecar: 0.10
  author_synthesis: 0.10
base_confidence: 0.77
tier: supporting
category: concepts
created: 2026-10-29T18:10:00Z
updated: 2026-10-30T19:38:37Z
lifecycle: draft
lifecycle_changed: 2026-10-29
sources:
  - "[[_papers/yi2023automated/yi2023automated-extracted.md]]"
  - "[[_papers/yi2023automated/yi2023automated.md]]"
  - "[[_papers/ganjia2026multiobjective/ganjia2026multiobjective-extracted.md]]"
  - "[[_papers/ganjia2026multiobjective/ganjia2026multiobjective.md]]"
relationships:
  - target: '[[references/yi2023-ace-gsf-automated-design-cvrptw]]'
    type: related_to
  - target: '[[references/yang2022-vrpd-bilevel-heuristic]]'
    type: related_to
  - target: '[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]'
    type: related_to
  - target: '[[concepts/actor-critic-entropy-automated-algorithm-design]]'
    type: related_to

---

# State Features for RL-Based Algorithm Design

## The design state
- ACE (Yi & Qu, 2023) keeps the state simple, i.e. search-dependent and instance-dependent information.  #state-features  #automated-algorithm-design
- Search-dependent features are the count of consecutive calls to the same operator, the number of calls in the last `l` steps, and the mean objective in the last `l` steps, computed over a window `l`. ^[extracted, p. 12]  #state-features
- Instance-dependent features are the time-window density, the number of customers, capacity, fleet size, distance factor, and capacity utilisation, computed offline from the instance. ^[extracted, p. 12]  #instance-features
- The state features are listed as `n_1`…`n_10` plus `o_bar`, `T`, `C`, `Q`, `q` in `references/yi2023-ace-gsf-automated-design-cvrptw.md`.  #automated-algorithm-design
- Yang & Ha (2022) compute the state from the current solution `s`, the current best solution, and the current generation `t`. ^[extracted, p. 5]  #reinforcement-learning
- Ganjia et al. (2026) use `f = [N, U, T, S]` — customers, capacity used, duration, load — with 470 episodes and `ε = 0.9 → 0.1`, `α = 0.01 → 0.03`. ^[extracted, p. 17]  #q-learning
- Chen & Hooker (2023) `references/xinyingchen2023guide` frames feature engineering for learning-augmented optimisation in its ML track. ^[synthesized, Q007]  #instance-features

## Why features matter
- A richer state lets the policy condition on the instance, so the same learned agent transfers across instance classes: the ACE policy learned on R-type narrow-window instances generalises to C-type and RC-type instances with GAP 0 on C101 and C201. ^[synthesized, Q007]  #transfer
- The state is deliberately kept small, so the design state can be computed online without a heavy feature pipeline. ^[inferred]  #representation
## Related pages
- [[references/yi2023-ace-gsf-automated-design-cvrptw]] — the ACE state features.
- [[references/yang2022-vrpd-bilevel-heuristic]] — state from current solution, best solution, generation.
- [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]] — q-learning state `[N, U, T, S]`.

## Sources

- `_papers/yi2023automated/yi2023automated-extracted.md`
- `_papers/yang2022solving/yang2022solving-extracted.md`
- `_papers/ganjia2026multio/ganjia2026multio.md`
