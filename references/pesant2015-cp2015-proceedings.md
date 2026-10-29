---title: "Principles and Practice of Constraint Programming — CP 2015 Proceedings (LNCS 9255)"
summary: "CP 2015 proceedings (LNCS 9255, ed. Pesant): 48 technical papers, 3 invited talks, 16 fast/journal-track abstracts, erratum, front matter, Author Index; 73 items, zero figures."
tags: [CP-2015, constraint-programming, proceedings-volume, encodings, scheduling, decision-diagrams, tractability, search]
provenance:
  extracted: 0.82
  inferred: 0.15
  ambiguous: 0.03
  base: 0.00
base_confidence: 0.67
tier: reference
created: 2026-10-29T15:40:00Z
updated: 2026-10-29T15:52:00Z
sources:
  - _papers/pesant2015principles/pesant2015principles.md
  - _papers/pesant2015principles/pesant2015principles-extracted.md
relationships:
  - { target: "concepts/encoding-preservation-under-composition-and-merging", type: "inbound" }
  - { target: "concepts/lagrangian-decomposition-propagation", type: "inbound" }
  - { target: "concepts/bound-tightening-relaxation-networks", type: "inbound" }
  - { target: "concepts/decision-diagrams-optimization", type: "inbound" }
  - { target: "concepts/search-combinators-meta-search", type: "inbound" }
  - { target: "concepts/automated-model-generation", type: "inbound" }
  - target: "[[concepts/decision-diagrams-optimization]]"
    type: related_to
  - target: "[[concepts/encoding-preservation-under-composition-and-merging]]"
    type: related_to
  - target: "[[concepts/lagrangian-decomposition-propagation]]"
    type: related_to
  - target: "[[concepts/bound-tightening-relaxation-networks]]"
    type: related_to
  - target: "[[concepts/search-combinators-meta-search]]"
    type: related_to
  - target: "[[concepts/automated-model-generation]]"
    type: related_to
lifecycle: active
lifecycle_changed: 2026-10-29T15:52:00Z
provenance_note: "Zotero item BAKF26BL (library-id 11058526, itemType book, Gilles Pesant (ed.), Springer, 2015, DOI 10.1007/978-3-319-23219-5). Provenance by script: 295 statement units, 89 verbatim markers (page-and-chapter citations, the 89 paper-index table rows, quoted equations, named algorithms, exact counts), 206 units without markers. Extracted rounded to 0.82; inferred 0.15 for theme-section grouping and author-name ordering; ambiguous 0.03 because fast-track and journal-track footnotes cite journal versions, so those items carry no Springer chapter DOI. Zero images in the source, so no captions to verify. Zero source page footnotes on the invited talks, so no page numbers are asserted for them."
---
# Principles and Practice of Constraint Programming — CP 2015 Proceedings (LNCS 9255)

> [!tldr] The full CP 2015 proceedings (Cork, Ireland, 31 Aug – 4 Sep 2015, LNCS 9255, ed. Gilles Pesant) as one book source: 48 technical-track papers, 3 invited-talk abstracts, 6 fast-track and 10 journal-track abstracts, an erratum (p. E1), front matter, and the volume Author Index — 73 items in 18,510 source lines, zero figures.

## Citation

Pesant, G. (ed.). **Principles and Practice of Constraint Programming: 21st International Conference, CP 2015, Cork, Ireland, August 31 – September 4, 2015, Proceedings.** Springer International Publishing, 2015. Lecture Notes in Computer Science 9255. DOI 10.1007/978-3-319-23219-5. Zotero key `BAKF26BL`, library-id 11058526, extracted text `_papers/pesant2015principles/pesant2015principles-extracted.md` (18,510 lines, 73 `# ` headings, zero image embeds).

