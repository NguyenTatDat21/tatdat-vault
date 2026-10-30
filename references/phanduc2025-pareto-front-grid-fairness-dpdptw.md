---
title: Pareto Front Grid Guided Multiobjective Optimization in Dynamic Pickup and Delivery with Two-Sided Fairness
category: references
tags: [multi-objective, evolutionary-algorithms, fairness, dynamic-vehicle-routing, pdptw, energy-consumption]
relationships:
  - target: "[[concepts/multi-objective-maritime-cargo-routing-scheduling]]"
    type: related_to
  - target: "[[concepts/fuzzy-weighted-max-min-scalarization]]"
    type: related_to
  - target: "[[concepts/multi-objective-metaheuristic-tuning-validation]]"
    type: related_to
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[concepts/leximax-leximin-fairness-principles]]"
    type: related_to
  - target: "[[references/richards1996-scheduling-to-maximize-customer-satisfaction]]"
    type: related_to
  - target: "[[references/ogryczak2014-fair-optimization-networks-survey]]"
    type: related_to
    note: "Reciprocal - references/ogryczak2014-fair-optimization-networks-survey references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
    note: "Reciprocal - references/ropke2006-adaptive-large-neighborhood-search-pdptw references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/xinyingchen2023guide]]"
    type: related_to
    note: "Reciprocal - references/xinyingchen2023guide references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/phanduc2025pareto/phanduc2025pareto-extracted.md
  - _papers/phanduc2025pareto/phanduc2025pareto.md
  - _papers/phanduc2025pareto/images/page_4_image_2.jpg
  - _papers/phanduc2025pareto/images/page_5_image_1.jpg
  - _papers/phanduc2025pareto/images/page_6_image_2.jpg
  - _papers/phanduc2025pareto/images/page_7_chart_5.jpg
  - _papers/phanduc2025pareto/images/page_8_chart_2.jpg
  - _papers/phanduc2025pareto/images/page_8_chart_4.jpg
summary: >-
  PFG-2F extends Pareto-front-grid selection to four-objective dynamic pickup-and-delivery (fuel, waiting, customer and vehicle fairness), beating NSGA-II, MOEA/D and PFG-MOEA on 180 Li-Lim instances.
provenance:
  extracted: 0.89
  inferred: 0.11
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-25T14:33:00Z
updated: 2026-10-30T14:38:55Z
---

# Pareto Front Grid Guided Multiobjective Optimization in Dynamic Pickup and Delivery with Two-Sided Fairness

> [!tldr] A four-objective dynamic PDPTW (fuel, maximum waiting time, customer fairness, vehicle fairness) is solved by extending the Pareto Front Grid MOEA to a two-level random-key encoding; hypervolume and IGD improve an order of magnitude over MOEA/D baselines.

## Problem & Motivation

Requests arrive dynamically in time slots; K homogeneous vehicles (capacity Q) share a depot and an operation time T. Each request r is \((l_p, l_d, q_r, sp_b, sp_e, sd_b, sd_e)\): pickup/delivery locations, load, soft pickup and delivery time windows — early arrival means waiting without penalty, late arrival a delay penalty. The paper builds on FairGA (Kang et al., GECCO 2024, p. 759-767), a two-sided-fairness dynamic VRP genetic algorithm using a two-level extended random-key encoding (LERK), whose stated limitations are single-objective optimization and simple operators. This paper adds four objectives and grid-based multiobjective selection.

![[_papers/phanduc2025pareto/images/page_4_image_2.jpg]]

*Figure 1: The overview of the proposed algorithm.*

## Method / Architecture

Energy model from mechanical power (Chen et al. 2023): instantaneous power Eq. (1) \(P_{ij}^v=\frac12 c_d \rho S \gamma^3 + (m_v+\tilde{Q}_{ij}^v) g c_r \gamma\); fuel per arc Eq. (2) \(L_{ij}^v=\frac{\xi}{\kappa\psi}(\omega R + \frac{P_{ij}^v}{\eta})\frac{d_{ij}}{\gamma}\); objective f1 is total fuel, Eq. (3).

[[concepts/leximax-leximin-fairness-principles|Fairness objectives]]:
- Eq. (4) \(WT_r=\max(\tau_r^p-sp_r^e,0)+\max(\tau_r^d-sd_r^e,0)\); Eq. (5) f2 = max waiting time over requests.
- Eq. (6) f3 = standard deviation of \(WT_r\) across all requests (customer fairness).
- Eqs. (7-8) DT_v = vehicle workload, f4 = standard deviation of DT_v across K vehicles (vehicle fairness).
- Eq. (9) minimize \(\{f_1,f_2,f_3,f_4\}\); constraints (10) each request served exactly once, (11) capacity, (12) arc-request linkage, (13-14) time-window lower bounds.

PFG-2F algorithm: two-level random-key encoding (upper layer = vehicle order, lower = request assignment) extended from LERK; Fairness Heuristics Initialization divides requests equally among K vehicles; the Urgent Time Ordering Rule (Eq. 15) reorders request keys ascending by time-window closing time. PFG selection (from Xu et al., Applied Soft Computing 136:110095, 2023): ideal point z* and nadir z^n updated each iteration, segment width \(d_j=(z_j^n-z_j^*+2\sigma)/GK\), grid index \(Grid_j(x)=\lceil (f_j(x)-z_j^*+\sigma)/d_j \rceil\); PFG segments keep the individuals with minimum grid value per objective segment; selection ranks within grids by non-dominated sorting, and individuals farthest from the z* hyperplane are removed. With probability ε, parents are drawn from consecutive grids \(PFG_i^j \cup PFG_{i+1}^j\); otherwise from the whole population (Eq. 16). The deployment solution is the intersection of the Pareto hyperplane with the ideal-nadir line, falling back to the point closest to the ideal.

