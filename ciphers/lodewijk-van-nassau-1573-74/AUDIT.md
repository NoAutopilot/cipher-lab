# AUDIT: Lodewijk van Nassau to Willem van Oranje, WVO 4610, 4611, 4612, 4616 (1573-1574)

Verifier V2 for LANE V2 (session_019R3BzX1XwBXWFgyfDT6zdm), 24 Sept 2026, 08:52-09:10 UTC. This session did not
solve the target and does not defend the solver's conclusions. Rule 10 levels N0-N5 (CLAUDE.md). No decoding was
done here and the cipher was not re-read.

Claim under audit (LANE R, R18/R20, 08:19-08:36 UTC, 24 Sept 2026; status.json results row, STATUS.md row NB1):
four cipher letters of Lodewijk van Nassau to Willem van Oranje, Koninklijk Huisarchief A 11/XIV D/13a, read in
part with a letter key aligned from the contemporary decipherments of sibling letters 4613 and 4615, graded
"C 2512, I 267, M 658, U 575 of 4012 groups", and "WVO records no solution".

## 1. Verdict

| item | date, place | prior plaintext | prior decipherment | class |
|---|---|---|---|---|
| 4610 | 3 Jun 1573, no place ("Pour Hollande", duplicate) | not located; the substance is answered in Orange's printed reply of 17 Jun 1573 (Groen IV, Lettre CDXXVII, pp. 156-160; WVO 4497) | the recipient read it in 1573 (his reply answers it); no surviving decipherment located | **N3** |
| 4611 | 2 Jul 1573, no place | not located; Orange's printed reply of 22 Jul 1573 acknowledges it (Groen IV, Lettre CDXXXIII, p. 175ff; WVO 4498) | recipient read it; no surviving decipherment located | **N3** |
| 4612 | 6 Mar 1574, Meer | not located; no printed reply identified | none located | **N3** |
| 4616 | 12 Apr 1574, Weeze | not located; Orange's printed reply of 15 Apr 1574 acknowledges it ("vostre lettre du xije du présent ... jusques à où vous estes arrivé", Groen IV, Lettre CDLXXXIV, pp. 368-369; WVO 4503) | recipient read it; no surviving decipherment located | **N3** |

N4 is withheld for all four. The reasons are in section 5.

## 2. Items (extracted from the repo)

All four: originals, KHA A 11/XIV D/13a, identified as Lodewijk's by secretary's hand and seal. The PDFs are at
`resources.huygens.knaw.nl/media/wvo/images/04000-04999/0461{0,1,2,6}.pdf`. They are mainly in cipher: a
homophonic letter table (five numbers per letter in blocks from n = 1-5 to m = 116-120), with code signs above
120 and French words written in clear between the numbers. WVO gives an incipit for three of them, taken from
the opening words written in clear:
- 4610: "Il fault que me pardonnez de ce que ne vous ay depesché ce message le lendemain". The WVO note says
  "Zie voor het antwoord nr. 4497".
- 4611: incipit "...", Inhoud "xxx".
- 4612: "J'é receu hier vostre lettre du xxime de febvrier, et veu ce que mandez de la".
- 4616: "Nous sommes cest soer icy arivé aupres de Goch et sommes".
WVO's Bron field lists only the manuscript for each of the four, and no edition. All four records were fetched on
24 Sept 2026 and read.

What the reading actually contains (from `reading_<nr>_tokens.tsv`, which counts only cipher signs; clear words
are not counted): 4610 has 1222 letter-numerals (C 1073), 4611 1145 (C 821), 4612 775 (C 369) and 4616 226 (C 200).
Grade C here means the numeral's value was seen aligned in 4613/4615. It does not mean that the letter text reads
correctly. The runs read as French only in stretches: 4616 gives "pour demain ... loger". 4612's numeral runs
mostly do not read as French under this key (e.g. p1_L04 `flvspaspfdmettbsesvsvntapbn`, p1_L07-L15). That could
be a different table in early 1574, transcription error, or both. It is not a reading.

## 3. Principal families

| family | status | what | result |
|---|---|---|---|
| Groen van Prinsterer, Archives, 1st series t. III, IV, V, Supplément, Table | searched | DBNL full text (`nieuws/text.php?id=groe009arch03/04/05/09/10`) fetched once. T. IV table of letters read by date for Jun-Jul 1573 and Mar-Apr 1574, plus grep of the full text for dates, places (Goch, Weeze, Meer, Cartilz), `chiffr`, and "vostre lettre du" | none of the four printed. T. IV prints Orange's replies to 4610 (CDXXVII), 4611 (CDXXXIII) and 4616 (CDLXXXIV). Supplément no. 49 is Lodewijk to Orange, camp de Cartilz, **4 Apr 1574**, which is a different letter (not 4613/4615/4616). Groen notes elsewhere that he could not decipher cipher passages (t. IV, Lettre CDXLIV; additions p. 91 "Nous n'avons pas même trouvé le chiffre") |
| Japikse, Correspondentie van Willem den Eerste | not applicable | the volume stops at 1561 | out of range; logged |
| Gachard, Correspondance de Guillaume le Taciturne | searched (t. III) | IA `correspondancede03will` djvu text, grep for dates, Goch/Weeze, chiffr, "comte Louis" | nothing on the four |
| Gachard, Correspondance de Philippe II (intercepts) | searched (t. II, III) | IA `correspondancede02phil`, `...03phil`, grep for interceptée/déchiffr near Louis | intercepts are mentioned generally (Gonçalez, Oct 1572); none of the four |
| Kervyn de Lettenhove, Les Huguenots et les Gueux | searched (t. III) | IA `leshuguenotsetle03kerv`, grep of footnotes for Louis's letters 1573-74 and the Mookerheyde chapter | cites Louis's letters only through Groen (18 Aug 1573, 1 Jun 1573 etc.) and Record Office items; none of the four |
| Kervyn, Relations politiques des Pays-Bas et de l'Angleterre | **not searched** | IA title search found no item | gap |
| Blok, Lodewijk van Nassau (1889) | searched | IA `lodewijkvannass00blokgoog` djvu text; the preface lists sources | none of the four quoted; the preface points to Blok's own 1887 edition |
| Blok, Correspondentie van en betreffende Lodewijk van Nassau (Werken HG n.s. 47, 1887) | **partly searched** | not on IA. Google Books full view (vfYnSGD4fpQC), but the text download needs a captcha (not bypassed). HathiTrust nnc1.0036704156 (Columbia, full view) checked through HTRC Extracted Features, per-page token counts | 1573-74 pages (seq 133-173) are German-language letters. No token Goch, Weeze, Wees, Meer (except seq 147, German), Cartilz, chiffre, cijfer, Mars/Avril/Juin/Juillet at those pages. A bag-of-words check, not a page reading |
| WVO database record and Bron/Literatuur | searched | 4 record pages fetched 24 Sept 2026 | Bron is the manuscript only. 4610 points to its reply 4497. No solution note |
| KHA inventories; HHStA Wiesbaden (Nassau-Dillenburg papers, where a primary of the duplicate 4610 or a file copy could be) | **not searched** | | gap |
| Google Books phrase search | searched | googleapis, 6 queries: incipits of 4610/4612/4616, "Lambert Certain" Nassau, Blok 1887 title | 0 hits on the incipits; the cover name "Lambert Certain" is printed widely (Kervyn 1884, Namèche 1885), which is not relevant to these four |
| IA full text (be-api, global) | searched | "aupres de Goch", "arrive aupres de Goch", "camp de Weess", "faisons amasser le plus", "sans mettre rien au hazard", "correspondance de Bruxelles" Nassau 1574, "de la rechute" Nassau 1573, "Lambert Certain" | 2 hits for "aupres de Goch" (Mercure hollandois 1678, unrelated); the rest are generic or unrelated |
| DBNL full text | searched through Groen texts | whole-site phrase search not run | partial |
| Solver repos, Cryptiana, Cipherbrain, DECODE | relied on check-solved of 24 Sept 2026 (NOTES.md "Check-solved sweep") and `sources/decode/` | not re-run | no hit |
| Scholarship | partly | CrossRef 4 queries (nothing relevant); HAL 1 query: one hit, "Louis de Nassau et le parti huguenot" (2007), **not read**; OpenAlex **unreachable** (shared daily budget exhausted, HTTP 429); Semantic Scholar **unreachable** (429, stopped); Persée reached, not parsed; JSTOR 3 rows queued | no cryptologic study of these letters found |

## 4. Evidence

| source | locator | what it shows |
|---|---|---|
| Groen, Archives I/IV (1837), Lettre CDXXVII, pp. 156-160 | DBNL groe009arch04_01, "[pagina 156]" | Orange, Leiden, 17 Jun 1573: "Vostre lettre du 3e jour de ce mois ... la fiebvre vous a de rechief quicté"; the Emperor's answer to princes about pacification; three cavalry companies. This answers 4610 |
| Groen IV, Lettre CDXXXIII, p. 175ff | DBNL groe009arch04_01 | Orange, Delft, 22 Jul 1573: "j'ay receu vostre lettre du second jour de ce mois". This answers 4611 |
| Groen IV, Lettre CDLXXXIV, pp. 368-369 | DBNL groe009arch04_01 | Orange, Gorinchem, 15 Apr 1574: "receu vostre lettre du xije du présent, et veu par icelle jusques à où vous estes arrivé". This answers 4616 |
| Groen, Supplément (1847), no. 49, pp. 154*-156* | DBNL groe009arch09 | Lodewijk to Orange, camp de [Cartilz], 4 Apr 1574, printed in full, not in cipher. A sibling, not an audited item |
| WVO 4610/4611/4612/4616 | resources.huygens.knaw.nl/wvo/app/brief?nr=... | manuscript only; incipits; no solution |
| HathiTrust nnc1.0036704156 (Blok 1887) | HTRC EF API | 1573-74 section is German; no French letter at these dates |

## 5. Did we first-decipher?

No. Orange read these letters in 1573-74. His printed replies to three of them answer their content, so a
contemporary decipherment existed on the recipient's side, even though none survives in the file (WVO) or was
located in print. The key used here is itself contemporary: it was aligned from the period decipherments of 4613
and 4615. What this repository has is a partial modern reading, with a period key recovered by alignment, of four
letters whose text was not located in print.

N4 is withheld because (1) Blok 1887, the principal edition of Lodewijk's correspondence, was checked only by
per-page word counts and not read; (2) Kervyn's *Relations politiques*, the KHA inventory and the Nassau papers
in Wiesbaden were not searched; (3) OpenAlex and Semantic Scholar were unreachable and the HAL item (2007) was
not read; (4) the reading is too gappy for a phrase search on deciphered text, so phrase searches used only the
clear incipits.

Confidence: moderate that no full print of these four exists in Groen, Gachard or Kervyn (read by grep of full
text; OCR for Gachard and Kervyn). Lower for Blok 1887.

## 6. Safe and unsafe sentences

- **4610**: safe: "WVO 4610 (3 June 1573) is partly read with a key aligned from the contemporary decipherments of
  WVO 4613/4615. No prior plaintext or decipherment of this letter was located in the sources listed in AUDIT.md.
  Orange's printed reply of 17 June 1573 (Groen IV, Lettre CDXXVII) answers its content." Unsafe: "the first
  decipherment of Lodewijk's letter of 3 June 1573".
- **4611**: safe: "WVO 4611 (2 July 1573) is partly read with the 4613/4615 key. Its text was not located in
  print in the sources listed in AUDIT.md, and Orange acknowledges it in Groen IV, Lettre CDXXXIII." Unsafe:
  "previously unread".
- **4612**: safe: "WVO 4612 (6 March 1574): the 4613/4615 key reads its clear passages and a few keyed words.
  Most of its numeral runs do not yet read as French. No prior plaintext or decipherment was located in the
  sources listed in AUDIT.md." Unsafe: "4612 read in French" or "newly recovered".
- **4616**: safe: "WVO 4616 (12 April 1574, two days before Mookerheyde) is partly read with the 4613/4615 key. No
  prior plaintext or decipherment was located in the sources listed in AUDIT.md. Orange's reply of 15 April 1574
  (Groen IV, Lettre CDLXXXIV) acknowledges it." Unsafe: "Lodewijk's last letter, unread until now".

## 7. Postmortem and corrections

The folder makes no novelty claim; the solver wrote "Novelty not classified". Three sentences over-reach, and
they are corrected in place:
1. status.json results row: "The four targets read in French where both passes agree". 4612 does not: its keyed
   runs are mostly not French under this key. Rewritten with the class and the safe sentence.
2. NOTES.md "Nobody has yet attempted that alignment" is a claim about everyone. It now reads "No prior
   alignment was found in the sources checked".
3. NOTES.md check-solved verdict "No solution, key, plaintext or documented attempt found in six sources" is
   left as a search result. A pointer to the printed replies has been added, because they show the letters were
   read in 1574 and they carry part of the substance.

Lesson for the next solver brief: grade C on a numeral says the key value is attested, not that the output reads.
Report per letter the share of keyed runs that read as French, and test 4612 (Mar 1574) for a changed table
before extending the key.

## 8. Second-opinion claims not confirmed

None filed yet. The prompt is `second-opinions/PROMPT-chatgpt.md`.

## 9. Requests (this session)

dbnl.org 9; archive.org advancedsearch 10, metadata 7, download 7; be-api.us.archive.org 11; resources.huygens.knaw.nl
4; www.googleapis.com 7; books.google.com 4 (search-in-book pages and one epub link, which returned a captcha page;
stopped); catalog.hathitrust.org 3; data.htrc.illinois.edu 2; openlibrary.org 1; api.openalex.org 7 (all 429);
api.semanticscholar.org 4 (429, stopped); api.crossref.org 4; api.archives-ouvertes.fr 1; persee.fr 1; WebSearch 2.

## Second audit (A1)

Second auditor A1 for LANE V2 (Opus), 24 Sept 2026, 09:20-09:45 UTC (`date -u` read). This session did no solving,
no decoding and no part of the first audit. It set out to find these four letters, their plaintext or a
decipherment in print, by attacking the first audit's named gaps and its method. The WV2 letters are out of scope.

### A1.1 Verdict

| item | V2 class | A1 class | why |
|---|---|---|---|
| 4610 (3 Jun 1573) | N3 | **N4** | every principal family in A1.3 is now covered or shown not principal; no prior plaintext or decipherment located |
| 4611 (2 Jul 1573) | N3 | **N4** | same |
| 4612 (6 Mar 1574) | N3 | **N3** (kept) | coverage is the same as the others, but there is no reading to qualify: most keyed runs do not read as French, so "no prior decipherment located" would describe a decipherment this repo does not have. Re-class when a reading exists |
| 4616 (12 Apr 1574) | N3 | **N4** | same as 4610; the reading is short (226 numerals) and partial |

Nothing was found that lowers any item to N0-N2. N4 still means only that the principal editions, catalogues and
project pages were covered. Internal or unpublished work, including a file copy in the Nassau papers at Wiesbaden,
is not excluded (see A1.3, Wiesbaden).

### A1.2 What was attacked, and the result

