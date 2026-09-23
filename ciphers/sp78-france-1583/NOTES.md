open

# France despatches, sibling folio catalogued "deciphered" in the same piece-run — TNA SP 78/111, SP 78/113

QUEUE row: N8 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

TNA, State Papers Foreign, France, **SP 78/111** and **SP 78/113**, The National Archives, Kew. Catalogue
text quoted verbatim from the Discovery API (`discovery.nationalarchives.gov.uk/API/search/records`, fetched
24 September 2026):

> SP 78/111/93 (1642 Sept 20/30): "Folio 212: **Letter entirely in cipher**."
> SP 78/111/135 (1644): "Folio 300: **Letter in cipher**."
> SP 78/113/57 (1657 Feb 24): "Folio 106: **Despatch largely in cipher from [Wm. Swyfte]**."
> SP 78/113/123 (1657 May 18/28): "Folio 189: **Letter mostly in cipher - deciphered**."

**Catalogue-date correction, established this sweep.** QUEUE N8's "What the catalogue says" cell and this
brief both describe the target as "1580s". The item-level covering dates above, taken directly from Discovery,
are **1642-1644 (piece 111, Civil War) and 1650-1657 (piece 113, Interregnum/Protectorate)** — not the
1580s. SP 78 runs chronologically from Henry VIII's reign to the 18th century across ~300+ pieces; piece 111
and piece 113 simply fall in the Civil War/Interregnum decades, not Elizabeth's reign. This is the same
class of scout-stage error the davaux-1633 sweep found (a date attached to the wrong item in a multi-item
description) — here it looks like the "1580s" guess was never checked against the pieces' own covering
dates before the row was written. **Consequence: the "Editions: CSP Foreign, Elizabeth, vols for 1583-84"
instruction in this brief is moot** — that printed calendar series covers only Edward VI through Elizabeth I
(ending 1589) and was never going to calendar Civil War or Protectorate French despatches. The relevant
printed source for piece 113 (1657) is Thurloe's State Papers (see point 2 below); piece 111 (1642-44) has
no comprehensive printed foreign-correspondence calendar for this reign at all.

## Check-solved sweep (24 September 2026)

1. **TNA Discovery, full item-description sweep (decisive for the "sibling decipher" question).**
   `tools/discovery_items.py` run against series "SP 78" with terms cipher/decipher/undeciphered/duplicate,
   filtered to each piece (8 requests: 4 terms x 2 pieces) — since Discovery's search matches full item text
   across the whole series and is then filtered by piece prefix, this returns *every* item in each piece
   whose description contains any of those words, which answers the brief's "which items are cipher without
   a deciphered note, and whether a decipher sits in the same piece" as completely as a full piece listing
   would, at a fraction of the request count. Results:
   - **SP 78/111**: 4 hits total — /58 and /61 ("Browne to Vane, and duplicate", nothing to do with cipher,
     the word "duplicate" is a false-positive match) and **/93, /135** (both cipher, neither "deciphered").
     No other item in the whole piece mentions decipher/undeciphered — **no sibling decipherment exists in
     piece 111** for either cipher item.
   - **SP 78/113**: 2 hits total — **/57** (cipher, no decipher note) and **/123** (cipher, already marked
     "deciphered" in its own catalogue text). No other item in the piece mentions decipher/undeciphered —
     **/57 has no sibling decipherment either**, and /123's "deciphered" note describes that item itself,
     not a separate paired item.
   Confirmed via the record-details endpoint (`/API/records/v1/details/{id}`, 6 requests: /93, /135, /57
   plus /123 already fetched for the sibling check) that **all four cipher items are `"digitised": false`**
   — none can be viewed online; a page-copy order is the only access route (rule 2, image over transcription,
   cannot be met without one).
2. **Print / scholarship.** No comprehensive printed calendar covers either piece (see the date correction
   above). For SP 78/113/57 (1657 Feb, Wm. Swyfte, France) specifically checked: Thurloe's *State Papers*
   (Birch, 1742, vol. 6 covers Jan-June 1657) is the standard printed source for Protectorate diplomatic
   intercepts and despatches and is on British History Online; WebSearch for "Swyfte" + Thurloe + 1657
   returned no hit naming him or this despatch, and `sources/cryptiana/web/thurloe.htm` (grepped for
   "Swyfte", "78/113", "France") has no match — Tomokiyo's Thurloe-cipher survey covers Montagu, Lockhart,
   Bampfield, Richard/Pawly and others by name but not Swyfte. Not conclusive (Thurloe's volumes were not
   opened page-by-page this sweep), so this stays a conditional gap, not a finding. WebSearch for SP 78/111
   1642/1644 turned up two unrelated TNA/journal items of interest for context but not this target: the
   TNA blog's Perwich cipher (SP 78/129, 1670 — solved 2025 by Matthew Brown/Lasry/Biermann/Tomokiyo, a
   different piece 18 pieces later in the same series) and a *Seventeenth Century* journal article on two
   June 1644 ciphers from Charles I's household to Prince Rupert "recently" broken — that article's letters
   are royalist domestic correspondence (intercepted by Parliament), a different catalogue context from SP
   78 (France, diplomatic), and were not confirmed to share a shelfmark with SP 78/111/135; treated as
   probably unrelated but not ruled out (title/abstract only, not read in full).
