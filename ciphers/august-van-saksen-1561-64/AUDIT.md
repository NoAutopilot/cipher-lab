# AUDIT: William of Orange to Elector August of Saxony, Brussels 16 Sept 1564 (WVO 126), cipher postscript

Verifier V3 for LANE V2, 24 Sept 2026 (08:51-09:05 UTC). This session did not solve the target and did not decode or
re-read the cipher. Claim under audit (LANE R worker R21, ROOM 08:41 UTC): "126 p4, 240 tokens: C 214 S 0 M 26 U 0;
key aligned from 98 f.66 against its decipherment on f.67; Spain news 1564: the Queen bled and purged twice, lost
the child." Letters 53 and 57 are not read and are out of scope.

## 1. Verdict

| item | class | prior plaintext | prior decipherment | confidence |
|---|---|---|---|---|
| WVO 126, postscript f.139 (Dresden, Geheimer Rat, Locat 8510/5, f.138r-140v) | **N3** | none located in print; a contemporary clear draft may survive unprinted (see 2.3) | none located | moderate |

Why not N4: the principal editions for this correspondence were searched (Groen t.I and Supplément, Gachard t.1-2,
Rachfahl I and II.1, Kluckhohn, von Weber, Raumer), but three named witnesses were not seen: the KHA minute with its
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
| Rachfahl, Wilhelm von Oranien I (1906), II.1 (1908) (IA wilhelmvonorani01rachgoog, 00rachgoog) | searched | phrases; "Locat 8510"; Sept 1564; Königin + krank/Frucht | one citation "Dr. Arch. Locat 8510" (II.1, n. to p.667): 1566 Augsburg diet context, not this letter |
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
