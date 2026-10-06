# PREREG R11-CLIN2380 (6 Oct 2026, written before the scored run)

Item 2380, B.147 p.120 cipher columns 3-7 (H-1649 Image 758, full/max 6032x4056, scratchpad only), continuing GAPS9
(columns 1-2, passes/check_2380.py: 52/93 exact on the printed 1778 page, 60/63 line-1 cells fitting the variant
"BY PERMISION of the RIGHT HONORABLE"). Same key, same statistic family, same control as GAPS9 and R10-CLIN3868/B.

Transcription: one blind Sonnet pass over ten column-half crops (c3-c7, top/bottom; PIL boxes in NOTES.md), then the
worker's re-read of cells that fail the key on zoomed crops, logged per cell, changing a cell only where the image
shows the pass misread (the reconciliation unit).

Alignment (letters never used): the cipher cells split into words at the copyist's underlines; clear words written by
the copyist are anchors. Cipher words are aligned to the decipherment words (passes/p134_reading.txt body) that follow
the 25 words GAPS9 aligned, by a Needleman-Wunsch alignment on lengths only (score +1 when a word's cell count equals
the decipherment word's length with doubled letters written once, 0 otherwise, gap -1). Pairs whose counts are equal
are compared cell by cell; the rest are reported apart and kept out of the gate.

Statistic: compared cells whose 1778 title-page letter equals the decipherment letter, computed twice and both
reported: (a) on the printed page (passes/title1778_reading.txt) and (b) with line 1 read as the GAPS9 variant
"BY PERMISION of the RIGHT HONORABLE" (fixed in advance from columns 1-2, not refitted). Control on the same axis:
the decipherment body letters shuffled (1000 seeds, seed 2380) at the same compared positions, under (b).
Gate: (b) share >= 0.80 AND count > control max. Each mismatch listed with a note on whether the image shows the figure
clearly (encipherer's slip) or ambiguously. Cipher/decipherment word conflicts recorded by witness (rule 4), no majority.
