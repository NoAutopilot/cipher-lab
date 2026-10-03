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

## Verdict: `blocked` (image route)

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

## Next step (costed)

An image of the 1714 letter is the only thing that moves this: owner-side copy order to Archiwum Narodowe w Krakowie for the Mniszech-to-Dunin 1714 item (reference 29/637/0/1.3/9908/9, ASKS 125), then one crop-based transcription per TRANSCRIPTION.md. Until then no cheap step is untried: Bourdeau's folder and the DECODE metadata are now read. If the DECODE full-size route opens for R7524 (re-test with `--guess-fullsize`, as A2-HDK did for record 4692, ~USD 1), that replaces the order.

## While waiting

- Re-test DECODE R7524 full-size images with one browser login (decode_browser_login.js, `--guess-fullsize`); depends on nobody (~USD 1). Bourdeau's local images came through DECODE's image manager, so the route may be open.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026)
Read so far: 0 of 232 cipher tokens (no image beyond 200-px thumbnails; nothing read)
- R7524 all 232 cipher tokens - blocker: not-attempted; DECODE full-size route untried for this record, Bourdeau's local images came through DECODE's image manager; next: one browser login with --guess-fullsize, ~$1
- Copy of the 1714 letter from the archive - blocker: waiting-on ASKS 125; the archive record says "No scans / photos", so only a copy order to Archiwum Narodowe w Krakowie supplies one

## Escalation (3 Oct 2026)
- [x] siblings: Bourdeau's potocka1714 folder read (3 Oct 2026); R7515, R7460, R7461 do not fit per his check.
- [n/a] clear-pages: the one clear leaf seen carries no cipher; cipher leaves unseen.
- [x] known-keys: Bourdeau checked the three Sanguszko key records; none fits.
- [x] print: no edition or decipherment located (solver diffs 2-3 Oct 2026).
- [ ] key-rebuild: needs an image first; planned step is a crop transcription after the full-size re-test.
- [ ] image-check: DECODE full-size re-test with one login, ~$1.
- [ ] retry: after a full-size image, a stronger homophonic attack with a control matched on 232 tokens and ~75 signs.
Verdict: keep going: 1 internal gaps; cheapest next: DECODE full-size re-test, ~$1