![[_papers/phanduc2025pareto/images/page_5_image_1.jpg]]

*Figure 2: Individual Representation.*

![[_papers/phanduc2025pareto/images/page_6_image_2.jpg]]

*Figure 3: Pareto Front Grid generation.*

## Key Equations

The full model is Eqs. (1)-(14) above; evaluation metrics are Eq. (17) hypervolume (HV, higher is better) over the four-objective space and Eq. (18) IGD — average, over a reference Pareto set Q, of the minimum Euclidean distance from each reference point to the obtained set (lower is better).

Energy constants used in experiments: \(c_d=0.7\), \(c_r=0.01\), \(\xi=1\), \(\eta=0.36\), \(m_v=3.2\) tons, \(\psi=737\) L/gram, \(\gamma=40\) km/h, \(\kappa=44\) kJ/gram, \(g=9.81\), \(\rho=1.20\), \(\omega=0.2\), \(S=3.912\,m^2\), \(R=165\).

Baselines: NSGA-II (Deb 2002), MOEA/D (Zhang & Li 2007), MOEA/D-DE (Li & Zhang 2009), PFG-MOEA, PFG-2F-PM (permutation encoding + PMX crossover), PFG-2F-RK (random keys, the proposed variant), FairGA.

## Results

180 instances from the Li & Lim PDPTW benchmark (100/200/400 requests; R/C/RC categories, time-window classes 1-2; 18 scenarios). Mean HV (Table 1, R/C/RC):

| Algorithm | C1 (100 req) | C2 (200 req) | C4 (400 req) |
|---|---|---|---|
| NSGA-II | 0.138/0.081/0.043 | 0.113/0.077/0.052 | 0.124/0.070/0.057 |
| MOEA/D | 0.077/0.038/0.018 | 0.067/0.037/0.018 | 0.066/0.036/0.023 |
| MOEA/D-DE | 0.081/0.038/0.020 | 0.064/0.039/0.021 | 0.071/0.036/0.022 |
| PFG-MOEA | 0.209/0.150/0.086 | 0.192/0.132/0.074 | 0.209/0.131/0.081 |
| PFG-2F-PM | 0.412/0.287/0.212 | 0.331/0.273/0.211 | 0.369/0.271/0.215 |
| **PFG-2F-RK** | **0.463/0.325/0.223** | **0.370/0.316/0.203** | **0.406/0.324/0.231** |

Mean IGD (Table 2, R/C/RC): NSGA-II 0.353-0.435, MOEA/D family 0.350-0.590, PFG-MOEA 0.201-0.370, PFG-2F-PM 0.004-0.040, PFG-2F-RK 0.010-0.035 — an order of magnitude below the MOEA/D baselines. PFG-2F-PM explores better in the first 50 generations on RC (IGD RC1 0.006 vs 0.026) but traps in local optima; RK keeps improving to convergence. Against FairGA, improvement percentages (Table 3) range 14.6-18.7% on energy cost, 58-69% on vehicle fairness, 28-59% on customer fairness, 33-52% on max waiting time. Worst results under R1 (random locations + tight windows); best under C2; performance declines as request counts grow under a fixed generation budget. ^[inferred]

![[_papers/phanduc2025pareto/images/page_7_chart_5.jpg]]

*Figure 4: Effectiveness of PFG-2F over all instances.*

![[_papers/phanduc2025pareto/images/page_8_chart_2.jpg]]

*(a) HV convergence trend of PFG-2F compared to other benchmarks.*

![[_papers/phanduc2025pareto/images/page_8_chart_4.jpg]]

*(b) IGD convergence trend of PFG-2F compared to other benchmarks.*

## Limitations

- Optimization runs per time-slot snapshot; requests arriving within a slot are handled, true online re-optimization is not modeled. ^[inferred]
- The permutation variant wins on RC datasets in early convergence, so the random-key encoding is not uniformly superior.
- Stated future work: machine-learning heuristics for task allocation. ^[inferred]

## Related

- [[concepts/multi-objective-maritime-cargo-routing-scheduling]] — same four-objective routing-fairness style (cost plus equity metrics) solved by scalarization/multiobjective metaheuristics.
- [[references/richards1996-scheduling-to-maximize-customer-satisfaction]] — exact-threshold analogue: a parametric sweep over preference-score levels replaces the Pareto-front grid, bounding the worst-off user exactly.
- [[concepts/fuzzy-weighted-max-min-scalarization]] — the alternative route to multiobjective routing (scalarization) that PFG selection replaces.
- [[concepts/multi-objective-metaheuristic-tuning-validation]] — validation discipline for HV/IGD comparisons over benchmark families.
- [[concepts/vehicle-routing-with-synchronization-constraints]] — time-window coupling between pickup and delivery legs is the feasibility core of the PDPTW model here.

## Sources

- [[_papers/phanduc2025pareto/phanduc2025pareto-extracted.md]]
- [[_papers/phanduc2025pareto/phanduc2025pareto.md]]
- Bibliographic record: Phan Duc, Bui Trong, Nguyen Thi, Huynh Thi Thanh (2025), GECCO '25, July 13-18 2025, Malaga, DOI 10.1145/3712256.3726467, https://dl.acm.org/doi/10.1145/3712256.3726467. Zotero PDF key UEBQA7RD.
