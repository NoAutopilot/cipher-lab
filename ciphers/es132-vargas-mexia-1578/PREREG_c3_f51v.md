# PREREG addendum, Cipher 3 pool page 6 -- es132-vargas-mexia-1578 f.51v (RUN5-ES50B, LANE-RUN5 account 1, 4 Oct 2026, written 12:53 UTC by `date -u`, before any f.51v pass or decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run5-wave1.md` section RUN5-ES50B unit (b). Everything is `PREREG_c3_f50r51r.md`
(ff236258) with the page changed to f.51v: statistic, nulls (200 order-shuffle, 200 key-shuffle, seed 1578), gate (b) on pass A, pass B
and reconciled (primary = both blind passes), positive control f.90v unprinted lines in the same run (else non-test), grades. Scorer
`test2.py --page f51v` ('f51v' added to C3_PAGES in 9eeef7bf with the same line list; no statistic changed), writes
`c3_test1_f51v_result.json` and `reading_f51v.txt`; `--check` exits 1 if stale.

## Page
cabinet-noir re-checked 12:4x UTC (fresh shallow clone of el-descifrador/cabinet-noir): `git log -1` = 47b6db9 (2 Oct 2026), unchanged;
es132 folders the same 30 (no f051). One 1200 px look at canvas 49: f.51v (left page) = about 25 cipher lines in one block, no clear text,
lines running into the binding; it follows f.51r. (The right page, f.52r, ends with a clear "Del Bosq[ue] ..." line: the letter ends there.)
Crop: `tools/iiif_lines.py --ark btv1b10032556x --canvas 49 --region 1050,780,2450,3560 --prefix f51v --follow-slope 300 --slope-margin 40
--max-width 1450 --debug` -> 25 bands x 2 segments; overlay checked by eye: 25 bands = 25 lines, one line per band.

## Transcription
Two blind Sonnet passes with `run2/pass_prompt_f51v.md` = `run2/pass_prompt_f50r_B2.md` (the f.50r prompt plus the paragraph calling out
the '.' dot vowel sign, PREREG_c3_f50r_B2.md) with crop paths, two segments and 25 lines; the notation is unchanged, only the reminder
is added, for both passes alike. -> `passes/f51v_passA.tsv`, `_passB.tsv`. Reconciliation (third unit): `run2/reconcile_f41r.py
--page f51v`, R1-R7 mechanical, default = pass A's token flagged '?'; no rule added after the decode is run. err_2reader and '?' reported.
