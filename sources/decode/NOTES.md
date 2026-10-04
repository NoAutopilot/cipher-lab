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

## Full-size images: account permission test (LANE N2 dcB), 24 September 2026

**Verdict: (b) blocked by permission.** Full-size DECODE page scans are gated to accounts our credentials do
not belong to; the gate is account-level, not per-record, per-uploader or a missing-image gap. Draft outreach
at `outreach/decode-image-access.md`; ASKS row filed (see below).

One login (`tools/decode_browser_login.js`, extended this session -- see "Tool changes" below -- rather than
written as a private script), `RECORD_ID=3754` (Bourdeau's florence1429 record, the one his own login fetched
a 5512x3674 full image from, per `ciphers/florence-dieci-responsive/NOTES.md` "Job 1"), `--fetch-page
RecordsView/3761,RecordsView/3758,personaldata`, `--guess-fullsize`, `--probe
"ImagesList?showmaster=records&fk_id=3754"`, `--delay 1700 --max-files 30`. 17 requests total (2 login,
1 primary RecordsView, 3 fetch-page, 6 filesrv fetches, 5 probe hops), well under the brief's 60-request cap.
Raw HTML/images kept in the session scratchpad, not committed (Usage rule 3, "digests not repositories"); the
navbar's account-name string was in `personaldata.html` (as CLAUDE.md's DECODE section warns) and is not
quoted anywhere below or committed to this file.

**1. Filesrv full-size fetch, three records (R3754, R3761, R3758).** Each RecordsView page's zoom-modal
`<img alt="IMG_R<record>_I<internal>_P.jpg">` names the underlying full-size file without the `TH_` prefix
carried by the thumbnail `<img src>` (`TH_IMG_R<record>_I<internal>_P.jpg`) -- confirmed by grepping the three
saved pages, `alt="IMG_R3754_I23011_P.jpg"`, `alt="IMG_R3761_I23018_P.jpg"`, `alt="IMG_R3758_I23015_P.jpg"`,
matching the `--guess-fullsize` flag's own derivation exactly. Requesting each un-prefixed name through
`/decrypt-custom/filesrv/?file=<name>` in the same logged-in session returned, for all three:

| record | thumbnail (real) | "full-size" request | sha1 | size/dims |
|---|---|---|---|---|
| R3754 | `TH_IMG_R3754_I23011_P.jpg`, 9165 bytes, distinct JPEG | `IMG_R3754_I23011_P.jpg` | `035489a0605851154ab88372216354b63596ca22` | 17947 bytes, PNG 986x568 |
| R3761 | `TH_IMG_R3761_I23018_P.jpg`, 16488 bytes, distinct JPEG | `IMG_R3761_I23018_P.jpg` | `035489a0605851154ab88372216354b63596ca22` | 17947 bytes, PNG 986x568 |
| R3758 | `TH_IMG_R3758_I23015_P.jpg`, 3852 bytes, distinct JPEG | `IMG_R3758_I23015_P.jpg` | `035489a0605851154ab88372216354b63596ca22` | 17947 bytes, PNG 986x568 |

