blocked

# Mniszech to Jakub Dunin, Crown regent, 1714 — Archiwum Narodowe w Krakowie, Archiwum Sanguszków teka 290/6

QUEUE row: CS2-27 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 280 at dbourdeau.github.io/cyphersolver/catalogue.html), DECODE R7524. Check-solved run
24 September 2026 by LANE N3 csCS2c (session_0113dPptSGXZiBF5uwvtKmtc), brief
`.claude/briefs/runs/2026-09-24-lane-n3-csCS2c.md`.

## What it is

Bourdeau's catalogue: "attempted, open (232 cipher tokens, separate numerical system; solver failed its own
synthetic control, so the negative is inconclusive)." Prior scout pass (24 Sept 2026) marked the image route
"DECODE only (thumbnail); archive's own online viewer not checked this pass" and the row "copy-order
(unconfirmed)."

## Image route (this pass: search attempted, no scan located; row stays copy-order)

szukajwarchiwach.gov.pl (the Polish State Archives' online catalogue/viewer) answers plain curl with an Incapsula
bot-challenge (both `/en/szukaj` and `/en/wyszukiwarka` paths); `tools/browser_fetch.js` cleared it, but the
site's search is a Liferay portlet requiring the actual search-box input to be filled and submitted (a bare
query-string GET on `/szukaj` or `/wyszukiwarka` 404s or "Portlet is temporarily unavailable"s) — filling
`#_Wyszukiwarka_INSTANCE_EHokej781yb7_keywords` via `--type` and letting it submit works.

Searched "archiwum sanguszkow" — confirms fond 26/637 "Archiwum Sanguszków" at Archiwum Narodowe w Krakowie, and
narrowed with "Mniszech Dunin" (one retry needed after a transient Incapsula re-challenge, per the good-citizen
rule) to **20+ individual letter records** from this correspondent pair, including an exact match: "Nadawca:
Mniszech J[ózef] - m[arszałek] w[ielki] k[oronny]. Odbiorca: Dunin Jakub," dated **"miejsce nieczytelne,
1714.05.02"** (place illegible, 2 May 1714) — sender Józef Mniszech (Crown Grand Marshal), recipient Jakub
Dunin, year 1714, matching this row's description exactly. Reference code **29/637/0/1.3/9908/9**.

**This specific record's own search-result markup states "No scans / photos."** (Confirmed from the raw HTML of
the search results, not just the rendered page — `<div class="no-picture"><p>No scans / photos</p></div>`
immediately follows this record's metadata block.) The item's own detail page
(`/jednostka/-/jednostka/41998993/obiekty/1613203`, both `/en/` and bare Polish-locale paths tried) returned
"Portlet is temporarily unavailable" / "Portlety jest tymczasowo niedostępny" on three attempts (one initial +
one retry per the good-citizen rule, plus one locale variant) — a persistent site-side rendering fault on this
detail portlet at the time of this pass, not a bot block (the same fault appeared on an unrelated, much older
item tried first, to rule out a query-specific cause). No image was reachable through this detail page either
way, consistent with the search result's own "No scans / photos" tag.

