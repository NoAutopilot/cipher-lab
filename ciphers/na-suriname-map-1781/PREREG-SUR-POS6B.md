# PREREG SUR-POS6B (13 Oct 2026, account 2, LANE DEFAULT-A2-2013) -- pushed before the call

Question: 4.VEL 2039 legend k pos 6 (`ciphertext_2039_legend.tsv`, held r M; SUR-LEGK shape passes 7, 7; SUR-POS6 sheet-tile call
a non-test). Instrument: one blind Sonnet vision call (`passes/signcmp_surpos6b/brief.md`) on `panel.jpg` (A-H: 4 settled r and
4 settled 7 tiles of the same legend, all conf H -- r: l3, n2, f16, p25; 7: m11, n6, e6, o2 -- unlabelled, shuffled, seed 20261013)
and `queries.jpg` (Q1-Q3 shuffled: the target and two known-answer H controls not in the panel, p30 = r, r9 = 7). Key in
`passes/signcmp_surpos6b/blind_key.json`, not shown to the reader. The reader is told only that the panel holds two different
characters of one hand, four of each; no value, reading or code is shown.
Scoring: the reader sorts A-H into two groups and assigns each Q to a group with conf H/M/L or unsure. A group's class = the
majority true class of its panel tiles (a 2-2 group has no class).
Gate (all three): (1) panel separation >= 7/8 tiles in the right group under the best mapping; (2) control p30 assigned to the r
group and r9 to the 7 group, each at conf H or M; (3) nothing else. Fail any -> NON-TEST, pos 6 stays r M with the split recorded.
Apply rule: only if the gate passes AND the target is assigned to one group at conf H. 7 group -> pos 6 becomes 7, conf H (two blind
shape passes + this same-hand call agree); r group -> r stays, conf back to H. Anything else (M/L, unsure, both) -> stays r M.
Nothing enters a key file either way. Note written before the call: the worker saw the built panel; tile A (l3, r H) has a 7-like
flat-bar outline (as SUR-POS6 described), so gate (1) may fail on it -- that is a finding about the panel, not grounds to rebuild it.
