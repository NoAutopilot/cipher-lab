# PREREG TX-ENGINEER-2 round 0 (LANE TX-ENGINEER-2, account 4, Fable, session_01NmaB9fhuaMSMYexV4NaVsR; written 9 Oct 2026 15:1x UTC by date -u; pushed BEFORE any read or score of this campaign)

Brief `.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer-2.md`. The first campaign's result
(`research/TX-ENGINEER-2026-10-09.md`), its register (`research/TX-IDEAS-2026-10-09.md`) and taxonomy are read. This file fixes
what success means and the gate; nothing below is loosened after any result is seen. Amendments are appended, dated, never
edited in place.

## What success means (copied from the brief, fixed)

S1 (primary, the owner's number): held-out per-sign error, measured against a known answer on a pool of leaves the lane never
   tuned an instrument on, is lower under the new pipeline than under today's (two blind passes + reconcile + relabels +
   follow-slope crops), with paired fixed > broken at the pre-registered p, on a pool big enough that a 30% relative reduction
   is detected with >= 80% power. Both figures are reported (as measured, flagged-excluded) and the sign count: "N more signs
   right per 1,000".
S2 (generalisation): the same pipeline, frozen, scores on ONE confirm item built by a separate session on a hand the lane never
   touched (TX-CONFIRM-SET-2, account 1), looked at once at the end; that number sits beside S1 in the headline.
S3 (application): the frozen pipeline run on one live unread letter (Birago 1572 f.117r/f.144r/f.168r, or Spinelli's unread
   passages) under the folder's own PREREG and power control: "the key now licenses N more tokens at grade S, judge not worse".
S4 (the sorter product, secondary): a read-free doubt list that holds >= 70% of the remaining held-out errors at <= 15% of
   positions flagged; plus a measured value curve: with an oracle standing in for the owner, how many sorter decisions take a
   leaf from today's error to 2% (read-free, from the benchmark).
S5 (cost): cost per 100 signs at equal error, reported per experiment (TRANSCRIPTION.md target 8).
A result counts only on S1 or S2; S3-S5 are reported beside it. Nothing moves TRANSCRIPTION.md's "Today" column but S1/S2.

## 0a. Power audit (tools/tx_power.py, run 15:1x UTC; table in benchmark-tx/txeng2/power-2026-10-09.md)

Planted instruments on every unit and pool on disk, 1,000 draws each (clean = fixes FIX of the baseline errors, breaks none;
noisy0.5 = also breaks correct signs at base_err x 0.5, the brief's level; noisy0.1 a milder column; worse, no-op and
random-3% are the negative controls; a pass is fixed > broken with two-sided sign test p < alpha):

| unit (baseline) | E | N | clean 30% @0.01 | @0.05 | clean 50% @0.01 | @0.05 | worse/no-op/random3 (any alpha) |
|---|---|---|---|---|---|---|---|
| dev_tune (L) | 12 | 343 | 0.008 | 0.106 | 0.208 | 0.622 | 0.000 |
| eval_heldout (L) | 15 | 376 | 0.053 | 0.269 | 0.505 | 0.857 | 0.000 |
| geo (L) | 15 | 169 | 0.048 | 0.278 | 0.529 | 0.859 | 0.000 |
| no87 whole (L) | 34 | 803 | 0.855 | 0.973 | 0.999 | 1.000 | 0.000 |
| spinelli confirm (passZ, mapped) | 14 | 193 | 0.025 | 0.208 | 0.408 | 0.821 | 0.000 |
| dint-f128 (pass B, mapped) | 11 | 85 | 0.004 | 0.077 | 0.138 | 0.513 | 0.000 |
| ceppo f21v / f87 / f36v (C, C, recon) | 1 / 7 / 7 | 189 / 139 / 16 | 0.000 | <= 0.004 | 0.000 | <= 0.067 | 0.000 |
| POOL eval today = eval_heldout + spinelli | 29 | 569 | 0.695 | 0.907 | 0.996 | 0.999 | 0.000 |
| POOL dev today = dev_tune + dint_B + f87_C + f36v | 37 | 583 | 0.914 | 0.984 | 1.000 | 1.000 | 0.000 |
| smallest E for a clean 30% fixer to pass >= 80% | | | 32 | 24 | 19 | 15 | |

