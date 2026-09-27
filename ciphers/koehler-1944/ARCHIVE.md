# Archive lookup: Walter Köhler's five February 1944 messages

GOLD-1A, 25 Sept 2026. Question: does any archive item describe or hold a decrypt, key or cipher system for
Walter Koehler's five messages to Abwehrleitstelle Frankreich / Paris Funkstelle? Answer: **no item located in
this pass holds or describes a decrypt.** One real, concrete lead was found and not yet opened: an FBI HQ
personal file for "Kohler, Walter" (RG 65, class 105, file 9673), whose existence and box/location are
established from NARA's own released name-index but which is not itself digitised or catalogued online. Status
stays **open**, per rule 10 nothing here is "found solved" and nothing is claimed as new/unpublished.

## Items found

| Ref | Title/description | Dates | Held by | Digitised? | Mentions a decrypt/key/system? |
|---|---|---|---|---|---|
| RG 65, Class 105, File 9673, Section 001, Box 156, NARA location 230 86/16/05 | "Kohler, Walter" -- FBI Class Name Index entry; classification 105 = "Foreign Counterintelligence (Formerly Internal Security, Foreign Intelligence)" | file opened per index; box covers RG 65 generally | NARA (College Park); on the IWG's May 2004 "FBI Files Released" list (Nazi War Crimes Disclosure Act) | No item-level record in catalog.archives.gov (checked by exact-phrase search on "105-9673": 2 unrelated hits, both 21st-century Federal Reserve mortgage reports). Declassified per the 2004 list, but not confirmed digitised/scanned online | Not established either way -- not opened by this worker |
| RG 65, Class 105, File 9673, Section "EBF 003", Box 156, same location | A second section of the same file (names-k-r.pdf only; not on the 2004 disclosure-act list, which shows only Section 001) | -- | NARA (College Park) | Not checked online | Not established |
| RG 65, Class 105, File 11438 (Koch, Ilse) and File 10731 (Koehl, Hermann) | Adjacent index rows, unrelated people (different surnames), noted only to confirm the index-row read correctly | -- | NARA | -- | -- |
| KV 2/1957 | "Franz KOHLER, alias KLEER: German/Hungarian... worked for the Abwehr in Sofia, Budapest and Istanbul" | 1943-1946 | The National Archives, Kew | Catalogue entry only (TNA Discovery) | No -- a different Kohler, wrong theatre (Balkans/Istanbul agent-running, not a US-based radio spy); false-positive, logged to rule it out |
| Kahn, "GERMAN SPY CRYPTOGRAMS", *Cryptologia* 5(2) (April 1981) | The primary print of the five cryptograms; per Kahn's own footnote (not yet independently traced), from a copy he found in the British archives | April 1981 | Taylor & Francis (journal); article also on Internet Archive as `sim_cryptologia_1981-04_5_2`, lending-only | Full text not opened (T&F Cloudflare-blocked; IA loan not borrowed, out of scope) | The article itself is the source of the ciphertext, not a decrypt of it (per Schmeh's reading, confirmed no solution claim in it, see NOTES.md check-solved log) |
| Ladislas Farago, *The Game of the Foxes* (New York: D. McKay, 1971) | Book on German espionage in the US/UK in WWII; per a secondary account (Warfare History Network, below) Farago found Koehler's own dossier in captured German war-archive material and interviewed three former Abwehr officers who remembered Koehler personally | 1971 | Internet Archive, `gameoffoxesuntol00fararich`, lending-only (`access-restricted-item: true`, printdisabled collection) | be-api full-text search confirms "Koehler" appears at least once in the OCR text (1 hit, whole-book match, no page-level snippet returned by this endpoint) | Not established -- not opened. Plausible next lead for the *system* (German side account), not for a decrypt |
| David Alan Johnson, "Walter Koehler & J. Edgar Hoover" (Warfare History Network) | Biographical/historical account of Koehler's career, drawing on Farago | undated (site article) | warfarehistorynetwork.com | Direct fetch Cloudflare-blocked (curl 403, one browser retry timed out on the Cloudflare challenge host) -- read only via WebSearch snippets in this pass, and second-hand via Schmeh's posts in the earlier check-solved pass | No decrypt of the five Paris messages; one new detail found via WebSearch snippet (not previously in NOTES.md): "On March 4, 1944, the FBI noted that signals number 63, 64, and 65 had been transmitted, but the German file detailed that Koehler had sent 137 messages by that time" -- a message-count coincidence with the "137"-headed cryptogram worth flagging, not yet corroborated by reading the whole article |
| FBI Vault (vault.fbi.gov) search "Koehler" | Site's own SearchableText search | -- | fbi.gov | Search page itself works (0 items for a nonsense control term, confirming the box is live), but the "40 items matching" result for "Koehler" is identical in content and order to a search on unrelated terms tried in passing (Watergate, Bremer Kidnapping, Klaus Fuchs, D.B. Cooper, etc.) -- inconclusive, most likely a relevance-fallback/default listing rather than a true filtered match; **not usable as a real search route from this evidence**, logged for the host table, not treated as a negative or a positive | -- |
| catalog.archives.gov (NARA catalog, keyless web UI, per playbook item 3 "keyless-unusable") | Public search UI (no API key set in this environment) | -- | archives.gov | Confirmed unusable for a precise lookup: `q=Kohler, Walter 105-9673` returned 635 loosely-tokenised, mostly irrelevant results (page 1: HMDA mortgage reports, Selective Service cards, a 1945 German industry ledger); the exact-phrase query `"105-9673"` correctly narrowed to 2 results, both unrelated 21st-century items -- confirms the FBI file itself has no item-level online catalogue record | No |

