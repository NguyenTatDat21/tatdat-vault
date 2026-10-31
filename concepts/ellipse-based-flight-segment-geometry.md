---
title: >-
  Ellipse-Based Flight Segment Geometry for Truck-Caried Drone Routes
category: concepts
tags: [uav]
relationships:
  - target: "[[references/wang2019routing]]"
    type: related_to
  - target: "[[concepts/hybrid-truck-drone-delivery]]"
    type: related_to
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[concepts/min-cost-tsp-with-drone]]"
    type: related_to
summary: >-
  Truck-carried drone flight segments as ellipses with two truck access points as foci, launch-recover arcs, and endurance-bounded segment construction.
provenance:
  extracted: 0.89
  inferred: 0.11
  ambiguous: 0.0
base_confidence: 0.67
tier: core
lifecycle: draft
lifecycle_changed: 2026-10-29
created: 2026-10-29T16:44:00Z
updated: 2026-10-30T18:52:00Z
sources:
  - _papers/wang2019routing/wang2019routing.md
---

# Ellipse-Based Flight Segment Geometry for Truck-Caried Drone Routes

> [!tldr] A truck-carried drone segment is an ellipse whose two foci are access points on the truck route: launch-recover arcs `d_QA + d_QB = D_max^su`, flight arc `d_AB = α·D_max^su`, segment length `β·D_max^su` with `1 ≥ β > α > 0`. ^[extracted]

![[_papers/wang2019routing/images/page_4_image_18.jpg]]
*Fig. 4. UAV truck launching, truck-carried UAV, and the ellipse for the UAV segment.* — the segment ellipse, the two access points as foci, customers on the arc.

The launch-recover arc lengths satisfy eq. 19-20, so the segment length is `β·D_max^su`; as β increases the ellipse's major and minor axes grow. ^[extracted]

![[_papers/wang2019routing/images/page_6_image_3.jpg]]
*Fig. 6. The illustration of the segment radius adaptation.* — segment radius adaptation: one unvisited customer expands the ellipse; multiple unvisited customers expand the ellipse.

![[_papers/wang2019routing/images/page_6_image_10.jpg]]
*Fig. 6. The illustration of UAV customers redistribution.* — customer redistribution across the truck route.

![[_papers/wang2019routing/images/page_6_image_12.jpg]]
*Fig. 6. The illustration of customer redistribution for segment.* — customer redistribution inside a segment: the segment node is the insertion location for min-cost.

![[_papers/wang2019routing/images/page_7_image_8.jpg]]
*Fig. 7. The illustration of segment route construction.* — segment route construction: an open TSP-like loop inside the segment.

![[_papers/wang2019routing/images/page_7_image_10.jpg]]
*Fig. 7. The illustration of UAV-exclusion for segment.* — UAV-exclusion inside a segment.

![[_papers/wang2019routing/images/page_7_image_12.jpg]]
*Fig. 7. The illustration of the segment node abstraction.* — segment node abstraction, the segment as a node on the truck route.

![[_papers/wang2019routing/images/page_12_chart_3.jpg]]
*Fig. 12. The illustration of the segment reroute.* — segment reroute, the segment node moved on the truck route.

Segment construction steps: radius expansion rules for no, one, and multiple unvisited customers inside the ellipse; splitting segments with multiple customers; min-cost insertion of customers redistributed across the truck route; the intra-segment open-loop route is an insertion-built TSP path, with a greedy UAV-exclusion loop under UAV constraints; the segment-node abstraction places the segment as a node at the farthest endpoint, with reroute costs `Δd1 = d_AP2 − d_AP1`, `Δd2 = d_BP2 − d_BP1`. ^[extracted] The segment is a TSP path with two endpoint access points, so launch-recover arcs and segment length bound the tour. ^[inferred]

![[_papers/wang2019routing/images/page_9_image_3.jpg]]
*Fig. 9. The illustration of time balancing.* — time balancing: truck time, drone time, fleet time.

