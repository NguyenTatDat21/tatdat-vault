---
title: >-
  Fair Optimization and Networks: A Survey
category: references
tags: [fairness, max-min-fairness, lexicographic-maximin, price-of-fairness, network-resource-allocation, location-theory, survey]
relationships:
  - target: "[[concepts/leximax-leximin-fairness-principles]]"
    type: related_to
  - target: "[[concepts/fuzzy-weighted-max-min-scalarization]]"
    type: related_to
  - target: "[[references/hartman2023-leximin-approximation]]"
    type: related_to
  - target: "[[references/phanduc2025-pareto-front-grid-fairness-dpdptw]]"
    type: related_to
  - target: "[[concepts/periodic-scheduling-under-capacity-constraints]]"
    type: related_to
  - target: "[[references/bar-noy2004-efficient-algorithms-periodic-scheduling]]"
    type: related_to
  - target: "[[references/barnhart1998-branch-and-price-column-generation]]"
    type: related_to
  - target: "[[references/richards1996-scheduling-to-maximize-customer-satisfaction]]"
    type: related_to
sources:
  - _papers/ogryczak2014fair/ogryczak2014fair-extracted.md
  - _papers/ogryczak2014fair/ogryczak2014fair.md
  - _papers/ogryczak2014fair/images/page_4_image_11.jpg
  - _papers/ogryczak2014fair/images/page_6_image_2.jpg
  - _papers/ogryczak2014fair/images/page_6_image_4.jpg
  - _papers/ogryczak2014fair/images/page_7_image_11.jpg
  - _papers/ogryczak2014fair/images/page_7_image_13.jpg
  - _papers/ogryczak2014fair/images/page_8_image_2.jpg
  - _papers/ogryczak2014fair/images/page_13_image_2.jpg
  - _papers/ogryczak2014fair/images/page_16_image_2.jpg
  - _papers/ogryczak2014fair/images/page_17_image_8.jpg
summary: >-
  Survey of inequality-averse fair optimization: fair-dominance axioms, OWA and alpha-fairness aggregations, lexicographic maximin algorithms, price-of-fairness bounds for networks and location.
provenance:
  extracted: 0.93
  inferred: 0.02
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T07:13:34Z
tier: core
created: 2026-10-26T07:13:34Z
updated: 2026-10-30T14:08:41Z
---

# Fair Optimization and Networks: A Survey

> [!tldr]
> **Authors:** Wlodzimierz Ogryczak (Warsaw University of Technology), Hanan Luss (Columbia University), Michal Pioro (Lund University and Warsaw University of Technology), Dritan Nace (Universite de Technologie de Compiegne), Artur Tomaszewski (Warsaw University of Technology)
> **Publication:** Journal of Applied Mathematics, vol. 2014, article 612018, 38 pages, 177 references. Received 7 March 2014, revised 3 August 2014, accepted 6 August 2014, published 3 September 2014; DOI 10.1155/2014/612018.
> **Central claim:** fairness in allocation systems should be modelled as *inequality-averse optimization* (fair dominance, lexicographic maximin / max-min fairness, alpha-fairness, ordered weighted averaging), not as minimization of an inequality index. The paper systematises the models, algorithms and complexity for communication networks, location-allocation, and the price of fairness.
> **Headline numbers:** price-of-fairness bound for proportional fairness `1 − 2√m/m`; for max-min fairness `1 − 4m/(m+1)²`; alpha-fairness `1 − O(m^{−α/(α+1)})`; `O(mn)` and `O(m²n)` lexicographic-maximin resource allocation; `O(pm⁸)` general ordered-median dynamic program.

## Problem & Motivation

Systems that serve many entities (network links, clients, facilities, jobs) need more than an efficiency metric. Efficiency objectives (total, mean, weighted sum) can discriminate individuals; the survey's organizing question is how to model "each entity ought to be provided with an adequate share of the services" while keeping the solution efficient. Fair treatment does not imply equal amounts, because operation-dependent constraints make perfect equity infeasible.

Motivating domains named in the introduction: bandwidth equity for all origin-destination pairs in telecom and Internet services; location of public services (police, fire, emergency medical) with fair response times; water allocation; flight scheduling and airport takeoff/landing slots; systems of systems; and the 21st-century problem of dividing natural resources — fossil fuels, clean water, and the atmosphere's greenhouse-gas absorption capacity.

