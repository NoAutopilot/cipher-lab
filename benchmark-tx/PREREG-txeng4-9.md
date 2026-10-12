# PREREG TXE4-9 CALIB (account 3, Fable 5.1 worker, session_01QfCyHvk7BBL8CgqTie3s5n, 12 Oct 2026 00:2x UTC by date -u; pushed BEFORE any read or score)

One of ten TXE4 experiments the account-3 parent launched on 12 Oct 2026 (brief `.claude/briefs/runs/2026-10-11-acct3-txe4-9.md`,
commit 93ecd72da). Question: does showing a reader its own wrong labels on two known-answer pages of the same hand make it read a
third page of that hand better than the same reader given the same two pages and its own read of them without the corrections?
Rules: the brief's common TXE4 rules R1-R10 bind. Readers blind (brief text + crops + their own calibration read + for arm F the
feedback file; no key, no truth, no other pass, no repository path); every reader output committed with its sha256 BEFORE any
score (benchmark-tx/txeng4/9/SHA256SUMS.prescore); no *.truth.tsv touched; the frozen confirm items never opened; nothing
published, nobody contacted. Truth and flags are opened only by tools/tx_bench.py (scoring) and by the new tools/tx_calibrate.py
`feedback` subcommand (which imports tx_bench.align and reads ONLY the two calibration items' plain truth files, never f.89's).

## Hypothesis
H1: on dint-f89-gloss, the arm F read (calibration crops + own calibration read + feedback on its own wrong labels) has fewer
unit-cost edits (S+D+I, tx_bench standard SER numerator) than the arm C read (identical context without the feedback), by the
gate below, in both passes, and the confusion pairs the feedback named fall.
H0 (a result): it does not; the extra context and extra examples of the hand, not the content of the feedback, explain any change,
or nothing changes at this N.

## Nearest prior (register rows) and what differs from them
- `txeng2/dint-f89-gloss`, `txeng2/dint-f98v-gloss`, `txeng2/dint-f113-gloss` (TXP-D89/D98/D113, 9 Oct 2026): built the three
  items of this hand and read each ONCE with two blind Opus passes + adjudication; no reader ever saw a known answer of the hand.
  Here Sonnet readers see two of the three items with their answers' consequences (own wrong labels only) and are scored on the
  third; the Opus figures (passA 0.079, passB 0.121, passZ 0.042 on f.89) are beside only, never a gate.
- `M17` (TXE-H pair hints, benchmark-tx/txeng/hints/RESULTS.md, dev-FAIL p 0.057): hints derived from TILE STATISTICS of other
  leaves were put in the brief; 7 of its 11 fixes were on a pair the hints never covered. This differs in the SOURCE of the
  hint: the reader's own confusions on known pages of the same hand, not a statistic over tiles; and in having a context-matched
  control arm (C) rather than a plain pass as the comparison. M17 is dev-FAIL, not retired; no retired instrument is re-run.
- TXE3-4 CALIB (benchmark-tx/txeng3/4/RESULTS.md, NULL): err_2reader does not predict err_true because the agreed-wrong rate is
  a property of the hand (0-16%) that no second reader sees; only a known answer in the same hand reaches it. This job uses
  such a known answer (two other pages of the same hand) as the instrument, which TXE3-4 could not.
- TXE3-3 CROSSHAND (benchmark-tx/txeng3/3/RESULTS.md, VERIFY.md): the real misreads on gunther were one reader's own (ro/b,
  g/phi/q, v/r), not shared; feedback on a known page can target exactly those. This job is the reader-side form of the
  critics' adjudicator-calibration item; RESULTS also say whether the same feedback files could calibrate an adjudicator.
Retired instruments named in R4 (':' mark rule, transcribe-and-decode crossword, look-alike pass as accuracy, exemplar compare
layout, M24 feature-first, err_2reader as predictor) are not used; the look-alike pass is not run.

