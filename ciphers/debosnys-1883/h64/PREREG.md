# H64 pre-registration (29 Sept 2026, DEBOSNYS-RUNNER-3b; pushed before the rerun)

Same as H62 (scripts/h62_r34_rule.py: RULE.md box set on settled c2, clear spans dropped, N 637; variants rule+folds
[primary] and rule; G-D/r34_replicate.py scan unchanged; seeds unchanged), with ONE change decided after H62's control
failed and before any real score exists: a planted height-R transposition counts as found when the scan's best
reading is any height R' with ceil(N/R') == ceil(N/R) (the same number of columns; at N 637 R32 and R33 both give 20),
or the exact height. Bar unchanged: each of TRANS-7/19/33 found in >= 10 of 12. The real scan's own best reading is
reported with its column count; the R34 lead is "R34 or a height with 19 columns" (R34, R35 at N 637: ceil(637/34) = 19,
ceil(637/35) = 19). Then the 200-scan own-shuffle null (scan max, so the multiple heights are paid for) and the halves
check at R34. Kill: p > 0.05 or either half <= 0.
