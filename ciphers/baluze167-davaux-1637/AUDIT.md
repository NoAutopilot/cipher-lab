# AUDIT -- baluze167-davaux-1637

## AUDIT (AUD1-B167), 8 Oct 2026, 12:12-12:3x UTC by date -u

Verifier: AUD1-B167 (account 2, Opus), for the account-3 orchestrator, brief `.claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md`
section "AUD1-B167". Separate from the solver (D4-B167, account 4) and from the rule-7 re-deriver (D4V-B167, account 4). Depth ruled
under `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md` (CLAUDE.md rule 4a literally). No decoding done here beyond re-running the
committed decode; search files in `aud1b167/`.

### 1. Item under audit

| field | value |
|---|---|
| Item | BnF Baluze 170, f.229r-v, the bare cipher passage of the letter ff.228r-230r (Gallica ark btv1b90015040, canvases 240 right and 241 left) |
| Sender, recipient, place, date | Léon Bouthillier, comte de Chavigny, to Claude de Mesmes, comte d'Avaux (at Hamburg); "Amyens ce 25 Aoust 1640" on f.230r (D1-BAL170) |
| Ciphertext | `ciphertext_b170f229.txt` (reconciled from two blind passes, D4-B167), 366 cipher tokens |
| Reading | `reading_b170f229.txt`, `reading_tokens_b170f229.tsv`; `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check` -> "reading up to date", exit 0 (re-run by this verifier) |
| Key | Tomokiyo, Cryptiana louisxiii.htm, "D'Avaux's Cipher (1637-1641) (DE=16')" table (images/louisxiii_davaux.png), applied as key.tsv. Key source: **published** (Satoshi Tomokiyo's modern key, credited). Two numerals (100' faire, 4' bi) are I-grade additions not in his table |
| Grades (rule 4) | H 106, M 258, I 1, U 1; C 0, S 0. All 180 letter-sign tokens are M; H tokens are numerals with clear marks |
| Period decipherment on the leaf | none: interlinear space bare on every cipher line (D1A-B167 eye check, f.229r L07, f.229v L13, L15; survey.tsv "absent") |
| Judge | fr17 PASS -0.824 vs real_p05 -0.853 (D4V-B167), with a non-independence caveat for the M letters (ARM-C1 shape) |

Distinctive phrases (as read): "touchant la jonction de leurs forces avec les armees de l'une ou de l'autre couronne ou avec les deux
ensemble"; "qu'ils veulent que leurs troupes soient jointes a M de Longueville et soubz son commandement"; "madame la Landgrave qui est
alliee avec le Roy et qui en recoit assistance"; "par la trop grande fermete de [73=] nous perdrons les seuls adherents"; "laissant
l'ennemi maistre de la campagne"; "On gratiffiera le comte d'Heberstein qui luy doit succeder affin de l'obliger a mieux faire que son
predecesseur".

What the solver side searched before this audit: Avenel VI whole-volume grep (CS-6 / earlier worker); Tomokiyo's page; DECODE R2756-2762
(R2761 = 170 f.228-230: "Decrypted", Inline Plaintext No, only the key attached); Bourdeau SOLVED_CATALOGUE.md line 239 and Aymeloglu
decode-catalog.csv (CS-6, 3 Oct 2026); web and blog searches (CS-6). D4-B167 searched nothing further.

### 2. Independent search log (8 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series: Avenel, *Lettres, instructions diplomatiques et papiers d'État du cardinal de Richelieu* | vols VI, VII, VIII (IA lettresinstructi06/07/08richuoft, `_djvu.txt` fetched once): grep for Eberstein/Heberstein, "jonction de leurs", "seuls adh", "maistre/maître de la campagne", OCR-tolerant "aoust i64o" dates, Avaux, Landgrave; plus print_check `ia` source rows on the three volumes | not found. Vol VI carries Richelieu's own letters from Amiens 2 and 19 Aug 1640 (OCR lines 38438, 38708), no Chavigny despatch to d'Avaux of 25 Aug 1640, no Eberstein in any of VI-VIII |
| (b) sender/recipient correspondence | Le Clerc, *Négociations secrètes touchant la paix de Munster et d'Osnabrug* t.1 (IA secretestouchant01lecl and negociationssecr01lecl, be-api fts): "Heberstein", "Eberstein", "seuls adherans", "jonction de leurs forces"; positive controls "Avaux" and "Longueville" hit | not found (the collection starts its documents in 1642). No edition of Chavigny's despatches to d'Avaux located (as CS-6) |
| (c) documentary editions / histories of the 1640 campaign | Le Laboureur, *Histoire du mareschal de Guebriant* (1657, IA bub_gb_cM5KS3lziccC, be-api): positive controls Eberstein, Avaux, Chavigny all hit (it prints letters of Eberstein and of Chavigny to Guébriant); "jonction de leurs forces", "seuls adherans/adhérents" 0. Noailles, *Le maréchal de Guébriant* (1913, IA lemarchaldegu00noai): Eberstein, Banier, Avaux, Chavigny hit; "Baluze", "25 août 1640", "Madame la Landgrave" 0 | not found; the 1640 junction with the Hessian and Lüneburg troops and Eberstein's command are discussed, not this despatch |
| (d) holding archive and project pages | Gallica (the leaf itself, bare); DECODE R2761 (via CS-6 and D1-BAL170 records); BnF archivesetmanuscrits record for Baluze 170 not read this pass | no decipherment of f.229 located |
| (e) full text: IA, Google Books | `tools/print_check.py` 8 phrases (aud1b167/phrases.txt -> aud1b167/print-check.tsv): IA global fts, Google Books (country=US, keyed), plus four targeted Google Books queries with snippets ("jonction de leurs forces" Longueville Landgrave Avaux; "comte d Eberstein" Chavigny; "seuls adherents" France; Heberstein predecesseur Landgrave 1640) | not found. Google Books returned word-bag matches only (300+ volumes per phrase, snippets do not carry the phrases); 3 phrases got HTTP 503 from Google Books in print_check and are covered only by IA and the targeted queries |
| (f) solver repositories and blogs | Tomokiyo louisxiii.htm (on disk): for 170 f.228 he quotes one fragment, "sont mal satisfaits de *", and "..."; nothing from f.229. Bourdeau / Aymeloglu / DECODE as logged by CS-6, 3 Oct 2026 (not re-cloned this pass) | no prior reading of f.229 located |
| (g) scholarship | OpenAlex (keyed) and CrossRef keyword rows via print_check: one OpenAlex work (unrelated back matter), CrossRef top hits ODNB/unrelated. Semantic Scholar: HTTP 429 on the first call, not retried (unreachable this pass). JSTOR: two rows appended to JSTOR-QUEUE.tsv (families i and ii) | not found; S2 unreachable; JSTOR queued |

Unreachable or not searched: Semantic Scholar (429); the Affaires étrangères Correspondance politique (Allemagne / Hambourg) and any
minute of this despatch in Chavigny's registers (not online here); Acta Pacis Westphalicae Serie I Bd 1 (instructions 1636-42, not
opened); Grotius *Briefwisseling* for August 1640; Avenel V (1635-37, out of date range). Requests: archive.org 7 (+ be-api 32),
www.googleapis.com 4 + 8 (print_check), api.openalex.org 9, api.crossref.org 2, api.semanticscholar.org 1 (429), all >= 1.6 s apart.

