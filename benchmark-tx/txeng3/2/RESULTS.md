# TXE3-2 FLOOR: why 18 signs defeat every method on no.87 (account 3, Fable worker, 11 Oct 2026 05:47-06:0x UTC by date -u)

PREREG `benchmark-tx/PREREG-txeng3-2.md` (commit 171be8be, pushed before any image call). Per-position table `floor.tsv`
(36 rows: 18 floor + 18 same-line right-sign controls, the blind classifier's raw answers and the mapped class). Build
`build_items.py` (material), `score_floor.py` (mapping, gate), `items/<line>/` (marked crops, tiles, prompt.md, answer.json),
`positions6.tsv` (tx_taxonomy over L A B C E F against the current truth). 13 Sonnet calls, one cipher line each, each given only
the tile, the marked line crop, the clerk clear-sheet crops with the word bracketed, and the value-blind printed sign sheet;
nothing about reads, key values, truth or which positions were errors. No truth file, flag file, BENCHMARK-TX.tsv or oracle1
file touched; no eval reader pass produced or scored; no confirm item opened.

## Verdict: measured: NON-TEST for the per-position classification (control above gate); the I/D-vs-S share stands

| statistic | floor (18) | control (18, right in all six) | gate |
|---|---|---|---|
| invented cause (PREREG step 6: Q1 not whole, or Q2 not clean, or Q4 problem, or top-1 not a truth-set sign) | 18/18 by the same rule (every floor top-1 is off the truth set by construction) | **7/18 = 0.389** | <= 0.25 (4/18): **FAIL** |
| any cause other than (v) after mapping | 11/18 | 5/18 | floor > control: yes, Fisher p = 0.32 (not significant) |

The classifier reports a cause on 7 of 18 signs that every reader got right, so by the pre-registered gate the per-position
classes below are **unreliable at this N**, and the instrument ranking is NOT issued from them. A null is a result. What the
control failure is made of (post hoc, not gated): 6 of the 7 are "top-1 not in the truth set" -- the classifier's own sign
identification against the PRINTED sheet missed the right sign on 6/18 right signs (its top-1 was in the truth set 12/18, the
sign the readers read 11/18, mean confidence 4.2 of 5); the image-side causes alone (Q1/Q2/Q4) fire on 4/18 controls (three
"joined" boxes, one "cut + faint" at the binding shadow) against 6/18 floor positions. Both halves of the rule leak.

## What was measured anyway (reported, not licensed)

Floor table (reads L A B C E F; flag = TX-TRUTH-VERIFY; class = PREREG step 5 mapping; `floor.tsv` has every raw answer):

| line | pos | plain | truth set | reads | flag | q1 | q2 | top1/top2 (hard?) | clerk word / issue | mapped class |
|---|---|---|---|---|---|---|---|---|---|---|
| f178r_L02 | 19 | s | T57 T92 T95 T98 X_CE | T70 x6 | - | whole | clean | T86(4)/T60(2) clear | ch'auesse / none | v |
| f178r_L03 | 23 | t | T27 T53 T65 | T90 x5, del | alignment | whole | clean | T85(3)/T51(2) hard | et / ampersand | iii, flagged |
| f178r_L03 | 31 | c | T36 T50 | T96 x2, del x4 | - | whole | clean | T83(4)/T81(2) clear | licencia / none | v (box approximate) |
| f178r_L03 | 34 | c | T36 T50 | T90 x2, T53, del x3 | - | whole | clean | T60(3)/T86(2) hard | licencia / none | v (box off the sign, classifier's own note) |
| f178v_L02 | 12 | e | T45 T66 T86 | T36 x6 | clerk | whole | clean | T36(4)/T18(2) clear | guase / none | v |
| f178v_L05 | 1 | e | T45 T66 T86 | T76 x4, T89, T26 | - | whole | clean | T76(3)/T26(2) hard | esso / none | ii T76~T26 |
| f178v_L05 | 4 | t | T27 T53 T65 | T90 x6 | alignment | whole | clean | T45(3)/T90(3) hard | et / ampersand | iii, flagged |
| f178v_L05 | 9 | s | T57 T92 T95 T98 X_CE | T64 x3, T13 x3 | clerk | whole | clean | T64(4)/T38(3) hard | lamossi / none | ii T64~T38 |
| f178v_L06 | 27 | u | T33 T49 | T76 x4, T15 x2 | alignment | whole | clean | T26(3)/T76(3) hard | hugonotti / none | ii T26~T76 |
| f178v_L09 | 4 | e | T45 T66 T86 | T96 x6 | clerk | whole | clean | T96(5)/T17(1) clear | de / none | v |
| f178v_L10 | 4 | e | T45 T66 T86 | T76 x4, T89, T26 | - | whole | damaged (blot) | T76(3)/T26(2) hard | de / none | iv |
| f178v_L11 | 5 | e | T45 T66 T86 | T76 x5, T89 | - | whole | clean | T76(3)/T66(2) hard | uole / none | ii T76~T66 (truth in top-2) |
| f178v_L13 | 7 | o | T19 T52 T55 | T70 x6 | alignment | whole | clean | T90(4)/T84(2) clear | questo / abbreviation | iii, flagged |
| f178v_L15 | 24 | c | T36 T50 | T46 x4, T97, del | alignment | whole | clean | T46(2)/T11(2) hard | catholici / none | ii T46~T11 |
| f178v_L21 | 21 | a | T37 T85 | T76 x5, T89 | alignment | whole | clean | T58(5)/T80(1) clear | malta / none | v |
| f178v_L22 | 2 | z | T10 T38 | T60 x6 | alignment | whole | faint | T60(3)/T86(3) hard | contentezza / none | iv |
| f178v_L22 | 24 | t | T27 T53 T65 | T90 x5, T45 | alignment | whole | clean | T90(3)/T45(2) hard | et / ampersand | iii, flagged |
| f179r_L02 | 8 | e | T45 T66 T86 | T24 x5, X_NEW | - | whole | clean | T24(4)/T96(2) clear | questa / none | v |

Counts: (i) cut/joined 0, (ii) look-alike 5, (iii) truth-doubtful 4 (all four already flagged; the classifier found the
ampersand/abbreviation on its own at 4 of the 11 flagged positions, 0 new), (iv) ink 2, (v) other 7. Pairs named by the
classifier: T76~T26 (x2), T76~T66, T64~T38, T26~T76, T46~T11; the T98/T18 pair is absent because no T98-for-d position is on
the floor (all seven are reader-split, FLOOR-AUDIT-803). Two observations that do not depend on the gate: **no floor sign
was judged cut or joined** (0/18; the four "joined" verdicts all fell on control signs the readers got right), and the
classifier's top-1 landed on the sign the readers read at 10/18 floor positions while the truth-set sign was in its top-2 at
1/18 -- on the page these 18 signs look like what the readers read, not like the printed shape of the truth value. Of the 7
unflagged floor positions, 2 (f178r L03.31, L03.34) sit on the sloping tail the atlas does not cover and were boxed by
proportion (the classifier said one box was off the sign): a cut or deletion cause there is not excluded by this pass.

Instrument reach if the mapping were trusted (it is not; for scale only): owner sorter question 7/803 = 0.0087 as measured,
3/792 = 0.0038 flagged-excluded; box check 4/803 = 0.0050 (the four positions some pass deleted), 2/792 = 0.0025;
key-constrained decode 1/803 = 0.0012, 1/792 = 0.0013. The whole floor is 18/803 = 0.022 / 7/792 = 0.009, so no instrument
reaches more than about 0.9 points of err_true on this item even if every mapped class were right.

## Insertions and deletions versus substitutions (read-free, tools/tx_bench.py standard SER, both masks)

| output | as measured S/D/I | I+D share | flagged-excluded S/D/I | I+D share |
|---|---|---|---|---|
| A | 45/8/0 | 0.151 (8/53) | 34/8/0 | 0.190 (8/42) |
| B | 64/8/6 | 0.179 (14/78) | 53/8/6 | 0.209 (14/67) |
| C (reconciled) | 41/0/0 | 0.000 (0/41) | 30/0/0 | 0.000 (0/30) |
| L (C + owner labels) | 34/0/0 | 0.000 (0/34) | 23/0/0 | 0.000 (0/23) |
| E (sheet) | 49/9/2 | 0.183 (11/60) | 39/8/2 | 0.204 (10/49) |
| F (Fable) | 52/19/2 | 0.288 (21/73) | 42/18/2 | 0.323 (20/62) |
| all six pooled | 285/44/10 | 0.159 (54/339) | 221/42/10 | 0.190 (52/273) |
| single passes A B E F | 210/44/10 | 0.205 (54/264) | 168/42/10 | 0.236 (52/220) |

C and L carry 0 insertions and 0 deletions by construction: the truth's sign sequence was aligned on the committed read C
(TX-BENCH build note), so C's segmentation is the reference and its own cut errors are invisible. For a single pass the
boxes could remove at most about a fifth of its errors (0.15-0.29 by reader; Fable's 0.29 is deletions, its abstentions);
for the reconciled read the benchmark cannot see what the boxes would remove, and the floor itself holds no sign the
classifier saw as cut. The box-check team should expect the gain on no.87 single passes to be bounded by those 8-21
deletions per pass, and to be unmeasurable on C/L until a truth built on independent boxes exists.

## For the owner, in three sentences

The 18 signs every method gets wrong are not badly cut and not faint: on the page they look like the sign the readers read,
and eleven of them are places where the clerk's clear text, not the cipher, is in doubt. A blind Sonnet judge asked to name
causes names one on 7 of 18 signs that were read correctly, so its per-sign diagnoses cannot be trusted at this size and no
fix ranking is issued from them. Boxes can at most remove about a fifth of a single reader's errors here and none of the
floor; the floor is a truth and encipherer question for a verifier and the sorter, not a segmentation one.

## Next step and cost

A second classification with the hand's own exemplar tiles (atlas/sheet_truth, the TX-SHEET sheet) instead of the printed
sheet, on Opus, with the control doubled to 36 right signs so a 0.25 gate has room (36 x 0.25 = 9): about USD 6 and 45
minutes; it is worth running only if the sign-ID half of the rule drops below 1/6 on controls, else the instrument is the
limit (rule 3's third-attempt clause would then retire blind image classification for the floor). Independent of that, the two
unboxed f178r L03 tail positions (31, 34) go to the box check (L74's oracle pages already hold f178v lines, not f178r) as a
named cut question, and the 7 unflagged floor positions are listed here for a verifier as encipherer-slip candidates, never
as flags from this job.

Cost: cap USD 15 / 2 h; 13 Sonnet calls at about 112k tokens each; the worker cannot read its own usage figure (get_session
shows none to the session itself), the parent records it from get_session. Rate-limit status at 06:00 UTC: allowed_warning
(BUDGETS.md scaling rule: no new workers; this job spawned none after that read). Hosts: none.
