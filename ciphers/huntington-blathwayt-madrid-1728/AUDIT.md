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