The conference was part of **George Boole 200** (the bicentenary of Boole's 1815 birth at University College Cork) and was co-located with the **31st International Conference on Logic Programming (ICLP 2015)**. It featured three invited talks (Claire Bagley, Gerhard Friedrich — joint with ICLP, Douglas R. Smith), four tutorials, six satellite workshops, a Doctoral Program, the MiniZinc Challenge results, a joint ICLP/CP programming competition, a first Industry Outreach effort led by Helmut Simonis, and a post-conference CSPlib sprint. Program chair Gilles Pesant; conference chairs Ken Brown and Barry O'Sullivan; application track chair Louis-Martin Rousseau; journal track chair Thomas Schiex; doctoral program chairs David Bergman and Marie Pelleau; workshop and tutorial chair Willem-Jan van Hoeve.

## Volume anatomy

- idx 1-5: cover, LNCS series front matter, title/copyright page + preface, tutorials and workshops, conference organization roster.
- idx 6-8: the three invited-talk abstracts, printed in the front matter without page footnotes.
- idx 9-56: 48 technical-track papers, chapter numbers 1-48, volume pages 3-721. **Chapter number = source index − 8** for idx 9-56 — verified against every paper's own page-1 Springer footnote.
- idx 57: the volume Erratum (p. 722, DOI chapter 53).
- idx 57: the volume Erratum, printed as page E1 (the Contents list it as "Erratum to: Modeling Universal Instruction Selection.... E1").
- idx 58-63: abstracts of papers fast-tracked to *Constraints* journal (pp. 723-729, six items).
- idx 64-73: abstracts of published journal-track papers (pp. 733-743, ten items), including Weller's MWSS/tractability abstract at p. 743, the last research item in the volume.
- Author Index, pp. 745-755, as a separate book feature: author → page numbers, no research content.

LNCS volume number 9255 is printed in the page footnotes of every technical-track paper, so page ranges and DOI chapter numbers for idx 9-56 are authoritative per item; the invited talks, the fast-track and journal-track abstracts, and the erratum carry no Springer chapter DOI in the extracted text.

## Keynotes and invited talks

The three invited-talk abstracts are printed in the front matter with no page footnotes, so the extracted text gives no page numbers for them; they are not DOI chapters.

- **Constraint-based Problems and Solutions in the Global Enterprise** (Claire Bagley, Oracle): surveying the combinatorial problems faced by a large technology corporation and the role of Oracle's Advanced Constraint Technology (ACT) group, tasked with identifying, understanding and solving them; the industrial framing of the talk is the origin of the CP 2015 Industry Outreach effort.
- **Industrial Success Stories of ASP and CP: What's Still Open?** (Gerhard Friedrich, Siemens, joint with ICLP): more than 25 years of configuration work with Siemens using CP, then ASP encodings, with the open problem of automating the generation of problem-specific heuristics; the abstract cites the QuickPup partner-unit configuration work, Pearl's heuristic discovery, and search combinators.
- **Synthesis of Constraint Solvers** (Douglas R. Smith & Stephen J. Westfold, Kestrel Institute): a mathematical framework from abstract interpretation for specifying and formally designing high-performance constraint solvers, built on the Kestrel technical report of 2013; the thesis is that a *generated* native solver always outperforms a reduction to an existing solver.

## Encoding, satisfiability, and the boundary to SAT

Six papers refine encodings of linear and counting constraints into CNF. Abio, Mayer-Eichberger & Stuckey exploit the implication chains `x1 ⇐ x2 ⇐ …` that already exist in a problem, so the combined encoding is no larger and propagates strictly stronger than the separate encodings (pp. 3-11, chapter 1) — tested on sports-league scheduling. Karpinski & Piwonski build selection comparator networks smaller than pairwise networks for cardinality constraints and prove that standard CNF encodings of selection networks preserve arc-consistency (pp. 210-225, chapter 16). Abio, Bessiere & Stuckey's generalized totalizer encoding for pseudo-Boolean constraints targets the decision problem only (pp. 200-209, chapter 15). Nightingale, Spracklen & Miguel add common-subexpression elimination to the Savile Row translator, operating on the abstract syntax tree before SAT encoding — `x × y` repeated three times becomes one new variable plus one constraint — and describe an identical-CSE algorithm independent of the target language (pp. 330-340, chapter 23). Stojadinovic & Maric's **meSAT** translates finite linear CSP specifications using direct, log, support, order and compact-order encodings plus their direct-support and direct-order combinations (p. 741, journal-track abstract). Monette, Flener & Pearson eliminate flattened auxiliary variables — 84% of them occur in exactly two constraints — by pattern matching two constraints sharing an auxiliary variable and compiling an indexical propagator for the merged predicate, implemented as `var-elim-idxs` for FlatZinc/Gecode (pp. 313-329, chapter 22).

On the SAT side, Ignatiev, Pretwich, Morgan, Marques-Silva & Lynagher extract a smallest minimal unsatisfiable subset (SMUS) by minimal hitting-set dualization, motivated by validating the quality of MUSes computed by modern extractors (pp. 173-182, chapter 13). Cooper, Duchein & Escamocher revisit **broken triangles**: BTP-merging preserves satisfiability, and the paper asks whether the order of merging and arc-consistency operations can be chosen to maximize domain reductions, proving results on the interaction of the two operations (pp. 58-73, chapter 5). Razgon simulates DNNF by a non-deterministic read-once branching program in quasipolynomial time (pp. 367-375, chapter 26). Ivrii, Malik, Meel & Vardi reduce the length of XORs and remove gates to find a minimal independent support 1/10–1/100 the size of the original, giving 1–2 orders of magnitude speed-up for uniform sampling, probabilistic inference and bounded equivalence reasoning (p. 725, fast-track abstract). Jefferson, Jeavons, Green & van Dongen represent finite-domain constraints as systems of multivariate polynomials whose simultaneous zero evaluations define allowed tuples, making Gröbner-basis processing singly exponential for finite domains and unifying constraint and continuous representations via standard computer algebra (p. 737, journal-track abstract). Jonsson & Lagerqvist initiate the study of upper bounds on the time complexity of NP-hard infinite-domain CSPs, measured as a function of the number of variables (pp. 183-199, chapter 14).

## Tractability, microstructure, and local consistency

Cooper, Jégou & Terrioux characterize a microstructure-based family of polynomially solvable binary CSP classes of maximal tractable width, using the microstructure encoding, tree decompositions and the Boolean-width of the microstructure graph (pp. 74-88, DOI 6). Kong, Li & Liu identify tractable classes of tree-convex constraints closed under the composition and intersection used by path-consistency, since row-convex and tree-convex classes are not closed under those operations and path-consistency can destroy the property (pp. 244-261, DOI 18). Stergiou revisits **restricted path consistency** twenty years after its proposal, comparing RPC, rRPC and maxRPC with arc consistency as the practical local consistency for binary constraints (pp. 419-428, DOI 30). Pesant's dispersion-constraint abstract achieves domain consistency and counts solutions for `spread`/`deviation`-style balance constraints, improving the state of the art on Nurse to Patient Assignment and the Balanced Academic Curriculum Problem (p. 740, DOI 66). Beldiceanu, Carlsson, Flener & Pearson reify global constraints `G(A)` as `R(A) ∧ (C(A) ⇔ b)` requiring the negation to satisfy the same restrictions, and report that 313 of 381 constraints in the Global Constraint Catalogue (82%) are reifiable (p. 733, DOI 60). Weller extends MWSS-on-NMRF reparameterizations to **all** reparameterizations of Boolean binary weighted models, giving an exact characterization of the enlarged tractable set and proving which pruned NMRFs are perfect (pp. 743-744, DOI 69).

The Benders/Lagrangian lineage of the volume continues in Bergman, Cire & van Hoeve, who add Lagrangian penalty costs between pairs of constraints so duplicated variable copies must agree, giving stronger bound computation and cost-based domain filtering for constraints represented by decision diagrams (pp. 30-38, DOI 3), and in Ha & Quimper, whose general bounding mechanism derives objective bounds for nonlinear global constraints (all-different, global cardinality, regular) that linear-relaxation-based IP solvers cannot express (pp. 158-172, DOI 12).

## Decision diagrams and automata

Bergman, Cire & van Hoeve prove MDD consistency on the Sequence constraint is **NP-hard** — the first negative result of its kind, because Sequence has the most MDD-friendly structure (prescribed variable ordering, contiguous sub-constraints, bounds reasoning) — and show it is fixed-parameter tractable in sub-sequence length (p. 734, DOI 61). Bergman, Cire, van Hoeve & Hooker recast discrete optimization as branch-and-bound in which **relaxed** BDDs play the role of the linear-programming relaxation (bounds and branching guidance) and **restricted** BDDs supply the primal heuristic, compiled from a dynamic-programming model with relaxation and restriction operators; the relaxed BDD gives the tightest MAXCUT bounds reported, in INFORMS J. Computing 2015 (p. 735, DOI 62). Beldiceanu, Carlsson, Douceon & Simonis describe the finite-transducer program: ~30 catalogue constraints unified by automata, 600+ new constraints synthesised, 100,000+ generated lines, in use as the structural backbone of the constraint library (p. 723, DOI 54). Papadopoulos, Pachet, Roy & Sakellariou give **perfect sampling** for Markov models with Regular constraints via a factor graph of binary factors combining a Markov chain and an automaton, with belief propagation adapted for sampling; Theorem 1 reduces sampling `p_target` to sampling `p_reg` plus projection, with a semiotic-structure example in the style of Bill Evans (pp. 341-350, DOI 24).

## Scheduling, resources, and time

The cumulative constraint is the volume's most recurrent object. Gay, Hartert, Lecoutre & Schaus give a simple, scalable time-table filtering for Cumulative, beating the O(n²) synchronized sweep in practice (pp. 149-157, DOI 11). Kameugne, Fotso & Scott give a quadratic extended edge-finding algorithm for cumulative resources, exploiting the fact that complete filtering is NP-complete and cumulative is implemented as a conjunction of polynomial relaxations whose fixpoints combine (p. 738, DOI 65). Dejemeppe, Van Cauwelaert & Schaus extend unary-resource propagation (Overload Checking, Detectable Precedences, Not-First/Not-Last, Edge-Finding) to **sequence-dependent transition times**, motivated by quay-crane scheduling (pp. 89-104, DOI 7). Siala, Artigues & Hebrard revisit hybrid CP/SAT disjunctive scheduling with two clause-learning approaches, avoiding redundant clauses created when lazily generating atoms for bound modifications (pp. 393-402, DOI 28).

Kreter, Schutt & Stuckey model **RCPSP/max-cal** — resource-constrained project scheduling with general temporal and calendar constraints, where execution-time intervals must satisfy min/max time lags, capacities, and calendar availability (pp. 262-278, DOI 19). Lombardi, Pigeron & Garchi estimate the expected makespan of a Partial Order Schedule under bounded duration uncertainty as a deterministic function of duration bounds, addressing the observation that state-of-the-art solvers do not fully exploit temporal flexibility (pp. 279-294, DOI 20). Lam, Van Hentenryck & Kilby jointly route and schedule vehicles and crews with an interdependent space-and-time model and a novel optimization constraint that detects infeasibility and bounds crew objectives, with LNS exploring vehicle and crew neighbourhoods (pp. 654-670, DOI 45). Gay, Lecoutre & Schaus guide backtrack search by reordering variables according to conflicts, making generic conflict-driven search competitive with domain-specific scheduling branching heuristics (pp. 140-148, DOI 10).

Applications cover evacuation (Even, Schutt & Van Hentenryck's non-preemptive evacuation scheduling maximizing evacuees and minimizing duration, pp. 574-591, DOI 40), satellite instrument running modes (Pralet, Lemai-Chenevier & Jaubert, mode automaton O/S/H/A with constraint-based local search, pp. 704-719, DOI 48), long-haul fleet mix and routing for a Queensland carrier with CP + adaptive LNS (Kilby & Urli, p. 729, DOI 59), plant outage scheduling plus optimal energy generation in a two-subproblem utility model (Gavranovic & Buljubasic, p. 736, DOI 63), differential harvest with two hoppers and ~10 s emptying latency (Briot, Bessiere & Vismara, pp. 541-556, DOI 38), power capping on the Eurora supercomputer with an extra finite power resource (Borghesi et al., pp. 524-540, DOI 37), segment routing with ECMP stacks (Hartert, Schaus, Vissicchio & Bonaventure, pp. 592-608, DOI 41), node-disjoint bounded paths in LR-PON fibre networks with CP local search on real networks where exact MIP is infeasible (Arbelaez et al., pp. 499-507, DOI 35), and round-robin sailing match-race pairing lists satisfying ISAF criteria, including the finding that some published ISAF schedules are illegal (Macdonald, McCreesh, Miller & Prosser, pp. 671-686, DOI 46).

## Search, hybrids, meta-search, and profiling

Allouche, de Givry, Katsirelos, Schiex & Zytnicki design **Hybrid Best-First Search** for weighted CSP, combining Best-First Search's global lower bound with Depth-First Search's upper bounds in an anytime scheme that reports an optimality gap and yields good solutions quickly, integrated with Backtracking with Tree Decomposition (pp. 12-29, DOI 2). Fioretto, Le, Pontelli, Yeoh & Son implement dynamic-programming-based DCOP algorithms exploiting GPU parallelism in centralized and distributed settings (pp. 121-139, DOI 9). Rendl, Guns, Stuckey & Tack present **MiniSearch**, a solver-independent meta-search language for MiniZinc: search combinators (sequence, branch, cut, parallel, portfolio, LNS, AND-OR search, branch-and-bound) express hybrid algorithms, compiled to a solver's search primitives, with experiments on the MiniZinc Challenge instances (pp. 376-392, DOI 27). Simard, Morin, Quimper, Laviolette & Desharnais bound the Optimal Search Path objective by relaxing it into a stochastic cop-and-drunk-robber game (the Copwin bound), the first CP implementation of the DMEAN bound and its comparison against the longest-path relaxation (pp. 403-418, DOI 29). Vanaret, Gotteland, Durand & Alliot hybridize interval CP with evolutionary algorithms (Charibde) for numerical global optimization with rigorous optimality proofs (pp. 446-462, DOI 32). Kilby & Urli combine CP and adaptive LNS for the long-haul fleet problem; Prestwich, Rossi & Tarim treat randomness as a constraint — entropy proxies from data-compression algorithms, k-gram repetition constraints, and the satisfiability bound `t_k ≥ ceil(n / m^k)` (pp. 351-366, DOI 25). Koriche, Lagrue, Piette & Tabary formalize General Game Playing as a stochastic CSP and show MAC-UCB beats UCT and FC-UCB in 1,350,000 face-offs (pp. 726-727, DOI 57). Shishmarev, Mears, Tack & de la Banda present the CP profiler visualizing search-tree structure and the interaction of heuristics and constraints (p. 728, DOI 58).

## Model generation, distributed CP, and learning

Wetter, Akgun, Frick & Pharfakos automate streamliner generation — uninferred pruning constraints previously hand-built by experts — from an Essence specification with Conjure (pp. 480-498, DOI 34). Monette, Flener & Pearson automate auxiliary-variable elimination as above. Beldiceanu, Carlsson, Flener & Pearson's reification scheme makes global constraints usable as Boolean guards in any solver. In distributed CP, Wahbi, Mechqrane, Osmana & Bessiere generalize termination values so any centralized dynamic variable ordering heuristic can be used asynchronously, in polynomial space (pp. 463-479, DOI 33). Van Beek & Hoffmann learn Bayesian network structure with a constraint-based depth-and-first branch-and-bound, encoding acyclicity and B De Kleer-style optimization to outperform ILP and A* (pp. 429-445, DOI 31). McCreesh & Prosser parallelize backjumping subgraph isomorphism with supplemental graphs (pp. 295-312, DOI 21). Kotthoff, Nanni, Guidotti & O'Sullivan mine mobility profiles by clustering trajectories with symmetry constraints to separate signal from one-off trips (pp. 638-653, DOI 44). Kemmar, Loudni, Le Patre, Bessiere, Tati & Kanouf find the complete set of constrained sequential patterns with the PREFIX-PROJECTION global constraint (pp. 226-243, DOI 17). Dao, Duong & Vrain solve constrained minimum sum of squares clustering exactly, adding user constraints to the WCSS criterion beyond ILP with column generation (pp. 557-573, DOI 39). Kadioglu, Colena, Huberman & Bagley optimize cloud service assignment, generalizing the Hungarian-algorithm assignment problem with side constraints (pp. 627-637, DOI 43). Blindell, Castaneda Lozano, Carlsson & Schulte model **universal instruction selection** as a graph-partitioning problem that handles general control-flow graphs, where the state of the art is restricted to trees/DAGs and efficiency differences reach two orders of magnitude; the volume prints an erratum correcting the saturated-sum C-code example and Eq. 8 to `sel(m) ⇒ loc(d) ∈ stores(m, d)` (pp. 609-626 and p. 722, DOI 42 and 53). Coffrin, Hijazi & Van Hentenryck adapt CP bound consistency to convex relaxations of non-convex AC power-flow models (pp. 39-57, DOI 4). Murphy, Manzano & Brown evaluate a Choco-based home energy recommender: AUTHENTIC Zigbee sensing, ~900 ms savings module, ~17 s scheduler at 30-min slots, 400 s at 5-min slots, with a cumulative constraint for peak power and an inverted frequency mask minimising abnormality (pp. 687-703, DOI 47). Barthe, Derrien, Fages, Petit & Prud'homme select video segments with Allen's temporal algebra constraints in a tractable class of temporal optimization problems (pp. 105-120, DOI 8). Barco, Detaux, Gué, Fages & Lejaut synthesize facade layouts as open packing with panels of unknown count and size, covering frames exactly once with panel corners attached to corners, and report the state of the art for building thermal retrofit (pp. 508-523, DOI 36). Papadopoulos et al.'s sampling work, Weller's MWSS tractability and Beldiceanu et al.'s transducers cover the probabilic-logical edge of the volume.

## Fast-track, journal-track, and erratum abstracts

The volume appends six fast-track abstracts (pp. 722-729) and seven journal-track abstracts (pp. 733-742), each one to three paragraphs: Beldiceanu et al. on finite transducers for structural time-series constraints; Hooker on projection, J-consistency and second-order expressions, arguing that a constraint-projection algorithm induces a consistency stronger than path-consistency and that logic-based Benders is a projection instance; Ivrii et al. on minimal independent support; Koriche et al. on General Game Playing; Shishmarev et al. on visual search-tree profiling; Kilby & Urli on long-haul fleet mix; Beldiceanu et al. on reification; Bergman et al. on MDD propagation for Sequence; Bergman et al. on discrete optimization with decision diagrams; Gavranovic & Buljubasic on large-scale energy management; Jefferson et al. on polynomial representations; Kameugne et al. on quadratic edge-finding; Pesant on dispersion constraints; Stojadinovic & Maric on meSAT; van Hoeve on LNG ship scheduling and inventory management, where two CP models based on a disjunctive scheduling representation with sequence-dependent setup times and cumulative inventory resources are much smaller and 4-10× faster than the MIP models of Goel et al. (EJOR 241(3):662-673, 2015). The erratum (p. 722) corrects the Blindell et al. instruction-selection paper's Fig. 1 and Eq. 8, pointing to the original paper's DOI 10.1007/978-3-642-32362-6.

## Paper index

`idx` is the structure-scan index used throughout this vault; `chapter` is the volume's DOI chapter number, `idx − 8` for the 48 technical-track papers. Pages are volume pages, from each paper's own page-1 Springer footnote and the volume Contents.

### Technical track (48 papers)

| idx | ch | pages | title |
|---|---|---|---|
| 9 | 1 | 3-11 | Encoding Linear Constraints with Implication Chains to CNF |
| 10 | 2 | 12-29 | Anytime Hybrid Best-First Search with Tree Decomposition for Weighted CSP |
| 11 | 3 | 30-38 | Improved Constraint Propagation via Lagrangian Decomposition |
| 12 | 4 | 39-57 | Strengthening Convex Relaxations with Bound Tightening for Power Network Optimization |
| 13 | 5 | 58-73 | Broken Triangles Revisited |
| 14 | 6 | 74-88 | A Microstructure-Based Family of Tractable Classes for CSPs |
| 15 | 7 | 89-104 | The Unary Resource with Transition Times |
| 16 | 8 | 105-120 | A Global Constraint for a Tractable Class of Temporal Optimization Problems |
| 17 | 9 | 121-139 | Exploiting GPUs in Solving (Distributed) Constraint Optimization Problems with Dynamic Programming |
| 18 | 10 | 140-148 | Conflict Ordering Search for Scheduling Problems |
| 19 | 11 | 149-157 | Simple and Scalable Time-Table Filtering for the Cumulative Constraint |
| 20 | 12 | 158-172 | General Bounding Mechanism for Constraint Programs |
| 21 | 13 | 173-182 | Smallest MUS Extraction with Minimal Hitting Set Dualization |
| 22 | 14 | 183-199 | Upper and Lower Bounds on the Time Complexity of Infinite-Domain CSPs |
| 23 | 15 | 200-209 | Generalized Totalizer Encoding for Pseudo-Boolean Constraints |
| 24 | 16 | 210-225 | Smaller Selection Networks for Cardinality Constraints Encoding |
| 25 | 17 | 226-243 | PREFIX-PROJECTION Global Constraint for Sequential Pattern Mining |
| 26 | 18 | 244-261 | On Tree-Preserving Constraints |
| 27 | 19 | 262-278 | Modeling and Solving Project Scheduling with Calendars |
| 28 | 20 | 279-294 | Deterministic Estimation of the Expected Makespan of a POS Under Duration Uncertainty |
| 29 | 21 | 295-312 | A Parallel, Backjumping Subgraph Isomorphism Algorithm Using Supplemental Graphs |
| 30 | 22 | 313-329 | Automated Auxiliary Variable Elimination Through On-the-Fly Propagator Generation |
| 31 | 23 | 330-340 | Automatically Improving SAT Encoding of Constraint Problems Through Common Subexpression Elimination in Savile Row |
| 32 | 24 | 341-350 | Exact Sampling for Regular and Markov Constraints with Belief Propagation |
| 33 | 25 | 351-366 | Randomness as a Constraint |
| 34 | 26 | 367-375 | Quasipolynomial Simulation of DNNF by a Non-determinstic Read-Once Branching Program |
| 35 | 27 | 376-392 | MiniSearch: A Solver-Independent Meta-Search Language for MiniZinc |
| 36 | 28 | 393-402 | Two Clause Learning Approaches for Disjunctive Scheduling |
| 37 | 29 | 403-418 | Bounding an Optimal Search Path with a Game of Cop and Robber on Graphs |
| 38 | 30 | 419-428 | Restricted Path Consistency Revisited |
| 39 | 31 | 429-445 | Machine Learning of Bayesian Networks Using Constraint Programming |
| 40 | 32 | 446-462 | Hybridization of Interval CP and Evolutionary Algorithms for Optimizing Difficult Problems |
| 41 | 33 | 463-479 | A General Framework for Reordering Agents Asynchronously in Distributed CSP |
| 42 | 34 | 480-498 | Automatically Generating Streamlined Constraint Models with Essence and Conjure |
| 43 | 35 | 499-507 | Constraint-Based Local Search for Finding Node-Disjoint Bounded-Paths in Optical Access Networks |
| 44 | 36 | 508-523 | Open Packing for Facade-Layout Synthesis Under a General Purpose Solver |
| 45 | 37 | 524-540 | Power Capping in High Performance Computing Systems |
| 46 | 38 | 541-556 | A Constraint-Based Approach to the Differential Harvest Problem |
| 47 | 39 | 557-573 | Constrained Minimum Sum of Squares Clustering by Constraint Programming |
| 48 | 40 | 574-591 | A Constraint Programming Approach for Non-preemptive Evacuation Scheduling |
| 49 | 41 | 592-608 | Solving Segment Routing Problems with Hybrid Constraint Programming Techniques |
| 50 | 42 | 609-626 | Modeling Universal Instruction Selection |
| 51 | 43 | 627-637 | Optimizing the Cloud Service Experience Using Constraint Programming |
| 52 | 44 | 638-653 | Find Your Way Back: Mobility Profile Mining with Constraints |
| 53 | 45 | 654-670 | Joint Vehicle and Crew Routing and Scheduling |
| 54 | 46 | 671-686 | Constructing Sailing Match Race Schedules: Round-Robin Pairing Lists |
| 55 | 47 | 687-703 | Design and Evaluation of a Constraint-Based Energy Saving and Scheduling Recommender System |
| 56 | 48 | 704-721 | Scheduling Running Modes of Satellite Instruments Using Constraint-Based Local Search |

### Fast-track abstracts to *Constraints* journal (pp. 722-729)

| idx | page | title |
|---|---|---|
| 57 | E1 | Erratum to: Modeling Universal Instruction Selection (Blindell, Castaneda Lozano, Carlsson, Schulte; correcting the original paper's Fig. 1, DOI 10.1007/978-3-642-32362-6) |
| 58 | 723 | Using Finite Transducers for Describing and Synthesising Structural Time-Series Constraints (Beldiceanu, Carlsson, Douceon, Simonis) |
| 59 | 724 | Projection, Consistency, and George Boole: Second-Order Expressions for Propositional Logic (Hooker) |
| 60 | 725 | On Computing Minimal Independent Support and Its Applications to Sampling and Counting (Ivrii, Malik, Meel, Vardi) |
| 61 | 726-727 | General Game Playing with Stochastic Constraint Programming (Koriche, Lagrue, Piette, Tabary) |
| 62 | 728 | Visual Search Tree Profiling for Modelling and Search Strategies (Shishmarev, Mears, Tack, de la Banda) |
| 63 | 729 | Long-Haul Fleet Mix and Routing Optimisation with Constraint Programming and Large Neighbourhood Search (Kilby, Urli) |

### Journal-track abstracts (pp. 733-743)

| idx | page | title |
|---|---|---|
| 64 | 733 | On the Reification of Global Constraints (Abstract) (Beldiceanu, Carlsson, Flener, Pearson) |
| 65 | 734 | MDD Propagation for Sequence Constraints (Bergman, Cire, van Hoeve) |
| 66 | 735 | Discrete Optimization with Decision Diagrams (Bergman, Cire, van Hoeve, Hooker) |
| 67 | 736 | A Hybrid Approach Combining Local Search and Constraint Programming for a Large Scale Energy Management Problem (Gavranovic, Buljubasic) |
| 68 | 737 | Representing and Solving Finite-Domain Constraint Problems using Systems of Polynomials (Jefferson, Jeavons, Green, van Dongen) |
| 69 | 738 | A Quadratic Extended Edge-Finding Filtering Algorithm for Cumulative Resource Constraints (Kameugne, Fotso, Scott) |
| 70 | 740 | Achieving Domain Consistency and Counting Solutions for Dispersion Constraints (Pesant) |
| 71 | 741 | meSAT: Multiple Encodings of CSP to SAT (Stojadinovic, Maric) |
| 72 | 742 | Constraint Programming for LNG Ship Scheduling and Inventory Management (Abstract) (van Hoeve) |
| 73 | 743 | Revisiting the Limits of MAP Inference by MWSS on Perfect Graphs (Weller) |

The fast-track and journal-track footnotes cite the journal version of each paper (e.g. *Constraints*, JAIR, RAIRO, AMAI, IJPS, EJOR, INFORMS J. Computing), not the Springer chapter DOI, so those items carry page numbers only.

## Book features

- **Front matter**: LNCS series page, volume title/copyright page, the editor's preface, the list of four tutorials and six satellite workshops, and the full conference organization roster (idx 1-5).
- **Invited talks**: three abstracts, one joint with ICLP (idx 6-8).
- **Author Index**, pp. 745-755: author-to-page mapping for the whole volume, no research content (source lines 18,415-18,511).
- **Award and competition notices**: the MiniZinc Challenge results, a first Industry Outreach effort led by Helmut Simonis, and a post-conference CSPlib sprint, recorded in the front matter.
- **George Boole 200 / ICLP co-location**: the volume is part of the Boole bicentenary events at University College Cork and co-located with ICLP 2015, with a joint programming competition.

## Concepts extracted

- [[concepts/encoding-preservation-under-composition-and-merging]] — the closed-class results for tree-convex constraints and DNNF simulation
- [[concepts/lagrangian-decomposition-propagation]] — Lagrangian penalties between constraints, and Lagrangian/relaxation bounds for global constraints
- [[concepts/bound-tightening-relaxation-networks]] — convex-relaxation bound tightening via CP bound consistency
- [[concepts/decision-diagrams-optimization]] — BDD/MDD-based propagation, relaxed-BDD bounds, and branch-and-bound with diagram relaxations
- [[concepts/search-combinators-meta-search]] — the MiniSearch combinator language and the search-tree profiler as a search-design vocabulary
- [[concepts/automated-model-generation]] — streamliner generation, auxiliary-variable elimination, common-subexpression elimination, reification: automated model-improvement steps

## Constraints & limitations

- The volume prints abstracts, not full papers, for 16 items (invited talks, fast-track, journal-track): their method and experiment details are not in the source, so this page's summaries of those items are abstract-level.
- 48 technical papers plus 16 abstracts means the results quoted here are headline-level, taken from abstracts and the printed text; tables and figures of the papers are not in the extracted text, so all numbers here come from body text.
- The structure scan's idx numbering is internal to this vault; the volume's own numbering is chapter 1-48 plus the appended sections. Cross-referencing a paper to Springer's DOI uses `10.1007/978-3-319-23219-5_` + chapter.
- Some author spellings in the extracted text carry the OCR's diacritics (for example Prud'homme, Jégou, Castañeda Lozano); the Author Index pp. 745-755 is the authority for full author lists.

## Sources

- `_papers/pesant2015principles/pesant2015principles.md` (Zotero bibliography export) and `_papers/pesant2015principles/pesant2015principles-extracted.md` (18,510 lines, Springer HTML export), the only sources for this page; page ranges and chapter numbers come from each paper's page-1 Springer footnote and the volume Contents.

## Related
- [[concepts/automated-model-generation]] — produced by the CP 2015 volume this page documents
- [[concepts/search-combinators-meta-search]] — produced by the CP 2015 volume this page documents
- [[concepts/bound-tightening-relaxation-networks]] — produced by the CP 2015 volume this page documents
- [[concepts/lagrangian-decomposition-propagation]] — produced by the CP 2015 volume this page documents
- [[concepts/encoding-preservation-under-composition-and-merging]] — produced by the CP 2015 volume this page documents

- [[concepts/decision-diagrams-optimization]] — produced by the CP 2015 volume this page documents