Reading: every first-campaign unit was a non-test for a 30% instrument at p < 0.01 (0.8-5% power) and under 30% at p < 0.05.
The noisy0.5 model (an instrument that breaks half as many signs as it finds wrong) passes nowhere at any N: no real instrument
is accepted on that shape, and the campaign's instruments are required to be fixers at the flagged positions, not blanket
re-readers (brief rule 2).

## The gate (fixed now; the weakest (pool, p) at which a clean 30% fixer passes >= 80%)

- **Single-experiment gate (S1):** paired fixed > broken, two-sided exact sign test **p < 0.01**, on the **eval pool** (below),
  one eval look per experiment, counted in `research/TX-IDEAS-2-2026-10-09.md`; the dev gate of each experiment is the same
  test on the dev pool at p < 0.05 (a dev pass licenses the one eval look; a dev fail does not).
- **Pool size condition:** the eval pool must carry **>= 32 baseline errors** under today's pipeline before any eval look is
  spent at p < 0.01 (tx_power: 80% power for a clean 30% fixer). Today it carries 29 (eval_heldout 15 + spinelli 14). Round 0b
  grows it; if 0b has not reached 32 when experiment 1 is ready, the single-experiment gate for THAT and every later
  experiment is p < 0.05 at >= 24 errors (0.907 power today) and the campaign says so in every table -- declared here, before any
  instrument result, never switched back and forth per result.
- **Combined frozen pipeline (final):** one look on the eval pool at the same p as the single-experiment gate in force, then
  S2's single confirm2 look (no threshold: reported whatever it is).
- **Pools.** Eval pool = eval_heldout (no.87 f178v L13-23 + f179r L01-03, L baseline) + spinelli-c1519-confirm (passZ_pipeline
  baseline, collapse_map.tsv) + every new `split=eval` item 0b builds. Dev pool = dev_tune (no.87 f178v L01-12) + dint-f128-print
  (pass B until a pipeline baseline exists) + ceppo-f87-S + ceppo-f36v-gloss + every new `split=dev` item. The geo unit (f178r
  L01-03 + the band-cut lines) stays outside both pools (its lines overlap dev and eval, and the sloped tail is a crop rule
  already adopted). An item's hand sits in one split only; no.87's hand is eval, so a Birago 1572 item is eval; Dinteville and
  Ceppo hands are dev; Spinelli is eval. Pass-level baselines are the committed outputs named above; a 0b item's baseline is
  today's pipeline (two blind Opus 5.5 passes, reconcile, the folder's Sonnet adjudication protocol, relabels where the family
  has them, follow-slope crops) run once, committed before the truth is opened by that worker.
- Scoring: `tools/tx_bench.py OUT.tsv --bench BENCHMARK-TX.tsv --item I --paired BASE.tsv [--label-map M]`; pool counts add
  fixed and broken over items; `--exclude-flagged` figures reported beside, never alone.

## 0b. Headroom pool (target >= 60 eval baseline errors on hands reading 8-25% today)
Truth only from a period/published key and a known text (a period decipherment, clerk sheet, printed plaintext), aligned by
`tools/interlinear_align.py`, exactly as build_birago87.py / build_spinelli_confirm.py; never from a reader, never from an
S-graded decode of the same passes. Each item: a build script with `--check`, sha256 of the truth, `split`, its baseline with
CI, in BENCHMARK-TX.tsv. Readers never see truth. Candidates, in order of expected errors per cost, with the prior_work and
NOTES check done by the worker before building:
1. DECODE "Decrypted" BnF Nevers-office 1590s items reachable today (Gallica 403): fr.3619 ff.73-113 (records 9438-9443),
   fr.3621 ff.31-89 (9444-9448; f.128 = 9450 is dint-f128-print), fr.3623 ff.23-75 (9452-9458); fr.4718 fols. 17, 21, 40
   (Dinteville, cipher with decipherment; no Gallica copy) if DECODE holds them. Scout first (TXP-DEC): which carry a legible
   period decipherment on the image, symbol or digit, estimated signs, sign repertoire against Dinteville's key_print. A hand
   there is a Dinteville-family hand (dev) unless its key differs, in which case it is a new hand and goes to eval.
