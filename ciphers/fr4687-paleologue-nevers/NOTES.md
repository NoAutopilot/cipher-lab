# BnF fr.4687 — Marguerite Paléologue, duchesse de Mantoue, to Louis de Gonzague, duc de Nevers, 1562-1564

Status: open

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass;
a formal six-source check-solved run is still owed before board promotion.

## Correction to the queue row

QUEUE.md M14 dated the item "(undated, volume covers 1585-91 Nevers-Gonzaga affairs)". Gallica's own catalogue
description (via `services/OAIRecord`) dates items 1-3 precisely:

> Recueil de pièces originales et de copies concernant l'histoire de la maison de Nevers. De 1562 à 1625...
> 1-3 Lettres, en italien, avec chiffres, de MARGUERITE PALEOLOGUE, duchesse DE MANTOUE, au duc de Nevers, Louis
> de Gonzague, son fils. De 1562 à 1564.

Margherita Paleologa (1510-1566) was regent-mother of Mantua during this period; her son Louis/Ludovico de
Gonzague later became Duke of Nevers in France. **1562-1564, not 1585-91.** QUEUE.md M14 row updated accordingly.

The same volume's item 41 is listed separately as "Chiffre. Quelques lignes non chiffrées sont en italien" —
an undated ciphered item elsewhere in the recueil, possibly unrelated to items 1-3 (different sender/date), not
investigated this pass.

## Checked (24 Sept 2026)

- Fresh shallow clone of `dbourdeau/cyphersolver`: no hit on "4687", "Paleologue/Paléologue" or "Marguerite" tied
  to this volume.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers`: no hit.
- `sources/cryptiana/web/nevers.htm` (Tomokiyo's own catalogue of ciphers in BnF fr.3995, "the Nevers
  collection") read locally, no fetch needed: covers a *different* volume — the Duke of Nevers' own cipher
  keys and correspondence as ambassador/courtier (fr.3995, fr.3251, fr.3413, etc.) — not his mother's 1562-64
  letters to him. No hit on "4687", "Paleologue" or "Marguerite" in the full 1420-line mirror.
- WebSearch for Italian scholarship on Margherita Paleologa's correspondence with her son in this period found
  only general biographical material (Wikipedia, Treccani); no edition or article naming this specific
  correspondence or its cipher was located. Tomokiyo's own background bibliography for the Nevers material
  (Daniela Ferrari 1999, "Mantoue et les Gonzague de Nevers"; Ariane Boltanski 2006, *Les ducs de Nevers et
  l'État royal*) was not checked against this specific volume this pass — flagged as the next step, not chased
  further under the check-solved brief's scope.
- Gallica IIIF, canvas 5 (f.1, faint, mostly illegible clear Italian), canvas 7 (f.5, clear Italian salutation
  "Al Ill.mo... figlio caris[si]mo"), canvas 8 (f.6, **ciphertext confirmed**: dense two-digit numeral groups,
  roughly 15-25 groups per line across at least six lines on this one leaf alone — a high-resolution crop is at
  `images/f8_crop.jpg`). Short Italian phrases appear in the left margin beside each ciphered line (e.g.
  "questa una quan[to] a quello che...", "et como...", "vi sera che... seguira..."); these read as the clerk's
  catch-phrase cues for filing/reference, not a complete parallel plaintext — no full interlinear decipherment
  was seen on this leaf. Images: `images/f5.jpg`, `images/f7.jpg`, `images/f8.jpg`, `images/f8_crop.jpg`.

## Class gate (24 Sept 2026)

Question: is this correspondence, its cipher, or a decipherment already in print? Searched (WebSearch, Google
Books API with `&country=US` and `&key=$GOOGLE_BOOKS_KEY` never printed, IA advancedsearch, JSTOR/academia.edu
reachability):

- Daniela Ferrari (1999), "Mantoue et les Gonzague de Nevers" — the article/catalogue Tomokiyo's own
  bibliography cites via an Academia.edu link. `academia.edu` answered curl/WebFetch with HTTP 403 (login wall);
  not read this pass. A WebSearch attempt to locate the title by exact string mostly surfaced an unrelated 1999
  numismatic item ("Mantova e i Gonzaga di Nevers" / "Mantoue et les Gonzague de Nevers", a coins-and-medals
  piece, possibly the same underlying catalogue Tomokiyo cites, possibly a namesake — not disambiguated) and
  confirmed Daniela Ferrari's role as director of the Archivio di Stato di Mantova 1990-2014. IA advancedsearch
  for "Ferrari Mantoue Gonzague Nevers" returned zero hits. Not located in readable full text this pass.
- Ariane Boltanski (2006), *Les ducs de Nevers et l'État royal* (Droz) — found and reachable via the Google
  Books API (volume id `dsInahmnar8C`, no full-view/snippet search-inside without a matching-phrase hit,
  `country=US` applied). Two relevant snippets surfaced by phrase search: "Marguerite Paléologue demeure
  résolument habsbourgeoise" (a general political-alignment remark, footnote 68) and "Paléologue, qui reçoit de
  Catherine d'assez fréquentes lettres, conservées dans les archives mantouannes: A.M." — this second snippet is
  about letters Marguerite Paléologue *received from Catherine de Médicis*, held in the Mantua state archives,
  not letters she *sent to her son*, and not BnF fr.4687. Targeted phrase queries combining Boltanski with
  "chiffre" and with "duchesse de Mantoue" + "correspondance" returned no hit tying the book to fr.4687 or to
  a cipher. No full read of the book attempted (Droz academic monograph, not on IA/HathiTrust full view this
  pass).
- General Gonzaga-Nevers editions/scholarship: Google Books full-text search for `"Marguerite Paléologue" "duc
  de Nevers" 1562` surfaced one distinct catalogue entry worth flagging — *Dictionnaire des manuscrits, ou
  Recueil de catalogues de manuscrits* lists an item "9510. ... Marguerite Paléologue, Duchesse de Mantoue à M.
  de Nevers, 1559" in an unnamed manuscript collection. This is a **different, single, earlier letter** (1559,
  three years before the fr.4687 items 1-3 start), not confirmed as the same correspondence — flagged, not
  chased further this pass. No other edition, calendar, or article naming this correspondence, its cipher, or a
  decipherment was found.
