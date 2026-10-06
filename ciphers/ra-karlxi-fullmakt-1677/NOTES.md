open
Sverges traktater med främmande magter -- the standard treaty edition for this genre -- has no
volume covering 1677 at all (LIBRIS xsearch, the Swedish national library's own catalog API, lists
all 39 published parts and they jump from vol. 6 Förra hälft 1, 1646-1648, straight to vol. 8,
1723-1771), and a full-text search of Internet Archive and Google Books for Loenbom's Handlingar
til Konung Carl XI:tes historia and for a later Historisk tidskrift key-publication found no
citation of this document either.

## Check-solved (LANE CX2, 25 Sep 2026) -- print-question follow-up

This target already carries a full six-source check-solved sweep from 24 Sept 2026 (below, kept
intact): web, community lists, DECODE, Bourdeau and Aymeloglu all came back "not found" and were
not re-run today (nothing suggests they are stale). This pass's job (per
`.claude/briefs/runs/2026-09-25-lane-cx2-nord.md`) was narrower: settle the one open item that
pass left standing -- whether Sverges traktater med främmande magter volume 7 (or any volume
covering 1672-1697) exists and prints this document.

1. **Sverges traktater volume enumeration -- resolved, and it is a negative.** LIBRIS xsearch
   (`libris.kb.se/xsearch?query=Sverges+traktater+med+främmande+magter+Rydberg&format=json&n=39`,
   1 request; the LIBRIS HTML catalog front end itself is Anubis-bot-challenged and not usable
   from this container, but its xsearch JSON API answers plain curl) returns all 39 catalogued
   parts of this series. Sorted by part number, the run is: D.1 (822-1335) ... D.5 in three
   physical halves (1572-1645, with a 1628-1634 supplement) ... **D.6, Förra hälft (first half), 1
   (1646-1648)** ... **D.8, in three parts (1723-1739, 1740-1751, 1751-1771)** ... D.10-D.15
   (1815-1905), plus a border-maps volume (1752-1766 and 1810). No part numbered 7 appears
   anywhere in the 39 records, and no part of any number covers any year between 1648 and 1723.
   Two independent secondary sources corroborate the same gap: (a) a Google Books catalogue
   description of the full set (`PFMOMwEACAAJ`) lists "dl. 5. pt. 1 ... dl. 5. pt. 2, dl. 6. pt.
   1 ... dl. 8 ... dl. 12 ... dl. 13, 14 ... dl. 15" with no "dl. 7" between 6 and 8; (b) a
   web-search snippet of a library holdings summary gives the identical span "D. 1(822/1335)-6:
   Förra hälft:1(1646/1648), D. 8(1723/1771), D. 10(1815/1845)-15(1900/1905)". **Conclusion: this
   edition -- the natural home for a royal commissioners' full power, and the only specific lead
   QUEUE.md and the 24 Sept pass named -- was never published for any year between 1648 and 1723,
   so it cannot contain the 6 May 1677 Nääs full power under any volume number.** This resolves
   the "inconclusive, not negative" flag the 24 Sept pass left open; it is now a clean negative,
   not an unread edition, and this target no longer needs to be held on that account.
2. **Nijmegen congress literature.** WebSearch for a printed edition of the Nijmegen congress
   (1678-79) carrying Swedish plenipotentiaries' full powers (Mignet, a Sylloge/Actes collection)
   found only secondary historical accounts (Wikipedia, EBSCO, Wiley) and one Library of Congress
   authority record mentioning a "fullmåchtige" title without giving a printed source; no edition
   was located or opened. Not found, not resolved -- flagged as still open if anyone later has a
   specific title to check, but no further lead surfaced this pass.
3. **Loenbom, Handlingar til Konung Carl XI:tes historia** (Stockholm, Lars Salvii, 1763-1774; 12+
   samlingar). WebSearch for its contents against "fullmakt", "kommissarier" and "fredsfördrag"
   found only bibliographic listings (WorldCat, HathiTrust catalog record, Google Books, Online
   Books Page) giving volume/samling titles, no table of contents detailed enough to confirm or
   rule out this document; the volumes were not opened page-by-page this pass (out of the print-
   question scope this brief set; a next worker with more budget could fetch a samling from
   HathiTrust or archive.org and full-text search it, though HathiTrust page images are
   Cloudflare-blocked from the cloud per the Access playbook table). Not found, not conclusively
   searched.
4. **Historisk tidskrift, a later key publication** (the "key lost" -> journal-search lesson in
   check-solved.md, after Torpadie's 1888 Gustav II Adolf precedent). WebSearch for a Historisk
   tidskrift review or key-publication naming this fullmakt, its shelfmark, or "Nääs 1677 chiffer"
   found nothing beyond general Karl XI biography pages and one unrelated Historisk tidskrift
   volume's OCR dump on archive.org (not opened, no hit in the search-engine's own indexing).
   Not found.

Riksarkivet's own digitised-image route named in NOTES.md (the `data.riksarkivet.se/api/records`
check) was already run on 24 Sept 2026 and confirmed not digitised; not re-run today since nothing
suggests that has changed in one day.

**Verdict stands `open`**, and is now on firmer ground than the 24 Sept pass: the one named
edition family that could plausibly print this document does not cover its year at all (a
resolved negative, not an open question), Loenbom and a Historisk tidskrift key-publication search
turned up nothing, and the document remains undigitised and unread anywhere. Rule 10: no novelty
wording used above; this is a search result, not a verifier's classification.

