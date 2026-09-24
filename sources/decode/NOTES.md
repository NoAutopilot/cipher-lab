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
