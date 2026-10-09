# MQS-SOLVER: the paper's and CTTS's solver settings, as options with one matched control (job F of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for one worker on
**account 4**; revised 9 Oct 2026 (clock read 01:26 UTC) by the check-and-fix pass. Lane brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background: matrix rows M12, M13, M14,
M17 of `research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model:** Opus 5.5. **Cap:** USD 7.5. **Box:** 160 min. CPU-bound runs: serialise them; no background computation
  beside foreground runs (Usage 6, GOLD-K3).
- **Goal:** every cheap, tested setting from the paper's App. A (pp.195-197) and the CTTS solver (CTTS paper p.2, README
  "Built-in Cryptanalysis", whose annealing follows Kopal 2019) as an option on the shared homophonic solver, each
  measured on one matched control. Sources: swap and reassign moves (App. A p.196, Figs A18-A19); the score
  S = sum N_g log F_g / sum N_c^2 (p.195-196); at most N homophones per letter (talk [00:15:58]-[00:16:18]; Fig. 8, 1-2
  per letter); a minimum count before a symbol enters the search and a total homophone budget (CTTS README: 76 symbols
  against 68 allowed homophones, threshold raised to 10, "93% of the transcribed symbols will be processed"); ignoring a
  letter such as h and doubled letters (CTTS paper p.2); marked symbols excluded from the homophones but kept in the
  stream as gaps (p.115-118, Fig. 7). Our own earlier digest of Lasry's methods, `LESSONS-LASRY.md` (27 Sept 2026),
  section 3, already names items 1 (escalating n-gram order), 3 (swap-only moves for syllabic designs) and 5
  (lock-and-rerun); read it first and cite it.

## What exists (checked 9 Oct; port from these, do not rebuild)

- `tools/homophonic_anneal.py` itself: the move set is reassign only (one sign gets a new random letter), plus an
  optional soft-pair flip; no per-letter cap, minimum count, budget, ignored letters or doubled-letter collapse. `--skip`
  **deletes** signs, which joins their neighbours into false n-grams; an internal `allowed=` has no CLI.
- **The swap move and the cap already exist in other shared solvers:** `tools/subst_hillclimb.py` (23 Sept 2026,
  bowes-walsingham-1583) has reassign 0.7 / swap 0.3 moves, `--max-homo` (default 2) enforced in every move and in the
  greedy polish, and `score_frags`, under which no n-gram crosses a fragment boundary; `tools/seg_homophonic.py` has an
  80/20 reassign/swap move and passage-separated scoring; `tools/families/columnar_homophonic.py` (R15-KAL14, 6 Oct) a
  50/50 swap/reassign move; `nomenclator_anneal.py` has `--max-homo`. `tools/partial_key_test.py` already scores
  "unmapped codes are gaps; a pair or triple counts only when every position is mapped".
- **Marked signs already have in-stream options:** `families/homophonic.py` `wild=` (H25, 28 Sept 2026: every occurrence
  of a wild sign annealed as its own per-position letter) and `homophonic_anneal.solve_nomen` with `word_signs`
  (R10-SIENA7N / R13-SIENAWC, 6 Oct 2026: signs that may take a vocabulary word).
- `--norm nc2` is **not** the paper's score: `ngram_term()` subtracts a floor per n-gram before dividing,
  `(raw - n_grams*floor) * n^2 * q0 / sumsq`, which changes rankings between keys with different sum N_c^2, and
  `score()` adds a KL unigram term (`--uni-weight`, default 1.0; families/homophonic.py also defaults uni_weight 1.0).
  Its docstring's "the ranking is exactly the paper's" is wrong. Its one real use was a NON-TEST (clair1161 planted
  control 0/3, LEDGER line 2583), and C1161-LOLO diagnosed why: "nc2 rewards rare letters at this free share (D2, D3)"
  (`ciphers/clair1161-avis-flandre-1688/tx/PREREG_reanneal_lolo.md` point 1). Quote that beside the nc2paper cell.
- SYSTEM.md s.8's `moves=swap_only` row is for `tools/families/syllabary.py` and `wordcode.py` (LESSONS-LASRY.md s.3
  item 3), not for this solver: this job does not build it there.

## Files

`tools/homophonic_anneal.py`, `tools/families/homophonic.py` (the same options as `--param`), the added
`tools/tests/test_homophonic_mqs.py`, `tools/tests/PREREG-MQS-SOLVER.md`, `tools/tests/MQS-SOLVER-controls.tsv` (every
control cell), rows in `tools/data/tool_shelf.tsv` and `SYSTEM.md` (**keep** s.8's `moves=swap_only` row, which is for
syllabary/wordcode, and append "homophonic: done (MQS-SOLVER)" to it). The 16 existing `tools/tests/test_*homophonic*.py`
files must pass unchanged. **MQS-LOCK starts only after your push of families/homophonic.py** (it may touch that file):
push it, and post the ROOM line "MQS-SOLVER pushed families/homophonic.py (<commit>)", **as soon as unit 1's offline
tests pass**, before the PREREG and the control cells.

## Units (stop before a unit that would cross 80% of cap or box)

Minutes are planning estimates, about 80% of the box split by each unit's dollar share (nearest measured rows: the
TOOLS-TOMO single-option Opus jobs of 8 Oct 2026, 11-18 min and USD 3.75-5.11 each, LEDGER.md lines 3548-3552). Two
timing probes on 9 Oct: `homophonic_anneal --control` at N=2600 K=40 runs in about 8-10 s at 2 restarts (the
check-and-fix pass's own probe: 9.5 s, 93.0% on an unmarked fr16 passage), so the CPU-bound cells are a small part of
the box; an unmarked control near 93% at N=2600 is near ceiling, which is why the N rule below chooses N on the
marked design's own blind baseline.

| # | Unit | USD | Min |
|---|---|---|---|
| 1 | The options (swap and cap ported from subst_hillclimb; gaps by fragment splitting) + offline tests + the docstring correction; push families/homophonic.py and post the ROOM line | 3.2 | 55 |
| 2 | PREREG; build the matched and mismatched controls; choose N by the rule; baseline and 2x-restarts baseline | 0.8 | 14 |
| 3 | Option cells, 3 seeds each | 1.6 | 28 |
| 4 | Registration | 0.4 | 7 |
| | Total 6.0 of cap 7.5; 104 of box 160 | | |

## Unit 1: options (homophonic_anneal.py CLI; the same names as families/homophonic.py `--param`)

- `--moves reassign|swap|both` (default reassign, today's behaviour): a swap exchanges the letters of two signs. Port the
  move and its proposal mix from `tools/subst_hillclimb.py` (credit it in the docstring: 23 Sept 2026,
  bowes-walsingham-1583), do not write a second one.
- `--max-homophones N`: no letter ever holds more than N signs in any accepted state (moves that would exceed it are
  skipped), ported from subst_hillclimb's `max_homo` check (every move and the greedy polish).
- `--min-count N` and `--homophone-budget K`: signs seen fewer than N times stay out of the search and decode as `?`;
  the run reports the share of tokens processed (CTTS's "93%"); `--homophone-budget` caps the number of signs searched.
- `--drop-letters h` (letters removed from corpus and model) and `--collapse-doubles` (a doubled letter folded to one in
  corpus and control text).
- `--as-unknown CLASSFILE` (and `--param exclude=FILE`): the listed signs stay in the stream as gaps; **no scored n-gram
  window spans a gap**; they are never deleted. Implement it as fragment splitting, following subst_hillclimb's
  `score_frags` and partial_key_test's gap rule, not as a new scoring path.
- `--norm nc2paper`: the paper's score exactly, raw n-gram log-likelihood divided by sum N_c^2, no floor; correct the
  nc2 docstring to say what it computes (floor-shifted nc2 plus the KL unigram term, a ranking that can differ from the
  paper's). Every norm runs with `--uni-weight 0` as well as 1 in the control.
- Offline tests `tools/tests/test_homophonic_mqs.py`: a swap preserves the multiset of assigned letters; the cap is never
  exceeded in any accepted state; `--min-count` reports the processed share and leaves low-count signs as `?`;
  `--drop-letters h` removes h from model and output; `--collapse-doubles` folds `ss` to `s`; with `--as-unknown`, a probe
  shows no scored window crosses a gap (must catch: the same probe under `--skip` does cross); `nc2paper` equals
  raw / sum N_c^2 on a toy; must not block: every default run reproduces today's scores byte for byte at a fixed seed.

## Units 2-3: the matched control and one mismatched cell (pre-register everything in PREREG-MQS-SOLVER.md first)

- **Design**, matched to the paper's cipher (Fig. 8 p.119): a synthetic homophonic French text from `tools/data/fr16`
  (a held-out passage), u/v and i/j merged, 1-2 homophones per letter (about 40 letter signs), plus nomenclature: 30% of
  tokens replaced by about 60 marked word or name signs, listed in a class file (the case `--as-unknown` is for).
- **N, by a fixed rule:** try N in {800, 1500, 2600} signs (2,600 is the paper's mean letter length, p.110); use the
  largest N at which the blind baseline (defaults, `--restarts 8`, marked signs handled by `--skip`) reads between 20%
  and 85% letter accuracy, mean of 3 seeds. If no N qualifies, write "no headroom at these N" and make no gain claim.
- **Cells**, 3 seeds each, same restarts unless named: baseline; baseline at 2x restarts (the restarts-alone bar);
  `--moves swap`; `--moves both`; `--max-homophones 2` (matched design: an **oracle upper bound**, since the generator
  uses exactly 1-2 homophones per letter, so the cap helps for that reason alone); `--max-homophones 2` on a
  **mismatched design** (same text, generator with 1-3 homophones per letter: the cell that grades the option);
  `--min-count 3`; marked signs four ways: `--as-unknown`, `--skip`, families/homophonic `wild=` and `solve_nomen` with
  `word_signs` (so the gate measures a gain over the existing alternatives, not only over deletion); `--norm nc2` and
  `--norm nc2paper`, each at `--uni-weight 1` and 0. `--drop-letters` and `--collapse-doubles` are covered by the offline
  tests only (no matched design for them here; say so).
- **Accuracy denominator (pre-registered):** all letter tokens of the control, with `?` (a low-count sign left out by
  `--min-count`, or a gap) counted wrong; report the processed share beside every cell. The same denominator for every
  cell, so neither `--min-count` nor `--as-unknown` is flattered by dropping tokens or penalised by an undefined one.
- **Gate per option:** it "helps" only if its mean gain over the baseline exceeds both the 2x-restarts gain and twice the
  baseline's seed SD (rule 3 headroom, the Salviati lesson); for `--as-unknown`, its gain must also beat the best of
  `--skip`, `wild=` and `word_signs`. Report every cell's mean and SD in `tools/tests/MQS-SOLVER-controls.tsv`. The
  marked-sign cells are the comparison that can fail differently: gaps, joined neighbours and per-position letters change
  the n-gram statistic itself.
- No target run in this job. A target use (the research note's s.2 audit of Salviati and es132, marked-sign targets) is a
  later job, after a cell passes.

## Registration

- tool_shelf rows, one per option: `homophonic_anneal.py --moves`, `--max-homophones`, `--min-count`, `--as-unknown`,
  `--norm nc2paper` (instrument; `controlled-only` when it passes its gate on this synthetic control, `weak` when it
  does not beat the restarts bar; evidence = the cell numbers and the TSV path).
- SYSTEM.md: name the options on homophonic_anneal.py's row; keep s.8's `moves=swap_only` row (syllabary/wordcode) and
  append "homophonic: done (MQS-SOLVER)".
- CLAUDE.md Usage 8 line (for the orchestrator): "Homophonic solver settings from the Mary Stuart paper and CTTS --
  `--moves swap|both`, `--max-homophones`, `--min-count`/`--homophone-budget`, `--drop-letters`, `--collapse-doubles`,
  `--as-unknown` (marked signs kept as gaps, never deleted) and `--norm nc2paper` (the paper's score) -- are on
  tools/homophonic_anneal.py and the family_run homophonic family, graded from one matched and one mismatched control
  (tools/tests/MQS-SOLVER-controls.tsv); swap and cap ported from tools/subst_hillclimb.py (MQS-SOLVER, 9 Oct 2026;
  Lasry, Biermann and Tomokiyo 2023 App. A; CTTS; Kopal 2019; LESSONS-LASRY.md s.3)."
- README common-tail line: "On a homophonic design with marked or nomenclature signs, keep them in the stream (--as-unknown
  gaps, or wild= / word_signs, whichever MQS-SOLVER's cells graded best), never --skip (which joins neighbours into false
  n-grams)."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-SOLVER worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD 7.5, box 160 min (80% line <HH:MM>) -- for LANE MQS (account 4)"`.
