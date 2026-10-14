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

## AUDIT 3 (AUD-SIG-CHAV), 8 Oct 2026, 23:39-23:5x UTC by date -u

Verifier: AUD-SIG-CHAV (account 3, Opus), for LANE-VERIFY-4 (account 3), brief `.claude/briefs/runs/2026-10-08-acct3-verify4-jobs.md`
-> `.claude/briefs/runs/2026-10-08-acct1-sig1-jobs.md` "## AUD-SIG-CHAV", step type `new-family-audit`. Account 3 did not read,
re-derive or first-audit this item (reader D4-B167 acct 4, AUD1-B167 acct 2, AUD2-B167 acct 1). f.228 (SIG-B228/B228B) is not
this audit's item. Task: the two families both audits left open -- (a) the AAE Correspondance politique and printed French selections,
(b) the Hessian side -- and the class may stay, rise or fall. No decoding. Files: `audsigchav/search-log.tsv`, `audsigchav/excerpts.txt`,
`audsigchav/prior_work_*.txt`, raw API answers `audsigchav/*.json`.

### Prior-work checks 3-5

- `tools/prior_work.py baluze167-davaux-1637 --item-spec 'shelfmark=BnF Baluze 170;folio=229r;date=1640-08-25;sender=Chavigny;recipient=Avaux;...' --step-type new-family-audit --fetch`: exit 4; 16 LEAD rows, all our own earlier reads and audits of this folder (D4-B167, D1-BAL170, AUD1/AUD2, the live claim), "new-family-audit is never DONE"; Tomokiyo CONTEXT (f.229 not quoted); solver caches CLEAR; editions UNCHECKED-NET (no prior_editions.tsv row). Nothing outside our own work.
- G3, same with `--reading reading_b170f229.txt --network`: exit 4; IA global CLEAR, Google Books not searched (HTTP 429). The tool's
  auto phrases were weak (it took the header line); AUD1's eight decoded phrases had already run on IA and Google Books, so G3 here
  was spent on the families the brief names (below): recipient side (d'Avaux's papers via Bougeant), Hessian staff and court (Rommel,
  Eberstein family history), the same autumn's royal letter to Eberstein (Caillet 1912), and the press of the day (Gazette 1640 --
  unreachable).

### 1. Search log (8 Oct 2026; full log `audsigchav/search-log.tsv`)

| family | searched | result |
|---|---|---|
| (b) Hessian: Rommel, *Geschichte von Hessen* VIII (1843) | IA 11749504bsb `_djvu.txt`, grep Eberstein, Melander, Chavigni, Bouthillier, Avaux, Longueville, Pension/Geschenk/gratif | pp. 588-590: Banér blamed Melander for the failed campaign; Amalie, "to sacrifice to unity with Sweden and France", gave the command to Kaspar von Eberstein as Generallieutenant (summer 1640). No French gratification, no Chavigny despatch |
| (b) Hessian: *Geschichte der Freiherren von Eberstein* (1865) | IA geschichtederfr00ebergoog, grep | pp. 732-733: Melander quarrelled with Banér at Saalfeld, proposed Kaspar von Eberstein, who received the Generalat "Anfang Juli" 1640. No French reward |
| (b) Hessian: *Amalie Elisabeth, Landgräfin von Hessen* (1812) | IA 10019860bsb, grep | Eberstein 0 |
| (a)/(b) Caillet, documents of the Morin-Pons collection (Bibl. mun. de Lyon) on France and the Landgravine, *Correspondance historique et archéologique* 19 (1912), pp. 61-66 | found by IA global full text "comte d'Heberstein"; IA lacorrespondancehistorique19 | **prints Louis XIII to the comte d'Eberstein, Saint-Germain-en-Laye, 9 Nov 1640, countersigned Bouthillier**: glad the Landgravine has given him her armies' command, and has ordered La Boderie "de vous donner une marque du gré que je vous en sçauroy"; the closing spells him "d'Heberstein". Caillet's note sends the reader to AAE Allemagne t. XII and XIV. Not this despatch; see section 3 |
| (a) d'Avaux's side: Bougeant, *Histoire des guerres et des négociations qui précédèrent le traité de Westphalie* II (1751, "composée sur les Mémoires du Comte d'Avaux") | IA histoiredesguerr002boug (be-api, then `_djvu.txt`); the 1727 4to and vol. III by be-api | Livre VI (1640): the d'Avaux-Salvius talks on renewing the Hamburg treaty, margins citing the King's despatches and Pufendorf; the Erfurt junction of Longueville and Guébriant with Banér, the Hessians and Lüneburg; France's interest "à s'attacher la Landgrave de Hesse & les Ducs de Lunebourg". No Chavigny despatch of 25 Aug 1640, no Longueville-command clause, no Eberstein gratification (Eberstein only at Kempen, 1642) |
| (a) French print: Siri, *Memorie recondite* VIII; *Mercure françois* XXIII-XXIV | be-api "Eberstein" | 0 |
| (a) AAE Correspondance politique 1640 (Allemagne, Hambourg, Suède) and its État numérique / inventories | IA advancedsearch | no inventory copy online on IA; the volumes (and the minute or duplicate of this despatch) unread, manuscript, not online here |
| G3 press: *Gazette* 1640 | IA advancedsearch | no IA copy; Gallica 403 all day, not probed (brief) -- unreachable |
| (e) Google Books | 6 queries + 2 after a pause (key, country=US) | 7 x HTTP 429, 1 x 200 / 0 items; stopped (good-citizen rule) -- unreachable this pass |
| (g) JSTOR | JSTOR-QUEUE.tsv | two rows appended, families (i) and (ii) |

