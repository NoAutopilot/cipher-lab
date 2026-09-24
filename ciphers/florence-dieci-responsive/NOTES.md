status: blocked

# ASFi, Dieci di Balìa, Responsive filze 7, 8, 9, 22 (32 DECODE records, ids 3758-3789)

Session of 24 September 2026 (LANE N2 worker csFL, session_012KVppnGmB2br8F4tiBCHr7), following the probe in
QUEUE.md "Florence, Dieci di Balìa Responsive (LANE N2 probe of 24 September 2026)" (worker flFI). That probe
established: no full-size image of any of the three named filze (7, 9, 22) on any public host tried; filza 7
is named on the first page of Gabbrielli's 1863-64 key volume (Yale Dataverse, Ilardi reel 58, CC0) alongside
filze 1, 2, 3, but without filza-7-specific letter numbers; filze 9 and 22 are unconfirmed either way (reel 58
pages 5-54 unread by that pass). This session's three jobs, in the time available before the shared rate-limit
window closed (06:34 UTC start, hard stop 11:10 UTC per COMMON RULES; claimed at 10:48, this note written by
~10:56 -- roughly 8 minutes of working time, well under the $6 cap).

## Job 1: how Bourdeau's florence1429/florence1414 got their images, and whether the route serves filze 7/8/9/22

Shallow-cloned `dbourdeau/cyphersolver` (depth 1, `/tmp/csolver`, grep/read only, not committed here) and read
`florence1429/NOTES.md` and `florence1414/NOTES.md` in full (both target folders only, per brief).

