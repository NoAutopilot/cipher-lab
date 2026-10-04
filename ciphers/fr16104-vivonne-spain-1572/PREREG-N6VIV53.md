# PREREG-N6VIV53 (4 Oct 2026, N6-VIV53, LANE-NEAR6 worker, account 2)

Written and pushed BEFORE any key.tsv decode of fr.16104 ff.170r-171r (ink 53, 5 Sept 1572, Saint-Gouard to the duc d'Anjou) exists.
Pages read: f.170r (22 lines), f.170v (29), f.171r (30); f.171v (18 lines) not transcribed (cap, NOTES "N6-VIV53").
Inputs frozen at this commit: tx/f170r_rec.tsv, tx/f170v_rec.tsv, tx/f171r_rec.tsv (two blind Sonnet passes per page,
tx/viv54_clean.py, tools/reconcile_passes.py, tx/reconcile_vivk.py --viv54 -- N5-VIVK's six label rules plus N5-VIV54's ':'/'o' rule,
nothing added); tx/glosses53.tsv (interlinear words read by this worker at native resolution from the cached source regions BEFORE any
decode; 6 rows use=yes: myssent, enquelque, infant, longuement, catixanura, portent); key.tsv unchanged (Tomokiyo's published values,
N5-VIVK). Tokenisation and decode exactly as tx/viv54_decode.py / tx/viv54_test.py ("o o" -> "oo"; codes absent from key.tsv unread).
One rng seed 20260904+53 = 20260957 for every null; 200 draws each.

## (a) Gloss check (the gate)
Identical to PREREG-N5VIV54 (a): window W = decoded letters of tokens floor((x0frac-0.08)*n) .. ceil((x1frac+0.08)*n) of the glossed line
(n = tokens on that line, clipped); Score(g) = LCS(gloss_letters, W)/len(gloss_letters), u/v and i/j folded; S_a = mean over the 6
use=yes rows. Null: 200 shuffled keys (key.tsv's 30 values permuted across its 30 codes, unread set unchanged) -> S_a per draw.
The null can differ from the target on this statistic (W's letters change with the key).
PASS (a): S_a > null p95 AND S_a >= 0.60. Void if the null median >= 0.95 (ceiling). Reported per gloss as well.
Known weakness stated in advance: "catixanura" is an unrecognised word and "longuement" has uncertain middle letters; both are scored as read.

## (b) Language judge (descriptive unless its positive control passes)
As PREREG-N5VIV54 (b), same judge block (tools/data/fr16: Catherine de Medicis Lettres I, II; Marguerite de Valois; 16th-century court
French, era- and register-matched, three source files only), candidate = all decoded letters of the three pages, positive control =
N5-VIVK's f.103r decode (tx/f103r_control_decode.txt, which FAILed this judge in N5-VIV54), 200 shuffled-key decodes of the target.
Rules in order: 1. positive control FAILs -> "judge not a gate"; 2. > 10/200 shuffled-key decodes PASS -> void; 3. else PASS (b) = candidate
PASSes and its score > shuffled-key p99. Rule 1 is expected to fire (it did for N5-VIV54 with the same control); then (b) is descriptive only.
Only (a) licenses "piece 53 ready for audit 1". Not gated: per-line reading by eye, print_check hits.
