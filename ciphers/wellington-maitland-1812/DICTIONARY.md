# Dictionary edition search, Wellington to Maitland, 2 Sept 1812

**Verdict: not found** (search of 19 Sept 2026, about two hours, 57 volumes tested; three near misses recorded below,
none with a constant offset). No reading is claimed here, so there is nothing to grade under CLAUDE.md rule 4; the
result is a negative search with the coverage listed at the end.

Inputs: `codebook.tsv` (57 distinct groups, all with known plaintext, grade H+C), `NOTES.md` "Dictionary
candidates" (first pass, Internet Archive only). Raw output of every test: `dictionary_tests_2026-09-19.txt`.
Scripts: `tools/gbooks_search_within.py` (Google Books search-within-volume, returns printed page numbers) and
`tools/ia_djvu_headwords.py` (Internet Archive per-page OCR, returns scan index and running head).

## 1. Constraints from the codebook

Page constraints (word -> printed page) and within-page constraints (position, column letter):

| word | page | pos | letter | word | page | pos | letter |
|---|---|---|---|---|---|---|---|
| Alphabet | 14 | 12 | z | outside | 297 | 10 | m |
| amount | 16 | 8 | z | period | 308 | 12 | x |
| and | 17 | 10 | n | provisions | 332 | 8 | x |
| another | 19 | 12 | l | Quarters | 336 | 3 | z |
| any | 20 | 9 | x | to rejoin | 346 | 20 | y |
| are | 23 | 9 | n | require | 349 | 20 | m |
| as | 25 | 3 | n | to rest | 350 | 21 | z |
| at | 28 | 3 | y | Sea | 365 | 22 | n |
| be | 38 | 7 | x | sent | 369 | 8 | l |
| can | 66 | 13 | x | South / Southward | 388 | 17 / 23 | y / y |
| Cypher / to Cypher | 79 | 21 / 22 | l / l | Spelling | 389 | 19 | m |
| day | 116 | 15 | x | supplying | 400 | 33 | x |
| early | 146 | 4 | y | that / the / this | 405 | 7 / 15 / 23 | l / l / n |
| enable | 151 | 13 | n | to | 408 | 12 | x |
| Event | 158 | 4 | y | Town | 409 | 7 | m |
| fortunate | 184 | 20 | y | Troops | 412 | 22 | x |
| Head / Height | 203 / 205 | 17 / 6 | n / m | use / to use | 429 | 5 / 6 | b / l |
| how | 211 | 16 | m | Westward | 432 | 29 | y |
| I inclose | 219 | 3 | l | which | 433 | 19 | l |
| it | 232 | 6 | y | will | 434 | 4 | y |
| left | 243 | 8 | b | with | 435 | 5 | m |
| me | 261 | 16 | l | words | 436 | 23 | x |
| more / tomorrow | 272 | 1 / 13 | y / y | you / your | 438 | 8 / 15 | y / y |
| occupy / of / on | 288 / 289 / 290 | 21 / 17 / 11 | y / l / z | | | | |

Cheap discriminators used on every candidate: the page of **morrow** (target 272, first entry of its column is
"more"), of **theft** (adjacent to "the", target 405) and of **younker / youth** (adjacent to "you", target 438),
then **alphabet** (14), **cipher** (79), **occupy** (288), **period** (308), **provision** (332), **quarter**
(336), **sea** (365), **southward** (388), **supply** (400), **westward** (432). A candidate passes only if all
hold; a constant offset over the whole run would mean the same setting with different front matter.

Three things the constraints imply, all inferred (grade I, not readings):

1. **The dictionary spells "Cipher".** With "can" on p. 66 and "day" on p. 116, C must run to about p. 118; a
   "Cypher" (cy-) at p. 79 is impossible, a "Cipher" (ci-) at p. 79 is exactly where it should be. The clerk's
   interlinear "Cypher" is his own spelling.
2. **The tail is compressed.** From "south" (388) to "you" (438) is 50 pages; in every 440-page dictionary tested
   that stretch is 84-94 pages. Relative to the body (cipher -> the, 326 pages) the tail (the -> you, 33 pages) is
   0.10; every candidate is 0.13-0.20. Either the printer squeezed T-Z to finish in a fixed number of sheets, or
   T-Z is set denser, or the vocabulary after S is unusually thin.
3. **Positions are small in the body and larger in the tail.** The 41 groups on pp. 14-389 have positions 1-23
   (max 23); the 16 groups on pp. 400-438 reach 29 and 33. If positions were uniform on 1-50 (a 50-line Entick
   column) the chance of 41 body positions all <= 23 is 1e-14. So a body column holds about 24 entries or lines
   and tail columns more: a small format (about 24 lines per column), or a numbering convention not yet
   understood (for example a count within a half-column). Entick's two 50-line columns do not fit this.

