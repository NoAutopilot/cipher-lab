## birago1572-no87: 169 scored positions, passes A, H, L
- A: 23 wrong-or-deleted of 169 covered positions (insertions not counted here; tx_bench adds them)
- H: 15 wrong-or-deleted of 169 covered positions (insertions not counted here; tx_bench adds them)
- L: 15 wrong-or-deleted of 169 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 23/169 | 2 (9% of errs; rate 40.0%; base 3%) | 21 (91% of errs; rate 13.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| H | 15/169 | 1 (7% of errs; rate 20.0%; base 3%) | 14 (93% of errs; rate 8.8%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| L | 15/169 | 2 (13% of errs; rate 40.0%; base 3%) | 13 (87% of errs; rate 8.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by segment-crop edge (left/right)

| pass | errors | - (base %) | inner (base %) | overlap (base %) |
|---|---|---|---|---|
| A | 23/169 | 13 (57% of errs; rate 15.3%; base 50%) | 9 (39% of errs; rate 16.1%; base 33%) | 1 (4% of errs; rate 3.6%; base 17%) |
| H | 15/169 | 7 (47% of errs; rate 8.2%; base 50%) | 6 (40% of errs; rate 10.7%; base 33%) | 2 (13% of errs; rate 7.1%; base 17%) |
| L | 15/169 | 7 (47% of errs; rate 8.2%; base 50%) | 7 (47% of errs; rate 12.5%; base 33%) | 1 (7% of errs; rate 3.6%; base 17%) |

### Error mass by line-band edge (top/bottom)

| pass | errors | - (base %) | cut (base %) | in (base %) | near (base %) |
|---|---|---|---|---|---|
| A | 23/169 | 13 (57% of errs; rate 15.3%; base 50%) | 5 (22% of errs; rate 35.7%; base 8%) | 5 (22% of errs; rate 8.6%; base 34%) | 0 (0% of errs; rate 0.0%; base 7%) |
| H | 15/169 | 7 (47% of errs; rate 8.2%; base 50%) | 5 (33% of errs; rate 35.7%; base 8%) | 3 (20% of errs; rate 5.2%; base 34%) | 0 (0% of errs; rate 0.0%; base 7%) |
| L | 15/169 | 7 (47% of errs; rate 8.2%; base 50%) | 5 (33% of errs; rate 35.7%; base 8%) | 3 (20% of errs; rate 5.2%; base 34%) | 0 (0% of errs; rate 0.0%; base 7%) |

### Error mass by box<->token op (glued 2:1, split 1:2)

| pass | errors | - (base %) | 1:1 (base %) | 1:2 (base %) | 2:1 (base %) |
|---|---|---|---|---|---|
| A | 23/169 | 13 (57% of errs; rate 15.3%; base 50%) | 10 (43% of errs; rate 12.5%; base 47%) | 0 (0% of errs; rate 0.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 2%) |
| H | 15/169 | 7 (47% of errs; rate 8.2%; base 50%) | 8 (53% of errs; rate 10.0%; base 47%) | 0 (0% of errs; rate 0.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 2%) |
| L | 15/169 | 7 (47% of errs; rate 8.2%; base 50%) | 8 (53% of errs; rate 10.0%; base 47%) | 0 (0% of errs; rate 0.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 2%) |

### Error mass by stroke weight (erosion-survival terciles)

| pass | errors | - (base %) | heavy (base %) | mid (base %) | thin (base %) |
|---|---|---|---|---|---|
| A | 23/169 | 13 (57% of errs; rate 15.3%; base 50%) | 4 (17% of errs; rate 14.3%; base 17%) | 2 (9% of errs; rate 7.1%; base 17%) | 4 (17% of errs; rate 14.3%; base 17%) |
| H | 15/169 | 7 (47% of errs; rate 8.2%; base 50%) | 4 (27% of errs; rate 14.3%; base 17%) | 0 (0% of errs; rate 0.0%; base 17%) | 4 (27% of errs; rate 14.3%; base 17%) |
| L | 15/169 | 7 (47% of errs; rate 8.2%; base 50%) | 4 (27% of errs; rate 14.3%; base 17%) | 1 (7% of errs; rate 3.6%; base 17%) | 3 (20% of errs; rate 10.7%; base 17%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+5 | L+10 | L+22 |
|---|---|---|---|---|---|---|
| A | 2/22 | 1/31 | 10/31 | 4/30 | 4/31 | 2/24 |
| H | 2/22 | 1/31 | 4/31 | 3/30 | 2/31 | 3/24 |
| L | 2/22 | 1/31 | 4/31 | 3/30 | 3/31 | 2/24 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | H | L |
|---|---|---|---|---|
| A | 23 | - | 11/23 (6) | 15/23 (12) |
| H | 15 | 11/15 (6) | - | 10/15 (6) |
| L | 15 | 15/15 (12) | 10/15 (6) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 10; wrong in exactly one: 11

### Top (truth value <- read) pairs per pass, with feature profile

**A** (23 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 1/0/1 | H= 3, L= 3 | L03.23 L05.4 L22.24 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | H~ 2, L~ 2 | L03.31 L03.34 |
| e <- T76 | 2 | 1/0/1 | 0/0/2 | 2/0/0 | 0/0 | 0/0/2 | L= 2, H~ 1, H= 1 | L05.1 L10.4 |
| s <- T50 | 2 | 0/0/2 | 0/0/2 | 0/0/2 | 0/0 | 1/1/0 |  | L05.25 L10.5 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | H~ 1, L= 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1 | L03.10 |
| t <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L03.24 |
| o <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L03.25 |

**H** (15 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 1/0/1 | A= 3, L= 3 | L03.23 L05.4 L22.24 |
| e <- X_NEW | 2 | 1/0/1 | 0/0/1 | 1/0/0 | 0/0 | 0/0/1 | A~ 2, L~ 1 | L03.32 L05.1 |
| e <- T60 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.11 |
| a <- T51 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, L~ 1 | L01.28 |
| h <- T52 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.15 |
| c <- T27 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, L~ 1 | L03.31 |
| c <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, L= 1 | L03.34 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A= 1, L~ 1 | L05.9 |
| e <- T76 | 1 | 0/0/1 | 0/0/1 | 1/0/0 | 0/0 | 0/0/1 | A= 1, L= 1 | L10.4 |
| n <- T15 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 |  | L10.17 |

**L** (15 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 1/0/1 | A= 3, H= 3 | L03.23 L05.4 L22.24 |
| e <- T76 | 2 | 1/0/1 | 0/0/2 | 2/0/0 | 0/0 | 0/0/2 | A= 2, H~ 1, H= 1 | L05.1 L10.4 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, H~ 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L03.10 |
| c <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, H~ 1 | L03.31 |
| c <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, H= 1 | L03.34 |
| s <- T64 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | A~ 1, H~ 1 | L05.9 |
| t <- T92 | 1 | 1/0/0 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | A= 1 | L10.1 |

