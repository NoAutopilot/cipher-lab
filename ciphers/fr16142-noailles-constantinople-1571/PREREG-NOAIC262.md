# PREREG NOAI-C262 -- c262 cipher rows below c262rc L10 (beside gloss L14-L21): two blind passes, reconcile, extended test0

Written 15 Oct 2026 02:5x UTC (date -u), pushed before either reader pass is run and before any score on the new rows exists.
Worker NOAI-C262, LANE DEFAULT-A4-0235-15 (account 4); brief `.claude/briefs/runs/2026-10-15-acct4-default-0235-jobs.md`.

## Material
- Canvas 262 (Gallica btv1b9060927q f262), the committed native file `images/src_ark_12148_btv1b9060927q_f262_full.jpg` (no new fetch).
- Crops (worker scratchpad, not committed; regenerable):
  `python3 tools/iiif_lines.py --image images/src_ark_12148_btv1b9060927q_f262_full.jpg --region 1330,3330,3470,760 --centres 95,277,394,537,654 --follow-slope 300 --slope-margin 15 --max-width 1800 --overlap 100 --prefix c262rd --out <scratch> --debug`
  -> 5 rows x 2 segments. Row c262rd L01..L05 = c262 cipher rows 11-15 (the row after c262rc L10 "+ ^ ..." beside gloss L13, down to
  the row ending before the "+ pour ceste mesme raison" row, which is not included). Overlay and a stack of all 10 strips checked by
  eye: one text row per crop.
- Reader references: Tomokiyo's table (CharlesIX_Acqs2.png, fetched once 15 Oct 2026, not committed); c262rc L01 and L04 crops with
  their `witness/c262rc_recon.tsv` label rows as worked examples; NX-RECUT's glyph rulings (2-with-stem-circle n1, 6-with-cross-above
  t2, box hanging from bar with stem down W:le, loop-S e3, cup-on-stem s2, theta-with-tail d1; '#' written o1/e2); label vocabulary =
  the 41 labels in c262rc_recon.tsv plus any other table position written <letter><row>, W:<word>, N<k>, D<k>, or ? .
- Gloss for the rows: `gloss_below_L13.tsv` L14-L21 (R10-NOX2, one print-blind read, M). Gloss is not shown to readers or used in
  reconciliation.

## Passes and the stop rule
Two Sonnet subagent passes (P, Q), blind to each other, to every earlier reading of these rows and to the gloss; each pass is two
calls (rows 1-3, rows 4-5), per-line crop paths only. Raw `witness/c262rd_passP_raw.tsv`, `_passQ_raw.tsv`; scored copies collapse
`?{...}` to `?`. `tools/reconcile_passes.py` aligns P and Q; err_2reader = disagreement columns / aligned columns.
**If err_2reader > 0.10: stop scoring** (TRANSCRIPTION.md, brief): write disagreements and focus rows, do NOT extend the recon or the
gloss, do not compute any test0 score on the new rows. Gate numbers "before" are reported (unchanged).

## If err_2reader <= 0.10
Reconcile from the crops (this worker; gloss not consulted; no decode printed before the reconciled file is written), and only
agreed columns or columns the crop settles enter the extension. Extended files are written beside the originals so every committed
results_*.json keeps passing --check: `witness/c262rc_recon_L15.tsv` (c262rc L01-L10 + c262rd rows as L11-L15) and
`gloss_L21.tsv` (gloss.tsv L01-L13 + gloss_below_L13.tsv L14-L21). Then `scripts/test0.py --ct witness/c262rc_recon_L15.tsv --gloss
gloss_L21.tsv --hash e|o --stat lcs|difflib --out witness/results[_lcs]_rc_recon15_<e|o>.json` and `--check`.
Gate (same rule as R9-NOX): extended reconciled block beats the MAX of both nulls (200 key shuffles, 200 gloss-order shuffles) at
both '#' resolutions under LCS -> "extension holds"; else reported as not met. Before numbers: LCS e 0.5618 (key max 0.4220,
gloss-order max 0.4462), difflib e 0.5215. The blind passes P and Q are also scored on the extended block (reported, not gated).
Licenses: nothing about depth or N-class; no token above M (rule 4).
