---
title: >-
  Handbook of Metaheuristics (Gendreau & Potvin, 2019)
category: references
tags: [book, metaheuristics, operations-research, optimization]
relationships:
  - target: "[[concepts/tabu-search]]"
    type: uses
  - target: "[[concepts/variable-neighborhood-search]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: uses
  - target: "[[concepts/parallel-metaheuristics-cooperative-search]]"
    type: uses
  - target: "[[concepts/hyper-heuristics]]"
    type: uses
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
  - _papers/gendreau2019handbook/images/page_20_image_3.jpg
  - _papers/gendreau2019handbook/images/page_20_image_4.jpg
  - _papers/gendreau2019handbook/images/page_26_image_2.jpg
  - _papers/gendreau2019handbook/images/page_47_image_7.jpg
  - _papers/gendreau2019handbook/images/page_85_image_2.jpg
  - _papers/gendreau2019handbook/images/page_123_image_2.jpg
  - _papers/gendreau2019handbook/images/page_257_image_2.jpg
  - _papers/gendreau2019handbook/images/page_115_image_2.jpg
  - _papers/gendreau2019handbook/images/page_117_image_2.jpg
  - _papers/gendreau2019handbook/images/page_365_image_3.jpg
  - _papers/gendreau2019handbook/images/page_380_image_10.jpg
summary: >-
  Distilled handbook-level patterns for simulated annealing, tabu search, VNS, LNS/ALNS, swarm intelligence (PSO/ACO), hybridization, cooperative parallel search, and hyper-heuristics.
provenance:
  extracted: 0.79
  inferred: 0.18
  ambiguous: 0.03
  ambiguous: 0.03
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-22T08:35:02Z
updated: 2026-10-24T04:37:31Z
---

# Handbook of Metaheuristics (Gendreau & Potvin, 2019)

This handbook consolidates core metaheuristic design patterns and compares how they are applied across combinatorial optimization domains, including routing and scheduling.

## Key Ideas

- Metaheuristics differ mainly by how they balance intensification and diversification under fixed compute budgets.
- Memory-based control (e.g., tabu search), neighborhood-change control (VNS), and destroy/repair control (LNS/ALNS) are reusable design families.
- Cooperative parallel search improves robustness and often solution quality when exchanges preserve diversity and avoid premature convergence.
- Hyper-heuristics move control one level up: they search over heuristics instead of directly searching over candidate solutions.
- Together, these families provide a shared vocabulary for designing routing solvers across truck-only and truck-drone settings. ^[inferred]
- **Simulated annealing is the acceptance rule, not just a method**: acceptance is a probability (Metropolis), the control parameter sets how much degradation is accepted, and the acceptance rate χ(c) ≈ 0.5 near the target temperature is the practical tuning signal — which is what the LNS + SA hybrid reuses on a complex neighborhood. [[concepts/simulated-annealing-metropolis-cooling]]
- **Swarm Intelligence** is defined by population-level problem solving with no central control: the double-bridge experiment, termite domes, and Kennedy's three levels (individuals, groups, culture) are the template for local sharing plus emergent global structure; canonical PSO is a velocity/position update, and its failure mode (single-particle premature convergence) is the reason social information and influence topologies matter. [[concepts/swarm-intelligence-pso-aco]]
- **Hybridization has four classes** — solution-based (global/phase), objective-evaluation-based, system-based, operator-based — and the two patterns that matter in routing: merge solutions exactly (set covering, fixed-variable MIP subproblems, CMSA), and let a relaxation (LP, Lagrangian, MST) rank which neighborhood to search. [[concepts/metaheuristic-hybridization]]

## Chapter Signals Relevant to Routing

- **Tabu Search (Chapter 2):** explicit treatment of tabu tenure, aspiration, and candidate-list strategies.
- **Variable Neighborhood Search (Chapter 3):** formal neighborhood-change logic (VND, RVNS, BVNS).
- **Large Neighborhood Search (Chapter 4):** destroy/repair framing and ALNS-style adaptive operator control.
- **Parallel Metaheuristics (Chapter 13):** cooperative multi-search taxonomies and communication design trade-offs.
- **Hyper-Heuristics (Chapter 14):** updated classification by selection/generation and online/offline/no learning.
- **Simulated Annealing (Chapter 1):** SA is framed for black-box optimization where the objective is a costly simulation; statistical equilibrium (Theorem 1) and asymptotic convergence are separated, and acceptance rate χ(c) ≈ 0.5 near the target control parameter is the tuning signal, with applications to the knapsack, TSP, and continental-scale aircraft trajectory planning (~30,000 flights).
- **Swarm Intelligence (Chapter 11):** canonical PSO, constriction/FIPS, bare-bones with Lévy α = 1.4, binary sigmoid PSO, discrete PSO with swap operators and path relinking competitive with ACO on the TSP, rotation-invariant SPSO-2011 with adaptive random topology (K = 3), LSGS/SSS guidance systems.
- **Ant Colony Optimization (Chapter 10):** pheromone-trail construction with evaporation, elitist ranking, and MAX–MIN pheromone ranges.
- **Metaheuristic Hybrids (Chapter 12):** CMSA, EA inside CPLEX branch-and-cut (Rothberg), set-covering merging for dial-a-ride, relaxation-guided VND, LP-dual pseudo-utility ratios, Lagrangian GA with the volume algorithm, bound-guided crossover.
- **Stochastic Search, Automated Algorithm Design, and Computational Comparison (Chapters 16-18):** search operators (random, greedy randomized, genetic), hyper-heuristic and reactive-search design, and performance-comparison methodology.