**Caveat:** the reference code found (29/637/0/1.3/9908/9) does not obviously match "teka 290/6" as cited in
Bourdeau's/DECODE's description of this target — this catalogue's own finding-aid numbering for the Sanguszko
archive may simply differ from the older "teka" numbering DECODE uses, or this may be a related but distinct
letter from the same correspondent pair and year rather than the exact DECODE R7524 item. Not resolved this
pass (would need the detail page, which is currently unreachable, or a direct teka-number search, which the
site's search box does not appear to index).

## Verdict: `blocked` (image route; superseded 4 Oct 2026: image in hand, status held at `blocked` by the intake gate until a check-solved re-run names the edition read -- see the A3V2-SANG section below)

No online scan located for the specific 1714 Mniszech-to-Dunin item found in this archive's own catalogue, and
its own record explicitly says so ("No scans / photos"). Per this brief's Part A instruction ("No image = row
stays copy-order, stop there for that row"), the six-source check-solved protocol was not run for this row.
Row stays `copy-order`, matching its prior status. **No nomination posted.**

Rule 10: no novelty claim made. Not decoded, not transcribed.

Requests this pass: szukajwarchiwach.gov.pl — browser_fetch: 2 failed URL-shape attempts (learning the site's
actual search path), 1 homepage load, 3 search-box submissions (1 needed a retry after a transient Incapsula
challenge), 3 item-detail-page attempts (all "portlet unavailable," not counted against the good-citizen
challenge-retry limit since the failure mode is a site-side rendering fault, not a bot challenge) = 9 browser
fetches total, well under this brief's <=15 cap. WebSearch 1 (confirming the site's real search URL pattern).

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/potocka1714/NOTES.md ; SOLVED_CATALOGUE.md #122
- Their extent, in their words: R7524 (Mniszech) "uses a separate, still unread numerical system"; the Potocka alphabet (R7525-7530, 7534-7536) is recovered, so the folder reads "read in part" but our item is the unread one
- Their date: 22-23 Sept 2026 (updated 30 Sept)
- Note: their target folder not cited in our NOTES.md (catalogue item 280 is)
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Re-check (CS-BATCH5, 3 Oct 2026)

WebSearch (standard) `Mniszech Dunin 1714 cipher Sanguszko archive letter deciphered`: results were HistoCrypt papers (papal cipher 1721, Brougham 1724), Augustus II ciphers and unrelated Dunin namesakes; none names this letter. Solver diffs of 3 Oct 2026 (sources/solver-diffs/2026-10-03-bourdeau.tsv, -aymeloglu.tsv) match this item as before (Bourdeau class b: R7524 "separate, still unread numerical system"; Aymeloglu: DECODE harvest listing only). No image exists online per the holding record ("No scans / photos"), so no edition or leaf was read and the status stays `blocked`. Premise check: (a) folder mentions no decipherment: not found; (b) Bourdeau's potocka1714 working files: not opened here (his page cited above only); (c) neighbours: unreachable, no scans; (d) recipient-side Polish edition: not located.

## Comparison with Bourdeau's Potocka alphabet and DECODE R7524 (A2P4-SANG, 3 Oct 2026)

Descriptive only; nothing here is a reading (H 0, C 0, S 0, M 0, I 0 tokens) and no cipher sign of R7524 was read by us.
Sources: Bourdeau's targets/potocka1714/NOTES.md (fetched once from raw.githubusercontent.com, 3 Oct 2026; D. Bourdeau, cyphersolver, code MIT, text CC BY 4.0, credited); DECODE https://de-crypt.org/decrypt-web/RecordsView/7524 (login-free page, 1 request, 3 `TH_IMG_R7524_I33989_P1-3.jpg` thumbnails, 3 requests, 200x296/297/157 px; nothing larger is served without the account gate, sources/decode/NOTES.md).

- **R7524 metadata (DECODE):** Krakow, Archiwum Narodowe w Krakowie; date 1714; type Cipher, status N/A, cipher type Unknown, symbol set Numerical, 3 pages, cleartext Polish, plaintext Polish, ciphertext flagged private; no key attached.
- **Bourdeau's account of R7524:** ASang teka 290/6, date 1714 from metadata and letter heading; 232 cipher tokens, about 75 distinct signs in his count, "a different alphabet" and "separate numerical system" from the Potocka letters; Polish quintgram homophonic annealing, a tentative *hetmanow* crib and a hypothetical null failed; his synthetic Polish homophonic control (232 tokens, ~75 signs) read only 49/232 (21.1%), so his negative is inconclusive (his words; consistent with rule 3 here, and it means no negative stands on this item).
- **Potocka system (his R7525-7530, 7534-7536; 887 tokens):** numerals about 16-37 for letters, plus person codes up to 270 and homophones (50=e, 52=a, 58=c, 74=r; a=26/27/5/10/15 in different records), French and Polish plaintext, key coverage 863/887 graded I by him. By his own check of the three Sanguszko key records (R7515, R7460, R7461) none fits R7524's neighbours.
- **Shared signs / numeral range:** cannot be stated from what we hold. His notes give R7524's sign count (~75) but not its numeral range or sign list, and our 200-px thumbnails of the cipher pages are not legible at digit level. A ~75-sign inventory against the Potocka letters' roughly 16-37 letter range plus homophones is a wider inventory, which agrees with his "different alphabet", but that is his observation, not ours.
- **Hand (one vision call, P1 thumbnail only, 200 px):** the first leaf is an ordinary clear-text letter page, 13-14 lines of cursive with a short address block and a date at top right, no figures visible at that size. The cipher lies on P2/P3 if it is on these leaves; not examined (one call allowed). Whether sender hand matches the Potocka letters is not judgeable at this size.
- **Found / not found:** found: his written statement that R7524 is a separate unread system and that his control failed; DECODE metadata above. Not found: a sign list or numeral range for R7524, any key or plaintext, any shared-sign claim. No size larger than the thumbnail was fetched.
- Cost: 1 vision call (thumbnail P1), 4 DECODE requests, 1 raw.githubusercontent request, 0 subagents.

