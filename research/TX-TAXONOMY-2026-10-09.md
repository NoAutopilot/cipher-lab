# TX-TAXONOMY: where the transcription errors are (LANE TX-ENGINEER round 1, 9 Oct 2026, account 4, Fable)

No reads were made. Every number comes from the passes already on disk, aligned to the BENCHMARK-TX truth files by
`tools/tx_taxonomy.py` (new, `tools/tests/test_tx_taxonomy.py`; the alignment is `tools/tx_bench.py`'s own, so the error
counts match the figures in TRANSCRIPTION.md to the insertion). Per-position tables: `benchmark-tx/taxonomy/<item>_positions.tsv`;
per-item summaries with every class table: `benchmark-tx/taxonomy/<item>_summary.md`. Regenerate with the commands in the
tool's docstring (no.87 takes `--boxes atlas/signs.tsv --box-token atlas/no87_box_token.tsv --harvest harvest` for the
geometry columns; the dev items have no box<->token map and get position and correlation columns only).

Passes read, no.87 (eval, 803 scored): A, B (the two blind Sonnet passes), C (reconciled, committed), L (C + NO87-LABELS
relabels, today's 0.045), E (TX-SHEET: Sonnet with the per-hand exemplar sheet), F (TX-FABLE), pad / s125 / warp (TX-VIEWS,
f.178r+f.179r only, 164 signs). Dev: Ceppo f.21v (A, B, C, F), f.87 (A, B, C, F), f.36v gloss (A, B, D, recon, F), Dinteville
f.128 (A, B, F, label-mapped). Wrong-or-deleted counts below leave insertions out (tx_bench adds them: A 55 = 54 + 1).

## 1. Birago 1572 hand (no.87, eval): the three classes that carry the mass

| class | mechanism | mass in pass A (54) | in C (43) | in L (36) | in F (73) | fixable by |
|---|---|---|---|---|---|---|
| **1. Inventory look-alike pairs** -- the hand's form sits between two sheet cells (or on none) | the 51-cell sheet shows one printed exemplar per cell; the hand's d (T18) / s (T98) differ by descender length, p (T90) / t (T53) and n (T76) / e (T66, T86, T45) by a loop, h (T64) / l by a tail; the curled Ce (s) is on no cell at all | top five pairs 22 (41%), with the same-shape singles 27 (50%) | 22 (51%) / 27 | 15 (42%) | 8 (m <- X_NEW: the m with curved foot filed off-sheet) + the same pairs | compare-don't-recall against the hand's own tiles under the key, not a richer sheet (E added hand tiles and s <- T50 went 7 -> 15) |
| **2. Crop geometry** -- pixels the reader never saw, or saw twice | (a) f.178r L03's sloping tail (pos 24-34) leaves the fixed band: deleted by every blind reader, recovered only by C's sloped re-crop; (b) the line band cuts 14% of the mapped boxes top or bottom (descenders): error rate there 9.5% vs 5.2% inside; (c) the brief says s1/s2/s3 overlap "about 100 px at 2x", the manifest boxes overlap 425 native px (5-6 signs): F de-duplicated by sequence matching and over-deleted (r, a, i, e, l <- deleted on L01-L02 pos 22-29, 10 signs) | 8 tail + 11 band-cut = 19 (35%; 4 of them also class 1) | 10 band-cut (23%) | 10 (28%) | 18 f.178r deletions + 12 band-cut = 30 (41%) | adaptive band height (ink extent, descender-aware), sloped bands, a truthful overlap statement in the brief, a second crop set shifted half a line |
| **3. Thin strokes** | hairline ink loses the tick or tail that separates the pair; the crops are native resolution (1250 px for about 30 signs, about 40 px a sign) | 20 of the 40 mapped errors (50%) at 29% base; rate 8.5% thin vs 4.2% mid/heavy | 16 of 36 (44%); 6.8% vs 4.2% | 13 of 29 (45%); 5.5% vs 2.9-3.8% | 22 of 42 (52%); 9.4% vs 4.2% | per-sign tiles at 4x with contrast (the UNA-BIR3252 route, 5/6 known-answer on f.36-37), targeted at the thin tercile only |

The classes overlap: of A's 8 T18/T98 confusions 4 are band-cut and 5 thin; of all 28 mapped T18/T98 positions 14 are
band-cut (base 14%) and the confused boxes are 7 px shorter than the pair's mean (94 vs 101). The d/s pair -- today's largest
single confusion -- is a descender the band cuts and the ink fades, read against a sheet cell that shows the full tail.

