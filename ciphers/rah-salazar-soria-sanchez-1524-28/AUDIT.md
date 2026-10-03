# AUDIT: items 1, 3 and 5 "already in print in CSP Spain" (rah-salazar-soria-sanchez-1524-28)

Verifier A2P4-VRAHSAL (account 2, LANE-A2PUSH4), 3 Oct 2026, 17:56-18:15 UTC. A separate session from the
solver/check-solved sessions (NX2-GATE2, NX2-RV) whose claim is audited; nothing here protects their conclusions.
Classes are CLAUDE.md rule 10's N0-N5. This project has **no reading of its own** of any of the five items (no
image has been obtained); the classes below therefore describe what is already known about each item, so that no
later session plans a campaign on a text that is already in print.

Claim under audit (NOTES.md "Verdict for the orchestrator", as of 26 Sept 2026): "three of the five items (1, 3, 5)
... their plaintext (in English translation) is already published in CSP Spain (Gayangos, vol.III parts 1 and 2,
1873/1877) -- items 1 and 3 via a surviving period/contemporary decipherment, item 5 via what appears to be
Gayangos's own 19th-century solving ... folio-level matches are inferred from date+place+correspondent+addressee".
Items 2 and 4 are out of scope (no images, not calendared).

## 1. Verdict

| # | RAH item (Índice) | CSP Spain entry | CSP margin shelfmark (read on the page image) | match | class | key | text |
|---|---|---|---|---|---|---|---|
| 1 | inv.5180, A-35 ff.310-312 (+f.313 cover), Soria to Charles V, Genoa 21 Sept 1525, "frases en cifra que no están descifradas a continuación" | vol.III pt.1 (1873) No.212, pp.340-343 | **A. 35, ff. 314** = Índice **inv.5181**, "Ejemplar duplicado de la carta anterior (5180)", A-35 ff.314-316 | same letter, **other copy** | **N2** | period | known (English calendar) |
| 3 | inv.6417, A-42 ff.243-244 (+f.245 cover), Soria to Charles V, Mirandola 14 Apr 1528, "frases en cifra que están sin descifrar" | vol.III pt.2 (1877) No.399, pp.652-654 | **A. 42, f. 279** = Índice **inv.6428** (Mirandola, 25 Apr 1528, ff.279-280), "cuya primera parte es duplicada de la reseñada con el nº 6417"; its period decipherment is **inv.6429** (ff.282-283) | item 3's text **via a later copy** (first part of 6428) | **N2** | period | known (English calendar) |
| 5 | inv.6502, A-42 f.443, Alonso Sánchez to Gattinara, Venice 17 Jun 1528, "algunas frases en cifra que no están descifradas a continuación" | vol.III pt.2 (1877) No.462, p.714 | **A. 42, f. 443** | **this very sheet** | **N0** | published | known (English calendar) |

**Net:** the claim's substance holds for all three -- the content of each letter's cipher passages is in print, in
English, in CSP Spain III -- but its stated basis was wrong for two of the three. For items 1 and 3 Gayangos
calendared a *different copy* (the duplicate of item 1; the later letter that repeats item 3), not the RAH sheet the
project holds as the item; the "exactly" in NOTES.md was inferred from date and place, and the margin shelfmark,
OCR-garbled in the djvu text ("ff, 314", "ry PD"), was not read. For item 5 the folio matches exactly, but
"Gayangos solved this cipher himself" is not established (section 3).

