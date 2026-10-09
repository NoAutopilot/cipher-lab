## ceppo-f87-S: 139 scored positions, passes C, A, B, F
- C: 7 wrong-or-deleted of 139 covered positions (insertions not counted here; tx_bench adds them)
- A: 4 wrong-or-deleted of 139 covered positions (insertions not counted here; tx_bench adds them)
- B: 8 wrong-or-deleted of 139 covered positions (insertions not counted here; tx_bench adds them)
- F: 36 wrong-or-deleted of 139 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| C | 7/139 | 0 (0% of errs; rate 0.0%; base 1%) | 6 (86% of errs; rate 4.5%; base 96%) | 1 (14% of errs; rate 25.0%; base 3%) |
| A | 4/139 | 0 (0% of errs; rate 0.0%; base 1%) | 4 (100% of errs; rate 3.0%; base 96%) | 0 (0% of errs; rate 0.0%; base 3%) |
| B | 8/139 | 0 (0% of errs; rate 0.0%; base 1%) | 7 (88% of errs; rate 5.3%; base 96%) | 1 (12% of errs; rate 25.0%; base 3%) |
| F | 36/139 | 1 (3% of errs; rate 50.0%; base 1%) | 33 (92% of errs; rate 24.8%; base 96%) | 2 (6% of errs; rate 50.0%; base 3%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 |
|---|---|---|---|---|---|
| C | 0/14 | 1/24 | 3/34 | 2/35 | 1/32 |
| A | 0/14 | 0/24 | 1/34 | 0/35 | 3/32 |
| B | 0/14 | 2/24 | 2/34 | 2/35 | 2/32 |
| F | 3/14 | 6/24 | 8/34 | 13/35 | 6/32 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | C | A | B | F |
|---|---|---|---|---|---|
| C | 7 | - | 1/7 (1) | 6/7 (5) | 4/7 (4) |
| A | 4 | 1/4 (1) | - | 0/4 (0) | 0/4 (0) |
| B | 8 | 6/8 (5) | 0/8 (0) | - | 4/8 (3) |
| F | 36 | 4/36 (4) | 0/36 (0) | 4/36 (3) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 0; wrong in exactly one: 37

### Top (truth value <- read) pairs per pass, with feature profile

**C** (7 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| o <- S88 | 4 | 0/1/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | F= 4, B= 3, B~ 1 | L03.25 L03.46 L04.29 L05.23 |
| a <- S65 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 2, A= 1 | L02.7 L03.6 L04.21 |

**A** (4 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| a <- S65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | C= 1 | L03.6 |
| c <- S74 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L05.20 |
| t <- S24 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L05.28 |
| h <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L05.39 |

**B** (8 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| o <- S88 | 3 | 0/1/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | C= 3, F= 3 | L03.25 L03.46 L04.29 |
| a <- S65 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | C= 2 | L02.7 L04.21 |
| i <- S66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.19 |
| e <- S25 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L05.2 |
| o <- S32 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | C~ 1, F~ 1 | L05.23 |

**F** (36 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- S56 | 4 | 0/0/4 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.24 L02.16 L04.16 L04.3 |
| o <- S88 | 4 | 0/1/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | C= 4, B= 3, B~ 1 | L03.25 L03.46 L04.29 L05.23 |
| r <- S69 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.11 L04.27 |
| g <- S69 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.20 L03.30 |
| c <- S25 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.24 L05.34 |
| m <- S77 | 2 | 0/1/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.45 L03.33 |
| a <- S23 | 2 | 1/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L03.1 L05.3 |
| g <- S95 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L03.7 L04.24 |
| c <- S20 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L04.14 L05.10 |
| m <- S37 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.13 |


### Reader agreement on the baseline's errors (baseline C; 7 errors; passes C, A, B, F)

| agree_class | errors | share |
|---|---|---|
| majority-wrong | 4 | 57.1% |
| minority-wrong | 3 | 42.9% |

| err_class | errors | majority-wrong | minority-wrong |
|---|---|---|---|
| look-alike | 7 | 4 (57%) | 3 (43%) |

| truth <- read | n | err_class | majority-wrong | minority-wrong | lines |
|---|---|---|---|---|---|
| o <- S88 | 4 | look-alike 4 | 4 | 0 | L03.25 L03.46 L04.29 L05.23 |
| a <- S65 | 3 | look-alike 3 | 0 | 3 | L02.7 L03.6 L04.21 |
