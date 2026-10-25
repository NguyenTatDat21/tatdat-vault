# TASK — Full Papers Re-Ingest via `wiki-ingest`

## Objective

Run a **full content ingest** for all papers under `./_papers` using the `wiki-ingest` skill.

> Scope: global
> Mode intent: full semantic re-ingest (not metadata-only backfill)

## Ground Rules (from skill)

1. Follow `wiki-ingest` + `llm-wiki` requirements for frontmatter, provenance, relationships, and Sources.
2. Apply **Paper Extraction Frame** for each paper page:
   - problem + novelty
   - method/pipeline (figure or Mermaid)
   - 1–3 core equations in `$$...$$`
   - setup + headline results table
   - ablations + limitations
3. Use `cache-update` for manifest updates (avoid hand-edit races).
4. Use `memory sync INGEST` for `index.md` / `log.md` / `hot.md` updates.
5. Run `qmd update` (and `qmd embed` when needed) after each wave.

## Baseline Snapshot

- `./_papers/*-extracted.md`: **117**
- Sidecar `.md` present: **117 / 117**
- Existing `references/*.md`: **17**
- `OBSIDIAN_MAX_PAGES_PER_INGEST=15`
- `WIKI_STAGED_WRITES=false`
- `QMD_WIKI_COLLECTION=tatdat-vault`
- `QMD_PAPERS_COLLECTION=_papers`

## Execution Model

Use **5-paper waves** (safe with `max_pages_per_ingest=15`).

- Total waves: **24**
- Waves 1–23: 5 papers each
- Wave 24: 2 papers

### Per-Wave Checklist

- [ ] Select wave files (`*-extracted.md` + sidecars)
- [ ] Read and run wiki-ingest skill
- [ ] Read and run cross-linker skill

## Wave Tracker

- [x] **W01** `_papers/ahmadi-javid2022delivery/...` → `_papers/archetti2018set/...`
  - ✅ Completed 2026-10-22T19:26Z — pages_created=6, pages_updated=3; cache-check unchanged (10/10); qmd update+embed+verify complete.
  - ⚠️ Note: `_papers/almgren2004optimal/almgren2004optimal-extracted.md` contains NUL bytes; extraction was read via a temporary cleaned copy for drafting, while manifest/cache used the original source file.
- [x] **W02** `_papers/archetti2023new/...` → `_papers/bar-noy2004efficient/...`
  - ✅ Completed 2026-10-22T19:36Z — pages_created=8, pages_updated=1; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W03** `_papers/barnhart1998branchandprice/...` → `_papers/black1992global/...`
  - ✅ Completed 2026-10-22T19:58Z — pages_created=7, pages_updated=0; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W04** `_papers/boland2017continuoustime/...` → `_papers/chen2010shrinkage/...`
  - ✅ Completed 2026-10-22T20:41Z — pages_created=9, pages_updated=0; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W05** `_papers/cheng2020drone/...` → `_papers/christiansen2020liner/...`
  - ✅ Completed 2026-10-22T23:22Z — pages_created=6, pages_updated=2; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W06** `_papers/clautiaux2018combining/...` → `_papers/dorling2017vehicle/...`
  - ✅ Completed 2026-10-22T23:54Z — pages_created=7, pages_updated=2; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W07** `_papers/dossantos2024multiobjective/...` → `_papers/furini2016modeling/...`
  - ✅ Completed 2026-10-24T01:31Z — pages_created=12, pages_updated=7; cache-check unchanged (10/10); qmd update+embed+verify complete.
  - ⚠️ Note: `fama1973risk` extracted markdown has no image links, so its page is text-only; equation/table image files exist on disk but their page-to-content mapping is unverified, and no image was embedded.
  - ⚠️ Deferred to a follow-up wave: adding back-links from `references/poikonen2020-k-mvdrp`, `references/lu2024-hybrid-evolutionary-algorithm-sop`, and `references/murray2020-multiple-flying-sidekicks-tsp` into the new UAV routing concept pages.
