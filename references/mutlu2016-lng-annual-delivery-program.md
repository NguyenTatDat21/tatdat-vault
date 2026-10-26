---
title: >-
  Annual LNG Delivery Program for Upstream Supply Chain (Mutlu et al., 2016)
category: references
tags: [paper, maritime, lng, inventory-routing, split-delivery, heuristic]
relationships:
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: uses
  - target: "[[concepts/maritime-routing-under-uncertainty]]"
    type: related_to
  - target: "[[references/ksciuk2023-maritime-uncertainty-review]]"
    type: related_to
  - target: "[[references/al-haidous2016-optimal-lng-deliveries]]"
    type: related_to
  - target: "[[references/andersson2017-creating-annual-lng-delivery-programs]]"
    type: related_to
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[references/deshpande2023-lng-adp-inventory-berth]]"
    type: related_to
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: related_to
  - target: "[[references/halvorsen-weare2013-lng-routing-berth-inventory]]"
    type: related_to
sources:
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md
  - _papers/mutlu2016comprehensive/mutlu2016comprehensive.md
  - _papers/mutlu2016comprehensive/images/page_8_chart_5.jpg
  - _papers/mutlu2016comprehensive/images/page_9_chart_2.jpg
  - _papers/mutlu2016comprehensive/images/page_9_chart_4.jpg
summary: >-
  Integrates LNG production, inventory, fleet routing, penalties and spot sales into an annual delivery program MIP; the vessel routing heuristic is 20.1% cheaper than 24-hour CPLEX.
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T09:52:03Z
updated: 2026-10-25T21:41:00Z
---

# Annual LNG Delivery Program for Upstream Supply Chain (Mutlu et al., 2016)

> [!tldr] The paper integrates production, inventory, fleet scheduling, and contract structure into LNG annual delivery planning, then shows a practical heuristic stack (VRH/MVRH) outperforms long-run exact baselines.

## Problem & Scope

The paper targets tactical annual delivery planning (ADP) for LNG suppliers over a 12-month horizon discretized into days, a specialization of [[concepts/maritime-inventory-routing-problem|maritime inventory routing]] with practical constraints including:
- production, storage and loading at a single liquefaction facility (the loading port $l$, reachable only through an artificial waiting port $l_d$), with a production rate $r_t$ that can change only once per month and bounds $R^{min}/R^{max}$, tank inventory bounds $S^{min}/S^{max}$, and $B$ loading berths,
- a heterogeneous fleet $\mathcal{V}$ with $G_v$ identical full-tank compartments of capacity $C_v$, integer tank inventory $g_{vt}$, and vessel–port compatibility sets $\mathcal{V}^i$,
- periodic maintenance (typically every five years) inside a vessel-specific maintenance window with a single maintenance port pair $(m, m_d)$ and disjoint windows across vessels,
- one contract berth per customer port, each customer port reached through its own artificial waiting port $i_d$ so vessels can wait for berth availability and time windows,
- contracts $\mathcal{C}_i = \{C_{i1}, \dots, C_{iN_i}\}$ with required volume $D_{in}$, volume bounds $\underline{D}_{in}/\overline{D}_{in}$, an expected delivery window $\mathcal{T}_{in}^e$ and a wider allowed window $\mathcal{T}_{in}^a$,
- over/under-delivery penalties $P_{in}^+/P_{in}^-$ per cubic meter and piecewise increasing early/late delivery penalties $P_{int}$,
- excess production cleared by spot sales through one potential spot vessel per day (binary $y_t$, operational cost $S$; revenues are deliberately not modelled),
- and split-delivery, where a vessel can deliver full-tank loads at several customer ports in one tour before returning to the loading port. Shipload delivery — one full cargo at one port per voyage, the rule in earlier ADP studies — is recovered by restricting the sailing set to $\mathcal{P}^{vi} = \{l_d, d\}$, so Halvorsen-Weare & Fagerholt (2013) ([[references/halvorsen-weare2013-lng-routing-berth-inventory]]), Rakke et al. (2011) and Stålhane et al. (2012) are special cases of this model. Split-delivery is bounded in practice by sloshing: the American Bureau of Shipping requires tank filling above 70% or below 10%, which most 4–6-tank vessels meet for full-tank deliveries.

The objective (Eq. 1) minimizes vessel operating cost, over/under-delivery penalties, early/late delivery penalties, and spot-sales operating cost:

