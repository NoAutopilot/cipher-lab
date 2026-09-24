status: n/a (a source-harvest manifest, not a cipher target)

# Huygens correspondence editions beyond WVO, cipher-letter harvest, 24 September 2026

LANE N harvest worker (hvHUY), brief `.claude/briefs/runs/2026-09-24-lane-n-hvHUY.md`, orchestrator
session_01W4z8JhXJYHRjorPC1Qkpiy. Job: find the same "in cijfer" / "onopgelost" pattern that
`sources/wvo/NOTES.md` found in the Willem van Oranje correspondence database, in the other Huygens
correspondence editions named by the brief -- Heinsius, Grotius, De Witt, Willem III/Bentinck-Portland,
Van Oldenbarnevelt, and the Staten-Generaal resolutions/despatches. Never check-solved, never promote, no
reading/solving beyond confirming a cipher passage exists in the editorial apparatus.

## Method

The QUEUE.md "Dutch and Belgian archives" section (24 Sept 2026 scout) had already found the productive
route for Willem van Oranje (WVO, a proper record database with an `opmerkingen` field) and explicitly
flagged that "the 1576-1625 resolutions, Bescheiden Oldenbarnevelt, Brieven van Johan de Witt, Heinsius and
Willem III/Bentinck editions are served only as page-image 'retroboeken' viewers with no full-text search
endpoint found this pass -- not searched (flagged for a future sweep)." That sweep is this harvest.

1. **Found each edition's `retroboeken` sub-site** from `resources.huygens.knaw.nl`'s own root link list:
   `retroboeken/heinsius` (Briefwisseling van Anthonie Heinsius, Veenendaal ed., 19 volumes), `retroboeken/
   dewitt` (Brieven aan/van Johan de Witt, Japikse ed.), `retroboeken/oldenbarnevelt` (Bescheiden
   betreffende het beleid van Van Oldenbarnevelt), `retroboeken/willemiii` (Correspondentie Willem III en
   Bentinck), `retroboeken/statengeneraal` (Besluiten Staten-Generaal, old + new series). Grotius has a
   *different* app (`grotius.huygens.knaw.nl/years`), not a retroboeken viewer -- not pursued, see caveat
   below (it duplicates the EM section's ePistolarium lead).
2. **Reverse-engineered the retroboeken viewer's own full-text search.** Each book is a Dojo/Zope page-turner
   whose "Zoek" (search) accessor pane is fetched lazily by JavaScript; the pane's own HTML form (fetched
   directly, no JS needed) gives the exact POST/GET field name (`search_term:ustring:utf-8`, sometimes with
   a `source_id` selector for "alle boeken" vs one volume) and the accessor's own path segment, which differs
   per book (`search_in_text` for heinsius/dewitt, `searchText` for oldenbarnevelt/willemiii/statengeneraal).
   This is a real full-text OCR search across the entire multi-volume printed edition, not a curated
   database field like WVO's `opmerkingen` -- it hits the OCR'd text of both the letters themselves and the
   19th/20th-century editors' own footnotes, so "cijfer" catches ordinary Dutch "figure/number" as noise the
   same way it did for the Staten-Generaal SG-resolutions search in the Dutch/Belgian scout section; the
   compound/derived terms below are much cleaner.
3. **Ran narrow terms, not the broad "cijfer".** `cijfer` alone returned 169 hits for Heinsius across 19
   volumes (spot-checked: mostly financial/accounting "digit" noise plus real hits already caught by the
   narrower terms) -- too many to read within budget and not run to completion. `cijferschrift`,
   `onopgelost`, `gecijferd` and `ontcijfer` (0 hits everywhere -- this exact stem is not how the OCR'd
   editions render it; "niet opgelost" as two words is caught by `cijferschrift` instead) gave: Heinsius 13 +
   9 + 0, De Witt 9 + 4 + 2, Oldenbarnevelt 6 + 0 + 0, Willem III 18 + 7 + 5, Staten-Generaal 6 + 2 + 1 -- all
   within one 20-result page each, no pagination needed.
