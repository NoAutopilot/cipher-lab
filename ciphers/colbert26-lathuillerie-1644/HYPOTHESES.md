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