## 2. Sources checked for a named dictionary (all 19 Sept 2026)

- Gurwood, *Dispatches* vol. 9 (IA `dispatchesoffie09welluoft`, full OCR): no dictionary named anywhere. Relevant
  passages: to Popham, Torre Lodones 11 Aug 1812, "I have no cipher in which I could correspond with you", PS
  "the numbers in your signal book would be as good a cipher as we could use; but you must send me a book";
  to Maitland 29 Aug 1812, "I shall answer your letter fully this day in cipher, and you can decipher it when
  you get the cipher, which is now on its passage from England".
- *Supplementary Despatches* vol. 7 (IA `supplementaryde02wellgoog`, full OCR): "cypher" 12 hits, all French
  ciphers or the Foreign Office decypherer; no dictionary.
- Urban, *The Man Who Broke Napoleon's Codes* (IA `manwhobrokenapol0000urba_n2j5`): lending copy; the
  search-inside endpoint answers "Item not available" and the OCR text is not downloadable; not read.
- Web (Wikipedia "George Scovell", "Book cipher"; militaryintelligencemuseum.org; navyhistory.au; forcesnews):
  all describe Scovell's system as page, column letter, entry number in "an English pocket dictionary", none
  names it. Google Books web search and the Books feed API for Scovell + dictionary + Entick/Perry/Johnson: nothing.
- TNA Discovery, WO 37 (Scovell papers) description: intercepted despatches, journal, notes; no dictionary in
  the series description (piece-level descriptions not consulted).

## 3. Access

Google Books: the legacy Atom feed (`books.google.com/books/feeds/volumes?q=`) lists editions with viewability;
the JSON endpoint `books?id=ID&q=WORD&jscmd=SearchWithinVolume2` returns printed page numbers; `output=text`
gives the OCR of a page once a cookie jar is used (used for Entick 1800 p. 438). The Books API v1 gave 429.
Internet Archive: `_djvu.xml` per page. HathiTrust: 403 (Cloudflare challenge) for every path from this
environment and also through the WebFetch tool; nothing on HathiTrust was tested.

## 4. Candidates tested

Numbers are printed page numbers unless marked `scan` (Google "PP" ids or IA scan index, front matter included).
Target row for comparison: alphabet 14, cipher 79, morrow 272, occupy 288, period 308, southward 388, supply 400,
the 405, you 438.

### Entick's New Spelling Dictionary (London, Dilly; five distinct settings)

| edition | source | alphabet | cipher | morrow | occupy | period | southward | supply | theft | youth | result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1766 | IA bim_..._entick-john_1766 | scan 40 | | scan 205 | | | | | scan 319 | scan 367 | fail, c. 340 pp |
| 1772 | IA bim_..._1772 | (and 14) | 53 | | | | (south 338) | | | (which 420) | fail, day 90 |
| 1773 | IA bim_..._1773 | 8 | | 248 | | | | | 373 | (will 422) | fail, morrow 248 |
| 1776 | GB yT3SS6sQ3k8C, IA bim_..._1776 | 43 (=11, grammar paginated in) | 86 | 248 | 259 | 275 | 347 | 364 | 373 | 427 | fail, alphabet |
| 1780 | GB xZUPAAAAQAAJ | 43 | 86 | | 259 | 275 | 347 | 364 | 373 | 426 | fail, alphabet |
| 1781 | GB 7LFmAAAAcAAJ, IA 11280377bsb | 12 | 58 | 233 | 245 | 263 | | 355 | 364 | 419 | fail, cipher 58 |
| **1782** | IA bim_..._1782 (548 scans) | **14** | | 268 | | 302 | (south **388**) | 408 | 418 | 482 | **near miss**, see below |
| 1783 | GB jVxgAAAAcAAJ | 12 | 58 | 233 | 245 | 263 | 338 | 355 | 364 | 419 | fail, cipher 58 |
| 1784 (Crakelt, 1st rev.) | GB 1V1iAAAAcAAJ | 13 | 60 | 240 | 252 | 270 | 348 | 366 | 375 | 432 | fail, cipher 60 |
| 1786 | GB RoJgAAAAcAAJ | 13 | 62 | | 258 | | | | 381 | 438 | fail, cipher 62 |
| 1787, 1795, 1800 | IA (first pass) | 13 | | 244 | 258 | 276 | (south 354) | | (the 382) | (you 438) | fail |
| 1788 | GB Xw1gAAAAcAAJ | 13 | 62 | 245 | 258 | | | | 381 | 438 | fail |
| 1790, 1791, 1795 (x2), 1796, 1798, 1800 | GB PfxIAAAAcAAJ, vEl4isg9Z_kC, SNwIalh3krMC, EF5iAAAAcAAJ, azlh2lf18B0C, LTRMbkQ7p-MC, 209gAAAAcAAJ | 13 | | 245 | 258 | | | | | | fail, same setting as 1786-1788 |
| 1788, 1791 "copious and accented vocabulary" (Crakelt, small) | IA 1791_0 (first pass); GB enRw7piHamwC, BWlbUYQ0oAQC | 10 | | | | 202 | | | | | fail |
| 1812 London, 400 pp | GB 16URAAAAIAAJ | 42 (grammar in) | | | 222 | | | | | | fail, c. 370 pp of text |
| 1812 "parts of speech accurately distinguished" | GB FZ4syDmUph8C | 39 (grammar in) | | 260 | 271 | | | | | | fail |
| 1812 American (Murray) | IA (first pass) | | | | | | | | | | fail |

