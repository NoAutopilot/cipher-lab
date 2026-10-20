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

## Decision
(Block appended after the run: the PREREG pushed at fb5e20b84 lacked it; Belief and Would change restate the pre-run text above.)
Belief: f.166 is a separate 2 May letter to the king, not the decipherment of ff.133/136 (different opening from f.132).
Would change it: c258 or c264 placed in f.166 (confirm-share margin >= 0.10 over p95 AND exact run > null max), with c269 vs f.140 meeting the same.
Observed: positive control c269 vs f.140: margin +0.035 (0.535 vs p95 0.500), run 14 vs null max 10 -- share clause FAILS, run clause passes; c269 vs f.166 (wrong letter): -0.069, run 7 vs 8. Targets vs f.166: c258 margin 0.000, run 6 vs null max 8; c264 margin -0.088, run 10 vs null max 10 (tie; the run is "pourlemoin", f.166r L19 "pour le moings", a stock phrase). Registered conjoint gate: non-test (control below gate). Post hoc, run clause only (control passes it): neither target placed.
Decision: change -- the two-line whole-letter test cannot settle f.166 either way; a 10-line decode of f.133 (brief step 2) placed against both f.166 and f.140 is the test that can.
Lesson: at two lines (~60-75 tokens) against a ~3,000-letter whole clear letter, confirm share under align_c268.py's local DP has no headroom over word-shuffled copies even at a true placement (+0.035); the exact-run statistic separates (14 vs max 10); gate whole-letter placement on the run, or read more lines.
