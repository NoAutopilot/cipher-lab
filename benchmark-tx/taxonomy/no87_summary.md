## birago1572-no87: 803 scored positions, passes A, B, C, L, E, F, pad, s125, warp
- A: 54 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- B: 74 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- C: 43 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- L: 36 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- E: 60 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- F: 73 wrong-or-deleted of 803 covered positions (insertions not counted here; tx_bench adds them)
- pad: 24 wrong-or-deleted of 164 covered positions (insertions not counted here; tx_bench adds them)
- s125: 22 wrong-or-deleted of 164 covered positions (insertions not counted here; tx_bench adds them)
- warp: 23 wrong-or-deleted of 164 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 54/803 | 4 (7% of errs; rate 16.0%; base 3%) | 49 (91% of errs; rate 6.5%; base 94%) | 1 (2% of errs; rate 4.2%; base 3%) |
| B | 74/803 | 6 (8% of errs; rate 24.0%; base 3%) | 68 (92% of errs; rate 9.0%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| C | 43/803 | 4 (9% of errs; rate 16.0%; base 3%) | 39 (91% of errs; rate 5.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| L | 36/803 | 4 (11% of errs; rate 16.0%; base 3%) | 32 (89% of errs; rate 4.2%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| E | 60/803 | 4 (7% of errs; rate 16.0%; base 3%) | 55 (92% of errs; rate 7.3%; base 94%) | 1 (2% of errs; rate 4.2%; base 3%) |
| F | 73/803 | 2 (3% of errs; rate 8.0%; base 3%) | 67 (92% of errs; rate 8.9%; base 94%) | 4 (5% of errs; rate 16.7%; base 3%) |
| pad | 24/164 | 0 (0% of errs; rate 0.0%; base 3%) | 24 (100% of errs; rate 15.5%; base 95%) | 0 (0% of errs; rate 0.0%; base 2%) |
| s125 | 22/164 | 1 (5% of errs; rate 20.0%; base 3%) | 21 (95% of errs; rate 13.5%; base 95%) | 0 (0% of errs; rate 0.0%; base 2%) |
| warp | 23/164 | 0 (0% of errs; rate 0.0%; base 3%) | 23 (100% of errs; rate 14.8%; base 95%) | 0 (0% of errs; rate 0.0%; base 2%) |

### Error mass by segment-crop edge (left/right)

| pass | errors | - (base %) | edge (base %) | inner (base %) | overlap (base %) |
|---|---|---|---|---|---|
| A | 54/803 | 14 (26% of errs; rate 15.4%; base 11%) | 0 (0% of errs; rate 0.0%; base 0%) | 29 (54% of errs; rate 6.3%; base 57%) | 11 (20% of errs; rate 4.4%; base 31%) |
| B | 74/803 | 20 (27% of errs; rate 22.0%; base 11%) | 0 (0% of errs; rate 0.0%; base 0%) | 39 (53% of errs; rate 8.5%; base 57%) | 15 (20% of errs; rate 6.0%; base 31%) |
| C | 43/803 | 7 (16% of errs; rate 7.7%; base 11%) | 0 (0% of errs; rate 0.0%; base 0%) | 27 (63% of errs; rate 5.9%; base 57%) | 9 (21% of errs; rate 3.6%; base 31%) |
| L | 36/803 | 7 (19% of errs; rate 7.7%; base 11%) | 0 (0% of errs; rate 0.0%; base 0%) | 21 (58% of errs; rate 4.6%; base 57%) | 8 (22% of errs; rate 3.2%; base 31%) |
| E | 60/803 | 16 (27% of errs; rate 17.6%; base 11%) | 2 (3% of errs; rate 66.7%; base 0%) | 33 (55% of errs; rate 7.2%; base 57%) | 9 (15% of errs; rate 3.6%; base 31%) |
| F | 73/803 | 31 (42% of errs; rate 34.1%; base 11%) | 0 (0% of errs; rate 0.0%; base 0%) | 28 (38% of errs; rate 6.1%; base 57%) | 14 (19% of errs; rate 5.6%; base 31%) |
| pad | 24/164 | 19 (79% of errs; rate 22.6%; base 51%) | 0 (0% of errs; rate 0.0%; base 2%) | 5 (21% of errs; rate 9.3%; base 33%) | 0 (0% of errs; rate 0.0%; base 14%) |
| s125 | 22/164 | 19 (86% of errs; rate 22.6%; base 51%) | 0 (0% of errs; rate 0.0%; base 2%) | 1 (5% of errs; rate 1.9%; base 33%) | 2 (9% of errs; rate 8.7%; base 14%) |
| warp | 23/164 | 17 (74% of errs; rate 20.2%; base 51%) | 0 (0% of errs; rate 0.0%; base 2%) | 5 (22% of errs; rate 9.3%; base 33%) | 1 (4% of errs; rate 4.3%; base 14%) |

### Error mass by line-band edge (top/bottom)

| pass | errors | - (base %) | cut (base %) | in (base %) | near (base %) |
|---|---|---|---|---|---|
| A | 54/803 | 14 (26% of errs; rate 15.4%; base 11%) | 11 (20% of errs; rate 9.5%; base 14%) | 28 (52% of errs; rate 5.2%; base 67%) | 1 (2% of errs; rate 1.9%; base 7%) |
| B | 74/803 | 20 (27% of errs; rate 22.0%; base 11%) | 15 (20% of errs; rate 12.9%; base 14%) | 36 (49% of errs; rate 6.6%; base 67%) | 3 (4% of errs; rate 5.6%; base 7%) |
| C | 43/803 | 7 (16% of errs; rate 7.7%; base 11%) | 10 (23% of errs; rate 8.6%; base 14%) | 25 (58% of errs; rate 4.6%; base 67%) | 1 (2% of errs; rate 1.9%; base 7%) |
| L | 36/803 | 7 (19% of errs; rate 7.7%; base 11%) | 10 (28% of errs; rate 8.6%; base 14%) | 18 (50% of errs; rate 3.3%; base 67%) | 1 (3% of errs; rate 1.9%; base 7%) |
| E | 60/803 | 16 (27% of errs; rate 17.6%; base 11%) | 14 (23% of errs; rate 12.1%; base 14%) | 29 (48% of errs; rate 5.4%; base 67%) | 1 (2% of errs; rate 1.9%; base 7%) |
| F | 73/803 | 31 (42% of errs; rate 34.1%; base 11%) | 12 (16% of errs; rate 10.3%; base 14%) | 25 (34% of errs; rate 4.6%; base 67%) | 5 (7% of errs; rate 9.3%; base 7%) |
| pad | 24/164 | 19 (79% of errs; rate 22.6%; base 51%) | 0 (0% of errs; rate 0.0%; base 5%) | 5 (21% of errs; rate 7.2%; base 42%) | 0 (0% of errs; rate 0.0%; base 2%) |
| s125 | 22/164 | 19 (86% of errs; rate 22.6%; base 51%) | 0 (0% of errs; rate 0.0%; base 5%) | 3 (14% of errs; rate 4.3%; base 42%) | 0 (0% of errs; rate 0.0%; base 2%) |
| warp | 23/164 | 17 (74% of errs; rate 20.2%; base 51%) | 0 (0% of errs; rate 0.0%; base 5%) | 6 (26% of errs; rate 8.7%; base 42%) | 0 (0% of errs; rate 0.0%; base 2%) |

### Error mass by box<->token op (glued 2:1, split 1:2)

| pass | errors | - (base %) | 1:1 (base %) | 1:2 (base %) | 2:1 (base %) |
|---|---|---|---|---|---|
| A | 54/803 | 14 (26% of errs; rate 15.4%; base 11%) | 38 (70% of errs; rate 5.6%; base 85%) | 1 (2% of errs; rate 14.3%; base 1%) | 1 (2% of errs; rate 4.5%; base 3%) |
| B | 74/803 | 20 (27% of errs; rate 22.0%; base 11%) | 52 (70% of errs; rate 7.6%; base 85%) | 1 (1% of errs; rate 14.3%; base 1%) | 1 (1% of errs; rate 4.5%; base 3%) |
| C | 43/803 | 7 (16% of errs; rate 7.7%; base 11%) | 35 (81% of errs; rate 5.1%; base 85%) | 1 (2% of errs; rate 14.3%; base 1%) | 0 (0% of errs; rate 0.0%; base 3%) |
| L | 36/803 | 7 (19% of errs; rate 7.7%; base 11%) | 28 (78% of errs; rate 4.1%; base 85%) | 1 (3% of errs; rate 14.3%; base 1%) | 0 (0% of errs; rate 0.0%; base 3%) |
| E | 60/803 | 16 (27% of errs; rate 17.6%; base 11%) | 40 (67% of errs; rate 5.9%; base 85%) | 1 (2% of errs; rate 14.3%; base 1%) | 3 (5% of errs; rate 13.6%; base 3%) |
| F | 73/803 | 31 (42% of errs; rate 34.1%; base 11%) | 39 (53% of errs; rate 5.7%; base 85%) | 1 (1% of errs; rate 14.3%; base 1%) | 2 (3% of errs; rate 9.1%; base 3%) |
| pad | 24/164 | 19 (79% of errs; rate 22.6%; base 51%) | 5 (21% of errs; rate 6.9%; base 44%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 5%) |
| s125 | 22/164 | 19 (86% of errs; rate 22.6%; base 51%) | 3 (14% of errs; rate 4.2%; base 44%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 5%) |
| warp | 23/164 | 17 (74% of errs; rate 20.2%; base 51%) | 6 (26% of errs; rate 8.3%; base 44%) | 0 (0% of errs; rate 0.0%; base 0%) | 0 (0% of errs; rate 0.0%; base 5%) |

### Error mass by stroke weight (erosion-survival terciles)

| pass | errors | - (base %) | heavy (base %) | mid (base %) | thin (base %) |
|---|---|---|---|---|---|
| A | 54/803 | 14 (26% of errs; rate 15.4%; base 11%) | 10 (19% of errs; rate 4.2%; base 30%) | 10 (19% of errs; rate 4.2%; base 30%) | 20 (37% of errs; rate 8.5%; base 29%) |
| B | 74/803 | 20 (27% of errs; rate 22.0%; base 11%) | 16 (22% of errs; rate 6.7%; base 30%) | 20 (27% of errs; rate 8.4%; base 30%) | 18 (24% of errs; rate 7.7%; base 29%) |
| C | 43/803 | 7 (16% of errs; rate 7.7%; base 11%) | 10 (23% of errs; rate 4.2%; base 30%) | 10 (23% of errs; rate 4.2%; base 30%) | 16 (37% of errs; rate 6.8%; base 29%) |
| L | 36/803 | 7 (19% of errs; rate 7.7%; base 11%) | 7 (19% of errs; rate 2.9%; base 30%) | 9 (25% of errs; rate 3.8%; base 30%) | 13 (36% of errs; rate 5.5%; base 29%) |
| E | 60/803 | 16 (27% of errs; rate 17.6%; base 11%) | 17 (28% of errs; rate 7.1%; base 30%) | 9 (15% of errs; rate 3.8%; base 30%) | 18 (30% of errs; rate 7.7%; base 29%) |
| F | 73/803 | 31 (42% of errs; rate 34.1%; base 11%) | 10 (14% of errs; rate 4.2%; base 30%) | 10 (14% of errs; rate 4.2%; base 30%) | 22 (30% of errs; rate 9.4%; base 29%) |
| pad | 24/164 | 19 (79% of errs; rate 22.6%; base 51%) | 1 (4% of errs; rate 5.9%; base 10%) | 3 (12% of errs; rate 10.3%; base 18%) | 1 (4% of errs; rate 2.9%; base 21%) |
| s125 | 22/164 | 19 (86% of errs; rate 22.6%; base 51%) | 2 (9% of errs; rate 11.8%; base 10%) | 0 (0% of errs; rate 0.0%; base 18%) | 1 (5% of errs; rate 2.9%; base 21%) |
| warp | 23/164 | 17 (74% of errs; rate 20.2%; base 51%) | 1 (4% of errs; rate 5.9%; base 10%) | 3 (13% of errs; rate 10.3%; base 18%) | 2 (9% of errs; rate 5.9%; base 21%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 | L+13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7/109 | 5/117 | 15/105 | 2/53 | 6/59 | 2/58 | 1/56 | 2/56 | 3/55 | 6/55 | 2/27 | 2/24 | 1/29 |
| B | 13/109 | 9/117 | 18/105 | 1/53 | 9/59 | 3/58 | 2/56 | 4/56 | 3/55 | 7/55 | 2/27 | 2/24 | 1/29 |
| C | 6/109 | 4/117 | 8/105 | 2/53 | 6/59 | 2/58 | 1/56 | 1/56 | 3/55 | 5/55 | 2/27 | 2/24 | 1/29 |
| L | 5/109 | 4/117 | 7/105 | 1/53 | 5/59 | 2/58 | 0/56 | 0/56 | 3/55 | 4/55 | 2/27 | 2/24 | 1/29 |
| E | 8/109 | 10/117 | 16/105 | 1/53 | 7/59 | 2/58 | 1/56 | 4/56 | 1/55 | 6/55 | 2/27 | 2/24 | 0/29 |
| F | 15/109 | 19/117 | 13/105 | 1/53 | 4/59 | 4/58 | 0/56 | 1/56 | 3/55 | 5/55 | 4/27 | 3/24 | 1/29 |
| pad | 6/52 | 7/61 | 11/51 |  |  |  |  |  |  |  |  |  |  |
| s125 | 3/52 | 8/61 | 11/51 |  |  |  |  |  |  |  |  |  |  |
| warp | 6/52 | 6/61 | 11/51 |  |  |  |  |  |  |  |  |  |  |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | B | C | L | E | F | pad | s125 | warp |
|---|---|---|---|---|---|---|---|---|---|---|
| A | 54 | - | 39/54 (34) | 43/54 (40) | 36/54 (33) | 38/54 (27) | 31/54 (20) | 14/14 (12) | 13/14 (10) | 14/14 (13) |
| B | 74 | 39/74 (34) | - | 32/74 (27) | 32/74 (27) | 35/74 (17) | 32/74 (17) | 14/30 (11) | 13/30 (9) | 15/30 (15) |
| C | 43 | 43/43 (40) | 32/43 (27) | - | 36/43 (36) | 31/43 (19) | 22/43 (13) | 8/8 (4) | 7/8 (3) | 8/8 (5) |
| L | 36 | 36/36 (33) | 32/36 (27) | 36/36 (36) | - | 24/36 (12) | 22/36 (13) | 8/8 (4) | 7/8 (3) | 8/8 (5) |
| E | 60 | 38/60 (27) | 35/60 (17) | 31/60 (19) | 24/60 (12) | - | 29/60 (17) | 14/23 (11) | 13/23 (11) | 13/23 (9) |
| F | 73 | 31/73 (20) | 32/73 (17) | 22/73 (13) | 22/73 (13) | 29/73 (17) | - | 14/31 (9) | 11/31 (6) | 13/31 (8) |
| pad | 24 | 14/24 (12) | 14/24 (11) | 8/24 (4) | 8/24 (4) | 14/24 (11) | 14/24 (9) | - | 14/24 (10) | 21/24 (18) |
| s125 | 22 | 13/22 (10) | 13/22 (9) | 7/22 (3) | 7/22 (3) | 13/22 (11) | 11/22 (6) | 14/22 (10) | - | 14/22 (10) |
| warp | 23 | 14/23 (13) | 15/23 (15) | 8/23 (5) | 8/23 (5) | 13/23 (9) | 13/23 (8) | 21/23 (18) | 14/23 (10) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 20; wrong in exactly one: 80

### Top (truth value <- read) pairs per pass, with feature profile

**A** (54 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 3/1/3 | C= 7, E= 7 | L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 |
| d <- T98 | 7 | 1/0/6 | 0/3/4 | 3/0/4 | 0/0 | 4/1/2 | C= 7, L= 7, B= 4, E= 2, F~ 1 | L06.18 L13.20 L15.9 L19.24 L19.6 L21.1 L23.21 |
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | C= 3, L= 3, F= 3, B= 2, E= 2, E~ 1, pad= 1, s125~ 1, warp= 1, B~ 1 | L03.23 L05.4 L22.24 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | B= 3, C= 3, L= 3, E~ 3, F~ 2, F= 1 | L05.1 L10.4 L11.5 |
| i <- <deleted> | 2 | 0/1/1 | 0/0/1 | 0/0/1 | 1/0 | 1/0/0 | B= 1, E= 1, pad= 1, s125= 1, warp= 1, F~ 1 | L03.30 L11.32 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 2, C~ 2, L~ 2, E= 2, pad= 2, s125= 2, warp= 2, F= 1, F~ 1 | L03.31 L03.34 |
| l <- T64 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/0 | 2/0/0 | B= 2, C= 2, L= 2 | L14.22 L20.17 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, C= 1, L= 1, F~ 1, pad= 1, warp= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, C= 1, L= 1, E~ 1, pad~ 1, s125~ 1, warp= 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B= 1, C= 1, L= 1, E= 1, F= 1, pad= 1, s125= 1, warp= 1 | L02.19 |

**B** (74 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| r <- T24 | 15 | 1/0/14 | 0/2/6 | 0/0/8 | 0/0 | 2/6/0 | F~ 3 | L01.15 L01.17 L01.20 L01.24 L01.29 L02.22 L02.25 L02.29 L02.4 L03.1 L03.16 L03.17 L03.4 L03.8 |
| d <- T98 | 11 | 1/0/10 | 0/3/8 | 4/2/5 | 0/0 | 4/3/4 | A= 4, C= 4, L= 4, F~ 2, E= 2 | L06.18 L07.23 L07.4 L08.17 L08.28 L09.3 L10.3 L10.8 L15.9 L21.1 L23.21 |
| e <- T76 | 4 | 1/0/3 | 0/0/4 | 4/0/0 | 0/0 | 2/0/2 | E~ 4, A= 3, C= 3, L= 3, F~ 2, F= 2, A~ 1 | L05.1 L10.4 L11.5 L20.15 |
| m <- X_NEW | 3 | 0/0/3 | 0/0/3 | 0/0/3 | 0/0 | 0/0/3 | E~ 3 | L05.7 L08.3 L08.5 |
| et <- T88 | 3 | 1/0/2 | 0/1/2 | 0/0/3 | 0/0 | 1/2/0 |  | L06.8 L09.1 L15.14 |
| l <- T66 | 3 | 0/0/3 | 0/1/2 | 2/0/1 | 0/0 | 0/1/2 |  | L11.4 L12.28 L15.11 |
| t <- T90 | 2 | 0/0/2 | 0/0/1 | 0/0/1 | 0/0 | 0/0/1 | A= 2, C= 2, L= 2, F= 2, E~ 1, pad= 1, s125~ 1, warp= 1, E= 1 | L03.23 L05.4 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, C~ 2, L~ 2, E= 2, pad= 2, s125= 2, warp= 2, F= 1, F~ 1 | L03.31 L03.34 |
| e <- T60 | 2 | 0/0/2 | 0/2/0 | 1/0/1 | 0/0 | 0/0/2 |  | L01.12 L05.11 |
| l <- T64 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/0 | 2/0/0 | A= 2, C= 2, L= 2 | L14.22 L20.17 |

**C** (43 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 7 | 0/0/7 | 0/1/6 | 0/0/7 | 0/0 | 3/1/3 | A= 7, E= 7 | L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 |
| d <- T98 | 7 | 1/0/6 | 0/3/4 | 3/0/4 | 0/0 | 4/1/2 | A= 7, L= 7, B= 4, E= 2, F~ 1 | L06.18 L13.20 L15.9 L19.24 L19.6 L21.1 L23.21 |
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | A= 3, L= 3, F= 3, B= 2, E= 2, E~ 1, pad= 1, s125~ 1, warp= 1, B~ 1 | L03.23 L05.4 L22.24 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | A= 3, B= 3, L= 3, E~ 3, F~ 2, F= 1 | L05.1 L10.4 L11.5 |
| l <- T64 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/0 | 2/0/0 | A= 2, B= 2, L= 2 | L14.22 L20.17 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, L= 1, F~ 1, pad= 1, warp= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, L= 1, E~ 1, pad~ 1, s125~ 1, warp= 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, L= 1, E= 1, F= 1, pad= 1, s125= 1, warp= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, L= 1, pad~ 1, s125= 1, warp= 1 | L03.10 |
| c <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, L= 1, E~ 1, F~ 1, pad~ 1, s125~ 1, warp~ 1 | L03.31 |

**L** (36 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| d <- T98 | 7 | 1/0/6 | 0/3/4 | 3/0/4 | 0/0 | 4/1/2 | A= 7, C= 7, B= 4, E= 2, F~ 1 | L06.18 L13.20 L15.9 L19.24 L19.6 L21.1 L23.21 |
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | A= 3, C= 3, F= 3, B= 2, E= 2, E~ 1, pad= 1, s125~ 1, warp= 1, B~ 1 | L03.23 L05.4 L22.24 |
| e <- T76 | 3 | 1/0/2 | 0/0/3 | 3/0/0 | 0/0 | 1/0/2 | A= 3, B= 3, C= 3, E~ 3, F~ 2, F= 1 | L05.1 L10.4 L11.5 |
| l <- T64 | 2 | 0/0/2 | 0/2/0 | 0/0/2 | 0/0 | 2/0/0 | A= 2, B= 2, C= 2 | L14.22 L20.17 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, F~ 1, pad= 1, warp= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, E~ 1, pad~ 1, s125~ 1, warp= 1 | L01.28 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, E= 1, F= 1, pad= 1, s125= 1, warp= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, pad~ 1, s125= 1, warp= 1 | L03.10 |
| c <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, C= 1, E~ 1, F~ 1, pad~ 1, s125~ 1, warp~ 1 | L03.31 |
| c <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, C= 1, E~ 1, F~ 1, pad~ 1, s125~ 1, warp~ 1 | L03.34 |

**E** (60 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 15 | 2/0/13 | 2/1/10 | 1/0/12 | 1/0 | 7/1/5 | A= 7, C= 7 | L01.1 L01.23 L01.4 L02.1 L02.30 L02.9 L03.17 L03.4 L03.8 L03.9 L04.4 L05.25 L07.29 L08.10 L10.5 |
| e <- T89 | 4 | 1/0/3 | 0/0/4 | 4/0/0 | 0/0 | 2/0/2 | A~ 4, B~ 4, F~ 4, C~ 3, L~ 3 | L05.1 L10.4 L11.5 L20.15 |
| m <- T66 | 3 | 0/0/3 | 0/0/3 | 0/0/3 | 0/0 | 0/0/3 | B~ 3 | L05.7 L08.3 L08.5 |
| e <- T60 | 2 | 0/0/2 | 0/1/0 | 0/0/1 | 0/0 | 0/0/1 | F~ 1, pad= 1, warp= 1 | L01.23 L12.14 |
| n <- T86 | 2 | 0/0/2 | 0/1/0 | 0/0/1 | 0/0 | 0/0/1 |  | L01.20 L03.19 |
| t <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | s125= 2, A~ 1, B~ 1, C~ 1, L~ 1, F~ 1, pad~ 1, warp~ 1, A= 1, B= 1, F= 1, pad= 1, warp= 1 | L03.23 L03.24 |
| i <- <deleted> | 2 | 0/1/1 | 0/0/1 | 0/0/1 | 1/0 | 1/0/0 | A= 1, B= 1, pad= 1, s125= 1, warp= 1, F~ 1 | L03.30 L12.32 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, B= 2, C~ 2, L~ 2, pad= 2, s125= 2, warp= 2, F= 1, F~ 1 | L03.31 L03.34 |
| t <- T90 | 2 | 0/0/2 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | A= 2, C= 2, L= 2, F= 2, B= 1, B~ 1 | L05.4 L22.24 |
| s <- T18 | 2 | 0/0/2 | 0/2/0 | 2/0/0 | 0/0 | 0/1/1 |  | L08.23 L10.12 |

**F** (73 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| m <- X_NEW | 8 | 1/0/7 | 0/2/6 | 0/2/6 | 0/0 | 4/3/1 |  | L11.22 L16.1 L16.14 L19.3 L20.24 L21.18 L21.3 L23.23 |
| r <- <deleted> | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | B~ 3 | L01.24 L01.29 L02.25 |
| a <- <deleted> | 3 | 0/0/3 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.25 L01.26 L02.24 |
| c <- <deleted> | 3 | 0/0/3 | 0/0/1 | 0/0/1 | 0/0 | 1/0/0 | C~ 3, L~ 3, A~ 2, B~ 2, pad~ 1, warp~ 1, A= 1, B= 1, E= 1, pad= 1, s125= 1, warp= 1, E~ 1 | L01.27 L03.31 L15.24 |
| d <- T36 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 1/1/0 | B~ 2, A~ 1, C~ 1, L~ 1 | L02.11 L06.18 L10.8 |
| t <- T90 | 3 | 0/0/3 | 0/0/2 | 1/0/1 | 0/0 | 0/1/1 | A= 3, C= 3, L= 3, B= 2, E= 2, E~ 1, pad= 1, s125~ 1, warp= 1, B~ 1 | L03.23 L05.4 L22.24 |
| s <- T18 | 3 | 0/0/3 | 0/2/1 | 1/1/1 | 0/0 | 3/0/0 |  | L02.11 L02.17 L03.11 |
| i <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L01.22 L02.22 |
| e <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | E~ 1, pad~ 1, warp~ 1, A= 1, B= 1, E= 1, pad= 1, s125= 1, warp= 1 | L01.23 L03.32 |
| l <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, E~ 1, pad= 1, s125~ 1, warp= 1 | L03.26 L03.29 |

**pad** (24 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T60 | 8 | 0/0/8 | 0/0/4 | 0/0/4 | 0/0 | 0/3/1 | warp= 7, E= 1, F~ 1, F= 1 | L01.11 L01.23 L01.28 L01.9 L02.16 L02.20 L02.9 L03.20 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, B= 2, C~ 2, L~ 2, E= 2, s125= 2, warp= 2, F= 1, F~ 1 | L03.31 L03.34 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, F~ 1, warp= 1 | L01.27 |
| a <- T95 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, C~ 1, L~ 1, E~ 1, s125~ 1, warp~ 1 | L01.28 |
| h <- T52 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | E= 1, s125= 1 | L02.15 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, E= 1, F= 1, s125= 1, warp= 1 | L02.19 |
| u <- X_NEW | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | F~ 1 | L02.23 |
| l <- T49 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, C~ 1, L~ 1, s125~ 1, warp~ 1 | L03.10 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, E~ 1, F= 1, s125~ 1, warp= 1 | L03.23 |
| t <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, E= 1, F= 1, s125= 1, warp= 1 | L03.24 |

**s125** (22 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| n <- T86 | 5 | 1/0/4 | 0/2/0 | 0/0/2 | 0/0 | 0/0/2 | F~ 1 | L01.21 L01.22 L02.1 L02.14 L02.30 |
| t <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | E= 2, A~ 1, B~ 1, C~ 1, L~ 1, F~ 1, pad~ 1, warp~ 1, A= 1, B= 1, F= 1, pad= 1, warp= 1 | L03.23 L03.24 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, B= 2, C~ 2, L~ 2, E= 2, pad= 2, warp= 2, F= 1, F~ 1 | L03.31 L03.34 |
| a <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, B~ 1, C~ 1, L~ 1, E~ 1, pad~ 1, warp~ 1 | L01.28 |
| s <- T18 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | warp= 1 | L02.3 |
| r <- T89 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L02.6 |
| h <- T52 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | E= 1, pad= 1 | L02.15 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, E= 1, F= 1, pad= 1, warp= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, pad~ 1, warp= 1 | L03.10 |
| o <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, E= 1, F= 1, pad= 1, warp= 1 | L03.25 |

**warp** (23 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T60 | 7 | 0/0/7 | 0/0/4 | 0/0/4 | 0/0 | 0/3/1 | pad= 7, E= 1, F~ 1, F= 1 | L01.23 L01.28 L01.9 L02.16 L02.20 L02.9 L03.20 |
| c <- <deleted> | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 2, B= 2, C~ 2, L~ 2, E= 2, pad= 2, s125= 2, F= 1, F~ 1 | L03.31 L03.34 |
| c <- T92 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, F~ 1, pad= 1 | L01.27 |
| a <- T66 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, E~ 1, pad~ 1, s125~ 1 | L01.28 |
| s <- T18 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | s125= 1 | L02.3 |
| s <- T70 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, E= 1, F= 1, pad= 1, s125= 1 | L02.19 |
| l <- T65 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, pad~ 1, s125= 1 | L03.10 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, C= 1, L= 1, E~ 1, F= 1, pad= 1, s125~ 1 | L03.23 |
| t <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, E= 1, F= 1, pad= 1, s125= 1 | L03.24 |
| o <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, B= 1, E= 1, F= 1, pad= 1, s125= 1 | L03.25 |

