# craven-rupert-1648 -- hypotheses and their matched controls (rule 3)

| date | by | hypothesis (table applied to R8447, N=41) | target | control | verdict |
|---|---|---|---|---|---|
| 8 Oct 2026 | D2-CRAV (registered WL gate) | each of T_8446, T_8446x, T_8448, T_8445, T_NR | WL 0 for all five; COV 6/14/4/2/8 | shuffled-key WL p99 12/14/15/7/0; random-code COV p99 8/12/8/8/17; matched-design self-enciphered control passes 0/1/0/0/14 of 20 | NON-TEST for all five: WL has no power at N=41 in seven short lines |
| 8 Oct 2026 | D2-CRAV (amendment A1, coverage exclusion) | R8447 enciphered with R8446's key (attested sample T_8446) | COV 6 | key-true p01 22 (median 29), random-code p99 8 | EXCLUDED |
| 8 Oct 2026 | D2-CRAV (A1) | R8447 enciphered with R8446's two odd letter series, extended (T_8446x, grade I table) | COV 14 | key-true p01 41 (median 41), random-code p99 11 | EXCLUDED |
| 8 Oct 2026 | D2-CRAV (A1) | R8447 enciphered with Jermyn's 19 Nov 1648 key (T_8448, sample) | COV 4 | key-true p01 34 (upper bound), random-code p99 8 | EXCLUDED (control is an upper bound: our pairs are a sample of the key) |
| 8 Oct 2026 | D2-CRAV (A1) | R8447 enciphered with the London 1 June 1648 key (T_8445, sample) | COV 2 | key-true p01 25 (upper bound), random-code p99 8 | EXCLUDED (same caveat) |
| 8 Oct 2026 | D2-CRAV (A1) | R8447 enciphered with the Nicholas-Rupert July 1645 letter table (Tomokiyo) | COV 8 | key-true p01 29, random-code p99 17 | EXCLUDED (letter part only; the word series 98-373/427-616 are unpublished) |
| 8 Oct 2026 | D2-CRAV | THE=g4 (Tomokiyo's reconstruction from 18982 f.79) | -- | -- | not tested: no published table found |

Scripts: test2/key_family_test.py --check, test2/coverage_exclusion.py --check. PREREG: PREREG-D2-CRAV.md (registered 85370ca81, A1 670996f9d).
All negatives are conditional on the two-pass transcription (95.3% agreement) and on single-reader M-grade sibling pairs.
