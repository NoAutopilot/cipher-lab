# PREREG-R7VIV53G (6 Oct 2026, R7A-VIV53, account 1 worker for LANE LANE-RUN7-account-1)

Written and pushed BEFORE any window of a gap tile is cut or re-read, and before any re-decode. Ink 53 (fr.16104 ff.170r-171v). The
N7-VIV53L reading (reading_piece53_L.tsv, piece53_L_decode.txt) was on file and seen. key.tsv unchanged. No 53L file is edited; all new
files carry `53G` in their name.

## Inputs (frozen)
tx/lookalike53L/<page>/53L_<page>_tiles.tsv rows with status `gap` (one reader only; 42 / 103 / 38 / 87 rows, deduplicated on
(passage, pos)), tx/lookalike53L/<page>/passD.tsv (the N7-VIV53L primary sequence), agreement.tsv, the p53 line crops regenerated from
images/p53/manifest.json. Window instrument = tx/viv53L_windows.py's window()/montage() unchanged (estimated x = pos/len along the inked span).

## (i) Re-read
Per gap tile one window; candidates = the tile's own `candidates` cell (the present reader's label + its confusion partners) plus
`NONE` ("no separate sign at this point: the tick falls on part of a neighbouring sign or blank space"), alphabetical, value-blind, the
present label never singled out. Mixed in as decoys (shuffled order, same caption style, the answer hidden in tx/lookalike53G/decoys.tsv):
12 agreed tiles per page (status `agree`, both readers, drawn with random.Random("R7VIV53G-decoy")), candidates = agreed label + its two
top confusion partners (tx/lookalike53L/confusion.tsv) + NONE. One Sonnet call per page, montages only (never a full page).

## (ii) Control gate (decoys) -- checked before any gap answer is folded in
Over the 48 decoys: correct = firm (H/M) answer equal to the agreed label; false-NONE = firm NONE. The gap fold-in is applied only if
correct >= 0.80 AND false-NONE <= 0.10. Otherwise the gap re-read is a NON-TEST: nothing is applied and the reading stays N7-VIV53L.
Echo check reported (gap answers = present label / NONE / other).

## (iii) Fold-in rule (fixed 2-of-3; the absent reader counts as a vote for NONE)
- firm answer == present label (after reconcile_vivk.MAP + '+'->'4', i.e. same code) -> settled present (2 of 3): the token loses its gap flag.
- firm NONE -> settled absent (2 of 3): the token is removed from the sequence.
- anything else (L, SPLIT, X_NEW, another candidate) -> unchanged: kept, flagged M (a third reader alone does not relabel).
Then the N7-VIV53L steps unchanged ("o o" -> oo, ': :' join, grades). Never "what decodes better".
The 82 UNSETTLED split tiles are not re-read in this job unless cap allows after the gap pass; if they are, the same window, candidates
from their tile row, NO NONE option, and the PREREG-N7VIV53L 2-of-3 rule.

## (iv) Gates and statistic, rule unchanged from PREREG-N7VIV53L (iv) and (ii)
b2 (tx/viv63_test.run, fr16, 200 letter-order shuffles, controls C1 f.103r and C2 ink 54 first) and (c) 200 wrong keys, seed "20261053G".
Stretch statistic: viv53L_stretches top()/runs() with vocabulary V_strict = fr16 forms (tx/viv53L_stretches.vocab folding) with
count >= 100 and length >= 3, plus viv54L_stretch.STRICT_SHORT; computed on BOTH the 53L (before) and the 53G (after) decodes, with
200 letter-order shuffles (seed "20261053G-stretch"), real top-1/top-3 vs null median/p99. Listed liberties as AUDIT 2 4a. A stretch
over ~42 letters is reported with its span and left to a verifier; no depth edit.
