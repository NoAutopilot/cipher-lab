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

## Amendment 7 (lane incarnation 2, 9 Oct 2026 21:3x UTC by date -u; after round 8 (X1b-v4, A2, REGFIX), TX-POOL-LEAF (account 1), the orchestrator's F28 decision of 21:18 and TX-RED pass 6 F29-F32; written BEFORE any eval look, none spent)
- **gunther8246-p2 pooled (F31).** Built outside the lane by TX-POOL-LEAF (account 1): WVO 8246 MS p.2, Willem van Oranje's
  German secretary, 1561 -- a hand, office, language and key family no other item uses; truth = the Japikse 1934 printed
  decipherment (Koot) aligned over the whole letter (0.900 vs shuffled max 0.311) through a key that is **ours, grade C,
  rebuilt from the sibling letter 5109** (the dint key_print class; 0b's "period/published key" wording reads "or a key
  rebuilt from an independent printed decipherment of a sibling" for this item); 372 positions, 317 scored, 15 flagged
  align-conflict by the build before any reader was scored; baseline passZ (two blind Opus + Sonnet adjudication, committed
  before the truth was opened) 18/317 as measured, **5/302 flagged-excluded** (13 of the 18 sit on flagged positions and repeat
  by label: key gaps or encipherer's slips, not misreads). The binding count is flagged-excluded (Amendment 2): the item adds
  **5**. **Eval pool = eval_heldout 10 + f178r 6 + spinelli 6 + f152r 1 + gunther 5 = 28 >= 24: the under-24 rule lifts**
  (tuned-letter lines 16; held-out leaves 12). Power at E 28 for a clean 30% fixer at p < 0.05: between 0.827 (E 26) and 0.908
  (E 29), about 0.88. The branch p < 0.05 at >= 24 does not move. Before the first look on it: (i) a verifier pass V3 on its 15
  flags from the Japikse print and the WVO scan (PREREG-txeng2-9 V3), (ii) the readers' p.1 calibration sheet -- atlas-built,
  labelled by the committed reading, the A1 shape -- crossed read-free against the whole-letter alignment (GS1).
- **Outside-the-frame checks for pool material (the owner's rule of 20:5x; corrects Amendment 5's "the 1572 hand is
  exhausted", which named only the in-frame scout).** Named now: (1) sources/cryptiana/READABLE.tsv -- 13 Tomokiyo
  "readable with key X" leaves, key-only except Clair.330 f.85, which carries an in-volume decipherment (Gallica, after 10 Oct
  00:00 UTC); (2) sources/cyphersolver/* -- three folders unscreened for a clear copy; (3) the 21 clairambault/colbert folders
  on disk, unscreened for a period decipherment. All three are the TX-POOL-LEAF-2 screen the orchestrator queued for account 1
  at 21:18; "needs new material" is replaced by "cheapest untried step outside the frame: that screen".
- **S2 (the orchestrator's decision, 21:18: route (b)).** S2 is the product baseline on an unseen hand as well as the
  instrument test; taken ONCE as soon as the baseline-side corrections are frozen by a dated line in PREREG-txeng2-S2 (written
  now: measured overlap sentence, do-not-resize, the folder's text-list sheet, no atlas), readers blind, sha256 before score,
  a verifier pass on the item's align-conflict flags before the count; reported as "product baseline on an unseen hand",
  never as an instrument result; any later instrument gets its own eval look on a second confirm-class leaf. The reads are a
  worker's job (PREREG-txeng2-9 S2-READ, no score); the verifier is a separate session (V-VIV); the single score is the lane's,
  run once after both land, and it is the campaign's S2 look (1).
- **X1c retired (F30 adopted).** Against passZ_v4 a grown-sheet read can reach at most 5 of Spinelli's 6 errors (all five
  NEW-flagged: circle-on-stem, long-s-crossbar, looped-H), and 5 fixed / 0 broken gives p 0.0625 > 0.05 at any pool size: X1c
  cannot pass the gate even if perfect -- a non-test by construction. Register: "retired: dissolved into a sheet correction;
  max reachable 5, 5/0 p 0.0625; instrument: grown sheet from the leaf's own NEW tiles; reopen when a leaf whose NEW-flagged
  errors exceed what 5/0 can carry (>= 6 reachable at the gate in force) enters the pool". The finding is the A1/B1 shape:
  the Spinelli sheet lacks three cells the published key carries; **B2** adds them to atlas_v4 from Domnina's published table
  (never from a tile chosen through a truth position) and re-reads the baseline once (a baseline change, one opening;
  PREREG-txeng2-9 B2); Spinelli's count in the pool is replaced by B2's whichever way it moves.
- **A2 (sheet audit across every folder).** 34 sheets: the only atlas-built sheets with a truth to cross are Birago 1572's
  atlas (69 non-eval exemplars: 1 mislabelled, T64 f184v_04_009 vs S T52 -- outside every benchmark unit; handed to the
  Birago folder's own lane as a one-line note, no edit by this lane) and key no.60's (4 value-conflicts already in its own
  agreement column); 4 folders read with an atlas-built sheet and no truth to check it (debosnys, salviati, seure, gramont;
  1,107 tiles) and 2 with a truth uncrossable at box grain (fr5761, clair349). Nothing corrected.
- **Register (F25 closed).** tools/tx_register.py now parses the lane's row shapes and `--check` fails on any unparsed txeng2
  row; the one row it flagged at this check-in (txeng2/sheets-all, no Verdict line) is covered by its results-log row below.

## Amendment 8 (lane incarnation 2, 9 Oct 2026 22:1x UTC by date -u; after round 9 (S2-READ, V-VIV, V3, GS1, B2) and TX-RED pass 7 F33-F37; written BEFORE any eval look and BEFORE the S2 score, neither taken)
- **S2 (F33, BLOCKING, the orchestrator's choice (a)).** The FROZEN step 3 was not executed on the S2 reads: the adjudicator's
  first hand-back settled all 375 queued rows by rule, the one resume settled 9 of 208 disagree rows from the image, so
  passZ_S2 is pass A at 199 of 208 splits. **No score is taken on passZ_S2.** Protocol repair, dated here under the FROZEN
  section's authority and made BEFORE the score: a fresh Sonnet adjudicator in TXE-Q's packet shape (<= 16 rows per call, each
  row's crop viewed, viewed recorded per row; the 208 disagree rows, about 13 calls; the 167 agreed-uncertain rows kept as
  agreed) produces passZ_S2b.tsv (PREREG-txeng2-10 S2-ADJ; a step of the pipeline, not a read of the truth; openings 0). The
  lane's single score then runs on passZ_S2b, --exclude-flagged, both figures, and the S2 line says (F34): "flags decided from
  the two blind clerk reads, not the clerk image (TXV-VIV: 236 FLAG / 0 CORRECT / 20 KEEP; 568 of 1,068 flagged, 500 bind)";
  the as-measured figure on all 1,068 beside it; the item's next step is a verifier pass with the clerk page images after the
  10 Oct 00:00 UTC Gallica probe, never a re-score. passA_S2 / passB_S2 single-pass figures are reported beside.
- **Gunther (F35; V3).** TXV-GUN: FLAG 12 (key-gap 10, slip 1, alignment 1), CORRECT 3 (34 -> u x2, 88x -> r); recount under the
  new flags: passZ_pipeline 15/317 as measured (0.047), **5/305 flagged-excluded** (12 flagged). GS1: the readers' p.1
  calibration sheet carries 6 mislabelled exemplars (d6 -> c x2, Ib -> s, 34 -> e, xb -> a, ps -> f), the same label families
  as most of the baseline's errors -- the Spinelli shape. **B3** (PREREG-txeng2-10): the sheet is corrected from the p.1 print
  alignment (p.1 is outside the scored p.2: no opening) and a fresh two-pass baseline is read and scored once (a baseline
  change, never a gain; one opening); until B3 is on file gunther's 5 is a count under a sheet with six wrong exemplars and
  no look is spent on it.
- **Spinelli (B2; F36).** passZ_v5 (atlas_v5 = v4 + KEY_G1, KEY_U_V2, KEY_SS from Domnina 2016 Ill.1 by a blind lookup): 13/193
  as measured, 11/191 flagged-excluded; position errors 10 / **8** (v4: 8 / 6); v4 -> v5 fixed 2 / broken 4 (p 0.69), accepted as a
  baseline change whichever way it moves. F36's check: of the 8, three are the new cell names the collapse map does not fold
  (u <- KEY_U_V2 x2, s <- KEY_SS x1) -- notation under PX-BRODEC, not reads: the published cells are the u/v sign 2 and the ss
  sign. Declared: the collapse map folds KEY_U_V2 and KEY_SS to the published cells' key codes (from key.tsv's Domnina rows,
  never from the truth) and the v5 score is re-run read-free; expected Spinelli count **5** flagged-excluded after the fold
  (8 before). The worker's grep leak (truth letters beside the three shapes, disclosed before any read, lookup delegated to a
  blind subagent) is on record; the outcome went the wrong way, so it did not help.
- **Pool after this amendment:** eval_heldout 10 + f178r 6 + spinelli 8 (5 after the fold) + f152r 1 + gunther 5 (pending B3)
  = **30 (27 after the fold)**; the under-24 rule stays lifted either way; gate p < 0.05; no instrument past dev; no look is
  spent on gunther before B3.
- **Outside the frame (F37).** TX-POOL-LEAF-2 (account 1): 5 pool-grade candidates, all Gallica-held (probe after 10 Oct 00:00
  UTC); Huntington 108(A) p.1 built (luzerne108a-p1: 0/58 flagged-excluded, no headroom, not pooled). The cheapest untried
  step is that Gallica probe.
- **Hand-over.** This incarnation hands over to incarnation 3 at this check-in (context about 560k); incarnation 3 runs the
  S2 score after S2-ADJ, the notation fold and the Amendment 9 recount after B3.

## Amendment 9 (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 9 Oct 2026 22:2x UTC by date -u; after the Spinelli notation fold and B3's stop (TXE2-BASE-GUN); written BEFORE any eval look and BEFORE the S2 score, neither taken; the S2 line is added below by a dated line when the score is run)
- **Spinelli notation fold (Amendment 8, F36), run read-free.** `benchmark-tx/txeng2/basespin2/fold/collapse_map_fold.tsv`
  (B2's map + the fold rows; rule in its comment lines; the truth was not opened, nothing re-read). KEY_U_V2 folds to HOOK:
  key.tsv's u rows are EM (U/V sign 1) and HOOK_U_V, and the 28 Sept atlas map's HOOK row places U/V sign 2 in the merged hook
  family, so the cell's key code is HOOK_U_V, already collapsed to HOOK. KEY_SS does NOT fold: key.tsv carries no row with
  value ss (the keymatch passes never assigned the cell a code), so the declared rule yields nothing and KEY_SS scores as
  itself. passZ_v5 under the fold: 8/193 as measured, **6/191 flagged-excluded** (B2's map: 10 / 8; v4: 8 / 6); v4 -> v5 under
  the fold fixed 4 / broken 4, p 1.0, a baseline change either way. Amendment 8's "expected 5" assumed both names fold; the
  pool takes **6** (the rule as declared, not the expectation). BENCHMARK-TX notes: the Spinelli base is passZ_v5 scored
  under the fold map; `tools/tx_bench.py ... --label-map benchmark-tx/txeng2/basespin2/fold/collapse_map_fold.tsv`.
- **B3 stopped before any read (TXE2-BASE-GUN, 22:15): the pre-registered treatment was wrong for 4 of the 6 tiles.** The
  worker enlarged the six GS1 exemplars: d6 (p1cal_L03.16, L06.14), Ib (L05.14) and 34 (L06.17) are drawn as labelled -- the
  disagreement is between the key and the print alignment (a key gap or homophone, d6 = c / Ib = s, and an alignment or
  encipherment question at 34 = e), the same label-level patterns the build already flags as align-conflict on p.2 -- while
  xb (L08.15, a plain x, no bar) and ps (L09.14, a p with no s joined) are shape slips whose relabels to x and p fit both the
  image and the key. A value-blind sheet's labels are shapes: relabelling the four by the print's letter would teach readers
  wrong shapes. **Decision (option b): B3b** -- the sheet is corrected on the two shape slips only (xb -> x at L08.15, ps -> p
  at L09.14), the four key-vs-print tiles stay as drawn and are recorded as "shape correct, value disputed" in a sheet
  changelog (readers never see values, so nothing a reader sees changes for them), the d6/Ib/34 conflicts are handed to the
  gunther folder's own lane as a one-line key question in its NOTES.md (no key edit by this lane), and the fresh two-pass
  baseline, reconcile, packet-shape adjudication and ONE score run as B3 declared (a baseline change, never a gain; one
  opening; PREREG-txeng2-11 B3b). GS1's lesson for the brief templates: a value-level cross (key value vs print letter)
  names candidate sheet defects; only an image check of the tile decides a relabel, and the relabel is to a shape label.
  Until B3b is on file, gunther's count stays 5 under V3's flags and no look is spent on it.
- **Pool after this amendment:** eval_heldout 10 + f178r 6 + spinelli **6** (fold) + f152r 1 + gunther 5 (pending B3b) =
  **28**; the under-24 rule stays lifted; gate p < 0.05 at >= 24; no instrument past dev; eval looks 0; S2 look 0 (owed on
  passZ_S2b after S2-ADJ, PREREG-txeng2-S2 "Protocol repair", F34 clause).
- **Refill (TX-PROGRAM slot rule).** Runnable now: B3b only. Gated until 10 Oct 00:00 UTC: the Gallica probe (N1 colour
  master btv1b9060248g canvases 182-184; the fr.16105 clerk pages ff.104-108 for a confirm2 image verifier; the five
  Gallica-held pool candidates in benchmark-tx/txpool/CANDIDATES.md). Gated on material outside the lane: X2b/X2c (no
  non-pool labelled ink of the 1572 hand), E-162r (built only with other new material), the owner's sorter session on the
  boxed eval tiles (owner-side). The slot count runs below 5 while no further row is runnable; that is reported, not padded.
- **S2 look taken (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 9 Oct 2026 22:22:57 UTC by date -u; the campaign's one S2 look, count 1): one tx_bench run (benchmark-tx/txeng2/s2score/tx_bench_S2.txt, inputs hashed first in SHA256SUMS.prescore; passZ_S2b da404e35..ffe520 as committed by S2-ADJ) on passZ_S2b.tsv --paired committed.tsv --exclude-flagged, the five other files beside in the same run. **Product baseline on an unseen hand (vivonne1573-f103r-confirm2, 1,068 scored): passZ_S2b as measured 0.296 (316/1068, 95% 0.269-0.324; wrong 239, deleted 56, inserted 21); flagged-excluded 0.150 (75/500, 95% 0.121-0.184)** -- flags decided from the two blind clerk reads, not the clerk image (TXV-VIV: 236 FLAG / 0 CORRECT / 20 KEEP; 568 of 1,068 flagged, 500 bind). Beside: passA_S2 0.292 / 0.148 (74/500), passB_S2 0.302 / 0.154 (77/500); the builder's own passes (N5-VIVK) passA 0.232 / 0.048 (24/500), passB 0.246 / 0.074 (37/500); committed.tsv 0.221 / 0.032 (16/500) -- the committed reading is the stream the truth was aligned to, so its figure is a floor by construction, not a reading. Paired vs committed: passZ_S2b fixed 7 / broken 66; passA_S2 7/65; passB_S2 9/76. The two-pass + packet adjudication gave no gain over either single S2 pass on this hand (0.150 vs 0.148 / 0.154). Top confusions: c<-deleted x24, s<-d x17 (present in every file, the committed too), a<-m x7, i<-m x7, e<-d x6, u<-deleted x6. Read-free label counts (no truth): the S2 reads carry ':' 75 vs the committed 156, 'S' 0 vs 141 ('s' 81), '3' and 'V' absent with 'z' 54 and 'y' 60 present, 1,890-1,907 signs vs 2,033 -- a label-inventory and segmentation gap between the readers' sheet (txeng2/s2read/sheet_SIGNS.md) and the committed inventory, so part of the 0.150 may be notation (CLAUDE.md rule 3, PX-BRODEC): a read-free notation audit (PREREG-txeng2-12 S2-NOTE) classifies the 75 and reports a normalised figure BESIDE this line; the look stands as taken; no re-read, no second look. Reported as a product baseline on an unseen hand, never an instrument result or a gain. Next step for the item: a verifier pass with the clerk page images after the 10 Oct 00:00 UTC Gallica probe.**
- **S2 line, final form (lane incarnation 3, 9 Oct 2026 22:3x UTC by date -u; after TX-RED pass 8 F38, F39, F41; the look itself unchanged). TIMING, disclosed: TX-RED pass 8 was posted at 22:19 UTC and the lane took the score at 22:22:57 UTC having read S2-ADJ's RESULTS but not yet pass 8; F41's acceptance evidence is nevertheless on file in benchmark-tx/txeng2/s2adj/RESULTS.md and packets/: per packet 16/16 rows viewed by the adjudicators' own report with the crop files listed per reply, sides-with over the 208 splits A 97 / B 95 / a third reading 5 / NONE 11 (a rule pass-through would read A about 199, as passZ_S2 did), no packet returned as a pass-through, and every packet task text says 'use ONLY the files named here' naming the sheet, the crops and the packet queue only -- grep of the 13 task texts and the template for passZ_S2, adjud_out, committed or truth: 0 hits -- so the adjudicators were never shown passZ_S2 or adjud_out.tsv. Had the evidence failed F41 the score would have been reported only under F33's option (b) wording; it did not. THE BRACKET (F39): the frozen pipeline reads this unseen hand at between 0.150 (75 of the 500 positions where the folder's earlier reading already agreed with the clerk decipherment -- biased LOW, since the flags are that reading's own disagreements and errors sit where signs are hard) and 0.296 (316 of all 1,068 scored, including 236 the verifier calls doubtful -- biased HIGH); the committed reader's own figures on the same two sets are 0.032 (16/500) and 0.221 (236/1068), the paired line against it (fixed 7 / broken 66) draws nothing because committed is right on the 500 by construction (rule 3's cannot-differ shape); 'an unseen hand at <= 5%' is tested against neither end alone -- both ends are above it. ERROR MASS BY CLASS (F38; from the look's confusion lines and the read-free alignment of the S2 reads to the committed labels, no new opening): (i) the two-dot mark ':' (key value c) dropped -- 'c <- deleted' x24 in the look, 69 of its 156 committed occurrences missing from the S2 reads: a segmentation failure of one mark class, specific and repairable by brief and sheet for a LATER item of this hand, never for this look; (ii) the 3/z pair ('3' = d, 'z' = a; 28 committed '3' read 'z' in passZ_S2): a value error where scored; (iii) 'S' written 's' (47) and 28 brace tokens outside the committed inventory: the readers' vocabulary did not hold to FROZEN step 2's 'committed inventory' rule (s2read/RESULTS.md disclosed it), S/s on key-M positions with no score effect, the brace tokens wrong wherever scored; (iv) residue: look-alike pairs (s <- d x17 is in every file, the committed too, so a truth/key matter; a <- m x7, i <- m x7, e <- d x6). S2-NOTE (PREREG-txeng2-12) classes the 75 formally with a map built before any error is seen. FOLD RE-SCORE counted as an opening (F40): the Spinelli fold re-score is openings 1, not 0; the running total of read-free openings rises by one. The S2 number of record stays the bracket 0.150 / 0.296 as taken at 22:22:57 UTC.**
- **Amendment 9, dated additions (lane incarnation 3, 9 Oct 2026 22:5x UTC by date -u; after round 11-13 reports; written BEFORE any eval look, none spent). (1) **B3b on file (TXE2-BASE-GUN2).** Sheet corrected on its two shape slips only (00577705c, before any read); two blind Opus passes (agree 97.9%), 4 Sonnet packets (58 rows, viewed 58/58), passZ_gv2 (a9a11b91): **0.051 (16/317) as measured, 0.020 (6/305) flagged-excluded**; vs passZ_pipeline 15 -> 15 wrong, fixed 6 / broken 6, p 1.0 -- a baseline change, never a gain. Declared deviations: 4 adjudication calls (the queue shape gave 58 rows), 'do not resize' in place of the original readers' 'enlarge 2-3x' (part of the baseline change, not separable); the worker saw one data row of the old passA/adjud_out at orientation, no reader did. The gunther base is now passZ_gv2 (BENCHMARK-TX notes); its pool count is **6** (was 5 under V3's flags; the two NEW: signs and the flagged key-gap labels carry the errors, none on the relabelled tiles). **Pool = eval_heldout 10 + f178r 6 + spinelli 6 + f152r 1 + gunther 6 = 29**; under-24 lifted; gate p < 0.05 at >= 24 (power about 0.91 at E 29); no instrument past dev; eval looks 0; S2 look 1 of 1. (2) **S2-NOTE on file (TXE2-S2NOTE).** Map (s -> S, H -> #, X? -> X) from the sheet and the committed inventory only, committed before any truth view; the 75 flagged-excluded S2 errors: **notation 0 / segmentation 42 (21 deleted + 21 inserted) / read 33** (14 where the committed reference is itself wrong by the truth, 19 other); as measured 316: 0 / 77 / 239. Normalised companion **0.154 (77/500) / 0.301 (322/1068)** beside the look's 0.150 / 0.296 (the map removes no error, re-aligns three positions). The S2 baseline is not a notation artefact; the S2 line's class (iii) is corrected: the truth sets carry lowercase s themselves, so s/S was never notation. Findings for the NEXT confirm-class brief, never for this look: the S2 readers used no '3' and no 'V' though the sheet defines both; 13 committed labels (t 4, Z 4, i 2, J, w, H) are absent from the sheet. (3) **DV1 on file (TXP-VIV102): vivonne1573-f102r-dev**, split dev, built by build_vivonne_f102r.py (--check ok; truth sha256 04bb775f): 1,008 scored, 403 unflagged (605 flagged); the build's own control 0.552 vs 200 value-shuffled keys max 0.549, **a margin of 0.003** (confirm2: 0.605 vs 0.557) -- the truth on this leaf is weak; by rule 3 the item is used for flagged-excluded paired counts and failure-class work only, never an as-measured level. Baseline from the folder's own Sonnet passes: committed 0.327 / 0.000 (home advantage by construction), passA 0.330 / 0.007, passB 0.353 / 0.042. Committed label counts ':' 84, 'S' 16, 's' 112, '3' 19, 'z' 94. It carries no today's-pipeline baseline yet: **DV1b** (PREREG-txeng2-14) reads it with the S2 pipeline (two blind Opus passes, reconcile, packet adjudication) as a dev baseline, which gives the dev-side failure classes (':' deletions, 3/z, invented names) for the mark-class detector TX-RED named (strategy 2). (4) **Register.** retired.py --check's one row with no reopen condition is ciphers/na-suriname-map-1781's, not R3b (R3b's row carries 'reopen when: new material -- a person's stroke mask ...'). (5) **Owner, 22:47 UTC (hub-seed/CHECKIN-PROMPT.md):** the seven_day allowed_warning is not a reason to hold work; spawning continues at the normal cadence; a five_hour rejected still pauses it.**
- **Amendment 9, dated additions 2 (lane incarnation 3, 9 Oct 2026 23:3x UTC by date -u; after DV1b (TXE2-VIV102-BASE) and TX-RED pass 9 F43-F46; BEFORE any eval look). (6) **DV1b on file: today's pipeline on the dev leaf f.102r** (sheet_SIGNS_dv1 = the S2 sheet + 6 missing labels, measured overlap 250 px, 10 Opus reads, reconcile 86.1%, 257 disagree -> 17 Sonnet packets viewed 257/257, passZ_dv1 e5081ff0): **0.199 (80/403) flagged-excluded**; 0.431 as measured, not read as a figure (the truth's control margin is 0.003); passA_dv1 0.208, passB_dv1 0.161 (the single pass B beats the pipeline here, as on confirm2 the pipeline did not beat its passes); class split of the 80: segmentation 48 (6 deleted, 42 INSERTED), read 26, notation 6 -- on this leaf the pipeline over-segments where on f.103r it dropped the ':' mark. The readers used '3' and 'V'. DV1b answers F45 (a): the dev baseline is now a fresh pipeline read, not the reference. **Dev pool: DV1 enters conditionally at 80** (dev 37 -> 117) pending F45 (b), the anchor check DV1c (PREREG-txeng2-15); until DV1c passes, a dev gate on f.102r is reported but licenses nothing. (7) **F44, a false count corrected in the line of record:** the S2 line's final form says '3' and 'V' were absent from the S2 reads; the files say passZ_S2b '3' 22 / 'V' 36 (committed 68 / 61), passA_S2 26 / 37, passB_S2 17 / 30, 'z' 54 against the committed 12 -- UNDER-use of two defined tokens with over-use of 'z' (a 3/z value confusion where scored), not absence; the sentence in the S2 line and S2-NOTE finding 2 read so from this line on (the lines themselves are left as written, dated; this correction governs). (8) **F43:** the owner paragraph's builder-passes sentence now reads as a floor-adjacent figure by construction ('the two passes from which the reference and its flags were made'), 4 Oct not 'weeks earlier', the naming sentence superseded by S2-NOTE, 'invented' replaced by the brace-token fact. (9) **F46:** pool 29 is the dated line of 22:5x; PREREG-12 was pushed at 22:26:04 (281917d81) before its worker was created at 22:26:59 and claimed at 22:28 -- the 22:29:51 push (65b43c220) was the preamble's check-output paste, not the PREREG; the rule push-before-spawn was kept and stays. (10) **Runnable now (PREREG-txeng2-15):** DV1c the f.102r alignment/anchor check (F45 b, read-free); SH-VIV a printed-key sheet for the Vivonne hand cut from Tomokiyo's drawings on disk (TX-RED strategy 1; for a LATER item, never f.103r); GP1 the Gallica probe, spawned not before 10 Oct 00:00 UTC. The ':' mark-class detector (strategy 2) is drafted after DV1c, since DV1b shows insertions, not deletions, on f.102r: the detector's target class has to be read from a leaf whose truth is anchored first.**
- **Amendment 9, dated additions 3 (lane incarnation 3, 10 Oct 2026 00:1x UTC by date -u; after round 15 (DV1c, SH-VIV) and TX-RED pass 10 F47-F49; BEFORE any eval look). (11) **DV1c: UNANCHORED (TXE2-VIV102-ANCHOR).** By the declared gate the f.102r truth fails: control margin at the build's bounds 0.0027 (reproduced), best bounds end+1 0.0293 (under 0.03), f.103r clean at 0.0476 under every bounds choice. **DV1's conditional dev-pool entry is withdrawn** (dev pool back to 37); f.102r-dev is labelled ink only, and no dev gate counts it. The worker's post-hoc, non-gating scan: the f.102r stretch aligns best at dec_norm offset about 500 (margin 0.164-0.171 at 200 shuffles, selection-fair null 0.147), not at the registered j0 1265 (0.035) -- the N5-VIVK anchor placed f.102r's opening about 750 letters too late, and f.103r's end-anchored stretch was unaffected. A re-anchored rebuild is a NEW truth (DV1d, PREREG-txeng2-16): the existing passes passA_dv1/passB_dv1/passZ_dv1 are re-scored once against it (no re-read); DV1b's 0.199 is then a figure against a withdrawn truth and is superseded, not corrected. (12) **SH-VIV on file (TXE2-VIVSHEET):** sheet_tomokiyo_v1 covers 40 of 40 committed labels (37 from the 1574 key, c and 2 from 1580, 8 from 1588, starred); value-blind; used by no reader yet. (13) **GP1 spawned 00:05 UTC** (TXE2-GALLICA, PREREG-15). (14) **F47 adopted, the dev-gate rule for a one-hand-heavy pool, declared before any dev run on a grown pool:** every dev result is reported split per item; a dev PASS needs the pooled count AND fixed >= broken on the pool without any single item that carries more than half of it (today: the four prior items, E 37), or a pass on at least two items; an instrument whose mechanism is insertion-trimming is gated on the position-level paired count (which excludes insertions) and its PREREG says so. (15) **F48 adopted, the two-rate decomposition:** under --exclude-flagged tx_bench's err_true is (position errors at unflagged positions + ALL insertions) / unflagged positions; from now every flagged-excluded figure is reported with `position errors / unflagged` and `insertions / signs read` beside it (S2: 54/500 = 0.108 + 21 insertions on 1,907 read = 0.011; DV1b: 38/403 = 0.094 + 42 on 1,827 = 0.023); TOOL-2RATE (PREREG-16) adds the option to tx_bench with an offline test; the paired gate is unaffected. (16) **F49:** a dated pointer line in txeng2/viv102base/RESULTS.md to item (7). (17) **Runnable now (PREREG-txeng2-16):** DV1d re-anchor + rebuild + one re-score + insertion locator; TOOL-2RATE; WIT-VIV the printed-witness scout (Groen van Prinsterer IV, d'Ars: do they quote the June 1573 dispatch; IA full texts on disk / be-api, zero Gallica; TX-RED strategy 1).**
- **Amendment 9, dated additions 4 (lane incarnation 3, 10 Oct 2026 00:3x UTC by date -u; on the outside review research/SO-TX-TRANSCRIPTION-2026-10-10.md (the owner's runner, PR 71; read in full) and the orchestrator's message of 00:3x; BEFORE any eval look). (18) **The 'bracket' wording is WITHDRAWN.** The S2 line's '0.150 to 0.296' are two operational scores under two masks (truth-verifier flags dropped, 500 positions; all 1,068 scored positions), not bounds on the page's true sign error: doubtful truth can favour a prediction as well as penalise it, homophone acceptance and missing-line exclusion act downward, and charging every line insertion to the reduced denominator acts upward. From this line on the S2 number is reported as 'two scores with their masks: 0.150 on the 500 unflagged positions (54 position errors + 21 line insertions), 0.296 on all 1,068 (295 + 21)'; 'bracket', 'biased low' and 'biased high' are struck wherever the lane wrote them (PREREG-S2 final form, Amendment 9 (18 corrects 7-9), the owner paragraph, TRANSCRIPTION.md's Today cell), by dated correction, never by rewriting the look line. (19) **The scorer findings are reproduced by the orchestrator on the current tools/tx_bench.py** and adopted as a tool job, TOOL-SCORER-FIX (PREREG-txeng2-17): (1) a truth line absent from the output is not charged (lines_missing only) -- missing lines become deletions on a fixed manifest and unknown line ids fail validation; (2) paired() ignores truth flags while the headline drops them (the S2 log: paired n 1,068 vs rate n 500) -- the paired endpoint uses the same population as the rate and includes insertions (per-line edit totals, paired by line); (3) an insertion repair scores fixed 0 / broken 0 -- invisible to the adoption gate; plus the flag split (truth-verifier flags are --exclude-flagged's only meaning; reader abstention is reported as accepted-token error vs coverage, never dropped), standard unit-cost SER (S+D+I)/N on complete reference lines reported beside the 0.75-indel alignment with a ranking-sensitivity line, a --strict mode scoring exact ref_sign (visual identity) beside the value-compatible truth set, no Wilson interval on a rate with insertions (a line-level paired bootstrap, conditional on the hands, as the interval), and per-hand reporting. Old behaviour stays reproducible under --legacy. THEN a corrected audit: the FROZEN S2 outputs (passZ_S2b, passA_S2, passB_S2, the builder's passes, committed) and the DV1b outputs are re-scored with the fixed scorer -- no new reads, old outputs and old score files preserved, declared 'corrected audit of a prior look', never a new look (eval looks stay 0, S2 looks stay 1); the S2 line gains a dated 'corrected audit' line with the new figures beside the originals. (20) **ORACLE-LOCATION-1 (the review's proposed instrument) enters the register as a PREREG candidate**, drafted in PREREG-txeng2-17 as a CANDIDATE, not spawned: three hands x 12 complete lines selected by seed 20261010 without regard to errors (f.102r by the independent visual route, Birago no.87, a third hand named before sampling; f.103r excluded), a human-checked visual reference (boxes, reading order, neutral IDs; the owner's desk step, LOCAL-QUEUE L74) built WITHOUT either arm's predictions or the old reference, arm A today's pipeline with the same atlas, arm B the same plus verified numbered boxes (one ID or UNKNOWN per box; location/order/count, never identities), three repetitions per arm averaged, scored by unit-cost SER on complete lines with the fixed scorer, PASS = M_B <= 0.70 M_A AND M_A - M_B >= 0.03 AND every hand improves; a finite-set diagnostic and an investment decision, never S1/S2 certification. Desk cost: the review names no figure and none is on file; estimated 30-50 minutes per 100 signs for VERIFYING machine-proposed boxes (not drawing them), to be measured on the first 100 signs and reported before the rest is scheduled. Not started before TOOL-SCORER-FIX lands (the orchestrator's order). (21) **Order of work, the lane's call:** the scorer fix first (every binding figure on file depends on it); ORACLE-LOCATION-1 second, before the ':' / segmentation detector -- the oracle diagnostic brings verified spatial information (new information, the kind the charter ranks first) and decides whether location alone takes this reader near 5%, while the detector attacks one mark class on one leaf whose truth has just failed its anchor; the detector is drafted only if the oracle run shows recognition holds once location is given. (22) **Also from the review, adopted as rules from this line:** 'unseen hand' is reported in one of three declared regimes (no hand-specific examples / a fixed support budget from the hand / ongoing human correction) -- S2 was regime 1 with a text-list sheet; a key drawing that specifies shapes is allowed support (regime 2), a sign-to-value key is semantic information and is said so; every evaluation exposure (scores, confusion tables, verifier notes, read-free tables) is logged in the openings ledger whether or not the truth file was printed -- the 'openings' count already does this and is kept; a reused benchmark supports regression and dev claims, and a fresh confirmatory claim needs an untouched hand after model selection. TX-RED is asked to review this addition and PREREG-17 before the corrected audit is read to the owner.**
- **Amendment 9, dated additions 5 (lane incarnation 3, 10 Oct 2026 00:5x UTC by date -u; after rounds 15-17 reports (GP1, DV1d, WIT-VIV, TOOL-SCORER-FIX tool part) and TX-RED passes 11-12 F50-F63; BEFORE any eval look; the lane hands over to incarnation 4 at this check-in). (23) **GP1: Gallica answered 0 of 2** -- HTTP 403 twice at 00:08 UTC, a Cloudflare 'you have been blocked' page (an IP-level block, new since 9 Oct's altcha 403s). The N1 colour master, the fr.16105 clerk pages (the confirm2 image verifier) and the five pool candidates stay gated on Gallica; the cheapest untried step is the owner's browser (LOCAL-QUEUE L75: the three N1 canvases and the ten clerk pages as native IIIF fetches), and a cloud re-probe no earlier than 11 Oct 00:00 UTC (one request). (24) **DV1d: ANCHORED at s* = 550** (margin 0.176 / selection-fair 0.149, gate 0.03): dev2 is the f.102r truth of record (truth sha256 007a8be9a280ff44; 1,234 scored / 679 unflagged; control 0.721 vs shuffled max 0.516), the DV1 truth withdrawn and kept. Against dev2 the frozen DV1b passes read passZ_dv1 **0.124** flagged-excluded (43/679 = 0.063 position + 41/1,827 = 0.022 insertions; 0.276 as measured), passA_dv1 0.143, passB_dv1 0.096: on this hand the single pass B beats the two-pass pipeline on both leaves (f.103r 0.154 vs 0.150 was a tie; here 0.096 vs 0.124) -- a dev observation, not a reader-model verdict (X21b's null stands; the paired test against committed cannot differ). Insertions by place: 27 elsewhere, 12 on the plain-word lines L01/L34/L37, 2 at the seam (5 of 41 at the seam vs chance 0.128): the brief's [PLAIN:...] rule is a secondary fix, no crop rule, and the mark-class / segmentation instrument is first among segmentation remedies once the oracle run has reported (Amendment 9 (21)). **dev2 enters the dev pool at 84 (43 position + 41 insertion events) under F47's rule** (per-item reporting; no pooled dev PASS without fixed >= broken on the pool without dev2, E 37) and under F56's endpoint (below). (25) **WIT-VIV: a printed witness exists** -- Gachard, La Bibliotheque nationale a Paris II (1875, IA labibliothquen02gachuoft) p.428 quotes the June 1573 dispatch (a search result, rule 10). It is anchor material for the f.102r/f.103r truths (a later read-free check of dec_norm against the quoted passage), never applied by this lane. (26) **TOOL-SCORER-FIX, tool part landed** (6896cf0e7: fixed manifest, unknown ids exit 2, --coverage-diagnostic, paired per-line edit totals with the position McNemar beside, abstentions wrong + accepted-token error / coverage, standard SER beside the 0.75 alignment, --strict, --ci line bootstrap, macro mean, --legacy byte-identical to the S2 and DV1b score files; review faults 10/10 FAIL old, 16/16 PASS new). The corrected audit is HELD for SCAN-103 (running); it also re-derives, under drop_flagged, every paired cell on file for the baseline changes (B1 8/2, B2 2/4, fold 4/4, B3b 6/6 -- TX-RED F55: Amendment 2's binding convention was never implemented in paired(); no gate verdict rests on it, eval looks 0). (27) **TX-RED passes 11-12, adopted as rules from this line:** every headline error figure carries 'value-level' until a visual-ID truth exists, and where a visual atlas is the key (Spinelli, gunther) a visual-ID score is reported beside by scoring the atlas code (F53; a read-free job for the successor); **the S1 endpoint becomes line-level edit totals (S + D + I over complete lines) with a paired test at the line level inside each hand and per-hand + hand-macro reporting, declared now before any instrument runs; the position-level sign test stays a diagnostic** (F56, F59); the next PREREG that gates quotes the noisy0.1 power beside the clean one (F62); a packet-adjudication job commits its tool-call file-access log, not only 'viewed = yes' (F63, worker template); 'unseen hand' is said with its regime -- S2 was a hand this lane had never read, with a shape-only text list as support, no hand-specific examples, on an item the folder had read in October (F61); F57/F60 are in the tool; F58 is done (18); F50 is SCAN-103; F52 noted (worker template: never print a result JSON whole). (28) **Hand-over.** Incarnation 3 hands over at this check-in (context about 620k): the successor runs the corrected audit after SCAN-103 under the orchestrator's decision rule, the F55 re-derivation, the F53 visual-ID companion scores, ORACLE-LOCATION-1's final registration once L74 is answered, and the HTRbyMatching / DTLR reachability probe TX-RED named (pass 12 strategy 1).**
- **Amendment 9, dated additions 6 (lane incarnation 4, session_01GukpgU1yBAfju3zg6g8ayG, 10 Oct 2026 01:0x UTC by date -u; after the hand-over of 00:5x and the in-session jobs of PREREG-txeng2-19; BEFORE any eval look, none spent; SCAN-103 still running).** (29) **Lineage depth.** Incarnation 4 sits at depth 8 and can spawn, re-arm and hand over nothing; the orchestrator's rule of 00:5x (research/TX-PROGRAM.md "Lineage-depth rule") governs from here: every incarnation is created by the orchestrator from its own session; this one is woken by an orchestrator-armed hourly routine, runs read-free script jobs itself (PREREG-txeng2-19, each a job the lane already ran in this campaign's shape, as PREREG-S2 had the lane run the single score), and names any worker as a WORK-QUEUE TX-* row for the account-4 dispatcher. (30) **F55 re-derived (txeng2/f55/):** under drop_flagged with the fixed scorer B1 8/2, B2 2/4 and the fold 4/4 are unchanged; **B3b is 4/4, not 6/6** (gunther's two flagged positions carried one fixed and one broken event each; p 1.0 either way; pool count 6 unchanged, it is the position-error count). Line-level (the S1 endpoint): B1 4 improved / 2 worsened, p 0.69, 14 -> 9 edits on 191; B2 3/3; fold 4/3; B3b 2/3 -- no baseline change moves lines at any p below 0.68. A note of record: the Spinelli fold's "8/193, 6/191" are position counts; the standard SER on the same files is 11/193 = 0.057 / 9/191 = 0.047 (3 line insertions). (31) **F53 companions (txeng2/compvis/):** the Spinelli base passZ_v5 reads **0.068 visual-ID (13/191) beside 0.047 value-level** under the fold map and the flagged-excluded mask (4 positions credited through a shared value; passB_v5 0.058 / 0.037); gunther passZ_gv2 **0.020 / 0.020** (6/305 both). Every headline from here carries 'value-level' with the visual figure beside where it exists; on both items ref_sign is the committed reader's atlas code, so 'visual identity' there means that reader's code, 0 for committed by construction -- the oracle diagnostic's frozen atlas is the visual reference proper. (32) **PROBE-R7:** a released detector is reachable in principle (git clone answers; raw READMEs 200; checkpoints on Google Drive, one more request to confirm a download; github.com HTML and API 403 through the proxy); idea 56 DET-RELEASED queued behind the oracle reference. (33) **ORACLE-LOCATION-1's manifest is committed** (txeng2/oracle1/manifest.tsv, sha256 d12f6cd9d3afb04d625a636ebeeab6cad8d69f9d1971abd1168fc8862172d513, 4cc8017d9): f.102r 12 of 37, no.87 12 of 29, the third hand **luzerne108a-p1** (all 11 lines; chosen over Ceppo f.21v, whose line crops are not committed, and gunther, whose 0.020 leaves no room for the 0.03 absolute condition), seed 20261010, every candidate crop on disk, nothing excluded; LOCAL-QUEUE L74's precondition is met; the final registration (reference protocol, arms, scoring, PASS rule as PREREG-17) is appended to PREREG-19 once L74 answers with the minutes per 100 signs. (34) **Outside experimenter (owner, 00:5x; TX-PROGRAM):** each landed [SO-TX-EXP-<id>] PR gets one register row with campaign=external after PR-LAND copies it to benchmark-tx/ext/<id>/; an eval or confirm score it needs is run once by the lane under the lane's look budget. (35) **CA-S2 stays HELD** for SCAN-103 (claim 00:39, box to 01:19); the decision rule is unchanged.
- **Amendment 9, dated additions 7 (lane incarnation 4, 10 Oct 2026 01:1x UTC by date -u; after SCAN-103 and CA-S2; BEFORE any eval look, none spent).** (36) **SCAN-103: NOT BEST** (txeng2/scan103/RESULTS.md, TXE2-SCAN103 1.53): registered 6655 real 0.6049, selection-fair margin 0.0267 (< 0.03); best 6500 real 0.6139, margin 0.0357; 155 letters apart on a flat plateau (6200-6650), the registered point beating every shuffled key everywhere and reproducing the build's control -- unlike f.102r's ~750-letter miss, a near miss of the gate. The orchestrator's rule applies: **RE103** (PREREG-txeng2-20; WORK-QUEUE TX-RE103 for the dispatcher, cap 6) builds a NEW item vivonne1573-f103r-confirm2-s6500 read-free at offset 6500 by build_vivonne_confirm2.py --start (the DV1d shape), old truth and item untouched, and re-scores the six frozen S2 files ONCE against it with the fixed scorer; look count unchanged. (37) **CA-S2 on the existing truth is on file** (txeng2/scorerfix/RESULTS.md "Corrected audit", 01:12:46 UTC, one run_audit.sh): the figures of record reproduce (0.150 / 0.296, value-level); standard unit-cost SER beside 0.134 (S 37 D 19 I 11) / 0.288; lines missing 0; the line-level paired test vs committed 0 improved / 23 worsened / 13 tied on the 500 (edits 16 -> 67), position McNemar 1 / 39 (the old 7 / 66 was the 1,068 population) -- the cannot-differ shape; `--strict` on confirm2 is agreement with the committed reader, not a visual-ID score (0.130 / 0.127), and is no figure of record. DV1b against dev2: 0.124 (84/679) reproduced, SER 0.118 (S 35 D 9 I 36); passB 0.096 / 0.087 stays the best single pass. The S2 sentence is unchanged; the owner paragraph and TRANSCRIPTION.md's Today cell carry the corrected-audit figures beside the look from this line on. (38) Openings this incarnation so far: Spinelli 1, gunther 1 (F55/COMP-VIS), confirm2 1 (CA-S2), dev2 1 (CA-S2); eval looks 0; S2 looks 1.
- **Amendment 9, dated additions 8 (lane incarnation 4, 10 Oct 2026 01:2x UTC by date -u; TX-RED pass 13 F64-F67 and the orchestrator's two binding decisions of 01:1x; BEFORE any eval look, none spent; before any annotation of the oracle manifest).** (39) **F64: the existing f.103r truth stays the truth of record.** SCAN-103's NOT BEST is a window-slack and grid artefact on a truth weakly supported at every offset of its plateau (fair margin about 0.03, against 0.149 for the re-anchored sibling), not an anchor error; CA-S2 (37) is the corrected audit of the one look; TX-RE103 (session_01LpVC17SHaMND2FjAvtq9Xm, spawned by the orchestrator 01:15) runs as a declared SENSITIVITY CHECK beside the record (item -s6500, split "sensitivity", never pooled, never of record; a 155-letter shift of a weakly supported truth, never a large correction); the F50 rule is amended in PREREG-20 (a rebuild of record needs a fair-margin difference above the scan's adjacent-offset swing at equal slack). **The open question of record is the S2 truth's own support, tested clerk-independently by WIT-GROEN** (PREREG-19 addendum: Groen IV pp.90*-91*, the closing passage from another manuscript copy, vs dec_norm's end; run in-session). (40) **F67 / F66: the oracle manifest is redrawn** -- no.87 from the dev_tune unit f178v_L01-L12 only (the first draw spent 7 eval-pool lines; superseded before any annotation), luzerne108a-p1 split eval -> dev by a dated line (0 pool errors; pool 29 unchanged); L74 resumes on the recommit. (41) F65 noted for the lane's part (the external register row records the repository-side grep). (42) Pool and gate unchanged: eval 29, dev 37 + 84, p < 0.05 at >= 24, eval looks 0, S2 look 1.
