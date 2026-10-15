# PREREG-HAR-37R (15 Oct 2026, 14:5x UTC by date -u), pushed before any image fetch, read or score

Job: `.claude/briefs/runs/2026-10-15-ytbiz-default-1410-jobs.md` "HAR-37R". Units: R8478 f.37r glossed cipher runs, R8480 f.41r cipher
block with its interlinear fragments and left-margin clear version. Key under test: Bourdeau's needham1587 three-grid pigpen
(github.com/dbourdeau/cyphersolver targets/needham1587/decode.py, commit 0445769; MIT code / CC BY 4.0 text), applied unchanged:
shapes J U L / C O F / N 7 D, plain a-i, dot below k-s, dot inside t u w x y z.

Reads (all blind): two Sonnet passes (P1, P2) transcribe the cipher signs of each run as shape+mark labels from line crops only, told the
nine shapes by their strokes and the three mark states, never told the key, any plaintext, the glosses or Bourdeau's strings; one Sonnet
pass (G) reads the gloss words from crops of the gloss band only, never told the cipher or the key. One reconcile (R) settles P1/P2
disagreements from the crops, still blind to G and the key. I do not settle the gloss before scoring (V-BRANDT rule).

Normalisation (CLAUDE.md rule 3, PX-BRODEC), applied identically to decode and gloss before any diff: lowercase; keep letters only
(word spacing dropped); j->i, v->u, y->i; collapse doubled letters; expand "L."/"Lo."/"Lord"->"lord", "Mr"->"master", "Sr"->"sir",
"&"->"and", "yt"->"that", "ye"->"the", a superscript/tilde abbreviation read by G as written (no expansion beyond this list).

Statistic per pair i: s_i = 1 - lev(D_i, G_i) / max(len D_i, len G_i), D = key decode of the reconciled cipher run, G = gloss pass.
Target statistic S = mean s_i over all pairs with both a cipher run (>= 3 signs) and a gloss (>= 3 letters).
Control: 1000 draws (random.Random(37)) permuting the gloss strings among the cipher runs; S_null distribution, p95 and the
fraction >= S. The control can fail differently from the target: it changes which gloss each decode is diffed against, which is
exactly what S measures (not orthogonal, rule 3 bCAS/AX-5799 clause).
Per-pass check: the same S computed with P1 alone and P2 alone (no reconcile) reported beside R.

Gate (fixed now):
- K1 (key holds on f.37r/f.41r): S(R) >= 0.80 AND S(R) > p95(S_null) AND both S(P1), S(P2) > p95(S_null).
- Pair classes: agree s_i >= 0.75; conflict s_i < 0.50 where P1 = P2 on every sign of the run (a read-agreed conflict, logged to
  HYPOTHESES.md with witnesses, rule 4); between or reader-split = unsettled (M).
- K2 (gloss adds key values at C): a sign label not in the key (a code mark, a symbol outside the 27 forms) that sits in an agree run
  where the gloss pins exactly one letter/word to it; else none added.
- f.41r margin: S computed on the cipher block (as one string) vs the margin clear version trimmed to the block's length by best local
  alignment; reported separately, not part of K1 if the margin's extent cannot be fixed from the crops (then: non-test, said so).
Outcomes: A = K1 pass (Bourdeau's key reads R8478/R8480 at C on the glossed runs); B = K1 fails with S > p95 but < 0.80 (key mostly
holds, reader or gloss noise; report pairs); C = S <= p95 (non-test or key does not hold; reader agreement P1 vs P2 decides which).
A FAIL or non-test is reported as such. Units priced: P1, P2, G, R (~0.6-1 each) + floor; stop before a unit crossing 80% of cap 4 or box.
