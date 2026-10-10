# Hypotheses and data conflicts: sachsstaatsarchiv-manteuffel-1712

## Rule-4 conflicts between Krauske's 1893 table and the period interlinear glosses (VERIFY-MANT, 3 Oct 2026)

| code | Krauske 1893 (Loc. 694/10 f.2) | period gloss witness | other witnesses | verdict |
|---|---|---|---|---|
| 26 | r | 694/08 f.467 (Manteuffel to Flemming, Berlin, Dec 1712, as received), lines 7 and 16: "R." over a lone 26, "R." also in the margin | f.468 (same series, Dec 1712): lone 26 with "R." in the margin; f.468 also glosses lone 39/9 "Ilg./Ilgen", 44 "Lol.", 66 "Arn" -- each the table's own letter value used as a person's initial | **not a conflict**: a letter code standing alone is the initial of a person (the pattern on both glossed leaves). Inside words (f.410 "c o u r" = 30 22 6 26) 26 = r stands. Which person "R." is stays open. |
| 4 | x | f.467 line 22: "Ilgen" over a group both blind passes and GAPS166 read "4" | Krauske notes "Ilgen" beside 9 and 39 (both = i); f.468's writer makes 4 and 9 alike (GAPS154: "a y-shaped glyph", and spelled group 3.35.44.12.34.21.7 = Welling wants 39/9 = i where "34" was read) | **open, M**: most likely a 9 read as 4 (one witness, one occurrence, a known glyph confusion); not resolved by majority. VERIFY-MANT's one vision look at f467_L11 did not cover line 22, so the digit was not re-read. Any lone "4" in a letter of this series is graded M. f.410 has no lone 4 (only inside 4001, U). |

Witness letters are from one direction only (Manteuffel to Flemming, 694/08, Nov-Dec 1712). No 1713 (694/09) gloss has been read.

### GAPS195 (3 Oct 2026, account-4): codes glossed on 694/08 ff.422v-423 (frame 0528) against Krauske's table

| code | Krauske 1893 (key.tsv) | 0528 period gloss | status |
|---|---|---|---|
| 73 | s\|z (M) | "Ilgen" over a lone 73 (f.423, 1 occurrence; both passes, gloss partly at a crop edge) | **conflict, open, M**: not overwritten. Either a lone letter code as a person's initial (the 26 = "R." pattern above would need "I"/"Ilgen" from a letter code, and 73 is not i) or a different table on this leaf. Graded M in any letter. Second witness (RUN3-MANT, 4 Oct 2026): frame 0501 (694/08, ff. ~400v-401, Nov 1712) also has "Ilgen" over a lone 73 (zoom; passes "Hen?"/"Hyen?"). Two leaves now agree on Ilgen; still not resolved by count (rule 4): open, M. Third code (RUN5-MANT4, 4 Oct 2026): frame 0502 glosses a lone 357 "Ilgen" (worker zoom; passes Hyen?/Ulyen?); 0502's per-leaf gate HELD (tie), so 357 stays M in f0500_0502/leaf_values_0502.tsv; with 98 Ilgen (C, 0528) the series would carry at least two, possibly three, codes for Ilgen. Update (RUN5-MANT5, 4 Oct 2026): under the pre-registered gloss normalisation (PREREG-MANT5) 0502 PASSES its gate, so 357 = Ilgen enters key.tsv at C: the series now carries two C codes for Ilgen (98, 357) and 73 still open, M -- consistent with homophone name codes, not resolved. |
| 82 | z (C) | "Schonborn" over a lone 82 (f.423, written "Schonbofn"; both passes) | **conflict, open, M**: not overwritten. 107 is also glossed Schonborn 6 times on the same leaf, so 82 would be a second code for him; with 73 above and 240 (Krauske Pless) sitting inside "du nord" twice, this leaf may use a different table from Krauske's in the range below ~400. Same direction and series (Manteuffel to Flemming, 694/08, late 1712) as f.467/f.468, which matched Krauske 17/17. |
| 401, 115, 156, 180, 230, 100, 84, 240 | o, à, Hoym, Golowkin, Le roi de Prusse, d, sch, Pless | frame 0501 (RUN3-MANT, 4 Oct 2026), inside multi-code glossed runs: 401...612 "le Pr Royal a tenu au feldmarechal qui la debite" (156 and 180 sit under "feldmarechal qui la debite", no Hoym/Golowkin in the gloss); 230.100.115.588.273.494 "comme la sienne"; 553...108 "qu'un troisieme appelle" (84 inside); 583.240.825 "generaux suedois" | 0528: 240 inside "du nord" twice | **inconsistent, M, recorded not resolved**: the multi-code class tied its shuffle control on 0501 (S_multi 0.250 = p95 0.250), so no chunk value is licensed; but with 240 now inside a non-Pless gloss on a second leaf and 156/180 under a gloss naming neither person, 0501 like 0528 reads as a different table from Krauske's in the range below ~400 (115 = à is the one value compatible with its gloss). |

