# Blind reconciliation of two readings of a 16th-century French marginal note, fr16045 canvas 252 (PIS-121B, 15 Oct 2026)

Do not read any file in the repository and do not search; use only the files named here. No context is given on purpose.

Inputs: two independent readings, /tmp/claude-0/-home-user-cipher-lab/72cf2d66-b26e-52a4-9211-b988f0574d27/scratchpad/P1.tsv and /tmp/claude-0/-home-user-cipher-lab/72cf2d66-b26e-52a4-9211-b988f0574d27/scratchpad/P2.tsv (block<TAB>line<TAB>text, 23 rows), of 23 line crops of a left-margin
note in a 1580s French secretary hand: /tmp/claude-0/-home-user-cipher-lab/72cf2d66-b26e-52a4-9211-b988f0574d27/scratchpad/gl/glA_L01.jpg ... glA_L07.jpg, glB_L01.jpg ... glB_L07.jpg, glC_L01.jpg ... glC_L09.jpg.
Left-edge text is partly lost in the binding; strokes at the far right edge belong to the main text and are ignored; read only the line
whose baseline runs through the middle of each crop.

Procedure: for each row where P1 and P2 differ, open that row's crop (one crop per Read call) and settle each difference from the
image: keep P1's letters, P2's letters, or another reading the crop supports; where neither reading is supported by the image, write '.'.
Where P1 and P2 agree, keep the text unless the crop plainly contradicts both. Keep period spelling; do not modernise or expand
abbreviations without a mark; do not make the note read more fluently than the strokes allow.

Output: one tab-separated file, no header, block<TAB>line<TAB>text, 23 rows, at the path given in your instructions. Then reply with only
the file path, the number of rows you changed from both P1 and P2, and the number of crops you opened.
