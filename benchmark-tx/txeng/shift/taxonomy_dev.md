## birago1572-no87: 343 scored positions, passes A, S0, S1, shift, L
- A: 23 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- S0: 22 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- S1: 17 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- shift: 17 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- L: 14 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 23/343 | 2 (9% of errs; rate 20.0%; base 3%) | 20 (87% of errs; rate 6.2%; base 94%) | 1 (4% of errs; rate 9.1%; base 3%) |
| S0 | 22/343 | 0 (0% of errs; rate 0.0%; base 3%) | 22 (100% of errs; rate 6.8%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| S1 | 17/343 | 0 (0% of errs; rate 0.0%; base 3%) | 17 (100% of errs; rate 5.3%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| shift | 17/343 | 0 (0% of errs; rate 0.0%; base 3%) | 17 (100% of errs; rate 5.3%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| L | 14/343 | 2 (14% of errs; rate 20.0%; base 3%) | 12 (86% of errs; rate 3.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by segment-crop edge (left/right)

| pass | errors | - (base %) | inner (base %) | overlap (base %) |
|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 19 (83% of errs; rate 8.7%; base 64%) | 4 (17% of errs; rate 3.3%; base 35%) |
| S0 | 22/343 | 0 (0% of errs; rate 0.0%; base 1%) | 17 (77% of errs; rate 7.8%; base 64%) | 5 (23% of errs; rate 4.1%; base 35%) |
| S1 | 17/343 | 1 (6% of errs; rate 25.0%; base 1%) | 13 (76% of errs; rate 6.0%; base 64%) | 3 (18% of errs; rate 2.5%; base 35%) |
| shift | 17/343 | 0 (0% of errs; rate 0.0%; base 1%) | 14 (82% of errs; rate 6.4%; base 64%) | 3 (18% of errs; rate 2.5%; base 35%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 12 (86% of errs; rate 5.5%; base 64%) | 2 (14% of errs; rate 1.7%; base 35%) |

### Error mass by line-band edge (top/bottom)

| pass | errors | - (base %) | cut (base %) | in (base %) | near (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (22% of errs; rate 8.8%; base 17%) | 18 (78% of errs; rate 7.0%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |
| S0 | 22/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (23% of errs; rate 8.8%; base 17%) | 17 (77% of errs; rate 6.6%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |
| S1 | 17/343 | 1 (6% of errs; rate 25.0%; base 1%) | 3 (18% of errs; rate 5.3%; base 17%) | 13 (76% of errs; rate 5.0%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |
| shift | 17/343 | 0 (0% of errs; rate 0.0%; base 1%) | 3 (18% of errs; rate 5.3%; base 17%) | 14 (82% of errs; rate 5.4%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (36% of errs; rate 8.8%; base 17%) | 9 (64% of errs; rate 3.5%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |

### Error mass by box<->token op (glued 2:1, split 1:2)

| pass | errors | - (base %) | 1:1 (base %) | 1:2 (base %) | 2:1 (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 21 (91% of errs; rate 6.5%; base 94%) | 1 (4% of errs; rate 25.0%; base 1%) | 1 (4% of errs; rate 8.3%; base 3%) |
| S0 | 22/343 | 0 (0% of errs; rate 0.0%; base 1%) | 20 (91% of errs; rate 6.2%; base 94%) | 1 (5% of errs; rate 25.0%; base 1%) | 1 (5% of errs; rate 8.3%; base 3%) |
| S1 | 17/343 | 1 (6% of errs; rate 25.0%; base 1%) | 14 (82% of errs; rate 4.3%; base 94%) | 1 (6% of errs; rate 25.0%; base 1%) | 1 (6% of errs; rate 8.3%; base 3%) |
| shift | 17/343 | 0 (0% of errs; rate 0.0%; base 1%) | 15 (88% of errs; rate 4.6%; base 94%) | 1 (6% of errs; rate 25.0%; base 1%) | 1 (6% of errs; rate 8.3%; base 3%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 13 (93% of errs; rate 4.0%; base 94%) | 1 (7% of errs; rate 25.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by stroke weight (erosion-survival terciles)

| pass | errors | - (base %) | heavy (base %) | mid (base %) | thin (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 7 (30% of errs; rate 6.2%; base 33%) | 4 (17% of errs; rate 3.5%; base 33%) | 12 (52% of errs; rate 10.6%; base 33%) |
| S0 | 22/343 | 0 (0% of errs; rate 0.0%; base 1%) | 6 (27% of errs; rate 5.3%; base 33%) | 6 (27% of errs; rate 5.3%; base 33%) | 10 (45% of errs; rate 8.8%; base 33%) |
| S1 | 17/343 | 1 (6% of errs; rate 25.0%; base 1%) | 5 (29% of errs; rate 4.4%; base 33%) | 4 (24% of errs; rate 3.5%; base 33%) | 7 (41% of errs; rate 6.2%; base 33%) |
| shift | 17/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (29% of errs; rate 4.4%; base 33%) | 4 (24% of errs; rate 3.5%; base 33%) | 8 (47% of errs; rate 7.1%; base 33%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 4 (29% of errs; rate 3.5%; base 33%) | 4 (29% of errs; rate 3.5%; base 33%) | 6 (43% of errs; rate 5.3%; base 33%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 |
|---|---|---|---|---|---|---|
| A | 2/57 | 4/57 | 2/53 | 5/59 | 8/60 | 2/57 |
| S0 | 3/57 | 3/57 | 4/53 | 4/59 | 6/60 | 2/57 |
| S1 | 3/57 | 3/57 | 3/53 | 3/59 | 4/60 | 1/57 |
| shift | 2/57 | 3/57 | 4/53 | 2/59 | 5/60 | 1/57 |
| L | 0/57 | 2/57 | 1/53 | 3/59 | 6/60 | 2/57 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | S0 | S1 | shift | L |
|---|---|---|---|---|---|---|
| A | 23 | - | 14/23 (12) | 8/23 (7) | 10/23 (9) | 14/23 (13) |
| S0 | 22 | 14/22 (12) | - | 14/22 (13) | 16/22 (16) | 10/22 (7) |
| S1 | 17 | 8/17 (7) | 14/17 (13) | - | 15/17 (14) | 8/17 (6) |
| shift | 17 | 10/17 (9) | 16/17 (16) | 15/17 (14) | - | 8/17 (6) |
| L | 14 | 14/14 (13) | 10/14 (7) | 8/14 (6) | 8/14 (6) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 8; wrong in exactly one: 9

### Top (truth value <- read) pairs per pass, with feature profile

**A** (23 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 4/0/3 | S0= 4, shift= 2 | L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | L= 3, S0= 2, S1= 1, shift= 1 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | S0= 1, S1= 1, shift= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | S0= 1, S1= 1, shift= 1, L= 1 | L02.12 |
| b <- T83 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 |  | L02.19 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | S0= 1, S1= 1, shift= 1, L= 1 | L05.4 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | S0= 1, S1= 1, shift= 1, L~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | L= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | S0~ 1, S1~ 1, shift~ 1, L= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | S0= 1, S1= 1, shift= 1, L= 1 | L09.4 |

**S0** (22 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 4 | 0/0/4 | 0/0/4 | 0/0/4 | 0/0 | 3/0/1 | A= 4, shift= 2 | L01.23 L03.4 L04.4 L05.25 |
| l <- T64 | 4 | 0/0/4 | 0/1/3 | 0/0/4 | 1/0 | 2/1/1 | S1= 4, shift= 4 | L07.25 L08.26 L09.13 L09.9 |
| e <- T76 | 2 | 0/0/2 | 0/0/2 | 2/0/0 | 0/0 | 1/0/1 | A= 2, L= 2, S1= 1, shift= 1 | L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, S1= 1, shift= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | A= 1, S1= 1, shift= 1, L= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 1, S1= 1, shift= 1, L= 1 | L05.4 |
| m <- X_NEW | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | S1~ 1, shift= 1 | L05.7 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A= 1, S1= 1, shift= 1, L~ 1 | L05.9 |
| i <- <deleted> | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 0/1/0 |  | L06.23 |
| u <- T15 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A~ 1, S1= 1, shift= 1, L~ 1 | L06.27 |

**S1** (17 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| l <- T64 | 5 | 0/0/5 | 0/1/4 | 0/0/5 | 1/0 | 3/1/1 | S0= 4, shift= 4 | L01.26 L07.25 L08.26 L09.13 L09.9 |
| per <- T76 | 1 | 0/0/1 | 0/0/1 | 1/0/0 | 0/0 | 1/0/0 | shift= 1 | L01.13 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, S0= 1, shift= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | A= 1, S0= 1, shift= 1, L= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 1, S0= 1, shift= 1, L= 1 | L05.4 |
| m <- T51 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | S0~ 1, shift~ 1 | L05.7 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A= 1, S0= 1, shift= 1, L~ 1 | L05.9 |
| u <- T15 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A~ 1, S0= 1, shift= 1, L~ 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1, S0= 1, shift= 1, L= 1 | L09.4 |
| e <- T76 | 1 | 0/0/1 | 0/0/1 | 1/0/0 | 0/0 | 0/0/1 | A= 1, S0= 1, shift= 1, L= 1 | L10.4 |

**shift** (17 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| l <- T64 | 4 | 0/0/4 | 0/1/3 | 0/0/4 | 1/0 | 2/1/1 | S0= 4, S1= 4 | L07.25 L08.26 L09.13 L09.9 |
| s <- T50 | 2 | 0/0/2 | 0/0/2 | 0/0/2 | 0/0 | 2/0/0 | A= 2, S0= 2 | L03.4 L05.25 |
| per <- T76 | 1 | 0/0/1 | 0/0/1 | 1/0/0 | 0/0 | 1/0/0 | S1= 1 | L01.13 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, S0= 1, S1= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | A= 1, S0= 1, S1= 1, L= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 1, S0= 1, S1= 1, L= 1 | L05.4 |
| m <- X_NEW | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | S0= 1, S1~ 1 | L05.7 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A= 1, S0= 1, S1= 1, L~ 1 | L05.9 |
| u <- T15 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A~ 1, S0= 1, S1= 1, L~ 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1, S0= 1, S1= 1, L= 1 | L09.4 |

**L** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | A= 3, S0= 2, S1= 1, shift= 1 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, S0= 1, S1= 1, shift= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | A= 1, S0= 1, S1= 1, shift= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 1, S0= 1, S1= 1, shift= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A~ 1, S0~ 1, S1~ 1, shift~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, S0~ 1, S1~ 1, shift~ 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1, S0= 1, S1= 1, shift= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1 | L10.1 |
| c <- T98 | 1 | 0/0/1 | 0/0/1 | 1/0/0 | 0/0 | 1/0/0 | A= 1, S0~ 1 | L10.31 |

