# AUDIT -- fr3621-dinteville-1592, f.130r cipher passages read with a key rebuilt from the f.128 gloss

**Current figures (3 Oct 2026, 08:25 UTC):** see "Second audit (VERIFY-DIN2)" at the end of this file: N3, key `period`, licensed grades C 177 / M 311 / U 39 on the print-aligned key (decode.json job 3). The grade figures in the first audit below describe superseded keys.

Verifier: VERIFY-DIN (account 3, an in-session verifier for the account-3 orchestrator), 3 Oct 2026, 07:26-07:50 UTC.
I'm not the solver (A2-DIN, A2-DIN2 and A2-DIN3 ran on account 2). Brief: `.claude/briefs/runs/2026-10-03-acct3-verify-din.md`.
A2-DIN4 (account 2, a second reader on the f.128 gloss at h and D) had no commit on origin/main at 07:26 UTC, so this
audit does not use it.

Claim under audit (NOTES.md, A2-DIN2/A2-DIN3): a period key rebuilt from the sibling f.128 interlinear decipherment
(Dinteville to Nevers, Langres, 1 July 1592) reads f.130r (no decipherment on the leaf). fr16 -1.334 vs a max of -1.538
over 1000 shuffled keys. After a pre-registered key repair, -1.271 vs repaired-shuffle p95 -1.582 (0/1000). Grades
C 329, S 71, M 127, U 0.

## Verdict

| item | class | key source | text |
|---|---|---|---|
| f.130r cipher passages (BnF fr.3621 no.116; 527 signs), the fragments as read | **N3** | `period` | not known in print (the 1882 calendar summarises only the clear text, see 3b) |
| f.128r cipher passage (BnF fr.3621 no.114, 1 July 1592), the key source | **N1** | (period gloss on the leaf) | `known`: the full plaintext is printed in *Revue de Champagne et de Brie* t.XII (1882) p.340 |

