# GAPS48 pre-registration (3 Oct 2026, account-4): crib placement under a one-part code hypothesis

Written and pushed before any target score is computed. Script: `gaps48/crib_place.py` (fixed seeds, disk only).

**Ciphertext.** No 4 letter (229 groups) + No 6 annex (75 groups) = 304 groups, image reading `gaps36/reconciled.tsv`
(dashes and "?" stripped; 455 and 1197 taken as read). Same code, same writer, same week. Values 15-1339; K = 216 distinct.

**design_prior.py** (run first, `--no-write`, on gaps48/no4_all.txt, 304 tokens, 216 distinct; output
gaps48/design_prior.txt): multi-sign d=1.12 not above null; mixed 1.62; letter 2.23; code(numbers) 2.72 excluded; FP
rate 0.05; nearest keys hellen-frederick-1752 sibling (mixed), huntington-luzerne (syllabary), vanbeuningen-dewitt-1657
(nomenclator). So the prior points to a large nomenclator/multi-sign table; a one-part (alphabetical) nomenclator is a
sub-hypothesis of that class, and design_prior cannot separate one-part from two-part (its statistics are label-free).

**Hypothesis H1 (one-part).** The code's value order tracks the alphabetical order of its plaintext units, roughly
uniformly over 15-1339, so a word's value is predictable (up to error) from its alphabetical rank in a vocabulary of
the language.

**Predictor.** Reference vocabulary = the 1299 commonest word types of the corpus plus the 26 letters, sorted
alphabetically (accents stripped, lower case); a word's predicted value = 15 + (bisect rank / 1325) x 1325. Run under
two languages: French (`tools/data/fr1810`) and Dutch (`tools/data/nl18`), since No 4's language under the figures is
not known (its clear frame is Dutch, its clear siblings No 2/No 3 French).

**Statistics (per crib c, given the text's group values).**
- S1 (primary): d1(c) = min |v - p(c)| over all distinct groups v in the text.
- S2 (secondary): d2(c) = min |v - p(c)| over groups v that occur at least twice in the text.
- Score of a crib list against a decoy list: AUC = P(d(crib) < d(decoy)) (ties 0.5). 0.5 = no information.

**Target cribs** (GAPS44 strong + medium, fixed now). French: agar, grand, duc, empereur, roi, sevenaar, traite,
ratifications, paris, utrecht, note, limites. Dutch: agar, groot, hertog, keizer, koning, zevenaar, tractaat,
ratificatie, parijs, utrecht, nota, grenzen.
**Decoys:** 300 content words (length >= 4, not in the cribs) drawn at random (seed 48) from the reference vocabulary.

**Matched control (rule 3).** Per seed (20 seeds) and language: a synthetic one-part code is built from a DIFFERENT
half of the corpus files than the predictor (builder vocabulary = commonest 1299 types of the builder half + 26 letters,
sorted, values 15..1339 consecutive); a random contiguous passage of the builder half is enciphered word by word (out-of-vocabulary words spelled letter by letter) until 304 groups. True cribs = 12
content words (length >= 4) present in the passage (S1: count >= 1; S2: count >= 2, as many as exist up to 12); decoys
= 300 content words of the predictor vocabulary absent from the passage. AUC computed exactly as for the target.
**Second control that must be able to fail differently:** the same passages under a two-part code (values assigned to
the builder vocabulary in random order). Under it the crib AUC must sit near 0.5; if it does not, the statistic is not
measuring order and the test is void.

**Gates (fixed now).**
- G0 (statistic can vary): two-part control mean AUC within 0.40-0.60 for S1.
- G1 (power): one-part control mean AUC >= 0.75 (S1) over 20 seeds, in the language being scored.
- G2 (ceiling check, rule 3): report the decoy hit rate d<=3 in the control; if one-part control AUC is >= 0.95 with a
  two-part AUC also >= 0.9, the control is at ceiling for a reason other than order and the gate is void.
- If G1 fails in a language: CONTROL BELOW GATE, the target is still scored but its number is logged as non-test
  ("untestable by crib placement at N=304"), never as a negative.
- Target PASS (only if G0 and G1 hold): target AUC above the 95th percentile of the two-part control's AUC distribution
  for the same crib count (12 cribs), in that language. A PASS licenses grade S candidates (crib -> nearest group) only,
  no reading. A FAIL with the control passing is a control-backed negative for "one-part code with these cribs present".
