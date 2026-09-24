found-solved

# Cotton MS Tudor state-papers cluster (England-Rome, -Burgundy, -Spain, -Scotland), c.1509-1603

QUEUE row: N40 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE") — explicitly
a caution/backlog row, "very high" edition risk, not a live lead: 16 items across 14 British Library Cotton
MS volumes, matched only by a generic "cipher" mention somewhere in each VOLUME-level description, not read
item-by-item before this pass.

## Source

British Library, Western Manuscripts: Cotton MS **Vitellius B II** (1509-1515), **Vitellius B VII** (1525),
**Vitellius B XIII** (1530-1532), **Galba B IV** (1516), **Galba B VII** (1521-1522), **Galba D III**
(1588-1589), **Vespasian C I** (1511-1520), **Vespasian C VII** (1471-1588), **Vespasian C VIII**
(1587-1603), **Vespasian F VI** (1572), **Caligula B VII** (1525-1556), **Caligula C IV** (1568-1575),
**Caligula C VI** (1580-1581), **Caligula D I** (1587-1589). Confirmed: exactly 14 volumes / 16 items,
matching QUEUE.md's row text verbatim — no evidence of further volumes beyond these 14.

## Check-solved sweep (24 September 2026) — per-volume calendar check

A Sonnet subagent under this worker's $10 cap checked each volume against its expected calendar series
(Letters and Papers Henry VIII, Calendar of State Papers Spain/Spanish/Scotland/Foreign), prioritising breadth
over depth as the brief directed for a 14-volume caution row. **Method note:** british-history.ac.uk's own
search endpoint served a Cloudflare challenge page to curl (individual article pages fetched fine); the
archive.org full-text-search API looked unreliable/under-indexed on the one Letters and Papers volume tested
and was not pursued further. Coverage below is uneven by design — this is a tooling/budget gap, not a search
that came back negative for the unchecked volumes.

| Shelfmark | Date range | Calendar series | Found calendared? | Note | Fire damage |
|---|---|---|---|---|---|
| Vitellius B II | 1509-1515 | L&P Henry VIII vol.1-2 | not checked this pass | no hit in cryptiana, solver repos, or web search; BHO search blocked | not checked (Vitellius press generally among the worst-damaged in the 1731 fire, not verified for this volume) |
| Vitellius B VII | 1525 | L&P Henry VIII vol.4 pt.1 | not checked this pass | no hit found | not checked |
| Vitellius B XIII | 1530-1532 | L&P Henry VIII vol.5 | not checked this pass | no hit found | not checked |
| Galba B IV | 1516 | L&P Henry VIII vol.2 pt.1 | not checked this pass | ordinary L&P vol.2 BHO pages for 1516 exist but no cipher-specific hit for this shelfmark | not checked |
| Galba B VII | 1521-1522 | L&P Henry VIII vol.3 | calendar coverage confirmed, cipher content not confirmed | BHO: this shelfmark is routinely cited/calendared in L&P vol.3 (a Wolsey-Henry VIII letter re: Piers Butler, Nov 1521, found this pass) but the cipher item itself not located | not checked |
| Galba D III | 1588-1589 | CSP Foreign, Elizabeth, 1588-89 | not checked this pass | no hit found | not checked |
| **Vespasian C I** | 1511-1520 | L&P Henry VIII vol.1-2; CSP Spain vol.2 | **yes** | Cryptiana, `sources/cryptiana/web/henryvii.htm`, quoted verbatim: "Stile's letters in cipher are found in Cotton MS, Vespasian, C I (calendared in Brewers (1920))." Tomokiyo independently reconstructed the cipher key (margin table, f.45/f.47) and cites calendared letters with live BHO links (e.g. Stile to Henry VII, 26 Apr 1509, f.36, british-history.ac.uk/letters-papers-hen8/vol1/pp1-8) | not noted |
| Vespasian C VII | 1471-1588 | L&P Henry VIII (pre-1547) + CSP Spain vols 1-4 (to 1558) + CSP Spanish, Elizabeth ("Hume" series, 1558-1603) | not checked this pass | no direct hit; note the date span crosses two different CSP Spain sub-series | not checked |
| Vespasian C VIII | 1587-1603 | CSP Spanish, Elizabeth ("Hume" series, 4 vols, 1892-99) | not checked this pass | no direct hit | not checked |
| Vespasian F VI | 1572 | CSP Foreign, Elizabeth, 1572-74 | not checked this pass | no direct hit | not checked |
| **Caligula B VII** | 1525-1556 | L&P Henry VIII vol.4 (1525 item); CSP Scotland vol.1 (later items) | **yes (at least the 1525 item)** | Cryptiana, `sources/cryptiana/web/henryviii.htm`, quoted verbatim: "A letter from Dr. Magnus to Wolsey, Edinburgh, 19 April 1525 (Cotton MS Caligula B VII, f.62-66) includes a paragraph in cipher. An incomplete (and partially incorrect) key is attached, and allows reconstruction of the cipher as below." Key already reconstructed by Tomokiyo | not noted |
| **Caligula C IV** | 1568-1575 | CSP Scotland vol.4-5 (Bain) | **mixed — one item open, one already deciphered** | Cryptiana, `sources/cryptiana/web/elizabeth.htm`, quoted verbatim: "(f.278) A few words in cipher, not deciphered. Walsingham to Killigrew, 30 July 1574, Woodstock." [still open, but only a few words] vs. "(f.301) Regent of Scotland to Walsingham, 17 November 1574, Dalkeith. This is only a deciphered copy, but shows that Walsingham shared a cipher with the Regent of Scotland." [already deciphered in the manuscript itself] | not noted |
| **Caligula C VI** | 1580-1581 | CSP Scotland vol.5-6 (Bain) | **yes (at least one item), printed 1759** | Cryptiana, `elizabeth.htm`, quoted verbatim: "(f.128) Walsingham to Randolph, 3 February 1581, Whitehall. Partly in cipher, deciphered. Printed in William Robertson, The History of Scotland during the reigns of Queen Mary and of King James VI., p.86." Key also reconstructed by Tomokiyo. A second item, f.83v (Bowes to Walsingham, 20 Sept 1580, "Names are in cypher"), sits in the same reconstructed Walsingham-circle key network | not noted |
| Caligula D I | 1587-1589 | CSP Scotland vol.9-10 (Thorpe/Bain) | not checked this pass | no direct hit | not checked |

