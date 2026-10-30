---
title: >-
  Transformer Sequence-to-Sequence Routing Solver
category: concepts
tags: [machine-learning, reinforcement-learning, operations-research, vehicle-routing]
relationships:
  - target: "[[references/fuertes2023-transformer-multi-uav-routing]]"
    type: derived_from
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/inverse-soft-q-imitation-learning]]"
    type: related_to
  - target: "[[references/garg2022-iq-learn-inverse-soft-q]]"
    type: related_to
  - target: "[[references/lu2024-hybrid-evolutionary-algorithm-sop]]"
    type: related_to
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
sources:
  - _papers/fuertes2023solving/fuertes2023solving-extracted.md
  - _papers/fuertes2023solving/fuertes2023solving.md
summary: >-
  An encoder-decoder neural policy that builds a routing solution node by node with masked attention and
  state-aware queries, trained by REINFORCE, giving near-MIP quality at millisecond inference.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-24T00:32:00Z
updated: 2026-10-30T17:47:00Z
---

# Transformer Sequence-to-Sequence Routing Solver

The construction recipe for neural routing policies (Kool et al. 2019 form, as instantiated by Fuertes et al. 2023). It is a sequence model over nodes, where the decoder's **query is the routing state**, not a positional embedding.

## Core Structure

- **Encoder**: linear embedding of node features (no positional encoding, unlike NLP), then stacked attention blocks of multi-head attention + linear embedding, each wrapped by a skip connection and batch normalization. $N=3$ stacks, $h=128$, $M=8$ heads.

$$
\text{Attention}(Q,K,V) = \text{SoftMax}\left(\frac{QK^T}{\sqrt{h/M}}\right)V
$$

- **Decoder**: **context embedding** of the current routing state — in the multi-UAV case the current node plus remaining time, so the budget is part of the query.
- **Masked multi-head attention** over the encoder output (Key/Value), with a mask marking visited and infeasible nodes.
- **Masked single-head attention** producing logits:

$$
\text{logits} = f_{mask}\left(C\cdot\tanh\left(\frac{Q'K'^T}{\sqrt{h}}\right)\right)
$$

$C=10$ clipping limits logit magnitude, $\tanh$ keeps logits in a bounded range, softmax turns them into a policy.
- **Training**: sample tours from the policy; REINFORCE gradient on cost $L(\nu) = -\sum r x$ with a **greedy-tour baseline** $b(\alpha)=\arg\max p_\theta(\nu|\alpha)$ for variance reduction; Adam.
- **Inference**: greedy decoding (argmax), one tour per agent; sub-millisecond for 20–200 nodes.
- **Shared network across agents** — agent identity enters only through the reward vector, not the architecture.
- **Metric pair for routing papers**: reward gap vs the best method, and $\log_{10}$ time gap vs the fastest method.

The masking mechanism is what makes a general-purpose sequence model a legal-move machine: the mask encodes constraints, so the model never emits an infeasible node. ^[inferred]

![[_papers/fuertes2023solving/images/page_4_image_3.jpg]]
*Fig. 3 (paper): encoder-decoder structure — linear embedding, attention stacks with skip + batch norm, context embedding, masked multi-head, masked single-head, softmax sampling.*

## Why It Matters

- It shifts the cost of solving to training time: inference is milliseconds, so routing becomes usable inside online planning loops where MIP time (108 ms at $n=200$, growing steeply) is not.
- It generalizes across instance sizes with one network, so a single trained model covers 20–200 nodes.
- State-aware queries let capacity/time constraints enter the policy directly, which the pointer-network form handles less cleanly. ^[inferred]
- It gives an accuracy/time frontier: ~0.1 reward gap vs the MIP at ~100× lower time, so the choice between MIP and learned policy is an explicit trade.
- It makes multi-agent routing tractable at fleet scale (4 agents, $n=100$), where exact solvers blow up.
- It provides the learned-solver baseline to compare against in routing papers, and the log-time metric standard. ^[inferred]
- It does not certify optimality: the gap is measured against a best-known-method benchmark, so a learned policy can be beaten by a better exact run without warning. ^[inferred]

## Related

- [[references/fuertes2023-transformer-multi-uav-routing]]
- [[concepts/set-orienteering-problem]]
- [[concepts/min-cost-parallel-drone-scheduling-vrp]]
- [[concepts/k-multi-visit-drone-routing-problem]]
- [[concepts/hyper-heuristics]]

## Open Questions

- Can the same masked-attention recipe handle heterogeneous per-agent constraints (payload, energy, time windows) in one network, as the paper's future work proposes? ^[inferred]
- Is a decoder that conditions on remaining time sufficient, or should fuel-consumption functions (nonlinear in speed) enter the state? ^[inferred]
- Do learned policies transfer to the instance families the vault's exact algorithms target, e.g. the [[concepts/large-neighborhood-search|LNS]]/MIP matheuristic setting? ^[inferred]

## Sources

- [[_papers/fuertes2023solving/fuertes2023solving-extracted.md]]
- [[_papers/fuertes2023solving/fuertes2023solving.md]]
- [[_papers/fuertes2023solving/images/page_4_image_3.jpg]]
