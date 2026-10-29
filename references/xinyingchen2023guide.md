---
title: A guide to formulating fairness in an optimization model (Chen & Hooker 2023)
summary: "Fairness criteria in optimization: inequality measures, maximin, leximax, convex combination, alpha fairness, Nash bargaining, Kalai-Smorodinsky, thresholds, parity, guidelines, MILP formulations."
tags: fairness, optimization, welfare-social-function, survey, distributive-justice
provenance:
  extracted: 0.80
  inferred: 0.16
  ambiguous: 0.04
base_confidence: 0.67
tier: core
created: 2026-10-29T17:35:00Z
updated: 2026-10-29T17:35:00Z
sources:
- _papers/xinyingchen2023guide/xinyingchen2023guide.md
- _papers/xinyingchen2023guide/xinyingchen2023guide-extracted.md
relationships:
- {target: "concepts/welfare-social-function-fairness-formulations", type: related_to}
- {target: "references/yi2023-ace-gsf-automated-design-cvrptw", type: related_to}
- {target: "concepts/inequality-measures-fairness-formulations", type: related_to}
- {target: "concepts/group-parity-fairness-metrics", type: related_to}
- {target: "concepts/alpha-fairness-proportional-fairness", type: related_to}
- {target: "concepts/nash-bargaining-solution-axioms", type: related_to}
- {target: "concepts/kalai-smorodinsky-bargaining-solution", type: related_to}
- {target: "concepts/utility-fairness-thresholds", type: related_to}
- {target: "concepts/sequential-leximax-threshold-models", type: related_to}
- {target: "concepts/convex-combination-weights-fairness", type: related_to}
- {target: "concepts/maximin-leximax-fairness", type: related_to}
- {target: "concepts/leximax-leximin-fairness-principles", type: related_to}
- {target: "references/ogryczak2014-fair-optimization-networks-survey", type: related_to}
- {target: "references/hartman2023-leximin-approximation", type: related_to}
- {target: "references/phanduc2025-pareto-front-grid-fairness-dpdptw", type: related_to}
lifecycle: source
lifecycle_changed: 2026-10-29T17:35:00Z
---

> [!tldr] Chen & Hooker 2023 (Annals of Operations Research): a critical survey of fairness criteria for optimization models, with practical formulations for linear, nonlinear, and mixed-integer programming, and axiomatic/bargaining derivations under interpersonal comparability.

## Source
- [[_papers/xinyingchen2023guide/xinyingchen2023guide]] — sidecar, zotero-key GQ22QRRP, DOI 10.1007/s10479-023-05264-y, accepted 2023-02-24, published 2023-07-01.
- [[_papers/xinyingchen2023guide/xinyingchen2023guide-extracted]] — extracted text.

## Overview
Chen (Stevens Institute of Technology, vchen3@stevens.edu) and Hooker (Carnegie Mellon, jh38@andrew.cmu.edu) survey fairness schemes proposed for optimization models: inequality measures, Rawlsian maximin and leximax, convex combinations, alpha fairness, proportional fairness = Nash bargaining, Kalai–Smorodinsky bargaining, utility-/fairness-threshold schemes, and group parity metrics popular in machine learning. They present what appears to be the best practical formulation of each criterion in a linear, nonlinear, or mixed-integer model, survey axiomatic and bargaining derivations from social choice taking interpersonal comparability of utilities into account, and cite philosophical and ethical literature. Tables 1–3 list each fairness criterion with the labels 'Nonlin?' and 'Integer?': inequality measures relative range, relative mean deviation, coefficient of variation, Jain's index, Gini coefficient, Hoover index; group parity: demographic parity, equalized odds, accuracy parity, predictive rate parity; convex combinations, maximin, leximax, McLoone index, alpha fairness, proportional fairness, Kalai–Smorodinsky, efficiency threshold, fairness threshold, efficiency threshold with predefined priorities, efficiency threshold with no priorities; maximin, leximax, maximin threshold, sequential leximax, fairness threshold. The paper closes with guidelines for selecting a criterion, and the appendix presents models for all social welfare functions. 2023 Annals of Operations Research, accepted 2023-02-24, published online 2023-04-07. ^[inferred]

