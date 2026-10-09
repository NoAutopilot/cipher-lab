## birago1572-no87: 343 scored positions, passes L, Lat4, R, Rshuf1
- L: 14 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- Lat4: 18 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- R: 17 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- Rshuf1: 18 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| L | 14/343 | 2 (14% of errs; rate 20.0%; base 3%) | 12 (86% of errs; rate 3.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| Lat4 | 18/343 | 2 (11% of errs; rate 20.0%; base 3%) | 16 (89% of errs; rate 5.0%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| R | 17/343 | 3 (18% of errs; rate 30.0%; base 3%) | 14 (82% of errs; rate 4.3%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| Rshuf1 | 18/343 | 3 (17% of errs; rate 30.0%; base 3%) | 15 (83% of errs; rate 4.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L | 0/27 | 2/27 | 0/25 | 0/28 | 3/30 | 2/28 | 0/30 | 0/30 | 1/28 | 3/31 | 3/30 | 0/29 |
| Lat4 | 0/27 | 3/27 | 1/25 | 1/28 | 4/30 | 1/28 | 0/30 | 1/30 | 1/28 | 4/31 | 2/30 | 0/29 |
| R | 0/27 | 2/27 | 1/25 | 0/28 | 3/30 | 3/28 | 0/30 | 0/30 | 2/28 | 3/31 | 3/30 | 0/29 |
| Rshuf1 | 0/27 | 2/27 | 1/25 | 0/28 | 4/30 | 2/28 | 0/30 | 1/30 | 2/28 | 3/31 | 3/30 | 0/29 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | L | Lat4 | R | Rshuf1 |
|---|---|---|---|---|---|
| L | 14 | - | 11/14 (9) | 13/14 (13) | 13/14 (13) |
| Lat4 | 18 | 11/18 (9) | - | 13/18 (10) | 15/18 (12) |
| R | 17 | 13/17 (13) | 13/17 (10) | - | 16/17 (16) |
| Rshuf1 | 18 | 13/18 (13) | 15/18 (12) | 16/18 (16) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 11; wrong in exactly one: 5

### Top (truth value <- read) pairs per pass, with feature profile

**L** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | R= 3, Rshuf1= 3, Lat4= 1, Lat4~ 1 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, R= 1, Rshuf1= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, R= 1, Rshuf1= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4~ 1, R= 1, Rshuf1= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, R= 1, Rshuf1= 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | R= 1, Rshuf1= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, R= 1, Rshuf1= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, R= 1, Rshuf1= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, R= 1, Rshuf1= 1 | L10.1 |
| c <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, R= 1, Rshuf1= 1 | L10.31 |

**Lat4** (18 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Rshuf1= 2 | L04.4 L05.25 L08.10 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, R= 1, Rshuf1= 1 | L02.8 |
| u <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.9 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, R= 1, Rshuf1= 1 | L02.12 |
| carmagnola <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | R= 1, Rshuf1= 1 | L03.24 |
| e <- T76 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, R= 1, Rshuf1= 1 | L05.1 |
| t <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L~ 1, R~ 1, Rshuf1~ 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, R= 1, Rshuf1= 1 | L05.9 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, R= 1, Rshuf1= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, R= 1, Rshuf1= 1 | L09.4 |

**R** (17 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 3, Rshuf1= 3, Lat4= 1, Lat4~ 1 | L05.1 L10.4 L11.5 |
| et <- T24 | 2 | 1/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Rshuf1= 1 | L06.8 L09.1 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, Rshuf1= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, Rshuf1= 1 | L02.12 |
| carmagnola <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, Rshuf1= 1 | L03.24 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4~ 1, Rshuf1= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, Rshuf1= 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Rshuf1= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, Rshuf1= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, Rshuf1= 1 | L09.4 |

**Rshuf1** (18 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 3, R= 3, Lat4= 1, Lat4~ 1 | L05.1 L10.4 L11.5 |
| s <- T50 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 2 | L05.25 L08.10 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, R= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, R= 1 | L02.12 |
| carmagnola <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Lat4= 1, R= 1 | L03.24 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4~ 1, R= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, R= 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, R= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Lat4= 1, R= 1 | L06.27 |
| et <- T24 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | R= 1 | L09.1 |