- **florence1429** (DECODE R3754, filza 2 no. 171, the Ricasoli letter, solved on Bourdeau's own index per his
  GitHub Pages site, confirmed by WebSearch snippet quoting his finished reading of "Madonna è pure femina e
  sospetosa"): the image (`IMG_R3754_I23011_P.jpg`, 5512 x 3674 px) was "fetched with Daniel's DECODE cookie" --
  i.e. Daniel Bourdeau's own DECODE login, not a public route. Three sibling images from the same key
  (R3753/3755/3756/3757, filza 1 no.72 and filza 3 nos.21/91/92) were fetched the same way, all comparable
  resolution (4010 x 4765 etc.). **DECODE does serve full-size page scans once logged in** -- this is not a
  20 Sept 2026 update to the record, it is the ordinary record-image route, just gated behind login the way
  CLAUDE.md's Access playbook already describes for DECODE generally.
- **The filename pattern `IMG_R<decode_record_id>_I<internal_image_id>_P.jpg` is Bourdeau's own local renaming
  after fetching, not confirmed to be DECODE's raw URL** -- his repo's code was not inspected (out of this
  brief's "grep/README/NOTES only" scope) and is MIT so could be read later if useful, but the notes themselves
  don't show the fetch call.
- **Our own tooling already has the matching route and it was not used on this cluster.** `tools/
  decode_browser_login.js` documents fetching "DocumentsList, ImagesList, RecordsList" sub-pages per record and
  then following any `/decrypt-custom/filesrv/?file=...` attachment links found in their HTML -- i.e. the image
  route is `ImagesList?showmaster=records&fk_id=<record_id>` (the same query-string shape as `DocumentsList`,
  confirmed in `tools/decode_fetch.sh`'s comments and in `sources/decode/NOTES.md`'s description of the
  DocumentsList calls). **dcA's pass on this same 32-record cluster (`sources/decode/NOTES.md`, 24 Sept 2026)
  fetched RecordsView + DocumentsList for all 32 but never ImagesList** -- so "0 documents, no images downloaded"
  in that note is accurate for what was checked, not evidence that no image exists. **Recorded here for the
  next DECODE-login worker (per this brief's instruction; this worker has no DECODE login):** re-run
  `tools/decode_browser_login.js` (or equivalent) against ids 3758-3789 with `--fetch` pointed at each record's
  `ImagesList?showmaster=records&fk_id=<id>` page, and follow any `filesrv` links found -- if DECODE's page
  scans for this fondo are full resolution the way Bourdeau's are, this would make some or all of filza 7/8/9/22
  copy-free by LANE N2's own definition ((d) in the brief's additions: a full-size image served online now),
  since DECODE is "online now" once the standing login works, the same way it already counts for other LANE N2
  DECODE targets. This is a recommendation to test, not a confirmed route for these specific ids -- no image
  was fetched or seen this session.
- Neither Bourdeau target names filza 7, 9 or 22 specifically; confirmed again this session (grep for "filza 9",
  "filza 22", "Responsive_9", "Responsive_22", "Responsive 9", "Responsive 22" in the full clone: zero hits
  outside florence1429/florence1414 themselves, which don't use those strings either). `aaymeloglu/
  unsolved-ciphers` was not re-cloned this session (flFI's probe already found no Florence target there;
  not re-checked, budget).

## Job 2: Gabbrielli's 1863 key volume vs. our 32 records

Fetched (not previously on disk in this repo) five more pages of the Yale Dataverse set (`doi:10.60600/YU/
XKVOWE`, CC0) via its API file list and `access/datafile/<id>`, 1.6s apart, saved to `sources/florence/keys/`:
`58-5.pdf` (key 3, "Johannes", 1424, filza 7), `58-6.pdf` (key 4, "Zaninus et Conradinus", 1424, filza 7), and
the three index pages `58-index1.pdf`, `58-index2.pdf`, `58-Index3.pdf`.

- **Both filza-7 keys (3 and 4) are read (image, not transcription).** Each is a Latin syllabic
  nomenclator-style cipher, near-identical letter/syllable table to the other (same alphabet skeleton, same
  Roman-numeral and short-word codes for "que/ra/is/est/set/sum/ad/gent/...", "au/ef/in/ter/gif/ad", etc.) --
  consistent with two related senders (Johannes; Zaninus et Conradinus) using variants of one house cipher, the
  same pattern as Ricasoli's own two ciphers on pages 1-2. **Neither page gives a specific letter number for
  filza 7** the way page 1 gave filza 1/2/3 numbers for Ricasoli's cipher (only the heading "Cifra ... Carteggio
  dei X di Balìa, filza N°.7, an.1424" is written, no margin note of which items the key was built from). So
  this pass **cannot yet confirm which, if any, of our six filza-7 DECODE records (ids 3758-3763, old numbers
  059, 061, 066, 070, 071, 102) either of these two keys applies to** -- that needs the actual filza-7 letter
  images (not available, job 1/see below) tested against these two tables, or Gabbrielli's vol. II sender index
  (per florence1414/NOTES.md, not digitised anywhere found).
- **58-index1/2/Index3 are not a filza-indexed table of contents.** index1's right-hand page is only the
  volume's title leaf ("Indice degli scrittori in cifra del carteggio dei Dieci di Balìa"); Index3 (and, by the
  same hand and layout, presumably index2, not fully read this pass -- budget) is an alphabetical sender index
  (Alberti, Adimari, ... under "A", "B") giving **years 1524-1559 and page/carta numbers, not filza numbers** --
  this index covers the later part of Gabbrielli's volume (the fondo runs to 1530 per the dataset description),
  decades after filza 7/9's 1424-on items and outside what the 45-of-150 ciphers reel 58 actually contains in
  full image; it does not resolve filza 9 or 22 either way. **Reel-58 pages 7-51 (the bulk of the 54-page set)
  remain unread** -- neither confirming nor ruling out a filza 9 or filza 22 key inside the ~45 ciphers Gabbrielli
  did image (this pass fetched and read only the two named filza-7 keys plus the index pages, per budget).
- No cross-match to our 32 `filza_carta` values was possible beyond "filza 7 has two named ciphers, no letter
  numbers given; filza 8/9/22 not found in what was read."

## Job 3: check-solved per filza cluster

Searched (WebSearch only this pass; no time/budget left for a Google Books or JSTOR sweep -- flagged below):
"Dieci di Balìa" Responsive filza 9/22 cifra 1424/1425/1426 (no hit naming either filza or a decipherment); "
Somogyi 2016 Gabbrielli cipher Dieci di Balia" (returned an unrelated 2016 Somogyi cipher paper on a different,
1489-90 Sforza correspondence -- the "Somogyi 2016" citation in QUEUE.md/florence1429/NOTES.md for *this* fondo
is not corroborated by this search and should be treated as unverified pending a direct look at the Bourdeau
citation's source, not as a real analysis of Gabbrielli's Dieci di Balìa key; flagged, not corrected here since
that citation is in another target's files, not this one's). Tomokiyo's Italian pages (`sources/cryptiana/`)
were not searched this pass (budget) -- **outstanding for the next worker**. Guasti's *Commissioni di Rinaldo
degli Albizzi* (relevant to the 1420s Florence-Milan war correspondence generally) was checked by
`florence1414/NOTES.md` for 1414 material only, not specifically for filza 7/9/22's likely-1424-30 letters --
also outstanding. No standard printed edition or calendar of the Dieci di Balìa's *Responsive* series
(letters received, as opposed to Legazioni e commissarie's outgoing instructions, which are calendared/edited
in Guasti) was located for any of the four filze.

**Verdict: `blocked`, all four filze (7, 8, 9, 22), per COMMON RULES rule 9** -- no standard edition or
calendar for the *Responsive* series was located or read (only the outgoing Legazioni e commissarie side has
one), so an "open" verdict cannot be written yet regardless of the image and key findings above. No nomination
line posted (rule: nomination lines only for stage-2 "Verified unsolved" verdicts; `blocked` is not stage-2).
Filza 7 is the strongest candidate for a future `recovery`-kind nomination once (a) a filza-7 letter image is
obtained (job 1's ImagesList route, above) and (b) it is tested against keys 3/4 here and Ricasoli's own key
(florence1429), and (c) Guasti/Tomokiyo/Google Books/JSTOR are swept for the *Responsive* series specifically --
none of that is done here.

## Files

`sources/florence/keys/58-5.pdf`, `58-6.pdf`, `58-index1.pdf`, `58-index2.pdf`, `58-Index3.pdf` (new this
session; `58-3.pdf`, `58-4.pdf` etc. from the 18/23 Sept passes are in the Bourdeau clone, not this repo, since
that clone was not committed).

## Per-host counts

dataverse.yale.edu: 6 (1 dataset-metadata API call, 5 file downloads, all >=1.6s apart, all HTTP 200 after
following a 303 redirect). github.com: 1 shallow clone (`dbourdeau/cyphersolver`, depth 1, grepped/read only,
not committed; `aaymeloglu/unsolved-ciphers` not recloned this pass). WebSearch: 2 queries. No de-crypt.org,
no archive.org (not this worker's IA slot), no Google Books (out of scope).

## Next steps (not done here, budget/window)

1. DECODE-login worker: fetch `ImagesList?showmaster=records&fk_id=<id>` (not just RecordsView/DocumentsList)
   for ids 3758-3789 and follow any `filesrv` attachment links -- job 1's recorded route.
2. Read Yale reel-58 pages 7-51 for a filza 8/9/22 key (this pass only read 5-6 and the index leaves).
3. Search `sources/cryptiana/` (Tomokiyo) and Guasti's *Commissioni di Rinaldo degli Albizzi* specifically for
   filza 7/9/22 or the *Responsive* series (not just the 1414 material florence1414 already checked).
4. Verify the "Somogyi 2016" citation independently before repeating it for this fondo (flagged above).
