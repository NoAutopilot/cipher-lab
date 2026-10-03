# Pre-registration 5: fixed-key scoring of the 22 fr.4712 f.7r glossed runs (GAPS88-fr4715-vieuville-pool, account-4)
Written 3 Oct 2026 (clock read 11:1x UTC), committed and pushed BEFORE scripts/f7r_fixedkey.py is run on the target.
Question: under Tomokiyo's letter table (key_vieuville_nevers.tsv, 33 numeric codes, nothing learned), do the cipher
runs of witness/f4712_7r_pairs_img.tsv (GAPS82, unchanged) decode closer to their own glosses than the same runs under
a permuted key? A different instrument from G1 (no alignment search, no learned key), so not a third G1 attempt.

## Material and normalization (fixed)
- Cipher run: unmarked tokens only (bare 1-2 digit N). N in the table -> its letter; N not in the table -> '?' (never
  matches). Marked tokens (dN, tN, bN) dropped. Gloss: NFKD to ASCII, lowercase, j->i, v->u, letters only.
- Per run: L = longest common subsequence of decoded string and gloss string; M = min(len decoded, len gloss).
  A run is scorable if M >= 4.

## Statistics
- Pooled T = sum of L over scorable runs; R = T / sum of M.
- Control (can differ: permuting values changes every decoded letter, hence L): the table's 33 values permuted over its
  33 codes, 10,000 draws, seed 7715, one permutation applied to all runs per draw. p99_T = 99th percentile of control T;
  meanR_ctl = mean control R. Per-run p = (1 + #draws with L_ctl >= L) / 10,001.
- Positive control (known answer, same code path): the 22 gloss texts enciphered with Tomokiyo homophones as
  scripts/g1_power_check.py's K2 (word-codes p 0.15, 10 pct substitution), seeds 1-20, each scored exactly as the
  target with its own 10,000-draw control (seed 7715). D_K2 = median over seeds of (R - meanR_ctl).

## Gate (fixed now)
- FK0 (instrument power): positive control PASSes FK1 and FK2 in >= 10/20 seeds. If not: non-test; the instrument is
  [retired] for this leaf and nothing below is read as a result.
- FK1: T > p99_T.   FK2: D = R - meanR_ctl >= 0.5 * D_K2.
- PASS = FK0 and FK1 and FK2.

## What each outcome means (fixed now)
- PASS: the f.7r runs as transcribed follow Tomokiyo's letter table against their glosses; the G1 FAILs are the
  aligner's misfit on this material (glosses longer than runs, 502 vs 374), not a different key. The leaf qualifies as a
  Vieuville-key witness for letters only; no word-code slot is read from this; next step: a separately pre-registered
  G2 (marked codes vs key no.71) with run boundaries anchored by the fixed-key LCS, not by the flat-start aligner.
- FK1 PASS, FK2 FAIL: a weak above-chance signal, partial agreement only; the leaf is held; per-run p names which runs
  carry it; next step named from the per-run list.
- FK1 FAIL (FK0 passing): the runs as transcribed do not decode to their glosses under Tomokiyo beyond a permuted key.
  Either f.7r (a different volume, fr.4712) uses a different letter key, or transcription/pairing is wrong; with G1 this
  is the third FAIL of the f.7r pairing against Tomokiyo, so f.7r is held as untestable-for-key-71-by-these-instruments
  (not a negative on key no.71 or on no.44's slots). Next step: a self-consistency test of G1's learned key (split-half
  agreement of the aligned codes) to tell "different key" from "noise", offline.
- Secondary, descriptive, does not change the verdict: count of scorable runs with per-run p < 0.01 (chance expectation
  about 0.2 of 22); 3 or more is reported as a localized signal with the run ids.
