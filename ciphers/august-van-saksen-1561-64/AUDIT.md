# AUDIT: William of Orange and Elector August of Saxony, WVO 126 (16 Sept 1564), 53 (24 Oct 1561), 57 (18 Nov 1561)

Classes (rule 10): **126 N4** (no prior decipherment located; V3 and A2 at N3, raised by 'N4 decision (D1)' at the end); **53 N3**, **57 N3** (A2, first verification). See section A2 below.

## V3 audit of WVO 126 (cipher postscript)

Verifier V3 for LANE V2, 24 Sept 2026 (08:51-09:05 UTC). This session did not solve the target and did not decode or
re-read the cipher. Claim under audit (LANE R worker R21, ROOM 08:41 UTC): "126 p4, 240 tokens: C 214 S 0 M 26 U 0;
key aligned from 98 f.66 against its decipherment on f.67; Spain news 1564: the Queen bled and purged twice, lost
the child." Letters 53 and 57 are not read and are out of scope.

## 1. Verdict

| item | class | prior plaintext | prior decipherment | confidence |
|---|---|---|---|---|
| WVO 126, postscript f.139 (Dresden, Geheimer Rat, Locat 8510/5, f.138r-140v) | **N3** | none located in print; a contemporary clear draft may survive unprinted (see 2.3) | none located | moderate |

Why not N4: the principal editions for this correspondence were searched (Groen t.I and Supplément, Gachard t.1-2,
Rachfahl I and II.2 [not II.1, see A2.2.2], Kluckhohn, von Weber, Raumer), but three named witnesses were not seen: the KHA minute with its
'Zeitung', the 20th-century Japikse copy in the KHA, and the Anna of Saxony literature (Böttiger 1836, Kretzschmar).
OpenAlex answered 429. See section 4.

Why not N0/N1: nothing on the leaf deciphers it. f.139 carries the cipher block, "Datum ut in lit[eris]", and
Orange's signature. Above line 1 there are four small letters ("e e r e") in a lighter hand. R21 found they
contradict the key, and they are not a decipherment. WVO's Opmerkingen say only "Het origineel met een postscriptum in
cijferschrift", with no "oplossing". For siblings 74, 98 and 153 the field does record one ("met de oplossing", "waarvan 2 oplossingen").

## 2. Item: WVO 126

### 2.1 Extracted from the repo
- Date and place: 16 Sept 1564, Brussels. From Willem van Oranje to August, Elector of Saxony.
- Witnesses (WVO record, fetched 24 Sept 2026): (a) Dresden HStA, Geheimer Rat, Locat 8510/5, "Schreiben", f.138r-140v,
  original, imaged at `resources.huygens.knaw.nl/media/wvo/images/00000-00999/00126.pdf`; (b) **KHA Den Haag, A 11/XIV
  I/4, nr. 26, minuut**; (c) KHA, Collectie Japikse, 20th-century copy. Opmerkingen: "Het origineel met een
  postscriptum in cijferschrift. De minuut met een 'Zeitung'."
- WVO Inhoud (clear letter only): Orange has heard from Wilhelm of Hesse that August is well, contrary to rumours of a
  hunting accident. Incipit "Wiewoll ich in gereumer zeitt von E. Churf. G. khein schreiben entpfangen". The summary
  does not mention the Spanish news.
- Plaintext as read (R21, `reading_126.txt`): "[Wir] konnen auch [E.L.] in freundtlichem vertrauen nit verhalten, [das]
  [wir] seidhero auss Hispanien andere zeitung bekommen haben, welche vermelden, [das] [die] Konnigin so heftig kranck
  [ge]worden sei, [das] man ir [die] adern zwei mahl schlagen [und] auch zwei mahl purgieren mussen, dermassen [das] sie
  irer frucht erlediget worden sei."
- Grades: 240 tokens, H 0, C 214 (from the known plaintext of sibling 98 f.67), S 0, M 26, I 0. Reproducible:
  `tools/decode_key.py ciphers/august-van-saksen-1561-64 --check`.
- What the solver searched: nothing for novelty (aligner brief). The earlier check-solved sweep (NOTES.md, 24 Sept
  2026) covered web search, Cryptiana, DECODE, and both solver repos for the trio.

### 2.2 The event is printed, the letter is not located
The news is the illness and miscarriage of Elisabeth of Valois, Queen of Spain, in August 1564. Histories of Philip
II's court print it widely. That makes it a phrase hook and a check on the date, not a prior print of this letter.
No edition located prints Orange's 16 Sept 1564 letter to August, its postscript, or a summary of the postscript.

### 2.3 The KHA minute
The minute (KHA A 11/XIV I/4 nr. 26) is recorded "met een 'Zeitung'". Chancery drafts of cipher postscripts were
normally written in clear before enciphering. This minute may therefore carry the postscript's text in clear, as a
newsletter enclosure or paragraph. If it does, the plaintext of this very item survives in the archive in clear, and
our reading is an independent decipherment of the Dresden ciphertext against an existing contemporary plaintext
(N0 in substance, although unprinted). WVO has not imaged the minute and no edition prints it. **Unverified. It is
the one lead that could lower the class.** A KHA request, or a WVO/Huygens inquiry for an image of A 11/XIV I/4 nr.
26, would settle it.

### 2.4 Did we first-decipher?
Not established. No prior decipherment was located in the families below. The KHA minute (2.3) may hold the
plaintext in clear, and it was not seen. Rule 10 allows no priority wording at N3.

### 2.5 Sentences
- **Safe:** "The cipher postscript of Orange's letter to Elector August of 16 Sept 1564 (Dresden Locat 8510/5 f.139;
  WVO 126) reads, with a key aligned from his 1563 letter WVO 98 and its contemporary decipherment, as news from Spain
  that the Queen had been bled and purged twice and had lost the child (C 214, M 26 of 240 signs). No prior decipherment
  or printed plaintext was located in Groen van Prinsterer, Gachard, Rachfahl or a full-text phrase search (24 Sept
  2026). The KHA minute of the letter, recorded with a 'Zeitung', has not been seen."
- **Unsafe:** "A previously unread cipher of William of Orange, deciphered for the first time" (N3 only; the KHA minute
  may hold the text in clear).

## 3. Search log (24 Sept 2026, all by this verifier)

| family | status | what | result |
|---|---|---|---|
| WVO record 126 (resources.huygens.knaw.nl) | searched | `wvo/app/brief?nr=126`, 1 request; fields Inhoud, Opmerkingen, Brongegevens | three witnesses (above); no oplossing; no edition in Brongegevens |
| WVO harvest (sources/wvo, sources/solver-diffs cijfer-96) | searched | rows 98, 126 | 98 "met de oplossing"; 126 "postscriptum in cijferschrift", none |
| Groen van Prinsterer, Archives 1st ser. t.I 1552-1565 (DBNL groe009arch01, full text) | searched | all letter heads to or from Saxony; the Aug-Nov 1564 section; Königin/Reyne/Royne, purg, frucht | Orange-August letters printed: XXIX, LXXXII (Apr 1564), and Saxony to Orange XXVII, XXXIII, LXXVI; **no 16 Sept 1564 letter**; the Spanish news absent |
| Groen, Supplément (groe009arch09) and Table (groe009arch10) | searched | 16 Sept 1564; Saxe/Sachsen + 1564; phrase roots | nothing |
| Gachard, Correspondance de Guillaume le Taciturne t.1, t.2 (IA correspondanced01willgoog, correspondancede02will) | searched | print_check phrases; grep Saxe/Auguste 1564, reine d'Espagne, fausse couche | nothing |
| Rachfahl, Wilhelm von Oranien I (1906), II.1 (1908) (IA wilhelmvonorani01rachgoog, 00rachgoog) [A2 correction: 00rachgoog is vol. II part 2 (1908); II.1 (1907) was not searched by V3, see A2.2.2] | searched | phrases; "Locat 8510"; Sept 1564; Königin + krank/Frucht | one citation "Dr. Arch. Locat 8510" (II.1, n. to p.667): 1566 Augsburg diet context, not this letter |
| Kluckhohn, Briefe Friedrich des Frommen I (IA bub_gb_3N1SAAAAcAAJ) | searched | phrases | nothing |
| von Weber, Anna Churfürstin zu Sachsen 1865 (IA annachurfrstin00webe) | searched (fts only) | phrases through be-api (djvu 500) | nothing |
| Raumer, Briefe aus Paris 1831 (IA bub_gb_EQ4MAAAAYAAJ) | searched | phrases | nothing |
| Böttiger, Vermählung Oraniens mit Anna von Sachsen (Hist. Taschenbuch 1836); Kretzschmar on Anna of Saxony | unreachable | IA advancedsearch by title: no item found | not seen |
| Demandt, Nassau-oranische Korrespondenzen (HessJb 38-39) | not applicable / unreachable | WVO cites it for 57 only, not 126 | not seen |
| Japikse (Collectie Japikse, KHA) | unreachable | unpublished 20th-c. copy | not seen |
| KHA minute A 11/XIV I/4 nr. 26 | unreachable | not imaged | not seen; see 2.3 |
| Dresden HStA catalogue (archiv.sachsen.de) | reachable, not searched at item level | Geheimer Rat is catalogued by Locat file, not by letter | no item-level record expected |
| Internet Archive global full text (be-api) | searched | 9 phrases (6 as decoded, 3 modernised) | no hits |
| Google Books API | searched | same 9 phrases | no hits |
| HathiTrust | not searched | no record numbers for the German Anna/Oranien literature to hand | gap |
| Solver repos (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers) | searched | fresh shallow clones, grep oranje/oranien/sachsen/saksen/8510/wvo | no hit for this correspondence |
| Cryptiana (sources/cryptiana/web german.htm, dutch.htm) | searched | grep | Saxony pages concern the 18th century only |
| DECODE (sources/decode, 24 Sept snapshot) | searched | grep Sachsen/Saxony/Oranien/1564 | only KHA Kauderbach 1754-56 records |
| Web search | searched | 2 queries (German, cipher + Queen of Spain + 1564) | nothing relevant |
| Scholarship: CrossRef | searched | 3 keyword queries | reference-work entries only (DOIs in print-check.tsv) |
| Scholarship: OpenAlex | unreachable | HTTP 429 on first call | not searched |
| Semantic Scholar, Persée, HAL | not searched | cap | gap |
| JSTOR | queued | 2 rows in JSTOR-QUEUE.tsv | pending, does not block |

