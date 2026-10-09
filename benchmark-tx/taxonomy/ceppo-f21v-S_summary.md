## ceppo-f21v-S: 189 scored positions, passes A, B, C, F
- A: 9 wrong-or-deleted of 189 covered positions (insertions not counted here; tx_bench adds them)
- B: 10 wrong-or-deleted of 189 covered positions (insertions not counted here; tx_bench adds them)
- C: 1 wrong-or-deleted of 189 covered positions (insertions not counted here; tx_bench adds them)
- F: 10 wrong-or-deleted of 189 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 9/189 | 0 (0% of errs; rate 0.0%; base 5%) | 8 (89% of errs; rate 4.7%; base 90%) | 1 (11% of errs; rate 11.1%; base 5%) |
| B | 10/189 | 1 (10% of errs; rate 10.0%; base 5%) | 9 (90% of errs; rate 5.3%; base 90%) | 0 (0% of errs; rate 0.0%; base 5%) |
| C | 1/189 | 0 (0% of errs; rate 0.0%; base 5%) | 1 (100% of errs; rate 0.6%; base 90%) | 0 (0% of errs; rate 0.0%; base 5%) |
| F | 10/189 | 0 (0% of errs; rate 0.0%; base 5%) | 10 (100% of errs; rate 5.9%; base 90%) | 0 (0% of errs; rate 0.0%; base 5%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2/28 | 1/11 | 4/34 | 0/15 | 0/27 | 1/9 | 0/25 | 0/5 | 0/18 | 0/5 | 1/12 |
| B | 1/28 | 0/11 | 3/34 | 0/15 | 0/27 | 0/9 | 2/25 | 0/5 | 3/18 | 0/5 | 1/12 |
| C | 0/28 | 0/11 | 0/34 | 0/15 | 0/27 | 0/9 | 0/25 | 0/5 | 0/18 | 0/5 | 1/12 |
| F | 1/28 | 1/11 | 5/34 | 1/15 | 0/27 | 0/9 | 2/25 | 0/5 | 0/18 | 0/5 | 0/12 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | B | C | F |
|---|---|---|---|---|---|
| A | 9 | - | 1/9 (1) | 1/9 (1) | 0/9 (0) |
| B | 10 | 1/10 (1) | - | 1/10 (1) | 5/10 (0) |
| C | 1 | 1/1 (1) | 1/1 (1) | - | 0/1 (0) |
| F | 10 | 0/10 (0) | 5/10 (0) | 0/10 (0) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 0; wrong in exactly one: 17

### Top (truth value <- read) pairs per pass, with feature profile

**A** (9 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| a <- S65 | 8 | 0/1/7 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.27 L01.4 L02.2.2 L03.20 L03.26 L03.28 L03.34 L06.2.13 |
| n <- S73 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, C= 1 | L11.17 |

**B** (10 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- S73 | 5 | 0/0/5 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | F~ 4, A= 1, C= 1 | L01.15 L03.10 L03.14 L03.7 L11.17 |
| n <- S97 | 5 | 1/0/4 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | F~ 1 | L07.10 L07.27 L09.1 L09.17 L09.6 |

**C** (1 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- S73 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L11.17 |

**F** (10 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- S30 | 4 | 0/0/4 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 4 | L01.15 L03.10 L03.14 L03.7 |
| s <- S55 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L03.33 L03.4 |
| i <- S66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.1.7 |
| l <- S42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L04.6 |
| a <- S23 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L07.7 |
| n <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 1 | L07.27 |