Why N2 and not N0 for 1 and 3: N0 needs the plaintext *and a decipherment of this very item*. The period
decipherments behind CSP Nos. 212 and 399 belong to the duplicate copies (CSP 212: "Contemporary deciphering",
of f.314; CSP 399: "Contemporary deciphering on separate sheet" = inv.6429, which the Índice ties to 6428 only).
The cipher passages on ff.310-312 and ff.243-244 themselves remain, by the RAH's own cataloguing, undeciphered
on the sheet, and no mapping of their ciphertext to the printed text was found. A duplicate normally carries the
same plaintext but may be enciphered differently (other homophones, or Soria's second cipher Ko.16), so the
printed text is a near-certain crib for those two sheets, not a reading of them.

Safe sentence (all three): "The content of the cipher passages of items 1, 3 and 5 is printed in English in the
Calendar of State Papers, Spain, vol. III (Gayangos, 1873/1877): item 5 from this very sheet (No. 462, A.42 f.443),
items 1 and 3 from other copies of the same letters (No. 212 from the duplicate A.35 f.314; No. 399 from A.42
f.279, whose first part repeats item 3) read through period decipherments."

Unsafe sentences: "items 1 and 3 match the RAH shelfmarks exactly"; "Gayangos solved item 5's cipher himself";
any wording that presents a future reading of these three as a recovery of unknown text (rule 10).

Key-source note (rule 10 addendum): `period` for 1 and 3 means the printed reading rests on decipherments of the
time (of the duplicates); this project rebuilt no key from them. `published` for 5 means Gayangos's printed
reading, source of the decipherment not stated by him. For all three, status.json would carry `text: known`.

## 2. Evidence, per item

Sources read: CSP Spain vol.III pt.1 (archive.org `calendarofletter0003pasc`, djvu text, 3.1 MB) and pt.2
(`calendarorleters0003vari`, 3.5 MB), fetched once each this session; the three margin notes read on the page
images (archive.org `/download/<id>/page/n391.jpg`, `n699.jpg`, `n761.jpg` = printed pp.340, 652, 714; leaves
located by the item's `_page_numbers.json` and the full-text-inside API; crops in `images/csp_margin_crops.png`,
one vision call on the crops, no full page sent); the RAH Índice OCR (`salazary-castro-22-nov-2016`, manifest in
`sources/salazar-castro-index/README.md`), entries inv.5177-5183, 6417, 6427-6429, 6498-6502 read in full.

**Item 1.** CSP No.212 "LOPE DE SORIA, Imperial Ambassador in Genoa, to the EMPEROR"; margin "21 Sept. ...
M. Re. Ac. d. Hist. Salazar, A. 35, ff. 314." Content matches the Índice abstract of inv.5180 point by point
(Stefano Grimaldo paying the rest of the 24,800 ducats; Bourbon to sail for Spain; the galleys to return for
Genoa's defence; the Doge and the 2,000 infantry; recommendation of the Grimaldi; the Duke of Ferrara wishing to
go to Spain). Dateline "Sestri, near Genoa, 21 Sept. 1525"; endorsed "From Genoa, Lope de Soria, 21 Sept.";
"Spanish. Original partly in cipher. Contemporary deciphering. pp. 4½" (djvu "44"; fraction not checked on the image). The Índice gives inv.5181,
A-35 ff.314-316, as "Ejemplar duplicado de la carta anterior (5180)", same abstract, "Original" -- it does not
mention the cipher on the duplicate, CSP does. Neighbours confirm the folio run: CSP No.210 (Sessa, 19 Sept) =
A.35 f.307 = Índice inv.5178 (the Sessa duplicate, ff.307-308). Cipher passages printed: four `(Cipher :)`
sections (Pope's galleys and protest; Andrea Doria and Juanin de Medicis; the Milan conference quotas; Ferrara,
Caracciolo, del Burgo).

**Item 3.** CSP No.399 "LOPE DE SORIA to the EMPEROR", margin "14 April. ... Salazar, A. 42, f. 279." Opens
"Duplicate of his letter of the 7th with the following postscriptum": Melfi stormed 23 March (Índice 6417's
abstract: Melfi taken, "no son escapadas XX personas", the Prince taken -- CSP: "only twenty persons ...
escaped"), Leyva out of Milan, Genoa's unrest; dated "La Mirandola, 14th April 1528"; then a further
"Postscriptum" (Germans to muster on St George's day; the Union proclaimed at Genoa; Adorno not wanted as Doge)
matching the Índice's abstract of inv.6428 (Mirandola, 25 Apr 1528, "cuya primera parte es duplicada de la
reseñada con el nº 6417", news of Ferdinand's relief army with thirty pieces of artillery, Genoa against
Adorno). Ends "Spanish. Original partly in cipher. Contemporary deciphering on separate sheet. pp. 7" = inv.6429,
"Texto descifrado de los párrafos en cifra del documento anterior", ff.282-283. Cipher sections printed include
the one with the Spanish quoted in a footnote, "Que el Papa ha concedido la dispensacion para que el Rey de
Inglaterra dexe su muger, y se case con la otra que quiere." Whether every cipher passage of 6417 recurs in
6428's first part is not checkable without images; the Índice's "duplicada" says so for the first part.

**Item 5.** CSP No.462 "The SAME [Alonso Sanchez] to the HIGH CHANCELLOR", margin "17 June. ... Salazar, A. 42,
f. 443." Addressed "Al Illmo. Señor el Señor Gran Canceller, mi señor"; "Venice, 17th June 1528"; "Spanish.
Holograph entirely in cipher. No deciphering appended. pp. 1½" (djvu "14"; fraction not checked on the image). Shelfmark, date, place, sender and
recipient (Gattinara, Índice inv.6502) all match. One discrepancy recorded: the Índice says "algunas frases en
cifra", CSP "entirely in cipher"; CSP prints one paragraph, all marked (Cipher), which may be abridged.

## 3. Item 5's decipherment: source not established

NOTES.md said the "No deciphering appended" note "can only mean Gayangos solved this cipher himself". Other
explanations are open: the Sánchez cipher of June 1528 was in use in the three letters to the Emperor of the same
day (Índice inv.6498-6500, A-42 ff.429-440, all "con algunos párrafos en cifra"), whose period decipherment sits
on ff.441-442 (inv.6501, "de los tres documentos anteriores" -- it names 6498-6500, not 6502); Gayangos could
have read f.443 with the key those deciphered letters yield, or from a decipherment elsewhere. Any of these makes
the printed text Gayangos's reading; none makes it established that he *broke* the cipher. Recorded as `published`
(his printed reading), mechanism unknown.

## 4. Other print searched (3 Oct 2026)

`tools/print_check.py` (results in scratch, not committed), five phrases (the Spanish footnote of No.399; four
English phrases from Nos. 212, 399, 462), against the two CSP volumes (positive controls: 4 of 5 hit in the right
volume; "Has tarried in Venice longer than he was desired" missed through the printed line-break "de- sired"),
IA full-text across all items, Google Books (keyed, country=US) and OpenAlex. Hits only in CSP Spain III itself
and its reprints (Google Books 1873/1877 and the 1969 reprint volumes); OpenAlex none; one Google Books query
answered HTTP 503, not retried. Earlier passes on file (NX2-GATE2, NX2-RV, JSTOR runner 26 Sept 2026): Rodríguez
Villa 1875/1885, Pizarro Llorente (UAM), DECODE, both solver repositories, JSTOR -- no other print of these three
letters' cipher passages. Not searched: the 1931 BRAH Soria catalogue (tomo 98, HathiTrust search-only),
Kolosova's 2017 thesis (CORE copy 404). Neither changes the classes: the CSP print alone sets them.

Requests this session: archive.org 9 (2 djvu texts, 2 page-number JSON, 2 metadata, 6 page images incl. 3 at a
wrong leaf offset, Índice djvu 1), ia800801/ia600804 fulltext-inside 3, print_check: archive.org 2,
be-api.us.archive.org 5, googleapis.com 5, api.openalex.org 5. All >=1.5 s apart, one at a time.

## 5. Postmortem

Failure: a folio-level match was asserted ("shelfmark matches exactly") from date, place and correspondents, while
the one field that decides it -- CSP's margin folio -- was garbled in the OCR and not read on the image. Two of
three were other copies. Cost of the check: one crop composite, one vision call. Lesson: when a calendar entry is
matched to an archive item, read the calendar's margin shelfmark on the page image and look up that folio in the
holding catalogue; a duplicate or a later letter repeating the first is common in ambassadorial series (this very legajo
holds duplicates and triplicates, Índice inv.5177/5178, 5180/5181, 6498-6500).

Consequence for the target: items 1 and 3 are not merely "dataset rows": with an image of ff.310-312 and
ff.243-244, the printed English (and, for 3, the period decipherment inv.6429 if imaged) is a crib that would show
which of Soria's two ciphers (Ko.6 or Ko.16) each sheet uses -- the question NOTES.md left open. That is a cheap
known-plaintext step once images exist; it stays behind the same REQUEST.md as items 2 and 4.

Corrections made in NOTES.md this session: the item 1 and item 3 "shelfmark matches exactly" sentences, the item 5
"can only mean Gayangos solved" sentence, and the verdict paragraph, each annotated in place with a pointer here.
No SECOND-OPINIONS-QUEUE.tsv row: no class is N3 or better.
