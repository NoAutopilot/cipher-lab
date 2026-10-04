# PREREG Cipher 3 pool, page 3 -- es132-vargas-mexia-1578 f.50v (RUN4-ES41V, LANE-RUN4 account 1, 4 Oct 2026, written 10:53 UTC by `date -u`, before any f.50v pass or decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run4-wave1.md` section RUN4-ES41V. Statistic, nulls, gate, positive control and grading are
those of `PREREG_c3_test1.md` (f.41r) and `PREREG_c3_f41v.md`, unchanged; scorer `test2.py --page f50v` (C3_PAGES gains 'f50v' with the
same line list; no statistic changed), writes `c3_test1_f50v_result.json` and `reading_f50v.txt`; `--check` exits 1 if stale.

## Page choice
cabinet-noir re-checked 10:4x UTC (fresh shallow clone): `git log -1` = 47b6db9 (2 Oct 2026 14:15 UTC), unchanged; es132 folders the same 30
(no f050). Letter: the next open Cipher 3 letter after f.41 in Tomokiyo's TOC order (f.44 and f.46 are cabinet-noir's): **f.50**, TOC no.25
(no.25-29 = f.50, 54, 58, 60, 62: Philip II to Juan de Vargas Mexia, Bosque de Segovia, 7 and 14 June 1578, Cipher 3; f.58 is cabinet-noir's).
Two 900 px looks (canvases 47, 48 = f.49v|f.50r, f.50v|f.51r): f.50r has the clear address and ~3 clear lines then ~23 cipher lines; f.51r
~33 lines with two paragraph breaks; **f.50v (canvas 48, left page) is 27 full cipher lines, no clear text, edge to edge** -- the most cipher
on one page of the letter. Chosen: f.50v.

## Transcription
Crops (pasted command): `python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 48 --region 800,850,2750,3450 --out
ciphers/es132-vargas-mexia-1578/images --prefix f50v --follow-slope 300 --slope-margin 40 --max-width 1450 --debug` -> 27 bands x 2 segments,
pitch 121, 54 crops. Debug overlay and a contact sheet (L01, L14, L27 both halves) checked by eye: 27 bands = 27 text lines, each centred.
The right ends of some lines run into the gutter (physical; a token at the gutter may be partial).
Two blind Sonnet passes with `run2/pass_prompt_f50v.md` (f41v's prompt, paths and line count changed only) -> `passes/f50v_passA.tsv`,
`_passB.tsv`. Reconciliation (third unit): `run2/reconcile_f41r.py --page f50v`, f.41r's shape rules R1-R7 applied mechanically (same hand
and cipher), default = pass A's token flagged '?'. The key is not consulted per span; no rule is added after the decode is run.
err_2reader = test2.err2 (reported; above one tenth -> per TRANSCRIPTION.md the next step for this hand is the lookalike pass / owner sorter,
not a third machine pass). '?' count reported.

## Gate (from PREREG_c3_test1.md)
S_b > p99 of both the 200-order-shuffle and the 200-key-shuffle nulls (seed 1578), for pass A, pass B and reconciled; primary verdict =
both blind passes. Positive control f.90v unprinted lines in the same run must PASS, else the f.50v result is a non-test. Standard judge
reported, not gated. A FAIL with key-null overlap counts against Cp.30 here; otherwise "judge cannot decide".
Grades: S where gate (b) passes on both blind passes and the control passes, else M; '?' tokens M; codes/braces/numbers >= 38 U.
