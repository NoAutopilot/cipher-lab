# R15-LAGMI pre-registration: adjacent mutual information (Z_MI), homophonic vs running key (6 Oct 2026, account 2, LANE-RUN15-account-2)

Committed and pushed before any scored run. Target: `basecode_cipher.txt` (N=229, K=26, marks stripped), as GAPS145/149 and R15-LAGDIG.
This is a second statistic, not a re-tune of R15-LAGDIG's Z_R. R15-LAGDIG reported Z_MI only descriptively (AUC 0.885 / 0.843
at e=0.23 on its seeds); that was seen after its run, so here it is tested afresh on control seeds R15-LAGDIG never used.

## Statistic
- **Primary: Z_MI.** Plug-in mutual information of adjacent pairs (c_i, c_i+1), z-scored against 200 within-sequence shuffles
  (shuffles keep the unigram profile, so Z_MI measures order only). Same `mi()` function as `digram_check.py`.
- Z_R (repeated-bigram count) is reported descriptively and decides nothing.
- Rule 3 orthogonality: Z_MI depends on token order; homophonic keeps plaintext contact, running key flattens it, so the
  designs can differ on it by construction.

## Controls (same designs and error bracket as R15-LAGDIG; new seeds)
- Homophonic: `tools/families/homophonic.py make_control`, K=26, N=229, fr16, `profile=target`, seeds **1001-1040**
  (R15-LAGDIG used 1-40).
- Running key: Vigenere tabula, plain fr16 window, key a window of a different fr16 book (RK-fr); and key from
  `tools/data/nl_repo` (RK-nl). Window/book choices and noise and shuffles from `random.Random(20261006)` (R15-LAGDIG: 1577).
- Noise: substitution redrawn from the sequence's own unigram profile at e = 0, 0.10, 0.23, 0.30. Indels not modelled (caveat).
- 40 seeds per design per error level.

## Decision rule (fixed now)
- **Power**, at e = 0.23 only: AUC of Z_MI(homophonic) vs Z_MI(RK-fr) and vs Z_MI(RK-nl). Passes only if **both >= 0.80**.
  If either < 0.80: stop; log "untestable by this statistic (Z_MI) at this N/error" in HYPOTHESES.md and NOTES.md; the
  target's Z_MI is not computed or reported. Other error levels are reported as the bracket only.
- **Scoring (only if power passes):** target Z_MI and its percentile in each design at e = 0.23. "Favours homophonic" if
  target Z_MI > the RK p95 (both variants) and >= homophonic p05; "favours running key" if target Z_MI < homophonic p05 and
  <= RK p95 (both); anything else "undecided". A favour is a design preference, not a reading.
- No third statistic on this question will be pre-registered from this run's results (rule 3 third-attempt clause).
Script: `families/mi_check.py` (seeded, `--check`), output `families/mi_check.tsv`.
