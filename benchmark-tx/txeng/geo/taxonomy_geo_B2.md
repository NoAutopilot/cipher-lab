## birago1572-no87: 169 scored positions, passes A, B, H, H2, L
- A: 23 wrong-or-deleted of 169 covered positions (insertions not counted here; tx_bench adds them)
- B: 32 wrong-or-deleted of 169 covered positions (insertions not counted here; tx_bench adds them)
- H: 15 wrong-or-deleted of 169 covered positions (insertions not counted here; tx_bench adds them)
- H2: 12 wrong-or-deleted of 169 covered positions (insertions not counted here; tx_bench adds them)
- L: 15 wrong-or-deleted of 169 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 23/169 | 2 (9% of errs; rate 40.0%; base 3%) | 21 (91% of errs; rate 13.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| B | 32/169 | 3 (9% of errs; rate 60.0%; base 3%) | 29 (91% of errs; rate 18.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| H | 15/169 | 1 (7% of errs; rate 20.0%; base 3%) | 14 (93% of errs; rate 8.8%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| H2 | 12/169 | 0 (0% of errs; rate 0.0%; base 3%) | 12 (100% of errs; rate 7.5%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| L | 15/169 | 2 (13% of errs; rate 40.0%; base 3%) | 13 (87% of errs; rate 8.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+5 | L+10 | L+22 |
|---|---|---|---|---|---|---|
| A | 2/22 | 1/31 | 10/31 | 4/30 | 4/31 | 2/24 |
| B | 5/22 | 3/31 | 12/31 | 5/30 | 5/31 | 2/24 |
| H | 2/22 | 1/31 | 4/31 | 3/30 | 2/31 | 3/24 |
| H2 | 1/22 | 0/31 | 2/31 | 3/30 | 2/31 | 4/24 |
| L | 2/22 | 1/31 | 4/31 | 3/30 | 3/31 | 2/24 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | B | H | H2 | L |
|---|---|---|---|---|---|---|
| A | 23 | - | 21/23 (19) | 11/23 (6) | 8/23 (5) | 15/23 (12) |
| B | 32 | 21/32 (19) | - | 11/32 (4) | 8/32 (5) | 15/32 (12) |
| H | 15 | 11/15 (6) | 11/15 (4) | - | 10/15 (9) | 10/15 (6) |
| H2 | 12 | 8/12 (5) | 8/12 (5) | 10/12 (9) | - | 8/12 (7) |
| L | 15 | 15/15 (12) | 15/15 (12) | 10/15 (6) | 8/15 (7) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 8; wrong in exactly one: 17

### Top (truth value <- read) pairs per pass, with feature profile

**A** (23 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| t <- T90 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | H= 3, H2= 3, L= 3, B= 2, B~ 1 | L03.23 L05.4 L22.24 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 2, H~ 2, L~ 2, H2~ 1 | L03.31 L03.34 |
| e <- T76 | 2 | 1/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 2, L= 2, H~ 1, H= 1, H2= 1 | L05.1 L10.4 |
| s <- T50 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L05.25 L10.5 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, L= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, H~ 1, H2~ 1, L= 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, L= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, L= 1 | L03.10 |
| t <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1 | L03.24 |
| o <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1 | L03.25 |

**B** (32 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| r <- T24 | 7 | 1/0/6 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.20 L01.24 L01.29 L02.25 L02.29 L03.1 L03.16 |
| t <- T90 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, H= 2, H2= 2, L= 2 | L03.23 L05.4 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, H~ 2, L~ 2, H2~ 1 | L03.31 L03.34 |
| e <- T76 | 2 | 1/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, L= 2, H~ 1, H= 1, H2= 1 | L05.1 L10.4 |
| d <- T98 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L10.3 L10.8 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, H~ 1, H2~ 1, L= 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1 | L03.10 |
| t <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L03.24 |

**H** (15 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| t <- T90 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 3, H2= 3, L= 3, B= 2, B~ 1 | L03.23 L05.4 L22.24 |
| e <- X_NEW | 2 | 1/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 2, B~ 2, L~ 1 | L03.32 L05.1 |
| e <- T60 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.11 |
| a <- T51 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, H2= 1, L~ 1 | L01.28 |
| h <- T52 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.15 |
| c <- T27 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, L~ 1 | L03.31 |
| c <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, H2= 1, L= 1 | L03.34 |
| s <- T13 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B~ 1, H2~ 1, L~ 1 | L05.9 |
| e <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, H2= 1, L= 1 | L10.4 |
| n <- T15 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | H2= 1 | L10.17 |

**H2** (12 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| t <- T90 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 3, H= 3, L= 3, B= 2, B~ 1 | L03.23 L05.4 L22.24 |
| a <- T51 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, H= 1, L~ 1 | L01.28 |
| c <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, H= 1, L= 1 | L03.34 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B= 1, H~ 1, L= 1 | L05.9 |
| l <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L05.14 |
| e <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, H= 1, L= 1 | L10.4 |
| n <- T15 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | H= 1 | L10.17 |
| z <- T60 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, H= 1, L= 1 | L22.2 |
| e <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L22.10 |
| t <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | H= 1 | L22.11 |

**L** (15 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| t <- T90 | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 3, H= 3, H2= 3, B= 2, B~ 1 | L03.23 L05.4 L22.24 |
| e <- T76 | 2 | 1/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, B= 2, H~ 1, H= 1, H2= 1 | L05.1 L10.4 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, H~ 1, H2~ 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L03.10 |
| c <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, H~ 1 | L03.31 |
| c <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, H= 1, H2= 1 | L03.34 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B= 1, H~ 1, H2= 1 | L05.9 |
| t <- T92 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1 | L10.1 |