Codes merged into key.tsv from this leaf (all new to it, none in Krauske's table): 98 Ilgen C, 107 Schonborn C, 754 le Roi
de Pologne C, 864 le Roi de Prusse C, 877 Bartholdi M, 879 Hannovre C -- single-code glosses only, licensed by the per-leaf
gate (PREREG-GAPS195, f423_0528/shuffle_control.tsv). Multi-code chunks were not merged (0/15 consistent, below the shuffle).

### Word-level pairing, multi-code class (RUN4-MANT, 4 Oct 2026)

| date | instrument | control | target | verdict |
|---|---|---|---|---|
| 4 Oct 2026 RUN4-MANT | whole-word code pairing on frame 0501's glossed multi-code runs (C3 C4 C7 C9[4 codes] C10 C12), PREREG-MANT-WORD (90d63000) | control: gloss-string permutation across runs, 200 draws seed 409: S_word mean 0.274, p95 0.500 | target: S_word 1/4 = 0.250 (at most 1 of 115/402/515/612 consistent under any cut; best cut: 402 'la') | HELD, below the shuffle mean; nothing into key.tsv. 515 is consistent as the chunk 'pr' (RUN3-MANT) but not as a word (Pr / propose): codes in this range are sub-word units, so a whole-word instrument cannot read them. Multi-code class: letter-chunk alignment (interlinear_align.py) failed on 0528 and tied on 0501; whole-word pairing, a different instrument, also fails on 0501. Both instruments are spent on the glossed material in hand; the next step needs new material (more glossed duplicates of these passages) or a sub-word instrument with a stated control, not a re-run. |
| 4 Oct 2026 RUN4-MANT2 | clear-vs-cipher witness diff, 0501 vs f.409r/f.409v (PREREG-MANT2 3cd76938) | known-answer: no code inside either pair is in key.tsv, so no check possible; 9 cipher-in-both runs agree 44/48 groups (variants 588/586, 494/94, 281/287) | 2 pairs: P1 371 = "Il" (single, once, M, into key.tsv); P2 161.583.237.932 = "affaires suedoises" (chunk, once, M, no per-code split) | hypothesis, not licensed: 583 ~ "suedois/Suede" -- it sits in 3 runs, 2 of them over "suedois(es)" (P2; 0501 gloss 583.240.825 "generaux suedois") and the 3rd (149.612.583.401) right after "le Comte Wartensleben"; position conflict (2nd of 4 vs 1st of 3), so no value until a 3rd clear or glossed attestation |
| 4 Oct 2026 RUN4-MANT3 | clear-vs-cipher witness diff, 0500/0502 vs f.409r/f.409v (PREREG-MANT3 eefcc308) | known-answer on the copy's glosses: 864 Roi de Prusse agree 2/2, 865 Prince Royal agree (run-level), letter runs L33-L35 agree; 21 cipher-in-both runs 146/165 groups | 0 pairs (no clear-vs-cipher slot); 371 = il stays M; 583 ~ suedois untested here (583 only inside runs cipher in both) |

### RUN5-MANT6 (4 Oct 2026): per-unit re-grade of codes resting on frame 0501

Frame 0501 ties its own shuffle control under the PREREG-MANT5 normalisation (single-code S 0.200 = p95 0.200; RUN5-MANT5,
f0500_0502/shuffle_control_norm_0501.tsv), so under rule 3's per-unit merge clause no code attested only there keeps a grade
above M. Leaf status: 0528 PASS (GAPS195), 0502 PASS (RUN5-MANT5), 0500 HELD (N floor), 0501 TIE. Codes listed by script from
key.tsv's source column (rows naming frame 0501):

| code | value | grade before | witnesses (leaf, kind, leaf gate) | independent cleared support? | grade after |
|---|---|---|---|---|---|
| 770 | Manteuffel | C | 0501 single-code gloss x2 (TIE); f.409r cipher-in-both runs 770 = 770 x2 (witness copy, run level, no gloss) | none: not on 0502 or 0528; Krauske's Manteuffel is 160 (and letter codes 13, 31 = m), not 770 | **M** (held pending a cleared leaf or a 2nd clear attestation) |
| 865 | le Prince Royal | M | 0501 single-code gloss "Pr: Royal" (TIE); 0500 run-level gloss "Prince Royal" over 840.865 (HELD, N floor); f.409r digits 865 | none | M (unchanged) |
| 371 | il | M | 0501 clear vs f.409v cipher (clear-vs-cipher pair P1, RUN4-MANT2; not the gloss gate) | none | M (unchanged; once-attested rule already held it) |

Grades in key.tsv: before C 129, M 39; after C 128, M 40. Code 770 does not occur in ciphertext.tsv, so reading token counts are
unchanged (C 202, M 84, U 137 of 423). Not a refutation: two agreeing single-code glosses on one leaf are held, not dropped.

### D2B-MANT27 (5 Oct 2026): file 0527 (ff.422v-423), per-leaf gate HELD -- witnesses only, nothing merged

| code | key.tsv value | 0527 witness | status |
|---|---|---|---|
| 73 | s\|z (Krauske, M) | "Ilgen" over 73 at the end of run 33 (402.604.247.44.214.73, f.423, gloss "conference Ilgen", zoom) | third leaf with Ilgen over 73 (0528, 0501, now 0527); 0527 HELD, so it adds no cleared support; conflict open, M |
| 82 | z (Krauske, C) | "Schonborn" over 82 ending runs 36 and 45 (f.423, "l'armee suedoise Schonborn", zoom) | second leaf with Schonborn over 82; 0527 HELD; conflict open, M |
| 99 | s\|ss\|sa (Krauske, M) | single-code gloss "K" (f.423 run 32, zoom only, M) | disagreement logged; one M gloss, not resolved |
| 868 / 898 | -- / -- | "Ilgen" beside 868 (run 5) and 898 (run 7) on f.422v; 898 = l'Empire 3x as single-code gloss on the same leaf | read doubtful (could be 98 = Ilgen with a lead stroke); kept as read, M |
| 754 | le Roi de Pologne (C) | single-code gloss "S.M." (run 26, M) | compatible (Sa Majeste), not a conflict |
Gate: f422v_0527/shuffle_control.tsv (S 0/52 vs p95 0.058; S_single 1/2 at N 2). Values: f422v_0527/leaf_values_0527.tsv.

## Pooled single-code-gloss gate (R7-MANTP, 6 Oct 2026, LANE LANE-RUN7-account-2, account 2)

| date | instrument | control | target | verdict |
|---|---|---|---|---|
| 6 Oct 2026 R7-MANTP | single-code glosses pooled across leaves 0502, 0501, 0527, 0528 (42 runs), S = share of recurring codes with identical MANT5-normalised glosses; PREREG-MANTP (fa516827) | gloss strings permuted across the pooled single-code runs, 1000 draws seed 7101: mean 0.053, p95 0.222 (within-leaf permutation, not gating: mean 0.046, p95 0.222) | S = 6/9 = 0.667 (N_rec 9) | **PASS**. Per leaf, same instrument: 0528 PASS (4/4 vs p95 0.250), 0502/0501/0527 HELD at the N floor (N_rec 1, 1, 2). Licensed: 98, 107, 357 (C, already C), 73 Ilgen (C by the rule but a Krauske row, s\|z M: not overwritten, conflict above stays open, now 2 leaves incl. cleared 0528), 770 (M, 0501 only, already M), 877 (M, every gloss read M, already M). Disagree: 864 ("le roy de prusse" vs "roy de prusse", article only), 754 ("s m" vs "le roy de pologne", compatible), 898 ("ilgen" x1 vs "l empire" x3). key.tsv unchanged; U tokens moved 0. The values the gate was meant to reach (898, 939, 539, 544) are single-attested in the pool, so no gloss gate can license them until another leaf glosses them. |

## Leaf 0574 (ff.463-463v) per-leaf gate and pooled gate with the leaf added (R7-MANT463, 6 Oct 2026, LANE LANE-RUN7-account-2, account 2)

| date | instrument | control | target | verdict |
|---|---|---|---|---|
| 6 Oct 2026 R7-MANT463 | per-leaf aligner gate on 30 glossed runs of ff.463-463v (PREREG-MANT463 c532b20e2, MANT27 shape, gloss_norm_0574 mant->manteuffel) | gloss strings permuted across the glossed runs, 200 draws seed 463: S mean 0.059 p95 0.109; S_multi mean 0.061 p95 0.113; S_single mean 0.022 p95 0.000 | S 11/55 = 0.200; S_multi 9/53 = 0.170; S_single 2/2 = 1.000 | **PASS** (leaf cleared). Only single-code glosses licensable; all six single codes (160, 150, 313, 38, 187, 266) are Krauske rows and agree or are compatible -- nothing new into key.tsv |
| 6 Oct 2026 R7-MANT463 | pooled single-code-gloss gate, PREREG-MANTP + PREREG-MANT463 addendum, leaf 0574 appended (54 runs) | gloss strings permuted across all pooled single-code runs, 1000 draws seed 7101: mean 0.035, p95 0.182 | S 7/11 = 0.636 | **PASS** (R7-MANTP without the leaf: 0.667 vs p95 0.222). Non-gating sensitivity with gloss_norm_0574 (mant->manteuffel): S 8/11 = 0.727 vs p95 0.182. 898, 939, 539, 544 do not occur on this leaf: still single-attested in the pool, nothing licensed |

Known-answer on this leaf (independent of the gloss-derived key rows): single-code glosses vs Krauske 1893 rows: 9 agree (160 x6, 313, 38, 187),
3 compatible (150 "S.M." x2, 266 "l'Electeur de Hannovre" vs "Hannover|Electeur de Hanovre"), 0 disagree. Descriptive, no control: the aligner's
chunks over codes that have a key.tsv value agree with that value at 210 positions and differ at 74 (0.74). Conflict 73 (Krauske s|z vs gloss Ilgen)
unchanged: 73 does not occur on this leaf. Registered-vs-rule note: the addendum registered 0574 as not prior-cleared in the pooled run; its own
per-leaf gate then PASSed, which by PREREG-MANTP's general rule clears it. Counting it cleared changes no licence (150 would read C, but 150 is a
Krauske row and is not overwritten).

## Leaf 0529 (ff.424v-425) per-leaf gate and pooled gate with the leaf added (R7-MANT529, 6 Oct 2026, LANE LANE-RUN7-account-2, account 2)

