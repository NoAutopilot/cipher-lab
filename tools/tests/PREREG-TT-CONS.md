# PREREG TT-CONS -- tools/decode_key.py --consistency (Tomokiyo practice 16, breaking.htm)

Written 8 Oct 2026, 22:5x UTC (date -u), before tools/tests/consistency_control_tt_cons.py was run.
Disclosure: one development smoke run of `--consistency --lexicon en` on the breaking.htm fixture (true key only) was
seen at about 22:47 UTC before this file was written (it showed 9 and 24 both in >=2 unrelated lexicon words). The
breaking.htm known-answer line below is therefore NOT blind; the null lines and both repo-key cases are.

Script: `python3 tools/tests/consistency_control_tt_cons.py` (offline). Lexicons: en (breaking.htm), es (rah-canada-1869),
de (nla-heinrich-braunschweig-1519, both jobs).

Pass lines:
1. Known answer (breaking.htm, Tomokiyo's 9(W) and 24(O)): both codes category `multi` (>=2 unrelated lexicon words).
2. Wrong value, every case: the true value of the named mid-frequency letter code (breaking: code 14 = d, x23; repo cases:
   the median-frequency letter code) has a lexicon stem count strictly higher than every one of the wrong letters
   (rank 1), and the wrong-letter median is at most a third of the true count.
3. Random key, every case: mean `multi` share over 20 seeds <= 0.20, and the true key's share >= 0.60 (breaking, canada).
   nla-heinrich is short (89-101 signs) and 1519 German spelling is far from the de corpus: its true-key share is reported,
   not gated; its null line still applies.
A case failing line 2 or 3 ships the option as grade `weak` with "controlled-only: failed ..."; if line 1 holds and 2-3 hold
for breaking and canada, grade `proven` is claimed only for "a reading with a word separator and an era-matched lexicon".

Why the nulls can fail differently from the target (rule 3): the statistic counts words found in the lexicon, and both
nulls change the values that make up those words, so a wrong or permuted key can (and should) lose words; a shuffled-order
null was not used because word membership for a fixed key would not change in a way that tests the values.
