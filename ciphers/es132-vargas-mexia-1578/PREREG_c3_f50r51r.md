# PREREG Cipher 3 pool, page 4 -- es132-vargas-mexia-1578 f.51r (RUN4-ES50, LANE-RUN4 account 1, 4 Oct 2026, written 11:26 UTC by `date -u`, before any f.51r pass or decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run4-wave3.md` section RUN4-ES50 (f.50r / f.51r, rest of the June 1578 letter; one page if two
would cross 80% of the USD 6 cap: 3 units x ~USD 1.5 per page = ~4.5 per page, so **one page**). Statistic, nulls, gate, positive control
and grading are those of `PREREG_c3_test1.md` / `PREREG_c3_f50v.md`, unchanged; scorer `test2.py --page f51r` (C3_PAGES gains 'f51r' with
the same line list, commit b0ec0d99; no statistic changed), writes `c3_test1_f51r_result.json` and `reading_f51r.txt`; `--check` exits 1 if stale.

## Page choice
cabinet-noir re-checked 11:16 UTC (fresh shallow clone): `git log -1` = 47b6db9 (2 Oct 2026 14:15 UTC), unchanged; es132 folders the same 30
(no f050/f051). One 1200 px look at canvas 48 (f.50v | f.51r) after RUN4-PIS2's Gallica line: **f.51r (right page) = about 32 cipher lines
in three paragraphs, no clear text** (f.50r: clear address + ~3 clear lines then ~23 cipher, per RUN4-ES41V). Chosen: f.51r, the more cipher,
and the page that follows f.50v (already read) in the same letter. f.50r stays unread (Remaining gaps).

## Transcription
Crops: `tools/iiif_lines.py --ark btv1b10032556x --canvas 48 --region <right page> --prefix f51r --follow-slope 300 --slope-margin 40
--max-width 1450 --debug` (exact command pasted in NOTES.md); overlay checked by eye before passes; blank gap bands are kept as empty rows.
Two blind Sonnet passes with `run2/pass_prompt_f51r.md` (f50v's prompt, paths and line count changed only) -> `passes/f51r_passA.tsv`,
`_passB.tsv`. Reconciliation (third unit): `run2/reconcile_f41r.py --page f51r`, f.41r's shape rules R1-R7 applied mechanically, default
= pass A's token flagged '?'. The key is not consulted per span; no rule is added after the decode is run.
err_2reader = test2.err2 (reported) and '?' count reported.

## Gate (from PREREG_c3_test1.md)
S_b > p99 of both the 200-order-shuffle and the 200-key-shuffle nulls (seed 1578), for pass A, pass B and reconciled; primary verdict =
both blind passes. Positive control f.90v unprinted lines in the same run must PASS, else the f.51r result is a non-test. Standard judge
reported, not gated. A FAIL with key-null overlap counts against Cp.30 here; otherwise "judge cannot decide".
Grades: S where gate (b) passes on both blind passes and the control passes, else M; '?' tokens M; codes/braces/numbers >= 38 U.
