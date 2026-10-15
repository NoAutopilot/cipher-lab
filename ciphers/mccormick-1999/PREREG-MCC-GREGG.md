# PREREG-MCC-GREGG (15 Oct 2026, 08:5x UTC by date -u; pushed before any control seed 1-3 or target score)

Worker MCC-GREGG (account 1, LANE DEFAULT-A1-0740-15). Step named by MCC-SUFX and MCC-JUDGE: the suffix-mark model with a
period shorthand lexicon in place of the plain-English pool, with its matched control and the MCC-JUDGE nulls.

## Rule 3 check (written before any score)
- Not a re-tune after a failed gate: MCC-SUFX's control read at N = 132 and its target beat its type and type-mark nulls;
  MCC-JUDGE's NCBE-fixed null did not remove the margin. The third-attempt clause (a third try at an approach that keeps
  failing its own gate) does not apply.
- What changes is the material, not a setting: the candidate word list. MCC-SUFX's pool was the 3,000 most frequent words
  of three 19th/20th-century novels (Pride and Prejudice, Gatsby, Huck Finn). Here the pool is restricted to words of a
  period shorthand lexicon never used on this target: John Robert Gregg, Gregg Shorthand Dictionary (1916; public domain;
  IA greggshorthanddi0000john_c6j8, about 17,000 entries, OCR headwords 14,565) plus the 208 word-signs (brief forms) of
  the Gregg Shorthand Manual (1916; IA greggshorthanda00greggoog, par. 61 key list), union 14,630 words
  (`families/gregg/build_lexicon.py`, OCR repairs fixed in that file). The decoder, LM, marks, classes and nulls are
  MCC-SUFX's, unchanged (disclosed: the instrument is the same; this tests the lexicon).
- Measured before any score (lexicon only): the Gregg pool shares 2,241 of its 3,000 words with MCC-SUFX's pool; 759 plain
  words drop out (had, him, said, got, came, saw, two, old, the novels' names, contractions) and 759 Gregg-admitted words
  enter. Share of the control text's tokens that are in the pool: plain 0.801, Gregg 0.739.
- What the Gregg dictionary does NOT give: Gregg outlines are pen strokes, not letters; nothing here maps a word to its Gregg
  outline. This variant asks only whether the target's stems fit a shorthand writer's VOCABULARY better or worse than a
  novel's, under the same letter-skeleton + mark coding.

## Design (fixed now)
- Pool: the top 3,000 words of the MCC-SUFX LM corpus (Pride + Gatsby + Huck Finn) that are in the lexicon or whose regular
  lemma is (`token_anneal.lexicon_lemmas`: -s, -es, -ies>y, -ed, -d (as -ed>e), -ied>y, -ing, -ing>+e, -ly, -ily>y, doubled
  final consonant undone after -ed/-ing). Same WordBigram LM (words outside the pool are UNK), alpha 3.0, beam 200, marks
  '', E, SE, BE, 11 classes, coordinate-ascent map fit from starts '' and E.
- Matched control (rule 3): MCC-SUFX's generator unchanged -- held-out Holmes + Moby-Dick prose on the target's kind sequence
  (116 code / 14 number / 2 letter), planted map and p_join 0.45 from fit_true_map, N = 132 (the target's own), seeds 1, 2, 3
  (rng 1000+seed), K = the control's own type count as generated. The control text is NOT filtered to the lexicon: words
  outside it cannot be read, which is the cost the lexicon carries on real prose (pool ceiling 0.739 of tokens).
- Command: `python3 specs/cheap-tests/mccormick-1999/token_anneal.py --sufx --lexicon
  ciphers/mccormick-1999/families/gregg/gregg1916_lexicon.txt --pool 3000 --n-list 132 --seeds 1,2,3 --nulls 40
  --target-nulls 200 --procs 4 --target --out ciphers/mccormick-1999/families/gregg/gregg.json`, then
  `python3 ciphers/mccormick-1999/families/judge/ncbe_null.py --lexicon ciphers/mccormick-1999/families/gregg/gregg1916_lexicon.txt
  --kinds ncbe --draws 200 --procs 4 --out ciphers/mccormick-1999/families/gregg/ncbe_gregg.json`.
- Nulls on the target, map re-fitted on every draw, 200 draws each: (a) type null (seeds 5000-5199), (b) type-mark null
  (6000-6199), (c) NCBE-fixed type-mark null (MCC-JUDGE's `ncbe`, seeds 7000-7199). Each can differ from the target on
  coverage and score per letter (they change the stem letters: 678 of 750 code letters for (c)).

## Criteria (fixed now)
- Control reads at N = 132 iff, on 3 seeds: word recovery mean >= 0.5; mark-map recovery >= 0.8 on every seed; control
  coverage above its own type-mark null maximum (40 draws) on every seed. If not: "not run on the target: the Gregg pool
  does not read its own control at 132" (no target run, no N = 500 rerun in this job), logged untested-by-this-tool.
- Target (only if the control reads): statistics coverage (C) and LM score per code letter (S); p = (1 + draws >= target) /
  201 against each of (a), (b), (c).
  * C and S above the maximum of all three -> "under a Gregg 1916 lexicon the target's stems still fit the suffix-mark
    scheme beyond the type, type-mark and NCBE-fixed nulls": a candidate, not a reading (rule 10), M at best;
  * above (a) on both but p >= 0.05 against (b) or (c) on both -> "under the Gregg lexicon the stems do not fit beyond a
    mark-keeping (or NCBE-keeping) shuffle": a control-backed negative for this lexicon under this scheme only;
  * anything else -> "mixed".
- Comparison with the plain pool (descriptive, no verdict word): the standardized margin z = (target - null mean) / null SD
  against the type-mark null (b), Gregg pool vs MCC-SUFX's plain pool (the plain figures from MCC-JUDGE's 200-draw `tm`
  null, ncbe_null.json). "fits the Gregg lexicon better" is said only if z_Gregg > z_plain on BOTH C and S; "worse" only if
  lower on both; otherwise "no difference in kind". Raw coverage is not compared across pools (different ceilings).
- Judge: tools/judge_plaintext.py on renderings A and B of the Gregg target decode beside the same renderings of draws 6000
  ((b)) and 7000 ((c)), as MCC-JUDGE; a PASS on a shuffle voids the judge for this family at this N. The `en` corpus spread
  (0.44-0.64) makes any PASS/FAIL of unknown reliability; expected: FAIL.
- No development run of the target or of seeds 1-3 under the Gregg pool was made before this file. The target stays `open`
  (rule 5) whatever the outcome; no word of any decode is offered as a reading.
