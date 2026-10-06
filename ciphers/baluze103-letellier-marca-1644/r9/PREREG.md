# PREREG -- R9-BAL103: a context rule for the ambiguous sign 9 (i|r|s), written and pushed before any rule output is computed

Worker R9-BAL103 (account 1, LANE LANE-RUN9-account-1), 6 Oct 2026, written 05:5x UTC by `date -u`.

Disclosure: calib/sign_table.tsv (R7C-BAL103K) already shows the 3 aligned letters of 9 on f.171r (s, s, i). So calib/ alone
cannot be a blind test at N=3; it is reported, and a held-out known-answer control at matched noise carries the gate.

Rule (fixed here, no tuning): for each token whose value is i|r|s, choose v in {i, r, s} maximising the sum of log10
P(letter | 3 previous) over the 4-grams of fr17 (tools/judge_plaintext.py's NgramModel, n=4, k=0.01) that contain v, in the
window of the 3 decoded letters left and 3 right of it on the same line (first value of each a|b, U and '?' dropped, word codes
expanded to their letters). Ties -> s. Training corpus for the control: fr17 minus lettresducardina01maza (held out); for the
calib and f.50 application: all of fr17.

Control A (known answer, can fail: the rule can lose to a constant): 2,000 positions drawn (seed 1644) from the held-out
Mazarin t.1 text where the true letter is i, r or s; the context letters get uniform random substitution noise at 0, 15, 27 and
35% (bracketing f.50's ~25-30% measured sign error, r8/result.tsv). Report rule accuracy, the best constant baseline (always the
commonest of i/r/s in the held-out text) and uniform random (1/3).
Control A' (shuffled model, varies on the same axis -- context information): same rule with an NgramModel trained on the same
corpus letter-shuffled; it must fall towards the constant baseline. If it does not, the control is void and so is the gate.
Control B (real, descriptive): the 3 occurrences of 9 in calib/f171r_passA.tsv decoded with key_decode.tsv (c = q as in
calib.py's registered test) vs their calib/sign_table.tsv letters: k/3.

Gate (rule licensed for f.50): Control A at 27% noise beats the best constant by >= 10 points AND beats A' by >= 10 points AND
Control B >= 2/3. Otherwise: logged as a FAIL, no change to f.50.
On PASS: the 42 f.50 tokens get the rule's letter as first value through exceptions.tsv (value v|others, grade M -- no grade
upgrade, the rule is a lean, not a reading), decode_key --check, fr17 judge. As in r8b/PREREG.md the change stays only if the
judge is not below the current -1.537; else exceptions.tsv is removed and the result logged. The judge for i-first (current), all-s
and the rule is reported either way (descriptive).
