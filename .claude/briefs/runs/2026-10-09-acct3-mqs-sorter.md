# MQS-SORTER: a sign sorter the owner can read, that stays blind, with a measured odd-ones-first view (job B of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for one worker on
**account 4**. Lane brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background: research note
`research/MARY-STUART-TALK-2026-10-09.md` section (f) and matrix rows M07, M08, M09, M10, M47.

- **Model:** Sonnet (`claude-sonnet-5`). **Cap:** USD 6.5. **Box:** 120 min.
- **Goal:** the owner's item 4, lessons from the authors' transcription GUI (CTTS; talk [00:12:45]-[00:13:41]; paper
  p.110-113, Fig. 4), without their one flaw for him: a hue per symbol type. He is red-green colour-blind and is the
  sorter's only human reader. And the sorter must stay **blind first** (TRANSCRIPTION.md: the person sorting is never
  shown key values or machine guesses that would bias the sort).

## What already exists (checked 9 Oct; do not rebuild)

- Tiles inside a pile are already ordered odd ones first by default: each tile's distance from its pile's mean tile
  (24x24 grey, normalised), `tools/sign_sorter.py` docstring line 20 and lines ~159-163; template option "Odd ones
  first" (line ~264, the first and default option) and the sort at line ~400. Shipped 1 Oct 2026. What is missing is a
  measured known-answer recall for it, so this job measures the existing score; it adds no rival ordering unless the
  existing one fails its gate (then a medoid / `bitmaps.npz` distance variant may be tried and reported beside it).