2. Birago 1572 f.152r (no.77): the decipherment slip (harvest/f152r/decipherment_slip.tsv, ~15 unread dots excluded) through
   the printed 1572 key; ~97 signs; eval (no.87's hand). TXP-152.
3. Florence c.111/c.127 glossed lines, fr.3252 f.36v gloss beyond line 1, fr2980-gramont, colbert26: held back -- their
   alignments do not hold at sign level today (A2-FLO3 pilot; F36-GLOSS gate FAIL; colbert26 63/294); reconsidered only if 1-2
   fall short of 32.
Excluded from this lane's pool: whatever leaf TX-CONFIRM-SET-2 (account 1) builds (its row says not Birago/Ceppo/Dinteville/
Spinelli, so no collision by construction).

## 0c. Gate controls (run before experiment 1, on the eval pool as it stands at that moment; recorded in the register)
(i) positive: a planted script fixer that fixes 30% of the pool's baseline errors at random must pass the gate in force in
>= 80% of 1,000 draws (tx_power clean@alpha); (ii) negative: no-op and random-3% perturbation pass in <= 1% / <= 5%; (iii) a
30%-worse instrument fails. If (i) fails, the pool is too small: back to 0b; the gate is never moved after an instrument's
result is seen. On today's pool: (i) 0.695 at p 0.01 (FAILS the 80% bar -> 0b continues; 0.907 at p 0.05 passes), (ii) 0.000,
(iii) 0.000.

## 0d. Error map
`tools/tx_taxonomy.py` over the baseline passes of every pool item, plus the column the first campaign lacked: reader
agreement on errors (the same wrong sign across readers and presentations), so a class whose errors are "every reader, every
presentation" is not re-attacked by another presentation. TXP-AGREE (read-free).