4. **Read the search snippets, then the actual printed page** for every hit that looked like a genuine
   unsolved-cipher remark (not "opgelost"/"ontcijferd" = solved, not "niet aangetroffen" = cipher passage
   missing entirely). The search result's `onclick="return showPage(page=N, source=M, ...)"` gives the
   internal `page_index`/`source_id` pair; `retroboeken/<book>/pages.json?source=<M>` (fetched once per
   volume needed) maps that to the real `html_url`/`image_url` for the OCR text and page-image JPEG. This
   is the same access pattern for all five books, just with different `<book>` slugs and volume ids.
5. **Confirmed the "H.A." archive siglum used throughout the Heinsius edition is Nationaal Archief 3.01.19's
   own inventory numbering.** `www.nationaalarchief.nl/onderzoeken/archief/3.01.19` titles itself "Inventaris
   van het archief van Anthonie Heinsius..."; `www.nationaalarchief.nl/onderzoeken/archief/3.01.19/invnr/756`
   (the H.A. number cited for letter 357 below) returns 200 with a scan viewer present ("Scan"/"Viewer" in
   the page). **Corrected 24 Sept 2026 (LANE N2 worker csHU2):** that "Scan"/"Viewer" text is generic page-
   shell boilerplate, identical on every invnr regardless of digitisation, and is NOT a per-item confirmation.
   The real signal is the same page's embedded `drupal-settings-json` -> `viewer.response`, which gives a
   per-item `availability` field and `scans` array; a positive control (NA 1.04.02 invnr 1, a VOC item) shows
   `"availability":"DIGITALIZED"` with real IIIF `info.json` image URLs at `service.archief.nl`, proving the
   accessor works correctly. Checked this way for six Heinsius invnrs cited in this harvest's own TSV --
   **756 (HU1), 946 (HU2), 1836 (HU5), 1975/2030/2044 (HU4), plus 2315/2316/2317 (a candidate cipher key found
   for HU2)** -- and every one of the nine returns `"availability":"PHYSICAL","scans":[]`. **None of the
   cipher-relevant items checked so far in NA 3.01.19 is actually digitised**, reversing this harvest's
   "many inventory numbers scanned on nationaalarchief.nl" general expectation for this specific slice of the
   archive (item 5's "general expectation" language above may still be true for the archive as a whole; it is
   not true for the cipher letters found by this harvest). Copy orders/REQUEST.md now written for HU1, HU2,
   HU4 and HU5 in their own folders.
6. **Classification is a heuristic reading of the editorial footnote**, exactly as WVO's harvest did for its
   `opmerkingen` field -- not a check-solved verdict (the brief forbids running check-solved here) and not a
   claim about what the *manuscript* actually says (rule 2, image over transcription: none of these
   printed-edition pages were checked against the archive's own manuscript image this pass; the "image" seen
   here is the *printed edition's own page scan*, which is one step closer than a plain transcription but is
   still not the original letter).

## What was found, by circle (see the TSV for full detail)

- **Heinsius, van Dopff, 18 May 1702 (HU1).** A numeric code (unrelated names replaced by numbers like 110,
  103, 121, 105, 111, 174, 37) with the editor's own footnote: "De sleutel van dit cijferschrift is niet
  gevonden" (the key to this cipher was never found). Single instance -- unicity risk without a sibling.
- **Heinsius, Sauniere de l'Hermitage, three letters Feb-May 1704, all H.A. 946 (HU2).** The same London-based
  correspondent's cipher passages are marked "gedeeltelijk in onopgelost cijferschrift" across letters 166,
  177 (which cross-references 166) and 477 -- the same unsolved system recurring three times in one
  three-month run, which helps unicity distance even though no solved sibling exists yet.