### 3. Classification

| item | prior plaintext | prior decipherment | class | key | confidence |
|---|---|---|---|---|---|
| Baluze 170 f.229r-v (Chavigny to d'Avaux, Amiens 25 Aug 1640, bare cipher passage) | none located (searched above; earliest relevant print checked Le Laboureur 1657) | none located: no interlinear gloss on the leaf; Tomokiyo quotes nothing from f.229; DECODE R2761 carries only the key | **N3** | published (Tomokiyo's table, credited) | moderate: the despatch is unedited as far as the printed series go, but a deciphered recipient copy or a clear minute in the AAE or in Chavigny's own papers is not excluded, and the open-index pass is incomplete (S2 429, JSTOR queued) |

Why not N4: the holding archive's catalogue record (archivesetmanuscrits, Baluze 170) and the AAE series were not read, Semantic
Scholar was unreachable, and three phrases missed their Google Books run (HTTP 503). Why not N1/N2: no printed text of the passage, in
cipher or in clear, was located, and no reading of these numerals or signs by anyone else was found.

- **Safe sentence:** "The bare cipher passage on Baluze 170 f.229r-v (Chavigny to d'Avaux, Amiens, 25 Aug 1640) was read by us with
  Tomokiyo's published D'Avaux key (106 numeral tokens at grade H, the 180 letter signs at M); no prior decipherment or printed text of
  it was located in Avenel's Richelieu letters (vols VI-VIII), Le Clerc's *Négociations secrètes*, the Guébriant histories (1657,
  1913), Internet Archive full text, Google Books, OpenAlex or CrossRef (searched 8 Oct 2026)."
