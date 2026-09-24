open

# To Paget (envoy to the Ottoman Porte), Dresden despatches with cipher postscript — TNA SP 105/60/121,135

QUEUE row: N36 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 105/60** (Levant Company series), items **/121** and **/135**:
- SP 105/60/121 (17/27 Nov 1693): "Folio 121. To Paget. Acknowledges letter from Constantinople, cover given
  in cipher, but has not [...]. Initial paras [hand of Plantamour]."
- SP 105/60/135 (1694): "Folio 135. To [? Paget]. Fragment, i.e. concluding portion of a letter giving details
  of... [hand of Plantamour]."
The TNA cataloguer's own note names **SP 106** (the small Miscellaneous Ciphers class, already touched by
N19's SP 106/40) as the expected home of the key and records it as **not found there** ("Key untraced in SP
106"). William, 6th Baron Paget, was English ambassador at Vienna 1689-92 and then Ambassador-Extraordinary
to the Ottoman Porte at Constantinople, arriving July 1693.

## Check-solved sweep (24 September 2026)

Six sources checked (Sonnet subagent, this worker's $10 cap). Per this run's host rules, the TNA Discovery
API was **not** called at all, including for the SP 106 key search the row itself recommends as the cheapest
next step — that step is gated on another worker (session_01JE9661cSHNoQDHEvtc2qQb, row-13 scoring) posting a
`done` line in ROOM.md, which had not happened as of this sweep.

1. **Editions.** No printed edition of Paget's outgoing Constantinople/Vienna correspondence was found by
   search (`"William Paget" ambassador Constantinople correspondence letters embassy 1693`, `"William Paget"
   ambassador Vienna Constantinople printed letters edition`) — his own papers are catalogued at SOAS (PP MS
   4, c.1684-1709, unpublished as far as this search went) and the Lexington Papers (vol. XX, ff.60-81b) hold
   related correspondence, but neither is a printed edition. **SP 105/60 is identified by web-search snippet
   (not fetched from TNA) as George Stepney's letter-book** for his mission to the Emperor and to Saxony — i.e.
   these are Stepney's out-letters *to* Paget at Constantinople from Vienna/Dresden, not the reverse. This
   matches `dbourdeau/cyphersolver`'s own `stepney/NOTES.md`, which independently states Stepney's
   letter-books are "TNA SP 105 (Archives of British Legations; Stepney's Vienna volumes c. SP 105/60-66)" and
   that SP 106 holds "the office's cipher templates of this type" — background on a *different* Stepney item
   (Vienna to Manchester, 23 Mar 1702, Yale OSB MSS fc37, verdict offline-only/unread there), not this pair,
   but it independently confirms a real, named "Mr. Stepney's cipher" existed (HMC 8th Rep. App. II p.85: a
   cipher was requested for a colleague in 1701 because "letters from Vienna were opened") and that his
   letter-books normally give plaintext.
   - Calendar of State Papers Domestic, William & Mary, vols 4 (1693, archive.org `calendarofstatep04grea_0`)
     and 5 (1694-95, `calendarofstatep05grea_0`), full-text searched via the archive.org fts API (no login):
     both calendar "Lord Paget" but only administrative entries — verbatim: "the allowance of the expenses of
     William, Lord Paget, ambassador to the Grand Seignior from Sept. 2nd" (v.4) and "Warrant for payment of
     extraordinary expenses of Lord Paget, Ambassador Extraordinary to the Grand Signor" (v.5). Nothing
     calendars SP 105/60 itself or any cipher content — expected, since CSPD Domestic draws on the SP 44 entry
     books, not the Foreign/Levant Company series.
   - "Plantamour": the one full-text hit in CSPD vol.4 ("Anne Plantamour and John Ugasse, her son") is an
     unrelated denization-list entry. A web-search snippet (TNA authority record, not fetched) names
     "Plantamour, Philip, (fl 1693-1704), Diplomat" — dates match the target exactly and this is probably the
     clerk named in the SP 105/60 catalogue note, but this is unverified beyond the snippet. Cross-target
     lead (24 Sept 2026, LANE S worker H, from the sp90-raby-whitworth-1705 BL sweep run this same pass): BL's
     `searcharchives.bl.uk` catalogue (Add MS 61142, "Vol. XLII... ff. 1-31b Philip Plantamour, agent in
     Berlin: Letters to Duke of Marlborough: 1702, 1703") independently confirms a "Philip Plantamour" active
     as a diplomatic agent/clerk in this same milieu (Berlin, correspondence with Marlborough) just a few
     years after our 1693-94 Dresden items — same given+surnames, plausibly the same person or a close
     relative, not yet checked against SP 105/60's own "hand of Plantamour" note; not fetched in full this
     pass (out of this target's assigned scope).
   - Google Books queries pending (this worker does not hold the slot): `"William Paget" Constantinople
     ambassador letters 1693`; `"George Stepney" Dresden Paget cipher 1694`; `"Lord Paget" "Grand Signor"
     correspondence Stepney`; `Lexington Papers Paget Constantinople 1694`; `"SP 105" Stepney letter-book
     Dresden Saxony`.
   - Tomokiyo/Cryptiana: `cryptiana.web.fc2.com/code/glorious.htm` ("Diplomatic Codes after the Glorious
     Revolution and Use of Printed Templates") fetched live — no mention of Paget, SP 105/60, Constantinople,
     Levant Company, Dresden 1693/94, or Plantamour. A site-restricted search and a local grep of
     `sources/cryptiana/` for "paget"/"SP 105"/"plantamour"/"levant company" returned zero hits.

2. **Community lists.** Web searches (`"Paget cipher" 1693 OR 1694 Dresden Constantinople Levant`, `"Paget
   cipher" Dresden Levant Company`, `"SP 105/60" Paget cipher Dresden Levant Company`) found nothing naming
   this item; no Cipherbrain/Cryptiana comment-thread hit.

3. **DECODE.** No login attempted (known broken). `sources/` and both solver-repo clones greped for
   "Paget"/"SP 105": no hits in `unsolved-ciphers/catalogue/decode-catalog.csv` or `decode-records.jsonl`. No
   DECODE record found for this item.

4. **Solver repositories** (both already cloned locally from an earlier worker's pass, reused rather than
   re-cloned). `dbourdeau/cyphersolver`: grep for "Paget" turns up only unrelated Paget/Pagett name matches
   (an sp53 1585 Morgan/Paget/Arundel key study, a stafford1586 "Charles Paget", OCR text in harley1582r8499)
   — none reference SP 105/60, Stepney-to-Paget, or 1693/94 Dresden/Constantinople. `stepney/` exists but is
   the unrelated, still-unread 1702 Vienna-to-Manchester item (README.md line 342: "Stepney → Manchester,
   Vienna | 1702 | Stepney's office cipher in TNA SP 105/106 or BL Add MSS 7058-78 | stepney/"). This item is
   not covered. `aaymeloglu/unsolved-ciphers`: zero "Paget" hits anywhere; no Stepney/Constantinople/SP105/SP106
   entries in TARGETS.md.

5. **General web search.** `"Paget cipher Dresden 1693"`, `"SP 105/60" cipher`, `"Plantamour" cipher clerk
   secretary 17th century`, `"Plantamour" Geneva Huguenot secretary diplomat 1690s` — no source ties a cipher
   key or decipherment to this item beyond the Plantamour-as-diplomat name-authority snippet above.

**Host requests this pass:** archive.org advancedsearch/metadata 4, be-api.us.archive.org fts 6, WebFetch 1
(cryptiana), WebSearch ~13 queries, GitHub 2 (no-op, repos already present). No TNA Discovery API calls, no
Google Books API calls, no DECODE login attempt, no Gallica/archivesetmanuscrits fetches.

## Verdict

**Status: open.** No printed edition, calendar entry, DECODE record, or solver-repository note names this
specific item, its plaintext, or its cipher key. CSPD only calendars Paget's embassy expenses, not this
correspondence. `dbourdeau/cyphersolver`'s unrelated 1702 Stepney→Manchester item confirms a distinct
"Stepney's own cipher" existed and that SP 106 is the expected class for this office's cipher templates —
consistent with, but not resolving, the cataloguer's own note that the key is untraced there.

**Google Books sweep (24 September 2026, LANE S worker H, holding the Google Books slot — key+country=US,
filter=full):** 5 queries run, >=2s apart. Two returned zero results: `"William Paget" Constantinople
ambassador letters 1693`; `"George Stepney" Dresden Paget cipher 1694`; `"SP 105" Stepney letter-book Dresden
Saxony`. Two returned real hits, both from **H. Manners Sutton (ed.), *The Lexington Papers: Or, Some Account
of the Courts of London and Vienna at the Conclusion of the Seventeenth Century*** (1851, several
archive.org/Google scans of the same edition): the table of contents lists "Lord Paget to Lord Lexington.
Death of the Grand Signor" and the body prints, verbatim, "Paget to Lord Lexington. Constantinople, Nov. 5,
1694. I cannot send such a relation as I would of the negotiation agitated here, but I am agoing to
Adrianople shortly..." — **this is a different correspondence channel from our target**: SP 105/60/121 and
/135 are letters *to* Paget (in Stepney's Dresden/Vienna letter-book, per the Editions section above), while
these Lexington Papers letters are *from* Paget, addressed to Robert Sutton, Lord Lexington (British envoy at
Vienna), not to Stepney. Same person (Paget), same exact months (Nov 1693-1695), wrong direction and wrong
addressee — not a match for either targeted item, but it establishes that a specialist printed edition of
Paget's Constantinople correspondence from this exact period exists and is on Internet Archive/Google Books
in full view, which the earlier general "no printed edition of Paget's outgoing correspondence" search did
not find. Worth a look for a future worker: the same volume's table of contents (page numbers only in this
snippet view) may also print letters *to* Paget from other correspondents in the same 1693-95 window,
including possibly Stepney — not checked this pass (out of scope: running the queries, not chasing every
lead to ground).

**TNA Discovery API sweep of SP 106 (24 September 2026, LANE S worker H).** Ran per this run's brief (the
row-13 scoring gate from the earlier pass is treated as cleared by the LANE S orchestrator's direct
assignment of this step). `tools/discovery_items.py "SP 106" "SP 106" <term>` for `Paget`, `Dresden`,
`cipher`, `key` — 4 calls, 3s apart, well under the 40-call cap. `Paget`, `Dresden` and `key` returned zero
records anywhere in SP 106. `cipher` returned all 67 items of the class (the term matches the series'
own boilerplate description, not this item specifically) — read in full: SP 106 is a chronological run of
named cipher/decipher tables by reign: Elizabeth I (106/1-3), James I (106/4), Charles I (106/5), **Charles II
(106/6, 1660 May 29-1685 Feb 6)**, then a gap, then **Anne to George II (106/7-9, 1702 Mar 8 onward)**. **No
item in the class covers 1685-1702** — the whole reign of James II and William & Mary, which includes our
1693-94 Paget/Dresden period, falls in a structural gap in SP 106's own coverage. This is a direct,
positive confirmation (not just an absence-of-search-term result) of the TNA cataloguer's own note on SP
105/60/121 that the key is "untraced in SP 106": there is no William & Mary-era cipher/decipher table in the
class at all, so no further term search within SP 106 can find one. Status unchanged (open) — this closes
the SP 106 branch of the search, it does not find the key elsewhere.

**Copy status:** no image of ff.121/135 seen this pass (catalogue text only) — remains a **TNA copy-order**
case; see REQUEST.md.

**Host requests this pass (LANE S worker H, 24 Sept 2026):** discovery.nationalarchives.gov.uk 4 (>=3s
apart); www.googleapis.com/books 5 (>=2s apart, key+country=US, never printed).
