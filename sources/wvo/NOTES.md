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

## Print check G3, 24 September 2026 (worker for LANE V2, session 01BmKBy)

Job 1: for each GPA/GPAS-code letter LANE R2 stopped reading on (5194, 5207, 5213, 5221, 5549, 5797, 5799, 5810,
10260), fetched its WVO detail page once for the Groen volume/page/nr from Brongegevens, found the letter's
direct DBNL page via that volume's own Inhoudsopgave (table of contents lists every "Lettre <roman>" with a
direct link -- no page-offset guessing needed), fetched that DBNL page once, and read whether the cipher
passage is printed in clear, omitted, or left as raw ciphertext. Full table: `groen-check-2026-09-24.tsv`.

**Result: WVO's Brongegevens "(onv)" flag is not a reliable proxy for "cipher passage still in ciphertext".**
Only 5549 and 10260 carry (onv) in Brongegevens; 5797 does not, yet 5797's own printed page carries an explicit
Groen editorial note that several passages "n'ont pu etre dechiffres" (could not be deciphered) and the printed
German text has visible syntactic gaps where a ciphered name/word was dropped rather than resolved. Conversely
5207, 5213, 5221, 5799, 5810 carry no (onv) and print as complete, ungapped plain French with no cipher-related
editorial note anywhere on the page (not even an acknowledgement that the source was enciphered) -- consistent
with a silent full decipherment, but that is an absence-of-a-note inference, not a positive statement from
Groen, so they are marked `unclear` rather than `yes` in the TSV.

Three distinct patterns found across the nine letters (evidence quotes in the TSV):
1. **Silently printed in clear, no cipher note at all**: 5207, 5213, 5221, 5799, 5810 (5 of 9). Whole letter,
   ordinary plain French, footnote only "Autographe" where present.
2. **Explicitly printed in clear with an editorial note confirming full decipherment**: 5194 -- "d'ordinaire le
   dechiffrement y est joint" (the decipherment usually accompanies it).
3. **Genuinely still ciphertext in the print**: 5549 -- Groen's Supplement prints the coded passage as raw
   numbers (e.g. "73. 50. 28. 9. 335...") interleaved with a handful of plain German connector words, never
   deciphered. This is a different case from "omitted": the numbers themselves are there, so a worker with the
   key could in principle check WVO's own transcription against this 1847 print as an independent witness.
4. **Explicitly printed with gaps, not fully deciphered**: 5797 -- Groen's own headnote says so outright, and
   the printed German text has short clauses missing their subject where a coded name once stood.
5. **Ambiguous**: 10260 -- WVO marks (onv) but the Groen VII printing itself reads as continuous plain French
   with no visible chiffre marker; the letter has four further editions (Lacroix/LMSAC 1860, Muller/MBWI 1888,
   Gerlo-de Smet/GSME 1990-96) not cross-checked this pass, any of which could hold the (onv) gap Groen's own
   print does not show.

**For LANE R2/V2:** before reading any cipher passage of 5207/5213/5221/5799/5810 as a genuine unread target,
open the DBNL page linked in the TSV and grade the reading against that print (silent-decipherment letters are
candidates for N0/N1, same pattern as 5200/5811/4503, not for a fresh S-grade attempt). 5549 is the one letter
in this batch where the ciphertext itself, not the plaintext, is what Groen printed -- a possible independent
transcription check, not a solved reading. 5797's gaps are Groen's own unsolved residue and may be worth a
fresh attempt with the modern key if one exists. 10260 needs its other four editions checked before any grade.

