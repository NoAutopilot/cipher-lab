# Louis de Geer papers with cipher key, 1644-1646

**Status: blocked**
The standard edition could not be opened: Dahlgren, *Louis De Geer 1587-1652* (1923) is not on archive.org (advancedsearch `title:(Dahlgren) AND title:(Geer)` 2 Oct 2026 returned no Dahlgren item) and no edition of the Leufsta letters or of Axel Oxenstiernas skrifter och brev (0 hits on IA `title:(Axel Oxenstiernas skrifter och brev)`) was reachable, so no page was read; blocked pending a copy or a digitised edition (the folder itself, SE/ULA/13506/1/I/45, `onlyDigitisedMaterials: False` on its Riksarkivet record, is also not online).

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
