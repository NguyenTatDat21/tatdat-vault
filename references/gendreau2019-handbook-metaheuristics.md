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
summary: "Reference for the handbook's metaheuristic patterns: LNS destroy/repair, VNS neighborhood change, tabu memory, SA cooling, PSO/ACO swarms, and hybrid search."
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-22T08:35:02Z
updated: 2026-10-25T00:53:13Z
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
- **Hybridization (Chapter 12, Raidl, Puchinger & Blum):** hybrids are distinguished by **four criteria** — the kinds of algorithms hybridized (MH+MH; MH+problem-specific algorithms such as simulations; MH+general OR/AI techniques, exact B&B, DP, LP/MIP, NLP, CP, SAT, and soft computing: NN, fuzzy, statistics), the **level** (high-level keeps identities with a defined interface; low-level mixes components), the **order of execution** (batch, sequential, intertwined, parallel), and the **control strategy** (integrative/coercive vs collaborative/cooperative). The two patterns that matter in routing: merge solutions exactly (set covering, fixed-variable MIP subproblems, CMSA), and let a relaxation (LP, Lagrangian, MST) rank which neighborhood to search. [[concepts/metaheuristic-hybridization]]

## Chapter Signals Relevant to Routing

- **Tabu Search (Chapter 2):** tabu tenure, multiple tabu lists per move type, aspiration rules (a tabu move is allowed when it beats the best known solution), candidate-list strategies for the admissible neighborhood, and granular tabu search keeping only short arcs.
- **Variable Neighborhood Search (Chapter 3):** formal neighborhood-change logic (VND, RVNS, BVNS).
- **Large Neighborhood Search (Chapter 4):** destroy/repair framing and ALNS-style adaptive operator control.
- **Intelligent Multi-Start (Chapter 7, Martí et al.):** re-starts for diversification against local optimality, classified by degree of randomization, memory, and rebuild; the term **Adaptive Memory Programming** was launched by multi-start tabu search. Memory-based variants (tabu search, GRASP, Analytical Randomized Tabu Search with short/long-term memory, path relinking to elite solutions, persistent attractiveness, strategic oscillation dismantling solutions to a variable degree), plus **GRASP** (Feo & Resende): each iteration = adaptive greedy construction, adding elements guided by a greedy function with randomized choice from a candidate list, then local search to a local optimum; path relinking between an improved solution and an elite guiding solution, reactive GRASP self-adjusting the candidate-list restriction parameter, and GRASP-with-path-relinking finding target solutions faster than memoryless GRASP (three-index assignment, MAXSAT, bandwidth packing, QAP).
- **Parallel Metaheuristics (Chapter 13, Crainic):** goals are speed/larger instances plus robustness across heterogeneous environments; cooperative multi-search is markedly more robust than sequential metaheuristics. Taxonomy along three dimensions: search-control cardinality (1C/pC), control & communications (synchronous RS/KS, asynchronous C/KC, KC derives new knowledge), search differentiation (SPSS/SPDS/MPSS/MPDS — same or multiple initial points, same or different strategies). Low-level master–slave schemes (neighborhood evaluation, fitness, ant construction, scatter-search subsets) give spectacular GPU speedups, but multi-search beats them in quality; hierarchical CPU+GPU settings are the practical pattern. [[concepts/parallel-metaheuristics-cooperative-search]]
- **Hyper-Heuristics (Chapter 14, Burke et al.):** a hyper-heuristic is a high-level strategy operating on a search space of heuristics, not of solutions; the term was coined in 1997 (automated theorem proving) and independently in 2000 for 'heuristics to choose heuristics'. Classification: heuristic **selection** vs **generation** (from components/search trails), constructive vs perturbation pools, online (learning on the single instance), offline (rules generalizing from training instances), no learning; perturbation hyper-heuristics combine selection + move acceptance, with single-point incumbents in the majority. [[concepts/hyper-heuristics]]
- **Simulated Annealing (Chapter 1):** SA is framed for black-box optimization where the objective is a costly simulation; statistical equilibrium (Theorem 1) and asymptotic convergence are separated, and acceptance rate χ(c) ≈ 0.5 near the target control parameter is the tuning signal, with applications to the knapsack, TSP, and continental-scale aircraft trajectory planning (~30,000 flights).
- **Swarm Intelligence (Chapter 11, Li & Clerc):** canonical PSO, constriction/FIPS, bare-bones with Lévy α = 1.4, binary sigmoid PSO, discrete PSO with swap operators and path relinking competitive with ACO on the TSP, rotation-invariant SPSO-2011 with adaptive random topology (K = 3); niching/speciation topologies with species seeds locate multiple optima in dynamic landscapes. [[concepts/swarm-intelligence-pso-aco]]
- **Ant Colony Optimization (Chapter 10):** pheromone-trail construction with evaporation, elitist ranking, and MAX–MIN pheromone ranges.
- **Metaheuristic Hybrids (Chapter 12):** CMSA, EA inside CPLEX branch-and-cut (Rothberg), set-covering merging for dial-a-ride, relaxation-guided VND, LP-dual pseudo-utility ratios, Lagrangian GA with the volume algorithm, bound-guided crossover.
- **Reactive Search (Chapter 15, Battiti, Brunato & Mariello):** RSO integrates subsymbolic machine learning into search heuristics via an internal online feedback loop that self-tunes critical parameters (reactions on the neighborhood, annealing schedule, objective function, prohibition-based methods), 'learning while optimizing'.
- **Stochastic Search (Chapter 16, Gutjahr & Montemanni):** a unified stochastic search process is a homogeneous Markov process $(M_t, L_t^+)$; random search with best-so-far memory converges in probability but with huge runtime, the canonical genetic algorithm never converges in probability (Rudolph), and adding the best-so-far solution to the memory restores convergence; Hajek's necessary and sufficient conditions under logarithmic cooling; too much exploration behaves like random search, too much exploitation causes premature convergence.
- **Automated Design (Chapter 17, Stützle & López-Ibáñez):** the algorithm-configuration problem, illustrated on ILS perturbation strength (increasing $k$ on non-improvement, resetting to $k_{min}$, gives basic VNS); F-race uses sequential statistical testing with Friedman tests; irace iterates candidate generation from a probabilistic model, racing, and model update around elites, with truncated-normal sampling for numerical parameters and no initial configuration required; automated ACO parameter-variation schedules improved anytime behavior significantly.
- **Computational Comparison (Chapter 18, Silberholz, Golden, Gupta & Wang):** comparing metaheuristics is harder than comparing other algorithms; for stochastic methods run ~10 replicates per instance recording average/best/worst and standard deviation, compare solution distributions, and use statistical tests including a binomial-based comparison; measure parameter interactions across the parameter space, compare quality and runtime, compare parallel variants, and make testbed instances accessible to other researchers.

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

