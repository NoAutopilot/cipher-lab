## birago1572-no87: 803 scored positions, passes L, A, B, C, E, F
- L: 34 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- A: 52 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- B: 72 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- C: 41 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- E: 58 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- F: 71 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| L | 34/803 | 4 (12% of errs; rate 16.0%; base 3%) | 30 (88% of errs; rate 4.0%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| A | 52/803 | 4 (8% of errs; rate 16.0%; base 3%) | 47 (90% of errs; rate 6.2%; base 94%) | 1 (2% of errs; rate 4.2%; base 3%) |
| B | 72/803 | 6 (8% of errs; rate 24.0%; base 3%) | 66 (92% of errs; rate 8.8%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| C | 41/803 | 4 (10% of errs; rate 16.0%; base 3%) | 37 (90% of errs; rate 4.9%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| E | 58/803 | 4 (7% of errs; rate 16.0%; base 3%) | 53 (91% of errs; rate 7.0%; base 94%) | 1 (2% of errs; rate 4.2%; base 3%) |
| F | 71/803 | 2 (3% of errs; rate 8.0%; base 3%) | 65 (92% of errs; rate 8.6%; base 94%) | 4 (6% of errs; rate 16.7%; base 3%) |

### Error mass by segment-crop edge (left/right)

| pass | errors | - (base %) | edge (base %) | inner (base %) | overlap (base %) |
|---|---|---|---|---|---|
| L | 34/803 | 7 (21% of errs; rate 7.3%; base 12%) | 0 (0% of errs; rate 0.0%; base 0%) | 19 (56% of errs; rate 4.2%; base 57%) | 8 (24% of errs; rate 3.2%; base 31%) |
| A | 52/803 | 13 (25% of errs; rate 13.5%; base 12%) | 0 (0% of errs; rate 0.0%; base 0%) | 28 (54% of errs; rate 6.2%; base 57%) | 11 (21% of errs; rate 4.4%; base 31%) |
| B | 72/803 | 21 (29% of errs; rate 21.9%; base 12%) | 0 (0% of errs; rate 0.0%; base 0%) | 36 (50% of errs; rate 7.9%; base 57%) | 15 (21% of errs; rate 6.0%; base 31%) |
| C | 41/803 | 7 (17% of errs; rate 7.3%; base 12%) | 0 (0% of errs; rate 0.0%; base 0%) | 25 (61% of errs; rate 5.5%; base 57%) | 9 (22% of errs; rate 3.6%; base 31%) |
| E | 58/803 | 16 (28% of errs; rate 16.7%; base 12%) | 2 (3% of errs; rate 66.7%; base 0%) | 31 (53% of errs; rate 6.8%; base 57%) | 9 (16% of errs; rate 3.6%; base 31%) |
| F | 71/803 | 30 (42% of errs; rate 31.2%; base 12%) | 0 (0% of errs; rate 0.0%; base 0%) | 28 (39% of errs; rate 6.2%; base 57%) | 13 (18% of errs; rate 5.2%; base 31%) |

### Error mass by line-band edge (top/bottom)

| pass | errors | - (base %) | cut (base %) | in (base %) | near (base %) |
|---|---|---|---|---|---|
| L | 34/803 | 7 (21% of errs; rate 7.3%; base 12%) | 10 (29% of errs; rate 8.6%; base 14%) | 16 (47% of errs; rate 3.0%; base 67%) | 1 (3% of errs; rate 1.9%; base 6%) |
| A | 52/803 | 13 (25% of errs; rate 13.5%; base 12%) | 11 (21% of errs; rate 9.5%; base 14%) | 27 (52% of errs; rate 5.0%; base 67%) | 1 (2% of errs; rate 1.9%; base 6%) |
| B | 72/803 | 21 (29% of errs; rate 21.9%; base 12%) | 15 (21% of errs; rate 12.9%; base 14%) | 33 (46% of errs; rate 6.1%; base 67%) | 3 (4% of errs; rate 5.8%; base 6%) |
| C | 41/803 | 7 (17% of errs; rate 7.3%; base 12%) | 10 (24% of errs; rate 8.6%; base 14%) | 23 (56% of errs; rate 4.3%; base 67%) | 1 (2% of errs; rate 1.9%; base 6%) |
| E | 58/803 | 16 (28% of errs; rate 16.7%; base 12%) | 13 (22% of errs; rate 11.2%; base 14%) | 28 (48% of errs; rate 5.2%; base 67%) | 1 (2% of errs; rate 1.9%; base 6%) |
| F | 71/803 | 30 (42% of errs; rate 31.2%; base 12%) | 13 (18% of errs; rate 11.2%; base 14%) | 23 (32% of errs; rate 4.3%; base 67%) | 5 (7% of errs; rate 9.6%; base 6%) |

### Error mass by box<->token op (glued 2:1, split 1:2)

| pass | errors | - (base %) | 1:1 (base %) | 1:2 (base %) | 2:1 (base %) | bad-cut (base %) | unsure (base %) |
|---|---|---|---|---|---|---|---|
| L | 34/803 | 7 (21% of errs; rate 7.3%; base 12%) | 26 (76% of errs; rate 3.9%; base 83%) | 1 (3% of errs; rate 7.7%; base 2%) | 0 (0% of errs; rate 0.0%; base 3%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 0%) |
| A | 52/803 | 13 (25% of errs; rate 13.5%; base 12%) | 36 (69% of errs; rate 5.4%; base 83%) | 2 (4% of errs; rate 15.4%; base 2%) | 1 (2% of errs; rate 4.5%; base 3%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 0%) |
| B | 72/803 | 21 (29% of errs; rate 21.9%; base 12%) | 49 (68% of errs; rate 7.3%; base 83%) | 1 (1% of errs; rate 7.7%; base 2%) | 1 (1% of errs; rate 4.5%; base 3%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 0%) |
| C | 41/803 | 7 (17% of errs; rate 7.3%; base 12%) | 32 (78% of errs; rate 4.8%; base 83%) | 2 (5% of errs; rate 15.4%; base 2%) | 0 (0% of errs; rate 0.0%; base 3%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 0%) |
| E | 58/803 | 16 (28% of errs; rate 16.7%; base 12%) | 38 (66% of errs; rate 5.7%; base 83%) | 1 (2% of errs; rate 7.7%; base 2%) | 3 (5% of errs; rate 13.6%; base 3%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 0%) |
| F | 71/803 | 30 (42% of errs; rate 31.2%; base 12%) | 39 (55% of errs; rate 5.8%; base 83%) | 0 (0% of errs; rate 0.0%; base 2%) | 2 (3% of errs; rate 9.1%; base 3%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 0%) |

### Error mass by stroke weight (erosion-survival terciles)

| pass | errors | - (base %) | heavy (base %) | mid (base %) | thin (base %) |
|---|---|---|---|---|---|
| L | 34/803 | 7 (21% of errs; rate 7.3%; base 12%) | 10 (29% of errs; rate 4.2%; base 29%) | 7 (21% of errs; rate 2.9%; base 30%) | 10 (29% of errs; rate 4.3%; base 29%) |
| A | 52/803 | 13 (25% of errs; rate 13.5%; base 12%) | 12 (23% of errs; rate 5.1%; base 29%) | 8 (15% of errs; rate 3.4%; base 30%) | 19 (37% of errs; rate 8.2%; base 29%) |
| B | 72/803 | 21 (29% of errs; rate 21.9%; base 12%) | 17 (24% of errs; rate 7.2%; base 29%) | 18 (25% of errs; rate 7.6%; base 30%) | 16 (22% of errs; rate 6.9%; base 29%) |
| C | 41/803 | 7 (17% of errs; rate 7.3%; base 12%) | 12 (29% of errs; rate 5.1%; base 29%) | 8 (20% of errs; rate 3.4%; base 30%) | 14 (34% of errs; rate 6.0%; base 29%) |
| E | 58/803 | 16 (28% of errs; rate 16.7%; base 12%) | 16 (28% of errs; rate 6.8%; base 29%) | 8 (14% of errs; rate 3.4%; base 30%) | 18 (31% of errs; rate 7.7%; base 29%) |
| F | 71/803 | 30 (42% of errs; rate 31.2%; base 12%) | 9 (13% of errs; rate 3.8%; base 29%) | 9 (13% of errs; rate 3.8%; base 30%) | 23 (32% of errs; rate 9.9%; base 29%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 | L+13 | L+14 | L+15 | L+16 | L+17 | L+18 | L+19 | L+20 | L+21 | L+22 | L+23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L | 2/79 | 3/88 | 4/76 | 0/28 | 3/30 | 2/28 | 0/30 | 0/30 | 1/28 | 3/31 | 2/30 | 0/29 | 3/29 | 1/25 | 2/29 | 0/30 | 0/26 | 0/26 | 2/27 | 1/24 | 2/27 | 2/24 | 1/29 |
| A | 3/79 | 4/88 | 11/76 | 1/28 | 4/30 | 2/28 | 1/30 | 1/30 | 1/28 | 4/31 | 3/30 | 0/29 | 4/29 | 1/25 | 2/29 | 0/30 | 0/26 | 1/26 | 2/27 | 2/24 | 2/27 | 2/24 | 1/29 |
| B | 10/79 | 7/88 | 16/76 | 0/28 | 5/30 | 3/28 | 2/30 | 4/30 | 3/28 | 5/31 | 2/30 | 1/29 | 2/29 | 1/25 | 4/29 | 0/30 | 0/26 | 0/26 | 0/27 | 2/24 | 2/27 | 2/24 | 1/29 |
| C | 3/79 | 3/88 | 5/76 | 1/28 | 4/30 | 2/28 | 1/30 | 1/30 | 1/28 | 4/31 | 2/30 | 0/29 | 3/29 | 1/25 | 2/29 | 0/30 | 0/26 | 0/26 | 2/27 | 1/24 | 2/27 | 2/24 | 1/29 |
| E | 6/79 | 7/88 | 15/76 | 1/28 | 5/30 | 1/28 | 1/30 | 4/30 | 1/28 | 5/31 | 1/30 | 2/29 | 1/29 | 0/25 | 2/29 | 1/30 | 0/26 | 0/26 | 0/27 | 1/24 | 2/27 | 2/24 | 0/29 |
| F | 11/79 | 16/88 | 11/76 | 1/28 | 3/30 | 2/28 | 0/30 | 0/30 | 2/28 | 3/31 | 3/30 | 2/29 | 2/29 | 0/25 | 1/29 | 2/30 | 0/26 | 1/26 | 1/27 | 2/24 | 4/27 | 3/24 | 1/29 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | L | A | B | C | E | F |
|---|---|---|---|---|---|---|---|
| L | 34 | - | 34/34 (31) | 30/34 (25) | 34/34 (34) | 22/34 (10) | 20/34 (11) |
| A | 52 | 34/52 (31) | - | 37/52 (32) | 41/52 (38) | 36/52 (25) | 29/52 (18) |
| B | 72 | 30/72 (25) | 37/72 (32) | - | 30/72 (25) | 33/72 (15) | 30/72 (15) |
| C | 41 | 34/41 (34) | 41/41 (38) | 30/41 (25) | - | 29/41 (17) | 20/41 (11) |
| E | 58 | 22/58 (10) | 36/58 (25) | 33/58 (15) | 29/58 (17) | - | 27/58 (15) |
| F | 71 | 20/71 (11) | 29/71 (18) | 30/71 (15) | 20/71 (11) | 27/71 (15) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 18; wrong in exactly one: 78

### Top (truth value <- read) pairs per pass, with feature profile

**L** (34 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| d <- T98 | 7 | 1/0/6 | 0/3/4 | 3/0/4 | 0/0 | 3/1/3 | A= 7, C= 7, B= 4, E= 2, F~ 1 | L06.18 L13.20 L15.9 L19.24 L19.6 L21.1 L23.21 |
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | A= 3, C= 3, F= 3, B= 2, E= 2, E~ 1, B~ 1 | L03.23 L05.4 L22.24 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | A= 3, B= 3, C= 3, E~ 3, F~ 2, F= 1 | L05.1 L10.4 L11.5 |
| l <- T64 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/0 | 2/0/0 | A= 2, B= 2, C= 2 | L14.22 L20.17 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, F~ 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, E~ 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, E= 1, F= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1 | L03.10 |
| c <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, C= 1, E~ 1, F~ 1 | L03.31 |
| c <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, C= 1, E~ 1, F~ 1 | L03.34 |

**A** (52 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/1 | 4/1/2 | C= 7, E= 7 | L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 |
| d <- T98 | 7 | 1/0/6 | 0/3/4 | 3/0/4 | 0/0 | 3/1/3 | L= 7, C= 7, B= 4, E= 2, F~ 1 | L06.18 L13.20 L15.9 L19.24 L19.6 L21.1 L23.21 |
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | L= 3, C= 3, F= 3, B= 2, E= 2, E~ 1, B~ 1 | L03.23 L05.4 L22.24 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | L= 3, B= 3, C= 3, E~ 3, F~ 2, F= 1 | L05.1 L10.4 L11.5 |
| i <- <deleted> | 2 | 0/1/1 | 0/0/1 | 0/0/1 | 1/0 | 1/0/0 | B= 1, E= 1, F~ 1 | L03.30 L11.32 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L~ 2, B= 2, C~ 2, E= 2, F= 1, F~ 1 | L03.31 L03.34 |
| l <- T64 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/0 | 2/0/0 | L= 2, B= 2, C= 2 | L14.22 L20.17 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, B= 1, C= 1, F~ 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, B= 1, C= 1, E~ 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, B= 1, C= 1, E= 1, F= 1 | L02.19 |

**B** (72 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| r <- T24 | 15 | 1/0/14 | 0/2/5 | 0/0/7 | 0/0 | 1/6/0 | F~ 3 | L01.15 L01.17 L01.20 L01.24 L01.29 L02.22 L02.25 L02.29 L02.4 L03.1 L03.16 L03.17 L03.4 L03.8 |
| d <- T98 | 11 | 1/0/10 | 0/3/8 | 4/2/5 | 0/0 | 4/3/4 | L= 4, A= 4, C= 4, F~ 2, E= 2 | L06.18 L07.23 L07.4 L08.17 L08.28 L09.3 L10.3 L10.8 L15.9 L21.1 L23.21 |
| e <- T76 | 4 | 1/0/3 | 0/0/4 | 4/0/0 | 0/0 | 2/0/2 | E~ 4, L= 3, A= 3, C= 3, F~ 2, F= 2, A~ 1 | L05.1 L10.4 L11.5 L20.15 |
| m <- X_NEW | 3 | 0/0/3 | 0/0/3 | 0/0/3 | 0/0 | 0/0/3 | E~ 3 | L05.7 L08.3 L08.5 |
| et <- T88 | 3 | 1/0/2 | 0/1/2 | 0/0/3 | 0/0 | 1/2/0 |  | L06.8 L09.1 L15.14 |
| l <- T66 | 3 | 0/0/3 | 0/1/2 | 2/0/1 | 0/0 | 0/1/2 |  | L11.4 L12.28 L15.11 |
| t <- T90 | 2 | 0/0/2 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | L= 2, A= 2, C= 2, F= 2, E~ 1, E= 1 | L03.23 L05.4 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L~ 2, A= 2, C~ 2, E= 2, F= 1, F~ 1 | L03.31 L03.34 |
| e <- T60 | 2 | 0/0/2 | 0/2/0 | 1/0/1 | 0/0 | 0/0/2 |  | L01.12 L05.11 |
| l <- T64 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/0 | 2/0/0 | L= 2, A= 2, C= 2 | L14.22 L20.17 |

**C** (41 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/1 | 4/1/2 | A= 7, E= 7 | L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 |
| d <- T98 | 7 | 1/0/6 | 0/3/4 | 3/0/4 | 0/0 | 3/1/3 | L= 7, A= 7, B= 4, E= 2, F~ 1 | L06.18 L13.20 L15.9 L19.24 L19.6 L21.1 L23.21 |
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | L= 3, A= 3, F= 3, B= 2, E= 2, E~ 1, B~ 1 | L03.23 L05.4 L22.24 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | L= 3, A= 3, B= 3, E~ 3, F~ 2, F= 1 | L05.1 L10.4 L11.5 |
| l <- T64 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/0 | 2/0/0 | L= 2, A= 2, B= 2 | L14.22 L20.17 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, A= 1, B= 1, F~ 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, A= 1, B= 1, E~ 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, A= 1, B= 1, E= 1, F= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, A= 1, B= 1 | L03.10 |
| c <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, A~ 1, B~ 1, E~ 1, F~ 1 | L03.31 |

**E** (58 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 15 | 2/0/13 | 2/1/10 | 0/0/13 | 1/1 | 8/2/3 | A= 7, C= 7 | L01.1 L01.23 L01.4 L02.1 L02.30 L02.9 L03.17 L03.4 L03.8 L03.9 L04.4 L05.25 L07.29 L08.10 L10.5 |
| e <- T89 | 4 | 1/0/3 | 0/0/4 | 4/0/0 | 0/0 | 2/0/2 | A~ 4, B~ 4, F~ 4, L~ 3, C~ 3 | L05.1 L10.4 L11.5 L20.15 |
| m <- T66 | 3 | 0/0/3 | 0/0/3 | 0/0/3 | 0/0 | 0/0/3 | B~ 3 | L05.7 L08.3 L08.5 |
| e <- T60 | 2 | 0/0/2 | 0/1/0 | 0/0/1 | 0/0 | 0/0/1 | F~ 1 | L01.23 L12.14 |
| n <- T86 | 2 | 0/0/2 | 0/1/0 | 0/0/1 | 0/0 | 0/0/1 |  | L01.20 L03.19 |
| t <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L~ 1, A~ 1, B~ 1, C~ 1, F~ 1, A= 1, B= 1, F= 1 | L03.23 L03.24 |
| i <- <deleted> | 2 | 0/1/1 | 0/0/1 | 0/0/1 | 1/0 | 1/0/0 | A= 1, B= 1, F~ 1 | L03.30 L12.32 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L~ 2, A= 2, B= 2, C~ 2, F= 1, F~ 1 | L03.31 L03.34 |
| t <- T90 | 2 | 0/0/2 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | L= 2, A= 2, C= 2, F= 2, B= 1, B~ 1 | L05.4 L22.24 |
| s <- T18 | 2 | 0/0/2 | 0/2/0 | 2/0/0 | 0/0 | 0/1/1 |  | L08.23 L10.12 |

**F** (71 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| m <- X_NEW | 8 | 1/0/7 | 0/2/6 | 0/2/6 | 0/0 | 5/3/0 |  | L11.22 L16.1 L16.14 L19.3 L20.24 L21.18 L21.3 L23.23 |
| r <- <deleted> | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 3 | L01.24 L01.29 L02.25 |
| a <- <deleted> | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.25 L01.26 L02.24 |
| c <- <deleted> | 3 | 0/0/3 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | L~ 3, C~ 3, A~ 2, B~ 2, A= 1, B= 1, E= 1, E~ 1 | L01.27 L03.31 L15.24 |
| d <- T36 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 1/1/0 | B~ 2, L~ 1, A~ 1, C~ 1 | L02.11 L06.18 L10.8 |
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | L= 3, A= 3, C= 3, B= 2, E= 2, E~ 1, B~ 1 | L03.23 L05.4 L22.24 |
| s <- T18 | 3 | 0/0/3 | 0/2/1 | 1/1/1 | 0/0 | 3/0/0 |  | L02.11 L02.17 L03.11 |
| i <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.22 L02.22 |
| e <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | E~ 1, A= 1, B= 1, E= 1 | L01.23 L03.32 |
| l <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, E~ 1 | L03.26 L03.29 |


### Reader agreement on the baseline's errors (baseline L; 34 errors; passes L, A, B, C, E, F)

| agree_class | errors | share |
|---|---|---|
| all-same-wrong | 6 | 17.6% |
| all-wrong-split | 12 | 35.3% |
| majority-wrong | 12 | 35.3% |
| minority-wrong | 4 | 11.8% |

| err_class | errors | all-same-wrong | all-wrong-split | majority-wrong | minority-wrong |
|---|---|---|---|---|---|
| crop | 10 | 2 (20%) | 4 (40%) | 3 (30%) | 1 (10%) |
| look-alike | 8 | 1 (12%) | 1 (12%) | 4 (50%) | 2 (25%) |
| thin | 3 | 0 (0%) | 3 (100%) | 0 (0%) | 0 (0%) |
| other | 13 | 3 (23%) | 4 (31%) | 5 (38%) | 1 (8%) |

| truth <- read | n | err_class | all-same-wrong | all-wrong-split | majority-wrong | minority-wrong | lines |
|---|---|---|---|---|---|---|---|
| d <- T98 | 7 | look-alike 4, crop 3 | 0 | 0 | 4 | 3 | L06.18 L13.20 L15.9 L19.24 L19.6 L21.1 L23.21 |
| t <- T90 | 3 | look-alike 2, crop 1 | 1 | 2 | 0 | 0 | L03.23 L05.4 L22.24 |
| e <- T76 | 3 | crop 3 | 0 | 3 | 0 | 0 | L05.1 L10.4 L11.5 |
| l <- T64 | 2 | look-alike 2 | 0 | 0 | 2 | 0 | L14.22 L20.17 |
| c <- T92 | 1 | other 1 | 0 | 0 | 1 | 0 | L01.27 |
| a <- T66 | 1 | other 1 | 0 | 0 | 1 | 0 | L01.28 |
| s <- T70 | 1 | other 1 | 1 | 0 | 0 | 0 | L02.19 |
| l <- T65 | 1 | other 1 | 0 | 0 | 1 | 0 | L03.10 |
| c <- T96 | 1 | other 1 | 0 | 1 | 0 | 0 | L03.31 |
| c <- T90 | 1 | other 1 | 0 | 1 | 0 | 0 | L03.34 |