## Swarm Intelligence & Hybrids (Ch. 11, 12)

![[_papers/gendreau2019handbook/images/page_365_image_3.jpg]]
*Fig. 11.1 (paper, verbatim): "The double-bridge experiment: ants find the shorter path of the two between the nest and the food source; (a) at the start, (b) after some period, more ants choose the shorter path."*

![[_papers/gendreau2019handbook/images/page_380_image_10.jpg]]
*Fig. 11.11 (paper, verbatim): "The points x_i′ is chosen at random inside the hypersphere H_i(G_i, ‖G_i − x_i‖)" — the rotation-invariant SPSO-2011 sampling.*

Canonical PSO update with inertia weight $w$ and cognitive/social coefficients $c_1, c_2$ (component-wise $\otimes$, uniform $R[0,1]$):

$$
\mathbf{v}_i \leftarrow w\mathbf{v}_i + c_1 R[0,1]\otimes(\mathbf{p}_i - \mathbf{x}_i) + c_2 R[0,1]\otimes(\mathbf{p}_g - \mathbf{x}_i),\quad \mathbf{x}_i \leftarrow \mathbf{x}_i + \mathbf{v}_i
$$

The chapter's phase-space analysis on $f(x) = x^2$ shows why social information is required: if $\mathbf{x}$ and $\mathbf{v}$ start on the same side of the minimum, $p$ always equals $x$, the update collapses to $\mathbf{v} \leftarrow w\mathbf{v}$, velocity decays, and the particle converges prematurely to a non-optimum; with $\mathbf{x},\mathbf{v}$ straddling the minimum the trajectory spirals in. FIPS generalises the attractor to any neighbourhood set, making the influence graph the design knob; SPSO-2011 fixes the canonical scheme's lack of rotation invariance by sampling inside a hypersphere centred on a three-point centre of gravity, plus an adaptive random topology (each particle informs $K = 3$ random particles after an unsuccessful iteration). Discrete PSO with swap operators and path relinking is competitive with ACO on the TSP. ^[extracted]

