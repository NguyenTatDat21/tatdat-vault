---
title: >-
  Generative Adversarial Self-Imitation Learning (GASIL)
category: concepts
tags: [reinforcement-learning, imitation-learning, adversarial-training, reward-shaping, modeling-pattern]
relationships:
  - target: "[[references/guo2018-generative-adversarial-self-imitation-learning]]"
    type: derived_from
  - target: "[[concepts/inverse-soft-q-imitation-learning]]"
    type: related_to
  - target: "[[references/garg2022-iq-learn-inverse-soft-q]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: related_to
  - target: "[[references/silver2018-alphazero-self-play-general-rl]]"
    type: related_to
    note: "Reciprocal - references/silver2018-alphazero-self-play-general-rl references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/guo2018generative/guo2018generative-extracted.md
  - _papers/guo2018generative/guo2018generative.md
summary: >-
  Adversarial self-imitation: discriminate the agent's own top-K past trajectories; the discriminator reward r − alpha·log D added to the policy gradient fixes sparse-reward credit assignment.
provenance:
  extracted: 0.85
  inferred: 0.13
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25T19:48:00Z
tier: core
created: 2026-10-25T19:48:00Z
updated: 2026-10-30T14:39:22Z
---

# Generative Adversarial Self-Imitation Learning (GASIL)

> [!tldr] A generator–discriminator loop where the generator is the agent's own policy and the training set is the agent's top-K past trajectories. The learned discriminator becomes an internal dense reward, filling the credit-assignment gap left by sparse or delayed environment rewards.

## When It Applies

Sparse-reward RL settings: reward at episode end only, hard-to-reach goals, no expert available (BC/GAIL need demonstrations; SIL needs prior trajectories). GASIL needs neither — its "expert" is the agent's own best past behavior. ^[inferred]

## Procedure

1. Keep a buffer $B$ of the top-K episodes by return $R=\sum_t\gamma^t r_t$.
2. Train discriminator $D_\phi$ to separate current-policy trajectories from buffer trajectories (JS form):
$$\max_\phi\ \mathbb{E}_{\tau_\pi}[\log D_\phi]+\mathbb{E}_{\tau_E}[\log(1-D_\phi)]$$
3. Score state–action pairs by $\log D_\phi(s,a)$ and add as reward, e.g. PPO with $r^\alpha=r-\alpha\log D_\phi(s,a)$; the policy gradient with discriminator advantage $Q(s,a)=\mathbb{E}[\log D_\phi\mid s_0=s,a_0=a]$ guides exploration beyond the environment reward.
4. Tune two knobs hard: buffer size (quality vs quantity — 500 and 5000 steps both fail in the 2D point-mass study) and discriminator updates per policy batch (too few and too many both hurt).

## Why It Matters

The discriminator is a learned proxy of the task: it concentrates reward where good behavior lives, so exploration is guided by the agent's own history. The pattern generalizes adversarial imitation (GAIL) to self-imitation, matching contemporaneous findings by Gangwani et al. (2018) and linking to optimal reward learning (Singh et al., Sorg et al.). ^[inferred]

## Limitations & Open Questions

- Deterministic environments are assumed for the policy-improvement guarantee; stochastic settings show larger empirical gains (Walker2d noise) without the guarantee. ^[inferred]
- Non-stationary buffer: as the policy improves, the discriminator is trained against a moving target — sample efficiency beats SIL here, stability is open.
- Hyperparameters (α, buffer, updates/batch) are task-sensitive; the paper gives a Humanoid schedule (α=0 then 0.02) as one worked example. ^[inferred]

## Related

- [[references/guo2018-generative-adversarial-self-imitation-learning]]
- [[concepts/inverse-soft-q-imitation-learning]] — an objective-derived internal reward for self-imitation, no adversary
- [[references/garg2022-iq-learn-inverse-soft-q]]
- [[references/gendreau2019-handbook-metaheuristics]] — metaheuristic analogue: reuse your own best past solutions
- [[references/shaabani2023-multiproduct-mirp-matheuristic]] — Phase 1 of that matheuristic is an SA loop; its parameters were tuned by a Taguchi L27(3⁶) design
- [[references/silver2018-alphazero-self-play-general-rl]] — self-play generates all training data, with no expert demonstrations

## Sources

- [[_papers/guo2018generative/guo2018generative-extracted.md]]
- [[_papers/guo2018generative/guo2018generative.md]]
