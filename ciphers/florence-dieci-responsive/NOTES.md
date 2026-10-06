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

## Step of 3 Oct 2026: Bourdeau check, date line, c.127 block-1/2 pilot alignment (A2-FLO3, account 2, LANE-A2PUSH)

Runs the Verdict's three-part step. Intake gate output, pasted before the step: `florence-dieci-responsive: open (line 1) --
edition/page or full-text-search citation found within 6 lines` (exit 0).

1. **Bourdeau's working files** (github.com/dbourdeau/cyphersolver, shallow clone of head 4d32ec9, 2 Oct 2026 21:07 -05:00,
   grepped, deleted after; MIT, cited). R3765/R3766 occur only in `targets/medici1425/NOTES.md` (lines 47-49, the DECODE table
   CS-A2-K already quoted), `targets/medici1425/profile.json` and `decode_updates/queue.json`, where his proposed DECODE
   update calls R3765 "the decipherment of R3766" (suggest record type key/decipherment) and R3766 "dated at 'il Guasto'
   30 Aug 1430", proposed status Decrypted, `reading: null`, `transcription: []`. No key, transcription or reading of c.127
   in his repository; nothing to align against, so this step did not duplicate any of his work.
2. **Date settled at native resolution: 26 December 1430.** c.127 last line (native crop x 150-1900, y 4060-4200, read at
   2x): "al guasto aymone a dì xxvj di dicẽb(re) 1430" -- the month word has no g descender and ends in an ascender b with an
   abbreviation stroke, so not "agosto". c.111's date line (native crop x 2300-3900, y 3410-3540) reads plainly "adì xxvj
   dicembre 1430". The two leaves agree; Bourdeau's preview-size "xxx d'agosto" does not fit either leaf. Grade M for the
   place word "aymone", the day and month as read from two independent leaves.
3. **Pilot transcription and alignment, two cipher blocks only** (c.127 lines 6-7 and 8-9: the stretch after "chomunita"
   to the clear "E di qu-", and the stretch after "di potrebbe" to the clear "che credo voi"), not the whole leaf: the full
   leaf (~24 cipher lines) is about 6x this unit and would cross this brief's cap. Files:
   - `c127_signs.md`: provisional ASCII sign labels (27 forms) so two blind passes write the same token; **not a settled
     alphabet** (Usage 6: the owner's sign sorter settles it).
   - Crops: `images/c127/` (tools/iiif_lines.py --image images/IMG_R3766_I23025_P.jpg --region 150,540,3860,500
     --max-width 1980 --overlap 100; 4 lines x 2 segments) and `images/c111/` (--image images/IMG_R3765_I23024_P.jpg
     --region 500,1060,3460,400 --max-width 1780 --overlap 100; 3 lines x 2 segments). Pasted output:
     `region 3860x500, 4 lines, 4 bands x 2 segments; pitch 112 ... centres (region y): 74 173 286 408; wrote 8 crops` and
     `centres (region y): 45 157 285; wrote 6 crops`.
   - `passes/c127b1_passA.tsv`, `passes/c127b1_passB.tsv`: two blind Sonnet passes (B read the crops in reverse order).
     Sign agreement 111 of 134 positions (82.8%), i.e. a 17% split -- above Usage 6's one-tenth line, so a third machine
     pass is not the next step.
   - `passes/c127b1_recon.tsv`: reconciliation by this worker from the same crops (each disagreement settled, with a note
     per crop; `o` + division mark merged as one sign `o/`, always written together here; a c-shaped tailed form `s`
     added; line 2 ends in clear "E d(i) qu"). 120 cipher tokens, 27 sign types (q 16, 4 13, p 11, t 11, a 9, ...).
   - Clear text of c.111 for the same two stretches, read by this worker from the c.111 crops (grade M throughout; the
     first word is the weakest): "amspendomi(?) come in italia non a piu bella compagnia ne meglio in punto che questa non
     mancandone niuna" and "provare(?) seicento lanze e quattro[cento](?) fanti" (c.111 strikes a word after "equa" and
     writes "rento" above the line).
   - **Length fit:** 81 signs against 85 plain letters, and 39 against 38 -- close to one sign per letter.
   - `align/c127b1_pairs.tsv` -> `tools/interlinear_align.py align --code-prefix @ --keep-fs` -> `align/c127b1_align.tsv`,
     `align/c127b1_key.tsv`: **28 of 120 tokens agree** with their code's majority meaning (75 conflict, 15 single).
   - **Controls (rule 3), both able to differ from the target on the same 'agrees' statistic:**
     `align/c127b1_control.py` (plain letters shuffled within each line, 20 seeds): agrees min 19, median 25, p95 28,
     max 31. **The target (28) sits inside the shuffle band: no consistent key emerges at this N.**
     `align/c127b1_known.py` (the same plain spans enciphered with a random substitution, two signs each for a e i o, run
     through the identical tool, 10 seeds): exact wording, no noise: agrees 118 of 120 every seed (ceiling, licenses
     little on its own); with 4 plain letters dropped and 17% of signs replaced at random (the target's own length gap and
     pass split): agrees 38-99, recovery 0.38-1.00, mean 0.74. **The target (28) is below that control's floor (38).**
   - **Reading of the numbers:** the pair behaves neither like a two-homophone letter substitution of c.111's exact wording
     at the measured noise, nor distinguishably from shuffled text. Not a negative on the pair (c.111 is labelled the
     decipherment of c.127 and opens, dates and signs the same way): the test cannot tell apart (a) heavier homophony than
     the control models (more signs per letter means fewer repeats at N=120), (b) nulls or word/syllable codes, (c) c.127's
     cipher wording differing from c.111's clear copy (abbreviation, word order), (d) errors in this worker's c.111 reading,
     the first word above all. One hint, unverified: the 4-sign run `q 4 2 z` occurs twice (tokens 5-8 and 69-72), which
     fits "-ndom-" in the first word and "-ndon-" in "mancandone" in position but not in its fourth sign (m vs n).
   - No reading is claimed; no key.tsv, no decode_key.py run (nothing to regenerate). Grade counts: none (no plaintext
     tokens assigned from the cipher).
4. Requests: github.com 1 shallow clone (grep only). No other host. Vision: 18 image reads by this worker (4 date-line
   crops and overviews, 3 iiif_lines debug overlays, 5 c.111 line crops, 6 c.127 crops for the reconciliation) and 2 Sonnet
   subagent passes over 8 crops each; no full page sent to a subagent.

Sorter inputs of 3 Oct 2026 (SORTER-FLORENCE, account 3): `sorter/` holds the tools/sign_sorter.py inputs for c.127 lines 6-9 (120 tiles, 27 piles from the A2-FLO3 recon, 15 focus tiles where the two passes split; boxes approximate, no image read by a model); build command and pre-publish image-terms check in `sorter/README.md`; the account-3 orchestrator publishes.

## GAPS106-florence-dieci-responsive (3 Oct 2026, account-4)

Runs the machine side of the Verdict's cheapest step ("the sorter job itself (crops of c.127's ~24 cipher lines + focus.tsv
...)"). SORTER-FLORENCE (account 3) built the sorter for the pilot lines 6-9 only and the account-3 orchestrator published
it (ASKS 107, open, never blocking); the rest of the leaf had no crops. Intake gate, pasted before the step:
`florence-dieci-responsive: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).
No other account's claim or commit on this folder in the 6 h before 12:22 UTC (last: SORTER-FLORENCE, 03:01 UTC).

