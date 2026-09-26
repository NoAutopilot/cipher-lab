# D1-CHECK: Lettere di D. Giovanni d'Austria a D. Giovanni Andrea Doria I (1568-78)

Verdict: **NO -- notes only, no cipher digits found printed anywhere checked. Close D1** (per SCOUT-OWN-3-2026-09-26.md).

Not confirmed exhaustively (page images of the 108pp volume were never actually seen -- every route to them
was blocked, see Requests below); this is the strongest evidence obtainable without a human at a keyboard or
a working Google Books/Cloudflare bypass, not a page-by-page read.

Worker: parent worker D1-CHECK (Sonnet, session_01Dz4db29x1c4QzieeuJ7mwf), for the owner-account parent
(session_01FXDfYR3CvGk7tcid1Aav1n). Date: 26 Sept 2026, 12:45-12:55 UTC. Do NOT create a `ciphers/` target
folder for this item -- filed here in `_triage/` per the brief.

## The one question

Does *Lettere di D. Giovanni d'Austria a D. Giovanni Andrea Doria I [1568-78]* (ed. Prince Alfonso Doria
Pamphilj, Rome, Forzani, 1896, 108pp, Spanish) print any cipher groups (digits, symbols, numeral runs)
anywhere, or does it only carry the editor's inline notes ("cifra descifrada" / "cifra no descifrada")?

## What was found

Three distinct editorial marker phrases turned up in this volume via Google Books phrase search, all in
running prose with **no digits, symbols or numeral runs visible in any snippet window on either side of the
marker**:

1. `(cifra no descifrada)` -- p.90 per SCOUT-OWN-3's original find. Snippet (volume `9-ZcAAAAcAAJ`): "...
   cifra no descifrada . me marauillo mucho que le de pena la pobreza teniendo vn amigo tan rico como yo que
   si lo fuesse de hazienda como voluntad podria perder el cuydado de la hija , pero lo que haze al caso es
   regalar la cuñada , y yo..." -- continuous plain Spanish immediately after the marker, no break for digits.
2. `(cifra descifrada)` -- volume `c-GJNFDx2tUC`. Snippet: "... cifra descifrada ) mas es tanta la falta de
   dinero que no se puede encarecer con quanta dificultad se haze qualquiera pequena labor . El Conde de
   Xuacemberg embaxador del Imperador , que ha dias que estaua con el Archiduque Mathias y..." -- a second,
   independent phrase probe against a bordering clause (`"quanta dificultad se haze"`) extended this same
   window by another ~40 words (through "vino aqui seys dias a asaber si su M.d y yo en su nombre tendria...")
   with the identical text recovered from a **third** scan of the same edition (`fT3wFVKPRqMC`, confirmed by
   its own volume metadata to be the same 1896 Doria Pamphilj edition) -- still zero digits, ruling out a
   single bad OCR pass as the explanation.
3. `(cifra no adivinada)` [cipher not guessed/worked out] -- a third marker phrasing, not previously recorded
   by SCOUT-OWN-3, found in volume `9-ZcAAAAcAAJ`: "... cifra no adivinada . El Señor Principe se halla
   todauia a la parte de lemburg y Octauio a la de Mons . Juntarnos emos dentro de seys dias desta parte de
   la Mosa entre el Pays de lieja y Mastrich y de alli tomaremos la resolucion que el..." -- again, continuous
   plain prose with no digits.

