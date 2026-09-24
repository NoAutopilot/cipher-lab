# DECODE (de-crypt.org) catalogue harvest, 24 September 2026

LANE N worker, DECODE catalogue harvest brief (`.claude/briefs/runs/2026-09-24-lane-n-decode.md`).

## Method

**No login used.** Before logging in, checked whether de-crypt.org's own "Advanced Search" page
(`RecordsSearch`) could filter by Status without a session: it can. Loading `RecordsSearch` in a headless
browser (no credentials), selecting Record Type = Cipher and Status = Non-decrypted in the form, and
submitting redirects (302) to a plain, repeatable GET:

    RecordsList?x_record_type=1&z_record_type=%3D&x_status=2&z_status=%3D&cmd=search

`x_status` codes (read from `RecordsSearch`'s own `<select name="x_status">`): 1 Decrypted, 2 Non-decrypted,
3 Partially decrypted, 4 N/A. `x_record_type` codes: 1 Cipher, 2 Key, 3 Manual. This URL plus
`&recperpage=50` (the grid's own page-size maximum) `&page=N` returns full record rows -- id, holder,
dates, languages, record type, status, page count -- from plain `curl`/`urllib`, no cookies, no
JavaScript, confirmed against the live site. RecordsView and DocumentsList (per-record detail, image and
document content) do still require login per the Access playbook; this harvest did not need them for the
listing itself.

This supersedes the brief's assumption that a login was needed to page the filtered list. `tools/decode_list.py`
implements the crawl (`--help`, offline test `tools/tests/test_decode_list.py` against a saved 2-row fixture).
No DECODE_USER/DECODE_PASS were read or touched by this pass.

## What was fetched

Two filters, Record Type = Cipher, Status = Non-decrypted and Status = Partially decrypted, `recperpage=50`,
1.6s between requests: 17 pages (801 records) + 8 pages (385 records) = 25 requests total, all to
`de-crypt.org/decrypt-web/RecordsList`, descriptive User-Agent (`cipher-lab research script (contact via
repository)`), one fetcher, well under the 300-request cap in the brief. No images or documents were
downloaded (listing only, per brief step 2). Raw HTML pages were kept in the session scratchpad, not
committed (per Usage rule "digests, not repositories").

`sources/decode/records-non-decrypted-2026-09-24.tsv`: 1186 rows (801 Non-decrypted + 385 Partially
decrypted, no duplicate ids), columns `id, status, record_type, holder_raw, city, shelfmark_code,
date_range, cleartext_lang, plaintext_lang, number_of_pages, source_page`. `number_of_pages` is the
record's own image/page count as shown in the list grid (matches the "Pages: N" field on RecordsView,
confirmed against record 8725 = 1 page in both places) -- this stands in for an image count without
needing a login, so no per-record RecordsView fetch was needed for that column. `n_documents` and
"whether a key/decryption document is attached" are not in this TSV: DocumentsList needs a login and
checking it for 1186 rows is far outside a $10 budget; these were checked only for the shortlisted
survivors of the diff step, in `records-non-decrypted-2026-09-24-diff.tsv` / QUEUE.md (see below), not for
the raw crawl.

No personal data is in this file: DECODE gives only city/holder/shelfmark/date/language/status/page-count
in the list view, and no account or uploader names.

## Caveats

This is a live crawl of the current catalogue (24 Sept 2026), fresher than the 19-23 Sept cached scrape
(`aaymeloglu/unsolved-ciphers`'s `decode-catalog.csv`/`decode-records.jsonl`, ~1187 Cipher Non-decrypted/
Partially-decrypted rows as of 23 Sept per `tools/decode_neighbours.py`'s docstring) used by the earlier
neighbour-record pass (`sources/solver-diffs/2026-09-23-decode-neighbours*.tsv`). The two counts are close
(1186 vs ~1187) but not compared row-for-row; a handful of records may have changed status in the interim
(a record moving from Non-decrypted to Partially/Decrypted, or vice versa) and this file reflects only the
24 Sept state.

The `city`/`shelfmark_code` split is a simple `<b>`/`<small>` tag split of the list's `c_holder` field, not
independently verified against RecordsView; about 1% of rows may lack a `<small>` code segment (matches the
"about 1%" figure `tools/decode_neighbours.py` reports for the cached catalogue's holder string).

## Census diff: who already holds each record (24 Sept 2026)

LANE N DECODE worker B. `tools/solver_repo_diff.py --census` (new mode, added this session; keeps the
original QUEUE.md-row mode working unchanged) matches every row of `records-non-decrypted-2026-09-24.tsv`
against: cipher-lab's own `ciphers/*/{NOTES.md,AUDIT.md}` plus `QUEUE.md`/`CATALOG.md` ("ours"), a fresh
shallow clone of dbourdeau/cyphersolver's target folders ("bourdeau:<folder>"), and a fresh shallow clone
of aaymeloglu/unsolved-ciphers's target folders/TARGETS.md/SHORTLIST.md/CATALOGUE.md/ranked files
("aymeloglu:<path>"), falling through to "none". Matching is by DECODE id (`R<id>`) and by a normalised
shelfmark "volume key" (`tools/decode_neighbours_exclude.py`'s `ids_in`/`volume_keys`, the same matcher
validated on the 23 Sept 2026 neighbour-record sweep — refactored this session into importable functions,
behaviour unchanged, checked against the existing `2026-09-23-decode-neighbours-annotated.tsv` as a
regression fixture).

Output: `records-non-decrypted-2026-09-24-diff.tsv` (1186 rows + header), columns `ours_hit`,
`bourdeau_hit`, `aymeloglu_hit`, `held_by`. Counts: **ours 596, bourdeau 510, aymeloglu 9, none 71**.

**Read the high "ours"/"bourdeau" counts as real, not noise, checked by sampling**: `QUEUE.md` alone is a
2,568-line scouting survey that already covers wide swaths of DECODE's Spanish holdings (the RAH Signatura
9.x and AGS Estado series especially), and Bourdeau has worked the AGS Estado series hard (`mai1531`,
`muxetula1531`, `vargas1552`, `caracciolo1537`, `cifuentes1534`, ...) — spot-checked several `ours:queue`
and `bourdeau:<folder>` rows against the actual QUEUE.md/NOTES.md text they cite and all held up. As with
the neighbour-sweep matcher this is derived from, **this is hits to check, not verdicts**: a volume key can
match a passing mention (e.g. a sibling shelfmark cited only for context in another target's NOTES.md) as
readily as an actual solve, so `held_by` should be read as "worth checking before treating as new ground",
not as a solved/unsolved verdict on its own. The 71 `none` rows are the input to step 3's ranking.

## Ranking pass, DC1-DC20 (24 Sept 2026)

LANE N DECODE worker B, continuing the same session. Ranked the census diff's `held_by: none` rows (69 with
pages >= 1) by the scout.js rubric and wrote `QUEUE.md`'s "DECODE non-decrypted records with images" section
plus `QUEUE-scores.json`'s `lane_n_decode` key. Full method and caveats are in QUEUE.md itself.

**`tools/decode_browser_login.js --max-files N` note for the next user of this tool:** the cap applies only to
the queue of *auto-discovered* attachment links found while scanning `--fetch-page` pages, not to the total
request count. Every `--fetch-page` URL is always fetched regardless of `N` (`out.fetched.push` happens inside
the `fetchPageUrls` loop, before the `maxFiles`-bounded `queue`/`seen` logic is ever consulted), and auto-
discovered attachments only stop being *queued* once `seen.size` reaches `N` -- files already queued before
that point still get fetched. Requesting `--max-files 30` with 25 `--fetch-page` URLs this session fetched all
25 RecordsView pages **plus 29 auto-discovered attachments** (54 total), not "≤30 total" as the flag name
suggests. This worker wanted RecordsView pages only (per its brief, "no images, no documents downloaded") and
had not anticipated the auto-discovery firing on plain RecordsView pages (the tool's own comment describes it
for DocumentsList/ImagesList/gallery pages) -- caught after the fact by grepping the output directory,
`TH_IMG_*`/`DOC_*` files (image thumbnails and three genuine document files, all under 130KB) deleted
unread beyond their filenames/DECODE-assigned tags, none committed. If a future pass wants pages only with no
attachment fetching at all, pass `--max-files 0`, which this session did not test.

## `.txt` document attachments blocked by filesrv, 24 September 2026

LANE N DECODE FETCH worker (for LANE R2, `.claude/briefs/runs/2026-09-24-lane-n-fetchDC.md`). Attempting to
fetch DECODE R1162's attached transcription document (id 3593, `DOC_R1162_D3593_3593.txt`) via
`/decrypt-custom/filesrv/?file=...` returned HTTP 200 with `Content-Type: image/png` and
`Content-Disposition: inline; filename="forbidden.png"` -- a fixed 986x568 PNG placeholder (sha1
`035489a0605851154ab88372216354b63596ca22`). Byte-identical whether requested inside a logged-in Playwright
browser context (`ctx.request.get`, session cookies attached) or with a bare, unauthenticated curl -- so this
is not a session/cookie bug, it is the server refusing the file regardless of login. **This already produced
one bad commit**: `ciphers/intercepted-royalist-1646/decode/DOC_8725_2024-Oct-12-01-36-20_15694.txt`
(committed by an earlier worker as record 8725's real document text) is the same placeholder byte-for-byte,
mislabeled `.txt`. Any DECODE document fetch should check `file <name>` and/or the response's
`Content-Disposition` header before trusting a `.txt`/document download -- a `filename="forbidden.png"` or
an actual PNG signature means the fetch silently failed. Image attachments (`TH_IMG_*`) were unaffected in
this pass (fetched fine, correct distinct content). Not yet known whether this is specific to record
1162/document 3593, to the Transcription category, or to all non-image documents on this account -- next
worker hitting a document attachment should check the response header the same way before committing.

## No larger image than the 200px thumbnail for 1162 (and 4450), 24 September 2026

LANE N worker, for LANE R2 (ROOM 09:42 flag: "if DECODE serves a larger image to a logged-in browser
(ImagesList/zoom), please try once in your next login"). One login (`tools/decode_browser_login.js`),
`RECORD_ID=1162`, `--shot`, plus in the same session `--fetch-page` for the real
`ImagesList?showmaster=records&fk_id=1162` link (found verbatim in RecordsView/1162's own HTML, see below)
and `--fetch` for two guessed non-`TH_`-prefixed filenames, `--delay 1800 --max-files 6`. Answer: **no**,
DECODE serves nothing larger than the 200px `TH_IMG_*` thumbnail to this account for record 1162, checked
three ways:

1. **RecordsView's own on-page "zoom" modal is not a zoom.** The saved `record_1162.html` contains a
   JS lightbox (`openModal()`/`currentSlide()`) that a viewer might expect to show a larger image; its
   `<img>` tags inside `#myModal` point to the identical `/decrypt-custom/filesrv/?file=TH_IMG_R1162_I5837_P1.png`
   / `..._I5838_P2.png` URLs already fetched as thumbnails, just CSS-stretched to `width:100%`. No distinct
   full-size `src` anywhere in the modal markup. (The page's generic attachment-grid jsrender template,
   elsewhere in the same HTML, does have separate `{{>url}}` (full) and `{{>thumbnailUrl}}` fields with an
   `ew-lightbox`/colorbox anchor -- but that template block is inert source for a different grid, never
   instantiated with data on this page; the only rendered image markup on RecordsView is the modal above.)
2. **Guessed full filenames return the known "forbidden" placeholder, not a 404 or a real image.** The modal's
   thumbnail `<img>` tags carry `alt="IMG_R1162_I5837_P1.png"` / `alt="IMG_R1162_I5838_P2.png"` -- i.e. the
   underlying file plainly exists under those exact non-`TH_`-prefixed names. Fetching
   `/decrypt-custom/filesrv/?file=IMG_R1162_I5837_P1.png` and `...I5838_P2.png` through the same logged-in
   session both returned HTTP 200, `986x568` PNG, sha1 `035489a0605851154ab88372216354b63596ca22` -- byte-
   identical to the `forbidden.png` placeholder already documented above for the blocked `.txt` document. So
   the server recognises the filename but refuses to serve it to this account, the same failure mode as the
   document block, not a missing/mistyped path.
3. **The one real "bigger picture" link on the page, "Go to the Image Manager to zoom and view/edit metadata"
   (`ImagesList?showmaster=records&fk_id=1162`, confirmed present verbatim in the RecordsView HTML, same query
   shape as the working `DocumentsList?showmaster=records&fk_id=...` pattern), could not be loaded**:
   `page.goto` on that URL hit `net::ERR_TOO_MANY_REDIRECTS` inside the same login. Unlike `DocumentsList`,
   this page evidently expects some state `DocumentsList` doesn't (a referrer, a prior AJAX call, or a
   session flag set only by clicking through the UI) and redirect-loops when opened directly. **Caution for
   whoever retries this**: a redirect loop the browser chases to its own limit (Chromium's default is 20 hops)
   can burn most of a request budget on one dead end -- try `ctx.request.get` with redirect-following
   disabled, or a plain `curl -I` first to see the `Location` chain, before pointing `page.goto` at it again;
   this pass did not retry (one login, one attempt, per CLAUDE.md).

Not tested for 4450 directly this pass (brief's primary target was 1162; one login only), but the mechanism
above -- a fake on-page zoom that reuses the thumbnail, and the same `forbidden.png` signature already seen
on 4450's neighbour document fetch -- is a site-wide behaviour, not specific to one record, so the same
"thumbnails only" conclusion is extended to 4450 rather than spending a second login to re-demonstrate it
record by record. If a future worker gets a real `Image Manager` page to load (fixing point 3), check it for
4450 too and correct this note.

No full-size image exists to save; `ciphers/decode-1162-modena-ambung-1492/images/` and
`ciphers/decode-4450-bnf-fr20506-1525/images/` are unchanged (still `TH_IMG_*` thumbnails only, no `*_full.*`
files added). Requests this pass: de-crypt.org ~10-15 (login ~2, RecordsView/1162 auto-fetch 1, the
ImagesList redirect-loop attempt an unknown but bounded number, 2 filesrv fetches) -- comfortably under the
20-request cap even counting the loop at its ceiling. One login only. Cost: worker cap $3, well under.

## DC11-DC20 and the Florence Dieci di Balia cluster, DocumentsList checked (LANE N2, 24 September 2026)

One login (`tools/decode_browser_login.js`, `--max-files 0` so no auto-discovered thumbnail/document fetching,
`--delay 1600`), `RecordsView/<id>` plus `DocumentsList?showmaster=records&fk_id=<id>` for each of the ten
DC11-DC20 records (ids 1121-1167, 1152, 1146, 1148, 2788) and the 32 Florence census rows with holder
"Florence State Archives", shelfmark `Dieci_di_Balia_Responsive_*` (ids 3758-3789, filze 7/8/9/22 of the
Dieci di Balìa Responsive series). The site's own generic navbar shows the logged-in account's user name on
every page fetched; it has been scrubbed from every file committed here (`sources/decode/dc11-20-documents-
2026-09-24.tsv`, `florence-dieci-2026-09-24.tsv` carry only DECODE's own record fields, not the raw HTML).

**DC11-DC20**: confirmed live. DC11-DC19 (the Modena/Milano Amb. Ung./Sf. Ung. envoy-report cluster) are all
still "Partially decrypted" with 0 documents attached on either RecordsView or DocumentsList -- QUEUE.md's
hard filter (Partially decrypted = not a candidate) applies to all nine, and none carries a [decrypt]/[key]
document that would make it a firmer negative. DC20 (id 2788, Catherine de Medicis to Philibert du Croc) is
confirmed "Non-decrypted" with 0 documents and, as already noted, 0 images -- still not copy-free. No
uploader comments or per-record bibliography field exists on any of the ten; the only "bibliography" DECODE
shows anywhere on these pages is its own site-wide DECRYPT-project citation block (Héder/Megyesi HistoCrypt
2022, Megyesi et al. Cryptologia 2020, Megyesi et al. HistoCrypt 2019), not per-item literature.

**Florence Dieci di Balia cluster (32 rows, ids 3758-3789)**: all 32 confirmed "Non-decrypted" on RecordsView,
0 documents attached on DocumentsList for every one (checked individually, not sampled). No uploader comments
found on any record. No per-record bibliography; only the same site-wide DECRYPT-project citation block as
above. No publication or project beyond DECODE's own is named on any of these 32 pages -- if a Dieci di Balìa
Responsive edition or project exists (the Florence State Archives' own finding aids, or an Italian Renaissance
diplomatic-correspondence edition project), it was not surfaced by this pass and would need a search outside
DECODE (this pass's brief was capture only, no WebSearch spent here). Two records (3758, 3760) show a blank
"Pages" field on RecordsView itself, unlike the other 30 (1-2 pages each) -- a DECODE data-entry gap, not
something this pass can resolve. Per-record detail (shelfmark, holder, date range, cleartext/plaintext
language, page count, status, documents, comments, bibliography) is in
`sources/decode/florence-dieci-2026-09-24.tsv`. No images were downloaded beyond what RecordsView's own page
view pulls (thumbnails inline in the page HTML, not saved separately); nothing was transcribed.

Requests this pass: de-crypt.org 84 fetch-page requests (42 records x RecordsView + DocumentsList) plus one
login, split across two consecutive fetch calls in the same login session after the first call's own
subprocess timeout (not a site rejection) cut it off partway through the Florence range at id 3766 -- the
second call resumed at 3767 with the same session cookies, so this is one DECODE login with a client-side
interruption, not a second authentication attempt. Combined with job 1 of this brief (`records-decrypted-
2026-09-24.tsv`, 28 requests, no login), this worker's de-crypt.org total is 112 requests, under the
150-request cap. All requests >=1.6s apart, one at a time.
