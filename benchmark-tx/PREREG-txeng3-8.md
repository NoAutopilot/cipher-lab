# PREREG TXE3-8 SHEET (account 3, Fable worker, session_01JABsEdZ9LuiUNtZAzPS9gv; written 11 Oct 2026 05:5x UTC by `date -u`, pushed BEFORE any read)

**What this is.** PREREG-txeng2-21 section **SHEET-H2** (TXE2-SHEETH2, written 04:0x UTC 10 Oct 2026, commit 754e6fb19) registered the
sheet-form test on a second hand: Birago 1572 no.87 dev_tune, pictured sheet (arm P) vs the same 51 cells as a value-blind text list
(arm T), two runs per arm. At 05:48 UTC 11 Oct it is **unrun and unclaimed**: no benchmark-tx/txeng2/sheeth2/ exists, no ROOM.md line names
SHEETH2 or SHEET-H2, LANE TX-ENGINEER-2's last ROOM line is 03:53 UTC 10 Oct (incarnation 5, closed), and account 4's orchestrator role
was taken over by the owner account at 06:22 UTC 10 Oct. This worker claims it in ROOM.md (addressed to TX-ENGINEER-2) and **runs it as
registered**, adding the two things its own brief requires: err_true on every output (edits are not accuracy) and a stop rule sized to this
worker's own cap. Nothing in SHEET-H2's protocol, endpoints or gate is changed; what is added or fixed is listed under "Differences".
Rules as PREREG-txeng2-5's preamble: readers blind; every output committed with its sha256 BEFORE any score; no eval item or eval line
opened (f178v L13-L23, f179r are never copied, named or scored); no truth file edited; value-level headline with the visual-ID (strict)
figure beside; truth-value lines of tx_bench's output stay in the score file, not on the worker's screen.

## Nearest prior and what differs
Nearest prior: SHEET-H2 (PREREG-txeng2-21, the registration this PREREG runs, unrun), SHEET-VIV and SHEET-VIV-C (txeng2/sheetviv/,
sheetvivc/: the sheet-form effect on the Saint-Gouard hand, pictured 58 edits vs text list 86 / 80), X21 / TXE2-MODEL (txeng2/model/: two Opus
readers on this very unit with the pictured sheet, a different reconcile step), TX-SHEET / passE_sheet (an exemplar sheet, retired). What
differs from SHEET-VIV/-C: a second hand, two runs per arm, the degradation direction. What differs from X21: the sheet form is the
manipulation, X21's was the reader model. What differs from SHEET-H2 as registered: nothing in protocol, endpoint or gate; the additions are
listed under "Differences" below.

## Hypothesis
On the Saint-Gouard hand (Vivonne f.102r dev2) a pictured key sheet in place of a value-blind text list lowered the unit-cost edit total
58 vs 86 / 80 (SHEET-VIV, SHEET-VIV-C; stands on edits only, line level p 0.26). H1: the same sheet-form effect appears on a second hand
(Birago 1572 clerk, no.87 dev_tune, 343 signs, 12 lines), i.e. the text-list arm reads worse than the pictured arm by more than the
within-arm run spread. H0: the between-arm gap is within the within-arm spread (sheet form does not matter on this hand; the Vivonne
effect was a one-hand or one-sheet artefact). Direction: degradation (no.87's readers have the pictured sheet today; the text list can
only add errors and has no ceiling at E 12).

## Protocol (SHEET-H2's, fixed; nothing changed)
1. Unit dev_tune: f178v_L01-L12, crops ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L01..L12_s{1,2,3}.jpg ONLY (36 crops,
   committed, no re-cut; crop step: none, the committed 2x crops are used as every prior dev_tune instrument did). Baseline for --paired:
   benchmark-tx/txeng/units/labels_dev_tune.tsv (path + sha256 only; never opened by eye).
2. Arm P: `sign_sheet_blind_1572.png` + `blind_pass_brief_1572.md` as is (copied to brief_P.md, byte-identical). Arm T: the same 51 cells
   T10..T98 as a TEXT LIST, `benchmark-tx/txeng3/8/sheet_text_1572.md`, one 3-8 word shape description per cell written by this worker from
   the sheet image alone (no truth, key, pass or decode consulted), + brief_T.md = brief_P.md with only the sheet reference changed and
   "match each sign to the cell whose description fits" (4 lines differ; `diff brief_P.md brief_T.md` is the whole change).