**The floor.** 20 of 803 positions (2.5%) are wrong in every one of the six full passes (A, B, C, L, E, F), 9 of them read
with the same sign by every reader (T70 for s at L02.19, T42 for g, T90 for t twice, T96 for e, T80 for r, T60 for z, T36 for e,
T76 for e). 34 of A's 54 errors are shared with B with the same wrong sign (63%): on this hand the two readers do not fail
independently, and reconciliation can only halve a single pass (0.069 -> 0.053), which is what it did. A third reader of the
same kind cannot cross this floor (TX-VIEWS: the views repeat 13-14 of A's 14 errors; TX-FABLE: 31 of F's 73 errors are A's).
Whether the 9 unanimous positions are the clerk's sheet, the key's homophone list or the hand is a question for the sorter
(round 3), not for another reader.

**Non-findings, so rounds 2-3 do not build for them.**
- Segment overlap zone (s1/s2 and s2/s3, 31% of mapped signs): A 4.4% vs 6.3% inner -- not elevated. The overlap itself is
  not where errors sit; the brief's wrong overlap figure is (class 2c, and only F fell for it).
- Fatigue by call position: no monotone trend in any pass (A by line index within the call: 6.4, 4.3, 14.3, 3.8, 10.2, 3.4,
  1.8, 3.6, 5.5, 10.9, 7.4, 8.3, 3.4%); the peaks are f.178r L03 (the tail) and f.178v L05/L10 (band-cut T76/T98 lines), not
  the end of a call. Capping signs per call is not indicated on this hand.
- First sign of a line: 16% (4 of 25) vs 6.5% inner -- real, 4 errors; last sign: 1 of 24. Too little mass to build for.
- Glued pairs (the segmenter's 2:1 boxes, 22 positions): A 1 error (4.5%) -- the segmenter's glue is not the readers' problem.
- Reader-specific bias, removed by reconciliation when the other reader has it right: B's r <- T24 x15 on f.178r (T83 r read
  as T24 f throughout one call; A right on all 15); F's m <- X_NEW x8 (L11-23). A one-call bias is cheap to catch with a
  per-call confusion count against the other pass (reconcile_passes already lists the disagreements; a flag on "one pass
  reads the same cell for >= 5 of the other's X" would name it).

## 2. Ceppo-Nevers hand (dev: f.21v 189, f.87 139, f.36v gloss 16)

| class | evidence | mass |
|---|---|---|
| **1. The n-cells split** (S30 / S73 / S97 against truth n) | B on f.21v n <- S73 x5 + n <- S97 x5; F n <- S30 x4; A, C n <- S73; f.36v L01 pos 6, 9, 16: every reader wrong, each on a different n-cell (A S30, B S73, D/recon `?`, F S30) | 17 of 42 errors over A, B, F on the three items; 3 of 16 on f.36v for all five passes |
| **2. One-call substitution bias** (a <- S65; o <- S88) | A on f.21v a <- S65 x8 of 9 errors (B 0 of them: A-B share 1 of 9 positions); f.87 a <- S65 (B 2, C 3), o <- S88 (B 3, C 4, F 4, same sign) | 8 of A's 9 on f.21v; 7 of C's 7 on f.87 |
| **3. The Fable collapse on f.87** | 36 errors over 20+ pairs (e <- S56 x4, o <- S88 x4, r/g <- S69, c <- S25/S20, m <- S77/S37, a <- S23 ...), 0 of them shared with A | 36 of 139 (0.295): a reader-level failure, not a class |

On f.21v A and B fail independently (1 shared position of 19), so reconciliation leaves 1 error; on f.87 B and C share 6 of 8
(C sided with B and the S-truth is the committed decode, so this item cannot separate B's bias from the truth's). The
f.36v line is 16 signs and every pass is at 0.31-0.44: the three n-signs are the whole story there.

## 3. Dinteville 1592 hand (dev: f.128 85 scored, label-mapped)

| class | evidence | mass |
|---|---|---|
| **1. The n-sign has no anchor** | A n <- t x3, y x2, 4, <deleted>; B n <- 0, 4, #, p, t; F n <- 4 x4. A and B are wrong on 10 of the same 14 positions but read the same wrong sign on only 3: the sign is hard, not biased | A 7 of 14, B 5 of 11, F 4 of 14 |
| **2. Agreed-wrong digit look-alikes** (i <- x, i <- 1) | all three readers, same sign, L04.37/40, L05.22 (+ F L03.48, L04.58) | 3 per pass |
| **3. Segmentation of glued digit groups** | A 2 deletions, F 9 insertions (TX-FABLE: more signs per line than B) | 2-9 per pass |

## 4. What this decides for rounds 2-3

Round 2 builds three instruments, one per Birago class, each pre-registered on dev and reported on eval with `--paired`
against L (0.045):

1. **Compare, don't recall** (class 1, half of today's mass and the whole floor): per-sign tile beside the atlas's top-3
   exemplars of the hand under the key's value constraint, the reader picks among shown candidates or "none"; resolved by
   `tools/key_decode_lattice.py`. Scored first on the 28 T18/T98 and the 23 T76 positions (where the pair is named), then whole.
2. **Crop geometry** (class 2, a third of A's mass and most of f.178r's excess): `iiif_lines.py` band height from the ink
   extent with a descender margin, sloped bands, a second crop set shifted half a line and read only where the two sets
   disagree; the brief's overlap sentence generated from the manifest, never typed.
3. **Thin-stroke targeted re-read** (class 3): the thin tercile only (29% of signs, half the errors), as 4x per-sign tiles
   with contrast, a yes/no "is it A or B" against the pair the lattice names -- never a whole re-pass (TX-VIEWS, phi 0.71-0.76).

Position effects, segment-overlap voting and fatigue capping are not built (section 1, non-findings). For the Ceppo and
Dinteville hands the first instrument is the same as Birago's class 1 (n-cells, the Dinteville n-sign): the compare-don't-
recall tool is hand-agnostic and is scored on f.21v/f.87/f.128 as dev before no.87.

Third hand for the benchmark (brief: fr2980-gramont f.29r, birago-fr3252 f.117): neither qualifies today. Gramont f.29r has
one reader plus a second-reader correction pass (NOTES "Second reader: changes applied"), grades H 533 / M 30 / U 5 from a
key recovered by us, no period or published key sheet and no two raw blind passes on disk. fr.3252 f.117 has two raw blind
passes (passA/passB_L01-04, 165/159 signs) but no known answer: no gloss, no clerk sheet, and the Ceppo-Nevers key reads it
only as a candidate (judge z 3.33 on pass A). The lodewijk WVO letters are digits. So no third hand is added; the eval set
stays no.87 alone, and the dev set carries the Ceppo and Dinteville hands.
