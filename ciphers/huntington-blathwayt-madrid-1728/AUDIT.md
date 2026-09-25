# AUDIT: huntington-blathwayt-madrid-1728 (BLA 184, 186, 191 enclosure (a))

Verifier: LANE W worker H (Opus), 24 Sept 2026, 08:35-08:55 UTC. Separate session from the solver (LANE R R17).
Claim under audit (NOTES.md, "R17: key and reading"): a key of 395 groups (grade C, from the contemporary
decipherments of BLA 179, 185, 187-190, 194) reads Huntington mssBLA 184 p1, 186 p1/p3 and 191 p5; 172 tokens,
C 129, S 0, M 22, U 21, H 0. The verifier did not decode and did not re-grade tokens.

## Verdict

| Item | Date, place | Tokens (C/M/U) | Prior plaintext | Prior decipherment | Class | Confidence |
|---|---|---|---|---|---|---|
| mssBLA 186, two cipher lines (p1, p3) | Madrid, 13 Sept 1728, letter of intelligence signed "N" | 24 (20/0/4) | not located | not located (none on the leaf, none elsewhere in the Huntington collection) | **N3** | medium |
| mssBLA 191, enclosure (a), p5 | Port Ste Marie, undated (forwarded from "Cesnok" to Newcastle 8 Aug 1729) | 141 (106/19/16) | not located | not located in the Huntington; the copy forwarded to Newcastle not traced | **N3** | medium-low |
| mssBLA 184 p1, 7 code groups | [1727-28], statement re M. Rottembourg | 7 (3/3/1) | not located | not located | **N3** (reading is 3 syllable groups; the names are unread) | medium |

**Second audit (below) corrects this table for BLA 186: the letter's clear text is printed (Rose 1831, ii 414-15), cipher
lines omitted; the classes stand.**

Why not N4: the principal editions are not all covered. Not reached: Google Books (LANE V's host, queries
posted), HMC *Polwarth* vols IV (1940) and V (1961) (Marchmont papers; not on Internet Archive; vols I-III are and
were searched), Christopher Storrs, *The Spanish Resurgence 1713-1748* (Yale 2016) (Storrs handled BLA 186 in
2006), HathiTrust full text, JSTOR (queued), and the unprinted originals in TNA SP 94/98-100 and the BL Newcastle
papers. Why not lower: no prior plaintext or decipherment of any of the three items was found in any family
searched, and the Huntington collection has no duplicate, draft or decipherment of them.

**The readings are partial.** U 21 and M 22 of 172 tokens; BLA 191(a) has 16 unkeyed groups and 19 uncertain ones,
BLA 184's four name codes are not read at all. Any outward sentence must say "partial".

## Per item

### mssBLA 186 (Huntington pointer 61211)
- Catalogue (dmGetItemInfo, 24 Sept 2026): "Letter of intelligence." Madrid, 1728-09-13. "In French, with two lines in
  cipher." Box 3 of the Blathwayt addenda. Archivist's slip in the folder: date corrected from 13 Sept 1708 to
  13 Sept 1728, "the letter ... describes the escape of Ripperda from confinement at Segovia", signed Christopher
  Storrs, 26 Apr 2006. The slip's field "For printed text or notice of this manuscript see:" carries no citation.
- Reading (R17): p1 *l'ambassadeur [73] a été fort [470] [778] [190]te affaire*; p3 *Monsieur de Patigno m'en a
  [849, doubtful] ce soir*. 24 tokens, C 20, U 4.
- Distinctive: Ripperda's escape from Segovia (2 Sept 1728 per Villars), a new Spanish squadron "pour empescher les
  gallions de passer en Europe", Patiño.
- Found: the event is widely printed (Villars, *Mémoires* t.5, "Riperda s'étoit sauvé du château de Ségovie";
  Petitot's *Collection des mémoires* t.70; TNA SP 89/35/51 Tyrawly to Newcastle 25 Sept 1728 NS; SP 78/196/64
  Robinson to Delafaye 19 Sept 1728; Hampshire RO 44M69/G2/193, a newsletter of 24 Sept 1728). None of these is this
  letter or quotes its cipher lines.

### mssBLA 191 enclosure (a) (pointer 61008, p5)
- Catalogue: to Newcastle, "Cesnok" (Cessnock, Ayrshire, the Hume-Campbell seat), 8 Aug 1729, signature
  illegible; "Enclosure: Two letters from Port Ste Marie: (a) undated, in cipher; (b) July 21, 1729, in French."
- Reading (R17): the writer thanks "milord" for his letter, says Keene gives him no orders, that he helped in "the
  past affair" without being told what he could offer towards the accommodement, and asks for orders. 141 tokens,
  C 106, M 19, U 16; "milord" rests on 665 = co|lo (M), "serai" on 1018 = sec|ser (M), "ignorance" on an unkeyed 585.
- The forwarding letter shows a sent copy went to Newcastle in Aug 1729. Whether the recipient's office deciphered
  it, and where that copy is (SP 94, SP 36, BL Add MSS Newcastle), was not established. TNA Discovery has no
  item-level description for it (SP 94/100, "Benjamin Keene (Seville, Port St Maries) ... 1729 Apr-Aug", is
  described at piece level only).
- Adjacent, checked on the image: mssBLA 192 (Port Ste Marie, 11 Aug 1729, pointer 61090, pp.1-2 read) is a clear
  French letter with bracketed passages in the pattern of BLA 189/190 (brackets mark what went into cipher),
  including "[je n'ai pu trouver aucun secours dans Monsieur Kenne ...]". It is on the same theme as 191(a) but is a
  different text; it is not a clear copy of 191(a).

### mssBLA 184 (pointer 60843)
- Catalogue: "Statement re M. Rottembourg", [1727-1728], "In French, partly in cipher." Slip: biographical note on
  Konrad Alexander Graf von Rothenburg (Repertorium der diplomatischen Vertreter), no print citation.
- Reading (R17): 7 groups inside clear prose; 3 C syllables (vo, s il, il s), 3 M, 1 U; the 1240/1243/1250/1259
  groups (names or nulls) unread. Class N3 only says that no prior reading was found; there is almost nothing read.

## Search log (24 Sept 2026)

