open
No printed edition of the Mniszech-Dunin letters exists in any source checked; full-text searches run by this worker on 4 Oct 2026: Internet Archive be-api fts "Mniszech" "Dukla" 1714 (336 hits, none this letter), "praetextu consilij" Congressow (0), "16 marca 1714" Dukla (0), "teka 290" Sanguszkow (0); Google Books API (country=US) "Mniszech do Dunina" (14 hits, none this letter), "TEKA 290, plik" (1 hit: Perlakowski 2004 cites teka 290 plik 1, 5, 33, not plik 6), "praetextu consilii" Congressow (0); OpenAlex "Mniszech Dunin 1714" (14 works, none names a cipher letter); Bourdeau's targets/potocka1714/NOTES.md read in full (he left R7524 open, his control failed). Verdict section "Check-solved re-run (A3V2-SANGCS, 4 Oct 2026)" below.

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

## Verdict: `blocked` (24 Sept 2026, image route; superseded 4 Oct 2026 twice: image in hand (A3V2-SANG), then check-solved re-run -> `open` (A3V2-SANGCS, section below))

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

## Check-solved re-run (A3V2-SANGCS, 4 Oct 2026, 05:17-05:4x UTC)

Six-source sweep with the leaf's own date and place (16 March 1714, Dukla; read on the DECODE full-size image by
A3V2-SANG, and now also confirmed from DECODE's own record metadata: `start_year 1714, start_month 3, start_day 16,
origin_city Dukla`, sender "Mniszech J[ózef] - m[arszałek] w[ielki] k[oronny]", receiver "Dunin Jakub - regent
koronny", from the login-free RecordsView/7524 page, 1 request, and Bourdeau's cached `R7524.json`).

| Source | What was searched (4 Oct 2026) | Result |
|---|---|---|
| Web (plain) | 4 plain searches: "Mniszech Dunin 1714 list szyfr Dukla"; "Archiwum Sanguszków" "teka 290" szyfr/cipher 1714; Józef Mniszech marszałek ... Jakub Dunin regent ... szyfrowane; "Mniszech" "Dunin" 1714 cipher deciphered / "solves" Claude / GPT / DECODE 7524 | no page names this letter or any reading of it; the model-solve family returns only the Urquhart distich (Vals AI, 31 Aug 2026; refuted 1 Sept 2026), unrelated |
| Print, IA full text (be-api fts, 10 queries) | "Mniszech" "Dukla" 1714 (336); "Dunin" regent "Mniszech" 1714 (506); "Mniszech" "Dunin" 1714 (797); "praetextu consilij" Congressow (0); szyfr Mniszech Dunin (34); "16 marca 1714" Dukla (0); "teka 290" Sanguszków (0); "Dunin" "szyfrem" 1714 (40); "przetykane szyfrem" (1); Congressow Mniszech 1714 Dunin (0); IA metadata search Mniszech AND Dunin (0), Sanguszków listy (0), creator Gierowski (0 relevant), title "saskim absolutyzmem" (0) | every non-zero hit set read at the snippet level: manuscript catalogues (Gdańsk, Kraków), genealogies, address books and 19th-c. histories; none prints or describes this letter. One lead for the recipient side (below): Studia genealogiczne (2016, `isbn_9788365548719`) quoting Konopczyński's PSB article "Dunin Jakub": Dunin sent "regularne, francuskie, często przetykane szyfrem relacje" (regular French reports often interspersed with cipher) |
| Print, Google Books API (country=US, 12 queries) | "Mniszech" "Dunin" 1714 (21); Mniszech Dukla 1714 list Dunin (0); szyfr/cyfrą "Mniszech" "Dunin" (2, irrelevant); "praetextu consilii" Congressów (0); "Archiwum Sanguszków" "teka 290" (1); "Mniszech do Dunina" (14); "z Dukli" 1714 Mniszech (8); Gierowski intitle + Mniszech Dunin (0); cyfrowany/szyfrowany Dunin Mniszech 1714 (0); "TEKA 290, plik" (1); "290, plik 1, 5" (1); "Dunina" "Mniszech" 1714 Dukla list (0) | the only shelfmark hit is Perłakowski, *Jan Jerzy Przebendowski jako podskarbi wielki koronny* (2004), whose source list cites "TEKA 290, plik 1, 5, 33" -- not plik 6, so no historian is shown to have used this item. Gierowski 1953 (*Między saskim absolutyzmem a złotą wolnością*) cites Dunin's Kórnik letters (BK 417), is NO_PAGES on Google Books, and its snippet search for Mniszech+Dunin returns 0 -- a weak negative, logged as such, not as a read |
| Scholarship (OpenAlex with key, 4 queries; Semantic Scholar with key, 1) | Mniszech Dunin 1714 (14 works); Mniszech szyfr korespondencja (1); Archiwum Sanguszków szyfr (2); szyfry konfederacja tarnogrodzka (0); S2 Mniszech Dunin 1714 cipher (0) | titles read; none concerns this letter or a cipher of Mniszech. "Wyznanie rosyjskiego jurgeltnika" (Klio 2024, abstract read) is about Antoni Dunin 1733-36, unrelated |
| Community lists / blogs | see "Web and blog check" below | no post or comment names Mniszech, Sanguszko or Dunin on any of the three blogs |
| DECODE | login-free RecordsView/7524, 7523, 7525 (3 requests) | 7524: Status N/A, no key, no plaintext, ciphertext private; 7525 (Potocka, teka 301/8) Status N/A; 7523 (teka 288/5, graphic signs + alphabet + numerical, "Inline Plaintext: Yes") is a different Sanguszko item with its own plaintext, not this letter's. No Sanguszko record in Aymeloglu's harvest (30 ASang rows in `catalogue/decode-catalog.csv`) carries a status other than N/A |
| Bourdeau (cyphersolver, fresh shallow clone 4 Oct 2026) | `targets/potocka1714/` read in full: NOTES.md, `r7524-cipher.txt` (his 232-token transcription with clear anchors), `r7524-*-result.txt` (4 failed trials), `control-result.txt`, `coverage.json` (7524 valued 0/232), `prepare_reading.py`; repo-wide grep for 7524/Mniszech; planning-text grep (next/todo/plan/queue) | "R7524 ... uses a separate, still unread numerical system"; "It is left open, with all ciphertext available for a stronger attack"; his synthetic control (232 tokens, 75 signs) read 21.1%, so his negative is inconclusive (his words). No planned next step on R7524 anywhere in his repository (no next/todo/queue line names it; `decode_updates/queue.json` has no 7524 entry); duplicate-effort risk low. Credit: D. Bourdeau, cyphersolver, code MIT, text CC BY 4.0 |
| Aymeloglu (unsolved-ciphers, fresh shallow clone 4 Oct 2026) | repo-wide grep 7524 / Mniszech / teka_290 | raw DECODE harvest row only (`catalogue/decode-catalog.csv` line 2675: 7524, ASang_teka_290/6, 1714, Dukla, Cipher, N/A, 3 pages); no folder, no attempt. Cited, no code copied |

**Identity of the archive record (ASKS 125): refuted.** The szukajwarchiwach record matched on 24 Sept 2026
(29/637/0/1.3/9908/9, "miejsce nieczytelne, 1714.05.02") is a different Mniszech-to-Dunin letter: this item is dated
16 March 1714 at Dukla on the leaf itself (A3V2-SANG, native-resolution image) and in DECODE's own record metadata
(16/3/1714, Dukla), two witnesses against the record's 2 May and illegible place. ASKS 125's copy order therefore
names the wrong item; it should be re-worded to "Mniszech to Dunin, Dukla, 16 March 1714, teka 290/6 (DECODE R7524)",
or withdrawn, since the full-size images are already in hand (A3V2-SANG). The szukajwarchiwach re-search for the
16 March record itself could not be run this pass: the site served its Incapsula bot-challenge to headless Chromium
on both the unit page (/en/jednostka/-/jednostka/41998993) and /en/szukaj, with a persistent profile and 9 s / 20 s
waits, 3 requests in all (initial + the one permitted retry after a 20 s pause + the unit page); stopped per the
good-citizen rule. Owner-side or a later session: search "Mniszech Dunin" in the site's own box and look for a
1714.03.16 / Dukla row and its scan flag.

**Verdict: `open`.** No plaintext, key or decipherment of this letter located in any of the six sources, no edition
prints it, and the one solver who attempted it (Bourdeau, 22-23 Sept 2026) left it open with an inconclusive
control-failed negative. Rule 10: this is a search result, not a novelty claim. Nothing decoded; H 0 C 0 S 0 M 0 I 0.
Requests per host: archive.org advancedsearch 5, be-api.us.archive.org 11, archive.org/metadata 1, googleapis.com/books 16,
api.openalex.org 5, api.semanticscholar.org 1, de-crypt.org 3, raw.githubusercontent.com 1, api.github.com 1 (403),
github.com 2 clones, platforma.bk.pan.pl 4, scienceblogs.de 2, cryptiana.blogspot.com 1, ciphermysteries.com 2 (406),
szukajwarchiwach.gov.pl 3 (all Incapsula), polona.pl 1 (404), fbc.pionier.net.pl 1 (reachability only). WebSearch 11.
Subagents 0. Container note: `certutil` was absent again (second container in one morning, after A3V2-SANG); installed
`libnss3-tools` and added the proxy CA by hand before any browser fetch.

Gate outputs, 4 Oct 2026 05:34 UTC: `python3 tools/intake_gate_check.py sanguszkow-mniszech-dunin-1714` -> "sanguszkow-mniszech-dunin-1714: open (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0; `tools/gaps_check.py` -> "OK keep-going ... 1 internal gap(s), 2 step(s) untried", exit 0; `tools/next_steps.py --wait-only | grep sanguszkow` -> no line.

## Web and blog check (A3V2-SANGCS, 4 Oct 2026)

(a) Plain web searches (WebSearch, standard): "Mniszech Dunin 1714 list szyfr Dukla" -- Dukla/Mniszech family pages, PSB
Dunin namesakes, nothing on this letter; "Archiwum Sanguszków" "teka 290" szyfr OR cipher OR cyfra 1714 -- the fond's
szukajwarchiwach page (zespol/31420, 75 series, 11,499 scans), Sanguszko-archive history articles, no teka 290 hit;
"Józef Mniszech marszałek wielki koronny listy 1714 Jakub Dunin regent koronny szyfrowane" -- Kórnik catalogue records
(BK 417, Dunin's letters to his mother 1713-19 "w niektórych listach po kilka słów szyfrem liczbowym", and 213251/213258
Szembek-era letter books naming Dunin's 1716 memorial and Mniszech letters of 1739), no reading of this letter; "Mniszech"
"Dunin" 1714 cipher deciphered OR "solves" Claude OR GPT DECODE 7524 -- only the Urquhart distich news (Aug-Sept 2026),
Cipherbrain's generic "21 previously unsolved encryptions solved" and Biermann posts, none about Poland 1714;
"Jakub Dunin regent kancelarii koronnej 1714 korespondencja listy Mniszcha wydanie edycja" -- no edition exists;
"Listy Jakuba Dunina ... BK 417 Kórnik szyfr" -- the Kórnik record only; Gierowski "Między saskim absolutyzmem" Mniszech
Dunin Dukla 1714 szyfr -- reviews of the 1953 book, nothing specific; szukajwarchiwach "Mniszech" "Dunin Jakub" 1714 Dukla
-- no indexed record; Tomokiyo cryptiana Polish ciphers 18th century -- Tomokiyo's pages cover Flemming-Wackerbarth
(HistoCrypt 2024) and no Sanguszko item.
(b) Site searches, each blog's own search: Cipherbrain scienceblogs.de/klausis-krypto-kolumne/?s=Mniszech and ?s=Sanguszko
-- "Wir konnten leider keine Beiträge finden" both; Cryptiana blog cryptiana.blogspot.com/search?q=Mniszech -- "No posts
matching the query"; Cipher Mysteries ciphermysteries.com/?s=Sanguszko and ?s=Mniszech -- HTTP 406 to curl (bot
rule; not retried further), covered by the WebSearch site: query, which returned no ciphermysteries.com page for
Mniszech, Sanguszko, Dunin or "Archiwum Sanguszków". Google site: searches for scienceblogs.de and cryptiana returned
no page from either domain for these names.
(c) Hits opened and comment threads: no hit named this letter, so no thread to read; Bourdeau's potocka1714 page (the
only page on the web about R7524) carries no comments and states the item is unread.

## Premise check (A3V2-SANGCS, 4 Oct 2026)

(a) Folder's own files: NOTES.md and the A3V2-SANG image notes mention no decipherment, gloss, interlinear, clear copy or
attachment; A3V2-SANG's one look at all three full-size pages found P1 cipher+clear, P2 (verso) bleed-through and an
archivist's pencil note "Pana Mnisz[cha]" only, P3 (spread) three cipher lines then clear Polish, pencil folio 29; no
later-hand slip, no interlinear values. No REQUEST.md, no spec yet. **Not found.**
(b) Other solvers' working files: Bourdeau's `targets/potocka1714/` cloned and read: `r7524-cipher.txt` is his full
232-token transcription (77 distinct signs, numerals 12-157) with the clear anchors in brackets; his four R7524 trials
(`r7524-result.txt`, `-crib-`, `-null-`, `-regularized-`) are failed annealing outputs, explicitly "not readings";
`coverage.json` values 0/232 for 7524; `prepare_reading.py` excludes 7524 from the Potocka key by design. Whether the
Potocka key would even apply: this worker counted (coverage only, no values printed, nothing read) that `key-potocka.json`
(46 entries, numerals 14-78) has an entry for 132 of the 232 R7524 tokens and 32 of its 77 signs -- 45 signs (100 tokens)
lie outside the Potocka range altogether, consistent with his "separate numerical system"; the Potocka key has not been
run on R7524 by him and does not cover it. Aymeloglu: catalogue row only, no working files. **Not found** (no prior
rendering of this text exists anywhere).
(c) Physical neighbours: facing page and verso viewed at native resolution by A3V2-SANG (P2, P3), no decipherment or slip.
The other items of teka 290 (plik 1-5, 7+) and the archive's unit listing could not be opened this pass
(szukajwarchiwach Incapsula, 3 requests, see above); DECODE's neighbouring records 7523 (teka 288/5, has an inline
plaintext of its own, graphic-sign system) and 7525 (teka 301/8, Potocka) are different letters, and Bourdeau checked
the three Sanguszko key records (R7515, R7460, R7461) against R7524: none fits. **Unreachable** for teka 290's own
neighbours; not found on the leaf's own canvases.
(d) Recipient's side: Dunin's own papers are at Kórnik (BK 417, 262 ff., his letters to his mother 1713-1719, some words
in numerical cipher, microfilm Mf 2442, no digital copy located; platforma.bk.pan.pl/en/bib_records/212918) -- the Dunin
side of a different correspondence, possibly the same key family, not this letter; letters received by Dunin are in
the Sanguszko archive itself (the holding). PSB "Dunin Jakub" (Konopczyński) describes his cipher-interspersed French
reports. No Polish or Saxon documentary edition prints a Mniszech-to-Dunin letter (Google Books and IA sweeps above).
**Not found.**
Result: no find; the item stays calibration-free and `open`; a solver may be briefed (intake gate output at the end).

## Transcription of R7524 (A3V2-SANGTX, 4 Oct 2026, 05:39-05:5x UTC)

**Result: `ciphertext.tsv`, 232 cipher tokens on 14 lines (P1 11 lines, P3-left 3 lines), 77 distinct signs, numerals
12-157, 49 two-digit and 28 three-digit signs, 30 hapaxes; 22 clear-word tokens carried as `[PLAIN:...]`. Nothing is
read: this is a transcription, H 0 C 0 S 0 M 0 I 0 as a reading.** Status stays `open`.

Method (TRANSCRIPTION.md, LLM line reading as the fallback for a numeral cipher). Images: one DECODE browser login
(`decode_browser_login.js 7524 <scratch> --guess-fullsize --max-files 8 --delay 1800`, 05:40 UTC, `loggedIn: true`, 7
requests to de-crypt.org: record page, 3 thumbnails, 3 full-size), the three full-size JPEGs byte-identical to A3V2-SANG's
(same sha256, table above); scratchpad only, not committed. Container: `certutil` absent again (third container in one
morning); `libnss3-tools` installed and the proxy CA added before the login. Crop step, pasted:
`python3 tools/iiif_lines.py --image <P1> --region 170,1560,2050,1340 --prefix p1 --out ciphers/sanguszkow-mniszech-dunin-1714/images --debug`
-> "11 lines, 11 bands x 1 segments; pitch 112 distance 78 prominence 118.0; centres 60 167 276 396 513 628 740 849 959 1066 1179";
`... --image <P3> --region 360,870,1780,480 --prefix p3l ...` -> "4 lines ... pitch 121 ... centres 72 186 303 427". Overlays
(`images/p1_lines_debug.jpg`, `images/p3l_lines_debug.jpg`) checked: every band edge falls in whitespace, no line split or
merged; a first P1 cut at width 1960 clipped the last group of lines 4 and 6 and was re-cut at 2050 (under the 2500 px limit).
The 12th P1 line is the lone clear word "actum" at the right margin (not cut; clear). Crops: 15 line images, 1.2 MB, committed
with manifest.json entries (folder 1.6 MB, far under 30 MB).

Passes: four Opus 5.5 subagent calls, one page per call, crops only (`passes/INSTRUCTIONS.md`; no access to the other pass,
to Bourdeau's file or to this folder), long format with H/M/L and an `alt` column: `passes/p1_A.tsv`, `p1_B.tsv` (197 rows
each), `p3l_A.tsv`, `p3l_B.tsv` (57 rows each). `tools/reconcile_passes.py` per page (`reconcile/p1_*.tsv`, `p3l_*.tsv`):

| page | signs A | signs B | agree | disagreement columns | agreed-H | agreed-uncertain (M/L in either pass) | err_2reader |
|---|---|---|---|---|---|---|---|
| P1 (11 lines) | 181 | 181 | 181/181 = 100.0% | 0 | 164 | 17 | 0/181 = 0.000 |
| P3-left (3 lines) | 51 | 51 | 51/51 = 100.0% | 0 | 39 | 12 | 0/51 = 0.000 |
| both | 232 | 232 | 232/232 = 100.0% | 0 | 203 | 29 | 0/232 = 0.000 |

err_true not measurable: no BENCHMARK-TX.tsv item of this hand or key (an 18th-century Polish numeral hand); err_2reader
0.000 is agreement, not accuracy (LESSONS.md "Look-alike pass"), and the reconciliation below found one agreed-wrong sign.
Reconciliation (this worker, the fifth call: all 14 cipher-line crops read, every one of the 29 agreed-uncertain positions
settled from the image): 28 of 29 confirmed as both readers wrote them (the 6s carry the hand's thin upward tail, the 0s are
plain ovals, the 7s a crossbar, the alternatives 30/70/20/60/38/13/103/81 rejected), graded H with the readers' confidences
and the rejected alternative in `why`. One agreed sign changed: **p1_L03 pos 12, both readers 36 -> reconciled 30 (M)**: a
two-line crop (`images/p1_L03_pos12_tall.jpg`) shows the stroke above the digit is the descender loop of the "y" in the clear
word of the line above ("Spraktykowały", p1_L02), continuous with it; the digit is a closed oval like the 30 at p1_L05 pos 6.
This is the TX-AGREEAUDIT shape (two readers agreeing on a wrong sign for the same reason, here an interfering descender),
caught only because the third reader disagreed there -- see the Bourdeau diff. Clear words where the readers' spellings
differ (p1_L02 "Spraktykowały", p1_L10 "niemogę", p1_L11 "qm" = quam, p3l_L04 "Przesyłam posty doniosłym WMM") carry the
reconciler's reading at M/L with both spellings in `alt`; they are clear text, not cipher, and nothing depends on them.
Final grades in `ciphertext.tsv`: 231 cipher tokens H, 1 M (p1_L03 pos 12).

**Diff against Bourdeau's `targets/potocka1714/r7524-cipher.txt`** (D. Bourdeau, cyphersolver, text CC BY 4.0, code MIT;
fetched once from raw.githubusercontent.com on 4 Oct 2026, 942 bytes; converted to our line ids in
`reconcile/bourdeau_r7524_long.tsv`, 232 cipher tokens, 77 signs, 12-157 -- his counts match ours exactly; a third reader,
not ground truth). `tools/reconcile_passes.py ciphertext.tsv bourdeau_r7524_long.tsv`: **231/232 = 99.6% agreement**, one
disagreement (`reconcile/bourdeau_disagreements.tsv`):

| position | ours | Bourdeau | image (reconciler) |
|---|---|---|---|
| p3l_L02 pos 3 (his line 13, token 3) | 36 (H; A:H, B:M) | 30 | `images/p3l_L02_pos3_tall.jpg`: the tail rises from the oval's top right exactly as the 6s of "66.26" on the line above; nothing descends from above. Stays 36. |
| p1_L03 pos 12 (his line 3, token 12) | 30 (M; both blind readers 36) | 30 | settled for 30 by the two-line crop (above); the only token where the image overruled both blind readers |

Before the reconciler's look the blind-agreed transcription differed from his at two positions (both 36 vs 30: the 6/0
look-alike under a descender); after it, one. The comparison tile `images/bourdeau_diff_36v30.jpg` shows both positions
beside an agreed 36, 30 and 60. Bourdeau's clear-word anchors differ from ours at p1_L02 ("Starosty horodly" vs our
"Spraktykowały") -- clear text, outside the cipher, not settled here.

Sign inventory (for the key test, no reading): most frequent 31 (18), 15 (12), 39 (10), 81 (9), 36/33/20 (8 each), 12/76
(7), 26 (6), 17/107/118 (5); the pair "15.20" recurs 8 times on P1 (lines 1, 1, 3, 3, 4, 5, 5, 6), "22.118.82.36.31.81" three
times (lines 2, 7, 10), "36.31.157.31.33.81" twice (lines 1, 5), "144.76.144" twice (p1_L06, p3l_L01). Observations of the
transcription, not readings.

Requests per host: de-crypt.org 7 (one login), raw.githubusercontent.com 1. Subagent calls: 4 (Opus 5.5, one page each) +
this worker's reconciliation. Not run (brief): any key test. Cost: see the lane ledger.

## Next step (costed, refreshed 4 Oct 2026, A3V2-SANGTX; steps (1)-(2) done by A3V3-SANGP below, see Remaining gaps for the current next step)

Key test, in this order, no transcription work left: (1) `tools/design_prior.py` on 232 tokens / 77 signs / 12-157 with
clear anchors; (2) Potocka key coverage on `ciphertext.tsv` (Bourdeau's `key-potocka.json`, 46 entries 14-78: by range it
touches 132/232 tokens and 32/77 signs, A3V2-SANGCS) read as a trial decode with a matched homophonic control at N=232,
77 signs (rule 3; `tools/family_run.py --family homophonic` after a spec `specs/sanguszkow-mniszech-dunin-1714.json`; a
Polish 18th-century corpus is still missing from tools/data, the V6-PTCORP shape, about 12 min); expect CONTROL BELOW GATE
at this N (Bourdeau's own control read 21.1%) and then the crib-assisted variant (the repeated "15.20", "22.118.82.36.31.81"
strings and the clear anchors "praetextu consilii", "Congressow", "unanimi voto") before spending on annealing. About USD 6
on Fable for (1)+(2) with the corpus build.

## While waiting

- Nothing is waiting on anyone: the image is in hand (re-fetch: one DECODE login, A3V2-SANG's command above), the
  check-solved verdict is `open`, the transcription is committed (`ciphertext.tsv`, A3V2-SANGTX), and the next step
  (key test) depends on nobody.
- ASKS 125 (copy order): names the wrong letter (refuted, A3V2-SANGCS); re-word to 16 March 1714 Dukla / teka 290/6 or withdraw.
- Parallel, owner-side only: a szukajwarchiwach search "Mniszech Dunin" from a desk browser for the 1714.03.16 row.

## Key test 1: language, corpus, design prior, Potocka key, homophonic family (A3V3-SANGP, 4 Oct 2026, 06:13-06:2x UTC)

**Result: the Potocka key does not read R7524 (control-backed negative); homophonic annealing at N=232/K=77 is a
non-test (CONTROL BELOW GATE). Nothing read: H 0 C 0 S 0 M 0 I 0.** Status stays `open`.

(1) Language. The 22 [PLAIN] anchors are Polish syntax with Latin phrases (*Spraktykowały*, *czyni*, *niemogę*,
*Przesyłam posty*, *iest*, *correspondencye*; *praetextu consilij*, *generaliter unanimi voto*, *Rempublicam*,
*tractantur*), so the cipher is most likely Polish (as Bourdeau's R7526 postscript in the sister key) with Latin
words possible. Built `tools/data/pl18` (5 IA files, 1683-c.1790 memoir/letter prose, about 2.27M folded letters;
README, MANIFEST, build.py) and wired it as `"pl18"` in the judge. Leave-one-file-out FN at N=232: blended 42.2%,
per fold 11.0/27.0/80.5/74.0/18.5% (pl19 for comparison: 91.5%, 78.5-98.0%) -- a p05-gate verdict against pl18 is of
unknown reliability (rule 3); the tests below compare against controls scored through the same model instead.

(2) `tools/design_prior.py potocka/r7524_tokens.txt` (232 tokens, 77 signs, 205 references at this N), pasted:
```
multi-sign (homophonic/nomenclator/syllabary) d=0.13 envelope=0.34 null_p05=0.36 -> plausible
letter-for-letter      d=0.68 envelope=1.17 null_p05=1.06 -> plausible
mixed (partial table)  d=1.50 envelope=3.8 null_p05=1.73 -> plausible
code                   d=2.18 envelope=3.78 null_p05=2.89 -> plausible
shuffled-input false-positive rate: 0.075
fine family ranking (advisory, not calibrated): syllabary=0.15; nomenclator=0.23; homophonic=0.48; alphabet substitution=0.68; mixed=1.50; code numbers=2.18
nearest keys: hellen-frederick-1752 key_comb_LR100 [syllabary] d=0.11; huntington-blathwayt-madrid-1728 [syllabary] d=0.13; fr7129-villeroy-bongars-1604 key_f275_v3 [nomenclator] d=0.15
```
Multi-sign class nearest by a wide margin; with 28 three-digit signs (100-157) a nomenclator/syllabary layer beside a
letter alphabet is the first design to test, not a plain homophonic alphabet.

(3) Potocka key trial (`potocka/potocka_trial.py`, `--check` passes; key fetched once from raw.githubusercontent.com,
Bourdeau, CC BY 4.0, used as data, no code copied). Statistic: mean log10 4-gram probability over the decode's
key-covered runs. Target -2.257 (132/232 covered, 13 four-grams); key-right control (held-out Otwinowski text
enciphered with the same key at the target's own covered positions) mean -0.90, p05 -1.18 to -1.29 over seeds 1-3;
key-wrong control mean -2.12 to -2.16; shuffled-target null mean -2.16 to -2.21, p95 -1.78 to -1.88. The control reads,
the target does not, and the target is no better than its own shuffle: **the Potocka key is not R7524's key**. Table in
HYPOTHESES.md H1. Target decode (gaps as ·) in `potocka/target_decode.txt`; it is noise (*qq*, *xaa*, *bb*), not a reading.

(4) `tools/family_run.py --family homophonic` N=232 K=77 pl18, seeds 1-3: control recovery 0.159/0.009/0.060, mean
0.076 < gate 0.6, target not run (HYPOTHESES.md table row). Bourdeau's own control read 21.1%. A blind homophonic
anneal has no power at this length; this is a non-test, not a negative.

Requests per host: archive.org 23 (advancedsearch 9, metadata 7, _djvu.txt downloads 7), pl.wikisource.org 5 (API
search; two returned non-JSON, abandoned for IA), raw.githubusercontent.com 2. Subagent calls: 0. Cost: see the lane ledger.

## Key test 2: crib-assisted homophonic (crib-drag on the repeats), control first (RUN3-SANG, 4 Oct 2026, 09:05-09:2x UTC)

**Result: CONTROL BELOW GATE (mean 0.257, range 0.039-0.388, gate 0.6, pre-registered in `crib/PREREG.md`, commit
358bfabf, before any run); target not run. Nothing read: H 0 C 0 S 0 M 0 I 0.** Status stays `open`.

Instrument: `tools/family_run.py specs/sanguszkow-mniszech-dunin-1714.json --family homophonic --seeds 3 --restarts 8
--param profile=target --param crib=drag` (new `crib=drag` option in `tools/families/homophonic.py`, offline test
`tools/tests/test_homophonic_cribdrag.py`; the pre-option default fixture in `test_homophonic_alphabet.py` (a) still
passes). The repeats R6 = 22.118.82.36.31.81 (x3) and R2 = 15.20 (x8) are pinned in turn to the top 200 pl18 6-grams and
top 40 bigrams by a short anneal, best pair pinned for the full anneal; the control carries one planted 6-sign repeat x3
and one 2-sign repeat x8 (same crib kind and count). Per seed (HYPOTHESES.md H3): the drag found the planted bigram 2/3
("ie"), the planted 6-gram 0/3 (they were names: obadwa, warsza[wa], orlows[ki]). Diagnostics (control-only, not gates):
with the planted strings added to the candidate lists the 6-gram still never reached stage 1's top 5 (0/3; mean 0.250),
so at N=232 the n-gram score cannot pick the right 6-gram even when offered it; with the true crib pinned outright
(`crib/oracle_ceiling.py`) the same design reads 0.845/0.478/0.694, mean 0.672. **A correct crib of this size would read
the control; choosing it by score does not.** The crib must come from outside the statistics (a known plaintext or a
sister letter in the same key), or N must grow. Clear anchors were used for the language only: none sits next to a
repeat in a way that fixes letters without a guess. Requests: none (offline). Subagent calls: 0. Cost: see the lane ledger.

## Remaining gaps (RUN3-SANG, 4 Oct 2026)
Read so far: 0 of 232 cipher tokens read; 232 of 232 transcribed (ciphertext.tsv, err_2reader 0.000, 231/232 with Bourdeau)
- R7524 all 232 cipher tokens - blocker: no-key-material; the Potocka key is excluded (control-backed, H1), blind homophonic is a non-test at N=232/K=77 (H2), and crib-drag on the repeats is untested-by-this-tool at N=232 (H3: control 0.257 < 0.6, the true crib never ranks top 5 even when offered; a correct crib would read, ceiling 0.672); the next instrument needs an externally justified crib or more ciphertext in the same key -- see the sister-letter row
- A sister letter in the same key (to lengthen N past the control's power line, or to supply a crib) - blocker: needs-physical-access; teka 290 neighbours and Dunin's Kórnik papers (BK 417, microfilm only) are not online (A3V2-SANGCS); next: owner desk search of szukajwarchiwach for Mniszech letters 1713-1715 in the Sanguszko archive, ~$0 here
- Identity of the archive record for the copy order (ASKS 125) - blocker: waiting-on ASKS 125 re-wording by the lane/owner; the 1714.05.02 record is a different letter (refuted, A3V2-SANGCS), nothing here depends on it; next: lane edits ASKS 125, ~$0

## Escalation (4 Oct 2026, refreshed RUN3-SANG)
- [x] siblings: Bourdeau's potocka1714 folder read in full (4 Oct 2026); R7515, R7460, R7461 do not fit per his check; R7523/R7525 are different letters.
- [x] clear-pages: P1 clear lines and P3 clear leaves seen at native resolution (A3V2-SANG); the clear anchors inside the cipher lines transcribed as [PLAIN] tokens (A3V2-SANGTX).
- [x] known-keys: Potocka key trial-decoded with key-right/key-wrong controls and shuffled null: control-backed negative (A3V3-SANGP, HYPOTHESES.md H1); Sanguszko key records excluded by Bourdeau.
- [x] print: check-solved re-run with the leaf's date and place, six sources, no edition or decipherment (A3V2-SANGCS, 4 Oct 2026).
- [retired] key-rebuild: blind homophonic anneal (H2) and crib-drag by n-gram score (H3, tools/families/homophonic.py crib=drag) both CONTROL BELOW GATE at N=232; instrument: homophonic_anneal with score-chosen cribs; reopens only with an external crib or a sister letter in the same key.
- [x] image-check: DECODE full-size served, 4 Oct 2026 (A3V2-SANG), three 300-dpi JPEGs, cipher legible; transcribed at 300 dpi (A3V2-SANGTX).
- [x] retry: crib-assisted homophonic attack with a control matched on N, K, design and crib count, pl18 (RUN3-SANG, H3): CONTROL BELOW GATE, target not run.
Verdict: parked: every unread piece is blocked from outside the session (no-key-material until a sister letter or an external crib; sister letters need-physical-access); next new-material step is the owner-side szukajwarchiwach search, ~$0 here
