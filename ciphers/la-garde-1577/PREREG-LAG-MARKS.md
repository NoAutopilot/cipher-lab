# PREREG-LAG-MARKS (9 Oct 2026, account 2, LANE FAMILY-A2e, written before any look result was read)

Question (brief LAG-MARKS): does the one-reader marks-kept transcription error fall inside LAG-SYL's covered band
(<= 0.107, where the syllabary control reads >= 0.60) or in the uncovered band 0.107-0.183?

Cells: every literal (marks-kept) split between pass A and its witness, `lag_marks_cells.py` -> `lag_marks_cells.tsv`
(63 comparisons over 345 aligned; 57 distinct cells, 9 already H-graded in v2 from WC-LAGARDE's image settles). The 48
remaining distinct cells are settled by one blind Sonnet look per batch (6179 p2; 6179 p3 + 6467 p2), from
`tools/iiif_lines.py` line crops of the 150 dpi page renders, candidates listed alphabetically with no pass named;
readings `sure`/`doubt`. The orchestrating worker reconciles: where its own look of the same crop disagrees with a
`sure` look, or a cell is `doubt`, the cell is graded `doubt` (no second-look budget is assumed).

Statistic (`lag_marks.py`): per comparison, reader error = split cells where that reader's sign differs from the settled
sign / aligned comparisons (doubt cells dropped from both numerator and denominator); one-reader error = mean of the two
readers' rates, pooled over the 345 comparisons. Bounds: lower = doubt cells charged to neither; upper = doubt cells
charged to both. A shared misreading (A and witness agree, both wrong) is invisible: the figure is a lower bound on true
one-reader error, stated as such.

Decision (fixed now):
- central AND upper <= 0.107: inside the covered band; LAG-SYL's syllabary (regular) negative covers the target.
- central <= 0.107 < upper: undecided at this resolution; the covered claim is not made; next control level named.
- central > 0.107: outside; name the next control level (the measured upper, rounded up to 0.01), do not run it.
The A-vs-B and A-vs-L1 figures are reported separately beside the pooled one; the decision uses the pooled figure.
