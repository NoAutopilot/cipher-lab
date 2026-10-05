# PREREG N9-GRAZ (5 Oct 2026, written 05:2x UTC before any z crop is cut or looked at)

Job: LANE-NEAR9 wave 1 N9-GRAZ (`.claude/briefs/runs/2026-10-05-ytbiz-near9-wave1.md`). Question: the sign the readers label
`z` (key.tsv `z A H`, Tomokiyo a row 3) aligns to R in 23 of 26 fr.3040 no.6 occurrences against Le Grand III (N8-GRA2 3/3,
N8-GRA3 20/23). Is it two signs, one sign with a key error, or one sign with two values?

## Material
- fr.3040 no.6: every token reconciled as `z` in `n8gra2/recon.tsv` (rows f18r_L01-L10) and `n8gra3/recon.tsv`, with the print
  letter it aligns to under the registered aligner (`n8gra2/score.py` align_agree, same normalisation), recomputed by script.
- f.30: every `z` in `ciphertext_f30.tsv` (43); f.29r: every `z` in `ciphertext.txt`.
- Key tables on disk: Tomokiyo `sources/cryptiana/web/francisGramont.png` (a row 3 z-shape; R rows), Lasry
  `sources/cryptiana/web/GL/BnF_fr3071_f17.png` (A and R columns).
- Strips: one per occurrence, cut from the committed half-line crops by proportional position (the A2-GRA3 method,
  `split_shapes_crops.py`), +-3 sign widths, target column ticked; strips are shuffled and numbered with no line id, source, codes or
  value printed.

## Instrument
One Sonnet blind shape-sort call: all strips plus the key-table z/A cells and R cells (also unlabelled, mixed in). It is asked to sort
the ticked signs into shape classes (1-4) by visible features only and to flag strips where the tick misses a z-like sign
("off-target"). No values, no alignment, no source shown. Then this worker compares classes against (source, aligned print letter) and
eye-checks the class boundary on the strips.

## Outcomes (decided in this order)
1. **Two signs (split)**: the sort gives >= 2 classes among on-target fr.3040 strips AND class membership is associated with the
   aligned letter (R vs not-R) at Fisher exact p < 0.05 (two-sided), AND by this worker's eye the classes differ by a stated
   stroke feature. Then: the R-class is a separate sign; its key value is R at grade C (known plaintext, rule 4) if >= 4 of its
   aligned occurrences read R and none reads another letter except gaps; the A-class keeps `z A H`. f.30 z occurrences are
   assigned to classes by the sort, and the effect on f.30 is counted under that assignment.
2. **One sign, letter-specific value (homophone with two values)**: no split by (1), but on f.30 the value A beats R under
   the f.30 test below. Then key.tsv is unchanged for f.30 (its letter); the fr.3040 value is recorded in NOTES only.
3. **One sign, key error**: no split by (1), and on f.30 R beats A under the test below. key.tsv is then changed to `z R`
   only if R also ranks in the top 3 of the 23 letter values on f.30; grade S (cryptanalytic with control), never C, since the
   known plaintext is a different letter.
4. **Undecided**: none of the above (e.g. off-target strips > 25%, or on f.30 neither A nor R ranks top 3). key.tsv unchanged.

## f.30 test (outcomes 2/3, and the effect count for 1)
Decode f.30 with key.tsv as committed (`reading_f30_extended_tokens.tsv` values) and substitute every z (or every z of a class)
with each of the 23 letters A-Z less J/U/W (V for U); score each stream with the fr16 n-gram model used by
`tools/judge_plaintext.py` (its own scoring function on the joined letter stream). Report the rank of A and R. Control that can
differ: the same rank test for a sign whose value is known at H from both tables with a comparable count on f.30 (the H sign of
nearest frequency to z): its own value must rank top 3, else the test has no power at this N and outcome 4 applies.
Effect: list every f.30 word span (between NULL/space tokens in the reading) that changes letters between z=A and z=R.