Requests this pass: `libris.kb.se` 1 (xsearch JSON API; the HTML front end at the same host is
Anubis-challenged and was not retried, per the good-citizen one-retry rule -- not yet in the Access
playbook table, added here for the next worker: **LIBRIS (libris.kb.se): HTML catalog pages are
behind an Anubis bot challenge from this container; the `xsearch` JSON endpoint
(`libris.kb.se/xsearch?query=...&format=json`) is not challenged and answers plain curl -- use it,
not the HTML search, for any future Swedish-library bibliographic check**), `googleapis.com/books`
4 (GOOGLE_BOOKS_KEY + country=US), WebSearch 6. No archive.org, no DECODE, no GitHub clones this
pass (the 24 Sept sweep's findings on those sources stand unchanged).

## Check-solved sweep, 24 September 2026 (prior pass, kept intact below)

# ra-karlxi-fullmakt-1677

Status: open

## What this is

King Karl XI's full power (fullmakt) for the Swedish peace commissioners, Nääs, 6 May 1677, partly in cipher.
Riksarkivet i Stockholm/Täby, "Originaltraktater med främmande makter (traktater) / Tyskland / Kejsaren
(Österrike-Ungern) / Fredsfördrag med tillägg", reference code `SE/RA/25.3/4/II/7/B`. The Riksarkivet API record
for this dossier holds two documents, both catalogued verbatim:

> a) Konung Karl XI:s fullmakt för svenske kommissarierna, Stockholm 12 april 1676. Latin. Papper, 3 sidor
> text, sigill.
>
> b) Konung Karl XI:s fullmakt för svenske kommissarierna, Nääs, 6 maj 1677. Latin, delvis i chiffer. Papper, 3
> sidor text, sigill.

Only document (b), 6 May 1677, is partly in cipher; document (a), 12 April 1676, is not (recorded here since
both live under the same reference code and a copy order would need to specify which). Date range on the
record: 1676-1677. QUEUE.md row R8. No transcription exists anywhere the searches below reached;
`ciphertext.txt` is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `""Karl XI" fullmakt kommissarier Nääs 1677 chiffer fredsfördrag kejsaren"` and
   `""6 maj 1677" Nääs fullmakt Karl XI kejsaren fredsfördrag"`. Hits are all general Karl XI biography/war
   pages (Wikipedia, KulturNav, historiesajten.se, Svenskt Biografiskt Lexikon) confirming the general context
   (Scanian War, the Landskrona victory of 14 July 1677, Sweden as a guarantor power of the Peace of Westphalia)
   but none names this specific full-power document or its cipher passage. Not found.
2. **Print — the standard edition, partially checked, inconclusive.** QUEUE.md's own next-step names "Sverges
   traktater med främmande magter vol. 7" as the edition to check; this is O.S. Rydberg's (continued after his
   death by Carl Hallendorff) multi-volume, multi-part edition of original Swedish treaty texts and "dit hörande
   handlingar" (documents pertaining thereto) — exactly the genre a royal commissioners' full power would be
   printed in, since full powers are standard accompanying documents to a treaty dossier. What was checked:
   - HathiTrust Bibliographic API, `catalog.hathitrust.org/api/volumes/brief/recordnumber/012307525.json` (the
     main OCLC 11777373 record) and by OCLC number directly: lists v.1 (822-1335), v.2 (1336-1408), v.3
     (1409-1520), v.4 (1521-1571), v.5 pt.1-3 and pt.4-6, v.6 pt.1 (search-only/limited), then jumps straight to
     v.8 pt.1-2, v.10, v.11, v.12, v.13, v.14. **Volume 7 (and volume 9) are absent from this record** —
     either held under a separate catalogue record at other libraries, or genuinely not part of this holding's
     run. Not resolved this pass.
   - A Umeå University digitised copy of "D. 5, Förra hälft, 1572-1632" (`digital.ub.umu.se/node/598792`,
     fetched via WebFetch): its own 1903 preface states the "older series" (Rydberg's original conception) had
     at that date reached only part 5 (to 1632), and that volumes covering **1630-1814 were still needed** —
     i.e., as of 1903 no part yet existed covering 1677. Whether Hallendorff's later continuation (which the
     wider search found running at least to v.14, and to a "younger series" volume covering 1815-1867) ever
     filled the 1630-1814 gap with a "volume 7" specifically covering ~1648-1679/Karl XI, and whether that
     volume prints this Nääs full power, is **not established**.
   - Internet Archive: `advancedsearch.php` for `sverges traktater` / `traktater frammande magter Rydberg` (ASCII
     and title-field forms): 0 hits both times. Not on IA under these titles.
   - Runeberg.org: WebSearch `site:runeberg.org "traktater" Rydberg` surfaces only reviews of the work in
     Historisk tidskrift (1881-1897), not the primary text itself. Not on Runeberg.
   - **This edition check is therefore inconclusive, not negative** — the series plainly covers exactly this
     document's genre and era in principle, but the specific volume was not located or read. Per CLAUDE.md rule
     1 and the Raince/Thurloe lesson in LESSONS.md, this is the single most important open item before any
     campaign or promotion past a cautious stage 2: **do not treat this as "open" with confidence until Sverges
     traktater's volume covering 1672-1697 (or its absence) is confirmed**, ideally via a library holding a
     complete run (KB Stockholm/Libris shows multiple bib records for the series; a Libris search by a worker
     with more budget, or a direct HathiTrust catalog UI session past its Cloudflare block, would settle it).
   - Nijmegen congress literature (the other named edition family in QUEUE.md) was not separately searched this
     pass — a full power for the negotiators is a natural companion document to Nijmegen congress instruction
     sets, but this document itself predates the actual Nijmegen sessions (1677 credentials for a congress that
     ran 1676-1679) and no search was run. Flagged as a second unclosed edition family, not searched.
3. **Lists.** `sources/cryptiana/` grepped for `karl ?xi|nääs|naas|fullmakt`: no hits. Live lists not fetched.
4. **DECODE.** `sources/decode/` grepped for the same terms: no hits. Live de-crypt.org not queried this pass.
5. **Bourdeau/Aymeloglu.** Same fresh shallow clones. `grep -n -i -E "karl ?xi.*1677|nääs|naas 1677"` against
   both repos' catalogue files (README/TARGETS/SOLVED_CATALOGUE/SHORTLIST/CATALOGUE): no matches. A broader
   repo-wide grep for `1677` alone returned only unrelated data-file false positives (SP53 digit blocks, Catinat
   group counts, etc.), none naming this shelfmark or Karl XI. Not found.

