---
title: Minimizing Service and Operation Costs of Periodic Scheduling
category: references
tags: [periodic-scheduling, approximation-algorithms, operations-research]
relationships:
  - target: "[[concepts/periodic-scheduling-under-capacity-constraints]]"
    type: derived_from
  - target: "[[references/bar-noy2004-efficient-algorithms-periodic-scheduling]]"
    type: related_to
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
sources:
  - _papers/bar-noy2002minimizing/bar-noy2002minimizing-extracted.md
  - _papers/bar-noy2002minimizing/bar-noy2002minimizing.md
summary: >-
  Defines a generalized periodic-scheduling model balancing service and operating costs, proves hardness, and gives strong approximation algorithms with nonlinear-relaxation bounds.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T19:33:55Z
updated: 2026-10-30T17:41:00Z
---

# Minimizing Service and Operation Costs of Periodic Scheduling

> [!tldr] Unifies maintenance, replenishment, and broadcast-disk style periodic scheduling into one NP-hard model, then builds approximation algorithms from a nonlinear relaxation.

## Problem & Motivation

The paper studies periodic scheduling with a capacity limit per slot (`M` activities) where each activity trades fixed service cost against linearly increasing operating cost between services.

## Method / Architecture

A generalized model (GMSP) is formulated, an optimal cyclic schedule is proved to exist, and a nonlinear relaxation is solved approximately to derive practical approximation algorithms.

## Key Equations

$$
\min \frac{1}{2}\sum_i a_i(\tau_i + p) + \sum_i \frac{c_i}{\tau_i}
$$

$$
\sum_i \frac{1}{\tau_i} \le M, \qquad \tau_i \ge 1
$$

## Results

| Result type | Reported finding |
|---|---|
| Complexity | NP-hard, including restricted variants |
| Structural property | Optimal cyclic schedule exists |
| Broadcast-disk variant | 9/8-approximation |
| General variant | ~1.57 approximation from Fibonacci-based construction |
| Generic baselines | Randomized and deterministic greedy 2-approximation |

## Limitations

- Approximation guarantees are worst-case bounds; instance-specific practical performance can vary.
- Model assumptions use linear growth of operating cost between services. ^[inferred]

## Related

- [[concepts/periodic-scheduling-under-capacity-constraints]]
- [[references/bar-noy2004-efficient-algorithms-periodic-scheduling]]
- [[concepts/set-orienteering-problem]]

## Sources

- [[_papers/bar-noy2002minimizing/bar-noy2002minimizing-extracted.md]]
- [[_papers/bar-noy2002minimizing/bar-noy2002minimizing.md]]
