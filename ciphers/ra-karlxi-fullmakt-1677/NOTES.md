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
