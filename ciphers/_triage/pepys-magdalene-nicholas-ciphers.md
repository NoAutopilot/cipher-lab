# CHECK-PEPYSNIC: LEAD-AO1, Pepys MSS (Evelyn volumes), Magdalene College, Cambridge

Verdict: **open, not digitised -- hold as a lead, do not promote** (no ciphers/ folder created, per brief).

Worker: worker CHECK-PEPYSNIC (account 4, session_01LvEv28eytnGRK6n6Z2yibs), for the account-4 parent. Date: 24 Oct
2026, 04:00-04:1x UTC.

## Correction to LEAD-AO1's own framing (first finding)

QUEUE.md's LEAD-AO1 (SCOUT-OPEN, 23 Oct 2026) and this job's own brief both call the holding collection
"the Pepys Papers (Sir Edward Nicholas's Civil War and exile collection)". That label is not supported by the
source. The HMC 1911 report's own introduction (E. K. Purnell, pp.v-vi) states plainly that these three volumes
descended from **John Evelyn**, via his father-in-law **Sir Richard Browne** (Clerk of the Council to Charles I
and ambassador's secretary in Paris, 1641-60); Evelyn sent them to Pepys in 1681, and they passed to Magdalene
with Pepys's library in 1724. Sir Edward Nicholas appears in the volumes only as one correspondent among many
(one Sign Manual letter he countersigned, one letter "from" him in the index) -- there is no dedicated "Nicholas
Papers" sub-collection here. This is independently confirmed by a web search this session: "A Historical
Manuscripts Commission report by E. K. Purnell covers three volumes of manuscripts owned by John Evelyn and sent
by him to Pepys in 1681" (search summary, 24 Oct 2026). The correct short name is the **Evelyn/Browne Collection
(Pepys MSS)**; the "Catalogue of Letters Taken at Worcester" (the sub-section holding items (5), (71), (303),
(352)) is a royalist Civil-War-exile correspondence catalogue *within* this collection, not a separate Nicholas
archive. Filed here under the brief's given slug regardless, since no folder is being created.

## 1. Prior plaintext / decipherment -- searched, none found for the four named items

- **Whole-volume grep, HMC report itself** (`reportonpepysman0000unse_f0i4_djvu.txt`, fetched this session):
  89 lines mention cipher/cypher. The four target items -- (5) "1648, Aug. 5 -- From [name in cipher] to Duke
  of York, written mostly in cipher"; (69) "Keys of ciphers and letters"; (71) "A triplicate in cipher from
  Mr. Hansnaw"; (303) "Letters in ciphers from The King"; (352) "A letter to the Prince in cipher" -- carry no
  "deciphered" annotation, unlike roughly 20 *other* items in the same report explicitly marked "partly cipher
  deciphered" or "Partly in cipher deciphered ; the cipher words are printed in italics" (e.g. lines 9493, 9690,
  9802, 10317, 11318, 12514, 12641 of the fetched text) -- confirming, as LEAD-AO1 already noted, that
  "undeciphered" in this report is a checked state the 1911 editors actively used, not an unexamined default.
  The p.308 key register (Vol. III, pp.903-987: Leicester/Huggins, Secretary Coke/Vane 1638, Sackville Crow,
  Hale, Hopton-in-Spain/Dorchester-Gerbier 1641, Lord Aston, Jo. Tailor, Windebank's "old Cipher", Rowlandson,
  Goring, the Earl of Leicester/Lord Viscount Sligo, "My Lord Ambassador's cypher") is real and belongs to the
  *same two volumes* -- confirmed by direct read of the fetched text, not just LEAD-AO1's summary -- but every
  endorsed key there is for 1630s-40s diplomatic ciphers (mostly Sir Arthur Hopton's embassy to Spain), a
  different correspondence stratum from the 1648-51 exile-court catalogue holding the four undeciphered items;
  no key in the register is endorsed to any of the four items' correspondents (an unnamed sender to the Duke of
  York, "Mr. Hansnaw", "The King" to an unnamed recipient, an unnamed sender to "the Prince").
- **Warner, *The Nicholas Papers* vol. 1** (Camden Society, 1886; `11481219bsb`, fetched djvu text, covers
  dated letters from 1641 into the early 1650s): no "August 5" / "Aug. 5" 1648 entry of any kind; 22 cipher
  mentions, all referring to a *different* cipher key for Nicholas's own correspondence (preserved in BL
  Egerton MS 2550), unconnected to the Pepys MSS p.308 register or to items (5)/(71)/(303)/(352). No match.
