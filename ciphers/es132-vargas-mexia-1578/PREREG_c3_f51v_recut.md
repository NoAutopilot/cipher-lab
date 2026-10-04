# PREREG addendum, f.51v re-cut -- es132-vargas-mexia-1578 (RUN5-ES51, LANE-RUN5 account 1, 4 Oct 2026, written 13:07 UTC by `date -u`, before any re-cut pass or decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run5-wave2.md` section RUN5-ES51 (a). **Re-cut, crops only.** Everything in
`PREREG_c3_f51v.md` (615d380f) stands unchanged -- statistic, nulls (200 order-shuffle, 200 key-shuffle, seed 1578), gate (b) on
pass A, pass B and reconciled (primary = both blind passes), positive control f.90v unprinted lines in the same run (else non-test),
grades, prompt `run2/pass_prompt_f51v.md` (verbatim, both passes), reconciliation `run2/reconcile_f41r.py --page f51v` (R1-R7, no
rule added), scorer `test2.py --page f51v` -- except the crops:

- Old crops (RUN5-ES50B): `--max-width 1450` -> 2 segments of 1450 px over a 2450 px band, ~450 px overlap; both readers doubled
  tokens at the join (a repeated run of >= 3 tokens on 15/25 lines pass A, 12/25 pass B).
- New crops: same cached native source (`images/src_ark_12148_btv1b10032556x_f49_1050_780_2450_3560.jpg`, region 1050,780,2450,3560
  of canvas 49, no new Gallica request), same band finder, `--max-width 1300` -> 2 segments of 1300 px, step 1150, **150 px
  overlap** (the overlap of the three-segment pages f.41r-f.51r, where the detector below finds 0-1 such lines per pass, e.g. f.51r 1/26 both passes, f.50r A 0/24). The brief's
  "3 segments" is not reachable at 1300 px without a ~725 px overlap, so the brief's named width is used and the overlap figure
  is the binding one. Command:
  `python3 tools/iiif_lines.py --image ciphers/es132-vargas-mexia-1578/images/src_ark_12148_btv1b10032556x_f49_1050_780_2450_3560.jpg --out ciphers/es132-vargas-mexia-1578/images --prefix f51v --follow-slope 300 --slope-margin 40 --max-width 1300 --debug`
  Dry run: 25 bands x 2 segments, the same 25 centres as the old cut. Overlay checked by eye before the passes.
- Old files kept beside the new ones with suffix `_es50b` (passes, ciphertext, reading, result JSON, units/firm); the new
  ones take the canonical names.

Reported (diagnostic, not gated): err_2reader old vs new; doubled-run lines per pass (`run2/doubled_runs.py`: a line counts when
some run of 3 consecutive tokens, '?' stripped, occurs twice in it), old vs new. Gate (b) PASS/FAIL is the result; whatever it is,
it replaces the provisional f.51v result.