## DECODE R7524 full-size images: served (A3V2-SANG, 4 Oct 2026)

One browser login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 7524 <scratch dir> --guess-fullsize
--max-files 8 --delay 1800`, 05:02 UTC, `loggedIn: true`, 7 requests to de-crypt.org: record page, 3 thumbnails,
3 full-size) served all three full-size images for record 7524 as real JPEGs, not the `forbidden.png` placeholder
(sha1 035489a0... absent). Second record after 4692 (A2-HDK, 2 Oct 2026) where the full-size route is open; the
"account-wide blocked" line in the CLAUDE.md host table is per record, not per account. Images stay out of git
(scratchpad only; re-fetch with the same command, one login).

| file | bytes | pixels | dpi | sha256 |
|---|---|---|---|---|
| IMG_R7524_I33989_P1.jpg | 1,756,542 | 2241 x 3324 | 300 | b4dbe872a97207850e137c91bcf57a9038091177ebb8a90baa8bac37b394ac87 |
| IMG_R7524_I33989_P2.jpg | 1,528,670 | 2233 x 3324 | 300 | e80567dba3af3d075b439f4def1f021d5fe793d8567c82ef16a831bf0d549e93 |
| IMG_R7524_I33989_P3.jpg | 3,495,701 | 4219 x 3333 | 300 | db6de4c8d746add7c56c92db6e6330bd2f4b5e2db7a8b54a8cd79a23ab3416f2 |

One look at each page (quarter-scale views plus three native crops; no transcription, nothing graded, H 0 C 0 S 0 M 0 I 0):
- **P1** (recto): heading at top right reads "16. Marty. 1714. / w Dukli." (inferred from the image, one look: 16 March
  1714, at Dukla); salutation "Monseigneur" with an archivist's pencil note; about seven lines of Polish clear, then
  about 13 lines mixing cipher groups with clear Polish/Latin words (e.g. "praetextu consilii", "Congressow",
  "generaliter", "unanimi voto", "Rempublicam", "memoriey", "Consilii"), closing "ut plus quam actum."
- **P2** (verso of P1): no cipher; bleed-through only, plus a pencil note "Pana Mnisz[cha]".
- **P3** (two-leaf spread): left leaf opens with three lines of cipher groups then clear Polish ("tractentur. Przesyłam
  ... "), continuing into clear Polish on the right leaf with the signature and a postscript; folio number "29" in pencil.
- **Cipher legibility:** fully legible at native resolution. Two- and three-digit groups separated by points, dark ink,
  no cuts, no fading; e.g. P1 first cipher line "110.36.31.157.31.33.81.15.20. 125.38.97.79.15.20. 128.42.17.15.130."
  and P3 left "152.66.26.31.49.94.31.76. 38. 39.107.102.25. 144.76.144.56." as seen on the crops (one look, not a
  transcription; the transcription pass re-reads every digit blind). The numeral range seen at a glance is about
  12-157, consistent with Bourdeau's ~75 distinct signs and "separate numerical system" (his count, not ours).
- **Date conflict with the catalogue match:** the szukajwarchiwach record matched on 24 Sept 2026
  (29/637/0/1.3/9908/9) is dated "miejsce nieczytelne, 1714.05.02"; this leaf is headed 16 March 1714 at Dukla. The
  earlier caveat stands and is now sharper: that record is probably a different Mniszech-to-Dunin letter, and
  ASKS 125's copy order names the wrong item unless the archive is asked for the 16 March 1714 letter (teka 290/6).

Container note: the Chromium NSS certificate fix the setup script is supposed to apply (CLAUDE.md access playbook 2)
had not run in this container (first attempt: ERR_CERT_AUTHORITY_INVALID before the login page; no login spent);
applied by hand (`certutil -N -f /dev/null` then `-A`), then the login worked first time.

## Next step (costed)

Crop transcription of the two cipher leaves (P1 and P3-left) per TRANSCRIPTION.md: `python3 tools/iiif_lines.py
--image <P1 file> --out ciphers/sanguszkow-mniszech-dunin-1714/images` (and P3-left as a region), check the debug
overlay, then two blind passes on the line crops only and one reconciliation (`tools/reconcile_passes.py`): 2 pages
x 2 passes + 1 reconciliation = 5 vision calls at about USD 1.2-1.5 per call, cap USD 7, box 60 min. Before any
cryptanalysis (CLAUDE.md pipeline 2, intake gate): a check-solved re-run that reads the letter's date, place and
clear-text phrases against the Polish editions and the Sanguszko inventory, now that the leaf can be read.
Then the retry: a homophonic attack with a control matched on 232 tokens and ~75 signs (rule 3), design prior from
`tools/design_prior.py` first.

## While waiting

- Nothing is waiting on anyone: the image is in hand (re-fetch: one DECODE login, command above).
- ASKS 125 (copy order): re-word to the 16 March 1714 Dukla letter or withdraw; it no longer blocks anything.

## Remaining gaps (A3V2-SANG, 4 Oct 2026)
Read so far: 0 of 232 cipher tokens (full-size images in hand since 4 Oct 2026; nothing transcribed or read)
- R7524 all 232 cipher tokens - blocker: not-attempted; full-size images only arrived this pass (table above), no transcription pass run yet; next: crop transcription P1 + P3-left, 2 blind passes + 1 reconciliation, ~$7
- Check-solved against Polish editions with the leaf's own date and phrases (16 March 1714, Dukla) - blocker: not-attempted; the 24 Sept and 3 Oct check-solved passes had no leaf to read, so no edition was searched by date or phrase (intake gate, status line stays blocked until this runs); next: check-solved re-run naming the edition read, ~$3
- Identity of the archive record (2 May vs 16 March 1714) - blocker: not-attempted; the heading read on P1 (above) disagrees with the matched record's date, so ASKS 125 may name the wrong letter; next: szukajwarchiwach search for the 16 March 1714 Dukla letter, ~$1

## Escalation (4 Oct 2026)
- [x] siblings: Bourdeau's potocka1714 folder read (3 Oct 2026); R7515, R7460, R7461 do not fit per his check.
- [x] clear-pages: P1 clear lines and P3 clear leaves seen at native resolution (4 Oct 2026); not transcribed.
- [x] known-keys: Bourdeau checked the three Sanguszko key records; none fits.
- [x] print: no edition or decipherment located (solver diffs 2-3 Oct 2026); re-run with the leaf's date owed (gap 2).
- [ ] key-rebuild: after the crop transcription (gap 1).
- [x] image-check: DECODE full-size served, 4 Oct 2026 (A3V2-SANG), three 300-dpi JPEGs, cipher legible.
- [ ] retry: after the transcription, a homophonic attack with a control matched on 232 tokens and ~75 signs.
Verdict: keep going: 3 internal gaps; cheapest next: szukajwarchiwach re-search ~$1, then crop transcription ~$7
