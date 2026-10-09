## spinelli-c1519-confirm: 193 scored positions, passes Z, A, B
- Z: 14 wrong-or-deleted of 193 covered positions (insertions not counted here; tx_bench adds them)
- A: 17 wrong-or-deleted of 193 covered positions (insertions not counted here; tx_bench adds them)
- B: 13 wrong-or-deleted of 193 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| Z | 14/193 | 1 (7% of errs; rate 14.3%; base 4%) | 13 (93% of errs; rate 7.1%; base 94%) | 0 (0% of errs; rate 0.0%; base 2%) |
| A | 17/193 | 2 (12% of errs; rate 28.6%; base 4%) | 15 (88% of errs; rate 8.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 2%) |
| B | 13/193 | 1 (8% of errs; rate 14.3%; base 4%) | 12 (92% of errs; rate 6.6%; base 94%) | 0 (0% of errs; rate 0.0%; base 2%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 |
|---|---|---|---|---|---|---|---|---|
| Z | 5/41 | 4/36 | 3/23 | 0/23 | 1/11 | 1/19 | 0/24 | 0/16 |
| A | 6/41 | 5/36 | 3/23 | 0/23 | 1/11 | 1/19 | 1/24 | 0/16 |
| B | 4/41 | 4/36 | 3/23 | 0/23 | 1/11 | 1/19 | 0/24 | 0/16 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | Z | A | B |
|---|---|---|---|---|
| Z | 14 | - | 14/14 (7) | 13/14 (13) |
| A | 17 | 14/17 (7) | - | 13/17 (6) |
| B | 13 | 13/13 (13) | 13/13 (6) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 13; wrong in exactly one: 3

### Top (truth value <- read) pairs per pass, with feature profile

**Z** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| r <- SIX | 4 | 0/0/4 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 4, B= 4 | L01.27 L02.11 L03.4 L05.20 |
| h <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, B= 2 | L01.14 L03.25 |
| u <- JHOOK | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 2, B= 2 | L02.27 L06.21 |
| t <- TEE | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L01.3 |
| i <- EIGHT | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L01.5 |
| e <- SIX | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L01.15 |
| p <- THREE | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L03.16 |
| s <- JHOOK | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B= 1 | L02.3 |
| n <- PHI | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L02.7 |

**A** (17 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| r <- NEW:tall-l-bottom-loop | 5 | 1/0/4 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z~ 4, B~ 4 | L01.27 L02.11 L03.4 L05.20 L07.1 |
| h <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 2, B= 2 | L01.14 L03.25 |
| g <- NEW:circle-with-vertical-stroke | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.17 L02.26 |
| u <- NEW:long-s | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z~ 2, B~ 2 | L02.27 L06.21 |
| t <- TEE | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1 | L01.3 |
| i <- EIGHT | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, B= 1 | L01.5 |
| e <- SIX | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, B= 1 | L01.15 |
| p <- THREE | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, B= 1 | L03.16 |
| s <- NEW:tall-flourish-stroke | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z~ 1, B~ 1 | L02.3 |
| n <- PHI | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, B= 1 | L02.7 |

**B** (13 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| r <- SIX | 4 | 0/0/4 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 4, A~ 4 | L01.27 L02.11 L03.4 L05.20 |
| h <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 2, A= 2 | L01.14 L03.25 |
| u <- JHOOK | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 2, A~ 2 | L02.27 L06.21 |
| i <- EIGHT | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, A= 1 | L01.5 |
| e <- SIX | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, A= 1 | L01.15 |
| p <- THREE | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, A= 1 | L03.16 |
| s <- JHOOK | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, A~ 1 | L02.3 |
| n <- PHI | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, A= 1 | L02.7 |


### Reader agreement on the baseline's errors (baseline Z; 14 errors; passes Z, A, B)

| agree_class | errors | share |
|---|---|---|
| all-same-wrong | 6 | 42.9% |
| all-wrong-split | 7 | 50.0% |
| majority-wrong | 1 | 7.1% |

| err_class | errors | all-same-wrong | all-wrong-split | majority-wrong |
|---|---|---|---|---|
| crop | 2 | 2 (100%) | 0 (0%) | 0 (0%) |
| look-alike | 6 | 0 (0%) | 6 (100%) | 0 (0%) |
| other | 6 | 4 (67%) | 1 (17%) | 1 (17%) |

| truth <- read | n | err_class | all-same-wrong | all-wrong-split | majority-wrong | lines |
|---|---|---|---|---|---|---|
| r <- SIX | 4 | look-alike 4 | 0 | 4 | 0 | L01.27 L02.11 L03.4 L05.20 |
| h <- <deleted> | 2 | crop 2 | 2 | 0 | 0 | L01.14 L03.25 |
| u <- JHOOK | 2 | look-alike 2 | 0 | 2 | 0 | L02.27 L06.21 |
| t <- TEE | 1 | other 1 | 0 | 0 | 1 | L01.3 |
| i <- EIGHT | 1 | other 1 | 1 | 0 | 0 | L01.5 |
| e <- SIX | 1 | other 1 | 1 | 0 | 0 | L01.15 |
| p <- THREE | 1 | other 1 | 1 | 0 | 0 | L03.16 |
| s <- JHOOK | 1 | other 1 | 0 | 1 | 0 | L02.3 |
| n <- PHI | 1 | other 1 | 1 | 0 | 0 | L02.7 |
