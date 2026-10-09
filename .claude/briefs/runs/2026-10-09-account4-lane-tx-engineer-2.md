# LANE TX-ENGINEER-2 (campaign, second run; owner's decision 9 Oct 2026 ~15:00 UTC): 10-15 more pre-registered experiments on the transcription pipeline, set up so that a success would be genuine

Written by orchestrator (account-4) session_01VQDEedJCaaN7fFPGcNPUUD at 15:1x UTC 9 Oct 2026 (by date -u). Lane orchestrator model:
Fable (`claude-fable-5-1`); workers Fable or Opus 5.5 (never below; Sonnet only where the thing measured IS the Sonnet reader).
Cap: the account-4 usage window (150 of usage; the only stop is the window itself -- five_hour `allowed_warning` past one
check-in or `rejected` pauses spawning until the reset, BUDGETS.md). Box: open-ended; hand over to a successor incarnation at
~700k context (create_session, depth +1, this brief first in the prompt). Address every ROOM line "for orchestrator (account-4)";
check in with your own send_later (30-45 min) and keep a "LANE TX-ENGINEER-2 handoff" section in STATUS.md current from the first
result. Lane rules: `.claude/briefs/parent.md` "Keep slots full", `.claude/briefs/README.md` common tail,
`.claude/briefs/transcription.md`, `TRANSCRIPTION.md`, CLAUDE.md Usage 6 and rule 3. Ledger every worker (cost by get_session),
archive each; never AskUserQuestion; never print credentials; stage by path; never force-push; never edit a *.truth.tsv except
through a build script whose truth comes from the key and the known text (TXE-T's flags went to a verifier, never to the lane).

## What the owner said (9 Oct 2026, after the first campaign's report)
"Point Fable at the results, and ask it to iterate 10-15 more experiments, and just keep going. Make sure it knows what
success means and the experiment is set up to be genuine success, not a failure of our setup." Read first, in this order:
research/TX-ENGINEER-2026-10-09.md (the first campaign's result), research/TX-IDEAS-2026-10-09.md (23 ideas, every number),
research/TX-TAXONOMY-2026-10-09.md, benchmark-tx/PREREG-txeng-2.md and -3.md, TRANSCRIPTION.md (the "No.87 truth verification"
table: 11 flags upheld, 2 truth corrections applied, `tx_bench.py --exclude-flagged` prints both figures), the first brief
`.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer.md` with Amendments 1-2, and the STATUS.md "LANE TX-ENGINEER handoff"
close-out (the retired families and the open items).

## Why the first campaign could not have succeeded as set up (the orchestrator's reading; verify it in round 0)
The first campaign scored 23 instruments on units where today's reading already errs on 15 of 376 held-out signs and 14 of 343
dev signs (9 of 338 with the upheld flags excluded), under a paired sign test at p < 0.01. A sign test at that level needs about
7 fixed with 0 broken, 10 with 1, or 12 with 2: an instrument that removed a third of the remaining errors cleanly (5 of 15)
could not pass, and one that removed half (7 of 15) passes only if it breaks nothing. CLAUDE.md rule 3 names this shape: a
control (here the baseline) already near ceiling has no headroom to show a gain, whatever the technique. So most of the first
campaign's FAIL rows are non-tests of the instruments at that N, and the campaign result is "no instrument was large enough to
show on 15 errors", not "no instrument helps". The product the owner needs is a pipeline that reads an unseen hand at 5% or
better: today an unseen hand reads at 0.088 (Spinelli, 17 errors in 193) and the live letters at err_2reader 0.13-0.25. That is
where the headroom is, and that is where a gain has to be measured.

## What success means (fixed before any experiment; copy it into PREREG-txeng2-0.md and never loosen it after a result)
S1 (primary, the owner's number): held-out per-sign error, measured against a known answer on a pool of leaves the readers never
   tuned on, is lower under the new pipeline than under today's (two blind passes + reconcile + relabels + follow-slope crops),
   with paired fixed > broken at the pre-registered p, on a pool big enough that a 30% relative reduction is detected with
   >= 80% power. Report both figures (as measured, flagged-excluded) and the sign count: "N more signs right per 1,000".
S2 (generalisation): the same pipeline, frozen, scores on ONE confirm item built by a separate session on a hand the lane never
   touched (TX-CONFIRM-SET-2, account 1), looked at once at the end; that number sits beside S1 in the headline.
S3 (application): the frozen pipeline run on one live unread letter (Birago 1572 f.117r/f.144r/f.168r, or Spinelli's unread
   passages) under the folder's own PREREG and power control: "the key now licenses N more tokens at grade S, judge not worse".
S4 (the sorter product, secondary): a read-free doubt list that holds >= 70% of the remaining held-out errors at <= 15% of
   positions flagged (TXE-O reached 9/15 at 6% and 11/15 at 18%); plus a measured value curve: with an oracle standing in for
   the owner, how many sorter decisions take a leaf from today's error to 2% (read-free, from the benchmark).
S5 (cost): cost per 100 signs at equal error, reported per experiment (TRANSCRIPTION.md target 8).
A result counts only on S1 or S2; S3-S5 are reported beside it. Nothing moves TRANSCRIPTION.md's "Today" column but S1/S2.

## Round 0 (cap 15): make the measurement able to say yes -- before any instrument
0a. Power audit (tools/tx_power.py, --help, offline test): for every unit and pool on disk (dev_tune, eval_heldout, geo, the
    Spinelli confirm item now spent as confirm and reusable as an eval item, dint-f128-print, ceppo-f21v-S, ceppo-f87-S, the
    f36v gloss), simulate 1,000 instruments that each fix a random 30% (and 50%) of today's errors and break none, and 1,000 that
    fix 30% while breaking signs at the base error rate x 0.5; report the share that pass the paired sign test at p 0.01 and
    0.05. Then the same for pools. Write the table into benchmark-tx/PREREG-txeng2-0.md. The gate the campaign uses is the
    weakest (unit, p) at which a clean 30% fix passes >= 80% of the time; if no pool on disk reaches that, round 0 builds one.
0b. Headroom pool: build known-answer items until the held-out pool carries >= 60 baseline errors under today's pipeline, from
    hands where today's error is 8-25% (that is where the owner's problem lives), with truth from a period/published key and a
    known text exactly as build_birago87.py / build_spinelli_confirm.py do (never from a reader, never from an S-graded decode of
    the same passes). Candidates, check prior_work.py and the folder NOTES first: the Florence c.111/c.127 glossed lines
    (TRANSCRIPTION.md names them), the fr.3252 f.36v gloss beyond line 1 (F36-GLOSS bands), Birago 1572 letters with a clear
    copy or gloss other than no.87, fr2980-gramont and colbert26 where a sign-level alignment to the interlinear key holds, the
    Spinelli filza's other passages with the published key, Ceppo S-tokens only as dev. Two blind passes of today's pipeline on
    each new item give the baseline. Each item: a `split` (dev / eval), sha256 of the truth, its baseline error with CI, in
    BENCHMARK-TX.tsv. Readers never see truth. An item's hand is in one split only.
0c. The gate's own controls, pre-registered and run before experiment 1: (i) positive control -- a planted instrument that fixes
    30% of baseline errors at random (script, no reader) must pass the chosen gate in >= 80% of 1,000 draws; (ii) negative
    control -- a no-op and a random-perturbation instrument (change 3% of positions at random) must pass in <= 1% / <= 5%; (iii)
    the two-sided check that a 30%-worse instrument fails. If (i) fails the pool is too small: go back to 0b; the gate is never
    moved after an instrument's result is seen.
0d. Error map on the new pool: tools/tx_taxonomy.py over the baseline passes, plus the first campaign's missing column --
    reader agreement on errors (same wrong sign across readers and presentations) -- so a family whose errors are "every reader,
    every presentation" is not re-attacked by another presentation. ROOM line: pool size, baseline errors, the gate, the three
    control results, the top three error classes with mass.

## Rounds 1-N (cap: the window): 10-15 experiments, one PREREG each, worked by expected gain per cost
Ideas register v2, research/TX-IDEAS-2-2026-10-09.md: at least 15 ideas, each with mechanism (from 0d), cheapest test on the
dev pool, cost, the gate from 0a, and status; re-ranked as results land; every negative with its numbers. Rules: (1) tune on
dev, one eval look per experiment, counted in the register (with 15 experiments some will "move eval" by luck: the p from 0a is
per-experiment, and the campaign's final claim is made on the combined frozen pipeline at the same p, one look); (2) no
experiment re-runs a family the first campaign retired for this hand (compare/exemplar layouts, feature-first vocabulary, plain
re-passes at scale or under rendering, the lattice as a blanket fixer) unless it is a genuinely different instrument -- say what
is different in the PREREG; (3) an experiment that fails its own gate three times with real fixes between is retired (rule 3);
(4) every instrument is a tool in tools/ with --help, an offline test, a tool_shelf.tsv row and a SYSTEM.md row (system_map_check
passes); (5) a reader never sees truth, decodes or other passes; (6) crop step mandatory and pasted, one page per subagent call,
price per pass, reconciliation a priced unit (Usage 6); (7) Gallica answered 403 all of 9 Oct: nothing Gallica-bound before
10 Oct 00:00 UTC except one probe then.
Seeds the orchestrator offers (take, reshape or discard; the register is yours), aimed at the classes the first campaign found and
at the unseen-hand headroom:
- Sheet inventory as the instrument: a read-free off-sheet detector (tile far from every exemplar of the hand's sheet) and a sheet
  that grows from the hand's own tiles before reading; measured on Spinelli (8 of 14 errors off-sheet) and the new items.
- Key and lexicon in the loop beyond bigrams: a word-level lattice decode (tools/segmenter.py + an era lexicon of the letter's
  language + key_decode_lattice) over a WIDENED lattice (reader alternatives + atlas top-3 + confusion pairs), with the read-free
  truth-in-lattice share measured first (27/97 today) -- a fixer only at positions the doubt detector flags, never blanket.
- Pair classifiers from known answers: for each look-alike pair (d/s, p/t, n/e, h/l) a small classical classifier (HOG or pixel
  features, logistic/kNN) trained on the family's known-answer tiles, leave-one-leaf-out, applied only at the pair's positions;
  different from MQS-CLASSIFY-ROUNDS (whole-inventory top-1) and from the compare layouts (no reader sees an exemplar).
- Calibrated sign-level confidence from the reader (top-3 with probabilities per sign), scored by calibration before use, then
  as lattice input at flagged positions only.
- Reader diversity with a learned weighting: readers that differ in crop set, scale and model, combined by per-reader-per-sign
  confusion weights learnt on dev (TX-VIEWS tested a plain majority; this is not that).
- The sorter value curve (S4): simulate owner decisions with the truth as oracle, cluster-propagated through the family atlas,
  and report decisions-to-2% per leaf; and the doubt detector re-tuned on the bigger pool.
- Same-sign retrieval: for a doubtful tile, every other occurrence of the candidate signs on the same page shown as a strip
  (no exemplar from elsewhere) -- test whether it is the compare family's pull or the exemplar's source that hurt.
- Cost: per-sign tiles in one call per line vs one call per page vs per cluster sheet, at equal error (S5).

## Stop and report
Stop at the window, or after 15 experiments plus the final combined pipeline; never because three in a row did not move (that
stop rule was the sterile one). Final: STATUS.md handoff table experiment | dev (paired, p) | eval (paired, p, looks so far) |
verdict; RESULTS in research/TX-ENGINEER-2-2026-10-09.md with one plain-language paragraph for the owner (what success was
defined as, whether it was reached, on how many signs, what he should do at the sorter) and the S1-S5 numbers; TRANSCRIPTION.md
"Today" column moved only on S1/S2; a LEARN line for the brief templates. The orchestrator reports to the owner only from that
file, in the OWNER REPORT FORMAT, when he asks.

## Amendment 1 (orchestrator, 9 Oct 2026 17:2x UTC, on the owner's decision to continue as a standing programme)
The owner continues this as the project's biggest challenge, with up to 10 recurring sessions on it, refilled as others close,
a shared memory of what was tried and failed, and an adversarial reviewer outside the lane. research/TX-PROGRAM.md is the
charter; this lane is slot 2. Changes to this brief: (1) keep 5-7 experiment or build workers live while the register has a
runnable row, refilling at every check-in (never below 5 while the window allows); the stop rule stays the window, not a count
of nulls. (2) `research/TX-REGISTER.tsv` (tools/tx_register.py, being built by TX-REGISTER) is the one memory: regenerate it at
every check-in, and from the moment it exists every new PREREG carries a "Nearest prior" line naming the register ids it is
nearest to and one sentence of what is different (`tools/tx_register.py --check PREREG.md` passes before the experiment
spawns). (3) TX-RED (brief 2026-10-09-account4-tx-red.md) reviews every PREREG and RESULTS and posts "flag for LANE
TX-ENGINEER-2 and orchestrator (account-4)" lines: answer each finding in research/TX-IDEAS-2-2026-10-09.md (adopted / rebutted
with the number / deferred with the reason) by your next check-in; a blocking finding on a running experiment pauses its eval
look until answered. (4) The strategy question TX-RED will press: the error mass that every reader gets wrong the same way
cannot be fixed by re-weighting, re-ordering or re-presenting the same passes; experiments that bring NEW information (a
better image, a sibling leaf, the key's own marks, the owner's tiles, a different segmentation) rank above those that do not,
at equal cost. (5) Your ROOM check-in line now also names: workers live / slots free, register rows added, red-team findings
open. Everything else in this brief stands (S1-S5, the gate, one eval look per experiment, the confirm2 item untouched).
