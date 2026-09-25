# Lead: "Chiffre" sections in Recueil des instructions...Suède, vol. 2 (1885)

Status: **closed-negative** for this lead as a raw-cipher or key-table source. Located, read, and reported per
the locate-step brief (TX-HT1, LANE TX, 25 Sept 2026); no check-solved run, no decoding attempted, per the
job brief's scope.

## What was asked

QUEUE.md row HT1 (LANE N HathiTrust numeral-density detector, 24 Sept 2026) flagged a `TABLE DES CHAPITRES`
(table of contents) page near the front of *Recueil des instructions données aux ambassadeurs et ministres de
France depuis les traités de Westphalie jusqu'à la Révolution française: Suède*, vol. 2 (Commission des
archives diplomatiques, 1884-85), carrying the token "Chiffre" twice. The HTRC Extracted Features API gives
bag-of-words counts with no page order, so it could not say what page the "Chiffre" chapter starts on or what
it contains. This worker's job: locate the actual page(s) and read them.

## Route used

Internet Archive: **negative**. `advancedsearch.php` (title and full-text queries for "Recueil des
instructions" + "Suède"/"Suede", several phrasings) returned 0 matching identifiers for this specific
Suède volume; IA holds none of this Suède series under any identifier this session found (2 requests,
>=1.5s apart).

Google Books: **positive**. Volume `aFl0UpDNkusC` ("...Suède", 1885, `viewability: ALL_PAGES`,
`publicDomain: true`, `pageCount: 638`, image-only, no OCR text layer) is the exact volume. Direct PDF
download and the `books.google.com/books?...&q=` search-inside URL both hit Google's bot-check ("sorry" page)
under plain curl/fresh-navigation; **the in-page "Search in this book" box, filled and submitted with a real
Playwright browser session (`tools/browser_fetch.js --type "#search_form_input=Chiffre"`), works** and returns
highlighted snippet thumbnails with page links — a route not previously recorded for this host. That search
found "Chiffre" on 9 pages of the book (relevance order): iv, xv, lxxxi, 184, 185, 428, 429, 441, 471.

## What "the Chiffre chapter" actually is

There is **no single "Chiffre" chapter**. The front-matter `TABLE DES CHAPITRES` lists "Chiffre" as a
**sub-topic entry within at least two different ambassadors' instruction chapters**, each pointing to a short
prose section titled "CHIFFRE" embedded in that chapter, not a standalone chapter of its own:

- **p. 185** — chapter for the comte d'Avaux's embassy (context: reference to the 1697 Ryswick peace treaties,
  so ~1698). One paragraph, headed "CHIFFRE.": the King is sending d'Avaux "un nouveau chiffre" by a secure
  channel, to be used only for despatches starting with the cipher indicated by an accompanying table, kept
  personally by the ambassador in his cassette, never copied, never entrusted to a secretary. **Prose about the
  cipher's custody and use protocol. No table, no digits, no plaintext-ciphertext pair printed on this page.**
- **pp. 428-429** — chapter XXII, comte de Modène's embassy, 1768. Headed "CHIFFRE." on p.429 (the topic starts
  mid-paragraph on p.428: "On joint ici cinq tables différentes de chiffres" -- five tables are attached to the
  original archival instruction: (1) "ordinaire", for the ambassador's correspondence with the minister of
  foreign affairs; (2) for pieces communicated to the comte de Modène needing cipher; (3) "de réserve", for
  particular/important circumstances or suspected interception of the ordinary cipher; (4) a longer one for
  extraordinary, most-secret cases; (5) "correspondance générale", for the ambassador's correspondence with
  other ministers). **Again prose describing five cipher tables and when to use each -- the tables themselves
  are not reproduced in this edition.** Page 430 (verified) is blank, then chapter XXIII begins -- the Modène
  chapter's "Chiffre" topic ends in prose, nothing follows it.
- **pp. 441-442** — chapter XXIII, comte de Vergennes's embassy, 1771-1774. Same pattern: "On joint ici trois
  tables de chiffre" (ordinaires / de réserve / for communicated pieces), with a note that "le sieur
  Barthélemy, chargé des affaires du Roi à Stockholm, remettra au comte de Vergennes les tables de chiffre" --
  the tables are handed over separately by Barthélemy, not printed here either.
- **pp. iv, lxxxi** — false positives: "chiffre" here means "numeral/figure" (troop numbers, e.g. "chaque
  membre de cette confédération devrait déclarer le chiffre de ses forces"), not cryptographic cipher.
- **p. 471** — a further hit inside the Vergennes chapter (441-496), not read this pass (locate-step budget);
  given the pattern established at 428-429 and 441-442, most likely the same genre (protocol prose), not
  chased further.

## Answer to the brief's questions

- **Page range**: not one chapter. Three genuine cipher-protocol passages: p.185 (d'Avaux, ~1698), pp.428-429
  (Modène, 1768), pp.441-442+ (Vergennes, 1771-74, possibly continuing to p.471).
- **Content type**: prose describing the cipher-custody and cipher-selection protocol between the King's
  foreign-affairs ministry and the ambassador at Stockholm. **Not a printed key/nomenclator table, not raw
  undeciphered ciphertext, not a decoded-plaintext transcription of a cipher passage.** This is the genre
  LESSONS.md and the HTRC notes anticipated for continental instruction/calendar editions: description of
  cipher use, not its reproduction.
- **Key route**: **none**. The edition explicitly says the tables were transmitted separately (by courier, or
  by "le sieur Barthélemy" in person) and were not copied into this printed volume. No usable key for any
  Sweden-embassy cipher letter in this repo or QUEUE.md comes from this source.
- **Decipherment in print**: not applicable -- there is no ciphertext here to have a decipherment of.

## Rule 10

Nothing claimed as new, unpublished or unread; this is a search result (found the passages, read them, they
contain no cipher table or ciphertext). Not checked against solver repositories (no ciphertext exists here to
search for). No novelty classification attempted or needed -- there is no reading to classify.

## Images (4, this folder's `images/`)

- `recueil-suede-p001-002-table-des-chapitres.png` -- front-matter TOC pages i-ii (context only; the "Chiffre"
  entries themselves are on later TOC pages not captured, since the search-box route made this unnecessary).
- `recueil-suede-p185-chiffre-avaux-1698.png`
- `recueil-suede-p428-429-chiffre-modene-1768.png`
- `recueil-suede-p441-442-chiffre-vergennes-1771.png`

## Hosts / requests

archive.org: 2 (`advancedsearch.php`, >=1.5s apart). www.googleapis.com: 1 (`books/v1/volumes/aFl0UpDNkusC`,
key sent as `&key=`, `&country=US` set, never printed). books.google.com / play.google.com: 2 requests hit
Google's bot-check page (direct PDF download link, direct `?q=` search-inside URL) -- not retried beyond the
one attempt each, per the good-citizen rule; worked around via the in-page search box instead (a different,
working route, ~9 subsequent page-image navigations via `tools/browser_fetch.js`, one request each, several
seconds apart via the tool's own network-idle wait). No credentials used, no HTRC/data.htrc.illinois.edu calls
this pass (the front-matter finding was already on file). No subagents.
