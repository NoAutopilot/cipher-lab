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
