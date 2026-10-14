# colbert26-lathuillerie-1644 -- hypotheses and per-code tests (append-only)

Created by D2-COL26 (8 Oct 2026). Earlier tests are recorded per job in NOTES.md (A2-COL6 ... DA1-COLV); this file starts the
side-by-side control/target register (CLAUDE.md rule 3) from here on.

## D2-COL26, 8 Oct 2026: sibling values of the six codes DA1-COLV lowered to M, value-independent units

PREREG-D2-COL26.md (pushed 65d490d04 before the run); siblings/d2col26_test.py; output siblings/d2col26_test_out.txt.
Units outside every R10-COL26B value-choice unit: c30 (failed its own instrument: anchor 17 vs L p95 18, excluded), c33, c51, c62
(cleared). Statistic: anchor-bracketed ordered walk at line grain. Gate per code: P < 0.05/6 under length-matched (L) AND
shuffled-gloss (S) controls, N >= 5, power floor P_min(L) < 0.0083.

| code | value | target H/N | L mean / p95 / P | S mean / p95 / P | verdict |
|---|---|---|---|---|---|
| 20 | i | 8/10 | 3.64 / 6 / 0.0093 | 3.37 / 6 / 0.0029 | FAIL (L P above 0.0083) |
| 30 | s | 19/22 | 8.21 / 12 / 0.0000 | 13.36 / 17 / 0.0062 | PASS |
| 67 | leur | 0/0 | - | - | TOO-SHORT |
| 81 | me (il) | 2/2 (0/2) | - | - | TOO-SHORT |
| 85 | na (luy) | 0/2 (0/2) | - | - | TOO-SHORT |
| 96 | que | 5/8 | 0.86 / 3 / 0.0032 | 1.20 / 4 / 0.0053 | PASS |

Verifier D2V-COL26 (8 Oct 2026, AUDIT.md addendum): the table above re-runs byte-identical (script fixed to run at HEAD); registration,
OUT status, controls and threshold hold. Propagation to f.23: 2 of the 17 f.23 tokens of 30 sit in own-gloss words with no s and are
lowered to M (exceptions_f23.tsv); f.23 C 127 -> 125.

## COL26-C29 (13 Oct 2026): canvas 29 (folio 26, 30 Mar 1646) known-answer and held-out tests (PREREG-COL26-C29.md, 4628221f)

| hypothesis | statistic | target (pass A / pass B) | control | verdict |
|---|---|---|---|---|
| key_f24 C codes (16, 25, 31, 51, 83, 92) hold on canvas 29 | positional known answer, WIN 0.25 | A 2/5, B 4/6 | R rotation p95 3 / 5 (P 0.62 / 0.32); L length-matched p95 3 / 3 (P 0.26 / 0.015) | FAIL (B passes L only) |
| 42 = si (held-out) | same, per code | A 0/3, B 0/3 | R max 0 (no gloss contains si: non-discriminating) | FAIL by rule; licenses nothing either way |
| 11 = le (held-out) | same | A 2/2 (P_min 0.069), B 3/3 (P 0.014); pooled with f.24 A 10/14, B 11/15 | R p95 2 / 2; pooled p95 8 / 9 | SPLIT on canvas 29, pooled PASS; not licensed |
| 6 = je (held-out) | same | A 0/3, B 0/4 | R max 0 (non-discriminating) | FAIL by rule; D07 scored side already FAILed |

## COL26-42 (13 Oct 2026, PREREG-COL26-42.md)

| hypothesis | statistic | target | control | verdict |
|---|---|---|---|---|
| 42 = s(ieur) (held-out canvas 20-21 + f.24, N 6) | positional known answer, WIN 0.25, s(ieur) tokens vs si | not computed | rotation / value-shuffle: 0 by construction (0/31 held-out units carry an s(ieur) token) | NON-TEST at the registered power check; licenses nothing either way |

## COL26-WP, 13 Oct 2026: canvas 20-21 leads 42 = si, 11 = le, 6 = je at word grain

PREREG-COL26-WP.md (pushed 82122f874 before any pairing or score); interlinear/c20c21_word_wp.py; output interlinear/c20c21_word_wp_out.txt.
alpha 0.05/44 (selection-corrected). Control W = gloss words permuted over word spans within each unit.

| code | value | control (known answer 83 de + 31 que) | target | verdict |
|---|---|---|---|---|
| 42 | si | stage 0: 31 que at N 4 best-case P_min 0.0020 | best-case P_min 0.0079 (N 4) | NON-TEST (underpowered at N 4) |
| 6 | je | as above | best case 1/4, P_min 0.25 | NON-TEST |
| 11 | le | instrument 3/9 vs p95 4, P 0.261 (FAIL) | not scored | NON-TEST (instrument) |

## COL26-11B, 13 Oct 2026: canvas 20-21 11 = le, second blind word-pairing pass

PREREG-COL26-11B.md (pushed 28c1312e0 before pass 2); instrument interlinear/c20c21_word_wp.py unchanged; wrapper
interlinear/c20c21_word_wp_pool.py; outputs interlinear/c20c21_word_wp_pool_out.txt, interlinear/c20c21_word_wp_p2_out.txt.

| hypothesis | control | target | verdict |
|---|---|---|---|
| 11 = le (word-level pairing, pooled two passes) | instrument 83 de + 31 que: H 3/8 vs Control W mean 1.60, p95 3, P 0.191 | not scored | NON-TEST; untested-by-this-tool (second attempt, readers agree 0.862 exact) |

## COL26-C33, 14 Oct 2026: canvas 33 20 = i, word-level pairing, two blind passes

| hypothesis | control | target | verdict |
|---|---|---|---|
| 20 = i (word-level pairing, c33, held out) | instrument key_f23 pre-DA1-COL C codes: p1 H 8/25 vs Control W mean 2.93, p95 6, P 0.0029; p2 8/26 vs mean 3.10, p95 6, P 0.0068 (both CLEAR) | p1 2/5 vs mean 0.56, p95 2, P 0.096; p2 2/5 vs mean 0.57, p95 2, P 0.092 (alpha 0.00833) | FAIL-LOWPOWER (power at N 5: 0.06/0.05); not a negative |

## COL26-C51, 14 Oct 2026: 20 = i, pooled held-out word grain (c33 + c51 + c63), stage 0

| hypothesis | control | target | verdict |
|---|---|---|---|
| 20 = i (word-level pairing, pooled held-out c33 + c51 + c63; c62 excluded, instrument failed) | power rule on the pre-DA1-COL C-code pool (c33 + c63, 47/48 occ, hit 0.32 vs Control W 0.12): power at N 10 = 0.163 (c33 p1), 0.120 (c33 p2) | not scored (no c51 pairing made) | TOO-SHORT at pooled N 10 (power < 0.5); ~25 needed, 10-11 exist; not a negative |
