# AUDIT: the fr.2980 f.29r reading (novelty class)

Verifier session, 24 September 2026, 00:50-01:20 UTC (`date -u` read; Opus, no subagents, started by the
orchestrator session_01SepNMpYrr6L2EwqL43aTnm). Audits NOTES.md, reading.txt, key.tsv and decode.py as of
commit 4493903. This session took no part in the check-solved, print-check or transcription passes. It did not
decode and does not protect the solver's conclusions. Classes are those of CLAUDE.md rule 10.

Claim under audit: "BnF fr.2980 f.29r (item 21), Cardinal Gabriel de Gramont, bishop of Tarbes, to Jean Breton
de Villandry, Rome, 20 May 1530: the cipher passage reads with Tomokiyo/Lasry's Gramont 1530 key, 569 signs,
H 538 / M 26 / U 5 (reading.txt, decode.py --check)." [Verifier V2, 24 Sept 2026: claim quoted as it stood; the leaf's
date line carries no year, so '20 May [1530]'; the current counts are 568, H 533 / M 30 / U 5.]

## 1. Verdict

| item | prior plaintext | prior decipherment of this item | class |
|---|---|---|---|
| BnF fr.2980 f.29r, no.21 (old shelfmark Anc. 8505), Gramont to Villandry, Rome, 20 May [1530], cipher passage of 568 signs (569 before the second reader) | **not located.** No printed text, extract, calendar entry or summary of the letter's content was found in the editions of section 4. The letter's *existence and date* are in print: the BnF *Catalogue des manuscrits français* (1868) describes it, and *Catalogue des actes de François Ier* IX (entry [411], list of ambassadors) cites "Écrit de Rome … 20 mai, ibid., 2980, fol. 29 et suiv." to date Gramont's stay in Rome. Neither gives any content. | **not located.** No decipherment was found on the leaf (NOTES.md, check-solved), in print or online. **But it has been identified as readable before us:** Tomokiyo (cryptiana, francis.htm, "BnF fr.2980 (1530)", live page re-read 24 Sept 2026) says "These undeciphered letters can be read with Gramont's cipher (1530)", and Bourdeau lists both items as catalogue 328, "Gramont 1530 key held" (dbourdeau/cyphersolver CATALOGUE.md line 76, sweep of 22 Sept 2026). Neither gives a reading. | **N3** |
| f.30r-v, no.22 (same date, entirely cipher) | not yet read by the solver | none located | **none assigned**: no reading exists to audit. The searches below cover it as well, so its prior-print status is the same as no.21's, but a class needs a reading. |

**Why N3 and not N4.** The principal editions for this embassy were covered (section 4), most of them by full
text. Four gaps keep it below N4. (1) Le Grand, *Preuves* (1688): read through the HTRC per-page token counts,
not page by page, because Google Books blocked the page and PDF routes (429 `/sorry/`). The counts are strong
evidence of absence, not a reading of the pages. (2) Camusat, *Meslanges historiques* (1619): only Google Books
API snippets could be checked. (3) HathiTrust full-text search (Cloudflare) and JSTOR (ASKS row 17) could not be
reached. (4) Michon's thesis *La Crosse et le Sceptre* and Wirtz-Daviau were not reached. If the owner runs the
JSTOR queries of section 4(g) and a second adversarial session closes (1) and (2), N4 is within reach. Outreach
gate 2 applies in any case: nothing above N1 goes outside the repo before that second audit.

**What the "H" means.** The 538 H tokens are signs whose *value* comes from the published table
(Tomokiyo/Lasry). The *identification of each sign* on the leaf rests on one reader. The two blind Sonnet passes
agreed on 29% of signs and decoded to nothing (reconciliation.md). About two lines (L10-L11) and parts of L02, L08,
L09 and L12 read as continuous French. The rest is letters not yet divided, and NOTES.md says some sign
identifications in L01, L03-L07 and L13 are probably wrong. So this is a **partial key-based reading from a
single transcription**. Grade H is correct under rule 4 for value-lookup, but the reading as a whole is not
"read" in the sense of a checked text. Evidence quality: medium for the key and the attribution, low-to-medium for
the sign-level transcription.

**Confidence in N3:** high that no printed plaintext exists in the English and papal series, in Pocock, Ehses,
Molini, Ribier, Scheurer's du Bellay or Decrue. Medium-high for Le Grand, whose token-count evidence is below.
Medium for Camusat.

**Safe sentence.** "BnF fr.2980 f.29r (no.21) is a letter of Gabriel de Gramont, bishop of Tarbes, to Jean Breton
de Villandry, Rome, 20 May [1530], with a 568-sign cipher passage (569 before the second reader). Tomokiyo had identified it as readable with
the published Gramont 1530 key (Tomokiyo; Lasry 2023). We transcribed the passage from the Gallica image (one
reader) and applied that key: the table gives values for 538 signs (H), 26 are uncertain and 5 unkeyed, and
several lines read as continuous French. No prior printed plaintext or decipherment of the letter was located in
the editions listed in AUDIT.md (N3)."

**Unsafe sentences.** "First decipherment of Cardinal Gramont's letter"; "a previously unread letter"; "newly
recovered"; "538 of 569 signs read", "533 of 568 signs read" or "read in full" (the reading is partial and single-reader); "Cardinal
Gramont" as of 20 May 1530 (he was created cardinal on 8 June 1530); "we found that the key applies" (Tomokiyo
said so first, and Bourdeau catalogued it).

*[Verifier note, f.30 audit, 24 Sept 2026: the counts above are the first reader's. After the second reader's
changes the passage is 568 signs, H 533 / M 30 / U 5 (NOTES.md, "Second reader: changes applied"; decode.py --check).
Use those in any safe sentence.]*

## 2. What the repo claims (extracted)

| field | value in the repo | source |
|---|---|---|
| shelfmark | BnF fr.2980 f.29 no.21 (Anc. 8505), Gallica ark:/12148/btv1b9059991d canvas f31 | NOTES.md, images/manifest.json, BnF notice cc494342 (re-fetched this session: "Ancienne cote : Anc. 8505") |
| sender, recipient | Gabriel de Gramont, bishop of Tarbes, to "monseigneur... de Villandry, conseiller du roy et secretaire de ses commandemens et finances" | BnF notice, verbatim |
| date, place | "A Rome, le XXme jour de may", no year on no.21; no.22 "M.D.XXX" | BnF notice |
| cipher, key | Gramont's Cipher (1530): Tomokiyo from fr.3019 f.20; Lasry 04/11/2023 from fr.3071 f.17 | key.tsv, NOTES.md |
| reading | reading.txt, 14 lines; distinctive decoded phrases: "il y baille a ce porteur ... article que j'ay mis a part"; "l'adresse de dessus a vous combien que ce soit au roy"; "vous prie le luy demander car c'est le total"; "du vingtiesme"; "pour le contenter et oster ... de suspecon"; "qui est cause que j'ay faict ledit article a part"; "pour vous donner cognoissance de tout"; clear text: "pensant que ce courrier pourra estre plustost a vous que le pacquet", "ung double des lettres que j'escriptz lundi", "satisfaction de nostre Sainct Pere" | reading.txt, NOTES.md |
| grades | 569 tokens: H 538, C 0, S 0, M 26, I 0, U 5 (first reader); now 568: H 533, M 30, U 5 (second reader, verifier V2 24 Sept 2026) | reading.txt header |
| solver's search | IA fts two phrases; Google Books API three queries; print-check pass (LP iv.3 direct, Decrue, PUR/Rentet, Tomokiyo, Bourrilly-Vindry vol.1, Google Books Le Grand bot-blocked) | NOTES.md |

## 3. The attribution tested against the plaintext

- **Recipient Villandry fits.** The cipher says the writer put an article apart and "faict l'adresse de dessus a
  vous, combien que ce soit au roy": he addressed it to the secretary although it is meant for the king. That is
  how one writes to the king's secretary of commands, Breton de Villandry, whose office was to carry such pieces
  to the king (Hamon, "Jean Breton", PUR chapter; author corrected by verifier V2, 24 Sept 2026). The clear text's "le pacquet que j'ay envoye au Roy" fits the same relay.
- **Rome fits.** The clear text mentions "la satisfaction de nostre Sainct Pere" and "les affaires du Roy par
  deca". The *Catalogue des actes* IX places Gramont in Rome from April to June 1530 (letters of 2 May, fr.3053
  f.11, and 20 May, this item). Spanish Calendar IV.1 p.560 cites him on 26 May, and LP iv.3 nos. 6441 and 6443
  (8-9 June 1530) have Mai congratulating "the cardinal of Tarbes on his promotion" in Rome.
- **Year 1530 fits, and the catalogue's title does not.** He signs "De Gramont E. de Tarbe" (bishop). He was
  created cardinal in the consistory of 8 June 1530 (LP iv.3 6441), so "cardinal" in the BnF notice and in the
  claim is the cataloguer's later title. The decoded "du vingtiesme" (L07) fits the date of 20 May. No.22's
  explicit M.D.XXX and the shared date support 1530 for no.21.
- **One internal point for the solver (grade I, not an attribution problem).** The draft clear text has a packet
  sent to the king "du xxi[?]e de ce moys". That cannot precede a letter of the 20th. 20 May 1530 (Julian) was a
  Friday, and the same sentence mentions letters written "lundi", i.e. Monday 16 May, so "xvi" is likelier. This
  note was added to NOTES.md for re-reading against the image.
- Nothing in the reading points to another sender, recipient or year. The Dupuy 468 failure (a wrong bracketed
  attribution narrowing the search) does not arise here: the notice has no brackets for these fields, and the
  search below was widened to the whole embassy (June 1529 to November 1530) and the later Rome missions
  (1531, 1532-33).

## 4. Search log (24 Sept 2026)

Hosts and counts are in section 6. "Searched" means the text itself was searched. "Snippet" means only
API snippets were checked.

(a) **Canonical series**
- *Letters and Papers Henry VIII* iv.3 (IA `11332111bsb`, full djvu.txt, 3.7 MB): grepped "Villandry"
  (2 hits: no.6245, 27 Feb 1530, Bologna; a 1530 mention of his return), "Tarb|Tarpe|Gramont", and "20 May". The
  20 May 1530 entries are nos.6394-6395 (Henry VIII to Dorigny; a silver assay). **No Gramont item of 20 May.**
  Searched. The *Addenda* vol. I (1929) was not found on IA (advancedsearch, 0 hits): **unreached**.
- *State Papers Henry VIII* vol. 7 (IA `statepaperspubli07grea`, full text): 0 "Villandry". The Tarbes/Gramont hits
  are English ambassadors' reports of 1530-33. Searched.
- *CSP Spanish* iv (IA `calendarofletter0004pasc`, `…_f5h4`, full text): 0 "Villandry". Searched. The
  *Catalogue des actes* cites iv.1 p.560 for Gramont on 26 May: that is Mai's report, not this letter.
- *CSP Venetian* iv, 1527-1533 (IA `calendarofstatep4187brow`, full text): 0 "Villandry". Searched.
- *CSP Milan*: not located on IA by title search. **Unreached** (and unlikely to hold a French secretary's letter).

(b) **Sender and recipient**
- **Le Grand, *Histoire du divorce* (1688), vols. I-III**, HathiTrust ids from the Bibliographic API (OCLC
  4941630): njp.32101037456710 (v.1), njp.32101037456702 (v.2), njp.32101037456694 (v.3, *Preuves*, 678
  scans). HTRC Extracted Features per-page token counts were downloaded for all three.
  - In v.3 "Villandry" occurs on 7 scans: 24 and 28 (1527-28 letters); 409 and 411 (printed pp.391-393, the
    Bologna 27 Feb 1530 letter, which LP 6245 also calendars); 491, 497 and 508 (pp.473-490, du Bellay's June 1530
    letters from Paris). "Tarbe(s)", "Gramont/Grammont" run from p.336 to p.457 (Bologna, Feb-Mar 1530; Ehses cites
    "III. 399" for 27 March and "III. 454"), then from p.511 (Aug 1530, "Aoust ... XXX") and pp.514-526 (Oct 1530
    and 1531). **No page carries Gramont or Tarbe together with a May 1530 Rome date.**
  - A per-page overlap of 28 words from the reading and the clear text (porteur, article, adresse, contenter,
    oster, suspecon, cognoissance, pacquet, courrier, plustost …, with long-s/f and u/v normalised) gives at most
    6 of 28 on any page. The best pages (seq 262, 475, 215, 183) are other letters.
  - v.1 (narrative): Grandmont with Rome on pp.~230-255, May on seq 232 and 238. This is the historian's narrative,
    and a paraphrase there cannot be excluded without reading those pages. **Gap, noted.**
  - v.2: Tarbes/Grammont hits only in the *Défense de Sanderus* and the *Réfutation*.
  - Google Books API (keyed, country=US): the *Preuves* volume `e1Z-8yywx6kC` is indexed and full view. A snippet
    for "Monsieur de Villandry" returns only the 27 Feb Bologna letter, which is headed "MSS. de Bethune" (the
    Béthune collection, the source of fr.2980). The API's signed PDF link and the page view both returned 429
    `/sorry/` (one attempt, then stopped).
  - **Result: not in Le Grand's *Preuves*** (token-count evidence, medium-high).
- **Decrue, *Anne de Montmorency*** (1885/1889): the print-check pass searched it and found no citation of items
  21-22. This session's IA fts for "Gramont" "Villandry" "1530" returned only the same volumes. Not re-searched.
- **Hamon** (not Rentet; corrected by verifier V2, 24 Sept 2026), "Jean Breton (v. 1490-1542)", in Michon (ed.), *Les conseillers de François Ier* (PUR 2011), pp.335-342 (pur/120024): read by the print-check pass. This session read the
  **PUR chapter on Gabriel de Gramont** (books.openedition.org/pur/120012, full text): the 1530 Rome mission is
  cited only to the Ferrarese ambassador (ASModena busta 9) and CAF; no fr.2980, no cipher. Searched.
- **du Bellay correspondence**: Bourrilly & Vindry vol. 1 (1527-29) is out of range (print-check). Scheurer,
  *Correspondance du cardinal Jean du Bellay* I (1969, IA `correspondancedu0000remy`, lending; fts within the
  item): "2980" 0 hits; "20 mai 1530" 0; "Gramont Breton" gives one note, a Gramont letter "citée par Breton à
  Montmorency le 20 mars" (not ours). Searched (fts only).
- **Camusat, *Meslanges historiques*** (1619; Google Books `MKpSAAAAcAAJ`, `1d19ZkCU0v8C`; not on IA): snippets
  for Gramont, Villandry and "Evesque de Tarbe". The hits are 1532-33 letters (Tournon and Gramont; Lazare de Baïf
  to the bishop of Auxerre). **Snippet only.**
- **Ribier, *Lettres et mémoires d'estat*** (1666; IA `bub_gb_Tbs9UbObcPUC`, `bub_gb_bOnmNv2ZLVoC`,
  `bub_gb_qWTswSr32NYC`, full text): "Villandry" 1-3 hits each, all later (benefices; "Agent à Rome", 1540s);
  "1530" 1 unrelated. Ribier does print another leaf of this volume, fr.2980 f.55 (I p.561, per Bourrilly,
  *Guillaume du Bellay* 1904), which shows the volume was used by editors. **Not items 21-22.** Searched.
- **Champollion-Figeac, *Captivité du roi François Ier*** (1847): not found on IA or through the Google Books API
  (0 hits for Gramont/Tarbes/Villandry). **Unreached.**

(c) **Documentary editions**
- **Pocock, *Records of the Reformation*** (1870), both volumes (IA `recordsreformat02pocogoog` = vol. 1, heavy on
  1527-30; `recordsofreforma02pocouoft` = vol. 2): 0 "Villandry". The Tarbe hits are English despatches. Searched.
- **Ehses, *Römische Dokumente*** (1893, IA `romischedokument00ehse`): 0 "Villandry". Gramont appears through papal
  documents and references to Le Grand III.399 and III.454 (Bologna, March 1530). Searched.