- **Unsafe sentence:** "We deciphered a previously unread letter of Chavigny" / "first decipherment" (rule 10: N3, published key,
  letter signs at M; "previously unread" is never allowed below N4).

### 4. Depth (rule 4a, depth bar of 8 Oct 2026)

- Tokens: 106 / 366 = **29%** H/C/S (all H, numerals); 258 M, 1 I, 1 U. Unread: names/codes 1 (13 "sued" before 73=, context does not
  settle it), other 1 (U, the two-dot sign f.229v L14); the M letter signs are read, not unread.
- **Cipher clause: not met.** The longest contiguous H stretch is 10-12 letters (f.229r L17 "avec le Roy" across two H numerals), far
  under the authentication distance for a nomenclator of about 150 numeral values plus homophonic letter signs, with 258 M liberties.
  The published key does not shrink H(K) to the liberties (depth bar, bullet 3).
- **Code clause: met.** Word-class codes of the published table read sensibly in two or more independent contexts: 8: = "leur" in
  "la jonction de leurs forces" (f.229r L07) and "que leurs troupes soient jointes" (L11); 10: = "les" seven times in different phrases
  (L05 "les dits ducs", L08 "les armees", L09 "les deux", L13, L20, f.229v L03 "les seuls adherents"); the name code 73= reads sensibly in
  "la trop grande fermete de [73=] nous perdrons les seuls adherents" (f.229v L02-03) and plausibly in "de creance pres de [73=]"
  (f.229r L04; unsettled spot). These are not repeated verbatim phrases. Letter signs are not counted for this clause (precedent:
  clair1161, "letter values ... are cipher letters, not code values").
- **External check:** the letter-sign values used (9 c, mm p, n l, P i/s) are those printed in Tomokiyo's table (D4V-B167 point 2); that
  is a D3/D4 element and is not used for D2 here. Context consistent with the reading, used only to corroborate, not to supply: Noailles
  1913 places Eberstein at the head of the Hessian troops in 1640, which fits "le comte d'Heberstein qui luy doit succeder"; the period
  French spelling of the Swedish marshal is "Banier" (Noailles), and 73= (Tomokiyo "Bavier") fits him in the f.229v context better than
  Bavaria. Not a regrade; 73= stays at the key's own value.
- **Verifier's sentence (D2):** "In this passage Chavigny tells d'Avaux that the dukes and Madame la Landgrave, who is allied with the
  King and receives his assistance, want their troops joined to M. de Longueville and kept under his command even when the armies of the
  two crowns are together, and that the comte d'Heberstein, who is to succeed [the present commander], will be given a gratification to
  bind him to do better than his predecessor." Written from the reading; conditional on the M letter signs, which the fr17 PASS and the
  key's own letter block support.
