# PREREG-MCC-SKEL (15 Oct 2026, 02:4x UTC by date -u; pushed before any seed 1-3 control score or any target score)

Worker MCC-SKEL (account 1, LANE DEFAULT-A1-0206-15). Instrument named by MCC-WORD (NOTES.md, 14 Oct): an abbreviation /
consonant-skeleton constrained code-word model, where the code's own letters are the evidence (each code segment may stand
only for words whose skeleton it is), unlike the two context-only instruments (char-4-gram, word-bigram) that failed their
own controls. Option on the existing instrument (Usage 8): `specs/cheap-tests/mccormick-1999/token_anneal.py --skeleton
--scheme drop|keepfinal --pool 3000 --n-list 132,500,2000 --seeds 1,2,3 --nulls 40 [--target]`; offline test
`tools/tests/test_mcc_skeleton.py`.

## Design (fixed now)
- Skeleton of a word: upper case, first letter kept, every later vowel (AEIOU) dropped, runs of one letter collapsed
  (would -> WLD). Two arms: `drop` (as stated) and `keepfinal` (also keeps a word-final vowel: house -> HSE), the second
  because 69% of the target's code tokens end in E.
- Decoder: lattice Viterbi; each code token is segmented into one or more skeletons (no word crosses a token boundary);
  a segment is read as a pool word with that skeleton (at most 10 per skeleton, most frequent first) or as UNK at 3.0
  nats per letter; path score = whole-word bigram LM (MCC-WORD's WordBigram, Jelinek-Mercer 0.8, closed vocabulary = top
  3,000 words of the held-out LM corpus tools/data/en/ Pride + Gatsby + Huck Finn); numbers and single letters are BND.
  Beam 200 previous-word states per position.
- Matched control (rule 3): a contiguous word stream from the `en` judge corpus (Holmes + Moby-Dick; held out from the
  LM) on the target's own per-position kind sequence (116 code / 14 number / 2 letter of 132), tiled to N; each code slot
  carries a word's skeleton, and with probability p_join the next word's skeleton is written onto the same token. p_join
  is fitted on the generator alone (grid 0-0.90, 2,000 tokens, rng 7) to the target's mean letters per code token (6.47):
  drop 0.55 (control 6.20), keepfinal 0.50 (6.28). N = 132 (the target's own), 500, 2,000; seeds 1, 2, 3 (rng 1000+seed).
- Generator-only diagnostics at N = 132 (no decode), seeds 1/2/3:
  drop: mean letters 6.02/5.63/6.98, type/token 0.888/0.862/0.853 (target 0.853), E share of letters 0.003/0.008/0.007,
  final-E share of tokens 0/0/0, truth words in the 3,000 pool 0.815/0.783/0.773.
  keepfinal: mean 6.38/6.17/6.57, type/token 0.888/0.922/0.836, E share 0.062/0.066/0.063, final-E 0.216/0.155/0.181,
  in pool 0.816/0.770/0.755.
  Target: E share of code letters 0.176, vowel share 0.244, final-E 0.690. The control matches N, the kind sequence,
  type/token ratio and token length; it cannot match the target's E profile under either scheme -- that mismatch is a
  property of the hypothesis (an English skeleton does not produce 69% final E), stated here before any score.
- Nulls, each able to differ from its comparison on its own statistic:
  (a) control read: the control's code tokens (with their truth) shuffled in ORDER among the code slots (rng 2000+seed);
      word recovery reads context, so order can move it.
  (b) coverage / score-per-letter (control power and target): all code letters permuted across the code tokens, each
      token keeping its length (40 shuffles); coverage and the LM score depend on which letter strings exist, so a
      letter shuffle can move them (an order shuffle could not move coverage: AX-5799 / bCAS lesson).

## Criteria
- Control reads at N (per arm): word recovery (per-token LCS of truth and decoded words / truth words) mean over 3 seeds
  >= 0.5 AND every seed above the order-null maximum at that N. Coverage power: control coverage above its own
  letter-null maximum on every seed at N = 132 (reported; the positive control at the target's own N, ARM3-ADJ lesson).
- Target run (per arm) only if that arm's control reads at N = 132. Target statistics: coverage (share of code letters
  read as pool words, not UNK) and LM score per code letter, each against the target's own 40 letter-shuffled nulls.
- Outcome wording, fixed now, per arm:
  * control reads at no N <= 2,000 -> "untestable by this instrument at N <= 2,000"; no target run.
  * control reads only above 132 -> skeleton family `too-short` at 132 tokens for this instrument; no target run.
  * control reads at 132, target coverage AND score-per-letter both above their letter-null maxima -> "the target's
    letters fit an English <arm> skeleton scheme beyond its letter-shuffled null"; the decode is a candidate, not a
    reading (rule 10), owed a judge run and an eye on the segments; graded M at best.
  * control reads at 132, target at or below either letter-null maximum -> "the target's code letters are not
    distinguishable from their own letter shuffle under the <arm> skeleton scheme": a control-backed negative for this
    scheme (vowel-dropped English skeletons with run-on groups, 3,000-word pool), not for abbreviation codes in general
    (Gregg-style or idiosyncratic abbreviation lexicons stay untested).
- Two arms are a multiplicity of two; with 40 nulls, "above the maximum" is p < 1/41 per arm.
- Development runs before this file, disclosed: dev seed 9 at 132, drop arm, 3 letter nulls (control word recovery
  0.808, order null 0.711, coverage 0.871 vs letter-null max 0.245); generator-only diagnostics above. Seeds 1-3 not run;
  the target not run.
- The target stays `open` (rule 5) whatever the outcome.
