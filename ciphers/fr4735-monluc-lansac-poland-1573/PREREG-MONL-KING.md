# PREREG MONL-KING step 1 placement test (20 Oct 2026, written and pushed before king_f166.py was run)

Question: is f.166r-v (aid item 66, "La premiere lettre est un dechiffrement ... Varsovie, 2 mai 1573", to the king; clear, with a
decipherer's strike-outs; dated "De Varsouie ce ii de May 1573") the decipherment of the king's cipher letter ff.132-136?
Why it is the candidate: the brief's items 17/18 (Monluc to the palatine of Sandomir and to "Sr Andreas", fol. 42-43, 1572) and
112-120 (Gilles de Noailles from Constantinople, 1577, fol. 266-272) cannot be a 28 Apr 1573 letter to the king by the aid's own
wording (sources/bnf-findingaids/2026-10-09/cc57784f.html); item 66 is the only Monluc "dechiffrement" to the king near that date.
Prior against: f.166 opens "Sire il y a huict iours que nous commencasmes a faire ceste depesche", f.132 opens in clear "Sire Nous
sommes si pres de voir le bien ou le mal de ma longue negotiation" -- different openings, so at best f.166 deciphers part of it.
Inputs: the existing blind reads leaf/passes/c258_read.tsv (f.133 L01-L02) and c264_read.tsv (f.136 L01-L02), MONL-LEAF, unchanged;
clear_f166.tsv (one reading pass by this worker from openapi.bnf.fr f316/f317 at 2800 px; single pass, MK1).
Statistic: align_c268.py's DP (key.tsv, local span of the whole clear letter, free start/end) -> confirm share of keyed tokens;
and the longest exact run of decoded letters inside the clear letter. Null: 200 word-shuffled copies of the same clear letter
(seed 166), p95. Positive control (same statistic, same code): c269_read.tsv against the whole ff.140r-141r letter, where its true
place is known (f.140r L26-L27, MONL-C269A); f.166 itself as a wrong-letter control for c269.
Gate: a read is placed in f.166 when its confirm-share margin over p95 >= 0.10 AND its exact run exceeds the null max -- and only if
the positive control (c269 vs f.140) meets the same two conditions; if the control fails, the test is a non-test (rule 3).
Decision: either read placed -> f.166 is (part of) the king's letter's decipherment: known text, stop. Neither placed with the control
passing -> f.166 is not the decipherment of f.133/f.136's first lines; go to brief step 2.