- **Depth: D2**, "partially deciphered (about 29%)". Held at D2 (not D3) because 29% < 80% H/C/S: the letter signs are an eye
  identification against a hand-drawn table with no shape-level control on this hand.

### 5. Postmortem and corrections

- No over-claim found in the target's files: D4-B167 and D4V-B167 both say "provisional", grade letter signs M, and make no novelty
  statement. NOTES.md line 1 status `partial` stands.
- One factual nuance carried into NOTES.md: the earlier phrase "Avenel VI prints no Chavigny despatch to d'Avaux of 25 Aug 1640" is now
  extended to vols VII-VIII and three further sources (above).
- status.json: a `results` row added for this item (N3, D2, key published, one audit). SECOND-OPINIONS-QUEUE.tsv: SO-BAL170-F229 queued,
  prompt `second-opinions/PROMPT-chatgpt-b170f229.md`. Second audit: one WORK-QUEUE row (AUD2-B167) for a different account.
- Rule 10: this audit is the only place the class is assigned; the solver files keep their "where not found" wording.

## AUDIT 2 (AUD2-B167), 8 Oct 2026, 12:43-12:5x UTC by date -u

Verifier: AUD2-B167 (account 1, Opus), brief `.claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md` section "AUD2-B167". This session
has not touched the target before (not D4-B167, D4V-B167 or AUD1-B167). Task: try to break AUD1's N3 / D2. Search log
`aud2b167/search-log.tsv`, raw API answers `aud2b167/gb*.json`, `aud2b167/s2.txt`. No decoding beyond reading the committed files.

### 1. Prior print or decipherment (the families AUD1 left open)

| family | result |
|---|---|
| BnF archivesetmanuscrits, Baluze 170 (ark:/12148/cc34098s/ca19857865) and parent cc34098s | read. Digitised (Gallica btv1b90015040, from microfilm MF 8419); no bibliography, no edition and no decipherment named; parent describes letters of Chavigny to d'Avaux 1637-1650 |
| Acta Pacis Westphalicae I 1 (instructions 1636-43), APW digital via the browser tool | Eberstein only in the Swedish 1637 memorials (the Eberstein counts); Chavigny only in the introduction and the 1643 instruction; no 1640 despatch to d'Avaux. All-APW query "Hamburg Chavigny 1640" hits only introductions and bibliographies |
| APW II B bibliography, followed up | led to Boppe, *Correspondance inédite du comte d'Avaux avec son père* (1887, IA correspondancei00avaugoog): it prints a letter of **25 Aug 1640** (letter LIX), but it is the father (Roissy) to d'Avaux from Paris, on other matters (AAE Allemagne vol. 13 per its heading); no Eberstein, "jonction" or "seuls adh" anywhere in the volume |
| Grotius *Briefwisseling* XI, letters 4803-4847 (25 Aug-22 Sept 1640, to Oxenstierna, Salvius) | read: Longueville's lack of reinforcements, the Weimarian colonels, d'Avaux and the Swedish treaty; no text of or reference to this despatch |
| Google Books, the three phrases that got HTTP 503 | "soient jointes a M de Longueville": 200, word-bag only. The two apostrophe/longer forms 503'd again; their variants ("maistre de la campagne" ennemi laissant; "perdrons les seuls") answered 200 with no match. Covered by variant, not by the exact form |
| Semantic Scholar (keyed) | 6 queries answered 200, nothing relevant; 2 further 429 |
| Solver repositories, re-cloned today | Bourdeau (head 7 Oct 2026): no Baluze 170 item. Aymeloglu (head 27 Sept 2026): only DECODE row 2761 (f.228-230 "Decrypted", key attached), as AUD1 logged |