- **Cryptiana** (`sources/cryptiana/web/`): `charlesi.htm` and `charlesii.htm` are Tomokiyo's own extensive
  treatments of Charles I/II Civil-War-era cipher correspondence (Nicholas, Rupert, Hopkins, Jane Whorwood,
  Ormonde, the Princes) and both cite *Memoirs of John Evelyn, Esq. F.R.S., Vol. 5* repeatedly as a primary
  source -- i.e. Tomokiyo has already worked this exact corpus family (Evelyn-derived Civil War cipher letters)
  hard, including a 2021 solve by Biermann and Brown of two Prince-Charles cipher letters -- but those two
  solved letters come from a different printed source (*Vindication*, p.158, a Newport/3 Oct 1648 letter and
  two companions), not from the Pepys MSS catalogue items. The distinctive surname "Hansnaw" (item 71) does not
  appear anywhere in `sources/cryptiana/` (grepped, 0 hits) or in a shallow clone of `aaymeloglu/unsolved-ciphers`
  (0 hits) or in `sources/cyphersolver*` (0 hits).
- **`be-api.us.archive.org` full-text search for "Hansnaw"** (one query, 83 hits): the only readable hits are
  an unrelated fictional character in a 1949 Scholastic magazine story -- no period-document hit anywhere on
  Internet Archive for this name.
- **DECODE listing cache**: `tools/decode_list.py`'s cached harvest files (grepped by filename, no fetch) show
  no entry naming Pepys, Evelyn, Magdalene, Hopton or the four items; not re-fetched live this session (not
  needed -- a login-free cache grep is sufficient to rule out a cached match).
- Google Books / OpenAlex / S2 phrase search on the four items' exact wording not run this session (time/cost
  budget spent on the higher-value archive.org/web checks above, which already found the governing facts); if
  this lead is re-opened, run `tools/print_check.py` with "triplicate in cipher from Mr. Hansnaw" and "Letters
  in ciphers from The King" as the first two phrases.

## 2. Physical location and digitisation -- not confirmed digitised anywhere

- The Pepys Library (Magdalene College) has no public online manuscript catalogue with item-level shelfmarks
  or an availability flag for these three Evelyn volumes: the complete printed catalogue (Latham, ed.,
  1978-1994) is print-only; Magdalene's institutional archives catalogue
  (`magdalene.maxarchiveservices.co.uk`) returns no record for "Evelyn papers" (checked this session -- a
  "Browse all descriptions" search link exists but no record surfaced); CUDL has no listing found for this
  collection either (search engine check, no hit). This is a **search result, not a digitisation verdict**
  (CLAUDE.md Usage 8a) -- no catalogue record with its own quoted flag was found, positive or negative.
- **Route**: Pepys Library, Magdalene College -- Special Collections Librarian, Catherine Sutherland,
  pepyslibrary@magd.cam.ac.uk, 01223 332115 (address read from the Library and Archives page,
  `www.magd.cam.ac.uk`, 24 Oct 2026) is the reproduction-request contact for appointments, photographic
  services and general enquiries.

## 3. Scoring -- not run; both gating tools refuse at pre-board stage

- `tools/prior_work.py pepys-magdalene-nicholas-ciphers --item-spec ...` refuses with "no folder
  ciphers/pepys-magdalene-nicholas-ciphers" -- the tool requires an existing target folder, which this brief
  explicitly forbids creating at triage stage. Not run.
- `tools/scout_rubric.py --rerank` only reranks entries already in `QUEUE-scores.json`; LEAD-AO1 was
  explicitly "not scored as a candidate" by SCOUT-OPEN (digitisation unconfirmed) and this session's checks
  leave that unchanged, so there is nothing to rerank.
- Per the brief, step 3 (scoring) was conditional on step 1 finding no plaintext AND step 2 finding the items
  located; (1) holds (no plaintext/decipherment found for the four items) but (2) only locates them
  bibliographically -- no confirmed digitisation -- so this stays a **lead**, not a scoreable candidate,
  consistent with SCOUT-OPEN's own original call.

## Premise check

