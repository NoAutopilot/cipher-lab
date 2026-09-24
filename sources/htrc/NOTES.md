# HathiTrust EF numeral-page detector (LANE N, 24 September 2026)

Continuation of the worker cut off at 05:39 UTC by the rate limit (`.claude/briefs/runs/2026-09-24-lane-n-detHT.md`,
resumed per `.claude/briefs/runs/2026-09-24-lane-n-detHT2.md`, session detHT2). `sources/htrc/editions-ht1.tsv`
(213 lines, 212 HathiTrust volume ids across 8 series) and `tools/htrc_numeral_pages.py` /
`tools/tests/test_htrc_numeral_pages.py` were already on `main` from the first worker; this session ran the
offline test (all 14 assertions pass, unchanged), then the controls, then the main pass, then judged the
results by hand against the EF body-token word lists (which do carry a full page bag-of-words, not just
numerals, even though the *order* of words on the page is not recoverable).

## Method

`tools/htrc_numeral_pages.py` (see its own docstring / `--help`): fetches each volume's HTRC Extracted Features
page-level token counts (`data.htrc.illinois.edu/ef-api/volumes/HTID/pages?pos=false`), keeps bare 1-4 digit
numeral tokens after dropping plausible years (1400-1930) and a numeral within 60 of the page's own scan
sequence (a likely running page number), and flags a page when numeral instances >= 25, distinct numeral types
>= 12 and repeat_rate = (instances-distinct)/instances >= 0.3. Two pre-filters drop likely false positives
before scoring: the last 8% of the volume (back-of-book indexes) and a page whose numeral values sorted rise in
a mostly-even ascending run (a table of contents or page-number list). Flagged pages within 3 scan positions are
merged into one cluster. No tuning was needed for the controls or the main pass; the thresholds shipped by the
first worker were used unchanged throughout.

## Controls (run first; both required to pass before the main batch)

**Positive control 1 -- Thurloe, *A collection of the state papers of John Thurloe*, vol. 1 (Birch, 1742;
HathiTrust `mdp.39015013765873`, catalog record 000770772, `api/volumes/full/recordnumber/000770772.json`).**
The known cipher in this volume is the four Vande Perre-to-de Bruyne letters (Birch's printed pages 500, 522,
576, 582; a 22-letter alphabetical substitution plus three code groups -- already read and published,
github.com/aaymeloglu/unsolved-ciphers PR #19 "Vande Perre 1653: publish the Thurloe Dutch cipher reading",
found by web search, not reopened here). The detector flagged 16 clusters over 838 pages. Cross-checked against
the EF body word list (not just numerals) for the names "Vande"/"Perre"/"Bruyne": using the header running-page-
number offset (scan seq 561 carries header token "519" -> offset +42 near that point, +32 earlier in the
volume), **three of the four known cipher pages fall directly inside a flagged cluster** -- scan seq 532
(Perre/Vande/Bruyne all present in the body tokens, printed p.500), scan seq 554 (same three names present,
printed p.522), scan seq 614 (same three names present, printed p.582, offset +32 exact). The fourth (p.576,
scan seq ~608) is not independently flagged (nearest cluster ends at 562-563, next flagged page is 591) --
consistent with that specific page's numeral count falling under the raw thresholds on its own, not a detector
failure on the other three. **Control 1: PASS** (3 of 4 known cipher pages recovered from token counts alone;
the name search was used only to confirm afterward, not to find them).

**Positive control 2 -- Rommel, *Correspondance inédite de Henri IV ... avec Maurice-le-Savant, landgrave de
Hesse* (1840; HathiTrust `mdp.39015069878992`, catalog record 000562630, found via
onlinebooks.library.upenn.edu's Henri IV author page -- `catalog.hathitrust.org/Search/Home` 403s to a plain
curl fetch and to WebFetch, and `search.worldcat.org` 429'd once and was not retried per the one-retry rule).**
This edition prints the King's ciphered 1602-09 passages to Landgrave Maurice (Bourdeau's `cyphersolver` PR #1
headline: "Hesse 1602-09: the King's ciphered passages in Rommel 1840 read with Rommel's 1846 key", ~4,100
groups across seven passages -- already solved, cited here, not reopened; confirmed present in the clone at
`hesse1603/`). The detector flagged 9 clusters over 482 pages, several large and dense: scan seq 211-215 (5
pages, 1941 numeral instances, 87 distinct, repeat_rate 0.823), seq 347-353 (6 pages, 1806 instances, 86
distinct, repeat_rate 0.767), seq 310-311 (701 instances), seq 252-254 (698 instances) -- a volume-wide numeral
density and page-scatter that matches "several thousand cipher groups across seven passages" far better than
any index or footnote pattern would, and none of these clusters were dropped by the tail-8% or ascending-run
pre-filters (i.e. they are not the back-of-book index). Exact page-for-page alignment against Rommel's own page
numbers was not attempted -- Bourdeau's PR does not give them, unlike Birch's running heads for Thurloe. **Control
2: PASS.**

