---
title: >-
  Swarm Intelligence: PSO, ACO, and Emergent Coordination
category: concepts
tags: [swarm-intelligence, particle-swarm-optimization, ant-colony-optimization, metaheuristics, emergent-behavior]
relationships:
  - target: "[[references/gendreau2019-handbook-metaheuristics.md]]"
    type: derived_from
  - target: "[[concepts/metaheuristic-hybridization]]"
    type: related_to
  - target: "[[concepts/parallel-metaheuristics-cooperative-search]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
summary: >-
  Swarm Intelligence as the handbook defines it: simple agents, local interaction, no central control, and the PSO family from canonical velocity updates to rotation-invariant SPSO-2011.
provenance:
  extracted: 0.87
  inferred: 0.10
  ambiguous: 0.03
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-24T04:37:31Z
updated: 2026-10-24T04:37:31Z
---

# Swarm Intelligence: PSO, ACO, and Emergent Coordination

Chapter 11 (Li & Clerc) defines SI as the study of collective behaviour in artificial and natural systems: a population of simple agents, no centralized control, complex self-organising behaviour emerging from local interactions between agents and with the environment, based on very simple rules. The term was coined by Beni & Wang in cellular robotic systems; the two representative techniques are Particle Swarm Optimization and Ant Colony Optimization. Kennedy's definition used in the chapter: problem-solving ability that emerges in the interactions of simple information processing units — the units can be insects, robots, array elements, workstations, real or imaginary, and "there must be interaction among the units."

## Core Structure

**Biological evidence the chapter uses:**
- **Double-bridge experiment** — two bridges of different length between nest and food: no pheromone at start, 50% choice, and the shorter path accumulates more pheromone because more ants cross it, so more ants follow it, and almost all converge on the shorter path. No ant knows the shorter path.
- **Bird flocks** (safety in numbers, fast alarm spread, foraging information transfer, aerodynamic efficiency), **fish schools** (coordinated motion, predator avoidance, friction reduction), **termite domes** (carry dirt toward the strongest pheromone, deposit where the smell is strongest; pillars attract more termites, positive feedback, deposits on inner sides produce an arch), **honey bee waggle dance** (duration = number of waggle phases, vigor = interval between them; more phases means a more profitable source, so more bees are attracted).
- **Human society** — bakeries: no one dictates where hundreds of bakeries go, yet they serve the city; Kennedy's three levels: individuals learn locally from neighbours, group-level regularities emerge from social learning (a society's global properties cannot be predicted from its individuals), and culture optimises cognition by transporting local innovations far away.

**Canonical PSO** (continuous space): particle $i$ has position $\mathbf{x}_i$, velocity $\mathbf{v}_i$, personal best $\mathbf{p}_i$, neighbourhood/global best $\mathbf{p}_g$:

$$
\mathbf{v}_i \leftarrow w\mathbf{v}_i + c_1 R[0,1]\otimes(\mathbf{p}_i - \mathbf{x}_i) + c_2 R[0,1]\otimes(\mathbf{p}_g - \mathbf{x}_i)
$$
$$
\mathbf{x}_i \leftarrow \mathbf{x}_i + \mathbf{v}_i
$$

with inertia weight $w$ and acceleration coefficients $c_1$ (cognitive) and $c_2$ (social); $\otimes$ is component-wise.