- [x] **W08** `_papers/ganjia2026multiobjective/...` → `_papers/goel2015constraint/...`
  - ✅ Completed 2026-10-24T04:05Z — pages_created=10, pages_updated=5; cache-check unchanged (10/10); qmd update (10 new/6 updated) + embed (176 chunks/16 docs) + `qmd get` verify complete; 88 wikilinks resolve, frontmatter/YAML fields present, summaries ≤200 chars, all YAML sources exist on disk, all 10 new pages in `index.md`.
  - New: `references/goel2012-large-neighborhood-search-lng-inventory-routing`, `references/goel2015-constraint-programming-lng-ship-scheduling`, `references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling`, `references/garg2022-iq-learn-inverse-soft-q`; `concepts/time-space-network-ship-flow-model`, `concepts/large-neighborhood-ship-pair-destroy-repair`, `concepts/cumulative-volume-lower-bound-cp-search`, `concepts/disjunctive-scheduling-constraint-programming-model`, `concepts/inverse-soft-q-imitation-learning`, `concepts/multi-objective-metaheuristic-tuning-validation`.
  - Updated: `references/gendreau2019-handbook-metaheuristics`, `concepts/large-neighborhood-search`, `concepts/variable-neighborhood-search`, `concepts/mirp-modeling-continuous-vs-discrete-time` (base_confidence 0.67→0.87), `concepts/maritime-inventory-routing-problem` (duplicate typeless relationship entry removed).
  - ⚠️ Caveat (corrected after source verification): the W08 headline claims I logged for ganjia — fuzzy weighted max-min, cost gap ≤0.62% vs 3.25%, 47% hypervolume edge, −7% cost / −16% CO₂ — are **not in the ganjia source** (grep: 0 hits for hypervolume, no fuzzy model, no CO₂ percentages). Ganjia builds the Pareto front with the **ε-constraint** method (gaps below 0.8%), tunes NSGA-II (pop 50, CR 0.5, MR 0.4) and MOPSO (pop 50, w 0.6, C₁ 0.5, C₂ 1.25, α 0.3) by a **Taguchi L27** smaller-the-better S/N design, and reports average gaps vs the ε-constraint front of **0.002% cost / 0.008% tardiness (NSGA-II)** and **0.020% / 0.055% (MOPSO)**; in 50 iterations cost goes 126.2 → 69.3 MLCU (45%) and tardiness 23,950 → 858 h (96%). Orientation endpoints reproduce single-objective extremes (economic 74.52 MLCU / 9.43 h, customer 2.17 h / 245.11 MLCU, compromise 112.98 / 5.29 h). Ganjia lists fuzzy approaches as future work, so the fuzzy max-min page's ganjia links are marked `^[inferred]`.
  - ⚠️ Fabricated handbook captions: `references/gendreau2019-handbook-metaheuristics.md` embedded handbook Figs. 4.1/4.2 under one caption claiming "15 customers removed (43 vehicles)" and "the accept() step" — those strings do not exist in the handbook. Fixed by splitting the caption and quoting the verbatim captions (Fig. 4.1 TSP/CVRP solution with depot as a square and demand-labeled nodes; Fig. 4.2 destroy/repair with **six** customers removed); the same wording was corrected in [[concepts/large-neighborhood-search]] and [[concepts/large-neighborhood-ship-pair-destroy-repair]], where `accept()` is now labelled as the chapter's own terminology, not caption text.
  - ⚠️ Handbook figure-to-caption mapping rule established: the extractor's image page index is **PDF page − 1** (`page_115` = PDF 116), verified with `pdftotext` page windows and `pdfimages -list`. pymupdf is **not** installed (pypdf 5.4.0 is), so caption checks use `pdftotext -layout -f N -l N`.
  - ⚠️ Frontmatter timestamps the W08 agent wrote by hand (`12:10Z`, `13:00Z`, `05:05Z`) drifted from the recorded sync times; pages were normalized to `created = updated = 2026-10-24T03:00:25Z` for the 10 new pages and `updated = 2026-10-24T03:00:25Z` with `created` preserved for the 5 updated pages, `lifecycle_changed: 2026-10-24`. `concepts/mirp-modeling-continuous-vs-discrete-time.md` base_confidence 0.87 → **0.83** (two independent papers), gendreau page **0.57** (book-only lineage), tabu-search/hyper-heuristics/parallel-metaheuristics **0.57**.
  - ⚠️ A bulk frontmatter patch written in a codemode script destroyed 15 W08 pages (bodies lost, files ending at the `updated:` line) because it split the text on the `---` delimiter and reassembled it wrong; the pages were restored from the vault's git backup commit `2fa7399` ("vault backup: 2026-10-24 04:32:30"). A stray `.manifest.json.tmp` was left behind because `os` was never imported, so `os.replace` never ran. Fix pattern: patch only the block matched by `^---\n(.*?)\n---\n` (re.S), rebuild `--- fm --- body`, then verify all 12 fields with `yaml.safe_load`; the manifest rewrite must be a single atomic write, never `json.dump(..., open('.manifest.json.tmp','w'))` + `os.replace` in a script whose imports are incomplete.
  - ✅ Two follow-up dispatch agents closed the W07/W08 caveats. Agent 1 (handbook distillation) produced **nothing**: it read the 12,014-line extracted markdown in 150-line windows (42 tool uses, 1.4M tokens, context 141%), was cut off mid-thought, and wrote no pages, no log lines, no cache entries; git status stayed clean. Lesson: for a 1.8 MB extracted file, jump to the chapter line numbers found by grep, read ~250-line windows, and write after each chapter.
  - ✅ Agent 2 closed the deferred concept updates: 10 pages changed (multi-objective, fuzzy max-min, annual LNG, green VRP, drone energy, payload, MIRP modeling, poikonen, lu2024, murray), 16 `cache-update` calls, one memory sync, `qmd update` + `embed` (203 chunks / 26 documents), `qmd get` verified `concepts/annual-lng-delivery-program.md`, its validation script reports 10 pages / 0 issues. It refused two decorative links (no multi-agent content in lu2024, no ML content in murray), kept `created` untouched, and used the real ganjia image names `page_20_chart_6.jpg` / `page_24_chart_5.jpg` (the names in my brief, `page_3_chart_1` / `page_4_chart_1`, do not exist).
  - ⚠️ Deferred (15-page cap): `concepts/annual-lng-delivery-program`, `concepts/tabu-search`, `concepts/hyper-heuristics`, `concepts/parallel-metaheuristics-cooperative-search`, `concepts/adaptive-large-neighborhood-search-for-mip`, `concepts/green-vehicle-routing-problem-taxonomy`, `concepts/nonlinear-drone-energy-function-in-routing`, `concepts/payload-induced-drone-battery-consumption-rate`, `concepts/multi-objective-maritime-cargo-routing-scheduling`.
  - ⚠️ Note: subagent frontmatter timestamps (e.g. `created: 2026-10-24T12:10:00Z`) run ahead of the `memory sync` log times (03:00Z); index/hot/log are generated by the CLI, so the drift is cosmetic.
