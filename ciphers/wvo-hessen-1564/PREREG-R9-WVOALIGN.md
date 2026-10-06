# PREREG R9-WVOALIGN -- f.23 interlinear alignment test (written and pushed before any scored run)

Worker R9-WVOALIGN, account 4, 6 Oct 2026 (06:1x UTC by date -u), for LANE LANE-RUN9-account-4.
Brief: .claude/briefs/runs/2026-10-06-account4-run9-jobs.md job R9-WVOALIGN.

Hypothesis: on f.23 each German row is a letter-over-sign decipherment of the cipher row below it (R9-WVOSORT's
observation, grade M by eye).

Inputs (all in r9align/, committed with this file):
- crops: `tools/iiif_lines.py --image ciphers/wvo-hessen-1564/images/01109_p3_400full.jpg --out ciphers/wvo-hessen-1564/r9align/crops
  --region 530,120,2790,1840 --centres 90,180,260,325,410,480,580,655,745,820,930,1015,1100,1190,1290,1375,1480,1560,1630,1720
  --lines-per-crop 2 --max-width 1500 --overlap 150 --prefix f23P --debug` (10 row-pair crops x 2 segments; `marked/` adds the
  red mid-overlap line); `crops_m/` the same with --top-margin 20 --bottom-margin 55 for reconciliation.
- two blind Sonnet passes (passA_1/2.tsv, passB_1/2.tsv; 4 calls, 5 row-pairs each), gloss and cipher transcribed
  independently, cipher in a fixed 28-code shape vocabulary, no alignment asked for.
- gloss_reconciled.tsv: this worker's reconciliation of the gloss rows against crops_m/ (1 unit).
- build_pairs.py -> pairs_piles.tsv (PRIMARY: the sorter's gloss-blind k-means pile ids, every tile in x order),
  pairs_passA.tsv, pairs_passB.tsv (SECONDARY: the blind passes' own codes).

Statistic (implemented as `tools/interlinear_align.py align --shuffle`): CONSISTENT = number of cipher labels whose top
aligned letter occurs >= 2 times, on >= 2 different rows, and is >= 0.6 of that label's aligned (non-empty) occurrences.

Alignment parameters (fixed now): `align PAIRS OUT_ALIGN OUT_KEY --code-prefix @ --seg-bonus 0 --keep-fs --null-cost -1.0`
(6 hard-EM iterations, default). Null cost -1.0 rather than -3.0 because the pile stream keeps every sorter tile, including
known cut faults (stray loops, gutter edge, split signs), which must be free-ish to take no letter.

Control: the same alignment with the gloss rows dealt to the wrong cipher rows (random derangement), 1000 draws, seed 1564
(`--shuffle 1000 --seed 1564`). It can vary on the statistic: a gloss over the wrong row puts letters over signs that do
not encode them, so label->letter agreement across rows falls; checked offline in tools/tests/test_interlinear_shuffle.py
(a true letter-over-sign set passes, a set of signs unrelated to its gloss does not).

Gate (primary, pile ids): real CONSISTENT > control p95 -> PASS; real <= p95 -> FAIL/tie. Secondary (passA, passB):
reported with their own controls, same gate, not used to overturn the primary.

Named descriptive checks (reported, not gated): (a) "worden sei" occurs in C05 and C10: count of the 9 letters whose
aligned label is the same in both; (b) "zweimahl" ends C06 and C07: count of its 8 letters whose aligned label is the same
in both. Matched control for (a)/(b): the same count for the same word positions in the shuffled-draw alignments is
not computed (the words do not stay over the same rows); these two are reported as descriptive only.

On PASS: key.tsv at grade C only for a label whose letter recurs consistently (top >= 2 on >= 2 rows, share >= 0.6) and
whose tiles are single signs; M otherwise; decode with the folder's decode config, --check exit 0. On FAIL/tie: log it;
status stays open.