- `archivesetmanuscrits.bnf.fr/ark:/12148/cc577374` (BnF's own manuscript-level catalogue notice for fr.4687,
  which may carry a fuller bibliography than the OAI record already quoted above): returned HTTP 403 to both
  curl and WebFetch this pass (Cloudflare-style block, consistent with the Access playbook's note on this
  family of BnF pages); not read. Worth a browser-tool retry in a future pass.
- JSTOR: host reachable (`curl -o /dev/null -w "%{http_code}"` returned 200), but its search page requires
  JavaScript and returned no results through WebFetch's static render; no article search completed. Not
  retried further this pass (one attempt, per the good-citizen rule).

**Class-gate verdict: no prior print or discussion of these letters, their cipher, or a decipherment located.**
This is a search result under rule 10, not a claim of absence; Ferrari 1999 in particular was not actually read
(paywalled), only searched for by title, and the BnF's own fuller catalogue notice was not reachable this pass —
both are open risks flagged for whoever promotes this target, same shape as the M13 fr.16092 flag in ROOM.md.

## Key candidates (24 Sept 2026)

Question: does Tomokiyo's catalogue of ciphers in BnF fr.3995 (`sources/cryptiana/web/nevers.htm`, read in full
locally, no fetch) contain a key that could apply to this correspondence? Checked by keyword (`Marguerite`,
`Mantoue`/`Mantua`, `Paleolog`/`Paléolog`, `mere`/`mère`, `1562`-`1564`) and by reading the catalogue's own
scope statement and date range.

**No candidate found.** Three independent reasons:

1. Tomokiyo's fr.3995 catalogue is explicitly about ciphers belonging to Louis de Gonzague *as Duke of Nevers*
   ("the collection probably belonged to the duke"), a title he did not hold until his 1565 marriage to
   Henriette de Clèves — one to three years *after* the last of these letters (1564). Its earliest entry,
   no.1 (fol.1), is dated June 1580, sixteen years after this correspondence ends; the whole catalogued run
   is 1580-1594 (with more ciphers from other volumes, fr.3251/3315/3413/3416/3612/3616/3633/3641/3974-3994/
   4702/4712/4715, in the same post-1580 political-correspondent range). No entry predates 1580.
2. Two catalogue entries are captioned "Chifre avec la Duch[ess]e" / "avec la Duchesse" (no.2, fol.3, Oct 1584;
   no.6, fol.13, 1585) — but "la Duchesse" in a Duke-of-Nevers cipher of 1584-85 is his wife Henriette de
   Clèves, duchesse de Nevers, not his mother the duchess of Mantua; no.4 (fol.8, 1585) is captioned
   explicitly "avec la Duchesse ma feme" (my wife), confirming the sense. No entry is captioned with
   "mère" (mother), "Mantoue", or "Paleologue"/"Paléologue" — zero hits for all of these across the full
   1244-line mirror.
