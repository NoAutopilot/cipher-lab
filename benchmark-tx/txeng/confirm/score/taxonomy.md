## spinelli-c1519-confirm: 193 scored positions, passes Z
- Z: 14 wrong-or-deleted of 193 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| Z | 14/193 | 1 (7% of errs; rate 14.3%; base 4%) | 13 (93% of errs; rate 7.1%; base 94%) | 0 (0% of errs; rate 0.0%; base 2%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 |
|---|---|---|---|---|---|---|---|---|
| Z | 5/41 | 4/36 | 3/23 | 0/23 | 1/11 | 1/19 | 0/24 | 0/16 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | Z |
|---|---|---|
| Z | 14 | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 0; wrong in exactly one: 14

### Top (truth value <- read) pairs per pass, with feature profile

**Z** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| r <- SIX | 4 | 0/0/4 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.27 L02.11 L03.4 L05.20 |
| h <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.14 L03.25 |
| u <- JHOOK | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.27 L06.21 |
| t <- TEE | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.3 |
| i <- EIGHT | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.5 |
| e <- SIX | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.15 |
| p <- THREE | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L03.16 |
| s <- JHOOK | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.3 |
| n <- PHI | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.7 |

