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

## Result (run 8 Oct 2026, 22:49 UTC by date -u; re-run after the word-code fix at about 22:51, numbers unchanged)

| case | true key multi | named codes | wrong value (code: true stems vs wrong median/max, rank) | random key multi, mean/max of 20 | lines |
|---|---|---|---|---|---|
| breaking.htm (Tomokiyo), en | 22/25 = 0.880 | 9 multi (7 stems: with, few, afterwards, which, we, well); 24 multi (20 stems: of, you, to, hook, officers, aboue) | 14=d: 13 vs 1.0/4 over 23 letters, rank 1 | 0.066 / 0.200 | 1 pass, 2 pass, 3 pass |
| rah-canada-1869 (C key), es | 21/28 = 0.750 | - | [g02]=g: 5 vs 1.0/3, rank 1 | 0.214 / 0.321 | 2 pass, 3 FAIL (0.214 > 0.20) |
| nla-heinrich 548 (H key), de | 4/19 = 0.211 | - | 9=s: 0 vs 0/0, rank 19 | 0.000 / 0.000 | 2 FAIL (no de lexicon stems at all) |
| nla-heinrich 562 (H key), de | 0/16 = 0.000 | - | 17=o: 0 vs 0/0, rank 16 | 0.000 / 0.000 | 2 FAIL |

Without a lexicon the true-key multi share is 0.880 / 0.893 / 0.737 / 0.750: every code a reading uses in several places
comes out multi whether or not its words make sense, which is why the lexicon is the part that can fail.
Verdict by the lines above: shelf grade `weak`, evidence "controlled-only: failed ..." -- the known answer holds and the
wrong-value null separates sharply where the lexicon covers the language (en, es), but a short-word language passes random
keys at about 0.21, and a lexicon far from the reading's spelling (1519 German against de) gives no signal at all.
Next fix, not made here: a minimum word length (3+ letters) for a lexicon hit, and an era-matched lexicon per target.
