# FLOOR-AUDIT: the 20 no.87 positions every pass gets wrong, traced to the truth source (TXE-T, 9 Oct 2026)

LANE TX-ENGINEER round 3, account 4, Opus 5.5. Brief `.claude/briefs/runs/2026-10-09-account4-txe-t.md`. Read-free: 0 vision
calls, 0 hosts. No truth file, BENCHMARK-TX.tsv or other instrument's file was edited. This is an auditor's proposal for a
verifier, not a change to the benchmark.

Per-position table: `no87_floor_audit.tsv`. Proposed flag column: `truth_flags_proposed.tsv` (13 rows, not applied).

## Method

The 20 positions are the rows of `no87_positions.tsv` with err_A..err_F all 1. For each I read: the `align87/align_real.tsv`
row and its neighbours (the truth file zips this table position by position onto the committed sequence, so ref_sign is
the committed sign); the clerk letters the aligner **skipped** (rebuilt by walking each row's chunk through the clerk span's
letter stream from `align87/pairs.tsv`, folded as `tools/interlinear_align.py plain_letters` folds it -- 43 skip sites, 81
letters in the whole letter); the clerk-sheet transcription row and its conf/note (`f179r_sheet/decipherment_sheet.tsv`);
the sign's clerk counts in `align87/key_real.tsv`; and the key rows that make the truth set (`key_1572_sheet.tsv`, T42=m
override, T95 s|l, T52 i|o, X_CE s, as `build_birago87.py` applies them). Classes per the brief.

## Counts

| class | n | positions |
|---|---|---|
| reader-wrong | 7 | f178r L02.19, L03.31, L03.34; f178v L05.1, L10.4, L11.5; f179r L02.8 |
| alignment-doubtful | 8 | f178r L03.23; f178v L05.4, L06.27, L13.7, L15.24, L21.21, L22.2, L22.24 |
| key-doubtful | 1 | f178v L02.8 |
| clerk-doubtful | 4 | f178v L02.12, L05.9, L09.4, L11.17 |

13 of 20 are truth-doubtful. Of the positions read with the same sign by every pass (8 by my count from
`no87_positions.tsv`; TX-TAXONOMY section 1 says 9, but f178v L22.24 has B = T45 and none of the T76 rows is unanimous, E
reads T89), **7 of 8 are truth-doubtful**; the one unanimous reader-wrong is f178r L02.19 (T70 for s).

## The two floor figures (both kept; the benchmark's number is not replaced)

| | as measured (BENCHMARK-TX) | doubtful 13 excluded |
|---|---|---|
| pass L err_true | 0.045 (36/803), 95% 0.033-0.061 | 0.029 (23/790), 95% 0.019-0.043 |
| floor (wrong in all six passes) | 20/803 = 2.5% | 7/790 = 0.9% |

`tools/tx_bench.py --item birago1572-no87 benchmark-tx/outputs/birago1572-no87/labels.tsv`:
`err_true 0.045 (36/803) 95% 0.033-0.061 | wrong 36 deleted 0 inserted 0 | excluded 50`. All 13 doubtful positions are in
L's 36 (every floor position is). The exclusion figure is conditional on this audit and on the verifier.

## What the trace found

1. **T90 is "et" three times.** All three of T90's t-alignments in the letter (key_real 90: p 19/23, t 3) sit on the t of a
   clerk "et" whose e the aligner skipped: "turino et tolto" (f178r L03.23), "esso, et l'amossi" (f178v L05.4), "in franza
   et" (f178v L22.24). L's whole `t<-T90 x3` confusion is this. Either the hand has an "et" sign the readers file under T90
   (an unlisted homophone of T29) or they misread T29; either way the truth "t" is a split artifact.
2. **Multi-letter clerk words on one or two signs.** "questo" on one T70 (L13.7, "quest" skipped); "hugonotti et" on X_NEW +
   T76 + T29 with a 9-letter chunk (L06.27); "catholici" split c | atholici over two T46 (L15.24; T46 aligns to turino, c,
   atholici and re, four values in four rows); "malta"/"contentezza" one sign short with a skip at the position itself
   (L21.21, L22.2).
3. **The clerk sheet is the doubtful side four times**: "guase ogna" for Guascogna (the readers' T36 c makes the word);
   "hauer ero forma", which the sheet itself marks "as written", conf M (decode "hauere io", T80 i 20/21); "l'amossi",
   which the sheet marks uncertain; "de rauelli" where the cipher writes "di" (T96 i 32/34).
4. **The key**: T42 at "di Guascogna" is the one g among 12 clerk alignments (m 11); the key row's own note names this
   position as the printed g. The truth uses the C override m, so the printed value scores as an error.
5. **What is left is reader-wrong** (7): three T76 for an e-sign on band-cut lines (the n/e look-alike pair, key_real 76
   e 3 = exactly these three), two crop deletions on the f.178r L03 sloping tail (class 2a; only C's sloped re-crop read
   them), T70 for s and T24 for e on clean alignments. Read-free I cannot separate a reader error from an encipherer's slip
   at the two unanimous-or-near ones (L02.19 T70, f179r L02.8 T24): that needs the image, i.e. the sorter.

## Caveats

- Classification is one auditor's judgement on tables; a verifier session decides (CLAUDE.md rule 3/7; the brief).
- The skip-site test was run only around the 20 floor positions. The same artifacts (skipped e of "et", multi-letter clerk
  words on one sign) may sit under positions some passes read right or wrong outside the floor; the 43 skip sites are the
  place to look. Follow-up (not done, one line): run the skip/chunk test over all 803 scored positions and flag the truth
  rows within 0-1 of a skip.
- The floor positions f178r L03.31/34 have the committed (C) sign as ref_sign; C's reads there come from the sloped re-crop
  and are themselves off-value, so the reference sign for those two is weak, but the truth (clerk c in "licencia") is clean.
