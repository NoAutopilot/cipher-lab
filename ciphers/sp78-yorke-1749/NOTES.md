open
Correspondence of John, Fourth Duke of Bedford (ed. Russell), vol. 1 (1842, archive.org india.history.resource.40863) and vol. 2 (1843, india.history.resource.40751) full-text-searched (be-api) by this worker on 2 Oct 2026 for "Yorke", "Mr. Yorke to the Duke of Bedford", "Paris, March", "March 8", "March 20", "1748-9", "Tobago", "Puyzieulx", "Albemarle", "Townsend": vol. 2 prints Bedford to Yorke of 16 Feb, 27 Feb, 13 Mar and 20 Mar 1748-9 and a private Yorke to Bedford of May 1749, but not this Yorke to Bedford of 8/20 Mar 1749 (no "Tobago"/"Puyzieulx"/"Paris, March" hit); absent.

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

**Update 3 Oct 2026 (A2P4-YOR3):** Albemarle/Aix-la-Chapelle/cypher fts of all three Bedford volumes and the Harris and Yorke Hardwicke lives found no print of f.103's content (details in the section below); status stays open.

**Recommended next step:** a TNA page-copy order for f.103; separately, a future worker with Discovery budget
to spare should check the `note` field of every item in SP 78/232 individually (not by keyword) for other
"partly/wholly in cipher" siblings, and check the Hardwicke Papers (1778) for Joseph Yorke's Paris
correspondence — neither chased this pass.

## NX-UNBLOCK (26 Sept 2026)

Free-route pass per CLAUDE.md's NX-UNBLOCK brief: checked TNA's current record-copying fee page
(`nationalarchives.gov.uk/help-with-your-research/record-copying/fees/`, read 19:01 UTC 26 Sept 2026 --
page check £9.92/record, digital copy up to A3 £1.52/copy) and tried the TNA Discovery search API for a
fresh digitisation check (`discovery.nationalarchives.gov.uk/API/search/records?sps.searchQuery=...`); it
returned HTTP 500, not retried per the good-citizen single-retry rule. No new free scan or edition found for
this item this pass; digitisation status stands as already recorded in this folder's REQUEST.md. This item
is now item in the consolidated order `outreach/tna-page-copy-batch.md` (ASKS row 73, status backlog) rather
than a standalone TNA order.

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: a TNA page-copy order for SP 78/232/44 (REQUEST.md, since 24 Sept 2026, now folded into the
consolidated TNA batch, ASKS row 73).

- [done 2 Oct 2026, A2-YOR: see "SP 78/232 per-item note check" below] M: check the note field of every item in SP 78/232 individually (not by keyword) for other cipher/decipher siblings -- tools/discovery_items.py, ~150 items, this file's own named next step.
- [catalogue part done 2 Oct 2026, A2-YOR2: BL Add MS 35355 f. 370, Bedford to Yorke 1749-51, copies, undigitised; see "BL catalogue check" below] S: search the Hardwicke Papers (BL Add MS 35349-36278) for this correspondence; the printed-text side (archive.org/HathiTrust) not checked.
- [done 3 Oct 2026, A2P4-YOR3: see "Bedford volumes, Albemarle / Aix-la-Chapelle pass" below; no print of f.103 found] S: full-text search the three Bedford correspondence volumes for 'Albemarle' or 'Aix-la-Chapelle'.
- [printed-text side of Hardwicke line done 3 Oct 2026, A2P4-YOR3: Harris 1847 and Yorke 1913 searched, no hit] S: archive.org/HathiTrust Hardwicke side (HathiTrust not reachable from the cloud; not searched).

## Bedford volumes, Albemarle / Aix-la-Chapelle pass (A2P4-YOR3, 3 Oct 2026, 17:4x UTC)