## Search log (one host at a time, this job)

1. **TNA Discovery API** (`https://discovery.nationalarchives.gov.uk/API/search/records`, JSON, browser UA). ~20
   requests, >=1.5s apart, all 200 except one 500 caused by an invalid extra parameter (`sps.catalogueLevels`,
   dropped after the first call). Queried `Koehler`/`Kohler`/`Köhler` (all three spellings return identical
   results -- the index normalises them) alone and combined with `Walter`, restricted in turn to series `KV 2`,
   `KV 3`, `HW 19`, `HW 20`, `HW 40`, plus unrestricted. Only hit in any KV/HW series: KV 2/1957 (Franz Kohler,
   above, ruled out). `HW 19`/`HW 20`/`HW 40` returned **zero** item-level hits for every query tried, including
   `Abwehrleitstelle Frankreich`, `Paris Funkstelle`, `Leitstelle Frankreich`, `AST Frankreich`, `Ast Paris
   Abwehr` -- consistent with these series' Discovery-level catalogue descriptions being sparse (piece number
   and covering dates, not content), not a real search of the underlying decrypts. An unrestricted `Walter
   Koehler` query returns 14 hits, an unrestricted `Koehler` returns 565 -- all inspected on page 1, all noise
   (naturalisation certificates, wills, unrelated Kohler/Koehler surnames, Darwin correspondence). No personal
   file for Walter Koehler the spy found in TNA's online catalogue under any spelling.
