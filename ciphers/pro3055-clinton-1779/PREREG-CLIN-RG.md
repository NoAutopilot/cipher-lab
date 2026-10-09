# PREREG CLIN-RG (9 Oct 2026, written and pushed before any score of this design is computed)

Job: CLIN-RG, LANE FAMILY-A2d (account 2). Item: B.148 p.123 (H-1649 Image 1205), the cipher copy of Carleton to Haldimand,
New York, 25 Sept 1782. Second attempt of the whole-page key check after D4-CLIN (8 Oct 2026, PREREG_D4-CLIN.md: registered
length-only alignment FAIL 22/92; addendum B2 FAIL 9/17). Rule 3 third-attempt clause: if this design FAILs, no third pass of it.
Inputs, unchanged and not re-read: passes/p123_full_reconciled.tsv (D4-CLIN, 192 cells), passes/title1778_reading.txt (1778 key),
passes/p102_reading.txt (the period decipherment, read at H, GAPS7) -- prepared exactly as check_p123_full.py's build() does
(decipherment words dw; key variants (a) printed, (b) line 1 "BY PERMISION of the RIGHT HONORABLE", (c) (b)+line 9 "OFICERS in the
several REGIMENTS", (d) (c)+doubled figures). No new vision. Script: passes/check_p123_regate.py (written after this file is pushed).

1. Class rule (fixed, from the page only). Cells in column order, head/clear/skip dropped. A "word" cell (a full pair written without
   x/+) whose preceding kept cell in the same column is a letter cell with underline "n" (an open letter word) is re-classed a letter
   cell starting key line L at position P (the x left off). Applied left to right, so a chain re-classes. Every other cell keeps its
   D4-CLIN kind. Cells are then resolved to absolute (line, pos) and split into tokens as in D4-CLIN: letter words end at an
   underline or at a word code; a word code is a token alone.
2. Anchor per column (the one step that uses the key): the first letter token of >= 3 cells, all graded H, whose decoding under (b)
   equals a decipherment word w exactly (or w with doubled letters written once). If w occurs more than once in dw, the occurrence
   taken is the earliest one after the previous column's anchor word (page order c1..c6; c1 takes the earliest). A column with no such
   token has no anchor and is left out (reported). The anchor token's cells are never scored.
3. Alignment (lengths only after the anchor): tokens after the anchor are aligned to dw starting at the word after the anchor word,
   tokens before it to dw ending at the word before it (reversed), each by D4-CLIN's Needleman-Wunsch scoring (+1 when a letter
   token's cell count equals the word's length or its doubled-letters-once length; 0 for a word code or a misfit; gap -1), the far
   end free. Pairs whose counts fit are compared cell by cell; M-graded cells are dropped.
4. Statistic (GATED): under (b), matched compared cells / compared cells, and the count. (a), (c), (d) reported, never gated.
5. Controls, 1000 seeds each, seed 123:
   K  page-permuted key: the title-page characters permuted across the page (line lengths kept), the same compared positions and
      wanted letters re-scored. Reported also: the full pipeline re-run under each permuted key (anchors re-found), never gated.
   S  shuffled-column: within each anchored column, the order of the non-anchor tokens is permuted (cells keep their resolved
      line-pos; the anchor token stays at its index), re-aligned by step 3 and re-scored under (b). Pre-scoring check (run first,
      printed before any score): the share of seeds whose compared (cell -> wanted letter) set differs from the target's; if
      below 0.95, S is logged a non-test (it cannot differ on this statistic) and the gate stands on K alone.
6. Gate: compared >= 40 AND share(b) >= 0.80 AND count(b) > K max AND (if S is a test) count(b) > S max. Fewer than 40 compared
   cells: non-test, not FAIL. PASS = the 1778 key confirmed on the rest of p.123 as a key check on a text read at H (known-text
   share). FAIL = logged as the second attempt of this design; no third.
