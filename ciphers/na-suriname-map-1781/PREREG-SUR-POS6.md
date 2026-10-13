# PREREG SUR-POS6 (13 Oct 2026, account 1, LANE DEFAULT-A1-1840) -- pushed before the call

Question: 4.VEL 2039 legend k pos 6 (`ciphertext_2039_legend.tsv`, held r M; both SUR-LEGK blind shape passes read digit 7).
Instrument: one blind Sonnet vision call (`passes/signcmp_surpos6/brief.md`), images `refs.jpg` (Nieuw sheet E-row 7 and T-row r,
labels X/Y shuffled) and `queries.jpg` (Q1-Q3 shuffled: the target and two known-answer H controls from the same legend line,
l pos 3 = r, m pos 11 = 7). Key in `blind_key.json` (seed 20261013), not shown to the reader.
Gate: both controls must be matched to the right reference at conf H or M. If either control is wrong or "neither/unsure",
the call is a non-test and pos 6 stays r M with the split recorded.
Apply rule: only if the gate passes AND the target is matched to one reference at conf H. Match to the 7 tile -> pos 6 becomes
7 (H for the shape, since two blind shape passes + this call agree); match to the r tile -> r stays, conf back to H only if the
call says H. Anything else (M/L conf, neither, unsure) -> stays r M, split recorded. Nothing enters a key file either way.