| date | instrument | control | target | verdict |
|---|---|---|---|---|
| 6 Oct 2026 R7-MANT529 | per-leaf aligner gate on 29 glossed runs of ff.424v-425 (PREREG-MANT529 213a49cc + addendum 1da59b45, MANT27 shape, MANT5 normalisation only) | gloss strings permuted across the glossed runs, 200 draws seed 529: S mean 0.015 p95 0.083; S_multi mean 0.015 p95 0.087; S_single mean 0.000 p95 0.000 | S 1/24 = 0.042; S_multi 0/23; S_single 2/2 = 1.000 (N 2) | **HELD (miss)**: leaf not cleared; S_single under the N >= 3 floor. Nothing into key.tsv; values held at M in f424v_0529/leaf_values_0529.tsv |
| 6 Oct 2026 R7-MANT529 | pooled single-code-gloss gate, PREREG-MANTP + PREREG-MANT463 + PREREG-MANT529 addenda, leaves 0574 and 0529 appended (63 runs) | gloss strings permuted across all pooled single-code runs, 1000 draws seed 7101: mean 0.040, p95 0.167 (within-leaf, not gating: mean 0.062, p95 0.167) | S 8/12 = 0.667 | **PASS** (5 leaves: 0.636 vs 0.182; 4 leaves: 0.667 vs 0.222). Per leaf 0529: N_rec 2, HELD (N floor). 898 now recurs in the pool (5 single-code runs on 0527 + 0529): 4 "l'Empire" (0527 x3, 0529 x1) vs 1 "Ilgen" (0527 run 7, read doubtful by D2B-MANT27) -> licence "disagree" under the registered rule, not licensed. 867 "le Feldmarechal" 2/2 on 0529 only (uncleared leaf) -> M. 939 occurs on 0529 only inside 272.939 "en Mecklenbourg" (multi-code): still single-attested as a single-code gloss. 107 Schonborn now 11/11 across 3 leaves (Krauske/key row, C already) |

Conflict 898 (logged, not resolved; rule 4): l'Empire is supported by 4 single-code glosses on two leaves (0527 f.422v-423 x3, 0529 f.424v x1),
"Ilgen" by one single-code gloss on 0527 (run 7) that D2B-MANT27 read as doubtful (98 = Ilgen in key.tsv; a misread lead stroke is possible but
not repaired). Non-gating note: without that one gloss 898 would read 4/4; the registered rule counts it, so 898 stays M (held, not in key.tsv).
Known-answer on this leaf: 107 Schonborn 4/4 agree with its key.tsv row; no other single code here has a key.tsv value (783, 867, 898, 714).

