status: n/a (a source-harvest manifest, not a cipher target)

# WVO database harvest, 24 September 2026

LANE N harvest worker, brief `.claude/briefs/runs/2026-09-24-lane-n-hvWVO.md`. Job: enumerate every WVO
(Briefwisseling van Willem van Oranje, `resources.huygens.knaw.nl/wvo`) record whose `opmerkingen` (remarks)
field mentions cijfer, cijferschrift, chiffre, gecijferd, onopgelost, oplossing or ontcijfering; parse into a
TSV; group the letters not already claimed by a folder into correspondence circles; mark recovery (a solved
sibling exists in the circle) vs cryptanalysis (none does). Never check-solved, never promote, no PDFs
downloaded (LANE R's capture workers do that per target, per the brief).

## Method

1. **Endpoint.** `resources.huygens.knaw.nl/wvo/app/brieven?opmerkingen=<term>&opmerkingenBool=AND&geavanceerd=1`
   is the advanced-search GET API (found by an earlier LANE N scout, `QUEUE.md` "Dutch and Belgian archives"
   section). It returns an HTML results list (briefno/date/direction/correspondent/place only — no remarks
   column) with a "downloaden als spreadsheet" CSV link, but the CSV also omits remarks (`Briefno.,Datum,
   Correspondent` only) and is session-scoped to whatever query set the cookie, so it is useless for anything
   past briefno/date/correspondent. The remarks text needed for classification lives only on each letter's own
   detail page, `wvo/app/brief?nr=<briefnr>`.
2. **Reused rather than re-fetched.** The earlier scout's `opmerkingen=cijfer` sweep already fetched and
   parsed all 96 matching detail pages into `sources/solver-diffs/2026-09-24-lane-n-wvo-cijfer-96.tsv`
   (nr/date/correspondent/place/opmerkingen/bronnen/has_ontcijferd/has_edition_source). Per "scripts read,
   models judge" and "fetch once", this harvest starts from that file rather than re-querying.
3. **Coverage check for the other five terms.** `cijfer` as a substring already covers `cijferschrift`,
   `gecijferd` and `ontcijfering`/`ontcijferd` (each contains the literal substring "cijfer"), confirmed by
   inspecting the 96-row dump. Ran the three terms it does *not* cover as separate searches: `chiffre` (1 hit,
   6131), `onopgelost` (2 hits, 1127 and 6179 — both already NB3/NB4 rows), `oplossing` (39 hits, two result
   pages, `start=25` for the second 14). Every briefnr returned by chiffre/onopgelost/oplossing is a subset of
   the 96 cijfer-search hits — the cijfer sweep is a complete superset for this brief's seven search terms, so
   no further detail-page fetches were needed for coverage. Requests: chiffre 1, onopgelost 1, oplossing 2
   (paginated), plus one `help_toelichting_pagina/bronnen` and one `literatuurlijst` probe (both unhelpful —
   no bronnen-code legend found on either page) = 6 new search-side requests, all on resources.huygens.knaw.nl,
   >=2 s apart.
4. **Three truncated remarks fields, refetched.** Three rows (424, 6131, 10260) had opmerkingen text cut off
   mid-sentence in the reused 96-row TSV (the earlier scout's extraction broke on a nested `<i>` edition-title
   tag). Refetched those three detail pages directly (3 requests) to get the full text before classifying.
   This mattered: 424's untruncated text reads "...De contemporaine kopie Archivo General de Simancas is
   ontcijferd en uit het Frans in het Spaans vertaald" (the Simancas contemporary copy is deciphered and
   translated Spanish<-French) — the truncated version had no solution marker at all and would have been
   wrongly harvested as a cryptanalysis candidate with no known decipherment. Full text moved it to "solved
   elsewhere"; it is not in the output rows.
5. **False positives excluded.** `cijfer` also matches `dagcijfer` ("day-number", i.e. a calendar digit, not
   cipher writing: nrs. 378, 390, 11643) and "Arabische cijfers" (Arabic numerals, not cipher: nr. 6754). All
   four dropped before classification.
6. **Already-claimed letters excluded from new candidacy, but kept for circle context.** Letters already
   inside a capture folder (NB1 lodewijk-van-nassau-1573-74: 4610/4611/4612/4613/4615/4616; NB2
   august-van-saksen-1561-64: 53/57/74/98/126/153/175; NB3 willem-van-hessen-1567: 1127; NB4 la-garde-1577:
   6179/6467/5564) and the two letters already tabled as QUEUE.md rows without a folder yet (NB5: 1109, NB6:
   5551) are marked `already_nominated=yes` in the TSV and excluded from the new WV rows below, but are still
   counted when deciding whether a *circle* has a solved sibling (e.g. Marnix's 6467, already imaged under
   la-garde-1577/images/, is the solved sibling that makes 10260 a recovery lead, not a cryptanalysis one).
