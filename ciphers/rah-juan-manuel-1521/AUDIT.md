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
