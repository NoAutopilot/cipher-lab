# PREREG TXE3-2 FLOOR (account 3, Fable worker, 11 Oct 2026 05:5x UTC by date -u; written and pushed BEFORE any subagent image call or classification)

One of ten TXE3 transcription experiments the account-3 parent launched on 11 Oct 2026 at the owner's request. Folder
`benchmark-tx/txeng3/2/`. Rules in force: readers blind; no truth file, BENCHMARK-TX.tsv or flag file edited; nothing written to
`benchmark-tx/txeng2/oracle1/`; no eval score of any new reader pass (this job produces no transcription pass: it classifies the
cause of errors already on disk); no confirm/single-look item opened (vivonne1573-f103r-confirm2 and kin: not touched).

## Hypothesis

The 18 no.87 positions wrong in all six committed outputs A, B, C, L, E, F (the floor: 18/803 as measured, 7/792 flagged-excluded,
TX-TRUTH-VERIFY table in TRANSCRIPTION.md) have causes that the IMAGE can separate -- segmentation (box joins/splits, crop edge),
look-alike pairs, doubtful truth, faint or damaged ink -- and most of the unflagged 7 are look-alike or cut errors that an existing
instrument (box check, owner sorter question, key-constrained decode) can reach. The read-free audits TXE-T (FLOOR-AUDIT.md) and
TXE-T2 (FLOOR-AUDIT-803.md) classified these from tables only; this job is the first image-based classification, and it is the
first with a control for the classifier itself.

## Endpoint