7. **Classification is a heuristic text match**, not a check-solved verdict (the brief forbids running
   check-solved here): cipher extent from Dutch quantifiers (hoofdzakelijk/grotendeels/vrijwel geheel ->
   mainly; gedeeltelijk/ten dele/enige/enkele/twee passages -> partly; geheel in cijfer -> whole; twee regels
   -> lines); solution status from onopgelost -> unsolved; oplossing/opgelost/ontcijferd(-ing)/déchyffré
   co-occurring with a same-leaf marker (afgebeeld/bijgevoegd/contemporaine kopie/inliggend/aanwezig) -> solved
   on leaf; the same words with a named edition (Groen van Prinsterer, Gachard, Kervyn, Japikse, Nepveu tot
   Ameyde, Lacroix, Demandt, or the bronnen codes GPA/GPAS/GCGT/NAC which co-occur with those names on
   confirmed rows) -> solved elsewhere; no solution word at all -> not stated. "Not stated" is not a claim
   that a letter is unsolved — only that this WVO record's own remarks do not say so, same caveat as the NB1/
   NB2/NB4 rows above it in QUEUE.md.

## Counts

- 96 raw hits (opmerkingen=cijfer), 4 false positives dropped -> 92 genuine cipher-related records.
- 19 already covered by a folder or an existing QUEUE.md row (NB1 x6, NB2 x7, NB3 x1, NB4 x3, NB5 x1, NB6 x1).
- Of the remaining 73, grouped by correspondence circle (the named party opposite Willem van Oranje in each
  record): 5 circles contain at least one letter with no solution stated and not yet claimed by a folder.
  4 of those circles also contain a solved sibling in the same run (recovery); 0 have no solution anywhere in
  the circle after the 424 correction above removed the only apparent cryptanalysis-only case.
- Full per-letter table: `sources/wvo/cipher-letters-2026-09-24.tsv` (92 rows: briefnr, date, direction,
  correspondent, place, archive_bronnen_codes, cipher_extent, solution_status, printed_edition_named, pdf_url,
  already_nominated).
- New QUEUE.md rows: WV1-WV4 (below "United States archives" section is not touched; new section added after
  the existing "Dutch and Belgian archives" section).

## Requests

resources.huygens.knaw.nl: 12 total this pass (chiffre search 2 [one without cookie, one with, to get the CSV
link's session working — CSV link turned out to not carry remarks and was abandoned], onopgelost 1, oplossing
3 [initial + cookie-jar page 1 + page 2], help_toelichting_pagina/bronnen 1, literatuurlijst 1, three detail-page
refetches for truncated rows 1 each = 3), all >=2 s apart, descriptive User-Agent. No PDFs fetched. No other
hosts touched. Combined with LANE R's 24 requests earlier the same session, well under the shared 80-request
soft budget noted in ROOM.md.

## Caveats / follow-ups (not pursued this pass, per brief scope)

- Archive-code (`bronnen`) abbreviations are reported as WVO gives them; only KHAG (Koninklijk Huisarchief Den
  Haag), HSAM (Hessisches Staatsarchiv Marburg), ARAB (Algemeen Rijksarchief van België) and SAD (Sächsisches
  Hauptstaatsarchiv Dresden) are confirmed from the excluded folders' own NOTES.md/shelfmarks. GPA, GPAS, GCGT
  and NAC are inferred edition abbreviations (Groen van Prinsterer / its supplement / Gachard / Nepveu tot
  Ameyde) from textual co-occurrence, not from a legend page (none found — the help page and literatuurlijst
  do not define archive-code abbreviations). JC and SAR (nr. 8246) and several codes on nr. 10260 (GSME, HUA,
  LMSAC, MBWI, SAG) are not resolved.
- No image was opened for any of the 73 not-already-claimed letters this pass (rule 2, image-over-transcription,
  still applies once a target is picked up — this harvest only read the database record text).
- Full shelfmarks (beyond the archive-code abbreviation) were not fetched per-letter; the four rows promoted
  to WV1-WV4 below would need one detail-page fetch each before a capture worker starts, the same as NB1-NB6.
