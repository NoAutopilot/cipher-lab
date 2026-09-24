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
   contents (pp. x-xiii, read through the snippets) lists for 1573-74 only letters with Hesse, Mainz, Saxony,
   Hendrik and Willem van den Berghe, and Orange to his brothers (LXI, 16 Oct 1573; LXII, 10 Oct). There is no
   letter of Lodewijk to Orange of 3 June or 2 July 1573, or of 6 March or 12 April 1574. **Result: none of the four
   is in Blok 1887.** This rests on search-within plus the table of contents, not a page-by-page read.
3. **Blok, Lodewijk van Nassau (1889)**, full djvu text (IA `lodewijkvannass00blokgoog`) grepped. It never
   mentions a cipher, and it quotes none of the four. It led to two families V2 had not listed (items 6 and 7).
4. **Kervyn de Lettenhove, Relations politiques des Pays-Bas et de l'Angleterre t. VI (1571-73) and VII
   (1574-75).** V2 logged these as "IA title search found no item". They are on IA as `relationspolitiq06nethuoft`
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
