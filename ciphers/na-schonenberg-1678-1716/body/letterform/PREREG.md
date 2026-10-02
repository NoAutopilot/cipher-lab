# GAPS14 pre-registration: code 36 c/e by gloss-hand letterform (written 2 Oct 2026 before any sorting pass)

Material: sheet.jpg (make_sheet.py --seed 14 from tiles_boxes.tsv): 14 value-blind tiles of the small gloss hand on the
native leaf image -- the gloss letter over each of the 4 code-36 occurrences (L04 pos17, L06 pos12, L10 pos10, L14 pos7),
over the 2 C-graded c tokens in the body (code 14, L04 pos8 and L09 pos5; the only C-graded c's in L01-L14) and over 8
C-graded e tokens (codes 60, 38, 5, 16, 10; picked one or two per line across L03-L14 where the gloss shows an e).
The tile -> id key stays outside the repository until all three calls are in.

Procedure: two blind Opus 5.5 subagent passes, each shown only the sheet and told only that every tile is one of two
letters of one late-17th/early-18th-century hand, in unequal numbers; each sorts the 14 tiles into group A / group B by
letterform. One Opus 5.5 reconciliation call sees the sheet and both sorts (still no labels) and settles any tile they
split. 3 vision calls in all.

Scoring (score.py, on the reconciled sort; both passes reported too):
- Group naming: the group holding the majority of the 8 known-e tiles is the e group; the other is the c group.
- Known-answer accuracy = known tiles (2 c + 8 e) in their own label's group / 10.
- Control: label shuffle, 20 seeds -- the 10 known labels permuted over the 10 known tiles, the same naming rule and
  accuracy recomputed on the same sort (the permutation can and does change the statistic).
- GATE (all must hold): known-answer accuracy >= 0.90 (at most 1 of 10 wrong); both known c tiles in the c group
  (per-class 2/2, since the c class has N=2 -- rule 3's unbalanced-class caution); accuracy > the p95 of the 20-seed
  shuffle; and all 4 code-36 tiles in one group. Then 36 takes that group's letter at C (gloss-hand letterform, two blind
  passes + reconciliation, known-answer control). Otherwise 36 stays M at c.
- If the gate fails, the 36 step is [retired] for this instrument (third instrument after the 4-gram GAPS12 and the
  dictionary GAPS13 tests; rule 3's third-attempt clause), not refuted.
Known weakness stated in advance: the c class rests on two tiles; a pass of the gate is a narrow one.
