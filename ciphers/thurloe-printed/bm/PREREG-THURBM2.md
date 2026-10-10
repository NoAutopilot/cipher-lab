# PREREG-THURBM2 -- seven-letter re-run of the PREREG-THURBM gate (written 10 Oct 2026, 15:1x UTC by date -u, before any score)

Job: THUR-BM2, LANE FAMILY-A2r (account 2). Brief: .claude/briefs/runs/2026-10-10-ytbiz-family-1410-jobs.md "### THUR-BM2".
The pre-registered rule of PREREG-THURBM.md is NOT changed: same statistic, same shuffled-key control (200 draws, seeds 0..199,
random.Random(seed).shuffle of the training key's meanings), same gate (for BOTH passes: every fold's real agreement above its own p95
AND pooled held-out agreement >= 0.70 on covered groups), same normalisation, same key build (`tools/interlinear_align.py align`,
default --floor 100, majority meaning). Only the pool changes: seven letters, leave-one-letter-out, seven folds per pass.

## Pool
- The four THUR-BM letters, passes unchanged (bm/passes/<line>_B1.tsv, _B2.tsv for l40469, l65889, l77385, l89881).
- Three more glossed Blank-Marshall letters of Birch 1742 vol 6 (bim_ copy): l3370 (pp.31-32, leaves 32-33, 11 Feb 1657 N.S.),
  l83274 (p.698, leaf 701, last Dec 1657 N.S.), l86815 (pp.729-730, leaves 732-733, 14 Jan 1658 N.S.). Two blind Sonnet passes each
  on line-strip crops (bm/crops/l3370_*, l83274_*, l86815_*), no key shown, written to bm/passes/<line>_B1.tsv, _B2.tsv. The gloss is
  the known answer and is NOT reconciled before scoring (V-BRANDT rule).

## One implementation detail fixed now (needed because l3370 is glossed word by word, not letter by letter)
A pass marks a printed gloss word spanning several groups as the word on the span's first group and "^" on the rest.
- Pairs for the aligner: plain_raw = the row's gloss words in order ("^" contributes nothing); cipher_raw as before.
- Per-group known answer for scoring: a span of n numeral groups all < 100 whose word normalises to exactly n letters gets one letter
  per group in order; a span of one group keeps the word; any other span (letter count != n, or a code >= 100 inside a multi-group
  span) is excluded from scoring (treated as unglossed) and counted in the gate table's `excluded` column.
- Everything else as bm/bm_gate.py (THUR-BM); the four-letter gate.tsv is not rewritten.

## Outputs
bm/bm_gate7.py [--check] -> bm/gate7.tsv (seven folds x two passes + POOLED rows). Full seven-letter key: bm/key_blankmarshall_7.tsv
(codes whose B1 and B2 meanings agree, grade C; disagreements listed with both meanings, grade M). bm/key_blankmarshall.tsv,
reading_l44535.*, AUDIT.md and status.json are not touched (V-THURBM audits them in parallel).
