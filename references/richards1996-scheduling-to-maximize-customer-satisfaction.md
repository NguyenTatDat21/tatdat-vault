---
title: >-
  Scheduling to Maximize Customer Satisfaction: A Project for the Shad Valley Program
category: references
tags:
  - scheduling
  - linear-programming
  - transportation-problem
  - bottleneck-objective
  - leximax-leximin-fairness
  - course-scheduling
  - customer-satisfaction
  - network-flow
  - student-scheduling
  - shad-valley
relationships:
  - target: "[[concepts/leximax-leximin-fairness-principles]]"
    type: related_to
  - target: "[[concepts/periodic-scheduling-under-capacity-constraints]]"
    type: related_to
  - target: "[[references/bar-noy2004-efficient-algorithms-periodic-scheduling]]"
    type: related_to
  - target: "[[references/phanduc2025-pareto-front-grid-fairness-dpdptw]]"
    type: related_to
  - target: "[[references/ogryczak2014-fair-optimization-networks-survey]]"
    type: related_to
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
  - target: "[[references/hartman2023-leximin-approximation]]"
    type: related_to
  - target: "[[concepts/fuzzy-weighted-max-min-scalarization]]"
    type: related_to
sources:
  - _papers/richards1996scheduling/richards1996scheduling.md
  - _papers/richards1996scheduling/richards1996scheduling-extracted.md
  - _papers/richards1996scheduling/images/page_3_image_2.jpg
summary: >-
  Shad Valley student-seminar scheduling is a capacitated transportation problem; the max-min bottleneck model
  removes last-choice assignments that the total-satisfaction model can produce.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.67
tier: core
lifecycle: draft
lifecycle_changed: "2026-10-26T12:26:00Z"
created: "2026-10-26T12:26:00Z"
updated: 2026-10-27T06:00:00Z
---

# Richards & Bhadury 1996 — Scheduling to Maximize Customer Satisfaction (Shad Valley)

## Sections

### Problem setting

Shad Valley is a four-week summer program in science, technology and entrepreneurship for gifted
high-school students, offered at 8 Canadian universities and running 14 years in Canada. Students pay a
significant tuition fee, so the seminar schedule they receive materially affects their satisfaction. Before ^[inferred]
automation, the director scheduled [[concepts/periodic-scheduling-under-capacity-constraints|week by week]]: students gave first/second/third choices, all seminars had
to be subscribed, and maximum capacities had to be respected. The manual procedure was feasible for week 1
but became complicated in later weeks, because the quality of earlier weeks (1st, 2nd, 3rd or last choice)
had to be tracked per student.

Indices: students i, seminars j, weeks k. N students, S seminars over 4 weeks, Ŝ_k the seminars offered in
week k (k ∈ {1,2,3,4}), s_k the number of seminars in week k, S = s1 + s2 + s3 + s4. U_jk and L_jk are the
upper and lower enrolment limits; each student is assigned exactly one seminar per week; seminars are
volunteer-run, so cancelling a seminar is not normally permitted. r_ijK is student i's rank of seminar j in ^[inferred]
week k on a 1..5 scale (lower rank = higher preference), R the set of possible ranks, r_max the largest
element of R.

### Objective function

The preference score function is p_ijk = a(r_max − r_ijk), with a ≥ 2 (eq. 1). The value of a does not
affect quality; a = 2, 3, 4, 5 were tested and 2 was chosen, so that the preference vector P ordered as
p1 ≤ p2 ≤ … ≤ p_rmax is distinct — for R = {1,…,5} and a = 2 it gives P = {2^4, 2^3, 2^2, 2^1, 1}. The
decision variable is binary, x_ijk = 1 when student i is assigned to seminar j in week k.

### Model 1 — capacitated transportation problem

Constraints: L_jk ≤ Σ_i x_ijk ≤ U_jk for all j, k (3.1); plus (3.2); Σ_{j ∈ Ŝ_k} x_ijk = 1 for all k, i
(3.3); and x_ijk binary (3.4). Constraints (3.1)–(3.3) are exactly the constraints of the classical
Capacitated Transportation Problem, so the constraint matrix is totally unimodular and — with L, U integer
— the LP relaxation always returns an optimal integer solution, meaning (3.4) can be dropped and branch
and bound is unnecessary. Model 1 maximizes Z = Σ_i Σ_j Σ_k p_ijk x_ijk subject to (3.1)–(3.4) (eq. 4), and
can be solved as an LP, as a network flow, as a minimum-cost network flow, by the transportation simplex, ^[inferred]
or directly as a bipartite matching problem.

