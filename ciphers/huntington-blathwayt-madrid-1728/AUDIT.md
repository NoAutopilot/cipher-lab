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
are new readings.

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