Editions of 1785, 1789, 1793, 1794, 1797, 1799, 1801-1811 exist in Google's catalogue without page view (about
90 records, 400-512 pages); by the pattern above they belong to the 1786-1800 setting or the 400-page setting
of 1804-1812. Dublin, Edinburgh and Glasgow reprints: none found in full view (Google feed queries
"entick dublin/wogan/edinburgh/glasgow").

### Other English dictionaries

| edition | source | alphabet | cipher | morrow | occupy | southward | theft | youth / younker | result |
|---|---|---|---|---|---|---|---|---|---|
| Perry, Royal Standard, 1775 | IA (first pass) | | | | | | | | fail, early 115 |
| Perry, Royal Standard, 1788 | IA 10797901bsb | | | | | | | | fail, octavo: head 274, sea 369, which 552 |
| **Perry, Royal Standard, 1795** (printing not identified) | GB 3ltWAAAAYAAJ | 31 (text begins p. 17) | | 275 | 289 | 383 | 408 | 455 | **near miss** in the middle, see below |
| Perry, Royal Standard, 1804 | GB FFtWAAAAYAAJ | 18+ | 89 | 291 | 307 | | | 479 | fail |
| Perry, Royal Standard, 10th ed. 1804 (pocket) | GB UUo1uw-_JZcC | 69 (text begins p. 56) | 124 | | 323 | 417 | 441 | 487 | fail |
| Perry, Royal Standard, 1806 | GB OY8VAAAAYAAJ; IA royalstandarden00cogoog (first pass: the 429, will 474) | | 89 | | 305 | | | 479 | fail |
| Perry, General Dictionary, 1795 | IA bim_..._perry_1795 (360 scans) | | | | | | | | fail, too small |
| Johnson's Dictionary in Miniature (Hamilton), 1795-1812 | GB _CcLJIP8xjQC, g8IDAAAAQAAJ, ZFlgAAAAcAAJ, tSRL29OIZBkC, JwC-GInMrW4C, KKQRAAAAIAAJ and others; IA (first pass) | 9 | | 143 | 150 | | 218 | 245 | fail, half scale |
| Ward's Diamond Johnson in Miniature, 1809 | GB OTp0T8jquBcC | | | 143 | | | 213 | | fail |
| "A Dictionary of the English Language, with ... heathen deities", 1794, 1797 | IA bim_..._1794, bub_gb_AenhsoA1PPIC | | | scan 164 | | | scan 230 | scan 255 | fail, c. 250 pp |
| "A General and Complete Dictionary", 1785 | IA ageneralandcomp00unkngoog | | | scan 161 | | | scan 227 | | fail |
| Scott, New Spelling, Pronouncing and Explanatory Dictionary, Edinburgh 1807 | GB -ounMLoVgd4C | 12 | | 209 | 220 | | | (westward 382) | fail, c. 390 pp |
| Scott, 1810 | GB AktgAAAAcAAJ | 66 (=12, grammar in) | | 263 | 274 | | | (westward 436) | fail, same setting as 1807 |
| Fulton and Knight, General Pronouncing and Explanatory Dictionary, Edinburgh 1802 | GB TV5iAAAAcAAJ | 17 | | 230 | 241 | 322 | 342 | 383 | fail |
| Fulton and Knight, 1814 | GB w6kBAAAAYAAJ | | | 219 | | | | 373 | fail |
| Jones, Sheridan Improved, 1798 | GB sDVAAAAAYAAJ | | | | | | | | no page numbers in OCR; 916 scans |
| Jones, Sheridan Improved, 1805 | GB dvYNAQAAMAAJ | | | scan 286 | | | | | fail |
| Jones, Sheridan Improved, 1812 | IA 10797864bsb; GB o29JAAAAcAAJ | | 76 | 253 | | 354 | 378 | 426 | fail |
| Jones, Sheridan Improved, 1813 | GB 5-NhdcFmyNwC, wuglVSZyJwYC | | | 248 | | | | 418 | fail |
| Sheridan, Pronouncing and Spelling Dictionary, 1800 | GB 0SRnAAAAcAAJ | | | 422 | 444 | | | 663 | fail, octavo |
| Walker, Critical Pronouncing Dictionary, octavo, 1791, 1802, 1806, 1807, 1809, 1810 | GB DaURAAAAIAAJ, q5tWAAAAcAAJ, MGAJAAAAQAAJ, VqURAAAAIAAJ, UPsTAAAAYAAJ, vJwRAAAAIAAJ | | | 343-351 | 360-366 | | | | fail, 600-1100 pp |
| Walker abridged (Smith), 1810 | GB CnQGwQfeT2wC | scan 28 | scan 80 | scan 252 | scan 263 | scan 338 | scan 358 | scan 395 | fail: body 1.1x shorter than target, tail ratio 0.13 |
| Walker, 1810, 422 pp | GB Ft4VAAAAYAAJ | 14 | 59 | 222 | | 318 | c. 340 | 389 | fail, cipher 59 |
| Browne, Union Dictionary, 1806, 1810 | GB 3KDQRByYtYEC, V_fkuRwhJzAC; IA uniondictionaryc00brow | scan 43 | scan 105 | scan 297-318 | | | scan 453-472 | scan 513-534 | fail, c. 500 pp octavo |
| Enfield, General Pronouncing Dictionary, 1807 | IA 10582071bsb; GB G_xIAAAAcAAJ | | | 179 | | | | 318 | fail |
| Fisher, Accurate New Spelling Dictionary, 1788 | IA bim_..._fisher_1788 | | scan 84 | | | scan 311 | scan 332 | scan 371 | fail, tail ratio 0.16 |
| Webster, Compendious Dictionary, 1806 | IA compendiousdictionaryoftheenglishlanguage1806 | | 51 | | | | 308 | 355 | fail |
| Ash, New and Complete Dictionary, 1795 | GB hu0IAAAAQAAJ, 8DNAAAAAYAAJ | | | | | | | | fail, two volumes with etymologies |
| Barrie, Spelling and Pronouncing Dictionary, 1794 | GB 0F1iAAAAcAAJ | | | | 170 | | | | fail |
| Newbery, Spelling Dictionary, 1786, 1792, 1805 | IA (first pass); GB R09gAAAAcAAJ | | | | | | | | fail, word list of c. 330 pp |
| Bentick 1786, Sheridan 1800, Newbery 1792 | IA (first pass) | 9 | | | | | | | fail |
| "A Spelling and Pronouncing Dictionary", 1814 | GB 4MQDAAAAQAAJ | | | 80 | | | | 127 | fail, arranged by syllables |
| Pocket Dictionary or Complete English Expositor 1753, 1758, 1765; Carter 1764; Green 1765; Johnston 1772 | IA | | | | | | | | OCR too poor to place any headword; untested |
| Mylius, School Dictionary, 1809 | IA myliussschooldic00myli | | | | | | | | not tested, 276 scans |

