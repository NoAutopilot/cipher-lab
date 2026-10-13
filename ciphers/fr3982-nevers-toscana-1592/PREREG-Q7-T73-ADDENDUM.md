# PREREG addendum: key no.73 on f.25 (lane BNF-FOCUS, account 2), written 13 Oct 2026 13:3x UTC by date -u,
# BEFORE any target score under no.73 exists and BEFORE f.25's transcription error is measured.

Facts at writing:
- BNF-Q7-T73 validation of q7test/screen.py with key_no73.tsv (matched no.73 controls, 100 texts, 100 nulls each):
  power 0.99 at 0% and 0.53 at 10% digit error; false detect on a no.46 text 0.00. Target not run (gate 0.8 at 10% failed).
- Lane run (same script, unchanged; q7test/s73_power_curve.out): power 1.00 at 3%, 5% and 7%.
- f.25 transcription: two blind passes agree 0.905 (BNF-Q7-KEY). That is agreement, not the reconciled text's error.

Rule fixed now (CLAUDE.md rule 3: the control's error band must bracket the target's measured error):
1. f.25's reconciled digit error e is measured by an independent reading (BNF-Q7-ERR): a third blind digit pass at native
   crops by a reader that has not seen ciphertext.tsv, scored against ciphertext.tsv digit by digit after alignment;
   e_hi = upper bound of the 95% Wilson interval on the disagreement share, counting every disagreement as an error of
   the reconciled text (conservative).
2. The target run under no.73 is licensed only if e_hi <= the largest validated level L with power >= 0.8, where the
   validated levels are 0, 0.03, 0.05, 0.07, 0.10 (L = 0.07 at writing). If e_hi > L, the run stays a NON-TEST and the
   next step is a better transcription, not a looser gate.
3. If licensed: one run, `screen.py target --key q7test/key_no73.tsv --lang it --nulls 1000` (seed as in the script), fit
   as screen.py defines it (beats every null in both families). A fit goes to a separate verifier; nothing above grade M.