1. **Bundled print in the WVO PDFs** (LANE N lesson, ROOM 09:16). All 13 rendered pages (4610 p1-4, 4611 p1-4,
   4612 p1-3, 4616 p1-2) were viewed as a contact sheet. Every page is manuscript: cipher, clear words, and address
   leaves with seals. None is printed and none carries an interlinear decipherment. The four PDFs were then
   re-fetched (4 requests) to check that nothing had been dropped when they were rendered. They hold 4, 4, 3 and 2
   image XObjects, the same as the page counts in `images/manifest.json`. Their only fonts are for the KHA footer
   caption, so they contain no bundled text page. The PDFs were deleted after the check.
2. **Blok, Correspondentie van en betreffende Lodewijk van Nassau (Werken HG n.s. 47, 1887)**, the first audit's
   main gap. It is on neither IA nor Delpher, so it was searched inside Google Books vfYnSGD4fpQC through the
   search-within endpoint (23 queries, no captcha). Positive controls hit: "Lodewijk" 20, "1574" 15, "Dillenburg" 6,
   "Monseigneur" 16. Zero hits: Goch, Weeze, chiffre, cijfer, duplicata, "Pour Hollande", Mook, Cartilz, xije.
   "Wees" and "Meer" hit only unrelated pages (p.184 "wees reeds", p.129 German "Meer", p.v, p.157). The table of
   contents (pp. x-xiii, read through the snippets; [V3c, 24 Sept 2026: pp. XI-XIII since read from page photographs, see
   'Second opinion SO-LODEWIJK-1573-74']) lists for 1573-74 only letters with Hesse, Mainz, Saxony,
   Hendrik and Willem van den Berghe, and Orange to his brothers (LXI, 16 Oct 1573; LXII, 10 Oct). There is no
   letter of Lodewijk to Orange of 3 June or 2 July 1573, or of 6 March or 12 April 1574. **Result: none of the four
   is in Blok 1887.** This rests on search-within plus the table of contents, not a page-by-page read.
3. **Blok, Lodewijk van Nassau (1889)**, full djvu text (IA `lodewijkvannass00blokgoog`) grepped. It never
   mentions a cipher, and it quotes none of the four. It led to two families V2 had not listed (items 6 and 7).
4. **Kervyn de Lettenhove, Relations politiques des Pays-Bas et de l'Angleterre t. VI (1571-73) and VII
   (1574-75).** [Correction, V3c, 24 Sept 2026, from the title pages: t. VI covers 5 Oct 1570 - 29 Nov 1573,
   t. VII 29 Nov 1573 - 28 Oct 1575, both Brussels 1888. Both were grepped in full, so coverage of the four dates is unchanged.] V2 logged these as "IA title search found no item". They are on IA as `relationspolitiq06nethuoft`
   and `relationspolitiq07nethuoft`, and their full text was grepped. Their "(En chiffre)" pieces are all from
   Spanish agents (Guerau de Spes, Guaras, Sweveghem, Mendoza). Every "Lettres interceptées" heading (for example
   t. VI no. MMDCXIX, 17 Aug 1573; t. VII, Heton, 3 Jan 1574) concerns English or Spanish correspondence. Louis
   appears only in third-party reports. **None of the four is there.**
5. **Groen, 1st series t. IV, by date and for cipher notes.** The DBNL text was re-fetched and every
   chiffr/déchiffr/indéchiffr occurrence read in context. The only decipherment note is on p. 89 (May 1573): a
   letter to the Nassau brothers "Depuis ce poinct il y a du chiffre dont le sens est icy joinct, tiré de la main de
   Sinisgar", with Groen's footnote "Nous regrettons de n'avoir pas trouvé ce déchiffrement". That is a different
   letter (May, sent to Louis, not from him). No note near the four dates. The Supplément had been covered by V2;
   the 2nd series t. I (1584-) is outside the range. Context from WVO's cipher-remarks sweep
   (`sources/solver-diffs/2026-09-24-lane-n-wvo-cijfer-96.tsv`): the sibling 4614 (4 Apr 1574) is "het origineel
   hoofdzakelijk in cijferschrift", yet Groen's Supplément no. 49 prints it in clear. So Groen printed cipher
   letters of this series when he had a decipherment, and he printed none of these four.
6. **La Huguerye, Mémoires inédits, ed. A. de Ruble (SHF, 1877), t. I** (IA `mmoiresindit01lahuuoft`). La Huguerye
   was Louis's secretary in 1573. Pp. 175-176 describe this correspondence: "Nous estions contrainctz de faire une ou
   deux, quelquefois trois, duplicata des dépesches adressantes aud. sr prince d'Orenge". He also "renforcer le
   chiffre, qui estoit significatif, de quatre choses, sillabes, lettres, vocables et nulles", and says that "bien
   que le duc d'Albe surprint souvent de ses pacquetz, si n'en peult-il jamais tirer la substance". This fits
   4610's duplicate status and the numeral design. It is a period statement that the Spanish did not read
   intercepted packets of this series, and it prints no plaintext of any of the four. The introduction (p. xl)
   lists La Huguerye's own printed letters: 20 Oct 1573 (Groen IV p. 216), May 1574 and 10 Jul 1574 (Groen
   Supplément). None is one of the four.
7. **Meulleners, "Legertochten tusschen Maastricht en Mook", Publications ... du Limbourg t. XXV (1888)** (IA
   `publicasocietehistlimbourg25`, full text). Cited by Blok 1889 for the 1574 campaign. Its sources are local
   Limburg records (Meerssen, Maastricht, Elsloo); it quotes no letter of Louis to Orange. Its "cijferletters" are
   chronogram letters. The continuation in t. XXVI was searched in-item (Goch 0, 1574 1 unrelated).
8. **Spanish intercept route.** CODOIN t. 102 (Requesens and Zúñiga, 1574; IA `coleccindedocu102madruoft`; the
   `...unkngoog` copy is dark, HTTP 500) was grepped: "Ludovico" 2 times, no intercepted or deciphered letter of
   his. IA full-text phrases "cartas del conde Ludovico", "cifra de Ludovico", "Ludovico" descifrada 1574,
   "lettres interceptées" "comte Louis" 1574 returned only unrelated hits (CODOIN t. 111 has Monteagudo's
   "carta descifrada", Vienna, not Louis). The WVO cipher-remarks sweep lists no contemporary copy, Simancas or
   other, of 4610/4611/4612/4616. It does list one for nr. 424, which shows WVO does record such copies when they
   exist. Gachard, Correspondance de Philippe II t. II-III was covered by V2.
9. **Holding-archive catalogue.** The KHA inventory is online (koninklijkeverzamelingen.nl, a JS app, rendered with
   tools/browser_fetch.js, 6 page loads). A 11/XIV d/13a, "Briefwisseling met diversen, 1568-1584", lists "Van
   Lodewijk van Nassau" 3 Jun 1573 (13a-17), 2 Jul 1573 (13a-18), 6 Mar 1574 (13a-19), 25 Mar (13a-20), 4 Apr
   (13a-21), 7 Apr (13a-22) and 12 Apr 1574 (13a-23). The item pages for 13a-17, -18, -19 and -23 say only "Voor
   het digitale exemplaar en een nadere beschrijving zie ... WVO". There is no decipherment and no copy.
10. **Phrase search** (Google Books API with a positive control of 300 hits, IA full text, Delpher books via
    `jsru.kb.nl` SRU collection `DTS_document`; `phrase_hits` in the session log). The reading has no long
    deciphered run that makes sense, so the phrases were the letters' clear-text runs plus the deciphered runs
    that read: "puissions avoir de vous nouvelles", "camp de Weess", "auprès de Goch" 1574, "mandez de la
    correspondance de Bruxelles", "sa pauvre famille", "conte van den Berghe" 1573, "une convocation" électeurs,
    "conseillers des électeurs" 1573, "quelques conditions" négociation électeurs, "Louys de Nassau" "vostre bon
    frere" 1574, "il fault que me pardonnez", "douze florins", "en chiffre" "comte Louis" 1573, "déchiffré" "comte
    Louis de Nassau" 1574, "lettres en chiffre" "Louis de Nassau", "Lambert Certain" Goch. Google Books: 0
    everywhere except one Groen Supplément table hit. IA: unrelated only (SHPF Bulletin t. 14, checked: 1571 La
    Rochelle; others generic). Delpher: 0 for all 16.
11. **Scholarship.** OpenAlex was still 429 (3 requests, stopped). Semantic Scholar was 429 (1 request, stopped).
    The HAL item V2 left unread is Hugues Daussy, "Louis de Nassau et le parti huguenot", in *Entre calvinistes et
    catholiques* (2007), pp. 31-43. It is a conference paper with no attached file, and it was not read. By its
    title it is political history. It stays a suggestion; JSTOR row added.

### A1.3 Principal families

| family | status | what | result |
|---|---|---|---|
| Groen, Archives 1st series III-V, Supplément | covered (V2 + A1 5) | DBNL full text; by date and cipher notes | none of the four; replies to 4610/4611/4616 printed |
| Sender's edited correspondence: Blok 1887 | covered (A1 2) | Google Books search-within, 23 q with controls; table of contents | none |
| Sender's biography: Blok 1889 | covered (A1 3) | IA full text | none; no cipher mention |
| Recipient's edited correspondence: Gachard, Guillaume le Taciturne t. III | covered (V2) | IA full text | none |
| Documentary editions: Kervyn, Huguenots et Gueux III; Relations politiques VI-VII; Gachard, Philippe II II-III; CODOIN 102 | covered (V2 + A1 4, 8) | IA full text | none |
| Secretary's memoirs: La Huguerye, Mémoires t. I | covered (A1 6) | IA full text | describes the cipher and duplicates; no plaintext of the four |
| Regional study: Meulleners, Limbourg XXV-XXVI | covered (A1 7) | IA full text | none |
| Holding archive: KHA inventory A 11/XIV d/13a | covered (A1 9) | online inventory, item pages | points to WVO only |
| Project pages: WVO records and cipher-remarks sweep | covered (V2 + A1 8) | 4 record pages; 96-row remarks sweep | manuscript only; no copy or solution |
| Page images (bundled print) | covered (A1 1) | 13 pages viewed; PDF objects counted | no print, no gloss |
| IA / Google Books / Delpher full text | covered (V2 + A1 10) | 16 new phrases × 3 hosts | none |
| DBNL | covered through the Groen texts; no whole-site phrase search | | partial, not principal beyond Groen |
| Solver repos, Cryptiana, Cipherbrain, DECODE | covered by check-solved, 24 Sept 2026 (NOTES.md) | | none |
| Scholarship | partly: CrossRef, HAL searched; OpenAlex, Semantic Scholar unreachable (429); Daussy 2007 not read; JSTOR queued (4 rows) | | no cryptologic study found |
| HHStA Wiesbaden Abt. 170/171 (Arcinsys) | **not searched in-catalogue** (WebSearch only). **Not principal for this class**: the four are Orange's received originals in the KHA, and a Dillenburg file copy would be unpublished work, which N4 does not exclude | | open; a suggestion |

### A1.4 Did we first-decipher?

No, in the sense of rule 10. Orange read these letters in 1573-74, and his secretaries worked from a key of this
system, as the decipherments on 4613/4615 show. What the repository has is a partial modern reading of 4610, 4611
and 4616, with a period key recovered by alignment. After the logged search no prior decipherment of them was
located. 4612 has no reading yet.

Confidence: moderate-high that no printed edition carries these four. Groen, Blok (both), Gachard, Kervyn (both
works) and La Huguerye are the editions that would, and the KHA and WVO catalogues give no copy. Lower for
scholarship: the open indexes were unreachable.

### A1.5 Safe and unsafe sentences

- **4610** safe: "WVO 4610 (Lodewijk van Nassau to Orange, 3 June 1573, duplicate) is partly read with a key aligned
  from the contemporary decipherments of WVO 4613/4615. No prior decipherment was located in the principal
  editions (Groen, Blok 1887 and 1889, Gachard, Kervyn), the KHA inventory or WVO; see AUDIT.md." Unsafe: "first
  decipherment of Lodewijk's letter" without "no prior decipherment located"; "unread since 1573" (Orange read it).
- **4611** safe: the same with "2 July 1573"; Groen IV CDXXXIII acknowledges it. Unsafe: "previously unread".
- **4612** safe (N3 kept): "WVO 4612 (6 March 1574): the 4613/4615 key reads its clear passages and a few keyed words;
  most keyed runs do not yet read as French. No prior decipherment was located in the sources listed in AUDIT.md."
  Unsafe: any "decipherment" or "first" wording.
- **4616** safe: "WVO 4616 (12 April 1574, near Goch, two days before Mookerheyde) is partly read with the 4613/4615
  key; no prior decipherment was located in the principal editions, the KHA inventory or WVO; Orange's reply of
  15 April 1574 (Groen IV CDLXXXIV) acknowledges it." Unsafe: "Lodewijk's last letter, unread until now".

### A1.6 Postmortem

The first audit's method was sound, but it closed two families too early. (1) Its IA title search missed Kervyn's
*Relations politiques*, which is on IA under a Toronto identifier. That was harmless: nothing is there. (2) It
did not follow the leads from Blok 1889's footnotes: La Huguerye's *Mémoires*, which describe this very cipher and
the duplicate practice, and Meulleners. Both are closed now with no plaintext. The Google Books captcha that
stopped V2 applies to download, not to the search-within JSON, which answered 23 queries without one. Record that
route for the next verifier. Nothing in the folder over-claims after V2's corrections. status.json and the second
opinion prompt are updated to the new classes and the new sources.

### A1.7 Requests (this session)

archive.org advancedsearch 9, metadata 1, download 6 (1 HTTP 500); be-api.us.archive.org 23; www.googleapis.com 17;
books.google.com 23 (search-within); jsru.kb.nl 24; www.delpher.nl 1; www.dbnl.org 1; resources.huygens.knaw.nl 4;
www.koninklijkeverzamelingen.nl 2 curl + 6 browser loads; api.openalex.org 3 (429); api.semanticscholar.org 1 (429);
api.archives-ouvertes.fr 2; WebSearch 3.

## N4 decision (D1)

N4-decision verifier D1 for LANE V2 (Opus), 24 Sept 2026, 09:48-10:00 UTC (`date -u` read). This session did none
of the solving, did no part of V2's or A1's audits, and did no decoding. Question: does the logged coverage of 4610,
4611 and 4616 (N3 by V2, set to N4 by A1, commit cec1a0f) meet rule 10's N4? 4612 (N3, no reading) is out of scope.

**Answer: yes. 4610, 4611 and 4616 are N4 (no prior decipherment located).** 4612 stays N3, as A1 set it.

### D1.1 Principal families