### English parts of bilingual pocket dictionaries

| edition | source | result |
|---|---|---|
| Nugent, French and English, 1791, 1793, 1795, 1797, 1800, 1807, 1814 | GB jic_boydmQYC, AidKHfbNGocC, OZ9yl6J8ZacC, hJPnWHPzhUMC, raxII5RjUvIC, 69xn_DHQ-RkC, _tgDAAAAQAAJ, KlbIN-cQyeEC | fail, English part 230-395 pp (morrow 233 at best) |
| Vieyra, Portuguese and English, 1809 | GB 0mESAAAAIAAJ | fail, English part: alphabet 18, morrow 237, westward 401, youthful 412 |
| Bottarelli, Italian, English and French, 1795 | GB 2jsba0qZhKoC | fail |
| Entick, English-Latin (prefixed to the Latin dictionary), 1792 | GB QgNgAAAAcAAJ | fail, theft 171, younker 196 |

## 5. Near misses

**Entick 1782 setting** (IA `bim_eighteenth-century_the-new-spelling-diction_entick-john_1782`, 548 scans, London,
"small pocket volume", grammar paginated in roman). Running heads read from the OCR: Alphabet 14 (target 14), at 26
(28), be 34 (38), morrow 268 (272), period 302 (308), south 388 (**388**), supply 408 (400), theft 418 (405),
which 474 (433), will 476 (434), youth 482 (438). It agrees at the start, runs 2-6 pages behind through P, meets
the target at S, then runs on to 482 where the target stops at 438. The offset is not constant, so it is not the
same setting shifted; but of all settings tested it is the only one that puts "alphabet" on p. 14 and "south" on
p. 388. Entick's text in this region also fits the within-page spacings (you -> your 7-8 entries, more -> morrow
12-14, south -> southward 6-8, that -> the 5-7), but so would any Entick-derived list. The 1782 page 268 has
"More" as its fourth line, the target has "more" as entry 1 of p. 272. Its columns hold about 50 lines, which
does not fit observation 3 above.

