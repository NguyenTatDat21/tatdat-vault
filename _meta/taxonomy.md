---
title: Tag Taxonomy
category: meta
tags: [taxonomy, metadata]
created: 2026-10-27T06:00:00Z
updated: 2026-10-27T06:00:00Z
---

# Tag Taxonomy

Controlled vocabulary for `concepts/` and `references/` pages. `_papers/**` raw sources and `templates/` are out of scope.

## Canonical tags (use these forms)

Domain families:
- **routing**: `vehicle-routing`, `vrp`, `vrptw`, `pdptw`, `tsp`, `fstsp`, `pdstsp`, `orienteering`, `set-orienteering-problem`, `team-orienteering`, `pickup-and-delivery`, `routing-with-synchronization`
- **drone / UAV**: `drones`, `drone-routing`, `truck-drone-routing`, `uav`, `drone-synchronization`, `drone-energy`, `multi-visit-drone`
- **maritime**: `maritime`, `lng`, `ship-routing-scheduling`, `maritime-inventory-routing`, `inventory-routing`, `time-space-network`, `berth-and-inventory`, `lng-delivery-program`
- **scheduling**: `scheduling`, `makespan`, `time-windows`, `periodic-scheduling`, `disjunctive-scheduling`, `cumulative-scheduling`
- **exact methods**: `mixed-integer-programming`, `milp`, `integer-programming`, `constraint-programming`, `cp-sat`, `branch-and-cut`, `branch-and-price`, `column-generation`, `cutting-stock`, `exact-methods`
- **heuristics**: `metaheuristics`, `heuristics`, `alns`, `lns`, `large-neighborhood-search`, `local-search`, `simulated-annealing`, `tabu-search`, `hyper-heuristics`, `matheuristics`, `ruin-and-recreate`, `variable-neighborhood-search`, `iterated-local-search`, `greedy-construction`
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
