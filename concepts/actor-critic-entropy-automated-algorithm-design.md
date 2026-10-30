---
title: Actor-Critic RL for Automated Algorithm Design
summary: A dual-critic actor-critic (ACE) method that learns which evolutionary-search components a hyper-heuristic should pick, using entropy-maximising rewards.
tags: [reinforcement-learning, automated-algorithm-design, hyper-heuristics, actor-critic, entropy, deep-rl, max-entropy]
provenance:
  extracted_paper_extracted_md: 0.85
  extracted_paper_sidecar: 0.10
  author_synthesis: 0.05
base_confidence: 0.67
tier: supporting
category: concepts
created: 2026-10-29T18:10:00Z
updated: 2026-10-30T14:08:41Z
lifecycle: draft
lifecycle_changed: 2026-10-29
sources:
- _papers/yi2023automated/yi2023automated-extracted.md
- _papers/yi2023automated/yi2023automated.md
- _papers/yang2022vrpdbi-levelhyper-heatroutingdimension/_papers/yang2022vrpdbi-levelhyper-heatroutingdimension-extracted.md
- _papers/xinyingchen2023guide/_papers/xinyingchen2023guide-extracted.md
- _papers/ganjia2026multio/multi-objective sustainable supply chain scheduling for electric freight ride-sharing via a memetic algorithm with q-learning guidance.md
relationships:
  - target: '[[concepts/metaheuristic-hybridization]]'
    type: uses
  - target: '[[concepts/state-features-rl-algorithm-design]]'
    type: related_to
  - target: '[[concepts/entropy-coefficient-adjustment-schemes]]'
    type: related_to
  - target: '[[concepts/rl-component-analysis-designed-algorithms]]'
    type: related_to
  - target: '[[concepts/hyper-heuristics]]'
    type: related_to

---

# Actor-Critic RL for Automated Algorithm Design
## What it is
- The ACE method (Yi & Qu, Information Sciences 2023, DOI 10.1016/j.ins.2023.119639) formulates automated algorithm design as an MDP whose action chooses **one operator and one heuristic** from the selection, crossover, mutation and replacement stages of a generic search framework.  #automated-algorithm-design  #hyper-heuristics
- The state consists of search-dependent and instance-dependent information (see [[concepts/state-features-rl-algorithm-design]]); an **entropy term** is added to the reward, following the maximum-entropy RL interpretation ^[inferred] and the coefficient schemes in [[concepts/entropy-coefficient-adjustment-schemes]].  #max-entropy
- Two critics estimate the advantage of each action; replay is used for the actor and critic updates; the target networks update softly with `τ` close to 1.  #actor-critic  #deep-rl
- Haarnoja, Zhou, Abbeel & Levine, "Soft actor-critic: Off-policy max entropy deep RL with a stochastic actor", arXiv 2018, the soft-update mechanism. ^[extracted, p. 12]  #max-entropy  #actor-critic
- Beullens, Pereira, Van Den Bussche & Shavit, "A review of deep RL methods for language modeling", arXiv 2021, the entropy-maximising RL view. ^[extracted, p. 12]  #max-entropy  #deep-rl
- Ye, Si & Lam, "Deep RL for automated algorithmic components design in hyper-heuristics: A new representation and model", IEEE CEC 2020, 1-8, the prior hyper-heuristic design work. ^[extracted, p. 12]  #hyper-heuristics
- The ACE loop: observe state → choose components → run a search phase → compute reward → update actor and critics, iterating `t ← t+1` until the stopping criterion. ^[extracted, Algorithm 1, p. 12]  #automated-algorithm-design
- The policy then drives a hyper-heuristic over the `O_E`/`H_SE`/`H_SR` design space of `references/yi2023-ace-gsf-automated-design-cvrptw.md`, and is tested on the CVRPTW.  #hyper-heuristics  #reinforcement-learning
- RL agents learn to generate new algorithms. ^[inferred]  #automated-algorithm-design
- The closest structural relative is [[concepts/metaheuristic-hybridization]]: the RL policy chooses the operators and heuristics that the hybrid literature fixed by hand — Yang & Ha (2022) bilevel design, Eiben, Gendreau & Ganjia (2025) search-space design, and Ganjia et al. (2026) q-learning-guided memetic search. ^[synthesized, Q007]  #hyper-heuristics  #automated-algorithm-design
- Chen & Hooker (2023) `references/xinyingchen2023guide` frames the same goal in its ML track, i.e. learning to design algorithms. ^[synthesized, Q007]  #automated-algorithm-design
## Related pages
- [[concepts/metaheuristic-hybridization]] — the closest structural relative: the RL policy chooses the operators and heuristics that the hybrid literature fixed by hand (Yang & Ha 2022 bilevel design, Eiben, Gendreau & Ganjia 2025 search-space design, Ganjia et al. 2026 q-learning-guided memetic search).
- [[concepts/state-features-rl-algorithm-design]] — the state ACE observes.
- [[concepts/entropy-coefficient-adjustment-schemes]] — how the entropy coefficient is set.
- [[concepts/rl-component-analysis-designed-algorithms]] — analysing which components the policy calls.

## Sources

- `_papers/yi2023automated/yi2023automated-extracted.md`
- `_papers/yi2023automated/yi2023automated.md`
- `_papers/yang2022vrpdbi-levelhyper-heatroutingdimension/_papers/yang2022vrpdbi-levelhyper-heatroutingdimension-extracted.md`
- `_papers/xinyingchen2023guide/_papers/xinyingchen2023guide-extracted.md`
- `_papers/ganjia2026multio/multi-objective sustainable supply chain scheduling for electric freight ride-sharing via a memetic algorithm with q-learning guidance.md`