Method: archive.org be-api fts (no login), one query at a time, 1.6 s apart, descriptive UA, per identifier: vol. 1
india.history.resource.40863, vol. 2 india.history.resource.40751, vol. 3 india.history.resource.40752. No djvu text was on
disk and none was fetched; fts returns a handful of snippets per book without a usable page number (see CLAUDE.md,
be-api note), so a "no hit" is a search result, not an exhaustive read. Requests: be-api 24 + 10 + 6, advancedsearch 1.
Positive control: "Tobago" reproduces the 2 Oct 2026 result (0 hits vols 1-2, vol. 3 hits the 1763 Peace of Paris passage).

| term | vol. 1 | vol. 2 | vol. 3 |
|---|---|---|---|
| Tobago | 0 | 0 | 1 (1763, not this letter) |
| Albemarle | 1 (Albemarle named in 1748 letters about the congress) | 1 (contents list "Earl of Albemarle to the Duke of Bedford" 1751; his "Most secret" letters) | 1 (1763) |
| Aix-la-Chapelle / Aix la Chapelle | 1 (congress, 1748) | 1 (treaty references; editor's preface) | 1 (Dunkirk, treaty references) |
| Puyzieulx / Puisieux | 1 / 1 (1748) | 0 / 1 (Bedford's replies about his conversations, undated in snippet) | 0 / 0 |
| cypher / cipher | 0 / 0 | 1 / 1 (Bedford: "your letter in cypher of the ... instant", "your Grace's packet, being great part in cypher I sent to Mr. Aldworth"; "Translation of a Letter in Cypher from Mr. Wall to Don Joseph de Carvajal"; one "cipher" = a person) | 0 / 1 (a person) |

Hits in 1749-50 that touch the target's content (SP 78/232/44: Albemarle's appointment, Townshend answer, Tobago refused to
Saxe): none. The vol. 2 contents list prints "Duke of Bedford to Mr. Yorke" and "Mr. Yorke to the Duke of Bedford" entries, and
its snippets show Bedford acknowledging a cypher letter and a packet "great part in cypher"; the snippets carry no date or
page, so whether the acknowledged letter is the 8/20 March one is not established. Follow-up queries ("Saxe Tobago",
"Townshend memorial", "Mr. Yorke Albemarle appointment") returned nothing tying a printed letter to f.103. Not found in print.
Cypher mentions in vol. 2 are evidence the volume prints some correspondence about cipher letters; they do not print any
plaintext of f.103.

Hardwicke printed side (search only): archive.org items lifelordchancel05harrgoog (Harris, Life of Lord Chancellor
Hardwicke, 1847) and lifecorresponden01york / cu31924031041571 (Yorke, Life and Correspondence of Philip Yorke, 1913): "Tobago"
0 hits in Harris and in lifecorresponden01york, 1 hit in cu31924031041571 (index entry "Tobago, occupied by the French, ii 7");
"cypher" 1 hit each, all the word meaning a nonentity. Not found: any printed Yorke-to-Bedford cipher letter or decipherment.
HathiTrust full text: not reachable from the cloud, not searched.

Grades: none (no reading made). No control of the rule-3 kind applies (print lookup, no solver).

Next cheapest step unchanged: the owner-side TNA page copy (REQUEST.md, ASKS row 73 batch). Optional, ~$1: read vol. 2's
index/contents pages by eye for the dated Yorke entries of March 1749 (needs page images, not fts).

## Web and blog check (GF-A2-4, 2 Oct 2026)

Queries (WebSearch, 2 Oct 2026 22:3x UTC), each with what came back:
1. sender + recipient + date: `Joseph Yorke to Duke of Bedford Paris March 1749 Albemarle Townshend Tobago Saxe letter
   cipher` -- only TNA catalogue pages (beta.nationalarchives.gov.uk C7340425 itself and siblings C7340422/429/434/436/
   438/449/450/451): f.130 (15/26 Mar, "Cipher"), f.114, f.94. No third-party page.
2. shelfmark + cipher: `"SP 78/232" cipher Yorke 1749` -- the same TNA catalogue pages plus C4539850; nothing else.
3. distinctive phrase (the catalogue's own wording; no clear-text of the cipher exists): `"Tobago has been refused to
   Saxe"` -- TNA C7340423/429/448 and unrelated Tobago history pages (Sloane letters, British History Online CSP
   Colonial 1683, Britannica copies). Nothing on this letter beyond the catalogue.
4. folder title: `Yorke Bedford Albemarle's appointment Townshend answer Tobago return partly in cipher 1749` -- TNA
   catalogue pages only (incl. f.112 and f.175 Bedford to Yorke, "Part to be sent in cipher").
5. Cipherbrain: `site:scienceblogs.de klausis-krypto-kolumne Yorke Bedford 1749 cipher` -- blog category/archive pages,
   no post on this letter.
6. Cryptiana blog: `site:cryptiana.blogspot.com British diplomatic cipher 1749 Paris Yorke` -- no cryptiana result.
7. Cipher Mysteries: `site:ciphermysteries.com Yorke Bedford 1749 State Papers France cipher` -- no ciphermysteries
   result.
The open web knows this letter only through TNA's own catalogue; no blog post, so no comment thread to read. No
decipherment or plaintext found.

## Premise check (GF-A2-4, 2 Oct 2026)

(a) Decipherments the folder already mentions: none -- NOTES.md and REQUEST.md mention no decipherment, gloss or
clear copy of f.103; the catalogue note is only "Partly in cipher." Not found.
(b) Other solvers' working files: shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers (2 Oct
2026), grep `Yorke|Albemarle|SP ?78/232|sp78`: cyphersolver mentions Yorke only as a name inside French/Dutch
ciphers of The Hague 1755-56 (affry1757 key word "yorke", README line 51 Kauderbach); Aymeloglu only DECODE R9154 (BL
Add MS 32256 f.67, 1721, "Mr. Frampton Yorke", a key, another man and decade). No file on SP 78/232. Aymeloglu cited,
not copied. Not found.
(c) Physical neighbours: Discovery API details read for the items on each side (2 Oct 2026, 5 requests): SP 78/232/42
f.99 (Yorke to Bedford 4/15 Mar, no note), /43 f.101 (Bedford to Yorke 9/20 Mar, acknowledging), /44 f.103 (target,
"Partly in cipher."), /45 f.105 (Reply to Townsend memorial, "Enclosed in f. 103. Copy." -- the enclosure, clear),
/46 f.107 (Bedford to Yorke 13/24 Mar, "Part to be sent in cipher"). No neighbouring item is described as a
decipherment of f.103; the leaves themselves are not digitised (`digitised: false`), so a decipherment written on
f.103-104 itself cannot be ruled out until the page copy (REQUEST.md) arrives. Not found in the catalogue; leaf
unreachable.
(d) Recipient's side: Bedford is the recipient; his printed Correspondence (vols 1-2) full-text-searched this pass
(line 2): it prints Bedford's own letters to Yorke of Feb-Mar 1749 and one Yorke private letter of May 1749, not this
one. The Hardwicke-side papers (Joseph Yorke's letters to his father, the 1st Earl of Hardwicke) are
not searched here -- a later step, not this gate pass. Not found in print.
Result: nothing found that reads f.103's cipher.

## SP 78/232 per-item note check (A2-YOR, 2 Oct 2026, 23:2x UTC)

Step run: the While-waiting "M" step -- the `note` field of every item in SP 78/232 read one record at a time, not by
keyword. `tools/discovery_items.py` gained a `--notes PARENT_ID` mode for this (children list, then one details
record per item, 1.6 s apart; offline test `tools/tests/test_discovery_items.py`). Command:
`python3 tools/discovery_items.py --notes C4539850 > ciphers/sp78-yorke-1749/sp78-232-notes.tsv` (C4539850 is the
piece, the `parentId` of SP 78/232/44). Output on disk: `sp78-232-notes.tsv`, 109 rows, one per item (the piece
has 109 items, not ~150; `hasMoreAfterLast: false`). Requests: discovery.nationalarchives.gov.uk 112 (1 details
probe, 1 children list, 109 details, 1 earlier children probe), no 403/429/500.

Result (catalogue only; every item `digitised: false` as far as checked earlier, no leaf read):
- **Yorke to Bedford, in cipher (incoming, note "Cipher."/"Partly in cipher."): 16 items**, the target and 15
  siblings, 4/15 Mar to 21 June/2 July 1749: SP 78/232/41 (f.94), 44 (f.103, target), 53 (f.130), 55 (f.138),
  62 (f.158), 68 (f.177), 73 (f.189), 74 (f.192), 77 (f.199), 84 (f.219), 86 (f.223), 91 (f.237), 95 (f.247),
  98 (f.255), 101 (f.261), 109 (f.279). The keyword search of 24 Sept found none of these as cipher items; the
  caveat recorded then was right.
- **Bedford (and once Aldworth) to Yorke, office drafts noted "Part to be sent in cipher"/"To be sent in
  cipher": 11 items**: SP 78/232/32 (f.69), 38 (f.88), 46 (f.107), 47 (f.112), 60 (f.152, Aldworth), 66 (f.172),
  67 (f.175), 79 (f.207), 99 (f.257), 100 (f.259), 108 (f.277). A draft marked "to be sent in cipher" is
  normally the clear text the office enciphered; if the sent, enciphered versions survive on Yorke's side
  (Hardwicke Papers, British Library), each pair is known plaintext for the embassy's cipher (crib material, grade
  C if aligned). Not checked whether the Yorke-side copies survive; whether one cipher served both directions is
  not established.
