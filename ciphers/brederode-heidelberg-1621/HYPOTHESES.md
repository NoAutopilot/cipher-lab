# HYPOTHESES -- brederode-heidelberg-1621

## Unit inventory vs nl16 (HEID-1621D, 15 Oct 2026; PREREG t1/PREREG-HEID1621D.md; t1/inventory.py --check; seed 1621)
| hypothesis | control | control number | gate | target number | outcome |
|---|---|---|---|---|---|
| word-level code (K at N=45 inside the nl16 word-window band) | C1 held-out word vs letter windows (coor001boev01), nearest pool median | 1.000 | 0.90 | K=25 (tuple), 30 (tuple+letter); word pool median 38, p05 32, p95 42; target pct 0.003 (0.021) | undecided: below the word band |
| syllable-sized unit | C1 syllable-proxy vs word | 0.000 (pools coincide at N=45) | -- | syllable-proxy pool median 38, p05 32; pct 0.002 | not testable by inventory at this N |
| letter-level unit | C1 word vs letter | 1.000 | 0.90 | letter pool median 17, p95 20; pct 1.000 | above the letter band |
| frequency rank-match of units to the nl16 word list | C2 synthetic word code at N=45, 20 held-out windows (K=32, nearest to 25) | 0.010 mean (max 0.067) | 0.50 | not run | CONTROL BELOW GATE: non-test at this N |

## Letter-sign look-alike pass + pooled test 1 (HEID-1621H, 15 Oct 2026; PREREG heid1621h/PREREG-HEID1621H.md; heid1621h/letters.py and pooled.py --check; seed 1621)
| hypothesis | control | control number | gate | target number | outcome |
|---|---|---|---|---|---|
| trailing letters transcribable at S (after look-alike pass) | 375 vs 379 per-unit agreement, post-pass units | 37/45 = 0.822 (unchanged: 22 split positions, 0 settled -- no re-read possible, crops not on disk) | 0.90 | -- | CONTROL BELOW GATE: letters stay M; letter field unreliable in the spec |
| pooled inventory, key KT (numeral tuple as transcribed), word-level code at N=59 | C3 synthetic word code (45/14 division, 423 form split), share in word band | 0.593 | 0.90 | K=36 | CONTROL BELOW GATE: non-test, band not read |
| pooled inventory, key KF (single = first number) | C3 same, key KF | 0.777 | 0.90 | K=29 | CONTROL BELOW GATE: non-test, band not read |
| rank-match of units to the nl16 word list at N=59 | C2 held-out windows K 35-39 | 0.017 mean (max 0.119) | 0.50 | not run | CONTROL BELOW GATE |
| 17 Sept single = 13 Aug pair's first number (numbers only) | value null (uniform 10-84), mean 3.35 | p 0.089 | p < 0.01 | 6/12 | not significant |
| 17 Sept single = either number of a 13 Aug pair (numbers only) | value null, mean 5.76 | p 0.013 | p < 0.01 | 10/12 | not under the threshold |
| a number shared by both letters carries the same letter sign (first / either) | shuffled-pairing null (letters permuted over the 12 S1 numbers), means 1.09 / 2.25 | p 0.0002 / < 0.0001 | p < 0.01 | 6/12 / 9/12 | counted lead (M; letters M): supports "two letters, one key"; not a key, not a reading |
