# PREREG R10-SIENA7C (6 Oct 2026, written before the error figure is computed)

Question: is agent J's sign error on no. 7 (transcripts/no07.tok) under R9-SIENA7's control crossover (the anchored
homophonic control falls to its 0.60 gate at about 10% injected sign error), on all arbitrated tokens?

Instrument: every agent J / pass B split spot on L02, L04-L07, L09-L11 read by the worker on autocontrast 3-6x zooms of the
R4796 P1 image (sha1 2b12f15a...), J's labels in view (not blind), as R9-SIENA7B did for L03/L08. L12 (half-cut in pass B's
crops) is checked token by token against the image instead. Verdicts: J (image agrees with J), B (J wrong), amb (undecidable;
counted against J for the upper figure). One row = one J error event.

Statistic (computed by specs/cheap-tests/siena-concistoro-2308/arb_error_no07.py from the R10 TSV plus the R9 TSV):
low = B rows / J tokens; high = (B + amb rows) / J tokens; Clopper-Pearson 95% on each. Primary scope L02-L11 (327 tokens);
secondary L02-L12 (363).

Decision rule: the R9-SIENA7 negative stands as control-backed on the whole letter only if the HIGH point estimate is under
10% AND the CP 95% upper bound of the HIGH figure is under 10%. If the high estimate is under 10% but its upper bound is not,
the verdict is "control-backed at the point estimate, not at the 95% bound". If the high estimate is at or over 10%, the
negative is conditional (non-test at the upper end). Limits stated in advance: spots where both readers agree are not
arbitrated (shared errors are invisible); the arbitration is not blind.
