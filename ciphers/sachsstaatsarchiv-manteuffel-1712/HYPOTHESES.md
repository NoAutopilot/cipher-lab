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
