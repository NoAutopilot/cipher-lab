## dint-f128-print: 85 scored positions, passes B, A, F
- B: 11 wrong-or-deleted of 85 covered positions (insertions not counted here; tx_bench adds them)
- A: 14 wrong-or-deleted of 85 covered positions (insertions not counted here; tx_bench adds them)
- F: 14 wrong-or-deleted of 85 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| B | 11/85 | 0 (0% of errs; rate 0.0%; base 1%) | 11 (100% of errs; rate 13.4%; base 96%) | 0 (0% of errs; rate 0.0%; base 2%) |
| A | 14/85 | 0 (0% of errs; rate 0.0%; base 1%) | 14 (100% of errs; rate 17.1%; base 96%) | 0 (0% of errs; rate 0.0%; base 2%) |
| F | 14/85 | 0 (0% of errs; rate 0.0%; base 1%) | 13 (93% of errs; rate 15.9%; base 96%) | 1 (7% of errs; rate 50.0%; base 2%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+2 | L+3 | L+4 | L+5 |
|---|---|---|---|---|
| B | 0/4 | 2/27 | 5/27 | 4/27 |
| A | 0/4 | 3/27 | 8/27 | 3/27 |
| F | 1/4 | 3/27 | 5/27 | 5/27 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | B | A | F |
|---|---|---|---|---|
| B | 11 | - | 10/11 (3) | 9/11 (4) |
| A | 14 | 10/14 (3) | - | 8/14 (4) |
| F | 14 | 9/14 (4) | 8/14 (4) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 8; wrong in exactly one: 9

### Top (truth value <- read) pairs per pass, with feature profile

**B** (11 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| i <- x | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, F= 2 | L04.40 L05.22 |
| n <- 0 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, F~ 1 | L03.26 |
| n <- 4 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, F= 1 | L03.50 |
| n <- # | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1 | L04.5 |
| n <- p | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, F~ 1 | L04.8 |
| g <- 0 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1 | L04.31 |
| i <- 1 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, F= 1 | L04.37 |
| e <- 0 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | F~ 1 | L05.28 |
| n <- t | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, F~ 1 | L05.35 |
| t <- y | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, F~ 1 | L05.36 |

**A** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- t | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 2, F~ 1 | L03.50 L04.5 L04.53 |
| n <- y | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 2, F~ 2 | L04.8 L05.35 |
| i <- x | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 2, F= 2 | L04.40 L05.22 |
| e <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L03.20 |
| n <- 4 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1, F= 1 | L03.26 |
| u <- c | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L04.10 |
| n <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L04.14 |
| g <- o | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1 | L04.31 |
| i <- 1 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, F= 1 | L04.37 |
| t <- 9 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1, F~ 1 | L05.36 |

**F** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- 4 | 4 | 0/0/4 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 3, A~ 3, A= 1, B= 1 | L03.26 L03.50 L04.8 L05.35 |
| i <- x | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 2, A= 2 | L04.40 L04.58 L05.22 |
| i <- 1 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, A= 1 | L03.48 L04.37 |
| t <- 3 | 1 | 0/1/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.8 |
| e <- 0 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L04.42 |
| o <- Z | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L05.2 |
| e <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1 | L05.28 |
| t <- 4 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1, A~ 1 | L05.36 |


### Reader agreement on the baseline's errors (baseline B; 11 errors; passes B, A, F)

| agree_class | errors | share |
|---|---|---|
| all-same-wrong | 3 | 27.3% |
| all-wrong-split | 5 | 45.5% |
| majority-wrong | 3 | 27.3% |

| err_class | errors | all-same-wrong | all-wrong-split | majority-wrong |
|---|---|---|---|---|
| look-alike | 2 | 2 (100%) | 0 (0%) | 0 (0%) |
| other | 9 | 1 (11%) | 5 (56%) | 3 (33%) |

| truth <- read | n | err_class | all-same-wrong | all-wrong-split | majority-wrong | lines |
|---|---|---|---|---|---|---|
| i <- x | 2 | look-alike 2 | 2 | 0 | 0 | L04.40 L05.22 |
| n <- 0 | 1 | other 1 | 0 | 1 | 0 | L03.26 |
| n <- 4 | 1 | other 1 | 0 | 1 | 0 | L03.50 |
| n <- # | 1 | other 1 | 0 | 0 | 1 | L04.5 |
| n <- p | 1 | other 1 | 0 | 1 | 0 | L04.8 |
| g <- 0 | 1 | other 1 | 0 | 0 | 1 | L04.31 |
| i <- 1 | 1 | other 1 | 1 | 0 | 0 | L04.37 |
| e <- 0 | 1 | other 1 | 0 | 0 | 1 | L05.28 |
| n <- t | 1 | other 1 | 0 | 1 | 0 | L05.35 |
| t <- y | 1 | other 1 | 0 | 1 | 0 | L05.36 |