| Family | What was searched | Result |
|---|---|---|
| (d) Holding archive, whole collection | CONTENTdm `dmQuery` on p15150coll7 with `CISOSEARCHALL^TERM^all^and`, full-text flag 1: Ripperda (0), "Ste Marie" (5: BLA 188, 190, 191, 192, unrelated HM 35183), "Sainte Marie" (1: BLA 189), Segovia (0), Patino (0), Keene (9: BLA 190 and unrelated), Madrid (15: BLA 130, 132, 142, 182, 186, 195 and non-BLA), deciphered (7: BLA 179, 185, 188, 189, 190, 194, one unrelated calendar), `callid^mssBLA` (all 195 BLA items listed; no second copy, draft or duplicate call number for 184/186/191). `dmGetItemInfo` on 182, 184, 186, 191, 192, 193 (wrapper "Correspondence from Port St. Marie 1729 Sent", modern endorsement "Secret Correspondence, etc."). `dmGetCompoundObjectInfo` 61090 and IIIF pp.1-3 of BLA 192. Local check: no 4-group run of the target ciphertext recurs in any glossed item (ciphertext.tsv) | **no duplicate, copy or decipherment of BLA 184, 186 or 191(a) in the collection** |
| (d) OAC finding aid | `oac.cdlib.org/findaid/ark:/13030/kt1199n4mx/entire_text/` (curl 202 empty; headless browser read) | item notes identical to CONTENTdm; no publication, microfilm or citation note for Box 3; related material: William Blathwayt Papers and the Blathwayt office papers (other finding aids, 17th c.) |
| (d) Huntington scholarship | IA full text "Blathwayt Addenda": *Huntington Library Quarterly* 56:3 (1993), notes cite "uncatalogued papers in the Blathwayt Addenda, Box 3", 1669 Temple-embassy items; fts in that issue for cipher, Ripperda, Keene, Marie: 0 | not our items |
| (a) Canonical prints | R17's `print-check.tsv`: Coxe, *Walpole* (1798) vols 1-3; Coxe, *Horatio Walpole* (1802); Coxe, *Kings of Spain* vols 2-3; HMC *Townshend* (1887); Armstrong, *Elisabeth Farnese* (1892), 7 phrases each, no hits. This session: HMC *Polwarth* vols I, I-II, II, III and two unnumbered IA scans (6 items) fts for Keene, "Port St. Mary", Cessnock: 0 relevant (Cessnock only in the family history) | no prior print located |
| (a) Ripperda narratives | IA: Syveton, *Une cour et un aventurier* (1896) fts "13 septembre 1728", "Port Sainte-Marie", Patiño, galions: no hit for the letter; IA global fts "sauvé du château de Ségovie": Villars *Mémoires* t.5 and Petitot t.70 only (the event, not this letter); Campbell *Memoirs of the Duke de Ripperda* (1740) and Moore *Lives* (1806/1814) identified, not phrase-searched individually (covered by the global fts only) | event printed; letter not located |
| (a) Keene | *Private Correspondence of Sir Benjamin Keene* (Lodge 1933) covers 1746-57, outside the date; not searched. McLachlan, *Trade and Peace with Old Spain* (IA global hit) cites Keene-Patiño letters in SP 94 for 1729-31, not these | no prior print located |
| (a) British Diplomatic Instructions (Camden) | no Spain volume for 1728-29 identified on IA (advancedsearch 0) | not reached |
| (b) TNA Discovery API | 14 queries: "Port St Mary 1729", "\"Port St Mary\" cipher", "Ripperda Segovia", "Ripperda escape 1728", "Cessnock 1729", "Keene Port St Mary", "Marchmont Newcastle 1729", SP 94 "Spain 1728/1729", SP 36 "Keene 1729", "Ripperda", "Port St Mary", "cipher Spain 1729" | SP 94 described at piece level only (SP 94/100 Keene 1729 Apr-Aug); SP 36 calendared items (36/13/171, 36/14/61, 36/8/208, 36/10/48) are not these letters; nothing for Cessnock or Marchmont |
| (c) Blathwayt scholarship | Jacobsen, *William Blathwayt* (1932) not searched: Blathwayt died 1717, these papers are 1725-34 strays in his family papers, outside the book's scope; CrossRef "Blathwayt papers Huntington Spain 1729" | nothing on Box 3's 1720s run |
| (e) IA global phrase search | "Marchmont" "Port St. Mary"; "Port St. Mary" 1729 Keene Patino; "Monsieur Keene" "aucun ordre"; "inutile dans l'ignorance"; "Blathwayt" "Port St"; "Port Sainte-Marie" 1729 Keene; "Earl of Marchmont" "Port St. Mary"; "Marchmont" 1729 spy Spain; "Storrs" "Blathwayt". "Cessnock" "Port St. Mary" returned 502 (not retried) | no hit for any item |
| (e) HathiTrust | not reached (site is Cloudflare-challenged; no phrase-search API) | unreachable |
| (e) Google Books | not this worker's host; queries posted in ROOM.md for LANE V | pending |
| (f) Solver repositories | shallow clones 24 Sept 2026, grep blathwayt, "port ste marie", "port st mary", ripperda, cessnock: dbourdeau/cyphersolver hits only `windischgraetz1720/key5018.md` (a name "Ripperda?" in a 1720 imperial key, a different system) and a Harley catalogue line on a 17th-c. Blathwayt grant; aaymeloglu/unsolved-ciphers 0 | no prior decipherment |
| (f) Cryptiana, DECODE | local `sources/cryptiana/` grep 0; DECODE catalogue cache no "Blathwayt" (check-solved, same date) | none |
| (g) Scholarship | CrossRef 6 queries (hits: Storrs, *The Spanish Resurgence* 2016; Lodge, "The Treaty of Seville (1729)", TRHS 1933, doi 10.2307/3678662; Goslinga, *Slingelandt's efforts* ch. on Soissons/Seville; none cites these items in metadata). OpenAlex 429 (one attempt). Semantic Scholar 200, 0 results. HAL 2 queries 0. Persée "Ripperda Ségovie 1728": loose matches only, top titles incl. "Lettres d'Espagne adressées par l'abbé de Montgon au cardinal et au marquis de Bissy" (French agent's letters, a different correspondence) | nothing on these items; Storrs and Lodge are leads |
| (g) JSTOR | 3 rows added to `JSTOR-QUEUE.tsv` | queued |

## Did we first-decipher?

Not established, and not claimable. No prior decipherment of these three items was located in the families above.
Two gaps matter: (1) BLA 191(a) was forwarded to Newcastle, whose office deciphered this correspondent's traffic
elsewhere in the run (BLA 188 is a set of copies to Newcastle and Townshend with decipherment); a contemporary
decipherment of the sent copy may sit in SP 94 or the Newcastle papers, which would make it N0/N1. (2) Storrs held
BLA 186 in 2006 and wrote the standard modern study of Spanish policy in these years; whether he read or quoted the
two cipher lines is unknown until his book is searched. The key itself is a recovery from contemporary
decipherments in the same collection (C), which is the Huntington's own material, not a cryptanalytic result.

## Safe and unsafe sentences

- **Safe (BLA 186):** "The two cipher lines of Huntington mssBLA 186 (Madrid, 13 Sept 1728) read in part (20 of 24
  groups) with a key set out from the contemporary decipherments of other letters in the same collection; no prior
  decipherment of these lines was located in the sources listed in AUDIT.md (N3)."
- **Unsafe (BLA 186):** "the first decipherment of the Ripperda-escape letter" / "previously unread lines".
- **Safe (BLA 191(a)):** "The undated cipher enclosure (a) of Huntington mssBLA 191 (Port Ste Marie, forwarded 8 Aug
  1729) reads in part (106 of 141 groups at grade C, 35 uncertain or unkeyed) with the same key; no decipherment was
  found in the Huntington collection or in the prints searched (N3)."
- **Unsafe (BLA 191(a)):** "the one item in the run never deciphered" / "genuinely undeciphered in the archive"
  (only the Huntington copy was checked; the copy sent to Newcastle was not traced).
- **Safe (BLA 184):** "Three of the seven code groups in mssBLA 184 read as syllables; the name codes are unread (N3)."
- **Unsafe (BLA 184):** any sentence that says BLA 184 has been read.

## Postmortem

Failure named: the item-level notes written before the reading (R1 inventory and NOTES "Image capture" section)
call BLA 191(a) "confirmed genuinely undeciphered in the archive" after checking only the Huntington leaves; the
forwarding letter itself shows a copy went to Newcastle. No sentence in the folder claims novelty in rule-10 words;
R17's report says "no novelty classified". Corrections made in NOTES.md (dated note under the R1 section and a
"Verifier audit" section) and in `images/inventory.tsv` (BLA191 p5 note). The French rendering in NOTES R17 is a
paraphrase that joins M tokens into words ("milord" from 665 = co|lo, "serai" from sec|ser); the graded tokens in
`reading_tokens.tsv` are the reading, the paraphrase is not. R17's flag stands: the glossed pages were not
re-checked for the '>' = 7 hand trait, so a few key values may be misread; this affects the key's C grade per group,
not the class.

Recommendations (not done here): a worker reads HMC *Polwarth* V and Storrs 2016 (library or Google Books) for
Port Ste Marie 1729 and BLA 186; the person may ask TNA/BL whether SP 94/100 or the Newcastle papers hold the
Aug 1729 Port St Mary enclosure and its decipherment. Second opinion requested: SO-BLATHWAYT-1728.

## Requests (this session)

hdl.huntington.org 19 (9 dmQuery, 6 dmGetItemInfo, 1 dmGetCompoundObjectInfo, 3 IIIF, >=2.5 s apart); oac.cdlib.org 2 (1 curl, 1 browser); archive.org 13 (advancedsearch 6, metadata 7);
be-api.us.archive.org 40; discovery.nationalarchives.gov.uk 14; api.crossref.org 6; api.openalex.org 1 (429);
api.semanticscholar.org 1; api.archives-ouvertes.fr 2; persee.fr 1; github.com 2 shallow clones.

## Second audit (adversarial), 24 Sept 2026

