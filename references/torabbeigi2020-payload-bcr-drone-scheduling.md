---
title: Payload-induced Battery Consumption in Drone Delivery Scheduling (Torabbeigi et al., 2020)
category: references
tags: [paper, drones, energy-modeling, scheduling]
relationships:
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: source_of
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: related_to
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: related_to
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: related_to
  - target: "[[references/dorling2017-drone-delivery-vrp]]"
    type: related_to
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: related_to
  - target: "[[references/murray2015flying]]"
    type: related_to
sources:
  - _papers/torabbeigi2020drone/torabbeigi2020drone-extracted.md
  - _papers/torabbeigi2020drone/torabbeigi2020drone.md
  - _papers/torabbeigi2020drone/images/page_2_chart_2.jpg
  - _papers/torabbeigi2020drone/images/page_3_chart_1.jpg
  - _papers/torabbeigi2020drone/images/page_9_chart_1.jpg
  - _papers/torabbeigi2020drone/images/page_0_image_2.jpg
  - _papers/torabbeigi2020drone/images/page_6_image_9.jpg
  - _papers/torabbeigi2020drone/images/page_10_image_1.jpg
summary: Introduces payload-dependent battery-consumption modeling for drone delivery and shows that ignoring it can make planned routes infeasible.
provenance:
  extracted: 0.89
  inferred: 0.09
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T10:00:17Z
updated: 2026-10-31T18:20:35Z
---

# Payload-induced Battery Consumption in Drone Delivery Scheduling (Torabbeigi et al., 2020)

> [!tldr] The paper adds payload-sensitive battery draw to drone scheduling and demonstrates that this single modeling change materially alters route feasibility and fleet sizing outcomes.

## Problem & Scope

The study focuses on delivery network planning where drones carry heterogeneous payloads, making energy use non-constant across missions.

It decomposes planning into:
- **Strategic Planning (SP):** selecting depot locations,
- **Operational Planning (OP):** scheduling and routing drones to satisfy delivery demand with minimal drone count.

## Method / Architecture

The central technical component is a linear payload-to-battery-consumption model:

$$
BCR = \alpha \cdot payload + \beta \tag{1}
$$

with estimated coefficients:
- \(\alpha = 2.297\)
- \(\beta = 3.879\ \text{(\% per minute)}\)

Both coefficients are statistically significant (p < 0.000115) and the adjusted R² of the regression exceeds 99% (source lines 58–61). The experiment used a DJI Phantom 4 Pro+ with a 1 lb maximum payload, data collected in hovering mode (hovering power exceeds the other modes because of effective translational lift), initial charge fixed at 95% because the drone consumes up to 5% before reaching hovering, and a 15% minimum charge required for a safe landing. Measured flight time is 13.76 min at the full 1 lb payload and 21.92 min with no payload (`_papers/torabbeigi2020drone/torabbeigi2020drone-extracted.md:47, 551`).

Battery-feasibility inequality that drives the covering range and the infeasible-arc preprocessing rules:

$$
t_{ij} < \frac{100 - MinCh_k}{\alpha_k d_i + 2\beta_k}\tag{3}
$$

and, at maximum payload, its specialization `t_ij < (100 − MinCh_k) / (α_k MaxP_k + 2β_k)` (eq. 4, source lines 153–159) defines the largest customer distance a depot can cover.


![[_papers/torabbeigi2020drone/images/page_2_chart_2.jpg]]
*Fig. 1 The remaining battery level (%) along the flight for different amount of payload (lb.)*

![[_papers/torabbeigi2020drone/images/page_3_chart_1.jpg]]
*Fig. 2 The relationship between the BCR and the payload amount*

![[_papers/torabbeigi2020drone/images/page_3_image_31.jpg]]
*Fig. 3 Covering customer i by candidate location j*

The OP stage is formulated as an optimization model with preprocessing and bound-tightening strategies (including infeasible-arc elimination and bound-generation components) to improve solvability.

## Results

- Controlled flight experiments (payloads from 0 to 0.882 lb) support the linear BCR model fit. Headline fit results (Table 1, lines 63–71):

   | Payload (lb) | Regression line (SOC vs t) | R² | BCR (%/min) |
   | --- | --- | --- | --- |
   | 0 | SOC = −3.834 t + 95.67 | 0.9997 | 3.834 |
   | 0.220 | SOC = −4.390 t + 95.88 | 0.9996 | 4.390 |
   | 0.441 | SOC = −4.977 t + 95.71 | 0.9996 | 4.977 |
   | 0.661 | SOC = −5.388 t + 95.91 | 0.9996 | 5.389 |
   | 0.882 | SOC = −5.867 t + 95.32 | 0.9994 | 5.867 |

   Moving from 0 to 0.22 lb raises BCR by 14.5%, and every line's intercept sits near 95.7 because the flight starts at 95% charge.
