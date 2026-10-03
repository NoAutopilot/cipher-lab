status: open
Guasti, *Commissioni di Rinaldo degli Albizzi* vol.3 (1867-73 ed., Florence 1873; IA bub_gb_ZsSBc8CtYB8C, 69,631 lines of OCR) and vol.2 (bub_gb_3ZkvD-9ug8IC, 37,833 lines) full-text searched by this worker on 3 Oct 2026 for "Guasto", "Aymone"/"Aimone", "Fibindac", "Zaninus", "Tomaso", "Neri Capponi", "26 di dicembre", "buona dispos" and "cifra": the 26 Dec 1430 letter of filza 8 c.127 is absent from both (hit counts in "Edition read" below); verdict scoped to the filza 8 c.111/c.127 pair, filze 7/9/22 as in Job 3.

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

## Step of 3 Oct 2026: DECODE image fetch and inventory, ids 3758-3789 (A2-FLO, account 2, LANE-A2PUSH)

Runs "Next steps" item 1. Intake gate output, pasted before the step: `florence-dieci-responsive: blocked (line 1) --
already terminal, nothing to gate` (exit 0).

- **Route.** One DECODE real-browser login (`tools/decode_browser_login.js 3758 <scratchpad> --max-files 0 --delay 1600
  --probe "ImagesList?showmaster=records&fk_id=3758" --listen <cmd>`), `loggedIn: true`. The `--probe` answered
  **HTTP 200 with no redirect**: the ImagesList redirect loop recorded by dcB on 24 Sept 2026 (sources/decode/NOTES.md,
  R3754) no longer happens for this account. Then `page ImagesList?showmaster=records&fk_id=<id>` for all 32 ids, and
  `get https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_R<rec>_I<img>_P<n>.jpg` (the thumbnail name without `TH_`)
  for every image the lists named. 71 requests after login, 1.6 s apart, one at a time, no 403/429/challenge.
- **Result.** 31 of 32 records list images (39 images: 24 single leaves, 7 two-leaf records); **all 39 full-size
  images were served** (HTTP 200, `image/jpg`, 0.85-19.2 MB, 3768-5853 px on the long side; none is the
  `forbidden.png` placeholder sha1 035489a0...). Record **3783** (filza 9, c. 190 by sequence) lists **no image** on
  DECODE although its record says 2 pages. DECODE's "Original Filename" column gives filza and carta for every image
  (`Dieci di Balia Responsive <filza>_<carta>[v].jpg`); note record 3761 is c. 102 and 3762/3763 are cc. 70/71 (the
  ids do not run in carta order). Every image's record, image id, original filename, size, dimensions, sha1 and URL
  are in `images/manifest.json`.
- **Committed sample.** Two full-size images, 19 MB: `images/IMG_R3765_I23024_P.jpg` (filza 8 c. 111) and
  `images/IMG_R3766_I23025_P.jpg` (filza 8 c. 127). The other 37 are re-fetchable from the manifest's `url` field
  with one login (`refetch` field); sha1 checks a re-fetch. ImagesList HTML pages were not committed (they carry the
  account name in the navbar).
- **Key / clear-copy leaves seen** (looked at two contact sheets of all 39 at about 380 px per leaf, plus three crops;
  4 image reads by this worker, no subagent; every observation below is grade M, read at low resolution, nothing
  transcribed):
  - **Filza 8 c. 111 (R3765) carries a later archival pencil note "Decifrato della lettera al N° 115"** below a text
    in clear Italian ending "data al ... adì xxvi dicembre 1430"; **filza 8 c. 127 (R3766) carries the ink stamp
    "N° 115"** and has long passages of symbol cipher among clear lines. Read together, c. 111 is labelled as the
    decipherment of the letter at c. 127 -- a plain/cipher pair inside this cluster. Not checked beyond the note and
    the stamp (no alignment, no reading); if it holds, it is the "clear-pages" rung for filza 8's symbol cipher.
  - Stamps on filza 8 run N° 75 (c. 82), 115 (c. 127), 116 (c. 128), 117 (c. 129), 118 (c. 130), 119 (c. 131).
  - Symbol cipher visible at contact-sheet scale: filza 7 cc. 61, 70, 102 (mixed with clear), filza 8 cc. 82, 82v,
    127, 128, 129, 130, 131. Filza 7 cc. 59 and 66 are narrow strips not legible at this scale; c. 71 looks mostly clear.
  - Filza 9 (cc. 172-194): letters in a cursive hand, most signed by the same two-line subscription; no symbol-cipher
    passage distinguishable at this scale (a cipher, if any, would need a page-level look; not done -- this step's
    scope is fetch and inventory). c. 193 is in a different, larger hand.
  - Filza 22 c. 243 (R3788) is a slip wholly in symbol cipher, **photographed upside down** (rotate 180° before any
    pass); c. 244 / 244v look like a clear letter and its address leaf.
  - No key table (a cipher alphabet laid out as a table) seen on any of the 39 leaves.
