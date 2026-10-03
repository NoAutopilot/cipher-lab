# GAPS54 pre-registration (3 Oct 2026, account-4): one-part frequency-position test

Written and pushed before any control or target score is computed. Script: `gaps54/freq_pos.py` (fixed seeds, disk
only). Ciphertext: `gaps54/no4_all.txt` = GAPS48's file (No 4 letter 229 + No 6 annex 75 = 304 groups, K 216, values
15-1339; the GAPS36 image reading).

**Hypothesis H1 (one-part).** The code's values follow the alphabetical order of its plaintext units, roughly uniformly
over 15-1339. Then the text's commonest groups (function words) should sit near the alphabetical places of the language's
commonest words (FR: de, la, le, et, que, les, a, ...; NL: de, het, van, en, een, te, ...).

**Predictor.** As GAPS48: reference vocabulary = 1299 commonest word types (length > 1) of the corpus + 26 letters,
sorted; predicted value p(w) = 15 + bisect-rank x 1325 / |vocab|. Function-word set F = the 15 commonest words (any
length) of the predictor corpus. French `tools/data/fr1810`, Dutch `tools/data/nl18`, scored separately.

**Statistic S (lower = more one-part-like).** Let T = the groups occurring >= 3 times in the 304-group text (target: 19
groups). S = mean over t in T of min over w in F of |t - p(w)|. Unweighted by count. If |T| < 5 in a control text,
T = the 5 commonest groups (ties by value).

**Matched control (rule 3, design-matched and K-matched).** Per seed and language, a synthetic code built from a
different half of the corpus files than the predictor (builder vocabulary = 1299 commonest types + 26 letters, values
15..1339). Encipherment of a random contiguous builder passage, word by word, out-of-vocabulary word -> the one group of
its alphabetical neighbour entry (GAPS48's `--kmatch` encoding; GAPS48's spelled-out encoding gave K 72-89 against the
target's 216, which would put letter groups at the top of the frequency list), until 304 groups.
- One-part control: builder vocabulary in alphabetical order. 40 seeds.
- Two-part control: the same passages, builder vocabulary in random order. 200 seeds. This is the null, and it can fail
  differently: shuffling value order changes which values the common words get, which is exactly the axis S measures
  (not orthogonal, cf. rule 3 bCAS/AX-5799).

**Gates (fixed now; control first).**
- G1 (power at N 304): at least 80% of the 40 one-part control seeds have S below the two-part p05 (the 5th percentile of
  the 200 two-part S values), in the language being scored. If G1 fails in a language, the target is NOT scored in that
  language: logged "untestable at this N by this statistic", and the script stops for that language.
- G2 (headroom / sanity): two-part mean S must sit within 25-75 (a random 15-point set over 1325 values gives a mean
  nearest distance of roughly 1325/32 ~ 41); outside that range the null is malformed and the test is void.
- Target, only if G1 and G2 hold: PASS if target S < two-part p05; FAIL otherwise. A FAIL with G1 passing is a
  control-backed negative for "one-part code, values uniform over the alphabet" in that language (not for one-part codes
  with names/syllables in separate sections or with non-uniform spacing). A PASS licenses grade-S candidates only
  (commonest group -> nearest function word), no reading; it goes to a separate session.
- Secondary (reported, not gated): S restricted to the 10 commonest groups; the per-seed K of the controls.
