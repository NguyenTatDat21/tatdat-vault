---
title: >-
  Supply Chain Optimization for the Liquefied Natural Gas Business
category: references
tags: [paper, lng-supply-chain, maritime-inventory-routing, mixed-integer-programming, time-space-network, boil-off]
relationships:
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: uses
  - target: "[[concepts/time-space-network-ship-flow-model]]"
    type: uses
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: related_to
  - target: "[[references/christiansen2008-maritime-inventory-routing-problems]]"
    type: related_to
  - target: "[[references/gronhaug2010-branch-and-price-lng-irp]]"
    type: related_to
  - target: "[[references/halvorsen-weare2013-lng-routing-berth-inventory]]"
    type: related_to
sources:
  - _papers/gronhaug2009supply/gronhaug2009supply-extracted.md
  - _papers/gronhaug2009supply/gronhaug2009supply.md
  - _papers/gronhaug2009supply/images/page_202_image_2.jpg
  - _papers/gronhaug2009supply/images/page_208_chart_3.jpg
summary: >-
  Coins the LNG-IRP for real tactical fleet planning; arc-flow and path-flow MIPs on 21 real-inspired instances, both optimal on small cases, path enumeration explodes at scale.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25T19:48:00Z
tier: supporting
created: 2026-10-25T19:48:00Z
updated: 2026-10-25T19:48:00Z
---

# Supply Chain Optimization for the Liquefied Natural Gas Business

> [!tldr] Grønhaug & Christiansen formalize the planning problem of a real LNG operator (Suez Energy International), coin the term **LNG inventory routing problem (LNG-IRP)**, and benchmark two MIP formulations — arc-flow and path-flow — on 21 real-inspired instances.

![[_papers/gronhaug2009supply/images/page_202_image_2.jpg]]
*Fig. 1. The LNG supply chain*

## Problem & Novelty

The chapter addresses the **LNG supply chain** (exploration, extraction, liquefaction, maritime transportation, storage, regasification) from the perspective of an actor responsible for both the LNG fleet and the plant/terminal inventories. Planning horizon is tactical: 2–4 months, with liquefaction, transportation, and regasification optimized jointly. This is the paper that introduces the term LNG-IRP, and its modeling complications became the template for all later LNG inventory-routing work. ^[inferred]

The LNG-IRP complications identified here:

- **Boil-off**: a constant rate of cargo evaporates each day (used as fuel), so delivered quantities depend on route duration.
- **Discrete full-tank unloading**: cargo tanks are loaded fully at pickup ports; at delivery ports a discrete number of tanks is unloaded, with boil-off-adjusted quantities.
- Loading/unloading takes exactly one time period; at most two consecutive delivery-port visits before the ship must return to a pickup port; successive pickup calls are disallowed; no depot.
- Variable production and sales (bounds $[\underline{S},\bar{S}]$ at liquefaction, $[\underline{Y},\bar{Y}]$ at regasification), berth capacity $N_i^{CAP}$ per period, and residual cargo constraints at horizon end.

![[_papers/gronhaug2009supply/images/page_208_chart_3.jpg]]
*Fig. 4. Illustration of a possible route through the network for ship v*

## Method / Pipeline

Two formulations over the same real data:

1. **Arc-flow model** (constraints 1–28): binary variables $x_{ijvt}$ (sailing/waiting arcs on a discrete-time ship network), $z_{iwvt}$ (load/unload tank $w$ at port $i$), $u_{ivt}$ (port call). One sailing per ship starts at $t=1$ from origin $o(v)$ and ends at destination $d(v)$; flow conservation links cargo-handling to sailing arcs; no waiting during handling; at most $T^W$ waiting periods outside ports; two consecutive delivery visits force all tanks empty.
2. **Path-flow model** (constraints 29–35): every feasible ship route (sailing times + unloading quantities) is enumerated a priori by a recursive `createPath` routine; a convexity constraint $\sum_{r\in R_v}\lambda_{vr}=1$ per ship selects one route; production/sales variables keep the port side.

