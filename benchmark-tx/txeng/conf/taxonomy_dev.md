## birago1572-no87: 343 scored positions, passes L, Lat4, M
- L: 14 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- Lat4: 18 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- M: 18 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| L | 14/343 | 2 (14% of errs; rate 20.0%; base 3%) | 12 (86% of errs; rate 3.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| Lat4 | 18/343 | 2 (11% of errs; rate 20.0%; base 3%) | 16 (89% of errs; rate 5.0%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| M | 18/343 | 2 (11% of errs; rate 20.0%; base 3%) | 16 (89% of errs; rate 5.0%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L | 0/27 | 2/27 | 0/25 | 0/28 | 3/30 | 2/28 | 0/30 | 0/30 | 1/28 | 3/31 | 3/30 | 0/29 |
| Lat4 | 0/27 | 3/27 | 1/25 | 1/28 | 4/30 | 1/28 | 0/30 | 1/30 | 1/28 | 4/31 | 2/30 | 0/29 |
| M | 0/27 | 3/27 | 1/25 | 1/28 | 4/30 | 1/28 | 0/30 | 1/30 | 1/28 | 4/31 | 2/30 | 0/29 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | L | Lat4 | M |
|---|---|---|---|---|
| L | 14 | - | 11/14 (9) | 11/14 (9) |
| Lat4 | 18 | 11/18 (9) | - | 18/18 (18) |
| M | 18 | 11/18 (9) | 18/18 (18) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 11; wrong in exactly one: 3

### Top (truth value <- read) pairs per pass, with feature profile

**L** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, M= 1, Lat4~ 1, M~ 1 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, M= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, M= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4~ 1, M~ 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, M= 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, M= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, M= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, M= 1 | L10.1 |
| c <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, M= 1 | L10.31 |

**Lat4** (18 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | M= 3 | L04.4 L05.25 L08.10 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, M= 1 | L02.8 |
| u <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | M= 1 | L02.9 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, M= 1 | L02.12 |
| carmagnola <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | M= 1 | L03.24 |
| e <- T76 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, M= 1 | L05.1 |
| t <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L~ 1, M= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, M= 1 | L05.9 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, M= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, M= 1 | L09.4 |

**M** (18 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 3 | L04.4 L05.25 L08.10 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1 | L02.8 |
| u <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1 | L02.9 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1 | L02.12 |
| carmagnola <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1 | L03.24 |
| e <- T76 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1 | L05.1 |
| t <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L~ 1, Lat4= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1 | L05.9 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1 | L09.4 |

