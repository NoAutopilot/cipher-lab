# PREREG-N7HELBC -- blank-cell test of R4388 (BL Add MS 32276 f.79, codes 2001-3900) on the 1763 letters

Written and pushed 4 Oct 2026 (about 12:4x UTC by `date -u`) by N7-HELBC (account 2 worker, for LANE-NEAR7), BEFORE the R4388
images are fetched in this session and before any cell is read or counted. Rule 3. N7-HELDK's one-reader strip look (11/28 tokens on
blank cells) is the reason for the test and is NOT reused as data.

## Target set (computed before reading, `blank_test.py --targets`)
The six 1763 letters (`../ciphertext_R1045..R1048, R1060, R1061.txt`), clean tokens only (all-digit whitespace tokens; tokens carrying
`?` or `__` are excluded): 1,153 clean tokens; **396 tokens / 270 distinct codes in 2001-3900** (2001-3000: 153 codes / 233 tokens;
3001-3100: 18 / 28; 3101-3900: 99 / 135). Brief said ~180 cells; the clean-token count is 270, stated here before reading.

## Null cells
100 codes drawn uniformly without replacement from 2001-3900 minus the 270 target codes, `random.Random(4388)` (list written by
`blank_test.py --targets` to `cells.tsv` before reading). Target and null cells are shuffled together (same seed) into the reading
tiles, so the readers cannot tell which cells matter.

## What is read
Per cell only: `F` filled (any written word or sign in the cell for that code), `B` blank, `X` crossed out with nothing else, `?`
cannot tell (crop fault). Not the words. Cell-to-code attribution follows N7-HELDK's head read (right of printed n = 2000+n under heads
2000,210..290; left of printed n = 3000+n under heads 310..390; pasted strip 3001-3100). If the images show a different attribution
at the layout step, an addendum is pushed here BEFORE any cell is read. Crops: one per cell, cut by script from the full-size page
(`crop_cells.py`), assembled into numbered tiles carrying only a running tile id (no code number shown beyond what the sheet itself
prints in the crop). Two blind Sonnet passes (separate subagent calls, same tiles, neither sees the other), then one reconciliation by
this worker from the crops for cells where the passes differ or either says `?`. Grades: agreed = reading; reconciled = reading with a
flag. err_2reader is reported.

## Statistic
S = share of the 396 in-range 1763 tokens whose cell is `B` (token-weighted; `X` counted as filled in the primary, as blank in a
reported sensitivity line; `?` cells dropped from numerator and denominator and counted).

## Null distribution
p0 = blank share of the 100 null cells. Null of S: 10,000 draws assigning each of the 270 target codes' token multiplicities to a cell
drawn with replacement from the null cells; report p01, p05, median.

## Positive control (subsampled to the target's N, rule 3 last paragraph)
R4369 on R1953 (the true-key precedent): of 486 clean in-range (801-1796) R1953 tokens, 16 read U for want of a cell value
(`../key_r4369/reading_R1953_tokens.tsv`, 3.3%). Subsampled to N=396 tokens, 10,000 bootstrap draws: report p95, p99.
Power check: control p99 must be below null p01, else the test is a NON-TEST at this N.

## Pass rule (fixed now)
- **PASS -> candidate for a full transcription (~$12)**: S <= 0.10 AND S < null p01.
- **FAIL -> R4388 retired as the 1763 key (rule 3 instrument: blank-cell test)**: S >= null p05.
- Otherwise: inconclusive, logged with the numbers; no third pass.
- A 3001-3100 strip-only S is reported, not gated.
No threshold is changed after the cells are read.
