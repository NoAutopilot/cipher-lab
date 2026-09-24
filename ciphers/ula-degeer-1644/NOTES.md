# Louis de Geer papers with cipher key, 1644-1646

**Status: open**

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

**Verdict:** open. No prior solution, key transcription, or attempt found anywhere searched. This is the
weakest-confirmed key-to-text match of the four rows in this batch (QUEUE.md's own caveat): the folder holds a
cipher key among de Geer's papers, but the catalogue note does not say it applies to any of the listed
letters/journals, so the physical folder must be seen before assuming this is a recovery rather than a
cryptanalysis target (or that a decipherable item exists in it at all).

**Not digitised — copy order needed.** See REQUEST.md.

## Request log

24 Sept 2026: no personal data logged here.
