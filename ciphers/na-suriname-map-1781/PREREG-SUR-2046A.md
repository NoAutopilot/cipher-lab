# PREREG SUR-2046A (15 Oct 2026, account 2, LANE DEFAULT-A2-1109-15): 4.VEL 2046 [d-hook] = e, wider-vocabulary anchor test

Written and pushed before any score; only `score_2046_dhook_vocab.py --dry` (vocabulary size and class counts) has run.

**Question.** Do the 10 unkeyed [d-hook] tokens on the 2046 block (No1:28, No1:49, No2:12, leg_d:24, :43, :57, leg_efgh:30, :58,
leg_ki:5, :24) read e as a class? SUR-ALIGN (13 Oct) anchored one of them (efgh:30, under "battery"/"batteryen", one span) and
logged the others as an observation only; SUR-TRY (15 Oct) retired --try for n = 1 questions. This is the class test SUR-ALIGN's
observation named: a vocabulary wider than crib_2042.

**Instrument.** `score_2046_dhook_vocab.py`. SUR-ALIGN's anchor rule unchanged (one segment, no keyed disagreement, two-valued
slots agree on either letter, keyed agreements >= max(4, L-2), U wildcards <= 2). Vocabulary frozen now: every word of >= 5
letters seen >= 3 times in `tools/data/nl18` (7 files, Dutch print 1770-1799) plus `vocab_prereg.txt`, folded (lowercase,
accents stripped, ij/ÿ -> y, j -> i, z -> s; the target's values get the same fold): 12,866 words. Input:
`reading_2046_legend_nieuw_tokens.tsv` as committed (H 233 C 22 M 83 U 24).

**Statistic.** For class C (n positions) and letter X in a..y without j, z (24 letters): set every C slot to X; Score(C, X) =
number of C positions covered by at least one anchor. The value-class null is the other 23 letters at the same positions (it
changes the statistic, so it can fail differently from the hypothesis: rule 3's orthogonality check).

**Decision per class.** ACCEPT X if Score(X) is the strict maximum, Score(X) >= ceil(n/2), and Score(X) - runner-up >= 2;
otherwise UNDECIDED.

**Controls (must accept a known H value of the same frequency class on the same sheet).** Each control class is blanked to U and
tested exactly as the target: h = n (primary; n 10, all H, the same count as [d-hook]), 5 = v (n 11: 10 H, 1 M valued v),
[hash] = o (9 H), [delta] = a (11 H), 6 = s (11 H). None is valued e, so a test that just favours Dutch's commonest letter fails
them. **Gate: h ACCEPTs n AND >= 4 of the 5 controls ACCEPT their key value.** Gate FAIL -> non-test, no key edit, whatever the
target scores.

**Outcomes and licensed edits.**
- Gate PASS and [d-hook] ACCEPT e -> **decided**: 10 rows `[d-hook] -> e` grade **M** (class-level context test, not a sheet
  match) appended to `exceptions_nieuw_image.tsv` by `--write-exceptions`, then `tools/decode_key.py ... ` regenerate and
  `--check`. Nothing else edited.
- Gate PASS and [d-hook] ACCEPT another letter -> undecided for e; logged, no edit (another value needs its own PREREG).
- Gate PASS and UNDECIDED -> undecided; logged, no edit.
- Gate FAIL -> non-test; logged, no edit.
Per-position coverage words are printed for the record; no per-token grade comes from them. One run, no re-tuning of the
vocabulary threshold, the anchor rule or the decision margins after this file is pushed.