$$
\min \sum_{v \in \mathcal{V}} \sum_{i \in \mathcal{P}^v} \sum_{j \in \mathcal{P}^{vi}} \sum_{t \in \mathcal{T}_{\mathcal{E}\chi}} C_{vij} x_{vijt} + \sum_{i \in \mathcal{P}^c} \sum_{n | C_{in} \in \mathcal{C}_i} P_{in}^- d_{in}^- + P_{in}^+ d_{in}^+ + \sum_{i \in \mathcal{P}^c} \sum_{v \in \mathcal{V}^i} \sum_{n | C_{in} \in \mathcal{C}_i} \sum_{t \in \mathcal{T}_{in}^a} P_{int} x_{v i_d i t} + S \sum_{t \in \mathcal{T}} y_t
$$

$C_{vij}$ covers fuel, personnel, port, channel and demurrage charges; production cost is negligible compared with these. Binary flow variables $x_{vijt}$ set vessel routes, $q_{vit}$ is the number of tanks loaded or unloaded, and $d_{in}^+/d_{in}^-$ are the over and under delivered volumes. Valid inequalities (Eq. 26–29) remove sailings outside allowed delivery windows, cap each $i \to j$ leg to one visit per $T_{vij} + \tau_{vji}$ cycle, require at least the precomputed minimum number of vessels $\beta_{jn}$ per contract, and bound loading-port visits by $\mathcal{N}_v$ from a companion MIP (Eq. 30–32).

## Method / Architecture

Two solution layers are combined:

Two solution layers are combined:

1. **MIP baseline (EM):** exact model solved with CPLEX 12.6, implemented in C++ with Xcode 6 and IBM ILOG Concert Technology, on a 2.7 GHz quad-core processor with 32 GB RAM under Mac OS X;
2. **Heuristic stack:** Vessel Routing Heuristic (VRH) and reranking-based extensions, then reduced-master refinement.

VRH ranks contracts (by the start of the expected delivery window, the midpoint of $\mathcal{T}_{in}^e$), then processes them one by one: it builds the candidate vessel set $V_{in}$ of vessels that can reach port $i$ inside $\mathcal{T}_{in}^a$ — including copies of vessels able to make several visits through the loading port — selects vessels with a small MIP (Eq. 33–35, a knapsack variant minimizing travel plus over/under/early/late penalties, where the planned minimum volume can be relaxed to $\underline{D}_{in} = \alpha D_{in}$ with $\alpha \in [0,1]$), schedules sailing dates, and assigns delivery volumes. A post-processing pass (Algorithm 2) sends vessels idling at the loading waiting port to under-delivered contracts when a round trip fits inside the waiting period. Loading-port inventory limits are only checked after all contracts are processed, with local rescheduling of arrivals and spot sales of the remaining excess. Multiple Vessel Routing Heuristic (MVRH, Algorithm 3) reruns VRH on reranked contract lists: contracts with high under-delivery penalties are pushed up the list, and at certain iterations the list is randomly reranked to escape reranking loops. The reranking metric is $\rho_k = (d_k^-/D_k)(P_k^-/\max P_i^-)$ combined with $\beta_k = D_k/\sum \beta_k^\nu G_\nu$, swapping adjacent contracts when both metrics increase and the expected window of contract $k$ starts before the allowed window of contract $k-1$ ends.

## Results

From the reported computational study on 18 instances generated from a commercial LNG trade database (Table 1), three size classes of 6 instances each, with the first four per class low-seasonality and the last two high-seasonality:

