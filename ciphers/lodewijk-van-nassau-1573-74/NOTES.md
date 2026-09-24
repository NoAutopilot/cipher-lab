open

# Lodewijk (Louis) van Nassau to Willem van Oranje, four cipher letters, 1573-1574

QUEUE row: NB1 (`QUEUE.md`, "Dutch and Belgian archives (LANE N scout of 24 September 2026)").

## Source

Four letters from Lodewijk van Nassau (Louis of Nassau, 1538-1574, younger brother of William of Orange) to
his brother, identified by secretary's hand and seal (Lodewijk did not sign), all "hoofdzakelijk in
cijferschrift" (mainly in cipher), no solution recorded in the WVO database:

| briefnr | date | place | WVO record |
|---|---|---|---|
| 4610 | 3 June 1573 | -- ("Pour Hollande", duplicaat) | https://resources.huygens.knaw.nl/wvo/app/brief?nr=4610 |
| 4611 | 2 July 1573 | -- | https://resources.huygens.knaw.nl/wvo/app/brief?nr=4611 |
| 4612 | 6 March 1574 | Meer | https://resources.huygens.knaw.nl/wvo/app/brief?nr=4612 |
| 4616 | 12 April 1574 | Weeze | https://resources.huygens.knaw.nl/wvo/app/brief?nr=4616 |

All four: Koninklijk Huisarchief Den Haag, A 11/XIV D/13a; free PDF, no login
(`resources.huygens.knaw.nl/media/wvo/images/04000-04999/0461{0,1,2,6}.pdf`). 4616 (12 Apr 1574, "Weeze",
en route toward Mook) is two days before Lodewijk was killed at the Battle of Mookerheyde (14 Apr 1574) --
plausibly his last surviving letter; QUEUE row NB6 (Jan van Nassau's report of the accident, 17 Apr 1574,
briefnr 5551) is a separate, much shorter item on the same event, not pursued by this brief.

Two further letters in the **same shelfmark and correspondence run**, dated in between (25 March and 7 April
1574), carry a **contemporary decipherment, imaged on the leaf**:

| briefnr | date | WVO record |
|---|---|---|
| 4613 | 25 March 1574 | https://resources.huygens.knaw.nl/wvo/app/brief?nr=4613 |
| 4615 | 7 April 1574 | https://resources.huygens.knaw.nl/wvo/app/brief?nr=4615 |

WVO's Opmerkingen field for both: "Tevens aanwezig de oplossing daarvan, die ook is afgebeeld" (the solution is
also present, also depicted). **Confirmed by eye this pass** (`images/04613_p1-1.png`, `images/04613_p2-2.png`):
p.1 is the numeral ciphertext (a mix of French plaintext words and 2-3 digit cipher groups, values up to ~150),
p.2 is a continuous running French plaintext ending with the same date, "25 de Mars l'an 1574" -- a period
decipherment on a separate sheet in the same file, not a transcription made by this worker. This is exactly the
"key beside the letter" / sibling pattern (LESSONS.md §2): if 4613/4615's key (i.e. the figure-to-letter
mapping recoverable by aligning ciphertext to the imaged plaintext) also covers 4610/4611/4612/4616 -- plausible
since Lodewijk's correspondence with his brother in this narrow eight-month window is likely to share one
cipher -- this is a recovery-by-alignment target, not a cryptanalysis-from-scratch one. **Nobody has yet
attempted that alignment**; this pass only confirms the material exists and is reachable, per the brief.

Three further letters *to* Lodewijk/Jan/Hendrik van Nassau from the same 1574 exchange (briefnrs 7205, 7206,
7208, held at the Algemeen Rijksarchief van België per the scout's row) also carry a contemporary solution,
per the scout's control (QUEUE.md) -- not fetched or viewed this pass, out of this brief's scope.

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents), per `.claude/briefs/check-solved.md`.