**Solver repositories** (both already cloned locally): zero matches in `dbourdeau/cyphersolver` for any of the
14 target shelfmarks. `aaymeloglu/unsolved-ciphers`'s CATALOGUE.md and decode-ranked.md list several Cotton MS
**Vespasian C III-IV** items (R8465 etc., 1526-29, Bishop of Worcester/Poyntz letters, "key attached; inline
cleartext", marked found-solved 16 Sept 2026, citing State Papers Henry VIII VI and L&P IV) — adjacent to but
distinct from our target Vespasian C I/C VII/C VIII, not a direct hit, but a strong corroborating pattern that
this whole run of Vespasian-C Tudor diplomatic cipher letters was worked over and printed decades ago. A
GitHub search also surfaced dbourdeau/cyphersolver PR #10 (Poyntz to Wolsey, 17 July 1527, Vespasian C IV
f.174-177, "read at the time, Tuke's decipherment in print") — same adjacent-volume pattern, not a direct hit.

**DECODE (de-crypt.org):** public/cached catalogue only, no login attempted; not separately reported as
checked for Cotton shelfmarks by name (see host counts below — treat as "not checked" for this cluster).

**Google Books queries pending** (this worker does not hold the slot): `site:books.google.com "Cotton
Vitellius B. II" OR "Vit. B. II" cipher`; `"Cotton Vitellius B. VII" 1525 cipher`; `"Cotton Vitellius B. XIII"
1530 1531 1532 cipher`; `"Galba B. IV" cipher 1516`; `"Galba D. III" cipher 1588 1589`; `"Vespasian C. VII"
cipher`; `"Vespasian C. VIII" cipher 1587..1603`; `"Vespasian F. VI" cipher 1572`; `"Caligula D. I" cipher
1587 1588 1589`.

**Host requests this pass:** british-history.ac.uk 3 (2 reachability/redirect tests, 1 WebFetch 403); archive.org
5 (1 advancedsearch, 1 metadata, 3 be-api fts, >=3s apart); WebSearch ~18; GitHub 0 API calls (repos already
present; one search surfaced a PR page, not fetched). No Gallica/archivesetmanuscrits fetches, no TNA
Discovery calls (BL material, not TNA), no DECODE login.

**Blocked:** british-history.ac.uk's internal `/search` endpoint serves a Cloudflare challenge page to curl
(a browser-based fetch via tools/browser_fetch.js was not attempted this pass, to conserve budget).
archive.org's be-api full-text search looked unreliable/under-indexed on the one L&P volume tested (0 hits
even for "Henry") and was not pursued further after the sanity check.

## Verdict

**Status: found-solved**, for the material actually checked — consistent with this row's own flag ("caution
row... low expected yield given the editorial coverage"). Of the 5 volumes with a specific, citable reference
found this pass (Vespasian C I, Galba B VII, Caligula B VII, Caligula C IV, Caligula C VI), **4 show at least
one cipher item already read at grade H** (a key or plaintext already in a known source: Tomokiyo's Cryptiana
reconstructions, or, for Caligula C VI f.128, print in Robertson's 1759 *History of Scotland*) — these should
be dropped from any future campaign as already-solved. The one exception found is **Caligula C IV f.278**, "a
few words in cipher, not deciphered" per Tomokiyo's own page — too small a fragment to be a live cryptanalytic
lead on its own, but technically still open.

**The other 9 volumes (Vitellius B II/VII/XIII, Galba B IV/D III, Vespasian C VII/C VIII/F VI, Caligula D I)
were not confirmed either way this pass** — a tooling/budget gap (BHO search Cloudflare-gated, archive.org
full-text search unreliable on the one volume tested), not a negative search result. They remain
unclassified. Given the pattern across the 5 checked volumes and the adjacent-volume corroboration from both
solver repositories (an entire neighbouring Vespasian C III/C IV run already found-solved), the working prior
for anyone picking this up next is that most or all of the remaining 9 will resolve the same way once a
proper BHO browser-based search (`tools/browser_fetch.js`) or a direct download-and-grep of the relevant L&P/
CSP volume OCR text is run, rather than generic web search — but this is a prior, not a finding, and rule 10
forbids treating it as one.

Not "new"; not "unpublished" — several items here are demonstrably already read (Tomokiyo's own keys, one
printed in 1759); the rest is a search result, not a discovery.