Chapter 12 (Raidl & Puchinger) classifies hybrids as solution-based (global/phase), objective-evaluation-based, system-based, and operator-based. The routing-relevant patterns: **exact merging** (CMSA over an incumbent sub-instance; Rothberg's EA inside CPLEX branch-and-cut fixing variables common to parents; set-covering merging of route pools for dial-a-ride with VNS-generated columns), **relaxation-guided ordering** (relaxation-guided VND, LP-dual pseudo-utility ratios for the MKP, Lagrangian GA with the volume algorithm), and **bound-guided crossover** (crossover must occur before the bound point of a partial solution). Details: [[concepts/metaheuristic-hybridization]], [[concepts/swarm-intelligence-pso-aco]], [[concepts/simulated-annealing-metropolis-cooling]].

![[_papers/gendreau2019handbook/images/page_115_image_2.jpg]]
*Fig. 4.1 (paper): "a TSP solution. Right: A CVRP solution. In the CVRP, the depot is represented by a square and each customer *i* is represented by a node labeled with a demand *q_i*." The chapter's CVRP: graph *G = (V, E)*, vertex 0 the depot, customers *N = {1…n}* with demand *q_i*, *m* homogeneous vehicles of capacity *Q*, minimize total edge cost over exactly *m* routes, each customer visited exactly once.*

![[_papers/gendreau2019handbook/images/page_117_image_2.jpg]]
*Fig. 4.2 (paper): "Destroy and repair example. The top left figure shows a CVRP solution before the destroy operation. The top right figure shows the solution after a destroy operation that removed six customers (now disconnected from the routes). The bottom figure shows the solution obtained after reinsertion of the customers by the repair operation."*

## LNS Chapter Numbers (Pisinger & Ropke, Chapter 4)

- LNS was proposed by Shaw, based on the ruin-and-recreate approach, and belongs to the **VLSN** class: the neighborhood is defined implicitly by the destroy and repair methods and is **sampled**, never searched exhaustively.
- Census: a 15% destroy on 100 customers gives $C(100,15)=2.5\times10^{17}$ removal choices; a 20% destroy on 1000 customers gives $4.2\times10^{208}$. Very large-scale neighborhoods are defined as $f(n)=O(n^k)$, $k\le 3$ — 2-opt, relocate, swap ($O(n^2)$); exchange is $O(n^3)$.
- VLSN motivation, stated as an observation: a large neighborhood gives a higher-quality local optimum and a more promising search path; filtering limits the subset searched, and random removal with capacity-respecting repair gives a fast heuristic with a large neighborhood.
- With simulated-annealing acceptance (accept improving; else accept $x^t$ with probability $\exp(-(c(x^t)-c(x))/T)$, $T_{new}=\alpha T_{old}$, $0<\alpha<1$) LNS becomes standard simulated annealing with a complex neighborhood. The original LNS accepted improving solutions only, i.e. a hill-climber.
- Stated advantage: the large neighborhood lets the method navigate easily on tightly constrained instances, whereas small-scale neighborhoods struggle to reach distant regions of the search space.
- Chapter 4 prescribes randomized destroy methods (customer removal, related removal, route removal) paired with constructive/repair heuristics; the ship-pair variant used in industry is [[concepts/large-neighborhood-ship-pair-destroy-repair]].

## VNS and Tabu Search Chapter Additions

- **VNS (Chapter 3):** proposed ~20 years before 2019; schemes VND, RVNS, BVNS, GVNS plus Skewed VNS and VNDS (two-level VNS on a problem decomposition, solving a sequence of reduced problems from LP relaxations with variables fixed by VNDS rules, producing sequences of upper and lower bounds). Neighborhood-change rule: if $f(x')<f(x)$, set $x\leftarrow x'$ and return $k$ to the initial neighborhood, otherwise move to the next. Three motivating facts: a local minimum in one neighborhood need not be one in another; a global minimum is a local minimum for all neighborhoods; local minima with respect to several $N_k$ are often close. Extensions: Formulation Space Search / variable formulation search; VNS for automatic programming and AI; AutoGraphiX graph-theory discovery (>1500 conjectures, more than half proved automatically, compared with about 400 by human efforts); VNS combined with local branching for MILP solution generation, and with exact solvers for very large MILP instances.
- **Tabu Search (Chapter 2):** hybridization is pervasive — TS with ALNS (order-batching, Žulj/Kramer/Schneider, EJOR 264:653–664, 2018), GA, CP and IP; multi-objective TS for continuous problems (Jaeggi/Parks/Kipouros/Clarkson, EJOR 185:1192–1212, 2008) and on GPUs (Tsitskas/Kipouros/Savill, 2014).
- The handbook's third edition has 18 chapters (the second 21, the first 19); the edition change drops the "future directions" framing in favor of "recent and emerging" methods.

## Bibliographic Record

- Citation key: `gendreau2019handbook`
- DOI: `10.1007/978-3-319-91086-4`
- Canonical URL: <http://link.springer.com/10.1007/978-3-319-91086-4>
- Publication: *Springer International Publishing* (2019)
- Authors: Michel Gendreau; Jean-Yves Potvin
- Companion metadata note: [[_papers/gendreau2019handbook/gendreau2019handbook.md]]

## Related

- [[concepts/tabu-search]]
- [[concepts/variable-neighborhood-search]]
- [[concepts/large-neighborhood-search]]
- [[concepts/parallel-metaheuristics-cooperative-search]]
- [[concepts/hyper-heuristics]]
- [[references/montemanni2024-pdsvrp-collective-drones]]
- [[concepts/pdsvrp-c]]
- [[_papers/ropke2006adaptive/ropke2006adaptive-extracted]]
- [[_papers/lourenco2019iterated/lourenco2019iterated-extracted]]
- [[_papers/pisinger2019large/pisinger2019large-extracted]]
- [[concepts/large-neighborhood-ship-pair-destroy-repair]]
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]]
- [[references/goel2015-constraint-programming-lng-ship-scheduling]]
- [[concepts/simulated-annealing-metropolis-cooling]]
- [[concepts/swarm-intelligence-pso-aco]]
- [[concepts/metaheuristic-hybridization]]

## Open Questions

- Which handbook patterns transfer best to collaborative truck-drone routing without heavy retuning?
- What communication policy gives the best robustness/compute trade-off in cooperative search for large VRP variants?

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
- [[_papers/gendreau2019handbook/gendreau2019handbook.md]]
- [[_papers/gendreau2019handbook/images/page_20_image_3.jpg]]
- [[_papers/gendreau2019handbook/images/page_20_image_4.jpg]]
- [[_papers/gendreau2019handbook/images/page_26_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_47_image_7.jpg]]
- [[_papers/gendreau2019handbook/images/page_85_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_123_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_257_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_115_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_117_image_2.jpg]]
