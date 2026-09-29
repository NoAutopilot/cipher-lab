# R2-2 sign-or-mark rule and declared folds (29 Sept 2026, written from the images before any reader call)

Looked at: six random instances each of BAR-SOLID (38 boxes), BAR-THIN (39), BLOB (42), DASH-V (8), DASH-H (13),
HOOK-L (3), each with its line context, from the public PNGs (script in LOG.md, row 2).

What the images show:
- **DASH-V** (6 of 6 seen): the scan's own page edge or the black border beside it. Not ink of the writer.
- **BAR-SOLID** and **BLOB**: dots and short solid dabs, at or under half the line's sign height, standing on the
  baseline, often in rows of 3-5 ("....", after `?`), or a dot placed against a neighbouring sign. Shape does not
  separate the two ids (the atlas already calls BAR-SOLID "the same ink blob as BLOB", NOTES.md line 469).
- **HOOK-L** (3 of 3): a comma on the baseline.
- **BAR-THIN**: a full-height vertical stroke, standing alone at sign spacing (as in a digit run "5 l 6"), except
  where it is the page edge (2 of 6 seen).
- **DASH-H**: a dash at mid-height, sometimes standing alone, sometimes one bar of a stacked sign or an underline.

Rule (applied to every pass and every reader alike, as a class-level fold, so it needs no re-reading):
1. BLOB, BAR-SOLID, HOOK-L and DASH-V are **marks** (punctuation, dots, the page edge), not signs of the cipher
   stream; they fold with `_`.
2. BAR-THIN and DASH-H are **signs** when they stand apart at sign spacing and full height (BAR-THIN) or mid-height
   (DASH-H); a BAR-THIN or DASH-H that is the page edge, a drawing's line, or a bar of the neighbouring sign is `_`.
   Readers are told this in their prompt; old passes cannot be re-judged by it and keep their ids.
3. A rule applied by one reader is a segmentation convention, not a reading (DIGEST-1 section 2, item 1).

Declared folds (DIGEST-1 section 2, item 2): PCT+PCT-SLASH, X+X-DOT, X+X-CURL. X+X-BAR, X+X-O and
CHEVRON+CHEVRON2 are not folded. Every figure is given three ways: unfolded; folds only; folds + rule.