Machine log: `print-check.tsv`, `print-check-hosts.tsv`, `phrases.txt`, `sources.tsv` in this folder.

## 4. Confidence
Moderate that no printed plaintext exists. Groen t.I prints Orange's April 1564 letter to August but not this one,
and Rachfahl, who used the Dresden files, does not mention it. The minute with its 'Zeitung' remains unseen and would
move the class down, not up.

## 5. Postmortem and corrections
No over-claim was found. R21 called the result a "cryptanalytic reading with a sibling key" and used no priority
wording. The status.json grade read "novelty not yet audited". One gap in earlier notes: the check-solved verdict and
`images/inventory.tsv` said 126 had "no printed-edition citation ... (manuscript only)" and "decipherment location:
none". Both overlooked WVO's second and third witnesses, the KHA minute "met een 'Zeitung'" and the Japikse copy. A
note was added to NOTES.md. Lesson: read every Brongegevens row, not only the imaged original, before calling a
postscript unsolved. A clear draft in the sender's archive is a decipherment witness.

Suggestion (not done): request an image of KHA A 11/XIV I/4 nr. 26 through the WVO team or KHA, and compare its
'Zeitung' with reading_126.txt.


---

# A2: second audit of 126, first verification of 53 and 57 (Auditor A2 for LANE V2, 24 Sept 2026, 09:20-09:38 UTC)

This session solved none of these letters and did not decode or re-read any cipher. Claims under audit: (a) V3's N3
for 126 (above); (b) LANE R2 S1's readings of 53 p1 and 57 p3 (NOTES.md "S1: 53 and 57", ROOM 09:12), whose search log
was an on-disk grep only.

## A2.1 Verdict

| item | class | prior plaintext | prior decipherment | confidence |
|---|---|---|---|---|
| WVO 126, postscript f.139 (Dresden Loc. 8510/5), 16 Sept 1564 | **N3** (V3's class stands after a second audit) | none located in print; KHA minute "met een 'Zeitung'" unseen and unimaged | none located | moderate |
| WVO 53, postscript f.266r-v (Dresden Loc. 9941/3), Breda 24 Oct 1561 | **N3** | none located | none located; the leaf carries none (both pages seen) | moderate |
| WVO 57, cipher "bijvoegsel" on p3 (KHA A 11/XIV B/41-6, received original), Torgau 18 Nov 1561 | **N3** | none located in print. Demandt's regests nr. 113 and 115 (read through Google Books snippets) summarise the clear letter and the 23 Nov postscript and do not mention the election. The sender's minute in Dresden (Loc. 9941/3 f.268-269, "met een 'Zettel'") is unseen | none located; the leaf carries none | moderate-low |

No item reaches N4: for each, a witness recorded by WVO itself (a minute or a 20th-century copy) was not seen, and
two of the open-index families (OpenAlex, Semantic Scholar) answered 429.

## A2.2 Findings that change the file

1. **53 has a second page that nobody had read.** The WVO PDF 00053 has two pages (checked 24 Sept 2026). Only p1 was
   ever fetched (manifest note "p2 not fetched"). p2 (f.266v) carries **three more lines of cipher** (about 90 signs),
   the end of the clear letter ("Datum Breda den 24 Octobris a[nn]o 61"), Orange's full signature, and an autograph
   postscript in clear about a recipe, a bitch and ferrets ("Das recept ... hundin sampt der fretgiren ... Dat. ut
   supra, Wilhelm printz zu Uranien"). There is no decipherment on either page. S1's reading of 53 (282 letters, 10
   lines) therefore covers **p1 only**. Its last word "mrch" is a line break, not the end of the postscript. The
   ciphertext continues at the top of f.266v. NOTES.md is corrected; the page is not transcribed here (not this
   brief). Crop for a solver: `images/00053_p2.png` (added, 100 dpi like the other pages).
2. **V3 mislabelled Rachfahl.** IA `wilhelmvonorani00rachgoog` (and `bub_gb_pIwKAAAAIAAJ`) is **vol. II, 2nd part (1908,
   pp. 518-901)**, not II.1. Rachfahl II.1 (1907), which covers 1559-1564, the marriage and Orange's news service to
   Dresden, is not on IA. It is full view on HathiTrust (`hvd.hnt3bj`, `njp.32101073665554`). HathiTrust page text is
   behind Cloudflare (1 request, 403 challenge, stopped). This audit checked it through the HTRC Extracted Features
   per-page token counts (574 pages, `data.htrc.illinois.edu`, 1 request). See A2.4.
3. **57's Dresden witness is a minute, not a copy.** WVO 57 lists (a) Dresden Loc. 9941/3 f.268r-269v **minuut**,
   "met een 'Zettel' en een tweede postscriptum d.d. 23 november"; (b) KHA A 11/XIV B/41-6 **origineel** (the imaged,
   received letter, with the cipher on p3); (c) Wiesbaden HHStA Abt. 171 M nr. 319-321 f.4 and 40, **excerpt**;
   (d) Demandt, Nassau-oranische Korrespondenzen I, 78 nr. 113, **excerpt**. The Opmerkingen say "Tevens een
   bijvoegsel in het origineel in cijferschrift". The Saxon chancery drafted cipher enclosures in clear before
   enciphering, so the minute's 'Zettel' may carry the plaintext of 57's cipher in clear. It has not been seen. It is
   the same kind of lead as 126's KHA minute: it could lower the class to N0-in-substance, and never raise it.

## A2.3 Item 126, second audit

V3's gaps, attacked:

| gap named in the brief | done | result |
|---|---|---|
| WVO record or image for the KHA minute A 11/XIV I/4 nr. 26 | WVO record 126 re-read (1 request); the minute is a Brongegevens row without an Afbeelding link. No other WVO record describes it (WVO keys records by letter, not by witness) | minute unimaged in WVO; still unseen |
| Bundled print in the WVO PDFs (lesson of ROOM 09:16) | 00126 is 5 pages, all read by R9 and listed in `images/inventory.tsv`: f.138r, 138v, 140, 139 (cipher), address leaf | no printed page bundled |
| Groen 1st ser. t.I by date | V3's DBNL full-text check re-run for the 1564 section (DBNL groe009arch01, 1 request) | no letter of 16 Sept 1564; confirmed |
| Kluckhohn, Briefe Friedrich des Frommen I | IA djvu text re-fetched and grepped | nothing (OCR is Fraktur-garbled: a negative on this volume is weak) |
| von Weber, Anna Churfürstin (1865) | V3 had fts only (djvu 500). This audit read the full djvu text of two other scans, `10061398bsb` and `annachurfrstinz00webegoog` | Orange appears for gifts, hunting and a 1564 letter of Anna; no Spanish news, no postscript |
| Böttiger, Vermählung Oraniens mit Anna (Hist. Taschenbuch 1836) | IA advancedsearch by title and by year | no item; unreachable |
| Kruse (Anna von Sachsen literature) | IA search; CrossRef | no text; unreachable |
| Rachfahl II.1 notes quoting Dresden letters | HTRC EF token counts, all 574 pages: pages carrying "8510", "Chiffre", "Zettel", "Zeitung", "Königin", "Frucht", "krank", "Niederkunft", "Hispanien" | the notes (seq 549-564) cite "Dresd. Arch. Locat 8510" often, but no page holds the Spanish queen's miscarriage vocabulary together (Königin pages are the 1561-63 Granvelle/Madrid narrative; Niederkunft pages 370 and 486 are Anna's own confinements). Token bags are not text: a negative, weaker than a read |
| Phrase search, German/French/Dutch variants | Google Books and IA global full text, see A2.6 | see A2.6 |

**126 stays N3.** The KHA minute is still the one lead that could lower it. The second audit found nothing in print.

## A2.4 Items 53 and 57

### 53 (Orange to August, Breda 24 Oct 1561)
- WVO record 53 (fetched 24 Sept 2026): Inhoud "Goede aankomst te Breda. Berichten over Spanje en Frankrijk.
  Toezending van honden en fretten." Opmerkingen "Het origineel met een eigenhandig postscriptum. Een gedeelte van de
  brief is in cijferschrift." Witnesses: Dresden Loc. 9941/3 "Printzen" f.266r-v, original, imaged; KHA Collectie
  Japikse, 20th-century copy. No edition in Brongegevens, no "oplossing".