- **Molini, *Documenti di storia italiana*** (1836-37, IA `documentidistor00-03moligoog`, both volumes, two
  scans each). Vol. 1 is a register of Béthune volumes by old number. Its entry for 8505 (= fr.2980) lists only
  Italian-language items (c.52, 61, 70-76). Vol. 2 prints only item 23 of 8505 ("Libr. R. MSS. Vol. N.° 8505 a
  c. 31", the 1526 truce). Molini lists Raince to Villandry, Rome, 11 May 1530, and several Gramont cipher letters
  in other volumes (27 Aug; 11 Oct). **Not items 21-22.** Searched.
- **Nuntiaturberichte**: the German series begins in 1533, and no French nunciature edition covers 1530.
  **Not applicable**, not searched.
- ***Catalogue des actes de François Ier* IX** (IA `collectiondesord09acad`, full text): entry [412] [verifier V2, 24 Sept 2026: [412], not [411]; [411] is Villebon's 1528 mission; Catalogue IX p.61] cites the
  letter by date, as in section 1. **Existence and date only.**
- **Tournon correspondence** (M. François, 1946, Google Books snippets): cites fr.2980 fol.33 (no.24, Lyon), not
  fol.29-30.

(d) **Holding archive**
- BnF notice `archivesetmanuscrits.bnf.fr/ark:/12148/cc494342`, re-fetched: Anc. 8505; items 21-22 described;
  no bibliography, no "déchiffré" and no edition cited. Microfilm MF 8140.
- Clairambault 312-452 finding aid (the 17th-century copies of Béthune pieces): the part that loaded (2,152 folio
  entries) lists no copy of fr.2980 ff.29-30. It has one leaf removed from fr.2980 (anc. fol.14, a Doge's letter),
  no 1530 Gramont entry, and no decipherment copy. Partial.
- Gallica/BnF blog: web search (below) found no page on this letter. No Gallica image or text service was
  used (another worker is fetching images).

(e) **Phrase search on the decoded text** (u/v, i/j and spacing normalised; accented and unaccented forms)
- IA full text (be-api fts, all items): "baille a ce porteur" 42 hits, all other letters (Gobat, Mazarin's
  *Lettres*, Foix). The following gave 0 hits: "adresse de dessus a vous", "combien que ce soit au roy", "pour le
  contenter et oster", "ledit article a part", "ledict article a part", "article que j ay mis a part", "faict
  ledit article", "car c est le total", "pensant que ce courrier", "le pacquet que j ay envoye au roy", "oster
  toute suspecon", "la depesche dudit porteur" and "satisfaction de nostre sainct pere". "donner cognoissance de
  tout" gave 2 hits and "oster toute souspecon" 10, all unrelated. "ung double des lettres que" gave 3 hits
  (Charles V; Catherine de Médicis), unrelated.
- Google Books API (keyed): "pour le contenter et oster", "faict ledit article a part", "l adresse de dessus a
  vous", "combien que ce soit au roy", "baille a ce porteur" Tarbe, "Gramont" "Villandry" "20 mai 1530", "Tarbes"
  "Villandry" "mai 1530", "fr. 2980, fol. 29", "fr. 2980, fol. 30" and "français 2980" Gramont: 0 relevant.
- IA fts "2980, fol. 29" found the *Catalogue des actes* entry above. "fr. 2980" Gramont found Decrue and
  Bourrilly's *Guillaume du Bellay* (fr.2980 f.31, f.55), not items 21-22.
- HathiTrust full-text search: Cloudflare-blocked per CLAUDE.md, not attempted. EF token counts were used for
  Le Grand instead. **Unreachable.**

(f) **Solver repositories and cipher pages**
- dbourdeau/cyphersolver, fresh shallow clone, head 763a3b9 (23 Sept 2026 12:30 -05:00). Grep for 2980,
  btv1b9059991d, Villandry, Tarbe and 8505 finds **CATALOGUE.md line 76, catalogue 328**, "Gramont to Villandry,
  Rome (BnF fr. 2980 nos. 21–22, ff. 29–30): Gramont 1530 key held (gramont1529)", in the 22 Sept sweep of
  letters "a key already in hand reads", and `gallica_sweep/bnf_candidates.txt` line 302. gramont1529/ reads
  fr.3071 no.7, not fr.2980. **Catalogued, not read.** This contradicts the check-solved note, which is now
  corrected.
- aaymeloglu/unsolved-ciphers, fresh shallow clone: 0 hits for 2980, Gramont, Villandry or Tarbe.
- Tomokiyo, francis.htm, fetched live 24 Sept 2026 (1 request; same text as the 23 Sept mirror): "These
  undeciphered letters can be read with Gramont's cipher (1530) below." No transcription or plaintext. GL.htm
  (mirror): no mention of fr.2980.
- Lasry: web search "Lasry Cryptologia French diplomatic ciphers Francis I Gramont 1530" found nothing on
  fr.2980 (Mary Stuart, Maximilian II, papal ciphers). His Gramont work is known through Tomokiyo's pages. His
  own "Codebreaking" pages were not fetched this session (Tomokiyo's GL.htm mirrors their listings).
- DECODE: login rejected (ASKS row 1); cached catalogue empty. **Unreachable.**

(g) **Scholarship**
- Web searches: "Gabriel de Gramont évêque de Tarbes ambassade Rome 1530 thèse correspondance"; "Gramont"
  "Villandry" 1530 "lettre chiffrée" Rome "20 mai". Results: Wikipedia, catholic-hierarchy, BnF notices
  (Clairambault, fr.3045) and the PUR chapter (searched above). Nothing on this letter.
- Not reached: Cédric Michon, *La Crosse et le Sceptre* (thesis; Tallandier 2008); Wirtz-Daviau on the 1529-30
  embassy (flagged in Bourdeau's notes; not located); Le Glay, *Négociations diplomatiques entre la France et
  l'Autriche* (the Margaret of Austria period, off-target).
- **JSTOR queries for the owner** (JSTOR is challenge-blocked, ASKS row 17): `"Gramont" AND "Villandry"`;
  `"évêque de Tarbes" AND 1530 AND chiffre`; `"fr. 2980"`; `"Gabriel de Gramont" AND (Rome OR Clement) AND 1530`;
  `"Gramont's cipher"`; `Lasry AND (Gramont OR "Francis I")` in Cryptologia 2022-2026. Log article and date in
  this file.

## 5. Postmortem

**Failure named: an incomplete repository grep reported as a negative.** The check-solved pass wrote "fr.2980
does not appear anywhere in his [Bourdeau's] repository" and "the only two projects that read letters in this key
... explicitly did not include this manuscript". Bourdeau's CATALOGUE.md lists both items as catalogue 328 with
the key marked "held". Nobody has published a reading, so the class is unaffected. The error matters for
outreach, though. A message to Bourdeau that did not mention his catalogue 328 would look careless, and the
fair credit line is "identified as readable by Tomokiyo, catalogued by Bourdeau (328), read here". Lesson: grep a
solver repository's catalogue and sweep files, not only its target folders, and quote the hit.

**Corrections made in NOTES.md** (each marked "Verifier correction, 24 Sept 2026"):
1. Title: "Cardinal Gabriel de Gramont" became "Gabriel de Gramont, bishop of Tarbes (cardinal from 8 June 1530)".
2. Check-solved, Bourdeau bullet: the "does not appear anywhere" sentence now carries the correction and the
   CATALOGUE.md citation.
3. Check-solved verdict: "explicitly did not include" became "have not read", with the correction.
4. "the cheapest kind of unique solve: a known key, an unread ciphertext" became "a key-based reading ... for
   which no prior reading has been located" (rule 10).
5. Print-check, Decrue bullet: "consistent with ... them being unread ciphertext in his day" became "his not
   having read them" (rule 10).
6. Transcription section, clear text: "du xxi[?]e" now carries a grade-I note that the date is impossible and
   "xvi" (Monday 16 May) is likelier. The reading itself is not changed.

**Not corrected here (outside this folder, for the orchestrator):** QUEUE.md row M8 calls him "cardinal", which
is anachronistic for 20 May 1530. The orchestrator's claim sentence ("Cardinal Gabriel de Gramont") has the same
problem. Any status or board line should use the safe sentence above and state that the reading is partial and
single-reader.

## 6. Requests this session

archive.org (advancedsearch, metadata, download, be-api fts): about 75, 1.6 s apart. data.htrc.illinois.edu: 4.
catalog.hathitrust.org Bibliographic API: 2. www.googleapis.com (Books, keyed, country=US): about 45, 1.6 s apart.
books.google.com: 1 (429 `/sorry/`, stopped). gallica.bnf.fr: 2 SRU catalogue queries, no images.
archivesetmanuscrits.bnf.fr: 3 (fr.2980 notice, Clairambault 312-452 twice). books.openedition.org: 1.
cryptiana.web.fc2.com: 2 (a 302 redirect, then 200). www.digitale-sammlungen.de: 1 (JavaScript page, unused).
github.com: 2 shallow clones. WebSearch: 3. No logins, no credentials printed, no decoding, and reading.txt,
key.tsv and ciphertext.txt untouched.

## Second audit (adversarial)

Separate verifier session (session_012r7Td2JUq7nX5UmkAJXLCd, Opus, no subagents), 24 September 2026,
01:19-01:55 UTC (`date -u` read), started by the orchestrator session_01SepNMpYrr6L2EwqL43aTnm. Audits the N3 above
(commit 22c282a). Brief: try to find item 21 in print and prove N3 wrong. No decoding. reading.txt, key.tsv,
ciphertext.txt and the f.30 work were not touched.

### Verdict

**N3 confirmed. Not moved.** No printed plaintext, extract or decipherment of fr.2980 f.29r (no.21) was found.
Two of the first audit's four gaps are now closed or narrowed: Le Grand's *Preuves* was read page by page, and
the same-volume and same-series decipherment test was run. Two gaps remain open: Camusat is still snippet-only,
and HathiTrust full text, JSTOR and Michon are still unreached. For that reason the class is **not raised to N4**.
Gate 2 of the Outreach rule is now met in its first half (a second adversarial audit ran and failed to find the
item in print). The credential session's JSTOR and Google Books queries are still owed (ASKS row 17).

**Safe sentence** (unchanged from section 1, one addition): "... No prior printed plaintext or decipherment of the
letter was located in the editions listed in AUDIT.md, including a page-by-page reading of Le Grand's *Preuves*
for February-October 1530 (N3, confirmed by a second adversarial audit)."

### The Raince test: is there a contemporary decipherment in the same volume or series?

This is the test that sank the Raince letter tonight (Jacqueton 1892, printed from a decipherment bound later in
the same Dupuy volume).
- **fr.2980 itself** (BnF notice cc494342, re-fetched in full, 46+ items): the words "déchiffr-" and "chiffre"
  occur only in the entries for nos.21 and 22. No. 23 (f.31) is a copy of the 1526 truce, and no. 24 (f.33) is
  Tournon and Gramont from Lyon. The volume holds no decipherment, copy or unattributed piece that could be
  a decipherment of nos.21-22. **Searched.**
- **The whole BnF manuscript finding aids** (archivesetmanuscrits.bnf.fr full-text search, via the browser
  because the result list is loaded by JavaScript). Queries: "Gramont Tarbe chiffre" (5 hits), "Tarbe
  Villandry" (3), "Tarbe déchiffrement" (2), "Granmont" (2), "Grantmont Tarbe" (0), "Gramont déchiffré" (0),
  "Déchiffrement Rome may" (20, all 1586-1626 Béthune-embassy items), "Déchiffrement lettre Rome 1530" (1: Dupuy
  264), "Gramont Tarbe Rome" (5) and "evesque de Tarbe" (41 hits across the French, Dupuy, Colbert and NAF series).
  **Result:** the only contemporary decipherment of a Gramont letter in the catalogues is **fr.3038 no.19,
  "Déchiffrement de la lettre de G. de Granmont, evesque de Tarbe ... à monseigneur de Villandry ... A
  Boulongne, le XXVIIe jour de febvrier"**. That is the Bologna letter of 27 Feb 1530, calendared at LP iv.3 6245
  and printed by Le Grand III pp.391-393. It shows that Villandry's Gramont ciphers *were* deciphered and filed
  in the Béthune series, and that the one decipherment that survives was printed. **None is catalogued for the
  20 May letter.** The copies "Coppie de la lettre ... à monseigneur l'admiral" (fr.3053 no.12, 25 Feb; fr.3083
  no.7, 19 Feb) and fr.3003 no.5 (to the king, 27 Feb) are all from Bologna. Dupuy 264 (the "Déchiffrement … 1530"
  hit) holds a 1522 Clermont decipherment and 1534-40 Rome letters, and no Gramont piece. Dupuy 495 holds the
  1527 Tarbes instructions only. **Searched.**
- **Same-series Gramont letters of May 1530 in clear:** fr.3019 no.31, Gramont to the grand maître, "A Rome, le
  XVe jour de may". This is a companion letter five days earlier, in clear by its description. It was not
  opened here: it is a Gallica image, and another worker holds the host. It is worth a look by whoever reads
  f.29r next, as context for the cipher passage. It is not a decipherment.
- **Limit:** a decipherment catalogued without Gramont's name (as the Raince decipherment was, "[par le meme?],
  s.d.") would only surface through a volume-by-volume read of the Béthune recueils, which was not done here. The
  searches above cover the words "déchiffrement", "Tarbe" and "Villandry" wherever the cataloguer used them.

### Gap (1) closed: Le Grand, *Histoire du divorce* III (*Preuves*, 1688), page by page

Route: the MDZ (Munich) scan **bsb10280117**, OCR per page from `api.digitale-sammlungen.de/ocr/bsb10280117/<scan>`.
The route was found in Bourdeau's `dubellay/ref/legrand3_p330_400.txt`, which uses the same scan. Scans 400-548
= printed pp.394-542 were fetched (149 requests, all 200) and read by script: every heading and dateline, then
the phrase list below.
- Sequence of datelines: pp.394-411, Gramont decipherments and Bologna letters (Feb-Mar 1530; p.394 is headed
  "Dechiffrement des Lettres de Monsieur de Tarbe", Béthune vol. 866); pp.408-452, Jean-Joachim de Vaux (London,
  including "May 1530" at p.420, the only May 1530 dateline in the stretch), du Bellay and Langey (Paris,
  Feb-Mar), Italian pieces and the papal inhibition; **pp.454-457, Gramont to Montmorency, "De Boulongne le 23.
  Mars" and "A Boulongne ce 28. jour de Mars"** (Béthune vol. 8565); pp.458-508, du Bellay to Montmorency and the
  king, Paris, June-August 1530, with Norfolk and Lizet; pp.508-509, the Angers determination; **pp.509-527,
  Raince's letters from Rome beginning "De Rome le xx. d'octobre M.D.XXX"**, then December 1530 and February,
  April and May **1531** (the weekdays "Jeudy quatriesme de May", "Mercredy dixiesme ... de May" fit 1531 Julian,
  not 1530); pp.527-542, Vaux (Italian), the papal inhibition and Casali.
- **There is no letter from Rome dated between 28 March and 20 October 1530**, and no Gramont letter after
  28 March 1530 in this range. The *Preuves* go straight from Bologna to Paris.
- Phrase search on the same OCR, normalised u/v, i/j/y, long-s and f/s. The control phrase "entretenir
  Monsieur de Rochefort" was found at p.454, as it should be. Phrases searched: "adresse de dessus", "combien
  que ce soit au roy", "article a part", "c'est le total", "contenter et oster", "donner cognoissance",
  "cognoissance de tout", "monstre tout", "a ce porteur", "mis a part", "satisfaction de nostre sainct pere",
  "pensant que ce courrier", "double des lettres", "suspecon"/"souspecon", "ledict porteur", "vingtiesme". **0 hits**,
  apart from the generic "pacquet" in du Bellay's Paris letters (pp.479, 490, 505).
- Le Grand v.1 (narrative; HTRC EF for njp.32101037456710): the Grandmont pages (scans 220-255) are the
  1531-33 narrative (Albany, Carne the excusator, Tournon). None carries the reading's vocabulary (porteur,
  adresse, article, suspecon, pacquet, courrier, cognoissance, total). **Closed at token level.**
- HTRC EF re-run for v.3 (njp.32101037456694) agrees with the MDZ reading: Grandmont+Rome+May pages sit at EF
  seq 529-546 = the 1531 Raince run above.
- Not read: *Preuves* pp.1-393 (1527 to Feb 1530), because they predate the letter. The first audit's
  whole-volume EF overlap test (at most 6 of 28 words on any page) covers them.

### Gap (2) still open: Camusat, *Meslanges historiques* (1619)

Not closed. Google Books page view is blocked (books.google.com answered 403 `/sorry/` to one request; host
stopped). The MDZ copy found by web search (bsb10209014) is Saint-Julien's 1589 *Meslanges historiques*, not
Camusat. A full-text Gallica copy exists at **ark:/12148/bpt6k5039434** (texteImage). It was not used because
the f.30 transcription worker held gallica.bnf.fr throughout this session (good-citizen rule: one worker per
host). **Next step, one request:** Gallica ContentSearch or `texteBrut` on bpt6k5039434 for "Villandry",
"Tarbe" and "1530". The first audit's snippets place Camusat's Gramont material in 1532-33 (Tournon and Gramont).

### Gaps (3) and (4) still open

HathiTrust full-text search: not attempted (Cloudflare). JSTOR: ASKS row 17. Michon, *La Crosse et le Sceptre*:
not reached. The Google Books API finds it only as cited in *Les conseillers de François Ier* (2011, snippet on
Gramont's diplomatic career from 1525), with no May 1530 text. Wirtz-Daviau: the API finds only her membership
listing (Soc. des antiquaires de l'Ouest, 1967) and bibliography entries, with no text. **Unreached.**

### Other families searched this session

(c) **Documentary editions and monographs not in the first audit:**
- Mignet, *Rivalité de François Ier et de Charles-Quint* (IA `rivalitdefranois01mign`, `…02mign`, fts per item):
  "Tarbes" 1 hit (1527-29 negotiations), "Grammont" 0, "Villandry 1530" 0. The work ends with Cambrai, 1529.
  **Searched.**
- Jacqueton, *La politique extérieure de Louise de Savoie* (1892, `lapolitiqueext00jacquoft`): "Tarbes" 1 hit,
  from 1525-26; "Villandry 1530" 0. It stops in 1526, and no sequel covering 1530 was found. **Searched, out of range.**
- Bourrilly, *Guillaume du Bellay* (1905, `guillaumedubella00bouruoft`): "Tarbe" 0. "Villandry 1530" gives only
  the du Bellay–Montmorency letters of January-March 1530 (fr.3079). **Searched.**
- Champollion-Figeac, *Documents historiques inédits* (IA `documentshistori03cham`, `…04cham`,
  `bub_gb_DLQKAQAAIAAJ`, `documentshistor06unkngoog`, `documentshistor00jacgoog`, `bub_gb_LsJnAAAAMAAJ`):
  "Tarbe" 1 unrelated hit (Franciscans of Tarbes); "Villandry 1530" 0. *Captivité du roi François Ier* (1847) is
  not on IA by title (its range is 1525-26). **Searched / Captivité unreached.**
- Friedmann, *Anne Boleyn* (IA `anneboleyn0000frie` and reprints, via the all-items fts): cites J. Breton de
  Villandry to Montmorency, 6 May 1530, fr.3079 f.45, which is not our letter. No fr.2980. **Snippet.**
- Hamy, *Entrevue de François Ier avec Henry VIII à Boulogne* (1898; Google Books `w7qXln-2ToAC`, API only):
  prints Gramont letters of 1532. "Villandry", "20 mai 1530" and "Tarbe may 1530" limited to the work gave 0.
  **Snippet only.**
- *English Foreign Policy 1528-1534: the Diplomacy of the Divorce* (1967 thesis, IA
  `bim_early-english-books-1641-1700_theodora-pierdos-bo_1967_ia40331301-07`): "2980", "Villandry", "May 20,
  1530" and "20 May 1530" all 0. **Searched.**
- Scheurer, *Correspondance du cardinal Jean du Bellay* vol. 2 (`correspondancedu0002remy`): 1535-36, out of
  range (surfaced by the fts).
(d) **Citation forms** (IA fts, all items): "2980, fol. 29" gives only the *Catalogue des actes* IX entry (three
scans) and false hits (Vienna, Lambeth). "2980, f. 29", "2980, fo 29" and "fr. 2980, fol. 30" gave 0 relevant.
Google Books API "fr. 2980" Gramont gives Decrue (other items) and Tournon's correspondence (fol.33). **Searched.**
(e) **Phrase search** on the decoded text (L02-L04, L08-L12), none tried by the first audit, u/v i/j normalised:
- IA fts: "luy ay monstre tout" 0; "lui ay montré tout" 0; "est cause que j ay faict" 0; "est cause que j ai
  fait ledit article" 0; "le luy demander car" 3 (Peiresc, Leibniz, 1865 grammar: unrelated); "car c est le
  total" 0; "le contenter et oster" / "ôter" 0; "donner cognoissance de tout" 2 (unrelated); "ledict seigneur et
  tous aultres" 6 (1559 quittance formula, unrelated); "j ay faict l adresse" 0; "l adresse de dessus" 0; "ledit
  article a part" 0.
- Google Books API (keyed, country=US): "luy ay monstre tout" 0; "le contenter et oster" 0; "car c'est le total"
  / "c'est le total" Tarbe 0 relevant; "combien que ce soit au roy" 0; "l'adresse de dessus a vous" 0; "ay mis a
  part" Tarbe 0; "est cause que j'ay faict" 3 (Thuanus, Bellièvre, Beaufort: unrelated); "donner cognoissance de
  tout" Tarbe 0; "Tarbe" "Villandry" "XXme jour de may" 1 (the 1868 BnF catalogue itself); "Gabriel de Gramont"
  Villandry chiffre 1530 0; "Gramont's cipher" 0.
(f) **Solver repositories**, fresh shallow clones:
- dbourdeau/cyphersolver, head **5dcd5c3** (23 Sept 2026 20:24 -05:00, newer than the first audit's 763a3b9).
  fr.2980 appears only at `CATALOGUE.md` line 76 (catalogue 328, "Gramont 1530 key held (gramont1529)") and
  `gallica_sweep/bnf_candidates.txt` lines 303-304 (the BnF catalogue entries, copied). `gramont1529/` reads
  fr.3091 no.23 (11 Oct 1529) and fr.3071 no.7 (21 July 1530). There is no file, transcription or reading for
  fr.2980. `rangone1530/NOTES.md` line 68 cites fr.2980 **no.44** (Trivulzio memo), not ours. **Catalogued, not
  read**, as the first audit said, and still so at the newer head. His `dubellay/ref/legrand3_p330_400.txt`
  (Le Grand pp.330-400) supplied the MDZ route above.
- aaymeloglu/unsolved-ciphers, head 2495c45 (23 Sept 2026): "2980" only as DECODE record id R2980 (BL Add MS
  32305, 1758); 0 hits for Villandry, Gramont or Tarbe outside unrelated rows. **Searched.**

### Corrections made (this session)

1. NOTES.md, print-check "General WebSearch" bullet: it said "created cardinal 9 March 1530, promoted 8 June 1530
   — so as of 20 May 1530 he already held the cardinal's hat". That is an over-claim and contradicts section 3
   above and LP iv.3 6441-6443 (Mai congratulating him "on his promotion", 8-9 June). The note is corrected: he
   was created cardinal in the consistory of 8 June 1530; a March reservation is not established by the sources
   read, and he signs as bishop.
2. NOTES.md, print-check Le Grand bullet: its "Gap" sentence now carries a pointer to this section (closed by
   the MDZ page-by-page reading).
No other over-claiming wording was found in the folder (grep for new/newly/first/unread/unpublished/never
printed/previously: all hits are rule-10 reminders, catalogue quotations or transcription vocabulary).

### Postmortem

The first audit's N3 holds. Its one weakness was method: token counts stood in for page reading because Google
Books blocked the page route. A page-level OCR copy of the same *Preuves* volume was sitting in a solver
repository that the first audit had cloned and grepped, but only for fr.2980. Lesson: when a principal edition is
blocked on one host, grep both solver repositories for the edition's *title* and scan id (here "legrand",
"bsb10280117") as well as for the target, and look for the MDZ copy before settling for counts.

### Requests this session

archivesetmanuscrits.bnf.fr: about 22 (4 notices by curl; about 18 search sessions through headless Chromium, each
a page load plus its result call, about 3 s apart). api.digitale-sammlungen.de: 150 (149 OCR pages, 1.6 s apart,
all 200; 1 manifest). data.htrc.illinois.edu: 2. archive.org (advancedsearch and be-api fts):
about 45, 1.6 s apart. www.googleapis.com (Books, keyed, country=US, key never printed): 23. books.google.com: 1
(403 `/sorry/`, host stopped). www.google.com: 1 (Books feed, 200, unused). github.com: 2 shallow clones.
WebSearch: 3. gallica.bnf.fr: 0. No logins, no credentials printed, no decoding, no subagents.

## Toward N4 (24 Sept 2026)

Verifier follow-up session (Sonnet, cap $8, orchestrator session_01EFmUvFAifLKGdBSsW9mjEG), 24 September 2026,
02:04-02:20 UTC (`date -u` read). Brief: close as many of the second audit's four remaining gaps as reachable —
Camusat, HathiTrust full-text search, the rate-limited Google Books queries, and the fr.3019 no.31 companion
letter. Not a solver session: reading.txt, key.tsv and ciphertext.txt were not touched. Reports what was found
and where it was not; does not move the class.

**Gap (2), Camusat — still not closed.** Three routes tried on `bpt6k5039434`, one worker's worth of traffic on
`gallica.bnf.fr` this session (other workers were concurrently using the same host for f.30/fr.16092/fr.4687
work per ROOM.md, which likely explains some of the resets below; not all failures here are Camusat-specific):
- `.texteBrut` (full-book OCR download): HTTP 302 to `/services/engine/search/altcha?...`, i.e. Gallica's own
  bot-verification interstitial ("Vérification de sécurité"), not a network failure. **Stop and log on altcha**,
  per brief — not retried.
- `/services/ContentSearch?ark=...&query=Villandry`: connection reset twice (`Recv failure: Connection reset by
  peer`), the second after a 5 s pause per the single-retry rule. Not retried further.
- IIIF `manifest.json` for the same ark: fetched cleanly (200, 875 KB) on the first attempt, but the manifest
  carries no OCR/ALTO text service or `rendering` link (`seeAlso` is only the OAI-DC metadata record) — Gallica's
  IIIF Presentation API does not expose page text for this item; there is no "OCR via the IIIF/document API"
  route to fall back to here, contrary to what the brief supposed. The full text exists only behind `.texteBrut`
  / `ContentSearch`, both blocked above.
- **Net: Camusat's content for 1530-1533 remains unverified beyond the first audit's Google Books snippets**
  (Gramont material there dated 1532-33). Not closed. Next attempt should hold `gallica.bnf.fr` alone (no other
  worker concurrent) and retry `.texteBrut` once cold, since an altcha challenge can be session/traffic-dependent
  rather than a permanent block.

**Gap (3), HathiTrust full-text search — still unreachable, as documented.** One attempt via
`tools/browser_fetch.js` at `babel.hathitrust.org/cgi/ls?...;a=srchls;lmt=ft` timed out (60 s) after the egress
proxy reported `brunhild.challenges.cloudflare.com:443 — connect_rejected (organization policy)` — the Cloudflare
challenge itself, not a transient error. Direct curl to `babel.hathitrust.org` and `catalog.hathitrust.org` both
403. This matches CLAUDE.md's existing note that HathiTrust Cloudflare-challenges this environment. The HTRC
Extracted-Features token-count route (`data.htrc.illinois.edu`, reachable, 200) is a substitute only for
volumes already identified by id (used for Le Grand in the first/second audit); it is not a general full-text
search and cannot substitute for one across all of HathiTrust. **Not closed; no new route found.**

**Gap (4), fr.3019 no.31 — located precisely, not read.** The BnF finding aid for fr.3019 (ark `cc49477m`, found
via the manuscript's own IIIF manifest `Relation` field, not previously in this file) lists item 31 verbatim:
"Lettre de « G[ABRIEL] DE GRAMONT, evesque de Tarbe... à monseigneur le grant maistre... A Rome, le XVe jour de
may ». Fol. 86." Gallica ark `btv1b9059994n` (290 canvases; also cited in `sources/cryptiana/web/venetian.htm`
for a different folio of the same volume). Two facts fix its relation to our target before any reading: **it is
addressed to the grand maître (Montmorency), not to Villandry** — a different recipient from f.29r/f.30 — and
**the finding-aid entry carries no "avec chiffre"/"en chiffre" flag**, unlike items 21-22 of fr.2980, consistent
with the second audit's "in clear by its description." Both reduce, without excluding, the chance of verbatim
phrase overlap. The folio itself was not read this session: canvas-to-folio correspondence for this manuscript
is not the fr.2980 pattern (double-page-per-canvas, offset +2) and was not established in budget — canvas f86
shows an unrelated military-campaign passage (chevaux légiers, artillerie) with a faint corner numeral read as
"84", canvas f87 shows a mostly blank verso with a small pasted salutation fragment ("Monsi[eu]r, mon..."), and
canvas f88 shows a blank leaf with a corner numeral read as "88" or possibly "86" (the pencil digit style is
ambiguous at this resolution) — the three probes did not converge on a folio reading "86" with Gramont/Rome/May
content. **Left open for a dedicated calibration pass** (three IIIF image fetches spent on this, all 200; no
further probing attempted under this session's cap). Recorded here so the next worker does not repeat the
finding-aid lookup.

**Google Books, re-run keyed (`&key=$GOOGLE_BOOKS_KEY&country=US`, key never printed).** The 429/403 `/sorry/`
failures logged earlier in this file are all on `books.google.com` (the inside-book page-view and PDF routes),
not on the `www.googleapis.com/books/v1/volumes` API itself — the API calls in section 4(e) were already keyed
and their zero-hit results stand; the key does not reach the page-view route, which is a separate
bot-challenge and was not re-attempted (a single attempt was already logged; the good-citizen rule caps retries,
not further attempts on an already-identified block).
- **Champollion-Figeac, *Captivité du roi François Ier* (1847)**: now located precisely — `DR5h-3UB_bQC`
  (Rutgers scan, `viewability: ALL_PAGES`, `publicDomain: true`) — but `readingModes.text` is `false`: this is an
  image-only scan with no OCR text layer in Google's own metadata, so no true within-book phrase search is
  possible via the API regardless of key. Three `intitle`-restricted content queries (Villandry; Gramont
  Villandry; Tarbe) returned 0 hits each, but this is a title-metadata filter, not a within-book search (same
  caveat the first audit already noted for Le Grand), and is weak evidence given the missing text layer.
  **Located but still not full-text-searchable; status changes from "unreached" to "found, unreadable via API."
  Closed below by a page-image read of the Gallica scan's own "Table générale" (24 Sept 2026): this gap no
  longer needs closing, because the whole volume is now confirmed out of scope for a 1530 letter.**

## Print check through Gallica page images, 24 Sept 2026

Worker session (Sonnet, cap $10, orchestrator session_014zWyan51u9qMn9gnHpm1Aq), 03:59-04:20 UTC (`date -u`
read at start and end). Not a verifier session: does not move the N3 class, does not decode. Brief: read
Champollion-Figeac's *Captivité du roi François Ier* (1847, Gallica ark `bpt6k204021j`) and Camusat's
*Meslanges historiques* (ark `bpt6k5039434`, per the "Toward N4" sections above) against reading.txt/
reading_f30*.txt's decoded phrases, using IIIF page images only (`.texteBrut`/`ContentSearch` are altcha-
blocked per CLAUDE.md and were not attempted). Full file list and per-image notes in
`images/print_check/manifest.json`.

**Champollion-Figeac — closed, definitively out of scope.** `tools/gallica_folio.py --list` shows the volume's
roman-numeral front matter runs to page LXXVIII (canvas f74), then arabic pagination 1-659 (canvas f76 =
page 1) to the last canvas (f746). The final canvas is not blank: it is the volume's own **"TABLE GÉNÉRALE"**,
which gives the whole book's scope in the author's own words: Introduction (pp. VII-LXX); **Première section,
Guerre du Milanais (Octobre 1524 — février 1525), p. 1; Deuxième section, Captivité en Italie (25 février —
22 juin 1525), p. 129; Troisième section, Captivité en Espagne (22 juin — 31 décembre 1525), p. 231;
Quatrième section, Délivrance de François Ier (Janvier — avril 1526), p. 458**; then the general document
table (p. 569), the Appendice table (p. 618), and two alphabetical tables. Page 1 itself opens "Première
section... (Octobre 1524. — 25 février 1525.)", matching the table exactly. **The entire volume's documents
run from October 1524 to April 1526 — the King's captivity itself, ending at his release** — and cannot
contain a letter of 20 May 1530, four years after the volume's own closing date. This is a stronger and
cheaper result than the previous "not found on IA or through the Google Books API": it is not a search
failure but a proof, from the book's own table of contents, that the target date falls entirely outside what
this volume prints. No page-by-page phrase search was needed or attempted. Images: `cf_title.jpg` (p. VII),
`cf_toc1.jpg` (p. LXXIV, an unrelated 1524 Appendice piece), `cf_p1.jpg` (p. 1), `cf_last.jpg` (last canvas,
the Table générale).

**Camusat, *Meslanges historiques* — not closed; this Gallica copy is a different edition, and the relevant
section is too large to read page-by-page within this cap.** Two findings before the search itself. First,
`bpt6k5039434`'s own title page (canvas f3) reads "TROISIESME EDITION... A TROYES, Par Iacques Febure...
1644" — **this is the 1644 Troyes third edition, not the 1619 first edition** the earlier "Toward N4" pass
was trying to reach via HathiTrust/Google Books identifiers (which are genuinely the 1619 edition, confirmed
image-only). The two are different scans of the same underlying text ("depuis l'an 1390 iusques à l'an
1580" per this title page), so this copy is still usable for a content search, but any page number found here
will not match the 1619 pagination the earlier snippets used. Second, this is a **recueil of separately-
foliated tracts bound together**, not a single continuously paginated book: canvas f8 carries an "INDICE AU
RELIEUR" (binder's note) giving the physical cahier order — the first tract (marriage articles, Chancellerie/
Notaires edicts) runs to its folio 73; then "le cayer commenceant par ces motz Lettres du Roy François premier
& instructions... iusques au feuillet 217"; then the Sieur de Taix memoirs (75 leaves); then the Sieur de
Mergey memoirs (26 leaves). Canvas f153 (whole-book label "73") confirmed the first tract's end (Notaires
content); canvas f155 confirmed the second tract's own folio "1", titled **"LETTRES DV ROY FRANCOIS PREMIER ET
INSTRUCTIONS A SES AMBASSADEURS... pour affaires traictées pour ledict Seigneur avec le Roy d'Angleterre HENRY
8"** — i.e. this whole ~217-folio tract is French diplomacy around Henry VIII's Rome divorce case, the same
affair Gramont's own 1530 Roman embassy served, and its second half of the title ("ensemble les memoires &
lettres desdicts Ambassadeurs") means ambassador-authored letters (not only the King's) are included. No
item-level table of contents exists anywhere in the volume for this or any other tract (checked the front
matter, canvases f1-f8, and the last canvas, f854, "FIN" — a Legation de Suède & Dannemarch epitaph, not an
index); only the binder's cahier note.

Given no index, nine folios of the 217-folio tract were sampled (roughly every 15-40 folios, at 1.6 s
intervals, one connection reset each at folios 20 and 60 that was not retried a second time per the single-
retry rule): folio 1 (undated, "Double d'une lettre... au... Pape touchant l'affaire du Roy d'Angleterre"),
folio 5 (undated, Cardinals mediating an Emperor/Pope/Genoa matter, "a la fin du moys de May prochain"),
folio 10 (dated Avignon, 8 Sept **1533**), folio 30 (Latin text on a Bologna papal-imperial congress
interrupted by Turkish incursions — matches the **second** Bologna congress of winter 1532-33, not the first
one of Nov 1529-Mar 1530 that Gramont actually attended), folio 90 (dated Paris, 7 Jan 1532/33 per a marginal
"Selon l'Edict" note, addressed to the **Bishop of Auxerre**, naming "Cardinaux de Tournon & de Gramont" as
advisors still in Rome — **the only occurrence of Gramont's name found this session**, but as a third party in
a King-to-Auxerre letter, not a Gramont-authored letter to Villandry), folio 120 (undated, "Coppie de la
lettre de Monsieur de Bayf", mentions the Diet of Spire and the Duke of Ferrara, ~1532 context), folio 150
(undated, a letter to "Monsieur d'Auxerre" about a cipher/decipherment matter), and **folio 180 ("A MONSIEUR
DE VILLANDRE du 4 Decembre 1531")** — the same correspondent, in period spelling, as our target's addressee,
but dated December 1531, eighteen months after our letter, and its content (the Auditor of the papal Chamber,
Monsieur de Paris's judges) does not match any of reading.txt's or reading_f30's decoded phrases. The sampled
folios run 1531-1533, not 1530, and are not in strict chronological order (folio 10 is later than folio 30 and
90), so the May 1530 letter's absence from these nine folios is not evidence it is absent from the other
~208. **Net: the right tract is identified and its correspondent (Villandry) does appear in it under a period
spelling, but the specific 20 May 1530 letter was not found in the folios sampled, and a full page-by-page read
of the remaining ~208 folios (roughly 400 pages) is outside this session's cap.** Gap (2) of "Toward N4" stays
open; it is now better characterised (right edition confirmed present in substance, right tract identified,
9/217 folios checked) rather than merely altcha-blocked. Images and per-folio notes: `images/print_check/
manifest.json`.

**Requests this session.** gallica.bnf.fr: about 33 (2 manifest fetches, both after one earlier reset each
retried once and succeeded; 29 image fetches, all 200 except 2 connection resets — folios 20 and 60 of the
Camusat tract — each retried once per the single-retry rule, the retry on folio 20 returning HTTP 500 and the
retry on folio 60 resetting again, neither pursued further). No other host. No logins, no credentials, no
decoding, no subagents, no edits to reading.txt/key.tsv/ciphertext.txt/reading_f30*.txt. Images saved under
`images/print_check/` (3.1 MB, well under the 30 MB cap).

**Recommendation (not a class change — this worker does not move the class).** Champollion-Figeac can be
struck from the "still open" list entirely — it is now a closed, structural negative, not a search gap. Camusat
remains open; the next worker on it should read the "Lettres du Roy François premier" tract's folios 1-90
first (denser with Rome/1530-33 diplomatic material on this sampling) rather than resampling at wide
intervals, and should expect the tract's own foliation (canvas = 155 + 2×(folio−1) on this ark) rather than
the whole-book label. N3 should stay N3.
- **Michon, *La Crosse et le Sceptre* (2008)**: located (`iwIMAQAAMAAJ`, and two other editions/reprints) but
  `viewability: NO_PAGES` — no snippet, no preview, nothing to search. **Confirmed unreachable**, not merely
  unsearched.
- **Wirtz-Daviau**: query for "Wirtz-Daviau Gramont" returns only bibliography/membership-listing hits (as the
  first audit found), nothing new.

**Recommendation (not a class change — the verifier does not move the class).** Two of the second audit's four
gaps are still open after this pass (Camusat, HathiTrust), one is now precisely characterised rather than closed
(Champollion-Figeac: a real book with no searchable text, not an unreached one), and the fr.3019 companion
letter is identified but unread. On the rule-10 test in section 1 ("If the owner runs the JSTOR queries... and a
second adversarial session closes (1) and (2), N4 is within reach"), condition (2) is not met and JSTOR is still
pending (ASKS.md row 17, now carrying this target's six queries verbatim). **N3 should stay N3** until Camusat
is read (a Gallica-only session, uncontended, retrying `.texteBrut` cold) or the person supplies a JSTOR/HathiTrust
result. The safe sentence of section 1 (as amended by the second audit) is unchanged.

### Requests this session

gallica.bnf.fr: 13 (1 root reachability check, reset, retried once, reset; 1 `.texteBrut`, 302→altcha; 1
manifest.json for `bpt6k5039434`, 200; 2 `ContentSearch`, both reset, one a same-rule retry; 2 SRU catalogue
queries, first reset then a retried success; 2 IIIF manifest.json for `btv1b9059994n`, first reset then a
retried success; 3 IIIF image fetches for `btv1b9059994n` canvases f86-f88, all 200 first try). Other workers
held this host concurrently per ROOM.md; the resets above are not all attributable to this session's own
traffic. archivesetmanuscrits.bnf.fr: 2 (1 wrong-path 404 while locating the fr.3019 search endpoint, then the
`cc49477m` notice, 200). www.googleapis.com (Books, keyed except one bare reachability check, country=US, key
never printed): 7. babel.hathitrust.org: 1 direct (403) + 1 via `tools/browser_fetch.js` (timed out, Cloudflare
`connect_rejected`). catalog.hathitrust.org: 1 (403). data.htrc.illinois.edu: 1 (reachability only, 200).
WebSearch: 1. No logins, no credentials printed, no decoding, no subagents, no edits to reading.txt/key.tsv/
ciphertext.txt.

## Toward N4, second pass (24 Sept 2026)

Verifier follow-up session (Sonnet, cap $8, orchestrator session_01EFmUvFAifLKGdBSsW9mjEG), 24 September 2026,
02:55-03:06 UTC (`date -u` read). Brief: the three gaps of the "Toward N4" section above by the routes it had
not yet tried -- Camusat via the HathiTrust Bibliographic API and HTRC EF headwords rather than Gallica; the
Champollion-Figeac *Captivité* via Internet Archive/Gallica rather than Google Books; the fr.3019 no.31
canvas-to-folio calibration from the manifest's own labelled leaves. Not a solver session: reading.txt, key.tsv
and ciphertext.txt were not touched. Reports what was found and where it was not; does not move the class.

**Gap (2), Camusat -- still not closed; the HathiTrust route is now exhausted, not merely untried.** Two
identifiers were obtained and tried against `catalog.hathitrust.org/api/volumes/brief/{oclc,lccn}/N.json` (both
endpoints reachable and returning valid empty JSON, not blocked): OCLC **78432468**, the only OCLC Open Library
lists for this work, attached to its "3e éd." (Troyes, J. Febure, 1644) rather than the 1619 first edition; and
LCCN **75403742**, from the Library of Congress's own MARCXML record for the true 1619 first edition (Troyes,
N. Moreau, "Pre-1801 Imprint Collection", confirmed by `lccn.loc.gov/75403742/marcxml`: dateline 1619, no
`(OCoLC)` control number in that record at all -- LC's copy is an uncatalogued-for-OCLC rare-book holding).
Both API calls returned `{"records": {}, "items": []}`: **no HathiTrust volume is linked to either identifier.**
A search-by-title fallback was also tried and is now confirmed blocked, not just for the mobile OCR/search
routes already logged: `catalog.hathitrust.org/Search/Home?lookfor=...` returns Cloudflare's "Just a moment..."
interstitial (HTTP 403, `cRay` challenge page saved), the same wall as `babel.hathitrust.org`. `search.worldcat.org`
was also tried (reachable, 200) but its results are rendered client-side from a JSON API this session did not
find; the page's embedded `__NEXT_DATA__` blob carries only UI strings, no result data, so no OCLC could be
recovered that way either. **Net: with the identifiers this session could locate, Camusat is not held by
HathiTrust under either, and the catalog cannot be searched by title from this environment. The HTRC
Extracted-Features route (`tools/htrc_ef_headwords.py`) was never reached because no HTID exists to feed it.**
This is a firmer negative than "unreached": it is "sought by two independent identifiers and not found."
- **Google Books, re-checked for a text layer rather than snippets.** Both scan ids in section 4(b) were
  fetched fresh via the metadata API (keyed, `country=US`, key never printed): `MKpSAAAAcAAJ` and `1d19ZkCU0v8C`
  both report `publishedDate: "1619"` -- **these are copies of the actual first edition**, not the 1644
  reprint -- `viewability: ALL_PAGES`, `publicDomain: true`, but **`readingModes.text` is `false`** for both:
  image-only scans, no OCR text layer, exactly the Champollion-Figeac situation in the first "Toward N4"
  section. No `industryIdentifiers` (expected for a pre-ISBN imprint) -- confirms the Google identifier cannot
  substitute for an OCLC/LCCN to try against HathiTrust either.
- **Status change:** from "Google Books page view blocked, MDZ copy is a different book, Gallica copy exists but
  altcha-blocked" (first pass) to that plus "confirmed absent from HathiTrust by both available identifiers, and
  confirmed image-only on both known Google Books scans of the actual 1619 edition." Still not closed. The one
  remaining route neither pass has tried is a cold, uncontended Gallica `.texteBrut` retry (per the first pass's
  own recommendation) or a manual page-by-page read of the Gallica images, both outside a Sonnet verifier's
  scope/cap.

**Champollion-Figeac, *Captivité du roi François Ier* (1847) -- located on Gallica; blocked by the same altcha
wall as Camusat, not a new route.** Not on Internet Archive: one `advancedsearch` for
`title:(Captivité) AND title:(François)` returns 4 hits, none this work (a 1892 Louise-de-Savoie diplomatic
history, an unrelated 1731 devotional title, an 1844 Paris municipal register, an unrelated 1792 report); a
narrower query adding "Champollion" to the text search returns 0. **Confirmed absent from IA**, as the first
pass already found by a different route. **Found on Gallica**: `dc.title`-anchored SRU query (`(dc.title all
"captivité roi François Champollion")`) returns exactly 1 hit, **ark:/12148/bpt6k204021j** (NUMM-204021,
"Captivité du roi François Ier / par M. Aimé Champollion-Figeac") -- not in AUDIT.md before this session. Its
`.texteBrut` OCR download 302-redirects to `/services/engine/search/altcha?altchaNotVerified=false`, the
identical Gallica bot-verification interstitial that blocked Camusat's `bpt6k5039434` in the first pass, not a
network failure. **Stopped and logged, not retried, per the access playbook.** A follow-up IIIF `manifest.json`
check (to see whether this item, unlike Camusat's, exposes an OCR/text `seeAlso` service) failed twice on
`gallica.bnf.fr` -- a connection reset, then, after the single allowed retry, a full timeout -- and was not
attempted a third time; other workers were concurrently active on `gallica.bnf.fr` this session per ROOM.md, so
these failures are not necessarily specific to this ark. **Status change: from "not found on IA or through the
Google Books API" (first pass, incomplete -- Gallica was not checked) to "not on IA; on Gallica but altcha-blocked
like Camusat, manifest OCR-service check inconclusive (host failures, not re-attempted)."** Still not closed, and
now grouped with Camusat as the same kind of gap: a real, located Gallica copy behind the same challenge.

**Gap (4), fr.3019 no.31 -- resolved: the calibration is canvas = folio + 2, correcting the first pass's
uncertain "88 or possibly 86."** The brief supposed the manifest carries two labelled leaves to fit an offset
from; it does not -- **all 290 canvases of `btv1b9059994n` are labelled "NP"** (checked programmatically, not by
eye), so no manifest-label calibration is possible for this manuscript at all, unlike (apparently) other targets
in this project. The finding aid gives the calibration instead: `archivesetmanuscrits.bnf.fr/ark:/12148/cc49477m`
(re-fetched, one reset then one retried success), read as plain text, pairs each item with a printed folio number
directly: item 3 "Fol. 6", **item 31 "Fol. 84"** (not "Fol. 86" as the first pass's paraphrase had it -- the
finding aid's own text says 84), item 47 "Fol. 131". Canvas f86 (`btv1b9059994n/f86`, the same canvas the first
pass already probed) was fetched again at 1600px width: **its top-right corner numeral reads "84" clearly** at
this resolution, not the "faint... read as '84'" of the first pass. **canvas 86 = folio 84, offset = canvas −
folio = 2**, consistent with the first pass's own leftover note that canvas 88's corner numeral was "88 or
possibly 86" -- 86 is correct under this offset (88 − 2). The +2 offset was not treated as a coincidence to
confirm further, since the finding aid and the image now independently agree on this one point, which is enough
to fix it (a single check, not a two-point line fit, because the finding aid supplies the second point that the
manifest cannot).
- **Content, read from a further crop of the same canvas (signature/closing region, no additional canvases
  fetched): not a diplomatic-protocol letter in the register of the f.29r/f.30 reading.** The visible text is a
  military/campaign report -- troops "de pied" and "de cheval", a camp, artillery pieces ("faulcons"), a named
  captain, movements near a marquis's territory -- ending in an ornate signature, below which a further short
  paragraph begins "J'ay escript au roy pour..." and names "Paule Camille" and "le marquis de [name partly
  illegible]", with a dateline that appears to read "Rome, le xv[e] jour de may", consistent with the finding
  aid's date for item 31. **This transcription is a rough visual scan by a non-specialist reader, not a
  paleographic reading** (1530 French secretary hand was not attempted line-by-line) -- it is offered as
  description, "context, not plaintext," per the brief, and should not be relied on for wording. **No exact
  match was spotted** for any of the ciphered letter's distinctive phrases (porteur, article, adresse,
  contenter, oster, suspecon, cognoissance, pacquet, courrier, plustost) in what could be made out, but this is
  not a rigorous phrase search and the hand defeats confident reading of most of the page. The subject matter
  (troop movements, artillery, a marquis) does not obviously overlap the ciphered letter's apparent subject
  (a courier, an article set apart, an address to the king via his secretary) -- consistent with the second
  audit's observation that item 31 is addressed to a different recipient (the grand maître, not Villandry) and
  carries no "avec chiffre" flag. **This remains context, not a decipherment or a source of new plaintext for
  item 21/22**, and it does not move the class.
- Two more canvas fetches (a mis-targeted crop, then a corrected one, both of the same already-fetched f86) were
  used to read the closing/signature region; no other canvases of `btv1b9059994n` were fetched this session.

**Recommendation (not a class change -- the verifier does not move the class).** Camusat and Champollion-Figeac
are now the same kind of gap -- a located copy, blocked by Gallica's altcha challenge -- rather than two
different problems; Camusat is additionally confirmed absent from HathiTrust by every identifier this session
could find. The fr.3019 calibration gap is closed (canvas 86 = folio 84), and its content, on a non-expert
reading, looks like unrelated context rather than a lead. **N3 should stay N3.** The single concrete next step
across both remaining gaps is the same one the first pass already named: a Gallica-only session (no concurrent
host traffic from other workers) retrying `.texteBrut` cold on both arks, since an altcha challenge can be
traffic-dependent rather than a permanent block; short of that, only a manual page-by-page read of either
Gallica scan, or the person's JSTOR/HathiTrust access (ASKS.md row 17), would close them. The safe sentence of
section 1 is unchanged.

### Requests this session

catalog.hathitrust.org: 4 (2 Bibliographic API calls by oclc/lccn, both 200 with empty results; 1 reachability
check; 1 `Search/Home` title search, 403 Cloudflare challenge, not retried). openlibrary.org: 4 (2 search.json,
1 work editions.json, 1 book record). lccn.loc.gov: 2 (redirect check, MARCXML). www.googleapis.com (Books,
keyed, country=US, key never printed): 2. archive.org (advancedsearch): 2. search.worldcat.org: 1 (reachable,
200, but client-rendered with no usable data in the static fetch). gallica.bnf.fr: about 11 (2 SRU queries, the
first mistargeted; 1 `.texteBrut` + 1 header-only recheck, both altcha; 2 manifest.json attempts for
`bpt6k204021j`, 1 reset + 1 timeout, not retried a third time; 1 manifest.json for `btv1b9059994n`, 200 after an
earlier unrelated reset/timeout episode on the other ark; 4 image fetches for canvas f86, all 200 -- full page,
two mistargeted/retargeted signature crops). archivesetmanuscrits.bnf.fr: 2 (1 reset, 1 retried success).
WebSearch: 2. No logins, no credentials printed, no decoding, no subagents, no edits to reading.txt/key.tsv/
ciphertext.txt. Images saved under `images/fr3019_check/` (not the target's own `images/manifest.json`, since
these are a companion manuscript's canvases, not fr.2980's).

## Open-index scholarship pass (24 Sept 2026)

Worker session (Sonnet, cap $8, orchestrator session_01EFmUvFAifLKGdBSsW9mjEG), replacing JSTOR as the
scholarship-coverage gate per the owner's 24 Sept note (CLAUDE.md, JSTOR-QUEUE.tsv). Not a verifier session: does
not move the N3 class, does not decode. Job: translate JSTOR-QUEUE.tsv rows 2-7 (this target) into phrase/keyword
queries and run them against OpenAlex, Semantic Scholar, CrossRef, Persée, HAL and Google Scholar (via WebSearch).
Full per-host results in `OPEN-INDEX-RESULTS.tsv` rows 2-7.

**Hosts unreachable for the whole pass, all six targets:** `api.openalex.org` (this container's shared egress IP
had exhausted its anonymous daily budget before this session started -- `{"error":"Rate limit exceeded",
"message":"Insufficient budget ... $0 remaining; resets at midnight UTC"}`, confirmed on 8 attempts with pauses;
no `OPENALEX` API key is set in this environment) and `api.semanticscholar.org` (429 "Too Many Requests" on 6
attempts with pauses, no key set). Neither could be made to answer even a one-word test query. Logged as
unreachable, not as a negative.

**CrossRef, Persée, HAL:** no hit on this letter. The one topically-adjacent Persée result (J. Fraikin, "La
nonciature de France de la délivrance de Clément VII à sa mort", MEFR 1906) was fetched (page only carries
metadata, no embedded full text) and set aside: it covers the *papal nuncio's* mission to France, the opposite
diplomatic direction from Gramont's French embassy to Rome, so it is unlikely to hold this letter and was not
read further. Everything else returned is keyword-collision noise (a modern IMF economist named Végh Gramont;
the château de Villandry; the Roman emperor Caligula-adjacent and Voynich/Linear-B "decipherment" hits on other
rows' generic terms) — logged in full in the TSV, not repeated here. HAL returned 0 hits for every combined
query on this target (a bare "Gramont" alone returns 469 hits, almost all the unrelated modern philosopher
Jérôme de Gramont).

**Lasry/Cryptologia (row 7):** CrossRef and WebSearch both confirm Lasry's actual Cryptologia bibliography (the
2023 Major Josse cipher paper, the 2016 columnar-transposition paper, the 2023 Mary Stuart paper with Tomokiyo
and Biermann) contains no article on Gramont or Francis I's 1530 ciphers. This corroborates, independently of
Tomokiyo's own pages, that Lasry's Gramont-1530 key work has not been published as a Cryptologia article — it
exists only via cryptiana's web pages, as section 4(g) already said.

**Row 6 (Google Scholar via WebSearch):** confirms, independently of this session's own re-clone, what the
second audit's clone of `dbourdeau/cyphersolver` (head `5dcd5c3`) already found: his `gramont1529/` folder reads
fr.3091 no.23 (11 Oct 1529) and fr.3071 no.7 (21 July 1530, "read ~85%"), using Lasry's 2023 key — both are
different items from fr.2980 f.29-30, not a reading of this target. Not new; flagged only so a future
check-solved sweep knows to re-check whether fr.2980 itself has since been solved there.

**Rows 2-3 (Google Scholar via WebSearch):** the search engine's own summaries surfaced only the BnF catalogue
description of fr.2980 (matches section 2 verbatim) and Gramont's other, already-known ciphered letters (27 Aug
and 5 Oct 1529, 28 March 1530 Boulogne) — all already covered by the Le Grand page-by-page reading in the second
audit. No new source for the 20 May 1530 letter to Villandry itself.

**Verdict for this pass:** no hit, on any of the six hosts, adds a new candidate print or decipherment of fr.2980
f.29r-30. Two of OpenAlex/Semantic Scholar/CrossRef/Persée/HAL/Google Scholar were unreachable (not searched);
the other four returned only noise, already-known facts, or one unread topically-adjacent lead (Fraikin 1906,
not fetched in full). This does not close any of the four gaps named in the "Toward N4, second pass" section
above (Camusat, Champollion-Figeac, HathiTrust whole-library search, Michon). **N3 unchanged; the verifier does
not move the class from a scholarship-pass worker's report.**

Requests this session: api.openalex.org 8 (all 429, one shared-budget message, no data returned).
api.semanticscholar.org 6 (all 429). api.crossref.org 6 (one per row, `query.bibliographic`, 200 each).
api.archives-ouvertes.fr 12 (6 combined-query attempts at 0 hits, 6 narrower single/double-term follow-ups,
200 each). www.persee.fr 6 (`ta=article&q=...`, 200 each) plus 1 article-page fetch (Fraikin 1906, 200). WebSearch
7 queries. No logins, no credentials, no decoding, no edits to reading.txt/key.tsv/ciphertext.txt/key_extension_f30.tsv.

## f.30

Verifier session (LANE V, Opus, cap $15, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ), 24 September 2026,
03:34-04:05 UTC (`date -u` read). It took no part in the f.30 passes, the reconciliation or the S extension. It did
not decode, and it did not touch ciphertext_f30.tsv, key.tsv, key_extension_f30.tsv or any reading. It audits
reading_f30.txt / reading_f30_tokens.tsv (published key) and reading_f30_extended.txt (key + grade-S extension,
commit e8567d0, which landed during this session). Section 4 and the three sections after it cover families already
searched for f.29r. They are reused here and not repeated. This section adds the searches that f.30's own plaintext
calls for.

Claim under audit (orchestrator, ROOM.md 24 Sept 03:16; status.json): "f.30r-v: read with the published key 24
Sept 2026, 1973 signs, H 1502 / M 239 / U 232, continuous French on 22 of 55 lines", and, since e8567d0, "11
unkeyed signs given values at grade S with a matched control (96/103): U 232 to 59, continuous French on 32 of 55
lines".

### Verdict

| item | prior plaintext | prior decipherment of this item | class |
|---|---|---|---|
| BnF fr.2980 f.30r-v, no.22 (Anc. 8505), entirely in cipher, "Faict à Rome, le XXme jour de may M.D.XXX", signed "De Gramont E. de Tarbe"; addressed **to the king** (see below), 1973 signs | **not located.** No printed text, extract, calendar entry or summary of this letter was found. Its existence and date are in print only in the 1868 BnF catalogue and the *Catalogue des actes* IX [412] [V3b, 24 Sept 2026: [412], not [411], per V2's check; p.61] ("2980, fol. 29 et suiv."). A **sibling letter** on the same negotiation is in print: Gramont to Francis I, Rome, April 1530, in clear (Béthune 8530 c.35), *Archivio storico italiano*, Appendice I (1842-44), doc. XXXVIII, pp.473-481 (Molini's transcription). **It is a different letter** (test below). | **not located.** None on the leaf, in the volume, in the BnF or Dupuy catalogues, in print or online. As for no.21, it had been **identified as readable** before us: Tomokiyo, francis.htm ("These undeciphered letters can be read with Gramont's cipher (1530)"; his page source also holds a commented-out image slot `francisBnFfr2980f29.png`, f.29 only), and Bourdeau, CATALOGUE.md line 76, catalogue 328 ("fr. 2980 nos. 21–22 … Gramont 1530 key held"; re-checked at head c85ece1, 23 Sept 2026 20:50 -05:00). Neither gives a reading. | **N3** |

**Why N3 and not N4.** The gaps that hold f.29r at N3 are shared by f.30 and are still open: Camusat (1619) and
Champollion-Figeac's *Captivité* (1847), both located on Gallica and both behind its challenge; HathiTrust full
text (Cloudflare). f.30 adds three gaps of its own. (1) The *Archivio storico italiano* Appendice was read in vol.
I only. Vols. II-IX, where Molini's and others' Florentine documents continue, were not grepped. (2) Sanuto's
*Diarii* for 1530 (vols. 52-53) were not searched. They register intercepted and copied letters, and they are the
next place a summary of a French letter from Rome would appear. (3) OpenAlex and Semantic Scholar were unreachable
this session (quota exhausted; 429). The JSTOR rows are queued and do not block the class on their own (CLAUDE.md,
24 Sept 2026). A session that closes (1) and (2) and reruns the open indexes can take f.30 to N4, together with
f.29r once Camusat is read.

**Confidence in N3:** high for the English, Spanish and Venetian calendars, Le Grand's *Preuves*, Desjardins,
De Leva, Pastor and the Dupuy catalogue, which were read or grepped in full text. Medium for the rest of Molini's
output and the Italian series.

**Safe sentence.** "BnF fr.2980 f.30r-v (no.22) is a letter written entirely in cipher by Gabriel de Gramont,
bishop of Tarbes, Rome, 20 May 1530. The formulas 'Sire' and 'vostre commandement' show that it is addressed to
Francis I. Tomokiyo had identified it as readable with the published Gramont 1530 key (Tomokiyo; Lasry 2023), and
Bourdeau catalogued it (328). We transcribed it from the Gallica image (one reconciled reading of two blind passes)
and applied that key: the table gives values for 1500 of 1973 signs (H), 241 are uncertain and 232 unkeyed. A
further 11 signs were given values cryptanalytically (grade S, matched control 96/103), leaving 59 unread. Parts of
32 of 55 lines read as continuous French, on the declaration of the liberty of Florence. No prior printed plaintext
or decipherment of the letter was located in the editions listed in AUDIT.md (N3). A clear-text letter of April 1530
from Gramont to the king on the same negotiation is printed in *Archivio storico italiano*, Appendice I, pp.473-481."

**Unsafe sentences.** "First decipherment" / "previously unread" / "newly recovered" / "unpublished" (rule 10;
N3 only). "Gramont to Villandry" for f.30: its cipher addresses the king, and the BnF notice names no recipient.
"Cardinal Gramont" on 20 May 1530: he was created cardinal on 8 June. "1502 of 1973 signs read" or "read in
full": the reading is partial and rests on one reconciled transcription. "1712 signs deciphered": S values are
cryptanalytic, not key readings. "A new letter on Florence": the negotiation is documented in print (ASI App. I;
Pastor X; De Leva III).

### Who, to whom, when, where: is f.30 a separate letter?

- **Separate item, own date and signature.** The BnF notice (re-fetched this session, cc494342, one reset then
  200) lists no.22 on its own, "Lettre en chiffre", with the full date "Faict à Rome, le XXme jour de may M.D.XXX".
  The date and signature on f.30v are in clear (NOTES.md, check-solved). No recipient is named in the notice (its
  "…" elides the address). no.21 names Villandry. **Established** (catalogue and image).
- **Recipient: the king.** The cipher contains "SIRE QV'IL VOVS" (f.30r L17), "… SIRE P[ET] MAINTENIR" (L21), "TRES
  HVMBL[EM]ENT SIRE" (f.30v L05-06) and "VOVSTRE [COM]MANDE[M]ENT" (f.30v L17). "Sire" is the form of address to the
  king. **Inferred, grade I, strong.** It fits f.29r's cipher: "il y baille a ce porteur ung article que j'ay mis a
  part, et … faict l'adresse de dessus a vous, combien que ce soit au roy" (reading.txt L01-L03). Villandry received
  a piece set apart and addressed on the outside to him, though meant for the king. f.30, an all-cipher letter to the king on the same
  day, is the obvious candidate for that piece. **This identification is an inference, not established.** An
  alternative is the "double des lettres que j'escriptz lundi" of f.29r's clear text. It is less likely because
  f.30 is dated the 20th in clear, not Monday the 16th.
- **Sender, place, year.** Gramont (clear signature), Rome, 1530 (clear dateline). Consistent with the embassy
  record (Pastor X: Gramont in Rome from April 1530; CSP Spanish IV.1 pp.560-561, Mai on Gramont "some days ago",
  late May 1530: a courier of Gramont's "stopped at Florence and the despatches taken from him").
- **Subject (grade I, from the decoded runs):** "la declaration de la liberte de Florence" (f.30v L02-03, L10),
  "la ville et la force entre vo[s] mains" (f.30v L09), "qu'il ve[u]lt aller en Avi[g]non" (f.30r L32), "pour
  recouvrer ce que ses predecesse[u]rs … ont perdu" (f.30r L33-34), "il n'a aucune desliberation" (f.30v L01),
  "l'ambassadeur … et aultres ses ministres" (f.30v L12). This continues the plan Gramont reported in April: the
  Florentines lay down arms, the papal camp withdraws, and "la force de la ville demourast entre voz mains", under
  the king's protection (ASI App. I p.477).

### Is f.30 the printed April letter in cipher? Test

The April letter (ASI App. I pp.473-481, OCR from IA `archiviostoricoi01fireuoft`, 16,126 letters after folding)
was compared with the f.30 reading (1,840 letters in 47 unbroken runs of 8+, extended reading). Both were folded to
the cipher alphabet (upper case, no accents, J→I, U→V, Y→I). For each run, the longest substring present in the
April text was found.
- **April letter:** longest shared run 18 letters (SIREQVILVOVSPLAISE, "Sire, qu'il vous plaise", a formula), then 14
  (FAIRECEQVILVOV; ETQVENEANTMOIN), then 12 (TACRAINDREQV, SICENESTQVEL, FAIRESERVICE).
- **Controls**, same length, same test: Bourrilly's *Jacques Colin* (French, 1905) 11; Desjardins II, two windows,
  11 and 11; De Leva III (Italian with French and Spanish quotations) 9.
- f.30 has continuous runs of 30-40 letters (e.g. f.30v L03, 40 letters). If it were a cipher copy of the April
  letter, those runs would match in full. **They do not. f.30 is a different letter.** Its slightly higher shared
  runs match a letter by the same writer, to the same recipient, in the same month-range and on the same subject.
  The shared vocabulary ("la force … entre voz mains", "recouvrer", "maintenir", "il est impossible") is topical, and
  the order differs: f.30 has "la ville et la force entre vo[s] mains", April has "la force de la ville demourast
  entre voz mains". Script: inline in this session; the method is reproducible from the two files named above.

### Reading quality (rule 4, rule 7)

- **decode.py --check passes** (exit 0, this session, after e8567d0). It prints f.29r 568: H 533/M 30/U 5; f.30
  1973: H 1500/M 241/U 232; f.30 extended: H 1500/S 158/M 256/U 59. These match NOTES.md and status.json.
- **H is from a key source.** Every key.tsv row graded H cites Lasry and/or Tomokiyo (checked by script: no H row
  without one of the two). Grade H is correct under rule 4 as "value from the published table".
- **What H does not say, and NOTES.md understated.** NOTES.md says "M means a sign read with doubt". In fact only
  the reconciler's `l` signs are demoted (decode.py line 53). **331 of the 1502 H tokens are on signs the
  reconciler read at medium confidence (`m`).** H on a high-confidence identification is 1171. Also, 43 H tokens
  fall on the four keyed signs the reconciler itself flagged as doubtful in context: eh 19, Tb 16, H 8. The
  solver's own model puts eh at T, not the table's D (47.6 bits; DECLARA*t*ION), a contradiction a key-image check
  must settle. This does not break rule 4, but the H count overstates the firmness of the reading. The honest
  summary is "values from the key for 1502 signs, 1171 of them on confidently identified signs; one reconciled
  transcription (agreement with blind passes 63.5% and 55.3%)". NOTES.md is corrected (below).
- **M/U share reported honestly.** U 232 (11.8%) and M 239 (12.1%) are stated in every place that gives H. The
  eight unread lines at the top of f.30r are named. The extension's S grade has a matched control run before the
  real signs (held-out 50/53) and states its limits (25 keyed signs in the pool; S values on `l` signs demoted
  to M). No over-claim found in the extension's wording ("a cryptanalytic result resting on a key-based reading").
- **Transcription.** A single reconciled reading, as NOTES.md says. The class is about print, not the transcription.
  Any outward sentence must still say "partial".

### Search log (24 Sept 2026, this session)

(a) **Canonical series, re-grepped for f.30's content** (full djvu text, IA): LP iv.3 (`11332111bsb`): "liberty of
Florence" 0 hits; "Avignon" hits are Wolsey/legatine (1527-29); no Gramont item of 20 May (as section 4). CSP
Spanish IV (`calendarofletter0004pasc`): Tarbes 121 hits. Mai's despatch printed at pp.560-561 (late May 1530)
reports Gramont's words to the pope and Muscettola, and a Gramont courier stopped at Florence. That is the imperial
report, not the letter. September 1530 hits (pp.701-702) are later. CSP Venetian IV (`calendarofstatep4187brow`):
Tarbes 77 hits, all 1527-29 (Spain, Burgos, Poza) or index. None is of May 1530. **Searched.**

(b) **Sender/recipient editions new to this file.**
- ***Archivio storico italiano*, Appendice, t. I (1842-44)** (IA `archiviostoricoi01fireuoft`, full text): the
  only Tarbes items are doc. XXXVIII (April 1530 letter to the king, above) and its index entry. **Searched; a
  sibling letter, not ours.** Vols. II-IX: **not searched** (gap 1).
- **Desjardins/Canestrini, *Négociations diplomatiques de la France avec la Toscane* II** (IA
  `gri_33125010469852`, full text): Carducci's legation 1528-30. Tarbes hits end with Gramont's 1529 departure for
  Italy. No Gramont letter of 1530, and no "liberté de Florence" declaration. **Searched.** Vol. I
  (`gri_33125017127347`) fetched; it predates 1510, out of range.
- **De Leva, *Storia documentata di Carlo V* III** (IA `storiadocumenta03levagoog`): cites Gramont's April letter
  (Molini, ASI App.) and Mai and Muscettola of 29 May 1530 (Simancas). No 20 May letter, and no 2980/8505.
  **Searched.**
- **Pastor, *Histoire des papes* X** (IA `kpbc.umk.pl.Magazyn_220_10_180359`, French tr., full text): Gramont in
  Rome from April 1530. Cites the April letter (ASI App. I p.476), Le Grand III p.386 (Bologna, Feb) and Vienna
  reports. No 20 May letter, no fr.2980. The German editions (`geschichtederpap42past`, `p2geschichtederp04past`)
  appear in the fts only for the April quotation. **Searched.**
- ***Catalogue de la collection Dupuy*** (1899, IA `cataloguedelaco00dupugoog`, `…01…`, full text): Dupuy 452
  holds **Gramont to Du Prat, Rome, 15 May [1530], orig. (f.48)**, a companion letter five days earlier, not
  flagged as cipher. It is the same volume as the Raince decipherment ("[par le même?], s.d. (31)"). No
  decipherment, copy or unattributed piece dated May 1530 "au Roi" is listed there. Catalogue-wide: 0 hits for
  "20 mai 1530" and for "déchiffr-"/"en chiffres" with 1530/Tarbe/Gramont. **Searched.** Dupuy 452 f.48 is
  context for the solver, not a decipherment (for LANE G, if wanted).
- Bourrilly, *Jacques Colin* (1905, `jacquescolinabb00bourgoog`): hit on a list of May 1530 dates. It is Colin's
  material, with no Gramont letter. **Searched.**

(c) **Holding archive.** BnF notice cc494342 re-fetched: no recipient for no.22, no bibliography, no decipherment
listed in the volume (confirms the second audit's Raince test). Gallica not used (LANE G's host); nothing
pending for it.

(d) **Phrase search on the decoded text** (u/v, i/j normalised; accented and unaccented).
- IA be-api fts, 0 relevant hits: "declaration de la liberte de Florence", "declaration de la liberté de Florence",
  "que ses predecesseurs ont perdu" Florence, "la force entre voz mains", "la ville et la force entre", "neantmoins
  qu'il ait mauvaise fantaisie", "maulvaise fantasie" 1530, "toutes choses qui vous touchent de si bon pied", "qui
  vous touchent de si bon pied", "qu'il n'a aucune deliberation", "maintenir les amitiez" 1530, "liberte de
  Florence" roy 1530 Rome, "2980, fol. 30", "2980, f. 30". The hits for "liberte de Florence" Tarbe, "aller en
  Avignon" Tarbe 1530, "de si bon pied" Tarbe, "pour recouvrer ce que ses predecesseurs" (3: a universal history,
  Hugh Capet), "la declaration de la liberte" Florence Tarbe and "la ville et la force" Florence 1530 are all
  unrelated (the Tarbé family, Froissart, Revolutionary debates). "Florance n'eust jamais este" found the April
  letter and the works citing it (Pastor, Reumont, the DHGE).
- Google Books API (keyed, country=US), 0 relevant: "declaration de la liberte de Florence" (both spellings),
  "liberté de Florence" Tarbes 1530, "liberté de Florence" Gramont (1: *Mercure françois*, 1970 reprint, unrelated),
  "libertà di Firenze" Tarbes 1530 (1: *L'assedio di Firenze*, 1857, the August capitulation), "la ville et la force
  entre", "que ses predecesseurs ont perdu" Florence, "veult aller en Avignon", "maulvaise fantasie" (3, unrelated),
  "evesque de Tarbe" "au roy" 1530 Florence, Gramont Tarbes "20 mai 1530" roi, "Tarbes" "mai 1530" Florence roi
  lettre chiffre, "2980, fol. 30", "Gramont" "lettre chiffrée" 1530 Florence, "qui vous touchent de si bon pied",
  "n'a aucune deliberation" Florence, "la ville et la force" Florence 1530 roy, "liberté de Florence" "mai 1530"
  Tarbes, "Tarbes" Clément "Avignon" 1530 Florence liberté. "évêque de Tarbes" "mai 1530" Florence gave 3: the
  Dupuy catalogue (searched above) and *Revue des Hautes-Pyrénées* 1907 (no snippet; a local-history journal,
  **not read**). "fr. 2980" Tarbe gives only Tournon's correspondence (fol.33) and the *Catalogue des actes*
  (fol.83, 1531).

(e) **Solver repositories and cipher pages**, fresh shallow clones, grep only, deleted after:
dbourdeau/cyphersolver head c85ece1: fr.2980 only at CATALOGUE.md:76 (328, "Gramont 1530 key held"),
rangone1530/NOTES.md:68 (no.44, not ours) and two mirrors of Tomokiyo's francis.htm. gramont1529/ reads fr.3091
no.23 and fr.3071 no.7. **Catalogued, not read.** aaymeloglu/unsolved-ciphers head 2495c45: its DECODE catalogue
has three Gramont records (fr.3040 f.16 and f.18, fr.3091 f.45-47, all "Non-decrypted" in DECODE's field and
all 1529 or Bologna 1530). None is fr.2980.

(f) **Scholarship, open indexes.** CrossRef (7 queries: Gramont Tarbes 1530; Gramont Tarbes ambassade Rome;
Gramont cipher 1530; liberté de Florence 1530 François Ier Clément VII; Gramont Villandry; French diplomatic
cipher Francis I Lasry; siège de Florence 1530 France diplomatie Rome): the only on-topic hit is the PUR chapter
"Gabriel de Gramont (1486-1534)" (2011), already read (section 4(b)). HAL (same 7): 0. Persée (2 queries,
"Gramont Tarbes 1530" and "évêque de Tarbes" Florence 1530): on-topic only "La première application à Bordeaux du
concordat de 1516: Gabriel et Charles de Grammont (1529-1530)" (*Annales du Midi* 1956, benefices; not the
embassy). **OpenAlex: unreachable** (429, "creditsRemaining 0", after one retry). **Semantic Scholar:
unreachable** (429, one retry). JSTOR: not probed. Three rows added to JSTOR-QUEUE.tsv: `"Gramont" AND Florence AND 1530 AND (liberté OR
liberty)`; `"évêque de Tarbes" AND Florence AND 1530`; `"Gabriel de Gramont" AND "Clement VII" AND Florence`.

(g) **Not searched (named gaps):** ASI Appendice II-IX; Sanuto *Diarii* 52-53; *Revue des Hautes-Pyrénées* 1907;
Varchi and Nardi (Florentine narratives, which would paraphrase at most); Camusat, Champollion-Figeac and
HathiTrust as for f.29r.

### Corrections made (this session)

1. NOTES.md, "f.30 reading", Grades paragraph: added a verifier note that `m`-confidence signs keep H (331 of
   1502), so "M means a sign read with doubt" understates the doubt. It also names the 43 H tokens on the
   flagged signs eh/Tb/H.
2. NOTES.md, "f.30 reading", Plain sense item 3: "The addressee of item 22 is not established here" now carries
   the verifier's finding (the king, grade I; the likely "article mis a part" of f.29r, an inference).
3. status.json, the fr2980-gramont row's `name`: "Gramont to Villandry, Rome, 20 May 1530, two letters in
   cipher" became "Gramont to Villandry (f.29) and to the king (f.30), Rome, 20 May 1530, two letters in cipher".
   Its `note` "569-sign" became "568-sign", to match its own counts (533+30+5) and decode.py.
4. Section 1 of this file (f.29r): its safe sentence gives 569 / H 538 / M 26, the first reader's counts. The
   current counts after the second reader are 568 / H 533 / M 30 / U 5 (NOTES.md, "Second reader: changes
   applied"). A pointer is added under section 1.
No new/first/unread/unpublished wording about f.30 was found in the folder, the ROOM line or status.json (grep).

### Postmortem

**Failure named: the recipient was carried over from the sibling item.** The board row and the folder title
presented both letters as "Gramont to Villandry". The BnF notice gives no recipient for no.22, and the cipher
addresses the king. Nobody read the plaintext for its addressee before this audit, and a verifier who took the
board's line would have searched Villandry's papers only. The Dupuy 468 lesson applied again: the plaintext
widened the search to letters to the king, and that is how the April 1530 letter in ASI App. I turned up. It is
the closest printed text to f.30. **Second finding: an editor's continuation was missed.** The first audit read
Molini's *Documenti* (1836-37) and found only item 23 of 8505. Molini's later Béthune transcriptions went into the
*Archivio storico italiano* Appendice, which no audit had opened. Lesson for the verifier template: when a
source's editor is identified, search that editor's later series and the journal they fed, not only the book.

### Requests this session

archive.org: about 75 (be-api fts about 41 queries, advancedsearch 6, metadata about 15, djvu.txt downloads 11),
at least 3.2 s apart. www.googleapis.com (Books, keyed, country=US, key never printed): 21, 3.2 s apart.
archivesetmanuscrits.bnf.fr: 2 (1 reset, 1 retry 200). api.crossref.org: 7. api.archives-ouvertes.fr: 7.
api.openalex.org: 9 (all 429; stopped). api.semanticscholar.org: 9 (all 429; stopped). www.persee.fr: 2. github.com: 4
shallow clones (two repositories, twice). gallica.bnf.fr: 0. No logins, no credentials printed, no decoding, no
subagents.

## Second audit (adversarial), f.30, 24 Sept 2026

Adversarial second auditor (LANE V, Opus, cap $15, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ), 24 September 2026,
04:21-04:40 UTC (`date -u` read). This session is separate from the f.30 solver, the reconciler, the first f.30 verifier
and the blind second reader (pass C, 04:28, which ran in parallel and whose files this section does not use). It did not
decode. Its only aim was to find no.22 (f.30r-v, Gramont to Francis I, Rome, 20 May 1530), its plaintext, an extract, a
summary or a decipherment, in print, and so prove the first audit's N3 wrong. It did not find one.

### Verdict

| item | first audit | this audit | reason |
|---|---|---|---|
| BnF fr.2980 f.30r-v, no.22, Gramont to the king, Rome, 20 May 1530, all cipher | N3 | **N3 confirmed (two audits)** | Gaps (1) and (2) of the first audit are closed as negatives: the *ASI* Appendice II-IX and the series' general index, and Sanuto's *Diarii* 52-54. So are Ribier, Molini, Desjardins II, the *Catalogue des actes* and both solver repositories, re-checked by phrase and name. The closest print is still the sibling letter of April 1530 (ASI App. I pp.473-481). **Not raised to N4** because Camusat (1644 ed., the tract of Francis I's letters) is sampled, not read (LANE G, cefda7c, 9 of about 217 folios); HathiTrust full text, OpenAlex and Semantic Scholar were unreachable; and the Simancas intercepts are unexamined (below). |

### What this audit found that the first did not

1. ***ASI*, general index of series I and Appendice I-IX** (IA `archiviostoricoi116depuuoft`, "Index 1-16 Append 1-9",
   full text). Its chronological list for 1530 has exactly one Tarbes item, "aprile. Lettera del vescovo di Tarbes al re di
   Francia … I App., 473" (the April letter). Between 4 May (Ferrucci) and 16-17 May / 31 May (Tedaldi) it lists nothing
   French. The name index has one entry, "Tarbes (Vescovo di). V. Ind. 2.°, an. 1530, aprile". This covers App. III as well,
   whose djvu text returned HTTP 500 twice (be-api fts on it: 0 hits for Tarbes). **Gap (1) closed.**
2. **Sanuto, *I Diarii* 53 (1 Mar-30 Sept 1530)** (IA `idiariidimarinos53sanu`, full text; vols. 52 and 54 checked for
   range). The editors' index gives "Gramont (Agramonte) (de) Gabriele … 268, 280, 298, 360, 368, 369, 544" and "Terbe (di),
   v. Gramont". Every column was read in context. They are Surian's reports from Rome: the cardinal's hat (col. 268, June),
   Gramont's remark about the king's sons (280), and the king's letters for Malatesta Baglioni and Gian Paolo da Ceri, 17 June
   (298). There are also a July congratulation on the hat (368-369, "Agramonte") and a brawl between his household and the
   Portuguese ambassador's (544, August). There is **no copy or summary of a Gramont letter of May 1530**. A proximity scan of
   the May columns (lines 11000-18300) for the French ambassador, "libertà" and Avignon found only Florentine and Venetian
   material. Vol. 52 (Oct 1529-Feb 1530) indexes Gramont at Bologna only. **Gap (2) closed.**
3. **An interception route, not a print.** Loaysa's letters to Charles V (Heine 1848, IA `briefeankaiserk00loaygoog`, full
   text; searched for Tarva/Tarbe) begin in late June 1530. In letter V the pope discusses "die in Asti aufgefangenen Briefe".
   CSP Spanish IV.1 p.603 (Mai to Covos, summer 1530; IA `calendarofletter0004pasc`, re-read this session) says "Tarbes has
   complained … that the governor of Asti, Scalenga, intercepts his letters" and that only letters going to Florence are
   touched. The imperial side therefore intercepted French letters of this embassy and deciphered some ("Contemporary
   deciphering on separate sheet" is noted on Mai's own despatches). No printed calendar entry is an intercepted copy or
   decipherment of the 20 May letter to the king. The BnF original reached the French side (Béthune), which argues against
   its interception. **An archival decipherment at Simancas (Estado) or Vienna is not excluded, because it is not in print.**
4. **Gramont's secretary.** Persée (Thorel, *RHR* 71, 2011, pp.91-105) names Berthault as Gramont's secretary until 1534.
   It is not a print of the letter, but a lead for anyone searching for a secretary's register of copies.

### Source-family log (this session)

(a) **Canonical series.** CSP Spanish IV (full djvu text, re-grepped for intercept/decipher/Asti with Tarbes and 1530):
nothing for 20 May. The Asti passage is above. LP, CSP Venetian: as in the first audit, not repeated.
(b) **Sender/recipient editions.** Ribier 1666, all three IA scans (full text, re-grepped for Tarbe/Gramont): hits are
1540s (the Alger expedition, "l'Evesque de Tarbe Ambassadeur du Roy vers l'Empereur"), none of 1530. Molini, *Documenti*,
four IA scans: 8505 appears only in the register of Béthune volumes, and the Gramont hits are other letters (Casale to
Gramont, etc.). Desjardins II (`gri_33125010469852`): 11 Tarbes hits, none of May 1530, and no phrase hits. *Catalogue des
actes* I, VI, VII, IX (full text): "2980" in IX only at [412] (existence and date, as known) [verifier V2, 24 Sept 2026: [412], not [411]; [411] is Villebon's 1528 mission; Catalogue IX p.61]; the other hits are act
numbers. **Searched.**
(c) **Documentary editions and journals.** *ASI* App. II, IV-IX (full djvu text) and III (index + be-api fts); the general
index (above). Tarbes hits: App. II p.153 (a review quoting Charles V, 1531, on the cardinal's return), App. VIII p.535 (a
review of Heine's Loaysa). **Searched.** Sanuto 52-54: **searched** (above). Heine/Loaysa: **searched**.
Champollion-Figeac, *Captivité* (LANE G, cefda7c): **closed**, structurally (Oct 1524-Apr 1526 only).
(d) **Holding archive.** Not re-queried (the first audit fetched cc494342 today). Gallica: not used (LANE G's host).
(e) **Phrase search on the decoded text** (tools/print_check.py, 12 phrases from reading_f30_extended.txt, 23 listed
sources plus IA-global, Google Books, OpenAlex and CrossRef; output kept in the scratchpad, not committed, because this
worker writes only AUDIT.md). All 23 listed sources gave **no hits** for every phrase. IA-global and Google Books gave no
hits for 9 of 12 phrases: "la declaration de la liberte de Florence", "la ville et la force entre vos mains", "qu'il veult
aller en Avignon", "pour recouvrer ce que ses predecesseurs ont perdu", "qu'il n'a aucune deliberation d'aller", "toutes
choses qui vous touchent de si bon pied", "neantmoins qu'il ait maulvaise fantasie", "l'ambassadeur et aultres ses
ministres", "qu'il ne s'y peut faire aultre chose". Three generic formulas hit unrelated works ("qu'il est impossible de
voir", "maintenir les amities", and "sur la foy que je vous dois", which found 3 HMC Salisbury calendars). **Searched.**
(f) **Solver repositories and cipher pages.** dbourdeau/cyphersolver, fresh shallow clone at head 54b0ac7 (23 Sept 2026
23:30 -05:00), newer than the first audit's c85ece1: fr.2980 still only at CATALOGUE.md:76 (328, "Gramont 1530 key held"),
gallica_sweep and rangone1530. Its raince/ and bethune/ folders are other volumes (fr.2984/3040/3091; fr.3484).
aaymeloglu/unsolved-ciphers head 2495c45: no fr.2980 (the "2980" and "8505" hits are DECODE record numbers of BL
items). Tomokiyo francis.htm, live (one 302 to https, then 200): the same sentence, "These undeciphered letters can be read
with Gramont's cipher (1530)". The key comes from fr.3019 f.20 and fr.3071 f.17, and there is no reading of no.22.
**Searched, catalogued not read.**
(g) **Scholarship, open indexes.** HAL (6 queries): only the PUR Gramont chapter (2011, already read). Persée (5 queries):
Fraikin, "La nonciature de France de la délivrance de Clément VII à sa mort", *MEFR* 26 (1906) pp.513-563 (a list of
nuncios and missions with Gramont's credences; the snippet was read and the full text is not served on the doc page), and
Thorel 2011 (above); nothing on this letter. CrossRef (5 queries by hand, 3 through the tool before a 429): nothing
on-topic. **OpenAlex: unreachable** (429 on the first call, again today). **Semantic Scholar: unreachable** (429, one retry
after a pause, 429). JSTOR: two rows added to JSTOR-QUEUE.tsv (the Asti interceptions; Berthault).
(h) **Not reached:** Camusat, the rest of the Francis I tract (LANE G's flag stands: read folios 1-90 densely); HathiTrust
full text (Cloudflare); *Revue des Hautes-Pyrénées* (the IA volume `revuedeshautesp00unkngoog` returned 500 for djvu;
phrase fts 0 hits; it is not known to be the 1907 volume); Simancas and Vienna intercepts (archival).

### Safe sentence

"BnF fr.2980 f.30r-v (no.22) is a letter written entirely in cipher by Gabriel de Gramont, bishop of Tarbes, to Francis I,
Rome, 20 May 1530. Tomokiyo had identified it as readable with the published Gramont 1530 key (Tomokiyo; Lasry 2023), and
Bourdeau catalogued it (328). We transcribed it from the Gallica image (one reconciled reading of two blind passes, since
compared with a third blind reader) and applied that key: the table gives values for 1500 of 1973 signs (H), and 158 more
are cryptanalytic (S, matched control), leaving 59 unread. The reading is partial. No prior printed plaintext, extract,
summary or decipherment of the letter was located after two independent audits of the editions and indexes listed in
AUDIT.md (N3). A clear-text letter of April 1530 from Gramont to the king on the same negotiation is printed in *Archivio
storico italiano*, Appendice I, pp.473-481."

### Unsafe sentences

All of the first audit's still apply. Also: "not in Sanuto or the *Archivio storico italiano*, so unpublished" (absence from
named sources is a search result; Camusat and the archives are not closed); "never intercepted" or "the imperials never
read it" (Asti interceptions are documented, and Simancas was not searched); "N4" (Camusat not read).

### Corrections made (this session)

1. status.json, the f.30 results row: grade "N3, single audit" became "N3, two audits". Its line "verifier (LANE V)
   running, no novelty class yet" was stale since the first audit and now reads "N3 after two audits; below N4 while
   Camusat is not read".
2. No over-claiming wording (new, first, unread, unpublished, never printed) about f.30 was found in AUDIT.md,
   status.json or the ROOM lines for this folder (grep). NOTES.md was not touched (the pass-C worker owns it this hour).

### Postmortem

**No failure of the first audit found. Its N3 stands.** Both named gaps were real places to look. The *ASI* index settles the
Appendice in one read, and a verifier should reach for a series' general index before per-volume greps (lesson for the
template). What the first audit could not have seen from print alone is the interception route. French letters of this
embassy were stopped at Asti, and Mai's despatches carry contemporary decipherments. So "no prior decipherment" means
"none in print". A Simancas decipherment of a Gramont letter of May 1530 would move the class, and only an archive search
(or a specialist, N5) can rule it out.

### Requests this session

archive.org: about 44 (advancedsearch 8, metadata 3, djvu.txt 21 including 3 HTTP 500s and one retry each, plus 15 by
print_check), at least 3 s apart. be-api.us.archive.org: 37 (1 by hand, 36 by print_check). www.googleapis.com (Books,
keyed, country=US, key never printed): 12, run through a copy of print_check with 3.2 s spacing. api.openalex.org: 1
(429). api.crossref.org: 8 (the last a 429). api.semanticscholar.org: 2 (429, 429). api.archives-ouvertes.fr: 6.
www.persee.fr: 6. cryptiana.web.fc2.com: 2. github.com: 2 shallow clones (deleted after). gallica.bnf.fr: 0. No logins,
no credentials printed, no decoding, no subagents.

## Camusat tract, dense read (24 Sept 2026)

LANE G access worker, for LANE V (picking up the flag left in "Print check through Gallica page images": "the next
worker on it should read the 'Lettres du Roy François premier' tract's folios 1-90 first ... rather than resampling
at wide intervals"). Not a verifier session: does not move the N3 class, does not decode. Job: read folios 1-90 of
the tract densely and compare against `reading.txt`'s and `reading_f30*.txt`'s decoded phrases and against the
target items' particulars (Gramont, cipher letters to Villandry, Rome, 20 May 1530).

**Method.** `tools/gallica_folio.py`'s prior calibration (canvas = 155 + 2×(folio−1) for folio N's recto on this
ark) was reused. Fetched the recto side of every folio 1-90 (90 canvases, `,1000`-width thumbnails; this printed
book's type is clean enough at that width to read letter headings, dates and body text directly, unlike a
manuscript hand) via a plain loop, one request at a time, ≥1.6 s apart, UA `cipher-lab research script (contact via
repository)`. 9 of the 90 hit a connection reset (HTTP code `000`); all 9 were retried once per the single-retry
rule and all 9 succeeded on retry — **0 unrecovered failures, 90/90 folio rectos read.** One further full-resolution
fetch (canvas 279, folio 63) was made to check a tentative "1530" date misread off the low-res thumbnail; the
full-resolution image corrected this to no year visible on that specific line, adjacent text dating the item to
~Sept/Oct 1531 (Louise of Savoy's death) — logged as a caught misreading, not reported as a finding.

**Verso sides (folio v) were not fetched.** This is a real gap: a letter heading that happens to land on a verso
rather than the following recto would not be caught by this scan. Given the pattern observed (letters mostly open at
the top of a fresh recto page in this edition, per the headings found), this is judged a minor residual risk, not
ruled out.

**Net result: no hit.** Across all 90 folio rectos:
- **No date of May or June 1530 appears anywhere.** Dated items found range from 16 Février 1531 (f.77r) to 21 Mai
  1532 (f.89r, the Franco-English treaty of Boulogne/Chasteaubriant), with one isolated outlier at 11 Septembre
  1566 (f.54r, a description of the kingdom of Poland, unrelated). The tract is not in date order (the volume's own
  editorial aside at f.57r, "AV LECTEVR... me contrainct de laisser l'ordre des dates", says so directly), but no
  amount of resampling within this span turned up 1530 at all — every dated item sits in 1531-1533.
- **"Villandry"/"Villandre" does not appear in folios 1-90** (the earlier pass's only hit for this name was folio
  180, outside this range — Gap (2) of "Toward N4" narrows further but is not closed: ~127 folios, 91-217, remain
  unread).
- **"Tarbes" does not appear in folios 1-90.**
- **Gramont is named five times, always as a third party, never as a letter's author or addressee**: f.2r-3r
  ("COPPIE DES LETTRES DES CARDINAVX de Tournon & de Gramont au Roy François du 21. Ianvier à Boulogne 1532" — a
  letter jointly signed by Tournon and Gramont, but dated January 1532 at Boulogne, eighteen months after the
  target and about a different matter — the Bologna/England negotiations, not a Villandry letter); f.34r (a royal
  letter mentioning "mon Cousin le Cardinal de Grãmont" and his efforts over "l'abolition & suspension des
  privileges", Fontainebleau, 10 Juillet 1531); f.64r (a royal letter to the Bishop of Auxerre mentioning Cardinal
  de Gramont's efforts over a "bulle" and "dispense" for a marriage, Chantilly, 16 Septembre 1531); f.82r-83r and
  f.84r (two royal letters to the Bailly de Troyes, England, both mentioning "les Cardinaux de Tournon & de Grãmont"
  as royal agents active with the Pope, undated on the visible page but sitting among 1531-1532 material). None of
  the five is a Gramont-authored letter, none is addressed to Villandry, none carries the target date.
- **No overlap** was spotted between any of these 90 folios' visible text and reading.txt's or reading_f30's
  distinctive decoded phrases ("le porteur", "l'adresse de dessus", "du vingtiesme", "pour vous donner cognoissance
  de tout", "la declaration de la liberté de Florence", "la ville et la force entre vos mains") — this is a
  non-rigorous visual scan at thumbnail resolution, not a phrase-searchable OCR pass (the whole reason this tract
  needs page images at all is that Gallica's own OCR/`.texteBrut` route is altcha-walled for this ark), so it is a
  read, not a search, same caveat as the first sampling pass.
- The tract's own structure, now clearer from a dense pass: folios 1-57 run under the header "Historiques" (mixed
  royal/ambassadorial correspondence, chiefly Auxerre's and the Bailly de Troyes' own dispatches, 1531-1533, with
  the Hungary sub-dossier at f.48r-51r and the 1566 Poland outlier at f.54r); folios 58-90 run under "Memoires ou
  meslanges" (ransom/obligation terms from the 1529 Cambray treaty, Swiss-canton articles, more Auxerre
  correspondence, then the Franco-English treaty text of May 1532 from f.85r to past f.90). Nothing in this
  structure suggests the 1530 Rome correspondence is filed nearby, just outside folio 90 — the Gramont mentions are
  scattered through both halves, and the volume is demonstrably not chronological, so this is not a strong signal
  either way about folios 91-217.

**Recommendation (not a class change — this worker does not move the class).** Folios 1-90 recto can be struck
from "still open": this specific span, read recto-side, contains no May 1530 material and no Gramont-authored or
Villandry-addressed letter. Camusat is not closed overall — ~127 folios (91-217) remain, plus the verso gap noted
above within 1-90. The next Camusat pass should (a) continue the recto read from folio 91, same method and same
calibration, and (b) if budget allows, spot-check versos in the 1-90 range near the five Gramont mentions above
(f.2v-3v, f.34v, f.64v, f.82v-84v) on the chance a companion or continuation letter sits there unseen by this
recto-only pass. N3 should stay N3.

### Requests this session

gallica.bnf.fr: 101 (1 initial single-canvas thumbnail check of f.155 before scripting the loop, 90 recto
thumbnails in the main loop — 81 succeeded first try, 9 hit a connection reset and were each retried once
successfully per the single-retry rule — plus 1 full-resolution re-fetch of canvas 279/folio 63 to correct a
tentative misreading). All ≥1.6 s apart, one request at a time, UA `cipher-lab research script (contact via
repository)`, shared with this session's Part A (fr5160, 1 request) under the LANE G two-fetcher/~110-request
courtesy cap — no more Gallica requests taken this session after this pass, to leave headroom for the other LANE G
fetcher (M18). No other host. No logins, no credentials, no decoding, no subagents. Images:
`images/print_check/camusat_dense/manifest.json` (all 90 folios logged: canvas, url, date/heading tag) plus a
10-image representative sample (title page + every Gramont-mention page + the two section-boundary pages) kept on
disk; the other 80 thumbnails were fetched, read from disk this session, and then deleted (not committed) to stay
under the 30 MB/folder cap — re-fetch any of them from the manifest's per-folio url, one request, in seconds.

## N4 decision, 24 Sept 2026

LANE V verifier, 05:08-05:15 UTC (`date -u` read), orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ. This session did
none of the solving, auditing or gap work above and did no decoding. Question: does the logged coverage of no.21
(f.29r, Gramont to Villandry) and no.22 (f.30r-v, Gramont to Francis I), both Rome, 20 May [1530] (f.30 dated 1530), each N3 after two
audits, now meet rule 10's N4?

**Answer: no, for both items. Each stays N3** (status.json unchanged). Two principal families are still uncovered, and
they are the same for both letters. (1) Camusat's *Meslanges historiques*: the tract "Lettres du Roy François premier
et instructions a ses ambassadeurs ... ensemble les memoires & lettres desdicts Ambassadeurs" has been read for folios
1-90 recto only. Folios 91-217 are unread, and the tract holds a letter to Villandry at f.180. (2) DECODE: nothing has
been written under "DECODE search" in this file yet. LANE N was asked at 05:07 UTC.

### 1. Principal families: covered or not

| family | no.21 f.29r | no.22 f.30 | where logged |
|---|---|---|---|
| Le Grand, *Histoire du divorce* III (*Preuves*), I, II | covered. The MDZ OCR was read page by page for pp.394-542, with a dateline sequence and a phrase search. v.1-2 and pp.1-393 were checked by EF tokens | covered, same pages. f.30's phrases were run through print_check | second audit, "Gap (1) closed"; f.30 second audit (e) |
| **Camusat, *Meslanges historiques*** (1619; the 1644 ed. on Gallica, bpt6k5039434) | **not covered.** Folios 1-90 recto of the Francis I tract were read with no hit. Folios 91-217 are unread (9 were sampled earlier, among them f.180, "A Monsieur de Villandre du 4 Decembre 1531"), and so are the versos of 1-90. The tract prints letters to Villandry and ambassadors' letters on the divorce affair, so it is the one French edition that could print either letter | **not covered**, same tract. It prints ambassadors' letters to the king | "Print check through Gallica page images"; "Camusat tract, dense read" |
| Champollion-Figeac, *Captivité* (1847) | covered: the volume's own table limits it to Oct 1524-Apr 1526 | covered, same | "Print check through Gallica page images" |
| Pocock, *Records of the Reformation* I-II | covered, full text | covered (4(c), shared) | section 4(c) |
| Ehses, *Römische Dokumente* | covered, full text | covered (shared) | section 4(c) |
| *L&P Henry VIII* iv.3; *State Papers* VII | covered, full text; no Gramont item of 20 May | covered, re-grepped for Florence/Avignon | section 4(a); f.30 (a) |
| L&P *Addenda* I (1929) | unreached (not on IA). **Not principal for this item**: the Addenda calendar English-held papers, and this letter is a BnF original with no English copy | same | section 4(a) |
| CSP Spanish IV, CSP Venetian IV | covered, full text | covered, re-grepped, including the Asti interceptions (p.603) | section 4(a); f.30 (a); f.30 second audit (a) |
| CSP Milan | unreached. **Not principal** (Milanese-held papers) | same | section 4(a) |
| Desjardins/Canestrini, *Négociations ... Toscane* II | covered through the shared embassy search | covered, full text | f.30 (b); f.30 second audit (b) |
| *Archivio storico italiano*, Appendice I-IX and the general index | covered (general index: one Tarbes item, the April letter) | covered; App. I doc. XXXVIII is the sibling April letter and was tested as a different letter | f.30 (b); f.30 second audit 1 |
| Sanuto, *Diarii* 52-54 | covered (index columns read in context) | covered | f.30 second audit 2 |
| Molini, *Documenti di storia italiana* | covered: 8505 prints only item 23 | covered | section 4(c); f.30 second audit (b) |
| Ribier, *Lettres et mémoires d'estat* | covered, full text, three scans | covered, re-grepped | section 4(b); f.30 second audit (b) |
| *Catalogue des actes de François Ier* I, VI, VII, IX | covered: IX [412] (p.61; not [411], corrected by verifier V2) gives existence and date only | covered | section 4(c); f.30 second audit (b) |
| BnF catalogue of fr.2980 (cc494342) and the BnF finding aids | covered: no bibliography, and no decipherment in the volume (Raince test). fr.3038 no.19 is the Bologna decipherment | covered: no recipient given for no.22 | second audit, Raince test; f.30 (c) |
| *Catalogue de la collection Dupuy* | covered (15 May letter to Du Prat, Dupuy 452) | covered | f.30 (b) |
| Sender and recipient studies: Hamon (Breton de Villandry, PUR 2011; not Rentet, corrected by verifier V2), Michon (Gramont, PUR 2011), Decrue, Scheurer I, Bourrilly | covered | covered | sections 4(b), second audit (c) |
| Michon, *La Crosse et le Sceptre* (2008) | unreachable (Google Books NO_PAGES). **Not principal for a print of the letter**: his PUR chapter on Gramont (2011) was read in full and cites no fr.2980 and no cipher. Noted as the residual specialist gap | same | "Toward N4"; section 4(b) |
| Tomokiyo, francis.htm and GL.htm | covered, live twice. "These undeciphered letters can be read with Gramont's cipher (1530)": no reading. GL.htm (cached 23 Sept 2026, re-grepped this session) has no mention of fr.2980 or Villandry: Lasry's Gramont list is fr.3040, fr.3091, fr.3071 and Clair.330 | covered, same | section 4(f); f.30 second audit (f); this section, 2 |
| Lasry's publications | covered: CrossRef and Google Scholar list no Gramont article. His 2023 Gramont work is known only through Tomokiyo's GL.htm, which does not claim nos.21-22 | covered | open-index pass row 7; this section, 2 |
| Bourdeau, dbourdeau/cyphersolver (main and all ten PR heads) | covered: CATALOGUE.md:76 (328, "key held"); no file or reading for fr.2980 at main ce81527 (24 Sept 2026 00:11 -05:00) or at PR heads 1-10, including arya1515's PRs 7-10 | covered, same | this section, 2; earlier heads in the audits |
| Aymeloglu, aaymeloglu/unsolved-ciphers | covered: head 2495c45. Its DECODE dump has three Gramont records (fr.3040 f.16 and f.18, fr.3091 f.45-47), none of them fr.2980 | covered | this section, 2; f.30 (e) |
| **DECODE (de-crypt.org)** | **not covered.** No "DECODE search" section exists here, and live search is LANE N's. Aymeloglu's dump of the catalogue (see above) is indirect evidence only, because it is a third-party snapshot, not a search | **not covered** | ROOM.md 05:07 UTC request |
| Phrase search on the decoded text (IA, Google Books, print_check) | covered, two audits | covered, two audits | section 4(e); second audit (e); f.30 (d); f.30 second audit (e) |
| Open indexes | CrossRef, HAL, Persée, Google Scholar: covered, several passes. OpenAlex and Semantic Scholar: 429 at every attempt today, this session's included. Unreachable and logged. They do not block N4 on their own (Danzay precedent) | same | open-index pass; f.30 (f); this section, 2 |
| JSTOR | 11 rows queued (2-7, 27-29, 33-34). Under the verifier template a queued row does not block N4 | same | JSTOR-QUEUE.tsv |
| HathiTrust full text | unreachable (Cloudflare). It is a search route, not an edition: the editions it would reach are covered above by IA, MDZ or HTRC EF | same | "Toward N4" |
| Simancas and Vienna intercepts | archival. N4 does not require internal or unpublished work to be excluded | archival, same | f.30 second audit 3 |

### 2. What this session searched (one pass)

- **OpenAlex**: 3 queries (Gramont Tarbes 1530; Gramont cipher Francis; Gabriel de Gramont), all 429 ("$0 remaining;
  resets at midnight UTC"). Stopped.
- **Semantic Scholar**: 1 query, 429; 1 retry after 45 s, 429. Stopped.
- **CrossRef**, 4 queries (Lasry Gramont cipher; Tomokiyo Francis cipher; Gramont Tarbes Rome 1530 ambassade;
  chiffre diplomatique François Ier 1530). Lasry's hits are the 2016 and 2022 *Cryptologia* papers and the HistoCrypt
  papers of 2022 (papal 1721) and 2023 (Armand de Bourbon 1649). None is on Gramont. Everything else is noise.
- **WebSearch**, 4 queries (fr.2980 Gramont deciphered Villandry; Lasry Gramont 1530 2023; arya1515 cyphersolver
  Gramont 2980; ciphermuseum Lasry Gramont). They surfaced Bourdeau's site and forks of his repository
  (arya1515/cyphersolver, aryasn2026/cyphersolver), whose work reaches Bourdeau as PRs 7-10. They also surfaced a
  Cipher Museum page on Lasry, whose search summary names no Rome 1530 letter (the page was not fetched: host not
  on this session's list). The Gramont letters read in the Bourdeau line are 11 Oct 1529 and 21 July 1530, not
  nos.21-22.
- **dbourdeau/cyphersolver**: shallow clone of main (ce81527) plus every `refs/pull/*/head`, grepped for 2980,
  btv1b9059991d, Villandr and 8505. The only hits are CATALOGUE.md:76 and the gallica_sweep candidate line; the rest
  are numeric collisions. Deleted after.
- **aaymeloglu/unsolved-ciphers**: shallow clone at 2495c45 (unchanged). Grepped, then deleted.
- **Tomokiyo GL.htm** (cached copy, 23 Sept 2026): no fr.2980 and no Villandry. francis.htm §"BnF fr.2980 (1530)":
  "These undeciphered letters can be read with Gramont's cipher (1530) below", and nothing more.
  Neither page says either letter has been deciphered.

### 3. Decision

**no.21 (f.29r): N3 stays. no.22 (f.30r-v): N3 stays.** Every calendar, documentary edition, catalogue and project
page in the table is covered, except for two principal families:
1. **Camusat, folios 91-217 of the Francis I tract**, and the versos of 1-90 near the Gramont mentions (f.2v-3v, f.34v,
   f.64v, f.82v-84v). This is the one French printed collection of royal and ambassadorial letters of 1531-33 on the
   divorce affair, and it prints a letter to Villandry. Folios 1-90 hold no 1530 date. That is a good sign but does
   not settle the question, because the tract says itself that it is out of date order (f.57r). About 127 recto pages
   remain, one LANE G session with the same calibration (canvas = 155 + 2×(folio−1)). **Asked of LANE G in ROOM.md.**
2. **DECODE.** One catalogue search for Gramont / Tarbes / "fr. 2980" / "Français 2980" / 1530 closes it (LANE N,
   requested at 05:07 UTC).

If both come back negative, the next verifier can assign N4 to both items without repeating anything else. Nothing
found here lowers either class.

**Safe sentences (N3, current):** those of the second audit (f.29r, "Second audit (adversarial)", Verdict, with the
second-reader counts 568 / H 533 / M 30 / U 5) and of the f.30 second audit ("Safe sentence"). Both credit Tomokiyo's
identification, the published key (Tomokiyo; Lasry 2023) and Bourdeau's catalogue 328, and neither may be shortened.

**Sentences for N4 only, not to be used until the two gaps close:**
- no.21: "No prior decipherment located of Gabriel de Gramont's cipher letter to Jean Breton de Villandry, Rome, 20 May
  1530 (BnF fr.2980 f.29r, no.21). It was identified as readable by Tomokiyo and catalogued by Bourdeau (328), and we
  read it here in part with the Gramont 1530 key published by Tomokiyo and Lasry (2023). Search log in AUDIT.md."
- no.22: "No prior decipherment located of Gabriel de Gramont's all-cipher letter to Francis I, Rome, 20 May 1530 (BnF
  fr.2980 f.30r-v, no.22). It was identified as readable by Tomokiyo and catalogued by Bourdeau (328), and we read it
  here in part with the Gramont 1530 key published by Tomokiyo and Lasry (2023), plus 158 signs at grade S. Search log
  in AUDIT.md."

**Unsafe sentences:** "N4" or "no prior decipherment located" today (Camusat and DECODE are open); "first decipherment",
"previously unread", "newly recovered", "unpublished" (not allowed at N3); "we broke Gramont's cipher" (the key is
Tomokiyo's and Lasry's); "read in full" or "1500 of 1973 signs read" (the reading is partial, on one reconciled
transcription); "Cardinal Gramont" on 20 May 1530; "Gramont to Villandry" for f.30.

### 4. Outreach gates (CLAUDE.md Outreach 1-6), both items

| gate | state |
|---|---|
| 1. verifier class in AUDIT.md | **met** (N3, both) |
| 2. above N1: second adversarial audit, open-index pass, Google Books queries, JSTOR rows answered or waived | second audit **met** (both). Open-index pass **met** except for OpenAlex and Semantic Scholar, which are unreachable and logged. Google Books **met**. JSTOR rows 2-7, 27-29 and 33-34 **not met**: they are queued, neither answered nor waived |
| 3. message is the safe sentence, states the prior print it rests on (Tomokiyo's francis.htm key; Lasry via GL.htm; Bourdeau 328), links AUDIT.md | **not met**: no draft exists |
| 4. rule 10 wording | only the N3 safe sentences may be used |
| 5. logged in CONTRIBUTIONS.md before sending | **not met** |
| 6. verifiable links: repository folder; Gallica ark btv1b9059991d at the leaf (f.29r, f.30r-v); Tomokiyo's francis.htm; for f.30, ASI App. I pp.473-481 (IA `archiviostoricoi01fireuoft`) as the closest print | links available; **not met** until a draft carries them |

**Postmortem.** No over-claim was found (grep of the folder's .md files and the status.json rows for new/first/unread/
unpublished/never printed: the only hits are rule-10 reminders and unsafe-sentence lists). The error to avoid is
the one the Danzay decision recorded: an audit that narrows a gap ("Camusat ff.1-90: no hit") must not be summarised
upward as "Camusat closed". The f.30 second audit's "Not raised to N4 because Camusat ... is sampled, not read" still
holds for ff.91-217. A lesson for the verifier template: grep a solver repository's `refs/pull/*/head` as well as
main. Bourdeau's forks (arya1515) reach it only as PRs, and none of the earlier audits here fetched them.

Requests this session: api.openalex.org 3 (429), api.semanticscholar.org 2 (429), api.crossref.org 4, github.com 2
shallow clones plus 1 PR-ref fetch (deleted after), WebSearch 4. No Gallica, no de-crypt.org, no Google Books, no
archive.org, no logins, no decoding, no subagents.

## Camusat tract, folios 91-217

LANE G print-check worker (Sonnet, for LANE V, orchestrator session_014zWyan51u9qMn9gnHpm1Aq), 05:18-05:34 UTC
(`date -u` read at start and end). Not a verifier session: does not move the N3 class, does not decode. Job:
continue the "Camusat tract, dense read" pass (which covered folios 1-90 recto) through the rest of the tract,
folios 91-217 recto, plus versos f.2v-3v/f.34v/f.64v/f.82v-84v (the brief's original list, near the five known
Gramont mentions in 1-90) — read against `reading.txt`'s and `reading_f30*.txt`'s decoded phrases and the target
items' particulars (Gramont, cipher letters to Villandry, Rome, 20 May 1530).

**Method.** Same calibration as the prior pass: canvas = 155+2×(folio−1) for folio N's recto, verso = recto+1;
this was re-verified against the printed folio numbers visible on the page images themselves (e.g. canvas 496
prints "171" in the running head) — no offset drift found across the whole range. 124 recto folios were fetched
(91-217 minus 120/150/180, already read and logged with content in the earlier sampling pass and in "N4 decision,
24 Sept 2026" §1), plus the 7 requested versos, all at `,1000`-width thumbnails, one request at a time, ≥1.6-1.8 s
apart, UA `cipher-lab research script (contact via repository)`, `--max-time 30`. **131/131 succeeded** (one
connection reset on f.174v retried once successfully per the single-retry rule; no altcha/403/429 seen).

**Mid-pass extension (not in the original brief, added because it bore directly on the question).** A recto page
came back visibly blank (canvas 495, f.171r — confirmed genuinely blank by two independent fetches, thumbnail and
native resolution, not a fetch failure). Checking its verso (canvas 496, printed folio "171") turned up an
editorial note announcing a **late-added dossier of Henry VIII divorce-affair documents**, followed immediately by
a real "LETTRES DE MONSIEVR LE CARDINAL DE GRAMONT à nostre S. Pere pour l'affaire du Roy d'Angleterre" heading —
i.e. genuine Gramont-authored letters to the Pope, in this very tract, on the right general subject. This was
worth chasing past the brief's original verso list: 6 further versos (f.172v-177v) were fetched (all succeeded,
1 retry on f.174v) to read the dossier in full rather than recto-only, since a letter opening on a verso in this
specific span would otherwise be missed. Total Gallica requests this session: **141** (131 in the main recto+brief-
verso batch + 2 for the blank-page recheck + 6 dossier-verso extension + 2 earlier isolated re-fetches), under the
brief's ~160 cap and shared with the other LANE G Gallica fetcher per the two-fetcher/1.5s+/UA courtesy rule.

**Net result: no hit.** Across all 131 folio-sides read this session:

- **No date of May 1530 appears anywhere.** The tract's dated items in this range run continuously from Chasteau-
  Briant 16 May 1531 (f.92r) through Arles 5 Octobre 1533 (f.141r) and on to Lyon/Venise items into 1534 (f.178r,
  Trivulzio, 16 Avril 1534), with a retrospective letter at f.155r referring back to the King's 1525 Spanish
  captivity (still not 1530), plus a run of undated Rome-affair letters at f.181r-211r independently dated by
  their own headers to Feburier-Aoust 1532. No 1530 material at all was found in 91-217, matching the "not in date
  order" pattern already established for 1-90.
- **"Villandry"/"Villandre" does not appear in folios 91-217 recto or in the 13 versos read** (the one earlier hit,
  f.180, "A Monsieur de Villandre du 4 Decembre 1531", was already logged in the prior sampling pass and is dated
  18 months after the target, addressing an unrelated Auditor-of-the-Chamber matter).
- **"Tarbes" does not appear anywhere in this range.**
- **Gramont is named repeatedly, always as a third party or joint addressee, never alone as a letter's author to
  Villandry or the King, with one partial exception (see next point).** He appears paired with Tournon as royal
  agents/cardinals travelling to and residing at Rome (f.98r, f.108r, f.112r [a memoire addressed to both
  jointly, not authored by either], f.117r, f.118r, f.121r, f.123r, f.126r-f.127r, f.129r, f.132r, f.189r, f.207r,
  f.210r-f.211r), always dated 1531-1533, never 1530, never Villandry-addressed.
- **The one real exception: f.171v-178r, "Lettres de Monsieur le Cardinal de Gramont à nostre S. Pere pour
  l'affaire du Roy d'Angleterre".** This is a distinct, late-added dossier (its own editorial preface at f.171v
  says the pieces "sont venues en mes mains" after the main tract was already printed) of genuine Gramont-authored
  Latin/French letters to Pope Clement VII and to the Legate/grand Maistre about Henry VIII's divorce — the
  closest thing to the target's subject matter found anywhere in this tract. Every dated item inside it, however,
  is Janvier-Iuillet 1532 through the closing letter (Pomponio Trivulzio, Lyon, 16 Avril 1534, "Fin des lettres de
  l'affaire d'Angleterre"): **no 20 May 1530 letter, and every letter in the dossier is addressed to the Pope, the
  Legate or the grand Maistre — none to Villandry or to the King.** This does not match no.21 (f.29r, to Villandry)
  or no.22 (f.30, to Francis I) on date, addressee or the pattern of both letters being from Gramont directly.
- **No overlap** between any of these 131 folio-sides' visible text and reading.txt's/reading_f30's distinctive
  decoded phrases ("le porteur", "l'adresse de dessus", "du vingtiesme", "pour vous donner cognoissance de tout",
  "la declaration de la liberté de Florence", "la ville et la force entre vos mains") — same non-rigorous visual-
  scan caveat as the first two passes (Gallica's OCR route is altcha-walled for this ark).
- **Structural finding: the tract's own text ends "FIN" at f.211r**, signed by Chancelier du Prat, dated Abbeuille
  28 Decembre [1532] — not at f.217 as the binder's cahier note implied. Folios 212r-217r are printer's filler
  inside the same gathering: Deschenetz/Dinteville family genealogical notes (spanning 1531-1619), a 1438 legal
  deed, and Troyes municipal documents from 1429 and (an extract) 1594. None of this is diplomatic correspondence
  and none of it was searched for anything beyond a visual read for names/dates — no Gramont/Villandry/1530
  content, as expected for its subject matter.

**Recommendation (not a class change — this worker does not move the class).** Camusat's *Meslanges historiques*
tract can now be struck from "still open" in its entirety: folios 1-217 recto have been read (dense pass 1-90,
this pass 91-217), plus 13 versos targeted at every known Gramont mention and at the one verso-side dossier this
pass turned up. No 20 May 1530 letter from Gramont to Villandry or the King was found. The remaining gap is the
same one both prior passes flagged: verso sides outside the 13 read here were not fetched, so a letter heading
landing on one of the other ~200 unread versos in 91-217 is not ruled out — judged the same "minor residual risk"
as for 1-90, not a reason to keep the family open pending exhaustive verso coverage, given the dense recto pattern
(letters open at the top of a fresh recto in this edition) held everywhere it was checked in this pass too.
AUDIT.md "N4 decision, 24 Sept 2026" §1 row for Camusat should be updated by the next verifier session to "covered
(91-217 recto + 13 targeted versos read, no hit; see 'Camusat tract, folios 91-217')" — this worker does not edit
that table itself, per its brief. The other principal-family gap (DECODE search, LANE N) is unaffected by this
session.

### Images

`images/print_check/camusat_dense/manifest_91_217.json` logs all 137 folio-sides read this session (folio, canvas,
url, one-line content note; every one of the 131 fetched images was viewed). 4 representative images are
committed (`camusat_f171v_dossier_start.jpg`, `camusat_f172r_gramont_header.jpg`, `camusat_f178r_dossier_end.jpg`,
`camusat_f211r_fin.jpg`); the other 127 fetched images were read from disk this session and then deleted (not
committed) to stay under the 30 MB/folder cap — re-fetch any of them from the manifest's per-folio url, one
request, in seconds.

### Requests this session

gallica.bnf.fr: 141 (see Method above for the breakdown), all ≥1.5-1.8 s apart, one request at a time, UA
`cipher-lab research script (contact via repository)`, shared with the other LANE G Gallica fetcher per the
two-fetcher courtesy cap — no other host. No logins, no credentials, no decoding, no subagents, no edits to
reading.txt/key.tsv/ciphertext.txt/reading_f30*.txt.

## DECODE search, 24 Sept 2026

LANE N DECODE worker B (Sonnet), 06:51-07:20 UTC (`date -u` read). Closes the "DECODE" row of the N4 decision
table above (05:08 UTC). This session did no decoding, no class change, no promotion.

### Method

The RecordsSearch advanced-search form POSTs to `RecordsSearch`, but every field it submits (not only
`x_status`/`x_record_type`, the two `tools/decode_list.py` already used) redirects to a plain, repeatable GET
on `RecordsList` — confirmed by submitting the live form once in a headless browser
(`x_c_holder=Gramont` → `RecordsList?x_c_holder=Gramont&z_c_holder=LIKE&cmd=search`) and then reproducing the
same URL with plain `curl`, no cookies, no login. One correction to `tools/decode_list.py`'s own discovery note:
the static HTML the server returns for a `RecordsList` GET **does** include the full result grid server-side
(no client-side AJAX render needed) — a `curl` fetch of `RecordsList?...&cmd=search` and a real-browser fetch of
the same URL contain the same `<table id="tbl_recordslist">` rows, confirmed byte-for-byte on the same query. An
earlier version of this session's own search script wrongly treated the fixed boilerplate string "No records
found" (present in the page's empty-state markup on every response, hit or no hit) as a negative signal and
under-reported every real hit as zero; the fix was to count `RecordsView/<id>` links in the response instead.
Recorded here so the next DECODE search does not repeat it.

Fields searched (from `RecordsSearch`'s own form, no login needed): `x_sender`, `x_receiver`, `x_c_holder`
(location + shelfmark), `x_additional_information` (catalogue notes), `x_origin_city`, plus `x_start_year`/
`y_start_year` (BETWEEN) for a date-range check. All are `LIKE` (substring) searches, so "2980" alone covers
"fr. 2980" and "Français 2980" as substrings; a separate query for each spelling was not needed. Not restricted
to any record type or status (all four statuses, all three record types are the GET default with no
`x_status`/`x_record_type` param set) — checked against a plain `origin_city=Rome` query returning `Cipher`,
`Key` and mixed-status rows together, confirming no implicit filter.

### Queries and results

| field | term | url | hits (ids) |
|---|---|---|---|
| sender | Gramont | `RecordsList?z_sender=LIKE&x_sender=Gramont&cmd=search` | 4: 3698, 4225, 4226, 4227 |
| sender | Tarbes | `RecordsList?z_sender=LIKE&x_sender=Tarbes&cmd=search` | same 4 (Tarbes is part of the sender string "Gabriel de Gramont, bishop of Tarbes") |
| receiver | Gramont | `RecordsList?z_receiver=LIKE&x_receiver=Gramont&cmd=search` | 0 |
| receiver | Tarbes | `RecordsList?z_receiver=LIKE&x_receiver=Tarbes&cmd=search` | 0 |
| c_holder | Gramont | `RecordsList?z_c_holder=LIKE&x_c_holder=Gramont&cmd=search` | 0 |
| c_holder | Tarbes | `RecordsList?z_c_holder=LIKE&x_c_holder=Tarbes&cmd=search` | 0 |
| c_holder | 2980 | `RecordsList?z_c_holder=LIKE&x_c_holder=2980&cmd=search` | 0 |
| c_holder | Villandry | `RecordsList?z_c_holder=LIKE&x_c_holder=Villandry&cmd=search` | 0 |
| sender | Villandry | `RecordsList?z_sender=LIKE&x_sender=Villandry&cmd=search` | 0 |
| receiver | Villandry | `RecordsList?z_receiver=LIKE&x_receiver=Villandry&cmd=search` | 0 |
| additional_information | Villandry | `RecordsList?z_additional_information=LIKE&x_additional_information=Villandry&cmd=search` | 0 |
| additional_information | Gramont | `RecordsList?z_additional_information=LIKE&x_additional_information=Gramont&cmd=search` | 1: 9473 |
| additional_information | Tarbes | `RecordsList?z_additional_information=LIKE&x_additional_information=Tarbes&cmd=search` | 0 |
| additional_information | 2980 | `RecordsList?z_additional_information=LIKE&x_additional_information=2980&cmd=search` | 2: 4736, 4761 |
| sender | 2980 | `RecordsList?z_sender=LIKE&x_sender=2980&cmd=search` | 0 |
| receiver | 2980 | `RecordsList?z_receiver=LIKE&x_receiver=2980&cmd=search` | 0 |
| origin_city | Rome | `RecordsList?z_origin_city=LIKE&x_origin_city=Rome&cmd=search` | 20 (page 1 only; not paged further — see below) |
| origin_city=Rome AND start_year 1528-1532 | — | `RecordsList?z_origin_city=LIKE&x_origin_city=Rome&z_start_year=BETWEEN&x_start_year=1528&y_start_year=1532&cmd=search` | 5: 9960, 9961, 9962 (Simancas, Spanish, Muxetula), 4226, 3696 (both BnF Gramont-series, below) |

### What the hits are

- **id 9473** ("additional_information" contains "Gramont"): "Cardinal de Gramont" appears in the notes of a Key
  record, Paris BnF NAF 4206 no.11 — a different manuscript series (Nouvelles acquisitions françaises, not
  Français), no date shown, `RecordsView` needs login to read further. Not fr.2980.
- **ids 3698, 4225, 4226, 4227** (sender = "Gabriel de Gramont, bishop of Tarbes"): all BnF Français 3040 and
  3091, addressed to Anne de Montmorency — the same Gramont-to-Grand-Master series Tomokiyo's francis.htm and
  Bourdeau's `gramont1529` already cover (Lasry's "Gramont's cipher (1530)" and "(1529)" keys). Grid columns:
  id 4227 Français 3040 f.18 (Boulogne, 1520-1539, Non-decrypted); id 4226 Français 3040 f.16 (Rome, 1529-,
  Non-decrypted); id 4225 Français 3040 f.12 (Rome, 1520-1539, **Decrypted**); id 3698 Français 3091 f.45-47
  (Rome, 1520-1540, Non-decrypted). None is Français 2980, none is dated 20 May 1530, and id 4225's Decrypted
  status matches what Bourdeau's `gramont1529/NOTES.md` already reports for that leaf (part of "Gramont's cipher
  (1529)"/"(1530)" group, not this target).
- **ids 4736, 4761** ("2980" in additional_information): both Klášter u Nepomuka (Czech regional archive),
  Kurtz von Senftenau to Trauttmansdorff, 1639, German/Latin — "2980" is an unrelated inventory or page number in
  the notes field. Not fr.2980, wrong century, wrong archive.
- **origin_city=Rome, 1528-1532**: id 4226 (above, Français 3040) and id 3696 (Français 3091 f.19, Rome, 1529-,
  Decrypted) are the same Gramont-to-Montmorency series; ids 9960-9962 are Simancas (Spanish), Antonio Muxetula's
  1531 cipher correspondence — a different ambassador, different archive, unrelated to fr.2980.

**No record for BnF Français 2980, no.21 or no.22, and no record naming Villandry, in any field searched.**
This matches the repo's own read of Bourdeau's CATALOGUE.md line 76 ("Gramont to Villandry, Rome (BnF fr. 2980
nos. 21-22, ff. 29-30; catalogue 328): Gramont 1530 key held") and Aymeloglu's cached DECODE dump (grepped
earlier this session, no fr.2980 rows): DECODE's own catalogue simply does not carry this shelfmark. The
Gramont-to-Montmorency letters DECODE does carry (fr.3040, fr.3091) are a different, already-published series
(Tomokiyo/Lasry keys, Bourdeau's `gramont1529` reading) and are not evidence for or against nos.21-22.

### Requests this session (de-crypt.org)

1 RecordsSearch page fetch, 1 headless-browser form submission (confirming the GET redirect pattern), ~24
`RecordsList` GET queries for this target (table above), all ≥1.6 s apart, one request at a time, UA
`cipher-lab research script (contact via repository)`. No login, no credentials touched, no images or documents
fetched. (The Danzay search below shares this session and its own request count is logged there; combined
this session's de-crypt.org total is under the brief's 150-request cap — see the final report.)

**DECODE family in the N4 table above: now covered, no hit.** The other open family (Camusat ff.91-217) was
separately closed negative by LANE G at 05:37 UTC (see "Camusat tract, folios 91-217" above). Both principal
families the 05:08 N4 decision named are now closed; a fresh N4-decision verifier can act on this without
further search, per that section's own words ("If both come back negative, the next verifier can assign N4 to
both items without repeating anything else"). This worker does not assign N4 (not its brief).

## N4 decision (final families), 24 Sept 2026

LANE V N4-decision verifier (Opus, session_01FwWKsqwM57oancfisEiVEE, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ),
06:54-07:03 UTC (`date -u` read). This session took no part in any solving, auditing, transcription or gap work above.
It did not decode. It re-checked the 05:08 table against the whole file, looked for principal families that table
missed, and closed the small reachable ones in one logged pass.

**Answer: no.21 (f.29r) N4; no.22 (f.30r-v) N4.** Both classes carry the rule-10 qualifier "no prior decipherment
located". Internal or unpublished work is not excluded.

### 1. The 05:08 table re-checked

- **Camusat ff.91-217: accepted as covered.** LANE G read 124 rectos plus 13 versos, and the verso dossier f.171v-178r
  in full ("Camusat tract, folios 91-217"). The tract's letters run from 16 May 1531 to 1534, with no 1530 date,
  no Tarbes and no letter to Villandry after f.180 (4 Dec 1531). The Gramont dossier is 1532-34, addressed to the
  Pope, the Legate and the grand maître. What is left is the unread versos. Letters in this edition open on a recto,
  and the chronology held across the whole tract, so this is a residual risk, not an open family.
- **Camusat, 1619 against 1644 (new check).** Every page read was in the 1644 Gallica copy (bpt6k5039434). Google
  Books lists two 1619 issues (`MKpSAAAAcAAJ`, 778 pp.; `1d19ZkCU0v8C`, 844 pp. with the *formulaire*). I searched both
  through the keyed API for two markers found in the 1644 copy. "A Monsieur de Villandre" returns `1d19ZkCU0v8C`
  with "du 4. Decembre 1531", the same letter as 1644 f.180. "Cardinal de Gramont" plus "affaire du Roy d'Angleterre"
  returns both 1619 issues with "du 7 Feburier ... à nostre S. Pere", the late dossier of 1644 f.171v-178r. The 1644
  copy's filler genealogies also stop at 1619 (LANE G). So the 1644 is treated as a reissue of the 1619 sheets and
  the family counts as covered. That the two editions are identical was not proven folio by folio.
- **DECODE: accepted as covered.** I checked the method as briefed. The worker's first script treated DECODE's
  empty-state text ("No records found", which appears on every page) as a zero and under-reported hits. The fix
  counts `RecordsView/<id>` links instead. The table in "DECODE search" was produced by the corrected method: its
  non-zero rows (sender Gramont 4, additional_information Gramont 1 and 2980 2, Rome 1528-32 5) name ids, grid
  columns and statuses, and the old method would have shown zero for all of them. The section does not say that
  each zero row was re-run after the fix, so I tested that independently from the repo's own login-free census,
  `sources/decode/records-non-decrypted-2026-09-24.tsv` (1,186 Non-decrypted and Partially decrypted Cipher records,
  collected by another route). It has ids 3698, 4226 and 4227 (Gramont, fr.3040/3091), as the live search found,
  and no row with 2980, Villandr, Gramont outside those, or Tarbe. A *Decrypted* fr.2980 record would be missed by the
  census. It would still have come up under sender = Gramont/Tarbes, a post-fix query whose four hits include the
  Decrypted id 4225, because DECODE files this BnF series under "Gabriel de Gramont, bishop of Tarbes". It would also
  have come up under Rome 1528-1532 (post-fix, 5 hits). **Residual, non-blocking:** sender "Grammont" (double m) was
  not queried, and neither the zero for c_holder "2980" nor the zero for receiver "Villandry" was shown to be a
  post-fix run. One re-run of those three queries would remove the residual (LANE N, suggestion only).

### 2. Principal families the 05:08 table missed, and this session's pass

| family | why it could print either letter | result |
|---|---|---|
| **Lanz, *Correspondenz des Kaisers Karl V.* I (1844)** (1513-1532) | Imperial correspondence; could print or summarise intercepted French despatches of 1530 | IA `bub_gb_RnURAAAAYAAJ` and `bub_gb_ns4FAAAAQAAJ` (both vol. I, full djvu): "Tarb" 3/2 hits, all OCR noise ("tarbatkias"); Gram(m)ont 0; Villandr 0. Vol. II (`bub_gb_UmwRAAAAYAAJ`) was fetched but not needed. **Covered, no hit** |
| **Heine, *Briefe an Kaiser Karl V. ... von seinem Beichtvater* (Loaysa, Rome 1530-32; 1848)** | Loaysa wrote from Rome in 1530 about Tarbes and about letters intercepted at Asti | IA `briefeankaiserk00loaygoog`, full djvu: "Tarba" about 19 times (the Spanish originals: Loaysa's reports of "Tarba"'s audiences, 1530-31), Agramont 2, Villandr 0. Letter IV, "Rom den 21. Juni" [1530], describes "gewisse Briefe, die in Asti aufgefangen und von Florenz gekommen sind" (Spanish: "letras interceptas en Haste"). It characterises them (French and English envy, no ducats sent to Florence) and **prints no text**. This matches the Asti row of the f.30 second audit. **Covered, no print** |
| **Weiss, *Papiers d'état du cardinal de Granvelle* I (1841)** | Imperial chancery papers of the period | IA `papiersdtatducar00gran` (tome I, full djvu): Tarb 0, Villandr 0, "1530" 0; Grammont 4 (the cardinal's return to Rome, 1530s retrospective). **Covered, no hit** |
| CSP Spanish IV **part 1** (1529-30) specifically | Mai's reports from Rome and intercepts | Metadata confirms that `calendarofletter0004pasc` (1879) is Part I and `_f5h4` (1882) is Part II. Both were searched in full text in section 4(a). **Covered** (a confirmation, no new search) |
| ***Revue des Hautes-Pyrénées* (1907)**, named as "not read" in the f.30 audit (g)/(h) and left out of the 05:08 table | Regional journal of Gramont's see. It was the only Google Books hit for "évêque de Tarbes" "mai 1530" Florence apart from the Dupuy catalogue | The IA item `revuedeshautesp00unkngoog` is sourced from Google Books `TOQVAAAAYAAJ`, **the same volume that hit** (Google: NO_PAGES). djvu and abbyy returned 500, and fts was run inside the item. The hit is an inventory of Dupuy manuscripts touching the Hautes-Pyrénées: "Tome 452. — Lettres originales de Gabriel de Gramont, évêque de Tarbes: au cardinal de Sens, chancelier de France; Rome, 15 mai [1530] (fol. 48); — au roi François Ier; Florence, 23 août 1529 (fol. 49)". Both are Dupuy pieces already in the table's Dupuy row, and neither is fr.2980. fts "2980" 0, "Villandry" 0, "chiffre" 0. **Covered, no hit** (a shelf-list, not a print) |
| Tomokiyo, Lasry, Bourdeau | brief item | Already covered in the 05:08 table rows (francis.htm "can be read", no reading; GL.htm's Lasry list has no fr.2980; Bourdeau CATALOGUE.md:76 "key held", no file at main or PR heads). Not re-fetched |
| IA full-text sweep with the double-m and Grandmont spellings | Earlier phrase sweeps used "Gramont" | be-api fts over all items: "Grammont" "Villandry" and "Grandmont" "Villandry" give only Loire guidebooks, parish registers and Touraine inventories; "Tarbes" "Villandry" 1530 gives Decrue and Scheurer I (both covered). **No hit** |

Nothing found lowers either class.

### 3. Decision

Every principal family is now covered: the canonical calendars, the documentary editions (French, Italian,
imperial), the sender's and recipient's studies, the holding archive's catalogue, both Camusat issues, the
transcription and cipher project pages (Tomokiyo, Lasry through GL.htm, Bourdeau, Aymeloglu, DECODE), and the phrase
search on the decoded text. Nothing turned up a prior plaintext or decipherment of either letter. **No.21: N4. No.22:
N4.** Logged and not blocking: OpenAlex and Semantic Scholar unreachable (429); HathiTrust full text unreachable
(Cloudflare); Michon, *La Crosse et le Sceptre* (2008), no pages; 11 JSTOR rows queued; archival intercepts (Simancas,
Vienna); DECODE's three unconfirmed zero rows (§1).

**Safe sentence, no.21 (N4):** "No prior decipherment located of Gabriel de Gramont's cipher letter to Jean Breton de
Villandry, Rome, 20 May [1530] (BnF fr.2980 f.29r, no.21). Tomokiyo identified it as readable, and Bourdeau catalogued it
(no.328). We read its 568-sign cipher passage in part with the Gramont 1530 key published by Tomokiyo and Lasry (2023):
533 signs at grade H, 30 uncertain, 5 unkeyed. The search log is in AUDIT.md."

**Safe sentence, no.22 (N4):** "No prior decipherment located of Gabriel de Gramont's all-cipher letter to Francis I,
Rome, 20 May 1530 (BnF fr.2980 f.30r-v, no.22). Tomokiyo identified it as readable, and Bourdeau catalogued it (no.328).
We read it in part with the Gramont 1530 key published by Tomokiyo and Lasry (2023): of 1,973 signs, 1,500 are at grade
H and 158 at grade S with a matched control. [V3b, 24 Sept 2026: counts stale. Since the seam fix and the second extension
(NOTES.md) f.30 has 1,969 signs; `decode.py --check` gives extended H 1,486, S 181, M 239, U 63 (published key alone H 1,502).
Quote: "of 1,969 signs, 1,486 are at grade H and 181 at grade S with a matched control".] Its closest print is the sibling letter of April 1530 (*Archivio storico
italiano*, Appendice I, pp.473-481), which is a different letter. The search log is in AUDIT.md."

**Unsafe sentences:** "first decipherment", "previously unread", "never printed" or "unpublished" without the qualifier
"no prior decipherment located"; "N5" or "confirmed new" (no archive or specialist has been asked); "we broke Gramont's
cipher" (the key is Tomokiyo's and Lasry's); "read in full" (both readings are partial and rest on one reconciled
transcription); "Cardinal Gramont" on 20 May 1530 (created 8 June); "Gramont to Villandry" for f.30.

### 4. Outreach gates (CLAUDE.md Outreach 1-6), both items

| gate | state |
|---|---|
| 1. verifier class in AUDIT.md | **met** (N4, both) |
| 2. above N1: second adversarial audit; open-index pass; Google Books queries; JSTOR rows answered or waived | second audit **met** (both). Open-index pass **met** (CrossRef, HAL, Persée, Google Scholar; OpenAlex and Semantic Scholar unreachable and logged). Google Books **met**. JSTOR **not met**: 11 Gramont rows in JSTOR-QUEUE.tsv (rows 2-7, 27-29, 33-34) are all `queued`. None is answered and none is waived by the owner. **Gate 2 is not met until the owner answers or waives them** |
| 3. the message is the safe sentence, states the prior print it rests on (Tomokiyo francis.htm; Lasry 2023 through GL.htm; Bourdeau 328), links AUDIT.md | **not met**: no draft exists (drafting is not this brief) |
| 4. rule 10 wording | the N4 sentences above are allowed, with the qualifier |
| 5. logged in CONTRIBUTIONS.md before sending | **not met** |
| 6. links a recipient can verify (repo folder; Gallica ark btv1b9059991d at f.29r and f.30r-v; Tomokiyo francis.htm; for f.30, ASI App. I pp.473-481 on IA `archiviostoricoi01fireuoft`) | available; **not met** until a draft carries them |

**Postmortem.** The 05:08 decision's table was right about the two families it named, but it left out one
family that an earlier audit had flagged as "not read": *Revue des Hautes-Pyrénées* 1907. That family was closed
here, negative. The f.30 audit also misjudged that item as "not known to be the 1907 volume". The IA item's `source`
metadata field names the Google Books id that hit, so a single metadata call settles it. Lesson for the verifier
template: before logging an IA volume as unidentified or unreadable, read its `source` field and run be-api fts
inside it (fts works when djvu returns 500). The DECODE section's own bug note was honest, but it did not say that
the zero rows were re-run after the fix. A search section that reports a mid-run fix should state which rows were
re-run.

Requests this session: archive.org 20 (6 advancedsearch, 1 metadata, 13 downloads including 5 byte-range probes; 3
returned 500, not retried beyond one abbyy attempt); be-api.us.archive.org 11; www.googleapis.com 8 (keyed,
country=US). No Gallica, no de-crypt.org, no logins, no decoding, no subagents.

## Second opinion SO-GRAMONT-F29R (ChatGPT, pull request 1), checked 24 Sept 2026, 16:06 UTC

Verifier V2 (Opus, for LANE V4, session_0178qzehvSNvWsP6vDrZRu7g). Input: `second-opinions/chatgpt-2026-09-24.md`
(GPT-6, copied from branch `second-opinion/SO-GRAMONT-F29R`, PR 1, unmerged). It reports no prior print or decipherment
of f.29r, one confirmed printed *reference* to the manuscript, and six corrections. Each checkable claim was checked
against the source below. No decoding.

| # | claim | source checked | verdict | correction made |
|---|---|---|---|---|
| 1 | *Catalogue des actes de François Ier* IX cites f.29 at entry [412], p.61; [411] is Villebon's 1528 mission; the volume is dated 1907 | IA `collectiondesord09acad` djvu text (fetched once): "Octobre-novembre 1528. — M. de Villebon ... [411]"; then "Juin 1529-novembre 1530. — Gabriel de Gramont ... 20 mai, ibid., 2980, fol. 29 et suiv. ... [412]", on the page headed "— 61 —" (entries [409]-[413]); title page "TOME NEUVIÈME ... DÉCEMBRE 1907"; IA metadata `date` says 1887 (wrong for this volume) | **right** | AUDIT.md's three "[411]" (section 4(c), f.30 second audit source log, N4 decision table) now read [412] with a note. The entry is a reference (existence and date), not a print of the letter: no class effect |
| 2 | sign count is 568 (H 533, M 30, U 5), not 569 | `reading.txt` header and `decode.py --check` (exit 0, "reading up to date": 568: H 533, C 0, S 0, M 30, I 0, U 5) | **right** | 569 kept only where it is a quotation of the first reader's counts, each now marked as such (AUDIT.md claim line, verdict table, section 1, grades row; NOTES.md Files and Grades); PROMPT-chatgpt.md now says 568. The safe sentences already said 568 |
| 3 | books.openedition.org/pur/120024 is by Philippe Hamon, "Jean Breton (v. 1490-1542)", in Michon (ed.), *Les conseillers de François Ier* (PUR 2011), pp.335-342, not by Thierry Rentet | the page's `citation_author` meta (Philippe Hamon), `citation_inbook_title`, "p. 335-342", its suggested citation; n.1 thanks Rentet, n.22 cites Rentet's 2008 paper | **right** | NOTES.md (author and book title, which was also wrong: "Conseils et conseillers") and AUDIT.md (three places) corrected |
| 4 | the prompt's phrase "il y baille a ce porteur" does not match the reading's letters "IAYEAI[LL]E" | `reading_tokens.tsv` L01: xr I, lam A, aq Y, q E (M), x A, z3 I, ll LL, sl E; key.tsv q: "read as 9 (reads B in L01 'baille')". There is no L before Y, so "il y" is not in the letters; "j'ay baille" is | **right** | PROMPT-chatgpt.md phrase list now "j'ay baille a ce porteur" plus "baille a ce porteur" alone. The earlier phrase sweeps ran "baille a ce porteur" without the pronoun (section 4(e)), so they are unaffected. reading.txt unchanged; the L01 gloss is logged as a solver suggestion in NOTES.md |
| 5 | the year should stay bracketed for f.29r | NOTES.md: BnF finding aid "A Rome, le XXme jour de may" (no year) and the clear-text draft "A Rome le xxme de may"; f.30 alone carries "M.D.XXX" | **right** | "20 May [1530]" for f.29r in the AUDIT.md claim note, the no.21 safe sentence, the N4 question line, NOTES.md's print-check question and the prompt. Dates that belong to f.30, and general date reasoning, are unchanged |
| 6 | E/B at L01 q and L04 sl?; T/F at L05 "tondement"; N/Q at L10 "cavsenve"; L11 Mx unkeyed | reading tokens and key.tsv (not re-read against the image) | **not a verifier matter**: conjectures on the reading, marked unverified by the second opinion itself | logged as a solver suggestion in NOTES.md; no reading changed |
| 7 | Camusat 1619 vs the 1644 Gallica copy: equivalence unverified | AUDIT.md "N4 decision (final families)", section 1 | **fair, already stated** | none. What AUDIT.md established: the 1644 Gallica copy was read, and two markers from it (the 4 Dec 1531 letter to Villandry, and the 1532-34 Gramont dossier) were found in the 1619 Google Books issues through the keyed API, so the 1644 is treated as a reissue of the 1619 sheets, explicitly "not proven folio by folio" |
| 8 | "no prior plaintext or decipherment" in the sources it reached (Tomokiyo francis.htm, Bourdeau CATALOGUE and gramont1529 notes, Hamon chapter, Catalogue IX, web phrase searches) | the same families are logged in the N4 decision table (Tomokiyo, Bourdeau, Hamon, *Catalogue des actes*, phrase search) | **agrees** | none |

**Its leads, one line each.**
1. Camusat edition comparison: already covered (N4 decision (final families), section 1); folio-by-folio identity of 1619 and 1644 remains a stated residual, not actionable without the 1619 page images.
2. Catalogue IX [412] and its neighbouring records: the catalogue is covered (section 4(c), now [412]); the sibling dispatches it lists (fr.3053 f.11, 2 May; fr.3019 f.20, 31 Aug; fr.3040 f.16; fr.3071; fr.3091 f.15) are manuscripts, not prints, and already appear in Tomokiyo's and Bourdeau's pages; not actionable for novelty.
3. Breton's network (Hamon chapter): covered (section 4(b), print-check pass). Its n.22 names Thierry Rentet, "Le pouvoir des lettres: l'année 1530 et la libération des fils de France à travers la correspondance d'Anne de Montmorency", in Claerr and Poncet (eds), *La Prise de décision en France (1525-1559)* (2008). No audit here has searched it by name: **new, low priority.** It works on the Montmorency correspondence at Chantilly (NOTES.md), not fr.2980. Not searched this session because the Google Books host was held by a sibling verifier.
4. Tomokiyo and Lasry's working material: covered as public pages (N4 decision table, Tomokiyo and Lasry rows); private notes are internal work, which N4 does not exclude; contacting them is the person's outreach, not actionable here.
5. Bourdeau's same-key letter fr.3071 no.7: a solver resource (NOTES.md already cites it for the g/9/q shapes), not a novelty family.
6. DECODE and Aymeloglu beyond the inspected files: covered (DECODE search section, and the N4 decision table's Aymeloglu row); the "Grammont" sender query is the residual already logged in N4 decision (final families) section 1; the old shelfmark "8505" was not queried in DECODE: **new, non-blocking**, one query for LANE N.
7. Uncompleted edition and scholarship families: Scheurer, Decrue and the scholarship indexes are covered (N4 decision table; open-index pass); Le Glay's *Négociations ... l'Autriche* was logged off-target (section 4(g)). **Marguerite d'Angoulême's letters (Génin, 1841 and 1842), named in our own prompt, had no logged search; closed this session:** IA `lettresdemarguer00marguoft` and `nouvelleslettres00marguoft`, full djvu text: Gramont/Grammont and Tarbes hits are Marguerite's 1525 Spanish voyage, the English marriage mission, a recommendation of "M. de Tarbes" and index lines; one letter from Marguerite to Villandry. **No Gramont letter of 1530 and nothing from fr.2980. Covered, no hit.**

**Class.** No check found a prior print or decipherment. **No.21 (f.29r) stays N4**, with the qualifier "no prior
decipherment located". No.22 is untouched. The no.21 safe sentence of "N4 decision (final families)" now carries
"20 May [1530]" and otherwise stands.

**Postmortem.** Four of the second opinion's corrections were right and were ours to catch: an entry number read one
line early in a catalogue whose numbers close each entry, a chapter author taken from a footnote instead of the byline,
a count updated in the reading but not in the prompt and the first audit sections, and a search phrase that divided
the letters into words they do not contain. None changes the class. Lesson for the verifier template: cite a catalogue
entry from its closing number and a chapter from its `citation_author`, and regenerate the prompt's counts and phrases
from `reading.txt` rather than from an earlier section.

Requests this session: archive.org 6 (1 djvu download and 1 metadata for Catalogue IX, 2 advancedsearch, 2 djvu
downloads for Génin 1841 and 1842); books.openedition.org 1. No Google Books, no Gallica, no
de-crypt.org, no logins, no subagents.

## Second opinion SO-GRAMONT-F30 (ChatGPT, pull request 4), checked 24 Sept 2026 16:31 UTC

LANE V4 verifier V3b (Opus, session_01J653u9mXgcT3gwBenQP5kh). Input: `second-opinions/chatgpt-f30-2026-09-24.md`,
GPT-6 via Codex, copied from branch `second-opinion/SO-GRAMONT-F30` (PR 4, unmerged). It found **no printing of the
20 May letter and no prior decipherment**. It offers one "near-match" to collate, Capponi's discussion of a Tarbes
letter. It also lists corrections to our counts and presentation. No decoding was done here.

| # | claim | source checked | verdict | correction made |
|---|---|---|---|---|
| 1 | Capponi, *Storia della Repubblica di Firenze*, 2nd ed. (1876) III, pp.273-275, n.216, discusses a long Tarbes letter to Francis I, Rome, April 1530, and cites *ASI* Appendice I p.473 | Gutenberg #67297 HTML (fetched once): title page "Seconda edizione ... Tomo terzo ... 1876". The text before page mark [274] describes the letter. N.216 quotes "Venant de Boullogne icy, j'ay entendu la force et la foiblesse des Fleurentins ..." and cites "(Lettera del Vescovo di Tarbes al re Francesco I; da Roma, aprile 1530. Archivio Storico Ital., Appendice, vol. I, pag. 473.)". N.217 quotes "... commanderez à baguette ..." and cites "(Lettera citata.)" | **right, and it is the sibling April letter this file already tested as a different letter** | none to the class. Both Capponi quotations come from *ASI* App. I doc. XXXVIII (pp.473-481). "Is f.30 the printed April letter in cipher? Test" ran on that text: longest shared run 18 letters, a formula. A further check here: the words Capponi quotes (BAGVETTE, ARBITRE, FLEVRENTIN, BOVLLOGNE, ACCESSOIRE, CONSERVACION, VICTVAILLE, AOVST) give 0 hits in the folded f.30 extended reading. Capponi is a secondary print of the April letter, not of f.30. It is added to the evidence here |
| 2 | Camusat 1619 vs the 1644 Gallica copy: equivalence not shown folio by folio | AUDIT.md "N4 decision (final families)" 1; V2's row 7 | **fair, already stated** | none (residual risk as logged there) |
| 3 | CSP Spanish IV.1 p.603: intercepted Tarbes letters, an archival route only | f.30 second audit 3 and (a), with the p.603 passage quoted | **right, already covered** | none. The intercepts are archival, and N4 does not exclude unpublished work |
| 4 | Tomokiyo francis.htm: the key is published and the letter is identified as readable; key credit is separate from plaintext | AUDIT.md f.30 verdict row (Tomokiyo's quotation, Bourdeau no.328) | **right, already covered** | none |
| 5 | Prompt counts stale: the reading now gives 1969 tokens, H 1486 / S 181 / M 239 / U 63, not 1973 with H 1502 / S 158 / M 254 / U 59 | `decode.py --check` (exit 0, "reading up to date"): "f30 extended # tokens 1969: H 1486, C 0, S 181, M 239, I 0, U 63"; published key alone 1969: H 1502 / M 231 / U 236 | **right** | PROMPT-chatgpt-f30.md counts updated. The no.22 N4 safe sentence is annotated in place with the current counts. status.json's no.22 line was not edited (no class change). The orchestrator should refresh it from the annotated sentence |
| 6 | "Avignon" is a normalization; f30r L32 reads AVILNON | reading_f30_extended.txt L32 "...QvILVEvLTA[LL]ElENAVILNON" | **right** | prompt phrase now "qu'il veult aller en Avilnon [Avignon?]". The reading itself is unchanged. A one-line solver suggestion was added to NOTES.md |
| 7 | "declaration" reads DECLARADION (eh T/D conflict) | reading L02 f30v; AUDIT.md "Reading quality" (eh at T, not the table's D) | **right, already recorded** | prompt phrase now marked "(letters as read: DECLARADION)" |
| 8 | L01, L02 and L11 are not continuous French | NOTES.md (the four lines, "Still not French") | **right, already recorded** | none |
| 9 | The two cross shapes should be split before values are tested | NOTES.md (cross pattée vs double-barred, both coded CROSS) | **right, already recorded** | none (a solver matter) |
| 10 | Grade S is not image confirmation; p = 0.01 from 100 draws is not the probability the reading is right | NOTES.md extension tables (p = 0.010, 100 draws) | **right in substance**; S is correctly defined as cryptanalytic with a control (rule 4) | none. AUDIT.md already says "a cryptanalytic result resting on a key-based reading" |
| 11 | The recipient "Sire" supports the king; pronouns and COM antecedents need analysis | AUDIT.md f.30, "Who, to whom, when, where" | **right, already covered** for the recipient; the pronouns are a reading matter | none |

**Leads.** (1) *ASI* App. I p.473: already read and tested (row 1). (2) The Asti intercepts in Simancas and Vienna are
archival and do not block N4. (3) Camusat 1619 vs 1644: the residual is stated. (4) Florentine narratives with French
originals: Capponi, the only concrete one named, is closed as row 1. Varchi, Segni and Nardi were named in our own
prompt. The f.30 audits cover the *ASI* series and its index. These narrative histories were not grepped by name here,
so they are **not searched**, low priority: they quote the April letter through Capponi at most. (5) An image recheck
of AVILNON, the crosses and eh is a solver matter (NOTES.md).

**Did the second opinion find a prior print or decipherment of f.30?** No. Its one concrete print is the April letter,
already known and tested as different. **Class: no.22 (f.30r-v) stays N4** (no prior decipherment located). No.21 is
untouched.

**Postmortem.** Two of our own statements were stale and the outside reader caught both. The first is the counts. The
prompt and the N4 safe sentence still gave 1,973 signs after the seam fix and the second extension changed them to
1,969. The second is the catalogue entry: V2 corrected [411] to [412] at three places, but a fourth, in the f.30
verdict row, was missed. Corrected in place. Lesson (it repeats V2's): regenerate a prompt's and a safe sentence's
counts from `decode.py --check` at the time of writing, and grep the whole file when correcting a citation.

Requests this session for this label: www.gutenberg.org 1. No Google Books, no Gallica, no archive.org.


## JSTOR (owner's machine, 24 Sept 2026)

Recorded by the JSTOR runner on the owner's machine (logged-in JSTOR account, built-in browser, one search per queue row, 6 s apart, no block page). First-page hits for every row are in `JSTOR-QUEUE.tsv`; only the hits that could print, calendar or discuss the letter were opened. No class is changed here; the verifier moves it.

Rows 2-6, 26-28, 32-33 answered (11 queries). Two hits opened:

- Mignet, "Rivalité de Charles-Quint et de François Ier: le siège de Naples. Paix de Cambrai", *Revue des Deux Mondes*, 2e période, 68/2 (15 mars 1867), pp. 382-426, https://www.jstor.org/stable/44726292 (open access). In-document search: "Villandry" 0 hits; "Gramont" and "Tarbes" 1 hit each, the same footnote (p. 419), which quotes a letter of Gabriel de Gramont, bishop of Tarbes, to the admiral Chabot de Brion dated 25 February 1530 (Mss. Béthune 8578, f. 43) on the emperor's coronation at Bologna. Nothing on the 20 May letter to Villandry, on fr. 2980 or on a cipher.
- Cédric Michon, "Quand l'Église fait l'État", *Annuaire-Bulletin de la Société de l'histoire de France* (2005), pp. 127-147, https://www.jstor.org/stable/23408509 (read online). In-document search: "Villandry" 0, "2980" 0, "Gramont" 2, both passing mentions (Charles de Gramont as a royal relay in Guyenne; Gabriel de Gramont among the prelates who came forward after Pavia). No letter cited.

The other first-page hits are bibliographies, parlement studies and name collisions (the `"fr. 2980"` query returns Swiss-franc prices). None discusses the letter.

## Outreach gate 2: JSTOR family and open indexes (verifier V5, 24 Sept 2026)

Verifier V5 (Opus, for LANE V4, session_01UBQ2tN51FBuKTx41RqnGAK), 24 Sept 2026 17:24 UTC. Triage of the JSTOR runner's first-page hits (JSTOR-QUEUE.tsv) by title, snippet and what the runner read; no decoding, no class change unless stated.

11 rows (file lines 2-7, 27-29, 33-34), 2 candidates read by the runner (Mignet 1867, 'Le siège de Naples. Paix de Cambrai', stable/44726292; Michon 2005, stable/23408509), both negative. One candidate not opened: **Mignet, 'Rivalité de Charles-Quint et de François Ier' (Revue des Deux Mondes 1867, stable/44728935)**, a different instalment of the same series, returned by 'Gabriel de Gramont AND "Clement VII" AND Florence'; it may narrate Rome in spring 1530 from Gramont's dispatches. Listed `to read (owner's machine)` and queued as a READ row. Context only: Aubert 1905/1906/1912 (parlement), Baudouin-Matuszek 2010, Michon 2003, Bourrilly 1918 (1536), Barbiche (légats), Braun (Renée de France 1528), Hauser 1905 bulletin, Revue Historique 'Recueils périodiques' lists, bibliographies, Drysdall (name collision), Nicolay 'Naples' dossier (Louis XII); 'fr. 2980' returns Swiss-franc prices.

JSTOR family: searched on the owner's machine 24 Sept 2026, 11 rows, 2 candidates read, result negative; 1 candidate (Mignet 1867, stable/44728935) still to read. Gate 2's JSTOR condition is **not yet met** (one READ row).

Open indexes: OpenAlex (`api.openalex.org/works?search=...`) and Semantic Scholar (`/graph/v1/paper/search`) retried once each from the cloud at about 17:21 UTC: both HTTP 429 (shared free daily budget used up). The owner's run of 24 Sept 2026 (ASKS 34) covered Thurloe, Eckert and Blathwayt only; this target's queries are owed (ASKS row 44, `outreach/openalex-s2-owner-queries-2.md`).

Outward drafts written this session (status drafted, nothing sent): see `outreach/` and CONTRIBUTIONS.md.
