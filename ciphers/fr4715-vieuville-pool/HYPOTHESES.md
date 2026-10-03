# fr4715-vieuville-pool -- hypothesis families (append-only)

CLAUDE.md rule 3: CONTROL and TARGET numbers side by side. Created by LIKELY-1, 2 Oct 2026 (account-4). The pool's
key of record is `ciphers/fr4715-montholon-1589/keys/key_vieuville_nevers.tsv`; no.58's own rows live in that folder's
HYPOTHESES.md.

| Leaf | Family | CONTROL | TARGET | Status | Reason |
|---|---|---|---|---|---|
| no.44 f.67r | key_vieuville_nevers.tsv applied to the leaf's in-key groups; French word-cover of the decoded runs vs 200 letter-shuffled keys (scripts/keytest.py, LIKELY-1, 2 Oct 2026) | no.58 dump (Tomokiyo's groups, same key, same scorer): full N 818 letters, real 0.891 vs shuffles mean 0.353 max 0.631, z 5.37, rank 1 of 201; subsampled to 200 windows of 8 in-key groups x 20 shuffles: real mean 0.816 vs shuffle mean 0.355, real above the shuffle mean in 195/200 windows, rank 1 of 21 in only 85/200 (11/200 windows have a shuffled key at 1.0) | 28 cipher groups, 8 in key (L01: 25 93 84 25 50 93 25 95 -> ausaluat), 4 unbarred out of key (6 7 14 15), 11 barred word-codes, 4 pass disagreements, 1 date numeral; cover 6/8 = 0.750 vs 200 shuffles mean 0.326 sd 0.293 max 1.000, z 1.45, rank 43 of 201; vs the first 20 shuffles max 0.875 (not rank 1) | **non-test at N=8 (not a negative)** | the target sits where 97.5 pct of known-good 8-group windows sit (above the shuffle mean) and where the rank-1 gate has 42 pct power; the leaf's cipher content is the word-code layer (13 barred groups), which the letter key does not cover; next: a stronger clear-French pass to read the word-codes from context, then no.37 f.60 (dense) the same way |
| no.44 f.67r | word-code context read (pass C, Fable 5.1 blind, 4 calls; pass D, call 5; GAPS-fr4715-vieuville-pool, 2 Oct 2026) -- no family run, a rule-4 data-conflict record | no.58's dotted codes glossed by Tomokiyo (fr4715-montholon-1589/scripts/decode_rest.py OWN_GLOSS, grade M): '27 = les, '25 = la | this leaf's clear context (witness/f67r_wordcodes_context.tsv): .27 and .25 both fill a masculine-subject slot ("Que sy [.27] a quelque desir ... quil se resolue", "Que sy [.25] peult aller [.49] ... luy"), where les/la cannot stand | CONFLICT, unresolved; both values graded M at best in either letter, neither applied here | two H/M witnesses disagree on one code (rule 4): no.58's mark is a dot over the first digit, this leaf's is a bar over both; whether bar and dot mark two lists (names vs common words, nevers.htm's fr.3633 description) is an inference for the no.37 f.60 step, whose period partial decipherment can settle it at grade H |

| no.37 f.60r + no.44 f.67r | period interlinear glosses on no.37 (the dépouillement's "en partie déchiffrée") read as the known answer for the word-code layer; tools/interlinear_align.py --floor 1 over witness/f60r_pairs.tsv; gloss class vs no.44's slot classes, scripts/wordcode_slot_test.py (GAPS-fr4715-vieuville-pool-2, 2 Oct 2026) | 20 value-shuffled glosses (every row of key_wordcodes_f60r_all.tsv permuted among the codes): mean 3.20/7 slot fits, max 6/7, 4 of 20 at or above REAL | REAL 6/7 = 0.857: .7 = Roy (C) fits all four .7 person slots, .71 = montolon (C) the informant slot, .27 = nauarre? (M) the "Que sy [X] a quelque desir" slot; .25 = de? (L) no fit; align: 7 and 27 agree at two sites each, 99 conflicts (bou vs bours) | NOT A PASS at N=7 (p about 0.2); values carried to no.44 at M | the same code glossed the same way twice on the leaf is the evidence, not the shuffle margin; .27 = nauarre? against Tomokiyo's '27 = les on no.58 is a second period witness in the conflict row above |
| no.37 f.60r (four L-grade gloss sites) + no.44 f.67r | tall native crops of the four sites re-read in one strong-model call (scripts/cut_f60r_gloss_sites.py; GAPS-fr4715-vieuville-pool-3, 2 Oct 2026); slot test re-run (scripts/wordcode_slot_test.py --shuffles 20) | 20 value-shuffled glosses: mean 3.20/7, max 6/7, 4 of 20 at or above REAL (unchanged) | REAL 6/7 = 0.857 (unchanged). Values moved: .25 de? L -> de M (text clear, sits over the 25/50 boundary); legat M with the text now clear, spans 23 30; L01 'labr' M (not cut on the tall crop) with a third word ?gal? over 50 90; L20 du/dn is over the dotted 16, not the barred one; L22 'pen?' is an interlinear insertion 'peu de', not a gloss | NOT A PASS at N=7 (unchanged); no decode-key value changed | .25: no.58's Tomokiyo gloss '25 = la and this leaf's 'de' are both common words, against no.44's person slot "Que sy [.25] peult aller"; the conflict row above stands, now with a period witness on .25 too (group cover M) |
| no.37 f.60r dense block L06-L14 | key_vieuville_nevers.tsv on the block (two blind Opus passes, 93.2 pct agreement, 98 disagreements reconciled; inventory-only segmentation incl. the 8-as-0 rule); keytest word-cover vs 200 letter-shuffled keys; judge fr16 (GAPS-fr4715-vieuville-pool-4, 2 Oct 2026) | no.58 dump same key and scorer: 0.891 vs mean 0.353, z 5.37, rank 1/201; judge: no.58 decode of the same design N=604 FAIL -1.056 (known text PASS -0.844) | 604 letters: 0.793 vs mean 0.331 max 0.604, z 5.11, rank 1/201; judge FAIL -1.275 (shuffled-token decodes -1.92..-2.01) | key reads the block (rank 1, z beside control); judge a non-test at this design (control FAILs); not a negative |

## Conflict: barred 27 -- Neuers (no.21 f.44r) vs nauarre? (no.37 f.60r) (GAPS-fr4715-vieuville-pool-10, 3 Oct 2026)
- no.21 f.44r (Jerome de Montholon, Tours, 21 Oct 1589): "Neuers" over a barred 27 at two sites ("celluy (9 27 auoir envoye"; "la lettre de 27, nay sceu"), grade M (witness/f44r_glosses_reconciled.tsv G3, G4).
- no.37 f.60r (Montholon, Tours, 12 Dec 1589): "nauarre?" over a barred 27 at two sites (L01, L20), grade M (key_wordcodes_f60r.tsv; nemours not excluded there).
- no.58 (Tomokiyo's alignment): '27 = les (dot-marked).
Not resolved by majority (rule 4): both period glosses are M, the leaves have different senders (Jerome de Montholon vs the Sr de Montholon) and different dates, and f.44r's glosses tie their own per-leaf shuffle control (2/2 vs p95 1.000). On no.44, .27 stays M "nauarre?" from f.60r, with Neuers as the f.44r alternative; no key row changed.

## GAPS-fr4715-vieuville-pool-13 (3 Oct 2026, account-4): no.28 f.51r gloss conflicts, logged only
- 44 = Roy (f.51r, M) vs 7 = Roy (f.60r, C): two codes for one gloss; a nomenclator may give the king two codes, or one gloss is misplaced. Not merged.
- 34 glossed twice on f.51r with two different words (Amyens S04, Libourn S05): a within-leaf conflict (the f50r_gloss_control.py within-leaf statistic 1/2, a tie with its shuffle p95 0.500). 34 not keyed.
- dotted 49: f.50r Champagne (two dots, gloss H both passes, leaf did not clear) vs f.51r Roy (pass B only, L, gloss placed between 'agui' and 49). Neither is keyed; no.44 .49 stays I.

## CABNOIR (3 Oct 2026, account-4): barred 27 -- a third witness, Cabinet Noir
- Descifrado, *Cabinet Noir* v1.0 (github.com/el-descifrador/cabinet-noir, `montholon-1589/cle/montholon1589_complements.tsv`, CC BY 4.0) gives ~27 = Nevers, SÛR-G. Their witnesses are the no.37 f.60r header gloss (the **same** L01 gloss we read "nauarre?" at M), fr.3414 p.78 v263 L16-17 and no.54.
- This agrees with our f.44r reading (Neuers, M, two sites). It conflicts with our f.60r reading of the same gloss.
- Not resolved by majority (rule 4). Their reading of the same ink is an outside witness, so our f.60r reading is the one to re-check. The next eye on the f.60r L01/L20 crops settles it, and key no.71 (fr.3995 f.133r) gives a period value for barred 27. Until then, .27 on no.44 stays M with both candidates.
- Also logged as data, not merged: 99 (ours "bours" M, read as a person; theirs '99 = vous, dotted). 52 with two strokes (ours Normandie M; theirs '52 = si with one dot; their key no.71 description puts places in a two-point layer, so this is compatible). 49 with two dots (ours: Champagne held; their no.27 transcription has ''49? at L21 and a clear gloss "Champagne?" at L22, with no value given).

## GAPS-fr4715-vieuville-pool-14 (3 Oct 2026, account-4): key no.71 (BnF fr.3995 f.133r) vs our glosses
| Leaf | Family | CONTROL | TARGET | Status | Reason |
|---|---|---|---|---|---|
| pool word-codes | period key no.71 read blind (1 Opus pass, 35 iiif_lines crops) and reconciled; gate pre-registered in witness/key71/PREREG.md (7778b15d); scripts/key71_control.py | A: gloss permutation p95 3 (mean 1.0), random code p95 1 (mean 0.088); B: letter-label permutation p95 0.121 | A 5/5 C glosses match; B 25/33 = 0.758 Tomokiyo letter rows printed (0 conflicts, 8 homophones absent) | FAIL as registered (B < 0.80) | the B statistic counted absent homophones as misses, a pre-registration design error. It was not re-scored after the result. The next step is a fresh registration on an unseen known answer |
Data conflicts, rule 4 (not merged, not settled by majority):
- barred 27: key no.71 prints Duc de Neuers 25/26/27 (braced). This agrees with f.44r "Neuers" (M) and Cabinet Noir ~27 = Nevers. It conflicts with our f.60r L01/L20 reading "nauarre?" (M). This is a third witness against that reading, which stays to be re-checked on the crops.
- barred 44: key no.71 prints Mr de Retz. f.51r S06 glossed Roy (M, pass B H, pass A L). Unconfirmed; the key's Roy is 6/7/8.
- 99: key no.71 prints dotted-tens 99 = vous and dot-each-digit 99 = Maire de ville, with no barred 99. Our f.60r "bours" (M) reads a person, so the code or the gloss there is in doubt.
- two-dot 49: key no.71 Prouinces 49 = Champaigne. This supports the f.50r Champagne lead (held, its leaf tied its control). The f.51r "Roy" (L) is not supported.
- 52 with two marks: key no.71 Prouinces 52 = Normandye. Agrees with f.62r Normandie (M).
- barred 13: Royne de nauarre (key), against f.62r "Narre" (M) and Cabinet Noir's Henri de Navarre on usage. The gloss and the key agree on "Navarre", and the person is disputed.

## GAPS-fr4715-vieuville-pool-15 (3 Oct 2026, account-4): key no.71 re-gated on an unseen known answer (second attempt)
| Leaf | Family | CONTROL | TARGET | Status | Reason |
|---|---|---|---|---|---|
| pool word-codes | the same reconciled key no.71 file, scored against 8 Cabinet Noir sure values never used or printed by GAPS-14 (Motz '29 '51 '74 '84 '94 '97; persons ~15 ~37); gate pre-registered in witness/key71/PREREG2.md (0c411223, pushed before scoring); scripts/key71_regate.py | value permutation (40,320 exact) p95 2 (mean 0.50, max 4); random code (10,000) p95 0 (mean 0.047) | 4 match, 3 conflict, 1 absent: SHARE 4/7 = 0.571 | FAIL as registered (SHARE < 0.80; REAL 4 > both p95s) | of the 3 conflicts, 2 are the match rule's notation misses, seen only after scoring and not re-scored: '29 "on" vs key "lon" (= l'on), ~15 "le cardinal de Vendôme" vs key "C. de vendosme" (silent s). 1 is real: ~37 Langres (Cabinet Noir, gloss) vs key "D. de Mayenne" (35-36-37 braced) |
Second attempt, as GAPS-14 was the first. Rule 3's third-attempt clause: the key is not re-gated a third time with this instrument, which is the reconciled transcription plus a token-subset match rule against a printed answer list. A further gate needs new material (the fr.4712 f.7r period interlinear pair, read from its image) or a different instrument (a second blind read of the key cells that no.44's six slots need).
Data conflict, rule 4 (not merged): barred 37. Key no.71 gives D. de Mayenne (braced 35-37). Cabinet Noir's SÛR-G value is Langres, from a gloss. Their README already notes that Montholon's clerk departs from the key's name table (~13, ~25). Logged; not settled.

## GAPS-fr4715-vieuville-pool-16 (3 Oct 2026, account-4): fr.4712 f.7r leaf control (PREREG3)
| family | control | control number | target number | result |
|---|---|---|---|---|
| f.7r period pair, flat-start interlinear_align vs Tomokiyo letters (G1) | Tomokiyo values permuted, 10,000 | mean 2.25, p99 5 | 5/32 | FAIL (tie with p99): leaf held, G2 key71 not run |
Mechanical reconciliation only (no image check of marks or glosses); an image reconciliation of the same crops is new
material for this instrument, not a re-tune.

## G1 known-answer power check (GAPS83, 3 Oct 2026, account-4; PREREG4_g1power.md, 750d4ff0)
| instrument | control (known answer) | target | verdict |
|---|---|---|---|
| flat-start interlinear_align, G1 A/S vs Tomokiyo (PASS S>=12, A/S>=0.70, A>perm p99) | synthetic f.7r glosses enciphered with Tomokiyo: K1 clean 1.000, K2 (word-codes 0.15, sub 0.10) 0.970, K3 (sub 0.20) 0.969 median, PASS 20/20 each | f.7r: GAPS-16 5/32 = 0.156, GAPS82 8/30 = 0.267 | gate reachable; target FAILs are real FAILs of the pairing as transcribed, not a non-test and not a key negative; no third reconciliation (rule 3); next instrument: fixed-key scoring vs permuted-key control |

## Fixed-key scoring of the f.7r runs (GAPS88, 3 Oct 2026, account-4; PREREG5_fixedkey.md, c27e21b8)
| instrument | control | target | verdict |
|---|---|---|---|
| Tomokiyo's letter table applied to each f.7r run (nothing learned), pooled LCS vs own gloss (scripts/f7r_fixedkey.py) | permuted key, 10,000: T mean 116.1, p99 137, max 152, meanR 0.318; positive control K2 synthetic: D_K2 0.566, PASS 20/20 | T 235, R 0.644, D 0.326 (gate 0.283); 16 of 19 runs p < 0.01 | PASS: f.7r follows Tomokiyo's letters; G1 FAILs were aligner misfit, not a different key; letters only, no slot read |

## G2 key no.71 on f.7r, LCS-anchored (GAPS91, 3 Oct 2026, account-4; PREREG6_g2anchor.md, a19bbf6a)
| family | control | control number | target number | result |
|---|---|---|---|---|
| key no.71 cell in the mark's layer vs the f.7r gloss words located by fixed-key LCS anchors (scripts/f7r_g2anchor.py), PREREG3 match rule | label permutation (exact 24) and random code (10,000, seed 71) | p95 1 (max 2) and p95 0 (max 2) | 11 items, 4 located: 2 match, 2 conflict; SHARE 0.500; all 18 tokens: 5 located, 3/2, 0.600 | NON-TEST (scorable 4 < 8): no slot read, no grade change |
Key no.71 re-gating is closed by PREREG3's clause: [retired] instrument = key no.71 against glosses or printed answer lists
with the token-subset match. Only a period gloss over one of no.44's slot codes (.03, .07, .49, .57, .6) reopens the slots.
Logged as data, not a gate (seen after scoring): the key no.71 cells of the unlocated f.7r codes equal Cabinet Noir's
f.7r gloss values for dotted 20, 16, 42, 99, 47, 11, two-dot 12 and barred 7. Conflicts by the locator (two-dot 11 "de"
vs "ville", dotted 33 "d. ma" vs "mon") are the locator's split of a longer gloss, not readings; not merged.