## Blindness and conduct (as PREREG-txeng-2, carried over)
A reader subagent sees crops (and the family's blind sign sheet) only; never truth, decodes, other passes, labels.json
overrides, align files. A worker opens an item's truth only after that split's reads are committed. No `*.truth.tsv` is edited
by hand; truth comes from a build script. Crop step mandatory and pasted; one page per subagent call; passes priced per call;
reconciliation a priced unit. No experiment re-runs a family the first campaign retired for this hand (compare/exemplar layouts,
feature-first vocabulary, plain re-passes at scale or under rendering, the lattice as a blanket fixer) unless its PREREG says what
is different. Three fails of one experiment with real fixes between retire it (rule 3). Every instrument is a tool in tools/
with --help, an offline test, a tool_shelf.tsv row and a SYSTEM.md row.

## Amendment 1 (lane, 9 Oct 2026 15:5x UTC by date -u; written after round 0 reports, BEFORE any experiment's eval look)
- 0b: `birago1572-f152r` built (TXP-152, 73 scored, baseline passZ 5 position errors + 1 insertion). Eval pool = eval_heldout 15 +
  spinelli 14 + f152r 5 = **34 baseline errors >= 32**: the **p < 0.01 branch is in force for every experiment** of this campaign.
- 0c on that pool (tx_power, 1,000 draws): (i) clean 30% fixer passes p < 0.01 in 0.863 (>= 0.80: PASS); (ii) no-op 0.000, random-3%
  0.000 (PASS); (iii) 30%-worse 0.000 (PASS). The gate stands and is not moved again.
- 0b continues for the OWNER's headroom (hands at 8-25%), with the split of every new item declared here before its build: the
  three glossed Dinteville leaves of fr.3619 (f.89, f.98v, f.113; DECODE 9440/9441/9443; same scribe as f.128 by the scout's eye)
  are the Dinteville hand and therefore **dev** (the rule "an item's hand sits in one split only"); the Birago-style 1590s symbol
  hand (fr.3623 f.23r, DECODE 9452; the short fr.3619 f.73 / fr.3621 ff.42-49 / fr.3623 f.41 runs if pooled) is a hand in no
  split today and goes to **eval**. Truth for all: the leaf's own period interlinear decipherment read by two blind Opus passes
  and reconciled, aligned by interlinear_align, forced through a key rebuilt from the alignment at agree >= 2 (the dint-f128-print
  recipe), checked against key_print where the Dinteville sign is in it; grade C with the note; reference sequence = the
  pipeline's own passZ (home advantage on segmentation, stated in the row, as dint-f128-print). Blind cipher readers must not
  see the gloss: crops are cut with the gloss rows masked (`--mask-neighbours`), checked on the overlay; an item whose crops
  still show gloss letters is marked `gloss-visible` in its BENCHMARK-TX notes and its baseline is reported as an upper bound
  on reader accuracy, never pooled with the others for a gate.
- 0d (TXP-AGREE): eval pool all-same-wrong 8 of 29 (28%), split 11, majority 7, minority 3; dev 6 of 37 (16%). The 8 all-same-wrong
  eval errors (Spinelli's two deleted h, no.87's o<-T70 and z<-T60 among them) are not attacked by presentation changes.
- Round 1 results (dev only, no eval look): X2 FAIL (1/11 wrong way); X20 FAIL (0/3); X6 is a measurement: whole-cluster
  propagation is destructive (77% cluster purity), per-tile the doubt feed removes a third to two thirds of what an oracle would.

## Amendment 2 (lane, 9 Oct 2026 17:4x UTC by date -u; answers to TX-RED pass 1 F1-F4, research/TX-RED-2026-10-09.md; written BEFORE any eval look, none spent)
- **F1 adopted.** The dev gate line above says "on the dev pool"; every no.87-only instrument ran on dev_tune (E 12), where a
  clean 30% fixer passes p < 0.05 in 0.106 of draws. Register verdicts are re-labelled: a right-way null on dev_tune is "dev
  non-test at E 12" (X3 4/5, X5 3/7, X7 5/4, X2b 3/0, X4's doubt arm); a wrong-way result significant at p < 0.05 stays
  "dev-FAIL" (X2 1/11, X13 2/14, X4 weights 2/9); X20 0/3 is a non-test too (p 0.25). From now: the dev stage of a no.87-only
  instrument is a SCREENING stage, pre-declared here: fixed > broken with two-sided sign-test p < 0.10 on dev_tune (so 5/0 or
  7/1 passes, 3/0 does not) AND every registered control failing; a screening pass licenses the one eval look at the gate in
  force; a right-way miss is logged non-test, never FAIL. A hand-independent instrument (X1, X12, X8, any read arm) gates on
  the dev pool as the line above says. X2b (3/0) does not pass screening; its own named next step stands.
- **F2 adopted.** The paired count that decides a pass is taken with `--exclude-flagged` (a verifier-flagged position has
  doubtful truth and cannot decide a pass); the as-measured count is reported beside. Eval pool, flagged excluded: eval_heldout
  10 + spinelli 14 + f152r 2 = **26** (< 32). The pre-declared fallback branch applies: **single-experiment gate p < 0.05 on
  the eval pool at >= 24 errors** (tx_power this amendment, E 26 / N 634: clean 30% fixer 0.849 at p 0.05, 0.543 at p 0.01;
  no-op, random-3%, 30%-worse 0.000). Amendment 1's "p < 0.01 branch in force" rested on the as-measured 34 and is withdrawn
  before any look; the branch now fixed is p < 0.05 and holds for every experiment of this campaign. The combined pipeline's
  look and S2 stay at the same p. A verifier pass on f152r's 3 flagged positions (TXV-152) may raise the pool; the branch
  does not change again.
- **F3 adopted.** dint-f89-gloss-kp2 leaves the dev pool for read arms: it is gloss-visible (Amendment 1's exclusion stands
  over PREREG-3 R2's pool rule, which omitted it -- the lane's error); it may serve read-free instruments only, and only after
  the recipe's known-answer control: kp2 run on dint-f128-print against the 1882-print truth (TXP-KP2C, PREREG-txeng2-4),
  reporting per-position agreement of the kp2 set with the print set and the baseline's err_true under each. Until that
  control is on file, f89-kp2 counts toward no gate. BENCHMARK-TX gains a `gloss_visible` note on the four gloss items.
- **F4 adopted.** S1's "leaves the lane never tuned on" is amended to "lines or leaves the lane never tuned an instrument on";
  every eval paired count is reported split: held-out lines of the tuned leaf (eval_heldout, 10 flagged-excluded) and
  held-out leaves (spinelli 14 + f152r 2 = 16), with the pool total; a result that holds only on the tuned leaf's lines is said
  so.

## Amendment 3 (lane incarnation 2, session_011EV9AKeJ4YuU9jjghdUy6F, 9 Oct 2026 18:3x UTC by date -u; after TXV-152 (V1) and TX-RED pass 2 F9/F11; written BEFORE any eval look, none spent)
- **Eval pool recount (F9 adopted).** After V1's verdicts (benchmark-tx/birago1572-f152r.flags.tsv: L03.32 CORRECT, L04.16 and
  L04.18 FLAG, L03.8 as built), `tx_bench.py ... --item birago1572-f152r --exclude-flagged` re-run this incarnation: as measured
  0.069 (5/73: 4 wrong + 1 inserted); flagged excluded 0.029 (2/70: 1 wrong + 1 inserted; 3 flagged). Position errors
  flagged-excluded = **1**. Eval pool, flagged excluded = eval_heldout 10 + spinelli 14 + f152r 1 = **25** (tuned-leaf lines 10,
  held-out leaves 15). `tx_power.py --errors 25 --n 630 --fix 0.3 --alpha 0.05` (1,000 draws): clean 30% fixer passes **0.797**
  (E 24: 0.774; E 23: 0.706); at p 0.01 0.221; no-op, random-3%, 30%-worse 0.000. The branch in force stays **p < 0.05 at
  >= 24 errors** as Amendment 2 declared; the 0.797 figure is reported as it is (three thousandths under the 80% bar at this
  draw) and the gate is not moved on it. Growing the pool is the remedy, never the threshold.
- **Under 24 (declared now, F9 ii).** If any later verifier verdict or truth correction takes the flagged-excluded pool under
  24, no eval look is spent until an eval item built under 0b's rules (an independent key and a known text) restores >= 24;
  the branch does not move in either direction.
- **Spinelli verification before the first look (F9 iii).** No eval look is spent before a verifier session (never a lane
  solver) has decided Spinelli's 6 all-same-wrong positions (the 2 deleted h, i <- EIGHT, e <- SIX, p <- THREE, n <- PHI;
  benchmark-tx/txeng2/errormap/spinelli-c1519-confirm_positions.tsv) from the Beinecke image and the 2017 plaintext through
  build_spinelli_confirm.py's flag column (TX-TRUTH-VERIFY's shape; PREREG-txeng2-5 V2), and the pool is recounted here as
  Amendment 4. A look taken on a pool a later verifier shrinks cannot be un-taken.
