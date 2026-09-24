open

# Yorke to Bedford: Albemarle's appointment, the Townshend answer, and Tobago's return, partly in cipher — TNA SP 78/232/44

QUEUE row: N51 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 78/232/44** (State Papers Foreign, France), folio 103, 1749 Mar 8/20.
TNA Discovery record detail (fetched fresh, 24 Sept 2026, Discovery id C7340425): scope description "Folio
103: Yorke to Bedford. Albermarle's appointment is welcomed. The answer about Townsend is enclosed. Tobago
has been refused to Saxe. Date and place: 1749 Mar 8/20 Paris." — **the "partly in cipher" statement is a
separate catalogue field, `note: "Partly in cipher."`, not part of the scope-content description text**; a
plain full-text search on "cipher"/"decipher" against the piece therefore does not reliably find this or
sibling items (see caveat below). `digitised: false`. Joseph Yorke (later Baron Dover) was secretary to the
embassy in Paris under the Duke of Bedford, Secretary of State for the Southern Department; the letter concerns
the Aix-la-Chapelle peace settlement's colonial disputes (Tobago, the neutral West Indian islands) and the
Earl of Albemarle's appointment as ambassador.

## Check-solved sweep (24 September 2026)

Six sources checked directly by this worker (Sonnet, no subagents — TNA Discovery and archive.org calls made
directly under this run's host list).

1. **TNA Discovery, siblings.** `tools/discovery_items.py "SP 78" "SP 78/232" cipher decipher` (and a wider
   run adding Yorke/Bedford/Townshend/Tobago as terms) returned dozens of items in the piece, but **none of
   their scope-content descriptions actually contains the word "cipher" or "decipher"** — confirmed by
   inspecting the tool's own `cipher_sentences` column, blank throughout. This means Discovery's full-text
   search is matching on the piece's *note* field (or other indexed text) rather than the description, and a
   `cipher_sentences`-style filter on description text alone will miss every "partly in cipher" item in this
   piece, including this one. **Caveat for any future worker searching SP 78/232 for cipher siblings: check
   the `note` field of each candidate record directly (`/API/records/v1/details/<id>`), not just the
   description returned by a keyword search.** No sibling item's `note` field was individually checked this
   pass beyond the target itself (out of budget: ~150 items in the piece); this is a genuine gap, not a
   clearance. (12 API calls, split across two `discovery_items.py` runs plus one record-detail fetch.)

2. **Editions.** *Correspondence of John, Fourth Duke of Bedford* (ed. Lord John Russell, 1842–46, 3 vols)
   searched via archive.org be-api fts (no login) on all three volumes' Internet Archive scans:
   `india.history.resource.40863` (vol. 1, 1842), `india.history.resource.40751` (vol. 2, 1843),
   `india.history.resource.40752` (vol. 3, 1846). `Tobago` → **0 hits in vols. 1 and 2**; 1 hit in vol. 3, but
   its snippet ("Indies, Dominica, Grenada, St. Vincent's, and Tobago... the late Earl of Albemarle, Sir
   Joseph Yorke...") is about the **1763** Peace of Paris negotiations (Minorca is mentioned in the same
   snippet, dating it to the Seven Years' War settlement, not 1749) — a different, later episode involving the
   same two men, not this letter. `Puyzieulx` (Bedford's principal French correspondent in the 1749 Tobago
   dispute per SP 78/232's own descriptions) → 1 hit in vol. 1, but the snippet is direct Puyzieulx–Bedford
   correspondence and table-of-contents entries about the Aix-la-Chapelle congress generally, not this Yorke
   letter, and vol. 1 has zero "Tobago" hits at all — the volume covers the congress and Sandwich's embassy,
   not the West Indies strand Yorke was reporting on. **No volume of Bedford's printed correspondence contains
   this letter or its content** as far as full-text search reached (caveat: be-api's index may not cover
   every page, and the physical tables of contents/indexes were not read by eye). Hardwicke Papers (Joseph
   Yorke was son of the 1st Earl of Hardwicke) were not checked this pass — a plausible next edition to try,
   named as a follow-up, not chased.

3. **Community lists.** WebSearch `Yorke Bedford 1749 cipher "SP 78/232" Tobago` surfaced only TNA Discovery's
   own catalogue pages for several neighbouring items in the same piece (C7340425 itself among them, plus
   /48, /54, /62, /67, /28), confirming the piece is indexed by search engines but finding no third-party
   discussion, solve claim, or community-list mention. No Cryptiana or Cipherbrain hit; local grep of
   `sources/cryptiana/` for "yorke"/"bedford"/"sp 78/232" returned zero hits.

4. **DECODE (de-crypt.org).** No login attempted (known broken; out of this lane's host list regardless).
   `aaymeloglu/unsolved-ciphers`'s cached `catalogue/decode-catalog.csv` and `decode-records.jsonl` greped for
   "yorke"/"bedford"/"sp 78/232": zero hits. No DECODE record found for this item in the cache.

5. **Solver repositories.** Fresh shallow clones of both (24 Sept 2026, shared with the other three targets
   this pass). `dbourdeau/cyphersolver`: grep for "yorke"/"bedford"/"tobago"/"albemarle" across the tree
   (excluding images) returns nothing; no target folder, no README row. `aaymeloglu/unsolved-ciphers`: grep of
   `TARGETS.md`, `SHORTLIST.md`, `catalogue/*` for the same terms returns nothing. Neither repository has
   touched this item.

6. **General web search.** The query in item 3 above is the general web search; a second pass restricted to
   "Joseph Yorke cipher 1749" and "Bedford Paris embassy cipher key 1749" found nothing naming this letter,
   its plaintext, or a decipherment; only unrelated modern cipher-teaching sites ("easy-ciphers.com/bedford",
   a coincidental name match with no historical content) and the Bucknell "Yorke's" sugar-mill history page
   (a different, unrelated "Yorke" — a Caribbean plantation family, not Sir Joseph Yorke).

**Host requests this pass:** discovery.nationalarchives.gov.uk 12 (shared running total with the other three
targets, ≥3 s apart), archive.org 9 (2 advancedsearch + 7 be-api fts, ≥3 s apart), WebSearch 2, GitHub 2
shallow clones (shared with the other three targets).

## Verdict

**Status: open.** No printed edition of Bedford's correspondence (the standard source, all three volumes
checked) contains this letter's content under "Tobago" or via its principal correspondent "Puyzieulx"; no
community list, DECODE cache, or either solver repository names it. The one real risk this pass could not
close is structural, not evidentiary: Discovery's own full-text search does not reliably surface "partly in
cipher" items by keyword in this piece (the note field lives outside the searched description text), so
"no cipher-related sibling found by keyword search" is weaker evidence here than in a piece where the
cataloguer's cipher language sits inside the description (contrast SP 78/69, this pass's N53, where "in
cipher" is written directly into the description and the keyword search worked cleanly). This does not
change the target's own confirmed status (it is definitely "partly in cipher" per its `note` field) — it
only means a sibling key or decipherment elsewhere in SP 78/232 could exist without having been found by this
pass's method.

**Copy status:** `digitised: false` (Discovery API, confirmed directly). **TNA page-copy order** case for
f.103 — see REQUEST.md.

**Recommended next step:** a TNA page-copy order for f.103; separately, a future worker with Discovery budget
to spare should check the `note` field of every item in SP 78/232 individually (not by keyword) for other
"partly/wholly in cipher" siblings, and check the Hardwicke Papers (1778) for Joseph Yorke's Paris
correspondence — neither chased this pass.