1. **Editions first.** Groen van Prinsterer, *Archives ou correspondance inédite de la maison d'Orange-Nassau*,
   1re série, tome IV (1572-1574) and tome V (1574-1577), both digitised cleanly by DBNL
   (`dbnl.org/tekst/groe009arch04_01/`, `.../groe009arch05_01/`) and confirmed to print genuine letters from
   this exact correspondent and period (e.g. Lettre CDLXVI, "Le Comte Louis de Nassau au Prince d'Orange...",
   Dec. 1573, `groe009arch04_01_0086.php`, fetched and read: not a cipher letter, not one of our four --
   incipit and date do not match). **This worker did not achieve an exhaustive letter-by-letter search of the
   full table of contents of tomes IV and V for our four specific dates** (3 Jun 1573, 2 Jul 1573, 6 Mar 1574,
   12 Apr 1574): DBNL's tome-level index pages are very long and the fetch/summarisation tool used could not
   reliably enumerate every entry (two independent attempts at the full ToC gave visibly incomplete or
   self-contradictory results, confirmed by cross-checking one entry directly). This is a genuine search gap,
   flagged for a future pass with either a proper HTML parse of the DBNL ToC or an archive.org OCR full-text
   search once the correct tome-IV/V Internet Archive identifiers are pinned down (attempted this pass with a
   phrase from a confirmed DBNL letter; be-api search on all `archivesoucorre*` identifiers returned no match
   for that phrase at all, suggesting either the wrong identifiers or OCR quality issues, not chased further
   within budget).
2. **The WVO database's own curatorial silence is the strongest evidence gathered this pass.** The database
   editors (J.G. Smit and collaborators) cite Groen van Prinsterer precisely, down to page and an "(onv)"
   incomplete-cipher flag, when a print edition of a WVO letter exists (see NB4/`ciphers/la-garde-1577/NOTES.md`
   for a worked example). For the **two solved siblings** 4613 and 4615 -- which do carry a period decipherment
   -- the Bron field cites **only the manuscript**, no print edition; for the four target letters, likewise
   only the manuscript. Since the editors do not use the Bron field to record decipherment status for this
   correspondence circle at all (that is done in the free-text Opmerkingen field instead, and only 4613/4615
   carry the "oplossing... afgebeeld" phrase, not 4610/4611/4612/4616), this is not proof of non-publication,
   but it does confirm that the editors -- working from the same physical archival file -- found no solution
   note for the four target letters where they did for the two siblings in the very same file.
3. **Community lists.** `sources/cryptiana/web/dutch.htm` (the repo's snapshot of Cryptiana's Dutch-cipher
   history page, read in full via `tools/html2text.py`) discusses only the already-known and already
   found-solved 21 Sept 1572 letter (`ciphers/orange-nassau-1572/`) and general Dutch cipher-history material
   (Beaulieu, Marnix van Sint-Aldegonde, d'Alaume, Huygens as codebreakers; later diplomatic ciphers 1615
   onward). No mention of Lodewijk van Nassau's 1573-74 letters. WebSearch (`Groen van Prinsterer Archives
   Orange-Nassau Lodewijk van Nassau 1573 1574 cijfer`, `dbnl Groen Prinsterer Lodewijk van Nassau cijfer`) found
   nothing beyond the DBNL edition pages themselves.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` (1187 rows) grepped for
   nassau/oranje/hessen/saksen/sachsen/"la garde"/lodewijk: zero hits. No DECODE record found for any of the
   four letters or their siblings.