## Welfare models
- Welfare maximizing models eq. 1 `max{W(u) | u=U(x), x∈S_x}` and eq. 3 `max{W(u) | (u,x)∈S}`, maximizing over a welfare social function (SWF) that trades off utilities. ^[inferred]
- Welfare constraining models eq. 2 `max{f(x) | W(u)≥LB, u=U(x), x∈S_x}` and eq. 4 `max{f(x) | W(u)≥LB, (u,x)∈S}` — used when no suitable SWF is available, e.g. a minimum fairness requirement; the triage example allocates budget B with costs c_i, utilities `u_i = a_i + b_i x_i`, QALYs. ^[inferred]
- Mortgage-approval example `u_i = p_i x_i` with 0/1 decisions, minimizing ΣR_i(x_i), upper bound x_i≤a_i. ^[inferred]
- Advantages: welfare maximizing regulates the efficiency-fairness tradeoff; welfare constraining applies when no suitable SWF, e.g. a minimum fairness. ^[inferred]

## Inequality measures
- Relative range `W(u)=−(1/ū)(u_max−u_min)` with ū=(1/n)Σu_i, linear fractional Charnes & Cooper 1962; relative mean deviation W(u)=−(1/ū)Σ|u_i−ū| linearizable; coefficient of variation convex nonaffine; Jain's index `W(u)=ū²((1/n)Σu_i²)⁻¹=1/(1+c_v²)`, 1 equality, 1/n perfect inequality; Gini `G(u)=(1/2ūn²)ΣΣ|u_i−u_j|`, Lorenz, linear fractional; Hoover index `W(u)=−(1/2nū)Σ|u_i−ū|` proportional to relative mean deviation. ^[inferred]
- Jain's index is strictly monotone in the coefficient of variation; QoE fairness Georgopoulos 2013, Hoßfeld 2018, TCP fairness Pokhrel 2016, G's fairness index, Bossaert's fairness index Mehta 2020. ^[inferred]
- Inequality metrics measure relative not absolute levels; philosophical range: equality≠fairness Frankfurt 2015, Parfit 1997, Scanlon 2023; Karsu & Morton 2015, Leonhardt et al. 2018, Speicher et al. 2018, Sühr et al. 2019 generalized entropy. ^[inferred]

