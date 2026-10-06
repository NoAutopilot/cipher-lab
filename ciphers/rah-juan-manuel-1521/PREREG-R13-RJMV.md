# PREREG R13-RJMV (verifier, 6 Oct 2026, written 13:3x UTC before the scored run)

Question: does "judge cannot decide" (R12-RJM9501) hold for the R9501 f.34 trial decode once the order-shuffled control is run over
more than one seed?

Run: scripts/decode9501.py's own reconcile and decode_tok, unchanged; the reconciled token list shuffled with random.Random(seed) for
seeds 1-20 (seed 1 = the committed reading_f34_shuffled.txt, which must reproduce byte for byte); each rendered with the script's own
render(); each scored with tools/judge_plaintext.py on es1600 (spec copy with judge.language=es1600) and on the spec's es17c.
The control varies on the statistic tested: token order changes every 4-gram across code-word and letter-run boundaries.

Decision, per corpus, fixed now:
- target score > every one of the 20 shuffled scores (empirical p < 0.05): the judge sees word order in the decode; record the margin
  over the shuffled max in units of the shuffled SD.
- otherwise: the judge does not separate the decode from its own shuffled control at this N.
Either way the target FAIL against real_p05 stands as recorded; "judge cannot decide" is kept unless the target clears real_p05 (it
cannot change: the target score is fixed) -- i.e. the spread only qualifies how close the control is, it does not turn the FAIL into a
negative on the key or into a pass. No key, grade or reading changes on any outcome.