Requests: archive.org 18 (advancedsearch 7, metadata 4, `_djvu.txt` download 7), be-api.us.archive.org 9 (plus the prior_work.py
G3 run's own ia-global calls), www.googleapis.com 8 (7 x 429), all one at a time, >= 1.6 s apart. Gallica 0.

### 2. Classification

| item | prior plaintext | prior decipherment | class | key |
|---|---|---|---|---|
| Baluze 170 f.229r-v (Chavigny to d'Avaux, Amiens, 25 Aug 1640) | none located: not in Bougeant II (built on d'Avaux's own papers), Rommel VIII, the Eberstein history, Caillet 1912, Siri VIII, Mercure françois XXIII-XXIV, nor in the sources AUD1/AUD2 logged | none located | **N3 (stays)** | published (Tomokiyo) |

Why it stays at N3 and does not reach N4: the printed families the brief names are now covered on both sides, but three things the
N4 bar needs are still open. (1) The AAE volumes, which may hold a minute or a deciphered duplicate; Caillet names Allemagne XII and
XIV for the Eberstein correspondence. A manuscript copy is "internal or unpublished work", but the published AAE inventory was not
reached either. (2) The press of the day: the 1640 *Gazette* is only on Gallica, which answered 403 all day. (3) Google Books was
unreachable this pass. JSTOR is queued and blocks nothing on its own. Why not N1/N2: no printed text of the passage, in cipher or in
clear, was located, and nobody else's reading of these signs was found.

### 3. External check and depth (keep or lower only)

- **Caillet 1912 corroborates the gratification clause from outside the cipher.** The reading's last ciphered sentence, "ON gratiffiera
  le comte d'Heberstein qui luy doit succeder affin de l'obliger a mieux faire que son predecesseur" (f.229v L12-15, letter signs M), is
  matched eleven weeks later by the King's letter of 9 Nov 1640, countersigned Bouthillier. It sends La Boderie to give Eberstein "une
  marque du gré" for serving the Landgravine, and it spells the name "d'Heberstein" as the reading does. Rommel VIII and the Eberstein
  history independently confirm "qui luy doit succeder": Eberstein took Melander's command in July 1640, after Banér blamed Melander.
  That also fits 73= = Banér (Bougeant's "Banier") in "la trop grande fermete de [73=]", AUD2's ruling; the value stays at the key's.
  These are non-statistical checks of *content*. They supply no sign value, they do not turn an M letter sign into H/C/S, and they do
  not change the 29%.
- **Depth: D2 (stays)**, "partially deciphered (about 29%)" (106/366 H). The 80% H/C/S bar for D3 is not met; depth is keep-or-lower
  only under the 8 Oct depth bar. The external check goes into the record so a later D3 ruling has it to hand.
- **Verifier's sentence (D2), written from the reading and the print:** "Chavigny tells d'Avaux in cipher that the King will give a
  gratification to the comte d'Heberstein, who succeeds [Melander] in command of the Landgravine's army, to bind him to do better than
  his predecessor -- a promise carried out on 9 Nov 1640, when Louis XIII wrote to Eberstein that La Boderie would give him a mark of
  his favour (printed by Caillet 1912)." Conditional on the M letter signs.

### 4. Safe and unsafe sentences; corrections

- **Safe:** AUD1's sentence with this audit's sources added: "... no prior decipherment or printed text of it was located in ...,
  Bougeant's *Histoire des guerres et des négociations* II (from d'Avaux's papers), Rommel's *Geschichte von Hessen* VIII, the
  Eberstein family history (1865) or Caillet's Morin-Pons documents (1912) (searched 8 Oct 2026, three audits); the King's letter of
  9 Nov 1640 printed by Caillet corroborates the Eberstein clause's content."
- **Unsafe:** "first decipherment", "previously unread", "new", or anything that presents France's reward to Eberstein as unknown. The
  reward is in print (Caillet 1912). What this passage adds is the *instruction* and its stated purpose, written in cipher on 25 Aug.
  research/SIGNIFICANCE-2026-10-08.md line 15 says "The command quarrel and Eberstein's appointment are already in print; what is ours
  is the coded intention". That stands, but it should now add that the reward itself was carried out and printed. That correction
  is made in the "## Lane SIG additions" line, not by rewriting line 15.
- No over-claim found in the target's files. status.json: `audit_refs` gains this section, `audit_status` "three audits", `gap`
  updated; class, depth and key unchanged. SECOND-OPINIONS-QUEUE.tsv SO-BAL170-F229: class and counts unchanged, row left as filed.

## AUDIT 1 f.228 (SIG-V228), 8-9 Oct 2026, 23:46-00:1x UTC by date -u

Verifier: SIG-V228 (account 1, Opus), for LANE SIG-1, brief `.claude/briefs/runs/2026-10-08-acct1-sig1-jobs.md` section "SIG-V228".
Separate from the solvers (SIG-B228, SIG-B228B, B167-228) and from both f.229 audits. No decoding: the committed reading was read, not
re-derived. Search files in `sigv228/`; downloaded texts kept outside the repository (re-fetchable from the IA ids below).

### 1. Item under audit

| field | value |
|---|---|
| Item | BnF Baluze 170, f.228r-v, the cipher passages on the first leaf of the letter ff.228r-230r (Gallica ark btv1b90015040, canvases 239 right and 240 left) |
| Sender, recipient, place, date | Léon Bouthillier, comte de Chavigny, to Claude de Mesmes, comte d'Avaux. One letter, not two: f.228r begins it, f.229r-v continues the same bare cipher, and the clear close on f.230r reads "Amyens ce 25 Aoust 1640" with Chavigny's signature (D1-BAL170, from the c239-241 overview; f.228 has no separate date or subscription). So the date 25 Aug 1640 comes from this letter's own close and not from a different f.229 letter. The clear words on f.228r a_L01 ("par ce que Madame la Langrave et les d[ucs]") were checked by this verifier on the crop |
| Claim under audit | NOTES "## SIG-B228B": reading_b170f228.txt, H 71 / M 70 / I 12 / U 1 of 154 cipher tokens, fr17 -0.925 vs real_p05 -0.935 (PASS by 0.010); content sentence "the cipher says Chavigny doubts the Landgravine of Hesse-Kassel would come to terms with the enemy because of the treaty she has recently made with the King" |
| Key | Tomokiyo's "D'Avaux's Cipher (1637-1641) (DE=16')" table (key.tsv), plus our shape values for the f.228 letter signs (f.229 values; SIG-B228/B exemplar tests). Key source: **published** (Tomokiyo's table, credited) **plus ours** (the letter-sign shape values) |
| Period decipherment on the leaf | none (survey.tsv c239-241 "absent"; D1-BAL170) |
| Prior print of any part | Tomokiyo, louisxiii.htm l.361: "f.228, undeciphered: "sont mal satisfaits de *", ...". Four words of f.228r a_L02 are therefore in print as his partial reading, with the name left as `*` |

Distinctive phrases (as read): "sont mal satisfaits de [73]"; "point a propos dans cette conjoncture de le traitter de la me[?]me sorte"
(clear + cipher); "quelque crainte que la langrave et les ducs de Lunebourg [...] avec les ennemis"; "qu'ainsy luy et [73=] soient contraincts
de se retirer chacun de leur coste"; "le traitte qu'elle a fait depuis peu avec le Roy"; "a tous ajustemens raisonnables pour le bien" (clear).

### 2. Prior-work gate (pasted)

`python3 tools/prior_work.py baluze167-davaux-1637 --item-spec 'shelfmark=BnF Baluze 170;folio=228r;date=1640-08-25;sender=Chavigny;recipient=Avaux;place=Amiens' --step-type audit --fetch`
first run: `holds: specific 19 (DONE 1, LEAD 18); generic 2 (UNCHECKED-NET 2) ... exit 3: the step is DONE`. The 17 own-folder LEADs (escalation
checkboxes of solver steps) and the Bourdeau holder LEAD (line 239: Tomokiyo fragments only, DECODE R2761 key only) were answered CONTEXT with
`--record`. Re-run: `holds: specific 1 (DONE 1); generic 2 (UNCHECKED-NET 2) / verdict plaintext: UNCHECKED-NET / verdict step: DONE / exit 3`.
**The DONE is a unit-matching artefact, not a prior audit of this item:** the status.json row it matches is "BnF Baluze 170 ff.229r-v (letter
ff.228r-230r)", i.e. the f.229 passage audited by AUD1/AUD2-B167; no AUDIT section covered f.228 before this one. Proceeded on that reading.
G3: `... --reading ciphers/baluze167-davaux-1637/reading_b170f228.txt --network` -> `6-g3 CLEAR ... ia-global: no hits`; `6-g3 UNCHECKED-NET
... gbooks: not searched (blocked: HTTP 429)`; `exit 3` (same DONE). Google Books also failed the 23:4x key livecheck (works yes->no).

### 3. Independent search log (8-9 Oct 2026)

`python3 tools/print_check.py ciphers/baluze167-davaux-1637 --phrases .../sigv228/phrases.txt --sources .../sigv228/sources.tsv --out .../sigv228/print-check.tsv`
-> `8 phrases, 9 listed sources: 92 rows, 2 with hits` (the 2 are CrossRef keyword rows whose top hits are unrelated ODNB/Oxford
Scholarly Editions entries on other Landgravines and other Avaux/Chavigny). Per source: the 7 listed IA volumes (Avenel VI, Rommel VIII,
Justi 1812, Charvériat II, Boppe 1887, Le Laboureur 1657, Noailles 1913) x 8 phrases = 56 rows, **no hits**; IA global full text 6 phrases
no hits, 2 (`j'ay peine a le croire veu le traitte`, `a tous ajustemens raisonnables pour le bien`) HTTP 502, not searched; OpenAlex 9 no
hits; Google Books 8 and Semantic Scholar 9 **not searched (HTTP 429)**. Requests: archive.org 1, be-api 8, googleapis 1, openalex 9,
semanticscholar 1, crossref 2 (plus this verifier's own 3 IA metadata/advancedsearch calls and 3 `_djvu.txt` downloads).
Raw: `sigv228/print-check.tsv`, `sigv228/print-check-hosts.tsv`.

| family | searched | result |
|---|---|---|
| (a) canonical series: Avenel, Richelieu VI-VIII | AUD1-B167's whole-volume greps cover this letter (no Chavigny despatch to d'Avaux of 25 Aug 1640); Avenel VI re-run through print_check with the f.228 phrases | not found |
| (b) sender/recipient correspondence | Le Clerc *Négociations secrètes* t.1 (from 1642), Boppe 1887 (d'Avaux and his father; its 25 Aug 1640 letter is the father's) covered by AUD1/AUD2 for this letter; Boppe re-run with the f.228 phrases | not found. No edition of Chavigny's despatches to d'Avaux located |
| (c) Hesse-Kassel side | Rommel, *Geschichte von Hessen* VIII (1843, IA 10021035bsb, `_djvu.txt` grep): Chavigni 1 hit (1630s patents), Avaux 2 (a 1638 letter to Amalie Elisabeth, the 1643 plenipotentiaries), Lunebourg 2 French hits (Du Mont 1641 treaty text; a footnote), none of the f.228 phrases. Justi, *Amalie Elisabeth* (1812, IA 10019860bsb): 0 Chavigny/Avaux/Banér | not found. Context only: Rommel VIII p.553 n. says the Dorsten treaty with France (1639) supplemented the Hamburg treaty and that Amalie Elisabeth lifted her secret reservation against France only in March 1640 (ratification to La Boderie, revers of 24 Mar 1640) -- consistent with "le traitte qu'elle a fait depuis peu avec le Roy" in Aug 1640; it corroborates the reading's sense, it does not supply it |
| (c) Brunswick-Lüneburg side, Banér's 1640 campaign | Charvériat, *Histoire de la guerre de trente ans* II (1878, IA histoiredelaguer02char): Avaux 68, Banier 245 hits, Lunebourg 2; none of the f.228 phrases, no Chavigny | not found. Le Laboureur 1657 and Noailles 1913 (Guébriant) covered by AUD1 and re-run with the f.228 phrases |
| (d) holding archive and project pages | BnF archivesetmanuscrits Baluze 170 (AUD2-B167, read 8 Oct: no edition or decipherment named); DECODE R2761 = ff.228-230, "Decrypted", Inline Plaintext No, key only (CS-6, AUD1) | no decipherment of f.228 located beyond Tomokiyo's fragment |
| (e) full text: IA, Google Books | print_check (above) on 8 f.228 phrases; G3 ia-global | IA: see table; Google Books unreachable this session (429) |
| (f) solver repositories and blogs | Tomokiyo louisxiii.htm (on disk): only the one f.228 fragment, nothing else from this letter; repo-wide grep of `sources/` for "mal satisfaits"/"Lunebourg": only Tomokiyo and two unrelated BnF finding aids; Bourdeau and Aymeloglu as re-cloned by AUD2-B167 on 8 Oct (no Baluze 170 reading; Aymeloglu only DECODE row 2761) | Tomokiyo's fragment is the only prior reading located |
| (g) scholarship | OpenAlex and CrossRef via print_check (above). JSTOR: two rows appended to JSTOR-QUEUE.tsv, family (i) Chavigny AND Landgrave AND Lunebourg AND 1640 AND cipher terms, family (ii) the bare quoted phrase "le traitté qu'elle a fait depuis peu avec le Roy" | see table; JSTOR queued |

Unreachable or not searched: Google Books (HTTP 429 this session); Semantic Scholar (HTTP 429; AUD2's 8 Oct queries for the same
letter found nothing); IA global full text for 2 phrases (HTTP 502); the AAE Correspondance politique (Allemagne/Hesse) and Chavigny's own registers (not online here); the Calenberg/
Lüneburg archive editions (none located on IA by title; not searched further); Gallica not touched (403 to cloud sessions on 8 Oct).

### 4. Adversarial reading check

**Crop spot check (34 tokens, native crops):** f.228r a_L02 (all 12 cipher tokens), c_L01 (2), f.228v b_L02 (first 18), b_L05 (10 of 10
cipher tokens), b_L06 (9). Sign identity and order agree with ciphertext_b170f228.txt on every token; the letter shapes match the classes the
reading uses (h = n, u4 = t, minim pair = l, wave/v = s, crossed ff = s, 4u = a, g+ = n, r-shaped sign = g, y+ = r, q = c). **Marks do not all
agree:** on f.228r a_L02 the numeral transcribed `16'` carries no acute (the crossbar of the preceding ff runs over it), `73=` carries no
overbar, and on c_L01 `86'` carries no acute. These three are exactly as D1-BAL170B's eye re-check recorded them ("'16 73' carry no mark or
bar (was 16' 73=); c_L01 86 has no tick"); SIG-B228 then re-marked them from two blind Sonnet reads (`b167228/sig_marks.tsv`).

**Correction 1 (grades).** SIG-B228 regraded 15 unmarked numerals to H because two Sonnet reads named a mark. That gate's control (prereg
item 6) tested only marks that are present (4 acute controls); it could not fail on the axis that matters here, a reader that sees a mark
where there is none (rule 3: a control orthogonal to the error). SIG-B228B's tight-crop reads then named "acute" on both pre-registered
"none" controls and SIG-B228B itself concluded Sonnet mark detection on this hand "is not a usable instrument at either scale". This
verifier's eye agrees with "no mark" on 3 of the 15 checked. So the 15 `sig_marks.tsv` regrades are not H. **Corrected counts: H 56, M 70,
I 27, U 1 of 154** (the 15 return to I, their pre-SIG-B228 grade; values unchanged, so the judge numbers are unchanged). Most consequential:
the name in "sont mal satisfaits de [73]" (f.228r a_L02) is **not** read -- an unmarked 73 has no value in the table; Tomokiyo left the same
spot as `*`. "Bavier" stands only at f.228v b_L03 (73= transcribed with its bar by both D1-BAL170B passes). Not applied to the reading
files here (no decoding in this brief): the next solver step sets `b167228/to_pipe.py` to grade the sig_marks tokens I and re-runs `--check`.

**Correction 2 (content sentence).** The verb of the fear clause is unread: f.228v b_L02-03 "la c [13] m mo de n t avec les ennemis" (13 is
unresolved, sued|co). "Come to terms with the enemy" is an inference (plausibly "s'accommodent"), supported by the clause that follows ("et
qu'ainsy luy et Bavier soient contraincts de se retirer chacun de leur coste"), not a reading. The sentence must say the verb is unread.

**Cipher vs clear share of the quoted clauses.** Of the clauses the solver quotes, the frame is clear text: "TESMOIGNE QU'IL A QUELQUE",
"ET QU'AINSY", "POUR", "J'AY PEINE A LE CROIRE VEU", "DEPUIS PEU", "MAIS POUR", "C'EST CHOSE QUI N'EST PAS" (plus f.228r a_L01 "par ce que
Madame la Langrave et les d[ucs]" and "a ce que l'on nous [mande]", "point a propos dans cette conjoncture"). The content words are cipher:
"crainte", "la langrave", "les ducs de Lunebourg", "avec les ennemis", "luy et Bavier soient contraincts de se retirer chacun de leur coste",
"le traitte qu'elle a fait", "avec le Roy". About 120 of the roughly 300 letters in those clauses are clear; the claimed meaning (doubt about
the Landgravine, reason = her recent treaty with the King) sits on the boundary: "I can hardly believe it" and "recently" are clear, the
subject and the reason are cipher.

**With every M letter doubted** (letter signs replaced by `?`, the 15 regraded numerals by their value with `?`): "crainte que ... la ????rave
et ca du?? de lune bo??? la ?[13]?mo de ?? [avec?] les enne mi? ... luy et Bavier so?en? con?ra????? de se re[ti?]re ?? ha cu? de leur co??e
POUR cu la ????rave J'AY PEINE A LE CROIRE VEU le [traitte?] que ?le ? fait DEPUIS PEU [avec?] le Roy MAIS POUR les du?? de lune bo???".
What survives on H numerals plus clear words: a fear about "la ...rave" (Madame la Langrave is named in clear on f.228r) and "Lunebo[urg]"
in connection with "les enne mi[s]"; "luy et Bavier" withdrawing ("se re..re", "chacun de leur coste"); and "J'AY PEINE A LE CROIRE" of the
"...rave" because of something "que ...le ... fait DEPUIS PEU ... le Roy". "Traitte" there rests on 29 with a diaeresis (`29:?`, M in the
file); this verifier sees the two dots on the b_L06 crop, and 29: = traitte is the key's own value. So the sentence survives in this form:
Chavigny finds it hard to believe of the Landgravine, given what she recently [made] with the King; the "treaty" and "she has made" add two
M-dependent words, and "come to terms" does not survive.

**Authentication distance (rule 4a, depth bar).** Longest contiguous H stretch after correction 1: 11 letters ("le Roy" / "les du", across
a clear-word break; inside one cipher run it is under 10). The design is a nomenclator of about 150 marked numerals plus homophonic letter
signs; H(K) counts the 70 M letter signs, 27 I and 1 U as liberties, and the published key does not shrink it. No stretch approaches 1.5 x
unicity. **Cipher clause: not met.**

**Judge.** fr17 PASS by 0.010 (-0.925 vs real_p05 -0.935), above all 40 shuffled nulls, positive control 3/3. The margin rests on four M
letter values fixed by an exemplar test whose decoy gate passed at its minimum (2/3), and the letter-sign transcription is shape-class
labelled with f.229 values, so it is not independent of the decoded text (the ARM-C1 caveat AUD1-B167 stated for f.229). Read as "worth a
verifier", not as confirmation of any one word.

### 5. Classification

| item | prior plaintext | prior decipherment | class | key | confidence |
|---|---|---|---|---|---|
| Baluze 170 f.228r-v (Chavigny to d'Avaux, Amiens, 25 Aug 1640; first leaf of the letter whose f.229 passage is classed N3 above) | four words only: Tomokiyo prints "sont mal satisfaits de *" from f.228 (louisxiii.htm); nothing else located | Tomokiyo's fragment (KNOWN-PART); no other | **N3** for the passage, with the f.228r fragment "sont mal satisfaits de" excluded as N1 (Tomokiyo) | published (Tomokiyo's table, credited) plus ours (letter-sign shape values matched to f.229 exemplars) | moderate: same gaps as the f.229 audits (AAE series, Chavigny's registers, JSTOR queued) plus Google Books unreachable this session |

Why not N4: the AAE and Chavigny's own registers are unread, Google Books was unreachable, JSTOR is queued.

- **Safe sentence:** "The cipher passages on Baluze 170 f.228r-v (Chavigny to d'Avaux, Amiens, 25 Aug 1640) were read by us with Tomokiyo's
  published D'Avaux key and letter-sign values matched to the same letter's f.229 (56 of 154 cipher tokens at grade H; the letter signs
  at M). Apart from the four words Tomokiyo already quotes ("sont mal satisfaits de"), no prior decipherment or printed text was located in
  Avenel's Richelieu letters, Rommel's *Geschichte von Hessen* VIII, Charvériat, the Guébriant histories, Boppe 1887, Internet Archive
  full text, OpenAlex or CrossRef (searched 8-9 Oct 2026)."
- **Unsafe sentences:** "first/new decipherment" or "previously unread" (rule 10); "the cipher says the Landgravine would come to terms
  with the enemy" (the verb is unread); "dissatisfied with Banér" for f.228r (the name there is an unmarked 73, unread); "H 71".

### 6. Depth (rule 4a, depth bar of 8 Oct 2026)

- Tokens: **56 / 154 = 36% H/C/S** (after correction 1); M 70 (letter signs and numerals with doubtful marks), I 27, U 1. Unread:
  names/codes 2 (13 "sued|co" in the fear clause; 73 unmarked on f.228r), other 1 (U, the wave-like sign f.228r b_L02).
- **Cipher clause: not met** (above).
- **Code clause: met.** 10: = "les" reads in two independent f.228v phrases, "avec les ennemis" (b_L03, on H en-ne-mi) and "mais pour les
  ducs de Lunebourg" (b_L07, clear-word frame); 9: = "luy" in "avec luy" (f.228r c_L01) and "luy et Bavier" (f.228v b_L03); 10: also reads
  "les" seven times on f.229 (AUD1/AUD2-B167). Neither rests on a sig_marks regrade.
- **Verifier's sentence (D2), from the reading, letter signs M:** "In cipher Chavigny reports a fear that the Landgravine and the dukes of
  Lüneburg would [verb unread] with the enemy, so that 'he' and [73=, Bavier in the key, Banér by context] would each be forced to withdraw
  to his own side; of the Landgravine he writes that he can hardly believe it, given the treaty she has recently made with the King, but of
  the dukes of Lüneburg he does not say the same." Context (Rommel VIII: Hesse-Kassel's French alliance confirmed March 1640) is
  consistent and is not used to supply any word.
- **Depth: D2**, outward words "partially deciphered (about 36%)".

### 7. Postmortem and corrections

- Over-claim 1: SIG-B228's 15 mark regrades to H, carried into SIG-B228B's "H 71" -- corrected here to H 56 / I 27 (section 4); NOTES.md
  carries a pointer under SIG-V228.
- Over-claim 2: SIG-B228's "sont mal satisfaits de Bavier [Banér]" on f.228r and the "Landgravine ... dissatisfied with Banér" sentence --
  the name there is unread.
- Over-claim 3: SIG-B228B's "come to terms with the enemy" -- the verb is unread.
- No novelty wording found in the solver sections. Rule 10: this section alone assigns the class.

### Revision carried in (9 Oct 2026, LANE SIG-1 orchestrator, rule 10 propagation)
Correction 1 above is now applied to the decode files (NOTES "## SIG-V228 correction applied"): counts H 56 / M 70 / I 27 / U 1 as stated
here. The "claim under audit" judge figure (-0.925 PASS) is superseded: the corrected reading scores **-0.956 vs real_p05 -0.918, FAIL**,
above all 40 shuffled-key nulls (max -1.172), positive control 3/3. f.228r b_L01 no longer reads "traitter" ("de le gu r de" with the
unmarked numerals at I). Class and depth as written above are this verifier's; the second audit (AUD2-SIG-228) rules on them with this revision.

## AUDIT 2 f.228 (AUD2-SIG-228), 9 Oct 2026, 00:14-00:4x UTC by date -u

Verifier: AUD2-SIG-228 (account 3, Opus), for LANE-VERIFY-4, brief `.claude/briefs/runs/2026-10-08-acct3-verify4-jobs.md` section
"AUD2-SIG-228" and WORK-QUEUE row AUD2-SIG-228. Separate from the solvers (B167-228 acct 4, SIG-B228/B228B acct 1) and from the first
auditor (SIG-V228 acct 1); account 3 neither read nor first-audited f.228. No decoding of the committed files: the grade correction was
simulated on a scratch copy of the folder. Files: `aud2sig228/`.

### 1. Which reading was audited

SIG-V228 audited **SIG-B228B's reading** (the 4 u4/4u -> a overrides applied): its claim row quotes B228B's counts (H 71 / M 70 / I 12 /
U 1) and its text quotes B228B's "qu'elle a fait"; `b167228/sig2_shape_map.tsv` and B228B's to_pipe.py change landed on main in
a38dd34a6 (23:52 UTC, folded into a generically titled commit) before SIG-V228's 3f439fd1e (00:00 UTC). The committed reading is still
that one: `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check` -> `ciphertext_b170f228.txt: tokens 154: H 71, I 12,
M 70, U 1 ... reading up to date`, exit 0 (9 Oct 00:16 UTC). No difference to carry.

### 2. The grade correction, re-run

Scratch copy of the folder with `b167228/sig_marks.tsv` emptied to its header, then `b167228/to_pipe.py` and `tools/decode_key.py` on
the copy (`aud2sig228/reading_b170f228_corrected.txt`): **H 56, I 27, M 70, U 1 of 154**, exactly SIG-V228's corrected counts. The 15
changed tokens are the 15 sig_marks rows, all H -> I. **But the correction is not value-neutral, as SIG-V228 stated ("values unchanged,
so the judge numbers are unchanged"):** 13 of the 15 keep their value, two change:
- f.228r a_L02 `73=` Bavier -> unmarked `73` = "so" (SIG-V228 already said this name is unread);
- f.228r b_L01 `29:` traitte -> unmarked `29` = "gu": **"point a propos dans cette conjoncture de le traitter de la me[?]me sorte" (SIG-V228's
  distinctive-phrase list) loses "traitte(r)"**; the f.228r line reads "de le [29]r de la me [?] me so r te". (The f.228v b_L06 `29:?`
  "le traitte que l le a fait" is not a sig_marks row and is unaffected.)
- Also I after correction, besides the 73: f.228r c_L01 `86` "avec" (in "avec luy") and f.228r b_L02 `98` "fait", `40` "la".

**Judge on the corrected reading** (`b167228/judge_null.py` unchanged except the token file, fr17 spec d4vb167/judge_spec_fr17.json,
seed 20261008; `aud2sig228/judge_corrected.py`, `.out`):
| text | SIG-B228B (as committed) | corrected grades (this audit) |
|---|---|---|
| reading_b170f228, U dropped | -0.925 vs real_p05 -0.935, PASS by 0.010, N 294 | **-0.956 vs real_p05 -0.918, FAIL by 0.038**, N 285 |
| shuffled key, all signs, 20 | max -1.063 | max -1.228 (median -1.340) |
| shuffled letter-sign values, 20 | max -1.134 | max -1.172 (median -1.244) |
| positive control, f.229 same N, 3 segments | 3/3 PASS | 3/3 PASS (unchanged) |
So the fr17 PASS rested on the two value changes the mark regrades made; with the regrades withdrawn the reading FAILs the p05 gate
narrowly while staying above all 40 shuffled nulls. Per rule 3 (ZX-DEC349) this is "judge cannot decide" near the gate, not a negative,
and no period gloss of this hand at this length exists to score (SIG-B228B). Any sentence citing "fr17 PASS" for f.228 is withdrawn.

### 3. Prior-work checks 3-5 (pasted)

- `python3 tools/prior_work.py baluze167-davaux-1637 --item-spec 'shelfmark=BnF Baluze 170;folio=228r;date=1640-08-25;sender=Chavigny;recipient=Avaux;place=Amiens' --step-type second-audit --fetch`
  -> `holds: specific 0 (none); generic 2 (UNCHECKED-NET 2) / verdict plaintext: UNCHECKED-NET / verdict step: CONTEXT / exit 0: proceed on
  the residue: whole item`. The two generic rows: 3-solver Aymeloglu (no cache) and 4-editions (no prior_editions.tsv row).
- 3-solver by hand: `git clone --depth 1 github.com/aaymeloglu/unsolved-ciphers` (9 Oct 00:2x), grep "baluze": only
  `catalogue/decode-catalog.csv` / `decode-records.jsonl` row 2761 "Baluze 170, f.228-230 ... Chavigni France Amyens ... Decrypted" (the DECODE
  catalogue line, key only per CS-6/AUD1), no reading. Bourdeau caches: CLEAR (tool).
- G3: `... --reading ciphers/baluze167-davaux-1637/reading_b170f228.txt --network` -> `6-g3 UNCHECKED-NET ... ia-global: not searched (HTTP
  503)`; `6-g3 UNCHECKED-NET ... gbooks: not searched (blocked: HTTP 429 ...)`; `exit 4`. SIG-V228's G3 had IA global CLEAR (no hits) on
  the same phrases; this audit adds nothing there.
- Google Books, one probe as briefed (`"mal satisfaits" Langrave Lunebourg`, country=US, key): **HTTP 429, "Quota exceeded for quota metric
  'Queries' ... per day"** -- the project's daily quota, not a rate burst; not retried. Google Books stays unsearched for f.228 in both audits.

### 4. Search log (families not repeated from SIG-V228 / AUD-SIG-CHAV; f.228's own words only)

| family | searched (9 Oct 2026) | result |
|---|---|---|
| AUD-SIG-CHAV's volumes, for f.228's words | be-api fts `Lunebourg`, `"mal satisfaits"`, `Langrave Lunebourg` in Bougeant II (histoiredesguerr002boug), Mercure françois XXIII (lemercurefranois23unkn), Siri VIII (memorierecondit03sirigoog) | Bougeant: `Lunebourg` 502, other two 0. Mercure XXIII: one page names "la Landgrave de Hesse & le Duc de Lunebourg" in a news report (Piccolomini and Hatzfeld moving) -- context of the 1640 campaign, not the letter; 0 for the phrases. Siri VIII: 0, 0, one 503 |
| Swedish side (new): Pufendorf | fts in *Suite de l'Introduction à l'histoire* (suitedelintroduc00pufe) and the French Charles Gustave history (bub_gb_0VQ_AAAAcAAJ_2, wrong reign, logged only) | Lunebourg hits concern George of Lüneburg and later events; 0 for "mal satisfaits"; one 503. Pufendorf's *De rebus Suecicis* (IA 10328986bsb etc., Latin) located but not searched (IA began answering 502/503; stopped per the good-citizen rule) |
| Brunswick-Lüneburg histories (Havemann), Chemnitz | IA advancedsearch by title | no IA item located under those titles; not searched further |
| Gallica | one SRU probe (`Chavigny` and `Lunebourg` and `Langrave`, before 1700) | HTTP 403 Cloudflare; not retried |
| scholarship | OpenAlex (key, header): "Lüneburg Hessen-Kassel 1640 Banér France" 0 results; "Amalie Elisabeth Hessen-Kassel Frankreich 1640" 20, none on this letter | not found |
| AAE Correspondance politique (Allemagne, Hesse) 1640; Chavigny's registers | no online inventory or printed selection located here (same as SIG-V228 and AUD-SIG-CHAV) | unreachable |
Requests: be-api.us.archive.org 15 (+ G3 via prior_work), archive.org advancedsearch 4, github.com 1 clone, googleapis 1 (+1 by G3),
gallica 1, api.openalex.org 2. IA answered 502/503 on 4 calls; no further IA requests after that.

### 5. Classification

| item | prior plaintext | prior decipherment | class | key | confidence |
|---|---|---|---|---|---|
| Baluze 170 f.228r-v (Chavigny to d'Avaux, Amiens, 25 Aug 1640) | Tomokiyo's four words "sont mal satisfaits de *" only | Tomokiyo's fragment (KNOWN-PART) | **N3 held**, the four-word fragment N1 | published (Tomokiyo) plus ours (letter-sign shape values) | moderate-to-low: Google Books unsearched in both audits (429), IA global unreachable this audit, AAE and Chavigny's registers unread, JSTOR queued |

Why not N4: as SIG-V228, and Google Books has now failed two audits running. Why not lower: no family searched by either audit found
the letter's text or a decipherment beyond Tomokiyo's fragment.

- **Safe sentence (replaces SIG-V228's):** "The cipher passages on Baluze 170 f.228r-v (Chavigny to d'Avaux, Amiens, 25 Aug 1640) were read
  by us with Tomokiyo's published D'Avaux key and letter-sign values matched to the same letter's f.229 (56 of 154 cipher tokens at grade
  H, the letter signs M); apart from the four words Tomokiyo already quotes ('sont mal satisfaits de'), no prior decipherment or printed
  text was located in Avenel's Richelieu letters, Rommel's *Geschichte von Hessen* VIII, Charvériat, the Guébriant histories, Boppe 1887,
  Bougeant II, the *Mercure françois* XXIII, Siri VIII, Internet Archive full text, OpenAlex or CrossRef (searched 8-9 Oct 2026, two
  audits); Google Books could not be searched."
- **Unsafe sentences:** SIG-V228's list, plus: "the reading passes the fr17 language judge" (with the corrected grades it fails by 0.038);
  "de le traitter de la même sorte" on f.228r (29 is unmarked, unread).

### 6. Depth (keep or lower; depth bar of 8 Oct 2026)

- Tokens re-counted on the corrected decode: **56 / 154 = 36% H/C/S**; M 70, I 27, U 1. Unread names/codes 2 (13 sued|co; 73 unmarked on
  f.228r), other 1 (U). Unchanged from SIG-V228.
- Cipher clause: not met (SIG-V228's count; the correction only shortens H stretches).
- Code clause: re-checked on the corrected decode. `10:` = "les" in "avec les ennemis" (f.228v b_L03; en-ne-mi H) and "les ducs de
  Lunebourg" (b_L07; du, lu, ne, bo H); neither 10: token is a sig_marks row. **Met.** SIG-V228's second example `9:` = "luy" is weaker
  than stated: "avec luy" on f.228r c_L01 now rests on an unmarked 86 (I), and "luy et Bavier" on an unmarked 96 "et" (I); it is not
  needed for the clause.
- This verifier's sentence (D2), from the corrected reading, letter signs M: "In the cipher of f.228v Chavigny reports a fear that the
  Landgravine and the dukes of Lüneburg would [verb unread] with the enemy, so that he and Bavier would each have to withdraw to his own
  side; of the Landgravine he finds it hard to believe, given the treaty she recently made with the King, but not so of the Lüneburg dukes."
- **Depth: D2 held**, "partially deciphered (about 36%)".

### 7. Postmortem and corrections

- SIG-V228 correction 1 is right in its counts but wrong that it leaves values and the judge unchanged: two values change and the fr17
  PASS becomes a FAIL by 0.038 (section 2). The solver step SIG-V228 named (grade sig_marks tokens I in to_pipe.py, re-run --check) should
  also re-run `b167228/judge_null.py` and expect `aud2sig228/judge_corrected.out`.
- SIG-V228's distinctive phrase "de le traitter" (f.228r) and the SO prompt's "de le traitter" rest on a mark regrade: corrected in
  `second-opinions/PROMPT-chatgpt-b170f228.md` (row SO-BAL170-F228, still queued) and in status.json.
- Not changed: the reading files, to_pipe.py, decode.py, keys (no decoding in this brief).

## AUDIT 3 f.228 (UNA3-BAL), 9 Oct 2026, 20:42-21:0x UTC by date -u

Verifier: UNA3-BAL (account 1, Opus), for the account-4 orchestrator, brief `.claude/briefs/runs/2026-10-09-account4-orch-unassigned-3.md`
section "UNA3-BAL". Separate from the solvers (B167-228, SIG-B228, SIG-B228B) and from both earlier f.228 auditors (SIG-V228, AUD2-SIG-228).
No decoding. Files: `una3bal/` (Google Books API responses as JSON).

### 1. Scope: the briefed step was already done twice

The brief was drawn from NOTES.md's SIG-B228B Verdict line ("a separate verifier on the f.228 reading"), which predates AUDIT 1 f.228
(SIG-V228) and AUDIT 2 f.228 (AUD2-SIG-228); `tools/prior_work.py baluze167-davaux-1637 --item-spec 'shelfmark=BnF Baluze 170;folio=228r;
date=1640-08-25;sender=Chavigny;recipient=Avaux;place=Amiens' --step-type second-audit` -> `verdict step: LEAD ... WORK-QUEUE AUD2-SIG-228 done
2026-10-09 00:36`, exit 4. Answer to the LEAD: a third full audit would repeat both; this audit works only the residue both left open,
**Google Books** (HTTP 429 in AUD2-SIG-228, daily quota), and re-checks the committed state.
- State: `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check` -> `ciphertext_b170f228.txt: tokens 154: H 56, I 27, M 70, U 1
  ... reading up to date`, exit 0 (20:4x UTC). The SIG-V228 grade correction is applied in the files (NOTES "SIG-V228 correction applied").
- `python3 tools/depth_check.py` exit 0 (20:48 UTC).
- JSTOR, both families, already answered for f.228: JSTOR-QUEUE.tsv rows (i) "Chavigny AND (Landgrave OR Landgravine) AND (Lunebourg OR
  Lüneburg) AND 1640 AND (chiffre ...)" and (ii) "\"le traitté qu'elle a fait depuis peu avec le Roy\"", both done 8 Oct 2026, no hit about
  the letter. SO-BAL170-F228 is queued. No further JSTOR or SO row is needed.

### 2. Google Books (API, key, country=US; 46 calls, 1.6 s apart, all HTTP 200; `una3bal/gbooks*.json`)

| query | result |
|---|---|
| `"mal satisfaits" Langrave Lunebourg`; `Chavigny Avaux 1640 Landgrave Lunebourg Amiens`; `"ajustemens raisonnables pour le bien"` | 0 volumes |
| `"traitte qu'elle a fait depuis peu avec le Roy"`; `"quelque crainte que la Langrave"`; `"contraints de se retirer chacun de leur coste"`; `"Madame la Langrave et les ducs"` | word-scatter hits only (Barbeyrac 1739, Michelet, Bossuet, Avenel's Richelieu letters 1642, *Teutsche Reichs-Archiv*); no snippet carries the letter's wording |
| `"ducs de Lunebourg" Chavigny 1640` | 1 volume: **Les papiers de Richelieu. Empire allemand, 1636-1642** (Google ids nUsjAQAAIAAJ, qIcMAQAAMAAJ, 6tRnAAAAMAAJ; Anja Hartmann, Adolf Wild; NO_PAGES, snippet only) |

**The edition (a source family neither earlier audit searched).** *Les papiers de Richelieu*, Section politique extérieure, Empire allemand,
the 1636-1642 volume (Google Books dates the record 1982; editors Anja Hartmann and Adolf Wild per the record). Its snippets show it prints
Chavigny-to-d'Avaux despatches **from these very volumes**, with German headnotes and `[: ... :]` brackets inside the French text, e.g. no. 142
"Chavigny an d'Avaux, Rueil 1639 II 19, Paris, BN, Fonds Baluze 169, fol. 191-193, Ausfertigung"; "Baluze 170, fol. 258-259" (Rueil
1640 XI 10, with "[: le traitté qu ..."); "Baluze 170, fol. 147-148, Konzept"; "Baluze 171, fol. 6-7". What the brackets mark was not seen
in an explanatory note; that they mark the passages in cipher is an inference from the pattern, not established.
For **f.228 (Amiens, 25 Aug 1640)** the edition's table of contents, as snippeted, runs "... [no. 183] ... Amiens 1640 VIII 4 ... 411 /
184 - Ferdinand III. an den Reichstag, Regensburg 1640 IX 13 ... 414" -- no numbered item between 4 Aug and 13 Sept 1640, so the f.228-230
letter is **apparently not printed as an item**. Queries `"Amiens 1640 VIII 25"`, `"Baluze 170" "fol. 228"`, `"fol. 228-230"`, `"Baluze 170"
"fol. 229"` returned nothing in this edition (the one `"fol. 228-229"` hit is the 1630-1635 volume, Mantua, unrelated). A quotation in a
footnote or headnote of another item is **not excluded** (snippet view only). Queued for a page view: LOCAL-QUEUE row L71.

Outside this item (reported, not worked): the same edition prints **"Baluze 168, fol. 246-248v°, Kopie"** with a German headnote (Vienna,
the Emperor wants no general peace, only to divide Sweden and France). That is the folder's f.246-247v bare passage (168 f.246). Whether the
cipher passage appears there in clear decides prior work for that passage and may give a clear text for the f.247 hand (the NOTES gap "look for
a glossed text in the f.246-248 hand"). Also in L71.

### 3. Classification (keep or change)

| item | prior plaintext | prior decipherment | class | key | confidence |
|---|---|---|---|---|---|
| Baluze 170 f.228r-v (Chavigny to d'Avaux, Amiens, 25 Aug 1640) | Tomokiyo's four words only; the Papiers de Richelieu 1636-1642 volume has no item of this date by its snippeted table of contents | Tomokiyo's fragment (KNOWN-PART) | **N3 held**, the four-word fragment N1 | published (Tomokiyo) plus ours (letter-sign shape values) | moderate-to-low: the edition's notes are unread (L71), AAE Correspondance politique and Chavigny's registers unread |

Why not N4: a principal edition of exactly this correspondence (the Papiers de Richelieu) is now known and read only by snippet.
Why not lower: no searched family carries the letter's text.

- **Safe sentence (replaces AUD2-SIG-228's):** "The cipher passages on Baluze 170 f.228r-v (Chavigny to d'Avaux, Amiens, 25 Aug 1640) were
  read by us with Tomokiyo's published D'Avaux key and letter-sign values matched to the same letter's f.229 (56 of 154 cipher tokens at grade
  H, the letter signs M); apart from the four words Tomokiyo already quotes ('sont mal satisfaits de'), no prior decipherment or printed text
  was located in Avenel's Richelieu letters, Rommel's *Geschichte von Hessen* VIII, Charvériat, the Guébriant histories, Boppe 1887, Bougeant
  II, the *Mercure françois* XXIII, Siri VIII, Internet Archive full text, Google Books, OpenAlex or CrossRef (searched 8-9 Oct 2026, three
  audits); the *Papiers de Richelieu* volume for the Empire 1636-1642 lists no item of this date but was read only in snippet view."
- **Unsafe sentences:** AUD2-SIG-228's list, plus "Google Books could not be searched" (it was, 9 Oct 2026) and any sentence implying the
  Papiers de Richelieu were checked in full.

### 4. Depth

No change from AUD2-SIG-228: 56/154 = 36% H/C/S on the committed (corrected) decode; cipher clause not met; code clause met by `10:` "les"
("avec les ennemis", "les ducs de Lunebourg"). **D2 held**, "partially deciphered (about 36%)". The D2 sentence stands as AUD2-SIG-228 wrote it.

### 5. Postmortem and corrections

- The step was briefed from a Verdict line two audits stale: the SIG-B228B "## Escalation" Verdict was never superseded after AUDIT 1/2 f.228,
  and NEXT-STEPS.tsv copied it. Corrected by a fresh "## Remaining gaps" / "## Escalation" / Verdict in NOTES.md (UNA3-BAL).
- status.json f.228 row: `depth_check` still cited "fr17 PASS by 0.010" and "9: luy" as a code example, and `gap` said the regrades were not
  yet applied and Google Books unsearched; corrected to the committed state (fr17 FAIL by 0.038 after the correction; regrades applied 9 Oct
  00:24; Google Books searched; Papiers de Richelieu snippet-only).
- Requests: www.googleapis.com 46 (all 200). No other host.

## AUDIT 4 f.228 (V-BAL167), 13 Oct 2026, 09:45-10:0x UTC by date -u

Verifier V-BAL167, account 4, for LANE DEFAULT-A4-0935 (brief `.claude/briefs/runs/2026-10-13-acct4-default-0935-jobs.md` "V-BAL167").
Not the solver (BAL-CROP and BAL-WL were owner-account sessions). Scope: template steps 1, 3a and 4 on the BAL-WL regrade (31 f.228 letter
tokens M -> S); the N-class is not in question and no novelty search was run. Disk only; no network; no subagent (item 3 settled from files).

### 1. Claim under audit
NOTES "## BAL-WL": a same-key wrong-label control passed (G1 P+ 0.917, G2 P- 0.000, one blind read) and 31 f.228 letter-sign tokens move
M -> S, values unchanged; f.228 now H 56, S 31, M 39, I 27, U 1 of 154.

### 2. Checks
| # | Check | Result |
|---|---|---|
| 1 | PREREG pushed before the read | **PASS.** `418e47a3` (07:41:35 UTC) adds only PREREG-BAL-WL.md + tiles_wl.py; `d45c9168` (07:44:36) adds read1.tsv, tiles, key, score, regrade. `git diff 418e47a3 d45c9168` on PREREG-BAL-WL.md is empty (unchanged after the read). Note: this clone is shallow at 41067c83; the order was read after `git fetch --shallow-since`. |
| 2 | Controls can differ from the target on the scored statistic (rule 3, AX-5799) | **PASS.** The statistic is the yes-rate on a proposed label; P+ and P- are the same kind of tile (same key, hand, leaves, geometry) and differ only in the proposed label, which is the input the yes/no depends on. They did differ (0.917 vs 0.000), and T (0.815) could sit anywhere. P tiles exclude the 12 exemplar instances (tiles_wl.py / tiles.py split: first labelled occurrence per letter = exemplar), so P+ is not identity matching. Reader not anchoring: P- best exemplar = true letter 10/11. |
| 3 | The 31 regrades are exactly those the gate licenses | **PASS, none reverted.** PREREG "Adoption": tokens of a CONFIRMED class move M -> S. score1.out CONFIRMED: q 6/6, ll 4/4, ll\|u4 1/1, u4\|4u 4/4, anchors 4u=a 1/1 and u4=t 1/1, y+ 2/2, ff 2/2, h 1/1. Exceptions file: q 6, ll 4, ll\|u4 1 (the tiled r_a_L02 token, a_L02 pos 4), ff 2, y+ 5, h 7, u4/4u 6 per token (the six tiled positions only) = 31. Majority-no classes (g+, hook, v) and gam (untested) not regraded. Tokens transcribed with an uncertain shape (`ll?`, `ll\|u4?`) are regraded only where their own tile was read; the second `ll\|u4?.` token and `q:` / `?(q-like)` are not in the file (fewer, not more). |
| 4 | Rule 7 re-derivation | **PASS.** `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check` -> `ciphertext_b170f228.txt: tokens 154: H 56, I 27, M 39, S 31, U 1` / `reading up to date`. `score_wl.py read1.tsv r20261013/key_private.tsv` is byte-identical to score1.out; `regrade.py` rewrote exceptions_b170f228.tsv byte-identically (clean `git status`). reading_tokens_b170f228.tsv vs its parent: 31 rows changed, all M -> S, zero non-grade changes. Values unchanged, so the fr17 input (values) is unchanged and its FAIL by 0.038 stands (AUDIT 2 f.228). |

**Limits a reader should weigh (none voids the gate, so no revert):**
- P- wrong labels were random letters from {a c l n r s t}, mostly visually distinct from the true sign. Only one within-key look-alike pair
  was tested (X50, true a / proposed t, the 4u/u4 mirror pair; rejected high). The control shows the reader rejects clearly wrong labels; its
  power against a near look-alike wrong value inside the key is mostly untested.
- Nine of the 31 S tokens carry S by class membership from the two-pass transcription, not their own tile: h 6 of 7 (one tile, the class
  verdict rests on it) and y+ 3 of 5. The PREREG licenses class-wide adoption; these nine depend on the transcription's shape labels too.
- ff=s rests on two low-confidence yeses; the gloss also fixes ff=s on f.258r (P+ X44, H15 "Brunswick", yes/low).
- One read only (the PREREG allowed a second read only on a gate failure).

### 3a. Depth (rule 4a), f.228r-v
- H/C/S: 87 of 154 cipher tokens = **56.5%** (H 56, S 31); unread: M 39, I 27, U 1 (name/code: `73=` Bavier read H, `sued|co` M; other M/I
  mostly letter signs and unmarked numerals).
- Cipher clause: longest H/C/S stretch about 12 letters ("n te que cu la l a", "le Roy les du c"), under the authentication distance: **not met**.
- Code clause: **met** by `10:` "les" ("avec les ennemis", "les ducs de Lunebourg"), unchanged.
- D3 not reached (needs >= 80% H/C/S). **D2 held**, outward words "partially deciphered (about 56%)".
- `python3 tools/depth_check.py` -> exit 0 (`unique solves (N3+ and D2+): 214 -- D4 5, D3 151, D2 58`); f.228 counted at N3/D2.
- True sentence (this verifier, from reading_b170f228.txt): in cipher, Chavigny writes that someone has shown a fear that the Landgravine and
  the dukes of Lüneburg would [verb partly unread] with the enemy, so that he and Bavier (73=, Banér by context) would each have to withdraw to
  his own side; Chavigny can hardly believe it of the Landgravine, given the treaty she recently made with the King, but does not say the same
  of the dukes of Lüneburg.
- status.json f.228 row: `depth` stays D2; `depth_pct` 36.0 -> 56.5 and `depth_check` / `depth_note` / `depth_by` / `depth_date` updated to
  this audit (the percentage is a depth field and the old figure would misstate the outward "about N%").

### 4. Postmortem
No over-claim found in BAL-WL's NOTES section: it said depth was not changed and a verifier was owed, and listed the same limits as above.
Lesson for the next control of this shape: draw some P- wrong labels from within-key look-alike pairs (4u/u4, h/g+, hook/v/ff for s) so the
negative tests the confusions that matter, not only random letters.
Requests: none (disk only). Subagents: none.

## AUDIT 5 f.228 (V-GHV), 13 Oct 2026, 10:52-11:0x UTC by date -u

Verifier V-GHV, account 4, for LANE DEFAULT-A4-0935 (brief `.claude/briefs/runs/2026-10-13-acct4-default-0935-jobs.md` "V-GHV").
I am not the solver (BAL167-GHV was session_01GfKaq9M3AqQrXZARpx32DY). Scope: the BAL167-GHV regrade (NOTES "## BAL167-GHV", PREREG-BAL-GHV.md
c60720e55, result commit ccdff89ef): 8 f.228 letter tokens M -> S (hook 7, v 1). The N-class is not in question and no novelty search
was run. Disk only, no network, no subagent.

### 1. Checks
| # | Check | Result |
|---|---|---|
| 1 | PREREG pushed before either read, and it provides for a second read | **PASS.** c60720e55 (10:38:39 UTC) adds only PREREG-BAL-GHV.md; ccdff89ef (10:42:07) adds glossA/B, labels, both reads, tiles and scores. `git diff c60720e55 origin/main -- PREREG-BAL-GHV.md` is empty. The PREREG's labels section lists the f.239r labels as "Expected (not yet read)", and the read gave 'pressa[?]' where it expected 'presser', which fits a PREREG written before the gloss reads. Its gates section says, in its own words: "If either fails on read 1: ONE second read (fresh subagent, seed 20261014) only within the 80% line; gates on read 2 alone." Read 2 was that read (seed 20261014), done well inside the 80% line (11:25). The second read was provided for, so it does not void the regrade. |
| 2 | The within-key look-alike negative can differ from the target on the statistic (rule 3, AX-5799) | **PASS, with a limit on power.** The statistic is the yes-rate on "same sign as E-s2". P- tiles are signs from the same key and hand whose gloss fixes a value other than s. The tile is the thing the yes/no depends on, so P- can come out at any rate, and so can T. Eye check of r20261014/sheet.png: the two z-swashes (N1, N2; u/y) are real near look-alikes, each a single curved stroke with a tail. The r-shape (N3, g) and the h (N4, n) are visually distinct from the hook, so they test very little. In effect the negative has 2 near look-alike tiles and 2 easy ones. All 8 P- answers were "no" (7 high), and the reader's best exemplar was E-b/E-n/E-g, never E-s2. This addresses V-BAL167's lesson for the u/y swash only. |
| 3 | What read 1's FAIL means for read 2's PASS | **Read 2 used the same instrument as read 1:** the same 9 tiles, the same E-s2 exemplar sheet and the same question. Only the tile order and the subagent changed. G1 failed on read 1 because of one tile: P+ L2 (the f.239r looped hook-form, 'presser'/'Salaire') read no/low on read 1 and yes/low on read 2. Every other tile gave the same yes/no on both reads, and both T tiles were yes/high on both. So read 2's PASS is that one low-confidence tile flipping. Taking the better of two reads raises the chance of passing, and gating on read 2 alone hides this. Pooling both reads, which is stricter than the PREREG: P+ 5/6 = 0.833 (G1 >= 0.75 still passes), P- 0/8 = 0.000, T 4/4 yes/high. The regrade stands on the pooled figures too, but the reader cannot settle the looped variant. |
| 4 | The 8 regrades are exactly what the gate licenses | **PASS, none reverted.** PREREG adoption: a CONFIRMED class moves all its f.228 tokens M -> S. score2.out confirms T:DECOY:hook=s and T:v. In the reconciled passes I count 7 `s:hook` tokens on f.228v (none with `?`) and 1 `s:v` token (f.228r a_L02 pos 7). The PREREG's "v 2" counted a comment line (`# ... col9 s:v (A v\|hook, B v)`) too, so the file holds fewer rows than the PREREG named, never more. Of the exceptions file's 39 rows, 31 are BAL-WL's, unchanged, and 8 are BAL167-GHV's. g+ (no form found on 5 glossed leaves) and gam stay M. reading_tokens_b170f228.tsv vs c60720e55: 8 rows changed, M -> S only, and no value changed. |
| 5 | Rule 7 and depth | **PASS.** `score_ghv.py` reproduces score1.out and score2.out byte-identically. `regrade_ghv.py` -> `8 tokens M -> S {'v': 1, 'hook': 7}`. `tiles_ghv.py 20261013` / `20261014` regenerate every tile and key byte-identically (clean `git status`). `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check` -> `ciphertext_b170f228.txt: tokens 154: H 56, I 27, M 31, S 39, U 1` / `reading up to date`. Values are unchanged, so the fr17 judge input is unchanged too. |

### 2. Depth (rule 4a), f.228r-v
- H/C/S: 95 of 154 = **61.7%** (H 56, S 39). Unread: M 31, I 27, U 1.
- Cipher clause: the longest H/C/S stretch is now 13 letters ("malsatisfaits", from reading_tokens_b170f228.tsv). That is far under the authentication distance (AUDIT 2: no stretch near 1.5 x unicity with ~98 letter liberties), so the clause is **not met**. Code clause: **met** (`10:` "les" in two contexts, unchanged).
- D3 needs at least 80% of tokens H/C/S, so f.228 is not D3. **D2 held.** `python3 tools/depth_check.py` -> exit 0 (`unique solves (N3+ and D2+): 214 -- D4 5, D3 151, D2 58`).
- The AUDIT 4 true sentence stands. No word in it depends on the 8 regraded tokens' values, and those values did not change.
- status.json is not edited, because depth did not change (the brief: depth fields only if depth changes). Parent item: status.json's `depth_pct` 56.5 now understates the share; 61.7 is the current figure. That only makes the outward "about N%" lower than it should be, never higher.

### 3. Postmortem
BAL167-GHV's NOTES section does not over-claim. It reports read 1's FAIL, says the gate was taken on read 2 under the PREREG, gives the
v 2 -> 1 count, and names the small arms and the one-tile-per-class limit. Three corrections and points for future work:
(a) The NOTES label basis for L2 combines two different supports. Both gloss reads put 'Salaire' over the hook (@9). The H codes on either
side (mm=p, 66'=re | hook | 71'=se, y=r) give 'presser'. Either one gives s, so the label stands, but the H-code alignment does not
support the gloss word 'Salaire'. (b) When a PREREG allows a second read on failure, the score file should also give the pooled
figure across both reads, so a reader can see whether the pass depends on taking the better read. Here it does not (pooled G1 0.833).
(c) Half the P- arm (r-shape, h) is not a near look-alike of the hook. Next time, the negative should take every
glossed z-swash/gam-type curl that can be found and drop the visually distinct shapes.
Requests: none (disk only). Subagents: none.

## AUDIT 6 f.228 (V-GSEQ), 13 Oct 2026, 21:38-21:5x UTC by date -u

Verifier V-GSEQ, account 2, for LANE DEFAULT-A2-2013 (brief `.claude/briefs/runs/2026-10-13-ytbiz-default-2013-jobs.md` "V-GSEQ").
I am not the solver (BAL167-GVER and BAL167-GSEQ were account-2 workers; GSEQ was session_01MVjyuMaQSTUEDsJ2e5x1Ds). Scope: the
BAL167-GSEQ regrade of the 3 f.228v g+ tokens M -> S (value n unchanged), resting on PREREG-BAL-GPLUS.md (376e75224), BAL167-GVER's
result (5fd337f2e), PREREG-BAL-GSEQ.md (4ef9e9bb6) and BAL167-GSEQ's result (886a934f0). The N-class is not in question; no novelty
search, no network, no subagent.

### 1. Checks
| # | Check | Result |
|---|---|---|
| 1 | PREREG order; is the sequence rule a different instrument or a retry? were the reads blind of the key? | **PASS on order.** 376e75224 (20:56:34) adds only PREREG-BAL-GPLUS.md, before GVER's gloss reads (5fd337f2e, 20:58:34). 4ef9e9bb6 (21:19:33) adds only PREREG-BAL-GSEQ.md, runs.tsv and settle_gseq.py, after GVER's (a) failed and before settle.out and every tile (886a934f0, 21:22:07). `git diff 4ef9e9bb6 origin/main` on the PREREG, the script and runs.tsv is empty. **Instrument:** the sequence rule is a different statistic from the x rule. It ignores x positions and consumes the gloss word against published H values, so it is a second instrument, not a re-run with one knob loosened. Three qualifications. (i) It uses the same two reads. (ii) It was written after GVER's own NOTES "Lead" had already shown that gt = n under this reading. So the hypothesis was formed and tested on the same data. It is not a held-out test. (iii) Its tolerance TOL = 1 carries the result. My re-run at TOL = 0 gives n on 4 of 6 token-reads; read B fails on both words, 'consintent' vs 71' se and 42' li vs 'si'. That is NOT SETTLED under the PREREG's 6/6 condition. The PREREG gives the reason for TOL = 1 in advance (e/i slips in a handwritten gloss), and at TOL = 1 the shuffled key still never settles (0/1000). So the tolerance did not buy false settles, but it was set with B's slips in view. **Blind:** glossA/B.tsv are what the readers wrote: numerals, sign descriptions and gloss letters. They were told no key value, no f.228 value and not Tomokiyo's table (PREREG-BAL-GPLUS (a)). I cannot check the prompt text itself, which was not committed. Both reads describe the sign in identical words, "gt (g-like with crossed t stroke)", which may come from the prompt; that label has no bearing on the gloss letter. |
| 2 | Circularity; can the shuffled-key control differ on the statistic? | **PASS.** The rule reads only rows of key.tsv with grade H and an acute code. Every anchor or consumed value (90' con, 71' se, 76' te, 43' lo, 44' lu, 72' si, 42' li; 40', 19', 16', 51' never reached) is `H tomokiyo-acute`, i.e. Tomokiyo's published table. None is an M or S value, and none comes from f.124 or g+. Letter signs (h, q, K, u4) take one letter each, and their BAL-WL S values are not used (M3). **Control:** the settle statistic depends on the key values (where the anchor falls, how many letters each sign consumes, and the mismatch count), and permuting the values changes all three. So C2 can differ from the target, and it does: 0/1000 settles, and 20/6000 token-reads with a single leftover. This is not the AX-5799 shape. The limit is that C2 tests whether the gloss agrees with the key. It does not test the letter: with the key fixed, the leftover is position arithmetic. What makes it a test of the letter is that three different words ('consentent', 'longues', 'conclusion') land on the same letter. **My added check (scratch, not committed):** I let every non-H sign and gt take 0, 1 or 2 letters instead of M3's fixed 1. The leftover sets are then {'', n, nt}, {'', n, ng} and {n, on}. The only value common to all three tokens is n, so M3's untested one-letter assumption does not decide the value once the sign is taken to have one value. C1 (10/10) passes, but it is weak: blanking a fixed-length sign returns the gloss letters at that position by construction, so it is a consistency check, not a test of power. |
| 3 | Tile test (b) as PREREG-BAL-GPLUS wrote it; V-GHV (c) on P- | **PASS as written, with a weak P- arm.** Exemplar E-g+ is f.124r's first gt (tile at 785,170). T is the 3 f.228 g+ tiles from sig_tiles TARGET. P+ is f.124r line-final and f.124v after K. P- is the crossed y = r on f.229 L4 and the f.228 decoy, plus the r-shape = g on f.239r N3. The bare g was not forced, so the arm runs with 3, as the PREREG allows. Gates are as written: G1 P+ 2/2 = 1.000, G2 P- 0/3 = 0.000, T 3/3 yes/high, on one read with no second read. **V-GHV (c):** by eye on r20261013/sheet.png, the two crossed-y tiles (X01, X02) are partial look-alikes: a descender with a horizontal bar, but no t-stem. The r-shape (X08) is visually distinct and tests nothing. So P- has 2 moderate tiles and 1 easy one, and no true near look-alike. A plain g, or the gt's own g bowl without the t, is not in the arm. On the other side, the gt is a highly distinctive two-part ligature. All three T tiles and both P+ tiles show the same 'g' + crossed 't' form at a glance, which agrees with BAL167-GPLUS's own identification. The test confirms sign identity, and that identity is not in doubt. The arm's weakness limits what the gate proves about the reader; it does not cast doubt on these tiles. |
| 4 | The 3 regrades are exactly what the gate licenses | **PASS, none reverted.** PREREG-BAL-GSEQ "If SETTLED ... n: run PREREG-BAL-GPLUS (b) exactly as written", whose adoption clause licenses the 3 f.228 g+ tokens M -> S if all T are confirmed and the settled value is n. Both conditions are met. exceptions_b170f228.tsv gains exactly 3 rows: b_L01 14, b_L03 1, b_L05 9, each n S. I checked these positions against d1bal170b/rec_f228v/ciphertext_draft.tsv's `s:g+` rows (1-indexed 11, 2, 9 on lines whose reading-token numbering is offset by the wrapped first line on b_L01 and by 1 on the others; the neighbouring tokens ll/u4 -> l/a line up in each case). reading_tokens_b170f228.tsv vs 4ef9e9bb6: 3 rows changed, grade M -> S only, value n unchanged. |
| 5 | Rule 7 and depth | **PASS with one gap.** `python3 balshape/gseq/settle_gseq.py` reproduces settle.out byte-identically. `python3 balshape/gplus/tiles_gplus.py 20261013` regenerates every tile, sheet and key_private.tsv byte-identically (clean `git status`). `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check` -> `ciphertext_b170f228.txt: tokens 154: H 56, I 27, M 28, S 42, U 1` / `reading up to date`. **Gap:** no committed script writes balshape/gplus/score1.out. score_ghv.py expects a `same_as_E-s2` column and tileread1.tsv has `same`. I recomputed the gate by hand from tileread1.tsv + r20261013/key_private.tsv: P+ 2/2, P- 0/3, T 3/3, so score1.out's figures are right. They are not script-regenerable, though, so the evidence file falls short of rule 7's letter (the reading itself is). Follow-up for a solver job: commit a scorer (or a `--col` option on score_ghv.py) that reproduces score1.out. |

### 2. Depth (rule 4a), f.228r-v
- H/C/S: 98 of 154 = **63.6%** (H 56, S 42). Unread: M 28, I 27, U 1.
- Cipher clause: the longest H/C/S stretch is still 13 letters ("malsatisfaits", reading_tokens_b170f228.tsv). The g+ tokens do not join longer runs, so the clause is **not met**. Code clause: **met** (`10:` "les" in two contexts, unchanged).
- Under 80%, so not D3. **D2 held.** `python3 tools/depth_check.py` (output in the done line).
- The AUDIT 4 true sentence stands. Values are unchanged, so the fr17 judge input is unchanged.
- status.json: `depth_pct` 61.7 -> 63.6. `depth_check`, `depth_by` and `fields_source` now name this audit. `depth` stays D2.

### 3. Postmortem
BAL167-GSEQ's NOTES section does not over-claim. It names the second-instrument status, the stated M3 limit, the small arms, the single
read, and its own order slip (prior_work.py run after the PREREG push). Points to carry forward:
(a) A rule written after a lead has already shown the answer on the same data is a confirmation of that lead, not an independent test.
Say so in the PREREG. Report the result at the strictest tolerance as well (here TOL = 0 gives 4/6), so a reader can see what the
tolerance carries.
(b) A PREREG'd gate needs a committed scorer in the same push as its output (rule 7). A hand-written score1.out is right here, but cannot
be regenerated.
(c) V-GHV (c) still applies: P- for a ligature sign should be its parts (a bare g, a lone crossed t) and other descender-plus-bar signs,
not shapes that differ at a glance.
Regrades: 3 kept, 0 reverted. Requests: none (disk only). Subagents: none.

## AUDIT 7 f.22r (VER-BAL22), 14 Oct 2026, 07:23-07:4x UTC by date -u

Verifier: VER-BAL22 (account 1, Opus), brief `.claude/briefs/runs/2026-10-14-acct1-default-0640-jobs.md` row VER-BAL22, for LANE
DEFAULT-A1-0640-14. Separate from the solver (BAL169-F22, session_01ThV43oDmKJK4XeTgdCDTXN). Earlier sections are not rewritten.
Search files in `verbal22/`. No decoding beyond re-running the committed decode; no key edit; no subagent.

### 1. Item under audit

| field | value |
|---|---|
| Item | BnF Baluze 169 f.22r lines 1-4 (Gallica ark btv1b9001488b, canvas 48): 24 cipher tokens inside clear French, no interlinear gloss (checked by this verifier on images/b169sweep/src_c048_f22r_1285,1140,2950,810.jpg) |
| Letter | f.21-24, Claude Bouthillier, Ruel, 21 May 1639 (per BAL169-SWEEP; signature and date not re-read by this verifier); recipient d'Avaux per the volume |
| Claim under audit | "...obligee de se deffaire de Milandre ... qu'elle en voulust donner le commandement a Mr de Ransau dont j'escris ... au S. de la Boderie", H 4 I 1 M 19 |
| Rule 7 | `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check` re-run here: `ciphertext_b169f22r.txt: tokens 24: H 4, I 1, M 19` / `reading up to date`, exit 0 |
| Key | Tomokiyo's D'Avaux table (key.tsv). Key source: **published** (credited); 100' faire is an I-grade addition (key.tsv) |
| Spec / judge | none (no spec for this target): no judge_plaintext run; 24 tokens is too short for one in any case |

### 2. Eye check of the reading against the image and Tomokiyo's table (images/louisxiii_davaux.png)

Numerals. Separate acute strokes, distinct from the i-dot of a written 1, stand over 71, 94, 51, 41, 13 (L03) and 70; 95 and 100 carry
acutes; 81 has a clear overbar. The solver graded 71', 51', 41', 13' M under the dotted-i rule; on this leaf the acute is a long
separate stroke, so those four could be H (an under-claim, left as is). A stroke above the 45 region (L03) may belong to 45 or to the
sign before it: 45' stays M. 12 and the second 13 (L03) show one dot only (the i of the 1): no diaeresis is visible, plain 12 has no table
value, and 12: ment / 13: Mr are chosen by context (M, right). 65 has no mark; only 65' ra exists in the table (M, right). The 16s carry the
6's own top flourish, which may or may not be the acute (M, right).

Letter signs (the solver "settled from context in this letter only"):
| pos | shape on the leaf | solver | Tomokiyo table, nearest shape | verifier |
|---|---|---|---|---|
| L01 8 | two minims + crossed 4 ("u4") | f | u4/n4 forms stand under t (and a u4 under g, row 3); f's row-1 form is an m-with-7 hook | context only: **I** |
| L03 4 | y with a long horizontal bar through the descender | r | crossed y under r (also r on 170 f.229 L4, V-GSEQ P- arm) | supported by the table: M |
| L03 7 | three minims + crossed 4 ("m4") | m | m4 under m | supported: M |
| L03 9, L04 1 | h (L04 with tail) | n | h under n | supported: M |
| L03 12 | y/4 top over a horizontal bar crossed by a vertical stem | a | closest table form is the crossed 7 under **d**; a's form is the plain (circled) 7 | context only, against the nearest table shape: **I** |
| L04 3 | y with a large curl | u | curled z/3 form under u; plain y is b | weak match: M |

So 2 of the 6 letter values (f, a) rest on context alone, one of them against the nearest table shape. Grading them M over-states them;
rule 4 calls a value inferred from context I. Verifier grade count for the 24 tokens: **H 4, I 3, M 17** as committed with that
correction (or H 8, I 3, M 13 if the four clear acutes are promoted; not done here, a solver's regrade). The reading's sense is not in
doubt for "se [de]f faire de Milandre" and "don ne r le co m ma n de ment": the numerals there are table values and the letter signs m, n, r
match the table. "a Mr de ra n sa u" rests on 12:, 13:, 65 and the a sign, all chosen by context.

### 3. Independent search log (14 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series: Avenel VI (1638-42) | print_check `ia` rows (6 phrases, verbal22/print-check.tsv); be-api fts in the volume: positive control "Milandre" 1 hit (an analysis "...de Weymar aupres de la landgrave et de Milandre..."), "Ransau" 0, "Rantzau Milandre" 0 | not found |
| (b) sender/recipient correspondence | Le Clerc, Négociations secrètes t.1 (secretestouchant01lecl), print_check `ia` | not found (collection starts 1642, AUD1-B167) |
| (c) histories of the campaign | Le Laboureur, Guébriant 1657 (bub_gb_cM5KS3lziccC); Noailles, Guébriant 1913 (lemarchaldegu00noai), print_check `ia` | not found |
| (d) holding archive / project pages | Tomokiyo louisxiii.htm (on disk): lists Baluze 169 ff.2-6, 46, 80, 52, 107, 112, 97, 129, 142 ... 208; **no f.21-22**. DECODE (sources/decode/records-decrypted-2026-09-24.tsv): Baluze 169 records 2759 (f.2-6) and 2760 (f.208-211) only. Lasry BnF research snapshot (sources/cyphersolver/2026-10-14-lasry/): no Baluze folder | no decipherment of f.22r located |
| (e) full text IA, Google Books | IA global fts, 6 phrases: 0. Google Books (keyed, country=US): 5 of 6 phrases HTTP 503 in print_check; one retry after a pause on two targeted queries ("deffaire de Milandre"; Milandre Ransau Landgrave): 503 again -> **unreachable**. The one phrase it answered (the clear "dont j'escris presentement au S. de la Boderie") returned a 334-volume word-bag match, no snippet carrying the phrase | IA not found; Google Books unreachable |
| (f) solver repositories / blogs | as (d); Bourdeau/Aymeloglu catalogues per CS-6 (3 Oct), not re-cloned | not found |
| (g) scholarship | OpenAlex (keyed) 6 phrases + keywords: no relevant work; CrossRef keywords: top hits are Elizabeth of Bohemia correspondence entries and Hesse-Kassel reference articles, none on this letter; Semantic Scholar: one phrase answered (5 unrelated papers), then HTTP 429, one manual keyed call (Melander Rantzau Hesse 1639) total 0; JSTOR: 4 rows appended to JSTOR-QUEUE.tsv, families (i) and (ii) | not found; S2 partly unreachable; JSTOR queued |

Not searched / unreachable: Google Books (503); the AAE Correspondance politique (Allemagne, Hesse) and Bouthillier's minutes; Acta Pacis
Westphalicae; Rommel, Geschichte von Hessen VIII (cited in AUD2 as searched for f.228, not run for these phrases); the holding record
on archivesetmanuscrits. Requests: be-api.us.archive.org 6 (print_check) + 3, www.googleapis.com 6 + 2, api.openalex.org 7,
api.crossref.org 2, api.semanticscholar.org 2 + 1 (one 429); a first print_check run crashed at write (wrong --out) after making the same
calls, so these hosts saw about twice the print_check counts. All >= 1.6 s apart.

### 4. Classification

| item | prior plaintext | prior decipherment | class | key | confidence |
|---|---|---|---|---|---|
| Baluze 169 f.22r (Bouthillier to d'Avaux, Ruel 21 May 1639, 24 cipher tokens in clear text) | none located | none located (no gloss on the leaf; not in Tomokiyo's list; no DECODE record for f.21-24) | **N3** | published (Tomokiyo's table, credited) | low-moderate: Google Books unreachable for every cipher phrase, S2 partly 429, JSTOR queued, AAE minute not searched |

Why not N4: Google Books, the AAE series and the holding record were not covered. Why not N1/N2: no print of the passage, in clear or in
cipher, and no reading of it by anyone else, was found.

Depth (rule 4a): H/C/S 4 of 24 = **17%** as committed (8 of 24 = 33% at most with the acute promotions). Cipher clause: the longest H/C/S
run is two tokens; no stretch reaches the authentication distance once the 19 M/I liberties (mark choices and context-fitted letters)
are counted. Code clause: 81= Milandre reads in this one context only. **D1: fragments read.** No content sentence is written: at D1 the
rule asks none, and the "Ransau" clause rests on context-chosen tokens.

- **Safe sentence:** "Fragments of the 24-token cipher passage on Baluze 169 f.22r (Bouthillier to d'Avaux, 21 May 1639) were read by us
  with Satoshi Tomokiyo's published table; the cipher phrase reads 'se deffaire de Milandre' and 'donner le commandement', with the
  following name only partly supported; no prior decipherment or print of the passage was located in the sources logged in AUDIT.md
  (Google Books unreachable)."
- **Unsafe sentence:** "The passage reads 'donner le commandement a Mr de Rantzau'" or any wording that treats the commander's name as read,
  or calls the reading new or a first.

### 5. Postmortem and corrections
- Over-claim corrected: the f and a letter signs are context fits (one against the nearest table shape), I not M; NOTES.md BAL169-F22's
  "These agree with D4-B167's values" holds for h = n and the crossed y = r only. Correction note appended to NOTES.md; reading files
  untouched (a regrade is a solver's job: exceptions rows and a re-run of `decode_key.py --check`).
- Under-claim noted: four numerals with clear separate acutes (71', 51', 41', L03 13') could be H.
- Wording: NOTES.md BAL169-SWEEP called f.22r "the one new bare passage"; changed to "the one further bare passage" (CLAUDE.md wording rule).
- Next step for the reading: a blind shape check of the six letter signs against Tomokiyo's table and glossed exemplars (the BAL-WL
  method), and a fresh rule-7 re-derivation; the commander's name stays unread until then.
- SECOND-OPINIONS-QUEUE row SO-BAL169-F22 appended (N3).

BAL22-SHAPE (14 Oct 2026, account 2, solver job, no class change): blind shape check of the 7 letter signs of 169 f.22r, both reads passed the same-key wrong-label gates; 5 tokens M -> S, f -> I, u stays M; f.22r now H 4, S 5, I 2, M 13. See NOTES.md "## BAL22-SHAPE".