All three "full-size" responses are the same sha1 as the `forbidden.png` placeholder already documented above
(the blocked `.txt` attachment on R1162/D3593) -- byte-identical to each other and to that placeholder, HTTP
200, `986x568` PNG, `Content-Disposition: inline` (per that earlier finding's header check; not re-verified
per-header this pass since the sha1 match alone is conclusive). The three real thumbnails are genuinely
distinct (different byte counts, different pixel dimensions per `file`), so the server can and does tell these
three records' images apart -- it simply refuses the un-prefixed name for all three, including **R3754**, the
exact record whose full image Daniel Bourdeau's own DECODE login *did* fetch (5512x3674, per
`ciphers/florence-dieci-responsive/NOTES.md`). Same record, same file, two different DECODE accounts, two
different results: this is not "no image was ever uploaded for this record" (Bourdeau's own notes prove one
exists) and not a per-uploader quirk of the Florence cluster specifically (R3754 isn't Florence) -- it is this
account being refused a file another account can read.

**2. ImagesList probe (`--probe`, `maxRedirects: 0`, no `page.goto`).** For R3754's
`ImagesList?showmaster=records&fk_id=3754` (the "Go to the Image Manager to zoom and view/edit metadata" link,
present verbatim in RecordsView's own HTML, same as documented for record 1162 above): the Location chain,
read without ever following a redirect automatically, is

```
GET ImagesList?showmaster=records&fk_id=3754        -> 302 Location: /decrypt-web/login
GET login                                           -> 302 Location: /decrypt-web/ImagesList?showmaster=records&fk_id=3754?showmaster=records&fk_id=3754
GET ImagesList?...?showmaster=records&fk_id=3754    -> 302 Location: /decrypt-web/login
GET login                                           -> 302 Location: /decrypt-web/ImagesList?...(query string doubling again)
GET ImagesList?...                                   -> 302 Location: /decrypt-web/login   [stopped at 5 hops, per brief]
```

This is a real finding, not the generic `ERR_TOO_MANY_REDIRECTS` a browser's own redirect-follower reports (the
1162 pass hit that limit at Chromium's 20-hop ceiling without ever seeing why): DECODE's server treats our
**already-authenticated** session (the same cookies that load RecordsView, DocumentsList and Personal Data
without issue) as unauthenticated specifically for `ImagesList` -- it redirects straight to `/login`, and
`/login` bounces back to the *same* `ImagesList` URL with its own query string appended a second time (a bug in
the login page's own return-URL handling, not something this account can route around). Since the failure mode
is "not logged in" rather than "logged in but refused," a plain GET is missing a prerequisite `ImagesList`
wants and `RecordsView`/`DocumentsList` don't -- consistent with `ImagesList` (the Image Manager) sitting behind
a separate permission check that this account's login does not satisfy, on top of (not instead of) the filesrv
block already shown in step 1. The brief's fallback ("reach it by clicking through the UI from RecordsView
instead of `goto`") was not attempted this pass to respect the brief's "ONE login" cap -- it would need a
second script invocation with the newly-added `--click` option (see below) or folding into a single combined
run; flagged here as the next concrete step for whichever worker next holds the DECODE login, since the same
result (redirect to `/login`) for a URL taken verbatim from an authenticated page's own HTML already answers
"is this reachable by a plain request" (no), and a click only tests whether the UI supplies some referrer or
prior AJAX call a script doesn't -- worth one try, not yet done.

**3. Profile/permissions and help/terms pages.** `/decrypt-web/personaldata` (the only per-account settings
page linked from the navbar's user menu, alongside `/decrypt-web/changepassword`) shows no role, tier or
access-level field of any kind -- its entire visible content is: *"Your account contains personal data that
you have given us. This page allows you to download or delete that data. Deleting this data will permanently
remove your account, and this cannot be recovered."* with Download/Delete buttons (a GDPR data-control page,
not a profile). No "researcher" vs "guest" wording, no request-access button, no upload-owner rule is stated
anywhere in the authenticated UI reached this pass. The navbar's "Administration" menu (visible only because
we are logged in at all) exposes exactly one item, "Record Group" (`/decrypt-web/RecordGroupList`) -- no
"Users"/"Logins"/"Permissions" list is offered to this account, meaning it is a plain non-admin member with no
in-UI path to request or grant itself elevated image access. No help or terms-of-use page is linked anywhere in
the authenticated interface (navbar, sidebar, user-menu, footer) beyond the standing DECRYPT-project citation
block (Héder/Megyesi HistoCrypt 2022, Megyesi et al. Cryptologia 2020, Megyesi et al. HistoCrypt 2019) already
noted above -- if DECODE documents an image-access permission tier anywhere, it is not reachable from inside
de-crypt.org itself with this account, and this brief's host restriction (de-crypt.org only) means the
project's own public site (cl.lingfil.uu.se) was not checked for it this pass.

**Tool changes (`tools/decode_browser_login.js`):** added `--guess-fullsize` (derives each thumbnail's
un-prefixed full-size filename and queues it, used in step 1), `--probe URL[,...]` (`maxRedirects: 0`,
manual up-to-5-hop redirect chain via `ctx.request.get`, used in step 2, never `page.goto`), and `--click
"PAGE_URL|LINK_TEXT"` (navigate, click the first link containing that text, save wherever it lands --
built for the step-2 fallback above but not yet exercised). All three are additive and off by default;
existing callers are unaffected. New offline test `tools/tests/test_decode_browser_login_guessfullsize.py`
(no network, no credentials) covers `guessFullsizeName`/`scanFilesrvLinks`; the existing `--help` and
`safeFilename` tests still pass unchanged.

**What this means for LANE N2/copy-free scoring:** the recommendation in
`ciphers/florence-dieci-responsive/NOTES.md` "Job 1" to re-run the login against ids 3758-3789's `ImagesList`
pages is now answered without needing to spend a second login on the Florence cluster specifically -- the
block demonstrated on R3754/R3761/R3758 is an account-wide gate (step 1 uses a non-Florence record precisely
to show this), so the same six filza-7 ids (3758, 3759, 3760, 3761, 3762, 3763) would return the same
`forbidden.png` placeholder. **No images were fetched into `ciphers/florence-dieci-responsive/images/`** and
none of DECODE's held copy-order rows become copy-free from this route. `outreach/decode-image-access.md`
drafted (subject/recipient/sign-off left blank) asking whether image access can be granted to this account,
citing this section; ASKS.md row added for the owner to send it once reviewed.

Requests this pass: de-crypt.org 17 (2 login, 1 primary RecordsView, 3 fetch-page, 6 filesrv, 5 probe hops),
all >=1.6s apart, one at a time, well under the 60-request cap. No other hosts. One login.

**Confirmed from the owner's own browser, 24 Sept 2026 16:50 UTC:** logged in as the account in Chrome on the owner's machine,
record 3754's page image opens as the same "Insufficient permissions to so see the full image" placeholder
(IMG_R3754_I23011_P.jpg), thumbnail fine. So the full-size block is an account role, not a session, proxy or browser
issue; no worker should retry it. The request for a role upgrade (both asks in one email) went to the DECRYPT project
mailbox on 24 Sept 2026 (CONTRIBUTIONS.md); until it is answered, DECODE gives thumbnails and record text only.

## Access mode field tested, and the bounced addressee fixed (DECODE-ACCESS, 26 September 2026)

Parent worker DECODE-ACCESS (`.claude/briefs/runs/2026-09-26-parent-decode-access-mode.md`), for parent 7e. The
owner reported the 24 Sept 2026 access-request email (ASKS row 42/43, CONTRIBUTIONS.md) bounced. Two questions:
does the "Access mode" field explain the block as a per-record holding-archive restriction rather than our
account's role, and where should the request actually go.

**1. Verdict: account-wide role, not a per-record restriction.** Every DECODE record checked shows "Access
mode: Authentication required", with no exceptions found. Login-free, plain curl, >=2s apart, 21 RecordsView
fetches (`sources/decode/access-modes-2026-09-26.tsv`) spanning six different holding institutions and two
different legal jurisdictions -- BnF (2077, 9451), British Library (8395, 8398, 9227, 8483, 9225), BAV Vatican
(215, 221, 233, 301, 10, 149), AAV/ASV (5622), Archivo General de Simancas (9963, 9960), Österreichisches
Staatsarchiv (1601, the brief's own Vienna example, and 1212), and Florence State Archives (3754) -- plus four
more already on file from earlier sessions (8725, and the 24 Sept BL cluster in `ciphers/boswell-1628/NOTES.md`,
`ciphers/intercepted-royalist-1646/NOTES.md`, `ciphers/randolph-sussex-1569/NOTES.md`), 25 records total, zero
variation. DECODE's own advanced-search filter for this field is a no-op: `RecordsList?x_access_mode=1&z_access_mode=%3D&cmd=search`
and `...=2...` both return the same 10,106-record total as the unfiltered listing (unlike `x_status`, which
genuinely filters, per `tools/decode_list.py`'s own finding) -- the site gives no way to search for a record with
a different access mode, consistent with there not being one to find. The "Additional Information: the image is
not in the public domain, publishing it is only possible with the permission of the archive/Library" note that
accompanies many (not all) of these records is boilerplate explaining why a login is required *at all* -- it
names whichever institution holds the item ("archive"/"Library" interchangeably) but reads identically across
totally unrelated holders (BnF, BAV, AGS, ÖStA, BL), and it is present on records our account CAN read the
thumbnail of and absent on some records (215, 221, 233, 301, 10, 149) that are just as firmly blocked -- it does
not track the placeholder outcome. It is not the same signal as the "Insufficient permissions to see the full
image" error DECODE shows when an image is actually requested, which is an account-role message, not an
archive-copyright message.

One login (`tools/decode_browser_login.js`, the single-attempt rule), record 2077 (the Marie de Medicis key,
ASKS row 43's blocker, never before login-tested) plus `--fetch-page RecordsView/8395` (the Barriere target),
`--guess-fullsize`, `--delay 1800 --max-files 10`: all 5 of 2077's guessed full-size filenames
(`IMG_R2077_I14888_P1.png` through `I14892_P5.png`) came back sha1 `035489a0605851154ab88372216354b63596ca22`,
986x568 PNG -- byte-identical to the placeholder already confirmed for R3754/R3761/R3758/R1162/8725/413/4930/
1172/1180, extending the same account-wide result to a fifth+ holding institution (BnF) and directly to ASKS row
43's target. 8395's thumbnails fetched fine (real, distinct images); its own guessed-fullsize names were not
requested this pass (kept the login to 10 requests, well under the 60-request cap, one at a time, >=1.8s apart).
No public/open-mode record existed to run the brief's intended public-vs-authenticated contrast (finding 1 above
is why), so the login was spent on a fifth, previously-untested holder plus a directly-blocked target instead,
which answers the same question (does this account's block correlate with the record's own terms, or not) with a
fifth negative data point rather than a repeat of Florence/Vienna/BL. Combined with the existing R3754
cross-account proof (Bourdeau's own login reads the identical file at 5512x3674; ours gets the placeholder) and
the owner's own browser reproducing "Insufficient permissions to see the full image" (24 Sept 2026 16:50 UTC),
the verdict is **account-wide role**, not per-record archive terms: CLAUDE.md's DECODE host-table row already
says this ("a role/permission gate, not a route problem"), so no correction is needed there.

**2. Why the email bounced, and the fixed addressee.** de-crypt.org's own home page footer (`id="contact"`) has
the block naming `decode@stp.lingfil.uu.se` **commented out** in the live HTML
(`<!--  <div class="block-5"> <span class="title-footer">Contact</span> ... decode@stp.lingfil.uu.se ... --> `,
read 26 Sept 2026) -- the site itself has stopped publishing that address, even though `termsofuse.php` (a
separate, apparently unmaintained page) still shows it uncommented. The live footer instead names, with no email
for either: Principal Investigator Prof. Beáta Megyesi, Stockholm University, Department of Linguistics, Sweden;
Hosting/System administrator Mihály Héder, Budapest, Hungary. This matches the brief's note that the PI moved to
Stockholm University -- the Uppsala mailbox (`lingfil.uu.se` is Uppsala's Department of Linguistics and
Philology) is very likely dead because of that move, which is the simplest explanation for the bounce.

Stockholm University's own staff directory gives Prof. Megyesi's current institutional address, read 26 Sept
2026: `beata.megyesi@ling.su.se` (`https://www.su.se/english/profiles/beba5639`, "Beata Megyesi - Stockholm
University", found via `www.su.se/english/search?query=megyesi`). This is a public-facing university staff page,
not a private individual's personal contact (CLAUDE.md rule 9/Access playbook item 4's "never a private
individual's address" is about people outside an institution, e.g. a dealer or a private owner; a professor's
university directory listing is the institutional contact for her role, the same category as an archive's own
"contact us" address). `outreach/decode-image-access.md`'s recipient line is updated to this address, dated, in
place of the generic "DECODE maintainers via the site or Personal Data page" line and the dead Uppsala address.
ASKS.md row 42 updated with the addressee fix and this verdict.

Also worth flagging, not part of this job's mandate: the DECRYPT project's own public "About" text says "all
records in the database are open to the public" -- in clear tension with the account-wide full-image block this
and prior sessions have confirmed. Worth quoting back verbatim if a reply from Megyesi/Héder disputes that a
role gate exists at all.

Requests this pass: de-crypt.org 21 RecordsView (login-free, sample) + 3 (search-form/filter-probe reads,
login-free) + login-session (2 login, 1 primary RecordsView, 1 fetch-page, 10 filesrv fetches) = 37, all >=1.5-2s
apart, one at a time, well under the 40-request login-free cap and the 60-request login-session convention. One
login. `su.se` 5 requests (2 search, 1 profile redirect, 1 profile, 1 staff-listing 404), >=1.5s apart, well
under any per-host cap. No credentials printed.

## Full-size images: access after the PI's extension (28 Sept 2026)

**Verdict: access works.** DECODE-OPEN (parent worker, owner account, session_015RJ8kumxcx2XKtHHU1zzsU), one login
through `tools/decode_browser_login.js` (real browser; `loggedIn: true`) at 14:54 UTC, 28 Sept 2026, repeating the
24 Sept test on record 3754 with `--guess-fullsize`:

| file | status | bytes | format / dims | sha1 |
|---|---|---|---|---|
| `TH_IMG_R3754_I23011_P.jpg` (thumbnail) | 200 | 9165 | JPEG | `47182c087ff704eb1bb9743e710ddb5b97032f0d` |
| `IMG_R3754_I23011_P.jpg` (zoom-modal alt name) | 200 | 16287379 | JPEG 5512x3674 | `71272e28743fa57c80391f3e3f1d48d4911e92b8` |

The full-size file is **not** the `forbidden.png` placeholder (`035489a0...`, 17947-byte 986x568 PNG): it is a
16.3 MB JPEG at 5512x3674, the same dimensions Bourdeau's own login fetched for this record
(`ciphers/florence-dieci-responsive/NOTES.md` "Job 1"). The account-role block of 24 Sept 2026 is lifted.
Images stay in the session scratchpad, never in this repository (the PI's reminder: the holding archive's
permission may be needed before any image is published).

Tool change: `tools/decode_browser_login.js --listen CMDFILE` keeps the one logged-in context open and takes
`page URL` / `get URL` lines from a command file, so a job whose later URLs depend on pages read earlier still
uses a single login.

### Formerly blocked records, full-size test (DECODE-OPEN, 28 Sept 2026)

Same login (listener mode), 15:01-15:05 UTC (file times; login at 14:54, Mercy records 14:54-14:57). For each record: its RecordsView page, then the first full-size
image named in its zoom-modal alt text. Every one came back a real image, none the placeholder (all sha1s differ
from `035489a0...`); images are in the worker's scratchpad only, never committed.

| record | item (DECODE name, status) | images | first full-size file: dims, sha1 (12) | what it unblocks |
|---|---|---|---|---|
| R5005 | Zeschau to Seebach 18.01.1841, HStAD 10731 Nr. 12 (Partially) | 6 | 7214x5412 JPEG, f75e920f9eb2 | the rubbed pencil gloss Bourdeau read, at full size |
| R5006 | same, 06.04.1842 (Partially) | 2 | 7214x5412, 483bbb1d719f | first ciphertext transcription on disk (none exists), then Bourdeau's 7 syllabary values tried (ASKS 64) |
| R5007 | same, dated 13.06.1846 in DECODE's name (Partially) | 2 | 7214x5412, b5ec8e9e93cd | as R5006 |
| R5008 | same, 26.10.1843 (Partially) | 2 | 7214x5412, 86e6105b60fe | as R5006 |
| R4931 | BL Cotton MS Caligula C II f.277 (Non-decrypted) | 2 | 7280x10152, c60e24407f97 | rule-2 check of our f.277 transcription |
| R4932 | BL Cotton MS Caligula C II ff.278-279 (Decrypted) | 4 | 7343x10055, 8de6b4a0c42f | the contemporary decipherment on f.278 that `randolph-sussex-1569` calls found-solved but never saw (bl.digirati.io blocked) |
| R9634 | BRAH Salazar 9/26 no. 2 (Non-decrypted) | 3 | 3256x2365, c7a149da7b40 | the only ciphertext of R9634 anywhere (no transcription exists, lope-hurtado NOTES l.174) |
| R9646 | BRAH 9/26 no. 15 (Non-decrypted) | 1 | 3440x2465, f58bbb5be686 | image check of the lope-hurtado R9646 work |
| R9649 | BRAH 9/26 no. 18 (Non-decrypted) | 3 | 3496x2465, 2cc8b6062f40 | same, R9649 |
| R1172 | BNE MSS/20211 item 123 (Non-decrypted) | 2 | 1114x1520 PNG, 11442cec6e3e | the target's own ciphertext at modest resolution (larger than the thumbnail, far smaller than the other hosts' scans) |
| R1180 | BNE MSS/20211 item 126 (Decrypted) | 3 | 1123x1549 PNG, 57e0a770a907 | the sibling's decipherment pages: a crib or partial key for item 123 (ASKS 45) without Tomokiyo 2018 |
| R9586 | ASN Esteri 2337 no. 37 (Non-decrypted) | 3 | 3056x4592, 940803e5b06a | rule-2 check of Bourdeau's castelcicala transcripts |
| R9587 | ASN Esteri 2337 no. 38 | 3 | 2935x3599, 156bdb616cdd | same |
| R9588 | ASN Esteri 2337 no. 39 | 2 | 3056x4592, cef33e2577e1 | same |
| R2859, R2860, R2865, R2866 | Yale Beinecke OSB MSS fc37 (Decrypted) | 4 each | 4157x5812, 4143x5812, 4349x5899, 4330x5950 (046d79b99bfa, a9e0e1b935b2, 2c7f4a849fc6, 4bf1d417724e) | image check of the Manchester word-code letters (already found-solved) |
| R4282, R4284 | Riksarkivet Chifferklaver låda II:113, II:114 (Non-decrypted) | **0** | -- | nothing: DECODE holds no image for either; riksarkivet-r4282-1628 still needs Riksarkivet's own route |

**Ranked by what a full image would unblock (for the orchestrator to turn into rows after the sprint; breadth is
frozen until 29 Sept 21:00 UTC):**

1. **zeschau-seebach-1841** (R5005-R5008, ASKS 64): three letters with no ciphertext on disk anywhere now have
   7214x5412 scans; transcribing R5006-R5008 lets Bourdeau's seven recovered values be tried on new material.
2. **bne20211-ferdinand-1478** (R1172, R1180, ASKS 45): the Decrypted sibling's three pages may give a crib or a
   partial key for item 123 without the academia.edu article; resolution is modest (about 1100x1500).
3. **lope-hurtado-1522** (R9634, R9646, R9649): R9634's ciphertext exists nowhere else; the other two get an image check.
4. **randolph-sussex-1569** (R4931, R4932): the found-solved verdict rests on Bourdeau's reading of f.278; the
   f.278 image can now be checked by us (rule 2).
5. **castelcicala-1816** (R9586-R9588): rule-2 check of Bourdeau's transcripts behind a `partial` target.
6. **beinecke-manchester-1699-1700** (R2859-R2866): image check only; the group is already found-solved.
7. **riksarkivet-r4282-1628** (R4282, R4284): nothing, since DECODE has no images for these records.

Requests this job: de-crypt.org 73 (2 login, 1 primary RecordsView, 2 image fetches in the login run, 68 in the
listener: 28 record pages, 5 documents, 35 images), all 1.7 s or more apart, one at a time, one login. No
other hosts.

## Key listing completed: N/A page 58 (OLD-DKEY, 2 Oct 2026)

`keys-all-2026-09-28-merged.tsv` lacked exactly one page of the status-N/A key crawl (page 58, ids 6097-6146, 50
Florence ASF records -- the H18 seam between the first session's pages 1-57 and the resumed pages 59-128). Fetched
2 Oct 2026 with `tools/decode_list.py --status n/a --record-type key --start-page 58 --max-pages 58` (note:
`--max-pages` is the last page to fetch, not a count from `--start-page`; and `--raw-dir` fails on the status name
`n/a` because the slash becomes a directory) into `keys-na-p58-2026-10-02.tsv`. The two files together are all 6,374
key records DECODE listed on 2 Oct 2026 (N/A 6,351, Decrypted 19, Non-decrypted 4 -- the N/A total unchanged since
28 Sept). 5 listing requests this session, 1.6 s apart, no login. Dutch-holder screen for 1595-1615 in
`ciphers/oldenbarnevelt-brederode-1605/decode_keys_1600s.tsv`.

## KEY1629-XMATCH (4 Oct 2026, account 3)
21 login-free RecordsView pages (R1193, R4104, R4118-4120, R4130, R4131, R4138, R4298-4301, R4303, R4305, R4313, R4315, R4334,
R5037-5040), 1.6 s apart, all HTTP 200, IS_LOGGEDIN false, saved in key1629-xmatch-2026-10-04/ with summary.txt (dates,
languages, "Additional Information" text). Purpose and result: ciphers/riksarkivet-r4282-1628/NOTES.md "KEY1629-XMATCH".