**Safe sentence:** "A key that we rebuilt from the contemporary decipherment on Dinteville's letter of 1 July 1592 (BnF
fr.3621 f.128) reads the two cipher passages of his letter of 4 July 1592 (f.130) far better than chance. So far it gives
only short French fragments (for example 'la ville et le roi', '... en l'obéissance', 'dehors les ... serviront').
About half the signs are read at grade C and the rest are uncertain. We have not found a prior decipherment of these
passages; an 1882 calendar of the letter summarises only its clear text."

**Unsafe sentence:** "We deciphered Dinteville's cipher letter of 3 July 1592 for the first time: C 329, S 71." This is
wrong on four counts. "First" is rule-10 wording and is not licensed at N3. The licensed grades are C 263, M 264, S 0
(section 2d). The fragments are not a continuous reading. The date on the leaf is read as both iij and iiij; the BnF
catalogue and the 1882 print both give 4 July.

## 1. Extract

- **Item.** BnF Français 3621 no.116, f.130r. Gallica ark:/12148/btv1b52524472n canvas f269. DECODE R9451, Non-decrypted.
  Joachim, baron de Dinteville, the king's lieutenant-general in Champagne, to Louis de Gonzague, duc de Nevers, from
  Langres. Date line "le iij^e" or "iiij^e Juillet 1592": Bourdeau reads iij, while the BnF finding aid and the 1882
  print give 4 July. The leaf is mostly clear French with two inline cipher blocks (A2-DIN2: 11 lines, 530 signs),
  followed by a clear postscript (VERIFY-DIN, one vision read of the whole leaf at 1800 px).
- **Key source.** f.128r (no.114, 1 July 1592), where a period decipherment is written word by word above 183 signs.
  A2-DIN aligned it with tools/interlinear_align.py to f128/key_syl.tsv.
- **Reading.** f130/repair/reading.txt and reading_words.md (A2-DIN3). It is fragments only, and L01-L04 and L06-L07
  are mostly undivided.
- **Solver searches.** Gomberville 1665 seconde partie (Google Books H2eV4wAmIr0C, full-text), Henri IV *Lettres
  missives* t.3, Pérot 1911, Tomokiyo mirror, Bourdeau and Aymeloglu clones, DECODE snapshot, web and blogs (csCS2b,
  csED2, csGOM, scGOM2, GF4-BATCH9; 24 Sept to 3 Oct 2026). None of them found the *Revue de Champagne* series.

## 2. Re-derivation and statistics

Script `verify/verify_din.py`, output `verify/result.json` (`--check` regenerates it). It imports the solvers' own
`score_f130.py` and `repair_f130.py` unchanged.

**(a) Rule 7.** `tools/decode_key.py ciphers/fr3621-dinteville-1592 --check` prints "reading up to date" (both jobs:
C 263/M 225/U 39; C 329/M 127/S 71). `f130/score_f130.py --check`, `f130/repair_f130.py --check` and
`f128/align_f128.py --syl --check` all print "committed outputs match" (exit 0). The numbers reproduce exactly.

**(b) Controls at fresh seeds.**

| test | real | seed | mean | p95 | max | >= real |
|---|---|---|---|---|---|---|
| key_syl vs free shuffle (A2-DIN2 design) | -1.334 | 31001 | -1.960 | -1.716 | -1.537 | 0/1000 |
| | | 31002 | -1.963 | -1.701 | -1.523 | 0/1000 |
| | | 31003 | -1.954 | -1.710 | -1.463 | 0/1000 |
| key_syl vs **frequency-banded** shuffle (new: letters permuted only within blocks of 4 signs adjacent in f.130 frequency rank, which keeps frequent sign -> frequent letter) | -1.334 | 31001 | -1.723 | -1.617 | -1.440 | 0/1000 |
| | | 31002 | -1.722 | -1.621 | -1.526 | 0/1000 |
| repaired key vs repaired shuffles (A2-DIN3 design) | -1.271 | 31001 | -1.787 | -1.583 | -1.439 | 0/1000 |
| | | 31002 | -1.794 | -1.588 | -1.446 | 0/1000 |

The control can differ from the target on this statistic, because a shuffle moves which sign carries which letter. The
banded shuffle is the stronger null, and the target still beats every one of 2,000.

**(c) Power control at the measured two-reader error.** A synthetic homophonic French cipher with f.130's own run
structure (527 signs in its clear-word-broken runs) plus a 183-sign f.128-sized segment, 33 sign types, plaintext from
*Lettres de Catherine de Médicis* t.2, judged by a 4-gram model built only from the other two fr16 files. 5 replicates per
cell; 300 shuffles each.

| injected error | key | true-key score | replicates beating all 300 shuffles | repair: freed rows recovered (all / signs >= 10 occ.) |
|---|---|---|---|---|
| 0% | exact | -0.896 | 5/5 | 0.79 / 57 of 70 |
| 5.5% | exact | -1.098 | 5/5 | 0.74 / 60 of 77 |
| **11%** | **exact** | **-1.275** | **5/5** | **0.40 / 33 of 75** |
| 11% | 4 rows wrong | -1.410 | 5/5 | 0.60 / 51 of 72 |
| 11% | 8 rows wrong | -1.866 | 5/5 | 0.54 / 45 of 72 |
| 16.5% | exact | -1.378 | 5/5 | 0.33 / 28 of 78 |

Real f.130 + f.128 runs under the same held-out model: repaired key **-1.344**, key_syl seed -1.532. At 11% error the shuffle test
has full power. The real score lies between an exact key (-1.275) and a key with 4 of 33 rows wrong (-1.410). That fits
a mostly right key with a few wrong rows. The real figure is somewhat flattered because the f.128 runs are the text the
key was fitted on. The recovery column is the instrument's own known-answer test (2d).

**(d) The key repair: instrument, hold-out, and the 71 S grades.**
- *Rule 3 third-attempt clause.* `f130/repair_f130.py` is its own coordinate-ascent climb on the fr16 4-gram statistic. It is
  not `tools/key_repair.py`, and it tests a different hypothesis (fill unkeyed and weak rows of a sibling-gloss key, not
  AX2-4612S's syllable or rare-letter substitutions in a Nassau key). It was pre-registered and run once. The clause does
  not apply, and nothing is retired.
- *Hold-out.* The climb's objective sees the f.128 cipher signs but not the gloss letters. The gloss is used afterwards as
  a filter. So it is held out of the objective, but it acts as a veto, not as a test that the climb was scored against.
  Scored as a test, it fails: of the 13 free key_syl rows, the climb's raw value agreed with the gloss on 5 (chance
  expectation 1.2). Three of those 5 are rows the climb left at their seed value (1, plus, div). Of the 10 rows it moved,
  2 agreed (c=r, r=n) and 8 contradicted the gloss (zh, D, o, 9, T, h, B, n).
- *Known answer on the real text.* Each held C row (14) was freed in turn and climbed from 5 random starts. The climb
  recovered the gloss value in a majority of starts for **4 of 14** rows (4, L, f, p).
- *Known answer on the synthetic (2c).* At 11% error the climb recovers **40%** of freed rows (44% of the signs with at
  least 10 occurrences; v', 0', plus and c are all in that class on f.130).
- The shuffle gate PASS (2b) shows that the held rows carry signal. It doesn't license any single repaired value. The
  pre-registration's own S rule (gate PASS, stable in 20 of 20 runs, not rejected) measures how reproducible the climb is,
  not whether it is correct, and the climb fails its own known-answer test at this N and error. **The 71 S tokens are
  graded M** (v' 22, plus 20, c 14, 0' 10, div 4, r 1). The two NEW signs also go to M.
- *Grade inflation in the repair.* A2-DIN3's grading also promoted five free rows to C because the gloss aligned their
  value at least twice, although their gloss agreement is low: 1 = e at 2/11 (50 tokens), D 2/4 (8), T 2/3 (5), o 2/3
  (3), 9 2/3 (0 tokens on f.130). Under A2-DIN2's own pre-registered C rule (agree >= 3 and agree/n >= 0.5, sign conf H)
  these rows are M.
- **Licensed grades, 527 cipher tokens (dots excluded): C 263, S 0, M 264, U 0, no H.** These are A2-DIN2's C tokens; every
  other token is M. The values are still those of key_repaired.tsv. The grade column in key_repaired.tsv and
  f130/repair/tokens.tsv overstates them; the solver's script is not changed here, and fixing it is a next step.

**(e) h and D (the f.130 words contradict the f.128 gloss).** Both are graded **M** in every token (h 5, D 9). The letters
the word-level reading wants (h = p in "pourvoir"; D = c in "auec/obeissance/conseruer", d in "demeure") are grade **I**.
The gloss support is weak on both sides. h's only gloss letter (u, L04.1 idx 44) sits in the span the reconciler read
"doibt aussi passer". The 1882 print of the same decipherment (3b) reads "qui doivent partir dans trois jours" there, so
that one alignment is in a span the print contradicts, and h = u is unsupported. D's 4 gloss occurrences split
a 2 / g 1 / t 1. This conflict is a gloss-reading question, not a two-H-witness conflict (rule 4).

## 3. Rule-10 search log (3 Oct 2026)

**(a) Searched, no prior decipherment of f.130's cipher passages:**
- Gomberville, *Mémoires du duc de Nevers* (1665), seconde partie: already full-text searched by scGOM2 and GF4-BATCH9
  (Dinteville/Dinteuille 0 hits). Not re-run.
- Henri IV, *Lettres missives* t.3 (csED2): only the king's letters to Dinteville.
- **Revue de Champagne et de Brie**, series "Lettres de M. de Dinteville 1589-1597" (begins t.XI p.490; it draws on fr.3614-
  3640 including 3621): IA full-text API (`be-api` fts, "Lettres de M. de Dinteville": 42 items), then the OCR of
  t.XI-XVI, XVIII, XX (`revuedechampagne1[1-8]/20pariuoft`, `revuedechampagn07hrgoog`, `revuedechampagn10unkngoog`)
  fetched and grepped. **Found, see (b).**
- Google Books API (country=US, key): 7 queries ("Dinteville" "Nevers" chiffre 1592; "Dinteville" Langres "juillet
  1592"; "Dinteville" "3621"; "l armee Lorraine" Strasbourg Langres 1592; "Messieurs de la ville" Langres Dinteville
  Nevers; "deux millions d or" Geneve Dinteville; "comte de Chateauvilain" Dinteville "juillet 1592"; plus "Dinteville"
  Nevers "en l obeissance" Langres and "Lettres de M. de Dinteville"). The hits were the same Revue calendar (also
  reprinted in *Nouvelle revue de Champagne et de Brie* 1899, XA859zs04_YC), *Histoire militaire du pays de Langres*
  (1884), *Langres pendant la Ligue* (1868), *Correspondance des Saulx-Tavanes* (2025), and the Swiss *Inventaire
  sommaire* (fr.3621 f.17). None prints a decipherment of f.130.
- Phrase search on the readable fragments ("en l'obeissance", "la ville et le roy", "dehors les ... serviront"): too
  generic to discriminate. Neither the Books API (0 for the combined query) nor IA fts tied any of them to this letter.
  The decisive check was the calendar entry itself (b).
- Tomokiyo, nevers.htm (local mirror, including HTML comments): one Dinteville letter, 13 Dec 1590 (another
  manuscript), and no fr.3621 f.130 or key. unsolved.htm names fr.3621 only for f.125 (Lorraine, R9449).
- Cabinet Noir (el-descifrador): the local snapshot `sources/cabinet-noir/2026-10-03` has no hit, and a web search
  (`el-descifrador cabinet noir Dinteville Nevers 1592`) found nothing.
- Bourdeau, cyphersolver (shallow clone, HEAD a439937, 3 Oct 2026 06:07 UTC): `targets/dinteville1592/NOTES.md` still says
  "attempted, open ... Not read". Aymeloglu (HEAD d2800bb, 27 Sept): catalogue rows only. Nothing was copied (no licence).
- DECODE local snapshot (24 Sept 2026): R9451 Non-decrypted; R9450 Decrypted. No new fetch (login reserved).
- Web: "Dinteville" "Nevers" 1592 chiffre déchiffrement Langres lettre. This found Desenclos and Lasry (Henri IV to
  Nevers, a different letter) and two ARCSI PDFs (arcsi.fr/doc/Tant/420.pdf, Chalons.pdf, fetched). Their text could not
  be extracted in this container (no PDF library). They are logged as **unread**, not as negatives.
- OpenAlex (key, header): "Dinteville Nevers cipher" 1 hit, unrelated; "Dinteville chiffre 1592" 1, unrelated; "Nevers
  cipher letters 1592 Langres" 0. Semantic Scholar (key): "Dinteville cipher" returned only noise; "Duke of Nevers
  cipher 1592" returned nothing.
- JSTOR: 4 rows appended to `JSTOR-QUEUE.tsv` (2 per family). They do not block N3.

**(b) What the 1882 print contains.** *Revue de Champagne et de Brie* t.XII (1882), pp.340-341 (excerpt, unmodified OCR:
`print/revue-champagne-t12-1882-pp340-341.txt`):
- "Langres, 1er juillet 1592. Au duc de Nevers", with the footnote "Lettre en chiffres". This is **f.128, printed in full**:
  "...m'a dit avoir vu descendre à Gène 2 millions d'or d'Espaigne. Il en a laissé à Besançon 45 mulets chargés qui
  doivent partir dans trois jours et prendre le chemin de Vesoul, n'ayant que cent chevaux d'escorte...". So the key
  source's plaintext is N1: our gloss reading is an independent re-reading of a printed text. The print also corrects the
  A2-DIN gloss reading in places ("bestiaux"/"besounasiana" vs Besançon/Vesoul; "doibt aussi passer" vs "doivent
  partir"). The two texts follow different conventions (an editor's normalised print vs a literal gloss), so rule 3's
  PX-BRODEC lesson applies before they are diffed.
- "Langres, 4 juillet 1592. Au duc", with the footnote "En chiffres". This is **f.130**: same date as the BnF finding
  aid, same place, same addressee, and the only 4 July Dinteville letter in ff.127-131. The entry is a summary
  ("Il craint que l'ennemi ne remarche sur Chateauvilain ... Langres demande 200 hommes de pied et 200 chevaux ... arrêter
  ici le comte de Chateauvilain ... Le sr de Beaujeu ... L'armée lorraine était hier près de Joinville") plus a quoted
  passage ("Je ne scais s'il s'eschauffera ... la pouldre que j'y ai envoie ... si peu de vivres"). I read the leaf once
  at 1800 px. Every summarised point and the quotation sit in the **clear** text or the clear postscript, for example
  "Messieurs de la ville supplient tres humblement le Roy et vous d'y placer deux cens chevaulx et deux cens hommes de
  pied" and "faict arrester icy le Conte de Chasteauvillain pour se justiffier". Nothing in the entry corresponds to the
  fragments read from the cipher. The editor calendared the letter without reading its cipher.

**(c) Unreachable or not done:** JSTOR (cloud-blocked; queued). The two ARCSI PDFs (no extractor). Boltanski, *Les ducs de
Nevers et l'État royal* (2006), and a full-text read of Pérot's sources (*Correspondance inédite de M. de Dinteville*
in the Revue, now located) beyond the 1592 entries. The fr.3623 f.23 sibling (Italian, R9452). A2-DIN4's gloss re-read.

## 4. Postmortem and corrections

- **Missed print.** Four check-solved and gate passes (24 Sept-3 Oct) searched Gomberville and Henri IV, but not the
  recipient-side calendar actually built from fr.3621. That calendar prints the key-source letter in full and summarises
  the target. The target's novelty survives because the summary covers only the clear text. The next pass on any
  fr.3614-3640 Nevers-correspondent letter should grep the *Revue de Champagne et de Brie* series first.
- **Grade over-claim.** "C 329 S 71 M 127" is corrected to **C 263 S 0 M 264** (2d) in NOTES.md (verifier section,
  Remaining gaps, Escalation) and in the NEAR.md row. The solver's committed outputs are not edited. Regrading
  repair_f130.py and decode.json job 2 is listed as a next step.
- **Date.** The leaf's date is iij or iiij. The BnF finding aid and the 1882 print say 4 July, and the folder says
  3 July. The status line is not changed. Keep both, as GF4-BATCH9 did.
- **The f.128 gloss** has a printed control text (3b), a different instrument from a second reader. The next step for
  h, D and the drifting spans is a normalised re-alignment of f128 against the 1882 print (rule 3, PX-BRODEC), then
  re-running align_f128.py --syl and repair_f130.py.

Requests this session: archive.org 12 (11 OCR downloads + 1 advancedsearch), be-api.us.archive.org 3,
googleapis.com/books 11, api.openalex.org 3, api.semanticscholar.org 2, gallica.bnf.fr 1 (f269 at 1800 px), arcsi.fr 2,
github.com 2 (shallow clones). Vision calls: 1. No decoding was done beyond the re-derivation, and no credentials were
printed.

## Propagation note (DIN-PRINT, 3 Oct 2026; rule 10, a reading revised after this audit)

DIN-PRINT (an account-3 solver worker, not a verifier) did the next step in section 4. It aligned the f.128 cipher to the
1882 print with the same interlinear_align.py settings, changing only the plain text. The result is consistency 0.831
against shuffle max 0.358 and rotation max 0.803, 0/1166, and 7 of 29 key rows change. f.130 was re-decoded with that
key and **no repair**: fr16 -1.271 against free-shuffle max -1.462 and banded max -1.450, 0/2000. Grades are C 357 M 131
U 39, or C 291 M 197 U 39 with the c/d and a/t polyphones (# and v) held at M. The reading of record is now
`f130/print/reading.txt` (decode.json job 3). Job 2, the repaired key, is marked superseded. The fragments quoted in the
safe sentence ("la ville et le roi", "... en l'obéissance", "dehors les ... serviront") stand in the new reading. The
grade counts in sections 2d and Verdict describe the superseded keys. They are not re-verified here. The class (N3) and
any revised grade sentence are for the next verifier session. SO-DIN-F130's prompt carries the same note.

## Second audit (VERIFY-DIN2, account 3, 3 Oct 2026, 08:09-08:25 UTC)

Verifier: VERIFY-DIN2, an in-session verifier for the account-3 orchestrator. It is separate from the solvers (A2-DIN,
A2-DIN2, A2-DIN3, DIN-PRINT) and from VERIFY-DIN. Brief: `.claude/briefs/runs/2026-10-03-acct3-verify-din2.md`. Claim
under audit (DIN-PRINT): the key aligned from the f.128 cipher to its 1882 printed plaintext reads f.130r at fr16
-1.271, beating 1000 free shuffles (p95 -1.705) and 1000 frequency-banded shuffles (p95 -1.575), 0/1000 each. Grades are
C 291, M 197, U 39 (conservative), against a pre-registered C 357. Script: `verify/verify_din2.py`, output
`verify/result2.json`, with `--check`.

### Verdict (supersedes the grade figures in the first audit; the class is unchanged)

| item | class | key source | text |
|---|---|---|---|
| f.130r cipher passages (BnF fr.3621 no.116; 527 signs), fragments as read with `f128/print_align/key_print.tsv` | **N3** | `period` (rebuilt by us from the 1882 print of the sibling f.128's plaintext; the decipherment it prints is period) | f.130's own **clear** text is summarised in print: the *Revue de Champagne et de Brie* XII (1882) p.341 calendar and its 1899 reprint. No printed text of the **cipher** passages or of any decipherment of them was located. |
| f.128r, the key source | N1 (unchanged) | period | `known`: printed in full, Revue XII (1882) p.340 |

**Licensed grades (527 cipher tokens, dots excluded): C 177, M 311, U 39, no H, no S.** C here means: the print-alignment
row has at least 2 occurrences and **no** conflicting alignment, and the f.130 sign is read at H. The polyphones `#`
(c 7 / d 6) and `v` (a 8 / t 5) are graded M, as the brief requires. Rows whose print alignment carries a minority
conflict are also graded M: `0` e 11/18 (s 4, p 2, c 1; 38 tokens), `m` u 8/10 (t 2; 37), `sq` s 7/9 (x 2; 31) and
`a` q 4/5 (ul 1; 11). The pre-registered rule (agree >= 3 and >= 0.5) admitted them. Every grade figure, so a reader can
choose: pre-registered C 357 / M 131; polyphones held at M (DIN-PRINT's conservative figure) C 291 / M 197; agree/n >= 0.75
C 253 / M 235; **strict, no conflict, C 177 / M 311**. U is 39 in all four. The `sq` x and `m` t splits may be orthographic or
aligner drift (x for final s in "cheuaux"/"deux"; two adjacent u/t slips). A per-occurrence look could promote 68 tokens.
Until that is done, they are M.

**Safe sentence:** "A key that we rebuilt from the 1882 printed text of Dinteville's deciphered letter of 1 July 1592 (BnF
fr.3621 f.128) reads the two cipher passages of his letter of 4 July 1592 (f.130) far better than chance, and better than keys
aligned to other French texts. So far it gives only short French fragments (for example 'conserver ... en l'obéissance', 'la
ville et le roi', 'dehors les ... serviront'). About a third of the signs are read at grade C and the rest are uncertain. We
have not located a prior decipherment of these passages. The letter's clear text is summarised in an 1882 calendar."

**Unsafe sentence:** "We have deciphered the 3 July 1592 cipher letter for the first time, with 55% of it certain." This is
wrong on three counts. "First" is not licensed at N3. 55% is the C 291 figure, which still counts conflicting rows; the
licensed figure is 34% (C 177). The date is not 3 July on present evidence (see 2).

### 1. Re-derivation and controls

- **Rule 7.** `f128/print_align/align_print.py --check` and `f130/print/score_print.py --check` print "check: committed
  outputs match". `tools/decode_key.py ciphers/fr3621-dinteville-1592 --check` prints "reading up to date" (3 jobs; job 3:
  C 357, M 131, U 39). All exit 0. `verify/verify_din2.py --check` also matches.
- **f.130 controls at fresh seeds** (1000 each; real -1.2714, 385 windows):

| seed | free mean / p95 / max (>= real) | banded mean / p95 / max (>= real) |
|---|---|---|
| 52001 | -1.955 / -1.698 / -1.489 (0) | -1.675 / -1.578 / -1.441 (0) |
| 52002 | -1.956 / -1.698 / -1.563 (0) | -1.674 / -1.572 / -1.417 (0) |
| 52003 | -1.957 / -1.705 / -1.510 (0) | -1.673 / -1.579 / -1.429 (0) |

  0/6000. Both controls permute which letter a sign carries, so they can move the statistic. They are not orthogonal.
- **f.128 alignment shuffle at a fresh seed** (52001, 300 shuffles of the print letters, re-split to the print's word
  lengths): real consistency 0.831 (160 occ) vs mean 0.292, p95 0.325, max 0.350, 0/300. The control changes which plain
  letter falls under each sign, so it can change consistency. It is not orthogonal either. DIN-PRINT's rotation control has a
  near-identity maximum of 0.803 (a one- or two-letter shift lets the aligner slip back into phase). The gate passes against
  the rotation max only narrowly. The shuffle and the wrong-text control below are the discriminating nulls.
- **Wrong-text control (new).** This asks whether any real French plain text forced through the same aligner gives a key
  that reads f.130 this well. Twenty passages of 16th-century French prose (fr16 `lettresindites00marg`, the print's
  per-segment word counts kept) were aligned to the f.128 cipher with the identical syllabic settings, and each key was
  applied to f.130. f.128 consistency: mean 0.367, max 0.468 (real 0.831), 0/20. f.130 fr16 score: mean -1.700, p95
  -1.488, max -1.440 (real -1.271), 0/20. These wrong texts sit inside the scoring model's own training corpus, which
  favours the control. The f.130 signal comes from the print being the right plaintext, not from the aligner forcing
  French letter frequencies onto the signs.

### 2. Date

- **Crop.** One native region of canvas f269 (`images/src_ark_12148_btv1b52524472n_f269_400_3825_2450_175.jpg`, via
  tools/iiif_lines.py) was fetched and looked at once (the brief's one vision call). It is **not the date line**. It is a
  body line of clear text ("...Lorraine a envoyé ... du duc de Parme, ..."). The region was chosen from the numeric ink
  profile of an 808 px thumbnail, which was not looked at. Its manifest entry says so. The image does not settle the date.
- **Print witnesses (new).** The BnF's own printed catalogue (*Catalogue des manuscrits français*, ancien fonds, t.III,
  1868; IA `p1cataloguegnr02bibluoft`) describes no.116 as "Lettre du Sr de « Dinteville,... à monseigneur le duc de
  Nyvernoys,... De Langres, le un' juillet 1592 ». (Fol. 130.)". In the same OCR, "u" stands for "ii" (xxvui = xxviii,
  n' = ii' for Potier's 2 July), so "un'" is most likely "iiii". With the 1882 *Revue* ("Langres, 4 juillet 1592") this
  gives two printed witnesses for 4 July, against Bourdeau's leaf reading iij. The same catalogue gives no.114 (f.128) as
  "Lettre, avec chiffre et déchiffrement" and no.116 with no cipher note, which fits no decipherment on f.130.
- **Status.** The folder's "3 July" heading is not supported by any print witness. 4 July is the better-supported date,
  but the leaf has still not been read at the date line. Next: one region fetch of the f269 block y 4180-5340 (heavier ink,
  where the date, signature and postscript appear to sit) and one look, about USD 1.5.

### 3. Second rule-10 search (3 Oct 2026, families VERIFY-DIN did not cover or could not reach)

- **Revue de Champagne et de Brie, other volumes.** IA full-text (be-api) for "Langres, 4 juillet 1592" returned 3 items.
  `revuedechampagne12pariuoft` and `revuedechampagn11unkngoog` hold the same p.341 calendar entry for f.130 ("Il craint que
  l'ennemi ne remarche..."). `revuedechampagn03unkngoog` (a Google scan, OCR fetched and read in context, pp.148-149 of the
  series) holds a **different** letter, "Le Conseil de Ville. Langres, 4 juillet 1592. Au duc de Nevers": the town
  council's complaint that Dinteville had to send all his troops to Châteauvilain. That letter is in clear, not f.130.
  "4 juillet 1592" (20 hits) turned up no other Dinteville entry.
- **1899 reprint**, *Nouvelle revue de Champagne et de Brie* (Google Books XA859zs04_YC, snippet): the same calendar
  ("Langres, 4 juillet 1592. Au duc. Il craint que l'ennemi ne remarche ... chiffres ... DINTEVILLE 341"). It is a reprint of
  the 1882 entry and prints no decipherment.
- **BnF catalogue for fr.3621** (the printed *Catalogue des manuscrits français* 1868, IA OCR, entries 97-117 read): see 2.
  It notes no decipherment for no.116. The online archivesetmanuscrits record was not fetched separately; it derives from
  this catalogue.
- **ARCSI PDFs** (unread in the first audit): both are now extracted with pypdf in a scratch venv. `arcsi.fr/doc/Tant/420.pdf`
  (D. Tant, "Autres codes", 8 pp.) lists archive cipher items, with no Dinteville and no fr.3621. `arcsi.fr/doc/Tant/Chalons.pdf`
  (D. Tant, "La lettre chiffrée de Chalons", 3 pp.) covers a different item: the 1594 Châlons cipher letter and key (Nevers is
  named in the key). Neither concerns f.130.
- **Drouot, *Mayenne et la Bourgogne* (1937)** (IA `IA41551607_0001/0002`, be-api): it cites fr.3621 among Nevers's
  correspondence and cites deciphered Dinteville letters elsewhere (8 July 1592 "lettre déchiffrée", fr.4718/4075). It has
  no entry for 4 July and nothing on f.130. This lead points to **other** Dinteville cipher letters with period decipherments
  (fr.4718, fr.4075 f.37), a possible further key test (SO question 2, gaps).
- **Boltanski, *Les ducs de Nevers et l'État royal* (Droz 2006).** It is in copyright and its full text is not reachable from
  the cloud. Google Books returned 0 for "Boltanski Nevers Dinteville Langres 1592" and "Boltanski ... Dinteville chiffre";
  the exact-title + Dinteville query returned HTTP 503 once and was not retried. OpenAlex lists only reviews (2007-2013).
  This family is **unreachable**, not negative. It is the main reason this audit holds N3, not N4.
- **Google Books** (key, country=US): "Dinteville" Nevers chiffre déchiffrement 1592 (3: the BnF catalogues); "Dinteville"
  "en chiffre" Langres Nevers (4: catalogues; Barthélemy, *La Réforme et la Ligue en Champagne* 1888, a different letter to
  Châlons); "Dinteville" Nevers "lettres chiffrées" (6, none about f.130); Dinteville Langres 1592 chiffre (12: the Revue
  calendar, 1899 reprint, Histoire militaire du pays de Langres 1884, Langres pendant la Ligue 1868, Annales de Bourgogne
  1947; none prints the cipher content); "Dinteville" "4 juillet 1592" (3: the two Revue entries and the 1899 reprint);
  "en l'obeissance" "conserver ces" Langres (302, generic, no Dinteville hit).
- **OpenAlex** (key): "Dinteville Nevers", "Dinteville Langres Ligue", "Joachim de Dinteville", "Nevers correspondance
  chiffrée Ligue", "Boltanski ducs de Nevers". No work on Dinteville's 1592 cipher letters. **Semantic Scholar** (key):
  "Dinteville Nevers 1592" returned the Lasry et al. paper on the king's digit-cipher letter to Nevers (a different letter,
  already known); the two other queries hit 429 and were not retried. **HAL**: "Dinteville" 5 (art history, Guillaume de
  Dinteville 1550s), "Dinteville Nevers" 0, "ducs de Nevers chiffre" 0. **Persée**: "Dinteville Nevers 1592" returned
  Dinteville mentions in HES 1990 and 2003 and BSNAF 2004, none on this letter or its cipher.
- **Not re-run** (covered by VERIFY-DIN, unchanged since 07:50): Gomberville, Henri IV Lettres missives, Tomokiyo, Cabinet
  Noir, Bourdeau, Aymeloglu, DECODE. JSTOR stays queued (VERIFY-DIN's 4 rows); it does not block N3.

### 4. Postmortem and corrections

- **Grade over-claim (residual).** DIN-PRINT's conservative C 291 still counted rows whose own print alignment conflicts,
  so the licensed figure is C 177 (Verdict above). I corrected the "about 55% of the letters are now firm" sentence in
  `second-opinions/PROMPT-chatgpt-DIN.md` to "about a third", and the NEAR.md row. The solver's committed outputs
  (key_dk.tsv, tokens.tsv, decode.json job 3) are not edited; regrading score_print.py to the strict rule is a next step.
- **Date heading.** The NOTES.md heading's "3 July 1592" has no print support (2). I have not changed it, because the leaf
  is not yet read at the date. Both stay flagged.
- **N4 blocker.** Boltanski 2006 is unread and the JSTOR rows are unanswered. A third search adding nothing else would not
  change the class without these.

Requests this session: gallica.bnf.fr 3 (info.json, one 808 px thumbnail read numerically only, one native region),
be-api.us.archive.org 9, archive.org 4 (advancedsearch 1, OCR 3), googleapis.com/books 10, api.openalex.org 5,
api.semanticscholar.org 3 (2 x 429), api.archives-ouvertes.fr 3, persee.fr 1, arcsi.fr 3 (one 404 on a wrong path).
Vision calls: 1. No decoding beyond the re-derivation and the controls. No credentials printed.

## Propagation note (DIN-FIRM, 3 Oct 2026, rule 10)

No reading or grade change. DIN-FIRM checked the strict rule's conflict rows sq and m one occurrence at a time
(pre-registered, firm/PREREG.md). sq has 1 spelling conflict and 1 unexplained; m has 2 unexplained (m reads t in 'doiuent'
and 'trois'). Neither row was promoted, so the licensed grades stay **C 177, M 311, U 39** (now decode.json job 4). The
SECOND-OPINIONS-QUEUE row needs no update. Date: the foot of f269 (y 4180-5762, x 280-3640) carries no date line, so the
date stays iij (Bourdeau) / iiij (prints), unread on the leaf. **Correction to the Second audit's Drouot line:** Drouot
cites fr.4718 f.76 (Dinteville to Nevers, 8 July 1592) without calling it deciphered. The "lettre déchiffrée" is fr.4075
f.37, on the 1589 Chaumont intrigue, writer unnamed. Gallica's Français 4075 (btv1b9060550k) is a 1613-41 Coeuvres copy
volume, so that shelfmark does not fit as printed. See NOTES.md "DIN-FIRM".


## Date note (orchestrator, 3 Oct 2026)

The date line (images/f130_dateline2_L01_s1.jpg) reads "le iiij^e Juillet": 4 July 1592, as the 1868 BnF catalogue and the 1882 print give. No change to the class or grades.

Desenclos check, 4 Oct 2026 (DESENCLOS-PREMISE, account 3): no hit. Searched 17 open full texts of the 36 items in sources/desenclos/2026-10-04/bibliography.tsv (HAL PDFs, DSpace Tartu HistoCrypt 2024/2025 PDFs, OpenEdition HTML; built from HAL, theses.fr, OpenAlex, Semantic Scholar, CrossRef, Google Books) for this item's shelfmark, sender/recipient, place and date (terms.tsv, search-log.tsv, search.py); none names this item, its key or its plaintext. Not read: her 2014 thesis (theses.fr: not online) and 2017/2021 cryptography chapters (not open; JSTOR-QUEUE rows of 4 Oct 2026). Context only: Desenclos and Lasry 2024 name fr. 3623 (the volume our NOTES.md gives for this letter's 5/13 July 1592 siblings) among the volumes holding at least 23 digit-cipher letters sent to Nevers in 1589-1591 (PDF page 5 of the dspace.ut.ee copy); they cite no folio of fr. 3623 and read none of those letters.