The methodological target is to replace "minimize an inequality index" with criteria that are provably compatible with fair rational preferences, then to characterise the algorithms and complexity of those criteria on network and location models.

## Fair Dominance, Axioms, and Aggregations

**Outcome model.** For `m` services with strictly increasing performance functions `f_i`, the vector maximization model is

$$\max\{f(\mathbf{x}) : \mathbf{x} \in Q\} \tag{1}$$

with attainable set `A`. Convexity of `Q` plus concavity of `f` does **not** guarantee convexity of `A`. Aggregated models `max{g(f(x)) : x ∈ Q}` require `g` strictly increasing in every coordinate.

**Axioms of fair preference** (6)–(7): *impartiality/anonymity* (any permutation of an outcome vector is indifferent) and the *Pigou-Dalton principle of transfers* (`y'_i > y''_i ⇒ y − ε·e'_i + ε·e''_i` is preferred for `0 < ε < y'_i − y''_i`).

**Fair dominance.** `y'` fairly dominates `y''` if a finite sequence of coordinate permutations, equitable transfers and coordinate increases moves from `y''` to `y'`. A solution is *fairly efficient* when its outcome vector is fairly nondominated. Every fairly efficient solution is Pareto-optimal, not the converse. Aggregation functions that are symmetric **and** strictly Schur-concave make every optimum of (3) fairly efficient; the mean and the minimum are symmetric but not strictly equitable. Utility family (10) `u(y, α) = y^{1−α}/(1−α)` (`α ≠ 1`), `log y` (`α = 1`) gives `α`-fairness: `α = 1` is proportional fairness, `α → ∞` approaches max-min fairness, and for discrete problems a large `α` guarantees exact max-min fairness.

**Equations 6, 7, 10** are extracted as equation crops `page_7_equation_13.jpg`, `page_7_equation_17.jpg`, `page_9_equation_6.jpg` (stripped text, no verbatim caption anchor in the extracted markdown) — the LaTeX is preserved above. ^[ambiguous]

![[_papers/ogryczak2014fair/images/page_4_image_11.jpg]]
*Figure 1: The fair dominance structures W(y); the set of outcomes fairly dominated by y and B(y): the set of outcomes fairly dominating y.* Source caption has math markup `W ( { \overline { { \mathbf { y } } } } ) ;$ ... 𝐵(y)`; normalized here. ^[ambiguous]

Figure 1 shows the fair dominance structure in a two-dimensional outcome space: `W(y)` (dominated outcomes) is in general not a cone and not convex, `B(y)` (dominating outcomes) is convex; lexicographic maximin assigns the whole interior of the inner white triangle to preferred outcomes. There is no fair dominance between `(1, 100)` and `(2, 2)`: max-min fairness prefers `(2, 2)`, proportional fairness prefers `(1, 100)`. Vector `(2, 99)` fairly dominates `(1, 100)`, and all fairness models (including MMF and PF) prefer `(2, 99)`.

![[_papers/ogryczak2014fair/images/page_6_image_2.jpg]]
*Figure 2: The fair dominance structure and the ordered OWA optimization.*

![[_papers/ogryczak2014fair/images/page_6_image_4.jpg]]
*Figure 3: Variety of fair OWA aggregations.*

**Cumulative / OWA criteria.** With ordering map `Θ` (`θ_1 ≤ θ_2 ≤ … ≤ θ_m`) and cumulation (15) `barθ_i(y) = Σ_{j≤i} θ_j(y)`, fair dominance is pointwise comparison of the cumulative ordered outcomes (Lorenz dominance / weak majorization). The multicriteria model (16) `max{(barθ_1(f(x)), …, barθ_m(f(x))) : x ∈ Q}` contains the mean (`barθ_m`) and the max-min (`barθ_1`) as endpoints; its lexicographic optimization (17) is lexicographic maximin. Weighted sums of `barθ_i` equal an ordered weighted averaging (OWA) model (18) `max{Σ ω_i θ_i(f(x)) : x ∈ Q}` on ordered coordinates. Strictly decreasing positive weights (`ω_1 > ω_2 > … > ω_m > 0`) make every OWA optimum fairly efficient; as weight differences tend to infinity the model becomes lexicographic maximin, as they tend to zero it approaches mean maximization. Yager's *andness* (19) calibrates this: min aggregation → andness 1, max aggregation → 0, mean → 1/2; an OWA with andness > 1/2 is considered fair, fairer as andness → 1, and a given andness level does not determine unique weights.