## Group parity metrics
- Group parity in ML: N protected, N' rest, a_i=1 selection, δ decisions, W(δ)=1−|B(δ)|; demographic parity `B(δ)= (1/|N|)Σδ_i − (1/|N'|)Σδ_i`, 0≤W≤1, complete parity W=1, Dwork et al. 2012, critiques; equalized odds equality of opportunity `B(δ)=Σa_iδ_i/Σa_i (N) − Σa_iδ_i/Σa_i (N')` eq. 6, qualified/qualified rates among qualified, unqualified false positive rate; accuracy parity `B(δ)= (1/|N|)Σ(a_iδ_i+(1−a_i)(1−δ_i)) − (1/|N'|)Σ…` eq. 8; predictive rate parity `B(δ)=Σa_iδ_i(N)/Σδ_i(N) − Σa_iδ_i(N')/Σδ_i(N')` eq. 9, risk-assessment recidivism Dieterich 2016, Chouldechova 2017, child maltreatment screening Chouldechova et al. 2018. ^[inferred]
- Demetric parity too strict for qualified individuals, no consensus among the four, pairwise incompatible; first three admit easy linear formulations, predictive rate parity is an extremely difficult optimization problem. ^[inferred]

## Maximin, leximax, McLoone
- Rawls difference principle, social-contract original position, maximin W(u)=min_i{u_i} linearizable; institutions and primary goods Freeman 2003, Richardson & Weithman 1999; maximin in bandwidth allocation Luss 1999, Ogryczak & Śliwiński 2002, Ogryczak et al. 2008, reviewer assignment Stelmakh et al. 2018, ridesharing Nanda et al. 2020, medical appointment scheduling Samorini et al. 2021, ML Rawlsian Hashimoto 2018, Heidari 2019, Shah 2021. ^[inferred]
- Maximin equality cost: budget Σx_i≤B, u_i=a_i x_i, maximin equalizes utilities, u_0=B/Σ(1/a_i), expensive welfare of individual k, upper bound d_k reduces everyone to a_k d_k, unused resources B−d_k a_k Σ(1/a_i). ^[inferred]
- Leximax lexicographic sequence removes leftover resources, avoids the high equality cost. McLoone index `W(u)=1/(|I(u)|ũ) Σ_{i∈I(u)} u_i`, ũ median, I(u)={i|u_i≤ũ}; 1 if none below median, 0 for long lower tail, 0-1 variables, fractional objective, linearized MILP, lower half. ^[inferred]

## Convex combinations and alpha fairness
- Convex combinations `W(u)=(1−λ)Σu_i+λΦ(u)`, λ interpretation problem; Eisenhandler & Tzur 2019 product SWF `Σu_i−(1/n)Σ_{i<j}|u_j−u_i|` (λ=1/2), Mostajabdaveh et al. 2019 `Σu_i+μ(1−G)Σu_i`, λ=μ/(1+μ); convex-combo maximin eq. 10, decreasing weights eq. 11, multi-criteria Yager 1997, Ogryczak & Śliwiński 2003, Hu & Chen 2020 ML classifier correspondence; stakeholder elicitation Gralla 2014, Carland 2018, Yilmaz & Kabak 2020, Hasnain 2021; Argyris et al. 2022 welfare-based dominance constraints MILP, weighted ordered averages continuum utilitarian↔maximin; Rea et al. 2021 request-vs-allocation deviations. ^[inferred]
- Alpha fairness Mo & Walrand 2000, Verloop et al. 2010 `W_α=(1/(1−α))Σu_i^{1−α}` for α≥0 α≠1, `Σlog(u_i)` for α=1; continuum α=0 utilitarian, α→∞ maximin; Bertsimas et al. 2012 worst-case trade-offs; α interpretation u_j reduced by (u_j/u_i)^α to compensate a unit increase in u_i. Lan & Chiang 2011 partition axiom, Kolmogorov mean h, ratio-scale comparability Roberts 1980, Lan et al. 2010, unnormalized Theil/Atkinson logarithmic. Proportional fairness α=1 product Πu_i, Nash bargaining = hyperrectangle volume Fig. 1a, bandwidth Kelly et al. 1998, Mazumdar et al. 1991. α anomaly: α≥1 (1,1) vs (t,T), t=1/T α=1, t=(2−T^{1−α})^{1/(1−α)} α>1, T^{1−α}<2. ^[inferred]

## Nash bargaining and Kalai–Smorodinsky
- Nash bargaining scale invariance φ_i=β_i u_i rules out utilitarian and Rawlsian, anonymity, Pareto, independence of irrelevant alternatives; Lan & Chiang 2022 partition axiom, alpha fairness family, maximin/minimax; Harsanyi 1977, Rubinstein 1982, Binmore et al. 1986, default d, SWF Π(u_i−d_i), Zeuthen 1955 procedure, expected (1−p_2)u_1+p_2 d_1. ^[inferred]
- Kalai–Smorodinsky eq. 17 `max-fraction β: u=(1−β)d+βu^max` SWF = Σu_i if u=(1−β)d+βu^max 0≤β≤1, 0 otherwise, u_i^max=max_{x,u}{u_i|(u,x)∈S}; monotonicity replacing independence of irrelevant alternatives; Thompson 1994, Gauthier 1983 contractarian, labor-management Alexander 1992; no α parameter; Dworkin 1981/2000, Barry 1988. ^[inferred]
- Fig. 1a Nash bargaining, Fig. 1b Kalai–Smorodinsky, both default position the origin. [[_papers/xinyingchen2023guide/images/page_18_image_2.jpg]], [[_papers/xinyingchen2023guide/images/page_18_image_4.jpg]]
- In both cases, the default position is the origin. Sec. 12 summary: SWF objective/constraint, utilities SWF perspective, categories/interpretations/optimization-suitable formulations.

## Threshold criteria
- Williams & Cookson 2020 two ways, parameter Δ easier than α, groups of different sizes, no axiomatic/bargaining justification, inherit maximin limitations; Hooker & Williams 2012 n-person efficiency-threshold MILP polyhedral healthcare, Elçi et al. 2022 fairness-threshold LP; efficiency-threshold parties within Δ of worst-off get priority, fairness-threshold parties >Δ above lowest no benefit. ^[inferred]
- 2-person efficiency-threshold SWF: `u_1+u_2` if |u_1−u_2|≥Δ, `2min{u_1,u_2}+Δ` otherwise, Fig. 2, continuity; hooker-wills `W(u)=(n−1)Δ+Σmax{u_i−Δ,u_min}` eq. 13, fair region u_i−u_min≤Δ, Δ=0 utilitarian/∞ maximin, groups `W^g=(Σs_i−1)Δ+Σs_i max{u_i−Δ,u_min}` eq. 14, MILP healthcare realistic size, Gerdessen et al. 2018 Pareto frontier convex-combo, count of disadvantaged. ^[inferred]
- Fairness-threshold 2-person SWF `2min+Δ` if |u1−u2|≥Δ, `u1+u2` otherwise, Fig. 3, utilitarian open dot, welfare-maximizing black dot, Elçi `W(u)=nΔ+Σmin{u_i−Δ,u_min}` eq. 15, groups `W^g=(Σs_i)Δ+Σs_i min{u_i−Δ,u_min}` eq. 16; equate solutions with very different fairness. ^[inferred]
- Maximin threshold ignores disadvantaged other than worst-off, constraint-set cap; McElfresh & Dickerson 2020 kidney exchange preference ordering, fair region max−min≤Δ, SWF eq. 17 `W=n u_1` if all |u_i−u_j|≤Δ, `Σu_i+sgn(u_1−u_i)Δ` otherwise; continuity claim false for n>2 counterexample W(0,0,Δ+ε)=ε, W(0,ε,Δ+ε)=2ε−Δ. ^[inferred]
- Chen & Hooker 2022 sequence `W_1=` Hooker-Wills, `W_k=Σ_{i=1}^{k-1}(n−i+1)u_⟨i⟩+(n−k+1)min{u_⟨1⟩+Δ,u_⟨k⟩}+Σ_{i=k}^n(u_⟨i⟩−u_⟨1⟩−Δ)^+ k=2..n`, γ^+=max{0,γ}, u_⟨i⟩ nondecreasing order; weight in fair region = number with same/greater utility, utilitarian unit weight; value independence ensures SWF continuity; socially optimal u*_⟨i⟩, valid inequalities, healthcare resource and earthquake shelter location seconds for given Δ. ^[inferred]

## Guidelines (Sec. 11, verbatim)
- Inequality metrics limited: no absolute levels, relative range outliers, relative mean deviation, Hoover proportional, CV/Gini widely used, Jain = CV, simple linear models. ^[inferred]
- ML group parity: demographic parity too strict qualifications, equalized odds, accuracy parity, predictive rate parity extremely difficult MILP/nonlinear, first three easy linear, no consensus, pairwise incompatible. ^[inferred]
- Disadvantaged: Rawls social contract, maximin surprising implications (incurable disease massive transfer, limit transfer reduces further, unused resources), leximax remedy, McLoone educational equality/public policy. ^[inferred]
- Convex combinations λ units; alpha fairness principled, engineering wide, nonlinearity, α interpretation welfare-preserving transfers, α≥1 anomaly. ^[inferred]
- Kalai–Smorodinsky suitable bargaining, unsuitable utility potential impairment, no parameter. ^[inferred]
- Threshold SWFs: Δ easier, groups, avoid anomaly; efficiency-threshold health/political sensitive, MILP readily solved; fairness-threshold traffic/telecom/disaster recovery, linear. ^[inferred]
- Maximin inheritance, constraint-set cap a priori; leximax threshold models: predefined preference organ transplants discontinuous SWF small changes large welfare; sequential SWFs continuous MILP readily solved, complexity impedes stakeholders; no fairness-threshold efficiency+leximax developed. ^[inferred]
- Sec. 12: SWF as objective/constraint, utilities SWF perspective, categories/interpretations/optimization-suitable formulations.
- Fig. 2 caption: 'Contours for the fairness-threshold SWF'; Fig. 3 'Contours for the fairness-threshold SWF' — utilitarian open dot, welfare-maximizing black dot. [[_papers/xinyingchen2023guide/images/page_21_image_3.jpg]]
- Tables 1–3 summarize criteria with Nonlin?/Integer? columns, welfare maximizing/constraining models, triage, mortgage approval. ^[inferred]
- Sec. 3 axiomatic derivations: invariance transformation φ(u), unit comparability φ_i(u_i)=βu_i+γ_i utilitarian, level comparability maximin/minimax, Nash bargaining scale invariance, monotonicity Kalai–Smorodinsky. ^[inferred]
- Sec. 4 inequality measures, equality≠fairness philosophical range, generalized entropy. ^[inferred]

## Related
- [[concepts/welfare-social-function-fairness-formulations]] — the welfare maximizing/constraining models, eq. 1–4.
- [[concepts/inequality-measures-fairness-formulations]] — relative range, relative mean deviation, coefficient of variation, Jain's, Gini, Hoover.
- [[references/yi2023-ace-gsf-automated-design-cvrptw]] — the RL-design goal that Chen & Hooker (2023) discuss in the survey's ML track.
- [[concepts/group-parity-fairness-metrics]] — demographic parity, equalized odds, accuracy parity, predictive rate parity.
- [[concepts/alpha-fairness-proportional-fairness]] — alpha fairness family, proportional fairness α=1, anomaly.
- [[concepts/nash-bargaining-solution-axioms]] — Nash bargaining SWF, scale invariance, Zeuthen.
- [[concepts/kalai-smorodinsky-bargaining-solution]] — equal fraction of potential gains, monotonicity.
- [[concepts/utility-fairness-thresholds]] — efficiency and fairness threshold SWFs, hooker-wills, Elçi.
- [[concepts/sequential-leximax-threshold-models]] — Chen & Hooker 2022 sequence, kidney exchange, valid inequalities.
- [[concepts/convex-combination-weights-fairness]] — λ weights, decreasing weights, dominance constraints, elicitation.
- [[concepts/maximin-leximax-fairness]] — maximin, leximax, McLoone, equality cost.
- [[concepts/leximax-leximin-fairness-principles]] — lexicographic maximin and leximax, OWA limits, water-filling.
- [[references/ogryczak2014-fair-optimization-networks-survey]] — inequality-averse fair optimization, fair dominance, alpha fairness.
- [[references/hartman2023-leximin-approximation]] — leximin approximation results for multi-objective fair optimization.
- [[references/phanduc2025-pareto-front-grid-fairness-dpdptw]] — Pareto-front-grid fairness selection in dynamic pickup-and-delivery.
- [[references/goel2015-constraint-programming-lng-ship-scheduling]] — maximin fairness in ship scheduling.
