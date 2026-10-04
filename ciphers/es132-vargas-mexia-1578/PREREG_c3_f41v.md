# PREREG Cipher 3 pool, page 2 -- es132-vargas-mexia-1578 f.41v (RUN3-ES41, LANE-RUN3 account 1, 4 Oct 2026, written 08:5x UTC by `date -u`, before any f.41v decode; the blind passes were still running)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run3-wave1.md` section RUN3-ES41 step 3. Statistic, nulls, gate, positive control and grading are
those of `PREREG_c3_test1.md` (f.41r), unchanged; scorer `test2.py --page f41v` (C3_PAGES gains 'f41v' with the same line list; no statistic
changed), writes `c3_test1_f41v_result.json` and `reading_f41v.txt`; `--check` exits 1 if stale.

## Page (step 3 choice)
f.41v = Gallica canvas 39, left page (900 px look at canvas 39, 4 Oct 2026 08:5x UTC): 31 full cipher lines, no clear text, the verso of
f.41r, i.e. the same letter (Tomokiyo TOC no.21, Philip II to Juan de Vargas Mexia, Madrid, 29 April 1578, Cipher 3). The brief's first
choice ("f.41v if it carries cipher"). cabinet-noir re-checked 08:4x UTC: last commit 47b6db9 (2 Oct 2026), no f041 folder (also none for
f037 or f079). The right page of canvas 39 is f.42r (cipher), not read here.

## Transcription
Crops `images/f41v_L01..L31_s1/s2.jpg`: `tools/iiif_lines.py --ark btv1b10032556x --canvas 39 --region 650,850,2700,4300 --prefix f41v
--follow-slope 300 --slope-margin 40 --max-width 1450 --centres <31 left-edge ink peaks>` (automatic detection merged lines on this
page's slope; the centres are the 31 row-ink peaks of the region's left 500 px, computed by script, and a contact sheet of L01/02/10/11/
20/21/30/31 and L15 at full width was checked by eye: each crop centred on its own line). Two blind Sonnet passes with
`run2/pass_prompt_f41v.md` (f41r's prompt, paths and line count changed only) -> `passes/f41v_passA.tsv`, `_passB.tsv`.
Reconciliation: `run2/reconcile_f41r.py --page f41v`, i.e. f.41r's shape rules R1-R7 applied mechanically (same hand, same letter), default =
pass A's token flagged '?'. The key is not consulted per span. No new rule is added after the decode is run.
err_2reader = test2.err2 (reported; above one tenth means per TRANSCRIPTION.md the next pass is the lookalike pass / owner sorter, not a third
machine pass).

## Gate (from PREREG_c3_test1.md)
S_b > p99 of both the 200-order-shuffle and the 200-key-shuffle nulls (seed 1578), for pass A, pass B and reconciled; primary verdict =
both blind passes. Positive control f.90v unprinted lines in the same run must PASS, else the f.41v result is a non-test. Standard judge
reported, not gated (es16 held-out FN 48.5-66.5% per fold). A FAIL with key-null overlap counts against Cp.30 here; otherwise "judge cannot
decide".
Grades: S where gate (b) passes on both blind passes and the control passes, else M; '?' tokens M; codes/braces/numbers >= 38 U.