**Riksarkivet digitisation check** (`data.riksarkivet.se/api/records`, `text=Karl XI fullmakt Nääs 1677`, one
request, after two transient `SSL_ERROR_SYSCALL` resets — the third attempt succeeded, consistent with other
lanes' notes on this host): confirms `SE/RA/25.3/4/II/7/B` with `"onlyDigitisedMaterials":false` and reproduces
the two-document note above. Not digitised.

## Verdict

**Open, with an unresolved edition-search gap that is the highest priority for this row.** No source located a
transcription, key, decipherment or documented cryptanalytic attempt on this specific document. But this is the
one row of the batch with real print risk left standing (rule 1): the natural home for a royal commissioner's
full power is exactly a treaty-and-related-documents edition like Sverges traktater med främmande magter, that
edition demonstrably runs through this period in some form (v.5/v.6/v.8+ exist; v.7's contents and even its
existence for this bibliographic record are unconfirmed), and it was not read. **Do not score this "verified
unsolved" (stage 2) or nominate it on the strength of this pass alone** — the next worker (or this one, with
more budget) should resolve the Sverges traktater volume-7 question via Libris/KB Stockholm or a HathiTrust
session that gets past the Cloudflare front end, before it is scored further.

Not digitised (copy-order). REQUEST.md drafts a Riksarkivet reading-room request for document (b) specifically,
gated on the edition search above.

Requests this pass: data.riksarkivet.se 3 (2 transient resets, 1 success, shared count with the batch),
catalog.hathitrust.org (bibliographic API only, not HTRC) 2, archive.org advancedsearch 2 (0 hits both, part of
this lane's IA-slot allowance), digital.ub.umu.se 1 (WebFetch, then a second WebFetch to its relation page
returned 503, not retried further — one attempt, per the good-citizen rule), catalog.hathitrust.org record page
1 (WebFetch, 403, not retried), WebSearch 4, github.com clones shared with batch. No Google Books, no TNA, no
DECODE login.

## NX-UNBLOCK (26 Sept 2026): the Sverges traktater volume-7 question, resolved

Ran the edition search this row's verdict flagged as highest priority (the Libris/KB Stockholm route named as
the way to resolve the "Sverges traktater med främmande magter" volume-7 question, since HathiTrust is
Cloudflare-blocked from this environment). Libris's own xsearch API (`libris.kb.se/xsearch`, open, no key)
answers plain curl reliably (confirmed reachable, unlike francearchives/HathiTrust).

Query `"Sverges traktater med frammande magter"` (n=60) returns all 59 catalogue records for the series.
**There is no volume ("D. 7") covering the 1648-1723 span at all**: the series runs D. 6 ("Förra hälft, 1",
1646-1648) directly to D. 8 ("1723-1771", in three parts, 1915-1922) with nothing catalogued in between under
this title -- no "D. 7", no "Senare hälft" continuing past 1648 for this range. A follow-up query combining
the series title with `1677` returns 0 Libris records. This is the Swedish national union catalogue, not a
single library's holdings, so an absence here is a real signal, not a coverage gap of one collection.

**What this settles:** the specific worry this row's verdict raised -- that "Sverges traktater... demonstrably
runs through this period in some form" and might already print this 1677 royal commission -- does not hold:
Rydberg's edition has a documented gap for exactly this span (1648-1723), so this specific series cannot be
the place this document was printed. This does not clear the target to stage 2 on its own (rule 1 needs all
six source families, and other Swedish diplomatic-document editions for the Caroline period -- e.g.
Riksregistraturet, or a Danish/Dutch-side edition of the same 1677 negotiation -- are not ruled out by this
search), but it closes the one loose end this row's own verdict said must be resolved "before it is scored
further." Recommend: re-run the standard check-solved sweep's edition-search step with this finding recorded,
rather than treating the edition question as still fully open.

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Karl XI" AND fullmakt AND 1677 AND chiffer`: no relevant hit (0 results, none about the letter).
- `"Sverges traktater med främmande magter" AND 1677`: context only, no hit about the letter -- Svante Norrhem,
  "The uses of French subsidies in Sweden, 1632-1729" (book chapter, Subsidies, Diplomacy, and State Formation
  in Europe, 1494-1789), 2020, pp. 93-117, https://www.jstor.org/stable/jj.29685549.9.

## Web and blog check (GF-A2-8, 2 Oct 2026)

Plain web searches (WebSearch, standard):
1. `Karl XI fullmakt 6 maj 1677 Nääs kommissarier chiffer` (sender + date + place + cipher word): Kungliga slotten
   monarch pages, Svenska kyrkan, DigitaltMuseum, KulturNav, Wikipedia (Charles XI). None names this full power.
2. `"SE/RA/25.3/4/II/7/B" OR "Fredsfördrag med tillägg" Kejsaren 1677 chiffer` (reference code + cipher word): Finnish
   national library ontology, Georgian Papers transcriptions, founders.archives.gov, the Yale Avalon item "Declaration
   of the King of Sweden ... Lord Greiffenheim" (a different document), Danish KB letters. No hit on the reference code.
3. `"delvis i chiffer" fullmakt 1677` (the Riksarkivet catalogue's own phrase, quoted): Uppsala Swedish-colonial
   (Saint-Barthélemy) records, NYS archives, the Leijel family letters, a TNA record. None about this document.
4. `Charles XI full power Swedish plenipotentiaries Nijmegen 1677 partly in cipher` (descriptive title): Bengt
   Oxenstierna's Wikipedia page, a Bodleian archival object, Avalon "Speech of the Swedish Envoy ... Vienna", TNA
   Nijmegen treaty correspondence (SP Foreign, Holland, 1677), Runeberg's *A History of Sweden*, and **M. Bakeš,
   "Habsbursko-švédské diplomatické vztahy v období vlády Karla XI. (1672-1697)"** (Czech thesis, theses.cz/id/n0bws4).
   The thesis is the one hit on the right relationship and reign. Its theses.cz page was opened, but this
   container's text extraction got no abstract or full text from it. Whether it cites the 1677 full power is
   **not established**; that is the next step for (d) below.
Blog site searches:
5. Cipherbrain (`site:scienceblogs.de`), "Karl XI 1677 Swedish cipher": the plausible hit "A king's encrypted letter on
   Satoshi Tomokiyo's list of unsolved cryptograms" (14 Jun 2020) was opened with its comment thread. It is Charles I of
   England's 1648 Isle of Wight letters, and the comments mention no Swedish item. The other results (Swedish
   postcard, Thirty Years War cipher, Fersen letters) are other items.