**Entick 1786-1800 setting** (Crakelt; Google RoJgAAAAcAAJ and eleven others; IA 1787, 1795, 1800). Tail agrees:
use 426 (429), will 434 (434), you and youth 438 (438); start nearly agrees: alphabet 13 (14); the middle runs
23-34 pages early (early 123/146, head 177/203, more 244/272, occupy 258/288, period 276/308, rejoin 313/346,
south 354/388, the 382/405). On p. 438 of the 1800 edition (Google text mode) "You" is the 14th entry of the
second column and "Your" the 22nd; the target has 8 and 15. Not this setting.

**Perry, Royal Standard English Dictionary, 1795** (Google 3ltWAAAAYAAJ, 564 scans; printing not identified,
title page not retrievable in text mode). Middle agrees within a few pages: day 121 (116), morrow 275 (272), occupy
289 (288), provision 331-335 (332), quarter 335 (336), seal 365 (365), theft 408 (405); but the text begins on
p. 17 with "alphabet" at 31 (14), southward 383 (388) and youth 455 (438). Perry's S and T-Z are distributed
differently from the target's, so this is a different book that happens to be the same size. Perry's other
settings (1775, 1788, 1804 x2, 1806) are further off.

## 6. What is left untested and why

- **HathiTrust** in its entirety (Cloudflare 403 from this environment, also through WebFetch). From a browser,
  the useful searches are: full-text search restricted to full view for "Alphabet" with date 1770-1812 and
  subject "English language Dictionaries"; catalogue searches for Scott 1797 and 1799 (440 and 443 pages per
  Google's records BW-TygAACAAJ, gEBCnQEACAAJ), Fulton and Knight 1802-1808, Jones's Sheridan Improved 1800
  (456 pages, 67V2tAEACAAJ), Perry's 24mo Royal Standard 1810-1813 (491 pages, dNhdtAEACAAJ, AybEZwEACAAJ,
  TBkWQAAACAAJ), "An Abridgment of Walker's Critical Pronouncing Dictionary" 1810 (428 pages, QNbqSAAACAAJ),
  Entick 1785 and 1789, and Dublin Entick reprints (Wogan, Byrne, 1790s-1800s).
- **Miniature formats.** Observation 3 (about 24 entries per column) points to a smaller format than Entick's
  12mo. Not found in full view: any 24mo or 32mo English dictionary of about 440 pages printed 1780-1812.
- **Urban pp. 232-233**: not read (lending copy only). Worth a library check for a named dictionary and for
  Scovell's own example 134A18.
- **The physical dictionary.** If Wellington sent Bentinck "that [cypher] which I sent to Lord Wm Bentinck", a
  copy of the dictionary went with it. It may survive in the Bentinck papers (Nottingham, Pw Jd), in WO 37
  (Scovell), or in the Maitland lot itself (Spink 26066 lot 1184 includes "a box"); the lot description does
  not mention a dictionary. This is the person's job (a question to Spink before 23 Sept 2026), not a worker's.
- **A different convention for the position number.** If the number counts lines within a half-column, or
  entries within a letter block, observation 3 changes; the 1782 Entick setting would then deserve a page-by-page
  check of every within-page constraint from the images (its OCR running heads are poor; about a third of the
  target words could not be located automatically).

## 7. Counts

| | |
|---|---|
| volumes tested this pass | 57 (Google Books 44, Internet Archive 13) |
| Entick settings tested | 5 (1766-1780, 1781-1783, 1782, 1784, 1786-1800) plus the 400-page 1812 and the "copious" variant |
| passes | 0 |
| near misses (partial agreement, no constant offset) | 3 |
| readings produced | none (H 0, C 0, S 0, M 0, I 3 inferences in section 1) |