### Network formulation

The network is a directed acyclic graph G with node sets V_k = {V_k^1 … V_k^N} for students,
W_k = {W_k^1 … W_k^{s_k}} for seminars per week, a single source node A, a single sink node B, and all other
nodes as transshipment nodes; the total number of nodes is 4N + S. Arc set 1 connects every student to every
seminar in the same week (V_k^i → W_k^j) with lower bound 0, upper bound infinity, and cost per unit flow
−p_ijk, adding NS arcs. Arc set 2 connects seminar nodes to the sink (W_k^j → B) with lower bound L_jk, upper
bound U_jk, cost 0; the source states this set adds 4N arcs, which conflicts with the natural count S, so the
arc-count statements in this paragraph are recorded as a source inconsistency.^[ambiguous] Arc set 3 connects
the source to the students (A → V_k^i) with lower and upper bound exactly 1 and cost 0; the source states this
set adds S arcs. Supply at A and demand at B are fixed at 4N. x_ijk = 1 when the optimal flow on arc V_k^i →
W_k^j is 1 (eq. 5). G has O(N + S) nodes and O(NS) arcs, and Orlin's strongly polynomial algorithm solves it
in O(NS log(N+S)(NS + (N+S) log(N+S))).

![[_papers/richards1996scheduling/images/page_3_image_2.jpg]]
Fig. 1. Directed acyclic graph G.

### Model 2 — bottleneck objective, two phases

Model 2 maximizes Min over {i,j,k | x_ijk = 1} [p_ijk x_ijk] subject to (3.1)–(3.4) (eq. 6): a Bottleneck
Capacitated Transportation Problem, in the family of bottleneck generalized-assignment and transportation ^[inferred]
problems. The [[concepts/leximax-leximin-fairness-principles|max-min]] objective finds a schedule whose worst assignment for any student is as good as
possible. Because bottleneck problems usually have multiple optimal solutions, a second phase resolves ties.

Phase 1 yields the optimal assignment X* and its bottleneck preference score p_{q*}. Phase 2 adds the
constraint (p_ijk − p_{q*}) x_ijk ≥ 0 for all i, j, k (7.1), which excludes assignments worse than the
bottleneck, then maximizes Σ p_ijk x_ijk (eq. 7) subject to (3.1)–(3.4) and (7.1) — the same threshold-scalarization family as [[concepts/fuzzy-weighted-max-min-scalarization]]. In the 3-student,
3-seminar, single-week example (upper enrolment 1, lower 2, ranks from Table 1: A→I = 1, II = 3, III = 3;
B→I = 3, II = 1, III = 2; C→I = 1, II = 2, III = 3), Model 1 assigns A to I, B to II, C to III for total
satisfaction 9, but the worst assignment is a 3rd choice (C to III); Model 2 assigns A to I, B to III, C to
II for total 8 with the worst assignment at a 2nd choice.

### Search algorithm

Rather than solving the two models in sequence, each iteration picks a target preference score from P and
tests feasibility. Starting with p_1, preferences are modified to p'_ijk = p_ijk when p_ijk ≥ p_1 and
−infinity otherwise (eq. 8); the modified objective (eq. 9) is the same as eq. 4 with p′. A positive
optimum means a feasible assignment exists with no student below p_1; a negative optimum means the problem ^[inferred]
is infeasible. The procedure repeats with p_2, and stops at the first infeasible iteration or at p_{rmax}.
The appendix formalizes this as a loop over q = 1 … r_max that stores x_ijk whenever the LP value is
positive, prints "The Given Problem Is Infeasible" when q = 1 is infeasible, and reports p_{q−1} as the
optimal bottleneck preference score (Phase 1) and the stored x_ijk as the optimal assignment (Phase 2). The
appendix refers to the modified problem as "problem (11)", while the body numbers the same modified problem
(9) — a numbering drift within the source.^[ambiguous] Eq. 9 is solvable in the same time as Model 1, and
since |P| = r_max the LP is solved at most r_max times, giving Model 2 a time of
O(r_max NS log(N+S)(NS + (N+S) log(N+S))); binary searching P reduces the number of solves to at most
(log r_max), giving O(log r_max NS log(N+S)(NS + (N+S) log(N+S))).