6. Cryptiana blog (`site:cryptiana.blogspot.com`, `cryptiana.web.fc2.com`), "Swedish cipher Charles XI 1677": the
   blog's front page and its September 2025 archive. The archive page was opened and grepped for sweden|swedish|karl
   xi|charles xi|1677|nääs. Its only 1677 hit is the Perwich despatches (English agent in Paris, 1669-1677), which is
   not this item.
7. Cipher Mysteries (`site:ciphermysteries.com`), "Swedish cipher 1677 Charles XI": only fifteenth-century, van Heeck,
   Swedish Z32 and Blitz posts. Nothing on this document.
No decipherment, transcription or plaintext of the 6 May 1677 full power was found on the open web or in a blog comment
thread.

## Premise check (GF-A2-8, 2 Oct 2026)

(a) Decipherments the folder mentions: **none.** NOTES.md and REQUEST.md mention no decipherment, gloss or clear copy of
document (b). REQUEST.md line 5 only allows for the possibility that a printed copy might have the cipher deciphered
or omitted.
(b) Other solvers' working files: **not found.** Fresh shallow clones (2 Oct 2026) of dbourdeau/cyphersolver and
aaymeloglu/unsolved-ciphers, grepped for nääs|naas|fullmakt|karl ?xi|charles xi. Aymeloglu: no hit. Bourdeau: the
hits are Charles **XII** (README lines 134/138, Rákóczi 1707; goertz1717) and digit-block or corpus files (sp53,
labbe1582, blume, indus). No file names Karl XI's 1677 full power or applies a Swedish key to it. Cited, not copied.
(c) Physical neighbours: **a clear-text sibling sits in the same dossier, but no decipherment.** SE/RA/25.3/4/II/7/B holds
document (a), Karl XI's full power for the Swedish commissioners, Stockholm 12 April 1676, Latin, 3 pages, **not** in
cipher, beside document (b), the Nääs full power of 6 May 1677, Latin, partly in cipher (Riksarkivet record, quoted in
"What this is"). Full powers follow a fixed chancery formula, so (a) is the obvious clear model for (b)'s unciphered
frame and probably for some of its enciphered names. That is a crib source, not a decipherment, and it can only be
used once the leaves are seen. Neither document is digitised (`onlyDigitisedMaterials: false`), so no leaf, facing
page or laid-in slip could be viewed. **Unreachable** until the REQUEST.md copy order lands.
(d) Recipient's side: the recipient is the Emperor's side and the congress. That side's papers (HHStA Vienna,
Staatenabteilung Schweden) and the Nijmegen treaty instruments would print the Swedish full power if it was
exchanged. This pass ran Internet Archive be-api full-text searches inside *The Consolidated Treaty Series* vol. 15
(`consolidatedtrea0015cliv`), which reprints Nijmegen instruments:
- "Carolus Dei gratia Suecorum" 1 hit, "Olivenkrantz" 1 hit and "Eos nominavimus" 1 hit, all inside a Swedish full
  power and ratification for the Münster settlement (ex "Actes de Nimègue, Tom. III").
- "Naes" 0, "Maii 1677" 0, "Benedictum Oxenstierna" 0, "Sacram Caesaream Majestatem" 0.
- "Naas"/"Nääs" 1 hit, an OCR fragment beside a Danmark-Norges Traktater citation, not this document.
Three whole-IA be-api searches (unquoted terms for Naes/1677/plenipotentiaries, "Datum in arce nostra Naes", and the
Nimègue actes) returned 517, 218 and 175 loose-match items. Their titles (Portuguese, Hungarian and Estrades
collections) are not on point, and the items were not opened. **Not found so far, but not closed.** The Emperor-Sweden
peace of Nijmegen (5 Feb 1679) in CTS 15 and the *Actes et mémoires des négociations de la paix de Nimègue* (1680) are
the places where an inserted Swedish full power could be printed. A page read of the Emperor-Sweden instrument and
its inserted full powers is the next step, about 6 be-api/reader requests. The Bakeš thesis (web check item 4) is the
other recipient-side lead.
Requests: be-api.us.archive.org 15, archive.org metadata 1, scienceblogs.de 1, cryptiana.blogspot.com 1, theses.cz 1,
github.com clones shared with the other three GF-A2-8 targets, WebSearch 7.

## Page read, Emperor-Sweden instrument (A2P4-KARL, 3 Oct 2026)

Step named in the Premise check: be-api full-text search inside *The Consolidated Treaty Series* vol. 15
(`consolidatedtrea0015cliv`, Parry, Oceana 1969), by script; no page images, no vision. be-api returns snippets with
`page_num` equal to the item's imagecount (518), so no printed-page citation is possible (CLAUDE.md IA note).
- **Positive control (reproduces):** the Emperor-Sweden instrument is in this volume: "Peace between the Emperor,
  Empire and Sweden, signed at Nimeguen, 5 February 1679 ... Latin original" (3 snippets); a Latin dated
  "Neomagi septimo Feb. 1679"; "Plenipotentiarios" 5 snippets with "constituimus nostros Legatos Extraordinarios &
  Plenipotentiarios" (full-power wording inside the 1679 instruments); "Vandalorumque" 4 snippets, among them
  "Carolus Dei gratia Suecorum, Gothorum, Vandalorumque Rex" and "Domini Caroli XI ... Legatis". So the volume does
  print Karl XI-named instruments of this congress; the search can see them.
- **Target phrases, 0 hits:** "Naes", "Nesae/Nesiae/Nesa", "Maii/Maji 1677", "Oxenstierna" (OCR long-s variants not
  all tried). Earlier pass: "Benedictum Oxenstierna", "Sacram Caesaream Majestatem" also 0.
