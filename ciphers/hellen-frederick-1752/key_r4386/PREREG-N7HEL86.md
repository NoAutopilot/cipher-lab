# PREREG-N7HEL86 -- blank-cell test of R4386 (BL Add MS 32276 f.75, about codes 1201-2200) on the 1763 letters

Written and pushed 4 Oct 2026 (about 13:2x UTC by `date -u`) by N7-HEL86 (account 2 worker, for LANE-NEAR7), BEFORE the R4386
images are fetched in this session and before any cell is read or counted. Rule 3. The rule is PREREG-N7HELBC's (`../key_r4388/
PREREG-N7HELBC.md`) copied unchanged except for the sheet, the band, the seed and N.

## Target set (computed before reading, `blank_test.py --targets`)
The six 1763 letters (`../ciphertext_R1045..R1048, R1060, R1061.txt`), clean all-digit tokens only: **121 tokens / 63 distinct codes in
1201-2000** (the brief's band; R4386's 2001-2200 is not used, R4388 already covers it and failed).

## Null cells
100 codes drawn uniformly without replacement from 1201-2000 minus the 63 target codes, `random.Random(4386)` (list written to
`cells.tsv` before reading). Target and null cells shuffled together (same seed) into the reading tiles.

## What is read
Per cell only: `F` filled, `Z` the word "zero" (counts as F), `B` blank, `X` crossed out / ink blot only, `?` cannot tell. Not the words.
Cell-to-code attribution: N7-HELDK's head read (one-part, printed 1-1000 form re-numbered by hundreds heads; 1201-2000 over columns 3-10
and 1-2 per the heads). Because N7-HELDK called the head placement "not fully clear", the layout is checked first from the full-size
pages and the attribution rule is pushed here as an addendum BEFORE any cell is read. If the attribution cannot be fixed for a column,
that column's cells are `?` (dropped and counted), not guessed. Two blind Sonnet passes (separate subagent calls, same tiles), then
one reconciliation by this worker from the crops for cells where the passes differ or either says `?`. err_2reader reported.

## Statistic
S = share of the 121 in-range 1763 tokens whose cell is `B` (token-weighted; `X` filled in the primary, blank in a sensitivity line;
`?` dropped and counted).

## Null distribution
p0 = blank share of the 100 null cells. Null of S: 10,000 draws assigning each target code's token multiplicity to a cell drawn with
replacement from the null cells; report p01, p05, median.

## Positive control (subsampled to the target's N)
R4369 on R1953 (`../key_r4369/reading_R1953_tokens.tsv`, U share of in-range 801-1796 tokens, 3.3%), 10,000 bootstrap draws at N = the
scored token count (<=121): report p95, p99. **Power check: control p99 must be below null p01, else NON-TEST at this N** (at N=121
this may fail if the sheet's base blank rate is low; that outcome is logged as NON-TEST, not as a pass or a retirement).

## Pass rule (fixed now)
- **PASS -> candidate for a full transcription**: S <= 0.10 AND S < null p01 (and power OK).
- **FAIL -> R4386 retired as the 1763 key (instrument: blank-cell test)**: S >= null p05 (and power OK).
- Otherwise: inconclusive, logged with the numbers; no third pass.
No threshold is changed after the cells are read.

## Addendum A (13:2x UTC by date -u, after the layout look, before any cell is read; tiles not yet cut)
- Images: one DECODE browser login, R4386 P1-P4 full size to scratch (P2/P3 sha1 a9b8eda3..., cde8d04b..., the same as N7-HELDK).
- Attribution fixed from the full-size heads: each printed column carries two entries per row, a letter string or name immediately
  RIGHT of printed n, and a right-aligned word immediately LEFT of the next printed column's number. The heads 120, 130, ..., 190 stand
  over the right-aligned entries left of printed 201-300, ..., 901-1000; so **code 1000+n (n 201-1000) = the entry LEFT of printed n**.
  Alphabet check (by eye, not a cell read): left of 201 starts "zero, zero, a, ab ...", left of 501 "debiter", left of 601
  "empressement", left of 801 "honneur", left of 901 "le Sieur", left of 1000 "munitions", and the column under head 200 (right of
  printed 1-100) continues "m'y, mystere, n ..." -- one alphabetical run 1201-2100, so the 1201-2000 band is unambiguous. (Printed
  1101-1200 by hand in column 2 carry names right of the number; not in the band.)
- Geometry in `crop_cells.py` (one 3-row band per cell, red arrow on the row, at the right edge, next to the printed number); checked on
  20 layout cells (debug tile, scratch) before the cell list was cut. "zero" = Z, counted F as registered.