### Shad Valley 1993 data

Week-by-week seminar offerings and enrolment limits are given in Table 3 for the Shad Valley 1993 program
(4 weeks, 10 seminar slots per week, ranks 1st–9th). N = 56 students, S = 33 seminars over 4 weeks,
8 seminars in weeks 1, 3 and 4 (n1 = n3 = n4 = 8) and 9 in week 2 (n2 = 9). Students ranked on a scale of
1–9, where 1 is highest. For programming convenience 10 seminars per week were assumed, with maximum
enrolment 0 for the non-existent seminars; rankings were converted to objective coefficients by eq. 1 with
a = 2. The model was solved on an IBM compatible PC (80486, 50 MHz, 16 Mb RAM) using LINDO Version 5.0, with
solution times under 10 seconds per run.

Model 1 (Table 4) reached objective function value 102,880. The staff judged the schedule reasonable, with
no significant departures from student desires, but one student (number 30) was assigned a fifth choice in
week 3, and the detail that this assignment was sacrificed was not revealed to students. Model 2 (Table 5)
reached objective function value 105,528. The parametric run on the 1993 data proceeded as: Step 1 choose
q = 2; Step 2 replace all objective coefficients ≤ 256 (2^8) with −999,999; Step 3 solve the LP; Step 4 the
value is negative, so infeasible; Step 5 choose q = 4; Step 6 replace coefficients ≤ 64 (2^6); Step 7 solve;
Step 8 the value is positive, so feasible; Step 9 choose q = 3; Step 10 replace coefficients ≤ 128 (2^5);
Step 11 solve; Step 12 the value is positive, so feasible; Step 13 the algorithm is over, and the solution
gives no assignment worse than a third choice, with the assignment in Table 5.

Model 2 guaranteed that the worst choice obtained by any student was a third choice, so no student received ^[inferred]
a fourth choice. Its overall satisfaction was not significantly worse than Model 1, and it is the assignment
the staff chose. Sensitivity analysis on the LP at the final iteration of Model 2 produced shadow prices for
the enrolment constraints, which identify the seminars where increasing the maximum attendance, or lowering
the minimum, would most improve the objective. The shadow price of a maximum constraint is the improvement in
the objective from allowing one more student; for a minimum constraint it is negative in this formulation.

### Shad Valley 1994 comparison

In 1994 a different individual was in temporary charge because of ill health of the previous director, and
decided not to use the system, so the data compare a manual year against the models computed on the same ^[inferred]
data. Seminar offerings were 5, 7, 5 and 6 in weeks 1–4, r_max was set to seven, and P = {128, 64, 32, 16, 8,
4, 2}. The manual objective value was 24,392 (Table 6); Model 1 gave 25,824 (Table 7); Model 2 gave 25,728
(Table 8). Model 2 reduced the worst assignment from 4 (students 22 and 23) to 3, at a cost of 96 relative to
Model 1, while still exceeding the manual result; the overall system schedule was better in the global sense
than the manual one by 1428 in objective value. The rank range implied by the seminar counts (5, 7, 5, 6 ^[inferred]
seminars → r_max 7) does not match the 9-column rank header printed in the tables, so the 1993 rank range is ^[inferred]
recorded as ambiguous.^[ambiguous]

### Implementation and conclusions

Implementation required only a computer, a Basic Interpreter, and an LP package such as Lindo, on a PC 386 ^[inferred]
with 4 MB RAM. The programs were adapted to varying seminar and student counts by changing parameters, all LP
inputs were produced automatically by the Basic programs, no LP/IP knowledge was needed, the administrator
prepared an ASCII file of student names and seminar offerings with minimum and maximum enrolments, and
students entered their rankings in a spreadsheet exported to a flat file. Output was a per-student assignment
listing and a seminar enrolment report. The extra cost was limited to acquiring an LP solver, with no
additional staffing. The authors report students and staff benefited, that the 1993 program required
considerably less time than the manual 1992 program, that no direct measure of satisfaction between years is
available, that modelling increased the credibility of the schedule, and that it is fair to state student
satisfaction was greater in 1993 than 1992.