- The leaf carries no decipherment (both pages seen, A2.2.1). Nobody in Dresden wrote the plaintext on it.
- Plaintext as read by S1 (p1 only, S 163 M 119 of 282): news that the Prince of Spain would marry his father's
  sister and come to govern "these lands", and a rumour that the Duke of Vendôme would recover his kingdom of Navarre
  "mit der gute oder krieg". The events (the 1561 rumours of a match between Don Carlos and his aunt Juana, and
  Antoine de Bourbon's Navarre claim) are common in print. That is a date check, not a print of this letter.
- Not in: Groen t.I (DBNL full text: nothing printed between Lettre XXXVIII of 16 Oct 1561 and Lettre XL of 6 Jan
  1562 except XXXIX to Pius IV) or its Supplément; Gachard t.1-2 (Vendosme/Navarre hits are other letters); Rachfahl I
  and II.2 (full text), II.1 (token bags: Navarra only on pp.175-179, French politics of 1560-61; Vendôme only
  p.484, Enghien); von Weber (Navarra only for August's 1561 letters to the Kings of France and Navarre); Kluckhohn
  (weak, OCR).
- **Class N3.** Not N4: the Japikse copy is unseen, and the second page of the cipher (about 90 signs) is unread,
  so part of the plaintext is not yet known.

### 57 (August to Orange, Torgau 18 Nov 1561)
- Witnesses as in A2.2.3. The imaged KHA original's p3 carries the clear postscript, "Augustus Churfürst", the cipher
  block, and "Augustus Churfürst" again. No decipherment on the leaf (seen).
- Plaintext as read by S1 (C 247 M 53 of 300): the Emperor had recently sent envoys asking August to elect his son
  Maximilian King of the Romans in the Emperor's lifetime; the same would be asked of the other Electors; keep it
  secret. Ferdinand I's approach to the Electors in autumn 1561, which led to the Frankfurt election of Nov 1562, is
  well known in print. The event is a date check, not a print of this letter.
- **Demandt nr. 113, read.** Karl E. Demandt, "Nassau-oranische Korrespondenzen 1553-1570, in Gestalt der von den
  Dillenburger Archivaren Johannes von Arnoldi und Heinrich Westerburg Ende des 18. Jahrhunderts verfaßten Regesten
  (I)", *Hessisches Jahrbuch für Landesgeschichte* 38 (1988), p. 49ff (Google Books `OU4FAQAAIAAJ`, snippet view).
  The regest's text was reconstructed from four overlapping API snippets, which join without a gap: "Torgau 1561
  November 18. Kf. August von Sachsen an den Prinzen Wilhelm von N'Oranien. Bezeigt seine Freude über die am 4.
  Oktober erfolgte glückliche Ankunft des Prinzen und seiner Gemahlin zu Breda und dankt für die ihm zugeschickte und
  mitgeteilte Kunst und neue Zeitung. Der Kg. von Schweden soll angeblich noch hoffen, die Königin zu erlangen, und
  will deshalb noch in diesem Herbst nach England, weshalb er bereits bei dem Kg. von Dänemark und den Hgg. von
  Lüneburg und Lauenburg um sicheren Durchzug und Paß zu Wasser nachgesucht hat. Die greuliche Fehde zwischen den Gff.
  von Öttingen [OCR 'Bettingen'] und Schertlin soll abermals wieder gestillt sein (fol. 4 und 40)." Nr. 114 is Juliane
  of Nassau, Hanau 19 Nov. Nr. 115, "Torgau 1561 November 23", is the second postscript: the King of Spain has stopped
  the Inquisition against the Lutherans and written to the Netherlands government; the Cardinal of Lorraine and the
  Duke of Guise will meet about marriages and the Augsburg Confession (fol. 40v). **Neither regest mentions the Emperor,
  Maximilian or the election.** The Dillenburg excerpts (Wiesbaden fol. 4, 40, 40v) are therefore of the clear text.
  They do not carry the cipher's content. This closes the check-solved sweep's open gap for 57. Caveat: snippet text,
  not a page image; the page number (p. 78) is WVO's.
- Reichstagsakten: reichstagsakten.de lists no volume for the Frankfurt election of 1562 (front page, 1 request).
  Kluckhohn I covers 1562 but prints the Palatine side (OCR weak). Ritter, Deutsche Geschichte im Zeitalter der
  Gegenreformation I: not fetched (cap). Its notes would cite, not print, a letter to Orange.
- Not in Groen t.I or Supplément (as for 53); Gachard t.1-2; Rachfahl I, II.2 full text; II.1 token bags
  ("Maximilian" + "römisch" + 1561 together on p.358 only, which is Anna's household religion).
- **Class N3.** One route could still lower it: the Dresden minute's 'Zettel' (N0-in-substance if it is the clear
  text of the enclosure). Not N4: that minute is unseen.

## A2.5 Principal families (A2's own searches, 24 Sept 2026)

| family | status | what | result |
|---|---|---|---|
| WVO records 53, 57, 126 | searched | 3 record fetches; PDF 00053 fetched (2 pages) | witnesses above; no oplossing; 53 p2 found unread |
| WVO PDFs, bundled print | searched | 00053 (2 pp, seen), 00057 (4 pp, inventory + p3 seen), 00126 (5 pp, inventory) | no printed page bundled in any of the three |
| Groen, Archives 1st ser. t.I (DBNL groe009arch01) | searched | full text: 1561 Oct-Dec and 1564 sections, Vandosm/Navarr/Maximilian/Romains | 53, 57, 126 not printed |
| Groen, Supplément (DBNL groe009arch09) | searched | full text | no 1561 letters at all; nothing for 1564 |
| Gachard, Correspondance t.1, t.2 (IA) | searched | djvu text grep | nothing |
| Rachfahl I (1906) and II.2 (1908) (IA) | searched | djvu text grep | nothing |
| Rachfahl II.1 (1907) (HathiTrust hvd.hnt3bj) | searched (token counts only) | HTRC EF, 574 pages | nothing matching; a bag-of-words negative |
| Kluckhohn, Briefe Friedrichs des Frommen I (IA) | searched | djvu grep | nothing (weak OCR) |
| von Weber, Anna Churfürstin 1865 (IA 10061398bsb, annachurfrstinz00webegoog) | searched | full djvu text | nothing |
| Böttiger 1836; Kruse; Kretzschmar | unreachable | IA title/year search; CrossRef | not seen |
| Demandt, HessJb 38 (1988) nrs. 113-115 | searched (snippet view) | Google Books `OU4FAQAAIAAJ`, 4+3 chained snippets; date queries for 24 Oct 1561 and 16 Sept 1564 | 113 and 115 summarise the clear letter and postscript of 57, no election; no regest found for 53 or 126 |
| Wiesbaden HHStA Abt. 171 M nr. 319-321 | searched through Demandt | fol. 4, 40, 40v as regested | clear text only |
| Dresden minute of 57 (Loc. 9941/3 f.268-269) | unreachable | not imaged by WVO | not seen |
| KHA minute of 126; Japikse copies of 53, 126 | unreachable | not imaged | not seen |
| Reichstagsakten (1562 election) | searched | reichstagsakten.de volume list | no 1562 volume online |
| Ritter, Deutsche Geschichte I | not searched | cap | gap |
| Google Books | searched | 18 phrase and keyword queries (A2.6), then 31 queries chaining Demandt's snippets | Demandt found (above); other hits are unrelated letters |
| Internet Archive global full text (be-api) | searched | 12 phrases (A2.6) + 2 in-item snippet checks | no hit on these letters |
| Solver repos, Cryptiana, DECODE | searched by V3 and the check-solved sweep (24 Sept 2026) for this correspondence | not repeated | no hit |
| CrossRef | searched | 3 queries | reference-work and unrelated entries only |
| OpenAlex | unreachable | HTTP 429 (budget exhausted for the shared IP; 4 requests sent before stopping, one more than the rule allows, logged) | not searched |
| Semantic Scholar | unreachable | HTTP 429, 1 request | not searched |
| HAL | searched | 1 query | nothing relevant |
| Persée | searched | 1 query ("Auguste de Saxe" Orange 1561) | one article on the Secrétairerie d'État allemande (RBPH 1998), 1566 letters, not these |
| JSTOR | queued | 2 rows in JSTOR-QUEUE.tsv | pending, does not block |

## A2.6 Phrase search

Google Books (API, 24 Sept 2026, `&country=US`, key) and IA global full text (be-api). Raw results in this
session's scratch; summary:

| item | phrase | Google Books | IA full text |
|---|---|---|---|
| 53 | "hertzog von Vandosmen" | 0 | 0 |
| 53 | "konigreich Navarra mit der gute" | 0 | 0 |
| 53 | "seines hern vatters schwester" / "vatters schwester ehlich vermahlet" | 0 | 0 |
| 53 | "dem printzen zu hispanien" | 300, top: RTA Augsburg 1555; Groen t.I (letter of Philipp of Hesse, "der Kay. Matt. eltestenn dochter uund dem Printzen zu Hispanien") | 3: Groen (same), MIÖG 37 (1916, Don Carlos's fall 1562) |
| 53 | "Königreich Navarra" "Güte oder Krieg"; two keyword queries (German, French) | 0 | 0 |
| 57 | "König Maximilianum noch bei" | 9, all 19th-century novels and lexica (Maximilian II of Bavaria) | 0 |
| 57 | "zu einem römischen Könige zu erwelen" | 6, all Ranke, Deutsche Geschichte im Zeitalter der Reformation (Ferdinand's election, 1530s) | 7, same Ranke |
| 57 | "durch seine stadtliche gesanndten" | 0 | 0 |
| 57 | Kurfürst August Oranien Torgau 18 November 1561 | 2: **Demandt, HessJb 1988** (regest nr. 113, A2.4) | n/a |
| 57 | "bei den andern Churfürsten gleicher gestalt"; French keyword query | 0 | 0 |
| 126 | "die adern zwei mahl schlagen"; "irer frucht erlediget" | 0 | 0 |
| 126 | German, French, Dutch keyword queries on the queen's miscarriage, Orange, Saxony, 1564 | 0 | n/a |

No hit prints any of the three cipher passages or a paraphrase of them.

## A2.7 Did we first-decipher?
Not established for any of the three. No prior decipherment was located. For 57 and 126 the sender's own chancery
minute, recorded with a 'Zettel' or a 'Zeitung', may hold the plaintext in clear. For 53 the second cipher page is
unread. Rule 10 allows no priority wording at N3.

## A2.8 Sentences
- **126 safe:** V3's safe sentence stands.
- **126 unsafe:** "first decipherment of Orange's 1564 cipher" (N3; the KHA minute is unseen).
- **53 safe:** "Part of the cipher postscript of Orange's letter to Elector August, Breda 24 Oct 1561 (Dresden Loc.
  9941/3 f.266r; WVO 53), reads with a cryptanalytically recovered key (S 163, M 119 of 282 signs; matched control
  280/282) as news that the Prince of Spain would marry his father's sister and govern the Netherlands, and that the
  Duke of Vendôme would recover Navarre. Three more cipher lines on f.266v are not yet read. No prior decipherment or
  printed plaintext was located in the sources listed in AUDIT.md (24 Sept 2026)."
- **53 unsafe:** "Orange's 1561 cipher broken for the first time" (N3, cryptanalytic, and half a page unread).
- **57 safe:** "The cipher enclosure of Elector August's letter to Orange, Torgau 18 Nov 1561 (KHA A 11/XIV B/41-6;
  WVO 57), reads with the key of Orange's 1562 cipher (C 247, M 53 of 300 signs) as secret news that the Emperor had
  asked August to elect Maximilian King of the Romans. No prior decipherment or printed plaintext was located in the
  sources listed in AUDIT.md (24 Sept 2026); Demandt's regest of the letter (HessJb 38, nr. 113) summarises only
  the clear text. August's minute in Dresden (with a 'Zettel') has not been seen."
- **57 unsafe:** "a previously unknown Saxon report of the 1561 election approach" (N3; the minute and the regest are
  unseen, and the approach itself is well known).

## A2.9 Confidence
126 moderate (unchanged). 53 moderate: no edition prints Orange-August letters of Oct-Nov 1561, and the only other
witness is a 20th-century copy. 57 moderate-low: the excerpt witnesses and Demandt's regests carry only the clear text, but August's minute with a
'Zettel' is unseen and is the likeliest place for the plaintext in clear.

## A2.10 Postmortem and corrections
- Failure 1 (capture, not over-claim): 53 was captured as one page. The PDF has two, and the cipher runs on. Every
  later pass inherited the gap. Lesson: count the PDF's pages before cropping, and record the count in the manifest.
  Corrected in NOTES.md (S1 section) and `images/inventory.tsv`.
- Failure 2 (verifier): V3's search log named IA `wilhelmvonorani00rachgoog` as Rachfahl II.1. It is II.2. The
  volume that matters for 1561-64 was not searched. Corrected in the V3 table above by a bracketed note.
- Over-claims: none. S1 and R21 used "cryptanalytic result" and "read with a sibling key", no priority wording.
  status.json's line said "WVO 53 and 57 not read"; that sentence is stale, not an over-claim, and is updated.
- Suggestions (not done): (1) a solver pass on 53 f.266v with key_53; (2) KHA inquiry for A 11/XIV I/4 nr. 26 (126's
  minute); (3) Dresden HStA inquiry for Loc. 9941/3 f.268-269 (57's minute and Zettel); (4) a page image of Demandt, HessJb
  38 (1988) nrs. 113-115, to replace the snippet reading.

Requests this session: resources.huygens.knaw.nl 4 (3 records, PDF 00053); archive.org ~27 (metadata, djvu text, advancedsearch); be-api 14; www.googleapis.com 49; dbnl.org 2; data.htrc.illinois.edu 1; catalog.hathitrust.org 2; babel.hathitrust.org 1 (Cloudflare 403, stopped); openlibrary 1; api.openalex.org 4 (429); api.crossref.org 3; semanticscholar 1 (429); HAL 1; persee 1; reichstagsakten.de 1; web search 4. No subagents.

---

## N4 decision (D1): WVO 126

N4-decision verifier D1 for LANE V2 (Opus), 24 Sept 2026, 09:48-10:05 UTC (`date -u` read). This session did none of
the solving, did no part of V3's or A2's audits, and did no decoding. Question: after two audits at N3 (V3, A2), is
N4 warranted for 126, or which principal family is still missing? 53 and 57 (one audit each) are out of scope.

**Answer: N4 (no prior decipherment located) for 126.** The two gaps that blocked it are either closed below or are
unpublished witnesses, which N4 does not exclude (rule 10). The KHA minute "met een 'Zeitung'" may still hold the
postscript's text in clear; that would make the item N0 in substance, unprinted. The safe sentence says so.

### D1.1 Principal families for 126

| family | covered by | with what | result |
|---|---|---|---|
| Groen, Archives 1st ser. t. I, Supplément, Table | V3 + A2 | DBNL full text, by date and phrase roots | no letter of 16 Sept 1564; Spanish news absent |
| Japikse, Correspondentie van Willem den Eerste (printed) | range | stops 1561 | not applicable to 1564 |
| Gachard, Correspondance de Guillaume le Taciturne t. 1-2 | V3 + A2 | IA full text | none |
| Rachfahl I (1906), II.2 (1908) | V3 + A2 | IA full text | none |
| Rachfahl II.1 (1907), the volume for 1559-64 | A2 + **D1** | HTRC Extracted Features per-page tokens, all 574 pages, twice with different vocabularies (D1 added Fehlgeburt, Ader-, purgier-, Aderlass, Wochenbett, schwanger-, Krankheit, krank). Not on IA (D1: `bub_gb_hq9AAAAAYAAJ` is vol. I again) and not full view on Google Books (D1, 2 API queries) | the only page with "Königin" plus illness vocabulary is seq 80 (Margaret of Parma's gout, Catherine de Medici; no Spain 1564). Pages with 1564 + September + Saxony (seq 555-565, notes) carry no Königin, Zeitung, Chiffre or Zettel. A token-bag negative, not a read; accepted because a paraphrase of the postscript cannot avoid "Königin" with one of those terms |
| Kluckhohn, Briefe Friedrich des Frommen I | V3 + A2 | IA djvu grep (weak OCR) | nothing; **not principal** (Palatine holdings) |
| von Weber, Anna Churfürstin zu Sachsen (1865) | V3 (fts) + A2 (two full texts) | IA | none |
| Raumer, Briefe aus Paris | V3 | IA | none |
| Anna of Saxony studies: Böttiger (Hist. Taschenbuch 1836), Kruse, Kretzschmar | unreachable (V3, A2; D1: IA title+date search for Historisches Taschenbuch 1835-37, no item) | | **not principal for 126**: they treat the 1561 marriage and Anna's later conduct, not Orange's Spanish news of 1564 |
| Demandt, Nassau-oranische Korrespondenzen (HessJb 38) | A2 | Google Books snippets; date query 16 Sept 1564 | no regest for 126 |
| Holding archive of the original: Dresden HStA | V3 | catalogued by Locat file, not by letter | no item-level record expected |
| Holding archive of the minute: **KHA inventory** | **D1 (closed here)** | koninklijkeverzamelingen.nl, 1 browser load of the A11 inventory at item `a11-xivi-04-26` | "A11-XIVi-04-26. Aan August van Saksen (Sachsen), 16 september 1564. Bestanddeel, 1 stuk", no scan, "Bereik en Inhoud: Voor het digitale exemplaar en een nadere beschrijving zie ... wvo/app/brief?nr=126". No decipherment or edition noted. (WVO's "A 11/XIV I/4 nr. 26" is this item) |
| Huygens ING / WVO record, PDF, cipher-remarks sweep | V3 + A2 | record; 5 pages; sweep | no oplossing, no bundled print |
| KHA minute (with 'Zeitung'); Collectie Japikse copy | unreachable, unimaged | | **unpublished witnesses**: N4 does not exclude them. The minute is the one route that could lower the class |
| IA / Google Books phrase search | V3 + A2 | 9 + 18 queries, German, French, Dutch | none |
| HathiTrust full text | unreachable (Cloudflare, A2) | | a route, not an edition; Rachfahl II.1 reached through HTRC instead |
| Solver repos, Cryptiana, DECODE | V3 | fresh clones, snapshots | none |
| Open scholarship | V3 + A2 | CrossRef, HAL, Persée covered; OpenAlex, Semantic Scholar 429 (do not block N4: Danzay precedent) | nothing relevant |
| JSTOR | queued | JSTOR-QUEUE.tsv lines 48, 49 | does not block |
| Ritter, Deutsche Geschichte I | not searched | | not principal (a general history; would cite, not print) |

### D1.2 Spot-checks

1. **A2's Rachfahl II.1 negative**: re-run from a fresh HTRC EF fetch with a wider vocabulary (above). Confirmed.
2. **A2's "not on IA" for Rachfahl II.1**: IA creator search lists `wilhelmvonorani01rachgoog`, `...00rachgoog` and
   `bub_gb_hq9AAAAAYAAJ`; the last was fetched and is "ERSTER BAND". Confirmed.
3. **V3's "no item-level record" for the minute**: partly wrong. The KHA inventory has an item record (above); it
   adds nothing beyond WVO. Corrected here, not a change of class.

### D1.3 Decision and sentences

**126: N4 (no prior decipherment located).** Confidence moderate: the editions are covered, Rachfahl II.1 only by
tokens; scholarship indexes partly unreachable; the KHA minute unseen.

- **Safe:** "The cipher postscript of Orange's letter to Elector August of 16 Sept 1564 (Dresden Locat 8510/5 f.139;
  WVO 126) reads, with a key aligned from his 1563 letter WVO 98 and its contemporary decipherment, as news from Spain
  that the Queen had been bled and purged twice and had lost the child (C 214, M 26 of 240 signs). No prior
  decipherment was located in the principal editions (Groen, Gachard, Rachfahl, von Weber), the KHA and WVO records,
  or a full-text phrase search (AUDIT.md, 24 Sept 2026). Orange's minute in the KHA (A11-XIVi-04-26), recorded with
  a 'Zeitung', is unimaged and may carry the text in clear."
- **Unsafe:** "first decipherment" without "no prior decipherment located"; "a previously unknown report"; any
  sentence that drops the unseen minute.

Outreach: gate 2 open on JSTOR lines 48-49 (ASKS row 37). CONTRIBUTIONS.md row added, held at gate 2.

Requests (D1, this item): data.htrc.illinois.edu 1; archive.org 4 (advancedsearch 2, metadata 1, djvu 1);
www.googleapis.com 2; www.koninklijkeverzamelingen.nl 1 browser load; WebSearch 1.

---

# Second audit 53/57 (A3) (Second Auditor A3 for LANE V2, 24 Sept 2026, 10:17-10:35 UTC)

This session solved neither letter and did not decode or re-read any cipher. It read A2's log first and did not repeat
A2's searches. Claims under audit: A2's N3 for 53 and for 57; the 53 reading as extended by LANE R2 F1 to f.266v.

## A3.1 Verdict

| item | class | prior plaintext | prior decipherment | evidence quality of our reading | confidence |
|---|---|---|---|---|---|
| WVO 53, cipher postscript f.266r-v (Dresden Loc. 9941/3), Orange to August, Breda 24 Oct 1561 | **N3** (A2's class stands) | none located | none located; the leaf carries none | **S only**: 364 tokens, S 238, M 126 (35% M), H 0, C 0; key_53 recovered cryptanalytically, matched control 99.3%. The class covers the text as read, not a letter-perfect text | moderate |
| WVO 57, cipher enclosure on p3 (KHA A 11/XIV B/41-6), August to Orange, Torgau 18 Nov 1561 | **N3** (A2's class stands) | none located | none located; the leaf carries none | C 247, M 53 of 300 (key of WVO 74, a sibling letter's decipherment) | moderate |

Neither item is raised to N4 by this audit: a separate D-verifier decides N4. What the principal-families table still
lacks is in A3.5. Neither item is lowered: no source prints either cipher passage or a paraphrase of it.

## A3.2 The finding that matters: Japikse I stops before both letters

The 20th-century "Collectie Japikse" copy of 53 in the KHA looked like a route to a printed decipherment, since
Japikse's *Correspondentie van Willem den Eerste* I (1934) prints the Prince's cipher passages deciphered in spaced type
(V4, `ciphers/gunther-van-schwarzburg-1561/AUDIT.md`, no.316, solved by H. Koot). Checked in the edition itself (Huygens
retroboeken viewer `willem_den_eerste`, its own full-text search and its page OCR, 24 Sept 2026):

- **Chronologische lijst, pp.386-389:** the last dated letters are "1561 Sept. ... 19 Aan [August], 286; 29 [Aan
  August], 287; 9 Aan de Landvoogdes Margaretha, 288" with a note "7 Oct., de Landvoogdes aan de Prinses van Oranje".
  p.390 begins the list of archives. **No letter of 24 Oct or 18 Nov 1561 is in the volume.** No later volume was
  published, so the Japikse copies of 53 (and of 126) are preparatory work for an unpublished continuation.
- Edition-wide search: "Navarre" hits pp.127 and 325 (other letters) and the index only; "Navarra" 0; "Maximilian" 0;
  "Torgau" last in the text at p.285 (10 Sept 1561).
- D1's line "Japikse ... stops 1561; not applicable to 1564" is right for 126 and now holds for 53 and 57 as well:
  the volume stops at the end of September 1561.

## A3.3 Families attacked (A3's own searches, 24 Sept 2026)

| family | status | what | result |
|---|---|---|---|
| Japikse, Correspondentie Willem den Eerste I (1934) | searched | retroboeken search x4 (Navarra, Maximilian, navarre, Torgau); pages.json; index pp.386-390 page text (resources.huygens.knaw.nl, 8 requests) | ends Sept 1561; 53 and 57 not in it |
| Goetz, *Maximilians II. Wahl zum römischen Könige 1562* (1891) (IA `WalterDieWahlMaximiliansII`, full djvu text) | searched | grep Oranien, Navarra, Breda, Oct-Nov 1561, Sachsen, Dresd | the standard monograph on the 1561-62 approach to the Electors (from Moser, Sickel, Kluckhohn, Bucholtz, Venetian reports). Orange appears only for the Leipzig wedding and a Paris rumour of Oct 1561 (Languet to Mordeisen, *Arcana* 2, 154). August's letter to Orange is not cited or quoted |
| Ritter, *Deutsche Geschichte im Zeitalter der Gegenreformation* I (IA `deutschegeschich01rittuoft`) | searched (weak) | grep Oranien, Vendôme, Navarra | Oranien in the 1560s narrative only; nothing on these letters. Fraktur OCR is garbled: a weak negative |
| Weiss, *Papiers d'État du cardinal de Granvelle* VI (1560-62) and VII (IA `papiersdtatduca00grangoog`, `papiersdtatduc07gran`) | searched | grep Saxe, roi des Romains, Vendosme, prince d'Espagne + tante, Saxe + chiffre | VI carries Chantonnay's and Granvelle's rumours that the Protestants or the Duke of Saxony might aim at the Roman crown, and the Orange-Saxony marriage. No Orange-August letter, no cipher from them |
| Kruse, "Wilhelm von Oranien und Anna von Sachsen", *Nassauische Annalen* 54 (1934) (Google Books `TCsjAQAAIAAJ`, search inside, no text view) | searched (weak) | Vendome, Vendosme, "römischen König", Juana, Chiffre, Ziffern, Geheimschrift, Zettel: 0 pages each. Navarra 2 pages (one is the index, p.180), Maximilian 5, "Karl von Spanien" 3 | no page carries the vocabulary of either cipher passage together. Snippets were not shown; page counts only |
| *Nassauische Annalen* 2007 (article on Breda 1561 and the Orange-Wettin marriage) (Google Books `bBFoAAAAMAAJ`, search inside) | searched (weak) | Chiffre 0; Navarra 1 page; Oktober 1561 2 pages | page counts only; no text view |
| Reichstagsakten, Reichsversammlungen 1556-1662 | searched | Google Books API volume list | published volumes returned are Regensburg 1556/57, Frankfurt 1558 / Augsburg 1559 and later diets. No volume for the 1562 Frankfurt election was found (confirms A2) |
| Gachard, *Don Carlos et Philippe II* (IA, 5 scans) | searched, as a control | IA full text, "prince d'Espagne" "sa tante" 1561 mariage | the Don Carlos-Juana marriage rumour **is** in print and the phrase search finds it. It is the event, reported by others. Not Orange's letter |
| Phrase search on the new f.266v text (53) and on 57 | searched | Google Books API 18 queries + 5 to surface Kruse; IA be-api 9 queries | see A3.4 |
| books.google.com page text (Goetz pp.64, 86, 114) | unreachable | "Sorry ... automated queries" on 3 requests, after 16 search-inside requests at 3.5 s. Stopped, logged in ROOM 10:25 | Goetz read on IA instead |
| OpenAlex, Semantic Scholar | unreachable | HTTP 429, 1 request each, stopped (as for A2) | not searched |
| Kluckhohn, Briefe Friedrichs des Frommen I | not repeated | A2 grepped it (weak OCR). Goetz cites Kluckhohn I 246 ff. and 303 n.1 for the Palatine side only | gap unchanged (weak) |
| Kervyn de Lettenhove, *Relations politiques* II | not reached | IA title search: 0 items | gap |
| Wartenberg (Politische Korrespondenz Moritz, to 1553); Bezold (Johann Casimir, from 1576) | not applicable | out of range | logged |
| Kretzschmar | unreachable | as A2 | gap |
| Dresden minute of 57 (Loc. 9941/3 f.268-269, "met een 'Zettel'") | unreachable | not imaged by WVO | unseen. It could lower 57 (N0-in-substance), never raise it |

## A3.4 Phrase search (A3)

| item | phrase | Google Books | IA full text |
|---|---|---|---|
| 53 f.266v | "König zu Frankreich noch so jung" / "konig zu franckreich noch so jung" | 0 / 0 | 0 / 0 |
| 53 f.266v | "dieweil der König zu Frankreich noch" | n/a | 0 |
| 53 f.266v | "keinen furgang gewinnen" / "werde keinen furgang gewinnen" | n/a / 0 | 9, all other texts (Ludwig of Bavaria, city chronicles) |
| 53 f.266v | "keinen Fortgang gewinnen" Navarra | 300, all the Ersch-Gruber *Encyclopädie* on a medieval Navarre siege | n/a |
| 53 | "seines vaters schwester" "printzen zu hispanien"; "diese Lande zu regieren" Hispanien 1561; "Prinz von Hispanien" "seines Herrn Vaters Schwester" | 0 each | n/a |
| 53 | "hertzog von Vendosme" Navarra 1561 Oranien | 1, an 1855 atlas (genealogy) | n/a |
| 53 | "24 Octobris" 1561 Breda Oranien Kurfürst | 0 | n/a |
| 53 control | "prince d'Espagne" "sa tante" 1561 mariage | n/a | Gachard, *Don Carlos et Philippe II* (the rumour, from Spanish and French dispatches) |
| 57 | "bei seinem Leben zu einem römischen König" | 0 | n/a |
| 57 | "Maximilianum" "römischen König" 1561 Torgau; "seinen Sohn König Maximilian" Kurfürsten 1561 | n/a | unrelated hits |
| 57 | "zu einem Römischen König" "bei seinem Leben" Maximilian 1561 | n/a | 7, unrelated (Strasbourg chronicle; an Oct 1561 letter to Maximilian on another matter) |
| 57 | keyword queries (Kaiser Ferdinand, Gesandte, Kurfürst August, Wahl Maximilian, 1561; Zasius) | Goetz 1891; Holtzmann 1903; Laubach 1977 (*Protestantisches Kaisertum*); Westphal 1975 (*Freistellung*) | n/a |

The four keyword hits for 57 are histories of the election approach. The event of 57 (the Emperor's envoys to the
Electors in late 1561) is printed there. That is the event, not the letter. No hit prints or paraphrases August's
enclosure to Orange or Orange's f.266v sentence.

## A3.5 N4: what the principal-families table still lacks (for the D-verifier)

| family | state after A2 + A3 | what would close it |
|---|---|---|
| Groen t.I and Supplément; Gachard *Correspondance de Guillaume le Taciturne* t.1-2 [D2 correction: A3 wrote 'de Philippe II']; Weiss VI-VII; Japikse I; Rachfahl I and II.2 (text), II.1 (HTRC tokens); von Weber; Goetz 1891 | covered | nothing |
| Demandt, HessJb 38 (1988) nrs. 113, 115 | snippet text only (A2) | a page image, or accept the chained snippets |
| Rachfahl II.1 (1907) | HTRC token bags only, not read as text | a text or page read of the 1561 chapter and its notes (HathiTrust is Cloudflare-blocked here) |
| Kluckhohn I; Ritter I | Fraktur OCR, weak | a clean text or page read of Kluckhohn I for Nov 1561 |
| Kruse 1934; *Nassauische Annalen* 2007 | page counts from search inside only | a text read of the pages with Navarra / Maximilian |
| Kervyn, *Relations politiques* II | not reached | IA or HathiTrust grep |
| OpenAlex, Semantic Scholar | 429 twice (A2, A3) | one run from another host or a later session |
| JSTOR | rows 55-56 queued (A2), rows added by A3 | owner's runner; does not block |
| Dresden minute of 57 with 'Zettel'; KHA Japikse copy of 53 | unpublished, unimaged | N4 does not exclude unpublished work; they can only lower the class |

For **57**, the D-verifier needs Kluckhohn I read clean (Palatine letters of Nov 1561, where August may pass the same
news to Friedrich III in similar words) and the open indexes. For **53**, it needs the open indexes and Rachfahl II.1 read
as text. **53 carries a further caution:** 35% of its tokens are M, so a phrase search on its text may miss a print
that words the passage differently. The D-verifier should search on the gist (Don Carlos + aunt + "these lands";
Vendôme + Navarre "by good or by war"; the King of France too young) as well as on phrases.

## A3.6 Did we first-decipher?
Not established. No prior decipherment of either item was located. For 57, August's minute with its 'Zettel' may hold
the plaintext in clear. Rule 10 allows no priority wording at N3.

## A3.7 Sentences
- **53 safe:** "The cipher postscript of Orange's letter to Elector August, Breda 24 Oct 1561 (Dresden Loc. 9941/3
  f.266r-v; WVO 53), reads with a cryptanalytically recovered key (S 238, M 126 of 364 signs; matched control 99.3%)
  as news that the Prince of Spain would marry his father's sister and come to govern the Netherlands, that the Duke
  of Vendôme would recover Navarre by agreement or by war, and Orange's view that, the King of France being so young,
  it would come to nothing. No prior decipherment or printed plaintext was located in the sources listed in AUDIT.md
  (24 Sept 2026); Japikse's edition ends in September 1561."
- **53 unsafe:** "Orange's 1561 cipher read for the first time" (N3, cryptanalytic, 35% M).
- **57 safe:** A2's 57 sentence stands, with "Japikse's edition ends in September 1561" added to the sources.
- **57 unsafe:** "an unpublished Saxon report of the 1561 election approach" (N3; the minute and its 'Zettel' are
  unseen, and the approach itself is printed in Goetz 1891).

## A3.8 Postmortem and corrections
- **Failure (verifier coverage, not an over-claim):** A2 and D1 logged Japikse only as "stops 1561", without the month.
  For 1561 letters the month decides. It ends in September, so the result stands, but the log did not show why. Lesson:
  log an edition's range to the month when the item falls in its last year.
- **Stale sentences corrected in place:** status.json's line "three more cipher lines on f.266v are unread" and its
  grade "53 (p1 only): S 163, M 119 of 282" now read both pages (S 238, M 126 of 364). The SO prompt for 53/57 now
  carries the f.266v text and the Japikse range. NOTES.md gets an A3 section.
- **Over-claims:** none found in the folder for 53 or 57. F1's report used "read with key_53", no priority wording.
- **Suggestions (not done):** (1) Kluckhohn I clean read for Nov 1561; (2) OpenAlex and Semantic Scholar from a session
  whose IP is not rate-limited; (3) the Dresden inquiry for Loc. 9941/3 f.268-269 (A2's suggestion 3) remains the one
  route that could lower 57.

Requests this session: resources.huygens.knaw.nl 8; www.googleapis.com 23; books.google.com 16 search-inside + 3 page
text (blocked, stopped); www.google.com 1; archive.org ~16 (advancedsearch, metadata, djvu text); be-api.us.archive.org 9;
api.openalex.org 1 (429); api.semanticscholar.org 1 (429). No subagents.

---

# N4 decision (D2): WVO 53 and 57

N4-decision verifier D2 for LANE V2 (Opus), 24 Sept 2026, 10:45-11:00 UTC (`date -u` read). This session did none of
the solving, took no part in the V3, A2, A3 or D1 audits, and did no decoding. The question: after two audits at N3 (A2 and A3),
should 53 and 57 go to N4, or which principal family is still missing? The gaps are the ones A3 named in A3.5.

**Answer: N4 (no prior decipherment located) for both.** Four of A3's five gaps are closed below. The fifth, the open
scholarship indexes, returned 429 for the third time; under the Danzay and D1 precedent that does not block N4. For 53, the
class covers **this ciphertext's decipherment, as read cryptanalytically** (S 238, M 126 of 364; no H, no C). It does
not certify a letter-perfect plaintext. Because 35% of the tokens are M, the print search for 53 was run on the gist as
well as on phrases (D2.2).

## D2.1 Gaps closed (D2's own searches, 24 Sept 2026)

| gap (A3.5) | what D2 did | result |
|---|---|---|
| Kluckhohn, *Briefe Friedrich des Frommen* I (1868), read clean for Oct-Dec 1561 | IA `briefefriedrichd00frie` (Columbia microfilm, all volumes, 6.1 MB djvu text; `bub_gb_3N1SAAAAcAAJ` is vol. II.2 only). One fetch. Isolated the Oct 1561-Jan 1562 run (nrs. 140-153), then read the letter headers and the hits for Navarra, Oranien, August/Sachsen, Kaiser, römisch, Maximilian and Hispanien in context. The Fraktur OCR is noisy but readable at sentence level | Nrs. 140-147 are Friedrich III's letters to Pfalzgraf Philipp, Johann Ludwig, Johann Wilhelm and Johann Friedrich of Saxony (Ernestine), Erbach's letter, Olevian and Boquin from Poissy, and Rambouillet's embassy. Nr. 148 is the imperial envoys' audience with the Palatine elector (Helfenstein and Zasius, 30-31 Dec 1561; Munich archive): the same approach as 57, from the Palatine side, with no word of August or Orange. Nr. 145's note tells of Christoph of Württemberg failing to rouse August over the "römische Practica" (Jan 1562; Sattler). **No letter from August, and nothing from or to Orange, in Oct-Dec 1561.** "Oranien" occurs once in vols I-II, in 1567+. The Navarra hits are the Poissy colloquy |
| Rachfahl, *Wilhelm von Oranien* II.1 (1907), as text | Not on IA (advancedsearch: `bub_gb_hq9AAAAAYAAJ` and `...01rachgoog` are vol. I, `...00rachgoog` is II.2). Google Books `GDzTAAAAMAAJ` (1907) is NO_PAGES, and a Wayback CDX query for the HathiTrust id timed out (504), so **text is unreachable**. Instead, one fresh HTRC Extracted Features fetch (`hvd.hnt3bj`, 574 pages), scanned **by co-occurrence of the gist** rather than single tokens | Carlos + (Tante/Schwester/Juana/Johanna): 10 pages. Only one (seq 104) also has August, and it describes the marriage negotiations (Moritz, Mitgift, Günther von Schwarzburg), not 1561 news. Navarra: 3 pages (seq 189, 193, 195), all the French politics of 1560-61 (Condé, Guise, Katharina, Staatsrat), with no August, Oranien-brief or Breda. Maximilian + römisch/Kaiser: 3 pages (250, 275, 372), none with Wahl news from August. Cipher words (Chiffre, chiffriert, Ziffer, Zettel, Nachschrift): 14 pages. The two with "chiffrierten/chiffrierter Zettel" plus August (seq 223, and the note on seq 549, which cites "Dresd. Arch. Locat") belong to the 1562 narrative: Guise, Elisabeth, Quadra, England and Netherlands neutrality, with dates 1562-63. That matches a 1562 cipher note (cf. WVO 74), not 53 or 57. **A token-bag negative, stronger than A2's because it tests the gist together. Still not a read** |
| Kervyn de Lettenhove, *Relations politiques* II (1883, 26 Aug 1559-12 Apr 1562) | IA `relationspolitiq02nethuoft`, full djvu text, one fetch; grep Saxe, Orange, Vendôme, roi des Romains, tante, Carlos, 1561 | Saxe: Orange's marriage "avec la fille de Maurice de Saxe" (introduction, from Aquila's letters of Oct-Dec 1561) and German levies in 1560. Vendôme: Anglo-French dealings. **No Orange-August letter, no Don Carlos-Juana marriage, no election.** Not a principal family for this correspondence (it prints Anglo-Netherlands diplomacy), and now covered |
| OpenAlex, Semantic Scholar | 1 request each at 10:52 UTC | **429 both** (OpenAlex: shared-IP daily budget exhausted, resets at midnight UTC). Unreachable for the third time (A2, A3, D2). Precedent (Danzay, D1): does not block N4. CrossRef, HAL and Persée were covered by A2 |
| Gist search for 53 (A3's advice), plus 57 | Google Books **API only** (books.google.com page text not touched): 12 gist queries in German, French and Dutch, 6 looser keyword queries, 2 snippet probes and 3 Böttiger probes, 3.5 s apart (list below) | No hit prints or paraphrases either cipher passage. See D2.2 |

## D2.2 Gist search (Google Books API, 24 Sept 2026, 10:50-10:56 UTC)

| query (abridged) | total | relevant |
|---|---|---|
| Oranien Kurfürst August 1561 Prinz Spanien Tante heiraten Niederlande regieren | 0 | - |
| Oranien 1561 "Herzog von Vendôme" Navarra Kurfürst August Brief | 1 | Kutscheit atlas 1855 (genealogy): no |
| "Prinzen von Spanien" Tante Heirat 1561 Oranien Sachsen | 0 | - |
| Wilhelm von Oranien August von Sachsen Oktober 1561 Breda Brief Chiffre | 0 | - |
| Oranien Breda 1561 Navarra "mit Güte oder" Krieg | 0 | - |
| Oranien Kurfürst August 1561 "König von Frankreich" jung Navarra | 0 | - |
| Guillaume d'Orange électeur de Saxe 1561 lettre chiffre Navarre prince d'Espagne tante | 300 | Gachard *Correspondance* volumes and other editions of Orange's letters, all covered (A2): no new title |
| Kurfürst August Oranien Nov 1561 Kaiser Maximilian römischer König Wahl geheim | 2 | Maximilian I biographies: no |
| August von Sachsen an Oranien 1561 Maximilian "römischen König" Gesandte Kaiser | 3 | Buchholtz 1767 and *Historisches Portefeuille* 1787 (Ferdinand courts the Electors, from the Brandenburg side): the event, not the letter |
| Willem van Oranje August van Saksen 1561 cijfer brief | 0 | - |
| "Anna von Sachsen" Oranien 1561 Briefe Kurfürst August Chiffre | 0 | - |
| Don Carlos Juana 1561 Oranien Sachsen Brief | 0 | - |
| Oranien "Kurfürst August" 1561 Navarra | 6 | Venetianische Depeschen 1895 index; Barthold 1848; Hessen Politisches Archiv (1954 inventory, Jan-July 1561); Reichstag Augsburg 1566 (2002): none carries these letters |
| Oranien "Kurfürst August" "Don Carlos" 1561 | 1 | *Historische Zeitschrift* 1882 (Maria Stuart / Don Carlos): no |
| "prince d'Orange" "électeur de Saxe" 1561 Navarre Vendôme | 5 | Larousse (biography of Anna): no |
| "prince d'Orange" électeur Saxe 1561 "roi des Romains" Maximilien lettre | 1 | Namèche, *Cours d'histoire nationale* (1884, Google `gyVwt_fxkc8C`, full view): the snippet is the Leipzig wedding of Aug 1561 and Philip II's wish for the Roman crown. A general history. Page text is not reachable here (books.google.com blocked since 10:25); two snippet probes returned 0. Logged as a weak lead, not a print |
| Oranien 1561 Chiffre Kurfürst Sachsen Brief entziffert | 1 | 1552 pamphlet: no |
| "Kurfürst August" Oranien 1561 Maximilian Wahl | 300 | Goetz 1891 (read by A3), Nuntiaturberichte (Hosius and Delfino 1560-61), Camerarius letters (2003), Meusser 2004, Reichstag 1566: the election approach and the wedding. None cites August's enclosure to Orange |
| Böttiger, *Historisches Taschenbuch* 1836 (3 probes) | 0 / 0 / 1 | unreachable again. The one hit (a Dresden art-history volume, 2025) cites Karl von Weber, "Des Kurf. August z. S. Verhandlungen mit König Maximilian über dessen Glaubensbekenntnis", *Archiv f. sächs. Gesch.* 3 (1865) 309 ff.: a follow-up lead for 57, not a principal family |

## D2.3 Principal families for 53 and 57 (complete table)

| family | covered by | result |
|---|---|---|
| Groen, Archives 1st ser. t. I, Supplément | A2 (DBNL full text) | neither letter printed |
| Japikse, Correspondentie van Willem den Eerste I (1934) | A3 (Huygens viewer, index pp.386-390) | ends Sept 1561: out of range for both |
| Gachard, Correspondance de Guillaume le Taciturne t. 1-2 | V3, A2 (IA) | none |
| Rachfahl I (1906), II.2 (1908) | V3, A2 (IA text) | none |
| Rachfahl II.1 (1907) | A2, D1 (HTRC tokens), **D2 (gist co-occurrence)** | none. Text unreachable (not on IA, Google NO_PAGES, HathiTrust Cloudflare) |
| von Weber, Anna Churfürstin (1865) | A2 (two full texts) | none |
| Kluckhohn, Briefe Friedrich des Frommen I | A2 (grep), **D2 (Oct-Dec 1561 read at sentence level)** | none. Nr. 148 is the Palatine side of 57's event |
| Goetz, Maximilians II. Wahl (1891) | A3 (IA text) | the event, not the letter |
| Weiss, Papiers d'État de Granvelle VI-VII | A3 (IA) | rumours only |
| Kervyn, Relations politiques II | **D2 (IA text)** | none |
| Demandt, Nassau-oranische Korrespondenzen (HessJb 38, 1988) | A2 (chained snippets) | 57: nrs. 113 and 115 regest the clear text only. 53: no regest found by date query. Snippet text accepted, as A2 did |
| Reichstagsakten | A2, A3 | no volume for the 1562 election |
| Kruse 1934; *Nassauische Annalen* 2007 | A3 (search-inside page counts) | weak: 0 pages for Vendôme, Juana, Chiffre, "römischen König" |
| Böttiger 1836; Kretzschmar | unreachable (V3, A2, D1, D2) | not principal: studies of the marriage, superseded on the Dresden files by Rachfahl II.1 |
| Holding archives: WVO records and PDFs; KHA inventory; Dresden (catalogued by Locat) | A2, D1 | no oplossing, no decipherment on either leaf, no bundled print |
| Unpublished witnesses: KHA Collectie Japikse copy of 53; Dresden minute of 57 (Loc. 9941/3 f.268-269, with a 'Zettel') | unseen | N4 does not exclude unpublished work. The Dresden minute could lower 57 to N0 in substance (clear text of the enclosure). It could never raise it |
| IA and Google Books phrase and gist search | A2, A3, **D2** | none |
| Solver repositories, Cryptiana, DECODE | V3, check-solved sweep | none |
| Open scholarship: CrossRef, HAL, Persée | A2 | nothing relevant |
| OpenAlex, Semantic Scholar | unreachable (429 in A2, A3, D2) | does not block (Danzay precedent) |
| JSTOR | queued: JSTOR-QUEUE.tsv lines 55, 56, 63, 64 | does not block |

## D2.4 Decision and sentences

**57: N4 (no prior decipherment located).** Confidence moderate. The editions are covered. The one witness that could change the
picture (August's Dresden minute with its 'Zettel') is unpublished and unseen.

- **Safe:** "The cipher enclosure of Elector August's letter to Orange, Torgau 18 Nov 1561 (KHA A 11/XIV B/41-6; WVO
  57), reads with the key of Orange's 1562 cipher (C 247, M 53 of 300 signs) as secret news that the Emperor had asked
  August to elect Maximilian King of the Romans in the Emperor's lifetime. No prior decipherment was located in the
  principal editions (Groen, Gachard, Rachfahl, von Weber, Kluckhohn, Goetz; Japikse's edition ends in September 1561)
  or in a full-text phrase search (AUDIT.md, 24 Sept 2026). Demandt's regest of the letter (HessJb 38, nr. 113) covers
  only the clear text. August's minute in Dresden, with a 'Zettel', has not been seen and may carry the enclosure in
  clear."
- **Unsafe:** "a previously unknown Saxon report of the 1561 election approach" (the approach is printed in Goetz 1891
  and Kluckhohn I nr. 148); "first decipherment" without "no prior decipherment located"; any sentence that drops the
  Dresden minute.

**53: N4 (no prior decipherment located), for a cryptanalytic reading.** Confidence moderate to low. The editions
are covered, but the text is S-grade with 35% M, and its gist, as well as its phrases, was searched.

- **Safe:** "The cipher postscript of Orange's letter to Elector August, Breda 24 Oct 1561 (Dresden Loc. 9941/3
  f.266r-v; WVO 53), reads with a cryptanalytically recovered key (S 238, M 126 of 364 signs; no key source; matched
  control 99.3%) as news that the Prince of Spain would marry his father's sister and come to govern the Netherlands,
  that the Duke of Vendôme would recover Navarre by agreement or by war, and Orange's view that, the King of France
  being so young, it would come to nothing. This is a cryptanalytic result. No prior decipherment was located in the
  principal editions (Groen, Gachard, Rachfahl, von Weber, Kluckhohn; Japikse's edition ends in September 1561) or in a
  phrase and gist search (AUDIT.md, 24 Sept 2026). The rumours themselves are in print from other senders."
- **Unsafe:** "Orange's 1561 cipher read for the first time"; any sentence that gives the text as certain word for
  word; any sentence that drops "cryptanalytic".

**Did we first-decipher?** Rule 10 allows only this: no prior decipherment was located after the logged search. That
is not established priority. For 57, the Dresden minute may already carry the plaintext.

## D2.5 Postmortem and corrections

- **Coverage failure found (not an over-claim):** A2.5 labels Gachard "Correspondance t.1, t.2", and A3.5 calls it
  "Gachard *Correspondance de Philippe II* t.1-2". V3's row 83 and D1 show it is the *Correspondance de Guillaume le
  Taciturne* (IA `correspondanced01willgoog`, `correspondancede02will`). The *Correspondance de Philippe II* was not
  searched. Its t.1 (1848) runs to 1567 and prints Margaret of Parma's and Granvelle's reports, not Orange's letters to
  Saxony, so D2 judges it not principal for 53/57. It is logged here as unsearched, not as covered.
- **Kluckhohn microfilm:** A2's "Kluckhohn (IA, weak OCR)" did not name the item. `bub_gb_3N1SAAAAcAAJ` holds only vol.
  II.2 (1572-76) despite its "2 volumes in 3" description. Vol. I is in `briefefriedrichd00frie`. Future workers should
  use the microfilm item.
- **Over-claims:** none found for 53 or 57 in NOTES.md, status.json or the SO prompt. status.json's results row is
  updated to the N4 classes and these safe sentences.
- **Suggestions (not done):** (1) Dresden inquiry for Loc. 9941/3 f.268-269, the one route that could lower 57; (2)
  Namèche 1884 pages on the Leipzig wedding, once books.google.com page text is usable again; (3) von Weber, *Archiv f.
  sächs. Gesch.* 3 (1865) 309 ff., for 57's context; (4) OpenAlex and Semantic Scholar from a session with a key or
  another IP.

Outreach: gate 2 open on JSTOR lines 55, 56, 63, 64 (ASKS row 39). CONTRIBUTIONS.md row added, held at gate 2, no draft.

Requests (D2): archive.org 14 (advancedsearch 8, metadata 2, djvu text 4), be-api.us.archive.org 1;
data.htrc.illinois.edu 1; www.googleapis.com 24; web.archive.org 1 (504); api.openalex.org 1 (429);
api.semanticscholar.org 1 (429). No subagents.

## Re-check 57 against DNOK (V8)

Verifier V8 (LANE V2), 24 Sept 2026, 11:36-11:40 UTC. Trigger: G3 (commit f3c4213, `sources/wvo/NOTES.md`) resolved WVO's
bronnen code DNOK on letter 57 as "Demandt, Nassau-oranische Korrespondenzen I, 78 nr. 113, excerpt", a printed work
that G3 thought D2's search log had missed. Scope: letter 57 only. Nothing was decoded.

**Verdict: 57 stays N4 (no prior decipherment located).** DNOK is the Demandt regest already read in A2.4. It
summarises the clear letter only.

| question | answer | evidence |
|---|---|---|
| (1) Is DNOK the publication and number A2 read? | **Yes.** "Nassau-oranische Korrespondenzen I" is part (I) of Demandt's *Nassau-oranische Korrespondenzen 1553-1570, in Gestalt der ... Regesten*, *Hessisches Jahrbuch für Landesgeschichte* 38 (1988) pp. 49-102. Part (II) is HessJb 39 (1989) pp. 87-150. WVO's "78" falls inside part I's page range, and nr. 113 is the "Torgau 1561 November 18" regest A2 read. It is not a separate monograph. G3's "1962" is not supported: the Google Books title search returns no Demandt edition of that title from 1962. The only other item of the title, `1YALtwAACAAJ` (1989, 100 pp., no preview, no ISBN), is probably an offprint of the same regests (inferred from title, year and length). The older *Nassau-Oranische Correspondenzen* (Meinardus, 1899) ends in 1559 and is out of range | Google Books API: title search (16 items); page ranges from *Repertorium van boeken en tijdschriftartikelen* 1993 ("dl 38, p. 49-102; 89, dl 39, p. 87-150"); *Archiv für Reformationsgeschichte* 1990 ("HessJb 38, 1988, S. 49"); *Hessisches Jahrbuch* 1991 ("Regesten (II) 87") |
| (2) Does nr. 113 print, paraphrase or summarise the cipher passage? | **No.** WVO's "excerpt" is the witness type: the Dillenburg archivists' 18th-century extracts (Wiesbaden 171 M fol. 4, 40), which Demandt printed as regests. Nr. 113 summarises the clear letter (the arrival at Breda, the Swedish king's English suit, the Öttingen-Schertlin feud). Nr. 115 summarises the 23 Nov postscript (Spain and the Inquisition; Lorraine and Guise) | Google Books full-text queries against the volume `OU4FAQAAIAAJ` (snippet view), all phrased `"Torgau 1561 November" + term`. Controls: "Schweden" (nr. 113) and "Inquisition" (nr. 115) both return the volume with the regest snippet. Test terms: Maximilian, Maximilians, "römischen König", römischen, Kaiser, Wahl, Kurfürsten, Zettel and Chiffre each return **0 volumes**. A snippet-view negative across the whole volume, not a page image |

**Residual risk.** Demandt abbreviates heavily ("Kf.", "Kg.", "Hgg."). "Ks." or "Kff." could evade the Kaiser and
Kurfürsten probes. "Maximilian" and "römisch" cannot be abbreviated that way, and both are absent from the volume. A page image
of p. 78 would still settle it (as D2's suggestion (4) says). It would not change the class unless it contradicts
the snippet text.

**Class unchanged: 57 N4**, confidence moderate. The D2.4 safe sentence stands. It already names "Demandt's regest of
the letter (HessJb 38, nr. 113) covers only the clear text". The unseen Dresden minute with its 'Zettel' remains the
one route that could lower it.

**Postmortem.** No miss by A2 or D2: WVO's own witness list (A2.2.3 (d)) already named the DNOK citation, and A2
read the regest. G3's flag came from the bare code's legend without the date. Its "1962" year is corrected in
`sources/wvo/NOTES.md`. No over-claiming sentence found. JSTOR: no new query (HessJb is not a JSTOR title in any row
here).

Requests (V8): www.googleapis.com 18 (books/v1, >=3 s apart). No other hosts, no subagents.