| 6 Oct 2026 R8-MANT | pooled single-code-gloss gate re-run, PREREG-MANTP + addenda (MANT463, MANT529) + PREREG-R8-MANT addendum 1 (86bb34ad2), 0527 run 7 code corrected 898 -> 848 from an image re-read (63 runs) | gloss strings permuted across all pooled single-code runs, 1000 draws seed 7101: mean 0.040, p95 0.167 | S 9/12 = 0.750 | **PASS** (R7-MANT529, before the correction: 0.667 vs 0.167). 898 "l'Empire" 4/4 single-code glosses on 0527 (x3) and 0529 (x1), both leaves HELD per leaf -> licensed **M** (per-unit merge rule) and added to key.tsv at M; 848 "Ilgen" single-attested, not licensed. 0527 per-leaf gate re-run: S 0.000 vs p95 0.057, HELD (S_single 2/2 at N 2, under the registered N >= 3). Outputs r8mant/*_r8.tsv |

Conflict 898 resolved as a misread, not a data conflict (R8-MANT, 6 Oct 2026): 0527 run 7's group is **848**, not 898. Two independent reads
of a native zoom (the worker's, and a blind Sonnet read given crop paths only) both give 8-4-8; the middle digit is this hand's open,
y-shaped 4 (as in 364 on the next line), while the leaf's undisputed 898 (f.422v L_L05) has a closed-loop 9 (as in 939). Both reads also put
"Ilgen" in the left margin, not over the code; the word over the code is unsettled (worker "l'Empire", blind read "Alexapice?", low), so the
run keeps its as-read gloss "Ilgen" (M, doubtful) on 848 under PREREG-R8-MANT. 848 occurs elsewhere only inside multi-code runs glossed
"... de l'Empire" (0527 run 18, 0529 run 6): a possible homophone or "l'Empereur", M, not tested here.

## Leaf 0530 (ff.425v-426) per-leaf gate and pooled gate with the leaf added (R8-MANT530, 6 Oct 2026, LANE LANE-RUN8-account-4, account 4)
| family | control | control result | target result | verdict |
|---|---|---|---|---|
| per-leaf gloss alignment (PREREG-MANT530, seed 530) | 200 gloss permutations across the leaf's 11 glossed runs | mean 0.017, p95 0.000 | S 1/3 = 0.333 (N_rec 3, floor) | PASS as registered, conditional: rests on run 5's M gloss (864 "le Roy de Prusse", worker zoom); passes' "le Roy de Suede" gives S 0.000 = p95, HELD |
| pooled single-code-gloss gate, 7 leaves (PREREG-MANTP + PREREG-MANT530 addendum) | 1000 permutations, seed 7101 | mean 0.036, p95 0.167 | S 9/12 = 0.750 | PASS, unchanged from R8-MANT; 357 Ilgen 3rd attestation; no code licensed that key.tsv lacks |

## Pooled multi-code-run aligner across the 7 glossed leaves (R9-MANTPOOL, 6 Oct 2026, LANE LANE-RUN9-account-4, account 4)
| family | control | control result | target result | verdict |
|---|---|---|---|---|
| pooled hard-EM multi-run aligner, key.tsv fixed (`interlinear_align.py --fix`, PREREG-R9-MANTPOOL) | 1000 gloss shuffles within code-count bins, seed 9501 | mean 14.93, p95 19 | S 24 free codes agreeing in >= 2 runs (of 87 recurring) | PASS, thin: ~15 expected by chance; known-answer 5/5 (letter codes only); 24 codes into key.tsv at M; first attempt with this instrument |

## Per-code shuffle test on R9-MANTPOOL's 24 codes (R9-MANTPC, 6 Oct 2026, LANE LANE-RUN9-account-4, account 4)
| family | control | control result | target result | verdict |
|---|---|---|---|---|
| per-code agreement A vs the same code's A under 1000 within-bin gloss shuffles (PREREG-R9-MANTPC, seed 9501, BH q 0.10) | power: 5 known-answer C codes unfixed, same test | 5/5 PASS (p 0.001-0.015, n 10-15) | 7/24 PASS (letter 4/18, word 3/6) | 237 341 402 451 588 592 714 kept M "per-code PASS"; 285 515 636 kept M (raw p < 0.10); 197 253 272 281 295 403 447 513 560 562 583 585 613 737 removed (raw p 0.10-0.91); low-n FAILs are closer to untestable than refuted |

## Per-code conflicts on the R9 codes (R9-MANTV verifier, 6 Oct 2026; rule 4)
| code | value in key.tsv (M) | competing witness | source | status |
|---|---|---|---|---|
| 714 | u (aligner, 3 of 5 runs; per-code PASS p 0.018) | 'une' in the other 2 aligned runs; 'un' as 0529 run 28's single-code gloss (M, single-attested) | r9mant/codes_r9.tsv; f424v_0529/leaf_values_0529.tsv | conflict: the value may be 'un'/'une' with the aligner splitting the tail to a neighbour; graded M, not settled by the majority chunk |
| 515 | e (aligner, 3 of 6 runs; raw p 0.037, BH FAIL) | 'p' in 2 runs; 'Pr' / 'propose' in f0501 word_values (inconsistent) | r9mant/codes_r9.tsv; f0501/word_values.tsv; RUN5-MANT5 flag | conflict: unresolved; weakest footing in the key |
| 402 | la (5 of 12; PASS p 0.003) | agrees: 0574 runs 10/16 '402.341 la guerre'; f0501 word_values 402 'la' | f463_0574/leaf_values_0574.tsv; f0501/word_values.tsv | corroborated, but the 0574 pair is one of the aligned runs (not independent) |
| 341 | guerre (5 of 6; PASS p 0.001) | agrees: 0574 '402.341 la guerre' | f463_0574/leaf_values_0574.tsv | same non-independence note as 402 |

## R10-MANT526 (6 Oct 2026, LANE LANE-RUN10-account-4, account 4): frame 0526 (f.422)
| date | family / instrument | control | target | result |
|---|---|---|---|---|
| 6 Oct 2026 R10-MANT526 | per-leaf aligner gate, PREREG-MANT526 (14 runs, 11 glossed) | 200 gloss permutations, seed 526: mean 0.025, p95 0.250 | S 0.250 (N_rec 4) | HELD (tie) |
| 6 Oct 2026 R10-MANT526 | pooled single-code-gloss gate, PREREG-MANTP + MANT526 addendum, 9 leaves (70 runs) | 1000 draws seed 7101: mean 0.026, p95 0.083 | S 0.667 (8/12) | PASS; 867 disagree (spelling only); sensitivity merging spellings 0.750, non-gating |
Witnesses logged, not resolved: 867 "le feld mareschal" (0526 single, C) vs "le Feldmarechal" (0529 x2, C) -- same title, two spellings;
0526 also writes "F.M." over 401.504.237.867. 714 opens "une conference" (0526 run 13, M placement) -- a further 'un/une' witness against
the aligner's 'u' (rule 4: graded M, not settled by the majority chunk).
| 6 Oct 2026 R10-MANT521 | per-leaf aligner gate, PREREG-MANT521 (frame 0521, 4 glossed pairs: 1 single, 3 lines of one run) | 200 gloss permutations, seed 521: mean 0.081, p95 0.250 | S 0.250 (N_rec 4, S_single N 0) | HELD (tie) |
| 6 Oct 2026 R10-MANT521 | pooled single-code-gloss gate, PREREG-MANTP + MANT521 addendum, 10 leaves (71 runs), MANT5 / rule SP | 1000 draws seed 7101: mean 0.026 / 0.029, p95 0.083 / 0.083 | S 0.667 (8/12) / 0.833 (10/12) | PASS / PASS; no licence changes; 160 stays disagree (mant / manteuffel) |
Witnesses logged, not resolved (R10-MANT521): 714 opens "un bon treve nous conviendra" (0521 run 4, gloss 'un' directly over 714, M) -- a
further 'un/une' witness against the aligner's 'u'; 160, Krauske's Manteuffel (C), also sits inside that run under the gloss 'treve' (M),
so in this run either 160 is a syllable code ('tre'/'eve') or the gloss is placed loosely; not settled here.

## Pooled multi-code aligner re-run with 0526/0521/0518 added (R11-MANTPOOL2, 6 Oct 2026, LANE LANE-RUN11-account-4, account 4)

| date / job | test | control | real | result |
|---|---|---|---|---|
| 6 Oct 2026 R11-MANTPOOL2 | pooled hard-EM multi-run aligner, 10 leaves, 122 runs, key.tsv minus R9 rows fixed (PREREG-R11-MANTPOOL2) | 1000 within-bin gloss shuffles, seed 9501: mean 17.47, p95 22; known-answer 5/5 | S 27 of 94 recurring | PASS, thin (second run of this instrument, both passed) |
| 6 Oct 2026 R11-MANTPOOL2 | per-code test (R9-MANTPC design), BH q 0.10 over 27 | same 1000 shuffles; power control 5/5 PASS | 5/27 PASS: 237 de, 341 guerre, 402 la, 592 s, 714 u | 451 u and 588 s PASS -> KEEP (p .025, .034); 285/515/636 KEEP; 214, 463, 548 new, FAIL |

Not resolved here (prereg: key changes only for codes that clear): 451 and 588 stay in key.tsv at M with the weaker verdict noted; whether a
code that loses BH significance when material is added should leave the key is an orchestrator decision. 714: 5 'u' vs 2 'une' chunks
(0521, 0526), the un/une conflict above, unchanged.
| 6 Oct 2026 R13-MANT85 | per-leaf aligner gate, PREREG-MANT85 (694/09 frame 0085, March 1713, 11 glossed pairs, letter range; runs 9+10 one pair) | 200 gloss permutations, seed 85: mean 0.310, p95 0.542 (secondary per-line pairing: mean 0.216, p95 0.438) | S 0.125 (3/24, S_single N 0); secondary 0.000 (0/16) | FAIL; nothing merges. Known-answer (not a gate): Krauske's letter table reads the glossed runs (la reyne, nous avons plus gagnes, k-r, g-r) -- table still in use in 694/09; 483/501/349 unglossed |

## MANT-0008 (8 Oct 2026, LANE FAMILY account 2): 694/09 frame 0008 gloss gate, and the rule-4 slots it raises
| family | control | control result | target result | verdict |
|---|---|---|---|---|
| Krauske key.tsv vs the leaf's own interlinear gloss, per-code DP alignment over 13 glossed runs (PREREG-MANT-0008, f0008_09/gloss_gate.py) | key values permuted over codes, 1000 draws, seed 8 | mean 31.66, p95 42, p99 46, max 57 | S 159/205 keyed codes (0.776) | PASS (S > p99 and >= 0.5 x keyed); 26 of 67 distinct codes matched on every instance |

Slots where the gloss reads a value Krauske does not give (rule 4: logged with both witnesses, key.tsv unchanged; each is one instance):
| code | Krauske 1893 (key.tsv) | 694/09 0008 gloss slot | context | status |
|---|---|---|---|---|
| 18 | null ("wahrscheinlich non-valeurs", brace 18-19) | q | G12 '29.18.67.25' under "...menaces qu'a..." (s q u a) | conflict, single instance; a null would leave 'q' unconsumed, which the DP also allows at -0.25 -- weak |
| 63 | null ("non valeurs?", brace 61-63) | ff | G05 '33.63.46.30' under "...offici..." (o ff i c) | conflict, single instance; gloss ending unread |
| 57 | s (C) | a | G02 '15.57.34' under "caprice" (c a p); every other code in G02 matched | conflict, single instance; 57 is also a reader split (57/59 on L02) and 57 misses twice more (G09 v, G12 t), so a misread 50 (= a) is as likely as a key difference |
| 130 | Walling (M) | 'Roy' by position (G09 '170.130.160.202' under "le Roy et la Pologne") | the DP scores names letters-only, so these name slots are positional only | listed, not scored as conflicts: 130 gloss Roy; 160 (Manteuffel, C) under "et"; 202 (la republique de Pologne, C) under "Pologne" (agrees in substance) |
Codes above 401 on the leaf: 503 and 399 (G08 run end, after "les forces" is fully spelled) and 297 (G10 run end, after "des troupes") sit under no gloss letters -- no value from this leaf.

### MANT-0609Y (9 Oct 2026, LANE FAMILY-A2d account 2): 694/09 file 0007 gloss pairs vs key.tsv (PREREG f0007_09/PREREG-MANT-0609Y.md)
| code | key.tsv | gloss reads | witness | status |
|---|---|---|---|---|
| 54 | u (C) | t | 0007 G01 '30.10.54.28.35' under "cette" (c e t t e); every other code in the run matched | conflict; second witness for 54 = t after f0008_09 G13-area slot (gate.out "54(u)=miss:t"), while 0008 also reads 54 = u twice (G04, G10). Reader split on 0007: 54 low, alt 59 (= t in key.tsv) under a stray diagonal stroke, so a misread 59 is as likely as a homophone; rule 4: not settled by count, key.tsv unchanged |
| 39, 46 | i, i (C) | 'Ilg' (worker) / 'Hy' (both blind passes) over single name codes | 0007 b2/b3/b5/b7 | initial agrees under the worker's reading only (single-letter key value vs a name gloss: weak class); under 'Hy' a conflict. Not settled |
| 44 | l (C) | 'Ld' over a single name code | 0007 b4 | initial agrees (weak class) |
| 54 | u (C) | t | 0056 G06 '43.66.9.28.60.35.36.6 / 54.67.27' under "maitre futur" (f u t u r); every other code in the run matched (MANT-0056, 9 Oct 2026; leaf gate PASS 69/77 vs p99 20) | conflict, now a third witness (0007, 0008, 0056) for 54 = t; still unresolved: key.tsv unchanged, not settled by count (rule 4); reader doubt on 0056: pass A '54?', pass B '54' |
| 205 | le grand général (C) | 'et' (of "eté") | 0056 G03 '...34.25.51.205.35.43...' under "pas eté mortelle"; 205 is crossed by a diagonal stroke (struck, or the gloss pen) and pass A read it '2?5?' | reading doubt, not logged as a key conflict: a struck token, possibly two groups; one instance |

## MANT-0056 gate row (9 Oct 2026)

| date / job | instrument | control | target | verdict |
|---|---|---|---|---|
| 9 Oct 2026 MANT-0056 | f0056_09/gloss_gate.py, PREREG-MANT-0056 (PREREG-MANT-0056 written to disk by 02:20 UTC before scoring (gate first run 02:22:59, file mtimes); NOT committed before scoring -- this worker's `tools/room.py "msg" --push <paths>` call committed ROOM.md only, so the file reached git with the results; rule-3 pre-registration breach in form, disclosed here, design copied unchanged from PREREG-MANT-0008): key.tsv vs 694/09 0056's own interlinear gloss, 6 spans, 78 code tokens, 77 keyed | key values permuted over codes, 1000 draws, seed 8: mean 11.61, p95 17, p99 20, max 24 | S 69/77 (0.896) | **PASS**. key.tsv unchanged; no candidate addition qualifies (406 is a null slot only, f0056_09/key_add_0056.tsv) |

## MANT-0063 gate row (9 Oct 2026)

| date / job | instrument | control | target | verdict |
|---|---|---|---|---|
| 9 Oct 2026 MANT-0063 | f0063_09/gloss_gate.py, PREREG-MANT-0063 (committed 9020d4bfb at 02:51 UTC by date -u, before the first score at ~02:53): key.tsv vs 694/09 0063's own interlinear gloss, 7 spans (3 French, 4 German), 36 code tokens, 36 keyed | key values permuted over codes, 1000 draws, seed 8: mean 4.75, p95 8, p99 9, max 12 | S 24/36 (0.667) | **PASS**. Secondary (exploratory): French spans 19/22 vs p99 7; German spans 5/14 vs p99 4 (under 0.5 x keyed). key.tsv unchanged; no unkeyed code in any span (f0063_09/key_add_0063.tsv header only) |

Rule-4 conflict (MANT-0063): | 84 | sch (key) | th | 0063 G03 '55.25 / 60.84' under "Barth:" (b a r + th); 55 25 60 matched | conflict, one witness; the gloss is an abbreviated name, so "Barsch" as the key gives it and "Barth" as the glossator wrote it are both plausible; key.tsv unchanged |

Exploratory, after scoring (not a gate, not grade-bearing): the key's own decode of the spans shows the gloss ink sits offset from the codes it glosses (abbreviated gloss, cipher continuing onto the next line): 103 17 26 after the ';' reads "le p r" (= the gloss "le Pr."); 3 66 51 8 50 [24] 28 reads "w a s h a [q] t" (= "Was hat", 24 unexplained); 120 34 15 8 = "d [p] c h" (gloss "Dich"; 34 would be i); 100 25 60 67 83 55 = "d a r u [sch] [b]" (cf. "darumb", 83 would be m); the C2 run 73 54 40 40 11 6 31 43 35 27 21 = "[s] u b [b] k u m m e r n" (cf. "zu bekümmern", 73 would be z, the second 40 e). 29 7 at the run start reads "s [g]" under "Si" (7 would be i). These six slots (7, 24, 34, 40 second instance, 73, 83) are flagged for a native eye re-check (possible misreads 9/7, 39/34, 10/40 not excluded) before any is treated as a rule-4 conflict; key.tsv unchanged.

## MANT-EYE63R (9 Oct 2026): 0063 flagged slots at native

| slot | transcribed (key) | alternative (key) | gloss | verdict |
|---|---|---|---|---|
| A1 tok2 | 7 (g) | 9 (i) | i | open: y-shaped glyph, neither this hand's crossed 4 nor its looped 9 |
| B2 tok2 | 84 (sch) | 89 (tz/z/s) | th | open; rule-4 conflict stands either way |
| C1 tok6 | 24 (q) | 29 (s) | s | open: same y-glyph; A2's '24' (crossed 4) reads q in "manquer" |
| C1 tok11 | 34 (p) | 39 (i) | i | open: same y-glyph |
| C1 tok19 | 83 (sch) | - | m/b | confirmed (low) |
| C2 tok4 | 40 (b) | 90 (c/ch) | e | open; neither gives e |
| C2 tok1 | 73 (s/z) | - | z | confirmed |

Gate unchanged (24/36 vs p99 9 PASS, `--check` exit 0); no token changed. The y=9 hypothesis is untested here: its only support on this leaf is
the gloss it would be scored against (circular). V-MANT08's two 4->9 corrections on 0390/0391 are the same confusion on other leaves. Test: a
pre-registered y-glyph census on leaves whose gloss is not the scoring target (eye63.tsv, NOTES "MANT-EYE63R").

### MANT-0136 (9 Oct 2026, LANE FAMILY-A2f account 2): 694/09 0136 P.S. ("chiffre ... celuy du proces"), PREREG f0136_09/PREREG-MANT-0136.md (committed d339fbe20 before scoring)

| date / job | gate | control | target | verdict |
|---|---|---|---|---|
| 9 Oct 2026 MANT-0136 (a), blind gloss pass A | f0136_09/gloss_gate.py --gloss gloss_A.tsv: key.tsv vs the r08 gloss, 1 span, 14 tokens, 13 keyed | key values permuted over codes, 1000 draws, seed 8: mean 1.74, p95 3, p99 4, max 6 | S 9/13 (0.692) | **PASS** |
| 9 Oct 2026 MANT-0136 (a), blind gloss pass B | same, gloss_B.tsv | mean 1.84, p95 3, p99 4, max 6 | S 8/13 (0.615) | **PASS** |
| 9 Oct 2026 MANT-0136 (b), unglossed tokens | f0136_09/judge_gate.py: fr18 4-gram of the key.tsv letter decode of tokens outside both gloss spans (62 letters); power control 0085 r9+r10 real -1.471 vs p95 -1.684 PASS | letter values permuted over letter codes, 1000 draws, seed 136: mean -2.017, p95 -1.759, p99 -1.675, max -1.554 | -1.401, 0/1000 permuted >= real | **PASS** |

Grades (grades.tsv): H 0, C 8, S 51, M 15, I 0, U 1 of 75. Rule-4 slots raised (M, not changes to key.tsv): 170 (key 'le') reads in
sense as a person twice ('faire obtenir a 170 la Livonie pour luy & pour ses descendens'; '170 comme bien d'autres auroit raison d'etre
sur ses gardes'); 66 = a in 'la Po[66]te a craindre' where sense needs r (worker eye: gloss 'r' under it, unscored); 20 = b in
'craindr[20]' where sense needs e (worker eye: gloss 'e', unscored); r09 'a ce p[6][29]nce' would need 6 = r, 29 = i ('a ce prince');
229 glossed 's' in both blind passes, most likely 29 (= s) with a struck 2. r01 (8 codes after 'negociation secrete de') and r02
(3 codes, subject of "m'en parla") decode to no French under the table: probably names spelt in letters or a nomenclator outside
key.tsv. Test: two further blind gloss passes at 3x on r07 under a PREREG amendment (would score 66, 20, 120, 26 against a gloss).

### MANT-R07 (9 Oct 2026, LANE FAMILY-A2f account 2): 0136 r07 + r08 gloss read blind, PREREG f0136_09/PREREG-MANT-0136-A1.md (committed 978bf33fc before scoring)

| date / job | hypothesis and data | control | target | result |
|---|---|---|---|---|
| 9 Oct 2026 MANT-R07 (a)-A1, blind gloss pass A1A | f0136_09/gloss_gate.py --gloss gloss_A1A.tsv: key.tsv vs the r07 + r08 gloss, 2 spans, 33 tokens, 32 keyed | key values permuted over codes, 1000 draws, seed 8: mean 4.19, p95 7, p99 8, max 11 | S 22/32 (0.688) | **PASS** |
| 9 Oct 2026 MANT-R07 (a)-A1, blind gloss pass A1B | same, gloss_A1B.tsv | mean 4.32, p95 7, p99 8, max 11 | S 21/32 (0.656) | **PASS** |

Rule-4 slots from both blind passes (M, not key.tsv changes): 20 glossed e (key b; 'craindr[e]'); 66 at 0136 r07.6 glossed r (key a;
'Po[r]te') -- both readers also saw the numeral as 68 there, so the slot may be a transcription question first; 120 glossed with an
unreadable curl (key d); 31 glossed n (key m) and 55 glossed h (key b|[a]) in r08 ('[c]omme [b]ien' expected; gloss 'o n m e h i e n');
229 glossed 'e s' (a struck 2 + 29 = s). Earlier candidates 6 = r / 29 = i (r09) untouched by this job.

## MANT-UNGL rule-4 slots (9 Oct 2026, 694/09 0103/0046/0233; M, not key.tsv changes)
- 0103 r02 '51.28.35.28.59' reads s t e t t under key.tsv only with 59 (= t); both blind passes 59 (alt 39), MANT-0609Y's eye 57 (= s);
  conf low. With r01 '110.17.33.13.31' = la p o m m, the pair reads as name stems 'la Pomm[erie]' / 'Stett[in]' (M, I for the
  identification). Not scored by gate (b): the fr18 4-gram gate FAILed on 0103 (power 0.92 at N=21), and its positive control is prose,
  not name stems -- a design mismatch logged, not a reason to re-run.
- 0103 r04 '44.33.12.8' = l o l h repeats 0136 r01's start '44.16.12.8...' = l o l h (o v e l): same unread name stem on two leaves (M).
- 0233 isolated codes 83 (key sch), 93 (key f|ff, x2), 59 (key t), 75 (not in key.tsv) and the run 4.10.11.2 (x e k e) do not read as
  letter values in context ('couronne de Suede. 83 donc a donne', 'on promet a 93 le gouvernement perpetuel du duche de Sleswig, et a
  4.10.11.2 20 m risdales', 'chez Gyque 59 a intercepte une lettre', 'de 93 a 75'): they behave as person/name codes; Krauske's table
  gives them letter values only. Open-codes for this clerk hand (the hand of 0136's "chiffre ... celui du proces").

## MANT-0454 (9 Oct 2026, LANE FAMILY-A2f account 2): rule-4 slots from 694/08 0454 (f0454_08/), no key.tsv change
- r03 '26.33.82.60.66.73.10.69.51.11.92' and r15 '60.33.82...' = r o z r a s|z e w s k y twice (26 and 60 both = r under key.tsv): the
  surname of Stanislas's envoy at Berlin, probably Rozrażewski (I for the identification; the two witnesses agree in letters 11/11, in codes 10/11).
- r12 '66.27.21.33.12.120' = a r n o l d ('continuer d'y employer le Sr. Arnold'); first code 66 (a) vs 68 (v) not settled on the image (M).
- r07 '60.35.14.16.21.30.35.50' = r e n o n c e a after 'en cas qu'il' and before 'et que [Roi de Suède] y consentit': sense 'renonçât';
  the last two codes give 'ea' with no t (M; a spelling or a dropped code, not a key change).
- r17 single '60' (key r|re|ro) in 'le pr. R. voiant le pr. 60 parler au Roi': a letter-valued code used for a person (M, open-code).

## MANT-NAMES136 (9 Oct 2026, LANE FAMILY-A2g account 2): name runs on 694/09 0136 and 0103, crib_list_fit.py (names136/), no key.tsv change
| date / job | hypothesis | control | control result | target result | verdict |
|---|---|---|---|---|---|
| 9 Oct 2026 MANT-NAMES136 | 0136 r01 '44.16.12.8.33.5.35.42' = Lölhöffel (Prussian resident in Poland) | C2 0136 r04 'livonie' (PASS 6/0 unique, P 0.000); N1 French window (no candidate) | gate met | strict list: no candidate; variant list (f->v chosen after seeing the decode): lolhovel unique, fit 7/0, P 0.000 | crib, **M**; external support: f.468 lone 44 'Lol.', 694/08 0370 'Mr. Lolhoffel' 6 Oct 1712, Heinsius XIV no. 142 |
| 9 Oct 2026 MANT-NAMES136 | 0103 r04 '44.33.12.8' = Lolh[ovel] abbreviated | same | gate met | too short for the rule (max fit 4 < 6); best 'lol' | **M**, same stem as 0136 r01 |
| 9 Oct 2026 MANT-NAMES136 | 0136 r02 '39.12.7' = Ilg[en] abbreviated | same | gate met | too short (max fit 3 < 6); best 'ilg' (f.468's 'Ilg.') | **M** |
| 9 Oct 2026 MANT-NAMES136 | 0136 r09 '50.15.10.17.6.29.14.30.35' = a phrase/name | same | gate met | no candidate; 'aceprince' 6-way tie at fit 3 | open, untested-by-this-tool beyond the fr18 list |

## MANT-0109 (9 Oct 2026, LANE FAMILY-A2g account 2): rule-4 slots from 694/08 0109 (f0109_08/), no key.tsv change
- r01 '11.60.66.6.28' = k r a u t ('entrevenu avec Kraut'); r03 '11.26' and r10 '11.27' = 'Kr.' abbreviations ('avant que Mr Kr.', 'soit a Kr.'):
  identification with the Prussian minister Johann Andreas Kraut (accounts, 'etats') is I.
- Name-abbreviation groups (PREREG rule): 55.44 x12 = 'bl' under key.tsv (55 = b|[a]; 'al' if [a]) and 7.60 x7 = 'gr' (60 = r|re|ro: 'gr'/'gre'/'gro'),
  two parties to the dispute over the accounts ('55.44 se retire tout camus chez luy'; 'Mr 7.60 ... une proposition a faire'). Who they are is
  open (I at best); candidates are not named here because no test was run on them.
- r18 '10.3.1.35.44.120.13.96.284.100.33.21.66.34.60.39.14.89.1000.260.259' = 'e w | f e l d m | le comte | d o n a | p r i n tz | et Kameke Ilgen',
  the commissioners named 'sur le champ' (Feldm[arschall] le comte Dohna, Printz[en], Kameke, Ilgen: identifications I; key 260 Kameke is itself M in
  key.tsv). The leading '10.3' ('ew') is unexplained (M; not a key change). 35 (e) and 33 (o) are low on the image (alt 55 each).
- r21 '103.7.60.66.21.120.31.50.9.28.26.10' = 'le grand maitre' ('d'un cote le grand maitre, qui sortant de son naturel ...'): which office-holder is
  meant is I.
- V-MANT0109 (verifier, 9 Oct 2026): every slot above is resolved in print -- Acta Borussica BO I (1894) Nr. 64 pp. 204-207 prints this letter
  (Berlin 4 June 1712) in clear: 55.44 = Blaspil, 7.60 = Grumbkow (also the period gloss over 7.60 on 694/09 0085), Kraut = Krautt, r18 = 'E. W. feldm.'
  (Wartensleben, editor's footnote) le comte Dhona, Printzen et Kameke, Ilgen; r21 le Grand-Maitre = Paul Anton von Kameke. Grade C against the print; see AUDIT.md.

## MANT-0453 (9 Oct 2026, LANE FAMILY-A2g account 2): rule-4 slots from 694/08 0453 (f0453_08/), no key.tsv change
- 170 (key.tsv 'le', Krauske's example word 'Roi') at "l'intention de 170 d'ajuster ainsi l'affaire": read in context as 'le Roi' (Augustus) beside
  150 'le Roi de Pologne' three times in the same paragraph; M, one occurrence; not a key change.
- 15.60.33.51.29.35 'crosse' at "l'article de ... etoit ajuste", with commissioners to examine "les endroits" on the spot: identification as
  Crossen (Krosno Odrzanskie) I, untested; 51 low (alt 57, also s).
- 0453 r04 tok5 '14' has a stroke through the 4 (a correction?); read 14 = n low; 'renoncer' reads either way only if 14 = n.
- Letter No. 88, Berlin 29 Oct 1712 (head on URL 0451 f.358) spans URL 0451-0454; 0454's reading and 0453's belong to it.

## MANT-CUC (9 Oct 2026, LANE FAMILY-A2h account 2): Krauske's table (key.tsv) against clear words written under code runs, 694/08 0323/0348/0282
PREREG-MANTCUC.md (4c5930db8, pushed before scoring); scorer mant0608/cuc/cuc_score.py; blind code passes A/B and one blind clear pass per leaf.
| date / job | hypothesis | control (1,000 permutations of key.tsv values, seed 6083) | target S (agreed tokens) | result |
|---|---|---|---|---|
| 9 Oct 2026 MANT-CUC | key.tsv letter values = the clear words under the runs, pooled 0323+0348+0282 | all-codes mean 16.0, p99 29; letter-codes mean 22.6, p99 36; 0/1000 >= real | 124/175 (0.709) | PASS (both controls); pass A 125/175, pass B 129/181, PASS |
| 9 Oct 2026 MANT-CUC | same, 0323 alone | all-codes p99 17; letter p99 19 | 62/82 (0.756) | PASS |
| 9 Oct 2026 MANT-CUC | same, 0348 alone | all-codes p99 9; letter p99 11 | 36/39 (0.923) | PASS |
| 9 Oct 2026 MANT-CUC | same, 0282 alone | all-codes p99 8; letter p99 10 | 26/54 (0.481) | PASS on the gate, but under the PREREG's 0.5 rate line; 10 of the 28 misses are two strips where the blind clear pass saw no underline ('-') |

## MANT-0176 (9 Oct 2026, LANE FAMILY-A2h account 2): rule-4 slots from 694/08 0176 (f0176_08/), no key.tsv change
- r02 '13.66.9.10.26' and r05 '13.66.9.2.26' = 'maier' (10 and 2 both e); the clear text of the same letter names 'la bibliotheque de Maier' in the
  affair of the commandant of Custrin and the prince's books: one person, M. Who Maier is, is I (not tested). Third digit 9 in both passes (alt 4;
  MANT-INV08B eye read 4 = x, which would give 'maxer'): low-cost image recheck owed before any identification.
- r02 trailing 36 (= f) after 'maier' ('que Maier f[?] enverroit'): does not read (M; B alt 56 = not checked against the key by the worker).
- r03 '51.17.50.[struck].44.120.1000.8.33.60.21' = 's|sa p a l d et h o r n' ('deux colonels, Spald et Horn jusqu'a ...'): two colonels' names, M/I;
  51 and 17 low on the image (A 51, B 5), 44 low (after a struck stretch). The struck stretch between 50 and 44 is not read.
- r04 '55.2.27.14.25.6.(7)' = 'b e r n a u (g)' ('jusqu'a Bernau ou je pourrois les faire venir a quelque village'): the place Bernau (by Berlin),
  I; final 7 low (a stroke before a blot, maybe punctuation).
- r01 '171.35.62' after 'le vieux' = 'le e [62 null]' does not read; worker's native look reads the last code 26 (and MANT-INV08B 17.41.35.26):
  the run is unsettled (M) -- who 'le vieux' is stays open.
- V-MANT0176 note (9 Oct 2026, verifier, M, no key edit): the cipher 'maier(f)' and the clear text's 'bibliotheque de Maier' are probably two people. The library is Dr J. F. Mayer's (d. 1712; 'des Hamburgischen Herrn D. Mayers Bibliothec, welche A. 1716 zu Berlin verauctioniret', IA 10123080bsb). The cipher name that sends two colonels to Bernau and whose 'certificat' is asked for reads best as Meyerfeldt (Swedish general, governor-general at Stettin 1712-13; Dumont, Corps universel diplomatique; Droysen IV.2 p.56). On that reading r02's trailing 36 'f' begins the name. Not confirmed by any print; the y-glyph (9/4) still conditions 'maier'. r04 pos 7: one blind look + verifier eye read a comma, not a digit ('bernau'). r01 pos 3: verifier eye reads 26 (with MANT-INV08B and the worker), not 62. See AUDIT.md 'AUDIT (V-MANT0176)'.

## MANT-0177 (9 Oct 2026, LANE FAMILY-A2i account 2): rule-4 slots from 694/08 0177 (f0177_08/) and the 0176 fix, no key.tsv change
- 0177 r01 '55.2.26.14.25.6' = 'b e r n a u' ('envoye quelqu'un a Bernau, pour s'informer si les colonels susdits y sont'): the same place as 0176 r04
  (55.2.27.14.25.6, now six codes after the fix); 27 vs 26 = two r homophones. M (gate (b) too-short on 0177); the clear context supports it (I).
- 0177 r02 and r04 '17.1' (twice: 'a ce que 17.1 me dit'; 'je tacherai d'exclure 17.1 du secret') = 'p f' by the letter table: a two-code name
  abbreviation of one person, recurring 2x (below the PREREG's >= 3 abbreviation rule, so scored as letters). Context: the person who came back and
  promised to bring the 'certificat' (0176), i.e. most likely 'le vieux' of 0176 r01. Unidentified (M/I).
- 0176 r01 (after the fix '171.35.26' = 'le e r' / 'leer'; 171 = 'le' as a word code) may instead be '17.1.35.26' with a dot the passes missed:
  then 'pf' + 'er', the same person as 0177's 17.1. Not tested; an eye check of the committed crop f0176_08/crops for a dot between 17 and 1 is owed
  before anything is read there (no transcription change by this job beyond the brief's two fixes).
- 0177 r03 '13' alone ('si 13 vouloit peut-etre me tromper') = 'm': one-code abbreviation, most likely the 'maier' of 0176 r02/r05 (13 = m is that
  name's first sign). M; who it is stays open (V-MANT0176's Meyerfeldt hypothesis neither supported nor weakened by 0177).

- MANT-0474 (9 Oct 2026): code 63 -- key.tsv null (Krauske 1893 f.3, brace 61-63 'non valeurs?', M) vs 694/08 0474 (stamp 379, Manteuffel to Flemming, ~Nov 1712) period gloss 'galere', where 63 sits at 'a' between matched 7 (g) and 103 (le); one instance, token low (A 76? / B 7.63?). Rule-4 conflict logged, both witnesses kept, key.tsv unchanged (f0474_08/candidates.tsv).

### V-MANTC (9 Oct 2026, verifier, account 2, LANE FAMILY-A2j): rule-4 conflicts 19, 63, 54 (AUDIT.md "## V-MANTC (9 Oct 2026)")
| code | key.tsv | witnesses (leaf, slot, dir/date) | V-MANTC finding | status |
|---|---|---|---|---|
| 19 | null (M) | 0398 s02 'Polonois' n; 0410 s02 'Han.' n and after 'l'E' (F->M, Oct 1712); 0494 T039/T091 dec/null (M->F) | the 0398/0410 second digits are the y-shaped 4 (as '44' on the same strip); 14 = n fits both n slots | not established as a conflict; probable 14 misreads; native re-read owed; key unchanged |
| 63 | null (M) | 0474 T032 'galere' a (M->F, Nov 1712); 0008 G05 'offici' ff (M->F, Jan 1713) | 0474's second digit is crossed by gloss ink, not a legible 3; 66 = a fits | 0474 withdrawn; 0008 single instance stands, unsettled; key unchanged |
| 54 | u (C -> **M**) | u: Krauske; 0474 T052/T103/T107; 0494 T063, T151; 0008 G04, G10. t: 0494 T149 ('touchant', eye 54), T035 ('Détaché'); 0007 G01; 0008 G01; 0056 G06 -- all M->F, Nov 1712 - Jan 1713 | same direction and dates for both values, same word on 0494; 0494 T134 is a 59 misread (eye), not a witness | data conflict, not settled by count; key.tsv grade lowered C -> M (V-MANTC) |
| 84 | sch (C) | 0089 T020 at the tail of the run glossed 'Keuk?' (blind pass; worker eye 'Kreutz'; Acta Borussica BO I p.208 names Creutz for the 31 May 1712 dispatch) (M->F, 31 May 1712) | second glyph y-tailed (4|9 open), so 84 itself is low; sch vs tz both plausible as a name ending | logged by MANT-0089 (9 Oct 2026), single instance, key unchanged |

## MANT-0290W (9 Oct 2026, LANE FAMILY-A2k account 2): word/syllable codes 281-674 on 694/08 0290, cross-leaf note consistency (PREREG-MANT0290W.md)

| hypothesis | control | target | verdict |
|---|---|---|---|
| 0290's unkeyed codes carry the same note on other leaves | notes shuffled over tokens, 1000 draws, seed 2900: p99 0, min = max = 0 | K 1 (583 only; 0494, no shared word), S 0, both passes | untestable on disk (K<5), non-test (control cannot move) -- not refuted |
| method check: keyed names on 0290 match their notes elsewhere | p99 3 (A) / 5 (B) | 4/6 (A), 6/7 (B) | PASS (known-answer only) |

## V-MANTH (9 Oct 2026, verifier, LANE FAMILY-A2k account 2): held name/word codes pooled across leaves (AUDIT.md "V-MANTH"); key.tsv unchanged

| code | supporting witnesses | conflicting witnesses | verdict |
|---|---|---|---|
| 321 | 0312 A12 'Stockolm'/'Stockhol' (16 Sept 1712; low digits) | 0530 f.425v L_L01 321.237.402... under 'frontiere de la v en bu r' (24 Nov 1712; table identity of 0528-0530 open) | **held, open, M**; not keyed |
| 191 | Krauske f.4 Stenbock; f.468 x3 'Stenbock' (Dec 1712, control cleared); 0312 A17/A18 'Steinbock' (Sept 1712, gate PASS) | none (spelling only; y-glyph: written '1y1') | M kept (verifier may only lower); raise is the lane's call |
| 254 | -- | -- | not a separate code: 0136 R10/R13 passes read 259 = key Ilgen (M); the 254 settlement rests on y = 4; second witness for 259 under y = 9, open until the y-glyph census |
| 199 | none with a value | 0502 F2-13 '1y1y' vs copy f.409v 99 | held, no value, M |
| 42 | Krauske l; contexts 'plus contre' (0494 L07, f.410 L06), 'mais lu[i]' (0494 L17, f.410 M4) | 0314 R11 n slot in 'la couronne' (both gloss passes) | **conflict, open**: key l C stands, 0314 R11 M; not settled by majority |

## MANT-0181 (9 Oct 2026, LANE FAMILY-A2l account 2): rule-4 slots from 694/08 0181+0182 (f0181_08/), Flemming to Manteuffel 6 July 1712, no key.tsv change
Gate (b) VOID under PREREG-MANT0181 (the shuffled-target decode beat the key-permuted p95 on 13 of 100 orders), so every slot below is M by the key
alone (worker's eye, not a gate). The decode is read under Krauske's table for Manteuffel's reports; this leaf is the OTHER direction (Flemming to
Manteuffel) -- that the same table reads it is itself a hypothesis these slots support but do not test.
- r04+r05 '5.9.25.13 | 27.35.7.9.25.13' = 'viam regiam' and r10+r11 '5.9.25.27.35.7 | 39.66' = 'via reg ia': the Latin via regia (royal highway),
  twice ('on veut seulement laisser [viam regiam]'; 'aux preuves qu'ils nous ont [acceptees] autre fois et a cette [via regia]'). Two spellings of
  the same phrase with the same codes = a two-context reading (rule 4a's D1/D2 criterion), still M without a gate. r11.1 39 is blotted (low).
- r06 '17.35.9.28.12' = 'p e i t l' and r07 '15.16.28.40.6.29' = 'c o t b u s': Peitz and Cottbus, the Prussian enclave in Lower Lusatia; r06.5 12
  is low (passes 12/11, the 2 runs into 'et'); 'Peitz' needs a z, not in the leaf's reading of 12 = l -- open (a misread digit, or a z-sign Krauske
  did not list). 'on rejette aussi [Peitz] et [Cottbus]' (M/I).
- r08 '13.25.14.29.1' = 'mansf': Mansfeld (most likely the county; M/I), 'rejette aussi [Mansf.]'.
- r09 '25.90.2.17.28.10.35.29' = 'a c|ch e p t e e s' -> 'acceptees' ('aux preuves qu'ils nous ont [acceptees] autre fois'). 90 = c|ch (key M).
- r02 'gr. 90.25.14.15' = 'gr. c a n c' -> 'le gr[and] canc[elier]' ('dont il faut parler avec le gr. canc.'): the grand chancellor (of Prussia?
  Saxony?) unidentified. r03 '15.26' = 'c r' (a name abbreviation, unidentified). r01 '12.16.44' = 'l o|ou|ous l' unread (follows a struck word).

## MANT-66 (10 Oct 2026, LANE FAMILY-A2m account 2): code 66 'Alefeld' on 694/08 0151 vs key.tsv 66 = a; no key.tsv change
- Witnesses for 66 = a (letter): every glossed spelled run on disk (f.463 x6, f.426, f.467, 66.60.21 'Arnh:' 0309/0312/0314/0375, and 0151 L
  66.8.44.1.2.12.120 = a-h-l-e-f-e-l-d under the 'Alefeld' gloss). No witness for 66 as a name code: the 0151 L gloss renders the spelled group.
- Standalone 66 = initial 'A.' (f.468 'Arn' x2, GAPS154; 0151 R '66. avoit ose' under 'Alefeld', eye only, M), the folder's single-letter-initial
  practice (9 Ilgen, 44 Lol.); referent fixed by context per letter, not a conflicting key value. Not a rule-4 data conflict. Open: 0151 R crop.