Boil-off in a route is aggregated as $B_v^{FA}=B^F\cdot(\text{total sailing time}-\text{handling periods})$, so the unloadable quantity of a tank is reduced accordingly (e.g. 75,000 m³ tank, 115 m³/period boil-off, 13-period duty ⇒ 1,265 m³ boil-off, 73,735 m³ unloadable). ^[inferred]

## Key Equations

Arc-flow objective (28), revenue minus cost minus sailing cost:

$$
\max \sum_{i,t} REV_{it}\,y_{it} - \sum_{i,t} COST_{it}\,y_{it} - \sum_{v}\sum_{(i,j),t} C_{ijv}\,x_{ijvt}
$$

Path-flow convexity per ship (34), one enumerated route per ship:

$$
\sum_{r\in R_v}\lambda_{vr}=1 \qquad \forall v
$$

Aggregated boil-off in a route (36): sailing periods minus handling periods, scaled by the daily boil-off rate:

$$
B_v^{FA}=B^F\cdot\Big(\sum_{(i,j)\in r}s_{ijv}-\sum_{(i,j)\in r}h_{ijv}\Big)
$$

The inventory-balance and berth-capacity structure (port stock balance, $\sum Z\lambda \le N_i^{CAP}$) is written in the same shape as the standard MIRP balance at [[concepts/maritime-inventory-routing-problem]]. ^[inferred]

## Setup & Headline Results

21 instances (1–5 ships, 3–6 ports, 30/45/60 periods), XPRESS 17.1, 3 GHz, 8 GB, 10 h time limit.

| Metric | Arc-flow | Path-flow |
|---|---|---|
| Small instances | solved to optimality | solved to optimality |
| Largest enumerated integer columns | — | 2,534,165 (instance 3); 1,561,996 (instance 21) |
| Instances 9 and 15 | solved | enumeration ran out of memory |
| Final MIP gap on unsolved instances | max 25.1% (instance 21) | max 42.9% (instance 21); overall range [2.9%, 42.9%] |
| Average LP relaxation gap | 19.4% | 19.4% |
| Fastest total time | 7 instances (excl. 9/15) | 7 instances |

## Ablations & Limitations

- Path enumeration scales with the number of feasible duties and fails outright on 2 of 21 instances; the 2010 branch-and-price successor exists precisely because of this. ^[inferred]
- A 19.4% LP gap in both models means weak bounds; large instances were not closed.
- The model fixes loading/unloading to one time period and assumes full-load at pickup — operational approximations that later LNG papers relax. ^[inferred]

## Bibliographic Record

- Publication: *Innovations in Distribution Logistics*, Lecture Notes in Economics and Mathematical Systems 619, Springer, 2009 (chapter, pp. 199–220 in the extracted book pagination)
- Chapter authors: Roar Grønhaug; Marielle Christiansen (the Zotero sidecar additionally lists the volume editors Jo A.E.E. Nunen, M. Grazia Speranza, Luca Bertazzi as creators). ^[inferred]
- DOI: 10.1007/978-3-540-92944-4_10
- Companion metadata note: [[_papers/gronhaug2009supply/gronhaug2009supply.md]]

## Related

- [[concepts/maritime-inventory-routing-problem]]
- [[concepts/time-space-network-ship-flow-model]]
- [[concepts/annual-lng-delivery-program]]
- [[references/christiansen2008-maritime-inventory-routing-problems]]
- [[references/gronhaug2010-branch-and-price-lng-irp]] — the successor method built on this chapter's instances
- [[references/halvorsen-weare2013-lng-routing-berth-inventory]]

## Sources

- [[_papers/gronhaug2009supply/gronhaug2009supply-extracted.md]]
- [[_papers/gronhaug2009supply/gronhaug2009supply.md]]
- [[_papers/gronhaug2009supply/images/page_202_image_2.jpg]]
- [[_papers/gronhaug2009supply/images/page_208_chart_3.jpg]]