3. **Community lists.** `sources/cryptiana/web/` grepped for "SP 78", "78/111", "78/113": no hit anywhere in
   the 90-page cached snapshot.
4. **DECODE.** `ay/catalogue/decode-catalog.csv` grepped for "SP 78"/"SP78": no record.
5. **Bourdeau.** `cs-recheck` grepped for "SP 78"/"SP78": no hit in `CATALOGUE.md`/`SOLVED_CATALOGUE.md`
   or any target folder.
6. **Aymeloglu.** `ay/*.md` grepped for "SP 78"/"SP78": no hit.

Requests: discovery.nationalarchives.gov.uk 14 (8 term-searches + 6 record-details lookups; two earlier
attempts at a blank-query piece-level lookup returned HTTP 202/500 and were abandoned in favour of the
term-search approach, which is the same pattern `tools/discovery_items.py` already uses successfully).
WebSearch: 4 queries.

## Edition risk

**Open, not moot.** Neither piece has a comprehensive printed calendar for its actual period (Civil War/
Interregnum, not Elizabeth). SP 78/113/57's period (1657, France) has one plausible printed source
(Thurloe's *State Papers*) not yet checked page-by-page. SP 78/111 (1642-44) has no obvious candidate
edition at all — this raises rather than lowers its value as a target, since it is less likely to have been
calendared anywhere.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Two cipher items with no sibling decipherment and no
matching entry in DECODE, Bourdeau's or Aymeloglu's working lists, or Tomokiyo's site: SP 78/111/93 (1642,
"entirely in cipher") and /135 (1644, "in cipher"); one item with a sibling issue resolved rather than open,
SP 78/113/57 (1657, "largely in cipher", no decipher note, no sibling in-piece) conditional on Thurloe vol.
6 (pp. 15-208, Jan-Apr 1657) being searched for Swyfte's despatches. SP 78/113/123 (1657, "mostly in cipher
- deciphered") is **not** a fresh target: its own catalogue text says it already carries a decipherment, but
it is not digitised, so the decipherment's nature (interlinear on the same document, like Lorraine 377 and
Dupuy 155, or a separate translation) cannot be confirmed without a page copy. Not "new"; not "unpublished" —
this is a search result, not a discovery (rule 10).

## Thurloe check (24 September 2026)

Job: check Thurloe's *State Papers* vol. 6 (1657, covering Jan-June) for SP 78/113/57 (despatch "largely in
cipher from [Wm. Swyfte]", 24 Feb 1657), and vols. 1-2 for the SP 78/111 items (1642-44) if their senders
are named. Fetched item-details for /93 and /135 first (`discovery.nationalarchives.gov.uk` item-details
endpoint, 2 requests, ids C7327886/C7327928, already cached from the earlier sweep): **neither carries a
sender name** — /93 reads only "Folio 212: Letter entirely in cipher" and /135 only "Folio 300: Letter in
cipher", no `note` field, no person named — so the vols. 1-2 check does not apply (job E's own condition).

For SP 78/113/57: identified vol. 6 on archive.org (`collectionofstat06thur`, 1742 printing, not
access-restricted; advancedsearch + metadata, 2 requests). A direct djvu-text download failed with a
persistent HTTP 500 from the archive.org download endpoint on two attempts (not retried a third time, per
the good-citizen stop-on-repeated-failure rule); used the no-login `be-api.us.archive.org/fts/v1/search`
full-text index instead (4 requests), which is indexed for this item (a control query for "Cromwell" returns
1 hit, confirming the index covers this volume). **"Swyfte" (the exact TNA spelling): 0 hits.** "Swift": 1
hit, appearing twice in what looks like a single indexed page — "To mr. Martin Nodi, for so much paid w mr.
Swift sent September 18..." and "...lordship of what I spoke concerning mr. Swift, in relation to some
place about the other..." — both read as a financial/patronage reference to a "Mr. Swift," not as a
despatch-from-France dateline, and neither snippet carries a February 1657 date or a French context.
**Inconclusive but not a positive match**: this does not establish that Swyfte's despatch is printed in
Thurloe vol. 6; treated as not found.

## Next

**SP 78/113/57 stays unprinted** after the Thurloe vol. 6 check (no genuine match); status line unchanged.
Order TNA page copies for all four items — SP 78/111/93 and /135 (undigitised, no decipher sibling, no
edition candidate), SP 78/113/57 (undigitised, no sibling decipherment, Thurloe checked and negative) and
SP 78/113/123 (to see what "deciphered" means on the page before deciding whether it is a target at all, the
same check that resolved Lorraine 377 and Dupuy 155 this session). All four items are catalogueLevel 7,
digitised: false on Discovery — no image route exists without a copy order. REQUEST.md drafted this session
(see ciphers/sp78-france-1583/REQUEST.md) batching all four references; no order placed, no price guessed,
no email sent. Also unresolved: whether the Cobham/Bourbourg negotiations overlap flagged in the original
QUEUE N8 row (BL Harley 287) is real — not reconciled this sweep either, since it depended on the same
wrong 1580s date.
