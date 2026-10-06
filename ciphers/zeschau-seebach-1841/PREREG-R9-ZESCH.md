# PREREG-R9-ZESCH: word-segmentation objective on pooled R5005+R5006+R5007 (6 Oct 2026, account-4, LANE-RUN9-account-4)

Written and pushed 6 Oct 2026 before any control accuracy or target statistic was computed. The only run before this
file is `wordseg_syllabary.py --time` (objective speed on a random key, no accuracy computed).

## Duplicate-effort check (done first)
Sparse clone of github.com/dbourdeau/cyphersolver, HEAD adbf9a1 (5 Oct 2026 21:27 -05:00), `targets/zeschau1841/` read by
grep, deleted after. His NOTES.md still says "R5006-R5008 are not transcribed yet"; his "What would move it" item 4 is "a
syllabary annealer with a proper French/German syllable model". He has run free-syllable and length-neutral syllabary
annealers (syll.py, syll2.py, syll3.py: "still no French") and no word-segmentation objective. Not run or published by
him, so the job proceeds.

## Why this is a different instrument (rule 3 third-attempt clause)
GAPS202's two attempts scored the decode's letters with a 4-gram model; both times the control's annealer found keys
scoring above the true key (the objective, not the search, failed). This job changes the objective, not a knob of it:
- **Score = word parse, not letter n-grams.** Each decode chunk (20 code tokens) is parsed by Viterbi into dictionary
  words from a word-unigram model (words seen >= 2 times, length <= 14); a letter left unparsed costs its unigram
  log-probability plus a fixed penalty of -2.0 (log10). The chunk score is that best parse minus the letter-unigram
  background of the same string: a log-likelihood ratio, so a longer decode is not rewarded or punished for its length
  as such, only for how much of it parses into words.
- **Injective key.** One code per unit (a move that takes a unit already held by another code swaps them), matching the
  control's one-code-per-unit design; GAPS202 allowed many codes to share a unit.
- **Era/register corpus:** French word model from `tools/data/fr1810` (Napoleonic official correspondence 1800-1811,
  diplomatic/official register, about 30 years before the 1841-42 letters; nearer than fr19's novels). German from
  `tools/data/de19` (1816-17 travel letters + 1814 novella), the only 19th-century German on disk; R5007 (German) is
  475 of the 2,666 tokens. Neither is Saxon diplomatic 1840s prose.

## Matched control (runs first)
GAPS202's construction unchanged in design: the pool as parsed (R5005 1,846 pairs by Bourdeau's phases, R5006 345,
R5007 475 = 2,666 tokens; K = 98 codes), a synthetic one-code-per-unit syllabary of the same K (26 letters + Bourdeau's
4 multi-letter pin units + the commonest training bigrams/trigrams), held-out text (fr1810 `lettresindites01napo`,
de19 `pg31538`) at each segment's token count and language, 1 pct digit errors, the 7 pin units fixed as Bourdeau's 7
are in the target. Same 277-unit search inventory. Seeds 2091, 2092, 2093; 2 restarts x 50,000 moves each; T 2.0 -> 0.05.
- Statistic: token accuracy over non-pin tokens (decoded unit == true unit).
- **Gate: mean token accuracy over the 3 seeds >= 0.60** (GAPS202's gate).
- Ceiling check: this design read 0.032 and 0.000 under GAPS202's objectives, so it is not at ceiling and can fail;
  token accuracy depends on the key the search returns, which the objective changes (not orthogonal).
- Diagnostic reported beside it: the true key's objective value vs each seed's best (if the annealer beats the true key,
  the objective is what fails, as in GAPS202).

## Stop rules
- Control mean < 0.60: CONTROL BELOW GATE; the target is not run; logged "untested-by-this-tool at this N" in
  HYPOTHESES.md (no further tuning of this objective in this job: no addendum, no second attempt).
- Control >= 0.60: run the target with the same seeds and settings, and the digit-shuffled target (shuffled within each
  letter, re-paired at phase 0) through the identical objective (rule 3 ARM-C1). Report the target's best J beside the
  shuffled target's; report the decode only as a candidate, every token M at most (no H/C/S without a verifier), and
  judge it with `tools/judge_plaintext.py` (fr1810) beside the shuffled decode.
- Cap 4 USD, box 06:02-07:12 UTC (80% 06:58): a run that cannot finish by 06:58 is not started.