5. **Solver repositories.** Fresh shallow clones this pass (24 Sept 2026):
   `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`. Grepped for
   nassau/oranje/lodewijk/huisarchief/khag/wvo across `.md` and catalogue files. All hits are unrelated items
   (Willem Frederik, Prince of Orange-Nassau, 1772-1843; Lodewijk van Toulon, 1767-1840; a note on "Louis of
   Nassau's levies" as the *content* of a different, French-side dispatch, Claude de Mondoucet to Charles IX,
   which is about Lodewijk, not by him, and already read/printed per Bourdeau's own SOLVED_RANKING.md). Neither
   repository has a target folder or catalogue row for any of these four letters.
6. **General web search.** As item 3.

## Verdict

**Status: open** (all four: 4610, 4611, 4612, 4616). No solution, key, plaintext or documented attempt found in
six sources. **Caveat, per this worker's own gap above:** the standard printed edition (Groen van Prinsterer,
located and confirmed readable) was not exhaustively searched letter-by-letter for these four dates; the
verdict rests on the WVO database's curatorial silence plus the six-source sweep, not on a page-by-page reading
of Groen's tomes IV-V. A future worker should either parse the DBNL table of contents directly (not through a
summarising fetch tool) or pin down the correct Internet Archive OCR identifiers for these tomes and run
`be-api` full-text search on the exact incipits given above (4612: "J'é receu hier vostre lettre du xxime de
febvrier..."; 4616: "Nous sommes cest soer icy arivé aupres de Goch et sommes...").

**Copy status: copy-free.** Free PDF scans confirmed reachable (HTTP 200) and viewed by eye (this pass):
cipher present on 4610 (`images/04610_p1.png`); the sibling 4613's contemporary decipherment confirmed
present and imaged (`images/04613_p2.png`). No REQUEST.md needed.

**Kind: recovery** (via the sibling's imaged decipherment, an alignment problem per LESSONS.md §2 -- key
recovery from 4613/4615, applied to 4610/4611/4612/4616 -- not cryptanalysis from scratch).

**Next step (not this brief's scope):** fetch 4611, 4612, 4616, 4615 and attempt the alignment: recover the
figure-to-letter/word mapping from 4613 and 4615's ciphertext-plaintext pairs, then test it against the four
open letters.

## Image capture, 24 September 2026 (LANE R worker R9)

All six letters (4610, 4611, 4612, 4616 targets; 4613, 4615 siblings) now fetched in full and rendered to PNG
at 150dpi in `images/`, with `images/manifest.json` and `images/inventory.tsv` (per-page content, cipher type,
approx tokens, decipherment location). Confirms by eye: all four targets carry a numeral cipher throughout most
of their body (values up to ~350); both siblings' contemporary decipherments (4613 p2, 4615 p3) are each on a
separate sheet in the same file, not interlinear, and each closes with the same date as its cipher letter's
closing date (25 March 1574 and 7 April 1574 respectively) -- strong confirmation these are the plaintext of
those specific cipher letters, not unrelated enclosures. No alignment attempted (out of this brief's scope, per
the "next step" above). Host: resources.huygens.knaw.nl, 4 requests this pass (>=2s apart), well under the
shared LANE R budget. Folder kept at 25MB (PDFs deleted after rendering; re-fetch pdf_url in manifest.json if
needed) under the 30MB cap.

## R13: target passes (24 September 2026)

Two independent blind Sonnet-subagent passes (never from an existing transcription, per LESSONS.md/CLAUDE.md
Usage item 2 and 3) of the four target letters' line crops (`tools/iiif_lines.py --image`, local PNGs already on
disk, `--distance`/`--prominence` tuned per page after checking the `--debug` overlay -- default autodetected
pitch under-segmented several pages, e.g. 4610 p3 found only 11 of ~34 real lines at default settings). Crop
filenames `<briefnr>_p<page>_L<NN>.jpg` give the canonical line id both passes share. `passA.tsv`/`passB.tsv`
columns: briefnr, page, line, idx, token (idx 1-based within line); clear French words as `=word`; uncertain
tokens carry a trailing `?`; footer/margin-only crops (archive stamp, blank page bottom) are one row,
token `[blank]`. Reconciled with `tools/reconcile_passes.py` via a small unpublished adapter script (line id =
`page_line`, e.g. `p1_L05`, since the tool's long-format header must start with the literal column `line` and
recognises `pos`/`idx` only as `pos`/`position`/`index` -- the committed passA/passB.tsv keep the brief's literal
column order and names; only the reconciler's throwaway input copy is reordered). Its `--crops` line-id-prefix
match does not find the crops (real crop filenames are `<briefnr>_p<page>_L<NN>.jpg`, not `p<page>_L<NN>.jpg`),
so `recon/<briefnr>/disagreements.tsv`'s `crop` column is empty; a reconciler settling a row should look at
`images/<briefnr>_<line-id-with-underscore-for-page>.jpg`, e.g. row `p1_L05` -> `images/4610_p1_L05.jpg` (briefnr
zero-padded to 4 digits as in the actual filenames, e.g. `04610_p1_L05.jpg`).

Do not settle disagreements.tsv from this brief; do not decode; do not classify novelty.

| briefnr | pages | lines | tokens A | tokens B | agreement (aligned cols) |
|---|---|---|---|---|---|
| 4610 | p1-p3 | 109 | 1934 | 1899 | 1558/1981 = 78.6% |
| 4611 | p1-p3 | 94 | 1692 | 1626 | 1201/1755 = 68.4% |

## R12: sibling passes, 24 September 2026 (LANE R worker R12)

Transcription only, per brief (`.claude/briefs/runs/2026-09-24-lane-r-nb1-passes.md`): two blind passes of the
sibling cipher pages (4613 p1, 4615 p1), a careful transcription of each contemporary decipherment sheet (4613
p2, 4615 p3), and exact-as-measured cipher token counts. No alignment, no key, per brief.

**Line crops.** `tools/iiif_lines.py --image images/04613_p1.png --out images --prefix 4613_p1 --debug --distance
30 --prominence 60` and the same for `04615_p1.png` (the script's existing `--image` option already reads a
local file with no network fetch, so no addition was needed). Default `--distance`/`--prominence` under-detected
(13 lines on 4613 p1 against ~26 real manuscript lines); `--distance 30 --prominence 60` gave 32 bands on 4613
p1 and 29 on 4615 p1, checked against `images/4613_p1_lines_debug.jpg` / `4615_p1_lines_debug.jpg` (per LESSONS.md
"check the debug overlay before handing crops to a pass") -- each red centre line falls on a real manuscript
line; a few bands are doubled where a marginal annotation or slanted ascender briefly raised the ink profile,
harmless since crops overlap into their neighbour rather than losing text. Both target letters' body text runs
at a slight upward slant across the page width, which the debug overlay shows the horizontal band cuts tolerate
without clipping (crops carry margin at top/bottom of the pitch).

**Two blind passes.** Two Sonnet subagents (parallel, `general-purpose`), each given only a labelled montage of
the line crops for both sibling pages (`4613_p1_montage.jpg`, `4615_p1_montage.jpg`, built by this worker with a
short PIL script stacking the crops with their L-number label -- not a private copy of iiif_lines.py, just a
read-time convenience so each pass could be given both pages in two Read calls instead of 61), never shown the
other's output, never shown the decipherment sheets. Output format `line briefnr page index token`, clear French
words prefixed `=`, doubtful tokens suffixed `?`, per brief. Written to `passA_sib.tsv` (596 tokens on 4613 p1,
588 on 4615 p1) and `passB_sib.tsv` (527 on 4613 p1, 560 on 4615 p1).

**Reconciliation.** `tools/reconcile_passes.py passA_sib.tsv passB_sib.tsv --out-dir recon_sib --crops images
--keep-plain` (the header `line briefnr page index token` already satisfies the tool's "long" format --
`line` first, `index`/`token` matched by name -- so `briefnr`/`page` ride along as extra, ignored columns; no
tool change needed). **Agreement: 4613 p1 32.5% (207/636 aligned columns), 4615 p1 56.3% (365/648), combined
44.5% (572/1284)** -- see `recon_sib/agreement.tsv` per-line and `recon_sib/disagreements.tsv` per-token. This is
a low agreement rate and this worker reports it as such, not as a settled reading: both subagents independently
flagged the same difficulty (dense, small, tightly packed 1-3 digit numerals; a `/`-joined pair of groups in
several places, read as one token by both but not always the same pair; two roman-numeral-style cipher glyphs
"ii"/"iii" inline; marginal annotations in a different, later hand on several 4613 lines, deliberately excluded
by both passes as instructed). 4613 p1 lines L08-L09 disagree almost completely (10.5%, 4.3% line agreement) --
flagged for whoever reconciles next as the worst two lines on either page, worth a dedicated close look at
`images/4613_p1_L08.jpg` / `_L09.jpg`. Per brief, this worker did not settle disagreements or build a key from
them.

**Decipherment sheets.** `plaintext_4613.txt` and `plaintext_4615.txt`: line-by-line transcription from
`images/04613_p2.png` and `images/04615_p3.png` (cropped/upscaled regions read directly, not a blind pass -- one
careful read each, per brief), abbreviations kept as written (nre, voz, l're), doubtful words and one illegible
struck-through correction marked `[?]` / `[struck: ...]`. Both close with the same place ("Camp de Cartel[z?]")
and date as their cipher letter's own closing line, consistent with R9's capture-stage finding that these are
each letter's own decipherment, not an unrelated enclosure.

**Token counts** (`images/inventory.tsv`, replacing the earlier `~250`/`~450` placeholders): 4613 p1 numeral
groups passA 525 / passB 461, clear words 71/66; 4615 p1 numeral groups passA 514 / passB 492, clear words
74/68. Given the reconciliation agreement above, these two passes are the honest range, not a single exact
count; no third pass was run (out of budget/brief scope) to settle which is closer.

No host requests (images already on disk from R9's capture). No key, no alignment, no novelty wording. Cost:
under the $6 cap (2 Sonnet subagents for the blind passes, no Opus).
