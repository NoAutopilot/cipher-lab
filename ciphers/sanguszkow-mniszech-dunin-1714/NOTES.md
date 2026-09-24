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
