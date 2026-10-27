---
title: >-
  Cooperative Multi-Agent Routing with Shared Reward
category: concepts
tags: [multi-agent, routing, uav, orienteering, clustering, coordination]
relationships:
  - target: "[[references/fuertes2023-transformer-multi-uav-routing]]"
    type: derived_from
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: related_to
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
  - target: "[[concepts/bilevel-vrpd-task-assignment-routing]]"
    type: related_to
sources:
  - _papers/fuertes2023solving/fuertes2023solving-extracted.md
  - _papers/fuertes2023solving/fuertes2023solving.md
  - _papers/fuertes2023solving/images/page_1_image_4.jpg
summary: "Fleet routing where agents earn different rewards for their own versus other agents' regions; cooperation is what makes adding vehicles pay (4-agent reward 100 to 150)."
provenance:
  extracted: 0.84
  inferred: 0.13
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-24T00:32:00Z
updated: 2026-10-25T01:47:51Z
---

# Cooperative Multi-Agent Routing with Shared Reward

A fleet of $m$ agents serves $n$ regions. Task assignment is by clustering (fuzzy C-means, one cluster per agent); the reward structure is the coordination mechanism.

## Core Structure

- Nodes $\{0, \dots, n+1\}$ (start/finish depots), $m$ agents, $m$ clusters.
- Reward rules per agent: $r^a = r_{init}$ for its own cluster's regions, $r^a = r_{shared}$ for regions in another cluster, with $r_{init} > r_{shared}$. Cooperative: $r_{init}=1$, $r_{shared}=0.5$. Non-cooperative: $r_{init}=1$, $r_{shared}=0$.
- Objective: maximize $\sum_a\sum_i\sum_j r_i^a x_{ij}^a$; per-agent time $\sum t_{ij}^a x_{ij}^a \le t_{max}$, fleet time $\max_a t^a \le t_{max}$; Miller-Tucker subtour elimination; degree constraints in $[0,1]$ so **a node may be visited by several agents** (each at most once).
- The $t_{max}$ values are set so each agent can reach roughly half the nodes — cooperation is not optional for coverage, it is required.
- Clustering comparison: FCM vs K-Means vs size-constrained K-Means showed no clear winner; FCM chosen for low computational cost. ^[extracted]
- Measured effect at $n=100$: 2 agents cooperative 92.932 reward / 99.034 nodes vs 89.703 / 91.028 non-cooperative; 4 agents cooperative **149.538 / 204.566** vs 99.897 / 108.561.
- Two agents alone cover almost all nodes, so a non-cooperative 4-agent fleet gains almost nothing from doubling fleet size — **reward scales with fleet size only under cooperation**. ^[inferred]
- Cooperation also mitigates lost agents (battery, comms loss), since shared regions remain reachable by the rest. ^[inferred]

![[_papers/fuertes2023solving/images/page_1_image_4.jpg]]
*Fig. 1. Representation of an example of a mission completed by a swarm of 4 UAVs: (a) A scenario consisting of a depot (square box) containing four UAVs and a collection of regions (circles). (b) Initial planning is performed by clustering the regions. (c) Routing problem solving entails visiting as many regions as possible within a given time limit in order to maximize the total reward received.*

## Why It Matters

- It puts fleet scaling and reward structure on the same axis: adding vehicles is free (parallel) and time does not grow, so the only question is whether the reward lets the extra agents do useful work.
- Cooperation dominates in both reward and coverage, so the reward design (not the solver) is the binding constraint on fleet value. ^[inferred]
- Shared regions act as a resilience buffer: a fleet with shared coverage degrades gracefully when an agent drops out.
- It is the routing analogue of the vault's parallel-search question — parallel agents need a rule for who covers what, and reward sharing is cheaper than explicit communication. ^[inferred]
- Cluster-based assignment is a heuristic: task assignment quality bounds routing quality, so the paper's pipeline has no global optimum. ^[inferred]
- The reward asymmetry $r_{init} > r_{shared}$ keeps assignment meaningful; making $r_{shared}=r_{init}$ collapses to unconstrained coverage where no agent is responsible. ^[inferred]

## Related

- [[references/fuertes2023-transformer-multi-uav-routing]]
- [[concepts/k-multi-visit-drone-routing-problem]]
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]]
- [[concepts/bilevel-vrpd-task-assignment-routing]]
- [[concepts/set-orienteering-problem]]

## Open Questions

- Is there a reward-sharing rule that provably maximizes coverage under a fleet budget, rather than the two fixed settings used here? ^[inferred]
- Can shared-region visits be coordinated explicitly (no double coverage) so 4 agents produce 4 agents' worth of new coverage, not 2 agents' worth plus overlaps? ^[inferred]
- How much of the cooperation gain survives once per-agent constraints (payload, energy, no-fly zones) differ?

## Sources

- [[_papers/fuertes2023solving/fuertes2023solving-extracted.md]]
- [[_papers/fuertes2023solving/fuertes2023solving.md]]
- [[_papers/fuertes2023solving/images/page_1_image_4.jpg]]