- **Your files.** Exactly the ones under "Files" below; the lane brief's file table says who owns what. Extend the
  existing script (CLAUDE.md Usage 8): an option and its functions; existing behaviour and existing tests unchanged.
  Run the tool's existing tests before your first edit and again before the push, and paste both results; a test that
  already failed before you started is named as pre-existing, not yours to fix.
- **Promotion (Usage 8).** Logic taken from a target-local script moves into the shared tool with credit in the
  docstring (the script's path, its job id and date). The original keeps working and gets one header line:
  `promoted to tools/<tool> <option> (MQS-SOLVER, 9 Oct 2026); kept because its outputs are cited` (the
  `tools/interlinear_align.py` precedent). No code from aaymeloglu/unsolved-ciphers (no licence; cite only). Bourdeau's
  code is MIT and CTTS is Apache-2.0: credit either if you adapt anything from it.
- **Usage 8a scope.** The docstring states, per option, what it is meant to catch and at least one case it must NOT
  flag, each backed by an offline test (no network in any test).
- **Rule 3.** Write every control's expected number and gate into `tools/tests/PREREG-MQS-SOLVER.md` and push that file
  BEFORE the control runs. Say in one line why each null can fail differently from the known answer for the statistic
  you compute (CLAUDE.md rule 3, the "control that cannot vary" paragraph). Check the control is not already near
  ceiling (about 95%) or matched by more restarts alone before reading any gain. A control that misses its gate ships
  the option with shelf grade `weak` and both numbers; it is not withdrawn, and nothing is run on a target from it.
- **Prior-work step** (`.claude/briefs/prior-work-step.md`). For every `ciphers/<slug>` folder you use as a known
  answer: `python3 tools/prior_work.py <slug> --step-type decode --known-answer gate:MQS-SOLVER --fetch` and paste its exit
  line. A known answer on already-read material is the point here. This is a tool job: no target is read, keyed or
  decoded beyond the named controls, and no target's status, key, reading or AUDIT.md changes.
- **Hosts.** None unless your job names one. Good-citizen rule: one request at a time, at least 1.5 s apart (2 s for
  BnF), User-Agent `cipher-lab research script (contact via repository)`, fetch once to disk with a manifest, read from
  disk after. On a 403, 429 or challenge page: stop using that host, log it in ROOM.md, never retry in a loop. No
  Gallica requests at all (HTTP 403 to cloud sessions since about 12:45 UTC on 8 Oct 2026). Report requests per host.
- **Registration (yours).** One row per tool or option in `tools/data/tool_shelf.tsv` (columns tool, kind, grade,
  use_when in the words a future brief would use, evidence = control numbers + file path, last_outcome). Paste
  `python3 tools/tool_shelf.py "<phrasing>"` for three phrasings per row, each showing your row in the top 3, and
  `python3 tools/tool_shelf.py --check` (your rows must not appear as MISSING; the 17 pre-existing MISSING rows are not
  yours). Name the tool or option on its row in `SYSTEM.md` (an added tool gets its own row, in the same commit) and
  paste `python3 tools/system_map_check.py` (exit 0). **Do not edit CLAUDE.md or `.claude/briefs/README.md`:** give the
  exact lines under "Registration" below in your final report; the lane orchestrator commits all eight jobs' lines in
  one edit at close (the TOOLS-TOMO precedent, 8 Oct 2026).
- **Commit and push.** Fetch and rebase before writing a shared file (`tools/data/tool_shelf.tsv`, `SYSTEM.md`,
  `ROOM.md`); keep both facts on a conflict. Before the final push run
  `python3 tools/file_shrink_guard.py <every file you touched>` and paste the output. Commit by explicit path only,
  ending the message with the two attribution lines YOUR session's system reminder gives (its Co-Authored-By line
  and your own Claude-Session URL; never a session URL copied from this brief, which would break the per-session
  trail rule 6 rebuilds from `git log`), through room.py's rebase-and-retry push:

  ```
  MSG="$(printf 'MQS-SOLVER: <one-line summary>\n\n<Co-Authored-By line from YOUR session's system reminder>\n<Claude-Session line from YOUR session's system reminder>\n')" \
    python3 tools/room.py --push <path1> <path2> ...
  ```

  Never `git add -A` or `git add .`, never force-push, never rewrite history. Push working increments (tests green)
  rather than one large commit at the end.
- **Words.** Rule 10 and rule 4a only: report what was found and where it was not found; never "solved", "cracked",
  "novel", "first" or "new" for anything this project did; do not classify novelty. Never name the owner in a
  committed file; never print a credential; never call AskUserQuestion.
- **Stop.** At the cap or at 80% of the box, whichever comes first, and do not start a unit that would cross 80% of
  either (Usage 6: the unit table gives each unit's dollar and minute estimates; check both before each unit). The orchestrator reads your cost every 15 minutes
  and will interrupt at the cap. Stop when the brief is met (Usage 7): follow-ups go in your report as one-line
  suggestions, never as extra work.
- **Done.** One ROOM line:
  `python3 tools/room.py "MQS-SOLVER worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