| family | covered by | with what | result |
|---|---|---|---|
| Groen, Archives 1st ser. t. III-V, Supplément, Table | V2 + A1 5 | DBNL full text; by date and every chiffr- note | none of the four; Orange's replies to 4610/4611/4616 printed (CDXXVII, CDXXXIII, CDLXXXIV) |
| Groen 2nd series | A1 5 | range | starts 1584; not applicable |
| Japikse, Correspondentie van Willem den Eerste | V2 | range | stops 1561; not applicable |
| Blok, Correspondentie ... Lodewijk van Nassau (1887) | A1 2 (V2 only EF) | Google Books search-within, 23 q with controls; table of contents | none |
| Blok, Lodewijk van Nassau (1889) | V2 + A1 3 | IA full text | none; no cipher mention |
| Gachard, Correspondance de Guillaume le Taciturne t. III | V2 | IA full text | none |
| Gachard, Correspondance de Philippe II t. II-III; CODOIN 102 | V2 + A1 8 | IA full text | no intercept of the four |
| Kervyn, Huguenots et Gueux III; Relations politiques VI-VII | V2 + A1 4 | IA full text | none |
| La Huguerye, Mémoires t. I (the sender's secretary) | A1 6 | IA full text | describes the cipher and the duplicates; prints none of the four |
| Huygens ING / WVO records, PDFs, cipher-remarks sweep | V2 + A1 1, 8 | 4 records; 13 pages; PDF object count; 96-row sweep | manuscript only; no bundled print, gloss, copy or solution |
| Holding archive: KHA inventory A 11/XIV d/13a | A1 9 | online inventory, item pages | points to WVO only |
| Kluckhohn, Briefe Friedrich des Frommen II; Saxon editions | not covered | | **not principal**: they print Palatine and Saxon holdings; these four are Orange's received originals in the KHA |
| Rachfahl, Wilhelm von Oranien | range | vols I-II end in 1569 | not applicable |
| Poullet/Piot, Correspondance du cardinal de Granvelle t. IV-V (1572-75; Spanish-side reports, intercepts) | **not covered**; D1 tried: IA has only t. VI-XI (`correspondancedu00-05gran` are microfilm t. VI-XI; t. X and XI checked by year counts), and Google Books lists no full-view copy (2 API queries) | | unreachable. **Not principal for these items**: the letters reached Orange (he answered three), A1 covered the intercept route through Gachard, CODOIN and the WVO copy sweep, and La Huguerye says Alba never got the substance of intercepted packets. A suggestion |
| Bor, Oorsprongk der Nederlandsche oorlogen | not covered | | not principal for private cipher letters (Bor prints public documents); a suggestion |
| DBNL | V2 + A1 | Groen texts | covered for the edition that matters |
| Google Books, IA, Delpher full text (phrases) | V2 + A1 10 | 16+ phrases × 3 hosts, with controls | none |
| HathiTrust | V2 (HTRC EF for Blok 1887) | superseded by A1's search-within | route, not an edition |
| Solver repos, Cryptiana, Cipherbrain, DECODE | check-solved, 24 Sept 2026 (NOTES.md) | | none |
| Open scholarship | V2 + A1 11 | CrossRef, HAL covered; OpenAlex and Semantic Scholar 429 (do not block N4: Danzay precedent); Daussy 2007 unread | no cryptologic study found |
| JSTOR | queued | JSTOR-QUEUE.tsv lines 52, 53, 54, 60 | does not block (verifier template) |
| HHStA Wiesbaden Abt. 170/171 | not searched in-catalogue | | unpublished work, which N4 does not exclude |

### D1.2 Spot-checks of the audits' claims (re-run, not re-swept)

1. **A1 2, Blok 1887 search-within** (`tools/gbooks_search_within.py vfYnSGD4fpQC`, 4 queries, 3 s apart): control
   "Lodewijk" 20 hits; "Goch", "chiffre", "Weeze" 0 each. Matches A1.
2. **V2/A1, Groen IV replies** (DBNL `groe009arch04`, fetched once): Lettre CDLXXXIV reads "receu vostre lettre du
   xije du présent, et veu par icelle jusques à où vous estes arrivé"; the Delft letter of 22 Jul 1573 reads "j'ay
   receu vostre lettre du second jour de ce mois". Both as cited.
3. **Groen IV cipher notes** (same file): the one "duplicata ... sans aulcun chiffre" passage (Nov 1573) is Orange to
   his brothers, not one of the four. Consistent with A1 5.

### D1.3 Decision

The principal editions (Groen, Blok both, Gachard both series, Kervyn both works, La Huguerye), the holding archive's
inventory and the project pages (WVO) are covered, most by full text and all with logged method. The uncovered
families are either out of range, not principal for received originals, or unpublished. **4610, 4611, 4616: N4
confirmed.** Confidence moderate-high for print; lower for scholarship (open indexes 429; Daussy 2007 unread).
The readings are partial; the safe sentences say so.

Safe sentences: A1.5 stands, verbatim, for each of the three. Unsafe: any "first decipherment" without "no prior
decipherment located", "unread since 1573" (Orange read them), "read in full".

Outreach: gate 2 open only on JSTOR lines 52-54, 60 (ASKS row 36). CONTRIBUTIONS.md row added, held at gate 2.

Requests (this section, D1): books.google.com 4; www.dbnl.org 1; archive.org 9 (advancedsearch 3, metadata 4, djvu
downloads of Granvelle t. X-XI 2); www.googleapis.com 2 (Granvelle).

## WV2 letters (V7): WVO 5811 and 4503, novelty audit (24 Sept 2026)

Verifier V7 for LANE V2, 24 Sept 2026, 10:45-10:55 UTC. This session did not solve these letters and does not defend
the solver's conclusions. No decoding; the cipher was not re-read. The four classes above (4610, 4611, 4616 N4;
4612 N3) are not touched.

Claim under audit (status.json results row "William of Orange to Louis of Nassau, 1574"; NOTES.md W1/W2): 5811 and
4503 read under R18's key (`decode_wv2.json`), 5811 C 616 I 81 M 792 U 53 of 1542, 4503 I 7 M 219 U 11 of 237,
"novelty not audited"; NOTES.md "WV2" section: "None carries a solution word in WVO's Opmerkingen ... Verdict: open".

### V7.1 Verdict

| item | date, place | prior plaintext | prior decipherment | class |
|---|---|---|---|---|
| 5811 | 13 Apr 1574, Dordrecht; Orange (signed for him by Nicolaas Brunynck) to Counts Jan, Lodewijk and Hendrik | **yes**: Groen van Prinsterer, Archives 1st ser. IV (1837), Lettre CDLXXXIII, pp. 364-366, the letter's full text including the postscript "Quant à Eyndhoven" and Brunynck's covering note | the print is this letter's plaintext, and WVO's own record of the cipher original (KHA A 3, 895/I) cites that print as the same letter; no separate decipherment sheet located | **N0** |
| 4503 | 15 Apr 1574, Gorinchem; Orange to Lodewijk, answering 4615 and 4616 | **yes**: Groen IV, Lettre CDLXXXIV, pp. 368-369, printed with omissions (WVO: "(onv)", onvolledig; Groen's "...." marks) | as for 5811: WVO's record of the original (KHA A 2, 723 A/I) cites the print | **N0** |

Why N0 and not N1: rule 10 separates "plaintext and decipherment of this very item already known" (N0) from
"plaintext already published anywhere" (N1). Here the printed text is not a parallel or clear copy of a different
document: it is the text of these two letters, and the holding catalogue links the cipher originals to the print
entry by entry. Groen does not say how he obtained the plain text (no "chiffre" note at either letter); if a clear
minute rather than a decipherment was his source, the class would read N1. Either way our readings are
re-decipherments of printed letters. N0 is the conservative choice; nothing would move either item above N1.

### V7.2 Evidence

| source | where | what it shows |
|---|---|---|
| WVO record 5811 | resources.huygens.knaw.nl/wvo/app/brief?nr=5811, fetched 10:47 UTC | Brongegevens: KHAG A 3, 895/I origineel; **GPA IV, 364-366 nr. CDLXXXIII**. Opmerkingen: "Grotendeels in cijferschrift. Met postscriptum. Antwoord op de nrs. 4614 en 4615. De brief is bij afwezigheid van de prins ondertekend door Nicolaas Brunynck. Met duplicaatschrijven." |
| WVO record 4503 | .../brief?nr=4503, fetched 10:47 UTC | Brongegevens: KHAG A 2, 723 A/I origineel; **GPA IV, 368-369 nr. CDLXXXIV (onv)**. Opmerkingen: "Gedeeltelijk in cijferschrift. Met een postscriptum. Antwoord op de nrs. 4615 en 4616." |
| Groen IV, CDLXXXIII | DBNL `groe009arch04` (fetched once), pp. 364-366 | "j'ay veu vostre délibération de venir avec voz trouppes pardeçà et à cest effect prendre vostre chemyn entre Grave et Thiel ... une bonne partie de mes Capitaines qu'ilz ayent au plus tost à se trouver ès environs de Tiel ... Escript à Dordrecht, ce xiij jour d'apvril 1574." Addressed "A Messieurs les Contes Jean, Louys et Henry de Nassau" |
| Groen IV, CDLXXXIV | same file, pp. 368-369 | "pour estre bien mal possible d'assambler en telle haste les gens que je désire de envoyer pour vostre escorte. Et toutesfois j'espère que pour demain aurons quelques trente-cinc ou trente-sis Compaignies ensemble ... me mander au plustost où vous avez délibéré de passer la rivière, pour vous y aller recepvoir ... Escript à Gorichum, ce xve jour d'Apvril 1574" |
| Script comparison (V7, letters only, v/u j/i y/i folded, difflib) | readings vs Groen text | 4503: 90.4% of the reading's 375 letters align to CDLXXXIV (79.2% in runs of 8+); 5811 p1+p2: 87.9% of 958 (62.8%); 5811 p5 (the duplicate): 78.9% of 796 (32.4%). Control, the same readings against an unrelated Groen letter of the same week (CDLXXXVI, same length): 4503 45.6% (13.6%), 5811 p1+p2 24.6% (5.3%). The readings are these printed letters |

### V7.3 Principal families

| family | status | what | result |
|---|---|---|---|
| Holding catalogue (WVO, Huygens) | searched | brief records 4503, 5811 (2 requests) | both cite Groen IV by page and number |
| Groen, Archives 1st ser. t. IV | searched | DBNL full text, read by date (13 and 15 Apr 1574), Lettres CDLXXXIII-CDLXXXVI | both printed; no cipher note at either |
| Groen t. V, Supplément; Japikse; Gachard (Guillaume t. III; Philippe II t. III); Kervyn; Blok 1889; Google Books API; IA full text; DBNL phrase search | not searched | not needed: the canonical edition and the holding catalogue already give the floor class N0; a further print could not change it | -- |
| JSTOR, second opinions | not queued | an N0 item needs neither (brief: second opinion only at N3+) | -- |

### V7.4 Did we first-decipher?

No. Both letters were printed in full (5811) or nearly in full (4503) in 1837, and WVO cites those prints on the
records of the very originals the solver worked from. What the readings do show is that R18's key, aligned on
4613/4615, reads the 1574 letters of Orange's chancery: a key validation, not a new text.

What the all-M grade of 4503 means for the class: M is the solver's transcription grade (both blind passes marked
their digits uncertain, so no token reached H or C). It limits what the reading can support on its own; it does
not bear on novelty. Had nothing been printed, a reading made only of M tokens could have supported "read in
continuous French, uncertain per sign", not a text for anyone to cite. Because the text is printed, the grade question
reverses: Groen's text is now known plaintext, and the solver can align it to regrade 4503's and 5811's tokens as C
(rule 4) and to test the M and U signs. The word-level differences worth that test (image, not print, decides):
5811 "[uingt][cheuaulxlegiers]" where Groen prints "pour la cavallerie"; "Quant au S'r Eschange" where Groen prints
"Quant au Rittmaistre Schenk"; 4503 "je crois que" where Groen prints "j'espère que". Groen also omits part of 4503;
no stretch of our 4503 reading was found outside the printed text.

Confidence: high. Both identifications rest on the holding catalogue's own citation, on dates, places and
correspondents, and on a script alignment against a control.

### V7.5 Safe and unsafe sentences

- **5811** safe: "Orange's letter of 13 April 1574 from Dordrecht to his brothers (WVO 5811) is printed in Groen van
  Prinsterer, Archives IV, Lettre CDLXXXIII; our reading under the 4613/4615 key is a re-decipherment that agrees with
  that print." Unsafe: "a newly read letter from the eve of Mookerheyde".
- **4503** safe: "Orange's letter of 15 April 1574 from Gorinchem to Lodewijk (WVO 4503) is printed, with omissions, in
  Groen IV, Lettre CDLXXXIV; our reading re-deciphers the cipher body and agrees with the print." Unsafe: "the
  unread letter that never reached Lodewijk".

### V7.6 Postmortem

Failure: the WV2 check-solved row (NOTES.md "WV2") read WVO's Opmerkingen for a solution word and its archive codes
column, but treated the code **GPA** as "inferred" (sources/wvo/NOTES.md) and never read the Brongegevens line, which
names Groen by volume, page and letter number. The two letters then went through capture, two passes, a build and
a settle attempt (W1, W2) before anyone opened Groen IV at 13-15 April 1574, where V2 had already cited Lettre
CDLXXXIV as "Orange's reply to 4616" earlier the same day without connecting it to WVO 4503. Lesson for the
check-solved and scout briefs: on a WVO row, the Brongegevens field is part of the status check; **GPA means printed
in Groen's Archives**, and every WVO cipher row carrying GPA (in `sources/wvo/cipher-letters-2026-09-24.tsv`: 5194,
5200, 5207, 5213, 5218, 5221, 5222, 5549 [GPAS], 5797, 5799, 5810, 10260 besides these two) should be looked up in
Groen by the cited page before any reading effort. Not done here (other items, outside this brief).

Corrections made in place: NOTES.md "WV2" verdict line (4503 and 5811 annotated as printed); status.json results
row for 5811/4503 (novelty field). NOTES.md status word stays `partial`.

Requests (V7): www.dbnl.org 1; resources.huygens.knaw.nl 2. No other hosts. No subagents.

## Residual families (LANE V3 G1, 24 Sept 2026)

Searcher, not a verifier: LANE V3 worker G1 (Sonnet, cap $5), 24 Sept 2026, 12:05-12:15 UTC. This session did not
solve, decode or re-read the cipher, and set no N-class. It closed named gaps against D1's table (section "N4
decision (D1)" above) for 4610, 4611 and 4616 (N4) and 4612 (N3, out of scope for class change). Nothing here
lowers or raises a class; the results go to the next N4-decision or retrospective session.

