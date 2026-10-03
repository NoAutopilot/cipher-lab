# GAPS22 pre-registration: rate-matched nl18 judge gate for 4.VEL 2077 (3 Oct 2026, account-4)

Written and pushed BEFORE the 2077 reading is scored by `judge_nl18_ratematch.py` (no score in this commit).

Target text: `judge/2077_legend_first.txt` (decoded cipher letters only, [g|l]/[k|i] -> first value; N=605 letters),
as written by `judge_nl18.py` from `reading_2077_legend_nieuw.txt` (H 500 M 106 U 52, M+U 0.240, GAPS21 0e8b2e63).

Corruption (the target's own measured pattern, not a uniform rate): the grade sequence of the 2077 tokens in text
order (`reading_2077_legend_nieuw_tokens.tsv`, 658 rows) is the mask. A held-out window of 658 letters is laid on the
mask position by position: a U position is DROPPED (the judge input drops unread signs), an M position is REPLACED by a
uniform random letter a-z (all M treated as wrong: the lenient end; M+U = 0.240 counted entirely as error, as the
brief states), an H position keeps its letter. Result: 606 letters, the target's own length within one.

Statistic: `NgramModel.score` (tools/judge_plaintext.py, mean log10 P(letter | 3 previous)), no word-cover term.

Folds: leave-one-file-out over the 7 files of `LANG_CORPORA["nl18"]`; model k trained on the other 6.
Per fold, 400 samples each, fixed seeds:
- corrupted-real: random held-out window, mask applied -> distribution R_k;
- corrupted-null: the same window letter-shuffled, then the same mask applied -> distribution Z_k;
- shuffled target: 400 letter shuffles of the 2077 target text -> distribution T_k.

Threshold per fold: thr_k = max(p05(R_k), p99(Z_k)).

Power criterion per fold (checked before the target is read): the fraction of R_k above p99(Z_k) >= 0.95.
Gate-level power: at least 5 of 7 folds powered; otherwise the gate is logged "non-test at this error" and the target
score is not reported as PASS/FAIL.

Shuffled-target check per powered fold: fraction of T_k above thr_k <= 0.05; if any powered fold exceeds it the gate is
void for this reading.

Verdict (powered folds only): PASS if the 2077 score > thr_k in every powered fold; FAIL if it is <= thr_k in a
majority of powered folds; otherwise MIXED (inconclusive, not a negative).
A PASS that also clears the shuffled-target check -> "reading ready" ROOM line for a separate verifier; no status
change, no novelty words (rule 10).

Reported beside the verdict (non-gating, sensitivity only): the same gate with M positions replaced at probability
0.5 (half the M signs right), and per-fold p05(R_k), p99(Z_k), target score, T_k max.