- **kp2 items (F11 adopted).** C1 (TXP-KP2C) FAILed its declared gate (31/59 = 0.525 set equality; the equal-or-contains
  59/59 figure is reported beside and is not a gate). Register verdict for dint-f89/f98v/f113-gloss-kp2: **truth-unknown;
  usable for err_2reader and read-free agreement work only**, not "pending a gate". No alternative gate on f.128 is
  pre-registered: on the one leaf with an independent truth kp2 scores 52 positions the print recipe excludes, where its
  truth is unverifiable by construction. A second independent witness (a print, a clerk sheet) is the only thing that makes
  those leaves a known answer.
- **Read-free eval openings (F6 adopted).** From this amendment every results-log row in research/TX-IDEAS-2-2026-10-09.md
  carries, in its eval cell, the count of read-free openings of eval truth the experiment made ("openings: N"), and the
  register's eval_result column inherits it; the campaign line "Eval looks taken so far" names both totals.
- **Audit trail (F7 adopted).** Every RESULTS.md written from this amendment carries the sha256 of each file it claims was
  committed before a score, beside the commit hash (lane brief Amendment 2); the round-5 worker brief states it; a RESULTS
  without it is entered in the register as "committed-before-score unverified".
- **Reader model (F13).** The campaign's "today's pipeline" mixes a Sonnet reconcile pipeline (no.87 L) with Opus pipelines
  (f152r, the gloss items, S2's planned passes). PREREG-txeng2-5 X21 tests the reader model as an instrument on the dev pool;
  if the Sonnet arm wins at p < 0.05 the baseline of every pool item is re-run as Sonnet before any instrument is scored on it
  and the "never below" rule is amended for the reader role; until then no eval look is spent on an item whose baseline model
  differs from the instrument's reader (declared here, before any look).

## Amendment 4 (lane incarnation 2, 9 Oct 2026 19:1x UTC by date -u; after V2 (TXV-SPIN), X21 (TXE2-MODEL) and TX-RED pass 3 F15-F19; written BEFORE any eval look, none spent)
- **Pool after V2 (F16).** TXV-SPIN: 2 FLAG (p1c_L01.5 i <- EIGHT reading-doubtful; p1c_L03.16 p <- THREE label-doubtful), 4 KEEP;
  the 2 "deleted h" are h <- SIX substitutions inside the band every pass saw (ERRORMAP's crop class was wrong). Spinelli
  flagged-excluded position errors 14 -> 12 (0.079, 15/191). Pool = 10 + 12 + 1 = **23 < 24**: Amendment 3's under-24 rule fired
  by its own words -- no eval look until an 0b-rule item restores >= 24.
- **f178r L01-03 declared an eval unit (the 0b-rule item).** Truth: no.87's clerk clear sheet through the printed 1572 key
  (build_birago87.py, C/H), already on file for these lines; in neither split until now (the geo unit, kept out because its
  f178v lines overlap dev/eval and because the sloped tail was a crop rule). Unit `f178r` = f178r_L01-03 only
  (benchmark-tx/txeng/units/labels_f178r.tsv, sha256 5a6477b4306f6af9...; passA_f178r.tsv beside it): baseline L 7/84 as
  measured, **6/83 flagged-excluded** (f178r_L03.23 flagged, the ampersand split). Caveat declared: these lines tuned the
  follow-slope crop rule (TXE-D), now part of the baseline both arms share; so they are "tuned-letter lines" and are reported
  in the split with eval_heldout, never with the held-out leaves. **Eval pool, flagged excluded = eval_heldout 10 + f178r 6 +
  spinelli 12 + f152r 1 = 29** (tuned-letter lines 16; held-out leaves 13). `tx_power.py --errors 29 --n 715 --fix 0.3
  --alpha 0.05`: clean 30% fixer **0.908**; no-op, random-3%, 30%-worse 0.000. The branch stays p < 0.05 at >= 24.
  Consequence: f178r L01-03 is never training ink; **X2c (TXE2-PAIR3, PREREG-txeng2-5) is cancelled** before any training
  (the first session never ran, the re-spawn was interrupted at its first turn); X2b's named next step now needs labelled
  no.87-hand ink that will never be pooled, which does not exist on disk -- logged "blocked: no non-pool labelled ink".
- **X21 (F15 adopted).** Pooled Sonnet 33/14 p 0.0079 is carried by ceppo-f87-S (19/2), whose truth derives from the
  committed passC = the Sonnet A/B reconcile the fresh Sonnet arm reproduces exactly; on the two Sonnet-independent items
  (dev_tune clerk sheet, dint 1882 print) it is 12/14, null. Register verdict: **pooled non-test; Sonnet-independent items
  12/14 null**. Amendment 3's re-baselining rule does NOT fire. Its sentence "no eval look on an item whose baseline model
  differs from the instrument's reader" is restated as a declared caution (every eval result names the baseline's reader
  model beside the instrument's), not a consequence of X21. Rule added: the Ceppo S items (truth = the committed Sonnet
  reconcile) never score a comparison between reader models or pipelines; they serve instrument-vs-L tests only, said so in
  every table. X21b (PREREG-txeng2-6) re-asks the question on independent truths only.
- **Sheet defect (F18 adopted; F17 d).** Spinelli's readers' sheet (ciphers/spinelli-beinecke-c1515/glyphs/atlas.png) shows
  this item's own h token (p1_01_025) as a SIX exemplar; 3 of Spinelli's 12 errors (the 2 h <- SIX, the SEVEN_E deletion at
  p1c_L01.15) are the sheet's. Because the defect was found through the eval truth, its fix is a **baseline change, never an
  instrument's gain**: the sheet is corrected read-free from the published key's cell shapes (never from the truth file), a
  fresh two-pass Spinelli baseline is read under the corrected sheet and scored once as the new baseline (an opening, counted;
  not a look), and until then every Spinelli instrument's paired count excludes p1c_L01.14, p1c_L01.15 and p1c_L03.25. X1c
  (the grown-sheet READ) is held on three counts: this baseline re-run, X21b, and TX-RED's review of the corrected section.
- **Audit (F19).** The register row for X21 carries the circularity caveat; the band-extent lesson is in iiif_lines.py's
  docstring. ERRORMAP's eval class counts are stale after V1/V2 and are re-run read-free (1 opening, counted) by A1.

## Amendment 5 (lane incarnation 2, 9 Oct 2026 19:5x UTC by date -u; after round 6 (X21b, A1, SC1, R3b) and TX-RED pass 4 F20-F23; written BEFORE any eval look, none spent)
- **X21b (reader model on independent truths).** dev_tune 8/6 p 0.79, dint (fresh blind Opus page pair) 5/3 p 0.73, f36v 4/2
  p 0.69; pooled 444: Opus 0.074 vs Sonnet 0.090, Opus 17/11, two-sided p 0.345 -> **null, "untested at this N on independent
  truths"; the reader rule (Opus 5.5 or Fable, never below) stands**. Register caveat (F23): both reference sequences are the
  Sonnet reconcile, so the Sonnet arm has the segmentation home advantage; the null is, if anything, generous to Sonnet, and
  "Sonnet not worse" is never read into it.
- **Prior instrument scores on eval units (F20 adopted).** "Eval looks 0" is a this-campaign count. f178r L01-03 (and
  f179r L01-03 inside eval_heldout) carry prior scores: passD (4 Oct), TX-VIEWS pilot (4 Oct, pad/s125/warp + 5-way vote),
  TX-ALTS (4 Oct), TXE-B H and TXE-B2 H2 (9 Oct, geo unit), the taxonomy error list; eval_heldout f178v L13-23 carry the
  first campaign's eval tables (read-free); Spinelli carries TXE-Q's confirm score (9 Oct) and X1b's recall table; f152r
  X1b's recall table. One line per unit now sits in benchmark-tx/txeng/units/README.md; the owner paragraph reads "outside
  both halves, scored by five earlier instruments". The crop rule those reads produced sits in the baseline both arms share;
  the units stay usable with this history stated.
- **A1 (sheet audit).** Spinelli atlas v3: 3 mislabelled exemplars (SIX p1_01_025 = ESS h; OMEGABAR p1_03_017 = OMEGADOT g;
  TEE p1_03_001 = PLUS b); atlas_v4.png (sha256 4ad8c0484ccf65c8...) built read-free, 0 mislabelled on re-cross; every other
  sheet in use is a printed-key cut or a text list (clean by construction). ERRORMAP re-run (pool 29: majority 10, split 10,
  all-same 6, minority 3). **B1 is spawned now** (PREREG-txeng2-6 B1: a baseline change, never a gain; one opening, counted).
- **Where the pool's growth comes from after B1 (F21; declared BEFORE B1's recount).** B1 may remove 3-7 of Spinelli's 12
  as a baseline change, taking the pool to 22-26; SC1 found the 1572 hand has only f.162r no.82 left (about 1 error for a
  2-2.5 build: logged queued, not worth building alone); R3b retired the f.23r re-cut. Route chosen: **(a) a second
  confirm-grade leaf built for the POOL by a separate session (TX-CONFIRM-SET's recipe, account 1: a hand with an
  independent witness, outside Birago/Ceppo/Dinteville/Spinelli/Vivonne), which keeps S2 whole** -- the ask goes to the
  orchestrator (account-4) in the lane's check-in line, since the lane cannot build it. **(b)**, a declared split of
  vivonne1573-f103r-confirm2 (lines 1-18 to the pool, 19-37 kept for S2, with S2's sentence amended to say its hand was
  touched), is the fallback only, chosen by the orchestrator, never by the lane on its own; until one of them is on file the
  under-24 rule holds whatever B1 reads.