- [x] **W09** `_papers/gronhaug2009supply/...` → `_papers/ha2020new/...`
  - 🚀 Dispatched 2026-10-25T19:48Z — background agent `88eb1f4e-cbbf-4c6` (general-purpose); prompt carries: manifest key check, 250–300-line read windows, verbatim captions (extractor page index = PDF page − 1), exact UTC `2026-10-25T19:48:00Z` for `updated`/`lifecycle_changed` (no hand-written `created`), cache-update + one memory sync INGEST per source, QMD update+embed+verify, all 12 gates. 5 keys: gronhaug2009supply, gronhaug2010branchandprice, guo2018generative, ha2020new, hadjsalem2023mathematical. W9 scope verified: TASK.md ranges for W09–W24 match the manifest's alphabetical 52-paper remainder exactly.
  - ✅ Completed 2026-10-25T21:35Z — pages_created=7, pages_updated=8 (15 pages = cap); cache-check 5/5 unchanged; INGEST ×5 logged (21:03:30–21:04:22Z); qmd update (7 new/10 updated) + embed (170 chunks/17 docs) + `qmd get` verify complete; index.md contains all 7 new pages; 12-field YAML check passes on all 15 pages; cross-link sweep found 0 additions (all candidate pairs already linked + typed; 0 unlinked author-year mentions; 0 orphans); provenance fix: `concepts/vehicle-routing-with-synchronization-constraints` extracted 0.85→0.86 (sum 1.00). Sidecars contradicted the guessed titles in the dispatch prompt — real papers: LNG supply-chain MIP chapter, LNG-IRP branch-and-price, GASIL (RL), VRP-SC lp-ALNS (co-authored by Tat Dat Nguyen), 2D variable-sized cutting-stock textile; agent ingested sidecar-true content.