**Shortfall duality.** Mean shortfalls to targets, (21) `δ_τ(y) = (1/m) Σ (τ − y_i)_+`, characterize fair dominance by pointwise comparison over all targets (`δ_τ(y') ≤ δ_τ(y'')` for all `τ`, one strict) = increasing concave order / Second Stochastic Dominance. Model (22) minimizes `(δ_{τ1}(f(x)), …, δ_{τr}(f(x)))` over `x ∈ Q`; lexicographic minimization of (22) is lexicographic maximin. Maximizing a concave increasing `u` is equivalent to minimizing a weighted aggregation of shortfalls with weights `w(ξ) = −u''(ξ)`.

## Key Equations

`barθ_k` needs ordering, yet is LP-representable:

$$\bar{\theta}_k = \max_t \left( k t - \sum_i \max\{t - y_i, 0\}\right)$$

Maximizing the *sum of the k smallest* outcomes is therefore an LP with auxiliary continuous variables and no binaries, while maximizing the `k`th smallest outcome alone is combinatorially hard. ^[inferred]

Counting-function formulation for nonconvex (0-1) lexicographic maximin with few distinct targets `τ_1 < … < τ_r` (24):

$$\text{lex}\min\left(\sum_i z_{1i}, \ldots, \sum_i z_{r-1,i}\right) \quad \text{s.t. } \tau_{k+1} - f_i(x) \le M z_{ki},\ z_{ki} \in \{0,1\}$$

The price of fairness (11), for criterion `F` on attainable set `A`, comparing the total-outcome-maximizing solution `y^T` with the fair solution `y^F`:

$$\mathrm{POF}(F, A) = \frac{\sum y_i^T - \sum y^F_i}{\sum y_i^T}$$

## Results

### Price-of-fairness bounds (compact convex `A`, equal maximum achievable outcome > 0)

| Criterion | Bound | Tightness |
|---|---|---|
| Proportional fairness | `POF ≤ 1 − 2√m/m` (12) | tight when `√m` is an integer |
| Max-min fairness | `POF ≤ 1 − 4m/(m+1)²` (13) | tight for all `m` |
| `α`-fairness | `POF ≤ 1 − min_{η∈[1,m]} (η^{1+1/α} + m − η)/(η^{1+1/α} + (m−η)η) ≈ 1 − O(m^{−α/(α+1)})` (14) | asymptotic |

Bounds depend strongly on the structure of the attainable set; there are problems where every fair solution is also total-outcome maximal, so the price is zero. Reference [75] generated a class of networks in which a fairer allocation is always more efficient — max-min fairness can achieve higher total throughput than proportional fairness.

### Worked examples (verbatim instance data)

- **Example 1 — two links in series** (three nodes `ν_1, ν_2, ν_3`, links `e_1, e_2`, demands `d_1 = {ν_1, ν_2}`, `d_2 = {ν_2, ν_3}`, `d_3 = {ν_1, ν_3}`, elastic traffic, equal capacities `c_1 = c_2 = 1.5`, feasible iff `X_1 + X_3 ≤ c_1`, `X_2 + X_3 ≤ c_2`): the maximum-throughput, proportional-fairness, and max-min-fairness solutions differ; max-throughput is `(1.5, 1.5, 0)` and the max-min-fair bandwidth allocation `(0.75, 0.75, 0.75)` is the perfect-equity point.

![[_papers/ogryczak2014fair/images/page_8_image_2.jpg]]
*Figure 6: A network example illustrating fairness issues.*

- **Example 2 — same network, ordered OWA weights:** `ω = (0.4, 0.35, 0.25)` yields `X = (1.5, 1.5, 0)` (maximum throughput); `ω = (0.6, 0.3, 0.1)` yields `X = (0.75, 0.75, 0.75)` (the max-min-fairness solution).
- **Example 3 — single facility on a triangular network:** `d_12 = 2`, `d_13 = d_23 = 100`; normalized weights `w_1 = w_2 = (1 − ε)/2`, `w_3 = ε` with tiny `ε > 0`. Locating at `ν_1` (or `ν_2`) gives `μ(ν_1) = 1 + 99ε` and `MAD(ν_1) = (1 − ε)(1 + 99ε)`; locating at the remote node `ν_3` gives `μ(ν_3) = 100(1 − ε)` and `MAD(ν_3) = 200ε(1 − ε)`. Hence `MAD(ν_3) < MAD(ν_1)` for small `ε`, and for `0 < ε < 1/200` location `ν_3` is the global MAD minimizer on the entire network — a direct illustration of minimization of a relative/inequality index rewarding a service location that is far from most clients.

