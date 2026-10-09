## birago1572-no87: 343 scored positions, passes L, fable, opus
- L: 14 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- fable: 15 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)
- opus: 15 wrong-or-deleted of 343 covered positions (insertions not counted here; tx_bench adds them)

### Error mass by position in line

| pass | errors | first (base %) | inner (base %) | last (base %) |
|---|---|---|---|---|
| L | 14/343 | 2 (14% of errs; rate 20.0%; base 3%) | 12 (86% of errs; rate 3.7%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| fable | 15/343 | 2 (13% of errs; rate 20.0%; base 3%) | 13 (87% of errs; rate 4.0%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |
| opus | 15/343 | 2 (13% of errs; rate 20.0%; base 3%) | 13 (87% of errs; rate 4.0%; base 94%) | 0 (0% of errs; rate 0.0%; base 3%) |

### Error rate by line index within the reader call (fatigue axis)

| pass | L+1 | L+2 | L+3 | L+4 | L+5 | L+6 | L+7 | L+8 | L+9 | L+10 | L+11 | L+12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L | 0/27 | 2/27 | 0/25 | 0/28 | 3/30 | 2/28 | 0/30 | 0/30 | 1/28 | 3/31 | 3/30 | 0/29 |
| fable | 0/27 | 2/27 | 0/25 | 0/28 | 3/30 | 2/28 | 1/30 | 0/30 | 1/28 | 3/31 | 3/30 | 0/29 |
| opus | 0/27 | 2/27 | 0/25 | 0/28 | 3/30 | 2/28 | 1/30 | 0/30 | 1/28 | 3/31 | 3/30 | 0/29 |

### Error correlation: share of the row pass's errors repeated by the column pass (same wrong sign in brackets)

| pass | errors | L | fable | opus |
|---|---|---|---|---|
| L | 14 | - | 14/14 (12) | 14/14 (13) |
| fable | 15 | 14/15 (12) | - | 15/15 (13) |
| opus | 15 | 14/15 (13) | 15/15 (13) | - |

Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): 14; wrong in exactly one: 0

### Top (truth value <- read) pairs per pass, with feature profile

**L** (14 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 3, opus= 3 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1, opus= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1, opus= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1, opus= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable~ 1, opus= 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1, opus= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1, opus= 1 | L06.27 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1, opus= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1, opus= 1 | L10.1 |
| c <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1, opus= 1 | L10.31 |

**fable** (15 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 3, opus= 3 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, opus= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, opus= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, opus= 1 | L05.4 |
| s <- T13 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L~ 1, opus~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, opus= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, opus= 1 | L06.27 |
| s <- T85 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | opus= 1 | L07.29 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, opus= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, opus= 1 | L10.1 |

**opus** (15 errors):

| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |
|---|---|---|---|---|---|---|---|---|
| e <- T76 | 3 | 1/0/2 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 3, fable= 3 | L05.1 L10.4 L11.5 |
| g <- T42 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, fable= 1 | L02.8 |
| e <- T36 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, fable= 1 | L02.12 |
| t <- T90 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, fable= 1 | L05.4 |
| s <- T64 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, fable~ 1 | L05.9 |
| d <- T98 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, fable= 1 | L06.18 |
| u <- T76 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, fable= 1 | L06.27 |
| s <- T85 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | fable= 1 | L07.29 |
| e <- T96 | 1 | 0/0/1 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, fable= 1 | L09.4 |
| t <- T92 | 1 | 1/0/0 | 0/0/0 | 0/0/0 | 0/0 | 0/0/0 | L= 1, fable= 1 | L10.1 |