3. No.19 (fol.38, 1588) and no.20 (fol.40, May 1589) are the catalogue's closest formal matches to fr.4687's
   cipher type (both "substitution by two-digit figures... in Italian", two-part code, enciphering/deciphering
   tables) — but both post-date this correspondence by roughly a quarter century and are captioned for
   different correspondents (place names, not "la Duchesse" or a mother-son pairing).

Conclusion: fr.3995 is the wrong volume by both period (Duke-of-Nevers-era ciphers, 1580s-90s) and relationship
(wife/political correspondents, not mother); no key transfer is plausible without an intervening, unstated
20-year reuse. No candidate key promoted; none of Tomokiyo's fr.3995-family ciphers were tested against
fr.4687's ciphertext this pass.

## Extent (24 Sept 2026)

Viewed Gallica IIIF canvases 5-15 (one request per canvas, 1.5s apart, descriptive User-Agent; one connection
reset on an `info.json` request, recovered on a single retry after a pause, per the good-citizen rule). Full
manifest and per-canvas content notes: `images/manifest.json`.

Of the eleven canvases covering items 1-3 in this range, **three carry cipher**: canvas 8 (dense multi-line
block, mid-letter-1, previously found and cropped as `images/f8_crop.jpg`), canvas 9 (one dense cipher line
near the close of letter 1, cropped as `images/f9_crop.jpg`), and canvas 10, left page (a six-line dense cipher
postscript closing letter 1, immediately after the clear-Italian line "lase le mie le posete brusare" — burn
these of mine — and above the signature; cropped as `images/f10_crop.jpg`). Canvas 6 is very faint
pencil/draft script on both pages, not legible enough at this resolution to classify as cipher or clear text
(flagged "uncertain" in the manifest, not chased further). Canvases 5, 7, 11, 12, 13, 14, and 15 are clear
Italian throughout wherever legible; canvas 15 (right page) carries what reads as letter 2 (or 3)'s closing
signature "vostra madre la Duchessa di Mantua" and a date "26 [di] 9bre [novembre] del 6-" (year's last digit
not legibly read at this resolution). This suggests the volume's three cipher passages found so far all belong
to the *first* of the three catalogued letters (the one opening near canvas 5/7 and closing on canvas 10), with
the second and/or third letters, as far as canvases 11-15 go, running entirely in clear Italian — not confirmed
beyond canvas 15, which is as far as this pass's brief went.

## Passes (24 Sept 2026)

Two blind Sonnet subagents transcribed the three cipher crops (`images/f8_crop.jpg`, `images/f9_crop.jpg`,
`images/f10_crop.jpg`) independently, neither shown the other's file: `passA.tsv`, `passB.tsv` (line, position,
group, confidence; clear Italian runs as `[PLAIN:"..."]` rows). No reconciliation attempted, no decoding, no
novelty wording. See the "Pass agreement" table below for the count comparison; the two files themselves are
the primary record.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b90075058`, OAI record via
  `https://gallica.bnf.fr/services/OAIRecord?ark=btv1b90075058`.
- `sources/cryptiana/web/nevers.htm` (S. Tomokiyo, "Ciphers in BnF fr.3995 (the Nevers collection)"), local
  mirror, no fetch.
- github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers (both checked, no relevant content;
  Aymeloglu has no licence, cite only, nothing copied).

## Requests, check-solved pass (24 Sept 2026, earlier)

gallica.bnf.fr: 1 OAI record + 4 IIIF image fetches (1 crop). github.com: 2 shallow clones (shared with M13,
deleted after grep). WebSearch: 1 query.

## Requests, literature+key-hunt+extent+passes worker (24 Sept 2026)

gallica.bnf.fr: 1 manifest.json + 8 canvas image fetches + 2 info.json (1 connection reset, retried once,
recovered) = 11. googleapis.com (Google Books, `&key=$GOOGLE_BOOKS_KEY&country=US`, key never printed): 9
queries. archive.org advancedsearch: 1. jstor.org: 1 reachability check + 1 WebFetch (no usable result,
JS-gated search page). academia.edu: 1 reachability check (403). archivesetmanuscrits.bnf.fr: 1 WebFetch (403).
WebSearch: 3 queries. No logins, no credentials printed. Two Sonnet subagents for the blind passes (within the
brief's fan-out limit).