(a) Folder's own NOTES.md/REQUEST.md/spec: none exist (no folder). (b) Other solvers' working files: Tomokiyo's
`charlesi.htm`/`charlesii.htm` cover the same correspondence family in depth (Evelyn's Memoirs as a direct
source) but name none of the four items; the 2021 Biermann/Brown solve is a different printed source
(*Vindication*). Aymeloglu's repository (shallow-cloned, grepped) and Bourdeau's `cyphersolver`/`cyphersolver-site`
(local checkouts, grepped) have no mention of Pepys, Magdalene or Hansnaw. (c) Physical neighbours: the HMC
report's own whole-volume read (not just the four items) found roughly 20 *other* cipher items in the same
report explicitly marked "deciphered" by the 1911 editors -- i.e. the editors did resolve what they could from
the same volumes, strengthening (not weakening) the case that the four flagged items are genuinely unresolved,
not merely unexamined. (d) Recipient-side editions: not applicable (no named recipient-office archive to check
beyond Nicholas's own papers, already checked in step 1).

## Requests (this session)

`archive.org/metadata` + `archive.org/download` (djvu text): 2 fetches (HMC report, Nicholas Papers vol. 1).
`be-api.us.archive.org/fts/v1/search`: 1 query ("Hansnaw"). `archive.org/advancedsearch.php`: 1 query (Nicholas
Papers title search). WebSearch: 3 queries (Pepys Library/Evelyn catalogue, reproduction route, PL shelfmark).
WebFetch: 1 (Magdalene archives catalogue search page). `github.com` shallow clone (depth 1): 1
(`aaymeloglu/unsolved-ciphers`, grepped, not pushed, deleted from scratchpad). No Gallica, no CUDL live fetch
beyond a reachability check, no Google Books API, no OpenAlex/S2, no logins, no credentials. `tools/dup_check.py
pepys-magdalene-nicholas-ciphers` run before claiming: ok, no live duplicate claim.

## While waiting

The one action that depends on nobody: the Library's reproduction-request route (pepyslibrary@magd.cam.ac.uk)
is itself the only way to confirm digitisation status or get an image; nothing else advances this lead without
either that reply or a human with a library-subscription database (JSTOR/Google Books full-view) check on the
*Vindication* source and the Evelyn Memoirs Vol. 5 appendix for an independent sighting of these four items'
text, which was not run this session (time/cost budget).

## Parent note (account-4 parent, 24 Oct 2026, 05:2x UTC): the six questions

1. **Learned.** Four 1648-51 exile-court items catalogued "in cipher" without the 1911 editors' "deciphered" mark, plus item (69)
   "Keys of ciphers and letters" in the same Worcester sub-catalogue; the p.308 key register is real but belongs to the 1630s-40s
   Hopton-embassy stratum and names none of the four items' correspondents; no prior plaintext in Warner vol. 1, Cryptiana, the two
   solver repositories or Internet Archive full text; no digitisation record; the route is the Pepys Library's own enquiry address.
   The collection is Evelyn/Browne, not a Nicholas archive (the scout's label, corrected here).
2. **Assumptions the result rests on.** That an HMC 1911 "in cipher" entry with no "deciphered" mark is unresolved today, not merely
   unprinted; that Warner vol. 1 covers Aug 1648 (it runs to early 1653, so yes); that item (69)'s keys are the exile-court keys
   rather than more Hopton material (untested, M).
3. **Unverified.** Physical survival and legibility of the five items; item (69)'s content and endorsements; *Memoirs of John Evelyn*
   vol. 5 appendix and *Vindication* not grepped; no Google Books / OpenAlex phrase search (worker's own gap).
4. **Alternatives.** "Letters in ciphers from The King" (303) may be Charles I letters whose plaintext is printed elsewhere (*The King's
   Cabinet Opened*, 1645, or Evelyn's Memoirs vol. 5); "Mr. Hansnaw" (71) may be a transcription of *Fanshaw* (Richard Fanshawe was
   with the Prince's court in 1648), which would tie this lead to LEAD-AO2's Hyde-to-Fanshaw 1659 items -- an M-grade guess, not a
   finding.
5. **Most informative different experiment.** Not more catalogue work: one enquiry to the Library asking whether (69), (5), (71), (303),
   (352) survive, their extent, and photography terms (SPRINT P14, the owner's email); on our side `tools/print_check.py` with
   "triplicate in cipher" and the Hansnaw/Fanshaw variants before any image arrives (about USD 1, next scout brief).
6. **Decision.** Acquire (SPRINT P14); no further scouting on this lead; LEAD-AO2 not opened as its own job -- one web check of the
   Heathcote (Conington) papers' current holder rides the next program-C brief instead.

Side-check by the parent (24 Oct 2026, 05:2x UTC, 3 Discovery API requests, scratchpad only): SCOUT-OPEN's remark that "most of
SP 84/165's own undecoded-cipher items" carry a "Decoded by P.R.O." gloss is not borne out by Discovery for that piece -- 85 items
match "SP 84/165" cipher and 25 match "SP 84/165" decoded, 0 carry any "decoded by" gloss, and the eleven Fuente items (ff.187, 228,
231, 243, 258, 263, 287, 306, 313, 315, 317) all still read "Undecoded cipher". The gloss, if it exists, is on SP 84/166-171 items;
SPRINT P12 and ciphers/sp84-fuente-1662 are unchanged.

## Correction (C-FOLLOW, 24 Oct 2026, 05:3x UTC): the gloss IS on SP 84/165 -- it lives in the `note` field, not `scopeContent.description`

The parent's side-check above searched/read the field the Discovery search-records listing shows by default
(`scopeContent.description`); the "Decoded by P.R.O." text is a *cataloguer's note*, returned only by the
per-item details endpoint (`/API/records/v1/details/<id>`) as the `note` field, which the side-check did not
fetch. Querying Discovery's full-text search for the exact phrase `"Decoded by P.R.O."` (no series filter)
returns exactly **8** items, and querying `"SP106/6"` (no series filter) returns those same 8 plus the key
piece itself (SP 106/6, record C3677736) -- **all 8 are in SP 84/165**, none in SP 84/166, 168 or 171:

| ref | folio | date | correspondents | note (verbatim) |
|---|---|---|---|---|
| SP 84/165/8 | 13 | 1662 nd | [Chauran] to [Williamson] | Original document partly in undecoded cipher. Decoded by P.R.O. For Key, see SP 106/6, no. 32. |
| SP 84/165/65 | 106 | 1662 Mar 5 | Wickfort to [Williamson] | ...Decoded by P.R.O. For key see SP 106/6, no. 32 |
| SP 84/165/64 | 105 | 1662 May 3 | Wickfort to [Williamson] | ...Decoded by P.R.O. For key see SP 106/6, no. 32 |
| SP 84/165/109 | 184 | 1662 Apr 19 | Wickfort to [Williamson?] | ...Decoded by P.R.O. For key see SP 106/6, no. 32. |
| SP 84/165/114 | 190 | 1662 May 7 | [Chauran?] to [Williamson?] | ...Decoded by P.R.O. For key see SP 106/6 no. 32. |
| SP 84/165/115 | 192 | 1662 Apr 26 | Wickfort to [Williamson?] | ...Decoded by P.R.O. For key, see SP 106/6, no. 32. |
| SP 84/165/126 | 213 | 1662 May 5 | Wickfort to [Williamson?] | ...Decoded by P.R.O. For key, see SP 106/6, nos. 31 and 35. |
| SP 84/165/127 | 214 | 1662 May 14 | Wickfort to [Williamson?] | ...Decoded by P.R.O. For key, see SP 106/6, no. 32. |

All 8 are Wickfort/Chauran-to-Williamson, Mar-May 1662 -- a narrow slice of SP 84/165, not "most" of it (a
separate query, `"SP 84/165" "undecoded cipher"`, returns 18 items; 8 of 18 carry the gloss, the other 10 do
not). These 8 are **known text** at best: already decoded by the PRO itself against SP 106/6, so a reading from
them is key application, never a fresh cryptanalytic result (CLAUDE.md rule 2 result-label note).

Checked separately, by their own Discovery `note` field (not the search-listing description), the 9 items
SCOUT-OPEN named in SP 84/166/7,41,51,52,71,81,84,98, SP 84/168/26 and SP 84/171/55: **none carry the gloss** --
every one reads "Undecoded cipher." / "Part in undecoded cipher." / "Small part in undecoded cipher." / "...Copy."
with no "Decoded by" text and no key citation of their own. SCOUT-OPEN's original framing for these 9 stands:
genuinely undecoded, no key cited in their own catalogue note (the SP106/6 key is attested only on the
SP84/165 cluster above, by the same correspondent network but not named on these 9's own records) -- a
key-assisted *candidate* once imaged, not yet a confirmed key-in-reach item. Full table:
`harvest/C-FOLLOW-2026-10-24-sp84-gloss.tsv`.

## Print check (C-FOLLOW, 24 Oct 2026)

`be-api.us.archive.org` full-text search (exact phrase, no series restriction) and the Google Books API
(`country=US`, keyed) on five of the brief's six phrases plus the two compound queries, scratchpad
`/tmp/cfollow_phrases.txt`, output `/tmp/cfollow_out/print-check.tsv` (not committed -- scratch, per Scratchpad
hand-off; results logged here instead since no target folder exists to hold it):

- **"triplicate in cipher"** -- ia-global 4 hits, all either the HMC 1911 Pepys report itself (three IA copies
  of the same `reportonpepysman*`/`reportonpepys*` volume) or an unrelated 1774-series Continental Congress
  index (`indexpapersofcon0002butl`) -- no independent prior print.
- **"Hansnaw"** -- ia-global 83 hits, all noise (a 1949 *Literary Cavalcade* story character, a 1933 physics
  journal, period newspapers with no connection) -- confirms CHECK-PEPYSNIC's own earlier single-query finding
  at a wider result count; still no period hit for this name anywhere on Internet Archive.
- **"Hanshaw" + 1648 + cipher** (compound, run by hand as `Hanshaw AND 1648 AND cipher` against
  `be-api.us.archive.org`, since the tool's phrase wrapper cannot express a conjunction) -- **0 hits**.
- **"Fanshaw" + "triplicate"** (same hand method) -- 10 hits, every one noise (Federal Register
  duplicate/triplicate form-copy boilerplate; a 2003 Alaska nautical-chart "Cape Fanshaw" coordinate
  description) -- no connection to Sir Richard Fanshawe or this correspondence.
- **"Letters in ciphers from The King"** -- ia-global 1 hit: the same HMC 1911 Pepys report volume
  (`reportonpepys00greauoft`) -- the catalogue entry itself, not an independent prior print.
- **"Keys of ciphers and letters"** -- ia-global 3 hits, all three HMC 1911 report copies -- same catalogue
  entry, not independent.
- **Google Books API** -- unreachable all session: every call (4 phrases, two passes 3 s apart, plus the two
  compound queries by hand, 10 calls total) returned HTTP 503 `backendFailed`, matching CLAUDE.md's documented
  12/15 Oct 2026 intermittent-fault note (RETRO-2026-10-19 P3); one retry taken per that note's instruction,
  then logged and moved on -- **not searched this session**, not a hit/no-hit verdict either way.

Net: every ia-global hit for the four single phrases traces back to the HMC report's own catalogue description
of these exact items, never to an independent printed source; the two compound name-variant queries found
nothing. This is a search result on this date by this method (CLAUDE.md rule 10), not a novelty verdict --
Google Books specifically still needs a re-run once the host's 503s clear.

### Parent correction (24 Oct 2026, 06:4x UTC, after C-FOLLOW)

The side-check above was wrong, and C-FOLLOW's answer stands: the "Decoded by P.R.O. For key see SP 106/6 no. 32" gloss is real on
SP 84/165, in Discovery's per-item *note* field (8 items: ff.13, 105, 106, 184, 190, 192, 213, 214, Wickfort and Chauran to Williamson,
Mar-May 1662; harvest/C-FOLLOW-2026-10-24-sp84-gloss.tsv). The parent read only the search endpoint's scope-content `description`,
which does not carry the note. Lesson: before contradicting a worker's catalogue reading, fetch `/API/records/v1/details/<id>` and
read the note field, not the search listing. What does not change: the eleven Fuente items (ff.187, 228-317, Spanish intercepts) carry
no gloss and stay SPRINT P12; the 9 SP 84/166, 168, 171 items (Wickfort/De Bacquoy, 1660-63) carry no gloss and no key citation, so
they are key-assisted candidates once imaged, with SP 106/6 no. 32 (and nos. 31, 35) as the key family to test first.

Six questions after C-FOLLOW: learned -- the SP 106/6 no. 32 family has 8 PRO-decoded letters (built-in known-plaintext controls) and
10 undecoded ones in the same network; the Pepys phrases have no independent print on archive.org (Google Books not searched, 503 all
session); the Heathcote papers split between Huntingdonshire Archives (CON) and Barking and Dagenham (M51-286). Assumptions -- that the
PRO decodes used no. 32 for every one of the 8 (their notes say so); that the 1660-63 letters use the same key as 1662 (M). Unverified --
which half holds the 1659 Hyde items; the DECODE images of SP 106/6 nos. 31, 32, 35. Alternatives -- the 1660 and 1663 items may use a
later or earlier key (Wickfort's own "nouveau chiffre", f.214, May 1662). Most informative next experiment -- get the SP 106/6 no. 32
key on disk from DECODE now (one browser login, per-record full-size test, A2-HDK), so the pool is ready when the TNA images arrive
(brief -47, DECODE-KEY32). Decision -- acquire (SPRINT P12 widened to the SP 84/166-171 items; no new money ask); Heathcote stays an
open triage lead with one cheap catalogue step named in its file.