![[_papers/ogryczak2014fair/images/page_16_image_2.jpg]]
*Figure 8: A network location problem for Example 3.*

- **Sensor location problem** (lexicographic maximin extension of equitable facility location): nodes to monitor `N = {2, 3, 4, 5}`, sensor sites `M = {1, 3, 4, 5}`, `K = 2` sensors, protection level of node `j` = number of sensors monitoring it. The unique optimum places sensors at nodes 1 and 5, so nodes 2, 3 and 5 are monitored by both sensors while node 4 is monitored by only one. Formulation (46a)–(46e) uses `X_j = Σ_{i∈I_j} x_i`, `Σ_{i∈M} x_i = K`, `x_i ∈ {0,1}`.
- **Single-path network throughput** (Figure 4, demands 1–2, 3–4, 3–5, link capacities such as 4 Gbs on link (1,3)): lexicographic maximin of demand throughputs is model (23a)–(23d).

![[_papers/ogryczak2014fair/images/page_7_image_11.jpg]]
*Figure 4: A single path for each demand.*

![[_papers/ogryczak2014fair/images/page_7_image_13.jpg]]
*Figure 5: Multiple path for demand between nodes 1 and 2.*

- **Content distribution with two servers** (Figure 7, tree topologies rooted at nodes 1 and 2; server 1 broadcasts programs 1–3, server 2 programs 4–6; link (1,3) capacity 100 Gbs; node 7 requests programs 2, 3 and 5): bandwidth allocation over shared trees is a fair optimization problem solved in the same complexity class as lexicographic maximin resource allocation.

![[_papers/ogryczak2014fair/images/page_13_image_2.jpg]]
*Figure 7: Content distribution from two servers.*

![[_papers/ogryczak2014fair/images/page_17_image_8.jpg]]
*Figure 9: The sensor location problem.*

### Complexity (Section 5, verbatim bounds)

| Model | Complexity |
|---|---|
| Fair OWA aggregation | single LP |
| Max-min fairness on convex sets | sequence of LPs; polynomial complexity |
| Lexicographic maximin (23a)–(23d), linear/exponential `f` | `O(mn)` or `O(m²n)` closed-form manipulations, polynomial time (`m` activities, `n` resources); same complexity for content distribution on trees |
| Load balancing MMF (linear costs, [147]) | `O(|V|⁵)`, guaranteed finite convergence |
| Single-source splittable-flow MMF (Megiddo) | polynomial time |
| Ordered median DP [152] | `O(pm⁸)` general, `O(pm⁴)` node-restricted |
| Single-facility ordered median [153] | `O(m³ log² m)` on trees, `O(|E| m³ log² m)` on general networks |
| Multifacility median/center and ordered median on general networks | NP-hard |
| MMF of unsplittable (single-path) flows, directed single-source multiple-sink [148], undirected general [149] | NP-hard; obtaining only the first entry of the sorted allocation vector (plain maximin) is already NP-hard, so all fairness models there are NP-hard |
| Max-Throughput Single-Path Network Routing subject to MMF allocation [150] | NP-hard even with unit capacities on all links |
| Modular (granular) splittable flows | NP-hard, nonconvexity from modularity |
| Nonpreemptive two-machine job-shop, fixed job count, any regular criterion | polynomial |
| `n`-job `m`-machine job-shop | NP-hard |

### Applications reviewed (Sections 3–4)