- **R3b (F22).** Gate as declared was incomplete (no "and no cipher stroke removed" clause); the worker reached 0/16 gloss
  letters only by cutting 3-8 cipher strokes per crop and refused to call it a pass. Register verdict: "gate incomplete as
  declared; worker's reading accepted; untestable by image means; family retired for this leaf (third attempt)". The
  f.23r masked re-cut needs a person's stroke mask or another witness.
- **Overlap sentence (F23).** Both reader-model jobs measured the s1/s2 overlap far wider than the typed brief sentence
  (dev_tune about 425 px at 2x vs about 100 stated; dint 1,100-1,300 px vs 150 stated), and the Sonnet baselines A/B were
  read under the same sentence. PREREG-txeng2-7 O1 audits read-free whether the baselines' deletions and insertions sit in
  the overlap zones (dev items read-free; eval items' error positions opened read-free and counted). If they do, correcting
  the overlap sentence (M16's manifest-generated `--overlap-note`) is a **baseline change, never a gain**, and every pool
  item's baseline read under a typed sentence gets the manifest note before an instrument is scored on it (declared now).
- **S2 stays held** (C1 on file, Amendment 2 reviewed by TX-RED, both conditions met): the frozen pipeline today contains no
  instrument beyond today's, so a look now would spend the single confirm2 look on a null; it is taken when the combined
  pipeline carries at least one instrument that passed its eval look, or when the programme closes, whichever first.

## Amendment 6 (lane incarnation 2, 9 Oct 2026 20:4x UTC by date -u; after round 7 (B1, O1, H1) and TX-RED pass 5 F24-F28; written BEFORE any eval look, none spent)
- **Spinelli baseline is now passZ_v4 (B1, a baseline change, never a gain).** Under atlas_v4: passZ_v4 err_true 0.057
  (11/193) as measured, 0.047 (9/191) flagged-excluded; position errors 8 / **6** (old passZ_pipeline 14 / 12); old -> new
  fixed 8 / broken 2 (p 0.109; the 3 sheet-defect positions all old-wrong -> new-right; 3 of the 6 remaining are adjudicated
  NEW: shapes, counted wrong under TXE-Q's rule, which stands). Every Spinelli base from here is passZ_v4
  (benchmark-tx/outputs/spinelli-c1519-confirm/passZ_v4.tsv; BENCHMARK-TX notes updated); passZ_pipeline stays on disk as
  the pre-correction figure. **F27:** 0.047 is a baseline after a truth-traced sheet correction on a tuned leaf, never the
  pipeline's unseen-hand number -- only S2 is that.
- **Eval pool, flagged excluded = eval_heldout 10 + f178r 6 + spinelli 6 + f152r 1 = 23 < 24.** Amendment 3's under-24 rule
  fires again: **no eval look is possible this incarnation** unless an 0b-rule item lands (TX-POOL-LEAF, queued on account 1
  by the orchestrator at 20:3x, route (a) of Amendment 5; the confirm2 split stays the orchestrator's call after it reports).
  The branch does not move.
- **X1c:** its "reachable <= 8 of 25" rested on the old 14; X1b's recall tables are re-derived read-free against passZ_v4
  (PREREG-txeng2-8 X1b-v4) before the X1c section is rewritten, and X1c stays held (pool under 24, TX-RED review owed).
- **O1 (overlap audit).** The typed s1/s2 overlap sentence was wrong on every folio but one (measured f178v 425, f179r 375,
  f178r 350 vs "about 100 px at 2x"; dint 1,100 vs 150; Spinelli p1c 200 / p2c 145 vs "~200"; f152r 612 as stated; f87 0 as
  stated), yet the baselines' indels are NOT concentrated at the seams (pooled no.87 + dint 13 of 45 in or at a seam, at or
  under chance 0.12-0.52; dint 7/21 below half; Spinelli 2/5 below half). Consequence: the corrected per-folio sentences
  (overlap/RESULTS.md "Corrected overlap sentences") go into every future brief for these folios, and no baseline is re-read
  for the overlap alone. The eval_heldout "overlap-sentence-suspect" mark (1 of 1 indel, chance 0.37-0.45) is **withdrawn
  (F26)**: a rule firing at N=1 by construction licenses nothing; units/README carries the withdrawal beside the mark.
- **H1 (housekeeping).** ciphers/spinelli-beinecke-c1515 stays at 44 MB: every one of its 213 images is cited (benchmark
  crops, confirm item, verifier pass, sheet audit, census); the manifest (images_manifest_full.tsv) and regen_images.sh are
  on file, regen 20/20 byte-identical on the on-disk-region crops. Decision: cited crops are evidence the readers saw and
  are never re-encoded; the only route is moving the pl24/pl29 crops and debug overlays after a host-backed regen test of
  the 158 full-canvas crops, deferred to a worker with the Beinecke host allowed (not this window).
- **S2 (F28, the orchestrator's call; the lane's recommendation).** Take S2 once as the PRODUCT baseline as soon as the
  baseline-side fixes are frozen into the pipeline (manifest overlap note in the brief, a text-list or printed-key sheet, do
  not resize, sha256 before any score, verifier flags before counting), because the instrument tests cannot reach it (pool
  under 24, no instrument past dev) and holding it until one does may mean never measuring the product on an unseen hand;
  any later instrument's generalisation then needs a second confirm-class leaf (TX-POOL-LEAF or its successor). The S2 PREREG
  draft now carries that pipeline; its dated freeze line is written only on the orchestrator's decision.
