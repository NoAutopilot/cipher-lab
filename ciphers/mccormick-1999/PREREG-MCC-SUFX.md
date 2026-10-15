# PREREG-MCC-SUFX (15 Oct 2026, 05:4x UTC by date -u; pushed before any seed 1-3 control score or any target score)

Worker MCC-SUFX (account 1, LANE DEFAULT-A1-0447-15). Instrument named by MCC-SKEL's Verdict: a suffix-aware abbreviation
model with an ending-matched control and a repeated-type-keeping null. Option on the existing instrument (Usage 8):
`specs/cheap-tests/mccormick-1999/token_anneal.py --sufx --pool 3000 --n-list 132 --seeds 1,2,3 --nulls 40 --procs 3
[--target]`; offline test `tools/tests/test_mcc_sufx.py`.

## Why this is a different instrument, not a knob on MCC-SKEL (rule 3, third-attempt clause)
MCC-SWEEP (char-4-gram anneal) and MCC-WORD (word-bigram anneal) read context only; MCC-SKEL read the code's letters as
fixed consonant skeletons, with the final E either dropped or treated as the word's own last letter. All three have no free
parameter tied to the endings. MCC-SUFX treats the recurring token endings as a closed set of MARKS (SE, BE, E, none) whose
meaning is a latent class -> mark map fitted per text, one consistent meaning per mark across every token: the
evidence is the cross-token consistency of that map, the parameter the instrument must recover on its control. The
control is built to match the target's ending profile (impossible for MCC-SKEL's design, its PREREG says so), and the
nulls keep the target's repeated types (NCBE x11 stays one type) and, in the sharper one, each type's mark, so the
question asked is whether the STEMS read beyond chance once the endings and the repetition structure are given. Shared
with MCC-SKEL, disclosed: the drop-skeleton of the stem, the lattice Viterbi segmentation, the word-bigram LM and the
3,000-word held-out pool. If this instrument's control fails, the skeleton-lattice line on this target is logged
retired-for-this-hypothesis (untested-by-this-tool), and the next step needs a different instrument or new material.

## Design (fixed now)
- Word -> (base, class) by fixed rules, longest first: -ing (len >= 5), -ed (>= 4), -ly (>= 4), -es / -s (not -ss) as
  class s, then the single final letter e / y / d / t / n / r (len >= 2); otherwise class `other` (base = whole word).
  11 classes. Code string of a word = drop-skeleton of the base (first letter + consonants, doubles collapsed) + the
  class's mark. Marks = the target's token-final endings of length 1-2 seen >= 10 times (E 80, SE 42, BE 15) plus no
  mark: SUFX_MARKS = '', E, SE, BE.
- Decoder: MCC-SKEL's lattice Viterbi (UNK 3.0 nats/letter, beam 200, <= 10 pool words per code key) with the key of each
  pool word = its sufx code under the map being tried. The instrument fits the map by coordinate ascent on the decode
  total (each class tried at each mark, up to 3 passes, two starts: all '' and all E; best total kept). The same fit runs
  on the control, the target and every null.
- Matched control (rule 3): held-out prose (the `en` judge corpus Holmes + Moby-Dick; LM from Pride + Gatsby + Huck Finn)
  on the target's own kind sequence (116 code / 14 number / 2 letter of 132), each code slot a word's sufx code, run-on
  groups with probability p_join. The planted map is fitted on the generator alone (no decode): every one of the 4^11
  maps scored by the L1 distance between the control's token-final mark profile (class shares of 2,000 tokens, rng 7)
  and the target's; then p_join (grid 0-0.90) on letters per code token. Result (generator only):
  planted map ing '', ed E, ly E, s SE, e SE, y SE, d BE, t E, n BE, r E, other ''; control mark profile realised
  '' 0.302 / E 0.194 / SE 0.362 / BE 0.142 vs target 0.310 / 0.198 / 0.362 / 0.129; p_join 0.45, letters per code token
  6.51 vs target 6.47. N = 132 (the target's own), seeds 1, 2, 3 (rng 1000+seed).
- Nulls (each can differ from its comparison on its own statistic: coverage and score depend on which stem strings exist,
  and both shuffles change the stem strings; neither changes N, token lengths or the type/token structure):
  (a) type null: the letters of the distinct code TYPES permuted across types, each type keeping its length, every
      occurrence of a type rewritten with its type's new string (repeated types stay repeated);
  (b) type-mark null: as (a), but each type keeps its final mark (longest of SE / BE / E) and only the letters before it
      are permuted. 40 shuffles each; the map is re-fitted on every null.

## Criteria
- Control reads at N = 132 iff, on 3 seeds: word recovery (per-token LCS of truth and decoded words / truth words) mean
  >= 0.5; mark-map recovery (share of truth words whose class gets its planted mark under the fitted map) >= 0.8 on every
  seed; and control coverage above its own type-mark null (b) maximum (40) on every seed (power at the target's own N,
  ARM3-ADJ lesson). No order null (MCC-SKEL addendum 1: an order shuffle cannot test letter-carried recovery).
- If the control does not read at 132: one run at N = 500 (3 seeds, 10 nulls) only to separate `too-short` from
  `untestable by this instrument`; no target run either way.
- Target run only if the control reads at 132. Statistics: coverage (share of code letters read as pool words) and LM
  score per code letter, each against nulls (a) and (b) (40 each, maxima). Fixed wording:
  * all four above their maxima -> "the target's stems fit the suffix-mark scheme beyond both type-keeping nulls": the
    decode is a candidate, not a reading (rule 10), owed a judge run and an eye on the segments; graded M at best;
  * above (a) on both but not above (b) on either -> "the target's endings and repetitions carry the fit; its stems do not
    read beyond a mark-keeping shuffle": a control-backed negative for the stems under this scheme (this class set, these
    marks, drop-skeleton stems, 3,000-word pool), not for abbreviation codes in general (Gregg-style lexicons untested);
  * at or below (a) on both -> "not distinguishable from its own type-keeping letter shuffle under this scheme";
  * any other split is reported as mixed, with no wording stronger than "mixed".
- Two statistics x two nulls; with 40 nulls, "above the maximum" is p < 1/41 per comparison.
- Development runs before this file, disclosed: generator-only fit above; dev seed 9 at N = 132 with 3 type-mark nulls:
  fitted map = planted map, mark-map recovery 1.000, word recovery 0.780, coverage 0.901 vs null max 0.481. Seeds 1-3 not
  run; the target not run.
- The target stays `open` (rule 5) whatever the outcome.
