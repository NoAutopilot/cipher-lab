# PREREG D4-CLIN (8 Oct 2026, written before the scored run)

Item: B.148 p.123 (H-1649 Image 1205), the cipher copy of Carleton to Haldimand, New York, 25 Sept 1782 (GAPS6/GAPS7).
Key: the 1778 Army List title page (passes/title1778_reading.txt), as GAPS7 and R10/R11/R15. Decipherment: passes/p102_reading.txt
(B.148 p.102, read at H, GAPS7). Only the 32 opening pairs of column 1 were checked before (GAPS7, 19/19 letter cells).

Transcription: Image 1205 full/max (5512x4056) to the scratchpad; tools/iiif_lines.py --image tried first (pasted in NOTES.md);
the six cipher columns cut as top/bottom halves by passes/cut_2380_p121_122.py (box added for 1205). Two blind Sonnet passes
(one call each, this page only) + one worker reconciliation on zoomed crops of every A/B disagreement, logged per cell in
passes/p123_full_reconciled.tsv. A cell still open after reconciliation is M and is left out of the compared set.

Cell classes (from the page, never from the decipherment): "x" or "+" before a full pair = letter cell starting a new key line;
"-P" = letter cell on the current line; a full pair without x = a 1782 word-code element (one word); the head pair 3-4 of column 1
is not a cell (as GAPS7). An underline ends a word; a word code is a word by itself.

Alignment (lengths only, never letters): the page says "Each column is continued on the page following", so each column is a
separate run of the text. Each column's cipher words are aligned to the decipherment word list on their own, by check_2380_c37.py's
Needleman-Wunsch with free leading/trailing decipherment words (+1 when the letter-word's cell count equals the decipherment word with
doubled letters written once; a word code pairs with any word at 0; gap -1). The best and second-best end positions are reported per
column. Equal-count pairs are compared cell by cell.

Statistics: (b) line 1 = "BY PERMISION of the RIGHT HONORABLE" -- GATED; (a) printed page; (c) (b) + line 9 "OFICERS in the
several REGIMENTS"; (d) (c) + the doubled-figure rule (R11-CLINV3), (a) (c) (d) reported, never gated. Control: decipherment body
letters shuffled, 1000 seeds, seed 123, same compared positions, under (b), (c), (d) -- it varies the plaintext side of every
comparison, so it can fail where the target passes. Gate: (b) share >= 0.80 AND (b) count > control max.
Word codes, reported apart (not gated): each code with the decipherment word it aligns to, consistency across repeats, and any
period interlinear gloss on the page ("under", "few", "have", "there", "forward" seen on the layout look) against that word.
Scope stop: p.124 (the continuation) is not fetched in this job.
