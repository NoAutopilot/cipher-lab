# PREREG-MCC-CMU (15 Oct 2026, 12:0x UTC by date -u; pushed before any control seed 1-3 or target score)

Worker MCC-CMU (account 1, LANE DEFAULT-A1-1140-15). Step named by MCC-GREGG's Verdict: the phonetic-skeleton variant of
the suffix-mark model, each word's code built from its pronunciation (CMUdict) instead of its spelling, with its matched
control and the three nulls of MCC-GREGG.

## Rule 3 check (written before any score)
- This is the third lexicon / key-function on the same suffix-mark instrument (plain pool MCC-SUFX, Gregg pool MCC-GREGG,
  phonetic key here). Under rule 3's third-attempt clause, fixed now: if the target does not beat all three null maxima on
  both statistics (the "candidate" row below), the suffix-mark family is logged [retired] in HYPOTHESES.md as
  "untested-by-this-tool" (not refuted), and no further lexicon or key swap on this instrument is briefed without new
  material or a different instrument.
- What changes: only `sufx_key`'s base skeleton (spelling -> sound). Decoder, LM, pool (MCC-SUFX's plain top-3,000, no
  lexicon filter), marks, classes, map fit, control generator and nulls are MCC-SUFX's / MCC-GREGG's, unchanged.

## Skeleton mapping (fixed now; `token_anneal.phon_skeleton`, `--phonetic`)
- Dictionary: CMUdict (BSD; raw.githubusercontent.com/cmusphinx/cmudict master, 135,166 lines, sha1 2619f7ef5e6d...,
  fetched 11:58 UTC), first pronunciation only, stress digits dropped; committed subset `families/cmu/cmudict_subset.dict`
  (19,100 entries = every corpus word type found in it; `build_subset.py` regenerates it).
- Ending class: MCC-SUFX's `suffix_class` on the spelling (unchanged); the class's own phones are stripped from the end of
  the pronunciation first: ing [IH NG]; ed [IH D]|[AH D]|[D]|[T]; ly [L IY]; s [IH Z]|[AH Z]|[S]|[Z]; y [IY]; d [D]; t [T];
  n [N]; r [ER]|[R]; e and other: nothing.
- Each consonant phone written as its commonest English grapheme: P B T D, K->C, G, CH->CH, JH->G, F, V, TH/DH->TH, S,
  Z->S, SH->SH, ZH->S, HH->H, M, N, NG->NG, L, R, ER->R, W, Y; vowels dropped, except that a vowel-initial word keeps its
  first spelled letter; runs of one symbol collapsed (nice -> NS, city -> ST, know -> N, phone -> FN, walked -> WC).
- Out-of-dictionary words fall back to the letter skeleton of the base (pool OOV 3.1%: contractions, novel names; control
  OOV 1.4-7.9% of code words on seeds 1-3).

## Measured before any score (generator only, no decode)
- Planted map and p_join from `fit_true_map` (unchanged procedure): map identical to MCC-SUFX's (it depends only on the
  ending classes), p_join 0.45, control mean letters per code token 6.33 vs target 6.47; token-final mark profile
  none/E/SE/BE 0.302/0.193/0.363/0.142 vs target 0.310/0.198/0.362/0.129.
- Seeds 1-3 at N = 132: type/token 0.871/0.862/0.810 (target 0.853). Letter shares differ from the target, a property of
  the hypothesis stated now: the control writes H at 0.07-0.10 of code letters (TH digraphs), the target 0.005; N 0.05 vs
  0.117; P 0.01 vs 0.039; K 0 vs 0.013.
- Distinct base keys among the 3,000 pool words: phonetic 1,520, letter 1,644 (sound keys are more ambiguous).

## Design and criteria (fixed now; as PREREG-MCC-GREGG with the pool unfiltered)
- Commands: `python3 specs/cheap-tests/mccormick-1999/token_anneal.py --sufx --phonetic
  ciphers/mccormick-1999/families/cmu/cmudict_subset.dict --pool 3000 --n-list 132 --seeds 1,2,3 --nulls 40
  --target-nulls 200 --procs 4 --target --out ciphers/mccormick-1999/families/cmu/cmu.json`, then
  `python3 ciphers/mccormick-1999/families/judge/ncbe_null.py --phonetic ciphers/mccormick-1999/families/cmu/cmudict_subset.dict
  --kinds ncbe --draws 200 --procs 4 --out ciphers/mccormick-1999/families/cmu/ncbe_cmu.json`.
- Matched control: synthetic note of the target's 132 tokens (kind sequence 116 code / 14 number / 2 letter) from held-out
  Holmes + Moby-Dick prose written under the same phonetic suffix-mark model (planted map, p_join above), seeds 1, 2, 3
  (rng 1000+seed). Reads iff word recovery mean >= 0.5, mark-map recovery >= 0.8 on every seed, and control coverage above
  its own type-mark null maximum (40 draws) on every seed. If not: stop, "non-test: the phonetic key does not read its
  own control at 132", logged untested-by-this-tool; no target run.
- Nulls on the target (map re-fitted every draw, 200 draws each): (a) type null (seeds 5000-5199), (b) type-mark null
  (6000-6199), (c) NCBE-fixed type-mark null (7000-7199). Each changes the stem letters, so each can move coverage (C) and
  LM score per code letter (S). p = (1 + draws >= target) / 201.
- Margin rule: C and S both above the maximum of all three -> "under a phonetic (CMUdict) key the target's stems fit the
  suffix-mark scheme beyond the type, type-mark and NCBE-fixed nulls": a candidate, not a reading (rule 10), M at best.
  Anything else (at or below any of the six maxima) -> the family is [retired] as above; the wording is "negative" if
  p >= 0.05 against (b) or (c) on both C and S, else "mixed".
- Comparison with the plain letter key (descriptive): z = (target - null mean) / null SD against (b), phonetic vs MCC-JUDGE's
  plain 200-draw `tm` (C 6.43, S 4.31). "Better" only if higher on both, "worse" only if lower on both, else "no difference
  in kind".
- Judge: renderings A and B of the target decode and of draws 6000 and 7000 through `tools/judge_plaintext.py
  specs/mccormick-1999.json`; a shuffle PASS voids the judge for this family at this N. Expected FAIL; `en` spread 0.44-0.64.
- No development run of the control seeds or the target under the phonetic key was made before this file (the offline test
  uses a 20-word synthetic dictionary). The target stays `open` (rule 5); no word of any decode is offered as a reading.
