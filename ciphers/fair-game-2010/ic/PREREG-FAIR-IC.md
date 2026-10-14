# PREREG-FAIR-IC (account 4, LANE DEFAULT-A4-2135-14, 14 Oct 2026, written 22:3x UTC before any score)

Question: FAIR-LANG's L0 (unigram letter counts) is blind to a substitution step. Is there a language with a corpus in
tools/data (every `LANG_CORPORA` key in tools/judge_plaintext.py, 34 keys) whose *substitution-invariant* letter
statistics the 67 marks fit, and does a simple substitution of that language read?

P0 (profile rank, `ic/ic_rank.py`, `--check`): target = test2/order_scroll.txt (67 letters; order is irrelevant to
both statistics). Folding as FAIR-LANG (NFKD, a-z). Per key, the same 2000 word-start N=67 windows of that corpus
(tools/families/transposition.word_window, seeds 1-2000, margin 0), and 200 uniform-random 26-letter strings of
length 67 (seed 20261014; the homophone-free random floor).
  - S1 IC = sum n_i(n_i-1) / (N(N-1)). Survival: target IC pct_rank (share of windows with IC < target) >= 0.01.
  - S2 sorted-frequency profile: the 26 counts sorted descending; reference = mean sorted profile of the 2000
    windows; statistic = L1 distance of a string's sorted profile to the reference. Survival: share of windows with
    distance > target's >= 0.01 (target not in the windows' worst 1%).
  A language survives P0 only if it survives both S1 and S2. Recorded per key: target value, pct_rank, p01 (p99 for
  S2), median, random-floor median and the random strings' share failing the same cut (power of the cut).
P1 (masc --langs): `tools/family_run.py specs/fair-game-2010.json --family masc --cipher test2/order_scroll.txt
--langs <survivors> --seeds 3 --restarts 8 --gate 0.6` (gate 0.6 = the masc rows already in HYPOTHESES.md; one matched
control per language first, that language's corpus). A language whose control misses 0.6 is CONTROL BELOW GATE, not a
negative. A target decode counts only if the judge in its own language PASSes; otherwise negative for that language.
Column order (test2/order_column.txt) is run for any language whose scroll decode PASSes. If more than 8 languages
survive P0, run the 8 with the highest min(S1, S2) pct_rank first and log the rest as next step (box 45 min, cap 2.5).
Prior on file: masc on English at N=67 K=21 reads 0.537-0.591 (GAPS71), below 0.6, so CONTROL BELOW GATE is the
expected P1 outcome in most languages; that is a non-test, not a negative.
