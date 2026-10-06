# PREREG R12D-GRAZB2 (6 Oct 2026, written 16:25 UTC by date -u (header first typed 16:37 in error, corrected in the next commit; nothing else changed), before any per-sign box is cut or looked at)

Job: LANE-RUN12-account-4 R12D-GRAZB2. Second attempt at PREREG-R12D-GRAZB.md's question with one change: the crop.

## Unchanged from PREREG-R12D-GRAZB.md
- The same 88 tokens, the same sets (T1 24 f.30 zb; T2a 17 + T2b 11 fr.3040 barred z; P 12 plain z; decoys fh 6+6, n6 6+6),
  read from `r12zb/occ.tsv` (ids, set, source, line position, image), and the same images on disk. No network.
- The instrument: one Sonnet blind shape-sort call, crop paths only, labels hidden, max 8 classes, OFF allowed.
- The gate G0, G1, SAME, DIFFERENT, UNDECIDED and the consequences, word for word; scored by `r12zb/score.py`'s logic
  (copied to `r12zb2/score.py` with only the file paths changed).

## Changed: the crop
- Each token is cut as one tight sign box, not a +-3-sign strip with a proportional tick. Boxes come from `r12zb2/seg.py`
  `align()`: ink-column runs of the half-line image, over-wide runs split, then the half's n tokens assigned to runs by a
  dynamic programme on the line's mean sign width; the token's box is its assigned run, padded 3 px, full line height.
- Eye check before the sort, by this worker (who is not the sorter): an overlay sheet per token showing the box on +-3 signs
  of context with the token's code; where the box is plainly on a neighbour, the worker moves it to the right run (or draws
  it by pixel range) and logs the change in `r12zb2/fixes.tsv` with the reason. The worker judges only "box on the intended
  sign position", using the token's position in the line and the neighbours' codes, never which class a target "should" join.
  At least 5 boxes are opened against the full line image and listed in NOTES.md.
- The sorter sees only the boxed tiles (shuffled ids from `r12zb/occ.tsv`), enlarged to a common height.

## If the decoy control (G1) fails again
Log the sort [retired] for this pair (second attempt with a real crop fix; rule 3) and name the owner's sign sorter as the next
instrument. key.tsv is unchanged under every outcome (as in PREREG-R12D-GRAZB.md).
