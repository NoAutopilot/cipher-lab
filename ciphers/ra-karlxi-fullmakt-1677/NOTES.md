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
