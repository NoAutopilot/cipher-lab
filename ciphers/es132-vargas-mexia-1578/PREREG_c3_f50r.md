# PREREG addendum, Cipher 3 pool page 5 -- es132-vargas-mexia-1578 f.50r (RUN4-ES50R, LANE-RUN4 account 1, 4 Oct 2026, written 11:42 UTC by `date -u`, before any f.50r pass or decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run4-wave3.md` section RUN4-ES50R (f.50r, one page). Everything is `PREREG_c3_f50r51r.md`
(ff236258) with the page changed from f.51r to f.50r: statistic, nulls (200 order-shuffle, 200 key-shuffle, seed 1578), gate (b) on pass A,
pass B and reconciled (primary = both blind passes), positive control f.90v unprinted lines in the same run, grades. Scorer
`test2.py --page f50r` ('f50r' already in C3_PAGES since b0ec0d99; no statistic changed), writes `c3_test1_f50r_result.json` and
`reading_f50r.txt`; `--check` exits 1 if stale.

## Page
cabinet-noir re-checked 11:41 UTC (fresh shallow clone of el-descifrador/cabinet-noir): `git log -1` = 47b6db9 (2 Oct 2026), unchanged;
es132 folders the same 30 (no f050). One 1200 px look at canvas 47: f.50r right page = "El Rey" + address and two and a half clear lines
("Juan de Vargas Mexia. Despues que ultimamente se os aviso del recibo de vuestras cartas ... del passado"), then cipher from mid line 3 to
the end (22 more lines). Crop region 3600,1340,2850,3060 -> 24 bands: L01 wholly clear, L02 clear then cipher, L03-L24 cipher. Clear text
is written `{CLEAR:...}` by the readers and dropped by test2.py (line 50), as on every earlier page.

## Transcription
Two blind Sonnet passes with `run2/pass_prompt_f50r.md` (f51r's prompt, paths and line count changed only) -> `passes/f50r_passA.tsv`,
`_passB.tsv`. Reconciliation (third unit): `run2/reconcile_f41r.py --page f50r`, R1-R7 mechanical, default = pass A's token flagged '?'.
No rule added after the decode is run. err_2reader and the '?' count reported.
