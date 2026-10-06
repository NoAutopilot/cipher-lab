# AUDIT -- rah-juan-manuel-1521

## R12-RJMV, 6 Oct 2026 (12:18-12:22 UTC): standing of R12-RJM42's held-out test of Tomokiyo's letter alphabet on R9502 f.40/f.42
Verifier session, separate from the solver (R12-RJM42, results commit 30d632ed6, PREREG commit 622a572e0). Brief:
.claude/briefs/runs/2026-10-06-account2-run12-jobs.md job R12-RJMV. This section rates a *test result*, not a reading: there is no
reading of any of the 28 letters yet, so no N-class or depth is assigned. Requests: de-crypt.org 4 (one browser login, RecordsView 9502,
full-size P1 and P3); no other host. Images in the scratchpad only; both sha1s match images/manifest.json
(P1 53ff7123..., P3 c9b31254...). Crops re-cut with the solver's own pasted commands (30 and 27 crops, same counts).

| check | finding | standing |
|---|---|---|
| PREREG before the scored run | 622a572e0 (author 12:02:19 UTC) adds only witness/PREREG_f42.md and scripts/test42.py; the outputs (results_test42.json, passes/align_f40_f42.tsv, ciphertext_f40_reconciled.tsv) and the three pass files first appear in 30d632ed6 (12:05:57), a descendant on main. `git diff 622a572e0 origin/main -- scripts/test42.py witness/PREREG_f42.md` is empty: the script that ran is the one pre-registered. Git can show the order of commits, not that the run itself happened after the push; nothing in the history contradicts it. The PREREG's two prose slips (time "12:1x", incipit "32 letters") are already recorded in NOTES.md; the script's 33 is the right count for "Esta otra letra se cerro anoche y no pudo". | holds |
| Reproducibility (rule 7) | `python3 scripts/test42.py --check` -> "up to date", exit 0 (12:20 UTC). Calibration 132/210 = 0.629 (gate 0.50); Tomokiyo S 0.276 vs control max 0.172 (N 134 scored, rank 1 of 201); alphabet.tsv S 0.156, FAIL. | holds |
| Leaf naming | P1 right page carries the folio number "40" top right and is the cipher (20 cipher lines, a 4-line clear passage naming "Rodrigo Niño" come "de Napoles", 6 cipher lines). P3 right page carries "42" and is the clerk's decipherment, headed "De don Joan manuel de Roma 8 de março 522", with "Claro" where f.40's clear passage stands. DECODE record 9502 gives "Signatura 9/23, f. 40-42", Status "Non-decrypted". NOTES.md's naming (f.40 cipher, f.42 decipherment) is right. | holds |
| Printed incipit kept out | Tomokiyo prints only line 1 of this letter's decipherment. The scored set drops cipher crop line 1 and any token whose chunk starts inside the first 33 gloss letters. The gloss reader wrote "screvio" for "se cerro" (both 7 letters), so the letter offset still ends exactly at "pudo"; in align_f40_f42.tsv line 1 ends at i=26 "pudo" and line 2 starts on "pa(rtir)". 9 symbol tokens excluded, 149 left (134 carrying a Tomokiyo label). | holds |
| Control can vary (rule 3) | The alignment is fixed and the 200 controls permute Tomokiyo's 12 values among the same 12 labels. The labels have different token counts (F 31, A 22, Z 22, 4 21, T 20 ...) and different chunk distributions, so a permuted key scores differently on S, and does (mean 0.064, max 0.172). This is not the AX-5799/bCAS shape: the manipulation (which value sits on which label) is the very thing S measures. Residual weakness, already reported by the solver: the null value '' sits on F, the most frequent label, and 29 of 149 chunks are empty; the solver's post-hoc F-removed rerun (0.257 vs 0.171, N 105) shows the pass does not rest on F alone. | holds |
| Alignment, opened against the crops and f.42 | 22 symbol tokens checked by eye (crops f40_L02, L08, L09 beside f42_L02-L03, L08-L10, plus the reconciled TSV for lines 3, 7, 10, 13, 30). **Right** (chunk = the clerk's letter at that place): i46 4=o and i47 F='' ("malo /"); i52 4=o ("duda / o en"); i148 R=s ("las cosas"); i160 Q=y ("manera / y el"); i177 Z=r and i180 R=s ("hartos"); i199 Z=r and i200 A=a ("enbiara"); i214 R=s ("los alemanes"); i218 Q=y ("y quiere"); i268 Z=r, i269 A=a ("enbiara"); i274 A=a ("de la gente"); i546 Z=r ("ser"); i552 Q=y ("y hame"). **Shifted by one letter** (wrong chunk): i32 F='o', i33 4='y' at "correo / oy" (true F='' at the clerk's virgule, 4=o); i159 F='ra' at "manera /" (code koh took only "mane"); i186 F='el' at "oficiales / el card." (true F=''); i203 R='di' at "los diez" (true R=s, lo=lo); i217 F='s' at "alemanes y" (ges took only "e"). **Uncertain**: i59 4='uy' ("es muy niño"?, the clerk's word not settled). | 15 right, 6 shifted, 1 uncertain |

What the alignment check says about the number. Every one of the 6 shifted tokens is a miss for Tomokiyo's value where the true
chunk would have been a hit (F='' at a virgule four times, 4=o once, R=s once): the aligner, which is prior-free and saw no letter key,
tends to give the null sign F a neighbour's letter rather than an empty chunk. So the 0.276 is, on this sample, an undercount for
Tomokiyo's key, not an overcount, and the misalignments do not favour it. The clerk writes a virgule "/" in f.42 at each place checked
where F stands in f.40, which fits Tomokiyo's F = null (a pause/separator sign) better than alphabet.tsv's F = i. None of the 22 tokens
shows an alignment that hands Tomokiyo a hit he should not have.

Limits (stated, not failures of the test). (1) "Held out" means held out from *our* keys and from Tomokiyo's printed incipit; Tomokiyo
says he built the table "mainly" on R9528 and checked it against first lines, so he may have looked at more of R9502 than he prints --
for licensing the use of his key that does not matter, but the test is not evidence that his table was built without this page.
(2) Reader error is 0.28 (err_true unmeasured); the PASS is at that error, with 128 split symbols left as ~. (3) Only A, Z, R, 4 and F
carry the result; T (0/17, Tomokiyo s), 9, X, 3, E, V (0 of 2-5 each) have no held-out support, and Q (no value in either key) takes y
4/8 -- consistent with Tomokiyo's y = "venus" sign (our K), a K/Q look-alike the sorter already lists.

Standing: R12-RJM42's PASS stands. The PREREG precedes the results in the history, the script reproduces the committed numbers, the
control can and does vary on S, the incipit is out of the scored span, the leaf naming is right, and the alignment errors I found
cut against the published key, not for it. alphabet.tsv's FAIL on f.40 (0.156) also stands.

Is a decode of R9501 with the published key licensed? **Yes, as a trial decode, with limits.** A decode of R9501 f.34 with
key_tomokiyo_alpha.tsv (key source `published`, Tomokiyo credited) plus the nomenclator is licensed by this test. Per-token grades: S
at most for tokens of the five labels that cleared here (A, Z, R, 4, F); M for T, 9, X, 3, E, V, Q and every split ~ token; nothing at
H or C (R9501 has no period decipherment in DECODE). The decode needs its own two blind passes, `tools/judge_plaintext.py` with a
shuffled-target decode through the same judge (rule 3, ARM-C1), and a rule-7 decode script with `--check`; until then nothing about
R9501's content is stated outside the repository. This test does not license changing alphabet.tsv's grades or replacing it.
Over-claims found: none in NOTES.md's R12-RJM42 section; its wording ("lands on the clerk's letters well above every permuted
control at reader error 0.28") is accurate.

## R13-RJMV, 6 Oct 2026 (13:19-13:3x UTC): standing of R12-RJM9501's R9501 f.34 trial decode with Tomokiyo's published key
Verifier session, separate from the solver (R12-RJM9501) and from R12-RJMV's solver. Brief: .claude/briefs/runs/2026-10-06-account2-
run13-jobs.md job R13-RJMV. Requests: none to any host (all checks on committed files; the R9501 image was not re-fetched). PREREG for the
shuffled spread: PREREG-R13-RJMV.md, pushed (df0591f6) before the scored run. This section rates a trial decode, not a reading of a
letter: no N-class or depth is assigned (none was before; the evidence below does not require one).

| check | finding | standing |
|---|---|---|
| Which leaf was read | images/manifest.json: IMG_R9501_I44762_P1.jpg, sha1 b510ebe5558b..., 3392x2436, record R9501, "f.34 (cipher)" (RUN1-SEG, 4 Oct); the solver's NOTES report the same sha1 for its fetch. images/crops_f34_manifest.json cuts every crop from that file. DECODE's listing (sources/decode/records-non-decrypted-2026-09-24.tsv) gives R9501 = "Signatura 9/23, f. 34-36", 3 images, so P1 is f.34. Content check: pass A's lower-case code words on lines 1-14 match the independent FT-A transcription of R9501 f.34 (ciphertext_f34.tsv) in order on the same line 120 of 147 times, against 13 (R9502 f.40 pass A), 17 (R9528 f.194) and 9 (R9526 f.147). The "f.40" in the solver's session summary is a slip (f.40 is R9502, the leaf of R12-RJM42's held-out test, which the decode script's docstring names); no committed file calls R9501's leaf f.40. | f.34 holds |
| Reproducibility (rule 7) | `python3 scripts/decode9501.py --check` -> "up to date", exit 0 (13:2x UTC). | holds |
| Grades inside R12-RJMV's licence | Of 753 tokens: S 309 = 169 agreed nomenclator codes + 140 agreed symbols, all of A/Z/R/4/F (Z 47, A 40, R 29, F 15, 4 9); M 113 = 51 codes one pass read + 62 agreed symbols of T/9/3/E/X/V; U 331 (218 split ~ plus 2 agreed-split, 101 out-of-table groups, 10 unvalued symbols). Script check over every row: 0 tokens at H or C, 0 S on a label outside A/Z/R/4/F, 0 S on a split or one-reader token, 0 agreed A/Z/R/4/F tokens below S. Split symbols sit at U, one step stricter than the licence's M. | 0 outside licence |
| Judge, re-run | es1600 target -1.128, seed-1 shuffle -1.208; es17c target -1.067, seed-1 shuffle -1.129: all four reproduce the solver's numbers exactly. All FAIL against real_p05 (-0.839 es1600, -0.884 es17c). | holds |
| Shuffled spread, 20 seeds (PREREG-R13-RJMV.md; scripts/shuffle_spread9501.py --check exit 0; results_shuffle_spread9501.json) | es1600: shuffled min -1.274, mean -1.214, max -1.169, sd 0.027; target above all 20 (z 3.2 vs mean, 1.5 vs max). es17c: min -1.198, mean -1.147, max -1.108, sd 0.024; target above all 20 (z 3.4 vs mean, 1.7 vs max). Seed 1 reproduces reading_f34_shuffled.txt byte for byte. | see below |

What the spread changes. By the pre-registered rule the judge does see token order in the decode on both corpora (rank 1 of 21,
empirical p < 0.05): the decode's sequence scores higher than any of 20 reshuffles of its own tokens. The solver's sentence "this judge
barely separates the decode from its own shuffled control" rested on one seed and understates that; the margin is small in absolute
terms (0.04-0.08 above the shuffled max) but clear of the spread. What it does not change: the target still FAILs real_p05 by 0.29
(es1600) and 0.18 (es17c), with 44% of tokens unread and no 1520s Spanish corpus on disk, so "judge cannot decide" stands as the
summary -- the order signal is a reason the decode is not noise in sequence, not a PASS and not a reading of the letter.

Limits, stated. (1) The 140 S symbols include 15 F, which Tomokiyo reads as a null: they carry no plaintext letter, so S counts tokens
graded, not letters recovered (125 S symbols yield a letter). (2) "Cardenal de Medi[ci]s" in NOTES.md is an inferred repair of the
table's "Medins" (grade I in prose, not in the grade file, where the code is S as written); NOTES already marks it with brackets.
(3) err_2reader 0.338, err_true unmeasured: the trial decode is at that reader error. (4) The order signal partly reflects the
nomenclator's set phrases ("vuestra magestad" x9 reads as one code pair in sequence); it is not evidence for the letter alphabet's
values on this leaf, which have no held-out test here.

Over-claims found: none that states content outside the repository. One under-statement corrected in NOTES.md (dated verifier note
below the R12-RJM9501 section): the one-seed "barely separates" is replaced by the 20-seed figures. No reading, key or grade changed by
this audit. SECOND-OPINIONS-QUEUE.tsv: no row for this target (none filed; no N3+ reading exists), so nothing to propagate.

## R13-RJMV2, 6 Oct 2026 (13:57-14:1x UTC): standing of R13-RJM34LA's f.34 look-alike pass and decode rerun, and the J-initial regrade
Verifier session, separate from every solver (R12-RJM9501, R13-RJM34LA) and from R13-RJMV. Brief: .claude/briefs/runs/2026-10-06-account2-
run13-jobs.md job R13-RJMV2. Requests: de-crypt.org 2 (one browser login: RecordsView 9501 + full-size P1, sha1 b510ebe5... = images/
manifest.json); image and crops in the scratchpad only (RUN1-SEG's iiif_lines command, 30 crops). No subagent. This rates a trial decode,
not a reading of a letter: no N-class or depth assigned (none was before; the evidence does not require one).

| check | finding | standing |
|---|---|---|
| PREREG before the re-reads | lookalike/PREREG_f34.md is on main from a15348c2d (13:45:37 UTC push order), byte-identical to today's file; the re-read and its outputs (f34_reread.tsv, passD, the _la results) first appear in 69f3548a6 (13:52:36). The hash the solver cites, 21427aac9, does not resolve on main: its local commit was folded by room.py's rebase into another session's commit (CLAUDE.md rule 6's known shape). | order holds; cited hash corrected to a15348c2d |
| Reproducibility (rule 7) | decode9501.py --check and decode9501_la.py --check exit 0 (before and after this audit's exception). | holds |
| Grades vs R12-RJMV's licence (solver's rerun, 753 tokens) | S 309 = 169 agreed codes + 140 agreed A/Z/R/4/F; every look-alike-settled token at M (48) or U (120), none S; 0 H/C; 0 S on a split, one-reader or non-licensed label; 0 agreed A/Z/R/4/F below S; S unchanged by the pass (0 tokens moved in or out of S). | 0 outside licence |
| Residual wording | NOTES and the PREREG report 0.065/0.066 as "agreement among three machine readers, not reader error and not true error" and name the 62 one-reader settlements as weaker. | correct (Usage 6) |
| J-initial pointer, eye check | All 8 S-graded places (L02.8, .11, .15; L04.7; L05.16, .19; L23.15; L27.16) and the 2 M places on L30 (.14, .17) read at 2x: each is one group, a tall capital J (flat top bar, vertical stem, large leftward hook below the line) joined to as/ez -- "Jas sad Jez" (L02, L05, L30), "dim Jas g dim" (L04), "gap Jez fop" (L23), "lal Jez bla" (L27). The Z sign (yogh, r) on the same lines is small and slanted, written apart: L05 "g D Z A Jas", L23 "fop Z cao". jas (parti) and jez (para) are table codes. | pointer confirmed |

Regrade applied (the brief allows it): lookalike/f34_exceptions.tsv (one rule, 10 places) merges each "Z as"/"Z ez" into the table code
jas/jez at M (one eye, not two blind readers; never S). decode9501_la.py reads it after passD and exits if a row does not match. Before ->
after, rule 4: **S 309 / M 161 / U 283 of 753 -> S 301 / M 169 / U 273 of 743** (8 S yogh tokens out; 10 codes in at M; 2 M yogh and 10 U
as/ez merged away). H 0, C 0. Line 2 now reads "... que vuestra magestad _ de parti da para _ y para ...". decode9501.py and its outputs are
untouched (the pre-pass record stays as R12-RJM9501 and R13-RJMV rated it, with S 309 there now known to include 8 code initials).

Judge after the regrade (same 20 shuffled-order seeds, results_shuffle_spread9501_la.json):
```
es1600: FAIL score=-1.103, real_p05=-0.833   shuffled -1.267..-1.169 (mean -1.208, sd 0.026), target above all 20
es17c:  FAIL score=-1.065, real_p05=-0.858   shuffled -1.198..-1.096 (mean -1.145, sd 0.023), target above all 20
```
Up from -1.129 / -1.093 (solver's rerun) by 0.026 / 0.028, about one shuffled sd; still FAIL by 0.27 / 0.21. "Judge cannot decide" stands.

Pointers, not applied: L04.1 "Z ul" and L23.5 "Z ump" look J-initial on the image too ("Jul", "Jump"), but jul/jump are not table codes,
so they stay as read. Other "Z + lower-case group" pairs in the rerun, not eye-checked here: L24 "Z um" (jum = otra is a table code, the
likeliest further merge), and L03 "Z bay", L07 "Z suf", L26 "Z log"/"Z bo", L29 "Z bay"/"Z geb" (no j-code in the table). No "Z as"/"Z ez" is left.

Over-claims found: none that states content outside the repository. Corrections: the PREREG hash in NOTES.md (21427aac9 -> a15348c2d), and
the S count after the J-merge (NOTES verifier note). SECOND-OPINIONS-QUEUE.tsv: no row for this target (no N3+ reading), nothing to carry.
