# GAPS141 pre-registration (written 3 Oct 2026 ~14:58 UTC, before either pass was read and before any score)

Material: R1411 p.1 (IMG_R1411_I6595_P1.png, sha1 126a2f4c...), region x380-3456 y660-1420, five numeral lines carrying a
period interlinear letter gloss (L01-L05). Crops: tools/iiif_lines.py --image ... --region 380,660,3076,760 --prefix p1g
--centres 70,195,310,405,645 --top-margin 45 --bottom-margin 35 --max-width 1600 --overlap 200.
Passes: two blind Opus passes (A, B), one call each, crops only; reconciled with tools/reconcile_passes.py, the worker
settling disagreements from the crops.

Pairs used: every reconciled (number, gloss) with a non-blank gloss; doubtful ('?') pairs left at M and excluded from
the fit and the test (reported separately).

Held-out test: glossed pairs in reading order (L01 pos 1 -> L05 last) split at the midpoint; table fitted on the first
half (majority letter per number), applied to the second half.
- coverage = test pairs whose number is in the fit table / test pairs
- accuracy = covered test pairs where the table letter equals the gloss / covered test pairs
Control: value-shuffled table -- the fit table's letters permuted among its numbers (letter frequencies kept), 10,000
draws, same accuracy statistic. This control can differ from the real table on accuracy (it changes which letter each
number carries), so it is not a non-test by construction (rule 3).
Gate: PASS if covered test pairs >= 8 AND accuracy >= 0.80 AND accuracy > the shuffled draws' 99th percentile.
If covered test pairs < 8: NON-TEST at this N (too few repeats), not a negative.
Secondary (descriptive, no gate): whole-sample self-consistency (share of repeated-number occurrences agreeing with the
number's majority letter) vs a position-shuffled-gloss control (glosses permuted across positions, 10,000 draws).
A PASS licenses a "reading ready" ROOM flag for the unglossed numerals (p.1 lower block and later pages); no status
change, no reading committed by this step unless the decode script with --check is added.