Traffic assignment problem with MMF, NPF and PF criteria (path-flow model (25a)–(25e), big-M routing binary formulation (26a)–(26c)); load balancing as `min r` (27a)–(27d) and its stronger MMF variant `lex min Θ(R)` (28a)–(28c); fixed-path TAP/MMF solved by the **water-filling** algorithm (uniformly increase allocations until a link congests, remove the blocked connections and their capacity, repeat); bottleneck-link integer programming characterization of TAP/MMF [92]; multisession multicast with multicast-specific fairness (multirate multicast traffic, lexicographically fair discrete bandwidth allocation [71, 72, 112, 115]); capacity allocation and dimensioning in IP networks; content distribution trees; TCP congestion control — additive-increase/multiplicative-decrease behaviour yields max-min-fair sharing in simplified networks and proportional fairness in large networks (end-to-end delays explain the gap), and linear networks under random traffic patterns show max-min fairness outperforming proportional fairness on throughput, with the converse for persistent flows. Location models: center (minimax) solutions for emergency facilities, lexicographically regularized criteria, inequality measures (variance, mean absolute difference/Gini's mean difference, mean absolute deviation, maximum absolute difference, relative measures normalized by the mean such as the Gini index `D(y)/μ(y)`), and the sensor location problem. Jain fairness index [61] and its multiattribute extension by Koppen et al. [172], where a leximin procedure selects the allocation maximizing the smallest Jain index; dominant resource fairness allocates by max-min fairness on dominant resource shares. Weighted variants: importance weights in scalar inequality measures, the Jain index, proportional fairness, and Weighted OWA (WOWA) aggregations, which remain LP-computable.

## Limitations

- Direct minimization of relative inequality measures contradicts optimizing individual outcomes: a facility at (or near) infinity gives near-perfect equality of service in dispersion-type measures — the survey flags this as a common flaw of all relative inequality measures, upper semideviations included.
- Discrete structure makes fair optimization "questioning possibility to achieve any fair solution in a reasonable time"; approximate/heuristic algorithms are needed.
- Fair optimization in job-shop scheduling is underexplored despite being recognized in 1989 [160]; vector/multiattribute fairness (heterogeneous CPU/memory/bandwidth demands in datacenters) is "still underexplored".
- Distributed fairness: in most cases distributed approaches must be based on game theory rather than direct optimization; only some equitable problems admit a parallel distributed implementation [113].
- Price of fairness for fair OWA models had not been studied at publication time; the survey reports no closed form for that family.

## Related

- [[concepts/leximax-leximin-fairness-principles]] — the concept page distilled from this survey.
- [[concepts/fuzzy-weighted-max-min-scalarization]] — the fuzzy/OWA-style scalarization of the same max-min family.
- [[references/hartman2023-leximin-approximation]] — approximation algorithms for the leximin objective the survey formalizes.
- [[references/richards1996-scheduling-to-maximize-customer-satisfaction]] — the bottleneck (max-min) transportation model the survey's bottleneck-objective literature line anticipates, solved on a 56-student/33-seminar data set.
- [[references/phanduc2025-pareto-front-grid-fairness-dpdptw]] — Pareto-front-grid fairness in dial-a-ride: a recent applied instance of the survey's framework.
- [[concepts/periodic-scheduling-under-capacity-constraints]] — periodic scheduling: the max-min bottleneck structure behind bandwidth allocation.
- [[references/bar-noy2004-efficient-algorithms-periodic-scheduling]] — scheduling under resource constraints, cited in the survey's scheduling discussion.
- [[references/barnhart1998-branch-and-price-column-generation]] — column generation, the standard device for the exponential path-list formulations the survey describes.

## Sources

- `_papers/ogryczak2014fair/ogryczak2014fair-extracted.md` — the extracted full text (1073 lines) read in full; all formulas, bounds, examples and complexity figures above are verbatim from it.
- `_papers/ogryczak2014fair/ogryczak2014fair.md` — Zotero sidecar (title, 5 authors, Journal of Applied Mathematics 2014, DOI 10.1155/2014/612018). The sidecar carries no tags; the extracted paper's own venue line and publication dates come from the extracted text.
- Embedded figure crops (verbatim caption anchors, 9 figures, 0 logos, 0 title-page product photos):
  - `_papers/ogryczak2014fair/images/page_4_image_11.jpg`
  - `_papers/ogryczak2014fair/images/page_6_image_2.jpg`
  - `_papers/ogryczak2014fair/images/page_6_image_4.jpg`
  - `_papers/ogryczak2014fair/images/page_7_image_11.jpg`
  - `_papers/ogryczak2014fair/images/page_7_image_13.jpg`
  - `_papers/ogryczak2014fair/images/page_8_image_2.jpg`
  - `_papers/ogryczak2014fair/images/page_13_image_2.jpg`
  - `_papers/ogryczak2014fair/images/page_16_image_2.jpg`
  - `_papers/ogryczak2014fair/images/page_17_image_8.jpg`
- The images directory also holds 77 `page_N_equation_M.jpg` equation crops. The extracted markdown contains exactly 9 image embeds (the figures listed above); equation crops have **no caption anchor** in the extracted text, so they are not embedded here — the equations are preserved as verbatim LaTeX in this page. `^[ambiguous]`
