## birago1572-no87: 343 scored positions, passes A, U, L
- A: 23 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- U: 20 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- L: 14 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 23/343 | 2 (9% of errs; rate 20.0%; base 3%) | 20 (87% of errs; rate 6.2%; base 94%) | 1 (4% of errs; rate 9.1%; base 3%) |
| U | 20/343 | 1 (5% of errs; rate 10.0%; base 3%) | 17 (85% of errs; rate 5.3%; base 94%) | 2 (10% of errs; rate 18.2%; base 3%) |
| L | 14/343 | 2 (14% of errs; rate 20.0%; base 3%) | 12 (86% of errs; rate 3.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1/27 | 3/27 | 1/25 | 1/28 | 4/30 | 2/28 | 1/30 | 1/30 | 1/28 | 4/31 | 4/30 | 0/29 |
| U | 3/27 | 2/27 | 0/25 | 0/28 | 3/30 | 1/28 | 0/30 | 1/30 | 1/28 | 4/31 | 4/30 | 1/29 |
| L | 0/27 | 2/27 | 0/25 | 0/28 | 3/30 | 2/28 | 0/30 | 0/30 | 1/28 | 3/31 | 3/30 | 0/29 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | U | L |
|---|---|---|---|---|
| A | 23 | - | 14/23 (10) | 14/23 (13) |
| U | 20 | 14/20 (10) | - | 11/20 (7) |
| L | 14 | 14/14 (13) | 11/14 (7) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 11; wrong in exactly one: 12

### Top (truth value <- read) pairs per pass, with feature profile

**A** (23 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | U= 2 | L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 |
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 3, U= 2, U~ 1 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | U= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | U= 1, L= 1 | L02.12 |
| b <- T83 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.19 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | U= 1, L= 1 | L05.4 |
| s <- T13 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | U= 1, L~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | U~ 1, L= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | U= 1, L= 1 | L09.4 |

**U** (20 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2 | L08.10 L10.5 L11.6 |
| e <- T76 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, L= 2 | L10.4 L11.5 |
| i <- X_NEW | 2 | 0/2/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1 | L11.32 L12.32 |
| e <- T60 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.12 |
| n <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.15 |
| c <- T27 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.16 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1 | L02.12 |
| e <- T26 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, L~ 1 | L05.1 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1 | L05.4 |

**L** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 3, U= 2, U~ 1 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, U= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, U= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, U= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, U~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, U~ 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, U= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L10.1 |
| c <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, U~ 1 | L10.31 |

