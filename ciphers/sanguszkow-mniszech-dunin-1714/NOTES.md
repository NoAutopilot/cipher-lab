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

## Next step (costed, refreshed 4 Oct 2026)

Crop transcription of P1 and P3-left per TRANSCRIPTION.md (two blind passes + one reconciliation, 5 vision calls, cap
USD 7, box 60 min; A3V2-SANG's section above), with Bourdeau's `r7524-cipher.txt` (CC BY 4.0, cited) as a third,
independent reader for the disagreement list -- never as a pass of ours. Then `tools/design_prior.py`, a spec
(`specs/sanguszkow-mniszech-dunin-1714.json`, Polish corpus check: tools/data has no 18th-century Polish corpus, so
building one is the V6-PTCORP shape, about 12 min) and a homophonic family run with a control matched on 232 tokens
and 77 signs (rule 3; Bourdeau's own control at this N read 21.1%, so expect a CONTROL BELOW GATE and plan the pooled
or crib-assisted variant before spending).

## While waiting

- Nothing is waiting on anyone: the image is in hand (re-fetch: one DECODE login, A3V2-SANG's command above), the
  check-solved verdict is `open` with the full-text searches named on line 2, and the next step (crop transcription)
  depends on nobody.
- ASKS 125 (copy order): names the wrong letter (refuted above); re-word to 16 March 1714 Dukla / teka 290/6 or withdraw.
- Parallel, owner-side only: a szukajwarchiwach search "Mniszech Dunin" from a desk browser for the 1714.03.16 row.

## Remaining gaps (A3V2-SANGCS, 4 Oct 2026)
Read so far: 0 of 232 cipher tokens (full-size images in hand since 4 Oct 2026; nothing transcribed or read)
- R7524 all 232 cipher tokens - blocker: not-attempted; images in hand, check-solved `open` (this section), no transcription pass run yet; next: crop transcription P1 + P3-left, 2 blind passes + 1 reconciliation, ~$7
- Identity of the archive record for the copy order (ASKS 125) - blocker: waiting-on ASKS 125 re-wording by the lane/owner; the 1714.05.02 record is a different letter (refuted above), nothing here depends on it; next: lane edits ASKS 125, ~$0
- Teka 290 neighbours (plik 1-5, 7+) for a filed key or decipherment - blocker: needs-physical-access; the teka has no scans per the archive's own record and its online unit listing is behind Incapsula for the cloud browser (3 requests this pass), so only an owner-side szukajwarchiwach search or the reading room can list the neighbours; next: LOCAL-QUEUE row or owner desk search, ~$0 here

## Escalation (4 Oct 2026, refreshed A3V2-SANGCS)
- [x] siblings: Bourdeau's potocka1714 folder read in full (4 Oct 2026); R7515, R7460, R7461 do not fit per his check; R7523/R7525 are different letters.
- [x] clear-pages: P1 clear lines and P3 clear leaves seen at native resolution (A3V2-SANG, 4 Oct 2026); not transcribed.
- [x] known-keys: Bourdeau checked the three Sanguszko key records; Potocka key covers 132/232 tokens by range only and is excluded by its own author.
- [x] print: check-solved re-run with the leaf's date and place, six sources, no edition or decipherment (this section, 4 Oct 2026).
- [ ] key-rebuild: after the crop transcription (gap 1).
- [x] image-check: DECODE full-size served, 4 Oct 2026 (A3V2-SANG), three 300-dpi JPEGs, cipher legible.
- [ ] retry: after the transcription, a homophonic attack with a control matched on 232 tokens and 77 signs.
Verdict: keep going: 1 internal gap (transcription, ~$7) plus 2 outside blockers that hold nothing up; cheapest next: crop transcription ~$7
