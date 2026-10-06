# PREREG R15-CLIN407 (6 Oct 2026, addendum to PREREG_R15-CLIN3853.md, written before the scored run)

Item 3853 (Robertson to Haldimand, 31 Oct 1781), cipher continued on B.147 p.407 (H-1649 Image 1058; R15-CLIN3853 saw the
frame at 1400 px: six columns, glosses "I will willingly give a very good" ... "says", ending "Oct. 31st 1781. J.R.").
Everything in PREREG_R15-CLIN3853.md holds unchanged (key variants (a)/(b)/(c), (b) GATED; alignment rule; control =
printed letters of the aligned span shuffled, 1000 seeds, seed 3853, scored under (b); gate (b) share >= 0.80 AND (b) count
> control max; grades S under the gate, M otherwise; conflicts by witness, not settled), with these changes only:

- Page: Image 1058 full/max, page label read on the frame before the pass. Column crops by passes/cut_2380_p121_122.py with a
  box added for 1058 (tools/iiif_lines.py --image first, pasted). One blind Sonnet pass over the half-column crops (one call,
  this page only, told nothing of the key or text), then the worker's re-read of uncertain / key-failing / count-differing
  cells on native crops, logged in passes/p407_reconciled.tsv.
- Printed text: the same passes/p381_print1920.txt; p.407 is expected to align to the printed words after "Vermont"
  ("I will willingly give ... Noblesse"). Nothing else changes in the alignment; the NW free leading/trailing printed words
  let it place itself.
- Scored separately as check_3853.py's p.407 block (same function, source p407_*.tsv), reported beside p.406, not pooled.
- "Text beyond the print" = cipher words on p.407 aligned to a gap; reported in full with their (b) letters; S only if the
  gate passes and the letters read as English, else M. Printed words with no p.407 cipher are reported as "print carries
  more than the cipher".
