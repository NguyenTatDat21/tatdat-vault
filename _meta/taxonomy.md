---
title: Tag Taxonomy
category: meta
tags: [taxonomy, metadata]
sources: []
created: 2026-10-27T06:00:00Z
updated: 2026-10-30T16:05:09Z
---

# Tag Taxonomy

Controlled vocabulary for `concepts/` and `references/` pages. `_papers/**` raw sources and `templates/` are out of scope.

## Canonical tags (use these forms)

Domain families:
- **routing**: `vehicle-routing`, `vrp`, `vrptw`, `pdptw`, `tsp`, `fstsp`, `pdstsp`, `orienteering`, `set-orienteering-problem`, `team-orienteering`, `pickup-and-delivery`, `routing-with-synchronization`
- **drone / UAV**: `drones`, `drone-routing`, `truck-drone-routing`, `uav`, `drone-synchronization`, `drone-energy`, `multi-visit-drone`
- **maritime**: `maritime`, `lng`, `ship-routing-scheduling`, `maritime-inventory-routing`, `inventory-routing`, `time-space-network`, `berth-and-inventory`, `lng-delivery-program`
- **scheduling**: `scheduling`, `makespan`, `time-windows`, `periodic-scheduling`, `disjunctive-scheduling`, `cumulative-scheduling`, `fifo-property`
- **exact methods**: `mixed-integer-programming`, `milp`, `integer-programming`, `constraint-programming`, `cp-sat`, `branch-and-cut`, `branch-and-price`, `column-generation`, `cutting-stock`, `exact-methods`, `dynamic-discretization`, `lower-bounds`, `valid-inequalities`, `subtour-elimination`
- **heuristics**: `metaheuristics`, `heuristics`, `alns`, `lns`, `large-neighborhood-search`, `local-search`, `simulated-annealing`, `tabu-search`, `hyper-heuristics`, `matheuristics`, `ruin-and-recreate`, `variable-neighborhood-search`, `iterated-local-search`, `greedy-construction`, `primal-heuristics`
- **learning / decision**: `reinforcement-learning`, `imitation-learning`, `machine-learning`, `forecasting`, `black-litterman`, `portfolio-optimization`, `asset-allocation`, `asset-pricing`, `factor-investing`, `accruals`, `profitability`, `risk-modeling`
- **cross-cutting**: `optimization`, `operations-research`, `modeling-pattern`, `multi-objective`, `fairness`, `decomposition`, `dynamic-programming`, `approximation-algorithms`, `synchronization`, `energy-modeling`, `survey`, `paper`

## Aliases (rewrite to the canonical form)

| alias | canonical |
|---|---|
| `VRP` | `vrp` |
| `ALNS` | `alns` |
| `liFePO4` | `lifepo4` |
| `HML` | `hml` |
| `Fama-French` | `fama-french` |
| `Dantzig-Wolfe` | `dantzig-wolfe` |
| `SCIP` | `scip` |
| `ASEAN` | `asean` |
| `heuristic` | `heuristics` |
| `mixed-integer-programming` (when a page also uses `milp`) | `milp` |
| `traveling-salesman` | `tsp` |
| `truck-and-drone` | `truck-drone-routing` |
| `uav-routing` | `drone-routing` |
| `factor-models` | `factor-investing` |
| `time-expanded-networks` | `time-space-network` |
| `depot-discretization` | `dynamic-discretization` |
| `duration-objective` | `scheduling` |
| `waiting-arcs` | `time-space-network` |
| `enumeration` / `exact-algorithms` | `exact-methods` |
| `time-dependent-travel` | `scheduling` |
| `travel-time-functions` | `time-windows` |
| `piecewise-linear` / `preprocessing` / `pruning` / `correctness` / `arc-sets` / `infeasible-sequences` / `properties-lemmas` | `modeling-pattern` |
| `network-refinement` / `arc-lengthening` | `dynamic-discretization` |
| `relaxation` | `approximation-algorithms` |
| `feasible-solutions` | `primal-heuristics` |
| `location-based` | `time-windows` |