## Fixed inputs (frozen now; nothing below changes after a number is seen)
- Label table: the one in `benchmark-tx/txeng2/dint-f89-gloss/blind_pass_brief_f89.md` (check 1 diffs it against the f98v and
  f113 briefs' tables; the three table bodies are byte-identical by `diff`, run 00:2x UTC, result repeated in RESULTS).
- Calibration items (truth is a TOOL INPUT, never scored, never shown to a reader): dint-f98v-gloss, crops
  `benchmark-tx/txeng2/dint-f98v-gloss/crops/read/f98v_L0?_s?.jpg` (6 lines x 2 overlapping segments, 1400 px wide at 2x, 53
  scored, 0 flags) with truth `benchmark-tx/dint-f98v-gloss.truth.tsv`; dint-f113-gloss, crops
  `benchmark-tx/txeng2/dint-f113-gloss/crops/f113e_L02.jpg, f113_L03/L05/L07/L09.jpg` (5 whole-line crops, 81 scored, 55
  align-conflict flags -> 26 unflagged scored positions give feedback) with truth `benchmark-tx/dint-f113-gloss.truth.tsv`.
  Plain truth files only (never -kp / -kp2). Flagged positions give NO feedback.
- Target (scored once per output): dint-f89-gloss, crops `benchmark-tx/txeng2/dint-f89-gloss/crops/f89_L01..L14.jpg` (14 lines,
  1290 px, 240 scored, 102 align-conflict flags -> 138 unflagged). Its truth is opened by tx_bench only.
- Readers: Sonnet (claude-sonnet-5) subagents in fresh contexts, one per call; each gets a scratch directory with copies of its
  files only (task.txt, the crops, and for call 2 calib_read.tsv and, arm F only, feedback.tsv); no repository path in the task.
- Call 1 task text: the f89 brief's general rules and label table + the f98v brief's crop notes (segment overlap 200 px at 2x,
  prose before L01's run and after L06's) + the f113 brief's crop notes (prose positions), output `passage pos sign_id alt conf
  note` with passages L01..L06 (f98v) and f113e_L02, f113_L03, f113_L05, f113_L07, f113_L09.
- Call 2 task text (arms F and C): the f89 brief VERBATIM, preceded by one paragraph saying the reader first read two other pages
  of the same hand (crops in calib/, its own read in calib_read.tsv) and, in arm F only, that feedback.tsv lists the positions
  where its own labels were wrong with the labels that were allowed there, to be studied against the calib crops before reading
  f.89. Arm C's paragraph says nothing about corrections. Output follows the f89 brief's format (passage L01..L14, CLEAR rows).
- tools/tx_calibrate.py (new; offline test tools/tests/test_tx_calibrate.py): `build` writes call 1's file list and task;
  `feedback` aligns the call-1 read to the calibration truth with tx_bench.align (G 0.75, truth sets, same as the scorer) and
  writes one row per wrong UNFLAGGED scored position: item, line, the reader's own label sequence with 3 neighbours each side,
  `[your label -> allowed labels]` (labels only, never a letter or key value); a deleted scored position is `a sign missed here`
  with the allowed labels; an output sign aligned to no reference position is `extra sign here`; `target` assembles call 2 (F or C).
- Normalisation before scoring f.89 outputs (the committed convention of outputs/dint-f89-gloss/pass*.tsv, RESULTS.md "Dots
  dropped"): drop CLEAR rows and '.' rows, prefix `f89_`, renumber pos; committed as `benchmark-tx/txeng4/9/norm.py`.

## Arms
- F: call 2 with calibration crops + own call-1 read + feedback.tsv + the 14 f.89 crops.
- C (control): call 2 with calibration crops + own call-1 read + the 14 f.89 crops, no feedback.
- 2 independent passes (pass 1, pass 2): each pass = one call 1 (its own calibration read and feedback) + one 2F + one 2C, 6 calls.
- T0 (a plain f.89 read with no calibration, one per pass): BESIDE only and only if both the time and the estimate are under 80%
  of their lines when all six calls are done (see stop rule); never part of the gate.

## Endpoint
PRIMARY: unit-cost edits (S+D+I, unit-cost Levenshtein on the 240 scored positions, tx_bench's `ser_errors`) of each arm's
normalised f.89 output, as measured, mean over the 2 passes. Reported on both masks (as measured; flagged excluded, never alone),
with err_true (0.75-indel) and Wilson 95% from the counts, --strict beside, S/D/I beside, from
`tools/tx_bench.py --item dint-f89-gloss --exclude-flagged --strict --ci [--json]`, and `--paired` 2F vs 2C per pass (C as BASE).
SECONDARY: the transfer check (below); call-1 calibration accuracy per pass (the feedback row count, tool output, no truth shown).

## Gate (the brief's, word for word)
PRIMARY: each arm's mean unit-cost edits over its 2 passes. Calibration feedback is adopted if all of these hold:
- mean(C) >= 1.2 x mean(F) as measured;
- the gap > the maximum within-arm pass spread;
- the flagged-excluded direction does not reverse;
- the transfer check: in each pass, the confusion pairs named in that pass's feedback occur less often in F's target read than in
  C's, in both passes. Use pair counts from tx_bench's top confusions, or --pair if TXE4-6 has landed it.
Otherwise the result is 'not distinguishable'.
Operational definitions, fixed now: "gap" = mean(C) - mean(F) in edits; "within-arm pass spread" = |pass1 - pass2| edits within
F and within C, the larger of the two; "direction does not reverse" = mean(C) - mean(F) on the flagged-excluded mask is > 0;
"confusion pairs named in the feedback" = for each feedback row at a calibration position, the pair (plain value of that truth
position, the reader's wrong label); its count on f.89 is the tx_bench `top_confusions` entry `value<-label` (--json, --top 999)
of the arm's normalised output; the per-pass sum over the pass's pairs must be STRICTLY smaller in F than in C (a tie, including
0 vs 0, fails the check). TXE4-6's --pair has not landed at this PREREG's time (no `--pair` in tools/tx_bench.py), so the
top-confusions route is used. The gate is applied by the committed script `benchmark-tx/txeng4/9/score.py`, once.

## Control and why it can vary
Arm C gets identical calibration crops and its own calibration read in the same context, without the corrections. That isolates
the content of the feedback from the extra context and the extra examples of the hand; its edits vary freely (nothing in C's
construction ties its edit count to F's: separate calls, separate contexts, the same images). The transfer check can fail
differently from the edit total: a generic gain would show in the total without a fall in the named pairs; a fall in the named
pairs with no total gain would show the feedback moved only what it named. Declared limits: the gloss is visible on f.89, so the
absolute level is an upper bound on shape reading and the gate is per item; dev item; Sonnet readers.

## Units, order, cost and stop rule
U1 tool + offline test (30 min). U2 checks: label-table diff; read-free power of the transfer check = how often the label pairs on
which the committed f98v and f113 passA/passB split occur in the committed f89 passA/passB (no truth) (15 min). U3 pass-1 call 1;
U4 feedback build; U5/U6 pass-1 2F and 2C (parallel); U7 pass-2 call 1; U8/U9 pass-2 2F and 2C (parallel). Each reader call is
one unit at about USD 0.5 and 8 minutes. U10 commit reads + sha256, score once, RESULTS, LEDGER, ROOM (10 min).
Box 00:19-02:19 UTC (claim); no unit starts after 01:55 UTC. Running estimate = Fable floor USD 9.0 (lower end of the brief's
9-10 for this shape) + 0.5 per reader call done; six calls reach 12.0, not past it; a T0 call would carry it past 12 and is
therefore not run unless the floor is revised downward by the parent (it is not, in this session). A call still running at a
line finishes; nothing new starts.
Declared reading by units done: fewer than 3 calls (no complete pass): non-test, no score run on a partial pass except to
report it as such. Pass 1 complete only (3 calls): the numbers are reported per arm for that pass; the gate needs two passes and
is reported as 'not distinguishable (one pass)'. Both passes: the gate above, word for word. A null is a result.

## What is NOT done
No truth file read by eye or by a tested arm; f.89's truth opened only by tx_bench; the calibration truths only by
tx_calibrate feedback (counts and label sets, never printed whole). No change to BENCHMARK-TX.tsv or any truth or flag. No tuning
after a score. No eval item (birago1572-no87, birago1572-f152r, gunther8246-p2, bir1591-f23r-gloss) is scored: LOOKS.tsv gets no
row from this job. No confirm item, no sorter page, no owner evidence. Nothing published.
