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
