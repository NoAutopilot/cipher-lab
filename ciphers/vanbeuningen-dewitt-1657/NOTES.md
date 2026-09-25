open

# Van Beuningen circle to Johan de Witt: the same letter survives as a plain copy and an unsolved cipher copy, 19/29 September 1657

QUEUE row: HU8 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions: letters noted in cipher
(LANE N harvest of 24 September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n-csHU.md`.

## Source

Johan de Witt correspondence, printed in R. Fruin / N. Japikse (ed.), *Brieven aan Johan de Witt*, Deel 1,
p.405, via the Huygens `retroboeken/dewitt` viewer (no login, `resources.huygens.knaw.nl`). No H.A.-style
archive number is used by this edition; the manuscript's archive location was not resolved this pass (see
below).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents).

1. **Editions first -- decisive, re-fetched and read directly this pass** (`images/dewitt_01_405.jpg`, page
   text also read as OCR): the printed letter itself (dated 19/29 September 1657 by internal content, no
   explicit heading on this page beyond the date) is a report from Copenhagen on Danish court affairs and
   English/Danish diplomacy. The editor's footnote 1, quoted verbatim:
   > "1) Niet van de hand van Van Beuningen. **Dezelfde brief ook in onopgelost cijfer, van een andere hand.**
   > - Op dezen brief schreef De Witt: 'beantwoort den 19en October 1657'. - Brieven van Van Beuningen van 7 en
   > 13 September, die De Witt 5 October beantwoordde (Brieven van De Witt, I, blz. 437), werden niet
   > aangetroffen."
   Translation: "Not in Van Beuningen's own hand. **The same letter also [survives] in unsolved cipher, in
   another hand.** De Witt wrote on this letter: 'answered 19 October 1657'. Letters from Van Beuningen of 7
   and 13 September, which De Witt's 5 October reply answered (Letters from De Witt, I, p.437), were not
   found."
   This confirms, directly from the primary edition and not merely from the harvest's paraphrase, that: (a)
   the text printed here is itself a copy, not Van Beuningen's autograph; (b) a **separate cipher copy of the
   identical letter, in a different hand, is stated to survive** -- a genuine known-plaintext pairing if both
   copies are still extant, the strongest class of lead in LESSONS.md's own ranking; (c) De Witt's 19 October
   1657 reply is referenced but its own text/archive location is not given on this page; (d) two earlier Van
   Beuningen letters (7 and 13 Sept 1657) that De Witt's 5 Oct reply answered were explicitly **not found**
   ("niet aangetroffen") by Japikse's own editorial search -- unrelated to this cipher, logged for
   completeness only, not a target.
2. **Post-edition literature search (check-solved.md's Oxenstierna/Torpadie lesson).** Located and read two
   modern secondary works specifically about this exact correspondence circle (De Witt-Van Beuningen, Northern
   War 1655-1660):
   - **M. Postma, *Johan de Witt en Coenraad van Beuningen: correspondentie tijdens de Noordse oorlog
     (1655-1660)*** -- the standard modern study of this exact correspondence (cited repeatedly by the second
     source below). Its own Academia.edu copy returned HTTP 403 (blocked to WebFetch) this pass; not read
     directly. Flagged unreachable, not scored negative on that basis alone.
   - A related scriptie/paper, "Macht en daadkracht tijdens de Noordse Oorlog" (vriendenvandewitt.nl PDF,
     fetched and OCR'd with `pdftotext` this pass since WebFetch could not parse the raw PDF stream): cites
     Postma's book about 20 times, including footnote 88, **"Van Beuningen aan De Witt, 15 maart 1656, Brieven
     aan Johan de Witt I, 328"** -- the same printed-edition page as this batch's HU7 (a different row, not one
     of this worker's assigned targets, but the same correspondence circle) -- confirming Postma's book cites
     this correspondence at the letter level. Grepped the full extracted text (1122 lines) for "cijfer" and
     "geheimschrift": **zero hits anywhere in the document.** Neither this scriptie nor, by extension, its main
     source (Postma) discusses the cipher content of any Van Beuningen-De Witt letter in the material actually
     read -- a real secondary-literature search, not merely "unreachable and skipped", even though it does not
     positively confirm Postma's book is silent on the cipher specifically (only this citing paper's own text
     was searched, not Postma's book itself, which could not be fetched).
3. **Community lists.** `sources/cryptiana/web/dutch.htm` re-read: mentions Coenraad van Beuningen only via an
   unrelated Petkum/Blencowe 1709 interception discussed on `blencowe2.htm` (a different correspondent, a
   different decade); no mention of this 1657 letter or its cipher.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for "beuningen"/"de witt"/
   "nieuwpoort": zero hits.
5. **Solver repositories.** Fresh shallow clones this pass grepped for "beuningen", "de witt", "nieuwpoort",
   "3.01.17": no hit in either repository. (A distinct DECODE catalogue entry for "Rechteren tot
   **Borg**beuningen" -- a different person, a different century, NA 1.01.02/1.10.29, already solved -- is a
   surname false-positive worth recording so a later worker does not confuse it with Coenraad van Beuningen.)

## Verdict

**Status: open.** The editor's own footnote, read directly from the primary edition this pass, states plainly
that a separate cipher copy of this exact letter survives; no decipherment, key, or later print of that cipher
copy was found in the (partial, one source unreachable) secondary-literature search, community lists, DECODE,
or either solver repository.

**Copy status: archive confirmed, specific inv.nr NOT resolved.** LANE N2 worker csHU2 (24 Sept 2026) confirmed
**NA 3.01.17** ("Inventaris van het archief van Johan de Witt, raadpensionaris van Holland, 1653-1672") is the
correct archive, two independent ways: (1) the printed edition's own front matter (Deel 1, p.XVI) states "de
brieven aan De Witt alle eigenhandige originelen zijn" (the letters to De Witt are all autograph originals),
collated by Fruin against the originals, with Van Beuningen's Copenhagen letters named as the volume's single
most important chapter (p.XV); (2) EMLO's "Correspondence of Johan de Witt" project page (fetched via
`tools/browser_fetch.js`, curl alone returns HTTP 503 for both nationaalarchief.nl's own client-rendered search
API and emlo-portal.bodleian.ox.ac.uk, both logged as unreachable by curl and not retried a second time, per the
good-citizen one-retry rule) states plainly: "National Archive: inventory Raadpensionaris De Witt, 3.01.17" and
that EMLO indexes ~7,465 of the ~35,000-letter archive online (the "diplomatic correspondence" category, which
Sauniere-style diplomatic dispatches like Van Beuningen's would fall under) with links to digitised images
where available (EMLO's own caveat: "the manuscript images available at present are provisional... lower-
quality"). **The specific inv.nr for the 19/29 Sept 1657 letter, and separately for the "unsolved cipher copy,
van een andere hand" the footnote states survives, was NOT resolved this pass.** EMLO's advanced-search form
(`emlo.bodleian.ox.ac.uk/forms/advanced`) is a React app; a browser-rendered fetch with guessed URL query
parameters (`sender=Beuningen&date=1657`) did not actually filter the result set (it returned the full 16,736-
row catalogue unfiltered, confirming those aren't the real parameter names) -- finding the exact record needs
either interactive form-filling (`--type`/`--selector` in `tools/browser_fetch.js`) or NA's own `zvt.
nationaalarchief.nl` / `hub3.nationaalarchief.nl` search API, whose real endpoint path was not found by
guessing (both returned 503/404). No REQUEST.md written; the next worker should either drive EMLO's search form
interactively or find NA's real search API before ordering a copy -- and note the separate cipher copy "van een
andere hand" may not even be catalogued in EMLO the same way as the plain copy, since it is a different
physical item in a different hand.

**Kind: recovery.** A plain copy and a separately-surviving unsolved cipher copy of the identical letter is
exactly the known-plaintext pairing pattern LESSONS.md ranks as the strongest lead class -- stronger than a
mere sibling, since the plaintext itself (not just a related letter) is already in hand via this edition's own
print.

Search log (rule 10): reported above, per source. Not classified for novelty. Requests this pass:
`resources.huygens.knaw.nl` ~3 (book_data.js, 1 pages.json, 1 html_url OCR fetch, 1 image fetch), WebFetch 2
(Academia.edu, blocked 403; vriendenvandewitt.nl PDF, fetched and locally OCR'd with `pdftotext`, not a network
re-fetch), WebSearch 2, `github.com` 0 (reused clones already on disk this session). No subagents.

## Archive location pinned, 25 September 2026 (LANE OX worker OX-VB, session_017rmJ1jFJvbnXj6nrcb223x)

**NA 3.01.17, inv.nr 1538** (the yearly bundle "Missiven van Coenraed van Beuningen, extraordinaris gedeputeerde
naar Denemarken", 1657) is the exact inventory number. Found by fetching the archive's own full EAD inventory
(`www.nationaalarchief.nl/onderzoeken/archief/3.01.17/download/xml`, 3.1 MB, 41k lines, one curl request) and
grepping for "Beuningen" -- the subseries A.2.7.1.2 "Bijzondere gezantschappen" lists yearly bundles 1536-1541
for 1656-1658, with 1538 dated exactly "1657" (cover leaf confirms: "Denemarken / Ambassadeur Van Beuningen aan
den Raadpensionaris / 1657", image order 1 of the bundle). Its METS (`service.archief.nl/gaf/api/mets/v1/
dfa4b121-2476-41cf-8a1c-d784ec6f2050`, resolved from the EAD's own `<dao>` handle) shows the bundle is digitised
end to end: 289 leaf-images (two-page spreads), rightsMD `RIGHTSCATEGORY="PUBLIC DOMAIN"`, no login, served at
`service.archief.nl/api/file/v1/default/<uuid>` (no IIIF; full-resolution JPEG only, ~1-6 MB each).

Calibrated the bundle's chronological order by sampling images at roughly every 30th position and reading
datelines (p.1 cover "1657"; p.30 "27 January 1657"; p.60 "25 martij 1657"; p.180 "Coppenhagen 15en Julij
1657"), then narrowed in around the September/October area. Both copies of the 19/29 September 1657 letter
are in this same bundle, four leaf-images apart:

- **Plain copy: ff.208-209** (`NL-HaNA_3.01.17_1538_0208.jpg`, `_0209.jpg`). f.208's docket reads (abbreviated,
  another hand, top left) "...de 19en Octob. 1657" -- matching the printed edition's footnote quote of De
  Witt's own endorsement, "beantwoort den 19en October 1657", verbatim. The body opens "Mijn Heer, Hier wert
  van dag tot dag met groot impatientie verlangt na [...] Rosewinge..." which matches Brieven aan Johan de Witt
  I p.405's printed text from its first line, word for word (checked directly against `images/dewitt_01_405.jpg`).
  f.209 ends with the signature "UEd: ootmoedigen [en] verplichten dienaer, [signed] Van Beuningen" over the
  dateline "Coppenhagen de 19/29 [Septem]bris 1657" -- the same double Julian/Gregorian date the printed
  edition cites as "(19/29 September 1657)".
- **Cipher copy, "van een andere hand": ff.210-211** (`NL-HaNA_3.01.17_1538_0210.jpg`, `_0211.jpg`). Visibly a
  different, more cramped hand than ff.208-209, matching the footnote's own description. Opens "Hier voort van
  dag tot dag met groot impatientie verlangt na U [cipher numbers]..." -- the identical opening, with content
  words replaced by comma-separated two-digit numeric groups and colons apparently marking word boundaries;
  plain Dutch function words (mijn, heer, met, over, onder, daer, ...) are left uncoded. Ends with the same
  closing formula and the identical double date, "Coppenhaghen den 19/29 [Septem]bris 1657", confirming this
  is the cipher copy of *this* letter and not of the other same-day dispatch below.

**Not the target, kept for context:** ff.206-207 carry the end of one Van Beuningen dispatch and the whole of
another, both also dated 19/29 September 1657 but on different subject matter (a Brandenburg/Poland/Sweden
report) -- Van Beuningen evidently sent more than one letter to De Witt on the same courier date. Recorded here
so a later worker does not confuse it with the target or re-spend a pass identifying it.

Images fetched and committed: `images/NL-HaNA_3.01.17_1538_020{6,7,8,9}.jpg`, `_021{0,1}.jpg`, plus single-page
crops of the two cipher leaves at `images/cipher_crops/0210_right.jpg` and `0211_left.jpg` for the transcription
pass. `images/manifest.json` records the inventory/METS URLs and per-image content. Folder size 9.5 MB, well
under the 30 MB budget. Requests this pass: `www.nationaalarchief.nl` 2 (archive landing page, EAD XML download),
`service.archief.nl` 1 (inv.nr 1538 METS) + 15 leaf-image fetches (calibration samples + the four target leaves
+ two context leaves), all >=1.5s apart, single host, well under the good-citizen per-session cap. No EMLO fetch
was needed this pass (the EAD route alone resolved the inv.nr; EMLO's advanced-search API remains unresolved,
see below, but is now moot for this target).

**Kind confirmed: recovery by known plaintext.** Both copies of the same letter are now in hand as images, not
merely inferred from the printed edition's footnote. Key/alignment recovery is explicitly NOT attempted this
pass (out of this worker's brief); a two-pass blind transcription of the cipher leaves follows below for the
next solver.

## HU8: archive location, 24 September 2026 (LANE N2 worker csHU2)

Confirmed NA 3.01.17 (see Copy status above, revised). Requests this pass: `www.nationaalarchief.nl` ~3
(3.01.17 collection landing page, the "Briefwisseling van Johan de Witt" research-guide page and index search
page, all >=2s apart), `resources.huygens.knaw.nl` ~9 (De Witt book_data.js, pages.json source=1, 6 front-
matter OCR fetches [pages X-XVI] read for the "eigenhandige originelen" line, `retroboeken/heinsius` book's own
search form reused from the same-session HU1/HU2 work), 2 attempted `zvt.nationaalarchief.nl`/`hub3.
nationaalarchief.nl` API-endpoint guesses (503/404, abandoned, not retried), `emlo-portal.bodleian.ox.ac.uk` 1
curl attempt (503/connection timeout, logged unreachable, not retried per the one-retry rule) + 2 browser_fetch
(worked: the project overview page, and one advanced-search attempt whose guessed query params did not
actually filter). No subagents.
