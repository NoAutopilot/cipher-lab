# Louis de Geer papers with cipher key, 1644-1646

**Status: blocked**
No ciphertext is reachable: the folder SE/ULA/13506/1/I/45 (`onlyDigitisedMaterials: False` on its Riksarkivet record) is not online and holds the only known key (needs-physical-access; REQUEST.md copy order). Editions (corrected 3 Oct 2026, GAPS124): the earlier reason "no edition of Axel Oxenstiernas skrifter och brev reachable" came from a wrong-title search; AOSB II:11 (1905, De Geer's letters to Oxenstierna 1621-1645, pp. 653-) was read in full OCR by A2-ULA on 2 Oct (one code group, "171" = Haag, p. 673 footnote) and Dahlgren's edition *Louis De Geers brev och affärshandlingar 1614-1652* (Historiska handlingar 29, 1934; Google Books 0-gOAAAAQAAJ, snippet-only) was searched for chiffer/chiffre/ziffer/cijfer with positive controls on 3 Oct, no hit. Dahlgren, *Louis De Geer 1587-1652: hans lif och verk* (1923, 2 vols) is not digitised on IA, HathiTrust or Google Books and was not read.

## Item

Louis de Geer (1587-1652, financier and armaments supplier to Sweden during the Thirty Years' War and the
1643-45 Torstenson War against Denmark, operating in Axel Oxenstierna's circle) — journals, letters and a cipher
key, 1644-1646. Shelfmark SE/ULA/13506/1/I/45 (Leufstaarkivet I, "Leufsta arkiv. Det historiska arkivet"),
Riksarkivet i Uppsala landsarkiv (Landsarkivet i Uppsala). Found by the LANE S scout of 24 September 2026,
QUEUE.md row R3, kind: recovery. Catalogue note in full: "Brev från W. Lancken (?) 1644, 2 st. Förteckning å
förluster som Louis de Geer lidit genom konungen av Danmark 1645-1646. Louis de Geers advertisement insänt till
Axel Oxenstierna 17/8 1644. Journal myner Reyse... Chiffernyckel. Förteckning över adressater (moderna) i
journalerna." — the cipher key sits among de Geer's own war-logistics correspondence and travel journals, but
which specific letter(s) it maps to is not stated in the catalogue snippet (an unconfirmed key-to-text match,
as QUEUE.md's own row already flags).

No transcription or image exists in this repository; `ciphertext.txt` is not created (rule 2).

## Check-solved sweep, 24 September 2026

Run directly by this worker, per `.claude/briefs/check-solved.md`'s six sources. 6/6 checked, 0/6 found a
solution, key transcription, or documented prior attempt.

**Editions first:** the standard biography is E.W. Dahlgren, *Louis De Geer 1587-1652: hans lif och verk*
(Stockholm, 1923; printed in only 300 copies per bookseller listings found by WebSearch, e.g. Bokus). Checked
Internet Archive for a scan: `archive.org/advancedsearch.php?q=title%3A(Louis+De+Geer)+AND+Dahlgren` returns
0 hits — not on Internet Archive. Not checked on HathiTrust (no HTRC Extracted Features test run this pass —
the book's rarity, 300 copies, makes a HathiTrust scan unlikely, but this is not confirmed absence, only
non-digitisation on the one route tried). A modern reissue, *Entreprenören Louis De Geer och hans samtid,
1587-1652* (Carlssons förlag), exists per WebSearch but as a recent commercial book, also not full-text
searchable. No edition of de Geer's own letters or the Leufsta journals specifically was found (as opposed to
biographical treatments of him).

**Web:** WebSearch "Louis de Geer chiffernyckel Oxenstierna 1644 Leufsta" and "Dahlgren \"Louis De Geer\" 1923
biografi brev chiffer" — results are genealogical/biographical (Adelsvapen-Wiki, SBL, Wikipedia, Leufstabruk
heritage-site pages) confirming de Geer's role in 1644 and his connection to Oxenstierna and Leufsta, but no
mention of "chiffernyckel" or any cipher-related matter in either search.

**Community lists:** `sources/cryptiana/` grepped for "geer"/"degeer" and "de geer" (word-boundary) — no hits.

**DECODE:** not logged separately — same session, same negative result as R1/R2 (no login attempted per this
brief; de-crypt.org not indexed by the web search engine for this name).

**Bourdeau:** same shallow clone. `grep -rli "de geer\|degeer"` (word-boundary) across the whole tree: no
matches at all. (An earlier broad substring grep for "geer" alone hit unrelated files —
`geertruidenberg/NOTES.md`, `sperantio1534/...`, `esp318/...` — all false positives on "Geer-" as a substring
of other words/identifiers, not de Geer; checked by eye and excluded.)

**Aymeloglu:** same shallow clone, same word-boundary grep, no matches.

**Riksarkivet digitisation check:** queried `text=chiffernyckel Geer&type=Record` (1 hit after one retried
transient `SSL_ERROR_SYSCALL` — the first attempt failed to connect, the retry after a ~5s pause returned 200).
This item's record, SE/ULA/13506/1/I/45: `onlyDigitisedMaterials: false` — **not digitised**. No IIIF manifest
or image link.

**Verdict:** open (24 Sept 2026; superseded by the blocked word above, 2 Oct 2026). No prior solution, key transcription, or attempt found anywhere searched. This is the
weakest-confirmed key-to-text match of the four rows in this batch (QUEUE.md's own caveat): the folder holds a
cipher key among de Geer's papers, but the catalogue note does not say it applies to any of the listed
letters/journals, so the physical folder must be seen before assuming this is a recovery rather than a
cryptanalysis target (or that a decipherable item exists in it at all).

**Not digitised — copy order needed.** See REQUEST.md.

## Request log

24 Sept 2026: no personal data logged here.

## Web and blog check (CS-A2-A, 2 Oct 2026)

Five WebSearch queries, none found a cipher item for De Geer:
1. `Louis De Geer chiffernyckel Leufsta arkiv 1644 chiffer brev Oxenstierna` -- Wikipedia, DBNL Oxenstierna pages, Upplands arsbok 1980 (Leufsta manors), SNL; no cipher mention.
2. `"De Geer" 1644 Torstensson war cipher letters ... deciphered key Uppsala Leufsta` (run with 3 variants) -- results on other Oxenstierna ciphers: HistoCrypt 2024 "Decipherment of a German encrypted letter ... Heusner von Wandersleben to Axel Oxenstierna in 1637" (dspace.ut.ee), HistoCrypt Portuguese-Brazil 1646 ciphertexts, Cipherbrain "an unsolved encrypted letter from the 17th century" (2019); the Leufsta Library page (Uppsala University Library). None names a De Geer cipher or this volume. Not opened beyond titles/snippets except as listed.
3. `SE/ULA/13506/1/I/45 Leufsta` -- only Leufsta heritage pages; no catalogue hit.
4. Site search, allowed_domains ciphermysteries.com, cryptiana.blogspot.com, scienceblogs.de (Cipherbrain), cryptiana.web.fc2.com: `Louis De Geer cipher` -- La Buse, McCormick, Louis XIV, Henry II, WWII machine posts; no De Geer. No Cryptiana or Cipher Mysteries thread names him.
5. Riksarkivet Sok API `data.riksarkivet.se/api/records?text=chiffernyckel Geer&type=Record` (first attempt SSL_ERROR_SYSCALL, one retry after 6 s, HTTP 200, 1 hit): SE/ULA/13506/1/I/45, type Volume, Riksarkivet i Uppsala, `onlyDigitisedMaterials: False`; note field as quoted above (cipher key mentioned, no letter linked to it). Record URL https://sok.riksarkivet.se/arkiv/atECqXwbhqgbWmoUy7y9YD.

Local `sources/cryptiana` grep for "geer" last done 24 Sept 2026 (no hit).

## Premise check (CS-A2-A, 2 Oct 2026)

- (a) folder's own mentions of a decipherment: none; the catalogue lists "Chiffernyckel" and a "Förteckning över adressater (moderna)" (a modern list of addressees for the journals), which is a finding aid, not a decipherment. Not found.
- (b) solver repos, fresh shallow clones 2 Oct 2026: grep `de ?geer` found nothing in dbourdeau/cyphersolver outside the earlier false positives and 0 rows in Aymeloglu's DECODE catalogue. Not found.
- (c) physical neighbours: no image; unreachable (not digitised).
- (d) recipient's side: Axel Oxenstierna's own letters/answers (Axel Oxenstiernas skrifter och brev, Riksarkivet series) were not reachable online; De Geer's 17 Aug 1644 advertisement to Oxenstierna may be printed there. Unreachable.

Request counts: archive.org 3 (advancedsearch), data.riksarkivet.se 2 (one SSL reset, one retry), WebSearch 7. Cheapest next step: a worker to look for Axel Oxenstiernas skrifter och brev volumes on a full-text host (runeberg, Google Books API snippets) for "chiffer" with De Geer, ~$1.

## Oxenstierna edition full-text search (A2-ULA, 2 Oct 2026)

Intake gate pasted before work: `ula-degeer-1644: blocked (line 3) -- already terminal, nothing to gate` (exit 0).
The target has no Remaining gaps / Escalation sections (status `blocked`), so this step goes under this dated heading only.

**What was wrong in the earlier search.** The 2 Oct check-solved sweep reported "0 hits on IA `title:(Axel Oxenstiernas skrifter och brev)`".
The edition's printed title is *Rikskansleren Axel Oxenstiernas skrifter och brefvexling*. Searching IA for `title:(Oxenstiernas) AND title:(brefvexling)`
returns 8 Google-scanned volumes: rikskanslerenax00akadgoog, 01akadgoog, 02akadgoog, 03akadgoog, 00styfgoog, 01styfgoog, 00palagoog and 01palagoog.
All 8 `_djvu.txt` OCR files were fetched with HTTP 200 and grepped locally for `de *geer` and for `chiff|ziff|cif(f)r|cyph|ciph|siffr`.

**Hit, AOSB II:11 (1905).** The volume is "Senare afdelningen, elfte bandet: Carl Bonde och Louis De Geer m. fl. bref angående bergverk, handel och finanser", identifier
`rikskanslerenax03akadgoog`. It prints "Louis de Geers bref 1621-1645" to the Chancellor from p. 653. The preface says that only the war years 1644-1645 involve letters on direct
commission. The 1644-45 letters printed there are: no. 15 (OCR reads "16"), Norrköping, 6 Jan 1644; no. 16, Haag, 28 Mar 1644 (autograph, Dutch); no. 17, Amsterdam, 4/14 May 1644; no. 18,
Amsterdam, 24 May 1644; no. 19, Amsterdam, 28 Aug 1644; no. 20, Göteborg, 14/24 Sept 1644; no. 21, Stockholm, 10 Jan 1645 (heading OCR "1646", year not checked on the image); no. 23, Stockholm, 28 Apr 1645; no. 24, Stockholm, 30 Oct 1645.
- **Cipher evidence, p. 673, letter no. 16 (Haag, 28 Mar 1644).** The text reads "...ende daer naer eerst partie kiesen, ende 171\*) niet achten." The editors' footnote on p. 673
  reads: "\*) Tydligen chiffer. Siffran återges i åtskilliga chifferklaver från denna tid med »Haag.»" ("Evidently cipher. Several cipher keys of this period render the number
  as 'Haag'.") So De Geer used a numbered code (a nomenclator-style name code) in at least one 1644 letter to Axel Oxenstierna. The 1905 editors identified the value from
  other period keys, not from De Geer's own key.
- **No other cipher token.** In the De Geer section (OCR lines about 34480-36300), grepping for two- and three-digit numerals that are not years, sums, or dates found no other
  code group, and the cipher-word grep found nothing else. The printed 1644-45 letters are otherwise in clear (German or Dutch). One caveat: the edition prints what survives
  in the Oxenstierna collection (Riksarkivet), and its notes name letters that are "not extant" (p. 672, the letter of 16/26 Feb 1644) or that apparently never arrived (p. 678).
  A letter in cipher may therefore be missing from the print.
- **The 17 Aug 1644 "advertisement".** The ULA catalogue note names "Louis de Geers advertisement insänt till Axel Oxenstierna 17/8 1644". No item with that date is printed
  in II:11. The nearest is no. 19, Amsterdam, 28 Aug 1644, which the p. 679 note calls "possibly the copy printed here as no. 19". The grep found no "advertis" string in the volume.
- **Other volumes.** De Geer is mentioned in II:1 (00styfgoog), II:8 (00palagoog: notes on "Louis de Geers flotta", Aug 1644), II:10 (01palagoog) and the first series
  (00akadgoog). None has a cipher word within 4 lines of a De Geer mention.
- **Google Books API** (keyed, `country=US`, 2 queries). `"de Geer" chiffer 1644` returned the same II:11 page as snippet ("...DGeer. \*\*) 17. Amsterdam den 4/14 Maj 1644 ...
  chiffer. Siffra..."), from both the 1905 volume and a duplicate record. It also listed *Bijdragen en mededelingen van het Historisch Genootschap* (1908), which prints
  "No. 48. Louis De Geer aan Johan Axelsson Oxenstierna ... Amsterdam 13/23 J[...]". That is a different correspondent and was not opened. `"Louis de Geer" chiffernyckel` returned 0 results.
- **runeberg.org.** One guessed path (`/aosb/`) returned 404. Runeberg was not searched beyond that path, so it is untested, not a negative.

**What this settles and what it does not.** (1) The Oxenstierna edition can be read online. The status-line reason "no edition of ... Axel Oxenstiernas skrifter och brev was
reachable" came from a search with the wrong title, so it no longer holds for that edition. Dahlgren 1923 and the ULA folder itself remain unread and are still not digitised.
(2) There is now printed evidence, at grade H as quoted, that De Geer used a numeric code to Oxenstierna in March 1644, in the same months the ULA folder covers. This makes
it more likely that the "Chiffernyckel" in SE/ULA/13506/1/I/45 is the key to his 1644-45 correspondence. Whether it actually is that key remains untested. (3) The printed
letters give only one code group ("171" = Haag, editors' identification from other keys). That is far too little for cryptanalysis, and no ciphertext is on disk (rule 2).
The target still depends on the ULA folder, or on unprinted De Geer letters in Riksarkivet's Oxenstierna collection (series not looked up).

Request counts: archive.org 10 (2 advancedsearch, 8 djvu.txt), www.googleapis.com 2, runeberg.org 1. No vision calls. Not found in: AOSB II:1, II:2, II:5, II:8, II:10, the first-series
volumes on IA (no cipher word near De Geer), or runeberg (one path tried).

Next cheapest step: check whether the folder's key matches code 171 = Haag. This needs the folder, so it stays with REQUEST.md (copy order). In parallel, a worker could
look up the Riksarkivet Oxenstierna collection record for "Louis de Geer" letters 1644-45 (Sök API, about $0.5) to see whether that series is digitised. Not done here, because it is outside this step's brief.

## GAPS124-ula-degeer-1644 (3 Oct 2026, account-4): edition step

Clock read 13:35 UTC 3 Oct 2026. Stale-check first: A2-ULA (2 Oct, above) had already found and grepped the Oxenstierna edition (8 IA volumes, II:11 p. 673), so this job covered what was left: Dahlgren 1923, Dahlgren's own edition of De Geer's letters, runeberg, and the stale status-line reason. Intake gate before work: `ula-degeer-1644: blocked (line 3) -- already terminal, nothing to gate` (exit 0). No vision, no subagents, no reading.

| Source | Route | Control | Result |
|---|---|---|---|
| Dahlgren, *Louis De Geer 1587-1652: hans lif och verk*, 2 vols, Uppsala 1923 | Open Library search -> OCLC 5198616, 54394464 -> HathiTrust bib API `volumes/brief/oclc/N.json` | same API returned a record for an unrelated 1923 OCLC (1563468) | 0 records for both OCLCs: not in HathiTrust; no EF test possible (no htid) |
| same | IA advancedsearch `"Louis De Geer" AND (Dahlgren OR date:1923)` | -- | 0 items (agrees with 24 Sept and 2 Oct searches) |
| same | Google Books API `intitle:"Louis De Geer" inauthor:Dahlgren`; author/title queries | -- | catalogue-only records (5LZp0AEACAAJ, c84OogEACAAJ), no text; not read |
| Dahlgren (ed.), *Louis De Geers brev och affärshandlingar 1614-1652*, Stockholm 1934 (Historiska handlingar 29), 707 pp. -- the sender's printed letters, not named in this folder before today | Google Books 0-gOAAAAQAAJ (Oxford copy, NO_PAGES, snippet search); queries `<term> "Louis De Geers brev och affärshandlingar"` | in-volume positives: `Oxenstierna 1644`, `Haag`, `Göteborg 1644`, `Amsterdam 1645`, `Leufsta Finspång` all return snippets from this volume (contents: no. 371-392, 1644-45 letters incl. to Axel Oxenstierna); cross-volume positive: `Haag 171 chiffer "De Geer"` finds AOSB II:11 p. 673 (also NO_PAGES) | `chiffer`, `chiffre`, `ziffer`, `cijfer`, `chifferbrev`, `chiffernyckel`: 1934 volume absent from every result. Caveat: two body-text controls (`1644 Danmark`, `Torstensson`) also missed, so the snippet index does not cover all body text; this is a search result on a partial index, not a read of the book (IA advancedsearch `title:(Geers) AND title:(brev)` 0, Open Library 0 -- not on IA) |
| runeberg.org | `/authors/dahlgew.html` (200, page not parsed: write error in the pipe, not retried), `/aosb/` (404) | -- | untested beyond two paths |

**Lead noted, not followed (outside this step):** *Riksarkivets beståndsöversikt: Särskilda bestånd* (1993, Google Books NK0mX6pUjJwC, snippet) indexes "Chifferklaver 205" and "De Geer, Louis 106" -- Riksarkivet keeps a collection of period cipher keys (the AOSB editors' footnote identified 171 = Haag from "several cipher keys of this period"). Whether De Geer's key or a copy is in that collection is unknown.

What this settles: the sender's two printed editions (AOSB II:11 in full OCR; Dahlgren 1934 by snippet search with controls) show one printed code group and no other cipher mention found; the cipher material itself is only in the undigitised ULA folder. Status stays `blocked` (needs-physical-access), with the line-3 reason corrected. Rule 10: nothing here is a novelty claim.

Requests: openlibrary.org 2, archive.org 2, catalog.hathitrust.org 3, www.googleapis.com 22, runeberg.org 3. Vision calls 0.

Next cheapest step: Riksarkivet Sök API (`data.riksarkivet.se/api/records`) for the "Chifferklaver" collection and for Louis de Geer letters 1644-45 in the Oxenstierna collection (digitisation flag), about USD 0.5; otherwise the REQUEST.md copy order.

## GAPS128-ula-degeer-1644 (3 Oct 2026, account-4): Riksarkivet Sök API step

Clock read 13:54 UTC 3 Oct 2026 (start). Route: Riksarkivet Sök API `data.riksarkivet.se/api/records` (JSON), one OAI-PMH `GetRecord` (`oai-pmh.riksarkivet.se`), one IIIF manifest (`lbiiif.riksarkivet.se`, manifest only, no image). Descriptive UA, >=1.6 s apart, `--tlsv1.2`; three `SSL_ERROR_SYSCALL` resets, each retried once after 6 s (two of the three retries returned 200; the `Louis de Geer` 1644-46 query and a json-ld record fetch did not, both re-run by another route). No vision, no subagents, no reading. Rule 10: what follows is catalogue search results, not a novelty claim.

**Positive control.** `text=chiffernyckel` returned 5 hits including this target's own volume SE/ULA/13506/1/I/45 (`onlyDigitisedMaterials: false`), as on 24 Sept and 2 Oct: the API finds a known De Geer cipher-key record.

| Query | Hits | What it shows |
|---|---|---|
| `text=Chifferklaver` | 7 | Fonds SE/RA/202 "Chifferklaver" (1500t-1894, not digitised): "Sökingången till innehållet är 2 st kortkataloger i volym 20 och 21" -- the item-level finding aid is H. Stålhane's 1934 card catalogue, SE/RA/202/20 (I:1, 1500t-1690t) and /21, both not digitised. SE/RA/202/1 (1500-1640) is the box with the itemised note (Kanslichiffer 1620-1650s, I:14 Oxenstierna-Torstensson, Anders Svensson, Camerarius, Spens...; quoted in ciphers/oxenstierna-gustav-adolf-1632/NOTES.md); **no De Geer in that note**. Also SE/RA/754/2/XX/4 (Horn's 1678-79 Prussian expedition, out of period). |
| `text=Chiffernycklar` | 27 | Units SE/RA/202/2 ("1600t", note only "Chiffernycklar, positiva och resolutiva"), /3 (1650t-1700), /4-/16 (1700s-1850s); all `onlyDigitisedMaterials: false`, none names a correspondent. Also **SE/RA/721502/3/1**, Oxenstiernaprojektets arkiv (1999-2005): "Chiffer och chiffernycklar avseende Axel Oxenstiernas korrespondens" -- the edition project's own notes on ciphers in Oxenstierna's correspondence; not digitised. |
| `text=chiffer&year_min=1643&year_max=1646` | 4 | Vellingk 1714, Karl XI fullmakt 1676-77, the Chifferklaver fonds, one 1810 KrA unit. Nothing 1643-46 and nothing De Geer. |
| `text=Geer chiffer` | 0 | -- |
| `text=Louis de Geer&year_min=1644&year_max=1646` (second form) | 48 | All Leufstaarkivet I volumes (I:14, I:20, I:22, I:26, I:33, I:39, I:46, I:48, I:49, I:109, I:138, I:155 ...) carry `onlyDigitisedMaterials: false` except I:42 (worker contracts, digitised, not a cipher unit). No cipher word in any of the 48 notes (grep `chiff|ciffr|cipher|nyckel|klav`) other than the target volume reached by the control. |
| `text=Geer Louis&year_min=1621&year_max=1652` | 58 | Adds SE/RA/2109/VII/17 (Kungl. Maj:ts instruktion for De Geer, 1643, copy), accounts (SE/RA/5103/109, KrA), registers; no cipher word. |
| `text=Geer&facet=PartOfArchive:Oxenstiernska samlingen` | 2 | **SE/RA/720701/II/01/B/I/E 584 "Dach-De Geer"**: Oxenstiernska samlingen > Oxenstierna af Södermöre > Axel Oxenstierna > Inkomna brev och ansökningar > Furstars, ämbetsmäns och enskilda personers brev -- the volume of letters to Axel Oxenstierna from senders Dach to De Geer, i.e. the originals AOSB II:11 prints from. `onlyDigitisedMaterials: false`; no note, no date range on the record (OAI-PMH EAD for E 584 adds only title and Arkis dates). Record https://sok.riksarkivet.se/arkiv/4ULhbVoSVas7yrWtjzBDN9. Also E 813 (fortifications/war material 1612-1653, "räkningar (bl.a. från Louis de Geer)"), not a letter series. |
| `text=Oxenstierna Geer` / `text=Oxenstiernska samlingen Geer` / long form | 823 / 1 / 0 | Noise (Leufsta and 20th-c. LLA units); the 1 hit is SE/RA/2109/I/2/2 (letters to the king 1609-20, "räkning från Louis de Geer", cross-reference "Oxenstiernska samlingen (E 592)"). |

**One digitised De Geer letter found (no cipher indication).** SE/RA/1133/1133.08/~/2, Kunglig Majestäts kansli, "Skrivelser till konungen" D-K, 1634-1654: note "De Geer Louis, odat. 1645 21 januari." `onlyDigitisedMaterials: true`; IIIF manifest https://lbiiif.riksarkivet.se/arkis!R0001367/manifest (HTTP 200, label "Skrivelser till konungen, SE/RA/1133/1133.08/~/2 (1634-1654, u.å.)", 292 canvases "Bild 1"...). Record https://sok.riksarkivet.se/arkiv/XDcqZ8cRrH6d0G02H087k3. This is a letter to the Crown, not to Oxenstierna; nothing in the record says it is in cipher; its canvas number within the volume is not known (senders are alphabetical, De Castro then De Geer, so it should be near the start). No thumbnail was fetched: without a canvas number a single thumbnail could not locate it, and the brief allows the thumbnail only for a digitised key or cipher letter.

**What this settles.** (1) No Riksarkivet record found names a De Geer cipher key or a De Geer cipher letter of 1644-46 other than the target volume itself; the Chifferklaver unit notes do not name him, but the units 202/2 and 202/3 carry only a generic note and the item-level index is the undigitised 1934 card catalogue (SE/RA/202/20-21), so "not in Chifferklaver" is **not** established -- it is unsearchable online. (2) De Geer's original letters to Axel Oxenstierna are in Oxenstiernska samlingen E 584 "Dach-De Geer", not digitised. (3) The Oxenstierna edition project kept notes on ciphers and keys in Oxenstierna's correspondence (SE/RA/721502/3/1, not digitised) -- the most likely place where code 171 = Haag (AOSB II:11 p. 673) is documented. (4) Status stays `blocked` (needs-physical-access): every unit that could hold the key or ciphertext -- SE/ULA/13506/1/I/45, Oxenstiernska samlingen E 584, Chifferklaver SE/RA/202/1-3 with cards 202/20, Oxenstiernaprojektet 721502/3/1 -- is `onlyDigitisedMaterials: false`.

Requests: data.riksarkivet.se 15 (including 3 SSL resets and their retries), oai-pmh.riksarkivet.se 1, lbiiif.riksarkivet.se 1 (manifest only). Vision calls 0. Clock at end 13:59 UTC.

### Next step / While waiting (3 Oct 2026)

- **Next (needs a person, REQUEST.md):** add to the existing copy order three Stockholm units beside the ULA folder: Oxenstiernska samlingen E 584 (De Geer's 1644-45 letters to Oxenstierna, to see whether any is in code beyond the printed "171"), Chifferklaver card catalogue SE/RA/202/20 (look up "Geer" / "Haag 171"), and Oxenstiernaprojektet SE/RA/721502/3/1.
- **While waiting (depends on nobody, ~USD 1-3):** one Opus vision pass over the first ~20 canvases of the digitised SE/RA/1133/1133.08/~/2 (lbiiif R0001367) to find De Geer's 21 Jan 1645 letter to the Crown and say whether it carries any code group; thumbnail-size first, one native crop only if a numeral group is seen.

## D2B-ULA (6 Oct 2026, account 2): the "21 Jan 1645" item in SE/RA/1133/1133.08/~/2

Clock read 00:13 UTC 6 Oct 2026 (start). This step is the one named in "While waiting (3 Oct 2026)" above, and it had not been run before. Route: Riksarkivet IIIF (`lbiiif.riksarkivet.se`): the manifest `arkis!R0001367/manifest` (292 canvases), then thumbnails 1000 px wide (canvas 2 at its native 792 px) of canvases 1-24 through the v2 image service, and one native-resolution region of canvas 10 (`400,1250,2400,450`) to read the date line. Descriptive UA, requests >= 1.6 s apart, no 403 or 429. No subagents were used. The pages were read by eye at thumbnail size, plus the one region crop.

**Where the De Geer material sits.** Riksarkivet's archivist slips arrange the volume alphabetically by sender: canvas 3 De Besche (1639), canvases 5-7 De Castro (Hamburg, 18 June 1646, Latin), **canvases 8-14 "Louis de Geer", slip marked "8 blad"**, and canvas 15 Jacob de la Gardie. The De Geer group contains:

| Canvas | Item | Language | Code groups seen |
|---|---|---|---|
| 8 r, 9 l | Account headed "Louis de Geers ... haben in aller Unterthänigkeit bey Ihrer Kön. May^t. und der Cron zu fodern" (his claims on the Crown: the 1643-45 fleet, interest, and a total "bis ult. Decemb. 1654"), with a running memorandum | German | none; every numeral is a sum in Rdr or a year |
| 9 r - 10 l | **The 21 Jan 1645 item.** It opens "Wij Christina ..." and ends (native crop, canvas 10): "hafwe Wij detta medh egen hand underskrifwit och wårt Secret bekräfftat, Datum Stockholm den 21 Januarij 1645". It is a copy or engrossment of the Crown's undertaking to De Geer about paying for the fleet he equipped in Holland (sums of 300000 and 100000 Rdr, "equippagen", "Lieutenant", "Cronones Wägnar"). **It is not a letter from De Geer.** | Swedish | none; numerals are sums |
| 11 r - 12 l | Undated letter to the Queen ("Großmächtigste Hochgeborene Fürstin, Allergnädigste Königin"), signed "Louys de Geer". It concerns a sale of 36 tonnes, "Pierre ... und Karel ...", "Comissarien zu deputiren". This is probably the "odat." half of the catalogue note | German | none |
| 13 r - 14 l | "Copia Ränttor uppå ... Quarnar i Norrköpinge ... An. 1628" (mill rents at Norrköping), followed by a German text continuing on 14 l | Swedish / German | none; numerals are rents and sums |

**Result.** The catalogue note "De Geer Louis, odat. 1645 21 januari" covers an undated German letter from De Geer to the Queen and a Swedish document of the Crown dated Stockholm, 21 Jan 1645. All of the De Geer material (canvases 8-14) is in clear text. No numeral group appears outside a running sum, date or rent, at thumbnail resolution. One region was checked at native resolution. This is a reading of the images, not of a transcription (rule 2). The caveat is that a short code group written inside a line of small German current hand could be missed at about 1/5 native scale. Nothing here bears on the key in SE/ULA/13506/1/I/45.

**What this settles.** The "While waiting" step is done: this digitised volume holds no De Geer cipher material. Status stays `blocked` (needs-physical-access). The cipher material is still only in the undigitised units named above: SE/ULA/13506/1/I/45, Oxenstiernska samlingen E 584, Chifferklaver SE/RA/202/1-3 with its cards 202/20, and Oxenstiernaprojektet SE/RA/721502/3/1. The REQUEST.md copy order is unchanged. No other step can be run online in the meantime.

Requests: lbiiif.riksarkivet.se 28 (1 manifest, 24 thumbnails, 1 stray full-size range request of canvas 10 aborted after the first byte, 1 region crop; 1 HTTP 400 on canvas 2 at 900 px, above native width). Vision: by eye in this session, no subagent calls. Clock at end: see the ROOM done line.

## Next step (R13-STALE, 6 Oct 2026)

Next step: the copy order in REQUEST.md ("waiting on you", owner-side) for SE/ULA/13506/1/I/45, extended to Oxenstiernska samlingen E 584,
the Chifferklaver card catalogue SE/RA/202/20 and SE/RA/721502/3/1 (all `onlyDigitisedMaterials: false`) -- needs the owner. The 3 Oct
while-waiting step is done (D2B-ULA, 6 Oct: the digitised 1133.08 volume's De Geer material is all in clear), and no online step is left that
depends on nobody. Status stays `blocked` (needs-physical-access). Housekeeping line, R13-STALE (account 4): no work run.