Auditor: LANE W worker I (Opus), 09:03-09:40 UTC, a session other than the solver's (R17) and the first
verifier's (worker H). Did not decode or re-grade tokens. Brief: try to find these texts, or a decipherment of
them, in print or catalogued elsewhere.

### Result in one line

**BLA 186's clear text is in print.** George Henry Rose, *A Selection from the Papers of the Earls of Marchmont*
(London 1831), vol. 2, pp. 414-415, "From the Abbé Paretti to Alexander Earl of Marchmont. [A translated
Extract.] September 3d, 1728", is an English translation of BLA 186 p1. The cipher line is not given. The
first audit's "prior plaintext: not located" for BLA 186 is wrong for the letter and right only for its cipher
lines. The three N3 classes stand, but only for the cipher passages.

### The Rose 1831 match (BLA 186)

- Source: IA `selectionfrompap02roseiala` (Rose, vol. 2, 1831), contents list "The Abbe Paretti to Alexander Earl
  of Marchmont . 414"; text pp. 414-415 (OCR `_djvu.txt`, downloaded once 24 Sept 2026). Found by be-api
  in-item search for "Paretti".
- Compared line by line with `images/BLA186_p1.jpg`: "Quoique je continue a estre privé de vos lettres ...
  la fuite de M. de Ripperda qui s'est sauvé du chateau de Segovie le 2e de ce mois, et qu'on n'a sçu icy que le
  10e ... Le Gouverneur ... fort bornés ... La Cour a depesché en Portugal ... à tous les ministres etrangers qui
  sont à Madrid ... s'il se trouve sur leurs estats. [cipher: 659.78.73.18.438.468.470.778.190.1102.53] Le
  Gouverneur du chateau estant proche parent de M. le Marquis de la Paix ... un coup de hazard, comme on en a
  veu mille autres." Rose: "Although I do not hear from you ... the flight of M. de Ripperda, who escaped from the
  Castle of Segovia, on the 2d instant, intelligence of which was not received here until the 10th ... letters
  have been written to all the foreign ministers, who are at Madrid ... if he is found in their states. . . .
  (Cypher.) . . . The governor of the castle being a near relation of the Marquis de la Paix ... as has happened
  in a thousand other cases." Every sentence matches, in order. It is the same letter.
- Date: Rose prints "September 3d, 1728"; the manuscript's dateline is "ce 13e Septembre 1728", and the text itself
  says the news came on the 10th, so Rose's "3d" is a slip or a dropped "1". This is why a date search on
  13 Sept 1728 missed it.
- The cipher line is shown as ". . . (Cypher.) . . ." and left out. Neither cipher line is given in any form.
  The p3 cipher line falls outside Rose's extract. Rose's source was the Marchmont papers, which is where the
  Huntington's Blathwayt Addenda BLA 179-194 run seems to come from (the finding aid says "formerly at Marchmont
  House"). This suggests Rose had the manuscript and did not decipher the line (inference, not established).
- Attribution: Rose names the writer as the Abbé Paretti (Pareti), "who communicated intelligence regularly to
  Alexander Earl of Marchmont during the Congress of Cambray, and who afterwards continued so to do from Spain for
  the benefit of the British government, and in consideration of a stipend from it" (p. 414 n.). The Huntington's
  own ArchivesSpace catalogue lists Pareti letters in this run. A web-search snippet of that catalogue on
  24 Sept 2026 read "Pareti, Giovanni Battista, Abbé ... Genoa ... resident of the duca di Modena in Madrid and
  London 1727-46", plus letters sent 19 July 1729 enclosing a cipher of 23 June 1729. I could not open the record:
  www.huntington.org returned 429, and I made no retry. BLA 186's "N" signature and the Port Ste Marie run
  (187-192) are therefore probably Pareti's (inference; the solver's files do not name him).
- Why earlier searches missed it: R17's print check and worker H's IA global full-text search used the French
  phrases, and Rose prints an English translation under a wrong date. Rose's *Marchmont Papers* was not on either
  source list. Lesson: for a letter to a British minister, search the English translation and the recipient's
  family papers, not only the original-language phrases.

### Search log (this session)

| Family | What was searched | Result |
|---|---|---|
| (a) HMC *Polwarth* | IA advancedsearch (3): only vols I (1911), I-II, II (1916), III, and two unnumbered scans (`reportonmanuscri0000unse_j5t0`, `reportonmanuscri0000grea_g6z8`) are on IA. From its be-api snippets (Pareti to Polwarth 1723-24, Cambrai; Rottembourg with St Contest), `g6z8` is a Cambrai-period volume (III or IV; the metadata has no volume number). be-api in-item on all six: "Port St. Mary", "Port St Mary", "Port Ste Marie", "Port Sainte Marie", "St. Mary's", Ripperda, Riperda, Keene, Cessnock, Pareti, Paretti | Cessnock only in the family history. Ripperda only 1725 (Vienna negotiation). Pareti/Paretti letters to Polwarth 1723-24 (Cambrai), some "in cipher", in `d2n9` (vol III) and `g6z8`. **Nothing from 1728-29. Vol V (1961, 1725-80) is not on IA and was not reached; vol IV (1940) could not be identified with certainty on IA** |
| (a) Rose, *Marchmont Papers* (1831) 3 vols | be-api in-item vols 1-3 (`selectionfrompap01roseuoft`, `02roseiala`, `03roseuoft`), the same terms, then the three `_djvu.txt` files downloaded once and grepped locally for port st, ste marie, sainte marie, keene, kenne, seville, cessnock, 1729, patino, patigno, cypher, cipher | **vol 2 pp. 414-415 = BLA 186 p1 (above)**; nothing on BLA 191(a), BLA 184, or any 1729 Port Ste Marie letter |
| (a) Warrender, *Marchmont and the Humes of Polwarth* (1894) | `marchmonthumesof00warr` in-item, the same terms | Riperda only for 1725, Cessnock only for the family; "Port Ste Marie" 502 twice (retried once) |
| (a) HMC Townshend (1887) | `manuscriptsofmar00greauoft` in-item | Ripperda project of 1726; Keene 1727 (H. Walpole to Keene); nothing from 1728-29 Port St Mary |
| (a) HMC Portland V-VIII | `manuscriptsofhis56greauoft` (V-VI), `manudukeportland07greauoft` (VII-VIII) in-item | "Port St. Mary" once, for someone's "services at Port St. Mary" (a 1702-era context); Ripperda only for Wharton's 1726 negotiations; nothing relevant |
| (a) HMC Carlisle (1897) | `earlcarlislehow00greauoft` in-item | Keene only in the 1770s (a different Keene); nothing |
| (a) HMC Egmont diary I (1920) | `manuegmontvisc01greauoft` in-item | nothing (the diary starts in 1730) |
| (a) HMC Stuart Papers | not searched: the Windsor calendar (vols I-VII) ends in 1718, before these items | out of range |
| (d) Ripperda narratives | in-item Campbell, *Memoirs of the Duke de Ripperda* (1740; `bim_eighteenth-century_memoirs-of-the-duke-de-r_campbell-john_1740`, `memoirsofdukeder00mass_0`), Moore, *Lives* (1806 `livescardinalal01moorgoog`, 1814 `livesofcardinala00mooruoft`), Syveton 1896 (`unecouretunavent00syve`): Patigno, galions, gallions, "Port St. Mary", Pareti | galleon context only (Moore 1806, Syveton); no Pareti, no letter of 13 Sept 1728 |
| (b) TNA Discovery API, 31 queries | "Port St Mary", "Port St. Mary", "Port Sainte Marie", "Port St Maries", Keene in SP 94 1727-30, Spain in SP 100 1727-30, SP 54 June-Dec 1729 (all), Seville in SP 54, Marchmont (1728-30; Jul-Sep 1729; SP 54), "Marchmont Spain", Ripperda 1728-29, Patino 1728-29, Segovia Aug-Dec 1728, Madrid 1-15 Sept 1728, cipher/decipher 1728-29, "intelligence Spain", Paret/Pareti, Cadiz. SP 89 query failed (URL encoding) and was re-run inside the SP 36/54 sweep only, not as SP 89 | SP 94/99 (1728) and 94/100 (1729 Apr-Aug, "Seville, Port St Maries") are described at piece level only. **SP 36/13/129** (19 July 1729) and **SP 36/14/184** (30 Aug 1729): Marchmont "from Cosnocke/Cesnock to [Newcastle]", "[Letter] to be laid before the Queen", "**The enclosures not forthcoming**". **SP 54/19/98A-B**: Marchmont 11 Nov 1729 enclosing a letter from Seville of 20 Oct 1729, "partially in cipher ... with de-cipher". Cholmondeley (Houghton) Ch(H) Corr. 1/1522: "Abbe Paret ? to Comte de Marchmont", 10 Apr 1728. No Discovery entry for Marchmont's covering letter of 8 Aug 1729 (BLA 191) or its enclosures. No item for BLA 186 or 184 |
| (b) BL Newcastle papers (Add MSS 32,686-33,201) | BL catalogue not tried (no API in the playbook; searcharchives.bl.uk is a JS app). Discovery lists "Add MSS 24321, 32253-309" (a family deposit) only | **unreachable / not searched** |
| (c) Scholarship | CrossRef, 7 queries (Abbé Pareti Marchmont; Ripperda escape Segovia 1728; Keene Seville 1729 Patiño; Storrs *Spanish Resurgence* Ripperda; British secret service Spain 1720s deciphering; Hume Campbell Marchmont Spain Cambrai; one 429, not retried). OpenAlex 429 (1 attempt). Semantic Scholar 429 (1 attempt). WebSearch 6 (Pareti Marchmont spy; Storrs Huntington Blathwayt Ripperda; HMC Polwarth V contents; Huntington mssBLA Pareti; Pareti Modena Madrid Ripperda; Campbell *Memoirs* 1740) | Storrs 2016 chapter DOIs only, no full text. ODNB entries for the 2nd and 3rd Earls. Nothing cites these items' cipher. Polwarth V's scope (1725-80) confirmed by the search summary |
| (c) JSTOR | 3 rows appended to `JSTOR-QUEUE.tsv` (Pareti AND Marchmont 1728/1729; Polwarth vol. V review; Storrs AND Blathwayt/Huntington/Pareti) | queued |
| (e) Google Books | not this worker's host; the 8 queries posted "for LANE V2" in ROOM.md at 09:03 | pending |
| (f) Phrase search | R17's `print-check.tsv` already ran the 7 French phrases through IA global full text (no hits). This session added in-item English/name searches (above), which found Rose | Rose 1831 (English translation) |
| (d) Holding archive | www.huntington.org ArchivesSpace record for Pareti: 1 request, 429, not retried. hdl.huntington.org excluded (covered by H) | seen as a search snippet only |

