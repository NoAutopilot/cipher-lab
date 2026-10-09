# PREREG SUR-0745R (9 Oct 2026, 20:2x UTC by date -u; pushed in its own commit BEFORE either blind pass is run; score.py, mk.py, pool4.py pushed with it, unchanged after)
LANE FAMILY-A2l (account 2), job SUR-0745 (brief .claude/briefs/runs/2026-10-09-ytbiz-family-2009-jobs.md). SUR-KB's / SUR-PARTIAL's named
next: more glossed lines, not more draws. This file is also the **amendment of PREREG-SUR-POOLPC.md** that adds a fourth unit to the pool.

## Unit
NA 1.05.03 inv. 373 scan 0745 **RIGHT page**: 23 gloss+cipher pairs (crops_manifest.tsv; every written line of the page is in a pair,
counted on a 46-strip contact sheet before this file). Held out: not in T (0693+0702+0730), never transcribed (FAM-SUR373 look.tsv 600 px
description only; SUR-0745 read the LEFT page only). A key test on an interlinear-glossed page: N0 by construction, not a reading.

## Readers (as SUR-BLIND / SUR-0744R / SUR-0745, unchanged)
Two independent blind Sonnet calls (A forward crop order L01->L23, B reverse), crop paths only, the SUR-BLIND reader prompt and
vocabulary (`[ij]` dotted y/ij shape, `y` undotted; reader decides). No values, no key, not told what is tested. Each pass's gloss rows are
its own (the gloss is read blind twice and scored per pass; it is never settled before scoring). Cipher tokens never edited; mk.py is
notation only, plus one rule fixed here: a leading marginal "1o" on L15's cipher row is plain numbering and is dropped.
Reconciliation unit: per-crop y-family count comparison A vs B, descriptive; no pass edited.

## Step 1: per-unit control first (rule 3 per-unit merge paragraph), score.py (SUR-0745's, logic unchanged)
(0) scan A vs C1 (10,000 deranged-gloss draws, seed 7450); (a) CLASS gate exactly as SUR-0745 (pooled y-family -> m|n share; PASS iff
n_al >= 10, share >= 0.60, share >= C1 p99 + 2/n_al, SAME SYSTEM); (b) per-unit SPLIT and (c) descriptive, as SUR-0745.
Can the control differ on the statistic? Yes, measured on 0744R before SUR-0745 (calib_0744R.out: derangement moves the share and S, sd
about 0.05, 200+ distinct values); the same score.py is used here.
**Merge rule: 0745 R enters the pool only if its unit CLASS verdict is PASS (both passes).** A unit that ties or fails its own control is
held out; then no pooled re-score is run and the pooled result stays SUR-POOLPC's / SUR-KB's.

## Step 2 (only if step 1 PASS): pooled SPLIT, 4 units (pool4.py = poolpc.py source with UNITS + 'inv373_0745R_blind', nothing else)
2a. Power curve first (`pool4.py`): SUR-PARTIAL's planted partial split at the new pooled line count, f = 0 (H0), 0.50, 0.75, 1.00;
    60 synthetic units per level per pass scaffold (fewer than SUR-PARTIAL's 200 to fit the box; stated: SE about 0.05 on a rate),
    K = 300 deranged-gloss draws per unit, master seed 20261011.
    **Gate: f = 1.00 detection >= 0.80 on both scaffolds AND H0 false LEANS n <= 0.05 on both -> PASS**, else FAIL and no real pooled score.
    Reported, not gated: the smallest tested f with power >= 0.80 (what a NO SPLIT SHOWN would then exclude).
2b. Only on a 2a PASS: `pool4.py --real`, 10,000 draws, seed 20261010, poolpc's verdict rule (LEANS n iff S > p99.5, LEANS m iff S < p0.5,
    else NO SPLIT SHOWN); unit verdict needs both passes.
If the box runs short, 2a is cut to the f = 1.00 and H0 arms only (stated in the result), never skipped.

## Consequences
Whatever the result: no edit to key.tsv, key_period_*.tsv, conflicts.tsv, any transcription file or token grade (no key change above M).
CLASS PASS = a fourth held-out page for [y-fam] = {m,n}. Pooled LEANS n / LEANS m on both passes = a candidate split for a verifier.
NO SPLIT SHOWN = excludes a second m sign at the levels 2a shows power for, nothing below. Anything that moves goes to a verifier.
Rule 10: report only.
