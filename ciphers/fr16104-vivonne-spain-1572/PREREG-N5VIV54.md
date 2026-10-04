# PREREG-N5VIV54 (4 Oct 2026, N5-VIV54, LANE-NEAR5 worker, account 2)

Written and pushed BEFORE any key.tsv decode of fr.16104 f.173r-v (ink 54, 7 Sept 1572) exists. Inputs frozen at this commit:
tx/f173r_rec.tsv, tx/f173v_rec.tsv (two blind Sonnet passes + tx/reconcile_vivk.py --viv54; err_2reader 0.223 / 0.193),
tx/glosses54.tsv (interlinear words read by this worker at native resolution BEFORE any decode; 7 rows marked use=yes),
key.tsv (Tomokiyo's published values, N5-VIVK). Tokenisation = tx/vivk_test.py tokens() ("o o" -> "oo"); codes absent from key.tsv
are unread (dropped from decoded letter strings). One rng seed 20260904+54 = 20260958 for every null; 200 draws each.

## (a) Gloss check
For each use=yes gloss: n = tokens on that line; window W = decoded letters of tokens floor((x0frac-0.08)*n) .. ceil((x1frac+0.08)*n)
(clipped to the line). Score(g) = LCS(gloss_letters, W) / len(gloss_letters) (u/v, i/j folded). Statistic S_a = mean over the 7 glosses.
Null: 200 shuffled keys (key.tsv's 30 values permuted across its 30 codes; the unread set unchanged) -> S_a per draw. The null can move
the statistic (W's letters change with the key).
PASS (a): S_a > null p95 AND S_a >= 0.60. Void if the null median >= 0.95 (ceiling).

## (b) Language judge
Judge: tools/judge_plaintext.py with a judge block {"corpora": tools/data/fr16 (Catherine de Medicis Lettres I, II; Marguerite de
Valois letters), "min_word_cover": 0.5}. Corpus era: 16th-century French court/diplomatic letters (c.1533-1615), era- and
register-matched to a 1572 ambassador's letter; three source files only (< 5): per rule 3 a FAIL/PASS is of limited reliability
on its own, which is why (b) is gated on the positive control below.
Candidate = the whole decoded letter string of f.173r+f.173v (unread codes dropped, no word division).
Positive control (same hand, key, similar length): N5-VIVK's held-out f.103r (tx/f103r_rec.tsv) decoded with key.tsv the same way.
Nulls: 200 shuffled-key decodes of the f.173 transcription (as in (a)); the judge's mean log10 4-gram score per letter is recorded per draw.
Rules, in order:
 1. If the positive control FAILs the judge, the judge is not a gate here: (b) is reported "judge not a gate", no PASS/FAIL claimed.
 2. If more than 10 of 200 shuffled-key decodes PASS the judge, the judge is void as a gate for this family at this N (ARM-C1).
 3. Otherwise PASS (b): the candidate PASSes the judge AND its 4-gram score > the shuffled-key null p99.
Either (a) or (b) passing licenses "piece 54 ready for audit 1"; both are reported side by side whatever the outcome.
Not gated (descriptive only): the per-line decode read by eye, and print_check phrase hits.