- **Heinsius, Schonenberg (Lisbon), 24 Jul 1709 (HU3).** One unsolved word/phrase in the body text, H.A. 1445.
  Low extent alone.
- **Heinsius, H.W. Rumpf / van de Bie (Rotterdam then Stockholm), 1716-1719 (HU4).** The most interesting
  circle found this pass: letter 142 (17 Nov 1716) has a cipher passage the editor states was "door d'Alonne
  niet opgelost" -- d'Alonne being Heinsius's own professional decipherer, so this was a contemporary failure,
  not just a later editorial one. Letter 309 (23 Mar 1718, H.A. 2030) is addressed directly "Aan A.T. d'Alonne
  in onopgelost cijfer" -- sent *to* the decipherer and still unsolved. Letter 446 (15 Aug 1719, H.A. 2044,
  from van de Bie) has TWO runs of cipher lines removed from the print entirely ("Enige regels" / "Twee
  regels onopgelost cijferschrift weggelaten") -- the ciphertext itself is not even in this edition, only
  the NA 3.01.19 original would carry it. A third instance (approx. printed p.337, one more omitted line) is
  in the same volume span but its exact letter number/sender was not resolved this pass (budget). All of
  these sit under the broader De Bie/Rumpf reporting relationship from Sweden during the endgame of the Great
  Northern War, which recurs across at least three archival years (1975, 2030, 2044) without d'Alonne ever
  breaking it -- worth treating as one cryptanalysis campaign with several ciphertext instances rather than
  one letter at a time.
- **Heinsius, van Borssele van der Hooghe, 3 Apr 1714, H.A. 1836 (HU5).** An unsolved cipher letter on the
  same leaf as no. 959, PLUS the editor's note that a solution of an enciphered letter (about the queen's
  health) is *also present nearby*, "mogelijk dezelfde" (possibly the same one). This is a genuine recovery
  lead -- if the "oplossing" the editor saw is for this exact letter, it is already solved and this is
  found-solved, not open; if it is for a different letter in cipher, this is a sibling-alignment case exactly
  like WVO's NB1 pattern. Neither has been checked against the actual leaf this pass.
- **Willem III/Bentinck, Vaudemont correspondence, *25 Mar 1699 (HU6).** Found via the edition's own
  alphabetical letter-index page (KS 24 p.812), which marks cipher letters with an asterisk throughout the
  Vaudemont run (1692-1699+) -- only this one entry's marginal note was read in full: "grootendeels in
  onopgelost cijferschrift; ook een ontcijferde brief is aanwezig" (mostly in unsolved cipher; a deciphered
  letter is ALSO present). A solved sibling is stated to exist in the same correspondence run. The index page
  itself is a lead for a much larger future sweep -- it lists many more asterisked (cipher) entries across
  the whole Vaudemont correspondence that were not individually opened this pass.
