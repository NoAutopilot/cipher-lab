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

## Next step (costed)

Open Bourdeau's targets/potocka1714 folder and DECODE R7524's own thumbnail and metadata for the sender/recipient hand and sign set, ~USD 1; then copy order to Archiwum Narodowe w Krakowie for the 1714 Mniszech letters, owner-side.

## While waiting

- Read Bourdeau's potocka1714 NOTES.md (public, MIT/CC BY) to see whether R7524's numeral system shares signs with the recovered Potocka alphabet; depends on nobody (~USD 1).
