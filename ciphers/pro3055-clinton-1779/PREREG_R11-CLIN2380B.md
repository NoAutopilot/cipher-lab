# PREREG R11-CLIN2380B (6 Oct 2026, written before the scored run)

Item 2380, B.147 p.121 (H-1649 Image 759, BL fo.105v, 8 cipher columns) and, if the cap allows, p.122 (Image 760, fo.106,
6 columns incl. a "P.S." column, signed "H. Clinton", endorsed "22d Oct ... Recd 20th May 1780 by Express via Niagara"),
continuing R11-CLIN2380 (p.120 columns 3-7, PREREG_R11-CLIN2380.md, c5d45b736). Same key (1778 title page,
passes/title1778_reading.txt), same alignment, same statistic family, same control.

Transcription: crops cut by passes/cut_2380_p121_122.py (boxes in the script; tools/iiif_lines.py found no usable rows).
One blind Sonnet pass per page over its column-half crops (one page per call), then the worker's re-read of cells that fail
the key on zoomed crops, logged per cell, changing a cell only where the image shows the pass misread (reconciliation).

Alignment (letters never used): cipher words split at the underlines; the "-P" / ditto-dot cells repeat the previous line
figure (carried across columns and from p.120 c7, line 6). p.121's cipher words are aligned to the decipherment words
(passes/p134_reading.txt body, digits dropped as in check_2380_c37.py) that follow "arrived" (the last word aligned on p.120);
p.122's, if read, to the words that follow p.121's last aligned word. Needleman-Wunsch on lengths only, as check_2380_c37.py
(+1 when the cell count equals the decipherment word with doubled letters written once, 0 otherwise, gap -1). Equal-count
pairs are compared cell by cell; the rest reported apart, outside the gate.

Statistics, all reported: (a) page letter = decipherment letter on the printed page; (b) line 1 read as the GAPS9 variant
"BY PERMISION of the RIGHT HONORABLE" -- THE GATED STATISTIC, as on p.120; (c) (b) plus line 9 read as "OFICERS in the
several REGIMENTS" (found post hoc on p.120, pre-registered here as a secondary, not gated); (d) (c) plus the doubled-figure
rule found post hoc on p.120 (a cell L-PP whose two digits repeat and P exceeds the line stands for the letter at single P),
secondary, not gated. Control on the same axis: the decipherment body letters shuffled (1000 seeds, seed 2380) at the same
compared positions, scored under (b), (c) and (d) each; per page.
Gate per page: (b) share >= 0.80 AND (b) count > control max under (b). Each mismatch listed with a note on whether the
image shows the figure clearly (encipherer's slip) or ambiguously. Cipher/decipherment word conflicts recorded by witness
(rule 4), no majority.