All three markers behave the same way regardless of whether the passage is marked deciphered or not: the
running text reads straight through them as ordinary sentences. This is the editorial convention of *quoting
the note inline and continuing (or resuming) plain narrative*, not the convention (Thurloe / Stuart Papers /
Rikskansleren, per CLAUDE.md's own precedent) of printing the surviving cipher figures beside an
undeciphered-passage note. Four independent Google Books scan IDs of the same edition were checked
(`9-ZcAAAAcAAJ`, `c-GJNFDx2tUC`, `fT3wFVKPRqMC`, `QzIoAAAAYAAJ`; the fourth returned no snippet for the
queries run) -- consistent behaviour across scans, so this is not a single defective digitisation.

## Requests (this session)

- `www.googleapis.com/books/v1/volumes`: 8 queries, all `&country=US&key=$GOOGLE_BOOKS_KEY`, ~1.5s apart, one
  volume-metadata lookup (`/volumes/fT3wFVKPRqMC`).
- `books.google.com` text view (`pg=PA90&output=text`): 2 attempts (1 + 1 retry, ~3s apart, Chrome UA), both
  HTTP 403 with the site's own "Sorry" bot-block page -- same captcha wall SCOUT-OWN-3 hit on PDF/epub
  download; not retried further per the good-citizen single-retry rule. Combined with SCOUT-OWN-3's own two
  prior attempts (PDF 429, epub 200-but-captcha-HTML), this route is now 2-for-2 sessions blocked.
- `archive.org/advancedsearch.php`: 1 query (title search) -- 0 hits, no separate IA copy of this edition.
- `be-api.us.archive.org/fts/v1/search`: 1 query + 1 retry (~2s apart) -- both HTTP 502 (site-side, not a
  challenge or rate-limit); not retried further.
- `api.europeana.eu`: 2 queries (`wskey=$EUROPEANA_API_KEY`) -- found a **second, independent digitisation
  host not previously on file**: Biblioteca Virtual Miguel de Cervantes (cervantesvirtual.com),
  `ark:/59851/bmc417f7`, catalogued there as "Cartas de Don Juan de Austria", same 1896 edition, 97pp per
  their catalogue entry (vs. 108pp Google Books -- likely a front-matter counting difference, not a different
  print run; not verified further).
- `cervantesvirtual.com`: 2 curl attempts (http then https, browser UA, ~2s apart) both HTTP 403 with a
  JS/cookie wall; 1 attempt via `tools/browser_fetch.js` (headless Chromium) returned a Cloudflare "Just a
  moment..." interstitial, not cleared. **New host for the Access playbook table**: cervantesvirtual.com is
  Cloudflare-challenged to both curl and the headless browser tool here; add a row if a future session finds
  a working route (a real browser session with cookies persisted, or its own IIIF/API endpoint if one exists
  -- not searched for this pass).
- `catalog.hathitrust.org`: 2 requests (bibliographic API guess by a wrong OCLC number, and the HTML search
  UI) -- both HTTP 403, Cloudflare challenge page. Consistent with the Access playbook table entry
  (HathiTrust's own site is Cloudflare-blocked from the cloud); not a new finding, not retried further.
- Check-solved side (is this correspondence printed elsewhere with the cipher resolved?): 2 Google Books
  queries -- (a) `"Don Juan de Austria" "Giovanni Andrea Doria" cifra`: 1 hit, an unrelated 2003 secondary
  work (*Il Regno di Napoli e la difesa del Mediterraneo*) using "cifra" in the sense of a price/figure, not
  cipher, and not printing any decipherment; (b) CODOIN + "Don Juan de Austria" + Doria + cifra: 0 hits; (c)
  Fernández Duro *Armada Española* + Doria + "Don Juan": 0 hits. No prior print of a resolved cipher for this
  correspondence found by this search (a search result, not a novelty verdict -- rule 10).

Totals: googleapis.com 8+1, books.google.com 2, archive.org 1, be-api.us.archive.org 2, api.europeana.eu 2,
cervantesvirtual.com 3 (2 curl + 1 browser), catalog.hathitrust.org 2. All ≥1.5s apart, one host at a time, no
logins, no subagents (brief allowed at most 1, none needed).

## Key route (for the record, if this or a sibling target ever needs it)

Don Juan de Austria was formally appointed Captain General of the Sea in 1568, the same year this
correspondence opens. Philip II's general ciphers **Cg.4 (1567)** and **Cg.5/Cg.5bis/Cg.5ter (1568-69)** --
issued 6 August 1567 and 26 May 1568 respectively -- explicitly name recipients "the Captain General of the
Sea" by title (`sources/cryptiana/web/spanish3.htm` lines 306, 338, on file; both ciphers printed in Devos
(1950) and independently reconstructed by Tomokiyo). Giovanni Andrea Doria himself appears as a named
recipient of the Spanish crown's general ciphers in later decades -- **Cg.13 (1588-89)**, deciphered by
François Viète, and a bespoke two-party **cipher between Don Diego de Ibarra and Andrea Doria (November
1592)**, both per the same source (`spanish3.htm` lines 970, 1009, 1079-1081) -- establishing he was inside
the crown's cipher network from at least the late 1580s onward. No source on file documents a specific
Don Juan-Doria *particular* cipher for 1568-78 itself; if this correspondence was ever enciphered (which the
edition's own annotations say it sometimes was), the era's general cipher (Cg.4/Cg.5, or its successors
through the 1570s -- the spanish3.htm timeline runs Cg.4 through at least the 1580s) is the most likely
candidate rather than a unique two-party key, by analogy with the 1592 Ibarra-Doria precedent -- **inferred,
not confirmed**; grade M if ever used in a brief.

## Deliverable per the brief's three options

**NO -- notes only.** Close D1: no evidence of printed cipher groups was found after phrase-searching all
three of this edition's own marker phrasings across four independent scans, extending two of those windows
with bordering-clause probes, and finding zero digits throughout every window recovered. This is not a
full-volume read (blocked -- see Requests) so it is reported as a search result, not a certainty; a person
with a copy of the physical book, or a working route past the books.google.com/cervantesvirtual.com bot
walls, could still find a page this method missed. No LOCAL-QUEUE row filed: this does not need JSTOR,
HathiTrust full text, or any of the other local-runner-only hosts -- the blocking routes here
(books.google.com captcha, cervantesvirtual.com Cloudflare) are cloud-session bot walls of the kind the
Access playbook already tracks, not owner-account-credential gates, so a LOCAL-QUEUE row would not obviously
help; if the owner wants to spend a few minutes confirming this by eye, the cheapest route is
`play.google.com/books/reader?id=9-ZcAAAAcAAJ`, page ~90, in an ordinary logged-in browser.

No novelty wording used (rule 10) -- this is a print-format triage, not a reading, and no plaintext or
decipherment is claimed here.