- Statistical tests in the paper indicate strong significance for payload effects on battery consumption.
- In the reported example, paths built with the fixed no-payload BCR (21.92 min flight time) look feasible on time but 3 of 5 (60%) fail the remaining-charge check once the payload-dependent BCR is applied — `^[inferred]` the fixed-rate model is optimistic only on time, pessimistic on energy, and still misses per-segment load (source lines 551–569, Table 6).
- Reversing an optimal flight path can flip its battery feasibility: 55.6% of the case study's optimal paths become infeasible when flown in reverse, because per-segment payload (and thus BCR) depends on direction.
- Case-study bounds and solution (20 customers, 5 candidate depots, SP selects D1 and D3):

   | Stage | Result | Source |
   | --- | --- | --- |
   | Initial run without bound generation | objective 10 with 18% relative gap after > 24 h | `:501` |
   | Primal bound (nearest-depot assignment, Algorithm 1) | 10 drones | Table 3 |
   | Dual bounds | Lagrangian 8.54 → 9, max clique 7, BPP-weight 8, final max{9, 7, 8} = 9 | Table 4 |
   | Optimal OP solution after preprocessing + bound generation | 9 drones (3 in D1, 6 in D3), solved in 20.82 min with 0% gap | `:505, 513` |

   The primal bound of 10 improved to 9, a 10% gain, and the optimal paths serve 2–3 customers each with 17.25–42.03% remaining charge.
- The case study demonstrates that infrastructure and scheduling choices are sensitive to whether payload-aware energy constraints are modeled.

![[_papers/torabbeigi2020drone/images/page_9_chart_1.jpg]]
*Fig. 5 A random test network with 20 customers and 5 candidate locations*

![[_papers/torabbeigi2020drone/images/page_10_image_1.jpg]]
*Fig. 7 Optimal flight paths- result of OP model for the case study network*


## Limitations

- Coefficients are estimated from a specific drone setup; transfer to other airframes/batteries likely needs recalibration.
- Multi-objective service metrics (lateness, fairness, resilience) are not the primary optimization target in this formulation. ^[inferred]
- Some extracted lines are oversized due embedded image payloads; fine-grained figure/table details should be verified from the PDF when needed. ^[ambiguous]

## Related

- [[concepts/payload-induced-drone-battery-consumption-rate]]
- [[references/dorling2017-drone-delivery-vrp]]
- [[concepts/min-cost-tsp-with-drone]]
- [[concepts/drone-speed-selection-in-routing]]
- [[references/tamke2023-vrpd-dss]]
- [[references/poikonen2020-k-mvdrp]]
- [[_papers/torabbeigi2020drone/torabbeigi2020drone-extracted]]

## Bibliographic Record

- Citation key: `torabbeigi2020drone`
- DOI: `10.1007/s10846-019-01034-w`
- Canonical URL: <https://doi.org/10.1007/s10846-019-01034-w>
- Publication: *Journal of Intelligent & Robotic Systems* (2020)
- Authors: Maryam Torabbeigi; Gino J. Lim; Seon Jin Kim
- Companion metadata note: [[_papers/torabbeigi2020drone/torabbeigi2020drone.md]]

## Sources

- [[_papers/torabbeigi2020drone/torabbeigi2020drone-extracted.md]] — Torabbeigi, Lim & Kim, *Journal of Intelligent & Robotic Systems*, 2020, DOI 10.1007/s10846-019-01034-w; zotero-key `QWIRPLV7`.
- [[_papers/torabbeigi2020drone/torabbeigi2020drone.md]] — companion metadata note.
- [[_papers/torabbeigi2020drone/images/page_2_chart_2.jpg]] — Fig. 1, "The remaining battery level (%) along the flight for different amount of payload (lb.)".
- [[_papers/torabbeigi2020drone/images/page_3_chart_1.jpg]] — Fig. 2, "The relationship between the BCR and the payload amount".
- [[_papers/torabbeigi2020drone/images/page_3_image_31.jpg]] — Fig. 3, "Covering customer i by candidate location j".
- [[_papers/torabbeigi2020drone/images/page_6_image_9.jpg]] — Fig. 4, "Example of a path consisting of two customers".
- [[_papers/torabbeigi2020drone/images/page_9_chart_1.jpg]] — Fig. 6, "Covering customers by depot candidate locations".
- [[_papers/torabbeigi2020drone/images/page_10_image_1.jpg]] — Fig. 7, "Optimal flight paths- result of OP model for the case study network".
