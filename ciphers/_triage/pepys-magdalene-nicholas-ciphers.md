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