Per floor position: one cause class (i) cut/segmentation, (ii) look-alike pair (named), (iii) truth doubtful (not yet flagged),
(iv) ink damage or faint ink, (v) other; and one instrument: box check (Fix the cut), owner sorter question, key-constrained
decode (`tools/key_decode_lattice.py`), truth verifier, or none. Output `benchmark-tx/txeng3/2/floor.tsv` (36 rows: 18 floor + 18
control, with the blind classifier's raw answers and the mapped class), and a ranked list of fixes with the expected err_true drop
each would give on no.87 (positions fixable / 803 and / 792), as measured and flagged-excluded, never the latter alone.

Second endpoint, read-free: across the six outputs, the share of errors that are insertions or deletions versus substitutions, from
`tools/tx_bench.py`'s standard SER line (S / D / I), as measured and flagged-excluded.

## Method (fixed now)

1. Floor set: the 18 rows of `benchmark-tx/txeng3/2/positions6.tsv` (tools/tx_taxonomy.py over L, A, B, C, E, F against the current
   truth, 803 scored) with err_L..err_F all 1. Listed in this file's appendix before any image is cut.
2. Control set: 18 positions right in all six outputs (err all 0, not flagged, not excluded), one per floor position, drawn at random
   (`random.Random(20261011)`) from the SAME cipher line as that floor position (so the control shares the line's crop, hand, ink and
   reader call). The control measures how often the classifier reports a cause on a sign nothing went wrong with.
3. Material per position, cut by `benchmark-tx/txeng3/2/build_items.py`: (a) the sign tile with a margin (atlas box from
   `ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv` via no87_box_token.tsv for f178v/f179r; for f178r, which the atlas does not
   cover, boxes from `tools/glyph_atlas.py segment` on the f178r source page, mapped to positions by order within the line and
   checked against the committed count, else a proportional window); (b) the line-segment crop the readers saw with a bracket drawn
   above every marked position in that crop (positions labelled by letters, floor and control mixed, order shuffled); (c) the clerk
   clear-sheet crops `harvest/f179r_sheet/dec_L??_s{1,2,3}.jpg` of the sheet line holding the clerk word at that position, with the
   sheet transcription of that line and the word bracketed (mapping: truth position -> align87/align_real.tsv row -> letter offset in
   align87/pairs.tsv plain_raw -> sheet line/word by difflib on folded letters); (d) the value-blind key sign sheet
   `harvest/sign_sheet_blind_1572.png` (T-numbers, no letters).
4. Classifier: one Sonnet subagent call per cipher line (CLAUDE.md Usage 6: never a full page), given only (a)-(d) for the marked
   positions on that line. It is told nothing about which positions are errors, what any reader read, what the key value or the truth
   is. It answers, per marked position: Q1 box = one whole sign / cut (part of a sign) / joined (more than one sign) / unclear;
   Q2 ink = clean / faint / damaged (blot, bleed-through, hole) / struck-or-overwritten; Q3 the two sheet signs it most resembles with
   confidence 1-5 each and whether the pair is hard to tell apart on this tile; Q4 the clerk word as it reads it, whether the letter
   at the indicated index is legible, and any abbreviation, ampersand, struck letter or correction at or beside it; Q5 a free note.
5. Mapping to classes (fixed now, applied by script to floor and control alike): Q1 cut/joined -> (i); else Q4 abbreviation /
   ampersand / struck / correction / illegible -> (iii) [if the position already carries a TX-TRUTH-VERIFY flag it is reported as
   "(iii), already flagged"]; else Q2 faint/damaged/struck -> (iv); else Q3 top-1 or top-2 is the readers' sign AND the other is a
   truth-set sign, or Q3 says hard-to-tell -> (ii), pair named as (readers' sign, truth-set sign nearest on the sheet); else (v).
   Instrument: (i) -> box check; (ii) -> owner sorter question, plus key-constrained decode when the truth-set sign is in the
   classifier's top-2 (truth-in-lattice); (iii) -> truth verifier, not a reader fix; (iv) -> owner sorter question; (v) -> none.
6. Control statistic: the share of the 18 right signs on which the classifier reports any cause ("invented cause" = Q1 not whole,
   or Q2 not clean, or Q4 problematic, or Q3 top-1 not in that position's truth set). It CAN differ from the floor set's share: the
   classifier sees the same material either way and is free to answer "whole / clean / legible / top-1 = the sign the readers
   read" on a right sign and anything else on a floor sign (rule 3: the control varies on the statistic). It also cannot be near
   ceiling by construction: a classifier that reports a cause on everything scores 18/18 on both sets and the floor result is then
   void (see gate).
7. Expected err_true drop per fix = number of floor positions the fix reaches / 803 (and / 792 flagged-excluded), reported with
   the control's invented-cause rate as the discount a reader should apply.

## Gate

The floor classification is INFORMATIVE only if the invented-cause rate on the 18 controls is <= 0.25 (<= 4 of 18) AND lower than the
share of floor positions given a cause other than (v) (two-sided Fisher p reported; the gate is the rate, the p is beside it). If the
control rate is above 0.25, the classifier invents causes and the per-position classes are reported as "unreliable at this N", the
instrument ranking is NOT issued from them, and only the read-free I/D-vs-S share stands. A null is a result.

## Stop rule

Cap USD 15 of usage, box 2 hours from 05:47 UTC (ends 07:47 UTC); stop before starting a unit (one subagent line call) that would
cross 80% of either (USD 12 / 07:23 UTC). Units: about 13 line calls (the 13 lines holding the 18 floor positions, controls on the
same lines), Sonnet, each about 4-7 small images; estimate USD 0.3 per call, USD 4 total, plus the build. Reconciliation of the
answers into floor.tsv is a script, not a second model pass (no reconciliation unit). No second attempt at a line whose call fails
badly: that line is reported "not classified".

## Not done here

No new reader pass; no truth edit; no flag proposed to the verifier beyond naming (iii) candidates in RESULTS.md; no owner pages; no
oracle1 files; no change to BENCHMARK-TX.tsv; the mark rule and the transcribe-and-decode crossword stay retired.

## Appendix: the 18 floor positions (from positions6.tsv, before any image is cut)

line pos plain truth-set | reads L A B C E F | TX-TRUTH-VERIFY flag
f178r_L02 19 s T57|T92|T95|T98|X_CE | T70 T70 T70 T70 T70 T70 | -
f178r_L03 23 t T27|T53|T65 | T90 T90 T90 T90 del T90 | alignment-doubtful
f178r_L03 31 c T36|T50 | T96 del del T96 del del | -
f178r_L03 34 c T36|T50 | T90 del del T90 del T53 | -
f178v_L02 12 e T45|T66|T86 | T36 x6 | clerk-doubtful
f178v_L05 1 e T45|T66|T86 | T76 T76 T76 T76 T89 T26 | -
f178v_L05 4 t T27|T53|T65 | T90 x6 | alignment-doubtful
f178v_L05 9 s T57|T92|T95|T98|X_CE | T64 T13 T64 T64 T13 T13 | clerk-doubtful
f178v_L06 27 u T33|T49 | T76 T76 T76 T76 T15 T15 | alignment-doubtful
f178v_L09 4 e T45|T66|T86 | T96 x6 | clerk-doubtful
f178v_L10 4 e T45|T66|T86 | T76 T76 T76 T76 T89 T26 | -
f178v_L11 5 e T45|T66|T86 | T76 T76 T76 T76 T89 T76 | -
f178v_L13 7 o T19|T52|T55 | T70 x6 | alignment-doubtful
f178v_L15 24 c T36|T50 | T46 T46 T46 T46 T97 del | alignment-doubtful
f178v_L21 21 a T37|T85 | T76 T76 T76 T76 T89 T76 | alignment-doubtful
f178v_L22 2 z T10|T38 | T60 x6 | alignment-doubtful
f178v_L22 24 t T27|T53|T65 | T90 T90 T45 T90 T90 T90 | alignment-doubtful
f179r_L02 8 e T45|T66|T86 | T24 T24 X_NEW T24 T24 T24 | -
