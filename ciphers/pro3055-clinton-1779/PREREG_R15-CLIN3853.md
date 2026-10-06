# PREREG R15-CLIN3853 (6 Oct 2026, written before the scored run)

Item 3853 (Robertson to Haldimand, 31 Oct 1781), cipher B.147 p.406 (H-1649 Image 1056, page label "406" read on the
1400 px frame; opens in clear "Dear Sir -- Thanks for the furs, Your Letters & the great pleasure I [have] here in being
continued in Your Friendship", then six columns of figure pairs with the copyist's glosses). Printed text compared:
the f.381 decipherment as printed in 1920 vol. III doc. (260) p.214 (passes/p381_print1920.txt, OCR slips normalised:
"(Sir" -> Sir, "will1" -> will, "youj" -> your, "1 doubt" -> I doubt).

Transcription: column crops cut by passes/cut_2380_p121_122.py (option added for Image 1056; tools/iiif_lines.py --image
first, pasted). One blind Sonnet pass over the half-column crops (one call, this page only), told nothing of the key or
the text; then the worker's re-read of cells the pass marks uncertain, cells that fail the key and count-differing words,
on native crops, logged per cell in passes/p406_reconciled.tsv, changing a cell only where the image shows the pass misread.

Key: passes/title1778_reading.txt (1778 Army List title page), cell L-P = letter P of line L ("-P" repeats the previous
line). Variant (b), GATED: line 1 = "BY PERMISION of the RIGHT HONORABLE" (GAPS9). Variant (c), secondary: (b) + line 9
= "OFICERS in the several REGIMENTS".

Alignment (letters never used): cipher words split at the copyist's underlines; glosses are units carrying their own
words. Needleman-Wunsch over units vs printed words: a gloss word scores +2 on an equal printed word, a cipher word +1 on
a printed word of equal letter count, gaps -1 on either side, free leading/trailing printed words. Equal-count pairs are
compared cell by cell; the rest reported apart. Cipher words aligned to a gap (no printed word) are the candidate
"text beyond the extract" and are reported in full with their (b) letters; printed words aligned to a gap are reported
as "extract carries more than this cipher page".

Statistics, all reported: (a) printed key page; (b) GATED; (c) secondary. Control: printed-text letters (from "Sir Henry
Clinton" to the end of the aligned span) shuffled, 1000 seeds, seed 3853, same compared positions, scored under (b).
Gate: (b) share >= 0.80 AND (b) count > control max. Gloss/print and cipher/print word conflicts recorded by witness
(rule 4), not settled. Grades: S for cipher cells read under the gate (the print is an edition of a period decipherment,
not a key source for these cells); any cipher word beyond the extract that reads as English under (b) is S if the gate
passes, else M.