**Single-particle dynamics** (the chapter's illustrative analysis on $f(x)=x^2$): if the initial $\mathbf{x}$ and $\mathbf{v}$ are on the same side of the minimum, $p$ always equals $x$, the update collapses to $\mathbf{v}\leftarrow w\mathbf{v}$, velocity decays to 0, and the particle **prematurely converges** to a point that is not the minimum; if they straddle the minimum, $p$ updates to better positions, velocity alternates sign, and the particle spirals into the minimum. In phase space the healthy trajectory is a spiral; the failed one never changes velocity direction.

**Two-particle interaction:** each particle informs only its own memory, and is informed by both memories. If particle 2's memory is better, particle 1's convergence improves while particle 2 is unaffected; when each particle's memory is sometimes better, both improve.

**Variants:**
- **Fully Informed PSO (FIPS)** generalises the attractor to any neighbourhood set:

$$
\mathbf{p} = \frac{\sum_{k\in N_i} \mathbf{R}[0, \frac{c_{max}}{|N_i|}]\otimes \mathbf{p}_k}{\sum_{k\in N_i}\varphi_k}
$$

  constriction Type 1 is the special case $k=2$ with $\mathbf{p}_1 = \mathbf{p}_i$, $\mathbf{p}_2 = \mathbf{p}_g$.
- **Bare-bones PSO** drops velocity: each dimension is drawn from a Gaussian with mean $(p_{i,d}+p_{g,d})/2$ and standard deviation $|p_{i,d}-p_{g,d}|$; a Lévy distribution with $\alpha = 1.4$ (fatter tails, between Cauchy and Gaussian) reproduces canonical PSO performance.
- **Binary PSO**: sigmoid on velocity as a probability, $s(v_{id}) = 1/(1+\exp(-v_{id}))$, $x_{id}=1$ if a uniform $R \le s(v_{id})$ else 0.
- **Discrete PSO**: discretize the updates, or design domain-specific velocity operators — Goldbarg et al. used swap operators and path relinking for the TSP; empirical studies show such discrete PSOs are competitive with ACO algorithms.
- **SPSO-2011**: canonical PSO is not rotation invariant — the cognitive and social components sample from axis-aligned hyper-parallelepipeds, so behaviour depends on the orientation of the coordinate axes. Fix: centre of gravity from three points,

$$
\mathbf{G}_i = \frac{\mathbf{x}_i + \mathbf{p}'_i + \mathbf{l}'_i}{3},\quad \mathbf{v}_i^{NEW} \leftarrow w\mathbf{v}_i + \mathbf{x}'_i - \mathbf{x}_i,\quad \mathbf{x}_i^{NEW} \leftarrow w\mathbf{v}_i^{NEW} + \mathbf{x}'_i
$$

  with $\mathbf{x}'_i$ drawn in the hypersphere centred at $\mathbf{G}_i$ with radius $\|\mathbf{G}_i-\mathbf{x}_i\|$ — rotation invariant. Plus an **adaptive random topology**: after each unsuccessful iteration, each particle informs $K$ random particles (typically $K=3$), so on average each particle is informed by $K$ others, occasionally by many. Competitive against state-of-the-art metaheuristics on the CEC'2013 real-parameter suite.
- **Guidance systems** from the chapter's SI framework: **LSGS** (learning social guidance system) — an environment description guides agents, and a learning model of the environment updates as agents change it; **SSS** (self-sufficient search system) — agent behaviour + local rules + environment dynamics generate emergent patterns; LSGS is a special case of SSS.

![[_papers/gendreau2019handbook/images/page_365_image_3.jpg]]
*Fig. 11.1 (paper, verbatim): "The double-bridge experiment: ants find the shorter path of the two between the nest and the food source; (a) at the start, (b) after some period, more ants choose the shorter path."*

![[_papers/gendreau2019handbook/images/page_380_image_10.jpg]]
*Fig. 11.11 (paper, verbatim): "The points $x_i'$ is chosen at random inside the hypersphere $H_i(G_i, \|G_i - x_i\|)$" — the rotation-invariant SPSO-2011 sampling.*

## Why It Matters

- It explains the swarm pattern used by routing methods that need no central planner: local rules plus a shared environment produce global structure — the same logic as pheromone trails and the UAV-cooperation incentive structure (shared regions reward both agents). ^[inferred]
- The single-particle analysis is the clearest explanation of premature convergence: the cognitive term alone collapses velocity; social information is what keeps the search alive. ^[extracted]
- FIPS generalises influence from "personal best + global best" to any neighbourhood, i.e. the influence graph is the design knob, the same knob as cooperative topologies in parallel metaheuristics.
- Discrete PSO with swap operators and path relinking is competitive with ACO on the TSP, so permutation routing problems are in scope for swarm methods, not just continuous ones. ^[extracted]
- Rotation invariance is a real robustness requirement: axis-aligned sampling makes canonical PSO sensitive to variable scaling/rotation, which matters in routing models with mixed units (time, cost, capacity). ^[inferred]
- The three-level society model (individual → group → culture) is the template for cooperative search: local sharing, group regularities, culture transporting innovations.

## Related

- [[references/gendreau2019-handbook-metaheuristics.md]]
- [[concepts/metaheuristic-hybridization]]
- [[concepts/parallel-metaheuristics-cooperative-search]]
- [[concepts/hyper-heuristics]]
- [[concepts/cooperative-multi-agent-uav-routing]]

## Open Questions

- No benchmark protocol in the chapter compares PSO, ACO, and GA on routing problems; "competitive with ACO" rests on TSP studies. ^[ambiguous]
- How much of SI's robustness claim is demonstrated, and how much is asserted from the biological analogy? ^[inferred]

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
- [[_papers/gendreau2019handbook/gendreau2019handbook.md]]
- [[_papers/gendreau2019handbook/images/page_365_image_3.jpg]]
- [[_papers/gendreau2019handbook/images/page_380_image_10.jpg]]