- Requests: de-crypt.org 1 login + 1 probe + 32 ImagesList pages + 39 full-size images (73 in all, including the login
  page and RecordsView/3758). No other host.

## Step of 3 Oct 2026: c. 111 / c. 127 pairing check (A2-FLO2, account 2, LANE-A2PUSH)

Runs the first clause of A2-FLO's handed-on step ("confirm the pairing from the images on disk"). Intake gate output,
pasted before the step: `florence-dieci-responsive: blocked (line 1) -- already terminal, nothing to gate` (exit 0).

- **Method.** The two committed full-size images only (`images/IMG_R3765_I23024_P.jpg`, c. 111, 4016 x 6016;
  `images/IMG_R3766_I23025_P.jpg`, c. 127, 4010 x 4440): one 1400 px view of each leaf and one native-resolution crop of
  each leaf's last lines (4 image reads by this worker, no subagent, no network). Every observation is grade M.
- **The pair holds** on every point the step named:
  - *Opening.* Both leaves open with the same clear words, "Magnifici etc. Io mi credetti avendo scritto a Neri Capponi
    della buona dispositione che io trovava in messer ...", and the clear lines that follow on c. 127 (about lines 1-5,
    13-17 and the last 8) recur on c. 111 in the same order.
  - *Date and place.* c. 111 ends "data al Guasto Aymone(?) a dì xxvi dicembre 1430"; c. 127's last line reads
    "al Guasto Aymone(?) a dì xxvi ... 1430" before the subscription. Same day and place as far as this hand can be
    read at this scale.
  - *Sender.* c. 127's subscription runs into a group of cipher signs after "servitor ... S. d. V." (the name is in
    cipher); c. 111's subscription has "S. d. V." followed by a name in clear ("Tomaso ...", second word uncertain) --
    the written-out form of that cipher group. The sender's name is not read here (grade M, not transcribed).
  - *Length.* c. 127 is about 44 lines, of which about 24 are wholly or mainly cipher (about lines 6-8 and 18-38 in the
    1400 px view, plus the cipher subscription); c. 111 is about 29 lines wholly in clear in a smaller hand, which fits
    a full clear text of c. 127 with the cipher stretches written out.
  - c. 111 also carries its own stamp "N° 102" (top right; foliation 111 bottom right) besides the later pencil note
    "Decifrato della lettera al N° 115"; c. 127 is stamped "N° 115" (foliation 127). c. 111 is a separately numbered
    item: a period decipherment (or clear copy) filed thirteen items before the cipher original.
- **Cipher shape seen** (for the next pass; not a transcription): a symbol script of roughly 40-60 forms (circled
  letters, barred and doubled strokes, triangles, Greek-like and numeral-like forms), with a ÷-like sign very frequent
  -- possibly a null or a word separator, untested. No key table on either leaf.
- **Stopped here, not transcribed.** The rest of the handed-on step (two blind transcription passes of c. 127 from
  line crops, reconciliation, alignment with tools/interlinear_align.py, key.tsv) is deep work, and CLAUDE.md Pipeline 2's
  intake gate bars deep work on a target whose check-solved verdict has not read the standard edition: this folder's
  status is `blocked` for that reason (Job 3 above), and A2-FLO's own gap line gates the filza 8 pass on the check-solved
  verdict. `tools/intake_gate_check.py` exits 0 only because `blocked` is terminal for it, not because the gate is met.
  Flagged to LANE-A2PUSH. The step also needs a unit nobody priced: a clear-text pass of c. 111 (small cursive hand),
  the plaintext the alignment needs, on top of 2 cipher passes + 1 reconciliation over about 24 cipher lines.
- The pair gives check-solved concrete search handles: a letter to the Dieci of 26 Dec 1430 dated "al Guasto Aymone"
  (reading uncertain), naming Neri Capponi, subscribed "Tomaso ...", with a period decipherment filed at filza 8 c. 111.
