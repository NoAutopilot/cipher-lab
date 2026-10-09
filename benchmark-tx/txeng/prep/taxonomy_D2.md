## birago1572-no87: 343 scored positions, passes A, K2, L
- A: 23 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- K2: 22 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- L: 14 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 23/343 | 2 (9% of errs; rate 20.0%; base 3%) | 20 (87% of errs; rate 6.2%; base 94%) | 1 (4% of errs; rate 9.1%; base 3%) |
| K2 | 22/343 | 2 (9% of errs; rate 20.0%; base 3%) | 20 (91% of errs; rate 6.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| L | 14/343 | 2 (14% of errs; rate 20.0%; base 3%) | 12 (86% of errs; rate 3.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by segment-crop edge (left/right)

| pass | errors | - (base %) | inner (base %) | overlap (base %) |
|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 19 (83% of errs; rate 8.7%; base 64%) | 4 (17% of errs; rate 3.3%; base 35%) |
| K2 | 22/343 | 0 (0% of errs; rate 0.0%; base 1%) | 17 (77% of errs; rate 7.8%; base 64%) | 5 (23% of errs; rate 4.1%; base 35%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 12 (86% of errs; rate 5.5%; base 64%) | 2 (14% of errs; rate 1.7%; base 35%) |

### Error mass by line-band edge (top/bottom)

| pass | errors | - (base %) | cut (base %) | in (base %) | near (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (22% of errs; rate 8.8%; base 17%) | 18 (78% of errs; rate 7.0%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |
| K2 | 22/343 | 0 (0% of errs; rate 0.0%; base 1%) | 8 (36% of errs; rate 14.0%; base 17%) | 12 (55% of errs; rate 4.7%; base 75%) | 2 (9% of errs; rate 8.3%; base 7%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (36% of errs; rate 8.8%; base 17%) | 9 (64% of errs; rate 3.5%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |

### Error mass by box<->token op (glued 2:1, split 1:2)

| pass | errors | - (base %) | 1:1 (base %) | 1:2 (base %) | 2:1 (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 21 (91% of errs; rate 6.5%; base 94%) | 1 (4% of errs; rate 25.0%; base 1%) | 1 (4% of errs; rate 8.3%; base 3%) |
| K2 | 22/343 | 0 (0% of errs; rate 0.0%; base 1%) | 21 (95% of errs; rate 6.5%; base 94%) | 1 (5% of errs; rate 25.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 3%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 13 (93% of errs; rate 4.0%; base 94%) | 1 (7% of errs; rate 25.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by stroke weight (erosion-survival terciles)

| pass | errors | - (base %) | heavy (base %) | mid (base %) | thin (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 7 (30% of errs; rate 6.2%; base 33%) | 4 (17% of errs; rate 3.5%; base 33%) | 12 (52% of errs; rate 10.6%; base 33%) |
| K2 | 22/343 | 0 (0% of errs; rate 0.0%; base 1%) | 9 (41% of errs; rate 8.0%; base 33%) | 3 (14% of errs; rate 2.7%; base 33%) | 10 (45% of errs; rate 8.8%; base 33%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 4 (29% of errs; rate 3.5%; base 33%) | 4 (29% of errs; rate 3.5%; base 33%) | 6 (43% of errs; rate 5.3%; base 33%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1/27 | 3/27 | 1/25 | 1/28 | 4/30 | 2/28 | 1/30 | 1/30 | 1/28 | 4/31 | 4/30 | 0/29 |
| K2 | 3/27 | 2/27 | 0/25 | 1/28 | 5/30 | 1/28 | 0/30 | 1/30 | 1/28 | 4/31 | 3/30 | 1/29 |
| L | 0/27 | 2/27 | 0/25 | 0/28 | 3/30 | 2/28 | 0/30 | 0/30 | 1/28 | 3/31 | 3/30 | 0/29 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | K2 | L |
|---|---|---|---|---|
| A | 23 | - | 14/23 (10) | 14/23 (13) |
| K2 | 22 | 14/22 (10) | - | 11/22 (8) |
| L | 14 | 14/14 (13) | 11/14 (8) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 11; wrong in exactly one: 14

### Top (truth value <- read) pairs per pass, with feature profile

**A** (23 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 4/0/3 | K2~ 2, K2= 1 | L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | K2= 3, L= 3 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | K2= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | K2= 1, L= 1 | L02.12 |
| b <- T83 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 |  | L02.19 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | K2= 1, L= 1 | L05.4 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | K2= 1, L~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | L= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | K2~ 1, L= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | K2= 1, L= 1 | L09.4 |

**K2** (22 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | A= 3, L= 3 | L05.1 L10.4 L11.5 |
| l <- T65 | 2 | 0/0/2 | 0/1/1 | 2/0/0 | 0/0 | 0/0/2 |  | L01.3 L01.8 |
| s <- X_NEW | 2 | 0/0/2 | 0/0/2 | 0/0/2 | 0/0 | 1/0/1 | A~ 2 | L04.4 L05.25 |
| s <- T50 | 2 | 0/0/2 | 0/0/2 | 0/0/2 | 0/0 | 2/0/0 | A= 1 | L10.5 L11.6 |
| d <- T98 | 1 | 1/0/0 | 0/0/1 | 1/0/0 | 0/0 | 1/0/0 |  | L01.1 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | A= 1, L= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 1, L= 1 | L05.4 |
| m <- T85 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 |  | L05.7 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A= 1, L~ 1 | L05.9 |

**L** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | A= 3, K2= 3 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, K2= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | A= 1, K2= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 1, K2= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A~ 1, K2~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, K2~ 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1, K2= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1 | L10.1 |
| c <- T98 | 1 | 0/0/1 | 0/0/1 | 1/0/0 | 0/0 | 1/0/0 | A= 1, K2~ 1 | L10.31 |