Chapter 12 (Raidl, Puchinger & Blum) lists hybrids by the four criteria above. The routing-relevant patterns: **exact merging** (CMSA over an incumbent sub-instance; Rothberg's EA inside CPLEX branch-and-cut fixing variables common to parents; set-covering merging of route pools for dial-a-ride with VNS-generated columns), **relaxation-guided ordering** (relaxation-guided VND, LP-dual pseudo-utility ratios for the MKP, Lagrangian GA with the volume algorithm), and **bound-guided crossover** (crossover must occur before the bound point of a partial solution). Details: [[concepts/metaheuristic-hybridization]], [[concepts/swarm-intelligence-pso-aco]], [[concepts/simulated-annealing-metropolis-cooling]].

![[_papers/gendreau2019handbook/images/page_115_image_2.jpg]]
*Fig. 4.1 (paper, verbatim): "Left: a TSP solution. Right: A CVRP solution. In the CVRP, the depot is represented by a square and each customer *i* is represented by a node labeled with a demand *q_i*" — the chapter's CVRP: undirected graph *G = (V, E)*, vertex 0 the depot, customers *N = {1…n}* with demand *q_i*, *m* homogeneous vehicles of capacity *Q*, minimize total edge cost over exactly *m* routes, each customer visited exactly once.*

![[_papers/gendreau2019handbook/images/page_117_image_2.jpg]]
*Fig. 4.2 (paper): "Destroy and repair example. The top left figure shows a CVRP solution before the destroy operation. The top right figure shows the solution after a destroy operation that removed six customers (now disconnected from the routes). The bottom figure shows the solution obtained after reinsertion of the customers by the repair operation."*

## LNS Chapter Numbers (Pisinger & Ropke, Chapter 4)

- LNS was proposed by Shaw, based on the ruin-and-recreate approach, and belongs to the **VLSN** class: the neighborhood is defined implicitly by the destroy and repair methods and is **sampled**, never searched exhaustively.
- Very-large-scale neighborhoods are defined as $f(n)=O(n^k)$ with $k\le 3$; the chapter's census example: destroying, say, 15% of the customers among 100 leaves $C(100,15)=2.5\times10^{17}$ removal choices, so the neighborhood must be sampled, not enumerated. Small neighborhoods — 2-opt (TSP), relocate and swap (CVRP) — are $O(n^2)$.
- VLSN motivation, stated as an observation: a large neighborhood gives a higher-quality local optimum and a more promising search path; filtering limits the subset searched, and random removal with capacity-respecting repair gives a fast heuristic with a large neighborhood.
- With simulated-annealing acceptance (accept improving; else accept $x^t$ with probability $\exp(-(c(x^t)-c(x))/T)$, $T_{new}=\alpha T_{old}$, $0<\alpha<1$) LNS becomes standard simulated annealing with a complex neighborhood. The original LNS accepted improving solutions only, i.e. a hill-climber.
- Stated advantage: the large neighborhood lets the method navigate easily on tightly constrained instances, whereas small-scale neighborhoods struggle to reach distant regions of the search space.
- Chapter 4 prescribes randomized destroy methods (random customer removal; worst/critical removal for intensification; history-based removal of variables assigned improper values; Shaw's related removal picking elements with high mutual relatedness) paired with constructive, greedy, exact, or MIP repair — LNS/A(LNS) with MIP repair is a matheuristic prototype; regret repair (Potvin & Rousseau) adds look-ahead. The ship-pair variant used in industry is [[concepts/large-neighborhood-ship-pair-destroy-repair]].

## VNS and Tabu Search Chapter Additions

- **VNS (Chapter 3):** proposed ~20 years before 2019; schemes VND, RVNS, BVNS, GVNS plus Skewed VNS and VNDS (two-level VNS on a problem decomposition, solving a sequence of reduced problems from LP relaxations with variables fixed by VNDS rules, producing sequences of upper and lower bounds). Neighborhood-change rule: if $f(x')<f(x)$, set $x\leftarrow x'$ and return $k$ to the initial neighborhood, otherwise move to the next. Three motivating facts: a local minimum in one neighborhood need not be one in another; a global minimum is a local minimum for all neighborhoods; local minima with respect to several $N_k$ are often close. Extensions: Formulation Space Search / variable formulation search; VNS for automatic programming and AI; AutoGraphiX graph-theory discovery (>1500 conjectures, more than half proved automatically, compared with about 400 by human efforts); VNS combined with local branching for MILP solution generation, and with exact solvers for very large MILP instances.
- **Tabu Search (Chapter 2):** hybridization is pervasive — TS with ALNS (order-batching, Žulj/Kramer/Schneider, EJOR 264:653–664, 2018), GA, CP and IP; multi-objective TS for continuous problems (Jaeggi/Parks/Kipouros/Clarkson, EJOR 185:1192–1212, 2008) and on GPUs (Tsotskas/Kipouros/Savill, Procedia Comput. Sci. 29:2152–2161, 2014).
- Preface: the third edition has 18 chapters; the second edition had 21, the first (2003) 19, with chapters discarded as less relevant between editions; the last four chapters cover reactive search, stochastic search, automated design, and computational comparison; the second edition added large neighborhood search, artificial immune systems, and hybrid metaheuristics, and the third edition adds a new chapter on swarm intelligence.

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
- [[concepts/multi-objective-metaheuristic-tuning-validation]] — Chapter 17's racing/configuration methods underpin automated tuning validation.
- [[concepts/adaptive-large-neighborhood-search-for-mip]] — Chapter 4's MIP-repair LNS is the matheuristic prototype that page formalizes.

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
