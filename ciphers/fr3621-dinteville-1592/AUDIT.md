# AUDIT -- fr3621-dinteville-1592, f.130r cipher passages read with a key rebuilt from the f.128 gloss

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