The conclusions are that automation guarantees consistency, is faster, and accommodates unanticipated
changes such as cancelled seminars or student illness; that Model 2 is preferable to Model 1 because Model 1
maximizes total satisfaction and can result in very poor assignments for one or a few students, while Model 2
gives individual satisfaction first priority and then maximizes overall satisfaction, and is easy to solve on
a PC; and that the shadow prices of the enrolment constraints identify extremely popular and unpopular
seminars, so the program should target enrolment changes for the next year, and possibly negotiate immediate
changes with the seminar leaders and re-run. Future work listed week-to-week scheduling as an alternative to
constructing the whole 4-week schedule, since it reduces the solution space, more flexibility to allow
seminars to be added and dropped mid-program, and four smaller sub-problems for larger systems, with current
running times of less than 10 seconds. Duplicate seminar offerings across weeks add constraint
Σ_{j,k duplicates} x_{i,j,k} ≤ 1 for all i; each pair of duplicate seminars adds N constraints, destroying the
unimodular structure, so the LP relaxation may need to be converted to an integer formulation. In a
hypothetical 1993 data set with 3 duplicate seminars, Model 1 with 168 additional constraints was solved in 8
seconds and the LP relaxation solution was integer, suggesting small numbers of such constraints — with ^[inferred]
coefficients of 1 — do not totally destroy the strong network structure. Acknowledgement: NSERC Grant #OGP 012
1689, plus thanks to Shad Valley staff, A. P. Punnen and an anonymous referee.

## Related
- [[concepts/leximax-leximin-fairness-principles]] — the max-min-first, then-total ordering of Model 2 is the same two-stage fairness structure, and the parametric q-loop is a lexicographic threshold sweep.
- [[concepts/periodic-scheduling-under-capacity-constraints]] — recurring weekly enrolment with lower and upper bounds on seminar capacity, solved through the periodic structure of the 4-week program.
- [[references/bar-noy2004-efficient-algorithms-periodic-scheduling]] — shares the periodic, capacity-bounded assignment structure with the Shad Valley week-by-week model.
- [[references/phanduc2025-pareto-front-grid-fairness-dpdptw]] — parallel fairness evidence: optimizing total cost while bounding the worst-off user through a grid of threshold values.
- [[references/ogryczak2014-fair-optimization-networks-survey]] — orders fairness objectives over networks, and the sum/bottleneck pair here is the classic equity-vs-total trade-off. ^[inferred]
- [[references/furini2016-two-dimensional-guillotine-cutting-ip]] — parallel case study of a capacity-constrained scheduling/cutting program solved as an ILP, with the LP-relaxation quality argument made here in cutting-stock form.
- [[references/hartman2023-leximin-approximation]] — the approximation-theoretic version of the same max-min-then-lexicographic ordering that Model 2 solves exactly by threshold sweep.
- [[concepts/fuzzy-weighted-max-min-scalarization]] — the scalarization family that generalizes the single threshold used in the parametric q-loop. ^[inferred]

## Sources
- [[_papers/richards1996scheduling/richards1996scheduling.md]] — Zotero sidecar: Richards, E. W.; Bhadury, J. (1996), Computers & Industrial Engineering, 1996-09, doi:10.1016/0360-8352(95)00185-9.
- [[_papers/richards1996scheduling/richards1996scheduling-extracted.md]] — full extracted text (530 lines, 4-page scan), read in windows 1–300 and 301–530.
- [[_papers/richards1996scheduling/images/page_3_image_2.jpg]] — Fig. 1 (directed acyclic graph G), the only embedded figure. All other crops are equation and table crops (no caption anchors), so they are not embedded; the tables are transcribed as text. ^[inferred]
-^[ambiguous] The source itself records internal inconsistencies: arc-count statements for arc sets 2 and 3, the "problem (11)" vs "(9)" numbering drift, and the 1993 rank range (9 ranks in the tables) vs the 1994 r_max of 7. Every numeric value above is transcribed verbatim from the extracted markdown; the vault contains no PDFs, so `pdftotext` cannot be used to disambiguate the scan.
