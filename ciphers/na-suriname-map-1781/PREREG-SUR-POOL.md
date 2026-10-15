# PREREG SUR-POOL (15 Oct 2026, account 2, LANE DEFAULT-A2-1109-15): [d-hook] = e anchor test pooled over 4.VEL 2046 + 2077

Written and pushed before any score; only `score_pool_dhook_vocab.py --dry` (vocabulary size, class counts, draw counts) has run.

**Question.** Do the 15 [d-hook] tokens on the 2046 and 2077 blocks (2046: No1:28, No1:49, No2:12, leg_d:24, :43, :57, leg_efgh:30,
:58, leg_ki:5, :24, all U; 2077: four U and L13:3, which reads e at grade C) read e as a class? SUR-2046A (15 Oct, PREREG-SUR-2046A.md,
8e1b31c8e) ran this instrument on 2046 alone and was a non-test (control gate 1/5: known values ranked first but under the ceil(n/2)
floor). Its named next is this pooled run. **This is the second attempt of the instrument**: new material only, nothing retuned.

**Instrument (unchanged from SUR-2046A).** `score_pool_dhook_vocab.py` is `score_2046_dhook_vocab.py` with the token pool extended to
`reading_2077_legend_nieuw_tokens.tsv` (as committed: H 538 C 12 M 63 U 45) beside `reading_2046_legend_nieuw_tokens.tsv` (H 233 C 22
M 83 U 24). Same anchor rule (one segment, no keyed disagreement, two-valued slots agree on either letter, keyed agreements >= max(4,
L-2), U wildcards <= 2), same frozen vocabulary (12,866 folded words: >= 5 letters, >= 3 times in tools/data/nl18, plus
vocab_prereg.txt), same fold, same 24-letter null, same per-class decision (ACCEPT X iff Score(X) strict max, >= ceil(n/2), margin
>= 2 over the runner-up).

**Target.** [d-hook], n = 15, every slot set to X together; one run.

**Controls (the same five classes, gate unchanged).** h = n (primary; occurs on 2046 only, n 10; run exactly as in SUR-2046A),
5 = v (pooled n 32), [hash] = o (32), [delta] = a (51), 6 = s (28). None is valued e. The pooled control classes are larger than the
target, so to match N (rule 3) each is scored on n = 15 subsamples: every position of the class is set to X (as for the target),
coverage is computed once per letter, and Score counts only the 15 sampled positions; each draw takes min(10, n on 2046) positions
from 2046 and the rest from 2077 (the target's 10:5 mix); 20 draws per control, `random.Random(seed)`, seeds 0-19. A pooled control
ACCEPTs its key value if the per-draw decision ACCEPTs that value in >= 10 of 20 draws. The value-class null moves the statistic, so
each control can fail differently from the target (rule 3 orthogonality).
**Gate: h ACCEPTs n AND >= 4 of the 5 controls ACCEPT their key value.** Gate FAIL -> non-test, no key edit, whatever the target scores.

**Outcomes and licensed edits.**
- Gate PASS and [d-hook] ACCEPT e -> **decided**: the 14 U [d-hook] rows get `-> e` grade **M** (class-level context test) appended to
  `exceptions_nieuw_image.tsv` by `--write-exceptions`; regenerate readings with `tools/decode_key.py ciphers/na-suriname-map-1781`
  and `--check`. Nothing else edited.
- Gate PASS and [d-hook] ACCEPT another letter, or UNDECIDED -> undecided; logged, no edit.
- **Gate FAIL -> non-test, and (brief, rule 3 third-attempt clause read conservatively: two control failures) the instrument -- the
  nl18-vocabulary anchor test -- is logged [retired] for [d-hook]; the target's score is not used for anything.**
Per-position coverage words are printed for the record; no per-token grade comes from them. One run; no change to vocabulary, anchor
rule, margins, subsample size, draw count or acceptance count after this file is pushed.