3. Four runs in the order drawn by `random.Random(20261010).shuffle(['P1','P2','T1','T2'])` = **P2, T2, P1, T1** (recorded here before
   any run). Each run = two blind Opus 5.5 passes (A, B) in fresh contexts, one call per 6 lines (L01-06, L07-12: 18 crops + the sheet per
   call, as X21's d87 reads), readers given scratch copies with no repository path; `tools/reconcile_passes.py --keep-alts`; DISAGREE rows
   only to fresh Sonnet packets of <= 16 rows (every crop of the packet's lines viewed; the arm's own sheet form in the packet, as SHEET-VIV-C
   gave its adjudicators the text list); passZ assembled as sheetviv/assemble_z.py (draft + verdicts, NONE drops); every read, queue, packet
   and passZ committed with sha256 before its score; the tool-call access log of every subagent (access_log.py) committed.
4. Score each run ONCE (`run.py score`, refuses a second call): `tools/tx_bench.py passZ_<run>.tsv <run>_passA.tsv <run>_passB.tsv --bench
   BENCHMARK-TX.tsv --item birago1572-no87 --coverage-diagnostic --exclude-flagged --strict --paired benchmark-tx/txeng/units/labels_dev_tune.tsv`
   (one invocation per run, the single passes beside in the same call as SHEET-VIV-C did; `--coverage-diagnostic` because the unit is 12 of
   the item's 29 truth lines).

## Endpoints and gate (SHEET-H2's, verbatim)
PRIMARY = the mean unit-cost edit total per arm on the unflagged dev_tune positions (the "unit-cost edits base 7 -> output N" figure of the
flagged-excluded paired line). **Sheet form matters on this hand if mean(T) >= 1.25 x mean(P) AND |mean(T) - mean(P)| > max(|P1 - P2|,
|T1 - T2|)**; "NOT DISTINGUISHABLE from run spread" otherwise, with every number. Beside, not gated: as-measured edits; position McNemar P
vs T run-wise; the 12-line counts (under-powered by construction, tx_power at E 12: a clean 30% fixer passes p < 0.05 in 0.106 of draws);
per-run agreement; and -- added by this worker's brief -- **err_true per output, as measured AND flagged-excluded, Wilson 95%, never the
latter alone**, value-level with strict beside.

## Control and its proof that it can vary (CLAUDE.md rule 3)
The control is arm T itself (the same reader pipeline, same crops, same 51 cells, the sheet FORM the only manipulation), and the statistic
is the edit total against truth. The manipulation (sheet form) acts on the readers' matching, which is exactly what the edit total measures:
on Vivonne the two forms moved it 58 vs 86 under one protocol while two same-form runs moved it 6 (SHEET-VIV-C), so the control's number
can differ from the target's on this statistic, in either direction, by construction. The within-arm spread (two runs per arm) is the
null yardstick, as registered. Beside, not a control: X21's Opus pipeline on the same unit with the pictured sheet (passX21_opus_pipeline:
15 edits as measured, 10 flagged-excluded, scored 05:5x UTC 11 Oct by this worker to check the command) is an earlier arm-P-form run under
a different reconcile step (reconcile_blind + adjudication sheet), quoted as a prior, never pooled into mean(P).

## Blind rules
Readers and adjudicators see only their scratch dir: task, the arm's sheet form, their crops, their own output. No truth, decode, key value,
labels_dev_tune, other pass or the other arm's sheet reaches them (access_log.py, committed per run). The L74 oracle pages
(benchmark-tx/txeng2/oracle1/) are not touched. Nothing is published; the owner is not contacted. This worker opens no truth by eye; the
dev truth is read only by tx_bench, once per run.

## Stop rule and budget (this worker's cap, smaller than SHEET-H2's 24 / 150 min)
Cap USD 15, box 2 h from 05:47 UTC (ends 07:47; 80% lines: USD 12 and 07:23 UTC). A run is the unit. Per-run cost is estimated BEFORE each
run from SHEET-VIV's calibration (USD 14.20 for 10 Opus reads + 12 Sonnet packets + an Opus worker: about 0.75 per Opus read, 0.30 per
packet) plus a USD 5 allowance for this Fable session's own turns: about 3.6 per run, so runs 1-2 (P2, T2) are planned; run 3 (P1) starts
only if the subagent token usage logged after runs 1-2 (usage.py shape) keeps the estimate for three runs + allowance under 12 and the
clock is before 06:50; run 4 (T1) only under the same test. **Declared readings by run count:** 4 runs = the registered gate; 3 runs = the
gate with the one measured within-arm spread (the other arm's spread unmeasured, said so); 2 runs (one per arm) = no gate, the between-arm
gap reported as a single replicate per arm beside the Vivonne spread (6) and X21's prior P-form figure, verdict "SHEET-H2 half run: within-arm
spread unmeasured", with the remaining runs named as the next step at their cost. A null is a result.

## Differences from SHEET-H2 as registered (all additive, none touching protocol, endpoint or gate)
- Output folder benchmark-tx/txeng3/8/ (this worker's), not txeng2/sheeth2/; RESULTS.md there.
- err_true (both masks, Wilson 95%) on every passZ and single pass, as this worker's brief requires.
- The stop rule above (SHEET-H2's cap 24 is above this worker's 15).
- CLAUDE.md Usage 6's "one line per subagent image call" is set aside for SHEET-H2's registered 6-lines-per-call layout (18 line crops +
  one sheet per call, never a page), since the registered design is what is being replicated.

## Step 1 files (committed with this PREREG, before any read): benchmark-tx/txeng3/8/SHA256SUMS_step1.txt
sheet_text_1572.md, brief_P.md, brief_T.md, run.py, adjud_task_template.txt, access_log.py, plus the hashes of sign_sheet_blind_1572.png,
blind_pass_brief_1572.md and labels_dev_tune.tsv as found.