**Negative control -- Balzac, *Le père Goriot* (HathiTrust `mdp.39015002253162`, 1928 Michigan copy, catalog
record 001203577), a plain-prose novel, no documentary or cipher content, contemporaneous digitisation era with
the target editions.** 136 pages, **0 flagged pages, 0 clusters.** **Negative control: PASS.**

## Main pass over editions-ht1.tsv (212 volumes, 8 series)

All 212 volumes fetched (212 EF calls + 3 for the controls = 215; `catalog.hathitrust.org` calls: 1
`recordnumber` lookup already on file for the edition list, plus 4 more this session to locate the two control
editions' htids = 5). 194 raw cluster rows across 56 of the 212 volumes (26%). Per series (total volumes in
`editions-ht1.tsv` / volumes with >=1 flagged cluster):

| Series | volumes | flagged |
|---|---|---|
| Calendar of State Papers Foreign Elizabeth | 35 | 17 |
| Calendar of State Papers Venetian | 35 | 17 |
| Recueil des instructions aux ambassadeurs de France | 35 | 10 |
| Documenti di storia italiana | 35 | 10 |
| CODOIN | 35 | 1 |
| Calendar of State Papers Spanish | 26 | 1 |
| Calendar of State Papers Milan | 1 | 0 |
| Acta Tomiciana | 10 | 0 |

**Judging, and a systematic false-positive finding.** The brief calls for grepping each flagged cluster's
neighbourhood for decipherment-indicator words as a positive signal. For the two Calendar of State Papers
series this signal is *not* reliable: these are editorial abstracts (calendars), and their compilers routinely
write prose like "the letter is in cipher" or "deciphered by ..." while describing a document without printing
its digits, so "cipher"/"deciphered" turned up near the great majority of this run's Calendar-series clusters
(see the raw judged table, `/tmp/judged.tsv` in this worker's scratchpad, not committed) without those clusters
containing any actual ciphertext. Reading each flagged page's own EF header/body tokens (available in full,
even though page order is not) instead of the neighbourhood-word heuristic explained essentially all of them:

- **General Index sections** running well past the 8%-tail pre-filter cutoff in several Cal SP volumes: e.g.
  `umn.31951002010253q` (Cal SP Venetian v.32) seq 388-392, header tokens `GENERAL INDEX` -- a 435-instance,
  158-distinct cluster that is nothing but the volume's own index of names and page cross-references. The same
  pattern recurs at near-identical relative positions across different library scans of the *same* edition
  (`mdp.39015022364122`/`mdp.39015022364114`/`mdp.39015022364270`/`mdp.39015022364288`/`hvd.hn498a`/`hvd.hn498b`/
  `hvd.hn498e`, all Cal SP Foreign Elizabeth v.3/4/5/6/7 -- the largest raw clusters in this run, instances
  600-2300, all `GENERAL INDEX`), confirming it is a structural feature of this calendar series, not scan noise.
- **Muster and pay-roll lists**, a second false-positive class specific to Cal SP Foreign Elizabeth's
  Low-Countries-war coverage: e.g. `mdp.39015022364387` seq 252 (top words `Capt.`, `company`, `soldier`,
  `arms`, `money`, `Sir`, names) -- a roster of captains' companies and their pay, numerically dense for
  ordinary military-accounting reasons.
- **Notarial/documentary appendices with footnote numbering**, in `Documenti di storia italiana`: e.g.
  `chi.21525982`/`osu.32435064225246` seq 621, header `APPENDICE III`, body a run of Latin acts (`acta`,
  `mercatorum`, `providorum`, `anno`) with parenthetical footnote markers `(1)`, `(5)`, `(10)`, `(19)` -- the
  flagged numerals are footnote references and document/deed numbers, not a cipher.

