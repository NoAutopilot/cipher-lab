# PREREG R12D-FAIR -- fair-game-2010, word-constrained substitution solve (written 6 Oct 2026, before any scored run)

Ciphertext: the marked letters themselves (the folder's simple-substitution hypothesis, Schmeh's frequency remark),
both credit-block orders reconciled by GF4-BATCH22 against Rossignol's screenshots (reconcile_2026-10-03.tsv):
scroll order = the spec/ATS text (`test2/order_scroll.txt`), column order = Schmeh 2026 (`test2/order_column.txt`);
67 known letters, position 1:4 (redacted) dropped, K=21. The Halpin next-letter scheme was read directly in test 1
(no key, control-backed negative) and is not re-run here.

Instrument (different from test 2's anneal, rule 3 third-attempt clause): `tools/families/masc_words.py` -- the masc
n-gram anneal followed by a hill-climb on n-gram score + lam x dictionary-segmentation log-prob (lam 1.0, polish 4000,
oov -12, corpus words with count >= 3). Crib sub-step: `r12d/isomorph_scan.py`, a pattern-consistency scan of the
credits' clear line "Democracy only works if you do your part" and its pieces (DEMOCRACY, ONLYWORKS, DOYOURPART,
YOURPART, TAKEPART) plus topical words, with the expected count on 200 shuffles; a crib with zero consistent
placements cannot be plaintext at any offset under simple substitution, so no crib-fixed solve is run for it.

Control: family_run.py's matched masc control (window with exactly K=21 distinct letters, N=67, one sign per letter),
en corpus (pg1661_holmes + pg2701_mobydick, the spec's), seeds 1-5, restarts 16.
Gates (both needed before the target run):
 G1 control mean letter recovery >= 0.60;
 G2 gain over blind: control mean >= 0.70, i.e. >= 0.10 above masc's own 0.591 at seeds 1-5 (r32, HYPOTHESES.md),
    so the word term demonstrably adds power; masc's 0.591 is far from ceiling, so there is headroom to show it.
If G1 or G2 fails: CONTROL BELOW GATE, the target is not run, logged as untestable by this instrument at N=67.
Target reading criterion (if gated): judge PASS (`tools/judge_plaintext.py specs/fair-game-2010.json`) AND the target's
judge score above every one of 5 shuffled-target decodes by the same instrument (shuffle seeds 7-11, same order).
Anything else is a FAIL; the en judge's unknown reliability (EN-FOLDS) is stated beside any result.