- **No item in the piece is noted or described as a decipherment, a decipher, or a key** (grep of note and
  description for decipher/key: 0 items). Whether the 16 incoming cipher letters carry interlinear decipherments
  on the leaf (common for Secretary-of-State incoming cipher) is not visible in the catalogue; only the leaves
  settle it.
- Tool false positives, for the record: SP 78/232/90 and /92 are flagged by the tool only because their
  descriptions contain "duplicate" (the tool's word list); their notes say nothing of cipher.

What this changes: the target is one of a 16-letter incoming cipher series in one piece over four months, plus 11
outgoing drafts in clear marked for encipherment -- a sign pool (CLAUDE.md pipeline 3, pools first), not a single
short letter. The page-copy order (REQUEST.md, ASKS row 73 batch) is better spent on one "Cipher." sibling with
the target, so the leaves show whether a period decipherment is written on them, before any cryptanalysis.

Next cheapest step (as written by A2-YOR; (a) run 2 Oct 2026 by A2-YOR2, see the next section): (a) ~$1, BL catalogue
check for Bedford's enciphered letters to Yorke in the Hardwicke Papers -- [done, A2-YOR2]; (b) add one "Cipher."
sibling (e.g. SP 78/232/41, f.94) to the TNA copy order in REQUEST.md -- an owner-side order, not run here.

## BL catalogue check for the Yorke-side copies (A2-YOR2, 2 Oct 2026, 23:4x UTC)

Step run: (a) above. Host: `searcharchives.bl.uk` only (JSON search `?format=json&per_page=50&q=...` and per-record
`/catalog/<id>.json`), 2 s apart, descriptive UA, 13 requests, all HTTP 200, no challenge. Queries (8): `"Joseph
Yorke" Paris 1749` (55 hits), `Yorke Bedford cipher` (0), `Bedford "Letters to Joseph Yorke"` (0), `"Duke of
Bedford" Yorke 1749 Hardwicke` (55), `Joseph Yorke cipher` (11, none 1749 Paris), `"Letters to Sir J. Yorke"` (15),
`Add MS 35354` (1), `Yorke cipher 1749` (0). Full hit list: `bl-catalogue-2026-10-02.tsv` (127 rows). Records read
in full: Add MS 35355, Add MS 35354-35358 (series), Egerton MS 3416, Add MS 36122.

Found (catalogue descriptions only; no leaf seen):
- **Add MS 35355** (Hardwicke Papers vol. VII, "II. ff. 410", 1749-1751; series Add MS 35354-35358 = Hardwicke's
  correspondence with his son Joseph, 1742-1764): **f. 370 "John Russell, 4th Duke of Bedford: Letters to Sir J. Yorke:
  1749-1751.: Copies."** This is the only BL entry naming Bedford-to-Yorke letters. It says "Copies"; it does not say
  cipher, decipher or in clear, nor which dates. Same volume: Puysieulx-Hardwicke correspondence 1749-51 (ff. 1, 10,
  225, 392, 394) and Yorke's appointment as Secretary of Embassy at Paris 1749 (f. 342). Digitised-content field
  (`url_tsi`) empty: not online.
- **Egerton MS 3416** (Leeds/Holdernesse Papers vol. XCIII, 1749-1751): ff. 1-19 Yorke's memorials to the French
  government on Tobago, 1749 (copies, French), and ff. 53-328 passim Bedford-Albemarle correspondence 1749-51,
  copies. Holdernesse's copies of the Paris embassy file after Albemarle's arrival, not Yorke's received cipher
  letters; no cipher noted. `url_tsi` empty.
- **Add MS 36122** f. 1: Yorke's appointment (warrant), no correspondence. Add MS 33026-33027 (Newcastle Papers):
  Albemarle's letter-books, and Yorke's letter-books "while in charge of the embassy at Paris: 1751" -- 1751, not
  the Mar-Jul 1749 span of the SP 78/232 pool.
- **Not found:** no BL record names Bedford's letters to Yorke as received in cipher, no decipher or key of the Paris
  embassy cipher of 1749, and no item-level entry for any of the 11 draft dates (SP 78/232/32 ... /108). The BL
  descriptions list selected contents per volume, not every letter, so this is a catalogue result, not proof that
  the enciphered sent copies are lost.

What this changes: the crib route through Yorke's side narrows to one volume, Add MS 35355 f. 370 onward, undigitised,
whose "Copies" may be Yorke's own clear (or deciphered) copies rather than the cipher as sent. Clear copies would only
repeat the TNA drafts; they would be crib material only if the sent cipher letters themselves survive somewhere, which
no catalogue entry found here shows. Whether the Yorke-to-Bedford letters (the target and its 15 siblings) carry a
decipherment written on the TNA leaves is still the cheapest open question, and only the page copy answers it.

Next cheapest step: the owner-side TNA page copy (REQUEST.md, ASKS row 73 batch) of f.103 plus one "Cipher." sibling
(SP 78/232/41, f.94) and one "to be sent in cipher" draft (SP 78/232/46, f.107), at the fees recorded 26 Sept 2026
(page check GBP 9.92 per record, digital copy GBP 1.52 per copy; not re-quoted) -- needs the owner. Lower priority, also owner-side: a BL reprographics quote for Add MS
35355 ff. 370-391 only if the TNA leaves carry no decipherment.

## Next step (R13-STALE, 6 Oct 2026)

Next step: the TNA page-copy order (REQUEST.md, item 9 of `outreach/tna-page-copy-batch.md`, ASKS row 73, owner-side, about GBP 11.44 per
record at the 26 Sept fees) for f.103, plus one "Cipher." sibling (SP 78/232/41, f.94) and one "to be sent in cipher" draft (SP 78/232/46,
f.107) -- needs the owner. Every agent step written above is done (per-item note check A2-YOR, BL catalogue A2-YOR2, Bedford and Hardwicke
print A2P4-YOR3); the only optional online step left is a by-eye read of Bedford vol. 2's contents pages for March 1749 entries, which needs a
lending-only page view (a person in the IA reader), not an agent. Housekeeping line, R13-STALE (account 4): no work run.