- Requests: none (images on disk). Vision: 4 image reads, 0 subagents.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026, A2-FLO)
Read so far: 0 of 39 leaves read (nothing transcribed or decoded; this cluster has only a fetch and inventory).
- filza 7/9/22 premise coverage - blocker: not-attempted; check-solved for the filza 8 pair is done (3 Oct 2026, CS-A2-K: Guasti vols 2-3 read, web and blog check, premise check; status open) but clear copies like c.111 were not looked for among filze 7/9/22; next: contact-sheet look for clear copies, ~$1
- filza 8 symbol cipher (cc. 82, 127-131) with the c. 111 "Decifrato della lettera al N° 115" leaf - blocker: not-attempted; pairing of c. 111 (clear, stamped N° 102) with c. 127 (cipher, N° 115) confirmed from the images on disk (same opening, same 26 Dec 1430 date and place, the c. 111 subscription writes out the cipher signature of c. 127; step of 3 Oct 2026, A2-FLO2), transcription not begun because the intake gate needs the check-solved verdict first; next: after check-solved, line crops of c. 127 and c. 111 (tools/iiif_lines.py --image), 2 blind cipher passes + 1 reconciliation + 1 clear-text pass of c. 111, then tools/interlinear_align.py with a gloss-shuffle control, ~$8
- filza 7, 9 and 22 cipher leaves (keys 3/4 of Yale reel 58 for filza 7; c. 243 is wholly cipher) - blocker: not-attempted; gated on the same check-solved verdict; next: after filza 8, a page-level look at filza 9 for cipher passages and a test of filza 7 against Gabbrielli keys 3/4, ~$6
- record 3783 (filza 9, c. 190) - blocker: needs-physical-access; DECODE lists no image for it although its record says 2 pages (step of 3 Oct 2026); only a copy order from ASFi (REQUEST.md) supplies it