Job 2: WVO's own `bronnen` page and `literatuurlijst` give no abbreviation legend (confirmed again, same as the
24 Sept harvest above); the working legend has to be built by matching each briefnr's own Brongegevens list
(which gives each source's full name) against that briefnr's `archive_bronnen_codes` column in
`cipher-letters-2026-09-24.tsv`, in row order -- the two lists correspond one-to-one. Resolved this pass, from
briefnr 57 (DNOK, HHSAWB, KHAG, SAD), 10260 (GPA, GSME, HUA, LMSAC, MBWI, NA, SAG) and 8246 (JC, SAR):

- **DNOK** = Demandt, *Nassau-oranische Korrespondenzen*, printed edition. On briefnr 57 it appears as
  "Demandt, Nassau-oranische Korrespondenzen I, 78 nr. 113 excerpt" -- an **excerpt**, not the letter in full;
  whether that excerpt covers the ciphered passage is not established this pass (would need the book open).
- **HHSAWB** = Hessisches Hauptstaatsarchiv Wiesbaden (archive, not an edition).
- **SAD** = Sachsisches Hauptstaatsarchiv Dresden (archive).
- **SAR** = Staatsarchiv Rudolstadt (archive; on briefnr 8246, Kanzlei Sondershausen 693).
- **JC** = Japikse, ed., *Correspondentie van Willem den Eerste, prins van Oranje*, eerste deel (1551-1561),
  's-Gravenhage 1934, printed edition -- already flagged as "Japikse" in 8246's own `printed_edition_named`
  column, not a new find.
- **GSME** = Gerlo & De Smet, eds., *Marnixi Epistulae. De briefwisseling van Marnix van Sint-Aldegonde*, 3 dln.
  (Brussel 1990-1996), printed edition. Not previously captured in 10260's `printed_edition_named` column
  (which only lists Groen/Lacroix) -- worth adding.
- **HUA** = Het Utrechts Archief (archive; on 10260, Staten van Utrecht 704-1).
- **LMSAC** = Marnix de Sainte Aldegonde, *Correspondance et melanges*, ed. Alb. Lacroix (Parijs-Brussel-Geneve
  1860), printed edition -- same edition already flagged as "Lacroix" in 10260's `printed_edition_named` column.
- **MBWI** = Muller, 'Brieven van prins Willem I en van zijne derde vrouw...', *Bijdragen en Mededeelingen van
  het Historisch Genootschap* 11 (1888) 509-520, printed edition. Not previously captured in 10260's
  `printed_edition_named` column -- worth adding.
- **SAG** = Stadsarchief Gent (archive; on 10260, Reeks 94 bis, 29-1, marked (onv) at that repository).
- **NA** = Nationaal Archief Den Haag (archive; on 10260, Staten-Generaal 1576-1796, 11099).

flag for LANE V2: **DNOK is a printed edition** (Demandt, *Nassau-oranische Korrespondenzen 1553-1570* [Regesten], HessJb 38 (1988) 49-102 and 39 (1989) 87-150; "1962" corrected by V8, 24 Sept 2026), and briefnr
57 -- one of the two N4 items D2 set this session (57 and 53) -- carries it as an "excerpt" source alongside
KHAG/SAD/HHSAWB. This was not in D2's AUDIT.md search log. Whether Demandt's excerpt prints 57's cipher
passage (in clear or not) is unresolved and should be checked, by a verifier with book access, before 57's
N4 stands; 53, 126, 4610, 4611, 4612, 4616 carry no DNOK or other edition code, only archive-holding codes
(KHAG/SAD), so this flag is scoped to 57 alone.

Requests this pass: resources.huygens.knaw.nl 12 (9 target-letter detail pages + briefnr 57 + briefnr 8246),
all >=2s apart; www.dbnl.org 22 (4 volume tables of contents [III, IV, V, VII] + 9 detail-page fetches on a
wrong URL shape caught immediately by a "Deze pagina bestaat niet" response, not retried in a loop, + 9 correct
refetches once the URL pattern -- `/tekst/<textid>/<textid>_<page>.php`, directory repeated -- was found from
the WVO-supplied 5549 dbnl link), all >=2s apart, descriptive User-Agent. No PDFs fetched, no images opened
(text-only per this job's scope). No novelty classification made -- this is a print-location check, not a
verifier pass.

## Print status, all 73 un-nominated letters (csWV3, LANE N2, 24 September 2026)

Worker for `.claude/briefs/runs/2026-09-24-lane-n2-csWV3.md`. Full per-letter table:
`print-status-2026-09-24.tsv` (briefnr, class A/B/C, edition page, gloss-on-leaf y/n, verdict).

**Result: zero new nominations.** Every one of the 73 rows resolves to one of: already owned by a folder (19
rows, skipped per brief); already claimed by LANE R3 in ROOM.md (5549); a genuine but small residual already
handled by csWV2 with no nomination warranted (5797, 7 gaps only); a contemporary on-leaf decipherment (a "key
source", not a target -- 174, 424, 1069, 4496, 4614, 5575, 5808, 6131, 6136, 7205, 7206, 7208, 7466, plus three
newly identified this pass: 58, 1069 [see below], 7630 [carries an attached *reconstructed key* and full
decipherment], 11250 [attached to the decipherment of 5801], 12630/12631 [contemporary Spanish decipherments at
Simancas]); or Class A, an edition prints it in clear, either confirmed by page (5194, 5207, 5213, 5221, 5799,
5810 via G3's groen-check; 4503, 5811 via Verifier V7; 5200, 5218, 5222 via LANE R2's bundled-print find; 8246,
5109 via Japikse "de editie met oplossing") or inferred by pattern from the same correspondence/edition without
opening the specific page (~25 rows, all "to Jan/Lodewijk van Nassau" GPA-cited letters plus a handful of
standalone-correspondent GPA/GCGT rows -- see the TSV's "verdict" column for which). Two rows (6178, 6238) carry
WVO's own "hetgeen is opgelost" (which has been solved) with no edition or on-leaf marker at all -- classified
`blocked`, not nominated, per COMMON RULES item 9 (never open without a locatable solution or a confirmed-absent
one). 10260 stays `blocked` (four of its five named editions still unchecked).

**Corrections applied to existing folders:** jan-van-nassau-1572-75/NOTES.md's "5207, 5213, 5221... open" line
(dating from before G3's groen-check pass was cross-referenced into that folder) corrected to Class A/not open,
citing G3's own page reads. **New key-source finding, flag for LANE R3:** briefnr 11250's own WVO record states
it is "gehecht aan de ontcijfering van nr. 5801" (attached to the decipherment of no. 5801) -- 5801 (a "to
Lodewijk" GPA letter, not previously flagged beyond the generic heuristic) therefore carries a genuine
contemporary decipherment, not yet imaged. Full detail in `ciphers/lodewijk-van-nassau-1573-74/NOTES.md`.

**Unfinished this pass (write-up only, not fetched/imaged):** the ~25 "A (inferred)" rows classified by pattern
rather than by an opened page -- 124, 4494, 4495, 4497, 4498, 4499, 4502, 5201, 5204, 5205, 5208, 5209, 5210,
5214, 5219, 5224, 5227, 5228, 5798, 5800, 5802, 5803, 5804, 5805, 5812 -- would benefit from the same DBNL
page-check G3 already ran on their six siblings, before any of them is treated as a settled N-class; none is a
nomination candidate either way, so this is a confidence upgrade, not an urgent gap. 6178 and 6238's "opgelost,
location unknown" status could be resolved with a fuller search (a named journal, a local Guelders/Aachen-area
edition) if either correspondent's circle is ever revisited. 174, 4496, 4614, 6136, 7205, 7206, 7208, 7466 (all
"solved on leaf") were not fetched/imaged this pass -- a genuine opportunity for LANE R3's cross-letter key
alignment work, listed in the relevant circle folders above.

**Requests this pass:** resources.huygens.knaw.nl 9 (detail-page fetches for 58, 1069, 5109, 6178, 6238, 7630,
11250, 12630, 12631; >=2s apart, descriptive UA; spaced around LANE R3 worker J5S's concurrent use of the same
host for 5575/5550/5557/5808, no overlap). www.dbnl.org 0 (G3's existing page reads reused, per "scripts read,
fetch once" and to stay well under the 20-request cap). archive.org 0 (not needed -- WVO's own remarks and the
reused G3/folder page-checks were sufficient). No subagents (none named in the brief). Well under the $8 cap.