**Result: AUD1's negative holds.** No printed text or decipherment of this passage was located. Still not searched: the AAE
Correspondance politique (Allemagne) duplicate or minute (unpublished, not online here); recipient-side Hessian and Lüneburg editions (for
example Rommel's *Geschichte von Hessen* VIII); JSTOR (rows queued by AUD1). **Class: N3 confirmed.** This audit does not raise it to
N4. The editions, catalogue and project pages AUD1 named as gaps are now covered, but the Hessian-side print has not been checked, and
two phrases were searched in Google Books only through variants. Key: **published** (Tomokiyo), unchanged.

### 2. Depth re-ruled under the 8 Oct depth bar

- **Code clause: met, on 10: alone; 8: is weaker but passes.** 10: = "les" appears 7 times. Two contexts discriminate, because other
  plausible values (des/ses/ces) fail: "LES DITs" (f.229r L05; L20 repeats the formula and counts once) and "COURONNE OU AVEC les deux
  ensemble" (L09, set in clear text). 8: = "leur" appears twice, in independent phrases. One sits in clear-text context ("QUE leur
  troupes soient jointes a M DE LONGUEVILLE", L11-12), which supports it. But "ses"/"nos" would also read there, so 8: shows that the
  value fits, not that it is the only value. An H grade on either value was not used (bar, bullet 4). 73= reads in three contexts, but
  its value is contested (Tomokiyo "Bavier" against Banér), so the clause does not rest on it.
- **Cipher clause: not met.** AUD1's ruling stands: there are 258 M liberties, and the published key does not shrink H(K).
- **Caveat AUD1 did not state:** the letter signs are transcribed as `L:x` (the transcription header says "letter settled from context
  in this letter"). So their transcription is not independent of the reading, which is one more reason they are M and stay out of both
  clauses. They also explain why the two blind passes split by 0.23-0.26.
- **This verifier's sentence (D2), taken from the ciphered parts:** "In cipher Chavigny writes that through the excessive firmness of
  [73=] France would lose the only adherents it has, each withdrawing shamefully and leaving the enemy master of the field, and that the
  comte d'Heberstein, who is to succeed, will be given a gratification to bind him to do better than his predecessor." This is
  conditional on the M letter signs. Corroborated, not supplied, by Grotius 4813/4836 (Longueville stalled on the Rhine, 1640).
- **Depth: D2 confirmed**, "partially deciphered (about 29%)" (106/366 H).

### 3. Crop spot check (images/crops/b170f229v_L02, L12, L13)

Signs were counted by eye on the crops and compared with `ciphertext_b170f229.txt`: L02 13/13, L12 13/13, L13 21/21. The order and the
identity of the numerals agree. The letter-sign shapes are consistent with the values given (the u-shape with a descending cross = f,
L12 pos 4 and L13 pos 19; without the cross = t, L02 pos 1 and L13 pos 11). On L02, 16 shows no clear accent at either position; it is
already transcribed `16'?` (M). No discrepancy found.

### 4. Corrections

None to the reading or the grades. Two points of wording, applied here only: AUD1's "Why not N4" list is now down to the Hessian-side
editions, the AAE series and JSTOR; and Banér, not Bavaria, remains the better contextual fit for 73=, with the value left at the
key's. The safe sentence stands as AUD1 wrote it, with "BnF catalogue, Acta Pacis Westphalicae I 1, Boppe 1887, Grotius *Briefwisseling*,
Semantic Scholar" added to the list of sources searched. Unsafe: anything stronger than N3 wording (rule 10).
Requests: googleapis.com 9, api.semanticscholar.org 8 (2 x 429), archivesetmanuscrits.bnf.fr 2, apw.digitale-sammlungen.de 7 (browser),
archive.org 2, grotius.huygens.knaw.nl 8, github.com 2 clones; all one at a time, >= 1.5 s apart except S2 (1.2-3 s).
