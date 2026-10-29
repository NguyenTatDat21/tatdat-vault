---
title: Search Combinators and Meta-Search Languages
summary: "Search is written, not chosen: combinator languages post constraints during search, profiles show what a strategy did, and conflict-driven orderings beat scheduling heuristics."
tags: [search-combinators, meta-search, minizinc, search-profiling, conflict-driven-search, lns]
provenance:
  extracted: 0.72
  inferred: 0.18
  ambiguous: 0.10
base_confidence: 0.67
tier: supporting
created: 2026-10-29T15:49:00Z
updated: 2026-10-29T15:49:00Z
sources:
  - _papers/pesant2015principles/pesant2015principles.md
  - _papers/pesant2015principles/pesant2015principles-extracted.md
relationships:
  - { target: "references/pesant2015-cp2015-proceedings", type: "export" }
  - { target: "concepts/large-neighborhood-search", type: "evolution" }
  - { target: "concepts/variable-neighborhood-search", type: "support" }
  - { target: "concepts/parallel-metaheuristics-cooperative-search", type: "co-evolution" }
  - { target: "concepts/disjunctive-scheduling-constraint-programming-model", type: "support" }
lifecycle: active
lifecycle_changed: 2026-10-29T15:49:00Z
---

# Search Combinators and Meta-Search Languages

> [!tldr] CP's power comes from writing hybrid search for the application. MiniSearch is a combinator language for that: built-ins return success/failure, `post()` adds constraints, `/\` runs them in order, and `minisearch.mzn` collects the standard strategies. A profiler makes the search visible, and conflict-driven orderings make generic search competitive with scheduling heuristics.

## Summary

Much of the power of CP comes from creating complex hybrid search algorithms specific to an application, and there is no widely accepted standard for specifying search (idx 35, chapter 27, pp. 376-393). Meta-search such as Branch-and-Bound and Large Neighbourhood Search happens on top of CP tree search, often by encoding the meta-search itself (idx 35, chapter 27, pp. 376-393). MiniSearch is a high-level meta-search language based on MiniZinc 2.0, with the `minisearch.mzn` library of search strategies, and the starting point is search combinators (idx 35, chapter 27, pp. 376-393).

## Key ideas

- **MiniSearch control** — all MiniSearch built-ins have an implicit return value of success (true) or failure (false), and all built-ins execute their arguments in order, so `/\` sequences the search (idx 35, chapter 27, pp. 376-393).
- **Adding constraints during search** — a constraint is added by calling `post()` with the constraint as argument, formulated with the same MiniZinc constructs as the model (idx 35, chapter 27, pp. 376-393).
- **Solution management** — a meta-search language's strength is using intermediate solutions to guide the remaining search; branch-and-bound needs the objective to post further constraints (idx 35, chapter 27, pp. 376-393).
- **Lexicographic BaB code** — `repeat( scope( post(lex_less(objs, [sol(objs[i]) | i in index_set(objs)])) /\ if next() then commit() /\ print() else break endif ) )` is the lexicographic branch-and-bound written in the language (idx 35, chapter 27, pp. 376-393).
- **Profiling the search tree** — Visual Search Tree Profiling presents the search tree of a model and strategy as a picture to reason about, with the tool public as `github.com/cp-profiler` (idx 62, fast-track abstract, p. 728).
- **Conflict ordering** — conflict-driven variable ordering by remembering the last variables on which decisions failed outperforms domain-specific scheduling heuristics, and is parameter-free, restart-friendly, and has an identical ranking of methods across the benchmark (idx 18, chapter 10, pp. 140-148).
- **Anytime hybrid search** — Hybrid Best-First Search is the best performing decomposition-unaware algorithm, outperforms DFS and DFS with Luby restarts significantly, and slightly outperforms LDS (idx 10, chapter 2, pp. 12-29).
- **Randomness as a constraint** — an entropy-style constraint for random-looking solutions: `entropy(v, e)` is impossible because algorithmic entropy is uncomputable, so patterns are eliminated by constraints derived from data-compression algorithms; the lex-least solution of 100 variables in {0..9} has gzip entropy 43 bytes against 80-83 bytes for a random digit sequence (idx 33, chapter 25, pp. 351-366).
- **Search-space bound** — a game of cop and robber on the graph bounds the optimal search path, giving an upper bound on the path a search can take (idx 37, chapter 29, pp. 403-418).
- **Hybridizing two solvers** — interval CP is combined with evolutionary algorithms so the two populations exchange information (idx 40, chapter 32, pp. 446-462).
- **Neighbourhood search in production** — CP with LNS is reported as the winning combination for segment-routing traffic engineering, for long-haul fleet mix and routing, and for satellite running modes (idx 49, chapter 41, pp. 592-608; idx 63, fast-track abstract, p. 729; idx 56, chapter 48, pp. 704-721).
- **Stochastic search** — MAC-UCB for stochastic constraint programming outperforms UCT and FC-UCB over 1,350,000 face-offs in general game playing (idx 61, fast-track abstract, pp. 726-727).

## Related

- [[references/pesant2015-cp2015-proceedings]] — the volume these papers are drawn from
- [[concepts/large-neighborhood-search]] — LNS as a combinator over CP search
- [[concepts/variable-neighborhood-search]] — the neighbourhood choice LNS needs
- [[concepts/parallel-metaheuristics-cooperative-search]] — search coordination at scale
- [[concepts/disjunctive-scheduling-constraint-programming-model]] — the scheduling model these strategies run on

## Sources

- `_papers/pesant2015principles/pesant2015principles-extracted.md` (18,510 lines), chapters 2, 10, 25, 27, 29, 32, 41, 48 and the idx 61, 62, 63 abstracts.