### Class per item (second audit)

| Item | Prior print of the letter | Prior plaintext of the cipher passage | Prior decipherment | Class | Change |
|---|---|---|---|---|---|
| BLA 186 (Pareti?, Madrid, 13 Sept 1728) | **yes**: Rose 1831, vol. 2, pp. 414-415, English translated extract of p1, misdated 3 Sept, with the cipher shown only as "(Cypher.)" | no (p1 omitted; p3 outside the extract) | none located | **N3, for the two cipher lines only**; the letter itself is printed (N1 for its clear text) | confirmed with a correction: the letter is not unpublished, only its cipher lines are unread in print |
| BLA 191(a) (Port Ste Marie, undated, forwarded 8 Aug 1729) | not located | not located | not located, but the sent copy's fate is open (see gap) | **N3** | confirmed; the N4 gap is narrowed to named places |
| BLA 184 (statement re Rottembourg, [1727-28]) | not located | not located | not located | **N3** (3 syllables read, names unread) | confirmed |

No item is raised. Nothing I found justifies N4. BLA 186 is not lowered below N3, because its cipher lines were
left out of the only print found. It is re-described: the letter is known and printed, and only the cipher lines
have no prior decipherment located (rule 10 wording for an N4 item; corrected by parent 7d after V7-QA4, 25 Sept 2026).

### What blocks N4 (toward-N4 list)

1. **HMC *Polwarth* vol. V (1961, 1725-80) and the vol. IV scope.** These calendar the Marchmont papers for exactly
   these years and would list Pareti's 1728-29 letters and any decipherments. Not on IA. Google Books snippet
   search (LANE V2 queries, plus "Pareti" OR "Paretti" 1728 1729 Polwarth) or a library read.
2. **TNA SP 36/13/129, SP 36/14/184, SP 54/19/98A-B, SP 94/99-100.** Marchmont's covering letters of 19 July and
   30 Aug 1729 survive with their enclosures "not forthcoming". The 8 Aug 1729 letter (BLA 191) is itself the
   covering letter, and it is at the Huntington, not TNA. SP 54/19/98B shows that the Secretary's office
   deciphered a later Pareti-type Seville letter. Whether a deciphered copy of 191(a) sits in SP 36/14, SP 54/19
   or SP 94/100 needs someone to read the images (State Papers Online, or the person / TNA copy order).
3. **BL Newcastle papers** (Add MSS 32,686 ff., diplomatic correspondence 1729): not reached.
4. **Cambridge UL Cholmondeley (Houghton) papers**, Ch(H) Corr. 1/1522 (Pareti? to Marchmont, 10 Apr 1728): Pareti
   copies reached Walpole. Check the Ch(H) calendar for Sept 1728 and Aug 1729 Pareti copies.
5. **Storrs 2016** full text (he dated BLA 186 in 2006): Google Books or JSTOR (queued).
6. **The Huntington ArchivesSpace Pareti record** (www.huntington.org, 429 today): read it once on another day for the
   letter list and any "deciphered" note.
7. **Rose's 1831 source manuscripts.** If the Huntington's BLA 186 is the very sheet Rose used, the "(Cypher.)"
   omission shows the cipher was unread in 1831. That is evidence for, not proof of, no contemporary
   decipherment.

### Safe and unsafe sentences (supersede the first audit's BLA 186 pair)

- **Safe (BLA 186):** "The Abbé Pareti's letter of 13 Sept 1728 to the Earl of Marchmont (Huntington mssBLA 186),
  on Ripperda's escape, was printed in English extract by Rose in 1831 (*Marchmont Papers* ii, 414-15, dated there
  3 Sept), with its cipher line omitted. Its two cipher lines read in part (20 of 24 groups) with a key set out
  from contemporary decipherments in the same collection. No prior decipherment of those lines was located in the
  sources listed in AUDIT.md (N3)."
- **Unsafe (BLA 186):** "an unpublished letter", "the first reading of the Ripperda-escape letter", "previously
  unread letter", and any sentence that does not cite Rose 1831.
- **BLA 191(a) and BLA 184:** the first audit's safe and unsafe sentences stand. For 191(a), add: "a decipherment
  of the copy sent to Newcastle may survive in TNA SP 36/54/94 or the BL Newcastle papers; not checked."
- All three readings are **partial**. Every outward sentence says so.

### Postmortem

Failure named: **a translated print under a wrong date.** The first audit and R17's print check searched the
French phrases, the date 13 Sept 1728 and the canonical diplomatic prints, but not the recipient's own printed
family papers (Rose 1831, which exists on IA in several copies). Rose prints the letter in English and misdates it
by ten days. The first audit's "Found: ... None of these is this letter" and its verdict row "Prior plaintext: not
located" for BLA 186 were over-broad. They are corrected here and in NOTES.md, and the class is unchanged because
the cipher lines were omitted. Brief lesson for `.claude/briefs/verifier.md` (a suggestion to the orchestrator; not
applied here): "search the recipient's printed family papers, in the language of the edition (often English
translation), by the writer's name and the event, not only by the original-language phrase and the date".

### Requests (this session)

archive.org 15 (advancedsearch 9, metadata 3, `_djvu.txt` download 3); be-api.us.archive.org 185 (in-item fts,
>=1.6 s apart and sequential, except about 7 minutes at 09:10 when a manual check overlapped the background run;
this may have caused 10 x 502, and the 6 failed queries were retried once); discovery.nationalarchives.gov.uk 31;
api.crossref.org 7 (one 429); api.openalex.org 1 (429); api.semanticscholar.org 1 (429); openlibrary.org 1;
www.huntington.org 1 (429, stopped); WebSearch 6.

## N4 decision, 24 Sept 2026

