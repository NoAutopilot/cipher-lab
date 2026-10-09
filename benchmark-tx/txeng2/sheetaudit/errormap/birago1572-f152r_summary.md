## birago1572-f152r: 73 scored positions, passes Z, A, B
- Z: 4 wrong-or-deleted of 73 covered positions (insertions not counted here; tx_bench adds them)
- A: 5 wrong-or-deleted of 73 covered positions (insertions not counted here; tx_bench adds them)
- B: 4 wrong-or-deleted of 73 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| Z | 4/73 | 0 (0% of errs; rate 0.0%; base 4%) | 4 (100% of errs; rate 5.9%; base 93%) | 0 (0% of errs; rate 0.0%; base 3%) |
| A | 5/73 | 0 (0% of errs; rate 0.0%; base 4%) | 5 (100% of errs; rate 7.4%; base 93%) | 0 (0% of errs; rate 0.0%; base 3%) |
| B | 4/73 | 0 (0% of errs; rate 0.0%; base 4%) | 4 (100% of errs; rate 5.9%; base 93%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 |
|---|---|---|---|---|
| Z | 0/5 | 1/23 | 1/25 | 2/20 |
| A | 0/5 | 2/23 | 1/25 | 2/20 |
| B | 0/5 | 1/23 | 1/25 | 2/20 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | Z | A | B |
|---|---|---|---|---|
| Z | 4 | - | 3/4 (3) | 4/4 (4) |
| A | 5 | 3/5 (3) | - | 3/5 (3) |
| B | 4 | 4/4 (4) | 3/4 (3) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 3; wrong in exactly one: 2

### Top (truth value <- read) pairs per pass, with feature profile

**Z** (4 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L02.18 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1 | L03.8 |
| a <- T52 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L04.16 |
| l <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L04.18 |

**A** (5 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| a <- T78 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.15 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, B= 1 | L02.18 |
| e <- T60 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L03.32 |
| a <- T52 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, B= 1 | L04.16 |
| l <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, B= 1 | L04.18 |

**B** (4 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, A= 1 | L02.18 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1 | L03.8 |
| a <- T52 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, A= 1 | L04.16 |
| l <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Z= 1, A= 1 | L04.18 |


### Reader agreement on the baseline's errors (baseline Z; 4 errors; passes Z, A, B)

| agree_class | errors | share |
|---|---|---|
| all-same-wrong | 3 | 75.0% |
| majority-wrong | 1 | 25.0% |

| err_class | errors | all-same-wrong | majority-wrong |
|---|---|---|---|
| other | 4 | 3 (75%) | 1 (25%) |

| truth <- read | n | err_class | all-same-wrong | majority-wrong | lines |
|---|---|---|---|---|---|
| e <- T36 | 1 | other 1 | 1 | 0 | L02.18 |
| d <- T98 | 1 | other 1 | 0 | 1 | L03.8 |
| a <- T52 | 1 | other 1 | 1 | 0 | L04.16 |
| l <- T64 | 1 | other 1 | 1 | 0 | L04.18 |
