# PREREG -- erba-2006 spec test 3 (letter-like design), R12D-ERBA3, 6 Oct 2026 (written before any scored run)

Only a 1-control, 2-restart, 800-iteration `--quick` smoke run of the script was made before this file (to check it runs);
its numbers are not the result and are superseded by the scored run below.

Corpus: `tools/data/it21news` (built this job: Italian Wikinews 2005-2026, CC BY 2.5; README there). Removes the it19 era caveat
(1800-1830) for a 2013 note; register is news, not a private letter (stated caveat).

Design (letter-like, per R12D-ERBA's test 2): each digraph token = one plaintext letter CLASS. With 9 case-folded token types and
~21 Italian letters, a letter-per-token design must be polyphonic (several letters per token). Case is folded (case variants look
positional, capitals at line/word starts; a case-sensitive variant is not run here). The 8 me/ne calls stay as read (grade M).
- V1: xs = word space; K = 8 classes (cu fi me mi ne pi ro un); 100 letters.
- V2: xs = one more class; K = 9; 114 letters; no spaces.
Plaintext alphabet: abcdefghilmnopqrstuvz (j->i, k->c, w->v, x->s, y->i). LM: letter bigram (+ space in V1), add-0.5, trained
on it21news folds y2005_06, y2007, y2008, y2009_10. Solver: simulated annealing over the letter->class assignment (every class
non-empty), objective = forward log-likelihood of the observed class/space sequence, 8 restarts x 5000 moves; decode = Viterbi.

Matched control (rule 3; can vary on the statistic -- letter accuracy against a known plaintext): 5 windows of the held-out
fold y2011_26 (not in the LM), same letter count as the target variant (100 / 114), V1 with real word spaces, enciphered under
a random K-class partition of the 21 letters, same solver and seed stream (seed 3). Reported per control: solver letter
accuracy, TRUE-key Viterbi accuracy (oracle ceiling of the design at this N under this LM), and whether the solver's
log-likelihood reaches the true key's (search adequacy).

Gate (per variant): control mean letter accuracy >= 0.60. Below -> CONTROL BELOW GATE: "untestable by this method at this N",
target not decoded (family_run.py's control-first order). At or above -> target decoded; its decode is judged with
`tools/judge_plaintext.py` against it21news and reported PASS/FAIL as such (a decode is not a reading).
The oracle number is descriptive: if the oracle itself is below 0.60, the design is unreadable at this N even with the key,
whatever any solver does.

Also run (test 2 era rerun): `test2_xs_segmentation.py --corpus tools/data/it21news --designs L` -- PREREG-test2.md's design-L
statistic, null and power gate unchanged, only the reference corpus swapped; reported beside the it19 numbers.

Corpus reliability (rule 3 fold-count paragraph): `tools/judge_plaintext.py --holdout` over the five it21news folds at N=114 and
N=300, per-fold spread reported with the blend.
