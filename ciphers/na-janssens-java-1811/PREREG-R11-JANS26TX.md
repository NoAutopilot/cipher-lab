# PREREG R11-JANS26TX (6 Oct 2026, written before any pass or score; account 2, LANE LANE-RUN11-account-2)

Material: invnr 26 scans 10 (right page, 19 rows) and 11 (left page, 2 rows), native IIIF (5000 px wide, maxWidth),
line crops in images/crops_inv26/ cut by tools/iiif_lines.py. Two blind Sonnet passes (crops only, one page per call),
then the worker's reconciliation -> inv26_reconciled.tsv.

Statistic: global alignment (Needleman-Wunsch, match +1, mismatch -1, gap -1, codes compared as whole strings) of the
reconciled inv26 code sequence against leaf 188's ciphertext.tsv sequence (163 codes, as transcribed, corrections.tsv
NOT applied, so the copy is a blind witness to the 13:11 correction). Score A = exact matches / 163.

Control (can differ: alignment agreement depends on order): the same alignment of the inv26 sequence against 1000
random permutations of leaf 188's 163 codes (seeds 0-999). Report real A, control mean, control max, and the count of
shuffles >= real.

Gate: the copy is accepted as a same-text witness only if A >= 0.80 AND A > control max. Below that, no
disagreement is used to correct leaf 188.

Use of disagreements (only if the gate passes): a leaf-188 digit is changed (corrections.tsv) only where (a) the
inv26 reading is unanimous across both passes and the reconciliation, AND (b) leaf 188's own reading is doubtful (its
split188 passes disagree or a pass marks it non-H, or its key grade is M/U) AND the leaf-188 crop re-read supports the
inv26 value. Otherwise the disagreement is listed, both readings kept. Codes present only in inv26 (e.g. the leading
5) are reported, not merged into key.tsv (no gloss).
