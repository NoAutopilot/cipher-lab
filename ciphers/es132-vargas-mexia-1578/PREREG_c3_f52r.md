# PREREG addendum, Cipher 3 pool page 7 -- es132-vargas-mexia-1578 f.52r (RUN5-ES51, LANE-RUN5 account 1, 4 Oct 2026, written 13:10 UTC by `date -u`, before any f.52r pass or decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run5-wave2.md` section RUN5-ES51 (b). Everything is `PREREG_c3_f50r51r.md` (ff236258) /
`PREREG_c3_f51v.md` (615d380f) with the page changed to f.52r: statistic, nulls (200 order-shuffle, 200 key-shuffle, seed 1578),
gate (b) on pass A, pass B and reconciled (primary = both blind passes), positive control f.90v unprinted lines in the same run (else
non-test), grades. Scorer `test2.py --page f52r` ('f52r' added to C3_PAGES with the same L01-L40 line list; no statistic changed),
writes `c3_test1_f52r_result.json` and `reading_f52r.txt`; `--check` exits 1 if stale.

## Page
cabinet-noir re-checked 13:08 UTC (fresh shallow clone of el-descifrador/cabinet-noir): `git log -1` = 47b6db9 (2 Oct 2026 14:15 +0000),
unchanged; es132-vargas-mexia holds the same 30 folio folders (f011-012 ... f255), no f052. Canvas 49 at 1200 px (1 Gallica request)
+ info.json (7008 x 5452, 1 request): f.52r (right page, foliated "52") = two cipher paragraphs (8 + 13 lines) then the clear line
"del Bosq de segouia ... de Junio 1578" and two signatures; the letter ends here.
Crop (native region, 1 request):
`python3 tools/iiif_lines.py --ark btv1b10032556x --canvas 49 --region 3950,640,2450,3220 --out ciphers/es132-vargas-mexia-1578/images --prefix f52r --follow-slope 300 --slope-margin 40 --max-width 1275 --overlap 50 --debug`
-> 22 bands x 2 segments of 1275 px, step 1175, **100 px overlap**; pitch 135. Overlay checked by eye: 22 bands = 22 lines, one line
per band (L01-L08 first paragraph, L09-L21 second, L22 the clear dating line).

## Transcription
Two blind Sonnet passes with `run2/pass_prompt_f52r.md` = `run2/pass_prompt_f51v.md` with crop paths, line count (22) and one
clause changed (L22 may be clear handwriting -> one {CLEAR:...} token, in place of the binding note, which does not apply to a
right page); notation unchanged, both passes alike. -> `passes/f52r_passA.tsv`, `_passB.tsv`. Reconciliation (third unit):
`run2/reconcile_f41r.py --page f52r`, R1-R7 mechanical, default = pass A's token flagged '?'; no rule added after the decode is run.
err_2reader, '?' and `run2/doubled_runs.py` per pass reported.
