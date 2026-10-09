## birago1572-no87: 343 scored positions, passes A, P, L
- A: 23 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- P: 15 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- L: 14 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 23/343 | 2 (9% of errs; rate 20.0%; base 3%) | 20 (87% of errs; rate 6.2%; base 94%) | 1 (4% of errs; rate 9.1%; base 3%) |
| P | 15/343 | 1 (7% of errs; rate 10.0%; base 3%) | 12 (80% of errs; rate 3.7%; base 94%) | 2 (13% of errs; rate 18.2%; base 3%) |
| L | 14/343 | 2 (14% of errs; rate 20.0%; base 3%) | 12 (86% of errs; rate 3.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by segment-crop edge (left/right)

| pass | errors | - (base %) | inner (base %) | overlap (base %) |
|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 19 (83% of errs; rate 8.7%; base 64%) | 4 (17% of errs; rate 3.3%; base 35%) |
| P | 15/343 | 0 (0% of errs; rate 0.0%; base 1%) | 13 (87% of errs; rate 6.0%; base 64%) | 2 (13% of errs; rate 1.7%; base 35%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 12 (86% of errs; rate 5.5%; base 64%) | 2 (14% of errs; rate 1.7%; base 35%) |

### Error mass by line-band edge (top/bottom)

| pass | errors | - (base %) | cut (base %) | in (base %) | near (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (22% of errs; rate 8.8%; base 17%) | 18 (78% of errs; rate 7.0%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |
| P | 15/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (33% of errs; rate 8.8%; base 17%) | 10 (67% of errs; rate 3.9%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (36% of errs; rate 8.8%; base 17%) | 9 (64% of errs; rate 3.5%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |

### Error mass by box<->token op (glued 2:1, split 1:2)

| pass | errors | - (base %) | 1:1 (base %) | 1:2 (base %) | 2:1 (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 21 (91% of errs; rate 6.5%; base 94%) | 1 (4% of errs; rate 25.0%; base 1%) | 1 (4% of errs; rate 8.3%; base 3%) |
| P | 15/343 | 0 (0% of errs; rate 0.0%; base 1%) | 12 (80% of errs; rate 3.7%; base 94%) | 1 (7% of errs; rate 25.0%; base 1%) | 2 (13% of errs; rate 16.7%; base 3%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 13 (93% of errs; rate 4.0%; base 94%) | 1 (7% of errs; rate 25.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by stroke weight (erosion-survival terciles)

| pass | errors | - (base %) | heavy (base %) | mid (base %) | thin (base %) |
|---|---|---|---|---|---|
| A | 23/343 | 0 (0% of errs; rate 0.0%; base 1%) | 7 (30% of errs; rate 6.2%; base 33%) | 4 (17% of errs; rate 3.5%; base 33%) | 12 (52% of errs; rate 10.6%; base 33%) |
| P | 15/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (33% of errs; rate 4.4%; base 33%) | 3 (20% of errs; rate 2.7%; base 33%) | 7 (47% of errs; rate 6.2%; base 33%) |
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 4 (29% of errs; rate 3.5%; base 33%) | 4 (29% of errs; rate 3.5%; base 33%) | 6 (43% of errs; rate 5.3%; base 33%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 |
|---|---|---|---|---|---|---|
| A | 2/57 | 4/57 | 2/53 | 5/59 | 8/60 | 2/57 |
| P | 0/57 | 3/57 | 1/53 | 3/59 | 6/60 | 2/57 |
| L | 0/57 | 2/57 | 1/53 | 3/59 | 6/60 | 2/57 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | P | L |
|---|---|---|---|---|
| A | 23 | - | 12/23 (9) | 14/23 (13) |
| P | 15 | 12/15 (9) | - | 11/15 (8) |
| L | 14 | 14/14 (13) | 11/14 (8) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 11; wrong in exactly one: 11

### Top (truth value <- read) pairs per pass, with feature profile

**A** (23 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 4/0/3 |  | L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | P= 3, L= 3 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | P= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | P= 1, L= 1 | L02.12 |
| b <- T83 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 |  | L02.19 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | P= 1, L= 1 | L05.4 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | P= 1, L~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | L= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | P~ 1, L= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | P= 1, L= 1 | L09.4 |

**P** (15 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | A= 3, L= 3 | L05.1 L10.4 L11.5 |
| i <- ? | 2 | 0/2/0 | 0/0/2 | 0/0/2 | 2/0 | 2/0/0 | A~ 1 | L11.32 L12.32 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, L= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | A= 1, L= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 1, L= 1 | L05.4 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A= 1, L~ 1 | L05.9 |
| u <- T15 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A~ 1, L~ 1 | L06.27 |
| n <- T86 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 |  | L08.16 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1, L= 1 | L09.4 |
| n <- T15 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 |  | L10.17 |

**L** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | A= 3, P= 3 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, P= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | A= 1, P= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 1, P= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A~ 1, P~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1, P~ 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | A= 1, P= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1 | L10.1 |
| c <- T98 | 1 | 0/0/1 | 0/0/1 | 1/0/0 | 0/0 | 1/0/0 | A= 1, P~ 1 | L10.31 |

