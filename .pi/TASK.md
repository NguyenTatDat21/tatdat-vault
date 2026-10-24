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
- [ ] Read sources and distill content (Paper Extraction Frame)
- [ ] Update/create `references/` and required `concepts/` pages
- [ ] Ensure required frontmatter + provenance markers + `## Sources`
- [ ] `obsidian-wiki cache-update` for extracted/sidecar/(used images)
- [ ] `obsidian-wiki memory sync INGEST ...`
- [ ] `qmd update`
- [ ] `qmd embed` if vectors are pending
- [ ] `qmd get` verification on at least one updated page
- [ ] Wave `cache-check` shows unchanged for processed sources

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
  - ⚠️ Caveat: `gendreau2019handbook-extracted.md` is 1.8 MB and was read in chapter windows (LNS, VNS, TS), so non-routing chapters of the handbook are not distilled.
  - ⚠️ Deferred (15-page cap): `concepts/annual-lng-delivery-program`, `concepts/tabu-search`, `concepts/hyper-heuristics`, `concepts/parallel-metaheuristics-cooperative-search`, `concepts/adaptive-large-neighborhood-search-for-mip`, `concepts/green-vehicle-routing-problem-taxonomy`, `concepts/nonlinear-drone-energy-function-in-routing`, `concepts/payload-induced-drone-battery-consumption-rate`, `concepts/multi-objective-maritime-cargo-routing-scheduling`.
  - ⚠️ Note: subagent frontmatter timestamps (e.g. `created: 2026-10-24T12:10:00Z`) run ahead of the `memory sync` log times (03:00Z); index/hot/log are generated by the CLI, so the drift is cosmetic.
- [ ] **W09** `_papers/gronhaug2009supply/...` → `_papers/ha2020new/...`
- [ ] **W10** `_papers/hadjsalem2023mathematical/...` → `_papers/he2002intuition/...`
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
Start **W09** (`_papers/gronhaug2009supply/...` → `_papers/ha2020new/...`) and log deltas (created/updated pages, QMD status, blockers) in this file.

### Caveats carried forward (read before dispatching the next wave)

**Known debt from W07/W08**
1. **UAV back-links** — `references/poikonen2020-k-mvdrp.md`, `references/lu2024-hybrid-evolutionary-algorithm-sop.md` and `references/murray2020-multiple-flying-sidekicks-tsp.md` do not yet link to [[concepts/cooperative-multi-agent-uav-routing]] or [[concepts/transformer-seq2seq-routing-solver]]; a dispatch agent is working on it.
2. **Concept pages deferred by W08** — multi-objective optimization methods (NSGA-II vs MOPSO, fuzzy weighted max-min, Taguchi tuning of metaheuristics, hypervolume), constraint-programming modelling primitives (interval variables, `cumul`, disjunctive scheduling), in-search lower bounds as a CP search device, imitation learning / behaviour cloning as a data-quality signal, time-space network flow for ship routing. The W08 dispatch agent is updating the pages that already exist; new pages should be created only by the waves that add sources (W09-W24).
3. **Gendreau & Potvin handbook** — the extracted markdown is 1.8 MB and was read in 150-line windows, so non-routing chapters (genetic algorithms, GRASP, simulated annealing, neural networks, tabu search hybrids) are not distilled; `references/gendreau2019-handbook-metaheuristics.md` currently carries LNS/VNS material from the survey's own LNS/VNS census. A dispatch agent is distilling the remaining chapters into the page plus [[concepts/tabu-search]], [[concepts/hyper-heuristics]], [[concepts/parallel-metaheuristics-cooperative-search]], [[concepts/adaptive-large-neighborhood-search-for-mip]], [[concepts/variable-neighborhood-search]] and [[concepts/large-neighborhood-search]].
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
