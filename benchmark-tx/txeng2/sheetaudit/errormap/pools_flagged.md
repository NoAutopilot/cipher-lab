| unit | baseline errors (flagged excluded) | scored | flagged baseline errors dropped |
|---|---|---|---|
| eval_heldout | 10 | 371 | 5 |
| spinelli | 12 | 191 | 2 |
| f178r | 6 | 83 | 1 |
| f152r | 1 | 70 | 3 |
| dev_tune | 7 | 338 | 5 |

### old ERRORMAP eval pool (eval_heldout + Spinelli): 22 errors

| agree_class | errors | share |
|---|---|---|
| all-wrong-split | 8 | 36.4% |
| majority-wrong | 7 | 31.8% |
| all-same-wrong | 4 | 18.2% |
| minority-wrong | 3 | 13.6% |

| err_class | errors | of which all-same-wrong |
|---|---|---|
| look-alike | 11 | 0 |
| other | 5 | 2 |
| crop | 5 | 2 |
| thin | 1 | 0 |

| unit | truth <- read | n | agree_class |
|---|---|---|---|
| eval_heldout | d <- T98 | 6 | minority-wrong 3, majority-wrong 3 |
| spinelli | r <- SIX | 4 | all-wrong-split 4 |
| eval_heldout | l <- T64 | 2 | majority-wrong 2 |
| spinelli | h <- <deleted> | 2 | all-same-wrong 2 |
| spinelli | u <- JHOOK | 2 | all-wrong-split 2 |
| eval_heldout | c <- T27 | 1 | majority-wrong 1 |
| eval_heldout | e <- T24 | 1 | all-wrong-split 1 |
| spinelli | t <- TEE | 1 | majority-wrong 1 |
| spinelli | e <- SIX | 1 | all-same-wrong 1 |
| spinelli | s <- JHOOK | 1 | all-wrong-split 1 |
| spinelli | n <- PHI | 1 | all-same-wrong 1 |

### Amendment 4 eval pool (+ f178r + f152r): 29 errors

| agree_class | errors | share |
|---|---|---|
| majority-wrong | 10 | 34.5% |
| all-wrong-split | 10 | 34.5% |
| all-same-wrong | 6 | 20.7% |
| minority-wrong | 3 | 10.3% |

| err_class | errors | of which all-same-wrong |
|---|---|---|
| other | 12 | 4 |
| look-alike | 11 | 0 |
| crop | 5 | 2 |
| thin | 1 | 0 |

| unit | truth <- read | n | agree_class |
|---|---|---|---|
| eval_heldout | d <- T98 | 6 | minority-wrong 3, majority-wrong 3 |
| spinelli | r <- SIX | 4 | all-wrong-split 4 |
| eval_heldout | l <- T64 | 2 | majority-wrong 2 |
| spinelli | h <- <deleted> | 2 | all-same-wrong 2 |
| spinelli | u <- JHOOK | 2 | all-wrong-split 2 |
| f178r | c <- T92 | 1 | majority-wrong 1 |
| f178r | a <- T66 | 1 | majority-wrong 1 |
| f178r | s <- T70 | 1 | all-same-wrong 1 |
| f178r | l <- T65 | 1 | majority-wrong 1 |
| f178r | c <- T96 | 1 | all-wrong-split 1 |
| f178r | c <- T90 | 1 | all-wrong-split 1 |
| eval_heldout | c <- T27 | 1 | majority-wrong 1 |
| eval_heldout | e <- T24 | 1 | all-wrong-split 1 |
| spinelli | t <- TEE | 1 | majority-wrong 1 |
| spinelli | e <- SIX | 1 | all-same-wrong 1 |
| spinelli | s <- JHOOK | 1 | all-wrong-split 1 |
| spinelli | n <- PHI | 1 | all-same-wrong 1 |
| f152r | e <- T36 | 1 | all-same-wrong 1 |
