# R10-HUNT2 context-fill pre-registration, attempt 2 of at most 3 (written 6 Oct 2026 09:5x UTC by date -u, before any R10 run)

Worker R10-HUNT2 (LANE LANE-RUN10-account-1). Nothing below has been computed; fill/context_fill_r10.py does not exist at push time.
Attempt 1 (R9-HUNT, PREREG-R9.md) FAILed its gate (control 0.346 < 0.40). This attempt changes the gate (precision above a margin
threshold, against the shuffled-context control at the same threshold) and fixes one defect; the LM, corpus (fr18), candidate rule,
context rule, control columns and 11% blanking are R9's, unchanged.

## Change 1: inverted-bracket fix (the R9 defect)
If the median of the lower three key values sorts above the median of the upper three (e.g. 470: 468 fort > 473 faire), the bracket is
[min, max] of all six values instead of the empty [lower median, upper median]. The widening rule (< 5 candidates) is unchanged.

## Change 2: margin threshold, fixed now as a number
t = 2.786 (the R9 t*, computed on seeds 1-3 with the old bracket; seen before this file, so seeds 1-3 are NOT used for the gate).

## Gate (fresh seeds 4, 5, 6 only; pooled over the three seeds; both must hold)
Control = R9's BLA185 leave-one-code-out columns (own context); shuffled = the same columns with context from another BLA185 position.
1. Control precision among columns with margin >= 2.786 is >= 0.60, on >= 30 pooled columns.
2. That precision exceeds the shuffled-context control's precision among ITS columns with margin >= 2.786 (matched margin), one-sided
   Fisher exact p < 0.05 on the 2x2 (hits/misses, control vs shuffled). If the shuffled control has fewer than 5 columns at that
   margin, condition 2 is evaluated with those columns anyway (Fisher handles small n) and the count is reported.
Can the control differ from the shuffled control? Yes: the score and margin depend on the context, which is what the shuffle changes.

## Grading
- PASS: target groups (the 18 unkeyed BLA186/191(a) groups, R9 rule, group 585 excluded) with margin >= 2.786 are graded S
  ("cryptanalytic with a control"); every other target fill stays U (not M). reading_tokens.tsv updated only for the S rows.
- FAIL: log "attempt 2 FAIL" in NOTES.md; no fill enters reading_tokens.tsv; the step is not re-tuned. Next is a different
  instrument (rule 3 third-attempt clause), named in NOTES.md, not a third pass of this context-fill.
Seeds 1-3 under the fixed bracket are also run and reported for comparison only; they do not enter the gate.