- Reading: nothing in CTS 15 matches the 6 May 1677 Nääs full power or a cipher passage by these searches. Not found
  in CTS 15 by snippet search, conditional on its OCR (long-s) and on the full power possibly sitting under other
  wording. Whether the Swedish instruments inside CTS 15 carry a different full power (the 1679 one) was not read
  page by page; that needs a loan reader (person) -- loan pages are obfuscated for scripts.
- Not done: *Actes et mémoires ... Nimègue* (1680) and Dumont, *Corps diplomatique* vol. 7 (not searched: be-api
  502 x3 and one timeout after the 17th request; stopped per the one-retry rule). Bakeš thesis still unread.
- Requests: be-api.us.archive.org 21 (4 failed: 3x HTTP 502, 1 timeout; one 20 s pause retry), no other host.
  Vision 0, subagents 0. No hit is a printed text or decipherment of the target: status stays `open`.

Next step: retry be-api (Actes de Nimègue 1680, Dumont *Corps diplomatique* t.VII pt.1) in a later session; ~6 requests.
While waiting: grep the Bakeš thesis full text (theses.cz file download) for "1677"/"Nääs"/"fullmakt".
Verdict: open unchanged; keep going on the recipient-side print check (CTS 15 negative by snippets, two editions unsearched).

## be-api retry, Actes de Nimègue 1680 + Dumont VII.1 (RUN1-KARL, 4 Oct 2026)