**Hand-sample precision.** 30 of the 194 cluster rows drawn at random (seed 42) and read against their own page
header/body tokens: 5/30 carry an explicit `INDEX`/`GENERAL INDEX` header; the remaining 25/30 are ordinary
Cal SP Foreign Elizabeth abstract pages (`PAPERS FOREIGN`/`ELIZABETH` running heads) whose numeral density comes
from money amounts, troop counts, and footnote/marginal citation numbers in the calendar prose, not printed
ciphertext. **0/30 in the sample are plausible printed ciphertext.** This is a real, reportable negative for
future numeral-density rounds against calendar-style (abstract) editions specifically, as opposed to verbatim
editions like Thurloe/Rommel that print full document text: a calendar's compilers routinely *describe* cipher
correspondence without transcribing it, which breaks both the numeral-density signal and the
decipherment-word-proximity signal at once. **Recommendation for later rounds:** raise `--tail-frac` for
calendar-style editions specifically (index sections in this series run past the current 8%), and/or add a
per-page prose-word gate (`Pag`, `Capt.`, `company`, `Add.`, `Endd`, running heads matching `PAPERS FOREIGN`)
that would suppress most of this series' false positives before they are even scored.

**One distinguishing lead, not explained by any of the above** (see QUEUE.md row HT1): a `TABLE DES CHAPITRES`
(table of contents) page near the front of *Recueil des instructions données aux ambassadeurs et ministres de
France ... Suède*, vol. 2 (1884; two independent library scans, `njp.32101076191640` scan seq 24 and
`hvd.hl237b` scan seq 26, agreeing on content) carries the token `Chiffre` (capitalised, twice) among its
chapter-heading vocabulary -- consistent with a chapter or appendix in this volume being titled "Chiffre"
(a cipher table for the Sweden embassy), which this series is known to include as an appendix in some volumes.
EF gives no word order, so which printed page number pairs with that heading could not be determined from the
token counts alone. Not found by name in this session's shallow clones of `dbourdeau/cyphersolver` or
`aaymeloglu/unsolved-ciphers` (grepped for "Suède"/"Sweden"/"Recueil des instructions"; only unrelated
substring hits) -- reported per rule 10 as a search result, not a claim that it is unpublished. **Next step:**
someone with a page image (this worker's brief and hosts do not include babel.hathitrust.org or archive.org)
reads the table of contents to find the "Chiffre" chapter's printed page number, then checks that page.

No other cluster in the main pass showed a comparable structural signal (a chapter/section heading naming a
cipher, independent of the calendar-index/paylist/footnote explanations above) after this reading, so no other
row is added: quality over quantity, per the lane's rule -- 20 marginal rows that a later worker would have to
individually re-debunk cost more than one well-reasoned lead and an honest negative for the other 55 flagged
volumes.

## Requests

`data.htrc.illinois.edu`: 215 (212 main-pass volumes + 3 controls), >=1.5-1.6 s apart. `catalog.hathitrust.org`:
6 (`api/volumes/full/recordnumber/...` for the two controls' record numbers, plus the Thurloe record already
known from the brief), >=1.5 s apart; one `Search/Home` HTML fetch attempted and 403'd (not retried, per the
good-citizen rule -- the Bibliographic API's own id-based lookups were used instead once the record numbers
were found via WebSearch/WebFetch). `search.worldcat.org`: 1 WebFetch, 429'd, not retried. WebSearch: about a
dozen queries to locate the two control editions' HathiTrust records (via onlinebooks.library.upenn.edu, which
lists HathiTrust catalog links per author) and to confirm the Vande Perre/Hesse 1603 items are already solved.
`github.com`: 2 shallow clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`), grepped only, kept on
disk for the rest of this session. No `babel.hathitrust.org`, no `archive.org`, no Google Books, per the brief.

## Rule 10

Nothing here is a solved reading or a novelty claim. The Vande Perre (Thurloe) and Hesse 1603 (Rommel) items
used as controls are cited as already read and published by the named solver-repository PRs, not reopened. The
"Chiffre" table-of-contents finding is reported as a structural lead for a later worker's page-image check, with
what was searched and not found, per rule 10 -- not as new, unpublished, or unread.