| Instance class | $\|\mathcal{V}\|$ vessels | $\|\mathcal{P}\|$ ports | $\|\mathcal{C}\|$ contracts | $B$ berths | DS | $\rho^P$ | $\rho^V$ | $\rho^I$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A (A1–A6, small-to-medium) | 20 | 8 | 65 | 3 | 0.02–0.13 | 0.65–0.95 | 7.06–10.25 | 6 |
| B (B1–B6, medium-large) | 30 | 12 | 93 | 4 | 0.02–0.23 | 0.65–0.96 | 7.20–10.62 | 6 |
| C (C1–C6, world's largest) | 40 | 16 | 111 | 5 | 0.05–0.29 | 0.65–0.95 | 8.14–11.93 | 6 |

- EM (CPLEX, 24 h limit) produced the first feasible solution only after more than 18 hours on every instance; small tests such as two vessels and four customers were not solved optimally within 24 hours, which is why the heuristic exists.
- VRH builds one ADP in about 1 second for class A and 2 seconds for class C. The full budget was 180 s of VRH plus 600 s of reduced-master solving per parameter set ($18 \times 780 = 14{,}040$ s, about four hours), with the reduced master solved for 600 s, until the gap fell below 3%, or the lower bound exceeded the best solution.
- Table 3: VRH cost is lower than the CPLEX 24 h solution on all 18 instances, with improvements from 1.0% (A3) to 53.6% (B4) and an **average improvement of 20.1%**. Optimality gaps are computed against the EM lower bound, so they are high for both methods (EM 17.8%–180.3%, VRH 12.8%–32.9%) — the authors attribute this to a weak lower bound caused by the large number of binary flow variables, meaning the 20.1% figure is a cost advantage over the 24-hour CPLEX solution, not a closed optimality gap.
- EM behaviour is erratic, performing poorly on B3 (180.3% gap) while performing relatively better on the larger C3 (17.8%); VRH performance is steadier.
- Demand seasonality degrades solution quality: instances 5 and 6 in each class are the high-seasonality counterparts of instances 2 and 3.
- Sensitivity on $\rho^I$ (storage-to-production ratio, base 6, tested at 8, 10, 12): average cost savings over the base case can reach **40%** when storage capacity is doubled.
- Split-delivery vs no-split (Table 4): savings range from 0.9% (B2) to 10.4% (A4) with **average 4.2%**, and grow as contractual demand relative to production capacity rises.
- VRH parameter settings are not separable: no parameter set is best on all instances (for example $r = R^{max}$ with $\alpha = 0.8$ and selective reranking is best on C1 but the second-worst on A1), yet the cost coefficient of variation across parameter sets is 0.04, 0.04 and 0.03 for classes A, B and C.

![[_papers/mutlu2016comprehensive/images/page_8_chart_5.jpg]]

*Fig. 1 (paper): Optimality gap vs. $\rho^P$ for VRH.*

![[_papers/mutlu2016comprehensive/images/page_9_chart_2.jpg]]

*Fig. 2 (paper): Optimality gap vs. DS for VRH.*

![[_papers/mutlu2016comprehensive/images/page_9_chart_4.jpg]]

*Fig. 3 (paper): Percentage cost savings over base-case vs. $\rho^I$ for VRH.*

## Limitations

- Results come from 18 generated instances built from a commercial LNG trade database, so transferability to other networks, contract structures and market conditions is not guaranteed.
- Gaps are measured against the CPLEX lower bound, so neither the EM nor VRH gap is a true optimality gap; the VRH-vs-EM comparison is a cost comparison against a 24-hour CPLEX run.
- Production rate is fixed by the heuristic before routing, revenues from long-term contracts and spot sales are excluded, sailing times are constant (no time-dependent travel as in Rakke et al. 2011 and Stålhane et al. 2012), no chartering is allowed, spot sales use one potential spot vessel per day, and maintenance windows are assumed disjoint. ^[extracted]
- The VRH parameter values in Table 2 ($r$, $\alpha$, $N_{max}$, $N_{imp}$, $L$) appear only as an image crop in the extracted markdown ($N_{imp} = 10$ and a three-minute limit are given in the text), so the full tested parameter grid needs PDF verification. ^[ambiguous]
- Heuristic quality depends on contract ranking, reranking strategy and parameters, and reranking can loop without random reranking. ^[extracted]

## Related

- [[concepts/annual-lng-delivery-program]]
- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/maritime-routing-under-uncertainty]]
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]]
- [[references/ksciuk2023-maritime-uncertainty-review]]
- [[references/al-haidous2016-optimal-lng-deliveries]]
- [[references/andersson2017-creating-annual-lng-delivery-programs]]
- [[references/deshpande2023-lng-adp-inventory-berth]]
- [[_papers/andersson2017creating/andersson2017creating-extracted]]
- [[_papers/al-haidous2016optimal/al-haidous2016optimal-extracted]]
- [[_papers/goel2015constraint/goel2015constraint-extracted]]
- [[_papers/fagerholt2023maritime/fagerholt2023maritime-extracted]]

## Bibliographic Record

- Citation key: `mutlu2016comprehensive`
- DOI: `10.1016/j.ejor.2015.10.031`
- Canonical URL: <https://www.sciencedirect.com/science/article/pii/S0377221715009571>
- Publication: *European Journal of Operational Research* (2016)
- Authors: Fatih Mutlu; Mohamed K. Msakni; Hakan Yildiz; Erkut Sönmez; Shaligram Pokharel
- Companion metadata note: [[_papers/mutlu2016comprehensive/mutlu2016comprehensive.md]]

## Sources

- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive-extracted.md]]
- [[_papers/mutlu2016comprehensive/mutlu2016comprehensive.md]]
- [[_papers/mutlu2016comprehensive/images/page_8_chart_5.jpg]]
- [[_papers/mutlu2016comprehensive/images/page_9_chart_2.jpg]]
- [[_papers/mutlu2016comprehensive/images/page_9_chart_4.jpg]]