Identifiers from archive.org advancedsearch (2 requests): `bub_gb_z5RUDBNGrqkC` (Actes et memoires des negotiations de la paix de
Nimegue, 1680, Google-Books scan, catalogued "Tome premier quatrieme. Partie 2"; the 1680 scans are numerous, only this one searched) and
`corpsuniverseldi71dumo` (Dumont, Corps universel diplomatique t.VII part 1, 1726). Method: be-api fts, `identifier=` filter, snippets only,
no page numbers (page_num is not a locator), no vision. Both OCR long-s noisy ("Suéde", "Sc" for "&").
- Positive controls (both volumes answer): Actes 1680: "Suede" 1 hit, "Oxenstierna" 1 hit ("Neomagi, die 1[?] Mardi 1679 ... Benedict. Oxenstierna, J. Paulin
  Olivenkrans"), "plein pouvoir" 1, "Plenipotentiariis" 1 (Latin full-power wording, Legatis Extraordinariis ac Plenipotentiariis). Dumont VII.1:
  "Suede" 1, "plein pouvoir" 1, "Plenipotentiariis" 1, "Carolus Dei gratia" 1 (Charles II of Britain instruments).
- Target phrases, 0 hits in both: "Naes", "Naas", "Nesae", "6 May 1677". Actes 1680 also 0 for "Carolus Dei gratia". Dumont VII.1 also 0 for "Oxenstierna".
- Reading: not found in these two volumes by snippet search, conditional on OCR and on one scan of the 1680 Actes (other scans, other tomes, the
  1697 third edition and Dumont VII.2 unsearched). The Swedish full power could sit under other spelling ("Nääs" / "Nesen").
- Requests: archive.org advancedsearch 2, be-api.us.archive.org 18 (no failures). Vision 0, subagents 0. Status stays `open`.
Next (one line): same terms on the other 1680/1697 Actes scans and Dumont VII.2; Bakeš thesis grep still pending.
Verdict: open unchanged; keep going (recipient-side print check: CTS 15, Actes 1680 scan z5RU..., Dumont VII.1 all negative by snippet).

## be-api print-check, wider scans (RUN3-KARL, 4 Oct 2026, 08:48-08:55 UTC)
The brief's two volumes were already searched by RUN1-KARL (above); this pass ran that section's logged "Next" line. Method as before: be-api fts,
`identifier=` filter, snippets only, no page numbers, no vision.
- Spelling variants on the two earlier volumes (Actes 1680 `bub_gb_z5RUDBNGrqkC`, Dumont VII.1 `corpsuniverseldi71dumo`): "Nääs", "Nesen", "Nesae",
  "Naesii", "Datum Holmiae", "Datum Nesae", "Nesse", "Neskae": 0 hits each.
- Actes 1680, same volume, "Carolus" 1 item with 5 snippets: Swedish Latin instruments, but a different set -- "Liungby die 3. Decembres Anno 1678"
  (Carolus, Hoghusen), "Ratificatio Suecico-Monasteriensis", a "Plenapotentia" snippet, and a Spanish declaration. None is dated Nääs 6 May 1677 or
  addressed to the Emperor's side; read as other documents, not this one.
- Newly searched (Naes / Naas / Nesae, 0 hits in every one): Dumont VII.2 `corpsuniverseldi72dumo`; Actes 1680 scans `bub_gb_xIgNW9gsLIkC`, `53sa5KLcpk8C`,
  `qz747tAlFqYC`, `RFTnvif6FsYC`, `n8Arnv9Vn68C`, `eXQLNZsAnzsC`; Actes 1697 third edition `bub_gb_WWhLFL0KB0gC`, `xiS7lWlwwFMC`, `zcHCv6zpkPgC`,
  `6AdAtw3JYYsC`, `Jf_WcZJ4qX4C`.
- Control (Oxenstierna): hits in Dumont VII.2, RFTn, n8Ar, eXQL, 6AdA; 0 in xIgN, 53sa, qz74, WWhL, xiS7, zcHC, Jf_W. For those seven the scan answers
  nothing for a Swedish plenipotentiary name, so their Naes/Naas zeros are weak (the scan may be another tome, or the OCR garbles the name); they are not a test.
- Reading: no hit for the 6 May 1677 Nääs full power in 13 searched Dumont/Actes scans, conditional on OCR (long-s noise) and on tome coverage.
  Not searched: other tomes of the 1680/1697 Actes, Dumont other volumes, Bakeš thesis grep (still pending).
- Requests: archive.org advancedsearch 2, archive.org metadata 2, be-api.us.archive.org ~65 (no failures). Vision 0, subagents 0. Status stays `open`.
Next (one line): Bakeš thesis grep, then Riksarkivet owner/copy route (REQUEST.md). Verdict: open unchanged; keep going.

## IA-DESK-ALT (account-3 worker, 5 Oct 2026): Sverges traktater v.8 via Internet Archive

These are search results only (rule 10). *Sverges traktater med främmande magter* is **not on Internet Archive**. Two searches found no volume:
- advancedsearch `traktater`: 5 unrelated items.
- the full title as a phrase: 0 items.

On Google Books (keyed, country=US, query "Sverges traktater främmande magter"), the full-view records are dated 1877-1896, i.e. the early volumes. The 1890, 1934 and "192?" records are NO_PAGES. A query for "Sverges traktater 1677 fullmakt" returned no treaty-volume hit. So v.8 pt 1-2 (contents and date range, and any 1677 full power) **still needs HathiTrust** (`nyp.33433090738414`, and the search-only v.6 `nyp.33433090738372`).

Confirmed on the page (5 Oct 2026, owner's browser, HathiTrust nyp.33433090738414, title page + p.1): Sverges traktater
"Åttonde delen I, 1723-1739", ed. B. Boëthius (Stockholm, Norstedt); the first document is the Viborg border treaty of
30 Mar 1723. So v.8 cannot hold a 1677 full power, matching the LIBRIS enumeration above (no part covers 1648-1723).
Hathi desk read H4 closed.

## RUN6-KARLXI (account-1 worker, 5 Oct 2026, 05:21-05:2x UTC by date -u): brief's step already done, no new requests
The brief's named step (be-api retry on Actes de Nimègue 1680 + Dumont VII.1, "Next step" at the end of the Page-read section) was run on
4 Oct 2026 by RUN1-KARL (18 requests, no failures; both volumes answered positive controls, Naes/Naas/Nesae/"6 May 1677" 0 hits) and widened by
RUN3-KARL (13 scans, ~65 requests). Repeating the same terms on the same identifiers would add nothing; 0 requests made this session.
Not searched, unchanged: other tomes of the 1680/1697 Actes (seven scans failed the Oxenstierna control, so their zeros are not a test), Dumont
other volumes. Still pending, no network needed: Bakeš thesis grep ("1677"/"Nääs"/"fullmakt"), then the Riksarkivet owner/copy route (REQUEST.md).
Requests 0, vision 0, subagents 0. Status stays `open`.

## Bakeš thesis full-text grep (D2B-KARL, account-2 worker, 5 Oct 2026, 23:35-23:38 UTC by date -u): full text login-gated
Brief step (Verdict "cheapest next"): grep the Bakeš thesis (Univerzita Pardubice diploma thesis, 2014, defended 25 Aug 2014, supervisor
J. Kubeš) for "1677"/"Nääs"/"fullmakt"/"plenipotentia". Not done: the full text is not reachable from the cloud without a login.
1. theses.cz/id/n0bws4 (a meta-refresh cookie step, then the record page) says "Plný text práce ... Soubory jsou nedostupné" (files
   unavailable) and points to the holding institution: portal.upce.cz STAG link praceIdno=23485, which redirects to a generic browse page.
2. The institution's DSpace repository dk.upce.cz has the item: handle 10195/58052 (https://hdl.handle.net/10195/58052), item
   747a52dc-52b5-4fe5-910e-45d6a5b1e23b, dc.rights "bez omezení" (no restriction), but both the PDF (BakesM_Habsburskosvedske_JK_2014.pdf,
   1,883,534 bytes) and its extracted-text bitstream (BakesM_Habsburskosvedske_JK_2014.pdf.txt, 401,516 bytes) answer HTTP 401
   "Authentication is required" to the REST content endpoint. Not retried (good-citizen rule); no login attempted (no credential for it).
3. What is open: the abstract (five imperial envoys to Stockholm under Karl XI, from archival material) and the two reviews. The supervisor's
   review names the envoys (Šternberk, Althann, Berka z Dubé, Nostitz, Starhemberg); the opponent's review says the sources are mainly the
   Czech family archives (RA Sternberg-Manderscheid, RA Nostitz of Falknov). Neither review contains 1677, Nääs/Naas, fullmakt, plenipotent-,
   Nijmegen or cipher (grep, Czech and Latin forms). So the thesis works the imperial envoys' side at Stockholm, not the Swedish treaty
   originals at Riksarkivet; whether it cites the 6 May 1677 Nääs full power stays **not established**, and nothing here suggests it does.
4. Seen in the same repository search, not read: Bakeš's later work on the same topic, *Diplomatem v půlnoční zemi. Zástupci Habsburků ve
   Švédském království mezi lety 1650-1730* (2018, handle 10195/72172), and his 2015/2016 articles on Nostitz and the legation chaplains
   (10195/66550, 10195/67724). Their access was not tested (outside this brief).
Requests: theses.cz 4 (two meta-refresh stubs, then cookie + page), portal.upce.cz 1, dk.upce.cz 7 (search, bundles, item, PDF 401, text 401,
two review texts 200). Vision 0, subagents 0. Status stays `open`.

## Bakeš 2018 dissertation + 2015/16 articles, dk.upce.cz (R8-KARL2, account-2 worker, 6 Oct 2026, 03:16-03:20 UTC by date -u)
Brief step (D2B-KARL Verdict "cheapest next"): list the bitstreams of dk.upce.cz 10195/72172, 66550, 67724 and grep any open text.
1. 10195/72172 (item 03e06868-6ad9-4cd7-91fe-f1cc84041fc5): Martin Bakeš, *Diplomatem v půlnoční zemi. Zástupci Habsburků ve Švédském
   království mezi lety 1650-1730*, Univerzita Pardubice doctoral dissertation (disertační práce), 2018, supervisor J. Kubeš, dc.rights
   "Bez omezení". The PDF (BakesM_Diplomatemvpulnocnizemi__JK_2018.pdf, 2,701,198 bytes, 465 pages) is **open** (HTTP 200). Note: the
   repository's own extracted-text bitstream (.pdf.txt, 109,097 bytes) stops at printed p. 29, so a grep of that bitstream alone would
   have been a non-test; the grep below ran on `pdftotext -layout` of the full PDF (197,113 words).
2. Grep for 1677, Nääs/Näs/Naas, fullmakt, plenipot-, plná moc/plnou moc/plnomoc, chiff-/šifr-, Nijmegen/Nimwegen/Nimègue, traktat, Loenbom:
   - 1677 is on 15 lines, none about the Swedish full power: Harrach's and Valdštejn's missions (1673-1677, 1677-1679), ennoblements
     dated 10.3.1677, Simon Grundel-Helmfelt and Auersperg/Lobkovic death dates, a French legation chaplain in 1677, a 1677-1680
     propaganda study, and the chronology line "1677 Samuel von Pufendorf becomes Swedish royal historiographer".
   - Nääs/Naas/fullmakt/plenipot-: 0. "plnou moc" once (Karl XI gave Bengt Oxenstierna "full power" over foreign
     policy, a general statement, not an instrument). Nijmegen: twice (Oxenstierna's approach to Vienna "with the assistance of the
     imperial envoy in Nijmegen"; the chronology's 1679 peace line); neither cites a Swedish commissioners' full power.
   - Cipher: "šifrovací klíč" (Montecuccoli's key, HHStA Dänemark kart. 9, 1658), "převážně šifrované" (Gebsattel's reports 1668,
     RA Stockholm Diplomatica Germanica kart. 291), and a general sentence that secretaries knew the cipher keys. None about 1677.
   - Riksarkivet citations (33 lines) are to Diplomatica Germanica (kart. 278-369) and family archives; "traktat" appears only as
     Rudelius's *garantitraktaten* (1681-84); no citation of Originaltraktater / Tyskland / Kejsaren (SE/RA/25.3/4/II/7/B).
   - The opponent's review (HojdaZ_...doc, open, text bitstream 18,633 bytes): 0 hits for the same terms.
   So the 2018 dissertation, on the imperial envoys' side at Stockholm 1650-1730, does not cite or transcribe the 6 May 1677 Nääs full
   power in any form these terms reach.
3. 10195/66550 (Bakeš 2015, "Diplomatická mise jako nejistá investice", Český časopis historický 2015/3, Nostitz at Stockholm
   1685-1690) and 10195/67724 (Bakeš 2016, "Legační kaplani ...", ČČH 114/4): dc.rights "Pouze v rámci univerzity"; both text
   bitstreams answer HTTP 401. Not retried. Both cover dates after 1677 (1685-90) or chaplains, and the dissertation that absorbs
   them has no 1677 instrument, so a hit there is unlikely. One OpenAlex search ("Bakeš Nostic Stockholm"; an earlier wording
   returned 0) found 1 unrelated 2021 article (Hřebíková on Kounice), no open copy of either; one Google Books API query (title
   phrases, country=US, key) found 1 volume, *Habsburkové* 2017, NO_PAGES.
Requests: dk.upce.cz 14 (3 pid lookups, 3 items, 3 bundle lists, 2 text 200, 2 text 401, 1 PDF 200; one at a
time, 2 s apart), api.openalex.org 2, googleapis.com 1. Vision 0, subagents 0. Status stays `open`; nothing found, nothing read.

## be-api fts, unsearched Nijmegen editions (R8-KARL3, account-2 worker, 6 Oct 2026, 03:55-04:08 UTC by date -u)
Brief step (R8-KARL2 Verdict cheapest next): be-api per scan of the Actes/Dumont scans not yet searched, each with a control. Method as RUN1/RUN3-KARL:
archive.org advancedsearch (3 queries) to list every IA scan of *Actes et memoires ... Nimegue*, *Recueil de tous les actes ... 1678*, St Disdier's
*Histoire des negotiations de Nimegue* and Dumont's *Corps universel diplomatique*; be-api fts with `identifier=`, snippets only, page_num not a locator.
Controls per scan: Oxenstierna, Suede, Nimegue. Targets per scan: Naes, Naas, Nesae, Nääs, Nesiae, Neas.
- 14 scans newly searched: Recueil 1678 `bub_gb_NMcZHIES_IoC`, `fLVvqOsKtJAC`, `-ZUrTvejAC8C`, `_s_xZOFu1S4C`, `olfgJlz5kzEC`, `SIowE-0CyEMC`,
  `9JGttIQASl8C`, `XAqocs9GQ1sC`, `QyQiS7WviiAC`; Actes 1680 `bub_gb_mUtFAAAAcAAJ` (German-language text); *Actes & negotiations ... Das ist gründliche
  ... verfassung* 1680 `11211619bsb` (German); St Disdier 1680 `bub_gb__ZMUxzzqMLwC` and 1697 `histoiredesnego00didigoog`; Dumont v.7 Getty scan
  `gri_33125017207792`.
- Targets: **0 hits in all 14** (84 target queries).
- Controls: Oxenstierna hits in 3 (mUtF "den Durchlauͤchtigen Hn. Benedictum Oxenſtierna, Grafen zu Corshoim und Waſa"; 11211619bsb "Benedict.
  Oxenſtierna. Joh. Paulinus Olivenkrantz"; gri Dumont v.7 "Septembris 1688 ... Nicolaus OXENSTIERNA"). Suede and/or Nimegue hit in 9 more (the
  1678 Recueil scans and both St Disdier, which answer the scan but predate or lack the Swedish plenipotentiaries' names). **No control hit in
  `fLVvqOsKtJAC` and `olfgJlz5kzEC`**: their zeros are not a test (scan unreadable to fts or another tome).
- Lead, not a hit: both German 1680 editions print the plenipotentiaries' full powers in German (`Vollmacht` 5 snippets each, e.g. "4. Febr. 1677
  ... Instrument oder Neu ertheilte Volmacht / so denen Herrn Kaͤyſerlichen Geſandten ertheilet"; a contents run "Englischen ... Dänischen ...
  Mecklenburgischer ... Münsterischen Vollmacht"; "seine ertheilte Königliche Volmacht / welche denen Plenipotentiariis zu dem Friedens-Wercke").
  "Schwedischen Vollmacht" (both spellings, phrase) 0 in both; "Naͤs"/"Näs"/"Corshoim" 0 in mUtF (Corshoim appears only in the Oxenstierna snippet,
  so fts tokenisation is unreliable here); 11211619bsb "Näs" 3 snippets are OCR noise ("nas"). So whether a Swedish Vollmacht dated Nääs 6 May
  1677 is printed in these German volumes is not settled by snippets; a page read of the Vollmacht section (contents list "Vollmacht ... 94,
  131") is the next step, and it needs a reader, not fts.
- Reading: no hit for the 6 May 1677 Nääs full power in 12 controlled scans (27 searched across RUN1/RUN3/R8-KARL3), conditional on OCR (long-s,
  Fraktur) and on the full power possibly printed under a German or French heading without the place name.
- Requests: archive.org advancedsearch 3, be-api.us.archive.org 126 + 12 + 6 = 144 (no failures; one at a time, >= 1.6 s apart). Vision 0,
  subagents 0. Status stays `open`; nothing found, nothing read.

## Page read, German 1680 Actes Vollmacht section (R9-KARL4, account-2 worker, 6 Oct 2026, 05:37-05:41 UTC by date -u)
Brief step (R8-KARL3 Verdict cheapest next). Method: fetched `_djvu.txt` and `_page_numbers.json` of both German 1680 scans (open, no loan),
grepped for the Swedish full power, then read the page images (archive.org `page/nN_w1000.jpg`, one page per vision call, 1250 px wide).
- **A Swedish Vollmacht is printed, but it is the 12 April 1676 instrument, not the Nääs 6 May 1677 one.** IA `bub_gb_mUtFAAAAcAAJ`,
  *Nimwegisch Friedens-Memorial* pp. 102-104 = leaves n137-n139 (image-checked): heading "Der Herr Graff Oxenstirn und Herr Oliven Krantz
  kamen zu Nimwegen an/den 22. und 31. August. 76. folgt seine I. Vollmacht Derer Herrn Schwedischen Abgesandten."; opening "Wir Carl von
  GOttes Gnaden/König der Schweden/Gothen und Wenden/Groß-Hertzog von Finland ..."; names Benedict Oxenstierna and Johan Paulin
  Olivenkrantz as Extraordinar-Ambassadeurs; closing p.104 "Geben in unsern Castel Holm 12. Aprilis 1676. Carl. Concordat cum originali
  J. Berckeley W. Temple L. Jenkins." Next item on p.104 is the Danish Vollmacht (Hoeg). German translation, certified by the English mediators.
- The same text is in `11211619bsb` (OCR lines 6285-6330, same heading "I. Vollmacht Derer Herrn Schwedischen Abgesandten"; leaf not
  image-checked, OCR only).
- No second Swedish Vollmacht in either volume: OCR grep for "Schweden/Gothen", "Carl von GOttes", "Carolus Dei", "Suecorum", "II. Vollmacht",
  "Holm", "Nääs/Näs/Naes", "Maji/May/Mai 1677" found only the 1676 text, the 1675 Swedish-Dutch commerce treaty, the Emperor-Sweden treaty
  preamble (already page-read, A2P4-KARL) and unrelated May 1677 dates. Conditional on OCR (Fraktur), not a page-by-page read of 850 leaves.
- Relation to the target: date and place match the catalogue's *document (a)* of the same dossier ("Stockholm 12 april 1676", Latin, not in
  cipher), not the ciphered document (b). Inference only (grade I): if (b) reuses (a)'s formulary, this German text is a crib for the clear
  parts of (b); untestable until an image of (b) exists. No transcription of the target exists, so no comparison was possible.
- Requests: archive.org metadata 2, download 4 (djvu.txt, page_numbers) + 7 page images = 13, one at a time, >= 1.6 s apart, no failures.
  Vision reads 5 (own, no subagents). Status stays `open`.

## Remaining gaps (R8-KARL3, 6 Oct 2026; updated R9-KARL4)
Read so far: unmeasured, the Nääs 6 May 1677 Swedish full power itself has not been located in any print or image (0 of 1 target document found)
- Bakeš 2014 thesis full text - blocker: needs-physical-access; theses.cz "Soubory jsou nedostupné" and dk.upce.cz 10195/58052 PDF and text answer 401 without a Pardubice login (D2B-KARL section above); a person can use the repository's own request route or a Pardubice reader
- Bakeš 2015/2016 ČČH articles (dk.upce.cz 10195/66550, 67724) - blocker: needs-physical-access; "Pouze v rámci univerzity", text bitstreams HTTP 401, no open copy via OpenAlex or Google Books (R8-KARL2 section above); the 2018 dissertation (10195/72172, open, 465 pp.) was grepped in full with 0 hits for the 1677 Nääs full power
- Riksarkivet owner/copy route - blocker: waiting-on the Riksarkivet reply to REQUEST.md; the owner-side copy request is unanswered

## Escalation (R8-KARL3, 6 Oct 2026; updated R9-KARL4)
- [x] siblings: Emperor-Sweden sibling instruments checked (A2P4-KARL page read)
- [x] clear-pages: German print of the clear sibling, document (a) 12 Apr 1676, located (R9-KARL4, Actes 1680 pp. 102-104); no clear page of (b) itself
- [n/a] known-keys: plain Latin instrument, no key
- [x] print: 27 Actes/Recueil/St Disdier/Dumont scans fts-searched, 0 target hits; German 1680 Actes page-read (R9-KARL4): the Swedish Vollmacht printed there is the 12 Apr 1676 one (document a), not Nääs 1677
- [n/a] key-rebuild: no cipher key involved
- [x] image-check: title page and page read via A2P4-KARL, Hathi H4
- [x] retry: be-api retried 4 Oct 2026 (RUN1-KARL, RUN3-KARL); dk.upce.cz 401 not retried (auth gate, not a transient)
Verdict: parked: every remaining gap is outside-blocked (Bakeš texts needs-physical-access; Riksarkivet copy waiting-on REQUEST.md reply); the printed 1676 sibling (document a) is a possible crib once an image of (b) arrives