## Escalation (3 Oct 2026, A2-FLO)
- [ ] siblings: the 31 imaged records are siblings of each other; Bourdeau's florence1429/1414 keys (filze 1-3) not yet tried here
- [x] clear-pages: c. 111 found labelled as the decipherment of the letter stamped N° 115 (c. 127), step of 3 Oct 2026 (A2-FLO); pairing confirmed from the images (opening, date, place, subscription), step of 3 Oct 2026 (A2-FLO2); not yet transcribed or aligned
- [ ] known-keys: Gabbrielli keys 3/4 (filza 7, sources/florence/keys/58-5.pdf, 58-6.pdf) against filza 7 leaves, after check-solved
- [x] print: Guasti *Commissioni* vols 2-3 full-text read 3 Oct 2026 (CS-A2-K), letter absent; no edition or calendar of the Responsive exists; Gabbrielli vol. II and Cavalcanti not read
- [ ] key-rebuild: from the c. 111 / c. 127 pair once aligned
- [x] image-check: 39 full-size DECODE images served and inventoried, images/manifest.json (step of 3 Oct 2026)
- [n/a] retry: no earlier failed attempt on this cluster to retry
Verdict: keep going: 3 internal gaps; cheapest next: re-read the c.127 date at crop scale (Bourdeau reads 'xxx d'agosto 1430', we read 'xxvi dicembre 1430'), then the filza 8 transcription and alignment (c.127 cipher passes, c.111 clear-text pass, interlinear_align with gloss-shuffle control), ~$8


## Edition read (CS-A2-K, 3 Oct 2026)

Standard edition for the Dieci di Balìa correspondence of the Lucca war: Cesare Guasti, *Commissioni di Rinaldo degli Albizzi per il Comune di Firenze dal MCCCXCIX al MCCCCXXXIII*, 3 vols, Florence 1867-73. It prints Rinaldo's own commissions and the Signoria/Dieci letters to and from him, not the Responsive series as such. Neither an edition nor a calendar of the *Responsive* is known (Job 3 above found none; none turned up in the searches below). Full-text greps of the whole OCR of vol.3 (1426-1433) and vol.2 (1424-1426), saved copy `djvu.txt` per volume, hit counts (case-insensitive, OCR with double spaces):

| query | vol.3 | vol.2 | what the hits are |
|---|---|---|---|
| "Guasto" (as a place) | 0 (only "guasti", damaged) | not run | no place-name hit |
| "Aymone" / "Aimone" | 2 | not run | Savoyard/Lausanne names, index, unrelated |
| "Fibindac" | 2 | 1 | index entries "Fibindacci (de') Carlo" and "Galeotto, ved. Ricasoli" (vol.3); heading "Galeotto de' Fibindacci da Ricasoli" (vol.2); no 1430 Pontremoli letter |
| "Zaninus" | 0 | 1 | bare name, no cipher context |
| "26 di dicembre" | 3 | not run | all inside the [1429-30] block (Dec 1429): Dieci courier Arrigo, letters of Giovanni Aliprandi and Niccolo, no letter to or from Neri Capponi |
| "dicembre ... 1430" | 1 | not run | Cosimo to Averardo, 10 Dec 1430; Dieci to Carlo da Ricasoli, 23 Dec (not the 26th) |
| "Neri Capponi" | 114 | not run | Neri sent as commissioner to the camp at Lucca on 20 Dec 1430 with Felice Brancacci and Alessandro degli Alessandri; no 26 Dec letter to him |
| "buona dispos" | 3 | not run | none about messer ... and Neri Capponi |
| "cifra" | 11 | 16 | Guasti's note (vol.3, [1429-30] block, n.4): the cipher "si compone di molti segni che corrispondono alle lettere dell'alfabeto, ai numeri e ad alcune parole ... un segno corrisponde anche ai nomi che si celano sott'altri nomi"; further hits are 'cifra' words in Rinaldo's own letters, none printing a decipherment of this item |

Result: the letter is not in Guasti vols 2-3 and neither volume prints a decipherment of any filza 8 item. This corroborates the dating context: Neri Capponi was sent to the camp against Lucca on 20 Dec 1430 (Guasti vol.3, near the Cosimo-to-Averardo passage of 10 Dec 1430), which fits a letter of 26 Dec 1430 that mentions having written "a Neri Capponi". Vol.1 (1399-1423) was not searched: it ends before any date in this cluster. The 1430 question that edition cannot answer is the place (see "Premise check (b)", date discrepancy).

## Web and blog check (CS-A2-K, 3 Oct 2026)

Plain web searches, 5 calls (WebSearch), queries as typed:
1. "Dieci di Balìa" Responsive filza 8 "Decifrato della lettera" 1430 Neri Capponi cifra -> no hit naming the item (generic Capponi/Dieci pages; warwick.ac.uk Italian elites letters, sepoltuario.iath, Wikisource).
2. Gabbrielli "Dieci di Balìa" cifre Neri Capponi 26 dicembre 1430 lettera in cifra "Tommaso" campo Lucca -> no hit.
3. cryptiana.blogspot.com Florence "Dieci di Balia" 1430 cipher letter Fibindacci OR Capponi decipherment -> no hit on that blog; surfaced dspace.ut.ee "A Florentine 'polyalphabetic' cipher in the 15th century" (Piero Capponi, Livorno cipher, not this item) and the Yale voynichverse Dataverse (Ilardi reel 58, already on disk).
4. ciphermysteries.com OR klausis-krypto-kolumne Florence fifteenth-century Dieci di Balia ciphers DECODE Gabbrielli Meister -> ciphermysteries.com 2017/07/08 "new paper fifteenth century cryptography" (Pelling, general), Cipherbrain page 75 listing (general); nothing on the Dieci filze 7/8/9/22 or this letter. Posts opened only as search snippets, comment threads not opened (no hit named the item).
5. Florentine 1430 Lucca war cipher letter Dieci di Balia Responsive deciphered Neri Capponi commissario "cifra" "al Guasto" (the call ran four follow-up searches) -> Neri di Gino Capponi biographical pages (Deutsche Biographie, sepoltuario), a Voynich Ninja thread (Florentine ciphers, general); no hit on the item or on a place "al Guasto".
Google Books API (key + country=US), 2 queries: `"Dieci di Balìa" cifra Responsive` returned 37 volumes (Machiavelli *Opere* 1874/1877 editions print Dieci di Balìa carteggio responsive with "Qui comincia la cifra ... Qui finisce la cifra" in Machiavelli-period items (not this fondo-year); Studies in the Renaissance 1962 names the Gabbrielli "cifra del Carteggio dei Dieci di Balia"); `"Neri Capponi" cifra 1430 Dieci` returned 3, fiscal history only. None is 1430 and none prints a decipherment of filza 8.
Site search of the three blogs by name: done as the engine's site-restricted terms in searches 3 and 4 (cryptiana.blogspot.com; ciphermysteries.com; klausis-krypto-kolumne); the local Cryptiana mirror (`sources/cryptiana`: web/, blog/, CRYPTO-INDEX.tsv) grepped for "Dieci di Bal", "Capponi", "Gabbrielli": one hit, web/polyalphabetic.htm, the Piero Capponi Livorno cipher of the 1490s, not this item. Found: no decipherment or plaintext of c.127 on any of them.
DECODE: status read from the saved login-free listing `sources/decode/florence-dieci-2026-09-24.tsv` (R3765, R3766 Non-decrypted, "none found" for documents) and from A2-FLO's 3 Oct 2026 login session; not re-listed live by this worker.

## Premise check (CS-A2-K, 3 Oct 2026)

(a) The folder's own mentions: **found.** c.111 (R3765) is itself the decipherment: pencil note "Decifrato della lettera al N° 115", a clear text of c.127 with the cipher stretches written out (A2-FLO2 above). It is an archival clear copy on disk, not a published reading and not transcribed by us; Bourdeau's note (medici1425 table) calls it a "19th-c. clear sheet", which would make it Gabbrielli-era work. That makes the key route a plain-copy alignment (rule 10 key `ours`) and the plaintext of this item a text in an archive, not a cryptanalytic result: a cryptanalytic reading of c.127 would be calibration against c.111, never a blind decipherment.
(b) Other solvers' working files: **found, not this item.** dbourdeau/cyphersolver (shallow clone, grepped, 2 Oct 2026 head): `targets/medici1425/NOTES.md` has a DECODE R3758-R3789 table in which R3765 = "19th-c. clear sheet endorsed 'Decifrato della lettera al n. 115': the decipherment of R3766" and R3766 = "Italian letter with long cipher passages, 'al Guasto ... ad xxx d'agosto 1430'. Read at the time via R3765"; R3764 "Ex Pontremulo, 4 martii 1430", Fibindacci; `research/oldest/scan_2026-09-23/italy.md` records that Bourdeau saw all 32 images by cookie and that Gabbrielli's volume holds 1430 keys (reel 58 frames 58-6..58-9, filza 8). His repository does NOT read c.127 or any filza 8 item (no output, key table or apply script for 1430 filza 8; medici1425 targets the Oct 1425 Faenza letter, a different letter). **Date conflict, M-grade on both sides:** Bourdeau's preview-size read "ad xxx d'agosto 1430" versus our A2-FLO2 read "a dì xxvi dicembre 1430" for the same leaf; the Guasti hits above make late December 1430 (Neri at the Lucca camp from 20 Dec) the more consistent reading, but the leaf date is to be re-read at crop scale before it is quoted anywhere. Place "al Guasto Aymone(?)" unresolved. aaymeloglu/unsolved-ciphers (shallow clone, 27 Sept 2026 head): `catalogue/decode-records.jsonl` and `decode-catalog.csv` list R3765/R3766 as Non-decrypted cipher records only; no work on them; Aymeloglu's repository has no licence, cited not copied.
(c) Physical neighbours: **found, c.111 is the neighbour.** The only clear copy in the cluster is the c.111 sheet; c.128-131 (R3767-R3770) are cipher slips in the same sign set per Bourdeau; no other clear copy or slip seen by this worker beyond the A2-FLO inventory (contact sheets); the facing pages of c.127 not viewed at native resolution by this worker (no image reads here), so (c) stays open for c.127 verso and c.128.
(d) Recipient side: **not found.** Neri Capponi's own *Commentari* and Guasti's Rinaldo registers searched as above (recipient/commission side); no printed edition of Neri Capponi's letters of 1430 was located in Google Books or the open web, and none is known to this worker. Not run: HathiTrust full text (Cloudflare), JSTOR (owner's machine), Gabbrielli vol. II, and Giovanni Cavalcanti's *Istorie fiorentine* (Dec 1430 events) as a letter source.
Net: nothing found that decodes c.127 in print or on the three blogs; what exists is c.111's archival clear copy, which is the project's alignment source and the reason the item is not a blind cryptanalysis target. Not classified for novelty (rule 10; a verifier does that).

## Requests (CS-A2-K)
archive.org 3 (advancedsearch 1, `_djvu.txt` 2); www.googleapis.com 2; github.com 2 shallow clones (grep only); WebSearch 5 calls. No de-crypt.org, no images, no vision calls, no subagents.

## Intake gate output (CS-A2-K)
`florence-dieci-responsive: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0, run 3 Oct 2026 after the edits)