| adaptive-large-neighborhood-search | heuristics |
| alpha-fairness | fairness |
| ant-colony-optimization | operations-research |
| asset-turnover | asset-allocation |
| auxiliary-variables | modeling-pattern |
| banking | risk-modeling |
| bdd | exact-methods |
| berth-capacity | berth-and-inventory |
| berth-constraints | berth-and-inventory |
| bi-objective-optimization | operations-research |
| bilevel-optimization | operations-research |
| bound-consistency | constraint-programming |
| branch-and-bound | branch-and-cut |
| broken-triangle | constraint-programming |
| capacity-expansion | operations-research |
| capital-asset-pricing-model | asset-allocation |
| chatfield | operations-research |
| combinatorial-optimization | operations-research |
| complexity | approximation-algorithms |
| constraint-propagation | constraint-programming |
| convex-relaxation | approximation-algorithms |
| cooperative-drones | drones |
| cost-optimization | operations-research |
| course-scheduling | scheduling |
| covariance-estimation | risk-modeling |
| cumulative | constraint-programming |
| cutting-and-packing | cutting-stock |
| cutting-planes | cutting-stock |
| cvrp | vrp |
| cvrplib | vrp |
| data-analysis-practice | operations-research |
| data-scrutiny | operations-research |
| decision-diagrams | exact-methods |
| decision-measures | operations-research |
| decision-optimization | operations-research |
| definitive-analysis | operations-research |
| design-flexibility | operations-research |
| drone-energy-models | energy-modeling |
| drone-swarm-synchronization | drone-synchronization |
| dynamic-vehicle-routing | vehicle-routing |
| earnings-management | accruals |
| effective-statistician | operations-research |
| eight-principles | operations-research |
| encodings | constraint-programming |
| energy | energy-modeling |
| energy-consumption | energy-modeling |
| energy-model | energy-modeling |
| epsilon-constraint | constraint-programming |
| exact-optimization | operations-research |
| experimental-design | operations-research |
| exploratory-analysis | operations-research |
| exploratory-data-analysis | operations-research |
| factor-construction | factor-investing |
| factor-portfolio-views | factor-investing |
| fair-division | fairness |
| financial-accounting | accruals |
| five-stages | operations-research |
| flattening | constraint-programming |
| flexibility | operations-research |
| gas-price-modelling | forecasting |
| geometric-brownian-motion | forecasting |
| gross-profitability | profitability |
| gtsp | vehicle-routing |
| high-dimensional-statistics | operations-research |
| hypergraph | hyper-heuristics |
| hyperparameter-schedules | hyper-heuristics |
| ida | operations-research |
| income-smoothing | accruals |
| interval-propagation | constraint-programming |
| jump-diffusion | forecasting |
| leximax-leximin-fairness | fairness |
| lng-annual-delivery-program | lng |
| lng-flexibility | lng |
| lng-supply-chain | lng |
| load-dependent-energy | energy-modeling |
| loan-loss-provisioning | risk-modeling |
| local-consistency | constraint-programming |
| makespan-objective | makespan |
| managerial-flexibility | operations-research |
| maritime-routing | maritime |
| maritime-terminals | maritime |
| maritime-transportation | maritime |
| matheuristic | matheuristics |
| max-min-fairness | fairness |
| mdd | exact-methods |
| mean-reversion | asset-pricing |
| mean-variance-portfolio | portfolio-optimization |
| methodology | operations-research |
| mfstsp | vehicle-routing |
| mmse | risk-modeling |
| model-formulation | modeling-pattern |
| model-generation | machine-learning |
| model-validation | operations-research |
| monte-carlo-simulation | risk-modeling |
| multi-objective-mip | multi-objective |
| multi-objective-optimization | multi-objective |
| multirotor-energy-model | energy-modeling |
| npv-distribution | risk-modeling |
| objectives | multi-objective |
| particle-swarm-optimization | operations-research |
| pdsmtsp | vehicle-routing |
| persistent-uav-routing | drones |
| personal-qualities | operations-research |
| pickup-delivery | pickup-and-delivery |
| poisson-jumps | forecasting |
| portfolio-construction | portfolio-optimization |
| portfolio-management | portfolio-optimization |
| portfolio-risk | portfolio-optimization |
| power-network | modeling-pattern |
| price-of-fairness | fairness |
| problem-formulation | operations-research |
| problem-solving | operations-research |
| procedure-classes | operations-research |
| production-scheduling | scheduling |
| profit-margin | profitability |
| profit-maximization | profitability |
| profits | profitability |
| prudential-regulation | risk-modeling |
| pseudo-boolean | exact-methods |
| quadratic-tsp | vehicle-routing |
| real-options | asset-pricing |
| regulation | risk-modeling |
| reification | operations-research |
| residual-analysis | operations-research |
| reverse-optimization | operations-research |
| risk | risk-modeling |
| risk-aversion | risk-modeling |
| risk-pricing | risk-modeling |
| robust-optimization | operations-research |
| route-optimization | operations-research |
| sample-survey | survey |
| sampling | operations-research |
| set-team-orienteering | orienteering |
| shrinkage | risk-modeling |
| speed-optimization | operations-research |
| statistical-practice | operations-research |
| statistics | operations-research |
| stochastic-optimization | operations-research |
| stochastic-simulation | risk-modeling |
| streamliners | heuristics |
| student-scheduling | scheduling |
| swarm-synchronization | drone-synchronization |
| tractability | approximation-algorithms |
| truck-drone-synchronization | drone-synchronization |
| tsptw | vehicle-routing |
| uav-endurance | drones |
| uav-power-model | drones |
| uav-speed | drones |
| valid-inequality | valid-inequalities |
| value-factor | factor-investing |
| vehicle-routing-with-profits | profitability |
| yard-scheduling | scheduling |

## Rules

- Tags are lowercase, hyphenated, no spaces, no acronyms in mixed case.
- Prefer the broad canonical tag over a narrow coinage; if a term appears on one page only, alias it to a canonical tag.
- New pages carry 3-5 canonical tags, plus `paper` for `references/` paper pages.
- Existing pages keep their descriptive long tag lists (vault convention, 73 pages exceed the framework max-5 rule); trim toward 5 canonical tags when a page is touched for another reason.
- `visibility/` tags are reserved: max one per page, never counted toward 3-5, never in this vocabulary.
- Add a new canonical tag here before using it on a page; keep the list ordered by family.

## Migration guide

- `grep -rn "tags:" concepts references | grep -E "VRP|ALNS|liFePO4|HML|Fama-French|Dantzig-Wolfe|SCIP|ASEAN"` to find remaining non-canonical forms, then rewrite.
- Alias rewrites are mechanical; family merges (e.g. folding `uav` into `drone-routing`) need a page-by-page pass so typed relationships keep meaning.
