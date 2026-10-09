## ceppo-f36v-gloss: 16 scored positions, passes A, B, D, R, F
- A: 5 wrong-or-deleted of 16 covered positions (insertions not counted here; tx_bench adds them)
- B: 6 wrong-or-deleted of 16 covered positions (insertions not counted here; tx_bench adds them)
- D: 7 wrong-or-deleted of 16 covered positions (insertions not counted here; tx_bench adds them)
- R: 7 wrong-or-deleted of 16 covered positions (insertions not counted here; tx_bench adds them)
- F: 5 wrong-or-deleted of 16 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) |
|---|---|---|---|
| A | 5/16 | 0 (0% of errs; rate 0.0%; base 6%) | 5 (100% of errs; rate 33.3%; base 94%) |
| B | 6/16 | 1 (17% of errs; rate 100.0%; base 6%) | 5 (83% of errs; rate 33.3%; base 94%) |
| D | 7/16 | 1 (14% of errs; rate 100.0%; base 6%) | 6 (86% of errs; rate 40.0%; base 94%) |
| R | 7/16 | 1 (14% of errs; rate 100.0%; base 6%) | 6 (86% of errs; rate 40.0%; base 94%) |
| F | 5/16 | 0 (0% of errs; rate 0.0%; base 6%) | 5 (100% of errs; rate 33.3%; base 94%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 |
|---|---|
| A | 5/16 |
| B | 6/16 |
| D | 7/16 |
| R | 7/16 |
| F | 5/16 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | B | D | R | F |
|---|---|---|---|---|---|---|
| A | 5 | - | 4/5 (1) | 5/5 (1) | 5/5 (1) | 3/5 (3) |
| B | 6 | 4/6 (1) | - | 6/6 (1) | 6/6 (1) | 3/6 (0) |
| D | 7 | 5/7 (1) | 6/7 (1) | - | 7/7 (7) | 3/7 (0) |
| R | 7 | 5/7 (1) | 6/7 (1) | 7/7 (7) | - | 3/7 (0) |
| F | 5 | 3/5 (3) | 3/5 (0) | 3/5 (0) | 3/5 (0) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 3; wrong in exactly one: 2

### Top (truth value <- read) pairs per pass, with feature profile

**A** (5 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- S30 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 3, D~ 3, R~ 3, F= 3 | L01.16 L01.6 L01.9 |
| i <- S66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, D= 1, R= 1 | L01.11 |
| r <- S69 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | D~ 1, R~ 1 | L01.18 |

**B** (6 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- S73 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 3, D~ 3, R~ 3, F~ 3 | L01.16 L01.6 L01.9 |
| p <- S42 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | D~ 1, R~ 1 | L01.1 |
| a <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | D~ 1, R~ 1 | L01.5 |
| i <- S66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, D= 1, R= 1 | L01.11 |

**D** (7 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- ? | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 3, B~ 3, R= 3, F~ 3 | L01.16 L01.6 L01.9 |
| p <- ? | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1, R= 1 | L01.1 |
| a <- ? | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1, R= 1 | L01.5 |
| i <- S66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, R= 1 | L01.11 |
| r <- ? | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, R= 1 | L01.18 |

**R** (7 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- ? | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 3, B~ 3, D= 3, F~ 3 | L01.16 L01.6 L01.9 |
| p <- ? | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1, D= 1 | L01.1 |
| a <- ? | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1, D= 1 | L01.5 |
| i <- S66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, D= 1 | L01.11 |
| r <- ? | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, D= 1 | L01.18 |

**F** (5 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- S30 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 3, B~ 3, D~ 3, R~ 3 | L01.16 L01.6 L01.9 |
| s <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.13 |
| o <- S42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.17 |

