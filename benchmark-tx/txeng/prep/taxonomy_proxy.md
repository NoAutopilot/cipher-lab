## birago1572-no87: 343 scored positions, passes plain, sr4, tight, combo
- plain: 70 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- sr4: 62 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- tight: 63 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- combo: 63 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| plain | 70/343 | 2 (3% of errs; rate 20.0%; base 3%) | 61 (87% of errs; rate 18.9%; base 94%) | 7 (10% of errs; rate 63.6%; base 3%) |
| sr4 | 62/343 | 2 (3% of errs; rate 20.0%; base 3%) | 53 (85% of errs; rate 16.5%; base 94%) | 7 (11% of errs; rate 63.6%; base 3%) |
| tight | 63/343 | 2 (3% of errs; rate 20.0%; base 3%) | 54 (86% of errs; rate 16.8%; base 94%) | 7 (11% of errs; rate 63.6%; base 3%) |
| combo | 63/343 | 2 (3% of errs; rate 20.0%; base 3%) | 54 (86% of errs; rate 16.8%; base 94%) | 7 (11% of errs; rate 63.6%; base 3%) |

### Error mass by segment-crop edge (left/right)

| pass | errors | - (base %) | inner (base %) | overlap (base %) |
|---|---|---|---|---|
| plain | 70/343 | 1 (1% of errs; rate 25.0%; base 1%) | 49 (70% of errs; rate 22.5%; base 64%) | 20 (29% of errs; rate 16.5%; base 35%) |
| sr4 | 62/343 | 1 (2% of errs; rate 25.0%; base 1%) | 43 (69% of errs; rate 19.7%; base 64%) | 18 (29% of errs; rate 14.9%; base 35%) |
| tight | 63/343 | 1 (2% of errs; rate 25.0%; base 1%) | 44 (70% of errs; rate 20.2%; base 64%) | 18 (29% of errs; rate 14.9%; base 35%) |
| combo | 63/343 | 1 (2% of errs; rate 25.0%; base 1%) | 45 (71% of errs; rate 20.6%; base 64%) | 17 (27% of errs; rate 14.0%; base 35%) |

### Error mass by line-band edge (top/bottom)

| pass | errors | - (base %) | cut (base %) | in (base %) | near (base %) |
|---|---|---|---|---|---|
| plain | 70/343 | 1 (1% of errs; rate 25.0%; base 1%) | 15 (21% of errs; rate 26.3%; base 17%) | 51 (73% of errs; rate 19.8%; base 75%) | 3 (4% of errs; rate 12.5%; base 7%) |
| sr4 | 62/343 | 1 (2% of errs; rate 25.0%; base 1%) | 16 (26% of errs; rate 28.1%; base 17%) | 43 (69% of errs; rate 16.7%; base 75%) | 2 (3% of errs; rate 8.3%; base 7%) |
| tight | 63/343 | 1 (2% of errs; rate 25.0%; base 1%) | 16 (25% of errs; rate 28.1%; base 17%) | 45 (71% of errs; rate 17.4%; base 75%) | 1 (2% of errs; rate 4.2%; base 7%) |
| combo | 63/343 | 1 (2% of errs; rate 25.0%; base 1%) | 15 (24% of errs; rate 26.3%; base 17%) | 46 (73% of errs; rate 17.8%; base 75%) | 1 (2% of errs; rate 4.2%; base 7%) |

### Error mass by box<->token op (glued 2:1, split 1:2)

