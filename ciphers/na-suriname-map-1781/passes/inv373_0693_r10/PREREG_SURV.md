# PREREG R10-SURV (verifier, 6 Oct 2026, ~08:1x UTC by date -u; committed and pushed before verify_blind.py is run)
Why: R10-SUR693's PREREG.md was first committed in 83538f780 (07:51:48 UTC) together with compare.out; the commit its NOTES
section names (ab4b9c64e) touches only ROOM.md. So the solver's gate cannot be shown to predate its scored run.
Re-test on the Sonnet BLIND pass (passA_sonnet_blind.tsv, read with no values and no gloss), not the reconciler's sign reads.
Positions: for each 'aligned' row of align_words.tsv, the same-length window of that line's blind tokens that best matches the
reconciler's sign sequence (blindcheck.py's rule; caveat: window choice uses the reconciler reads, token identities do not);
blind tokens normalised only by blindcheck.py's map ([ij]/y -> [y-fam], [lambda] -> λ, [d-loop] -> [ezh-dot]); '?' tokens dropped.
Statistic: share of blind tokens keyed in key_period_codes_nieuw.tsv whose key value equals the gloss letter (i=j=y=ij, u=v;
'a|b' agrees if either). Blind 'x' is scored as key x=q (no credit for a missed dot: conservative).
Control: gloss letters permuted across all such positions, 1,000 permutations, seed 6930.
Gate: SAME SYSTEM (blind) if real >= 0.60 AND real > control p99. Otherwise 'not shown'. Per-code agree/conflict is descriptive.
