# PREREG SUR-MRICH (10 Oct 2026, 11:4x UTC by date -u; LANE FAMILY-A2q, account 2)

Pushed in its own commit BEFORE any power draw is scored and before any new transcription. Step 1 (count_m.py -> counts.tsv,
counts.out) is a gloss-letter count from committed files, no cipher statistic; it ran before this file and fixes the candidate lines.

**Question.** SUR-0745R's pooled SPLIT (88 lines, 4 units) has power 0.20/0.15 at f = 0.50 (a second m sign on half the m positions).
Would adding the m-richest glossed lines already on disk lift that power to >= 0.80?

**Step 1 result (fixed, before any draw).** Gloss m per 100 letters is 1.2-3.1 on every glossed page on disk (pool 2.5-3.1 except 0745 R
1.2-1.35; out of pool 0702 2.10, 0730 2.69, 0746 1.90, 0758 R 2.58, 0692R/0693L 2.82, 372 0189 R 2.74): no page is m-rich. Out-of-pool
lines with gloss on disk: 117 (gloss m 98). By line: 7 lines carry m >= 3, 17 carry m = 2, 42 m = 1, 51 m = 0. These lines' cipher
has only one blind pass (R13/R14/R10) or the SUR-372 two-pass page, so none is pool-ready under the PREREG merge rule (two blind passes,
unit CLASS control) without new passes.

**Power method (SUR-0745R's, unchanged).** mrich_power.py execs ../inv373_0745R_blind/pool4.py up to `if __name__` unchanged: per-pass
scaffolds (facing, deletion, insertion from the real 4-unit pool, aligner steer as before), ctrl() = score.py (b) with K = 300
deranged-gloss C1 draws per synthetic unit and the same verdict rule; planted arm = SUR-PARTIAL's (each gloss m drawn as [y-fam] written
'Mx' with probability f). Only change: a synthetic unit is 88 lines bootstrapped from the pool gloss PLUS nx lines bootstrapped from an
extra gloss set (gloss text of out-of-pool lines, counts.tsv). f = 0.50 only. Master seed 20261012.
Levels: **L1** = the 23 m-richest out-of-pool lines (rank: gloss m desc, m per letter desc, file order; 54 gloss m; this is about one
page-equivalent, the most the cap can transcribe as 2 passes x 2 halves + 1 reconciliation), nx 23, 30 units per pass;
**L2** = all 117 out-of-pool lines, nx 117, 30 units per pass (upper bound of what is on disk);
**L3** (run only if L2 < 0.80 on either pass) = nx 234 drawn from all 117, 20 units per pass (to bracket the count still needed).

**Gate.** L1 detection (LEANS n) >= 0.80 on BOTH pass scaffolds -> step 2 (blind two-pass transcription of the L1 lines, unit control,
then the existing SPLIT unchanged on the enlarged pool). Otherwise stop after step 1; the result is the number of m-glossed lines still
needed, read from L1/L2/L3 (the smallest level >= 0.80 on both passes, with its added gloss m; if none, "more than L3's").
NA requests: none planned for the power step (all inputs on disk).

**Stated limits (before the run).** H0 (f = 0) is not re-run at these sizes (0/120 false LEANS n at 88 lines in SUR-0745R); the extra
lines are enciphered with the pool's facing (not their own pages' readers); 30/20 units per level gives SE about 0.07-0.09; bootstrap
from 23 lines at L1 repeats lines; only a second m sign is planted; the statistic and scaffold keep the aligner's [y-fam]={m,n} steer.