| pass | errors | - (base %) | 1:1 (base %) | 1:2 (base %) | 2:1 (base %) |
|---|---|---|---|---|---|
| plain | 70/343 | 1 (1% of errs; rate 25.0%; base 1%) | 55 (79% of errs; rate 17.0%; base 94%) | 4 (6% of errs; rate 100.0%; base 1%) | 10 (14% of errs; rate 83.3%; base 3%) |
| sr4 | 62/343 | 1 (2% of errs; rate 25.0%; base 1%) | 47 (76% of errs; rate 14.6%; base 94%) | 4 (6% of errs; rate 100.0%; base 1%) | 10 (16% of errs; rate 83.3%; base 3%) |
| tight | 63/343 | 1 (2% of errs; rate 25.0%; base 1%) | 48 (76% of errs; rate 14.9%; base 94%) | 4 (6% of errs; rate 100.0%; base 1%) | 10 (16% of errs; rate 83.3%; base 3%) |
| combo | 63/343 | 1 (2% of errs; rate 25.0%; base 1%) | 48 (76% of errs; rate 14.9%; base 94%) | 4 (6% of errs; rate 100.0%; base 1%) | 10 (16% of errs; rate 83.3%; base 3%) |

### Error mass by stroke weight (erosion-survival terciles)

| pass | errors | - (base %) | heavy (base %) | mid (base %) | thin (base %) |
|---|---|---|---|---|---|
| plain | 70/343 | 1 (1% of errs; rate 25.0%; base 1%) | 20 (29% of errs; rate 17.7%; base 33%) | 21 (30% of errs; rate 18.6%; base 33%) | 28 (40% of errs; rate 24.8%; base 33%) |
| sr4 | 62/343 | 1 (2% of errs; rate 25.0%; base 1%) | 17 (27% of errs; rate 15.0%; base 33%) | 19 (31% of errs; rate 16.8%; base 33%) | 25 (40% of errs; rate 22.1%; base 33%) |
| tight | 63/343 | 1 (2% of errs; rate 25.0%; base 1%) | 18 (29% of errs; rate 15.9%; base 33%) | 16 (25% of errs; rate 14.2%; base 33%) | 28 (44% of errs; rate 24.8%; base 33%) |
| combo | 63/343 | 1 (2% of errs; rate 25.0%; base 1%) | 19 (30% of errs; rate 16.8%; base 33%) | 17 (27% of errs; rate 15.0%; base 33%) | 26 (41% of errs; rate 23.0%; base 33%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain | 4/27 | 4/27 | 3/25 | 5/28 | 7/30 | 8/28 | 4/30 | 6/30 | 9/28 | 7/31 | 11/30 | 2/29 |
| sr4 | 4/27 | 4/27 | 3/25 | 3/28 | 8/30 | 8/28 | 2/30 | 6/30 | 7/28 | 6/31 | 10/30 | 1/29 |
| tight | 3/27 | 3/27 | 3/25 | 3/28 | 8/30 | 7/28 | 3/30 | 6/30 | 8/28 | 6/31 | 11/30 | 2/29 |
| combo | 4/27 | 3/27 | 4/25 | 3/28 | 8/30 | 7/28 | 3/30 | 5/30 | 9/28 | 6/31 | 10/30 | 1/29 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | plain | sr4 | tight | combo |
|---|---|---|---|---|---|
| plain | 70 | - | 61/70 (54) | 61/70 (58) | 60/70 (50) |
| sr4 | 62 | 61/62 (54) | - | 59/62 (50) | 59/62 (49) |
| tight | 63 | 61/63 (58) | 59/63 (50) | - | 60/63 (50) |
| combo | 63 | 60/63 (50) | 59/63 (49) | 60/63 (50) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 57; wrong in exactly one: 9

### Top (truth value <- read) pairs per pass, with feature profile

**plain** (70 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 5/0/2 | sr4= 7, tight= 7, combo= 7 | L01.23 L03.4 L04.4 L05.25 L08.10 L10.5 L11.6 |
| o <- T83 | 7 | 0/0/7 | 0/3/4 | 0/0/7 | 1/0 | 2/3/2 | sr4= 3, tight= 3, combo= 2 | L04.19 L05.26 L06.12 L06.7 L07.8 L11.20 L12.21 |
| i <- _ | 5 | 0/3/2 | 0/2/3 | 1/1/3 | 3/1 | 3/2/0 | sr4= 5, tight= 4, combo= 3, combo~ 2, tight~ 1 | L08.19 L10.21 L10.32 L11.32 L12.32 |
| d <- T36 | 3 | 1/0/2 | 0/0/3 | 2/0/1 | 0/0 | 2/1/0 | sr4= 3, tight= 3, combo= 3 | L01.1 L04.16 L06.18 |
| n <- _ | 3 | 0/1/2 | 0/0/2 | 0/0/2 | 1/0 | 2/0/0 | sr4= 2, tight= 2, combo= 2 | L05.31 L10.17 L10.22 |
| f <- T37 | 3 | 0/0/3 | 0/1/2 | 1/0/2 | 0/0 | 1/0/2 | sr4= 3, tight= 3, combo= 3 | L06.9 L10.27 L11.19 |
| a <- _ | 2 | 0/1/1 | 0/0/2 | 0/1/1 | 1/0 | 1/1/0 | sr4= 1, sr4~ 1, tight= 1, combo~ 1 | L02.16 L07.30 |
| carmagnola <- _ | 2 | 0/1/1 | 0/0/2 | 0/0/2 | 2/0 | 2/0/0 | sr4= 2, tight= 2, combo= 2 | L03.24 L08.30 |
| e <- T85 | 2 | 0/1/1 | 0/0/2 | 0/0/2 | 0/0 | 0/1/1 | sr4= 2, combo= 2, tight~ 1, tight= 1 | L03.26 L08.2 |
| l <- _ | 2 | 0/0/2 | 0/0/2 | 1/0/1 | 0/0 | 1/0/1 | tight= 2, combo= 2, sr4= 1 | L09.13 L11.31 |

**sr4** (62 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 5/0/2 | plain= 7, tight= 7, combo= 7 | L01.23 L03.4 L04.4 L05.25 L08.10 L10.5 L11.6 |
| i <- _ | 5 | 0/3/2 | 0/2/3 | 1/1/3 | 3/1 | 3/2/0 | plain= 5, tight= 4, combo= 3, combo~ 2, tight~ 1 | L08.19 L10.21 L10.32 L11.32 L12.32 |
| d <- T36 | 3 | 1/0/2 | 0/0/3 | 2/0/1 | 0/0 | 2/1/0 | plain= 3, tight= 3, combo= 3 | L01.1 L04.16 L06.18 |
| o <- T83 | 3 | 0/0/3 | 0/1/2 | 0/0/3 | 1/0 | 1/2/0 | plain= 3, tight= 2, combo= 2 | L05.26 L06.12 L06.7 |
| f <- T37 | 3 | 0/0/3 | 0/1/2 | 1/0/2 | 0/0 | 1/0/2 | plain= 3, tight= 3, combo= 3 | L06.9 L10.27 L11.19 |
| carmagnola <- _ | 2 | 0/1/1 | 0/0/2 | 0/0/2 | 2/0 | 2/0/0 | plain= 2, tight= 2, combo= 2 | L03.24 L08.30 |
| e <- T85 | 2 | 0/1/1 | 0/0/2 | 0/0/2 | 0/0 | 0/1/1 | plain= 2, combo= 2, tight~ 1, tight= 1 | L03.26 L08.2 |
| n <- _ | 2 | 0/1/1 | 0/0/1 | 0/0/1 | 1/0 | 1/0/0 | plain= 2, tight= 2, combo= 2 | L05.31 L10.22 |
| z <- T83 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/1 | 0/2/0 | combo= 2, plain= 1, tight= 1, plain~ 1, tight~ 1 | L06.15 L11.9 |
| l <- _ | 2 | 0/0/2 | 0/0/2 | 1/0/1 | 1/0 | 1/1/0 | plain~ 1, tight~ 1, combo~ 1, plain= 1, tight= 1, combo= 1 | L08.26 L11.31 |

**tight** (63 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 5/0/2 | plain= 7, sr4= 7, combo= 7 | L01.23 L03.4 L04.4 L05.25 L08.10 L10.5 L11.6 |
| i <- _ | 5 | 0/3/2 | 0/2/3 | 0/1/4 | 4/1 | 4/1/0 | plain= 4, sr4= 4, combo= 3, combo~ 2, plain~ 1, sr4~ 1 | L04.21 L10.21 L10.32 L11.32 L12.32 |
| d <- T36 | 3 | 1/0/2 | 0/0/3 | 2/0/1 | 0/0 | 2/1/0 | plain= 3, sr4= 3, combo= 3 | L01.1 L04.16 L06.18 |
| o <- T83 | 3 | 0/0/3 | 0/0/3 | 0/0/3 | 1/0 | 2/1/0 | plain= 3, sr4= 2, combo= 2 | L05.26 L06.7 L11.20 |
| f <- T37 | 3 | 0/0/3 | 0/1/2 | 1/0/2 | 0/0 | 1/0/2 | plain= 3, sr4= 3, combo= 3 | L06.9 L10.27 L11.19 |
| carmagnola <- _ | 2 | 0/1/1 | 0/0/2 | 0/0/2 | 2/0 | 2/0/0 | plain= 2, sr4= 2, combo= 2 | L03.24 L08.30 |
| n <- _ | 2 | 0/1/1 | 0/0/1 | 0/0/1 | 1/0 | 1/0/0 | plain= 2, sr4= 2, combo= 2 | L05.31 L10.22 |
| l <- _ | 2 | 0/0/2 | 0/0/2 | 1/0/1 | 0/0 | 1/0/1 | plain= 2, combo= 2, sr4= 1 | L09.13 L11.31 |
| e <- T37 | 2 | 0/0/2 | 0/1/1 | 1/0/1 | 0/0 | 0/1/1 | plain= 2, sr4= 2, combo= 1, combo~ 1 | L09.21 L11.16 |
| z <- _ | 1 | 0/0/1 | 0/1/0 | 0/0/1 | 0/0 | 0/1/0 | plain= 1, sr4= 1, combo= 1 | L01.11 |

**combo** (63 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 5/0/2 | plain= 7, sr4= 7, tight= 7 | L01.23 L03.4 L04.4 L05.25 L08.10 L10.5 L11.6 |
| d <- T36 | 3 | 1/0/2 | 0/0/3 | 2/0/1 | 0/0 | 2/1/0 | plain= 3, sr4= 3, tight= 3 | L01.1 L04.16 L06.18 |
| o <- T83 | 3 | 0/0/3 | 0/0/3 | 0/0/3 | 1/0 | 2/1/0 | plain= 2, sr4= 2, tight= 2 | L03.17 L05.26 L06.7 |
| f <- T37 | 3 | 0/0/3 | 0/1/2 | 1/0/2 | 0/0 | 1/0/2 | plain= 3, sr4= 3, tight= 3 | L06.9 L10.27 L11.19 |
| i <- _ | 3 | 0/2/1 | 0/1/2 | 0/1/2 | 2/1 | 2/1/0 | plain= 3, sr4= 3, tight= 3 | L10.21 L10.32 L11.32 |
| carmagnola <- _ | 2 | 0/1/1 | 0/0/2 | 0/0/2 | 2/0 | 2/0/0 | plain= 2, sr4= 2, tight= 2 | L03.24 L08.30 |
| e <- T85 | 2 | 0/1/1 | 0/0/2 | 0/0/2 | 0/0 | 0/1/1 | plain= 2, sr4= 2, tight~ 1, tight= 1 | L03.26 L08.2 |
| n <- _ | 2 | 0/1/1 | 0/0/1 | 0/0/1 | 1/0 | 1/0/0 | plain= 2, sr4= 2, tight= 2 | L05.31 L10.22 |
| z <- T83 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/1 | 0/2/0 | sr4= 2, plain= 1, tight= 1, plain~ 1, tight~ 1 | L06.15 L11.9 |
| l <- _ | 2 | 0/0/2 | 0/0/2 | 1/0/1 | 0/0 | 1/0/1 | plain= 2, tight= 2, sr4= 1 | L09.13 L11.31 |