- **Crops of the main cipher block of c.127, done.** `python3 ../../tools/iiif_lines.py --image images/IMG_R3766_I23025_P.jpg
  --region 150,1290,3860,2330 --max-width 1980 --overlap 100 --prefix c127b2 --distance 70 --out images/c127b2 --debug`.
  Pasted output: `region 3860x2330, 18 lines, 18 bands x 2 segments; pitch 122 distance 70 prominence 381.0` /
  `centres (region y): 112 216 344 464 591 720 845 943 1079 1208 1360 1496 1628 1744 1869 1976 2090 2223` /
  `wrote 36 crops and images/c127b2/manifest.json`. The debug overlay was checked by eye (two reads, downscaled): every
  centre sits on a text line, none missed. **L01 is clear text** ("Io sono venuto fino ... Rispetto ...", not cipher);
  **L02-L18 are the 17 cipher lines** of the block (L02 opens with clear "ghalio", L18 ends in clear "/ ... medite
  delcquan..."). The default `--distance` (86) found 14 lines and the first region (1830 px tall) clipped the last two;
  both corrected before the final cut. 36 crops, 2.1 MB; images/ now 22 MB (under 30). Debug overlay not kept.
  Not cut here: the scattered code signs inside clear lines 2-3 (e.g. after "achostui") and the cipher subscription
  group on the date line; with the pilot crops (images/c127/, lines 6-9) the leaf's cipher is now cropped apart from those.
- **glyph_atlas segment tried, not usable at default settings.** `tools/glyph_atlas.py segment --page
  c127=images/IMG_R3766_I23025_P.jpg@150,300,4000,4300` (scratch only, not committed): 1218 signs, 811 marks, median
  sign height 21 px, 33 lines found against about 44 on the leaf; cipher lines got 25-47 boxes against roughly 40-50
  signs each by eye at overview scale (adjacent signs merged, `÷`-type dots split off as marks). So the atlas cannot
  stand in for transcription passes or sorter tiles on this leaf without tuning its merge and mark thresholds (a
  no-vision job, untried).
- **Not done (and why).** No transcription pass of c127b2: Usage 6 / TRANSCRIPTION.md put the owner's sign sorter
  (ASKS 107) before further machine passes once two passes split by more than a tenth (pilot: 17%). No sorter tiles for
  L02-L18 either: tiles need a per-sign box and a pile label, and these lines have no pass yet. No reading, no grade counts.
- Vision: 3 image reads by this worker (debug overlays and line-end check, downscaled), 0 subagents. Requests: none
  (images on disk).

## GAPS108-florence-dieci-responsive: contact-sheet look at filze 7, 9, 22 for clear copies (3 Oct 2026, account-4)

Runs the first "Remaining gaps" line (filza 7/9/22 premise coverage). All observations grade M (contact-sheet scale,
about 600-900 px per leaf; nothing transcribed).

- **Route.** One DECODE real-browser login (`tools/decode_browser_login.js 3758 <scratchpad> --max-files 0 --delay 1600
  --listen <cmd>`), then `get` for the 30 filza 7/9/22 URLs in `images/manifest.json`; all 30 served HTTP 200 and all 30
  sha1s match the manifest. (The first run died at `page.goto` with ERR_CERT_AUTHORITY_INVALID before the login form, so
  no login was spent; the CLAUDE.md certutil fix was applied and the single login then succeeded.) Images kept in the
  session scratchpad only, not committed (30 MB rule; re-fetchable from the manifest). Three contact sheets built
  locally with PIL (filze 7+22, 9 leaves at 900 px tiles; filza 9 in two sheets of 11/10 at 700 px tiles; c. 243 rotated
  180 degrees).
- **Result: no clear copy (decipherment) of a cipher letter seen in filze 7, 9 or 22.** No archival "Decifrato ..." note
  like c. 111's, and no clear leaf whose layout, date or subscription mirrors a cipher leaf, at this scale.
  - Filza 7: cc. 61 and 70 (stamps N° 60?, N° 68) open with a clear Latin address of the Duke of Milan ("Dux Mediolani
    etc. Papie Angleri[que] Comes ac Janue dominus") and run in symbol cipher; c. 70 has a clear Latin opening, cipher body,
    clear dating line ending "1424"(?) and a subscription reading "Zaninus"(?); c. 59 (strip, N° 58) has the same ducal
    heading and a subscription reading "Conradinus"(?); c. 66 (strip) mixes cipher and clear. **These subscriptions match
    the name of Gabbrielli's key 4, "Zaninus et Conradinus", 1424, filza 7 (sources/florence/keys/58-6.pdf)**: a
    candidate key for the filza 7 cipher letters, read only at contact-sheet scale (M), not tested. c. 71 is mostly
    cipher-like script mixed with clear lines (not a clear copy); c. 102 (N° 100/101) is an Italian letter mostly in
    clear with some cipher lines, dated "...1424"(?) -- not a decipherment of another leaf.
  - Filza 9 (cc. 172-194, 21 leaves): all in clear Italian, no symbol-cipher passage and no decipherment note visible.
    cc. 172-174 one hand, dated 1431(?); cc. 181-194 (except 193) subscribed by the same two names, read as "Laurentius
    de Ridolfis(?) miles / Laurentius de Medicis(?)"; c. 193 in a larger hand, subscribed "Lorenzo ... / Lorenzo ...".
    These look like original clear despatches, not copies of cipher letters; any cipher in them would be single words or
    short groups invisible at this scale (a line-level look is the only way to rule that out).
  - Filza 22: c. 243 is the wholly-cipher slip (Latin-looking plain words such as "et", "solet" visible between cipher
    groups after rotation); c. 244/244v is a clear Italian letter with an address panel and the name "Nicholaus
    Soderinus orator"(?) near the foot of 244v. c. 244 may be the covering letter of the c. 243 slip; it is not visibly
    a decipherment of it.
- Vision: 3 contact-sheet reads by this worker, 0 subagents. Requests: de-crypt.org 1 failed page.goto (cert, before any
  login), then 1 login + RecordsView/3758 + 30 image gets; no other host.

## GAPS112-florence-dieci-responsive: filza 7 check-solved and Gabbrielli key 4 against c. 70 (3 Oct 2026, account-4)

**Step A, check-solved scoped to filza 7 cc. 59/61/66/70 (DECODE R3758-R3760, R3762), 3 Oct 2026.** These are letters
of Filippo Maria Visconti, Duke of Milan, subscribed by his secretaries "Conradinus" (Corradino da Vimercate) and
"Zaninus" (Zanino Riccio), held in the Florentine Dieci's incoming filza (Bourdeau, `targets/medici1425/NOTES.md`
table, agrees). Searched, in rule 1's order:
- Web search, four queries ("Zaninus" "Conradinus" Visconti 1424 cifra Dieci di Balìa; Filippo Maria Visconti 1424
  lettere cifrate intercettate Firenze decifrate Gabbrielli; Gabbrielli "Dieci di Balìa" cifre 1424 Zanino Corradino;
  Visconti cipher 1424 intercepted letters Florence deciphered Zanino/Corradino): no decipherment or edition of these
  letters. Hits: the Treccani DBI life of Filippo Maria (names Corradino da Vimercate and Zanino Riccio as cipher
  secretaries), ciphermysteries.com 2011/06/28 "Milanese enciphered letters" and 2016/07/06 (Sforza-period, not this),
  Domnina, HistoCrypt 2018 (Tranchedini cipher, 1440s-50s; full text grepped: no Balìa/Gabbrielli/1424/Zaninus), and a
  HathiTrust record "Due lettere intercette dai Dieci di Balìa ... 1384" (1893; its own title gives 1384, not 1424).
- Printed Milanese side: Osio, *Documenti diplomatici tratti dagli archivj milanesi* (1869 volume, IA
  bub_gb_XkUAjq5V07wC, 36,917 lines OCR, grepped): prints ducal letters countersigned "Conradinus"/"Zaninus" from the
  Milan registers, 7 lines mentioning 1424, "cifra/zifra" 6 hits none about Florence or the Dieci, and no "Decem
  Balie"/"intercett" hit. Not a decipherment of these ASFi originals.
- IA full-text (be-api fts, no login): "Zaninus et Conradinus" 0 hits; the bare names return Milanese chronicles and
  documentary volumes (Osio, *Archivio storico lombardo*, Giulini), none about Florentine decipherment.
- Calendars and state papers: none exist for the Responsive (CS-A2-K above). Blog threads: CS-A2-K's three-blog check
  stands; the two ciphermysteries posts above are on the Milanese chancery, not these leaves.
- DECODE (on-disk records TSV, sources/decode): R3758-R3763 all "Non-decrypted", 0 documents.
- Solver repositories: dbourdeau/cyphersolver (shallow clone, head a439937, 3 Oct 2026 01:07 -0500), grepped for
  Zaninus/Conradinus/R3758-R3763: only the medici1425 table (identification, no reading) and florence1429's note "R3758
  not this cipher"; no key application or output for filza 7. aaymeloglu/unsolved-ciphers: catalogue rows only (Premise
  check (b) above).
