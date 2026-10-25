---
title: "Planning LNG Annual Delivery Programs with Speed Optimization and Multiple Loading Ports"
category: references
tags: [paper, maritime, lng, annual-delivery-program, speed-optimization, mixed-integer-programming]
relationships:
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: extends
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: related_to
sources:
  - _papers/haug2023planning/haug2023planning-extracted.md
  - _papers/haug2023planning/haug2023planning.md
  - _papers/haug2023planning/images/page_5_chart_2.jpg
  - _papers/haug2023planning/images/page_13_chart_2.jpg
summary: >-
  Time-space-network MIP for the LNG annual delivery program adding vessel speed
  optimization and multiple loading ports; gaps below 1% within 1 hour for horizons up to
  180 days.
provenance:
  extracted: 0.87
  inferred: 0.06
  ambiguous: 0.07
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T10:50:35Z
updated: 2026-10-25T10:50:35Z
---

# Planning LNG Annual Delivery Programs with Speed Optimization and Multiple Loading Ports

> [!tldr] Haug et al. extend the LNG annual delivery program MIP with vessel speed optimization and multiple loading ports (LNG-ADP-SO-MLP), reaching gaps below 1% within an hour for 180-day real-life instances with a commercial solver.

## Problem & Contribution

- Extends the LNG-ADP with two features of industrial practice: vessel speed optimization and multiple loading ports (LNG-ADP-SO-MLP, abstract, line 7).
- Motivated by charter-rate volatility: a 160,000 m³ vessel averaged 89,000 USD/day in 2021 vs 59,300 USD/day in 2020, with 2022 spot peaks of 400,000 USD/day (line 19).
- Objective maximizes profit: revenue from own and chartered DES deliveries, long-term and spot FOB cargoes, and end-of-horizon LNG value, minus speed-dependent sailing costs and chartering costs (lines 31-37, 43).
- Prior ADP work built on: Rakke et al.'s rolling-horizon pioneer, Al Haidous' fleet-size minimization, Andersson's valid inequalities, Mutlu's production-as-decision model, Li's Yamal LNG transshipment models (lines 23-25).

## Method

Time-space network with one-day periods; each arc ((i,t),(j,t′)) covers sailing, potential waiting, purge/cool-down, and port operations, with sailing placed first to simplify berth constraints and reduce symmetry (lines 53-61).

![[_papers/haug2023planning/images/page_5_chart_2.jpg]]
"Fig. 1. Illustration of an arc $((i,t),(j,t^{\\prime}))$ and the vessel activities it represents"

