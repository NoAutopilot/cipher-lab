# PREREG R11-CLIN2380C (6 Oct 2026, written before the scored run)

Item 2380, B.147 p.122 (H-1649 Image 760, BL fo.106: 5 cipher columns + a "P.S." column, "(Signed) H. Clinton"),
continuing R11-CLIN2380B (p.121, PREREG_R11-CLIN2380B.md, 4aa284973) exactly: same key (passes/title1778_reading.txt),
same alignment, same statistics, same control.

Transcription: the six column crops cut by passes/cut_2380_p121_122.py (default SHEAR 0.025, PAD 30; tools/iiif_lines.py
--image img760.jpg --region 1900,600,1900,2900 wrote 0 crops). One blind Sonnet pass over the twelve half-column crops
(one call, this page only), then the worker's re-read of cells the pass marks uncertain and cells that fail the key, on
zoomed crops, logged per cell in passes/p122_reconciled.tsv, changing a cell only where the image shows the pass misread.

Alignment (letters never used): cipher words split at underlines; "-P" / ditto cells repeat the previous line figure
(carried from p.121's last cell). p.122's cipher words are aligned to the decipherment words (passes/p134_reading.txt body)
after p.121's last aligned word, by check_2380_c37.py's length-only Needleman-Wunsch. The "P.S." heading is not a cell; the
P.S. column's cells continue the word stream (the decipherment body ends "I have received your Dispatches by the
Defiance", which the alignment may pair with it). Equal-count pairs compared cell by cell; the rest reported apart.

Statistics, all reported: (a) printed page; (b) line 1 = "BY PERMISION of the RIGHT HONORABLE" -- GATED; (c) (b) + line 9
= "OFICERS in the several REGIMENTS" (secondary); (d) (c) + the doubled-figure rule verified by R11-CLINV3 (L-PP with
repeated digits and P beyond the line = letter at single P), secondary, reported as a separate variant, never in the gate.
Control: decipherment body letters shuffled, 1000 seeds, seed 2380, same compared positions, scored under (b), (c), (d).
Gate: (b) share >= 0.80 AND (b) count > control max under (b). Each mismatch listed with an image note (clear = encipherer's
slip, or ambiguous). Cipher/decipherment word conflicts recorded by witness (rule 4), no majority.
