## birago1572-no87: 115 scored positions, passes A, L, Tord, Tshuf
- A: 8 wrong-or-deleted of 115 covered positions (insertions not counted here; tx_bench adds them)
- L: 5 wrong-or-deleted of 115 covered positions (insertions not counted here; tx_bench adds them)
- Tord: 13 wrong-or-deleted of 115 covered positions (insertions not counted here; tx_bench adds them)
- Tshuf: 10 wrong-or-deleted of 115 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| A | 8/115 | 0 (0% of errs; rate 0.0%; base 3%) | 7 (88% of errs; rate 6.5%; base 94%) | 1 (12% of errs; rate 25.0%; base 3%) |
| L | 5/115 | 0 (0% of errs; rate 0.0%; base 3%) | 5 (100% of errs; rate 4.6%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| Tord | 13/115 | 0 (0% of errs; rate 0.0%; base 3%) | 13 (100% of errs; rate 12.0%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| Tshuf | 10/115 | 0 (0% of errs; rate 0.0%; base 3%) | 10 (100% of errs; rate 9.3%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+6 | L+8 | L+11 |
|---|---|---|---|---|
| A | 1/27 | 2/28 | 1/30 | 4/30 |
| L | 0/27 | 2/28 | 0/30 | 3/30 |
| Tord | 4/27 | 2/28 | 2/30 | 5/30 |
| Tshuf | 2/27 | 2/28 | 2/30 | 4/30 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | A | L | Tord | Tshuf |
|---|---|---|---|---|---|
| A | 8 | - | 5/8 (5) | 5/8 (3) | 3/8 (2) |
| L | 5 | 5/5 (5) | - | 3/5 (2) | 3/5 (2) |
| Tord | 13 | 5/13 (3) | 3/13 (2) | - | 8/13 (8) |
| Tshuf | 10 | 3/10 (2) | 3/10 (2) | 8/10 (8) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 3; wrong in exactly one: 6

### Top (truth value <- read) pairs per pass, with feature profile

**A** (8 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| s <- T50 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tord= 1, Tord~ 1 | L01.23 L08.10 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Tord~ 1, Tshuf~ 1 | L06.27 |
| e <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Tord= 1, Tshuf= 1 | L11.5 |
| r <- T80 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, Tord= 1, Tshuf= 1 | L11.17 |
| e <- T60 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1 | L11.29 |
| i <- <deleted> | 1 | 0/1/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L11.32 |

**L** (5 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, Tord~ 1, Tshuf~ 1 | L06.27 |
| e <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, Tord= 1, Tshuf= 1 | L11.5 |
| r <- T80 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, Tord= 1, Tshuf= 1 | L11.17 |
| e <- T60 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L11.29 |

**Tord** (13 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| l <- T65 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tshuf= 1 | L01.3 L01.8 |
| l <- T64 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tshuf= 2 | L01.26 L08.26 |
| s <- T50 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1 | L01.23 |
| a <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tshuf= 1 | L06.16 |
| u <- T15 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, L~ 1, Tshuf= 1 | L06.27 |
| s <- T29 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1 | L08.10 |
| e <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1, Tshuf= 1 | L11.5 |
| s <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L11.6 |
| e <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tshuf= 1 | L11.16 |
| r <- T80 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1, Tshuf= 1 | L11.17 |

**Tshuf** (10 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| l <- T65 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tord= 1 | L01.8 L08.20 |
| l <- T64 | 2 | 0/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tord= 2 | L01.26 L08.26 |
| a <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tord= 1 | L06.16 |
| u <- T15 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A~ 1, L~ 1, Tord= 1 | L06.27 |
| e <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1, Tord= 1 | L11.5 |
| e <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | Tord= 1 | L11.16 |
| r <- T80 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | A= 1, L= 1, Tord= 1 | L11.17 |
| l <- <deleted> | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 |  | L11.31 |

