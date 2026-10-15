# PREREG CLIN-SIB (15 Oct 2026, written before any blind pass is read and before any score is computed)

Job CLIN-SIB, LANE DEFAULT-A1-0206-15 (account 1). Item: B.147 p.243 (H-1649 Image 887, IIIF c0j96066137x; BL Add MS 21807 fo.206v),
the middle page of the cipher copy of item 3050 (PRO 30/55/26/2; Clinton to Haldimand, New York, 2 Oct 1780; cipher pp.242-244 =
Images 886-888). Chosen as the sibling page with the longest pure cipher run named in Remaining gaps ("the rest of 3050/3077 (p.242
cols 4-6, pp.243-244, p.247 cols 3-8)"): four columns of figure cells, about 110 cells, few clear words (p.244 has three short
columns; p.247 cols 3-8 are mixed with clear runs). Text known: the period decipherment B.147 p.245 (Image 889), read at H by GAPS12
(passes/p245_reading.txt) -- the known answer. Key: the 1778 Army List title page, passes/title1778_reading.txt **as printed
(variant a, line 1 "BY PERMISSION of the RIGHT HONOURABLE")**, because GAPS12 found the 3050/3077 line-1 cells fit the printed line 1
(unlike 2380); fixed here from GAPS12, not from this page. Variant (b) (line 1 "BY PERMISION ... HONORABLE", UNA-CLIN's) is
reported, not gated. A key-consistency check on a text already read at H, not a reading.

Retired, not used: whole-page / per-column alignment (D4-CLIN, CLIN-RG; rule 3 third-attempt clause).

Transcription: Image 887 at 3200 px to the scratchpad (not committed); four columns cut with tools/iiif_lines.py --image
(--region per column, --centres every 44 px, --lines-per-crop 13, --overlap 40 -> two crops per column, eight crops; command in
NOTES). Two blind Sonnet passes on the eight crops only (no key, no p.245 text, no other page's data, not told the question), then
one worker reconciliation on the crops of every A/B disagreement. passes/p243_reconciled.tsv; a cell still open after
reconciliation is graded M. Crops stay untracked (lane rule: no images in git); images/h1649/p243_cols/manifest.json and the
regen command are committed.

Cell classes (from the page only, never from the decipherment), the 1780 convention of p242_p247_cells.tsv / check_3050_3077.py:
- "L-P" (a full pair) = letter cell, position P on key line L; "-P" = letter cell, position P on the current line.
  (No 1782 word codes in the 1780 copies; every figure cell is a letter cell.)
- A clear word on the page is not a cell; it ends a run. An underline ends a run (it closes a cipher word).

Statistic B2 (UNA-CLIN's, the class rule above in place of the 1782 R0): decode every letter cell on the key; split into runs at
underlines and clear words (a run never crosses a column); keep runs of >= 3 cells all graded H; a run is a hit when its decoded
string occurs as a substring of the p.245 decipherment letters (the body from the line after "Sir" to "Colonies", spaces and
punctuation removed, '&' kept; '?' -- a position beyond its line -- never matches). B2 share = hits / runs.
Control (rule 3): the title-page characters permuted across the page, line lengths kept, 1000 seeds, seed 123, the same runs.
Pre-scoring checks, run first and pasted: (i) can-differ: the share of control seeds on which at least one run decodes to a different
string than under the real key; below 0.99 = NON-TEST. (ii) floor: runs_ge3 >= 10; below it = NON-TEST.
**Gate: B2 share >= 0.60 AND hits > control max.** Threshold the same 0.60 as D4-CLIN and UNA-CLIN (not re-tuned).
Reported, not gated: variant (b)'s share and hits; each hit's position in the p.245 text; the clear words in order.

A PASS says only that the 1778 key reads p.243's runs as the p.245 text beyond its permuted-key control; no reading changes, AUDIT.md
is not touched, grades of the letter stay as GAPS12. A FAIL or NON-TEST is logged as such, with both numbers.
Scorer: passes/check_p243.py (--check exits 1 when check_p243.json is stale, rule 7).