Key constraints (lines 101-265): inventory initialization, evolution, and limits $S_i \le s_{it} \le \bar{S}_i$ (2)-(4); maintenance exactly once for $V^M$ (5); start-position or unused vessel (6); flow conservation (7); DES demand per partition with boil-off bounds $\underline{D}_{jp} \le \cdot \le \overline{D}_{jp}$ (8); long-term FOB cargoes picked exactly once (9); spot FOB at most once, with an artificial unlimited-revenue-zero contract allowing surplus LNG disposal (10); berth capacity $B_{jt'}$ (11); charter load bounds $\underline{L}^C w \le g \le \overline{L}^C w$ (12). Boil-off runs 0.10-0.12% per day (line 19).

Setup: Python + Gurobi 10.0.0 on a Dell Optiplex 7780 with Intel Core i7-10700 @ 2.90 GHz (line 269). Instances come from two LNG producers; IDs encode |N^L|, |N^U|, |F^U|, |V|, |T|, e.g. n-1-7-27-23-120 (lines 271-277).

## Results

Average gap over 3 instances at 300/3600/10800 s, objective in mill USD, time to first feasible solution (Table 2, line 292):

| Instance | 300 s | 3600 s | 10800 s | obj | TTFFS (s) |
|---|---|---|---|---|---|
| n-1-2-2-18-30 | 0.00 | 0.00 | 0.00 | 73.1 | 0 |
| n-1-6-16-18-45 | 0.40 | 0.30 | 0.27 | 426.3 | 3 |
| n-1-6-16-18-60 | 0.39 | 0.23 | 0.23 | 668.1 | 12 |
| n-1-7-27-23-120 | 0.71 | 0.51 | 0.48 | 1 168 | 58 |
| n-1-7-40-23-180 | 1.55 | 0.42 | 0.22 | 1 615 | 240 |
| n-1-17-75-23-365 | no feasible solution within limit | | | | |
| a-1-6-12-11-60 | 1.63 | 1.32 | 1.30 | 263.1 | 33 |
| a-2-6-38-15-180 | 1.11 | 1.10 | 0.42 | 1 400 | 154 |

- The abstract's "gaps below 1% within 1 hour" headline holds for the single-loading-port instances, but a-1-6-12-11-60 shows 1.32% and a-2-6-12-11-60 1.70% at 3600 s (abstract line 7 vs Table 2, line 292). ^[ambiguous]
- Comparable to Rakke et al.'s instance B4 (16 vessels, 121 days, ≈ n-1-7-27-23-120): their gap 10.63% after 24 h vs 0.51% at 1 h here, with solver/hardware improvements over 12 years and a cost-minimization vs profit-maximization objective caveat (line 281).

Speed optimization on instance n-1-7-27-23-120 at 1800 s, gap 0.24% → 0.19% (Table 3, lines 300-305):

| Component | without speed opt | with speed opt | change |
|---|---|---|---|
| DES own-vessel revenue | 747.7 | 815.8 | +9.1% |
| DES chartered-vessel revenue | 181.8 | 116.8 | −35.7% |
| Chartering costs | 38.9 | 22.9 | −41.2% |
| Own-vessel costs | 79.9 | 90.1 | +12.9% |
| FOB long-term revenue | 304.3 | 304.3 | 0 |
| End-of-horizon LNG value | 1.6 | 2.1 | +23.1% |
| Total profit | 1 117 | 1 126 | +0.83% |

![[_papers/haug2023planning/images/page_13_chart_2.jpg]]
"Fig. 2. Distribution of vessel speeds with- and without speed optimization for instance $n - 1 - 7 - 2 7 - 2 3 - 1 2 0 - a$ . The central horizontal line denotes the average speed of the vessels."

- Binary speed variables more than double the model's binary count; chosen speeds span the full spectrum with peaks at 14-15 kn vs the default 16-17 kn, lowering fuel cost per distance (lines 298-311).
- Speed-optimization profit effect is +0.83% total, +3.1 mill USD DES revenue (line 307); instances contain no spot contracts, so the effect is expected to be stronger when spot cargoes and artificial FOB value are present (line 313).

## Limitations

- The 365-day instance found no feasible solution within the time limit; the authors propose embedding the model in a rolling-horizon heuristic for longer horizons (lines 319-321).
- The "below 1% within 1 hour" headline does not hold for the two-loading-port instances at 3600 s, as shown in the table above. ^[inferred]
- The speed-optimization effect was measured on instances without spot contracts, so generalization is open (line 313).

## Related

- [[concepts/annual-lng-delivery-program]]
- [[concepts/maritime-inventory-routing-problem]]
- [[references/mutlu2016-lng-annual-delivery-program]]

## Bibliographic Record

- Citation key: `haug2023planning`
- DOI: 10.1007/978-3-031-43612-3_10
- URL: none in metadata (sidecar url empty)
- Publication: conferencePaper, Computational Logistics (LNCS 14239, pp. 170-184), 2023
- Authors: Helle V. Haug, Sigrid H. Solum, Sanna B. Warholm, Kjetil Fagerholt, Mingyu Li, Inge Norstad, Joachim R. Daduna, Gernot Liedtke, Xiaoning Shi, Stefan Voß
- Companion metadata: [[../_papers/haug2023planning/haug2023planning.md|haug2023planning metadata]]

## Sources

- [[_papers/haug2023planning/haug2023planning-extracted.md]]
- [[_papers/haug2023planning/haug2023planning.md]]
- [[_papers/haug2023planning/images/page_5_chart_2.jpg]]
- [[_papers/haug2023planning/images/page_13_chart_2.jpg]]
