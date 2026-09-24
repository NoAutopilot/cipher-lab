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

## Follow-up sweep of the 9 unchecked volumes (24 September 2026, LANE S worker H)

Per this run's brief: checked each of the 9 previously-unchecked volumes against its expected calendar
series by fetching the calendar's full OCR text from archive.org (djvu.txt) and grepping it directly
offline for the volume's shelfmark form (`Vitell`, `Galba`, `Vesp`) co-occurring with `cipher`/`cypher`
within a few hundred characters — the same method the original Vespasian C I / Caligula B VII / Caligula C
VI hits in the table above used, chosen because british-history.ac.uk's search is Cloudflare-gated and
archive.org's be-api full-text search index is confirmed (again, this pass) unreliable on these older Google
Books-sourced OCR scans (`q=Vitellius&identifier=letterspapersfor01greauoft` returned 0 hits despite the
word occurring 83 times in the plain-text file itself — do not rely on be-api fts for this OCR generation;
fetch and grep the djvu.txt).

| Shelfmark | Volume checked | Result |
|---|---|---|
| **Galba B IV** | *L&P Henry VIII* vol. 2 pt. 1 (`Vol2Pt1LettersAndPapersForeignAndDomestic`, Brewer, full text fetched and grepped) | **found-solved.** At least 6 distinct cipher items with contemporary decipherments already printed in this 1864 edition, all Sir Richard Spinelly's or Cuthbert Tunstal's 1516 despatches to Wolsey from Brussels: no. 2244 (Galba, B. iv. 130, 4 Aug. 1516, endorsed with a Latin decipher "by Ammonius"); no. 2358 (Galba, B. iv. 164, 13 Sept. 1516); no. 2373 (Galba, B. iv. 175, 20 Sept. 1516, "Hol., cipher, deciphered by Tuke"); no. 2663 (Galba, B. iv. 250, 12 Dec. 1516); no. 2673 (Galba, B. iv. 246, 14 Dec. 1516, "one passage in cipher, undeciphered" — the one exception, still unread even in print); no. 2703 (Galba, B. iv. 261, 26 Dec. 1516). Brian Tuke, Wolsey's own cipher clerk, is named as decipherer on several. This drops Galba B IV from any future cryptanalysis campaign as already-read in a public-domain 1864 edition. |
| **Vitellius B XIII** | *L&P Henry VIII* vol. 5 (`letterspapersfor0005jame`, James Gairdner, full text fetched and grepped) | **strong candidate, not certain — status left open.** No. 891-892 ([Casale and Benet] to Henry VIII, Rome, 23 March 1531/32, "23 HENRY VIII"), on the King's divorce case, is cited "Vit. B. x11. 178" with "Cipher deciphered" and a cross-reference "Burnet, iv. 176" (i.e. also printed in Gilbert Burnet's *History of the Reformation*). The digit rendering is OCR-ambiguous between "xii" (Vitellius B XII, a different volume) and "xiii" (our target): a frequency check of every "Vit. B. [numeral]" citation in this same file shows clean, unambiguous renderings of both "XII." (once) and "XIII." (once) elsewhere, with the garbled form "x11"/"xm"/"xiu"/"x111" appearing 9 times total — a distribution consistent with "x11" etc. being OCR's usual mangling of "xiii" (dropping one stroke of a triple-i) rather than of the already-cleanly-rendered "xii". Not conclusive enough to change the status word without opening the image or the physical L&P volume; flagged as the cheapest next step for this row (check whether Vit. B. xiii f.178 vs Vit. B. xii f.178 in the Cotton catalogue, or open Burnet vol. 4 p.176 to confirm the letter is Casale/Benet from Rome, 23 March 1532). |
| **Vespasian F VI** | *CSP Foreign, Elizabeth, 1572-74* (`calendarofstatep0000vari_o6f2`, full text fetched and grepped) | **Checked, not found — a real (if narrow) negative for this specific edition.** The whole volume cites "Cotton" only as the surname of a person (Mr. Thomas Cotton, an agent in the Low Countries, unrelated) and "Vesp" only once, in "Sicilian vespers" (unrelated). This calendar draws almost entirely on State Paper Office material with only occasional cross-references to BM manuscripts, and none reaches Vespasian F VI in the volume checked — narrows, does not close, the QUEUE row's edition risk for this item (a companion CSP Foreign volume or a different year within Vespasian F VI's 1572 span was not checked). |
| **Vitellius B II** | *L&P Henry VIII* vol. 1 (`letterspapersfor01greauoft`, full text fetched and grepped) | **Checked, not found.** 83 occurrences of "cipher" in the whole volume; none within 400 characters of any "Vit"/"Vitell" shelfmark citation. Consistent with (not proof beyond) the original pass's "no hit found." |
| Vitellius B VII | *L&P Henry VIII* vol. 4 | **Not resolved — wrong sub-volume fetched.** The archive.org identifier picked this pass (`letterspaperspt204greauoft`) turned out to be **Vol. IV, Part II** (content from 1526 onward, confirmed by its own title page and by 200 "1526" hits vs 16 "1525" hits), not the Part I our 1525 target needs. No exact "Vit. B. vii" citation found in the wrong part fetched. The correct Part I identifier was not pinned down this pass (archive.org's metadata does not distinguish part 1/2/3 in the `volume` field for the other `lettersandpaper*offigoog` candidates found); flagged as the cheapest next step. |
| Galba D III | *CSP Foreign, Elizabeth, 1588-89* | **Not resolved.** archive.org search did not turn up an identifier clearly matching the specific 1588-89 volume of this series this pass (the series runs ~23 volumes and only a handful of identifiers surfaced by title search); not fetched. |
| Vespasian C VII | *L&P Henry VIII* (pre-1547) + *CSP Spain* vols 1-4 + *CSP Spanish, Elizabeth* | **Not attempted.** Its 1471-1588 span crosses at least three separate calendar series (confirmed multi-series in the table above); out of proportion to check exhaustively for a single generic volume-level "cipher" mention within this pass's budget. |
| Vespasian C VIII | *CSP Spanish, Elizabeth* (Hume, 4 vols, 1892-99) | **Not resolved — identifiers found, not fetched.** archive.org holds this edition (`cu31924032735098`, `cu31924032735106`, `cu31924032735114`, `cu31924032735122`, plus a Google-scan copy `calendarletters00offigoog` and three Michigan copies `adw2692.000[2-4].001.umich.edu`) but which of the four volumes covers 1587-1603 specifically was not determined this pass (no per-volume date range surfaced in the search metadata; would need one more archive.org metadata call per candidate). |
| Caligula D I | *CSP Scotland* vol. 9-10 (Thorpe/Bain) | **Not resolved — identifier ambiguity.** Candidates found (`calendarofstatep08grea` labelled "vol.9" but titled for the 1547-1605 Mary/Scotland run generally; `calendarstatepa00thorgoog`; `cu31924091754360`) were not disambiguated to the specific 1587-89 volume this pass. |

**Host requests this pass (LANE S worker H, 24 Sept 2026):** archive.org-family (advancedsearch, metadata,
djvu.txt downloads) 20, all one at a time, >=3s apart (well under the shared 60-request session cap; none of
this session's other three targets touched archive.org). be-api.us.archive.org fts: 1 (sanity-check
reconfirming the earlier "unreliable on this OCR generation" finding, not pursued further). No
british-history.ac.uk, no TNA Discovery, no Gallica/archivesetmanuscrits, no Google Books calls for this
target (its Google Books queries remain pending, not this worker's slot task).

Not "new"; not "unpublished" (rule 10) — Galba B IV joins the already-established pattern that this whole
Tudor-diplomatic-cipher run was worked and printed by Brewer/Gairdner/Gardiner between 1862 and 1920; the
"strong candidate" line for Vitellius B XIII is explicitly not a claim, only a lead for whoever resolves the
OCR ambiguity next.

## Verdict

**Status: found-solved**, for the material actually checked — consistent with this row's own flag ("caution
row... low expected yield given the editorial coverage"). Of the 5 volumes with a specific, citable reference
found this pass (Vespasian C I, Galba B VII, Caligula B VII, Caligula C IV, Caligula C VI), **4 show at least
one cipher item already read at grade H** (a key or plaintext already in a known source: Tomokiyo's Cryptiana
reconstructions, or, for Caligula C VI f.128, print in Robertson's 1759 *History of Scotland*) — these should
be dropped from any future campaign as already-solved. The one exception found is **Caligula C IV f.278**, "a
few words in cipher, not deciphered" per Tomokiyo's own page — too small a fragment to be a live cryptanalytic
lead on its own, but technically still open.

**Follow-up (24 Sept 2026, LANE S worker H): of the 9 previously-unchecked volumes, 5 are now checked.**
**Galba B IV joins the found-solved group** — at least 6 cipher items already printed with contemporary
1516 decipherments in Brewer's 1864 L&P edition (see table above; item 2673 stays unread even there, "one
passage in cipher, undeciphered"). **Vitellius B II and Vespasian F VI were checked and not found** in
their expected calendar volume (real, if narrow, negatives — not the earlier pass's tooling gap). **Vitellius
B XIII** has a strong but OCR-ambiguous candidate (no. 891-892, Casale/Benet to Henry VIII, 23 March 1532,
"Cipher deciphered", also cross-cited to Burnet's *History of the Reformation* iv.176) not confirmed enough
to change its status word. **Vitellius B VII, Galba D III, Vespasian C VII, Vespasian C VIII and Caligula D
I remain unconfirmed** — the BHO Cloudflare gate is now resolved for future workers by the download-and-grep
route this pass used successfully instead (no browser_fetch.js needed), but this pass ran out of budget
identifying the exact archive.org volume for these five before fetching them. Given the pattern across all 6
checked-and-found volumes (Vespasian C I, Galba B VII, Caligula B VII, Caligula C IV, Caligula C VI, Galba B
IV) and the adjacent-volume corroboration from both solver repositories (an entire neighbouring Vespasian C
III/C IV run already found-solved), the working prior for the remaining 5 is that most will resolve the same
way once the correct volume identifier is pinned down — but this is a prior, not a finding, and rule 10
forbids treating it as one.

Not "new"; not "unpublished" — several items here are demonstrably already read (Tomokiyo's own keys, one
printed in 1759, six more in Brewer's 1864 L&P edition); the rest is a search result, not a discovery.
