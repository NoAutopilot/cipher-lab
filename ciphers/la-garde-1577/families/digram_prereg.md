# R15-LAGDIG pre-registration: contact/digram test, homophonic vs running key (6 Oct 2026, account 2, LANE-RUN15-account-2)

Committed and pushed before any scored run. Target: `basecode_cipher.txt` (N=229, K=26, marks stripped), as GAPS145/149.

## Statistics (both computed on the token sequence; null = 200 within-sequence shuffles, which keep the unigram profile)
- **S1 (primary): repeated-bigram excess.** R = sum over distinct adjacent bigrams of C(n_b, 2). Z_R = (R - mean_shuf) / sd_shuf.
- **S2 (secondary, descriptive only): adjacent mutual information.** Plug-in MI of (c_i, c_i+1); Z_MI against the same shuffles.
Rationale: homophonic substitution keeps the plaintext's bigram dependence (spread over a few signs per letter; at K=26 almost
one sign per letter), so Z_R > 0; a running key's ciphertext bigrams are close to independent, so Z_R ~ 0. Both statistics
depend on token order, and the designs can differ on them by construction (rule 3 orthogonality check passed).

## Controls (matched to the target)
- **Homophonic:** `tools/families/homophonic.py make_control`, K=26, N=229, fr16, `profile=target` (the target's own sign
  frequency profile), noise 0 at generation; noise added afterwards by the common recipe below.
- **Running key (two variants):** Vigenere tabula, plain = fr16 window, key = a window of a different fr16 book (RK-fr);
  and plain fr16 with key from `tools/data/nl_repo` (17th-c. Dutch print; RK-nl).
- **Noise:** substitution at rates 0, 0.10, 0.23 (the target's measured band), 0.30; each token with probability e is
  redrawn from the sequence's own unigram profile (the `homophonic.py` / GAPS149 profile recipe). Insertions/deletions are
  not modelled (caveat, as GAPS149).
- **Seeds:** 40 per design per error level (>= 20 required).

## Decision rule
- **Power (step 1)**, at e = 0.23 only: AUC of Z_R(homophonic) vs Z_R(RK-fr) and vs Z_R(RK-nl). Power **passes** only if
  both AUCs >= 0.80. If either is < 0.80: stop, log "untestable by this statistic at this N/error" in HYPOTHESES.md and
  NOTES.md; the target is not scored (its Z_R is not computed or reported). e = 0, 0.10, 0.30 are reported as the bracket.
- **Scoring (step 2, only if power passes):** target's Z_R and its percentile in each design at e = 0.23. "Favours
  homophonic" if target Z_R > the RK p95 (both variants) and >= homophonic p05; "favours running key" if target Z_R <
  homophonic p05 and <= RK p95 (both); anything else "undecided". A favour is a design preference, not a reading.
- S2 is reported descriptively and decides nothing.
Script: `families/digram_check.py` (seeded, `--check`), output `families/digram_check.tsv`.