- **De Witt, van Beuningen circle, 15 Mar 1656 and 19/29 Sep 1657 (HU7, HU8).** Two distinct recovery-shaped
  leads from "Brieven aan Johan de Witt" deel 1: (a) four numeric groups the editor tried against a *named,
  otherwise-working key* ("het cyfer van de heer Nieupoort", the resident in England's own cipher) and still
  could not resolve -- suggesting either a transcription slip or a table-version mismatch, not a fresh
  cryptanalysis problem; (b) an explicit statement that the identical letter survives BOTH as an
  (apparently plain) copy not in Van Beuningen's hand AND separately as an unsolved cipher copy "van een
  andere hand" -- if both survive, this is a known-plaintext pairing, the strongest kind of lead in
  LESSONS.md's own ranking, not ciphertext-only. Letter numbers were not resolved this pass (the search
  snippet's page context did not carry the letter heading within budget); a follow-up needs one more page
  fetch each to get the exact `van ... , [date]` heading and H.A.-equivalent archive reference (this edition
  uses its own numbering, not "H.A.", not yet identified).
- **De Witt, unnamed 1660s letter (not carried to QUEUE.md).** Three numeric groups (67, 31, 37) the editor
  calls omittable from the sentence -- below unicity distance alone, listed in the TSV for completeness only
  (rule 10, "report what was found") per the WVO harvest's own precedent for its NB6 row.
- **Van Oldenbarnevelt, letter no. 221, 29 May 1598 -- excluded, F-type.** The edition's own footnote says the
  original is partly in cipher but the *copy* already has it deciphered and the key survives in the same
  archival dossier (Legatie-Archief 611, IV). Not a target; kept in the TSV as a negative result so a later
  pass does not re-find it and nominate it by mistake.
- **Staten-Generaal, Deel 7 (Jul 1624-Jul 1625), p.100 -- not resolved.** "De brief is vrijwel geheel in
  cijferschrift" (the letter is almost entirely in cipher), no solution stated in the snippet, but the
  volume's internal source-id naming (plain "7" vs "7OR"/"7NR" for old/new series) was not disambiguated
  before the budget for this pass ran out, so the sender/date/archive reference were not recovered. Not
  carried to QUEUE.md as an HU row; flagged here for a five-minute follow-up (one more `pages.json?source=7`
  fetch plus the matching page fetch).

## Caveats

1. **Nothing here has been check-solved.** Every row rests on the edition's own 19th/20th-century editorial
   footnote (Veenendaal for Heinsius, Japikse for De Witt, and the respective editors for the other three),
   read from the OCR'd printed page, not from the manuscript. Per rule 2 and the common-tail quality rule, no
   row should be scored `open` by a later worker until check-solved's six-source sweep runs, and per the
   check-solved lesson of 24 Sept 2026 (Thurloe/Montagu), any of these editions could itself print a facing
   or interlinear decipherment for one of these very letters that this pass did not see, because the search
   only found the editor's *footnote about non-decipherment*, not a positive check that no decipherment
   exists on an adjoining page.
2. **HU5 and HU6 are explicitly ambiguous** between "already solved, just not adjacent in this footnote" and
   "a real recovery lead" -- the next worker on either must read the actual leaf/index before nominating
   further, not just this harvest's footnote paraphrase.
3. **Grotius was not searched by this harvest.** `resources.huygens.knaw.nl/briefwisselinggrotius` links out
   to a separate app (`grotius.huygens.knaw.nl/years`), not a retroboeken viewer, and the "Digital correspondence
   editions with cipher notes" QUEUE.md section (24 Sept 2026, LANE N) already found and partly read the
   Grotius-Reigersberch "cijfer" hits via the Huygens ePistolarium/tc13 backend (17 hits, 2 of 17 read, 15
   unread, flagged there as "a lead, not a candidate" -- see QUEUE.md's "Digital correspondence editions"
   section). Re-running that search here would have duplicated that lane's work; the 15 unread ePistolarium
   hits remain that section's own flagged follow-up, not picked up here.
4. **A DECODE catalogue overlap risk, not excluded by name-matching alone:** `aaymeloglu/unsolved-ciphers`'s
   `catalogue/decode-catalog.csv` row 2827 is "Nationaal Archief... collection 1.10.29 Familie Fagel, inv.
   nr. 5345... cipher_Bentinck_1748" -- a *different* Nationaal Archief collection (1.10.29 Fagel family, not
   3.01.19 Heinsius) and a later date (1748) than the "Correspondentie Willem III en Bentinck" edition's own
   span (which ends with Willem III's death in 1702), so it is very unlikely to be the same item as HU6, but
   it was not read this pass to confirm -- flagged for whoever picks up HU6.
5. **"H.A." archive-siglum resolution (item 5 in Method) was spot-checked on one inventory number only**
   (756). If a future worker hits an H.A. number with no live NA 3.01.19 record, that is new information, not
   a contradiction of this note.
6. **No PDF or image was downloaded**, per the brief (copy-free harvest only, no capture). The printed-edition
   page images (`image_url` in each book's `pages.json`) were not fetched, only the `html_url` OCR text --
   the next worker on any of these rows should still get the manuscript image from NA 3.01.19 directly (rule
   2), not rely on the printed edition's own page scan as "the image."
7. **Letter numbers/senders for the third Deel 19 instance (HU4's "455" row) and both De Witt rows (HU7, HU8)
   were not fully resolved** -- their printed-page headings sit on an earlier page than the footnote/snippet
   fetched, and one more page fetch each (cheap, same pattern as the rest of this note) would close the gap.

## Requests

`resources.huygens.knaw.nl`: approximately 95 this pass (2 root/reachability checks; 5 edition landing pages;
5 book-root/redirect probes; 5 `book_data.js` fetches; ~14 search-form/search-result fetches across the
narrow-term sweep [cijfer x5, cijferschrift x5, onopgelost x5, gecijferd x5, ontcijfer x5 -- not all landed,
some 404'd on a wrong accessor name before the right one was found]; 13 `pages.json?source=` fetches; ~24
individual OCR-page `html_url` fetches). All ≥2s apart, descriptive User-Agent
(`cipher-lab research script (contact via repository)`), no logins, no images downloaded, well under the
250-request budget named in the brief.
`www.nationaalarchief.nl`: 3 (root reachability re-test after the earlier-session 503 outage was confirmed
over; the 3.01.19 collection landing page; one inventory-item page, invnr/756). Well under the 100-request
budget named in the brief.
`github.com`: 2 shallow clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`), grepped for
Heinsius/Grotius/de Witt/Bentinck/Portland/Oldenbarnevelt, kept on disk in `/tmp`, not committed.
No other hosts touched. No subagents (brief did not name any). No novelty wording; nothing promoted; no
check-solved run.

## Addendum, 24 September 2026 (LANE N2 check-solved+access worker csHU2)

Ran check-solved on HU1 and HU2 (see `ciphers/heinsius-dopff-1702/` and `ciphers/heinsius-hermitage-1704/` for
full sweeps) and the NA 3.01.19 digitisation check named in item 5 above (now corrected). Two findings worth
recording here for the next worker on this series:

- **A candidate cipher key survives in the same archive as HU2's letters.** NA 3.01.19 invnr. 2317, "Sleutel
  van een cijferschrift, waarschijnlijk voor correspondentie met Engeland" (c.1705), sits in a small dedicated
  "Cijferschrift" subsection (invnrs 2315-2317) at the end of the Heinsius series, found via WebSearch, not the
  retroboeken viewer. Not confirmed to match Sauniere de l'Hermitage's cipher (the editor's own "waarschijnlijk"
  is uncertain), but no better-fitting English correspondent exists among HU1-HU8. Worth a targeted search of
  this "Cijferschrift" subsection (and any sibling subsections in other correspondents' archives, e.g. is there
  an equivalent in 3.01.17 De Witt or elsewhere) for keys matching other rows in this table -- not done this
  pass (out of scope, flagged as a lead).
- **HU2's letter 166/177/477 footnotes cross-reference each other but a fourth instance (letter 251, same H.A.
  946 dossier) uses different wording** ("Door Sauniere gedeeltelijk in cijferschrift gesteld", no "onopgelost")
  -- ambiguous whether already resolved by the editor. See `ciphers/heinsius-hermitage-1704/NOTES.md`.
- **HU8's archive (Brieven aan Johan de Witt, van Beuningen circle) is confirmed NA 3.01.17**, via the printed
  edition's own front matter and EMLO's project page (not this harvest's search route) -- see
  `ciphers/vanbeuningen-dewitt-1657/NOTES.md`. The specific inv.nr for the 19/29 Sept 1657 letter (and its
  separately-surviving cipher copy) remains unresolved; EMLO's advanced search is a React app that needs
  interactive form-filling, not URL query guessing.