- Gabbrielli's own volume: key 4 *is* a decipherment key for this correspondence (period-derived or rebuilt by
  Gabbrielli, 1863-64), but no printed decipherment of any letter was found; Gabbrielli vol. II not seen (not digitised).
Verdict for filza 7 cc. 59/61/66/70: **open** -- no printed decipherment or plaintext of these letters located in the
sources above, searched 3 Oct 2026. Rule 10: a search result, not a novelty class. Key route for any reading here
would be `period` (Gabbrielli's key), not `ours`.

**Frame numbering.** Our `sources/florence/keys/58-6.pdf` carries Gabbrielli's own heading "4. Zaninus et Conradinus,
an. 1424, Cifra, Carteggio di X di Balia filza N.o 7" (and 58-5.pdf "3. Johannes"), checked on the image this session;
Bourdeau's italy.md calls key 4 "frame 58-5". A file/frame naming difference, not a content conflict.

**Step B, known keys: c. 70 (R3762) against key 4.** Pre-registered before any c. 70 read in `key4/PREREG-GAPS112.md`.
- Key: `key4/key4.tsv`, 158 entries read from the key image at 150 dpi (20 letters with homophones for a, d, o, u;
  about 130 syllable, Roman-numeral and word codes such as `cul`=de, `dla`=dictus, `hec`=ten, `hoc`=tel, `Slag`=
  Florentini, `Slaf`=Pape); every value M.
- c. 70: one DECODE login, 1 image get (sha1 46f5e949... matches the manifest); `tools/iiif_lines.py --image ...
  --region 400,150,4300,2300 --prefix c70 --debug` cut 17 lines x 2 segments (kept in the session scratchpad, not
  committed; re-cut from the manifest image). Read: L07_s1, L08_s1 (with key 4's letter row beside them), L08_s2,
  L09_s1, L10_s1.
- **What the leaf looks like (M):** c. 70 is a *partly* enciphered Latin letter: clear Latin runs ("Intelleximus
  etiam que scripsisti de ...") with cipher stretches between them, and lines 9-10 mostly cipher. The cipher stretches
  carry forms that are specific entries of key 4, not generic symbols: the word-codes `cul`, `dla` (and `dlal`, `dla?`
  variants not in the table as read), `hec`, a `Sla`-like group, `ñ` (=que), the Roman-numeral group XXIIII (or
  "xxiiij") several times, and the letter signs `÷`, `δ`, `oo`, `□`, `‖`, `—`, `7`, `3`, `h`, `φ`, `qq`. Coverage of
  the 70 tokens read by a key-4 entry: 53/70 = 0.757 (descriptive only: a value-permuted key has the same coverage, so
  no shuffled control can vary on it -- rule 3, orthogonal-control clause).
- **Gated test (`key4/key4_check.py`, la18 char 4-gram, 1000 value permutations among the 27 sign entries used):**
  target, 13 runs / 81 decoded chars: real -2.759 vs shuffled-key p95 -2.732, p 0.075 -> **FAIL**. Positive control
  (la18 Latin spans with the same run and value-length shape, 5 seeds): 5/5 PASS at 0 and 10% injected reader error,
  2/5 at 25%, 0/5 at 40% (`key4/run_noise0*.txt`).
- **Reading of the numbers (rule 3, error-band clause):** the control loses power between 10% and 25% reader error;
  this read is M throughout, by a reader who saw the key values (not blind), with 17/70 signs unmatched outright and
  several ambiguous (`φ` = M or `non`, `y` = es or in) -- its error is not measured but is very likely above 25%. So
  the FAIL is a **non-test at this reader error**, not evidence against key 4. Against that, the presence of key-4-
  specific word-codes (`cul`, `dla`, `hec`) on a filza 7 leaf subscribed "Zaninus" is consistent with key 4 being this
  letter's key (M, descriptive, uncontrolled).
- No reading claimed; no token graded above M (70 tokens: H 0, C 0, S 0, M 70, I 0). Rule 7 does not yet apply.
- Next step: a blind transcription of c. 70's cipher stretches against an anonymised key-4 sign sheet (shape ids, no
  values; two passes, line crops as above, plus one reconciliation), then re-run `key4/key4_check.py` on it with the
  noise sweep; ~$6 at the current Opus vision rate (2 passes x 2 crop sets + 1 reconciliation, about 5 calls). The clear
  Latin runs on the same leaf bound the cipher stretches and can serve as crib context.
- Vision: 3 calls by this worker (the key page; key letter row + 2 line segments; 3 line segments), 0 subagents.
  Requests: de-crypt.org 1 failed page.goto (cert, before any login; certutil fix applied) + 1 login + RecordsView/3762
  + 1 image get; archive.org 3 (Osio djvu, 2 metadata) and be-api.us.archive.org 6; catalog.hathitrust.org 1 (403) +
  1 API; ep.liu.se 1; github.com 1 clone.
- `python3 tools/gaps_check.py florence-dieci-responsive` (3 Oct 2026, after this update): "OK keep-going florence-dieci-responsive: keep going: 2 internal gap(s), 3 step(s) untried / gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped", exit 0.

## GAPS117-florence-dieci-responsive: blind two-pass c. 70 against an anonymised key-4 sheet (3 Oct 2026, account-4)

Pre-registered in `key4/PREREG-GAPS117.md` (pushed b687336e at 13:26 UTC, before either pass ran).
- **Sheet:** `key4/sheet_key4_anon.png`, 162 sign cells cut from 58-6.pdf at 300 dpi by `key4/make_anon_sheet.py`, labelled
  K001-K162 in shuffled order (seed 117), with header letters and values removed. The values are in `key4/sheet_map.tsv`,
  which the readers never saw. While building it, this worker read the key's letter row from the image (M): E carries three
  homophones (X, a 9-like sign, 7), and U and V carry three each. `key4.tsv` (GAPS112) put two of these under d. That is a key-reading
  conflict between two M readings of the same image; `sheet_map.tsv` follows this worker's read, and key4.tsv is unchanged.
- **Crops:** c. 70 fetched again with one DECODE login (sha1 46f5e949..., matches the manifest). `tools/iiif_lines.py --image
  IMG_R3762_I23019_P.jpg --region 400,150,4300,2300 --prefix c70 --debug` output: "region 4300x2300, 17 lines, 17 bands x 2
  segments; pitch 64 distance 44 prominence 463.3". The debug overlay shows L07-L13 on the text lines and L14 onward
  misaligned. Passes read L07-L10, 8 crops. The s1 and s2 segments overlap by 500 px; `passes/gaps117/dedupe.py` dropped the
  repeated s2 prefix per pass (A: 4/5/4/6 signs; B: 4/5/0/0, because B had not repeated them).
- **Passes:** two independent blind Opus subagent calls, each given the 8 crops and the sheet only. A: 130 rows, 22 `?`, 49 L.
  B: 112 rows, 17 `?`, 43 L. `tools/reconcile_passes.py` (nw): A 111 / B 103 signs, **agree 74/113 = 65.5%**: 19 agreed-H,
  55 agreed-uncertain (12 of them both-`?`), 39 differ. Reader disagreement is therefore 34.5%, or 38.6% if both-`?`
  columns are excluded. Files: `passes/gaps117/`, `key4/c70_blind_reconciled.tsv` (agreed positions kept, every
  disagreement set to `?`).
- **Shapes neither reader could place on the sheet (M):** a recurring ligature, a b/h joined to "ay" with a long tail and
  often an x in front ("xbom"/"xoxomi"/"G1"), about 9 times in four lines, matches no key-4 cell. An "H" plus "xxiiij°"
  group in L07/L08 may be clear script (a date or number) rather than cipher. Either the key as Gabbrielli copied it lacks
  a frequent nomenclator sign, or that sign was missed when the sheet was cut. Not settled here.
- **Gate (`key4/key4_check.py --tokens c70_blind_reconciled.tsv --map sheet_map.tsv`, la18 char 4-gram, 1000 value
  permutations):** coverage 61/112 = 0.545, not gated. Target: 23 runs / 118 chars / 30 entries, real -2.828 vs shuffled p95
  -2.472, **p 0.640**. Positive control, same shape: 5/5 at 0 noise, 4/5 at 10%, 5/5 at 25%, **2/5 at the measured 35%**
  (`key4/run_gaps117_noise*.txt`). Under the pre-registered rule this is a **NON-TEST at this reader error**. The control
  fails below 4/5 at the error the readers actually have, so the target's FAIL licenses nothing about key 4 either way
  (rule 3, error-band clause).
  The measured blind error (34.5%) now replaces GAPS112's unmeasured "very likely above 25%". It sits past the band where
  the control holds (<=25%), as GAPS112 suspected.
- **Grading (rule 4):** no reading claimed. 113 transcription positions: 61 agreed K-ids (shape matches, M), 1 clear run,
  51 `?`. Decoded tokens H 0, C 0, S 0, M 0, I 0. Rule 7 does not apply.
- **Next:** two machine passes split by more than a tenth, so per CLAUDE.md Usage 6 (transcription) the next pass is the
  owner's. Put c. 70's sign set (L07-L13 crops, the G1 ligature, the numeral group) and key 4's 162 cells into the sign
  sorter (`tools/sign_sorter.py`; ~$1.5 to build). Re-run `key4_check.py` only once the settled labels bring disagreement under
  25%. A third machine pass of the same crops would repeat an approach already shown to fail its gate (rule 3).
- Usage: vision -- this worker 7 looks (key page, 3 gridded renders, 2 sheet checks, crop debug overlay), 2 Opus subagent
  passes, 0 reconciliation vision calls (script only). Requests: de-crypt.org 1 failed page.goto (cert, before the login;
  certutil fix applied) + 1 login + RecordsView/3762 + 1 image get; no other host.
- `python3 tools/gaps_check.py florence-dieci-responsive` (3 Oct 2026, after this update): "OK keep-going florence-dieci-responsive: keep going: 2 internal gap(s), 3 step(s) untried / gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped", exit 0.

## R9-FLOR: glyph_atlas threshold tuning on c.127 line crops (6 Oct 2026, account 1, LANE-RUN9-account-1)

Runs the Verdict's cheapest next ("glyph_atlas threshold tuning on c.127 (no vision) so the sorter can cover lines
L02-L18"). Script only: 0 image reads, 0 subagents, 0 network requests. PREREG `atlas_tune/PREREG-R9-FLOR.md`
(commit 25ed9bc83, pushed before any segment run). Reproduce: `atlas_tune/run_tune.sh <scratch dir>`; per-crop
counts in `atlas_tune/coverage.tsv`.

- **What changed from GAPS106.** GAPS106 ran `segment` on the whole leaf (page mode) and found 33 of ~44 lines, so
  adjacent signs on the cipher lines merged (25-47 boxes per line). Here `segment` runs on each `tools/iiif_lines.py`
  half-line crop (images/c127/ pilot, images/c127b2/ L02-L18), so line finding is no longer the failure point.
- **Grid (tuning set c127b1 L01_s1, L01_s2, L02_s1; reference = reconciled pilot tokens, clear '=' tokens removed):**
  --rel 0.70/0.78/0.85 x --mark-h 0.45/0.55/0.7 x --min-area 0.12/0.25. rel 0.85 explodes (ratios 5-11), rel 0.70
  over-splits (L01_s1 1.75-1.90); best: rel 0.78 (default), --mark-h 0.7, --min-area 0.25 (summed |ratio-1| 0.44 vs
  default 0.54). Tuned ratios on the tuning set: 1.35 (crop opens with the clear word "chomunita", split into
  several boxes), 1.00, 0.91.
- **Gate as registered: FAIL.** Held-out L04_s1 (pure cipher, 23 tokens): 21 boxes, ratio 0.91, in [0.85, 1.15];
  held-out L03_s2: 22 boxes vs 8 recon tokens, ratio 2.75. The PREREG is in error on L03_s2: it is a mixed crop
  (pass A reads four clear words before the 8 cipher signs; the recon dropped them rather than marking them '='),
  which the PREREG's own ">2 clear tokens" exclusion was meant to catch. Logged as FAIL as registered; on the one pure
  cipher held-out crop the count is in band (N=1 crop, weak). A count ratio cannot see a merge and a split that
  cancel; boxes wider than 1.8x the crop median: 0-1 per pure-cipher crop.
- **Default vs tuned barely differ;** the gain is from cutting by line, not from the thresholds. Per line (s1+s2,
  each pair shares a ~100 px overlap, so ~1-2 signs double-counted), default -> tuned boxes: L02 37->37, L03 40->37,
  L04 43->42, L05 38->36, L06 41->41, L07 52->45, L08 74->63, L09 52->49, L10 49->47, L11 47->42, L12 38->38,
  L13 39->37, L14 40->39, L15 42->42, L16 38->38, L17 44->43, L18 49->47 (723 boxes tuned; GAPS106 eye estimate
  ~40-50 signs per line). 12 of 17 lines sit at 36-43 per line (tuned), in line with the pilot's 19-23 per half-line.
- **Outliers, cause named from the tool's own log:** L05_s1, L07_s1, L08_s1, L09_s1 have a per-crop median sign
  height of 18, 14, 4 and 24 px against 26-72 px on every other crop: specks/dots dominate the component count, the
  scale-free thresholds collapse, and the crop is over-split (L08_s1 also finds 3 line bands in one crop). No
  per-crop threshold fixes that; the fix is a shared scale (a `--median-h` option on `segment` taking the leaf's own
  median, ~50 px here), which is a tool change outside this job.
- Not done: no sorter build, no tiles, no reading, no grade counts (brief).

## R10-FLOR2: shared-scale segment and c.127 L02-L18 sorter inputs (6 Oct 2026, account 1, LANE-RUN10-account-1)

- **Tool.** `tools/glyph_atlas.py segment --median-h PX|pool` (default mode only): every page uses one shared median sign
  height instead of its own; `pool` = median of the pages' own medians. Offline test in `tools/tests/test_glyph_atlas.py`
  (synthetic: a speck-dominated strip whose own median collapses to 4 px against 57 on a clean strip loses its 20 signs;
  with the shared value it gets all 20; the clean strip's boxes are identical at its own scale). Test passes.
- **Re-tune** (`atlas_tune/run_tune.sh`, new config `shared` = tuned + `--median-h pool`; pool over all 42 c.127 crops =
  51.5 px, own medians 4-72; column `boxes_shared` in `atlas_tune/coverage.tsv`). The four outliers, tuned -> shared:
  L05_s1 16 -> 18, L07_s1 25 -> 22, L08_s1 44 -> 16, L09_s1 30 -> 22 (own medians 18/14/4/24 px -> 52). The others move by
  0-3; pure-cipher held-out pilot L04_s1 21 -> 22 boxes against 23 reference tokens (0.96). L08_s1's debug overlay (eyed):
  the speck boxes are gone, but about three of its 16 boxes hold two signs (under-split), so ~19 signs; one crop clips
  the line's bottom. No reading, no grade counts.
- **Sorter inputs, not published:** `sorter/c127b2/` (build_inputs.py, README.md, signs/labels/marks/focus/cipher_lines
  .tsv): 625 tiles on 33 crops (L02_s1..L18_s1, L02_s2..L17_s2), 30 provisional shape-cluster piles k01..k30 (no labels,
  no values), 71 marks, 22 focus tiles. Clear text removed by eye: L02_s1 x < 420 ("ghalio"), L18_s1 x >= 1045, all of
  L18_s2. `tools/sorter_preflight.py` first FAILed right-line at 6.1% (20 boxes reaching neighbour lines); after a trim
  of edge-touching boxes to the line-centre ink run: **preflight PASS** (27 = 4.3% shape flags, 0 off-line tiles, 22
  answerable focus tiles); output pasted in `sorter/c127b2/README.md`. Contact sheet eyed: cuts on single signs, two
  fragments for BAD-CUT. Open question put in the focus box: L08_s1's "a b a b" forms, clear word or cipher signs.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026, A2-FLO)
Read so far: 0 of 39 leaves read (nothing transcribed or decoded; this cluster has only a fetch and inventory).
- filza 8 symbol cipher (cc. 82, 127-131) with the c. 111 "Decifrato della lettera al N° 115" leaf - blocker: not-attempted; pairing confirmed (A2-FLO2) and date settled to 26 Dec 1430 on both leaves (A2-FLO3); a two-block pilot (120 cipher tokens, 2 blind passes split 17%, reconciled) aligned to c.111 by tools/interlinear_align.py gives 28/120 agrees, inside the clear-shuffle band (p95 28) and below a noisy known-answer control (min 38) -- no consistent letter key at this N, cause undetermined (step of 3 Oct 2026, A2-FLO3); owner sign sorter for lines 6-9 published 3 Oct 2026 (ASKS 107, open); line crops of the remaining 17 cipher lines cut 3 Oct 2026 (GAPS106, images/c127b2/ L02-L18); glyph_atlas segment at default settings under-segments this leaf in page mode (GAPS106), but on the line crops gives 36-49 boxes per line on 16 of 17 lines (L08 63) with --mark-h 0.7 --min-area 0.25, registered gate FAIL on a mis-registered mixed crop, pure-cipher held-out 0.91 (R9-FLOR, 6 Oct 2026); the 4 over-split half-line crops fixed by a shared scale (--median-h pool) and sorter inputs for L02-L18 built, preflight PASS, not yet published (R10-FLOR2, 6 Oct 2026); next: publish that sorter, then owner settles the c.127 sign set (ASKS 107), then a full-leaf transcription of c.127 (pilot crops + c127b2) against those labels and a careful clear-text pass of c.111, re-run align/c127b1_control.py and align/c127b1_known.py at full N with a homophone-count sweep, ~$8
- filza 7, 9 and 22 cipher leaves (keys 3/4 of Yale reel 58 for filza 7; c. 243 is wholly cipher) - blocker: not-attempted; no clear copies among filze 7/9/22 at contact-sheet scale (GAPS108, 3 Oct 2026); filza 7 check-solved done 3 Oct 2026 (GAPS112): open, no printed decipherment located; c. 70 against Gabbrielli key 4 (GAPS112): key-4-specific word-codes (cul, dla, hec) present, coverage 53/70 (descriptive), gated decode FAIL (real -2.759 vs shuffled p95 -2.732, p 0.075) but a non-test at this reader error (control 5/5 at <=10% error, 2/5 at 25%, 0/5 at 40%; read M, not blind); blind two-pass c. 70 (GAPS117, 3 Oct 2026): passes agree 74/113 (34.5% disagreement), control 5/5 at 0, 4/5 at 10%, 5/5 at 25%, 2/5 at 35% -> NON-TEST at this reader error (target p 0.640); a recurring ligature (about 9x) matches no key-4 cell; next: owner sign sorter for c. 70 + key-4 cells (tools/sign_sorter.py, ~$1.5 to build, never blocking), then re-run key4/key4_check.py once disagreement is under 25%; then key 3 for the other leaves and a line-level look at filza 9
- record 3783 (filza 9, c. 190) - blocker: needs-physical-access; DECODE lists no image for it although its record says 2 pages (step of 3 Oct 2026); only a copy order from ASFi (REQUEST.md) supplies it

## Escalation (3 Oct 2026, A2-FLO)
- [ ] siblings: the 31 imaged records are siblings of each other; Bourdeau's florence1429/1414 keys (filze 1-3) not yet tried here
- [x] clear-pages: filze 7/9/22 contact-sheet look found no clear copy (GAPS108, 3 Oct 2026); c. 111 found labelled as the decipherment of the letter stamped N° 115 (c. 127), step of 3 Oct 2026 (A2-FLO); pairing confirmed from the images (opening, date, place, subscription), step of 3 Oct 2026 (A2-FLO2); not yet transcribed or aligned
- [ ] known-keys: Gabbrielli keys 3/4 (filza 7, sources/florence/keys/58-5.pdf = key 3, 58-6.pdf = key 4) against filza 7 leaves; check-solved for filza 7 done (open, GAPS112 3 Oct 2026); key 4 vs c. 70: inventory consistent (cul/dla/hec present), gated decode a non-test at this reader error (GAPS112); blind anonymised-sheet two-pass done (GAPS117, 3 Oct 2026): measured disagreement 34.5%, control 2/5 there, so still a non-test; next: owner sign sorter for c. 70 + key-4 cells, ~$1.5 to build, then re-run key4_check.py
- [x] print: Guasti *Commissioni* vols 2-3 full-text read 3 Oct 2026 (CS-A2-K), letter absent; no edition or calendar of the Responsive exists; Gabbrielli vol. II and Cavalcanti not read
- [ ] key-rebuild: from the c. 111 / c. 127 pair; pilot of 3 Oct 2026 (A2-FLO3) on 2 blocks, 120 tokens: real 28 agrees vs shuffle p95 28 and noisy known-answer min 38 -- no key at this N; needs the settled sign set and full-leaf N
- [x] image-check: 39 full-size DECODE images served and inventoried, images/manifest.json (step of 3 Oct 2026)
- [n/a] retry: no earlier failed attempt on this cluster to retry
Verdict: keep going: 2 internal gaps; cheapest next: publish the c.127 L02-L18 sorter built from sorter/c127b2/ (preflight PASS, R10-FLOR2 6 Oct 2026; account-3 orchestrator, image-terms check first), ~$0.3; then a sign-sorter build for filza 7 c. 70 (crops L07-L13, the unmatched ligature, the 162 anonymised key-4 cells) for the owner, ~$1.5, after which key4/key4_check.py re-runs once reader disagreement is under 25% (GAPS117, 3 Oct 2026: blind two-pass 34.5%, a non-test); filza 8 waits on the owner's sign sorter (ASKS 107, open, never blocking), after which full-leaf c.127 passes against the settled labels + c.111 clear-text pass + align controls at full N, ~$8


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

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the Verdict's cheapest next -- publish the c.127 L02-L18 sorter (inputs built, preflight PASS, R10-FLOR2 6 Oct 2026), then the sign-sorter build for filza 7 c.70 (crops L07-L13, the unmatched ligature, the 162 anonymised key-4 cells), ~$1.5. Only the owner's sort itself (ASKS 107, never blocking) waits on a person.
