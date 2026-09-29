# DEB-SWARM-B log (English plaintext, homophonic letter substitution)

Group B's working log, 29 Sept 2026. One row per attempt. Times are UTC from `date -u`. Nothing here is a reading.

Tooling (all in this folder): `hsolve.c` (annealer: one letter a-z per sign, score = sum of n-gram log10 over every
window of consecutive non-gap signs minus BETA x N x KL(plain unigrams || English unigrams), optional bounded-loss
table `HS_ROBUST=q`), `build5.c` (Witten-Bell interpolated 5-gram conditional model), `gb.py` (driver: model build,
hand-planted controls, target fit). LM corpus: Moby-Dick, Huckleberry Finn, Pride and Prejudice, Gatsby (tools/data)
plus 18 Project Gutenberg books 1813-1902 fetched once into `corpus/` (not committed; `corpus/MANIFEST.tsv` lists
them), 17.3 M letters. Control plaintext: Holmes, *Adventures* (tools/data/pg1661_holmes.txt), kept out of the LM.

score.py was not frozen when this group started (no swarm/README.md at 02:54 UTC), so Phase 1 below uses the brief's
fallback: hand-planted controls. A planted control is shaped like c2: its own non-gap length (643 letters), the
target's gaps (`_`, MULTI) at the target's own positions, clear spans dropped, punctuation-class boxes dropped, and a
sign-count curve following c2's (signs allotted greedily to letters, occurrences drawn by remaining quota). Noise =
share of tokens replaced by a random other sign (c2's settled draft carries 14-17 pct measured type noise).
Recovery = share of planted letters read right, noised tokens included (ceiling about 1 - noise).

| time | method | parameters | control result | real-text held-out pct | why it failed / note |
|---|---|---|---|---|---|
| 02:58 | quadgram annealer, 2.2 M-letter LM | c2-shaped, noise 0, beta 0.5-2, t0 1-2.5, 30 restarts x 3 M | 0.43-0.78 | not run | the planted key scores about 70-90 log10 below the best keys found: quadgrams from 2 M letters over-fit at N/K about 5 |
| 03:00 | quadgram, 17.3 M-letter LM | same | 0.44-0.75 | not run | truth still about 70 below the optimum; more data alone does not fix a quadgram objective at this N/K |
| 03:00 | 5-gram Witten-Bell conditional | noise 0, beta 1 / 2 / 4, 30 x 3 M | **0.93** / 0.89 / 0.86 | not run | clean control passes the 70 pct stepping stone |
| 03:01 | 5-gram, beta 1 | noise 0.10 (seeds 2, 3) | 0.41, 0.71 | not run | noise breaks it on one seed of two |
| 03:01 | 5-gram, beta 1 | noise 0.15 (seeds 2, 3) | 0.61, 0.47 | not run | below 70 at the measured noise |
| 03:03 | 5-gram + bounded loss q 0.05 / 0.15 | noise 0.15, seeds 2, 3 | 0.63, 0.59 / 0.64, 0.51 | not run | small gain; still below 70 at 15 pct noise |
| 03:05 | 5-gram + bounded loss q 0.1, 100 restarts x 5 M | noise 0.10 (s2, s3) / 0.15 (s2, s3) | 0.59, 0.78 / 0.65, 0.60 | not run | more search helps a little; 15 pct noise holds it near 0.6 (ceiling about 0.85) |
| 03:10 | same, 60 x 4 M, **real c2, X as a letter** | beta 1, q 0.1, seed 1 | matched control (noise 0.15, s2): 0.65 recovery, -0.892 per 5-gram window | c2 fit: -0.999 per window; its own sign-shuffled text: -1.057 | target sits much nearer its shuffle than the matched English control; see held-out row below |
| 03:10 | same, **real c2, X dropped as a null** | seed 1 | matched X-null control (noise 0.15, s2): **0.196** -- control FAILS | c2 fit -0.939; shuffled -0.930 (no better than shuffle) | non-test: with X removed (N 547, K 121) the method cannot read its own control at 15 pct noise |
| 03:13 | held-out proxy (`heldout.py`: key fitted on c2 applied to c1, 5-gram mean per window vs 1000 value-permuted keys) | X letter, seed 1 | power check `control2` (one planted key over c2+c1, fit c2, test c1): noise 0: recovery c2 0.94/0.93, c1 0.83/0.88, held-out pct 100/100; noise 0.15: c2 0.42/0.62, c1 0.38/0.64, held-out pct **100/100** (all four above p99.9) | **c2->c1: 88.6** (X letter); X null 47.6; key from the shuffled c2: 97.3 | real key below the power-checked bar; the shuffled-text key does as well or better, so the 88.6 is noise |
| 03:16 | same, more seeds, real c2 X letter | seeds 2, 3, 4 | (as above) | c2 fit -1.008 / -0.990 / -1.006 per window; c2->c1 held-out **98.9 / 89.3 / 86.3** | never above p99.9; seed spread 86-99 on the same text is the size of the noise in this statistic at 59 scored windows |
| 03:16 | reverse direction, fit c1 -> test c2 | control2 fit c1 (N 125, K 74), noise 0 | recovery c1 **0.008**, c2 0.019 -- control FAILS | not run | the c1->c2 direction is untestable by this method: c1 is too short to fit a homophonic key; any bar that needs both directions cannot be met by a letter-homophonic key found by annealing |
| 03:18 | **X as the word space** (27-symbol 5-gram with spaces, X fixed to space) | c2, noise 0 / 0.15 | 0.93 / 0.64 letters (0.71 incl. spaces); fit -0.569 / -0.848 per window | c2 fit **-1.051** vs own shuffle -1.045; c2->c1 held-out 53.0 (shuffled-text key 91.2); power check control2 (noise 0.15): c1 0.67, held-out 100 | target no better than its shuffle; English with X as the space is not what the anneal sees |
| 03:22 | **pooled fit c2+c3+c4 -> test c1** (shared-key band per h15; N 1013, K 151) | X letter, noise 0.15 controls, 60 x 5 M | English controls (seeds 41, 42, 61, 62): fit recovery 0.75 / 0.66 / 0.69 / 0.77, c1 0.66 / 0.69 / 0.58 / 0.74, fit -0.935 / -0.921 per window (61, 62), held-out 100 x4 | target seeds 1-3: fit -1.110 / -1.115 / -1.117; held-out **98.7 / 97.3 / 99.9** (99.92 at 5000 nulls, seed 3); own shuffles (4 seeds): fit -1.113 to -1.122, held-out 75.7-96.7 | fit no better than shuffle; see the wrong-language row: the held-out excess over shuffles is not English |
| 03:31 | **wrong-language control**: French plaintext (Madame Bovary; Le Rouge et le Noir, tools/data/fr19) enciphered the same way, fitted with the ENGLISH model, pooled fit -> c1 | noise 0.15, seeds 51, 52, 63, 64 | recovery 0.20-0.32 (as expected: wrong LM); fit -1.060 / -1.043 per window (63, 64) | held-out **100 / 85.6 / 98.5 / 99.9** | the held-out percentile against value-permuted keys does not identify the language: French read with an English model reaches it as often as the real text does. The real text (-1.11) fits below even this wrong-language control (-1.04 to -1.06) |
| 03:35 | pooled, lines read right to left | seed 1 | (English controls as above) | fit -1.106 (forward -1.110 to -1.117) | no direction effect |
| 03:35 | pooled, X as space | seed 1 | c2 controls above | fit -1.143 vs own shuffle -1.175; held-out 97.1 vs shuffle 84.9 | target above its shuffle but nowhere near English controls (-0.85 on c2) |
| 03:38 | pooled, H31 pictograms read as gaps (capitals/determinatives), N 958, K 128 | seeds 1, 2 | English control (seed 71, same shape, noise 0.15): recovery 0.73 fit, 0.7 c1; fit -0.977; held-out 100 | fit -1.080 / -1.080 vs own shuffles -1.111 / -1.119; held-out 97.3 / 97.8 vs shuffles 87.8 / 97.9 | the target's margin over its shuffle grows (0.03 vs 0.00-0.01 with pictograms kept) -- more sequential order without them -- but it is still 0.10 per window short of English |

## Harness frozen (score.py FROZEN ed4a3743, blob d80e6baa, 03:14 UTC); Phase 1 on the harness controls

At 03:41 the harness's EN-HOMO plaintext turned out to be Tennyson's *Idylls of the King* (PG 610), which was in this
group's LM corpus (`corpus/pg610.txt`). Removed and both models rebuilt at 03:42 (16.9 M letters) before any Phase 1
row below; every row above used the LM with Tennyson in it but none of them used a Tennyson plaintext (my own
controls are Holmes and, for the wrong-language rows, Flaubert and Stendhal). Method from here on is `fit_key.py`
(defaults 60 restarts x 5 M, q 0.1, beta 1, t0 2.5), reading only the named ciphertext.

| time | method | parameters | control result | real-text held-out pct | why it failed / note |
|---|---|---|---|---|---|
| 03:45 | `fit_key.py --control EN-HOMO` (pooled c1+c2 of the control) | default | **score.py --control EN-HOMO: recovery 95.19** (c1 96.97, c2 94.83) | -- | Phase 1 met |
| 03:45 | `fit_key.py --control EN-HOMO-N15` | default | **recovery 73.8** (c1 75.0, c2 73.56) | -- | Phase 1 met at the -N15 noise too |
| 03:45 | same, fit on the control's c2 only, score.py held-out EN-HOMO.c2 -> .c1 | default | clean: recovery_test 90.15, en_quad 100/100 strat, en_dict 100/100; N15: recovery_test 73.48, en_quad 100/100, en_dict 100/100 | -- | the c2 -> c1 direction passes on the matched control at both noise levels (so do fr/es quad: a correct key reads as "some language" in every quad model) |
| 03:48 | `fit_key.py --text c2` -> KEY_fit_c2.tsv; `--text c1` -> KEY_fit_c1.tsv | default | (Phase 1 above) | committed before scoring; next row | fit per window: c2 -1.001 (EN-HOMO-N15 c2 fit -1.027, EN-HOMO clean -0.839); c1 -0.767 (N 125, K 55: over-fit, cf. README reachability) |
| 03:50 | **Phase 2, score.py held-out, KEY_fit_c2.tsv, fit c2 -> test c1** (`keys/P2_fit_c2_test_c1.json`) | coverage_test 0.90, read_letters 113 | matched EN-HOMO-N15 c2 -> c1: en_quad 100 / strat 100, en_dict 100 / 100 | **en_quad 93.3 / strat 32.7; en_dict 0.0 / 0.0**; best of the eleven: fr_quad 100 / strat 98.2 (not beats_all_strat), la_quad 98.6 / 92.8, es_quad 98.7 / 83.7; vocab 0 | no statistic passes; the English statistics are the weakest (the stratified null takes away the frequency match, leaving 32.7); the fr_quad lead is a frequency effect of an English-fitted key, not a French reading (group A's question) |
| 03:50 | **Phase 2, KEY_fit_c1.tsv, fit c1 -> test c2** (`keys/P2_fit_c1_test_c2.json`) | coverage_test 0.71, read_letters 453 | this direction fails on the control too (control2 fit c1: 0.8 pct recovery; README reachability 1.1 pct) | en_quad 79.1 / 78.1; en_dict 0 / 0; best es_dict 92.4 / 91.2 | untestable by a fitted homophonic key at c1's length; logged, not a negative |
| 04:02 | refit null (amendment), `refit_null.sh c2 c1 50`: fit_key.py on c2 with its sign order shuffled, each refit scored by score.py c2 -> c1 | the earliest 16 of 50 | -- | real KEY_fit_c2 en_quad -5.842 vs refit median -5.582, p99 -5.321: **below 15 of 16 refits**; en_dict 0.000 vs refit median 0.071; refits' own plain pct median 99.5 (max 100) on en_quad, none beats_all under both nulls | the real key reads c1 worse than keys fitted on order-shuffled c2: nothing English in c2's order that carries to c1. Final numbers at 50 refits in `refit/summary_c2_c1.json` |
| 04:05 | score.py on the explore/ pooled keys (fit c2+c3+c4, restricted to c2 signs, test c1; informational -- not Phase 2 keys, they read c3/c4 too) | real seeds 1-3; shuffled-pool seeds 1-4; pictograms-as-gaps real/shuffled | -- | en_quad pct / strat: real 99.9/72.6, 92.4/47.6, 99.5/87.4; shuffled 97.4/66.1, 93.0/21.7, 99.3/97.1, 94.3/43.7; no-pictogram real 88.1/31.9 vs its shuffle 98.8/56.9 | my own proxy's 98.7-99.9 for the pooled keys was the frequency match: under score.py's stratified null the real keys sit inside the shuffled-text keys' range (21.7-97.1) |
| 04:05 | what the fit does with the top sign | KEY_fit_c2 | -- | X -> e (and X-DOT -> e); e is 19.1 pct of the read letters (English about 12.5) | the fit needs e far above English to place X; the KL term (beta 1) does not hold it -- a symptom of a text whose top sign is not an English letter at its English rate |
| 04:32 | refit null complete, 50 refits c2 -> c1 (`refit/summary_c2_c1.json`) | -- | -- | real en_quad -5.842: **4 of 50 refits below it** (refit median -5.633, p99 -5.321); en_dict 0.000 vs refit median 0.035, p99 0.142; vocab 0.000 vs 0.027; refits' own plain pct on en_quad: median 99.1, max 100; no refit beats_all under both nulls | both nulls say no: the real key is under the plain/stratified bar AND at about the 8th percentile of the refit null |
| 04:35 | fold split (README's reachable alternative; informational, the bar is unchanged): fit c1+c2a -> test c2b, and c2b -> c1+c2a | default | EN-HOMO-N15: c1+c2a -> c2b recovery_test 48.0, en_quad **100 / 100**, en_dict 0 / 0; c2b -> c1+c2a recovery_test 21.8, en_quad 92.9 / 58.2 (fails on the control) | real c1+c2a -> c2b: en_quad **100 / 98.1**, en_dict 89.3 / 55.1, fr_quad 100 / 93.2, es_quad see json; real c2b -> c1+c2a: en_quad 83.3 / 54.5 | the one near number in this log; refit null for this direction started 04:36 (40 refits) before anything is read into it. c2b (N 197) is too short to fit, on the control as on the real text |
| 05:05 | refit null for the fold, 40 refits c1+c2a -> c2b (`refit/summary_c1+c2a_c2b.json`) | -- | -- | real en_quad -5.488: 36 of 40 refits below (refit median -5.657, **p99 -5.356**: real below it); the same rank in every language: fr_quad 36/40, es_quad 37/40, pt_quad 38/40, la_quad 22/40; vocab 0.073, 39/40 below (p99 0.084); **one refit on order-shuffled text beats_all under BOTH nulls on en_quad** (and one each on fr_dict, es_dict) | not a pass (real under the refit p99; not beats_all_strat). The real key's lead over shuffled refits is the same size in French, Spanish and Portuguese as in English: order shared between c1+c2a and c2b that no one language model prefers, not English |

## Result (DEB-SWARM-B, round 1, 29 Sept 2026 05:1x UTC)

- **Phase 1 met.** `fit_key.py` on EN-HOMO: score.py recovery 95.19 pct; on EN-HOMO-N15: 73.8 pct. Held-out on the
  control (fit .c2, test .c1): en_quad and en_dict beat all 1000 shuffles under both nulls, clean and N15.
- **Phase 2, no pass.** KEY_fit_c2 -> c1: en_quad 93.3 / strat 32.7, en_dict 0 / 0, at the 8th percentile of 50
  shuffled-order refits. KEY_fit_c1 -> c2: en_quad 79.1 / 78.1 -- a direction the method fails on its own control
  (c1 is too short), so it is untestable, not a negative. With EN-HOMO-N15 beside it (100 / 100 in the same c2 -> c1
  test), the c2 -> c1 row is a control-backed negative for English written as homophonic letters with X as an
  ordinary sign, conditional on the settled transcription.
- Variants that also failed against a working control: X as the word space (c2 and pooled), X as a null (control
  fails at N 547: non-test), lines reversed, pictograms read as gaps, pooled c2+c3+c4 fit (informational), fold
  c1+c2a <-> c2b (informational).
- Attempts: 30 rows in this log (about 180 annealer runs, plus 90 refits).

## Transferable insights for the merge (at most three)

1. **A structural fact:** under an English 5-gram annealer, the real text fits no better than its own sign-order
   shuffle (pooled -1.110 to -1.117 vs -1.113 to -1.122 per window), below a FRENCH plaintext read with the same
   English model (-1.04 to -1.06), and far below English controls at the same noise (-0.92 to -0.98). Yet keys fitted
   on the real order carry to the held-out text a little better than refits on shuffled order, by the same margin in
   every language (fold: 36-38 of 40 refits beaten in en/fr/es/pt). Some order is shared between the texts (cf. H41's
   recurring pairs), and no letter language model prefers it.
2. **A constraint on the bar:** the value-permuted null does not identify a language. Keys fitted on shuffled text
   reach plain pct 99-100 on every quad model (median 99.1-99.3 over 90 refits); a French plaintext fitted with the
   English model reached 85.6-100 on my held-out proxy; and one of 40 shuffled-text refits cleared plain AND
   stratified beats_all on en_quad. The refit null (amendment) is needed; so is a cross-language check (a claim in
   language L should beat the same key's standing in the other languages, not only its own nulls).
3. **A tool:** `hsolve.c` + `build5.c` (Witten-Bell 5-gram conditional, not quadgram) take a homophonic control of this
   exact shape from 0.43-0.78 (quadgrams, planted key scoring about 80 log10 below the found optimum) to 0.93-0.95
   clean and 0.74 at 15 pct noise; any group fitting letter keys at N/K about 5 should use 5-grams, not quadgrams.
   `fit_key.py --shuffle-seed` and `refit_null.sh` supply the amendment's refit null for any fitter.