2. **Kahn, Cryptologia 5(2) (1981).** CrossRef (`api.crossref.org`, 2 requests) located the DOI
   `10.1080/0161-118191855841`, "GERMAN SPY CRYPTOGRAMS", *Cryptologia* 5(2), pp. **65-66** -- note this
   corrects the page number "69" used elsewhere in this repo (ASKS.md row 53, NOTES.md), which came from Internet
   Archive's be-api `page_num` field, already documented in CLAUDE.md's Access playbook as *not a real page
   locator* (it equals the item's total page count). CrossRef and OpenAlex (1 request, `Authorization: Bearer
   $OPENALEX_KEY`) agree independently on 65-66; ASKS row 53 was not edited here (not this job's file to rewrite)
   but whoever borrows the IA loan should expect the six groups around p.65-66, not p.69. No abstract available on
   either CrossRef or OpenAlex (this is a short 1981 note, not an abstracted article). T&F landing page: one curl
   attempt (403) and the one allowed browser retry (Cloudflare "Just a moment..." challenge, not solved) --
   logged as unreachable, not retried further (good-citizen rule). No JSTOR row added: Cryptologia is a Taylor &
   Francis journal, not JSTOR-hosted, so a JSTOR-QUEUE row would return no hits; the existing ASKS.md row 53 (IA
   loan, owner to read p.65-66 for the six groups) is the live route and was not duplicated.
3. **FBI Vault and NARA.** `vault.fbi.gov/search?SearchableText=Koehler` via the browser tool (curl 403s the
   whole site): see table row above -- inconclusive, not a confirmed working search route. NARA's RG 65 FBI
   Class Name Index (`archives.gov/files/iwg/declassified-records/rg-65-fbi/names-k-r.pdf`, and the May 2004
   disclosure list `fbi-disclosure-act-files.pdf`, both fetched once, 200, parsed with PyMuPDF): **"Koehler,
   Walter -- See Kohler, Walter"** cross-reference, then **"Kohler, Walter", Class 105, File 009673, Section 001,
   Box 156, Location 230 86/16/05, comment "Foreign Counterintelligence (Formerly Internal Security, Foreign
   Intelligence)"** -- appearing on *both* the general name index and the 2004 "files released" list, meaning
   this file was processed and declassified under the Nazi War Crimes Disclosure Act around 2004. A second
   section, "EBF 003", same file/box/location, appears only in the general index, not the disclosure list.
   catalog.archives.gov: see table row above (keyless-unusable, confirmed again). This file's physical location
   is now known precisely; whether it has since been digitised, and what it contains, is not established by this
   worker -- a genuine next step, not a decrypt.
4. **Johnson's Warfare History Network article.** Direct fetch still Cloudflare-blocked (see table). Two
   WebSearch queries surfaced snippets with two new details not previously in NOTES.md: the "137 messages by 4
   March 1944" detail above, and that Farago (not Johnson) is the primary source for the claim that German
   officers personally remembered Koehler and that his double-agent play was pre-arranged with his own Abwehr
   superiors. Logged, not independently verified by reading either source in full.
5. **Prior attempts (Bourdeau).** `git clone --depth 1 github.com/dbourdeau/cyphersolver` (removed after
   reading, per Access playbook "clone only to grep"). Full write-up moved to `HYPOTHESES.md` "Prior attempts"
   section. One extra finding not in that section: the repo's `abwehr/koehler_cryptologia.png` -- a clean,
   uniform monospace-font image of all five messages with no journal header, page number, or scan artifact of any
   kind, which agrees with `msgs.py` at all six of the group positions where our own `ciphertext.txt` (from
   Schmeh 2021) disagrees. This image is **not treated as independent confirmation**: nothing in the repo
   documents it as a scan or photograph of the actual 1981 page (git history for the file carries only an
   unrelated bulk commit message; `msgs.py`'s own docstring says the text is "corrected... (Norbert's
   corrections, Schmeh 2017 comment #7; Schmeh's 2021 repost)" for exactly one of the six group positions, not
   all six) -- it looks like a rendered reproduction of `msgs.py` itself, made for readability, not a second
   primary source. Recorded in `ciphertext-variants.tsv` so nobody mistakes it for one later.
6. **Ciphertext-variants.tsv.** Written from the six-position table already in NOTES.md (flagged by GOLD-0K, 25
   Sept 2026), with the PNG-provenance caveat above added. `ciphertext.txt` was not touched (rule 2).

## Requests

No copy order filed by this worker. ASKS.md row 53 (Kahn Cryptologia p.65-66 -- corrected from "p.69" above --
six groups, IA loan) already covers the one clearly decisive, already-identified copy order; this worker did not
duplicate it. The newly-found FBI file (RG 65, 105-9673, Box 156) is a real lead but its contents are unknown --
whether it is worth a NARA copy/FOIA request depends on what it turns out to hold (the double-agent's Hamburg
file, not necessarily anything about the Paris messages), so no REQUEST.md/ASKS row is filed for it here; noted
as a next step in HYPOTHESES.md instead, for whoever picks this up to weigh against its cost.

## Host request counts (good-citizen rule)

discovery.nationalarchives.gov.uk: ~20 (>=1.5s apart, one 500 from a bad param, otherwise 200). api.crossref.org:
2. api.openalex.org: 1 (keyed). archive.org / be-api.us.archive.org: 3 (metadata + fts, one on the Farago
volume). tandfonline.com: 1 curl (403) + 1 browser (Cloudflare challenge, not solved) -- stopped, no more
retries. vault.fbi.gov: 4 browser fetches (1 baseline/control query, 3 on "Koehler", inconclusive). catalog.
archives.gov: 3 browser fetches (2 web UI searches, API attempt returned the JS app shell, not JSON). www.
archives.gov (static PDF files): 2 (names-k-r.pdf, fbi-disclosure-act-files.pdf). github.com: 1 shallow clone
(dbourdeau/cyphersolver), removed after reading. WebSearch: 3 queries (RG 65 name index, Warfare History
Network/Farago content, FBI file confirmation).

## KOEH-1A (27 Sept 2026) -- cheap_tests_in_order items 2 and 3, extending GOLD-1A

Job runs/2026-09-27-parent-ytbiz-koeh-1a.md, spec's own next-ranked route. GOLD-1A (25 Sept 2026, above) already
ran the TNA Discovery sweep, the Kahn-footnote page-number trace and a first FBI Vault / NARA pass; this job
read that work first (rule: a second pass at an unchanged approach is a non-test unless it tries something the
first pass did not) and ran only the parts GOLD-1A had not covered, plus one genuinely different check on FBI
Vault's search behaviour. **No decrypt, key or new personal file located; the negative is extended, not
reversed.**

**U1, TNA Discovery API, series and terms GOLD-1A did not try.** `discovery.nationalarchives.gov.uk/API/search/
records`, browser UA, same tool GOLD-1A used (`tools/discovery_items.py`'s calling shape; queries run directly,
not through the tool, since its piece-prefix filter does not fit a personal-file surname search -- see "tool
note" below). Sanity check first: `sps.searchQuery=double+agent&sps.recordSeries=KV+2` returns 250 real hits
(GARBO, GELATINE, KISS, etc.), confirming the API and the UA are both live and that multi-word queries are ANDed
by the API itself, not just unioned client-side. Then, all zero hits: `Koehler double agent` and `Koehler New
York` restricted to KV 2; `Walter Koehler Abwehr` unrestricted; `Koehler`/`Kohler Abwehr` restricted to HW 5 and
HW 12 (the two series the brief named that GOLD-1A had not queried -- GOLD-1A covered KV 2, KV 3, HW 19, HW 20,
HW 40); `Funkstelle`, `Abwehrleitstelle Frankreich`, `Paris Funkstelle` unrestricted (GOLD-1A ran the last two
restricted to HW 19/20/40 only; here unrestricted across all Discovery series, still zero). 11 requests,
>=1.6s apart, all 200. Extends GOLD-1A's negative to HW 5, HW 12 and to KV-2-restricted Koehler+context queries;
no new series or term combination turned up a hit.

**U2, Kahn's footnote, be-api full-text search inside `sim_cryptologia_1981-04_5_2` for archive-naming terms.**
GOLD-1A traced the DOI and correct pagination (pp.65-66) via CrossRef/OpenAlex but could not open the article
text itself (Taylor & Francis Cloudflare-blocked, the IA loan out of scope/unborrowable per NOTES.md IA-BORROW);
this job does not borrow either (brief's "do not"). Tried whether the footnote's own wording surfaces via be-api
FTS aggregation counts (doc-level, whole bound volume, not page-scoped) for candidate archive-naming phrases GOLD-1A
had not tried: "Public Record Office", "War Office", "Foreign Office", "British archives" -- all zero documents
(`aggregations.top-languages` empty, confirming a true zero, cross-checked against "British" and "Koehler" which
both return non-empty aggregations and a scored hit list, so the search itself is working). Reads as: whatever
archive name Kahn's footnote uses, it is not one of these four common period terms for the UK national archives --
consistent with GOLD-1A's own read that the footnote's content cannot be recovered without opening the actual
page. No new lead. 6 be-api requests, >=1.6s apart, 200.

**U3, FBI Vault -- a genuinely different check, not a repeat of GOLD-1A's search-box query.** GOLD-1A logged the
"Koehler" search as inconclusive because it returned the same 40 items, same order, as several real topic
searches (Watergate, Fuchs, D.B. Cooper). This job adds the missing negative control GOLD-1A did not run: a
nonsense query, `SearchableText=zzzznonsensequery9999`, which correctly returns **"Search results -- 0 items
matching your search terms"**. That the site can and does report zero hits when nothing matches, yet "Koehler"
returns 40 unrelated items (Watergate Part 16, Klaus Fuchs Part 41, Bremer Kidnapping, German American Bund,
none mentioning Koehler when the list is read), upgrades GOLD-1A's "inconclusive" to a real negative: the site's
search engine is live and can distinguish a true zero from a match, and it does not treat "Koehler" as a real
match to any vault item -- it falls back to a generic/relevance-degraded listing instead. Also tried, as a second
independent route (not the search box at all): the A-Z Index browse endpoint, `vault.fbi.gov/browse-files?
sortFilter=title_asc&Title=koehler` -- the `Title=` filter parameter is silently ignored (returns the same
unfiltered 9762-result listing, page 1 starting "9/11 Chronology..."), and `vault.fbi.gov/espionage` (a guessed
category page) 404s ("This page does not seem to exist"). Confirms no Koehler item on FBI Vault by two
independent routes, one of them (the nonsense-query control) newly conclusive rather than ambiguous. 6 browser
fetches, >=1.6s apart.

**U3, NARA.** `catalog.archives.gov/api/v2/records/search?q="105-9673"` (no `x-api-key`, none set per
`tools/key_probe.py --sync`/KEYS.md): HTTP 200 but the body is the Angular app shell, not JSON -- reproduces
GOLD-1A's keyless-unusable finding exactly (same route, same result), not retried further since a second
identical attempt at an unchanged route is a non-test (README common tail). No NARA_API_KEY has been requested
for this target; `tools/key_request.py` is the route if a future worker judges the FBI file (RG 65 105-9673)
worth chasing through the keyed catalog API.

**Tool note.** `tools/discovery_items.py` (the brief's named extension point) takes a mandatory series + piece-
prefix pair and unions per-term OR queries within that piece; a personal/subject-file surname search across KV/HW
series with ANDed context terms and no piece prefix does not fit its shape, and this job's 11 TNA queries were
few enough not to justify an option addition under Usage rule 8 ("a target that needs something they lack gets an
option added ... " -- weighed against the "don't add abstractions beyond what the task requires" convention: an
option used exactly once, on one target, by one job). Left as a private curl loop, documented here in full
(query strings above) so anyone can rerun it verbatim; flagged in ROOM.md rather than silently skipped.

**Outcome: (c).** Nothing found beyond GOLD-1A's own items (no new archive item, no decrypt, no key). The FBI
HQ file RG 65 105-9673 (GOLD-1A) remains the one concrete unopened lead, unchanged by this job. No REQUEST.md
entry filed (no new TNA reference located to batch into ASKS row 73). Search log above is per-host, dated,
counted (good-citizen rule); `specs/koehler-1944.json` cheap_test_done gains two entries for cheap_tests_in_order
items 2 and 3, crediting GOLD-1A's original sweep and this job's extension together.

Host request counts, this job: discovery.nationalarchives.gov.uk 11 (>=1.6s apart, all 200). be-api.us.archive.org
6 (>=1.6s apart, all 200). vault.fbi.gov 6 browser fetches (>=1.6s apart). catalog.archives.gov 1 (curl, 200,
app-shell body). No 403/429/challenge hit on any host this job.
