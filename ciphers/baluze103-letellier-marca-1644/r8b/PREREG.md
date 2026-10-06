# PREREG -- R8-BAL103B: look-alike pass on the f.50 confusable pairs (written and pushed before the re-read runs)

Worker R8-BAL103B (account 1, LANE LANE-RUN8-account-1), 6 Oct 2026, about 04:1x UTC by `date -u`.

- Input: passC = ciphertext.tsv with R8-BAL103's 10 `r8-2of3` corrections undone (old sign from `alt`) -> `r8b/passC.tsv`, so the
  pass re-decides those columns. Tiles (`r8b/build_tiles.py` -> `r8b/tiles.tsv`): the 51 R7B A/B split columns (gap columns excluded)
  whose pair lies in a named family: m/mm/mt, venus/P/q2/q, x/xc/xs/xbar, 6/sigma, hz/hbar, tt/venus, mm/tt, 9/venus.
- Instrument: `tools/lookalike_pass.py windows` (label hidden, alphabetical candidates, shape descriptions `r8b/sign_desc.tsv`, no
  values), one blind Sonnet re-read of the 9 montages -> `r8b/reread.tsv`.
- Rule (the tool's, fixed): `tools/lookalike_pass.py reconcile`: a firm (H/M, not SPLIT) re-read matching reader A or B settles the
  tile 2-of-3; otherwise passC stands and the tile goes to `r8b/focus.tsv`.
- Echo/bias check (R8-BAL103 lesson, m -> mm every time): report the share of settled tiles that moved in each direction per family;
  if >= 80% of m/mm settlements go the same way (>= 5 tiles), the family is flagged as a probable reader bias and its settlements are
  NOT applied (held for the owner's sign sorter via focus.tsv).
- Measured: fr17 judge (`tools/judge_plaintext.py` via `tx/r7b/judge_input.py`) on three ciphertexts: pre-R8 (passC), R8 (committed),
  look-alike (passD). The look-alike result is applied to ciphertext.tsv only if its judge score is not below pre-R8's; otherwise
  ciphertext.tsv is set back to pre-R8 for the R8 columns only if pre-R8 beats R8, and passD is kept as a file. Either way no
  outcome is called a reading; the 2-of-3 residual is agreement, not accuracy (LESSONS.md "Look-alike pass").
