# PREREG UNA-CLIN (9 Oct 2026, written before any p.124 transcription is read or any score computed)

Item: B.148 p.124 (H-1649 Image 1206, IIIF c0b27pp7jj22), the continuation of the p.123 cipher copy of Carleton to Haldimand,
New York, 25 Sept 1782 (p.123's foot: "Each column is continued on the page following"). Text known: B.148 p.102 period
decipherment, read at H (GAPS7, passes/p102_reading.txt) -- the known answer. Key: the 1778 Army List title page,
passes/title1778_reading.txt, variant (b) (line 1 = "BY PERMISION of the RIGHT HONORABLE"), as D4-CLIN's B2. This is a key-consistency
check on a text already read at H, not a reading.

Retired, not used: whole-page / per-column alignment (D4-CLIN length-only, CLIN-RG anchored; rule 3 third-attempt clause).

Transcription: Image 1206 full/max to the scratchpad; columns cut by `SHEAR=0.012 PAD=0 python3 passes/cut_2380_p121_122.py IMGDIR OUT 1206`
(box for 1206 with its own bottom-half boxes and no shear, since the columns fan out); crops committed under images/h1649/p124_cols/.
Two blind Sonnet passes (column crops only; no key, no p.102, no p.123 data, not told the question), then one worker reconciliation
on the crops of every A/B disagreement. passes/p124_reconciled.tsv; a cell still open after reconciliation is graded M.

Cell classes (from the page only, never from the decipherment):
- "x" or "+" before a full pair = letter cell starting a new key line; "-P" = letter cell on the current line.
- A full pair without x/+ = a 1782 word-code element. **A full pair without x inside an un-underlined letter run is classed as a word
  code (the registered rule R0: it ends the run before it and starts a fresh run after it). No exception from context.**
- A clear word on the page (column 6's head) is not a cell; it ends a run. An underline ends a run.
- Reported apart, never gated: rule R1 (CLIN-RG's: a full pair without x with a letter cell directly before it, no underline under
  that letter cell, and a letter cell directly after it = a letter cell on a new line).

Statistic B2 (D4-CLIN Addendum B, unchanged): decode every letter cell on the key; split into runs at underlines, word codes and clear
words; keep runs of >= 3 cells all graded H; a run is a hit when its decoded string occurs as a substring of the p.102 decipherment
letters (spaces and punctuation removed; '?' -- a position beyond its line -- never matches). B2 share = hits / runs.
Control (rule 3): the title-page characters permuted across the page, line lengths kept, 1000 seeds, seed 123, the same runs.
Pre-scoring checks, run first and pasted: (i) can-differ: the share of control seeds on which at least one run decodes to a different
string than under the real key; below 0.99 = NON-TEST. (ii) floor: runs_ge3 >= 10; below it = NON-TEST.
**Gate: B2 share >= 0.60 AND hits > control max.** Threshold fixed here, the same 0.60 as D4-CLIN's B2 on p.123 (not re-tuned).
Reported, not gated: R1's share and hits; each hit's position in the p.102 text and whether column k's hits continue where p.123's
column k ended (D4-CLIN's decoded runs); the word codes with any interlinear gloss.

A PASS says only that the 1778 key reads p.124's letter runs as the p.102 text beyond its permuted-key control; no reading changes,
AUDIT.md is not touched, grades of the letter stay as GAPS7. A FAIL or NON-TEST is logged as such, with both numbers.
Scorer: passes/check_p124.py (--check exits 1 when check_p124.json is stale, rule 7).
