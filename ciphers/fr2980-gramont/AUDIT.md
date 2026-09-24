# AUDIT: the fr.2980 f.29r reading (novelty class)

Verifier session, 24 September 2026, 00:50-01:20 UTC (`date -u` read; Opus, no subagents, started by the
orchestrator session_01SepNMpYrr6L2EwqL43aTnm). Audits NOTES.md, reading.txt, key.tsv and decode.py as of
commit 4493903. This session took no part in the check-solved, print-check or transcription passes. It did not
decode and does not protect the solver's conclusions. Classes are those of CLAUDE.md rule 10.

Claim under audit: "BnF fr.2980 f.29r (item 21), Cardinal Gabriel de Gramont, bishop of Tarbes, to Jean Breton
de Villandry, Rome, 20 May 1530: the cipher passage reads with Tomokiyo/Lasry's Gramont 1530 key, 569 signs,
H 538 / M 26 / U 5 (reading.txt, decode.py --check)."

## 1. Verdict

| item | prior plaintext | prior decipherment of this item | class |
|---|---|---|---|
| BnF fr.2980 f.29r, no.21 (old shelfmark Anc. 8505), Gramont to Villandry, Rome, 20 May [1530], cipher passage of 569 signs | **not located.** No printed text, extract, calendar entry or summary of the letter's content was found in the editions of section 4. The letter's *existence and date* are in print: the BnF *Catalogue des manuscrits français* (1868) describes it, and *Catalogue des actes de François Ier* IX (entry [411], list of ambassadors) cites "Écrit de Rome … 20 mai, ibid., 2980, fol. 29 et suiv." to date Gramont's stay in Rome. Neither gives any content. | **not located.** No decipherment was found on the leaf (NOTES.md, check-solved), in print or online. **But it has been identified as readable before us:** Tomokiyo (cryptiana, francis.htm, "BnF fr.2980 (1530)", live page re-read 24 Sept 2026) says "These undeciphered letters can be read with Gramont's cipher (1530)", and Bourdeau lists both items as catalogue 328, "Gramont 1530 key held" (dbourdeau/cyphersolver CATALOGUE.md line 76, sweep of 22 Sept 2026). Neither gives a reading. | **N3** |
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
de Villandry, Rome, 20 May [1530], with a 569-sign cipher passage. Tomokiyo had identified it as readable with
the published Gramont 1530 key (Tomokiyo; Lasry 2023). We transcribed the passage from the Gallica image (one
reader) and applied that key: the table gives values for 538 signs (H), 26 are uncertain and 5 unkeyed, and
several lines read as continuous French. No prior printed plaintext or decipherment of the letter was located in
the editions listed in AUDIT.md (N3)."

**Unsafe sentences.** "First decipherment of Cardinal Gramont's letter"; "a previously unread letter"; "newly
recovered"; "538 of 569 signs read" or "read in full" (the reading is partial and single-reader); "Cardinal
Gramont" as of 20 May 1530 (he was created cardinal on 8 June 1530); "we found that the key applies" (Tomokiyo
said so first, and Bourdeau catalogued it).

## 2. What the repo claims (extracted)

| field | value in the repo | source |
|---|---|---|
| shelfmark | BnF fr.2980 f.29 no.21 (Anc. 8505), Gallica ark:/12148/btv1b9059991d canvas f31 | NOTES.md, images/manifest.json, BnF notice cc494342 (re-fetched this session: "Ancienne cote : Anc. 8505") |
| sender, recipient | Gabriel de Gramont, bishop of Tarbes, to "monseigneur... de Villandry, conseiller du roy et secretaire de ses commandemens et finances" | BnF notice, verbatim |
| date, place | "A Rome, le XXme jour de may", no year on no.21; no.22 "M.D.XXX" | BnF notice |
| cipher, key | Gramont's Cipher (1530): Tomokiyo from fr.3019 f.20; Lasry 04/11/2023 from fr.3071 f.17 | key.tsv, NOTES.md |
| reading | reading.txt, 14 lines; distinctive decoded phrases: "il y baille a ce porteur ... article que j'ay mis a part"; "l'adresse de dessus a vous combien que ce soit au roy"; "vous prie le luy demander car c'est le total"; "du vingtiesme"; "pour le contenter et oster ... de suspecon"; "qui est cause que j'ay faict ledit article a part"; "pour vous donner cognoissance de tout"; clear text: "pensant que ce courrier pourra estre plustost a vous que le pacquet", "ung double des lettres que j'escriptz lundi", "satisfaction de nostre Sainct Pere" | reading.txt, NOTES.md |
| grades | 569 tokens: H 538, C 0, S 0, M 26, I 0, U 5 | reading.txt header |
| solver's search | IA fts two phrases; Google Books API three queries; print-check pass (LP iv.3 direct, Decrue, PUR/Rentet, Tomokiyo, Bourrilly-Vindry vol.1, Google Books Le Grand bot-blocked) | NOTES.md |

## 3. The attribution tested against the plaintext

- **Recipient Villandry fits.** The cipher says the writer put an article apart and "faict l'adresse de dessus a
  vous, combien que ce soit au roy": he addressed it to the secretary although it is meant for the king. That is
  how one writes to the king's secretary of commands, Breton de Villandry, whose office was to carry such pieces
  to the king (Rentet, PUR chapter). The clear text's "le pacquet que j'ay envoye au Roy" fits the same relay.
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
- **Rentet**, PUR chapter on Breton de Villandry (pur/120024): read by the print-check pass. This session read the
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
- ***Catalogue des actes de François Ier* IX** (IA `collectiondesord09acad`, full text): entry [411] cites the
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
  **Located but still not full-text-searchable; status changes from "unreached" to "found, unreadable via API."**
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