- Every tile state already carries a glyph and a border (out = x with a dashed ink border; kept/ref = check with a
  solid border; questioned = ? with a dashed accent border) and text chips ("done", "same as X", "not a letter", "to
  do"). LESSONS.md line 245 already says no information by colour alone.
- What fails today (recomputed 9 Oct with scikit-image CIEDE2000 after the Machado 2009 simulation): `--ok #2f6b3a` vs
  `--bad #b3261e` 11.3 (deutan) and 8.7 (protan); `--accent` vs `--bad` 2.7-9.3. The cut editor draws the box, its
  handles and the erased-ink rim in red #b3261e (`drawEdit`, template lines ~1200-1215). The hint text names colours
  ("Click the orange ?", "The red x", line ~258). Boxing is machine-only (the person cannot add or split a box; out of
  scope here, a later SORTER-BOX job).

## Files

`tools/sign_sorter.py`, `tools/sign_sorter/template.html`, `tools/sign_sorter_apply.py`, `tools/sorter_preflight.py`;
tests `tools/tests/test_sign_sorter_cvd.py`, `tools/tests/test_sign_sorter_blind.py` (added) and the existing
`test_sign_sorter.py`, `test_sign_sorter_apply.py`, `test_sorter_preflight.py` (extended, never weakened);
`tools/tests/PREREG-MQS-SORTER.md`; rows in `tools/data/tool_shelf.tsv` and `SYSTEM.md`. **Read-only:**
`tools/cvd_check.py` (MQS-SHEETS owns it; import it), every `ciphers/` file (never overwrite an owner's in-progress
sort, a `db/` export or a `settled_*.tsv`). Build outputs (sorter pages) go to your scratchpad, never into the repo, and
are never published by you: the account-3 parent publishes.

## Units (stop before a unit that would cross 80% of cap or box)

| # | Unit | Estimate |
|---|---|---|
| 1 | Blind-first default, the declared non-blind mode, the `mode` export column + tests | USD 1.0 |
| 2 | Pile sorting by size / mark category (blind-safe) and by value (non-blind only) | 0.6 |
| 3 | `--oddness-audit` + PREREG + the planted-mislabel control | 0.9 |
| 4 | Score the owner's no.87 sort with `tx_bench.py` against BENCHMARK-TX | 0.4 |
| 5 | Palette, cut editor, hint text, per-pile box patterns, `sorter_preflight.py --cvd` + tests (after the MQS-SHEETS "step 1 pushed" ROOM line) | 1.6 |
| 6 | Rebuild the Birago no.87 sorter in scratch, preflight PASS, one screenshot read (1 vision call) | 0.5 |
| 7 | Registration | 0.4 |
| | Total 5.4; cap 6.5 | |

Units 1-4 do not need `tools/cvd_check.py`; do them first. If the MQS-SHEETS line has not appeared when you reach
unit 5, wait up to 20 minutes (one ROOM check every 5), then write a ROOM flag and stop at unit 4 with a report.

## Unit 1: blind first

- The default page shows **no key values and no machine value guesses**: no value text, no capitals mapping, no group
  by value. (Ranking which tiles to ask first, `--rank-lattice`, stays as it is: an order, not a displayed value.)
  Test `test_sign_sorter_blind.py`: build a page with key and top-k inputs present and assert that none of the key's
  value strings appear in the page's visible text or display data.
- A declared non-blind mode, `sign_sorter.py --show-values KEY --blind-sort DB_EXPORT`: refused (non-zero exit, a
  message naming TRANSCRIPTION.md) unless `--blind-sort` names a saved blind export for the same tiles. The page header
  then says "Non-blind view: values shown; decisions here are not transcription evidence". In that mode only: values
  in CAPITALS when the owner set them or the key confirms, lower case for machine and top-k guesses, `_` prefix for
  nulls, `?` for unknown (the same mapping as `decode_key.py --style case`, matrix M10); a "Group by value" view with I/J
  and U/V merged, as a working form of the paper's homophone strip (Fig. 8, p.119).
- `sign_sorter_apply.py` writes a `mode` column (`blind` or `keyed`) on every exported row, read from the page's data.
  Its docstring and a test say a `keyed` row is never used as BENCHMARK-TX evidence or adjudication evidence.

## Unit 2: sorting piles (CTTS habit)

A "Sort piles" control: by size, by name, and by mark category (from `--marks` families: base, dotted, hooked, slashed
... as the atlas gives them) in every mode; "by value" only on a non-blind page. One line of help text cites the CTTS
README's tip (segment about 500 symbols, then classify in bulk, category by category; credit Lasry, CTTS, Apache-2.0).

## Unit 3: is odd-ones-first any good? (pre-register before running)

- Add `sign_sorter.py --oddness-audit --signs S --labels TRUTH --pages P --plant 0.05 --plants random|lookalike
  [--confusion C.tsv] --seeds 20`: it uses the **same** oddness function the page uses (so the measure is of the
  shipped feature, rule 7) and prints, per seed, recall@10% (the share of planted tiles in the first 10% of their pile)
  and the shuffled-order p95.
- Known answer: Birago no.87 clean piles: the no.87 tiles grouped by their truth-derived sign label
  (`ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token.tsv`, `atlas/sheet_truth/`). Two plant kinds, 5% each, 20
  seeds: **random** (a tile moved to a random other pile) and **look-alike** (moved to its top confusion partner's pile,
  from the no.87 confusion table: s<-T50, d<-T98, t<-T90, e<-T76 ..., TRANSCRIPTION.md line 71; `tools/lookalike_pass.py`
  has the plant logic). Random plants are far easier than the real errors, which are look-alikes, so report both.
- Gate (write it in PREREG first): random plants recall@10% >= 0.6 and above the shuffled-order p95 in at least 18 of
  20 seeds; look-alike plants above the shuffled-order p95 (the number reported, whatever it is). The shuffled order can
  fail differently: it changes which tiles sit in the first 10%, which is exactly the statistic.

## Unit 4: score the owner's no.87 sort

The owner sorted 248 no.87 tiles on 4 Oct (`ciphers/nevers-birago-fr3251-1572/sorter/no87/owner-sort-2026-10-04/settled_no87.tsv`;
BIR87-ALIGN gave his piles 0.848 clerk-sheet agreement vs shuffled 0.338, the committed machine labels 0.896).
TRANSCRIPTION.md says each owner session is scored against BENCHMARK-TX where an item exists, and no.87 is the eval
item. Run `python3 tools/tx_bench.py` on his labels with `--label-map` (owner pile -> value, from BIR87-ALIGN's C values
per pile, `harvest/bir87align/`) and `--paired` against the committed machine labels on the same positions; report
err_true with its interval for both and the paired fixed/broken counts. Set the `sign_sorter.py` shelf grade from that
(the shelf's own definitions; "owner labels are one strong reader, not ground truth"). If the mapping cannot be built
honestly, say so and leave the grade `untested`.

## Unit 5: the palette (research note section f; after the MQS-SHEETS line)

- Light tokens from `cvd_check.PALETTES['sorter_light']`: `--ok` blue #0072B2 (check chip, solid border); `--bad` dark
  orange #B35900 (cross chip, dashed border; never a text colour on #f3f1ec, where it reaches 4.28:1); `--warn` a yellow
  #F0E442 tint as fill only, with a '!' chip and a dotted ink border; `--accent` ink #24211c with a double border; grey
  #767676 for muted marks. Dark tokens from `PALETTES['dark']`: ok #56B4E9, bad #E69F00, ink #ece6dc. Text stays ink.
- The cut editor: no red. Box outline dark orange dashed over a white under-stroke; erased-ink rim dotted ink; handles
  blue squares and circles with white borders (shape tells edge from corner).
- Hint text names glyphs, never colours ("Click the ? badge", "The x on a sign").
- Boxes on the page and region views: each pile's boxes take blue, dark orange or grey crossed with a fill pattern
  (solid, hatch, dots) and carry the pile's short ID (labels on by default), so no two neighbouring piles differ by hue
  alone; a "show only this pile" filter; the selection outline a thick black-and-white double dashed line.
- `sorter_preflight.py --cvd` (and run by default as a fifth check): parse the template's `:root` tokens (light and
  both dark blocks) and the box palette, run `cvd_check`, and fail on any pair under the gate or any colour word
  ("red", "green", "orange") in hint text. Tests `test_sign_sorter_cvd.py`: the legacy tokens FAIL (must catch); the
  updated template PASSES; a template with a red/green pair FAILS; a hint naming "red" FAILS; must not block: the word
  "green" in a non-hint string (a pile name, a data value) passes.

## Unit 6: rebuild for the owner's eye

Rebuild the Birago no.87 sorter page with `sh ciphers/nevers-birago-fr3251-1572/sorter/no87/build.sh <your scratch>/birago-no87-cvd.html`
(read-only use of that folder; if the script writes into the folder, copy its steps with outputs to scratch), beside
the existing page, never over the owner's sort. Run `sorter_preflight.py` (PASS required) and read one screenshot.
Put this ASKS.md text in your report (the parent appends it with the link once it publishes the page): "Colour check of
the sign sorter (MQS-SORTER, 9 Oct 2026): open <link>. Can you tell done / to do / not a letter / bad cut apart without
reading the chips? yes/no". The owner's answer, not the simulation, is the final test.

## Registration

- tool_shelf rows: `sign_sorter.py --oddness-audit` (instrument; grade from unit 3), the `sign_sorter.py` row's
  evidence and grade from unit 4, `sorter_preflight.py --cvd` (gate).
- SYSTEM.md: name `--oddness-audit`, `--show-values` and `--cvd` on their tools' rows.
- CLAUDE.md Usage 8 line (for the orchestrator): "The sign sorter shows no key values or machine guesses by default
  (TRANSCRIPTION.md, blind first); `sign_sorter.py --show-values` is a declared non-blind mode available only after a
  blind sort is saved, and its exports carry mode=keyed, never transcription evidence. `sorter_preflight.py` fails any
  sorter page whose colours fail `tools/cvd_check.py` or whose hints name a colour (MQS-SORTER, 9 Oct 2026)."
- README common-tail line: "A sorter page is built blind (no values shown); a non-blind page is declared on the page and
  its decisions are never used as transcription evidence."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-SORTER worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD 6.5, box 120 min (80% line <HH:MM>) -- for LANE MQS (account 4)"`.
- **Your files.** Exactly the ones under "Files" below; the lane brief's file table says who owns what. Extend the
  existing script (CLAUDE.md Usage 8): an option and its functions; existing behaviour and existing tests unchanged.
  Run the tool's existing tests before your first edit and again before the push, and paste both results; a test that
  already failed before you started is named as pre-existing, not yours to fix.
- **Promotion (Usage 8).** Logic taken from a target-local script moves into the shared tool with credit in the
  docstring (the script's path, its job id and date). The original keeps working and gets one header line:
  `promoted to tools/<tool> <option> (MQS-SORTER, 9 Oct 2026); kept because its outputs are cited` (the
  `tools/interlinear_align.py` precedent). No code from aaymeloglu/unsolved-ciphers (no licence; cite only). Bourdeau's
  code is MIT and CTTS is Apache-2.0: credit either if you adapt anything from it.
- **Usage 8a scope.** The docstring states, per option, what it is meant to catch and at least one case it must NOT
  flag, each backed by an offline test (no network in any test).
- **Rule 3.** Write every control's expected number and gate into `tools/tests/PREREG-MQS-SORTER.md` and push that file
  BEFORE the control runs. Say in one line why each null can fail differently from the known answer for the statistic
  you compute (CLAUDE.md rule 3, the "control that cannot vary" paragraph). Check the control is not already near
  ceiling (about 95%) or matched by more restarts alone before reading any gain. A control that misses its gate ships
  the option with shelf grade `weak` and both numbers; it is not withdrawn, and nothing is run on a target from it.
- **Prior-work step** (`.claude/briefs/prior-work-step.md`). For every `ciphers/<slug>` folder you use as a known
  answer: `python3 tools/prior_work.py <slug> --step-type decode --known-answer gate:MQS-SORTER --fetch` and paste its exit
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
  with the two attribution lines, through room.py's rebase-and-retry push:

  ```
  MSG="$(printf 'MQS-SORTER: <one-line summary>\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_0198Cv8ypBfBVfRToKVWx33M\n')" \
    python3 tools/room.py --push <path1> <path2> ...
  ```

  Never `git add -A` or `git add .`, never force-push, never rewrite history. Push working increments (tests green)
  rather than one large commit at the end.
- **Words.** Rule 10 and rule 4a only: report what was found and where it was not found; never "solved", "cracked",
  "novel", "first" or "new" for anything this project did; do not classify novelty. Never name the owner in a
  committed file; never print a credential; never call AskUserQuestion.
- **Stop.** At the cap or at 80% of the box, whichever comes first, and do not start a unit that would cross 80% of
  either (Usage 6: the unit list below gives each unit's estimate). The orchestrator reads your cost every 15 minutes
  and will interrupt at the cap. Stop when the brief is met (Usage 7): follow-ups go in your report as one-line
  suggestions, never as extra work.
- **Done.** One ROOM line:
  `python3 tools/room.py "MQS-SORTER worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