| family | searched or unreachable | route and queries | result |
|---|---|---|---|
| Daussy, "Louis de Nassau et le parti huguenot" (2007), the HAL item D1/A1 left unread | **searched** | `api.archives-ouvertes.fr/search/` confirmed `openAccess_bool: false` (no attached PDF on HAL: not a reachability accident, the deposit itself carries no file). The piece is a chapter (pp. 31-43) in *Entre calvinistes et catholiques : les relations religieuses entre la France et les Pays-Bas du Nord (XVIe-XVIIIe siècles)*, ed. Krumenacker (PUR, 2007). Found on Google Books as `tjUsAQAAMAAJ` (NO_PAGES for the ordinary API, but `tools/gbooks_search_within.py` reaches it). Ran single-word search-within queries landing inside the article's own page range (31-43): "1573" hit pp. 40 and 42 (about the Schomberg embassy to the German princes, not Nassau's letters); "chiffre" returned only pp. 139 and 258, outside the article; "Orange" returned only pp. 240-262 (the town in Vaucluse, a different chapter); "Goch" and "Weeze" returned nothing in the volume at all; "Louis de Nassau" (3 words) was blocked by the endpoint | **No cipher, no Goch/Weeze, no chiffre inside Daussy's own pages.** By its title and this page-anchored sample it is party-political history (the huguenot party's dealings with Louis), not a cipher or correspondence study; nothing found that quotes or prints 4610/4611/4616. Read at the page level via search-within snippets, not a full page-by-page read: residual risk is small (the terms tried are exactly what a cipher discussion would use) but not zero |
| Poullet/Piot, *Correspondance du cardinal de Granvelle, 1565-1586* — D1 logged "IA has only t. VI-XI... Google Books lists no full-view copy (2 API queries)" for what D1 called t. IV-V | **re-tried, still inconclusive on tome identity; content negative** | Google Books title search now lists 10 editions of this title (the multi-tome Poullet/Piot continuation series), 5 of them `ALL_PAGES`: `d7hCAQAAMAAJ`, `oNhuxIVUoNkC`, `IEXBRwjsjc4C`, `DVLp0PUCBlgC`, `kZiklb8G1Z8C`. None of the five carries a tome number in its Google Books metadata (title/subtitle/description all blank beyond the series title), so which one(s) cover 1572-75 could not be fixed from the API. Ran search-within (single words, 3 s apart) for "Nassau" (all 5: many hits, none dated 1573-74 or naming Louis's June/July 1573 or April 1574 letters), "chiffre" (3 of 5: only the ordinary sense "number", not a cipher passage), "Weeze" (all 5: zero), "Goch" (all 5: one hit, `DVLp0PUCBlgC` p. 438, "Goch uff Bleyenbeck genommen", German, in a volume whose other hits (Idiaquez, Antonio Pérez) place it in the 1580s, not 1573-74) | Inconclusive on whether the true t. IV/V (1572, 1573-74) is among these five or is one of the `NO_PAGES` copies; **content found is negative** wherever searched. D1's judgement stands unchanged: this correspondence is Spanish-side (Granvelle in Rome/Madrid after 1570), a real risk only for an intercept, and A1 already covered the intercept route (Gachard *Philippe II*, CODOIN 102) with none of the four found; La Huguerye says Alba's interceptions of this series never yielded their substance. Still logged as a gap, since tome identity was not resolved |
| OpenAlex | **unreachable** | 1 query, `api.openalex.org/works?search=...` | HTTP 429, shared-IP daily budget ("$0 remaining; resets at midnight UTC"). Fourth 429 in this folder's log (V2, A1, D1, now G1); does not block N4 (Danzay/D1 precedent) |
| Semantic Scholar | **unreachable** | 1 query, `api.semanticscholar.org/graph/v1/paper/search` | HTTP 429. Same precedent |

No item found that quotes, paraphrases or decodes 4610, 4611, 4612 or 4616. No `flag for LANE V3` raised.

Requests (G1): api.archives-ouvertes.fr 2; www.googleapis.com (books/v1 + search-within) 24; api.openalex.org 1
(429); api.semanticscholar.org 1 (429). No archive.org, no HathiTrust (Granvelle tome identity unresolved, so
LANE W2 was not called in). No subagents.

## Second opinion SO-LODEWIJK-1573-74 (ChatGPT, pull request 8), checked 24 Sept 2026, 16:29 UTC

Verifier V3c (Opus, for LANE V4, session_01HBMnLTuZ2DR2voSQ3vFQHs). Input: `second-opinions/chatgpt-2026-09-24.md` (GPT-6,
copied from branch `second-opinion/SO-LODEWIJK-1573-74`, PR 8, unmerged). It reports no page-citable print and no surviving
independent decipherment of 4610, 4611, 4612 or 4616, and adds cautions and leads. Each checkable claim was checked against
the source named below. No decoding.

| # | claim | source checked | verdict | correction made |
|---|---|---|---|---|
| 1 | Groen IV, Lettre CDLXXXIV, pp. 368-369, Orange to Louis, 15 Apr 1574, acknowledges a letter of the 12th; a reply, not a print of 4616, and not proof that a written decipherment survives | DBNL `groe009arch04_01_0107.php`: "Lettre CDLXXXIV", [pagina 368]-[369], "receu vostre lettre du xij e du présent, et veu par icelle jusques à où vous estes arrivé" | **right**; agrees with section 1 and V7 | none: section 1 already says "no surviving decipherment located" |
| 2 | Groen IV CDXXVII pp. 156-160 and CDXXXIII p. 175ff answer 4610 and 4611 (it marked these unverified) | DBNL `_0045.php` (CDXXVII, "Vostre lettre du 3e jour de ce mois", page markers 157-160 after the letter's start, so it begins on p. 156) and `_0052.php` (CDXXXIII, pages 175-178) | **right** (our citations confirmed) | none |
| 3 | La Huguerye, Mémoires inédits t. I (1877) pp. 175-176 describes the duplicates and the four-part cipher; context, not a print of the four and not a description of the five-number table | IA `mmoiresindit01lahuuoft` djvu text: "duplicata des dépesches" under running head "MÉMOIRES DE LA HUGUERYE. 175"; "sillabes, lettres, vocables et nulles" before head "176" | **right**; the caution matches A1.2 item 6 | none |
| 4 | Blok, Correspondentie ..., WHG n.r. 47, Kemink & Zoon 1887; the contents claim (pp. x-xiii) rests on snippets; zero-hit searches cannot exclude a differently spelled place or a clear copy | Google Books API `vfYnSGD4fpQC` (Kemink and zoon, 1887, 210 pp.); **its scan lead, periodata.nl `BlokCorrespondentieLodewijk.pdf` (photographs by G.W. Drost, 113 slides, title slide "Nieuwe serie nr 47 ... 1887. XIII, 210 blz."), loaded here.** Contents pp. XI-XIII read from the photographs: the 1573-74 entries are LVI-LXXVII (Lodewijk to Hessen 25 May 1573, August of Saxony, Hessen to Mainz, a Schuldbekentenis, Theyllingen, de Fiennes, Orange to his brothers 16 Oct 1573 (LXI), Orange to Lodewijk 10 Oct 1573 (LXII), Lodewijk to Hessen Jan-Feb 1574, Hendrik 13 Jan 1574, Van den Berghe 3 Mar 1574, Malsburg, the Rhenish electors' councillors 31 Mar 1574, Hessen to Saxony Apr-Jun 1574, Frederik of the Palatinate, Nalatenschap); part II (I-XVIII, 1566-1579) has none either | **right** on the bibliography and on the method caution; **the gap it names is now closed at contents level**: no letter of Lodewijk to Orange of 3 Jun or 2 Jul 1573, or 6 Mar or 12 Apr 1574, is listed | A1.2 item 2 and NOTES.md (V2 section) annotated. A contents listing is still not a page-by-page read of every letter; the text pages of the scan were not read (image-only, no text layer) |
| 5 | Kervyn, Relations politiques t. VI covers 1570-1573 and t. VII 1573-1575, not 1571-73 and 1574-75 as AUDIT.md says | IA `relationspolitiq06nethuoft` / `07nethuoft` title pages: "TOME VI ... (5 octobre 1570 - 29 novembre 1573) ... 1888"; "TOME VII ... Première partie (29 novembre 1573 - 28 octobre 1575) ... 1888" | **right** | A1.2 item 4 corrected in place. No coverage effect: both volumes were grepped in full |
| 6 | WVO 4610, 4611, 4612, 4616, dates and KHA A 11/XIV D/13a (marked "inherited from the prompt") | section 2 and section 4 (WVO records fetched by V2) | **consistent with the repo**; not re-fetched | none |
| 7 | No known file/folio for a counterpart in Wiesbaden, Marburg or Dresden; an Arcinsys web-index search found none, which is not a catalogue examination | not re-run | **unverifiable**, and consistent with the residual already logged (A1.3, D1) | none; the Wiesbaden residual stands |
| 8 | 4612's keyed runs mostly fail to read French; a C numeral attests a value aligned in 4613/4615, not the target's word; test 4612 for a changed table | section 2 (4612 775 numerals, C 369; runs "mostly do not read as French") | **right**; matches our own caution | none: 4612 already N3 with no reading; the table-change test is already a logged solver suggestion |
| 9 | Groen IV CDLXXXIII pp. 364-366 is 5811 (it marked this unverified) | DBNL `_0106.php`: "Lettre CDLXXXIII", [pagina 364]-[366]; p. 367 is Groen's commentary on Mookerheyde | **right** (our citation confirmed) | none |

**Its leads, one line each.** Blok page images: done at contents level (row 4); the text pages remain unread and are a
low-value residual, since the contents list no candidate. Kervyn: covered (A1.2 item 4, full-text grep). Item-level archival
counterparts (HHStA 170/171, Marburg, Dresden): the logged residual, not actionable from here. Modern study of the
five-number table: none known to it, none to us.

**Class.** No check found a prior print or decipherment. **4610, 4611, 4616 stay N4** ("no prior decipherment located");
**4612 stays N3**. The Blok 1887 contents check narrows the residual behind N4; it does not raise any item to N5.

Requests (V3c, this label): www.dbnl.org 5; archive.org 3 (one full djvu text, two 6 KB ranges); www.googleapis.com 1;
www.periodata.nl 1. No subagents.

## Outreach gate 2: JSTOR family and open indexes (verifier V5, 24 Sept 2026)

Verifier V5 (Opus, for LANE V4, session_01UBQ2tN51FBuKTx41RqnGAK), 24 Sept 2026 17:24 UTC. Triage of the JSTOR runner's first-page hits (JSTOR-QUEUE.tsv) by title, snippet and what the runner read; no decoding, no class change unless stated.

4 rows (file lines 52-54, 60). The runner wrote no section for this target; triage here. Context only: Revue Historique 'Recueils périodiques' 1900 and 1910 (periodical listings), Erbe (Bauduin 1563), Zijlstra-Zweens (Geuzenschaaltje), Fagel's two chapters in *Protagonists of War* (Dávila and Julián: the Spanish side of Mookerheyde), the Dauxy espionage article (Antwerp 1560s), Motley review 1856, reference works. Daussy 2007 ('Louis de Nassau et le parti huguenot') is not hosted on JSTOR. No candidate.

JSTOR family: searched on the owner's machine 24 Sept 2026, 4 rows, 0 candidates read (none found), result clean. **Gate 2's JSTOR condition is met for 4610, 4611, 4616.** Daussy 2007 remains unread (not on JSTOR).

Open indexes: OpenAlex (`api.openalex.org/works?search=...`) and Semantic Scholar (`/graph/v1/paper/search`) retried once each from the cloud at about 17:21 UTC: both HTTP 429 (shared free daily budget used up). The owner's run of 24 Sept 2026 (ASKS 34) covered Thurloe, Eckert and Blathwayt only; this target's queries are owed (ASKS row 44, `outreach/openalex-s2-owner-queries-2.md`).

Outward drafts written this session (status drafted, nothing sent): see `outreach/` and CONTRIBUTIONS.md.

## Revision log (26 Sept 2026, LANE AX): readings revised after this audit

Worker AX-REDERIV (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-rederiv.md`. This is a log entry, not a
verifier pass: it records what changed in the readings after every class above was assigned, and names what a
verifier should re-check. It sets no N-class and changes none of the classes recorded above.

**What changed.** Since this AUDIT.md's classes were assigned, two LANE AX workers (AX-NAMES2, AX-MERGE, both
26 Sept 2026, logged in this folder's NOTES.md) built `key_full.tsv` -- `key.tsv` plus 22 codes newly licensed
from (a) contemporary interlinear glosses on sibling WVO letters 5550 and 4496 (grade H, rule 4), (b) Groen's
own printed French at the exact 5797 cluster (grade C), and (c) >=4-observation empty-NULL codes from the
sibling-letter aligner (`names.tsv`, grade C) -- and regenerated `reading_{4610,4611,4616}_full.txt` and the
5797 spots file (`reading_5797_full.txt`) from it. `revisions_for_audit.tsv` (249 rows) is the full diff against
the `key.tsv`-only readings this AUDIT.md's classes were written against; this session (AX-REDERIV) independently
re-derived all four readings fresh from `key_full.tsv` and the transcriptions and found them byte-for-byte
identical to the committed files (0 tokens differing from a from-scratch regeneration; NOTES.md AX-REDERIV
section, 26 Sept 2026) -- the revision content below is confirmed reproducible, not merely committed.

**Counts per letter** (NULL placements: a `?`/unkeyed position resolved to a silent null, no letter recovered;
word/name changes: a position now reads a person/place/title):

| letter | class above | NULL placements | word/name changes | total revised | U before -> after |
|---|---|---|---|---|---|
| 4610 | N4 | 122 | 11 | 133 | 288 -> 155 |
| 4611 | N4 | 88 | 8 | 96 | 227 -> 131 |
| 4616 | N4 | 1 | 0 | 1 | 26 -> 25 |
| 4612 | N3 | -- | -- | 0 (not touched; still no reading, key_full does not license a table change) | unchanged |
| 5797 (spots file, not yet classed above) | not classed | 15 | 4 | 19 | 31 -> 12 |

226 NULL + 23 word/name = 249 total, matching `revisions_for_audit.tsv`'s row count exactly (checked by this
session directly against the file, not copied from a prior summary). Note for whoever next reads this: an
earlier in-progress count (AX-NAMES2, before AX-MERGE's second pass) cited "14" word/name rows; the current,
committed `revisions_for_audit.tsv` has 23 (AX-MERGE's pass added the 192/roidespagne and 221/hollande rows
after AX-NAMES2 wrote that figure). The 23 below is what is actually on disk.

**The 23 word/name changes, individually** (position, old value graded U with no letter, new value and grade;
source tag keyed below):

| letter | line | pos | old -> new | grade | source |
|---|---|---|---|---|---|
| 4610 | p1_L33 | 2 | ? U -> roidespagne | H | [S-192] |
| 4610 | p1_L34 | 12 | ? U -> roidespagne | H | [S-192] |
| 4610 | p2_L02 | 1 | ? U -> roidespagne | M | [S-192] (M: sign-confidence downgrade at this position) |
| 4610 | p2_L11 | 18 | ? U -> hollande | H | [S-221] |
| 4610 | p3_L03 | 20 | ? U -> pfaltzgraf | H | [S-153], see flag below |
| 4610 | p3_L08 | 2 | ? U -> roidespagne | H | [S-192] |
| 4610 | p3_L09 | 11 | ? U -> pfaltzgraf | H | [S-153], see flag below |
| 4610 | p3_L13 | 1 | ? U -> roidespagne | H | [S-192] |
| 4610 | p3_L15 | 6 | ? U -> herzogvonalba | C | [S-200] |
| 4610 | p3_L15 | 10 | ? U -> franckreich | H | [S-202] |
| 4610 | p3_L22 | 14 | ? U -> roidespagne | H | [S-192] |
| 4611 | p1_L14 | 12 | ? U -> herzogvonalba | C | [S-200] |
| 4611 | p1_L24 | 7 | ? U -> harlem | C | [S-223] |
| 4611 | p2_L01 | 14 | ? U -> hollande | H | [S-221] |
| 4611 | p2_L02 | 10 | ? U -> herzogvonalba | C | [S-200] |
| 4611 | p2_L10 | 3 | ? U -> hollande | H | [S-221] |
| 4611 | p2_L17 | 18 | ? U -> herzogvonalba | C | [S-200] |
| 4611 | p2_L20 | 4 | ? U -> herzogvonalba | M | [S-200] (M: sign-confidence downgrade at this position) |
| 4611 | p2_L20 | 14 | ? U -> herzogvonalba | C | [S-200] |
| 5797 | p5_spot3 | 2 | ? U -> herzogvonsachsen | C | [S-154] |
| 5797 | p5_spot3 | 7 | ? U -> landgraf | H | [S-161], see key-source check below |
| 5797 | p6_control_abso | 4 | ? U -> herzogvonalba | M | [S-200] (M: sign-confidence downgrade at this position) |
| 5797 | p7_spot2 | 1 | ? U -> pfaltzgraf | H | [S-153], see flag below |

Source key: [S-153] "5550 leaf 2 contemporary interlinear gloss 'Palsgrave' over 153 (x2, runs p2-5, p2-11)".
[S-161] "5550 leaf 2 contemporary interlinear gloss 'Lantgrave' over 161 (run p2-11, bey 153.161 und)".
[S-192] "4496 (WVO PDF p4) contemporary interlinear gloss 'R. d'Espagne' over 192, confirmed by two independent
blind Sonnet passes (AX-GLOSS)". [S-221] "4496 (WVO PDF p4) contemporary interlinear gloss 'Hollando' over 221
(x3), corroborated unglossed in 4614 p1 'tiré de la Haye en 221'". [S-200] "Groen IV p.224 prints 'vom Herzog
von Alba absondern' at 5797 p6 'von 200.122.132.142 abso-'" (print-at-cluster, grade C by rule 4; the one M row
per letter is this session's transcription-confidence downgrade, not a different source). [S-202] "5550
contemporary interlinear gloss over 202 (x4, runs p1-1, p2-3, p2-9, p2-15)". [S-223] "aligned to Groen IV
CDLXVIII (5810) print, 3 of 3 observations agree". [S-154] "Groen IV pp.223-224 prints 'Bey dem Herzog von
Sachsen und' at 5797 p5 'Bey 154.124.144.134 und'".

**Key-source check on 153/161 (this session, AX-REDERIV) -- flag for the next verifier.** I opened WVO 5550
(the source PDF, not on disk before this session) myself and read the interlinear gloss before opening any
transcription of it (NOTES.md AX-REDERIV section has the crops and full account). Code 161's single occurrence
and one of code 153's two occurrences (the run "153.161. und", page 2) carry an unambiguous per-code gloss
reading "Pfaltzgraue" over 153 and "Lanttgraue" over 161 -- this independently confirms the H grade for both.
**Code 153's other occurrence** (the run "153.130.90.1.79.173", same page) carries a different gloss, "Ertz-
hertzoge vnd graf" (Archduke and Count), spanning the six-code run rather than a single word over 153 -- **not**
a confirmation of "Palsgrave" at that spot as [S-153]'s "(x2, ...)" wording implies. This does not overturn the H
grade (the p2-11 occurrence and the 5797 p7_spot2 match against Groen's clear frame both still support
153=pfaltzgraf independently), but a verifier re-confirming the classes above should know the source note's "x2"
corroboration for code 153 is only half borne out by an independent read, and treat the three rows tagged
"[S-153], see flag below" (4610 p3_L03, 4610 p3_L09, 5797 p7_spot2) accordingly.

**For the verifier.** The N-classes above (4610, 4611, 4616 at N4; 4612 at N3) were assigned against the
`key.tsv`-only readings, before `key_full.tsv` existed. These revisions add proper names, place names and
titles read from period interlinear glosses (Palsgrave/Pfaltzgraf, Landgrave, King of Spain, Holland, Duke of
Alba, France, Harlem, Duke of Saxony) plus additional silent-null placements; they do not add any new plaintext
content that was not already implied by the earlier reading's unresolved `?` positions, and this session's own
print/gloss searches (rule 10 sense) were not run -- no new novelty search was done here. A verifier should
confirm the classes still hold given the added name content (in particular, whether any of the eight now-named
titles/places changes what a phrase search for 4610/4611/4616 should have tried) before this folder's classes
are treated as current against `key_full.tsv`. Not done here: novelty was not reclassified, per the brief's
scope; this is a log, not an audit pass.

SO-LODEWIJK-1573-74 (`SECOND-OPINIONS-QUEUE.tsv`): a note was appended to that row's last column pointing back
here, since the second opinion answered was against the pre-`key_full` reading.

## V8 audit: WVO 5797 and key_full revision (26 Sept 2026)

Verifier V8-NA5797 for LANE V8 (session_01YRuw3TCf7d1w85DLmYNnw4), 26 Sept 2026, 03:52-04:09 UTC (`date -u` read). This
session did not solve, align or decode anything and does not defend LANE AX's conclusions (AX-5797, AX-NAMES, AX-NAMES2,
AX-MERGE, AX-REDERIV). No key, ciphertext, decode or reading file was changed.

Claim under audit (LANE AX, ROOM 03:37 UTC 26 Sept 2026): in WVO 5797 (Jan and Lodewijk van Nassau to Orange, Dillenburg,
22 Oct 1573; KHA A 3, 895/I, a *minuut* per its WVO record; printed Groen, Archives 1re serie IV, Lettre CDXLIV,
pp.217-226), two of the passages Groen prints as blanks read under key_full: p5 "Bey dem Herzog von Sachsen und
[161 Landgraf] ist willens", p7 "[153 Pfaltzgraf] helt sich wol und thut in warheit viel", grade H each; plus the
key_full revision of 4610/4611/4616 (revision log above).

### V8.1 Verdict

| item | what is read | prior plaintext | prior decipherment | class | key |
|---|---|---|---|---|---|
| 5797, the letter | Groen's printed text; our six control words (secours, entrepr-, zeuget, abso-, mit, election) re-read words Groen already prints | **yes**: Groen IV CDXLIV pp.217-226 (1837), whole letter bar the blanks | yes for everything Groen prints | **N0** (text known) | -- |
| 5797 p7 spot, code 153 | "[Pfaltzgraf] helt sich wol und thut in warheit viel" (Groen's blank before "helt") | no: Groen IV p.225 prints the blank; not found in any source below | none located | **N4** (no prior decipherment located) | `period` (153 from the 5550 interlinear gloss); the surrounding table `ours` |
| 5797 p5 spot, code 161 | "Bey dem Herzog von Sachsen und [Landgraf] ..." -- **gap partly read**: the same blank also holds 126 (NULL, C), 136 (key_full value 'vingt', M, which cannot be right here) and 146 (U) before "ist willens" | no: Groen IV pp.223-224 prints the blank | none located | **N4** for the one word; the blank is not read in full | `period` (161 from the 5550 gloss); table `ours` |
| 5797, the other four blanks (p5_spot5, p6_spot4, p7_spot6, p8_spot7) and the p.222 garbled paragraph | not read (codes 172, 173, 182, 156 have no key_full row; spot 1's interior never located) | -- | -- | not classed (nothing to class) | -- |
| 4610 | revised by key_full (122 NULL placements, 11 names) | as before | as before | **N4 confirmed** | `ours` (table) + `period` (192, 221, 153, 202 glosses) |
| 4611 | revised (88 NULL, 8 names) | as before | as before | **N4 confirmed** | `ours` + `period`/print-at-cluster C (200, 223) |
| 4616 | revised (1 NULL, no names) | as before | as before | **N4 confirmed** | `ours` |

`text: known` for 5797 (Groen prints the letter); the two single-word readings are the only part not in print.

### V8.2 Grade check (rule 4): 153 and 161

I read the 5550 gloss myself: AX-REDERIV's two crops (`images_wv2/crops_rederiv/05550_p2_153-161_gloss.png`,
`05550_p2_153-130-run_gloss.png`) and a fresh 500 dpi render of 05550.pdf p.2 (one fetch, scratchpad only, not committed).

- **Run p2-11, "153.161. und andere so bu[ndnus]"**: the gloss is two words, one over each code, and reads
  **"Palsgraue Lantgraue"** (the key_full note's 'Palsgrave'/'Lantgrave' is right; AX-REDERIV's NOTES transcribe it
  "Pfaltzgraue ... Lanttgraue", same meaning, different spelling). A clean per-code key-source reading: **H stands for
  161, and H stands for 153 on this occurrence alone** (one clean period gloss is a key source under rule 4; it does not
  need a second).
- **Run p2-5, "153.130.90.1.79.173"**: the gloss spans the run and ends "... vnd graf". Its first word is partly
  overwritten by a descender of the main hand. Its opening letters match the "Pals-" of the p2-11 gloss letterform for
  letterform (same capital, a, l, long s); what follows is unclear (possibly "-duc" or a contraction). I read neither
  AX-REDERIV's "Ertzhertzoge" nor a clean "Palsgrave" there. **Correction to key_full's source note (recorded here, not
  in key_full.tsv, per brief)**: for 153 read "5550 p.2 gloss 'Palsgraue' over 153 at run p2-11 (clean, one word per
  code); the p2-5 gloss over the run 153.130.90.1.79.173 is partly obscured, opening 'Pals-' ... 'vnd graf', not an
  independent confirmation". Consequence: the three rows tagged "[S-153], see flag below" in the revision log
  (4610 p3_L03, 4610 p3_L09, 5797 p7_spot2) keep **H**, from one attestation, not two. None needs M.
- Context, not evidence of value: Glawischnig 1973 (IA fts, below) records that Pfalzgraf Johann Casimir went to Kassel
  (the Landgrave's court) for his father the Elector Palatine soon after 16 Oct 1573, which fits a 22 Oct 1573 letter
  speaking of the Palatine and the Landgrave. It is not a source for the code values and is not used as one.

### V8.3 Did the revision change what the 4610/4611/4616 N4 rested on?

D1's N4 rested on: no prior plaintext or decipherment of these letters located across the principal families (Groen,
Blok 1887/1889, Gachard, Kervyn, La Huguerye, KHA inventory, WVO). key_full adds silent nulls (no letter changes) and
eight names/titles (roi d'Espagne, Hollande, Pfaltzgraf, duc d'Albe, France, Harlem) into still-gappy French. A name
filled in cannot create a prior print; what it can do is give a phrase search a handle it lacked. I built the three
French phrases the revised lines support ("bruit que le duc d'Albe seme icy" 4611 p1_L14; "forces du duc d'Albe le
capitaine" 4611 p2_L02; "frere du roy d'Espagne" 4610 p3_L22) and ran them with the 5797 phrases (V8.4): no hit in any
listed edition; ia-global and Google Books hits for the generic "frere du roy d'Espagne" are other correspondences
(Henri IV, d'Ossat, Jeannin), none a Nassau letter. **4610, 4611, 4616: N4 confirmed**, key `ours` for the table with
the name rows `period` (glosses) or C print-at-cluster, as the revision log tags them. 4612 stays N3 (untouched).

### V8.4 Search log (5797)

| family | status | method | result |
|---|---|---|---|
| Groen, Archives, **both series, every IA copy** (35 identifiers: 1re serie I-VIII + I2 + Supplement, 2e serie I-V) | searched | `tools/print_check.py` (downloads each djvu once, exact + proximity) and my own grep of the cached text | Groen IV located as `archivesoucorre03housgoog` (and `bub_gb_zBQish8rkmAC`), Lettre CDXLIV at text line 12742; both copies print the blanks exactly as dbnl ("Bey dem Herzog von Sachsen und ist", a blank line before "helt sich wol"). No other volume cites CDXLIV or 22 Oct 1573; no later correction or supplement fills a blank |
| Positive control, Groen's own clear words at the spots | searched | same run, ia-global | "helt sich wol und thut in warheit viel": 2 IA items, both Groen copies (`archivesoucorre03pringoog`, `archivesoucorre11pringoog`) -- the method finds this letter's print when it exists |
| 5797 phrases with the names ("Pfaltzgraf/Pfalzgraf helt sich wol ...", "Herzog von Sachsen und Landgraf ist willens", "Sachsen und Landgraf ist willens") | searched | 35 Groen + 6 Gachard + Glawischnig + ia-global + Google Books (keyed, country=US) + OpenAlex + CrossRef | **0 hits anywhere** (print-check.tsv) |
| Gachard, Correspondance de Guillaume le Taciturne I-VI | searched | print_check, IA djvu | 0 hits |
| Blok 1887, Correspondentie van en betreffende Lodewijk van Nassau (HathiTrust nnc1.0036704156) | searched (co-occurrence) | HTRC Extracted Features, all 238 pages: pages carrying Groen's distinctive clear words at the spots (helt+warheit, urbietig, schaumhedt) | none; "Oct" + "1573" only on the table of contents (seq 15, 17). 5797 is not printed there |
| Glawischnig 1973, Niederlande, Kalvinismus und Reichsgrafenstand (IA `niederlandekalvi0000glaw`, lending-only) | searched (full-text search, no pages) | be-api fts inside the item; positive control "Dillenburg" hits | the 5797 phrases 0; "Oktober 1573" hits (Johann Casimir to Kassel; Jan's talks with Salentin of Cologne), no quotation of 5797; "Chiffre" 0 -- the book does not discuss the cipher |
| Rachfahl, Wilhelm von Oranien (IA cache, 2 vols) | searched | local grep | no 22 Oct 1573, CDXLIV or phrase |
| WVO catalogue | searched | brief?nr=5797: Opmerkingen "Met enige passages in cijferschrift. Antwoord op nr. 5804.", Brongegevens GPA IV 217-226 only (KHA A 3, 895/I, minuut); brief?nr=5550: "Gedeelten in opgelost cijferschrift" | no other edition, no solution recorded |
| Tomokiyo, Cryptiana | searched (snapshot of 19 Sept 2026, `sources/cryptiana/web/`) | grep Nassau/Orange/Lodewijk/Ludwig/1573/Dillenburg | Nassau appears only for 1519-1520s letters (Henry of Nassau) and Maurice 1585; nothing on the 1573 Nassau cipher |
| Solver repositories | searched | fresh clones dbourdeau/cyphersolver fc0c9e8, aaymeloglu/unsolved-ciphers 2495c45, grep Nassau/Lodewijk/Dillenburg/5797/Pfaltzgraf/Landgraf and Nassau+1573/1574; deleted after | only 1795-1803 Orange-Nassau items and unrelated hits; nothing on the 1573-74 letters |
| Kervyn de Lettenhove | not searched again | IA advancedsearch for Kervyn "Documents inedits" returned 0; Kervyn's two works were covered for 4610-4616 by A1/D1 and are French/English-state papers, not the Dillenburg-Orange German correspondence | not principal for 5797 |
| Google Books | searched | print_check gbooks (keyed, country=US), 9 calls | 0 for all 5797 name phrases |
| OpenAlex | searched | keyed, 11 calls, 2 keyword sets | one irrelevant work (Mediating War in Early Modern German Prose, 2012) |
| CrossRef | searched | 3 keyword sets | irrelevant (Nassau constitutional texts) |
| Semantic Scholar | **unreachable** | S2_KEY sent; 1 call answered (0 results for "Ludwig von Nassau 1573 Chiffre"), then HTTP 429 twice by hand and once inside print_check; stopped per the good-citizen rule | -- |
| CORE | not searched | CORE_API_KEY unset in this container (key probe) | -- |
| JSTOR | queued | 2 rows appended to `JSTOR-QUEUE.tsv` (Nassau 1573 Chiffre + Pfalzgraf/Landgraf; Graveneinigung/Wetterauer Grafenverein 1573) | never blocks a class on its own |

Rule 7: AX-REDERIV's re-derivation (03:22, byte-identical) is on file; not repeated. Judge: FAIL on reading_5797_full.txt
(spots file below the judge's length; reported as FAIL by AX-NAMES2/AX-MERGE, stands).

### V8.5 Did we first-decipher?

For the two words only, and only in the rule-10 sense: no prior decipherment of the p5 and p7 blanks located after the
search above; the letter itself is in print since 1837. The words were read by putting two name-code values taken from
a *period* gloss on a sibling letter (5550) into blanks located with *our* table. Confidence: moderate for print (Groen
all volumes full text, Gachard, Blok 1887 by co-occurrence, Glawischnig by fts); lower for scholarship (Semantic
Scholar 429, CORE absent, JSTOR queued, Wetterauer Grafenverein literature, e.g. G. Schmidt 1989, not reached).

### V8.6 Safe and unsafe sentences

- **5797, safe:** "In WVO 5797 (Jan and Lodewijk van Nassau to Orange, 22 Oct 1573), printed by Groen van Prinsterer in
  1837 with several passages left undeciphered, two of the blanks read in part, 'the Palsgrave (Pfaltzgraf) holds
  well' and '... and the Landgrave ...', by locating them with a letter table recovered by our own cryptanalysis and
  valuing the two name codes from a contemporary interlinear gloss on the sibling letter WVO 5550; no prior decipherment
  of these blanks located (N4); the letter's other text is Groen's."
- **5797, unsafe:** "We deciphered Lodewijk's 22 Oct 1573 letter", "the missing passages of Groen's CDXLIV are now
  read", "first decipherment", "newly recovered names", or any sentence that calls the p5 blank fully read (136 and
  146 sit unread in it) or calls the name values ours (they are the 5550 gloss's).
- **4610, 4611, 4616:** A1.5's safe sentences stand, with "read in part with a letter table aligned from contemporary
  decipherments of sibling letters, some names valued from contemporary glosses" where a name is quoted.

### V8.7 Postmortem and corrections

Failure found: the key_full source note for 153 claims two gloss attestations; one is clean, the other partly
obscured (V8.2). AX-REDERIV caught it and then over-corrected in the other direction ("Ertzhertzoge"); neither read is
established on the p2-5 run. The grade does not move. Second: AX-NAMES2's table marks the p5 spot "gap filled? yes";
it is filled by one word out of four codes (NOTES.md annotated). No sentence in the folder calls 5797 new, first or
unpublished; nothing else corrected. SO-LODEWIJK-1573-74: the answered prompt predates key_full and does not cover
5797; a dated note was added to the prompt file and the queue row.

Requests (this session): resources.huygens.knaw.nl 3 (05550.pdf, brief 5797, brief 5550); archive.org 46
(advancedsearch 5, print_check 41); be-api.us.archive.org 34 (print_check 27, by hand 7); www.googleapis.com 9;
api.openalex.org 11; api.crossref.org 3; api.semanticscholar.org 4 (1 answered, 3 x 429, stopped);
data.htrc.illinois.edu 1; github.com 4 (two shallow clones, twice). No subagents.

## Revision log v3 (26 Sept 2026, LANE AX)

Worker AX-REDERIV2 (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-rederiv2.md` (amendments applied: the
key is `key_full.tsv` v3, after AX-MERGE3, 04:07 UTC). This is a log entry, not a verifier pass: it records what
changed in the readings since the "Revision log" section above (AX-REDERIV, v2) and the "V8 audit" section above
(V8-NA5797, which classed against v2/early v3) were written, and names what a verifier should re-check. It sets
no N-class and changes none of the classes recorded above.

**Rule-7 re-derivation (this session).** Freshness rule followed: read only `specs/lodewijk-5797.json`,
`key_full.tsv`, `ciphertext_{5797,4610,4611,4616}.tsv`, `decode_{5797,4610,4611,4616}_full.json` and
`tools/decode_key.py` before running anything. `tools/decode_key.py ciphers/lodewijk-van-nassau-1573-74 --config
<decode_N_full.json> --check` reports "reading up to date" for all four (5797, 4610, 4611, 4616), and a fully
independent regeneration into an isolated scratchpad mirror (copies of only the freshness-rule inputs, not the
committed target directory) diffed byte-for-byte identical against every committed reading and token file: **0
differing tokens on all four letters** (73/1545/1393/261 tokens respectively). Rule 7's condition for the
AUDIT-move gate is met with no exceptions: this is the v3 readings (`key_full.tsv` after AX-MERGE3, 04:07 UTC),
not v1/v2.

**Key-source check, code 172 (per this brief's amendment).** `key_full` v3 licenses 172 = le Conte Jean at grade
H from 4614's period decipherment (AX-COMP, AX-MERGE3). I located the occurrence myself first
(`ciphertext_4614.tsv` line `04614_p1_L02_c` pos 17), then fetched the WVO PDF for 04614 once
(resources.huygens.knaw.nl, HTTP 200, descriptive UA; not on disk before this session -- only crops of the cipher
pages existed, none of the companion decipherment leaf) and rendered pp.5-6 (the companion plaintext decipherment
leaf) at 200dpi. Before opening AX-COMP's `decipherment_4614.txt` or `key_4614.tsv`, I read the line myself:
"...est party pour Francfort. on il trouvera mon frere. le Conte Jean lequel est allé pour entendre la
charge..." -- the words directly following "mon frere" and preceding "lequel" are **"le Conte Jean"**, over the
cipher code 172 in the corresponding cipher line. This independently confirms `key_full` v3's H grade for 172.
Crops: `images_wv2/crops_rederiv/04614_decipherment_p5_full.jpg`,
`images_wv2/crops_rederiv/04614_decipherment_p5_L06_zoom.jpg`.

**Counts per letter, v3** (`revisions_for_audit.tsv`, regenerated by AX-MERGE3, 259 rows total; NULL placements:
a `?`/unkeyed position resolved to a silent null; word/name changes: a position now carries a name/title/word
value, or a grade change on an already-valued position):

| letter | NULL placements | word/name changes | total revised | U before (key.tsv) -> after (key_full v3) |
|---|---|---|---|---|
| 4610 | 122 | 14 | 136 | 288 -> 155 |
| 4611 | 88 | 13 | 101 | 227 -> 130 |
| 4616 | 1 | 0 | 1 | 26 -> 25 |
| 5797 (spots file) | 15 | 6 | 21 | 31 -> 11 |

226 NULL + 33 word/name = 259, matching `revisions_for_audit.tsv`'s row count exactly (checked directly against
the file). This is +10 word/name rows and +0 NULL rows since the "Revision log" section above (v2: 249 rows, 23
word/name, 226 NULL) -- the NULL count is unchanged because AX-MERGE3 added no new NULL placement, only regraded
20 already-NULL positions (code 129) from C to M (still counted in the same 226).

**What changed since v2, individually** (`axmerge3/diff_v2_v3.tsv`, 30 tokens; the two that changed *value*,
listed individually as the brief asks, plus the 28 that changed grade only, summarized below the table):

| letter | line | pos | code | v2 | v3 | kind | source |
|---|---|---|---|---|---|---|---|
| 4611 | p1_L03 | 1 | 172 | ? U | lecontejean H | value | 4614 (WVO PDF pp.5-6) contemporary decipherment on the companion leaf: "mon frere le Conte Jean lequel" over "mon frere [172] lequel" (1 of 1, AX-COMP `key_4614.tsv`; independently re-read this session, key-source check above) |
| 5797 | p6_spot4 | 1 | 172 | ? U | lecontejean M | value | same source; M is this position's own sign-transcription-confidence grade (`decode_key.py`'s single-pass downgrade), not a different source from the H row above |

28 grade-only changes (no letter value moves): code 129 (NULL, class-b null since AX-NAMES2) C -> M x20, across
4610 (p1_L05, p1_L21, p2_L02, p2_L07, p2_L19, p3_L06, p3_L10, p3_L15 -- 8 occurrences), 4611 (p1_L03, p1_L10,
p1_L14, p1_L16, p1_L18, p1_L22, p1_L29, p1_L31, p2_L01, p2_L06, p2_L08 -- 11 occurrences) and 5797 (p8_spot7 -- 1
occurrence); and code 95 (kf value 'g', conflict code) I -> M x8, across 4610 (p1_L31, p2_L17, p3_L08), 4611
(p1_L26, p1_L31, p2_L08, p2_L16) and 5797 (p6_spot4 pos5). Both downgrades come from AX-MERGE3's conflict-test
gate (`axmerge3/conflict_test.tsv`): 129 and 95 are two of the four codes the gate could not settle to a single
value (4614's period decipherment disagrees with `key_full`'s value at these codes), so every occurrence is
downgraded to M rather than left at the higher grade a single-source table would otherwise carry. No word or
name value changed at any of these 28 positions; the same value `key_full` v2 already gave them is kept.

**Orchestrator's decision on the 123/129 context-rule flag (AX-MERGE3 flagged this for the orchestrator; recorded
here verbatim per this brief's amendment): no context rule adopted; 123 (l) and 129 (NULL) stay dual readings
graded M in v3 until a letter with a period decipherment settles them in context.** (107 and 95 are the other two
dual-reading codes from the same gate; they are not part of this context-rule question, which AX-MERGE3 raised
specifically for 123/129.)

**5797 spots, v3 (supersedes the "Spots with a value" lines in the sections above): 3 of 6 spots now carry a
value** (p5_spot3 "...und [161 Landgraf, H] ist willens..."; p6_spot4 "**[le Conte Jean, M]** zeuget diesen
morgen..." -- new in v3, a value from a different correspondent's own letter (4614, Lodewijk alone) applied to
this jointly-signed letter (5797, Jan and Lodewijk), so read as a candidate consistent with the surrounding
German, not as confirmed by 5797's own context, per AX-COMP's own caveat; p7_spot2 "[153 Pfaltzgraf, H] helt sich
wol..."). The V8 audit section above lists p6_spot4 among "the other four blanks... not read (codes 172, 173,
182, 156 have no key_full row...)" -- that was true when V8-NA5797 wrote it (before AX-MERGE3 completed at 04:07
UTC); it is superseded by this section for 172 specifically. p5_spot5, p7_spot6 and p8_spot7 remain unread (173,
182, 156 still have no `key_full` row).

**For the verifier.** The N-classes above (4610, 4611, 4616 at N4 confirmed; 4612 at N3; 5797's p5/p7 blanks at
N4, V8 audit section) were assigned against the v2 (or, for 4610/4611/4616, effectively v1/v2) reading. This v3
revision adds one new name value (172 = le Conte Jean, at 4611 and at the previously-unread 5797 p6_spot4) and
eight grade downgrades on an already-established letter (95) plus twenty grade downgrades on an already-NULL
code (129); it adds no new plaintext content beyond that one name and does not change the letter content of any
already-classed passage. A verifier should confirm the classes still hold given 172's addition -- in particular,
whether "[le Conte Jean] zeuget diesen morgen ... der hofnung" (5797 p6_spot4, now partly read) needs its own
phrase search, the way V8.3 ran one for the earlier name fills -- before this folder's classes are treated as
current against `key_full` v3. Not done here: no new phrase search, novelty was not reclassified, per this
worker's brief and scope.

SO-LODEWIJK-1573-74 (`SECOND-OPINIONS-QUEUE.tsv`): a note for v3 was appended to that row's last column, alongside
the existing v2 note.

## V8 second audit (A2): WVO 5797 (26 Sept 2026)

Second adversarial verifier V8-NA5797-2 for LANE V8 (session_01YRuw3TCf7d1w85DLmYNnw4), 26 Sept 2026, 04:30-04:40 UTC
(`date -u` read). Separate session from the solver lane (AX) and from the first verifier (V8-NA5797, section above).
Brief: break V8.1's N4 on the two 5797 blanks (CLAUDE.md Outreach gate 2, rule 10). Nothing decoded, aligned or changed
in any key, ciphertext, decode or reading file.

### A2.1 Verdict

| item | V8.1 class | A2 class | why |
|---|---|---|---|
| 5797 p7_spot2, code 153 "[Pfaltzgraf] ... helt sich wol und thut in warheit viel" | N4 | **N4 held** | no print, quotation, paraphrase that fills the blank, or contemporary decipherment of 5797 located in the new families (A2.3); every scholar who uses CDXLIV quotes Groen's clear text only |
| 5797 p5_spot3, code 161 "Bey dem Herzog von Sachsen und [Landgraf] ... ist willens" | N4 (one word of a four-code blank) | **N4 held**, same limit | as above |
| 5797 p6_spot4, code 172 "le Conte Jean" (key_full v3, AX-MERGE3 04:07) | not classed | **not classed** | "p6_spot4 held: no v3 re-derivation on file at 04:39 UTC 26 Sept 2026" -- when this step ran, ROOM.md carried AX-REDERIV's rule-7 pass (03:22) on the pre-v3 key only. AX-REDERIV2's v3 re-derivation (ROOM 04:41, 0 differing tokens; section "Revision log v3" above) landed two minutes later, so p6_spot4 is now ready for a verifier; this pass did not audit it |
| 5797, the letter | N0 | N0 (`text: known`) | Groen IV CDXLIV pp.217-226 (1837) |

Key source: `period` for the two name values (the 5550 interlinear gloss), `ours` for the letter table that locates the
blanks -- unchanged from V8.1. Confidence: **moderate** (up from V8.5's "lower for scholarship" on the German
Palatine/Hessian side, which this pass covered; still not covered: Schmidt 1989 inside the book, JSTOR, CORE).

**One correction, p7 (A2.4):** V8.1 describes the p7 blank as "[Pfaltzgraf] helt sich wol"; the blank Groen leaves is
three codes, `153.146.137` -- 153 Pfaltzgraf H, **146 unread (U)**, 137 NULL C. So the p7 blank, like the p5 blank, is
read **in part** (one name of a three-code blank). V8.6's safe sentence already says "two of the blanks read in part"
and stays correct; the V8.1 table row and NOTES.md's "gap filled? yes" rows are annotated.

### A2.2 What was attacked

1. **Did anyone fill the blanks by conjecture or from another copy?** The strongest route to N1/N2 is a historian who
   quotes CDXLIV and supplies the missing subject, or a clear copy of 5797 (or of a parallel Nassau letter to Heidelberg
   or Kassel) in the Palatine or Hessian papers. Searched the three editions that print those papers and the two
   general histories that quote CDXLIV (A2.3). Result: **Kluckhohn** (Briefe Friedrichs des Frommen II, 1872, p.580
   n.1) cites "Groen van Prinsterer IV, 217 ff." only for Dathenus and says that in autumn 1573 Dathenus took a mission
   of the Nassau brothers to Orange ("ibid. 220 ff."); **Bezold** (Briefe des Pfalzgrafen Johann Casimir I, 1882, in
   the 1573 introduction, n.1) cites "Johann, Ludwig und Heinrich von Nassau an Oranien, Dillenburg 22. Okt." at
   Prinsterer I.4 p.224, paraphrases only the clear Graveneinigung sentence, and adds that the brothers' letter to
   Orange of 21 Nov (Supplement p.140* ff.) is "nicht dechiffrirt" -- a period scholar recording, in 1882, that these
   cipher passages had not been read; **Janssen** (Geschichte des deutschen Volkes IV, 1893 ed., "Säcularisationspläne
   1573", n.2 "Groen van Prinsterer 4, 224"; French translation L'Allemagne ... 1555-1580, 1895) quotes the same clear
   sentence ("nicht nur etliche Grafen, sondern auch Kurfürsten ...") and nothing from a blank. None prints a word in
   either blank.
2. **Does secondary literature state the p7 content anyway?** Blok, Lodewijk van Nassau (1889), on late 1573: "De
   keurvorst van de Paltz steunde met alle kracht en trachtte ook dien van Saksen te bewegen" -- the Elector Palatine's
   support is general history (Kluckhohn II nos.684-697 print his letters urging Saxony and Hesse to help Orange), not
   a reading of the blank and not cited to CDXLIV. This does not lower the class (rule 10 classes the plaintext and the
   decipherment of this item), but it bounds the claim: **the p7 value adds no historical fact that was not already
   known**; a safe sentence must not present it as news about the Palatine's policy.
3. **Did the Groen series itself later fill a blank?** Grep of all 38 cached Groen IA texts for CDXLIV and for
   back-references "T. IV, p. 21x-22x": Groen V (1838) refers back to IV p.219 twice, both for Dathenus, and to p.226
   for Bossu; the 2e serie hits for "MCDXLIV" are a different letter (York to Orange, 1681). No errata, supplement or
   later note fills a 5797 blank. Groen's own Tables des matieres (1847, Google Books full view) was queried by snippet
   only (A2.3).
4. **A method gap in the first audit (not a finding against the class).** print_check's listed-source search on the
   Groen IV copy V8 relies on (`archivesoucorre03housgoog`) returns **no hit for the positive-control phrase** "helt
   sich wol und thut in warheit viel", in V8's run and in this one: that copy's OCR reads "heit sicb wol mid thut in
   warheit TÎel" (cached text line 12997), which defeats both the exact and the proximity match. The control succeeds
   only through ia-global (the two `pringoog` copies) and Google Books (8 Groen copies). So a per-source "no hits" on
   an OCR-damaged Groen copy is not a test; V8's conclusion stands because V8 also read CDXLIV by hand (dbnl text,
   `groen/groen_IV_CDXLIV.txt`) and because the variant phrases were also run on ia-global and Google Books. The
   Fraktur texts of Kluckhohn, Heppe and Rommel are worse (OCR renders "Groen" as "©roen"), so for those the phrase
   search is recorded but the result rests on the manual grep of dates, "Prinsterer IV, 2xx" citations and context.

### A2.3 Search log (families new to this pass)

| family | status | method | result |
|---|---|---|---|
| Kluckhohn, Briefe Friedrich des Frommen II (1572-76), IA `bub_gb_3N1SAAAAcAAJ`; also `briefefriedrichd00frie`, `bub_gb_3U8VAAAAYAAJ` (vol I/both) | searched | djvu text, manual grep (Oct-Nov 1573 register nos.686-699, "Prinsterer IV, 2xx", Chiffre/Ziffer) + print_check phrases | cites Groen IV 217 ff. / 220 ff. (Dathenus), no quotation of a blank; Chiffre 0 in vol II body |
| Bezold, Briefe des Pfalzgrafen Johann Casimir I (1882), IA `briefedespfalzgr01joha` | searched | same | cites 5797 (Prinsterer I.4 p.224) for the clear Graveneinigung sentence; notes the 21 Nov letter "nicht dechiffrirt"; notes the Palatine archive keeps cipher keys (Ma. 544/15) but few cipher letters |
| Janssen, Geschichte des deutschen Volkes IV (1893), IA `deutschenvolkesseit04jans`; French tr. 1895 (Google Books `bydeij0MPSoC`) | searched | grep + Google Books snippet | quotes Groen 4, 224 clear text only |
| Heppe, Geschichte des deutschen Protestantismus II (1853), IA `bub_gb_IilBAAAAcAAJ` | searched | grep | church history, no Nassau letter of Oct 1573 |
| Rommel, Geschichte von Hessen V (1835), IA `bub_gb_c4AAAAAAcAAJ` | searched | grep | no 1573 Nassau/Orange correspondence |
| Blok, Lodewijk van Nassau (1889), IA `lodewijkvannass00blokgoog` | searched | grep (Paltz, landgraaf, cijfer, 22 oct) | general statement on Palatine support, no blank filled (A2.2 item 2) |
| Groen, all cached copies (38) for later fills/errata | searched | grep CDXLIV, "T. IV, p. 21x-22x" | back-references to Dathenus/Bossu only |
| Groen, Tables des matieres (1847) | snippet only | Google Books `xI9lDKGU5b4C` | index entry "Graveneinigung ... 1573, IV. 46"; PALATIN entries seen are for Frederick V; no page read |
| Schmidt, Der Wetterauer Grafenverein (1989) | **unreachable inside the book** | Google Books `zxxoAAAAMAAJ` (NO_PAGES; one keyword snippet: Dillenburg as a hub of French diplomacy); CrossRef lists two reviews (BMGN 1995, ZRG GA 1991) | book text not searchable from the cloud; JSTOR row queued |
| Wilhelm IV of Hessen-Kassel correspondence editions | not located | IA advancedsearch (Landgraf Wilhelm Briefe/Correspondenz 1850-1930): 0 | no printed edition of his 1573 political correspondence found on IA |
| Google Books | searched | keyed, country=US, 16 calls + 10 in print_check (A2 variants: Pfalzgraue/Pfaltzgrave/Churpfaltz/Pfaltzgraff helt sich wol, Landtgraue/Landgraue/Landgrave ist willens; "22. Oktober 1573" Nassau; "22 octobre 1573" Nassau Orange; Graveneinigung 1573; Grafenverein topical) | name-variant phrases 0; all CDXLIV quotations are of clear text (Groen copies, Janssen, Juste 1865, Sutherland 1961 citing pp.219-226) |
| Internet Archive full text (ia-global) | searched | print_check, 10 phrases | control phrase finds the two Groen `pringoog` copies; name variants 0 (the one hit set, "Herzog von Sachsen und Landgraf", is numismatics/church-administration, not 1573) |
| OpenAlex | searched | keyed (Bearer), 12 calls incl. "Wetterauer Grafenverein Nassau 1573", "Johann Casimir Kassel 1573 Oranien" | Past & Present 2021 (dynastic scenario thinking), a 2013 Calvinism volume -- neither concerns the letter |
| CrossRef | searched (after one retry) | 429 inside print_check; one retry after a pause answered | Schmidt 1989 reviews; Nassau genealogy chapters; nothing on the letter |
| Semantic Scholar | searched (after one retry) | 429 x2 inside print_check; two retries after a pause answered 200 | 0 results ("Nassau 1573 Graveneinigung Wetterau Pfalz Hessen", "Ludwig Nassau 1573 cipher") |
| HAL | searched | api.archives-ouvertes.fr, Nassau+1573+chiffre / Grafenverein / Dillenburg+1573 | 0 |
| Persée | searched | persee.fr search "Nassau 1573 Dillenburg" | 3,774 generic results; first page reviews (Juliana van Stolberg; Kluiver 1578-84) -- nothing on 5797 |
| CORE | not searched | CORE_API_KEY unset (key probe at session start) | -- |
| JSTOR | queued | 2 rows appended to `JSTOR-QUEUE.tsv` (Schmidt 1989 reviews / Grafenverein + Chiffre; Dathenus mission Oct 1573) | V8's 2 rows also still open |
| Marburg (HStAM) / Dresden (HStA) files for a clear copy | not searched | Arcinsys/HStA catalogues not tried (no route in the host table); Bezold says the Hessian material is richer at Marburg | a clear copy there is the one route to N1/N2 this pass could not close |

Files: `print-check-a2.tsv`, `print-check-a2-hosts.tsv` (V8's `print-check.tsv` untouched). IA caches kept in the
scratchpad, not committed.

### A2.4 Brief items 3 and 4

- **172 / p6_spot4:** held, not classed (A2.1).
- **123/129 dual-M (AX-MERGE3):** neither code sits inside or beside a classed spot. 123 is in p5_spot5
  (`131.123.173`, before "ist gestern zue ghen gezogen") and 129 in p8_spot7 (`156.127.135.144.129`, before "begert
  meiner"); the classed spots are p5_spot3 (`... 161.126.136.146`) and p7_spot2 (`153.146.137`). Neither classed
  reading changes under either value of 123 or 129. The context rule itself is the solver lane's decision.

### A2.5 Safe and unsafe sentences

- **Safe (unchanged from V8.6, which stays correct):** "In WVO 5797 (Jan and Lodewijk van Nassau to Orange, 22 Oct
  1573), printed by Groen van Prinsterer in 1837 with several passages left undeciphered, two of the blanks read in
  part, 'the Palsgrave (Pfaltzgraf) holds well' and '... and the Landgrave ...', by locating them with a letter table
  recovered by our own cryptanalysis and valuing the two name codes from a contemporary interlinear gloss on the
  sibling letter WVO 5550; no prior decipherment of these blanks located (N4); the letter's other text is Groen's."
- **Unsafe:** anything in V8.6's list, plus "the p7 blank is read" (146 is unread in it), "this shows the Palatine
  supported the Nassau league" as news (known since Kluckhohn 1872), or "le Conte Jean" in 5797 as a reading (p6_spot4
  is not classed).

### A2.6 Gate 2

**second adversarial audit done: yes** (N4 not broken for p7_spot2 and p5_spot3; p6_spot4 not classed), **open-index
pass done** (OpenAlex, Semantic Scholar and CrossRef each answered, HAL, Persée; CORE not available), **Google Books
done**, **JSTOR rows 88, 89 (V8) and 90, 91 (A2) open** -- per the verifier template a queued JSTOR row does not block N4,
but CLAUDE.md Outreach gate 2 requires them answered or waived by the owner before any post.

### A2.7 Postmortem and corrections

The first audit's N4 holds. Two things it got less than right: the p7 blank was described as if fully read (146 is
unread; annotated in NOTES.md), and its listed-source positive control silently failed on the Groen IV copy it named
(OCR), masked by V8's manual reading. NOTES.md line "reads correctly at 5797 p7_spot2 against Groen's clear frame"
over-states: Groen's frame is blank there, so the frame only shows that a subject fits, it cannot check the value
(annotated). No sentence in the folder calls 5797 new, first or unpublished. The safe sentence does not change, so
second-opinions/PROMPT-chatgpt.md is not edited; the SO-LODEWIJK-1573-74 row gets a one-clause dated note.

Requests (this session): archive.org 31 (advancedsearch 15, metadata 8, djvu 8; one at a
>= 1.6 s apart); be-api.us.archive.org 10; www.googleapis.com 16 (+10 inside print_check); api.openalex.org 12;
api.crossref.org 2 (1 x 429, 1 answered); api.semanticscholar.org 4 (2 x 429, 2 answered); api.archives-ouvertes.fr 1;
www.persee.fr 1. No subagents.

## V8 audit: 5797 p6_spot4 (172) (26 Sept 2026)

Verifier V8-NA172 for LANE V8 (session_01YRuw3TCf7d1w85DLmYNnw4), 26 Sept 2026, 05:10-05:25 UTC (`date -u` read). Separate
session from the solver lane (AX-COMP, AX-MERGE3, AX-REDERIV2) and from both earlier verifiers of this letter (V8-NA5797,
V8-NA5797-2). Nothing decoded, aligned or changed in any key, ciphertext, decode or reading file.

Claim under audit: key_full v3 (AX-MERGE3, 04:07 UTC) gives 172 = le Conte Jean from the contemporary decipherment of the
sibling letter WVO 4614; with it 5797 p6_spot4 reads "[le Conte Jean] zeuget diesen morgen ... der hofnung".

### V8C.1 Verdict

| item | what is read | prior plaintext | prior decipherment | class | key |
|---|---|---|---|---|---|
| 5797 p6_spot4, code 172 | "[172 = le Conte Jean, i.e. Count Johann (Jan) of Nassau] zeuget diesen morgen Kölln der hofnung die sachen ... dahien zu handlen das er [the Elector of Cologne] sich ... vom Herzog von Alba absondern ..." | **no** for the name: Groen IV CDXLIV p.225 (dbnl text `groen/groen_IV_CDXLIV.txt` line 252) prints "soll. zeuget diesen morgen Kölln der hofnung", the subject left blank; not found in any source below | none located | **N4** (no prior decipherment located) | `period` (172 from the 4614 companion decipherment leaf); the table that locates the spot `ours` |

Confidence: **moderate**, the same as A2 for the other two spots (Schmidt 1989 inside the book, Lossen, Der Kölnische
Krieg I (1882) inside the book, CORE, and the Wiesbaden file STAW 171 C 368 not reached). `text: known` for the letter
(N0), as before.

Scope of the spot, stated exactly: Groen's blank at p6 is **one code wide**. The cipher at the spot is
`172 | 58.85.38.95.82.35 (zeuget) | diesen morgen | 100.155 | der hofnung`; Groen prints every word of it except 172,
including "Kölln" over 100.155 (our table reads 100 = h, I, and 155 unread, so our table does not reproduce Groen's
"Kölln"; the word is Groen's, not ours). So 172 fills Groen's p6 blank in full -- unlike p5 and p7, where the blank is
read in part -- but the *spot* in our reading is still read in part (155 unread, 95 dual-M). Safe wording: "the blank's
one code valued", not "the passage deciphered".

### V8C.2 Rule 4: is H right for 172?

- **Value.** I read the 4614 companion decipherment crop myself (`images_wv2/crops_rederiv/04614_decipherment_p5_L06_zoom.jpg`):
  "est party pour francfort. ou il trouvera mon frere. le Conte Jean lequel est allé pour entendre la charge du sieur
  ...". And the cipher line (`images_wv2/crops_comp/04614_p1_L02.jpg`, third row): "... 84.24.82 **172** .111.81.16 ..."
  -- the sign reads 172 cleanly to my eye; the transcription's M/"agree-flagged" on that sign is conservative, not a
  doubt I can see. One clean period decipherment over a legible sign is a key source; V8.2 set the same precedent
  for 153 (one clean gloss suffices). **H for 172 in key_full stands.**
- **The token in 5797 is M, not H.** The 5797 sign at p6_spot4 pos 1 is single-pass (decode_key.py's downgrade), so
  the reading carries **M** (as `reading_5797_full_tokens.tsv` already records). Any quotation says "[le Conte Jean]"
  with that grade, not "read at H".
- **Cross-correspondent transfer.** 4614 is Lodewijk's French letter; 5797 is a German letter of Jan and Lodewijk
  jointly (a *minuut*). The p5/p7 values also come from a sibling (5550), so this is the lane's standing method, and the
  nomenclator family is the same table. Consistency, not proof: (a) grammar -- "zeuget" (= zeucht, zieht) is third
  person singular, so the blank's subject is one person, which a name fits; (b) sense -- the rest of the sentence
  (Groen's clear text) is about winning the Elector of Cologne (Salentin von Isenburg) to leave Alba, marry, keep the
  electorate and change religion (Groen's own n.(1): "L'Electeur de Cologne ... n'accomplit pas les autres parties de ce
  triple projet"); (c) history -- Glawischnig 1973 (IA fts inside `niederlandekalvi0000glaw`, 2 queries) records "das
  Gespräch JvN mit Salentin im Oktober 1573" and a letter "JvN an LvN über das Gespräch JvN mit Salentin im Oktober
  1573" (STAW 171 C 368), and Bezold 1882 (IA `briefedespfalzgr01joha`, p.130, djvu text read) says "Die Verhandlungen
  mit dem sehr ungeistlichen Kölner, Salentin von Isenburg, führten im Winter 1573 Johann von Nassau und Ehem". So
  Count Johann setting out for Cologne on or about 22 Oct 1573 is what the independent literature leads one to expect.
  One oddity, not a contradiction: a letter signed by Jan and Lodewijk naming Jan in the third person. A *minuut*
  drafted by Lodewijk's side on the morning of Jan's departure fits it; Glawischnig's "JvN an LvN" letter about the
  talk shows the two were apart soon after.
- **"le Conte Jean" is French in a German letter.** The table value is a person code, not a phrase: the 4614
  decipherer wrote it in his letter's language. A German reader of 5797 would render it "Graf Johann" (period
  spellings Graff Johan, Graue Johan), possibly "mein bruder Graf Johann". That does change the phrase search: a
  print of the passage would carry the German form, so V8C.3 searched the German renderings as well as the French.

### V8C.3 Search log (new for this spot only)

The families V8.4 and A2.3 logged (Groen both series and later fills, Gachard, Blok 1887/1889, Glawischnig, Kluckhohn,
Bezold, Janssen, Heppe, Rommel, Rachfahl, WVO, Tomokiyo, solver repositories, Google Books, IA, OpenAlex, CrossRef,
Semantic Scholar, HAL, Persée) are not repeated wholesale. JSTOR rows 88-91 were answered in the local runner's
`jstor-runs/2026-09-26-0455.tsv` (branch `jstor-run/2026-09-26-0455`, PR 17), read here: rows 88 and 91 "no relevant hit",
rows 89 and 90 context only (Schindling 1994, Rohls 2007), none about the letter.

| family | status | method | result |
|---|---|---|---|
| Positive control, Groen's clear words at p6 ("zeuget diesen morgen Kölln der hofnung") | searched | `tools/print_check.py`, `print-check-v8c.tsv` | **found**: exact in Groen IV `archivesoucorre11pringoog` (djvu text) and ia-global 1 item (`dutch_nederlandse_boeken_archive`); not in `archivesoucorre03pringoog` (OCR) nor via Google Books -- the method finds this letter's print when it exists |
| p6 with the name, 7 phrases: "Graf Johann / Graff Johan / Graue Johan zeuget diesen morgen", "Grave Johann zeucht diesen morgen", "Conte Jean zeuget diesen morgen", "mein bruder zeuget diesen morgen Kölln", "Graf Johann zeucht gen Köln" | searched | same run: 2 Groen IV copies, ia-global, Google Books (keyed, country=US), OpenAlex (keyed), CrossRef | **0 hits** in IA, Google Books and OpenAlex; CrossRef returns only relevance noise (dictionary entries "Graf, Johann", unrelated titles) |
| Groen IV CDXLIV's own note at p6 | read | dbnl text, n.(1) [#499] | the note glosses the Cologne plan only; it does not name who went to Cologne and does not fill the blank |
| What Count Johann did "this morning" about 22 Oct 1573 | searched | Glawischnig (IA fts, 2 queries); Bezold I (djvu text, 1 fetch, scratchpad); Google Books 2 queries (Lossen; Salentin + "Johann von Nassau" 1573 Köln) | Jan's talks with Salentin in Oct/winter 1573 are recorded (V8C.2); **no source quotes 5797 at p6 or names the subject of "zeuget"**; Bezold cites Prinsterer I.4, 339 and 342-4 (later letters), not 224-5 |
| Lossen, Der Kölnische Krieg I (1882) | **snippet only** | Google Books `iRNlEQAAQBAJ` (2025 reprint, PARTIAL): Salentin "erbot, durch Johann von Nassau zu erkunden ..." | not on IA by creator search; the book's account of Oct 1573 not read inside. The one principal Salentin study this pass could not open; a person with the volume can check whether Lossen quotes CDXLIV p.225 and supplies the subject |
| Kramer, Der Kölner Kurfürst Salentin von Isenburg (1937), Google Books `e24-AAAAMAAJ` | not reached | NO_PAGES | -- |
| JSTOR | queued | 1 row appended (Salentin + Johann von Nassau + 1573 + Köln) | never blocks a class on its own |
| CORE | not searched | CORE_API_KEY unset (key probe at session start) | -- |

### V8C.4 Safe and unsafe sentences

- **Safe (p6, add to V8.6):** "In the same letter, the one-code blank Groen leaves before 'zeuget diesen morgen Kölln'
  ('... goes this morning to Cologne') is valued as a name code, 'le Conte Jean' (Count Johann of Nassau), from the
  contemporary decipherment of the sibling letter WVO 4614, the blank located with our own letter table; the sign in
  5797 is read at a single pass (grade M); no prior decipherment of this blank located (N4). That Count Johann
  negotiated with the Elector of Cologne in October 1573 is already known (Bezold 1882; Glawischnig 1973)."
- **Unsafe:** "first decipherment", "newly revealed that Count Johann went to Cologne" (the fact is in print), "the p6
  passage is deciphered" (155 unread, "Kölln" is Groen's word), "read at grade H" for the 5797 token (it is M), or
  any sentence that presents 172 as our value (it is the 4614 decipherer's).

### V8C.5 Gate 2 for this spot

The orchestrator decides; my argument is that **A2 does not cover this spot and a separate second audit is still
needed, but a short one**. For: every family the p6 phrase touches through the letter itself (Groen all series and later
fills, Gachard, Blok, Kluckhohn, Bezold, Janssen, IA, Google Books, open indexes, JSTOR rows 88-91) was searched by V8
and A2 for the same letter, and a print of the p6 blank would sit in the same editions as the p5/p7 blanks, which they
found blank. Against: the name opens a family neither audit targeted -- the Cologne literature (Lossen 1882-97, Kramer
1937, the Salentin/Kurköln studies, the Wiesbaden file STAW 171 C 368 on Jan's talks) -- where a historian following
Jan's October 1573 journey could quote CDXLIV p.225 and supply the subject by conjecture (an N1/N2 risk), and this pass
reached Lossen and Kramer only by snippet. A second audit scoped to that family (Lossen I inside the book, Kramer, the
Kurköln literature, one JSTOR row) would close it.

### V8C.6 Postmortem and corrections

No sentence in the folder calls p6 new, first or unpublished. Corrections: A2.5's unsafe item "'le Conte Jean' in 5797 as
a reading (p6_spot4 is not classed)" is superseded by V8C.1 (classed N4, token M). NOTES.md's AX-MERGE3 table row ("yes,
new in v3") is annotated: "new" there means new relative to key_full v2, not a novelty claim. The safe sentence
changes (a third spot), so a dated note with V8C.4's sentence was added to `second-opinions/PROMPT-chatgpt.md` and the
SO-LODEWIJK-1573-74 row.

Requests (this session): archive.org 4 (print_check 2, advancedsearch 1, Bezold djvu 1); be-api.us.archive.org 20
(print_check 16, Glawischnig fts 4); www.googleapis.com 10 (print_check 8, by hand 2); api.openalex.org 8;
api.crossref.org 8. No subagents. Files: `phrases.txt` (V8C block), `print-check-v8c.tsv`, `print-check-v8c-hosts.tsv`;
IA caches in the scratchpad, not committed.

## V8 second audit (A3): 5797 p6_spot4 (26 Sept 2026)

Verifier V8-NA172-2 for LANE V8 (session_01YRuw3TCf7d1w85DLmYNnw4), 26 Sept 2026, 05:45-05:55 UTC (`date -u` read).
Separate session from the solver lane (AX) and from V8-NA5797, V8-NA5797-2 and V8-NA172. Scope: V8C.5, the Cologne
literature. Nothing decoded; no key, ciphertext, decode or reading file touched.

### A3.1 Verdict: N4 lowered to **N2**

| item | prior plaintext | prior decipherment | class | key |
|---|---|---|---|---|
| 5797 p6_spot4, code 172 "[le Conte Jean] zeuget diesen morgen Kölln" | **yes, in substance**: Lossen, *Der Kölnische Krieg* I (Gotha 1882), p.212: "Graf Johann aber brach in aller Stille am 22. Oktober nach Arnsberg auf zum Kölner Kurfürsten" -- the same day as 5797 ("Datum Dillenbergk, am 22sten Octobris Ao 1573", Groen IV CDXLIV) and the same person and errand that the blank plus Groen's clear words give | none located: Lossen does not quote or cite CDXLIV (no "IV, 217-226" citation anywhere in the volume; his Groen citations for 1573 are IV 63*, 127*, 294, 342, 350 and Suppl. 140*), does not fill the blank, and says of the one cipher letter he cites (Jan to Orange, 21 Nov 1573, Suppl. p.140*) "ist leider nicht entziffert" | **N2** (plaintext content known elsewhere; no prior mapping of this ciphertext to it found) | `period` (4614 decipherment), table `ours` -- unchanged |

Why lowered: rule 10's N3/N4 need "no prior plaintext located". The blank carries one fact -- who set out from Dillenburg
towards the Elector of Cologne on the morning of 22 Oct 1573 -- and Lossen printed that fact, day and all, in 1882, from
the Dillenburg papers (his p.214 n.2 cites Dill. A. C. 368 fol. 25, Jan's own draft relation of the talks, and fol. 32,
Jan's report of 1 Nov 1573, the file V8C.2 knew as STAW 171 C 368). V8C.2 had the October talks from Bezold and
Glawischnig only in general ("im Oktober", "im Winter"); Lossen's exact day turns "consistent with the literature" into
"the literature already says it". Our result is the mapping: a period key value (172) placed into Groen's one-code blank.
That is an independent confirmation of Lossen from the cipher side, not new information. V8C's `text: known` for the
letter stands; the spot is now `text: known` in substance too.

Not a break of the reading. Lossen corroborates 172 = Count Johann (day, direction, subject in the singular), so the
H grade of 172 in key_full and the M grade of the 5797 token are unaffected. Minor difference, not a conflict: Lossen
says Arnsberg (the Elector's residence), Groen's clear text says "Kölln" (read as "to Cologne", i.e. the Elector).

Correction to V8C.3: Lossen I **is** on the Internet Archive (four copies: `bub_gb_QnURAAAAYAAJ`, `derklnischekrie01lossgoog`,
`derklnischekrie00lossgoog`, `bub_gb_bW0IAAAAQAAJ`, found by `title:(kölnische krieg)`; V8C searched by creator only).
The "Kramer 1937" of V8C and of the brief is **Karl Heinrich Graff**, *Der Kölner Kurfürst Salentin von Isenburg* (1937;
Google Books `e24-AAAAYAAJ` / `K5UQMwEACAAJ`, NO_PAGES; reviewed 1939 per CrossRef).

### A3.2 Search log (Cologne family)

| family | status | method | result |
|---|---|---|---|
| Lossen, Der Kölnische Krieg I (1882) | **searched inside** | IA djvu text of two copies (`bub_gb_QnURAAAAYAAJ` Fraktur OCR, `derklnischekrie01lossgoog` clean OCR), grep Groen/Prinsterer, Arnsberg, Oktober, zeuget/zeucht, diesen morgen, entziffert/chiffr, IV 21x/22x; pp.211-215 read | **p.212, 22 Oct departure of Graf Johann to the Elector** (A3.1); no quotation of 5797, no CDXLIV citation, no filled blank; "entziffert" 1 hit (Suppl. 140*, a different letter, "nicht entziffert") |
| Lossen's other Salentin work (vol. II 1897; Masius letters 1886, `bub_gb_xj0OAAAAQAAJ`) | not read | vol. II covers 1582-86; Masius letters end with Masius's death (April 1573) | out of the October 1573 window by date; not opened |
| Graff 1937 (Salentin monograph) | unreachable | Google Books keyed, country=US: NO_PAGES both records; IA creator search 0 | JSTOR row appended |
| Kurköln/Salentin literature, open indexes | searched | OpenAlex keyed ("Salentin Isenburg Nassau 1573", 3 results: Neuss archive inventory 1897, Reichshofrat Antiqua 8, an inventory 2022); CrossRef (8 rows: Graff reviews 1939, Visitationsprotokolle 1569, noise) | nothing on Jan's 22 Oct journey or 5797 |
| Semantic Scholar, HAL, Persée, CORE | not searched this pass | time box; V8/A2/V8C covered them for the letter; CORE_API_KEY unset | -- |
| Phrase control and name phrase, Google Books | searched | `"zeuget diesen morgen"` (7 hits: 6 copies of Groen IV + one 1763 hymnal, unrelated); Salentin + "Graf Johann" + 1573 + Arnsberg (0) | only Groen prints the passage, blank as ever |
| HHStAW Abt. 171 C 368 (Arcinsys Hessen) | unreachable by plain URL | `arcinsys.hessen.de` detail URL answers 302 (session/JS app); not pursued further | Lossen's footnote gives the file's content (Jan's draft relation, fol. 25; report of 1 Nov 1573, fol. 32) |
| JSTOR | queued | 1 row appended (Graff/Salentin + Arnsberg + Oktober 1573) | never blocks a class on its own; the earlier V8C row is still queued |

### A3.3 Safe and unsafe sentences (replace V8C.4)

- **Safe:** "In the same letter (Dillenburg, 22 Oct 1573), the one-code blank Groen leaves before 'zeuget diesen morgen
  Kölln' is valued as the name code 'le Conte Jean' (Count Johann of Nassau), from the contemporary decipherment of the
  sibling letter WVO 4614, placed with our own letter table; the 5797 sign is read at a single pass (grade M). The fact
  it supplies is already in print: Lossen, Der Kölnische Krieg I (1882), p.212, has Count Johann leave quietly on
  22 October 1573 for the Elector of Cologne at Arnsberg. The cipher confirms Lossen; no prior decipherment of this blank
  located (N2)."
- **Unsafe:** anything in V8C.4's unsafe list, and in addition "no prior plaintext", "N4", "reveals who went to Cologne",
  or any wording that presents the identity or date of the journey as information the cipher adds.

### A3.4 Gate 2

Second adversarial audit done for p6_spot4: **yes** (class lowered N4 -> N2). JSTOR rows open: the V8C row (Salentin +
Johann von Nassau + 1573 + Köln) and this pass's row. Gate 2 for an outward post above N1 is met on the search side
subject to those two rows; the post, if any, must use A3.3's sentence and cite Lossen p.212.

### A3.5 Postmortem

Failure: V8C searched Lossen by creator name only, concluded "not on IA", and read him by snippet; the title search found
four full-text copies in one call. The brief's author name for the 1937 monograph (Kramer) was wrong (Graff), which would
have sent a catalogue search astray. Corrections carried: `second-opinions/PROMPT-chatgpt.md` (dated note, A3.3 sentence
replaces V8C.4's), SECOND-OPINIONS-QUEUE.tsv row SO-LODEWIJK-1573-74 (note). V8C.1's N4 and V8C.4's safe sentence are
superseded by A3.1/A3.3.

Requests (this session): archive.org 5 (advancedsearch 3, djvu 2); api.openalex.org 1; api.crossref.org 1;
www.googleapis.com 3; arcinsys.hessen.de 1. No subagents. IA caches in the scratchpad, not committed.