- [ ] **W10** `_papers/hadjsalem2023mathematical/...` → `_papers/he2002intuition/...`
  - 🚀 Dispatched 2026-10-25T21:41Z — background agent (general-purpose); same prompt template as W09, with the sidecar-authority rule made explicit: read the sidecar first, never assume a title from the folder key. 4 keys: halvorsen-weare2013routing, hartman2023leximin, haug2023planning, he2002intuition (hadjsalem2023mathematical, the wave's nominal start, was ingested in W09). Wave keys verified against the manifest: 70/117 paper entries ingested, 47 un-ingested, W10's 4 keys all in that set.
- [ ] **W11** `_papers/hendel2022adaptive/...` → `_papers/jimenez-piqueras2023constraint/...`
- [ ] **W12** `_papers/kakinuma2020empirical/...` → `_papers/ledoit2004wellconditioned/...`
- [ ] **W13** `_papers/li2024drone/...` → `_papers/mbiadousaleu2022parallel/...`
- [ ] **W14** `_papers/meng2023multivisit/...` → `_papers/montemanni2024combining/...`
- [ ] **W15** `_papers/montemanni2024parallel/...` → `_papers/mutlu2016comprehensive/...`
- [ ] **W16** `_papers/nguyen2022mincost/...` → `_papers/novy-marx2013other/...`
- [ ] **W17** `_papers/ogryczak2014fair/...` → `_papers/pesant2015principles/...`
- [ ] **W18** `_papers/pham2023efficient/...` → `_papers/poikonen2020multivisit/...`
- [ ] **W19** `_papers/qian2001conditional/...` → `_papers/ropke2006adaptive/...`
- [ ] **W20** `_papers/sacramento2019adaptive/...` → `_papers/skalnes2024new/...`
- [ ] **W21** `_papers/sloan1996stock/...` → `_papers/torabbeigi2020drone/...`
- [ ] **W22** `_papers/vilim2015failuredirected/...` → `_papers/windrasmara2022adaptive/...`
- [ ] **W23** `_papers/xinyingchen2023guide/...` → `_papers/yusuf2023strategic/...`
- [ ] **W24** `_papers/zhang2021energy/...` + `_papers/zhao2025large/...`

## Definition of Done

- [ ] All 117 extracted papers fully ingested (content-level)
- [ ] Sidecar metadata integrated for all 117
- [ ] References expanded/updated with valid provenance and sources
- [ ] Manifest/cache stable (`cache-check` unchanged on processed sources)
- [ ] QMD refreshed and verified

## Next Action

W09 dispatched 2026-10-25T19:48Z to background agent `88eb1f4e-cbbf-4c6` (general-purpose). On completion: verify the dispatch result against gates (a)–(g) in item 12, run the cross-linker pass over the new pages, log the wave delta, mark W09 complete, then dispatch W10 (`_papers/hadjsalem2023mathematical/...` → `_papers/he2002intuition/...`) with the same prompt template — supply fresh UTC and verify the wave's keys against the manifest's un-ingested set first.

### Caveats carried forward (read before dispatching the next wave)

**Known debt from W07/W08**

1. **UAV back-links — CLOSED.** Agent `4275f84e-e36a-4ed` added the links: `references/poikonen2020-k-mvdrp.md` links [[concepts/cooperative-multi-agent-uav-routing]] + [[concepts/transformer-seq2seq-routing-solver]] (real multi-agent content), `references/lu2024-hybrid-evolutionary-algorithm-sop.md` links the transformer page (its decoder is the same masked-softmax seq2seq family), `references/murray2020-multiple-flying-sidekicks-tsp.md` links the cooperative page (single salesman + N sidekicks = one shared network). Its own report flags two of these links as decorative `^[inferred]` and one as adding no new claims, so the back-link debt is discharged at that confidence.
2. **Concept pages deferred by W08 — CLOSED (10 pages, validation script reports 10 pages / 0 issues).** `concepts/annual-lng-delivery-program` (Goel CP interval/cumul/disjunctive constraints, W06 caveat), `concepts/tabu-search` (Gendreau & Potvin), `concepts/hyper-heuristics` (Ganjia Taguchi/NSGA-II/MOPSO tuning), `concepts/parallel-metaheuristics-cooperative-search` (Ganjia multi-start, Goel LNS restarts), `concepts/adaptive-large-neighborhood-search-for-mip` (Goel ship-pair destroy, four-day repair window, P13 optimal), `concepts/green-vehicle-routing-problem-taxonomy` (Ganjia fuel/emission term), `concepts/nonlinear-drone-energy-function-in-routing` + `concepts/payload-induced-drone-battery-consumption-rate` (Poikonen per-km rate, payload linear in battery, Fuertes transformer routing), `concepts/multi-objective-maritime-cargo-routing-scheduling` (Ganjia bi-objective MINLP coupling scheduling + due-date assignment + batch delivery + heterogeneous VRPTW, emission term linear in weight and load, quadratic in speed). New pages should be created only by the waves that add sources (W09-W24).
3. **Gendreau & Potvin handbook** — the extracted markdown is 1.8 MB / 12,014 lines and has **no text layer**, so captions cannot be mapped to pages. `pdftotext -layout` on the Zotero PDF returns only form feeds. The mapping rule for a PDF **with** a text layer: extractor image **page index = PDF page − 1** (`page_115` = PDF page 116), proven for the handbook via `pdftotext -layout -f N -l N` page windows and `pdfimages -list`. pymupdf is NOT installed; pypdf 5.4.0 is. Chapters distilled so far: Ch. 4 LNS, Ch. 10 ACO, Ch. 11 Swarm Intelligence, Ch. 12 Hybrids → `references/gendreau2019-handbook-metaheuristics.md`, `concepts/swarm-intelligence-pso-aco.md`, `concepts/metaheuristic-hybridization.md`, `concepts/simulated-annealing-metropolis-cooling.md` (Ch. 1 SA acceptance, χ(c) ≈ 0.5 near the target control parameter, knapsack/TSP/aircraft trajectory). **Not distilled: Ch. 2 Tabu Search, Ch. 3 VNS, Ch. 13 parallel, Ch. 14 hyper-heuristics, genetic algorithms, GRASP, ILS, neural networks, reactive search, Ch. 16-18.** Chapter start lines: Ch1=199, Ch2=1198, Ch3=1566, Ch4=2643, Ch7=5076, Ch10=6825, Ch11=7643, Ch12=8242, Ch16=10479, Ch17=11029, Ch18=11648. Read in 250-300-line windows; 150-line windows overflow the context and produce nothing (first dispatch agent: 42 tool uses, 1.4M tokens, 141% context, zero writes).
4. **`references/fama1973-risk-return-equilibrium-empirical-tests.md` is text-only** — the extracted markdown contains **no** inline image links, the Zotero PDF behind `extracted-pdf` is a scan **with no text layer** (`pdftotext` returns only form feeds, 31 pages), so the 41 page-numbered crops in `_papers/fama1973risk/images/` cannot be mapped to captions. Page numbers in the file names are inferred from crop geometry, not verified against the paper, so no image may be embedded with a caption; the same applies to [[concepts/fama-macbeth-two-stage-cross-sectional-regression]]. A second copy of the paper exists at `/home/tatdatnguyen/Downloads/Fama-Macbeth.pdf` if verification is ever attempted (pymupdf is not installed; pypdf 5.4.0 is).
5. **Fama-MacBeth numbers come from the extracted text, not the rendered PDF.** The Table 2 column set (`s(R_p)`, `s(ε̂_p)`, `s̄_{p,t-1}(ê_i)`, `β̂_p`, `r²`) is read from prose, and Tables 3/4/5 (the gamma statistics behind every reported t-statistic) are tables in the paper that the extracted markdown renders as prose runs. Every figure in the fama pages is therefore unverified against the PDF. Treat them as single-source claims with one lineage; `base_confidence` reflects that. ^[inferred]
6. **Timestamps.** Wave agents write frontmatter timestamps by hand and drift (W08 pages said `12:10:00Z` / `13:00:00Z` while the recorded syncs are `03:00:24-25Z`); W08 pages were normalized to `created = updated = 2026-10-24T03:00:25Z`, `lifecycle_changed = 2026-10-24`. `created` is not the first writing time — it is the re-ingest time for pages created in a content re-ingest wave; `updated` is the last content change, so `updated ≥ created` and `updated` changes only when the page's prose, links, sources, provenance, confidence, tier, summary, lifecycle state, or bibliographic record changes. Future dispatch prompts must supply the real current UTC for `lifecycle_changed` and `updated`.
7. **Frontmatter patching.** Editing frontmatter by splitting on `---` destroyed 15 pages (bodies lost) before a vault backup restore. Patch the frontmatter block between the two `---` delimiters (regex `^---\n(.*?)\n---\n`, `re.S`) and rebuild `--- fm --- body`; verify all 12 required fields with `yaml.safe_load` after the patch, and check `hot.md`/`index.md` were not rewritten by hand.
8. **QMD** — `qmd update` reports 0 new documents when the collection already contains every page; freshness is proven by `qmd ls tatdat-vault | grep <new page>` plus a `qmd get` read of one page, not by the update output. QMD collection `tatdat-vault` is the only collection; `_papers` is the sources dir, not a collection.
9. **Reading large extracted markdown** — `tools.read` in codemode returns truncated content, which produced false reports of missing pages in `index.md`; verify vault-level checks with bash `grep`. Use `read` with `offset`/`limit` windows for extracted markdown larger than ~200 KB.
10. **Concurrent writes** — the vault is written by parallel agents, so use `obsidian-wiki cache-update` (advisory lock, atomic write, portable key) instead of hand-editing `.manifest.json`, and one `obsidian-wiki memory sync` per source instead of hand-editing `index.md`/`log.md`/`hot.md`.
11. **Subagent steering** — background agents keep stale anchors when files are rewritten behind them. Send a steer message telling them the files were restored/normalized, to re-read before editing, to keep `created` unchanged and `lifecycle: draft`, and to split the combined "Fig. 4.1 ... ; Fig. 4.2 ..." caption in `references/gendreau2019-handbook-metaheuristics.md` so each figure has its own caption.
12. **Verification gates for every wave** — (a) all wikilink targets resolve (build the target set from every `[[...]]` in the touched pages, strip display text and `#`, check against vault paths); (b) `yaml.safe_load` every touched page and require the 12 fields, `summary` ≤ 200 chars, every `sources:` path existing, provenance summing to ~1.0; (c) `cache-check` returns 0 new / 0 modified / N unchanged; (d) `qmd ls` + `qmd get` on a new page; (e) `index.md` contains each new page as `[[slug]]` (grep, not a truncated read); (f) `hot.md` has takeaways for the wave; (g) `log.md` has one INGEST line per source.
13. **base_confidence formula** (`llm-wiki/SKILL.md` 387-445) — `min(lineages/3, 1.0) × 0.5 + avg per-lineage quality × 0.5`, quality buckets paper 1.0, official 0.9, documentation 0.85, book 0.8, repository 0.75, blog 0.55, session transcript 0.5, forum/unknown 0.4, LLM-generated 0.3. A paper PDF + extracted md + sidecar + images count as **one** lineage, so a single-paper page is 0.67, two papers 0.83, book-only 0.57. Recompute only when sources change materially; the W08 pages are normalized to the formula, and `_meta/trust-ledger.json` validation needs human approval.
14. **Fabricated figure captions — fixed, and the pattern to watch.** `references/gendreau2019-handbook-metaheuristics.md` embedded handbook Figs. 4.1/4.2 under **one** caption claiming "a 100-customer CVRP solution with 15 customers removed (43 vehicles)" and "the LNS destroy-and-repair process with the accept() step"; "43 vehicles" and "accept()" do not exist in the handbook source. The real captions, quoted verbatim from the PDF text layer: Fig. 4.1 = a TSP solution and a CVRP solution with the depot as a square and customers labelled with demand `q_i`; Fig. 4.2 = destroy/repair with **six** customers removed, the bottom panel being the reinsertion result. The caption was split and rewritten in the handbook page plus `concepts/large-neighborhood-search.md` line 53 and `concepts/large-neighborhood-ship-pair-destroy-repair.md` line 54, where `accept()` is now labelled as chapter terminology, not caption text. Rule: **never write a caption from memory** — quote it verbatim from the source, one caption per embedded figure, and state the page-mapping rule (extractor page index = PDF page − 1) in the caption.
15. **Subagent outcomes to plan around.** The first handbook agent (150-line read windows, 80+ calls, 1.4M tokens, 141% context) finished `Done` mid-thought and wrote **nothing** — no pages, no log lines, no cache entries. Dispatch prompts must give chapter line numbers, 250-300-line windows, and "write immediately after each chapter". Background agents keep stale anchors when files are rewritten behind them, and W08 hand-written timestamps (`12:10Z`, `13:00Z`) drifted from the recorded sync (03:00:25Z); supply the real UTC in the prompt. Use `general-purpose` with `run_in_background: true` and one dispatch per source group.