![[_papers/wang2019routing/images/page_9_image_12.jpg]]
*Fig. 9. The illustration of step 3.* — time-balancing step 3.

![[_papers/wang2019routing/images/page_10_chart_3.jpg]]
*Fig. 10. The illustration of time balancing.* — time balancing, circle, segment, truck.

![[_papers/wang2019routing/images/page_10_chart_6.jpg]]
*Fig. 10. The illustration of step 1.* — time-balancing step 1.

![[_papers/wang2019routing/images/page_10_chart_8.jpg]]
*Fig. 10. The illustration of step 2.* — time-balancing step 2.

![[_papers/wang2019routing/images/page_11_chart_3.jpg]]
*Fig. 11. The illustration of step 3.* — time-balancing step 3.

![[_papers/wang2019routing/images/page_11_chart_6.jpg]]
*Fig. 11. The illustration of the global route construction.* — global route construction.

![[_papers/wang2019routing/images/page_11_chart_8.jpg]]
*Fig. 11. The illustration of the segment node abstraction.* — segment node abstraction.

![[_papers/wang2019routing/images/page_12_chart_5.jpg]]
*Fig. 12. The illustration of the global route construction.* — global route construction, circle, segment, truck.

![[_papers/wang2019routing/images/page_12_chart_7.jpg]]
*Fig. 12. The illustration of time balancing.* — time balancing, truck time, drone time, step 1, step 2, step 3.

The ellipse geometry turns truck-carried drone routing into a cluster-then-visit problem: customers are clustered by DBSCAN at endurance scale, each cluster becomes one segment on the truck route, and segments are sequenced by the truck backbone. ^[inferred]

## Related

- [[references/wang2019routing]] — the ellipse segment paper (Wang et al. 2019, IEEE IoT-J). ^[extracted]
- [[concepts/hybrid-truck-drone-delivery]] — the model that embeds segments in truck routes. ^[extracted]
- [[concepts/vehicle-routing-with-synchronization-constraints]] — launch-recover arcs as synchronization. ^[extracted]
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] — intra-segment open-loop route construction uses TSP insertion steps. ^[extracted]
- [[concepts/k-multi-visit-drone-routing-problem]] — multi-visit drones inside one endurance circle. ^[extracted]
- [[concepts/min-cost-tsp-with-drone]] — min-cost TSP-with-drone lineage for segment loops. ^[extracted]
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] — truck backbone plus drone arcs lineage. ^[extracted]

## Sources

- [[_papers/wang2019routing/wang2019routing-extracted]]
- [[_papers/wang2019routing/images/page_4_image_18.jpg]]
- [[_papers/wang2019routing/images/page_6_image_3.jpg]]
- [[_papers/wang2019routing/images/page_6_image_10.jpg]]
- [[_papers/wang2019routing/images/page_6_image_12.jpg]]
- [[_papers/wang2019routing/images/page_7_image_8.jpg]]
- [[_papers/wang2019routing/images/page_7_image_10.jpg]]
- [[_papers/wang2019routing/images/page_7_image_12.jpg]]
- [[_papers/wang2019routing/images/page_12_chart_3.jpg]]
- [[_papers/wang2019routing/images/page_9_image_3.jpg]]
- [[_papers/wang2019routing/images/page_9_image_12.jpg]]
- [[_papers/wang2019routing/images/page_10_chart_3.jpg]]
- [[_papers/wang2019routing/images/page_10_chart_6.jpg]]
- [[_papers/wang2019routing/images/page_10_chart_8.jpg]]
- [[_papers/wang2019routing/images/page_11_chart_3.jpg]]
- [[_papers/wang2019routing/images/page_11_chart_6.jpg]]
- [[_papers/wang2019routing/images/page_11_chart_8.jpg]]
- [[_papers/wang2019routing/images/page_12_chart_5.jpg]]
- [[_papers/wang2019routing/images/page_12_chart_7.jpg]]
