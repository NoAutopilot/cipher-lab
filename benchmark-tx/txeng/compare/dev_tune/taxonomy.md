## birago1572-no87: 343 scored positions, passes L, G
- L: 14 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- G: 26 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| L | 14/343 | 2 (14% of errs; rate 20.0%; base 3%) | 12 (86% of errs; rate 3.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| G | 26/343 | 1 (4% of errs; rate 10.0%; base 3%) | 25 (96% of errs; rate 7.8%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by segment-crop edge (left/right)

| pass | errors | - (base %) | inner (base %) | overlap (base %) |
|---|---|---|---|---|
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 12 (86% of errs; rate 5.5%; base 64%) | 2 (14% of errs; rate 1.7%; base 35%) |
| G | 26/343 | 0 (0% of errs; rate 0.0%; base 1%) | 18 (69% of errs; rate 8.3%; base 64%) | 8 (31% of errs; rate 6.6%; base 35%) |

### Error mass by line-band edge (top/bottom)

| pass | errors | - (base %) | cut (base %) | in (base %) | near (base %) |
|---|---|---|---|---|---|
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (36% of errs; rate 8.8%; base 17%) | 9 (64% of errs; rate 3.5%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |
| G | 26/343 | 0 (0% of errs; rate 0.0%; base 1%) | 5 (19% of errs; rate 8.8%; base 17%) | 21 (81% of errs; rate 8.1%; base 75%) | 0 (0% of errs; rate 0.0%; base 7%) |

### Error mass by box<->token op (glued 2:1, split 1:2)

| pass | errors | - (base %) | 1:1 (base %) | 1:2 (base %) | 2:1 (base %) |
|---|---|---|---|---|---|
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 13 (93% of errs; rate 4.0%; base 94%) | 1 (7% of errs; rate 25.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 3%) |
| G | 26/343 | 0 (0% of errs; rate 0.0%; base 1%) | 25 (96% of errs; rate 7.7%; base 94%) | 1 (4% of errs; rate 25.0%; base 1%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error mass by stroke weight (erosion-survival terciles)

| pass | errors | - (base %) | heavy (base %) | mid (base %) | thin (base %) |
|---|---|---|---|---|---|
| L | 14/343 | 0 (0% of errs; rate 0.0%; base 1%) | 4 (29% of errs; rate 3.5%; base 33%) | 4 (29% of errs; rate 3.5%; base 33%) | 6 (43% of errs; rate 5.3%; base 33%) |
| G | 26/343 | 0 (0% of errs; rate 0.0%; base 1%) | 11 (42% of errs; rate 9.7%; base 33%) | 7 (27% of errs; rate 6.2%; base 33%) | 8 (31% of errs; rate 7.1%; base 33%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L | 0/27 | 2/27 | 0/25 | 0/28 | 3/30 | 2/28 | 0/30 | 0/30 | 1/28 | 3/31 | 3/30 | 0/29 |
| G | 1/27 | 3/27 | 0/25 | 0/28 | 3/30 | 3/28 | 1/30 | 0/30 | 4/28 | 3/31 | 7/30 | 1/29 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | L | G |
|---|---|---|---|
| L | 14 | - | 10/14 (8) |
| G | 26 | 10/26 (8) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 10; wrong in exactly one: 20

### Top (truth value <- read) pairs per pass, with feature profile

**L** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | G= 2, G~ 1 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | G= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/1/0 | 1/0/0 | 0/0 | 0/1/0 | G= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | G= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | G~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 |  | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | G= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | G= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 |  | L10.1 |
| c <- T98 | 1 | 0/0/1 | 0/0/1 | 1/0/0 | 0/0 | 1/0/0 |  | L10.31 |

**G** (26 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 3 | 0/0/3 | 0/0/3 | 0/0/3 | 0/0 | 3/0/0 |  | L01.23 L10.5 L11.6 |
| i <- T38 | 3 | 0/0/3 | 0/3/0 | 0/0/3 | 0/0 | 1/1/1 |  | L09.18 L11.25 L12.20 |
| e <- T36 | 2 | 0/0/2 | 0/1/1 | 2/0/0 | 0/0 | 1/1/0 | L= 1, L~ 1 | L02.12 L11.5 |
| e <- T76 | 2 | 1/0/1 | 0/0/2 | 2/0/0 | 0/0 | 0/0/2 | L= 2 | L05.1 L10.4 |
| e <- <deleted> | 2 | 0/0/2 | 0/1/1 | 1/0/1 | 0/0 | 0/1/1 |  | L09.21 L11.16 |
| g <- T42 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 | L= 1 | L02.8 |
| h <- T13 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/1/0 |  | L02.23 |
| t <- T90 | 1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | L= 1 | L05.4 |
| s <- T13 | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 1/0/0 | L~ 1 | L05.9 |
| o <- <deleted> | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 0/1/0 |  | L06.12 |