A fresh verifier session, LANE W worker K (Opus; orchestrator session_011UFnhZnyCntZ8Bn9FpKyTq), 09:48-10:00 UTC.
It did none of the solving (R17), the first audit (H) or the second audit (I), and it did not decode. Question:
does the logged coverage meet rule 10's N4 ("N3 with the principal editions, catalogues and project pages covered,
internal or unpublished work not excluded") for BLA 186, BLA 191(a) and BLA 184?

**Answer: not yet. All three stay N3.** Every principal printed edition is now covered. HMC *Polwarth* vol. V, the
one printed gap, was closed this session at token level through HathiTrust's HTRC Extracted Features (s.2). The
holding archive's catalogue is covered. One principal project family is still open: **DECODE's "Decrypted"
records.** The only DECODE check so far is a grep of two cached lists that hold the Non-decrypted and Partially
decrypted records (and a grep of Aymeloglu's cached catalogue for "Blathwayt" only). A Huntington, Blathwayt or
Marchmont record marked Decrypted would not appear in either list. This has been posted for LANE N. If LANE N's
search finds no DECODE record for these items, all three go to N4 with no further work, using the sentences in s.4.

### 1. Principal families and coverage

| family | principal? | covered | where AUDIT.md shows it |
|---|---|---|---|
| Rose, *Marchmont Papers* (1831) vols 1-3 (the recipient's printed papers) | yes | yes: in-item fts plus local grep of all three `_djvu.txt`; **vol 2 pp.414-15 = BLA 186 p1 in English, cipher omitted** | second audit, Rose rows |
| HMC *Polwarth* vols I-III and two unnumbered IA scans | yes (the Marchmont calendar) | yes, in-item fts | first audit (a); second audit (a) |
| HMC *Polwarth* vol. IV | yes (scope check) | **yes, this session**: HTRC EF `mdp.39015031910725`. The tokens 1728 and 1729 occur on no page, so the volume ends before these items. Ripperda occurs there only in the Cambrai/Vienna years | s.2 |
| HMC *Polwarth* vol. V (1961; 1725-80) | yes: the one printed calendar of the Marchmont papers for these years | **yes, this session, at token level** (HTRC EF, two copies: `msu.31293105166841` and `mdp.39015031910733`). The volume does not print BLA 186, 191(a) or 184 (s.2) | s.2 |
| Warrender, *Marchmont and the Humes of Polwarth* (1894) | yes (family) | yes | second audit (a) |
| HMC Townshend, Portland V-VIII, Carlisle, Egmont; Coxe *Walpole*, *Horatio Walpole*, *Kings of Spain*; Armstrong 1892 | yes (period editions of the ministers the letters reached) | yes | first audit (a); second audit (a); print-check.tsv |
| British Diplomatic Instructions (Camden) | would be principal | no Spain volume exists for these years (first audit: IA advancedsearch 0; the series has Sweden, France and Denmark volumes for 1689-1789) | first audit (a) |
| Ripperda narratives (Campbell 1740, Moore 1806/1814, Syveton 1896, Villars/Petitot) | yes for the event | yes | first audit (a); second audit (d) |
| Huntington catalogue: CONTENTdm item records, compound objects, whole-collection full text | yes (holding archive) | yes | first audit (d) |
| Huntington finding aid (OAC export of the ArchivesSpace catalogue) | yes | yes, entire text | first audit (d) |
| Huntington ArchivesSpace item pages (www.huntington.org/collections/lib-mssbla-aspace-*) | same catalogue as OAC | covered through OAC. This session's WebSearch shows the per-item Pareti and Du Bourgay records with the finding-aid wording (1720-34 agents, "Giovanni Battista Paretti"). No extra field has been seen. www.huntington.org gave a 429 to worker I, so no request was made this session | this section |
| TNA Discovery catalogue | yes (catalogue) | yes, 45 queries; SP 94 is described at piece level only | first audit (b); second audit (b) |
| TNA SP 36/13, SP 36/14, SP 54/19, SP 94/99-100 leaves; SP 89 | **no for N4**: archival, unpublished leaves. Rule 10 N4 leaves "internal or unpublished work not excluded" (Eckert precedent: NARA RG 107, Meigs letterbook) | pointer only | second audit, toward-N4 2 |
| BL Newcastle papers (Add MSS 32,686 ff.) | **no for N4**: archival | not searched | second audit, toward-N4 3 |
| Cambridge UL Cholmondeley (Houghton) correspondence | **no for N4**: archival | not searched | second audit, toward-N4 4 |
| Storrs, *The Spanish Resurgence* (2016); JSTOR; OpenAlex, Semantic Scholar, CrossRef, HAL, Persée | **no for N4**: scholarship, not an edition or catalogue. It is outreach gate 2 (CLAUDE.md, 24 Sept 2026: a queued JSTOR row never blocks N4 on its own) | CrossRef, HAL, Persée yes; OpenAlex and S2 429; JSTOR 6 rows queued | first and second audit (g)/(c) |
| Google Books phrase search | yes (template family e) | yes: LANE V2, 8 queries, all totalItems 0, API confirmed live | google-books-2026-09-24b.tsv |
| IA full text (global and in-item) | yes (template family e) | yes | first audit (e); second audit |
| HathiTrust whole-library full text | no for N4 (a search engine, not an edition). The HathiTrust volume that matters, *Polwarth* V, is covered by HTRC EF | EF yes; site search unreachable (Cloudflare) | s.2 |
| Solver repositories (Bourdeau, Aymeloglu), Cryptiana | yes (cipher community) | yes | first audit (f) |
| **DECODE (de-crypt.org), Decrypted records** | **yes (cipher community; the catalogue where a prior decipherment of a manuscript cipher would be listed with its holder)** | **no**: `sources/decode/records-non-decrypted-2026-09-24.tsv` (1,186 Non-decrypted and Partially decrypted rows) has no Huntington holder and no 1728-29 item except BL Add MS 32270 ff.41-42 (1727, a different holder). The Decrypted status (x_status=1) has not been listed. Aymeloglu's cached catalogue was grepped for "Blathwayt" only | this section; NOTES "DECODE" |

### 2. HMC *Polwarth* IV and V through HTRC Extracted Features (this session)

Route: the HathiTrust Bibliographic API (`catalog.hathitrust.org/api/volumes/brief/recordnumber/000233444.json` and
`100220849.json`, full Chrome User-Agent) lists these copies: v.4 `msu.31293027029150` and `mdp.39015031910725`
(full view); v.5 `msu.31293105166841` (full view, pdus), `mdp.39015031910733` (search-only) and
`osu.32435022299184` (search-only). Record numbers came from a WebSearch restricted to catalog.hathitrust.org.
Per-page token counts came from `data.htrc.illinois.edu/ef-api/volumes/HTID/pages?pos=false`, fetched once per
volume through `tools/htrc_ef_headwords.py`'s cached fetcher (cache in the scratchpad, not committed). They were
grepped by regex for Pareti/Paretti, Ripperda/Riperda, cypher/cipher, decypher, Port, Mary, Marie, Keene, Patiño,
Segovia, 1728, 1729, Cessnock, Madrid, Rottembourg, Seville, Abbé.

Vol. V (`msu.31293105166841`, 474 pages, 280,094 tokens; `mdp` copy consistent at an offset of -4):

- The 1725-30 section is seq 47-72. It calendars the 2nd Earl's letters to and from Townshend, Rondeau, Newcastle,
  Stair, Eglinton, Haddington and others, and the Scottish civil list (seq 53-56). The 1729 pages (seq 66-68) are
  about Gibraltar, Don Carlos, Parma and the Seville treaty, as news in Marchmont's own correspondence.
- **Pareti** is on seq 48 (Townshend to Marchmont, Sept 1725, "Abbe Pareti"), seq 50 (a letter headed ABBE
  PARETI, Oct/Nov 1726, Genoa/Madrid/Cambray, personal: health, "overturnd" chariot, "unknight/knighting"), seq 62
  (Townshend to Marchmont, Sept 1728, about the Abbé Pareti as a correspondent: "intelligences", "secret",
  "channel", "canal", "marks", "papers", "money", "office"), and seq 452 (index: "Pareti, Paretti ... letter(s),
  pension, Genoa, Madrid").
- **Ripperda** occurs once, seq 15 (the introduction). **Segovia 0, Patiño 0, Rottembourg 0.** No page carries
  Pareti with Ripperda, Segovia or any 1728 escape vocabulary.
- **decypher** occurs once, seq 60. The page also has Rondeau, Moscow, Petersburg, Czarish, Keene and Townshend in
  July-Sept 1728, and no Pareti, Madrid or Spain token. It is Russian-court correspondence, not these items.
  cypher/cipher: seq 226-414 only, the 1740s-60s.
- **Port St Mary** is not printed. "Port" is on seq 54 (civil-list page), 171, 349 and 436-462 (late matter and
  index). None of those pages has Mary/Marie with Port. Cessnock is on seq 447 and 462, index only.

Reading: vol. V prints no text of BLA 186, 191(a) or 184 and no decipherment of them. The nearest item is
Townshend's Sept 1728 letter about Pareti's intelligence channel (seq 62). It shows that Townshend's office got
Pareti's reports. It does not print them. **Limits:** this is a token-level reading of OCR, with no word order and
no sight of the page. A decipherment printed without any of the searched names is not excluded. The regexes found
the expected tokens (Pareti in the index, Townshend's letters), so the method works on this OCR.

Vol. IV (`mdp.39015031910725`, 436 pages): Pareti on 8 pages and Ripperda on 10. The tokens 1728 and 1729 occur on
no page, so the volume ends before these items. It is out of range.

### 3. Decision per item

**BLA 186 (Pareti to Marchmont, Madrid, 13 Sept 1728), two cipher lines: N3, not raised.** The letter's clear part
is printed (Rose 1831 ii 414-15, English extract, misdated 3 Sept, cipher shown only as "(Cypher.)"). No printed
edition, catalogue or holding-archive record gives the cipher lines or a decipherment. That includes *Polwarth* V,
covered this session. The one open principal family is DECODE Decrypted records.

**BLA 191(a) (Port Ste Marie, undated, forwarded from Cessnock 8 Aug 1729): N3, not raised.** Same position.
The copy sent to Newcastle, and any decipherment made of it in SP 36/54/94 or the Newcastle papers, is
archival and unpublished. It does not block N4 (Eckert precedent), but the safe sentence must name it.

**BLA 184 (statement re Rottembourg, [1727-28]), seven code groups: N3, not raised.** *Polwarth* IV has many
Rottembourg pages and ends before 1728. Vol. V has no Rottembourg token. Same open family as the other two.

**Blocking family, all three items: DECODE Decrypted records.** Smallest job: one LANE N search on de-crypt.org
(the no-login `RecordsList` form with x_status=1, or a holder/keyword search) for Huntington, Blathwayt, Marchmont
and Ripperda, plus Madrid, Seville or Port Ste Marie for 1728-29. Posted in ROOM.md. It needs no person. **If
the search is negative, all three go to N4 with the sentences below, and no other family is left to cover.**

### 4. Sentences for use once DECODE is negative (not before)

- **BLA 186 (N4, conditional):** "The Abbé Pareti's letter of 13 Sept 1728 to the Earl of Marchmont (Huntington
  mssBLA 186), on Ripperda's escape, was printed in English extract by Rose in 1831 (*Marchmont Papers* ii,
  414-15, dated there 3 Sept), with its cipher line omitted. Its two cipher lines read in part (20 of 24 groups;
  4 unkeyed) with a key set out from contemporary decipherments of other letters in the same collection. No
  prior decipherment of those lines located (search log in AUDIT.md)."
- **BLA 191(a) (N4, conditional):** "The undated cipher enclosure (a) of Huntington mssBLA 191 (Port Ste Marie,
  forwarded 8 Aug 1729) reads in part (106 of 141 groups at grade C; 19 uncertain, 16 unkeyed) with the same key.
  No prior decipherment located in print, in the Huntington's catalogue or in the cipher community's catalogues.
  The copy sent to Newcastle, and any decipherment made of it in the State Papers or the Newcastle papers, was
  not checked."
- **BLA 184 (N4, conditional):** "Three of the seven code groups in mssBLA 184 read as syllables. The name codes
  are unread. No prior decipherment located." Since almost nothing is read, this is not worth an outward note.
- Until then, the second audit's N3 sentences stand. Every sentence says "partial" or "in part". None says "first",
  "unpublished", "new" or "unread", and every BLA 186 sentence cites Rose 1831.

### 5. Postmortem

No over-claim found in this pass. One correction: the second audit's toward-N4 item 1 ("HMC *Polwarth* vol. V
... would list Pareti's 1728-29 letters and any decipherments") is now answered. Vol. V does not print them. It
mentions Pareti only in Townshend's letters and the index. Items 2-4 and 6-7 on that list are archival or
holding-archive details and do not block N4. Item 5 (Storrs) is outreach gate 2. The gap nobody logged is
DECODE's Decrypted status. The earlier audits recorded DECODE as covered from lists that cannot contain a
Decrypted record. Lesson for the verifier brief (suggestion, not applied): "a DECODE cache check names which
statuses the cache holds; a Non-decrypted list cannot show a prior decipherment."

### 6. Requests (this session)

catalog.hathitrust.org 2 (Bibliographic API); data.htrc.illinois.edu 6 (3 metadata, 3 page files, 2 s apart,
sequential); WebSearch 2; www.huntington.org 0; de-crypt.org 0; Google Books 0; gallica 0.

### DECODE Decrypted search (LANE N2), 24 September 2026

For LANE W (ROOM 09:51, worker K): the DECODE gap named in section 5 above ("the earlier audits recorded
DECODE as covered from lists that cannot contain a Decrypted record") is now closed. `tools/decode_list.py
--status decrypted --record-type cipher` (no login; the RecordsList grid is public for any status per
`sources/decode/NOTES.md`) fetched the full Decrypted-cipher catalogue: **1360 records**, 28 requests, 1.6s
apart, written to `sources/decode/records-decrypted-2026-09-24.tsv`. Case-insensitive grep of `holder_raw`,
`city`, `shelfmark_code` against each name/place:

| Query | Hits |
|---|---|
| Huntington | 0 |
| Blathwayt | 0 |
| Marchmont | 0 |
| Ripperda | 0 |
| Keene | 0 |
| Pati\[nñ\]o (Patiño/Patino) | 0 |
| Madrid | 59 (none dated 1725-1732; date ranges cluster 1424-1626, none in 1728-29) |
| Sevill(e/a) | 0 |
| Port(e)? Sainte.Marie | 0 |
| Puerto de Santa Mar(ía/ia) | 0 |

No DECODE Decrypted record matches Huntington, Blathwayt, Marchmont, Ripperda, Keene, Patiño, or Madrid/
Seville/Port Sainte-Marie/Puerto de Santa María for 1728-29. This does not change any N-class above (no
prior decipherment of BLA 186, BLA 191(a) or BLA 184 found on DECODE); it closes the one still-open search
family named in section 5. Note per rule 10: absence from DECODE's Decrypted list is a search result, not a
novelty verdict -- the N4 sentences in section 4 stand as written. No N-class in this file is changed by this
subsection (append-only per LANE N2 brief).

Requests this subsection: de-crypt.org 28 (decode_list.py, no login). Cost: well under $5 cap for this step.

## N4 set (LANE W2 worker B1, 24 Sept 2026)

A verifier session, LANE W2 worker B1 (Opus; orchestrator session_01CLm9uFwyau9hRmDcm2vALE), 11:00-11:04 UTC. It
did no solving (R17) and none of the three audits (H, I, K) or the DECODE search (dcA). It did not decode.
Question: is K's condition ("if LANE N's search finds no DECODE record for these items, all three go to N4") met,
and is any principal family left open that K's table did not name?

**Answer: met. BLA 186 (cipher lines), BLA 191(a) and BLA 184 are N4, "no prior decipherment located".** The
letter BLA 186 itself stays N1 for its clear text (Rose 1831 ii 414-15).

### 1. dcA's DECODE Decrypted search, re-checked from its own file

`sources/decode/records-decrypted-2026-09-24.tsv`: 1,361 lines = header + 1,360 rows, 1,360 distinct record ids,
matching dcA's count. The file has holder, city, shelfmark and date columns only (no title, sender or recipient),
so a name can match only through the holder or shelfmark. Case-insensitive grep, whole file:

| Query | Hits |
|---|---|
| Huntington, San Marino, Blathwayt, Marchmont, Polwarth, Ripperd, Keene, Pati (Patiño/Patino), Pareti | 0 each |
| Stanhope, Townshend, Newcastle, Hardwicke, Waldegrave, Walpole | 0 each |
| Sevill, Seville, "Santa Mar", "SP 94"/"SP94" | 0 each |
| 1727, 1728, 1729, 1730, 1731, 1732 (anywhere in a row) | 0 each |
| Madrid | 59 rows; none has a date range reaching 1725-32 |

Date columns: every row whose date range overlaps 1725-1732 was listed (a range test, not a string match). Besides
BL Add MS 20563 (53 rows, 1706-25, Italian), they are BL Add MS 32264 f.47 (1653-1850), 18982 f.195 (1649-1950),
32270 ff.19-40 (1719-1839), 32287 f.48 (1716-1836), 32305 ff.2-3 (1726), ff.4 and 8-9 (1700-99); Beinecke Osborn fc37
box 6 folder 35 (1697-1737, English); HHStA Vienna Chiffrenschlüssel Kt.13-14, 20 (keys, 1540-1877); TNA State
Papers inv.nr. 106 box 7 (1702-1837, French). None is held by the Huntington, and none is a Blathwayt, Marchmont or
Pareti item. The BL Add MS 32264-32305 run and SP 106 are cipher-key collections. Whether one of them holds this
key is a lead for a solver (below). It is not a prior decipherment of these three leaves. **dcA's result holds.**

### 2. Any principal family left open?

K's table (s.1) lists every family in the verifier template, rule 10's N4 wording and the second audit's toward-N4
list. Checked each against the logs:

- Canonical and recipient prints (Rose 1831; HMC *Polwarth* I-V; Warrender; HMC Townshend, Portland, Carlisle,
  Egmont; Coxe; Armstrong; Ripperda narratives): covered (first and second audit; K s.2).
- Holding archive (CONTENTdm, OAC finding aid): covered. ArchivesSpace item pages: covered through OAC (K).
- TNA Discovery catalogue: covered. SP leaves, BL Newcastle papers, Cholmondeley (Houghton): archival and
  unpublished. Rule 10's N4 leaves "internal or unpublished work not excluded" (Eckert precedent), so they do not
  block N4. BLA 191(a)'s safe sentence names them.
- Google Books (8 queries, 0), IA full text (global and in-item): covered.
- Solver repositories and Cryptiana: covered (first audit f). DECODE Decrypted: covered (dcA; s.1 above).
- **Cipherbrain (Schmeh) was not logged by any audit.** The Danzay and Eckert N4 decisions covered it. Closed now:
  one WebSearch restricted to scienceblogs.de, cipherbrain.net and scienceblogs.com for Blathwayt, Marchmont,
  Pareti or Ripperda with cipher, 1728 and Huntington (the tool ran three variants). No post on these items or this
  correspondence. Hits were the Top-50 list, Thirty Years' War cryptograms, Henry II's device and other unrelated
  posts.
- Scholarship (Storrs 2016, Lodge 1933, the open indexes, JSTOR): not a principal edition or catalogue, so it does
  not block N4 (K s.1; CLAUDE.md: a queued JSTOR row never blocks N4 on its own). It is outreach gate 2 (s.5).
- HathiTrust whole-library full text: unreachable (Cloudflare). The one HathiTrust volume that matters,
  *Polwarth* V, is covered at token level (K s.2).

Nothing principal is open.

### 3. Verdict

| Item | Prior print | Prior decipherment | Class | Confidence |
|---|---|---|---|---|
| mssBLA 186, two cipher lines (p1, p3); Abbé Pareti to Marchmont, Madrid, 13 Sept 1728 | the clear part is printed in English extract: Rose, *Marchmont Papers* (1831) ii 414-15, dated there 3 Sept, cipher shown only as "(Cypher.)". p3 is outside the extract | none located | **N4** for the cipher lines; **N1** for the letter's clear text | medium |
| mssBLA 191, enclosure (a), p5; Port Ste Marie, undated, forwarded 8 Aug 1729 | none located | none located. The copy sent to Newcastle and any State Papers or Newcastle-papers decipherment of it were not seen | **N4** | medium-low (the sent copy's fate is open) |
| mssBLA 184 p1, seven code groups; statement re Rottembourg, [1727-28] | none located | none located | **N4** (3 syllable groups read, name codes unread) | medium |

The readings are partial: C 129, M 22, U 21 of 172 tokens, no H. They are grade C from contemporary
decipherments of sister items, not cryptanalysis.

### 4. Safe and unsafe sentences (supersede K s.4's conditional wording; its sentences are adopted unchanged)

- **BLA 186.** Safe: "The Abbé Pareti's letter of 13 Sept 1728 to the Earl of Marchmont (Huntington mssBLA 186),
  on Ripperda's escape, was printed in English extract by Rose in 1831 (*Marchmont Papers* ii, 414-15, dated
  there 3 Sept), with its cipher line omitted. Its two cipher lines read in part (20 of 24 groups; 4 unkeyed)
  with a key set out from contemporary decipherments of other letters in the same collection. No prior
  decipherment of those lines located (search log in AUDIT.md)." Unsafe: "an unpublished letter", "first
  decipherment of the Pareti letter", or any sentence that omits Rose 1831.
- **BLA 191(a).** Safe: "The undated cipher enclosure (a) of Huntington mssBLA 191 (Port Ste Marie, forwarded 8 Aug
  1729) reads in part (106 of 141 groups at grade C; 19 uncertain, 16 unkeyed) with the same key. No prior
  decipherment located in print, in the Huntington's catalogue or in the cipher community's catalogues. The copy
  sent to Newcastle, and any decipherment made of it in the State Papers or the Newcastle papers, was not
  checked." Unsafe: "never deciphered", "read for the first time", or a full reading.
- **BLA 184.** Safe: "Three of the seven code groups in mssBLA 184 read as syllables. The name codes are unread.
  No prior decipherment located." Unsafe: any sentence that names the persons coded. Not worth an outward note.

### 5. Outreach gate 2 (for the orchestrator; no draft written)

- JSTOR-QUEUE.tsv rows for this target, all `queued`, none answered or waived: file lines 45, 46, 47, 57, 58, 59
  (Port St Mary/Keene/Marchmont; Ripperda Segovia 1728; Blathwayt Huntington Spain; Pareti Marchmont 1728/29;
  Polwarth V review; Storrs Spanish Resurgence). ASKS row 40 asks the owner to run or waive them.
- Open-index pass: CrossRef (first audit 6 queries, second 7), HAL (2), Persée (1) done. **OpenAlex 429 in both
  audits; Semantic Scholar 200 with 0 results in the first audit, 429 in the second.** OpenAlex is not done. Either
  one retry from a session whose OpenAlex quota is fresh, or the owner runs it or waives it (ASKS row 40).
- Google Books queries done (LANE V2, 8 queries, 0 hits).
- Any outreach note on BLA 186 must state the Rose 1831 print (gate 3) and link the Huntington item image, Rose
  vol. 2 at pp.414-15 on archive.org (`selectionfrompap02roseiala`), and this AUDIT.md (gate 6).

### 6. Postmortem

No over-claim found in the repo's files. Two gaps corrected: (1) no audit had logged Cipherbrain; closed above.
(2) status.json's grade line said "N4 waits only on a DECODE Decrypted search"; updated to N4. Lead for a solver,
not done here (Usage rule 7): DECODE's BL Add MS 32270 ff.19-40 and 32305 ff.2-9 (1719-1839, 1726) and TNA SP 106
box 7 are 18th-century British key collections; one may hold the Pareti code and settle BLA 191(a)'s 16 unkeyed
groups.

### 7. Requests (this session)

WebSearch 1 (Cipherbrain, three variants inside the tool). No other network requests: de-crypt.org 0,
www.huntington.org 0, Google Books 0.

## Second opinion SO-BLATHWAYT-1728 (ChatGPT, pull request 6), checked 24 Sept 2026, 16:35 UTC

Verifier V3a (Opus, for LANE V4, session_017iueT2nBBNcQkKp8Se8pcP). Input: `second-opinions/chatgpt-2026-09-24.md`
("GPT-6 (Codex)", copied from branch `second-opinion/SO-BLATHWAYT-1728`, PR 6, unmerged). It finds no prior print or
decipherment of the cipher passages, points out that our prompt left out the Rose 1831 print, and makes eight remarks on
the reading. Its own access failed on Rose, Storrs, OAC and the Huntington. No decoding.

| # | claim | source checked | verdict | correction made |
|---|---|---|---|---|
| 1 | the prompt omits the known print: Rose, *Marchmont Papers* (1831) ii 414-15, English extract, "Paretti" to Marchmont, dated 3 Sept 1728, cipher shown as "(Cypher.)" | PROMPT-chatgpt.md (no Rose, no Paretti); AUDIT "The Rose 1831 match" (line-by-line comparison with the p1 image, IA `selectionfrompap02roseiala`) | **right**: our prompt was stale; the print is ours and page-verified | PROMPT-chatgpt.md now states the Rose print and that only the cipher lines are in question |
| 2 | Storrs (2016) and Lodge, TRHS 1933: located, unverified for these items | AUDIT search log (g) (Storrs; Lodge doi 10.2307/3678662) and N4 decision table (scholarship, outreach gate 2) | **agrees**; no new family | none |
| 3 | Rose's 3 Sept vs the MS's 13 Sept is 10 days, not the 11-day style difference, so not a routine conversion; "misprint" needs evidence | AUDIT "The Rose 1831 match": the letter says the news reached Madrid "le 10e", so it was written after the 10th; Rose's own text (translated) carries "not received here until the 10th" | **right on the arithmetic; our inference already rests on internal evidence**, not on style conversion | none |
| 4 | BLA186 p3 mechanical output "m'en a monsieur ce soir": 849 = monsieur from one BLA188 gloss | reading.txt BLA186_p3_L01; key.tsv 849 monsieur C, n=1, BLA188; NOTES already: "849 needs its BLA188 gloss re-checked on the image" | **right, already recorded** | solver suggestion restated in NOTES.md |
| 5 | BLA191 paraphrase overstates: milord, m'aime, serai, ignorance rest on joins and repairs; 585 = ig inferred | reading.txt BLA191_p5 L01 "mi co r d", L06 "m' ame", L12 "je sec ai in utile dans l' [585] no ra n ce"; NOTES: 585 "I, not in the key" | **right** for the prompt (NOTES marks 585) | PROMPT-chatgpt.md marks the French as interpretation; NOTES.md suggestion |
| 6 | BLA184 not established by three syllables | NOTES and N4 set: "3 syllable groups read, name codes unread"; safe sentence says so | **agrees** | none |
| 7 | shared 7/3 transcription error could propagate through training glosses | NOTES (both transcribers misread the same form of 7) | **fair**, reading matter | NOTES.md suggestion |
| 8 | the Keene sentence says only that he has no orders for the writer | reading.txt L06-07 "il n a aucun ordre des [1019] [711] s pour moi"; NOTES said "complaining that Keene ... gives him no orders" | **right** (NOTES gloss too broad) | NOTES.md gloss narrowed |
| 9 | Pareti attribution holds for BLA 186 (Rose), not automatically for the Port Ste Marie enclosure | safe sentences: BLA 186 names Pareti (Rose); BLA 191(a) names no writer; NOTES l.315 "very probably" Pareti for 186 only | **agrees**; no over-claim found | none |
| 10 | Storrs's folder slip is handling, not decipherment | AUDIT per-item BLA 186 | **agrees** | none |

Also corrected: NOTES.md's novelty line still read "BLA 186 N3, BLA 191(a) N3, BLA 184 N3" after the N4 set; it now
gives the N4 set's classes.

**Its leads.** (1) Rose vs BLA 186: done (Rose match). (2) Newcastle's receiving copy, SP 36/13/129, SP 36/14/184,
SP 54/19/98A-B: already the stated residual in the BLA 191(a) safe sentence (archival). (3) group 849 and 7/3: solver
suggestion. (4) Storrs's notes: scholarship, outreach gate 2 (ASKS 40). (5) British key collections: solver resource,
not a novelty family. (6) enclosure date vs forwarding date: the safe sentence says "undated ... forwarded 8 Aug 1729".

**Class.** No check found a prior print or decipherment of the cipher passages. **BLA 186 cipher lines N4 (clear text
N1), BLA 191(a) N4, BLA 184 N4**, all unchanged; the N4 set's safe sentences stand.

**Postmortem.** The prompt was written from the first audit, before the second audit found Rose, and was never
refreshed; an outside reader was asked to find a print we already had. NOTES.md's novelty line lagged two audits.
Lesson: regenerate a prompt's "where we have looked" and known prints from the latest AUDIT section, and update the
NOTES novelty line in the same commit as a class change.

Requests: api.crossref.org 1 (Lodge; answer unreadable, not retried; Lodge was already in the log). No archive.org, no
Google Books, no Huntington, no logins, no subagents.

## Outreach gate 2: JSTOR family and open indexes (verifier V5, 24 Sept 2026)

Verifier V5 (Opus, for LANE V4, session_01UBQ2tN51FBuKTx41RqnGAK), 24 Sept 2026 17:24 UTC. Triage of the JSTOR runner's first-page hits (JSTOR-QUEUE.tsv) by title, snippet and what the runner read; no decoding, no class change unless stated.

6 rows (file lines 45-47, 57-59). The runner wrote no section for this target; triage here. Rows 57 and 59 no hits; row 46 three reference works. Context only: Webb 1969 (William Blathwayt to 1717), Goulding and Nelson (Dyrham Park cartography), McCully 1962, Altbauer 1980, Murray 1974, Durand (Laborde memoirs), directories and indexes. No review of HMC Polwarth vol. V on the first page; Storrs 2016 is not on JSTOR. No candidate.

JSTOR family: searched on the owner's machine 24 Sept 2026, 6 rows, 0 candidates read (none found), result clean. **Gate 2's JSTOR condition is met for BLA 186, 191(a) and 184.**

Open indexes: the owner ran this target's two queries on OpenAlex (API) and Semantic Scholar (site search) from their own machine on 24 Sept 2026 (ASKS row 34, `outreach/openalex-s2-owner-queries.md`): no relevant hit. V5's single cloud retry at about 17:21 UTC was 429 on both and is superseded. **Gate 2 is met for this target**: JSTOR family clean, open-index pass done, Google Books and the second adversarial audit done earlier (this file's earlier gate table left only the JSTOR rows and the open-index pass open). The outward draft carrying it is `status: ready` (for Thurloe P4, issue 2 of outreach/bourdeau-issues.md; for Eckert and Blathwayt, outreach/huntington-eckert-blathwayt.md).

Outward drafts written this session (status drafted, nothing sent): see `outreach/` and CONTRIBUTIONS.md.

## Open-index queries, cloud, 25 Sept 2026 (parent worker FOLLOWUP-2315)

ASKS.md row 40's open-index sub-item, re-run from the cloud with OPENALEX_KEY (Access playbook; the owner's earlier
24 Sept 2026 machine run and V5's cloud retry both got 429 on OpenAlex). No decoding; no class change.

| query | host | result |
|---|---|---|
| "Pareti Marchmont 1728" | OpenAlex (`works?search=`) | no relevant hit (0 results) |
| "Ripperda Segovia escape 1728" | OpenAlex (`works?search=`) | no relevant hit (2 results: a 2010 Ghent conference paper on international law in diplomatic practice, unrelated; a 2026 Open Book Publishers chapter "Chapter Six: 1725-1727" from an edition of Pietro Giannone's autobiography, an Italian historian's imprisonment, not Ripperda's Segovia escape) |

Requests: api.openalex.org 2, 1.5s apart, key sent as `Authorization: Bearer`, never printed. Semantic Scholar not
queried for this target (ASKS row 40 names OpenAlex only). JSTOR-QUEUE.tsv rows (file lines 45, 46, 47, 57, 58, 59)
stay with the ChatGPT/owner runner, per the brief.
