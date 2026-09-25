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
