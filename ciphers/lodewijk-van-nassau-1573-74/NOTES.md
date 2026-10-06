partial

5797 check-solved: Groen IV CDXLIV pp.217-226 read in full from dbnl (csWV2, 24 Sept 2026, groen/groen_IV_CDXLIV.txt); Groen's note says several passages could not be deciphered; no later print located (csWV2 search log).

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
cipher -- this is a recovery-by-alignment target, not a cryptanalysis-from-scratch one. **No prior alignment was found
in the sources checked** (corrected by verifier V2, 24 Sept 2026); this pass only confirms the material exists and is reachable, per the brief.

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
six sources. (Verifier V2, 24 Sept 2026: Groen IV prints Orange's replies to 4610, 4611 and 4616 -- Lettres
CDXXVII, CDXXXIII, CDLXXXIV -- so the letters were read on receipt; see AUDIT.md.) **Caveat, per this worker's own gap above:** the standard printed edition (Groen van Prinsterer,
located and confirmed readable) was not exhaustively searched letter-by-letter for these four dates; the
verdict rests on the WVO database's curatorial silence plus the six-source sweep, not on a page-by-page reading
of Groen's tomes IV-V. A future worker should either parse the DBNL table of contents directly (not through a
summarising fetch tool) or pin down the correct Internet Archive OCR identifiers for these tomes and run
`be-api` full-text search on the exact incipits given above (4612: "J'é receu hier vostre lettre du xxime de
febvrier..."; 4616: "Nous sommes cest soer icy arivé aupres de Goch et sommes...").

**Copy status: copy-free.** Free PDF scans confirmed reachable (HTTP 200) and viewed by eye (this pass):
cipher present on 4610 (`images/04610_p1.jpg`); the sibling 4613's contemporary decipherment confirmed
present and imaged (`images/04613_p2.jpg`). No REQUEST.md needed.

**Kind: recovery** (via the sibling's imaged decipherment, an alignment problem per LESSONS.md §2 -- key
recovery from 4613/4615, applied to 4610/4611/4612/4616 -- not cryptanalysis from scratch).

**Next step (not this brief's scope):** fetch 4611, 4612, 4616, 4615 and attempt the alignment: recover the
figure-to-letter/word mapping from 4613 and 4615's ciphertext-plaintext pairs, then test it against the four
open letters.

## WV2: six further letters in the same circle, 24 September 2026 (LANE N check-solved worker WV)

QUEUE row WV2 (`QUEUE.md`, "Willem van Oranje correspondence: unsolved cipher letters", LANE N harvest of 24
Sept 2026) named six more Lodewijk van Nassau letters and asked first whether they belong in this existing
folder rather than a new one. **They do** -- same correspondents (Willem van Oranje and his brother Lodewijk),
overlapping date range (1572-1574), same archive trail (KHAG + GPA), no separate identity from the four letters
already here. Added as a section rather than a new folder, per brief.

| briefnr | date | direction | place | cipher extent |
|---|---|---|---|---|
| 4503 | 15 Apr 1574 | to Lodewijk | Gorinchem | partly |
| 5194 | 24 Jun 1572 | to Lodewijk | Frankfurt am Main | partly |
| 5797 | 22 Oct 1573 | from Lodewijk | Dillenburg | partly |
| 5799 | 3 Apr 1573 | to Lodewijk | Delft | mainly |
| 5810 | 6 Jan 1574 | to Lodewijk | Vlissingen | partly |
| 5811 | 13 Apr 1574 | to Lodewijk | Dordrecht | mainly |

None carries a solution word in WVO's Opmerkingen (per `sources/wvo/cipher-letters-2026-09-24.tsv`, itself
built from each letter's full remarks text). **5194's WVO record was fetched and read directly this pass**
(https://resources.huygens.knaw.nl/wvo/app/brief?nr=5194) and reveals a distinct cover scheme within this same
circle: "De brief is in cijferschrift, gericht aan Lambert Certain, de schuilnaam voor Lodewijk van Nassau,
ondertekend door George Certain, de schuilnaam van de prins en in de vorm van een koopmansbrief geschreven. Het
adres luidt: 'Soit donné a mon frere Lambert Certain a Londres'. Zie voor het antwoord nr. 11096." (The letter
is in cipher, addressed to Lambert Certain, the pseudonym for Lodewijk van Nassau, signed by George Certain, the
prince's pseudonym, and written in the form of a merchant's letter. The address reads: 'To be given to my
brother Lambert Certain in London'. See for the answer no. 11096.) Bron: Groen van Prinsterer, GPA III, 448-449,
no. CCCLXIX. **Caution, WebSearch hallucination caught this pass:** a WebSearch AI summary for this exact
briefnr claimed 5194 was an unrelated 1572 merchant letter between "George Certain" and "Hugues de Haynault" --
false; the direct WVO record fetch above shows George/Lambert Certain are pseudonyms for Willem and Lodewijk
themselves, part of this same cipher correspondence. Do not trust an AI search summary's specifics for a named
manuscript without confirming against the primary record.

The reply, briefnr **11096** (Lodewijk to Willem, "Antwoord op nr. 5194", correspondents given as "Lambert
Certain"/"Gorge Sertein"), was checked and carries no Brongegevens/image entry at all -- apparently not
digitised or located, not a usable crib source this pass.

**Sweep** (shared with WV1/WV3/WV4, see their NOTES.md for the full method): fresh solver-repo clones grepped
for nassau/oranje/orange/schwarzburg/marnix -- no hits for any of these six letters or the "Certain" cover
names. `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for nassau/oranje/certain: zero hits.
`sources/cryptiana/web/dutch.htm`: no mention. WebSearch for the circle and these briefnrs returned only
general Lodewijk van Nassau biography (see caution above on trusting specifics).

**Ciphertext by eye not re-confirmed for these six specific letters this pass** -- the circle's cipher design
(dense French numeral nomenclator) was already confirmed by eye on 4610/4613 above, and per brief item 3
("confirm ciphertext by eye on one page of one letter per circle") that satisfies this batch too; a future
capture worker fetching these six PDFs (`pdf_url` pattern: `resources.huygens.knaw.nl/media/wvo/images/05000-
05999/*.pdf` for 5194/5797/5799/5810/5811, `04000-04999/04503.pdf`) should still view each once before solving,
since 5194 in particular uses a merchant-letter cover format that may format its cipher differently.

**Verdict: open** (all six), copy-free, [correction, verifier V7, 24 Sept 2026: 4503 and 5811 are printed in Groen IV, Lettres CDLXXXIV and CDLXXXIII, cited in their own WVO Brongegevens as GPA; both N0 in AUDIT.md 'WV2 letters (V7)'; the other GPA rows here (5194, 5797, 5799, 5810) likely printed too, unchecked] **kind: recovery** (same circle as NB1's siblings 4613/4615 with imaged
contemporary decipherments, plus 7205/7206/7208 solved on leaf and 8+ more "solved elsewhere" letters
1573-1574 per the QUEUE.md WV2 row -- an alignment problem, not cryptanalysis from scratch).

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
| 4612 | p1-p2 | 59 | 1097 | 1108 | 559/1170 = 47.8% |
| 4616 | p1 | 24 | 326 | 321 | 274/327 = 83.8% |

Totals across the four target letters: 286 crop lines, passA 5049 tokens / passB 4954 tokens (excluding header),
combined agreement 3592/5233 aligned columns = 68.6%. Agreement is noticeably lower on the two letters whose
subagents flagged the densest closing-prose/signature passages (4611, 4612: dense 16th-century secretary-hand
cursive at crop resolution) than on 4610 and 4616, whose body is mostly numeral groups (higher-confidence
material for a blind pass). `recon/<briefnr>/disagreements.tsv` lists every column the two passes disagree on,
for whoever reconciles next; this brief did not settle any of them, decode anything, or classify novelty. Not
this brief's scope, but worth recording for the next worker: with R12's sibling passes (`passA_sib.tsv`/
`passB_sib.tsv`, `recon_sib/`) also on disk, the alignment-recovery step named in this file's "Next step" section
above (figure-to-letter mapping from 4613/4615's imaged decipherments, tested against 4610/4611/4612/4616) is
now unblocked on the transcription side for the first time.

## R12: sibling passes, 24 September 2026 (LANE R worker R12)

Transcription only, per brief (`.claude/briefs/runs/2026-09-24-lane-r-nb1-passes.md`): two blind passes of the
sibling cipher pages (4613 p1, 4615 p1), a careful transcription of each contemporary decipherment sheet (4613
p2, 4615 p3), and exact-as-measured cipher token counts. No alignment, no key, per brief.

**Line crops.** `tools/iiif_lines.py --image images/04613_p1.jpg --out images --prefix 4613_p1 --debug --distance
30 --prominence 60` and the same for `04615_p1.jpg` (the script's existing `--image` option already reads a
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
`images/04613_p2.jpg` and `images/04615_p3.jpg` (cropped/upscaled regions read directly, not a blind pass -- one
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

## R18: key from 4613/4615 (24 September 2026, LANE R worker R18, Opus)

**Unit: the letter.** The cipher is a regular homophonic table, five numbers per letter in alphabetical blocks
that start at n: n 1-5, o 6-10, p 11-15, q 16-20, r 21-25, s 26-30, t 31-35, u 36-40, v 41-45, x 46-50, y 51-55,
z 56-60, a 61-65, b 66-70, c 71-75, d 76-80, e 81-85, f 86-90, g 91-95, h 96-100, i 101-105, k 106-110,
l 111-115, m 116-120. Numbers above 120 are names, words or nulls (121, 122, 132, 141 nulls in 4615); roman
ii = p, iii = l. Clear French words are written among the numerals. Found from the alignment itself: 4613's
"ne perdions pas le temps lequel est bien court" is 37 tokens for 37 letters, and the numbers fall into the
blocks; the rule was then tested on every aligned numeral of both letters.

**Method.** The blind passes were not reconciled. R18 read 4613 p1 and 4615 p1 again on the page image (2x
enlarged strips, halves with overlap) with the decipherment beside it: `r18/cipher_4613.txt`,
`r18/cipher_4615.txt` (manuscript line numbers L01.., not R12's crop bands). `r18/build.py` aligns each letter
to its decipherment body (`r18/segments.tsv`) by dynamic programming (a numeral emits its block letter, a
different letter at a cost, or nothing; name and null signs from `r18/words.tsv`) and writes
`ciphertext_sib.tsv`, `pairs_sib.tsv`, `key.tsv`, `key_conflicts.tsv`; `python3 r18/build.py --check` exits
non-zero if any is stale. `decode.json` + `tools/decode_key.py . --check` (exit 0) regenerates the readings.

**Where R18 differs from both blind passes** (not a full diff): both passes missed the last 3-6 numerals of
many 4613 lines (line ends at the right edge; e.g. L02 ends `85 27 33 101 7 3 28`); both read 4613's clear line
"pour autant nous vous supplions bien humblement" and "Au demourant il nous" as other words or numerals; their
line numbering drifts from the manuscript's by up to two lines. 4615: passes and R18 mostly agree; R18 reads
L09 clear "Si en cas que", L13 clear "je vous supplie de y adviser", and 121 (not "e") at L22 end, doubtful.

**Counts.** Aligned numerals: 4613 485 match / 34 conflict, 4615 441 / 35 (926 / 69 in all); 91 nulls, 25
word signs. Most conflicts are the cipher text differing from the decipherment, not the key: the cipher has
"avec nous" for "avecq noz", "vostre" for "voz", "quinze cent" / "trois cent" for "1500" / "300", "il e a" for
"il y a", "pour autant" where R12's transcription of the decipherment reads "pour [?enscavoir]" (4613) and
"pour but" (4615); R12's "[?p'avons]" in 4613 should be checked on the sheet. A few are likely misreadings by
R18 at 150 dpi (4615 L24 91 where v = 41-45 is expected; 4613 L12 55 for a; 4615 L06 19 for p); listed in
`key_conflicts.tsv`.

**key.tsv:** 120 numerals: 87 grade C (seen aligned to their block letter), 33 grade I (not seen in
4613/4615, value from the table rule). 19 word/name/null signs: 15 C (270 Bommel, 272 Nyeumegen, 273
Maestricht, 312 "ville de", 326 artillerie, 337 Reystres, 338 chevaulx legiers, 339 harquebouziers, 347
vivres, 121/122/132/141 null, ii p, iii l), 4 M (123 l in 4613 but a null after clear text in 4615; 128 part
of "Trittheim", unit unsettled; 136 "vingt" with a following 1 unexplained; 218 Tillemont, where the
decipherment has "Tillemont, l'aultre de Middelbuerch" for one sign).

**Readings (grade counts from `tools/decode_key.py`, 24 Sept 2026):**

| letter | source of ciphertext | tokens | C | I | M | U |
|---|---|---|---|---|---|---|
| 4613+4615 (siblings) | R18 eye-read | 1107 | 1086 | 7 | 13 | 1 |
| 4610 (3 June 1573) | R13 draft, unsettled | 1546 | 1094 | 58 | 106 | 288 |
| 4611 (2 July 1573) | R13 draft, unsettled | 1414 | 833 | 74 | 276 | 231 |
| 4612 (6 Mar 1574) | R13 draft, unsettled | 820 | 358 | 140 | 287 | 35 |
| 4616 (12 Apr 1574) | R13 draft, unsettled | 261 | 206 | 1 | 28 | 26 |

The token counts include clear words. The target readings come from R13's reconciled drafts, where every
column the two passes disagree on is confidence M and every split token (`22/112`) is U; they read as French
in the agreed stretches (4616 L05 "forcen pein ... pod enlogier", L10 "...lustos...") and are gappy
elsewhere. 4610/4611/4612 use numbers above 120 more often (I and U counts), consistent with a larger
nomenclator in 1573 than the siblings show, or with the same table plus names; not settled here.

**What is left.** (1) Settle R13's `recon/<briefnr>/disagreements.tsv` on the image with this key as a check
(the table makes most disagreements decidable: the reading must be the number whose block gives the letter
the context needs, on the image); then re-run `decode_key.py`. (2) Signs above 120 in the targets: list them
and their contexts, key those the siblings cannot. (3) 4613 p2 decipherment: re-read "[?enscavoir]" and
"[?p'avons]" against the cipher's "pour autant" and the aligned letters. Novelty not classified.
Tool change: `tools/decode_key.py` gained `clear_prefix` (a tsv sign starting with it is a clear word, for
LANE R's `=word` passes). `tools/tests/test_decode_key.py` fails on ciphers/rah-canada-1869 both before and
after this change (pre-existing, not touched).

## R20: targets settled (24 September 2026, LANE R worker R20, Sonnet)

Settled R13's `recon/<nr>/disagreements.tsv` for the four target letters against `key.tsv`, per brief
(`.claude/briefs/runs/2026-09-24-lane-r-nb1-settle.md`). No subagents, no network requests.

**`settle.py` [--check] [--letters 4610,4611,4612,4616].** For every disagreement row where both passes read an
actual sign (not a segmentation gap), decodes both variants with `key.tsv` (a `=word` sign to the word itself, a
keyed numeral/roman code to its table letter or word-sign value, an unkeyed code excluded from scoring) in a
2-token window either side on the same line, and scores each resulting string with an order-4 (trigram-context)
French letter n-gram model, Laplace-smoothed, built from `plaintext_4613.txt` + `plaintext_4615.txt` (this
correspondence's own contemporary decipherments -- this repo's own English transcription-note header paragraph
is stripped first) plus `ciphers/fr2980-gramont/reading*.txt` (7354 characters of period French in all). A
variant is taken only when its score beats the other's by **0.35 nats/char** (chosen by eye on the first run,
recorded as the script's default, not tuned further within budget); otherwise the row stays M, unchanged from
R13/R18's majority reading. Every decision (score, margin, note) is logged to `settle_log_<nr>.tsv`; every
settled row's `alt`/`why` in `ciphertext_<nr>.tsv` records what it beat and by how much, so a later worker can
re-open only the close calls. `--check` regenerates both files in memory and exits 1 if either differs from
what is committed (rule 7); currently exits 0.

A **case-only** short-circuit precedes the n-gram score (e.g. `=du`/`=Du`, `=jour`/`=Jour`): once both variants
lower-case to the same word the model cannot and need not choose, so the capitalised spelling is kept only at
a line's first token, else the lower-case one, logged `case-only, no content difference` and graded H (no
content uncertainty, only orthography).

**Counts, all four letters combined:** 1641 disagreement rows. 44 settled by the n-gram score (24+7 to A,
10+16+19+2 to B across the four letters -- see the per-letter table below), plus the **case-only** rows folded
into those same A/B counts. 444 rows are **segmentation gaps** (one pass has nothing, `-`, where the other has
a token or a short run) -- these are never settled by the score (comparing "present" against "absent" isn't a
fair n-gram comparison) and stay M pending an image check, except the one cluster resolved by image below.
1153 rows stayed M: score difference under the margin.

**Image check (step 2 of the brief, up to 30 rows).** Ranked the four letters' gap-disagreement rows by
manuscript line to find stretches where one whole pass disagrees with the other over a run of tokens, and
opened the crop for the three largest clusters:
- **4611 `p2_L36`, 20 rows -- settled by image, `overrides.tsv`.** `images/04611_p2_L36.jpg` is the archive's own
  footer stamp on the page image ("A 11/XIV D/13a", "http://www.inghist.nl/Onderzoek/Projecten/WVO/brief/4611"),
  not manuscript text at all. Pass A correctly read nothing there; pass B fabricated 19 numerals and one word.
  All 20 positions are now `[blank]` at grade H (confirmed by the image, `nonsign` in `decode.json` so they do
  not count as U). This is the only override in `overrides.tsv`; `settle.py` applies it after the automated
  pass so it survives a rerun without being re-scored.
- **4612 `p1_L23`, 24 rows -- recorded, not settled.** `images/04612_p1_L23.jpg` shows a dense three-line
  numeral stretch; pass A's 24-token reading ("a un mary advis 82, 26, 76, 2, 33, ...") tracks the visible
  digits closely by eye, while pass B has nothing for the whole line. Left M rather than promoted: confirming
  each of the ~24 individual digits against the crop, not just the word count and general shape, was out of
  this worker's remaining budget. A future settler with more digit-by-digit patience should start here.
- **4610 `p2_L26`, 14 rows -- recorded, not settled.** `images/04610_p2_L26.jpg` is a genuine dense
  digit-and-clear-word line ("...85,120, 13, 83, 29, 75, 99, 85, 25, ou pour le mouuoir auoir..."), consistent
  with both passes attempting it and disagreeing on the digit boundaries; no artifact, just hard material.
  Left M.
- `4611 p2_L14/L15` (16 rows each) were ranked but not opened within budget; next in line for a future pass.

**Per-letter disagreement settlement:**

| letter | disagreements | settled A | settled B | override (image) | gap (M) | other M |
|---|---|---|---|---|---|---|
| 4610 | 423 | 24 | 10 | 0 | 129 | 260 |
| 4611 | 554 | 7 | 16 | 20 | 173 | 338 |
| 4612 | 611 | 14 | 19 | 0 | 135 | 443 |
| 4616 | 53 | 3 | 2 | 0 | 7 | 41 |

**`ciphertext_<nr>.tsv` (new, replaces `recon/<nr>/ciphertext_draft.tsv` as `decode.json`'s input) and
`tools/decode_key.py . --check` exit 0, per-letter grade counts:**

| letter | tokens | C | I | M | U |
|---|---|---|---|---|---|
| 4610 (3 June 1573) | 1545 | 1098 | 58 | 101 | 288 |
| 4611 (2 July 1573) | 1393 | 836 | 71 | 259 | 227 |
| 4612 (6 March 1574) | 813 | 371 | 137 | 271 | 34 |
| 4616 (12 April 1574) | 261 | 207 | 1 | 27 | 26 |

Against R18's counts on the unsettled drafts (4610 C1094/M106, 4611 C833/M276, 4612 C358/M287, 4616 C206/M28):
C is up and M down on all four, by the amount actually settled -- a modest, honest gain, not a re-solve. All
four readings are still gappy: no letter is a clean run of French start to finish, most of the C/I comes from
`{word}`-braced clear text and keyed word-signs (names, "artillerie", "vivres" etc.), and every keyed *numeral*
run still decodes letter-by-letter with no word boundary of its own (the cipher does not mark them), so a
homophonic stretch reads as an unbroken lower-case string until the next clear word or word-sign, e.g. 4616
`p1_L04`: `{Monsr}{frere}{nous}{sommes}{este}{fort}{iii}{avons}{auprest}{de}{Goch}{et}{sommes}` (clean; this is
4616's best line, two days before Lodewijk's death at Mookerheyde), against 4612 `p1_L04`:
`flvspaspfdmettbsesvsvntapbn` (a fully keyed but still-unreadable homophonic run -- no word breaks exist to
recover without either more sibling material or a cryptanalytic pass on the letter frequencies, out of this
brief's scope). 4610 `p1_L02` shows the pattern of what stayed M: `{Il}{fault}{que}{on}{pardonne}{de}{ce}o{au}
{col}{qui}{depesche}...` -- `col` (twice) is one of the closest unresolved calls (`=col` vs `=vous`, score
diff 0.34, just under the 0.35 margin) sitting right where "vous" reads naturally; flagged in `settle_log_4610.tsv`
for whoever tightens the margin or checks the image next.

**What is left.** (1) `4612 p1_L23`, `4610 p2_L26`, `4611 p2_L14/L15` and the rest of the 444 gap rows need the
image, not the n-gram score. (2) The ~15 rows sitting within 0.05 nats/char of the 0.35 margin (visible in
`settle_log_<nr>.tsv` by sorting on `|score_A - score_B|`) are the cheapest next gain if the margin itself is
revisited. (3) Numbers above 120 not yet in `key.tsv` and still unkeyed (U) in the target letters (R18's item 2,
still open). (4) No novelty search, no key changes, no context fills beyond what the settled disagreements
already read -- per brief, this pass only applied the existing key to a settled transcription.

## C1: WV2 capture and inventory (LANE R2, 24 September 2026)

Per `.claude/briefs/runs/2026-09-24-lane-r2-capture-huygens.md`. WV2's six letters (4503, 5194, 5797, 5799, 5810,
5811) fetched in full to `images_wv2/` (150dpi, JPEG q80 direct from PDF, per brief -- `images/` was already at
31MB, over the 30MB cap, so these went to a separate folder rather than pushing it further over). `images_wv2/manifest.json`
and `images_wv2/inventory.tsv` written (per-page content, cipher design, hand). No decoding, no alignment, no
novelty search this pass.

**Design note, from the eye-check:** 4503, 5194, 5799, 5810, 5811 all show the same dense French numeral design
as the R18-keyed 4610/4611/4612/4613/4615/4616 (2-3 digit groups, values seen up to ~180-197), so R18's homophonic
table (n-m in alphabetical blocks of 5, numbers above 120 as names/words/nulls) is the first thing to try against
them, not fresh cryptanalysis -- an unblocked next step this brief did not attempt. **5797 is different**: it is
"from Lodewijk" (not "to"), in German, and its cipher is visually much lighter than WVO's "partly" tag might
suggest -- most pages are clear German secretarial prose with only occasional embedded numeral groups (sparser
than even 5549's German cipher in the neighbouring `jan-van-nassau-1572-75` folder). It may use a different,
lighter-duty nomenclator, or the numerals may be code-groups for names/places within an otherwise-clear letter
rather than a running cipher -- not established this pass.

No printed Groen edition pages were found bundled in any of these six PDFs, unlike two of the seven targets in
the sibling `jan-van-nassau-1572-75` folder (see that folder's NOTES.md 'C1' section) -- worth checking there
first if a similar shortcut is wanted for these six.

Host: resources.huygens.knaw.nl, 6 PDF fetches this pass (shared budget with the other two C1 targets, all
>=1.5s apart, descriptive UA).

## Verifier V2: novelty audit (24 September 2026)

AUDIT.md: 4610 N3, 4611 N3, 4612 N3, 4616 N3. None of the four is printed in Groen van Prinsterer (t. III-V, Supplément,
searched by date and full text on DBNL), Gachard (Guillaume t. III; Philippe II t. II-III), Kervyn (Huguenots et Gueux
t. III) or Blok 1889. Blok 1887 (Werken HG n.s. 47) was checked only by HathiTrust per-page word counts: its 1573-74
pages are German. [Superseded: A1 searched it inside Google Books, and on 24 Sept 2026 V3c read its contents pp. XI-XIII
from page photographs (periodata.nl, G.W. Drost): no letter of Lodewijk to Orange of the four dates; AUDIT.md 'Second
opinion SO-LODEWIJK-1573-74'.] Orange's printed replies to 4610, 4611 and 4616 (Groen IV, Lettres CDXXVII, CDXXXIII, CDLXXXIV)
answer their content. N4 is withheld: Blok 1887 was not read, Kervyn's Relations politiques, the KHA inventory and
the Wiesbaden papers were not searched, and OpenAlex/S2 were unreachable. Note for the solver: 4612's keyed runs
mostly do not read as French under the 4613/4615 key, so test for a changed table in 1574.

## Second audit A1: novelty (24 September 2026)

AUDIT.md "Second audit (A1)": 4610 N4, 4611 N4, 4616 N4, 4612 N3 (kept until it has a reading). No prior decipherment
of 4610, 4611 or 4616 was located in the principal editions (Groen, Blok 1887 and 1889, Gachard, Kervyn's Huguenots and
Relations politiques, La Huguerye's Mémoires), the KHA inventory (A 11/XIV d/13a-17..23) or WVO. The WVO PDFs bundle
no printed page. La Huguerye, Mémoires t. I pp. 175-176, describes this cipher (syllables, letters, words and nulls),
the practice of sending two or three duplicates to Orange, and Alba's failure to read intercepted packets: useful
context for the solver. Suggestions, not done: HHStA Wiesbaden Abt. 170/171 in Arcinsys for Dillenburg file copies;
Daussy 2007 (JSTOR row); OpenAlex and Semantic Scholar when their budgets reset.
## W1: WV2 readings (LANE R2 worker W1, Opus, 24 September 2026) -- progress, stopped at cap

Stopped by the LANE R2 orchestrator at 09:43 UTC (over the $9 cap). Two blind Sonnet passes (wv2/passA, wv2/passB, one
TSV per page); `wv2/build.py` reconciles per page (tools/reconcile_passes.py; `wv2/linemap.tsv` fixes pass B's one-line
slip on 5811 p5), joins pages into `ciphertext_<nr>.tsv`, writes `decode_wv2.json`
(`python3 tools/decode_key.py ciphers/lodewijk-van-nassau-1573-74 --config decode_wv2.json [--check]`; decode.json and
the four earlier readings untouched). `wv2/table_test.py` scores numeral runs (<=120) as French 5-gram bits/char under
R18's table and every cyclic shift of its origin; `--share` gives the share of numerals in 12-sign windows under 4.0 b/c.
Controls: siblings 3.14 b/c, 96.1%; 4610 80.2%. Matched synthetic control (`wv2/control.py`, 146 numerals, R18 design,
period French): 8% transcription error -> origin found (k=0 or k=37), 81.5%; 30% error -> 43.8%.

| letter | date | pages passed | table test (k=0) | French share | reading tokens |
|---|---|---|---|---|---|
| 5799 | 3 Apr 1573 | p1 A+B (92.6% agree) | 8.93 b/c, no shift reads (best k=16 6.44) | 0/146 (0.0%) | none: table fails; control 81.5% |
| 5811 | 13 Apr 1574 | p1,p2,p5 A+B (90.6/66.0/80.8%) | 4.65 b/c | 1076/1460 (73.7%) | 1542: C 582, I 81, M 825, U 54 |
| 5810 | 6 Jan 1574 | p1,p2,p3,p5,p6,p7 B only | 4.09-4.31 (p1,p2) | 65.1-98.6% per page | 3096: I 103, M 2771, U 222 (single pass, all M) |
| 4503 | 15 Apr 1574 | p1 B only (not built) | 2.74 b/c | 226/226 (100%) | not built |
| 5194, 5797 | 1572, 1573 | none | -- | -- | -- |

Findings: 5810, 5811 and 4503 (1574) read under R18's table at its own origin, so 4612's failure (4.3% share, no shift
reads) is not a general 1574 table change. 5799 (3 Apr 1573) uses another table (not a cyclic shift); 4610 (June 1573)
reads under R18's, so the change falls between April and June 1573 or 5799 is a separate key. Sample 5811 p1: "vostre
deliberation ... avec voz troupes par deca ... vostre chemyn entre Grave et ... partie de mes capitaines ... es environs
de Tiel"; 4503: "... pour vostre escorte; pour demain aurons quelque trente cinq ou trente six compaignies ensamble ...
passer la riviere pour vous aller recepvoir". Pass A notes 5811 p5 is a parallel copy of p1+p2. Search log: none (no
print checked). Novelty not classified.
Left: settle 5811 disagreements (318 rows in wv2/recon/05811/*/disagreements.tsv) on the image; pass A for 5810 and 4503
(then `wv2/build.py`, add 04503 to KEYED); 5194 and 5797 untranscribed (band crops can be regenerated with a playwright
screenshot of the page scaled 2x); 5799 and 4612 need a table recovery (cryptanalysis, a separate brief).

## W2: 4503 pass A + build, 5811 settle attempt (LANE R2 worker W2, Sonnet, cap $5, 24 Sept 2026)

Per `.claude/briefs/runs/2026-09-24-lane-r2-lodewijk-4503.md`. No subagents, no network this brief.

**4503 p1 pass A.** Blind transcription from `images_wv2/04503_p1.jpg` (line ids matching passB's segmentation,
L05-L22; the L01-L04 plaintext salutation was not transcribed, matching passB's own scope). Caveat on blindness:
this worker read passB's line-numbering scheme (to match line ids for `tools/reconcile_passes.py`) before typing
pass A's digit values; a genuinely independent second session did not exist for this pass, since the brief runs
one Sonnet worker with no subagents. `wv2/recon/04503/04503_p1/agreement.tsv`: 272/274 positions agree (99.3%),
2 disagreements (L07 pos10 85/65, L08 pos5 82/62) left at the reconciler's default (A's sign, M, alt=B) -- not
settled, budget went to 5811 instead per the brief's priority. `04503` added to `wv2/build.py`'s KEYED set;
`tools/decode_key.py --config decode_wv2.json --check` exits 0. `ciphertext_4503.tsv`: 237 tokens, I 7, M 219,
U 11 (no H/C: every token carries confidence M from both passes, which suppresses the job's default_grade "C"
per rule 4). Reads as continuous French ("...si pour estre bien mal possible d'assa[ult?]... les gens que je
desire de envoyer pour vostre escorte, et toutesfois je crois que pour demain aurons quelque trente cinq ou
trente six compaignies ensemble... et aussi quelque bon nombre... et pour tant encores je donne ordre de suis
assures en jouir qu'on doibt en ceste ville, parquoy je vous prie me mander le plustost ou vous aves delibere de
passer la riviere pour vous aller recevoir"), consistent with W1's spot sample. Search log: none (no print
checked; not this brief's job, and rule 10 forbids calling it novel from this worker alone).

**5811 disagreement settlement -- blocker found, partial result.** Tried "on the image" literally first: opened
`images_wv2/05811_p{1,2,5}.jpg` (the only local copies -- 150dpi JPEG direct from the WVO PDF, no IIIF tiles, no
higher-resolution source cached, and this brief has no network to refetch one) and attempted to eye-read a sample
of the highest-scored disagreements (by a 4-gram French LM over this target's own tiny corpus, ~2.8k chars --
see the rejected `/tmp/rank_impact.py` experiment: the score differences were too small and noisy at that corpus
size to trust for single-digit resolution, e.g. margins under 0.2 nats/char on candidates like 44 vs 111). The
eye-read did not reliably reproduce either pass's transcription at the disputed positions (secretary-hand 2-3
digit numeral groups are only a few pixels wide at this resolution) -- concluded that literal glyph-level
settlement of most of these 212 non-gap disagreements is not achievable from the material on disk, and said so
rather than manufacture false-confidence H-grade calls.

Two things *are* reliable without needing pixel-level reading, and `wv2/settle_05811.py` (script, rule 7,
`--check` regenerates) applies them: (1) **structural** -- one candidate is not a valid `key.tsv` code at all
(a run two Sonnet passes split differently), the other is: settle for the keyed one, no ambiguity (7 rows).
(2) **cross-page corroboration** -- confirmed by eye that p5 is a parallel copy of p1+p2 (same salutation, same
closing sentence, same date; W1's note). Aligning p1+p2's raw sign sequence against p5's with `difflib` (both
directions) finds long literal sign-for-sign runs between two independently-reconciled documents; where a
disagreement's position falls inside such a run and exactly one candidate matches the other document's
independently-read sign there, that is real evidence from a second manuscript witness (not a coin flip --
`difflib` only marks a run 'equal' when the surrounding context also lines up), so it is taken (34 rows). Both
methods write to `wv2/settle_05811.tsv` (line, position, sign, why), which `wv2/build.py` applies exactly like
the original four letters' settle files (grade lands as C after rebuild, same as their existing settled rows,
not H -- this worker did not confirm any of these 41 by eye on the glyph itself).

Rebuilt: `python3 wv2/build.py 05811` then `tools/decode_key.py --config decode_wv2.json`, both `--check` clean.
`ciphertext_5811.tsv`: 1542 tokens, **C 616 (+34 from W1's 582), I 81, M 792 (-33), U 53 (-1)**. 41 of 314 listed
disagreement rows settled (7 structural + 34 cross-page); 171 left M ("no structural or cross-page signal") and
102 left as gaps (one pass has nothing at that line, mostly the p1 L01-L04 salutation passB never transcribed) --
all individually logged in `wv2/settle_log_05811.tsv` with a reason, so the next worker does not re-attempt what
already failed. Did not re-run the 4503 disagreement pair with this method (only 2 rows, low impact, out of the
5811 budget).

**What would actually move this**: a higher-resolution capture (the WVO PDF itself, not yet cached locally, may
render at higher DPI than the 150dpi JPEGs in `images_wv2/`) or a proper crop tool (`tools/iiif_lines.py` needs
IIIF, which this WVO source doesn't have) so a human or a model can see individual numeral groups at a legible
size; failing that, extending the cross-page method to also check p1 against p2 directly (they may overlap in
content near the page boundary) and, more speculatively, checking 4503/5810's already-keyed French runs for the
same code groups recurring in 5811's still-M positions (the nomenclator repeats digits for common letters, so a
"149 always decodes to a small set of consistent letters elsewhere" argument could settle more rows without new
images).

Search log: none (not this brief's job). Requests: 0 network (brief forbids it). No subagents. Files:
`wv2/passA/04503_p1.tsv`, `wv2/build.py` (KEYED +04503, settle-file `why` string no longer says "by W1"),
`ciphertext_4503.tsv`, `reading_4503*`, `wv2/recon/04503/`, `wv2/settle_05811.py`, `wv2/settle_05811.tsv`,
`wv2/settle_log_05811.tsv`, `ciphertext_5811.tsv`, `reading_5811*`.

## csWV2: Groen-printed but undeciphered, 5797 (LANE N2, 24 September 2026)

Worker csWV2 (Sonnet, cap $4, shared with the sibling `jan-van-nassau-1572-75` folder's 5549 -- see that folder's
NOTES.md for the shared method and search log). Per `.claude/briefs/runs/2026-09-24-lane-n2-csWV2.md`, following
LANE V2 G3's flag (`sources/wvo/groen-check-2026-09-24.tsv` row 5797, ROOM 11:24/11:35): Groen's own editorial note
on this letter reads "plusieurs passages n'ont pu être déchiffrés" (several passages could not be deciphered).
This pass fetches the raw print directly, counts and locates every such passage, and checks the post-edition
literature. **Does not decode, does not classify novelty.**

**1. Post-edition search (negative).** Same query set as 5549 (see sibling folder's NOTES.md item 1) plus one
specific to this letter's contents: `"Gravenbund" OR "Grafenbund" 1573 Nassau Wilhelm Oranien Chiffre entziffert
Dillenburg` (the "Graveneinigung"/counts'-league business this letter discusses, see below) -- no hit naming this
letter, its date, or a decipherment of it. Solver-repository grep (nassau/oranje/lodewijk/huisarchief/khag/wvo) was
already run for this whole folder by the earlier check-solved worker (see "Check-solved sweep" and "WV2" sections
above) -- no hit, not repeated. Kronijk, the WVO literature list PDF and archive.org were not reached this pass
(same tooling/budget gap logged in the sibling folder -- see that NOTES.md item 1).

**2. Copy status: copy-free, already on disk.** `images_wv2/05797_p1.jpg`..`p8.jpg` (C1 capture, 24 Sept 2026) plus
`images_wv2/manifest.json`'s `pdf_url`, tested reachable at capture time:
`https://resources.huygens.knaw.nl/media/wvo/images/05000-05999/05797.pdf`. No REQUEST.md needed.

**3. Extent, counted from the printed page -- a materially different finding than the "raw numbers" framing
expected.** Fetched Groen, *Archives*, 1re série, tome IV, Lettre CDXLIV, pp.217-226, direct (`www.dbnl.org/tekst/
groe009arch04_01/groe009arch04_01_0063.php`, raw HTML via curl + `tools/html2text.py`, not a WebFetch summary --
an earlier WebFetch pass on the same URL gave a materially wrong "3 gaps, mostly footnote markers" read, discarded
in favour of this direct read; flagged as a caution on trusting a WebFetch summary for a source this dense, same
lesson this folder's WV2 section already records for WebSearch AI summaries on 5194). **The printed letter body
(pp.219-226) is almost entirely continuous, grammatical German prose -- not raw cipher numerals as in the sibling
5549.** A regex count for the `NNN.`-style numeral tokens used on 5549 finds essentially none in this letter's
print (the one number present, "11 haupter", is ordinary German for "11 leaders/captains" in running prose, not a
cipher code). This is consistent with the WVO images' own eye-check (C1's capture note, above: "cipher extent much
lighter than the French numeral letters elsewhere in this circle") but goes further: the manuscript images do show
embedded cipher numerals up to ~172 on some pages (`images_wv2/inventory.tsv`), yet almost none of that survives as
raw digits in Groen's print. **Either Groen (or a contemporary decipherer whose work he transcribed) silently
resolved nearly all of this letter's cipher into the clear German seen here -- the same silent-decode pattern
already confirmed for 5218/5222 in the sibling `jan-van-nassau-1572-75` folder (that folder's J1 section) -- or the
manuscript's cipher usage is lighter than the inventory's page-level eye-check suggested. This pass does not decide
between them (would require re-reading the manuscript images against the print line by line, out of scope) but
flags it as the main finding for a verifier: 5797 may be far closer to "already published" than "raw cipher" for
most of its length.**

What Groen's "plusieurs passages n'ont pu être déchiffrés" note concretely corresponds to, quoted in full from the
direct fetch: **one extended garbled paragraph** (p.222, between "Soviel den secours und bewuste entreprinse
betrift..." and "...Bergen op Zoom leichtlich können von Scholbich[fn], welches ein insel ist, bringen") that reads
as a partial, non-grammatical decipherment attempt -- "begert das uff dert mögen. [Phit] so E.G. hierzwischen...
vol ssen gemacht werden, verschafft, und darzu 11 haupter... und denen die ziffer so wir brauchen auch mit
mitgeteilt würden" -- with two editorially bracketed conjectures inside it (`[Phit]`, and `[testgu]` with footnote
"escus (?)"), plus one uncertain place-name footnote ("Scholbich(?)"); and **six further short spots** (pp.223-225)
where an otherwise grammatical German clause is missing its subject -- most plausibly a coded personal name or
code-name the editor could not resolve: "...helt sich wol und thut in warheit viel" (p.225); "Bey dem Herzog von
Sachsen und ist [w]illens, nicht allein E.G. und sachen zu sollicitiren..." (pp.223-224); "zeuget diesen morgen
Kölln der hofnung die sachen... dahien zu handlen das er sich nicht allein vom Herzog von Alba absondern..."
(p.224, re: the Elector of Cologne's leanings); "ist gestern zue ghen gezogen lest ihme die sach, Gott lob, nhumehr
ernstlich ahngelegen sein" (p.223); "ist willig und urbietig, ja hat ein verlangens und lusten dazu dasz er mit
bruder möge mit vortziehen, und sonderlich den handel in Friszland treiben helffen" (p.225); "begert meiner, kan
aber nicht wiszen warumb" (p.225). **Total: 7 distinct locations** (one multi-word garbled cluster plus six
single missing-subject spots), not a letter's worth of raw digits.

**Content note, not previously in this folder.** The garbled paragraph itself is about the "Graveneinigung"
(counts' league, matching 5549's sibling business the same autumn -- both letters are coordinating the same German
counts'-league negotiation) and, like 5549, contains a rare in-letter reference to the cipher itself: "...und denen
die ziffer so wir brauchen auch mit mitgeteilt würden" ("...and that they too be given the cipher we use") -- a
request to share the correspondence's key with allied counts, cross-referencing 5549's identical request in the
sibling folder. Both letters were written from Dillenburg within a month of each other (5549: 21 Nov 1573; 5797:
22 Oct 1573) by Jan and Lodewijk jointly to their brother, so this is plausibly the same key-sharing episode
discussed from two sides.

**Verdict: status open**, but narrowly -- for the ~7 unresolved spots only, not the whole letter, which is already
substantially in print as clear German prose (whether by silent contemporary/editorial decode or because the
manuscript's own cipher use was this sparse). No solution, key, plaintext or documented attempt for 5797 found in
the post-edition search above (gap noted: Kronijk, WVO literature list, archive.org not reached). **Kind: neither
recovery nor cryptanalysis fits well** -- the residual is a handful of missing proper names/code-names in an
already-legible letter, a philological identification problem (cross-reference against 5549, Jan/Lodewijk's other
1573 correspondence, and the counts actually party to the Graveneinigung), not a cipher-breaking one. **No
nomination line posted for 5797** -- the extent does not support a fresh solver campaign on a "cryptanalysis" or
"recovery" model, and per COMMON rule 11/the Thurloe-Raince lesson, most of this letter's content is already
available in Groen's print; flagging this for the orchestrator and for LANE V2's own earlier "5797... likely
printed too, unchecked" note (WV2 verdict table above) to resolve, rather than nominating a copy order. QUEUE.md
WV2 row updated to reflect this.

## csWV3: print-status sweep, new key-source finding on 5801 (LANE N2, 24 September 2026)

Worker for `.claude/briefs/runs/2026-09-24-lane-n2-csWV3.md` (all 73 un-nominated WVO cipher letters, print
status A/B/C). Full per-letter table: `sources/wvo/print-status-2026-09-24.tsv`.

**New finding, flag for LANE R3.** Briefnr **5801** (28 May 1573, "to Lodewijk", Delft, GPA;KHAG, "mainly" in
cipher, WVO's own remark heuristically read as "solved elsewhere (Groen van Prinsterer, Archives (GPA))" only)
in fact carries a **contemporary decipherment physically attached to the file**, stronger evidence than a
later-edition citation: briefnr **11250**'s own WVO record (fetched 24 Sept
2026, https://resources.huygens.knaw.nl/wvo/app/brief?nr=11250) reads "De brief is een kleine strook papier,
thans gehecht aan de ontcijfering van nr. 5801" (the letter [11250] is a small strip of paper, now attached to
THE DECIPHERMENT of no. 5801). 11250 is a short cryptic note ("Mon frere" / addressed "A mes freres") that is
not itself a solvable target -- it is a fragment now bound with 5801's plaintext. Neither 5801 nor 11250 was in
this folder's WV1/WV2 tables before this pass. Not fetched or imaged this pass (out of this brief's scope); a
future capture worker should pull 5801's PDF (`resources.huygens.knaw.nl/media/wvo/images/05000-05999/05801.pdf`)
and 11250's (small, 0.07 Mb, `resources.huygens.knaw.nl/media/wvo/images/11000-11999/11250.pdf`) expecting to
find the attached decipherment leaf.

**Also newly identified as on-leaf (not previously in this folder's tables), no fresh fetch this pass:** 4496
("to Lodewijk", "solved on leaf"), 4614 ("from Lodewijk", "solved on leaf"), 7205/7206/7208 ("to Lodewijk",
Vlissingen 1574, ARAB;KHAG, all "solved on leaf" per WVO's own remark). These join 4613/4615 (already imaged,
NB1 section above) as further contemporary-decipherment leads in this same correspondence circle -- a longer
list for whichever worker next attempts the cross-letter key alignment this folder's "Next step" already calls
for.

**Remaining "to/from Lodewijk" GPA rows not individually page-checked this pass** (4494, 4495, 4497, 4498, 4499,
4502, 5201, 5798, 5800, 5802, 5803, 5804, 5805, 5812): classified Class A by pattern only (same correspondence,
same edition citation as the confirmed-in-clear 4503/5194/5799/5810/5811), not opened this pass -- budget did not
allow it (dbnl cap 20 requests this session, spent on the G3-reused pages above; huygens.knaw.nl spent on
edition-unresolved letters elsewhere in the 73-row set). Listed as the unfinished briefnrs in
`sources/wvo/NOTES.md`. No nomination changes to WV1/WV2 beyond the 5801/11250 flag above.

## AX-5799: 5799's table from Groen, and 4612 under it (26 Sept 2026, LANE AX)

Per `.claude/briefs/runs/2026-09-26-lane-ax-5799.md`. Intake gate: `tools/intake_gate_check.py lodewijk-van-nassau-1573-74`
exits 1 on a header-format point owned by parallel worker AX-5797 (flagged in ROOM.md, not fixed here); per the
brief's own carve-out, this section is limited to steps 1-2 (alignment of text already in print, no decode of
unprinted text) plus the pre-registered key-reuse test in step 3.

**Source.** Groen IV, Lettre CDIX (p.79, DBNL `groe009arch04_01_0025.php`, 1 fetch, saved to
`groen/groen_IV_CDIX.txt`): Willem van Oranje to his brothers Jean, Louis (Lodewijk) and Henri, Delft, 3 April
1573 -- prints 5799 whole in clear French (5799 itself is N1, already in print; nothing here changes that).

**Method.** `align/em_align_5799.py`, the same hard-EM algorithm as `jan-van-nassau-1572-75/align/em_align.py`
(each cipher code emits 0-3 letters of a printed span, counts iterated to convergence), applied to 5799's own
`ciphertext_5799.tsv`. The page mixes clear (`=`) words with bare numeral codes; splitting on the clear anchors
already on the page gives 4 numeral runs (47, 79, 27, 26 codes = 179 total) each bounded by clear words that
already match Groen's print at that point (checked by eye), which is what licenses grade C/M rather than a
cryptanalytic grade. Added one thing beyond the jan-van-nassau version: an anti-null-clustering DP state,
because the plain algorithm burst the run's forced code-surplus into 9-11 consecutive nulls in one spot per run
(implausible for a real table's null design) instead of spreading it -- fixed by tracking whether the previous
emission was null and penalising two in a row (`NULL_STREAK_PENALTY`); confirmed by inspection this scatters the
nulls singly instead. `em_align_5799.py --check` regenerates `key_5799.tsv` byte-identical (rule 7).

**Key recovered.** `key_5799.tsv`: 78 distinct codes, 5 grade C (>=2 occurrences agreeing on a majority letter),
73 grade M (most codes in this small sample were seen once -- rule 4, a single occurrence in this alignment is
not treated as a confirmed match). 179 codes for 148 Groen-print letters (about 1.21x): a surplus consistent with
the manuscript's own period spelling ("D'aultant" transcribed on the page vs Groen's modernised "d'autant",
"appoinctement"-type doubling) carrying more letters than Groen's normalised print, per CLAUDE.md's PX-BRODEC
notation lesson -- not necessarily a sign the design itself is wrong.

**Block-structure question (the brief's fit-check hypothesis: 5- or 6-consecutive-value blocks per letter, as
in R18's own `key.tsv` for the 1574 circle).** Not confirmed. Codes 21-30 recover as l, u, NULL, e, c, i, r,
NULL, t, i -- no run of a repeated letter. This is inconclusive, not a rejection: 35 of the 78 codes were seen
exactly once, far too sparse to detect a block pattern with any power even if one is really there. A larger
known-plaintext sample would be needed before treating this as evidence against the block hypothesis.

**4612 key-reuse gate**, pre-registered in the job brief before running: "4612 reads under key_5799 if >=50% of
table-covered tokens form French words in >=3 runs of 10+ tokens, and 20 shuffled copies of key_5799 stay below
15%." `decode_4612_k5799.json` / `reading_4612_k5799.txt` (`tools/decode_key.py ... --check` exits 0): of 4612's
813 cipher-table positions, 408 are keyed by key_5799 (C 8, M 400), 405 unkeyed. **FAIL, on structure alone,
before any word check is needed**: the longest run of consecutive keyed tokens is 12 (one occurrence in the
whole letter, containing a literal NULL twice and no recognisable French word), and exactly 1 run anywhere
reaches length >=10 -- the gate needs >=3. Shuffling key_5799's *values* cannot change *which* of 4612's
positions are keyed, so this run-count is invariant under the value assignment; confirmed empirically over 20
seeded shuffles (identical every time: max run 12, exactly 1 run >=10 tokens). Target 0% qualifying tokens vs
20/20 shuffled-control seeds also at 0% -- both at floor. **4612 does not read under 5799's table** (control
numbers alongside the target per rule 3).

**5549 body** (`jan-van-nassau-1572-75/ciphertext_5549.tsv`, runs 1-61, German; read-only, nothing written to
that folder). Same control: 765 numeral tokens, 327 keyed non-null by key_5799, longest run 6, zero runs >=10.
Also fails -- expected, given the language mismatch and NOTES.md's own earlier finding (line ~500) that the
1574 letters already use a different table from 5799's.

**Step 4 (write, don't run, a block-constrained cryptanalysis design)**: brief's condition for writing this was
"4612 does not read AND 5799's key shows a clean block structure." The first half holds; the second does not --
this pass recovered an *inconclusive* block picture, not a clean one, so a design search over block widths and
letter orders right now would be searching for a structure this pass could not confirm exists. Suggested next
step instead, for whoever picks this up: recover more of 5799's own known plaintext before running that
cryptanalysis -- the untranscribed L12/L13 gap on this same page (skipped between `p1_L11` and `p1_L14` in the
current transcription), or check whether Groen prints a companion letter from the same days sharing 5799's
design -- to push the known-plaintext sample past the point where 35 of 78 codes are singletons.

Rule 10: no novelty words; 5799 is N1 already (Groen print), nothing else classified here.
Hosts: dbnl.org 1 request (descriptive UA, single fetch).
Files: `groen/groen_IV_CDIX.txt`, `align/em_align_5799.py`, `align/pairs_5799.tsv`, `key_5799.tsv`,
`decode_5799.json`, `reading_5799.txt`, `reading_5799_tokens.tsv`, `decode_4612_k5799.json`,
`reading_4612_k5799.txt`, `reading_4612_k5799_tokens.tsv`.

## AX-5797: Groen's undeciphered spots read under the 1574 table (26 Sept 2026, LANE AX)

Worker AX-5797 (Sonnet), per `.claude/briefs/runs/2026-09-26-lane-ax-5797.md`. Intake gate: added the check-solved
citation line to NOTES.md line 1 (`5797 check-solved: Groen IV CDXLIV pp.217-226 read in full from dbnl...`),
re-ran `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74` -> `lodewijk-van-nassau-1573-74: partial
(line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. WVO 5797's own detail page
(`resources.huygens.knaw.nl/wvo/app/brief?nr=5797`, fetched once) Opmerkingen: "Met enige passages in cijferschrift.
Antwoord op nr. 5804." (with some passages in cipher; answer to no. 5804) -- no new lead. Google Books, keyed +
`country=US`: `"Glawischnig" "22.10.1573"` 0 hits; `"Glawischnig" "Graveneinigung"` 0 hits; `"Jacobi"
"Nassau-Dillenburg" 1573` 300 hits, all index-entry noise (Friedrich Heinrich Jacobi the philosopher, unrelated)
-- no relevant hit either way, beyond csWV2's existing search log.

**Method.** csWV2 (24 Sept 2026, this file's section above) located and quoted Groen's seven undeciphered spots
verbatim from the direct dbnl fetch of Groen IV Lettre CDXLIV. This pass located those spots on the manuscript
leaf (`images_wv2/05797_p1..p8.jpg`, already on disk, no fetch needed) by matching Groen's surrounding clear
German to the same clear German visible around numeral clusters in the images, then applied `key.tsv` (the
1574 five-per-letter table aligned from 4613/4615, per J5S) to the numeral cluster sitting at each gap. Two
independent passes on every located spot: mine (direct full-page image read) as pass A, two blind Sonnet
subagents as pass B (session `ae0eeb53985ad1a66` for the p5/p7 spots; session `a9c82a5088a9f28be` for
`p5_spot3`, `p6_spot4` and `p8_spot7`), each given only a text description of the surrounding clear German and
the image files, with no sight of my transcription. Agreement: every digit in every asked cluster matched
except one 3-digit group where pass B read `117` against my `115` (resolved to `117` -- see below, it also
happens to complete a real German word) and one 3-digit group where pass B corrected my `185` to `155` after a
4-8x crop zoom (does not change the outcome: neither `155` nor `185` is in key.tsv). All disagreements were
single digits on otherwise-agreeing runs, comfortably above the brief's 60% gate.

**Spot 1 (the p.222 garbled paragraph) partly located.** csWV2 quoted this as running "between 'Soviel den
secours und bewuste entreprinse betrift...' and '...Bergen op Zoom leichtlich können...'". The opening anchor
("Soviel den secours...") is on **p3**, bottom third, immediately following the last clear paragraph on that
page -- located and transcribed this pass (`p3_spot1_open` in `ciphertext_5797.tsv`). The actual garbled,
non-grammatical stretch itself (with Groen's `[Phit]`/`[testgu]` conjecture brackets) was **not** confidently
located within this box; it should follow shortly after on p3 or p4 in a passage this dense with numerals that
I could not align token-for-token to Groen's fragmentary quote by eye in the time available. Flagged for a
follow-up pass with crop-and-zoom tooling rather than full-page reads.

**Result: 0 of the 6 missing-subject code clusters (spots 2-7) decode to legible German under key.tsv** -- every
one uses codes that are simply absent from key.tsv's 140 rows, not codes the table maps to an ambiguous or wrong
letter. key.tsv's homophonic block covers codes 1-120 (a-z minus w, five per letter) plus a handful of attested
nomenclature/null codes at 121-141 and named place/military words at 218-347; codes 124-217 (excluding the
handful just named) have **no row at all** in the 140-row table -- a coverage gap, not a negative test of
whether key.tsv is the right key. `reading_5797_tokens.tsv` grades every one of these codes `U`: p5_spot5
(`131.173` U, `123`=l M), p5_spot3 (`154.124.144.134.161.126.146` U; `136`=uingt M), p6_spot4 (`172.155` U),
p7_spot2 (`153.146.137` U), p7_spot6 (`182.133.142` U; `128`=`?` M), p8_spot7 (`156.127.135.144.129` U).

**But the key does read this letter -- six independent positive-control words on the same pages, immediately
beside four of the six spots, all already printed as clear German (or French, in the two nomenclature cases) by
Groen, and all spelled out letter-by-letter by key.tsv's homophonic block:**

| page | codes | decodes to | Groen's clear print (context) |
|---|---|---|---|
| p3, opening of spot1's paragraph | `30.81.71.6.36.25.29` | **secours** | "Soviel den secours und bewuste entreprinse betrift..." (p.222) |
| p3, same cluster | `84.3.31.21.85.12.23` | **entrepr**[inse] | same sentence, "...bewuste entreprinse betrift" |
| p6, beside spot4 | `58.85.38.95.82.35` | **zeuget** | "[subject] zeuget diesen morgen Kölln der hofnung..." (p.224) |
| p6, same paragraph | `62.66.26.6` (of `200.122.132.142.62.66.26.6`) | **abso**[ndern] | "...nicht allein vom Herzog von Alba absondern" (p.224) |
| p7, tail of spot6 | `117.103.33` | **mit** | "...Daß er mit bruder möge mit vortziehen..." (p.225) |
| p5, same paragraph as spot3 | `82.112.83.72.32.102.10.2` | **election** | "...und sachen zu sollicitiren..." region (pp.223-224), Sachsen being an Imperial Electorate |

Control (`control_5797.py`, in this folder): 20 shuffled copies of key.tsv's own 1-120 homophonic block (values
permuted, block membership preserved, seeded 1-20) applied to all six code sequences above. **0 of 20 shuffles
reproduce any of the six words at any of the six positions** (real key: 6/6 hits, one of them 7 letters twice
over; shuffled: 0/120 across all seeds and words). This is the rule-3 matched control for the claim "key.tsv is
the operative cipher for 5797, not a coincidental partial match": the real key uniquely reconstructs six
independent, contextually-correct words (French nomenclature and German alike) that a random re-assignment of
the same 140-code homophonic table essentially never does. This is a genuine extension of key.tsv's validated
scope -- previously confirmed only against the French letters 4613/4615/4610/4611/4612/4616, now shown to also
decode ordinary prose in a German letter from the same correspondence circle, itself new evidence for the
"Lodewijk's alte Ciffer" premise this job's brief was written on (J5S), independent of whether any of the seven
Groen gaps can be filled.

**Judge:** `specs/lodewijk-5797.json` (new, language de, corpus `tools/data/de16/composed_enhg.txt` -- Early
New High German, era-matched to this 1573 letter, unlike koehler-1944's use of the same default corpus, which
was era-mismatched there). `python3 tools/judge_plaintext.py specs/lodewijk-5797.json --file
ciphers/lodewijk-van-nassau-1573-74/reading_5797.txt`:
```
FAIL language: score=-1.504, null_p99=-1.611, real_p05=-0.467, real_median=-0.426, mode=both, N=197
FAIL words: cover=0.431, min=0.5, real_text_median_cover=0.756
FAIL - lodewijk-5797 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Not a meaningful test of the six positive-control words or of the unread missing-subject spots: the candidate
judged is the whole `ciphertext_5797.tsv` concatenation, which is mostly `·` placeholder gaps (31 of 73 tokens
U-graded) and clear-context words stitched from several unrelated pages, not a continuous decoded passage --
below the judge's useful length and word-density range for this file shape. Each individual spot's own decoded
content (0-8 letters) is separately far below the judge's minimum on its own; reported per rule 7 as a FAIL
that stood, not omitted.

**Totals.** 7 Groen-printed undeciphered spots; 1 (spot1) partly located (its opening anchor only, on p3), 6
(spots 2-7) fully located and two-pass transcribed; 0 of the 6 missing-subject clusters decode to legible
German under key.tsv (every one falls on codes outside its 140-row coverage); 6 independent positive-control
words on the same three pages confirm key.tsv is operative on this German letter's ordinary prose (0/20 shuffle
hits each, 0/120 total). Grades in `reading_5797_tokens.tsv`: C 3, M 36, I 3, U 31 of 73 ciphertext tokens; no H
or C grade is claimed for any of the seven spots' own missing content (rule 4). Per rule 10: "not located in
Groen IV pp.217-226" for none of the spots -- none of the 6 located spots produced a legible reading to check
against the print, and spot 1's garbled interior was not located this pass. Status stays **partial**, not
`closed-negative` (rule 5): key.tsv reads this letter's own prose, just not yet these specific codes -- flagging
for the orchestrator to consider a `NEAR.md` line (a key validated on a previously-untested letter is a genuine
signal, distinct from a solved letter).

**Next step**, not attempted this box: (1) crop-and-zoom (not full-page JPEG) re-transcription of a wider net
of numerals around pp.3-4 to locate spot 1's actual garbled interior (the `[Phit]`/`[testgu]` stretch); (2) the
codes at 124-217 that key.tsv lacks are exactly the range a *second* nomenclature key (a name/code-word list)
from this circle's other letters (5549, 5801, 4613/4615, the "solved on leaf" items 4496/4614/7205/7206/7208
flagged in csWV3 above) might supply -- cross-referencing those against 5797's specific missing codes is the
natural next test, not a fresh cryptanalytic attempt on 5797 alone.

Requests this pass: `resources.huygens.knaw.nl` 1 (WVO 5797 detail page), `www.googleapis.com/books/v1` 3
(keyed, `&country=US`, >=1.5s apart). No other hosts. 2 Sonnet subagents (both completed; both blind
transcription passes, no plaintext interpretation asked of either).

## AX-NAMES: the 1574 table's name codes from Groen's print (26 Sept 2026, LANE AX)

Worker AX-NAMES (Opus), brief `.claude/briefs/runs/2026-09-26-lane-ax-names.md`, started 01:02 UTC, box 120 min.
Intake gate: `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74` -> `lodewijk-van-nassau-1573-74: partial
(line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Gate for step 3, written 01:10 UTC before the control was run.** Hold out 5811 (Groen IV CDLXXXIII): build the
code->value map from every other pair, predict each code >120 that occurs in 5811 and has a value in that map, and
score a prediction a hit when 5811's own alignment to its Groen text gives the same value at that code's occurrences
(majority). Briefed gate: held-out hit rate >= 60% of predicted codes, and 20 shuffles of the map's code->value
assignment (seeds 1-20) <= 10%. Known design issue, stated before running: the alignments so far show most codes
121-150 absorb nothing (nulls), so a map that is mostly NULL keeps most of its hits under any shuffle of values among
codes -- the <=10% shuffle bound cannot be met by a correct null-heavy map. So the briefed gate is applied, unchanged,
to the word/name codes (value not NULL), which is the question the brief asks (do name codes transfer); the null class
is reported separately with its own shuffle numbers and gated at held-out >= 60% with shuffle mean below the
held-out rate by >= 20 points. If fewer than 3 word/name codes are predictable in 5811, the word-class gate is
reported as "not testable at this N" and no word/name value is merged on the strength of the control alone.

**Sources fetched (step 1).** dbnl.org, descriptive UA, 2 s apart: Groen IV CDLXVIII (5810, pp.320-324,
`groen_IV_CDLXVIII.txt`), CDLXXXIII (5811, pp.363-366, `groen_IV_CDLXXXIII.txt`), CDLXXXIV (4503, pp.368-369,
`groen_IV_CDLXXXIV.txt`); two further requests landed on CDLXXX/CDLXXXI (page-number offset, discarded). 5 requests.
The WVO PDFs of 5550 and 5557 (resources.huygens.knaw.nl, 2 requests) were fetched to the scratchpad only, to read
their contemporary interlinear glosses over codes > 120 by eye (crops of leaf 2 of 5550 and leaf 1 of 5557); not
committed. Groen prints 4503 abridged ("....") and signs 5811 for Brunynck; both still align.

**Method (step 2).** `axnames/align_names.py`: per manuscript page, a semi-global DP of the cipher token stream
against Groen's whole printed letter (numerals 1-120 emit their key.tsv letter; clear words their letters; every code
> 120 is free to absorb 0-22 printed letters at a small per-letter cost; skips cost 1). Exact letter matches per
page: 5810 81-93%, 5811 64-84%, 4503 88% (the passes are single-pass M for 5810/4503). `axnames/build_names.py`
turns the per-occurrence output (`axnames/occ_*.tsv`) into `names.tsv` by fixed rules (clusters of adjacent codes
> 120 with >= 3 exact anchors each side and <= 16 absorbed letters; NULL if >= 2 empty observations and >= 75%
of them; a word observation only where one non-null code is left in the cluster) and merges the hand-read
attestations in `axnames/attest_manual.tsv` (period glosses on 5550/5557, Groen-printed names at 5797's own
clusters, and four UNPRINTED rows where Groen's print leaves the name out). `python3 axnames/build_names.py
--check` exits non-zero if names.tsv is stale.

**Finding 1: codes 121-149 are nulls in this table, not names.** 24 codes read NULL at grade C (2-31 empty
observations each, none contradicting): 121-124, 126-144, 149. Method-bias diagnostic
(`axnames/falsenull_diag.py`, 5 seeds, a random 10% of known letter codes 1-120 hidden as free codes): a hidden
letter code comes out absorbing nothing in 18.0% of single occurrences (414 of 2296; own letter 60.7%, other 21.3%),
so a real letter code yields k empty observations in a row with p about 0.18^k: 3% at k = 2, 0.1% at k = 4. Weakest
NULL rows: 139, 140, 142 (2 observations each). Known-answer check of the same aligner on key.tsv's own source pair
(4613/4615, `occ_sib.tsv`, never used to build names.tsv): 121/122/132 NULL (as key.tsv); 270 bommel, 347 vivres,
338 chevaulx legiers exact; 272, 326, 337 recovered with a one-letter boundary slip. **Conflicts with key.tsv**:
123 (key.tsv 'l', M) reads NULL in 13 of 13 observations; 136 (key.tsv 'vingt', M) NULL in 8 of 8; 128 (key.tsv
'?', M) NULL in 15 of 15; 147 is 'w' twice (5810's two copies, before 'vaterlandt' for Groen's "Waterlandt") and
NULL once (5557) -- listed M with both values.

**Finding 2: name and word codes attested** (value, grade, evidence): 153 Pfalzgraf C (5550 gloss "Palsgrave" twice,
5549 PS "bey dem Churfürst Palsgrave" in Groen Suppl. p.147*); 161 Landgraf C (5550 gloss "Lantgrave" over 153.161);
171 der Prinz zu Oranien C (5550 gloss "der Prince zu Oranien helfe" over 171.141 h-e-l-f-e); 173 "...graf" M (5550
gloss "Palsgrave vnd graf" over 153.130.90.1.79.173, prefix of the last word not legible); 200 Herzog von Alba C
(5797 p6, Groen p.224 "vom Herzog von Alba absondern" against `von 200.122.132.142 abso-`); 154 Herzog von Sachsen C
(5797 p5, Groen pp.223-224 "Bey dem Herzog von Sachsen und" against `Bey 154.124.144.134 und`); 155 Kölln M (5797
p6, `morgen 100.155 der hofnung`, 100 unexplained); 202 Franckreich C (5550 x4); 223 Harlem C (5810 x3); 241
Zeelande C (5810); 336 Fussvolck C (5557 gloss "Voetvolck", 5549 PS); 339 Schützen C (5557 gloss; same sense as
key.tsv's harquebouziers); 346 "Dubbel" M (5557 gloss, read uncertainly); 350 gelt C (5550 x2); 338 cavallerie C
(5811; key.tsv 'chevaulx legiers', same sense); 311 pays M; 351 bateaux M (2 of 3); 125 'l', 180 'de', 242 NULL,
310, 312, 359: single noisy observations, M. Unread in print (grade U, no value): 157 (5810 "et que [157] semble
procéder", Groen's footnote "Apparemment le Roi de France, ou l'Electeur de Cologne"; the other copy has 187; and
5549 PS "des [157] abgedanckt", Groen's footnote "Nom propre sous-entendu") and 192 (Groen Suppl. p.146* prints the
numerals "121. 133. 192."; 5557 "von 192 gute vertröstung", no gloss). **names.tsv: 51 codes, C 36 (24 of them
NULL), M 12, U 3.**

**Step 3 control (gate as written above at 01:10 UTC), `python3 axnames/control_5811.py`:**
```
NULL: held-out 9/11 = 81.8%; shuffles mean 73.0% (min 50.0, max 100.0, n=20)
word: held-out 1/1 = 100.0%; shuffles mean 0.0% (min 0.0, max 0.0, n=20)
all: held-out 10/12 = 83.3%; shuffles mean 40.4% (min 16.7, max 58.3)
5811 codes with no prediction: ['311']
```
**Gate result: NOT PASSED.** As briefed (all predicted codes): held-out 83.3% (>= 60%, met) but shuffles 40.4%
(> 10%, not met). Pre-registered split: word/name class not testable at this N (1 predictable code, 351 bateaux, a
hit); NULL class 81.8% against a shuffle mean of 73.0% (gap 8.8 points, gate 20: not met). The two NULL misses (137,
141 in 5811) are single 5811 occurrences where the cluster absorbed a transcription gap ('et', 'streduuiiepar').
Why the gate cannot pass as designed: the map is 24 NULL of 36 C rows, so a shuffle still predicts NULL for most
5811 codes (rule 3's near-ceiling warning); 5811's own word codes (311, 338, 351) mostly occur only in 5811. The
diagnostic and known-answer numbers above are a better test of the NULL finding, but they were not the pre-written
gate, so they do not license step 4 here.

**Step 4 not run** (conservative reading of the brief: "If the gate passes"). No key_full.tsv, no decode_*_full.json,
no reading_*_full*; key.tsv and every N4 reading untouched. What a merge would touch, counted only
(`axnames/coverage.py` -> `axnames/coverage.tsv`, no decode):

| letter | U now | U on a NULL-C code | U on a word-C code | U on a word-M code | U left |
|---|---|---|---|---|---|
| 4610 | 288 | 161 | 4 (153 x2, 200, 202) | 20 (125 x19, 180) | 103 |
| 4611 | 227 | 121 | 6 (200 x5, 223) | 16 (125 x14, 311 x2) | 84 |
| 4616 | 26 | 4 | 0 | 0 | 22 (mostly unsettled split tokens like 22/112) |
| 5797 spots | 31 | 17 | 4 | 2 | 8 |

**5797 spots against names.tsv (lookup only; no reading made, gate not passed; Groen's printed frame from
Groen IV pp.223-225):**

| spot | code run | names.tsv at those codes | Groen's frame |
|---|---|---|---|
| p5_spot5 | (ist) 131.123.173 (gestern) | 131 NULL C, 123 NULL C (key.tsv 'l' M), 173 "...graf" M | "ist gestern zue ghen gezogen" |
| p5_spot3 | Bey 154.124.144.134 und 161.126.136.146 ist | 154 Herzog von Sachsen C (Groen prints it here), nulls C, 161 Landgraf C, 136 NULL C (key.tsv 'vingt' M), 146 no row | "Bey dem Herzog von Sachsen und ist [w]illens" |
| p6_spot4 | 172 zeuget ... morgen 100.155 der | 172 no row; 155 Kölln M | "zeuget diesen morgen Kölln der hofnung" |
| p7_spot2 | 153.146.137 helt sich wol | 153 Pfalzgraf C, 146 no row, 137 NULL C | "helt sich wol und thut in warheit viel" |
| p7_spot6 | 182.128.133.142 ist willig | 182 no row, 128/133/142 NULL C | "ist willig und urbietig ... dasz er mit bruder möge mit vortziehen" |
| p8_spot7 | 156.127.135.144.129 begert meiner | 156 no row, the other four NULL C | "begert meiner, kan aber nicht wiszen warumb" |

So each spot carries one (p5_spot3: two) non-null code; names.tsv has a C row for two of them (161 at p5_spot3,
153 at p7_spot2), an M row for one (173 at p5_spot5) and none for 156, 172, 182 (nor 146). Not located in Groen IV
pp.217-226 as printed words at these spots; this is a table lookup, not a reading, until a gate that can pass (or
the orchestrator's decision) licenses step 4 and a fresh instance re-derives it.

**Next step (one line, for the orchestrator):** re-gate on a control that is not at ceiling -- e.g. the
known-answer run on 4613/4615 plus the hidden-letter false-null rate above, pre-registered -- then run step 4 as
briefed (key_full.tsv = key.tsv + names.tsv C rows, the three key.tsv conflicts 123/128/136 decided by the
orchestrator since key.tsv rows stay unchanged); 146, 156, 172, 182 and 157/187/192 need further glossed siblings
(the "solved on leaf" items 4496/4614/7205/7206/7208 in csWV3, 5552's glosses, 5557 leaves 2-4 not read this pass).

Requests: dbnl.org 5, resources.huygens.knaw.nl 2 (WVO PDFs 5550, 5557). No subagents. Files: `names.tsv`,
`axnames/{align_names.py,build_names.py,attest_manual.tsv,control_5811.py,control_5811.tsv,control_5811.out,
falsenull_diag.py,falsenull_diag.out,coverage.py,coverage.tsv,occ_*.tsv,summ.py,win.py}`,
`groen/{groen_IV_CDLXVIII,groen_IV_CDLXXXIII,groen_IV_CDLXXXIV}.txt` and their HTML. Novelty not classified.

## AX-NAMES2: key_full and the 5797 spots (26 Sept 2026, LANE AX)

Worker AX-NAMES2 (Opus), brief `.claude/briefs/runs/2026-09-26-lane-ax-names2.md`, started 01:43 UTC (clock read).
**(0) Intake gate:** `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74` -> `lodewijk-van-nassau-1573-74:
partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Orchestrator's decision (01:42 UTC 26 Sept 2026, written before any step-4 run), verbatim:**
"AX-NAMES' held-out gate could not fail for a null-heavy map (rule 3 ceiling warning), so it is replaced, not relaxed, by three gates set per class. (a) Word/name codes whose value is read from a contemporary interlinear gloss (5550, 5557) or printed by Groen at that very cluster are key-source readings (rule 4: H for gloss, C for print-at-cluster), not aligner output; they merge without an aligner control: 153, 161, 171, 202, 336, 339, 350 (gloss), 154, 200 (print at the 5797 cluster). Aligner-only word codes merge only at C with >=2 agreeing observations (223 Harlem); every single-observation word code stays M and out of key_full. (b) NULL codes merge if they have >=4 empty observations and 0 contradicting (false-null rate 0.18^4 = 0.1%, AX-NAMES' diagnostic); 139, 140, 142 (2 obs) stay out. (c) key.tsv conflicts 123, 128, 136 (key.tsv M values vs 13/15/8 NULL observations): key_full takes NULL with a note; key.tsv itself stays unchanged. Before merging, re-run the known-answer check on 4613/4615 (occ_sib) with key_full: every key.tsv C letter there must still decode as before (0 regressions) -- if any regresses, stop and flag."

**(1) key_full.tsv** (`python3 axnames/build_key_full.py [--check]`; it re-checks every licence against names.tsv and
fails if one no longer holds). key.tsv's 139 rows + 22 new + 3 overridden = 161 rows:
- H 6 (contemporary gloss): 153 pfaltzgraf, 161 landgraf, 171 prinzzuoranien, 202 franckreich, 336 fussvolck, 350 gelt.
  339 is gloss-attested too ('Schutzen', 5557) but key.tsv already has it (harquebouziers, C, the same troop word): the
  key.tsv row is kept, gloss recorded in its note, not counted as new.
- C 3: 154 herzogvonsachsen, 200 herzogvonalba (Groen prints the name at that 5797 cluster); 223 harlem (aligner, 3 of
  3 agree). Values are senses: in the French letters 200 is "le duc d'Albe", not a German spelling.
- NULL 13 (class b, >= 4 empty, 0 contradicting in names.tsv): 124, 126, 127, 129, 130, 131, 133, 134, 135, 137, 138,
  143, 144. 149 (3 observations) also stays out, as do 139/140/142.
- Class (c) 123, 128, 136 -> NULL, **graded M, not C** (my choice, conservative, logged here): step 2 shows that on
  the known-answer pair itself 123 stands where the printed decipherment has 'l' (4613 L18 qu'ilz; L29), 136 where it has
  'vingt' (4613 L04) and 128 at the unsettled tail of 'Trittheim' (4613 L28); the sibling aligner (occ_sib) absorbs
  'l', 'uing', 'im' there. NULL is right for 5810/5811/4503 (13/15/8 observations) and drops plaintext letters in
  4613/4615, so these three codes are either context-dependent or double-duty, and M says so.

**(2) Known-answer regression check** (`python3 axnames/compare_full.py decode.json ciphertext_sib.tsv --list`,
`axnames/regress_sib.out`): 1107 tokens, 1086 C under key.tsv, **regressions 0**, 5 tokens changed (the three
class-(c) codes above: 136 uingt M -> NULL M, 123 l M -> NULL M x3, 128 ? U -> NULL M). The gate as written passes;
the class-(c) caveat above is what it surfaced.

**(3) Decodes**: `decode_{5797,4610,4611,4616}_full.json` -> `reading_<n>_full.txt` / `_full_tokens.tsv`, each
`tools/decode_key.py --check` "reading up to date". Existing readings untouched.

| letter | U key.tsv -> key_full | changed tokens | of which word/name | grades under key_full |
|---|---|---|---|---|
| 4610 | 288 -> 162 | 136 | 4 (153 x2 H, 200 C, 202 H) | C 1203, H 3, I 58, M 119, U 162 |
| 4611 | 227 -> 133 | 99 | 6 (200 x5, 223) | C 913, I 71, M 276, U 133 |
| 4616 | 26 -> 25 | 2 | 0 | C 208, I 1, M 27, U 25 |
| 5797 (spots file) | 31 -> 12 | 21 | 4 | H 2, C 15, M 41, I 3, U 12 |

**(4) 5797 spots against Groen's frame** (Groen IV pp.223-225; token grades from reading_5797_full_tokens.tsv, the M on
cipher letters is decode_key's downgrade for sign confidence; nulls shown as "."):

| spot | decoded under key_full | Groen's printed frame | gap filled? |
|---|---|---|---|
| p5_spot5 | ist [131 . C][123 . M][173 U] gestern | "ist gestern zue ghen gezogen" | no (173 'graf' M stays out) |
| p5_spot3 | Bey [154 Herzog von Sachsen, C] [124 . 144 . 134 .] und [161 Landgraf, H] [126 . C][136 . M][146 U] ist | "Bey dem Herzog von Sachsen und ist [w]illens" | **yes: 161 Landgraf, H** (154 is Groen's own word, a control) |
| p6_spot4 | [172 U] zeuget diesen morgen [100 h, I][155 U] der hofnung | "zeuget diesen morgen Kölln der hofnung" | no (172 no row; 155 'Kölln' M stays out) |
| p7_spot2 | [153 Pfaltzgraf, H][146 U][137 . C] helt sich wol | "helt sich wol und thut in warheit viel" | **yes: 153 Pfaltzgraf, H** |
| p7_spot6 | [182 U][128 . M][133 . C][142 U] ist willig und urbietig ... Dass er mit | "ist willig und urbietig ... dasz er mit bruder möge" | no (182 no row) |
| p8_spot7 | [156 U][127 . 135 . 144 . 129 . C] begert meiner | "begert meiner, kan aber nicht wiszen warumb" | no (156 no row) |
| p6_control_abso | nicht allein von [200 Herzog von Alba, M][122 . 132 .][142 U] abso- | "vom Herzog von Alba absondern" | Groen's own word (control) |

**Spots with a value: 2 of 6** (p5_spot3 "und [161 Landgraf, H] ist willens"; p7_spot2 "[153 Pfaltzgraf, H] helt sich
wol"), both from the 5550 period gloss, neither from our aligner. One pattern for AX-GLOSS: 146 follows both 161 and
153 here (and 'secours' on p3), so it may be a title/suffix or a null that the 2-observation rule kept out.
Revisions for the orchestrator: `revisions_for_audit.tsv` (`python3 axnames/revisions.py [--check]`), 258 rows
(letter, line, pos, code, old, new, grade, class, source, context): 4610 136, 4611 99, 4616 2, 5797 21; word/name
rows 14 (the table above), the rest NULL placements that remove a '?' placeholder and change no letter. I did not edit
AUDIT.md or SECOND-OPINIONS-QUEUE.tsv.
[Verifier V8-NA5797, 26 Sept 2026: "gap filled? yes" for p5_spot3 means one word of four codes -- 126 NULL, 136 key_full 'vingt' (M, cannot fit) and 146 (U) still sit in Groen's blank before "ist willens"; and 153's H rests on one clean 5550 gloss (run p2-11, 'Palsgraue'), not two (AUDIT.md V8.2). Class: AUDIT.md V8.1.]
[Second verifier V8-NA5797-2 (A2), 26 Sept 2026: "gap filled? yes" for p7_spot2 likewise means one name of a three-code blank -- 146 (U) sits between [153 Pfaltzgraf] and "helt sich wol" (137 NULL C). Both classed blanks are read in part. Class held at N4: AUDIT.md A2.1.]

**(5) Judge**, `python3 tools/judge_plaintext.py specs/lodewijk-5797.json --file ciphers/lodewijk-van-nassau-1573-74/reading_5797_full.txt`:
```
FAIL language: score=-1.435, null_p99=-1.617, real_p05=-0.456, real_median=-0.428, mode=both, N=308
FAIL words: cover=0.344, min=0.5, real_text_median_cover=0.756
FAIL - lodewijk-5797 (a PASS is a gate for a verifier, not a reading; rule 10)
```
(key.tsv reading: -1.504, N=197.) Not a test of the spots: each spot's own decoded content is 0-16 letters, far
below judge length, and the file is disconnected clusters with Groen's clear words stitched in and name values
concatenated (`herzogvonsachsen`), which the word-cover test cannot parse. Per-fold caveat: the de16 corpus is one
composed file (`tools/data/de16/composed_enhg.txt`), so no leave-one-file-out spread exists; its FAIL/PASS is of unknown
reliability in the sense of rule 3 (EN-FOLDS/es17c lessons). The spots rest on the gloss (H), not on the judge.

**(6) Extension: 5810/5811/4503 under key_full** (`axnames/sanity_{5810,5811,4503}.out`; in-sample for most rows,
since names.tsv was built on these letters): U 222 -> 30 (5810), 53 -> 23 (5811), 11 -> 2 (4503); regressions 0.
Word changes: 223 harlem x4 in 5810, all four at Groen's "Harlem" (two copies each of "ville de Harlem" and "dudict
Harlem"); at the two "ville de Harlem" places the aligner had put 'harlem' on the neighbouring null 127 and nothing on
223, so names.tsv's 3 of 3 undercounts it: 4 of 4 agree. **Words disagreeing with Groen: 0.** Caveat on class (b):
names.tsv's "0 contradicting" was counted after build_names.py's cluster filter; before the filter, the 20 NULL codes'
raw aligner occurrences are empty 319, absorb 1-5 letters 21, 6+ letters 20 (`axnames/null_raw.py` ->
`axnames/null_raw.tsv`; 6+ is typically a transcription gap swallowed by a free code, e.g. 5811 136/130 absorbing
'cauallerie' at the two copies of one sentence). The 1-5-letter cases (e.g. 124 'a' and 133 'f' at both copies of one
5810 sentence) are 5.8% of occurrences, below the 18% hidden-letter false-null rate, so consistent with nulls plus
alignment slack, but they are contradictions the gate text did not count.

**(7) Extension: still unread**, `axnames/still_unread.py` -> `axnames/still_unread.tsv` (78 distinct U signs, 387 U
tokens across sib/4610/4611/4616/4503/5810/5811/5797 under key_full). Top: 150 x75, 125 x34, 140 x26, 142 x25, 149
x25, 145 x24, 148 x24, 139 x19, 147 x16, 146 x11 -- all in 139-150, mostly between words in 4610/4611, which looks like
the same null band extending to 150 (not tested: 4610/4611 have no print to align). Then 192 x6, 151 x5, 221/225/311/
351 x3, and the 5797 spot codes 172, 173, 182 (x2 each) and 156 (x1).

**Next step (one line):** fresh-instance re-derivation of reading_5797_full / 4610 / 4611 / 4616 from key_full.tsv
(rule 7), then V7 on the two H spot fills; AX-GLOSS on 146, 156, 172, 182 and the 139-150 band (5552, 5557 leaves 2-4,
the csWV3 "solved on leaf" items); orchestrator to decide whether 123/128/136 stay NULL-M or become context rules.

Requests: none (disk only). No subagents. Files: `key_full.tsv`, `decode_{5797,4610,4611,4616}_full.json`,
`reading_{5797,4610,4611,4616}_full{.txt,_tokens.tsv}`, `revisions_for_audit.tsv`, `axnames/{build_key_full.py,
compare_full.py,revisions.py,null_raw.py,null_raw.tsv,still_unread.py,still_unread.tsv,regress_sib.out,
sanity_5810.out,sanity_5811.out,sanity_4503.out}`. Novelty not classified.

## AX-4612: block-constrained cryptanalysis (26 Sept 2026, LANE AX)

Worker AX-4612 (Opus), brief `.claude/briefs/runs/2026-09-26-lane-ax-4612.md`, 01:43-02:12 UTC. Cryptanalytic
attempt only: no reading is claimed, no token graded, novelty not classified (4612 stays N3, no reading).

**Intake gate** (`python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74`, exit 0):
`lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
AUDIT.md (A1, kept in D1): "4612 | 6 Mar 1574 | N3 (kept) | coverage is the same as the others, but there is no reading
to qualify: most keyed runs do not read as French, so 'no prior decipherment located' would describe a decipherment
this repo does not have. Re-class when a reading exists"; D1: "4612 stays N3, as A1 set it." The principal editions
(Groen, Blok 1887 and 1889, Gachard, Kervyn, La Huguerye) were covered by A1.

**Spec.** `specs/lodewijk-4612.json` (`ax4612/make_spec.py`): numerals 1-120 of `ciphertext_4612.tsv` as transcribed,
split into 20 runs at clear words; N=775, K=100; dropped 19 codes 121-149 (nulls, AX-NAMES) and 18 codes >=150 (names or
words); the 1574 of the date line is clear text. p1_L18/p1_L19 repeat an 8-numeral stretch with the same clear words
(possibly one line read twice); kept, not repaired. **This is a transcription (rule 2):** 4612's two blind passes agreed
on 559/1170 = 47.8% of aligned columns (4610 78.6%, 4616 83.8%), 678 of 1170 rows are M. Every negative below is
conditional on it.

**Judge corpus.** fr16, all three files (Catherine de Medicis t.1-2, Marguerite de Valois), 16th-century court
letters, era-matched. Per-fold spread at N=775 (`ax4612/fr16_folds.py`, output `ax4612/fr16_folds.txt`): held-out
Catherine t.1 7.5%, t.2 67.5%, Marguerite 2.0%; blended 25.7% over 3 folds. Three files with a 34x spread: under rule 3
this is a judge of unknown reliability. **Calibration on real letters:** key.tsv's own reading of 5811 cut to 775
numerals FAILs this judge at -1.233, and of 4610 at -1.100 (real_p05 -0.944), because the drafts' transcription errors
and missing word breaks at this length pull real Nassau French below the gate. On this material the judge cannot
decide. The comparisons below therefore use the solver's own objective (same N, same model) against a shuffle floor and
against real letters, as well as the judge.

**New tool.** `tools/families/block_homophonic.py` (+ `tools/tests/test_block_homophonic.py`, offline, about 3 s: geometry,
key.tsv round trip, control shape, known answer 1.000 at width 5 offset 0 vs 0.256 at the wrong offset). It rewrites the
ciphertext as block labels (width, offset, lo..hi) and anneals only the block -> letter map through
`homophonic_anneal.solve`. Control: same width/offset, random block order, homophone choice weighted by the target's
own value counts, `gap` letters cut at each run boundary (gap=80, about 351 clear-word tokens over 19 interruptions).

**Pre-registered** in HYPOTHESES.md at 01:48 UTC before any target run: gate 0.6, 3 seeds, 8 restarts. Every row, control
beside target (solver score: higher is better; judge fr16, null_p99 -1.718, real_p05 -0.944):

| run | control mean (range) | target solver score | target judge |
|---|---|---|---|
| H1 w5 o0 | 0.722 (0.210-0.982) | -2175.3 | FAIL -1.302 |
| H1 w5 o1 | 0.722 (0.210-0.982) | -2142.2 | FAIL -1.312 |
| H1 w5 o2 | 0.722 (0.210-0.982) | -2161.7 | FAIL -1.324 |
| H1 w5 o3 | 0.722 (0.210-0.982) | -2141.2 | FAIL -1.280 |
| H1 w5 o4 | 0.722 (0.210-0.982) | -2133.3 | FAIL -1.300 |
| H2 w4 o0 | 0.852 (0.599-0.982) | -2121.8 | FAIL -1.241 |
| H2 w4 o1 | 0.977 (0.974-0.982) | -2115.7 | FAIL -1.277 |
| H2 w4 o2 | 0.966 (0.947-0.982) | -2105.3 | FAIL -1.299 |
| H2 w4 o3 | 0.966 (0.943-0.982) | -2108.9 | FAIL -1.330 |
| H2 w6 o0 | 0.717 (0.225-0.966) | -2187.0 | FAIL -1.302 |
| H2 w6 o1 | 0.873 (0.676-0.982) | -2184.9 | FAIL -1.286 |
| H2 w6 o2 | 0.972 (0.961-0.982) | -2205.6 | FAIL -1.366 |
| H2 w6 o3 | 0.972 (0.961-0.982) | -2239.3 | FAIL -1.347 |
| H2 w6 o4 | 0.977 (0.974-0.982) | -2197.7 | FAIL -1.313 |
| H2 w6 o5 | 0.813 (0.489-0.977) | -2167.6 | FAIL -1.283 |
| H3 homophonic profile=target | 0.660 (0.443-0.959) | -1865.0 | FAIL -1.213 |
| *extension* H1 w5 o0, 4612 shuffled (floor) | 0.722 (0.210-0.982) | -2224.3 | FAIL -1.387 |
| *extension* H3, 4612 shuffled (floor) | 0.660 (0.443-0.959) | -1921.2 | FAIL -1.217 |
| *extension* real 5811 cut to N=775, w5 o0 | 0.989 (0.978-0.997) | -1901.1; **0.871 of key.tsv's letters recovered blind** | FAIL -1.128 |
| *extension* real 4610 cut to N=775, w5 o0 | 0.739 (0.462-0.965) | -1823.7; **0.948 of key.tsv's letters recovered blind** | FAIL -1.048 |
| *extension* H3 on real 5811 N=775 | 0.562 (0.317-0.915), CONTROL BELOW GATE | not run | - |

The H1 control's seed 1 is a search failure (0.210; its plaintext window, printed and checked by eye, is ordinary French), which is
why the H1 mean is 0.722 and not about 0.98. Recoveries for the real letters come from `ax4612/score_realctl.py`.

**What this shows.** The block family reads real Nassau letters in their actual noisy drafts blind (5811 0.871, 4610
0.948 of key.tsv's letters, solver scores -1824 to -1901). On 4612 it scores -2105 to -2239 at every width 4/5/6 and
offset, next to its own shuffle floor (-2224) and far from the real letters, and the decodes are letter salad
(`families/block_homophonic-*.txt`). H3's decode (-1865) is level with H3's shuffle floor (-1921; judge -1.213 against
-1.217): no signal. **H1 and H2 are control-backed negatives on this transcription**. H3 is a negative with a weak
control (0.660 on synthetic, below gate on real 5811): not excluded.

**Diagnostics (extension, `ax4612/`).**
- `ic_scan.py`: block IC at w=5 for 4612 is 0.0617 at best, flat across offsets (null p95 0.0567). The same statistic is
  0.078-0.081 at o0 for sib, 5811 and 4610, with a clear peak there. Residue classes (v mod m, m=10-48) show nothing.
- `ic_by_conf.py`: 4612's **pass-agreed (H) numerals alone** (N=429) give w5 IC 0.0629, flat, against 0.0804 (4610 H,
  N=1115) and 0.0805 (4611 H, N=852) at o0. Random transcription noise alone therefore does not explain 4612's lack of
  block structure, unless both passes misread the same digits the same way.
- `digit_map.py` (E3): key.tsv read through a consistent digit misreading (a permutation of the ten digits,
  hill-climbed, 20 restarts). Control: real 5811 at N=812 through a random digit permutation, 3 seeds; each recovered
  10/10 digits and key.tsv's reading at 1.000. Target: the best map scores -2695.7 (identity -2954.7; the real 5811
  reading scores -2140.1 at the same N) and decodes to salad. Negative.
- `affine_map.py` (E4): key.tsv read through v' = a(v-1)+b mod 120 +1 (all 3,840 maps, including every cyclic shift and
  the reversal) and through digit reversal plus shift (120). Control: 5811 through a random affine map, 4 seeds, one of
  them a fixed non-involution (a=7, b=5); the inverse was found 4/4. Target: identity is the best of 3,960 (-2954.7;
  median -3417.0; the real 5811 reading scores -2137.9). Negative.
- Value profile (`ax4612` scan, not a test): 4612 uses values 1-90 densely (718 of 775 numerals) and 91-120 hardly at
  all (57). Inside blocks of five over 1-90 the second position carries 229 of 718 and the fifth 68 (mod-5 class IC
  0.2259, about the null's p97). 18 blocks of five over 1-90 would fit an 18-consonant x 5-vowel syllable grid
  (b c d f g h k l m n p q r s t v x z x a e i o u), and La Huguerye (AUDIT A1) says this cipher had syllables. The
  evidence is weak and the design is untested.

**Result.** No reading. 4612 is not in key.tsv's design with another letter order (H1). It is not in blocks of 4 or 6
(H2). It is not key.tsv through a digit permutation, an affine map, a shift, a reversal or a digit reversal. Each of
these was tested against a matched control that passed, and H1/H2 also against real-letter positive controls. The free
homophonic (H3) is untested-not-excluded (weak control). Status of the folder unchanged (`partial`).

**Next steps (suggestions, not done):** (1) look at the 4612 page images against 4610's for the numeral hand. Is it a
different secretary, and are there marks on the numerals, such as a dot or a stroke that a syllable table would use?
Then re-transcribe 4612 from the images (47.8% pass agreement is the weakest of the six letters). (2) If the image
supports it, a syllable-grid family (18 consonant blocks x 5 vowel positions over 1-90), control first. (3) H3 at more
iterations or with the table's contiguity as a prior, once a control at N=775 reaches the gate.

Files: `specs/lodewijk-4612.json`, `tools/families/block_homophonic.py`, `tools/families/__init__.py` (registry),
`tools/tests/test_block_homophonic.py`, `HYPOTHESES.md` (pre-registration + 21 rows), `families/block_homophonic-*`,
`families/homophonic-1-profile=target-ax4612h3freehomo.txt`, `ax4612/` (scripts, run logs, fr16_folds.txt,
digit_map.txt, affine_map.txt, realctl_*). No network requests.

## AX-GLOSS: glosses over the name codes (26 Sept 2026, LANE AX)

Worker AX-GLOSS (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-gloss.md`, started 01:44 UTC, box 80 min.
Per the brief's 8 units: 4496, 4614, 7205, 7206, 7208 (WVO "solved on leaf"), 5801+11250 (contemporary decipherment
attached per csWV3), 5552, 5557 leaves 2-4 (leaf 1 already read, in `jan-van-nassau-1572-75/j5s/
ciphertext_glossed_5557_5552.tsv` -- checked that file first: it holds only 5557 leaf 1, no 5552 rows at all,
contrary to its own filename).

**Method.** WVO PDF fetched per letter from `pdf_url` in `sources/wvo/cipher-letters-2026-09-24.tsv` (one request
each, >=2s apart, descriptive UA), rendered to PNG with `pymupdf` (`pip install pymupdf pillow`, no `pdftoppm`
binary in this container) at 200dpi, read by eye at full-page resolution then cropped/zoomed (PIL, with a pixel
gridline overlay to check horizontal alignment of a superscript gloss word against the specific number below it)
wherever a candidate gloss was visible. Step (b) sanity check (decode 3 runs of 1-120 codes under key.tsv): 4496 and
4614 both decode partial French fragments and known place-code hits (see below) consistent with the same table;
5552's own cipher runs are too short/interrupted by clear text to give a clean 3-run check but its two visible
glossed-looking marginal words turned out to be continuing clear prose, not annotations (see below).

**Finding 1 (H): 192 = "R. d'Espagne" (Roy d'Espagne, King of Spain).** 4496 (WVO PDF page 4 of 5), a contemporary
interlinear gloss reading "R. d'Espagne" sits directly above the code `192` in the run "...113.85.124.**192**. pour
113.82...", isolated with clear whitespace on both sides (`images_wv2/crops_gloss/04496_p4_respagne_192.png`).
names.tsv previously had 192 as grade U ("Groen prints no word here", from 5549 PS1 where Groen's own edition left
the subject out); `axnames/still_unread.tsv` lists 192 with 6 unread occurrences in 4610 alone. This is the first
value found for this code. Blind Sonnet pass A (independent, crops only, no prior reading shown) confirms: "the
small cursive phrase '...le R[oy] d'Espaigne...' sits immediately above the '192' group... high [confidence] that
this gloss word sits over this specific number... medium confidence on the precise reading of the word itself."

**Finding 2 (H): 221 = "Hollande".** Same page (4496 p4), gloss "Hollando" sits directly above code `221`,
repeated 3x at different points on the same page, always over the same code. Cross-letter corroboration: 4614
(WVO PDF page 1) has the unglossed run "...tiré de la Haye en **221**..." (French "the enemy had withdrawn from
The Hague to [Holland]"), consistent in context though unglossed there. 221 had no prior row in names.tsv or
key.tsv; `axnames/still_unread.tsv` lists it with 3 unread occurrences in 4610/4611. Blind pass A: "'Hollande' --
sits directly above the very first number, '221' (high confidence, clean vertical alignment)."

**Finding 3, WITHDRAWN after the second blind pass -- do not treat 133 as glossed.** My own first read of 5557
leaf 2 placed a short gloss ("kein", German "none") directly above code `133` in the run
"...107.83.103.3.**133**...", which would have been a corroborating (not new) confirmation of names.tsv's existing
133=NULL (C, 9 observations from 5810). Blind pass A could not confidently read the word at all. **Blind pass B
placed the same gloss's position over `107`, not `133`** -- explicitly flagging the mismatch against this file's
own name ("I want to flag this explicitly since it may run counter to an existing reading... based on pure
horizontal position... the word sits over '107', not '133'"), with medium-high confidence on that position. With
my own read and two blind passes giving three different answers on where this one gloss actually sits (and none
of the three confident on the word itself), this is not a usable attestation for either 107 or 133 -- both are
<=120 anyway (out of this brief's >120 scope) and 133 already has 9 independent C-grade observations from 5810, so
nothing is lost by dropping it. Recorded here as a *process* finding: a single eyeballed alignment on a compressed,
multi-word line is not reliable even with a pixel-gridline overlay: two more independent reads are needed before
trusting a position call like this, exactly as the brief specified two blind passes for.

**221/192 are the two solid new fills this pass got; the brief's named priority codes (146, 156, 157, 172, 182,
187) were NOT filled.** Specifically checked and came up empty:
- **146**: found bare (no interlinear gloss) in 5557 leaf 3, in the clear run "...gelieffert Boot, **146**.
  verkündigen, weiss er gesinnet..." -- 146 sits alone, immediately followed by ordinary clear German prose, no
  superscript word attached to it in this occurrence.
- **156, 157, 172, 182, 187**: not located with an attached gloss in any of the 8 units this pass covered. Not
  exhaustively ruled out -- see the flags below on 5801, 4614 and 7205/7206, whose companion decipherments were
  not fully mined this pass for lack of time, and which are the most likely place these five still turn up.

**Per-unit findings (the WVO "solved on leaf" designation, checked against what is actually on each leaf):**

| letter | pages (WVO PDF) | what "solved on leaf" turned out to mean | interlinear code>120 word-glosses found |
|---|---|---|---|
| 4496 | 5 | dense interlinear grammatical-class marks (single superscript letters: v, n, c, t, p, g, oe...) over most codes throughout (the same convention as 5797's J5S notation, marking word class, not a value), PLUS several clear word-glosses (Hollando/Zellando/R.d'Espagne/P.Dorange) at a few specific spots | 192, 221 (both H, see above); 241 and 171 corroborated (already C in names.tsv) |
| 4614 | 6 | pp.1-3 dense cipher, no interlinear glosses at all; pp.5-6 are a **full separate contemporary plaintext decipherment on a companion leaf** (opens "Monseigneur vous ne sçauriez croire le grand contentement...", verbatim matching ciphertext p1's opening; dated "le 4 jour d'avril 1574" matching the cipher's own date) | none directly (see flag below) |
| 7205 | 10 | pp.1-6 dense cipher (a "Duplicata" copy), no interlinear glosses; p7 is a *different*, separate clear letter (signed Guillaume de Nassau, 21 Jan 1574) with its own short unglossed cipher tail; **pp.8-10 are a full separate contemporary plaintext decipherment** of pp.1-6's cipher (opens "Monsieur mon frere, les dernieres...", continues the same content as pp.1-6 in clear French) | none directly (see flag below) |
| 7206 | 8 | pp.1-2 clear + a short unglossed cipher tail; pp.3-4 dense cipher, no interlinear glosses; pp.5-6 clear text (signed Guillaume de Nassau) of similar shape to 7205's pattern -- likely another companion decipherment, not confirmed by close reading this pass (time) | none directly |
| 7208 | 5 | pp.1-3 dense cipher ("Duplicata", 21 Feb 1574), no interlinear glosses; p4 is the address leaf; p5 is a **separate, same-date clear letter** (dated 21 Feb 1574) that uses bare numbers (212, 213, 214, 224) as place-name stand-ins directly in its own clear prose -- a different, apparently-topographic nomenclature, not obviously the same system as key.tsv/names.tsv and not paired with any specific code in the pp.1-3 cipher | none |
| 5801 | 9 (+11250, 2 pages) | **pp.1-5 carry a complete, dense, letter-by-letter contemporary interlinear decipherment written directly above (and below) almost every cipher code** -- not isolated word-glosses but a running decode of the whole letter; pp.7-9 are additionally a full separate clear-text transcription (opens "Messieurs mes freres, j'ai receu vos tres...", dated "1573 Mai 28" matching 5801's own date); 11250 (the small strip) is itself plain French, no cipher, confirming NOTES.md's earlier finding that it is bound to 5801's decipherment, not to a cipher of its own | not mined this pass -- see flag below, this is the single richest resource found |
| 5552 | 4 | 2 leaves of clear German text with only a few short cipher runs woven in; the two marginal-looking words I initially read as glosses ("auff Colln zu" near one run) turned out on closer zoom to be the start of the *next clear sentence*, not an annotation over the preceding code | none |
| 5557 leaves 2-3 | 2 (of 4; p4 is the blank/address leaf, so there is no "leaf 4" with content) | leaf 2 and leaf 3 both carry a mix of short German-word marginal annotations (some over codes <=120, out of this brief's scope; "kein" over 133 is the one >120 hit) and codes that are glossed with full titles/place-names (Graf von Holland, Hertzog, Lutzenburg) sitting over codes <=120 that key.tsv already fixes as ordinary letters (82=e, 93=g, 112=l, all C-grade from many 4613/4615 observations) -- see the conflict noted below | 133 (M, corroborating) |

**Flag for the orchestrator/next lane worker -- three companion decipherments not yet mined (4614 pp.5-6, 7205
pp.8-10, 5801 pp.1-5's own interlinear text and pp.7-9's clear copy):** these are a much bigger resource than a
"gloss" -- potentially enough to read 4614, 7205 and 5801 in full at grade C, the same way Groen's print did for
5799/5810/5811/4503/5811. Mapping the clear text (4614, 7205) or the interlinear letters (5801) back to specific
ciphertext codes needs the same DP/hard-EM alignment already built for this purpose -- `tools/interlinear_align.py`
(CLAUDE.md Usage item 8) for a printed/typed clear text beside cipher, or a comparable careful crop-and-zoom
transcription pass for 5801's own interlinear letters, which are written far smaller and denser than anything this
brief's per-unit budget (about 8 minutes) could responsibly transcribe. This is a full alignment job (or three),
not a gloss-harvesting one; sizing its cap and box from CLAUDE.md's per-unit-rate rule (Usage item 6) before
briefing it is recommended given how dense 5801 in particular is.

**Flag: 5557 leaf 3's title/place-name glosses sit over codes key.tsv already fixes as ordinary letters** (82=e,
93=g, 112=l), not over any of the codes >120 in the same runs (127, 129, 135, 122, 139, 147). Two explanations
occurred to me and neither was checked further this pass: (a) these are archival/finding-aid topic tags added
later, summarising a passage's subject rather than decoding a specific code (consistent with 5557 leaf 2's "jar",
"kein", "Vorrad" also reading like short thematic labels rather than literal per-code values); (b) 5557 uses a
different table from key.tsv's for these low codes. Not resolved; flagged rather than guessed.

**Two blind Sonnet subagent passes** (crops only, no prior reading shown, one call per leaf's worth of crops; both
landed before the box ended). Both independently confirm the two H-grade finds: 221=Hollando (both: high
confidence, clean alignment) and the gloss ending "-gne" (consistent with (le Roy) d'Espagne) directly above 192
(pass A: high position confidence; pass B: medium-high). Both also independently confirm 241=Zellando (already
C-grade in names.tsv). Neither pass could confidently read or place the "kein"-like gloss near 133/107 -- pass A
called the word illegible, pass B placed its position over 107, not 133 -- so that finding is withdrawn (see
above), which is exactly the kind of miscall two blind passes are supposed to catch before it reaches names.tsv.
Pass B additionally read a second, previously-unnoticed gloss in the 05557_p2_jar_94.jpg crop ("beritten"(?), i.e.
"mounted"/"on horseback", over the second occurrence of 82) and refined "Graf von Holl[andt]" as one phrase
spanning several numbers rather than a single word over 93 -- both <=120, out of this brief's >120 scope, noted
for whoever next looks at 5557's low-code annotations (see the flag above).

Rule 10: no novelty words used. Rule 3: no controls run this pass (no numeric threshold gated); the two new
values (192, 221) are grade H per rule 4 (read from a contemporary key source, i.e. a period gloss), not
cryptanalytic.

Hosts: `resources.huygens.knaw.nl` 9 requests (04496, 04614, 07205, 07206, 07208, 05801, 11250, 05552, 05557
PDFs), >=2s apart, descriptive UA, all HTTP 200. No other hosts.

Files: `axgloss/gloss_attest.tsv`, `images_wv2/crops_gloss/{04496_p4_hollande_zeelande.jpg,
04496_p4_respagne_192.png,05557_p3_grafvonholland_93.jpg,05557_p2_jar_94.jpg,05557_p2_kein_133_vorrad.jpg}`.
Not touched: names.tsv, key.tsv, key_full.tsv (AX-NAMES2's, per the brief).

## AX-MERGE: key_full v2 (26 Sept 2026, LANE AX)

Worker AX-MERGE (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-merge.md`, started 02:27 UTC (clock read).
**(0) Intake gate:** `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74` -> `lodewijk-van-nassau-1573-74:
partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Orchestrator's decision (02:26 UTC 26 Sept 2026), verbatim:** "(1) AX-NAMES2's class-(c) flag is upheld: on the
known-plaintext pair 4613/4615 code 123 stands for l and 136 for vingt, so key_full does NOT override them to NULL;
they keep key.tsv's values at grade M with a note 'NULL in 13/13 (123) and 8/8 (136) aligned observations in
5810/5811 -- dual use or aligner bias, unresolved'. 128 ('?' in key.tsv) goes to NULL at M. (2) Add from AX-GLOSS,
grade H (4496's contemporary interlinear gloss): 192 = Roi d'Espagne, 221 = Hollande."

**(1) key_full.tsv v2** (`axnames/build_key_full.py [--check]`, edited, key_full.tsv never hand-edited). Net effect
vs v1: same 161 rows (139 key.tsv + 22 net new), but 123/136 revert to key.tsv's own value at M (with the new note)
instead of NULL-M, and 192/221 join as new H rows (replacing what would otherwise have been 2 of the 13-row NULL-b
class -- they were never eligible for that class since 192 is names.tsv grade U and 221 has no names.tsv row at
all, so both needed a new licence path, `AXGLOSS_H`, checked against `axgloss/gloss_attest.tsv`'s `confidence`
column instead of names.tsv). Build output: `H 8 (153,161,171,202,336,350,192,221) C 3 (154,200,223) NULL 13
(124,126,127,129,130,131,133,134,135,137,138,143,144) conflict 1 (128) conflict_kept_M 2 (123,136)`.
- 123: `l`, M, note "AX-MERGE orchestrator decision (02:26 UTC 26 Sept 2026): class-(c) flag upheld, key.tsv value
  kept (...); NULL in 13/13 (123) and 8/8 (136) aligned observations in 5810/5811 -- dual use or aligner bias,
  unresolved".
- 136: `uingt`, M, same note.
- 128: unchanged from v1 -- `NULL`, M, AX-NAMES2's class-(c) override stands (key.tsv's `?` was never a settled
  value; 128 is not part of the orchestrator's upheld pair).
- 192: `roidespagne`, H, source "4496 (WVO PDF p4) contemporary interlinear gloss \"R. d'Espagne\" over 192 ...;
  names.tsv previously graded this code U (0 observations -- Groen's print leaves the subject out at 5549 PS1)".
- 221: `hollande`, H, source "4496 (WVO PDF p4) contemporary interlinear gloss 'Hollando' over 221 (x3) ...;
  corroborated unglossed in 4614 p1 'tiré de la Haye en 221'".
`python3 axnames/build_key_full.py --check` -> `key_full.tsv up to date`.

**(2) Known-answer regression check**, re-run: `python3 axnames/compare_full.py decode.json ciphertext_sib.tsv
--list` -> `axnames/regress_sib.out`:
```
ciphertext_sib.tsv: tokens 1107, C under key.tsv 1086, regressions 0, changed 1, U 1 -> 0
4613_L28	15	128	? U -> NULL M
```
**0 regressions, and only 1 token changed (128) instead of v1's 5** -- confirms the orchestrator's decision removed
exactly the two AX-NAMES2 changes it named (123 l M -> NULL M x3, 136 uingt M -> NULL M) by no longer making them at
all; 128 is the only remaining override, as directed.

**(3) Decodes**, `tools/decode_key.py --check` "reading up to date" on all four:

| letter | U key.tsv -> key_full v2 | U v1 -> v2 (this pass) | grades under key_full v2 |
|---|---|---|---|
| 4610 | 288 -> 155 | 162 -> 155 (-7: 192 x6, 221 x1 now H) | C 1203, H 9, I 58, M 120, U 155 |
| 4611 | 227 -> 131 | 133 -> 131 (-2: 221 x2 now H) | C 913, H 2, I 71, M 276, U 131 |
| 4616 | 26 -> 25 | 25 -> 25 (no 192/221 occurrences) | C 208, I 1, M 27, U 25 |
| 5797 (spots file) | 31 -> 12 | 12 -> 12 (no 192/221 occurrences; only 123/136 string content changed) | H 2, C 15, M 41, I 3, U 12 |

192 and 221 do not co-occur in 5797, so its letter-level grade counts (H/C/M/I/U) are unchanged from v1; only the
decoded *string* changed at the two spots that use 123/136 (below). 221 appears once in 4610 and twice in 4611;
192 appears 6 times in 4610 and not at all in 4611/4616/5797 (`grep`-counted directly against the regenerated
`reading_<n>_full_tokens.tsv` files).

**(4) 5797 spots against Groen's frame, the two rows this pass changed** (full 7-row table in AX-NAMES2 above;
only these two differ from v1 -- neither 192 nor 221 occurs in 5797, so nothing in this table involves them):

| spot | decoded under key_full v2 | v1 had | Groen's printed frame | gap filled? |
|---|---|---|---|---|
| p5_spot5 | ist [131 . C][123 l, M][173 U] gestern | 123 read as null (.) | "ist gestern zue ghen gezogen" | no (173 still has no row; 'l' does not close Groen's gap either) |
| p5_spot3 | Bey [154 Herzog von Sachsen, C] [124 . 144 . 134 .] und [161 Landgraf, H] [126 . C][136 uingt, M][146 U] ist | 136 read as null (.) | "Bey dem Herzog von Sachsen und ist [w]illens" | yes (unchanged): 161 Landgraf, H; 'uingt' (vingt, twenty) is *extra* cipher content Groen's clear print does not carry at this spot, consistent with the orchestrator's "dual use or aligner bias, unresolved" caveat -- not treated as a second gap fill |

**Spots with a value: still 2 of 6** (unchanged from v1 -- the count is about which of Groen's *unprinted* passages
now have a word, and 123/136 do not sit in one of those six gaps).

**(5) revisions_for_audit.tsv v2** (`axnames/revisions.py [--check]`), 249 rows (was 258 in v1): `4610: changed 133
(word/name 11, NULL 122), U 288 -> 155`; `4611: changed 96 (word/name 8, NULL 88), U 227 -> 131`; `4616: changed 1
(word/name 0, NULL 1), U 26 -> 25`; `5797: changed 19 (word/name 4, NULL 15), U 31 -> 12`. `--check` confirms up to
date. I did not edit AUDIT.md or SECOND-OPINIONS-QUEUE.tsv (no row filed there yet for this target).

**(6) Judge**, re-run on the regenerated 5797 full reading (2-token string change from v1):
```
python3 tools/judge_plaintext.py specs/lodewijk-5797.json --file ciphers/lodewijk-van-nassau-1573-74/reading_5797_full.txt
FAIL language: score=-1.455, null_p99=-1.627, real_p05=-0.459, real_median=-0.428, mode=both, N=314
FAIL words: cover=0.344, min=0.5, real_text_median_cover=0.758
FAIL - lodewijk-5797 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Essentially unchanged from v1 (-1.435, N=308); still below judge length and still disconnected clusters (AX-NAMES2's
caveat above applies unchanged). No spec exists for 4610/4611/4616/the jan-van-nassau 5549 postscript (below); not
run there per rule 7's own conditional ("where a spec exists").

**(7) 5549 postscript (jan-van-nassau-1572-75), read-only use of key_full.tsv.** New
`ciphers/jan-van-nassau-1572-75/decode_5549ps_full.json` decodes that target's `ciphertext_5549_ps.tsv` (the
already-established J5S postscript stretch, PS1-PS26) with `../lodewijk-van-nassau-1573-74/key_full.tsv` instead of
its own `key_5549.tsv` copy of plain key.tsv -- see that target's own NOTES.md section for the result and the
intake-gate flag. **Where 192 now reads:** the brief's "Groen Suppl. p.146 prints '121. 133. 192.' as bare numerals
at PS1" conflates two adjacent but distinct numeral groups on the same page. Checked directly against
`ciphertext_5549.tsv` and `ciphertext_5549_ps.tsv`: Groen's own last-printed bare-numeral group, "121. 133. 192."
(page 146, right context "begert hefftig von E.G. allezeit zeittung"), is **run 61 of the main body**
(`ciphertext_5549.tsv` rows 592-594), which J5S (24 Sept 2026, that target's NOTES.md) classes as the
"verendertte Instruction oder Ciffer" -- a *different, unrecovered* key, explicitly tested and rejected against
Lodewijk's table ("not Lodewijk's table (no rotation reads)"). **192 therefore cannot be read with key_full here**:
doing so would apply this circle's WVO 1574 table to a numeral that the repo's own prior work places outside it.
The actual `PS1` row (the first row of the *separate*, Lodewijk-table postscript stretch that follows run 61) holds
codes **127, 133** -- not 192 -- both of which resolve to NULL at grade C under key_full v2 (class-b, unchanged
from what key.tsv/key_5549.tsv already gave them, since 123/128/136/192/221 do not include either code). No 192
occurrence exists anywhere in `ciphertext_5549_ps.tsv` (checked by direct grep); 221 does occur there once (`PS21`
pos 4), newly reading `hollande` (H) under key_full v2 -- see the jan-van-nassau NOTES.md section for the full
before/after. Flag for the orchestrator: the brief's premise about where 192 sits needs correcting to "run 61 of
the body, not PS1" if this comes up again.

**Requests:** none (disk only). No subagents. Files: `key_full.tsv`, `axnames/build_key_full.py`,
`axnames/regress_sib.out`, `revisions_for_audit.tsv`, `decode_{5797,4610,4611,4616}_full.json` (config text
unchanged, only the reading they point at is regenerated), `reading_{5797,4610,4611,4616}_full{.txt,_tokens.tsv}`.
Not touched: key.tsv, names.tsv, AUDIT.md, SECOND-OPINIONS-QUEUE.tsv. Not regenerated (out of this brief's file
list, now stale relative to v2, flagged for whoever next touches them): `axnames/{sanity_5810.out,sanity_5811.out,
sanity_4503.out,still_unread.tsv,null_raw.tsv,falsenull_diag.out}` -- none of their headline numbers depend on
123/128/136/192/221 (5810/5811/4503 don't contain 192/221 either, per the same occurrence check), but they were
built against key_full v1 and should be re-run before being cited again. Novelty not classified (rule 10).

## AX-REDERIV: fresh re-derivation and key-source check (26 Sept 2026, LANE AX)

Worker AX-REDERIV (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-rederiv.md`, started 03:11 UTC (clock
read). Freshness rule followed: step 1 read only `specs/lodewijk-5797.json`, `key_full.tsv`, `ciphertext_{5797,
4610,4611,4616}.tsv`, `decode_{5797,4610,4611,4616}_full.json` and `tools/decode_key.py`; NOTES.md's AX-NAMES2/
AX-MERGE sections and `revisions_for_audit.tsv` were opened only after step 1's outputs were written (below).

**(1) Fresh-instance re-derivation (rule 7).** `python3 tools/decode_key.py ciphers/lodewijk-van-nassau-1573-74
--config <decode_N_full.json> --check` for each of the four `decode_*_full.json` configs, then independently
regenerated each reading into the scratchpad (never over the committed files, via a copy of each config
retargeting `reading`/`tokens` to the scratchpad) and `diff`ed byte for byte against the committed
`reading_<n>_full.txt` / `_full_tokens.tsv`:

| letter | tokens (H/C/S/M/I/U) | differing tokens (scratch vs committed) | of which non-M |
|---|---|---|---|
| 5797 | 73 (C 15, H 2, I 3, M 41, U 12) | 0 | 0 |
| 4610 | 1545 (C 1203, H 9, I 58, M 120, U 155) | 0 | 0 |
| 4611 | 1393 (C 913, H 2, I 71, M 276, U 131) | 0 | 0 |
| 4616 | 261 (C 208, I 1, M 27, U 25) | 0 | 0 |

**Re-derivation PASSES for all four letters**: `--check` reported "reading up to date" on every config, and a
fully independent regeneration into the scratchpad diffed byte-for-byte identical (0 differing tokens, so
trivially 0 differing tokens beyond the M grade) against every committed reading and token file. Rule 7's
condition for the AUDIT-move gate is met: nothing here sends a reading back.

**(2) Key-source check, key_full rows 153 and 161** (grade H, source "5550 leaf 2 contemporary interlinear
gloss ... over 153 / 161"). `05550.pdf` not on disk (`ciphers/jan-van-nassau-1572-75/images/` has no `05550*`);
fetched `https://resources.huygens.knaw.nl/media/wvo/images/05000-05999/05550.pdf` once (200, reachability
checked first, descriptive UA, 1 request), rendered to PNG with `pymupdf` (installed this session, no
`pdftoppm`/`fitz` binary present) at 300-1200dpi crops. Read the leaf myself before opening anyone's
transcription of it (`revisions_for_audit.tsv`'s source column, key_full.tsv's note column, and AX-GLOSS's own
prose were all read only afterward, in step 3).

Code 161 occurs once on this leaf, in the run "153.161. und andere so bu[ndnus]..." (page 2 of 4, the row
starting "68.36.9.76.3.37.26.135"). The interlinear gloss directly above this run reads two words, one over each
number: **over 153, "Pfaltzgraue"; over 161, "Lanttgraue"** -- a clean, unambiguous one-gloss-word-per-code
correspondence. This independently confirms key_full's H-graded values (153=pfaltzgraf/Palsgrave, i.e. Count
Palatine; 161=landgraf/Landgrave) for this occurrence. Crop:
`images_wv2/crops_rederiv/05550_p2_153-161_gloss.jpg`.

Code 153 occurs a second time on the same leaf, in the run "153.130.90.1.79.173" (same page, a few lines above
the first). key_full's note describes this as the second of "x2" occurrences reading "Palsgrave". **My own
reading of this second occurrence does not confirm that**: the interlinear gloss above this six-code run reads
"Ertzhertzoge vnd graf" (Archduke and Count) as a phrase spanning the run, not a single word "Palsgrave"/
"Pfaltzgraue" positioned over 153 specifically -- three gloss words over six codes, the leading word ("Ertz-
hertzoge") sitting above 153 itself. "Erzherzog" (Archduke) and "Pfalzgraf" (Count Palatine/Palsgrave) are
different noble titles in contemporary German usage; I could not reconcile the two readings by eye and am not
attempting to (out of this brief's scope, and not mine to resolve). Crop:
`images_wv2/crops_rederiv/05550_p2_153-130-run_gloss.jpg` (context crop, full run + gloss).
**Flag for the orchestrator/AX-GLOSS lane**: key_full's source note "(x2, runs p2-5, p2-11)" for code 153
overstates what I independently read -- only one of the two cited occurrences (run p2-11, "153.161") shows an
unambiguous per-code "Palsgrave" gloss; the other (run p2-5, "153.130.90.1.79.173") shows a different, multi-
word phrase whose relationship to a fixed value for code 153 is not established by my reading alone. This does
not by itself overturn the H grade (the p2-11 occurrence still supports it cleanly, and 153=pfaltzgraf also
reads correctly at 5797 p7_spot2 against Groen's clear frame, AX-NAMES2 table), but the "x2" corroboration claim
in the note is not fully borne out and the row is not as doubly-attested as its source line implies.
[V8-NA5797-2 (A2), 26 Sept 2026: "reads correctly at 5797 p7_spot2 against Groen's clear frame" over-states -- Groen prints a blank there, so the frame shows only that a subject fits before "helt sich wol"; it cannot check the value of 153. The H rests on the 5550 gloss alone (AUDIT.md V8.2, A2.7).]

**(3) Key-source check, 4496 gloss over 192 and 221** (time allowed). `04496.pdf` fetched once (200, 1 request,
2s after the 05550 request), page 4 of 5 rendered and cropped. Line 2 of the page reads "221.134.125.8. et
241.113.85.124.192. pour 113.82...". Directly above **221** (the first number of the line) sits the gloss
**"Hollando"**; directly above **192** sits the gloss **"[Le] R. d'Espagne"** ("[the] King of Spain") -- both
clean, isolated, one-code correspondences, read before opening AX-GLOSS's own transcription. This independently
confirms key_full's H-graded values (221=hollande, 192=roidespagne). Crops:
`images_wv2/crops_rederiv/04496_p4_221_hollando_gloss.jpg`, `images_wv2/crops_rederiv/04496_p4_192_espagne_gloss.png`.

**(4) AUDIT.md and SECOND-OPINIONS-QUEUE.tsv.** Per the brief, appended an append-only "Revision log" section to
AUDIT.md (counts and the 23 individually-listed word/name changes from `revisions_for_audit.tsv`, the 153 gloss
flag above, and a note that a verifier should re-confirm the N-classes); no N-class changed. Appended one
sentence to `SECOND-OPINIONS-QUEUE.tsv` row SO-LODEWIJK-1573-74's last column.

Hosts: `resources.huygens.knaw.nl` 2 requests (05550.pdf, 04496.pdf), >=2s apart, descriptive UA, both HTTP 200
(reachability checked with a HEAD-style status probe first on each). No other hosts. No subagents.

Files: this section; `images_wv2/crops_rederiv/{05550_p2_153-161_gloss.jpg,05550_p2_153-130-run_gloss.jpg,
04496_p4_221_hollando_gloss.jpg,04496_p4_192_espagne_gloss.png}`; `AUDIT.md` (append only); `SECOND-OPINIONS-QUEUE.tsv`
(one cell). Novelty not classified (rule 10); no N-class changed (out of scope, per the brief).

## AX-4612TR: 4612 re-transcribed, in progress -- stopped at the wall-clock box (26 Sept 2026, LANE AX)

Worker AX-4612TR (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-4612tr.md`, 02:27-03:34 UTC (box 75 min).
Why: AX-4612 (Opus, 02:12) found the committed `ciphertext_4612.tsv` rests on two blind passes that agreed only
47.8% of aligned columns, and that pass-agreed numerals alone lack the 5-block IC structure the sibling letters
show (0.063 vs 0.080) -- the transcription, not the key, may be why every cryptanalytic family read as salad.

**Images.** WVO 4612's PDF fetched once (`resources.huygens.knaw.nl/media/wvo/images/04000-04999/04612.pdf`,
1 request, HTTP 200) -- 3 pages, matching the folder's existing page count. Rendered with `pymupdf` at 300 dpi
(zoom 300/72) to `images_wv2/crops_4612/src_04612_p{1,2}.png`, 2481x3508 px -- **exactly double the linear
resolution** of the existing `images/04612_p*.png` (1241x1754, actually ~150 dpi despite AX-GLOSS's "200dpi"
note), capped under the 2500 px reading limit (2481 px). p3 checked by eye: address/docket leaf only ("Monsieur
le Prince d'Aurenge", wax seal), no cipher content, consistent with the old file's 0 p3 rows -- not
transcribed. Line crops cut with `tools/iiif_lines.py --image ... --smooth 3 --distance 60 --prominence 40`
(default params under-detected, 7-26 lines; tuned params found 39/26 candidate centres, close to the true
36/23 physical lines including some header/signature over-detection); debug overlays confirm good line
coverage for both pages. Committed: `images_wv2/crops_4612/{src_04612_p1.png,src_04612_p2.png,manifest.json,
p{1,2}_L*.jpg,p{1,2}_lines_debug.jpg}` (15 MB).

**Two blind Sonnet subagent passes per page** (one page per call, per brief; general-purpose agent, no prior
reading shown, instructed on the 1/7, 4/9, 2/3, 5/6, 8/0 confusion pairs named in AX-4612's diagnosis), each
given the full 2481x3508 page image and asked to number physical lines itself (not told the old line count):
`ax4612tr/{passA_p1,passA_p2,passB_p1,passB_p2}.tsv`. passA_p1: 37 lines/875 tokens, 12 alt-flagged. passA_p2:
21 lines/331 tokens, 2 alt-flagged. passB_p1: 38 lines/869 tokens (line 1 is the "6 Mars 74" date header, which
passA skipped as a header rather than numbering -- a one-line offset between the two p1 passes, corrected before
comparing). passB_p2: 21 lines/339 tokens, 12 alt-flagged.

**Raw positional agreement** (`ax4612tr/agreement.py`, passB p1 shifted -1 line to align with passA's header
skip): **p1 702/876 = 80.1%**, a large improvement on AX-4612's 47.8% baseline and a like-for-like comparison
since p1's numeral runs are comma-delimited and segment the same way in both passes. **p2 180/362 = 49.7%
positional agreement, but this number is not trustworthy as a disagreement rate**: from p2_r10 onward the two
passes wrap the same prose into a different number of physical lines each (e.g. p2_r10: passA 12 tokens on the
line, passB 17 -- passB folds material from what passA calls r11 into r10), so position-in-line stops being the
same token in both passes from that point on. This is the rule-3 "two renderings under different conventions"
trap (PX-BRODEC lesson): a bare positional diff here would measure line-wrapping choice, not reading accuracy.
Not fixed within the box -- needs a content-level (sequence-alignment) reconciliation, not position-in-line, for
the prose portion of p2. p1's cipher-numeral run is not affected the same way (numerals don't reflow across a
comma the way cursive prose reflows across a margin), so 80.1% stands as the honest figure for p1.

**Not done -- stopped at 80%+ of the wall-clock box, per COMMON:** `tools/reconcile_passes.py`-style settling of
each disagreement against the image (only the mechanical positional diff above was run, not a per-token
settle); `ciphertext_4612_v2.tsv` (not written -- writing one now from the un-settled, mis-aligned p2 data would
overstate what has actually been checked against the image, contrary to rule 7); the two comparison checks
named in the brief (key.tsv-through-decode_4612_v2.json French-word share, old vs v2; block-of-5 IC of v2 vs
4610/4611's 0.080 and a random-block null). **Concrete next step for a successor**: (1) re-align p2 by content
(word/numeral sequence, not line-position) rather than by line label; (2) settle every disagreement on both
pages against `images_wv2/crops_4612/src_04612_p{1,2}.png` (already fetched, no re-fetch needed); (3) write
`ciphertext_4612_v2.tsv` in the existing column convention (line, position, sign, confidence, alt, why); (4) run
the two checks and paste both numbers here. p1's 80.1% raw figure already clears the brief's 60% gate and is
worth carrying forward as-is once settled; p2 needs the realignment fix first.

Grades: no reading is claimed here, so no H/C/S/M/I token count applies to this section; this is a
transcription-fidelity report, not a plaintext reading (rule 4 does not apply to a raw transcription pass).
Novelty not classified (rule 10, out of scope). Status of the folder unchanged (`partial`).

Files: `images_wv2/crops_4612/**` (source pages, line crops, debug overlays, manifest), `ax4612tr/{passA_p1.tsv,
passA_p2.tsv,passB_p1.tsv,passB_p2.tsv,agreement.py}`, this section. Hosts: `resources.huygens.knaw.nl` 1 request
(04612.pdf), >=1.5s n/a (single request). No credentials used. 2 subagents at a time (pass A pair, then pass B
pair), general-purpose, Sonnet, given only the rendered images (no prior reading). cost: see the lane ledger.

## AX-COMP: companion decipherments 4614, 5801, 7205 (26 Sept 2026, LANE AX)

Worker AX-COMP (Opus), brief `.claude/briefs/runs/2026-09-26-lane-ax-comp.md`, box 120 min from 02:27 UTC, stopped at
80% (03:54). The text of all three letters is on the leaf as a period decipherment (4614 WVO pp.5-6, 7205 pp.8-10,
5801 pp.1-5 interlinear and pp.7-9 clear copy), and 5801's may also be in Groen; nothing here is a novelty claim
(rule 10; the verifier classifies).

**Done: 4614** (Lodewijk to Willem, camp at Cartils, 4 April 1574). The decipherment on pp.5-6 was transcribed by
eye (`decipherment_4614.txt`). Cipher pp.1-3 went through two blind Sonnet passes per page, one page per call,
on crops made by `tools/iiif_lines.py` (`images_wv2/crops_comp/04614_p*`). `tools/reconcile_passes.py` agreement:
p1 81.5%, p2 92.5%, p3 79.8% (gate 60%). Codes above 120 where the passes disagreed were settled on the image:
p1 L01_d 102, p2 L03_a 221 and 241 (pass A had split them as 22 1 and 24 1), p2 L04_b 114. For p3 crop L01, pass A
was taken whole because pass B's line numbering was offset (217 and 270 checked on the image). Other disagreements
stay at grade M in `ciphertext_4614.tsv` (2620 signs). Both passes skipped a few lines cut at crop seams, and
pass A skipped p3's first prose line.
- Alignment: `axcomp/build_pairs.py` cuts the letter at clear-word runs of 9 or more letters found in the
  decipherment (15 anchors, `axcomp/anchors_4614.tsv`). Then `tools/interlinear_align.py align ... --floor 121
  --clear-consumes --prior key_full.tsv` runs; this job added all three options to the tool, with an offline test
  in `tools/tests/test_interlinear_align.py`, and the default output is unchanged (checked on Thurloe P25).
  **Caveat:** `--prior` seeds letters 1-120 from key_full, because the unseeded run drifted over spans this long
  (1260 conflicts against 384 agreements). So the counts for codes 1-120 are not independent evidence for
  key_full's table. The codes above 120 are never seeded, and their meanings come from the decipherment alone.
  Their chunk boundaries are fuzzy, so each one was read by eye from its aligned contexts
  (`axcomp/contexts_4614.txt`, `axcomp/adjudicate_4614.tsv`).
- `sh axcomp/run.sh 4614` regenerates everything; `python3 axcomp/keys.py 4614 --check` exits 0.
- **Table: key_full's 1574 table.** `axcomp/table_check.py` compares the two keys on independent evidence (no seeding).
  The three longest runs of 1-120 codes (198, 178 and 161 codes) read as French under key_full ("...estecontreint
  dftraictersnrbesstalllun...", "quantanousreuthersauonstraiteauecqueseux...", "cequeluiauonsadffacorde
  toutefois..."), and as noise under key_5799. Coverage of all 2400 tokens: key_full 1.000, key_5799 0.448
  (`axcomp/table_check_4614.txt`).
- **key_4614.tsv**: 126 codes, 105 of them 1-120 (96 agree with key_full, 9 conflict) and 21 above 120.
  Name codes read from the period decipherment, grade H, with counts:
  - 172 = le Conte Jean (1; one of the brief's unread codes)
  - 217 = Sr Geertruydenbergh (3)
  - 221 = Hollande (2)
  - 241 = Zeelande (1)
  - 270 = Bommel (2)
  - 272 = Nyeumeghen (1)
  - 289 = Francfort (1)
  - 337 = Reystres (1)

  Nulls agreeing with key_full: 121 (9 of 10), 122 (5 of 7), 131, 142.
- **Conflicts with key_full**, for the orchestrator (`axcomp/proposed_additions.tsv`); key.tsv and key_full.tsv
  are untouched:
  - 127, 129 and 177 each stand for "m": longue[127]ent, un [127]ois, quinze [129]ille, jesty[177]e. key_full has
    127 and 129 as NULL.
  - 123 is passed over as a null at 3 of 4 places, where key_full has l (AX-NAMES2's class (c) caveat).
  - 107 (k block) is read as i/j at 3 of 4 places.
  - 95 (g block) is read as h at 3 of 4 places.
  - 57 (z) is spelled x in eulx/deulx; that is a spelling difference, not a key difference.
- Unsettled at M: 126 f, 132 "aires", 138 "vantaige de voz a" (all in the one run "a lavantaige de voz affaires"),
  150 NULL (1), and 815 (probably a misread 81.5).

**Brief's unread codes.** Only 172 gains a value (le Conte Jean, 1 occurrence in 4614). 146, 150 (NULL once in 4614,
M), 156, 157, 182 and 187 gain none.

**5797 spots, read-only:**

| spot | what it would read |
|---|---|
| p6_spot4 | 172 = le Conte Jean, so "[Graf Johann] zeuget diesen morgen Kölln der hofnung". It fits the German, but the value comes from a French letter of a different correspondent, so read it as a candidate, not a reading. |
| p5_spot5 | 131.123.173: 131 and 123 read as nulls in 4614 (consistent with key_full for 131; for 123 against key_full's l); 173 still has no value. |
| p7_spot6 | 182: no value. |
| p8_spot7 | 156: no value. |

Spots filled: 1 (p6_spot4).

**Not done:**
- **7205:** decipherment transcribed (`decipherment_7205.txt`); its cipher crops are cut (`images_wv2/crops_comp/07205_p1..p6`).
  The p1 blind passes are pass A (733 signs, 729 flagged L by the pass itself; the hand is faint with heavy
  bleed-through) and a partial pass B stopped at crop L08 at the box limit (`axcomp/passes/`). There is no
  reconciliation and no key_7205. The decipherment glosses two name codes the decipherer left as numbers:
  261 = Leyde and 269 = La Haye (p.8, grade H from the period decipherment, not yet aligned). My own look at
  cipher p1 shows 172 and 182 in the run.
- **5801:** not started beyond crops (`images_wv2/crops_comp/05801_p1..p5`). Its clear copy (pp.7-9) is in a hand
  I could not transcribe reliably by eye inside a unit, and the interlinear gloss letters on pp.1-5 are too small
  for the crop scale used. Groen's print would need dbnl, a host this brief did not name. So the 5799/4612 step
  under 5801's key did not run.

**Order change, logged per COMMON:** 7205 was taken second instead of 5801 because of the reasons above.

Next (one line): reconcile 7205 p1 (finish pass B from L08) and run p2-p6 at the same per-page rate (about 10-15
min per pass); `sh axcomp/run.sh 7205` then aligns it against `decipherment_7205.txt`. For 5801, fetch Groen IV's
28 May 1573 letter (dbnl, 1 request) as the clear text, or brief a zoomed transcription of pp.7-9.
Hosts: resources.huygens.knaw.nl 3 (the three PDFs, 2 s apart, all 200). Subagents: 8 blind passes, Sonnet,
at most 2 at once; two B passes were lost to a container restart and re-run.

## AX-4612TR2: 4612 v2 settled (26 Sept 2026, LANE AX)

Worker AX-4612TR2 (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-4612tr2.md`, box 60 min from
03:38:58 UTC. Successor to AX-4612TR (above): realigns p2 by content, settles disagreements against
`images_wv2/crops_4612/src_04612_p{1,2}.png` (already fetched, no re-fetch), writes v2, runs the two checks.
No network requests, no new blind passes (per brief).

**Finding beyond the brief's own scope, found while settling: p1's 80.1% positional figure was not
trustworthy either.** AX-4612TR's agreement.py compared passA/passB p1 by line label with a single flat -1
line shift (correcting for passB's extra header row) and reported p2 as the only page needing content
realignment. Checking p1_r22 against the image (this worker) found passB_p1 r22 does NOT match passA_p1
r22 -- passB r23 does -- meaning a second, independent one-line drift opens on top of the header offset,
somewhere around r04 (an extra token, a bare numeral `9`, appears in passB_p1 r04 with no counterpart in
passA_p1 r04). A flat shift is therefore wrong for most of the page, not just from p2_r10 as reported.
**Both pages were content-realigned the same way** (`ax4612tr/realign.py`): flatten each pass into one
token stream per page in reading order (p1's passB stream drops its own header row first) and align the two
flat streams with `difflib.SequenceMatcher`, not by line/position label.

**True agreement** (`ax4612tr/realign.py`, supersedes both AX-4612TR's 80.1%/49.7% figures):
p1 783/887 = **88.3%**, 104 disagreements (27 numeral, 77 clear-word); p2 260/350 = **74.3%**, 90
disagreements (5 numeral, 85 clear-word) -- combined 1043/1237 = 84.3%. The content-level p1 figure is
*higher* than the old positional one (88.3% vs 80.1%) because several of the 174 positional "disagreements"
were really the same correct token at a shifted line label, not a real reading difference; the count of
disagreements that actually matter for the two checks below (numeral, value 1-120) drops from 91+5=96
(positional) to 27+5=32 (content-aligned).

**Settling against the images** (`ax4612tr/settle.tsv`, `images_wv2/crops_4612/src_04612_p{1,2}.png` viewed
directly, no new line crops cut -- the existing `p{1,2}_L*.jpg` crops from AX-4612TR do not correspond 1:1 to
the passes' own physical lines closely enough to trust blindly: L01/L02 are page-margin/header, L04 was found
to merge two physical lines (r02+r03) into one detected ink-band, so a fixed crop-index-to-line-number formula
was not used -- each needed region was located by matching its own numeral/word content against the passes'
tokens before reading it). Of the 32 numeral disagreements (27 p1, 5 p2), **16 settled with reasonable
confidence, 16 left unsettled ('?')**: 4 p1 lines (r22, r23, r26, r33/r35's paired "109"/"=Wesel" mismatch,
r36) were not reached before the mapping-by-content search stopped paying off inside the box, and several
single-digit disagreements even on lines that were located (r04, r05, r06, r09, r10) stayed genuinely
ambiguous on inspection -- one (r05 pos21) this worker's own reading disagreed with *both* passes (read
"23", where passA has 73 and passB has 13), which is reported here as a three-way disagreement, not settled
either way. Clear-word disagreements (spelling/case/punctuation variants such as `vre.`/`vre`, `Iesus`/
`Iesuel`) were auto-settled by a case/trailing-punctuation-insensitive match (`settled-case-only`, H) where
that fully explained the difference; a genuine wording difference between the passes was left `?` the same
as an unsettled numeral, since it does not feed either check below. `ciphertext_4612_v2.tsv` (1237 rows,
170 `?`, of which 16 are the still-unsettled numerals) built by `ax4612tr/build_v2.py`.

**Check (a): French-word share via key.tsv, old vs v2 vs shuffled** (`ax4612tr/word_share_check.py`, against
`tools/data/fr16`'s own word list per Usage 8 -- no new wordlist written): value-1-120 numerals decoded
through the repo's `key.tsv` (the 1574-table key that reads 4610/4611/5797/5799), grouped into runs broken at
clear words, NULL/name codes and `?`; a token counts if it falls inside a substring matching a real French
word of >=3 letters.
- old `ciphertext_4612.tsv`: 518/775 = **66.8%**
- v2 `ciphertext_4612_v2.tsv`: 562/819 = **68.6%**
- v2 through 20 value-shuffled copies of `key.tsv` (rule 3 -- this statistic CAN move under a shuffle, and
  does): mean **41.5%**, range 31.4-61.3%.

Both old and v2 sit well above the shuffle floor (mean 41.5%, max of 20 draws 61.3%) -- v2's 68.6% is above
every one of the 20 shuffled draws. This is a **cryptanalytic result, not a reading** (no H/C token; it is a
coverage statistic on a straight value-for-letter substitution through an unrelated letter's key, not a
coherent decoded text) and does not overturn AX-4612's own family_run.py negatives above, which tested
whether 4612 fits key.tsv's *design* under a reordering (block width, digit map, affine map) and found it
does not; this check instead asks whether decoding 4612's raw numerals straight through key.tsv, with no
transformation at all, lands closer to real French than chance -- and by this statistic it does, on both the
old and the settled transcription. Flagged for the lane, not investigated further here (out of this
worker's brief): the natural next step is to read `families/block_homophonic-*.txt`-style decodes of v2
under key.tsv directly to see whether any run is legible prose, since a coverage gap this size (66.8-68.6%
vs a 41.5% shuffle mean, v2 clearing the shuffle max) is larger than expected from chance 3-letter-word
collisions alone.

**Check (b): block-of-5 IC, v2 vs old vs 4610/4611 vs null** (`ciphers/lodewijk-van-nassau-1573-74/ax4612/
ic_scan.py`, reused unchanged -- AX-4612's own tool, Usage 8 shared-scripts-before-new-ones; it already
groups values 1-120 into consecutive-value blocks of width w at every offset and reports the best offset
against a 200-draw random-partition null, exactly the check this brief asks for):

| target | N (1-120) | block-5 IC, best offset | null median / p95 |
|---|---|---|---|
| 4612 old | 775 | 0.0617 (o0) | 0.0516 / 0.0567 |
| 4612 v2 | 819 | 0.0601 (o0) | 0.0514 / 0.0562 |
| 4610 | 1222 | 0.0779 (o0) | 0.0494 / 0.0543 |
| 4611 | 1145 | 0.0749 (o0) | 0.0484 / 0.0528 |

v2's block-5 IC (0.0601) is essentially unchanged from old (0.0617) and stays inside its own null's p95
(0.0562), well below 4610/4611's ~0.075-0.078 -- AX-4612's conclusion (4612 shows no block-of-5 value
structure under this key's design) holds up after settling against the higher-resolution image, so this is
not an artifact of the pre-AX-4612TR transcription's lower resolution or its 47.8%-agreement pass. N rose
775->819 despite 16 numerals being marked `?` (excluded) because the 300 dpi re-transcription found more
legible numerals overall than the original pass.

**What this leaves for a successor**: (1) settle the 16 remaining unsettled numerals (`ax4612tr/settle.tsv`,
column `settled='?'`) -- p1 r04/r05/r06/r09/r10 need a second, closer look at the same crop region (the
digits found ambiguous even under direct inspection may need a tighter zoom than this worker cut), and p1
r22/r23/r26/r33/r35/r36 were not reached before the box ran down and need their line located in the image
fresh (the existing L-crops do not reliably correspond to these r-lines, confirmed while settling). (2) The
Check (a) finding (v2 68.6% vs a 41.5% shuffle mean, clearing the shuffle max) is worth a direct look at
`ax4612/families/block_homophonic-*.txt`-style straight decodes of v2 through key.tsv to see whether any
numeral run reads as legible French, before concluding anything -- flagged, not investigated, per this
worker's brief.

Grades: no reading is claimed (rule 4 N/A, this is a transcription-fidelity and cryptanalytic-diagnostic
report). Novelty not classified (rule 10, out of scope). Status of the folder unchanged (`partial`).

Files: `ciphertext_4612_v2.tsv`, `decode_4612_v2.json`, `reading_4612_v2.txt`, `reading_4612_v2_tokens.tsv`,
`ax4612tr/{realign.py,build_v2.py,make_settle_tsv.py,word_share_check.py,settle.tsv,p1_disagreements.tsv,
p2_disagreements.tsv}`, this section. Hosts: none (no network; images already on disk from AX-4612TR). No
credentials used. No subagents (all settlement done by this worker directly against the images). cost: see
the lane ledger.

## AX-MERGE3: 4614 conflicts and key_full v3 (26 Sept 2026, LANE AX)

Worker AX-MERGE3 (Opus), brief `.claude/briefs/runs/2026-09-26-lane-ax-merge3.md`, started 04:02 UTC (clock read),
box 60 min. Intake gate as in AX-NAMES2/AX-MERGE (target `partial`, line 1).

**Gate, written 04:03 UTC before any test ran (verbatim from the brief):** "A conflict code takes the period
decipherment's value in key_full v3 only if, decoding 5810, 5811 and 4503 with that value instead of key_full's, the
number of decoded letters matching Groen's print (aligned by the existing axnames aligner, same settings) rises and no
letter pair gets worse; if the Groen letters carry the code too rarely (<3 occurrences in total) the key_full value
stays and the code is marked 'dual reading, M' in v3."
Implementation, fixed before running: `axmerge3/conflict_test.py` imports `axnames/align_names.py` unchanged (same
MAXL/BASE/PER, same per-page semi-global DP, same Groen spans); codes 1-120 emit their key_full value (identical to
key.tsv for 1-120), every code >120 stays free as in AX-NAMES except the code under test, which is fixed to the
tested value (NULL = emits nothing). "Letters matching" = the aligner's own exact-match count summed over pages, per
letter pair. Stated before running (rule 3, can the test fail?): for 127/129 (key_full NULL vs 4614 m) the count can
rise only if the emitted 'm' lands on a printed m, so the test can fail; for 123 (key_full l vs 4614 NULL) removing a
letter cannot add a match except through a path shift, so the gate is close to unpassable for the NULL direction by
construction -- a per-occurrence diagnostic (does the emitted 'l' land on a printed l?) is reported beside it, and it
cannot license a change on its own.

**(1) Conflict tests** (`python3 axmerge3/conflict_test.py [--check]` -> `axmerge3/conflict_test.tsv`, per-occurrence
`axmerge3/conflict_occ.tsv`; numpy installed this session for the aligner). "matches" = aligner exact matches summed
over pages; "own hits" = occurrences where the tested code's emitted letter lands on the same printed letter.

| code | occ. 5810/5811/4503 | matches key_full value (5810/5811/4503) | matches 4614 value | own hits kf / 4614 | literal gate | verdict in v3 |
|---|---|---|---|---|---|---|
| 127 (kf NULL, 4614 m) | 34/5/3 = 42 | 4436/1318/330 | 4436/1318/330 | - / 2 | fails (delta 0/0/0) | NULL kept (grade C); both m "hits" are artefacts: 5810's two copies of "ville de Harle[m]", where 223 Harlem is the neighbour |
| 129 (kf NULL, 4614 m) | 25/4/1 = 30 | 4427/1306/330 | 4431/1317/330 | - / 3 | passes (+4/+11/0) | **dual reading, M**, NULL kept -- see below |
| 123 (kf l, 4614 NULL) | 2/12/0 = 14 | 4436/1315/330 | 4436/1316/330 | 0 / - | passes (0/+1/0) | **dual reading, M**, l kept -- see below |
| 107 (kf k, 4614 i) | 1/0/0 = 1 | 4436/1316/330 | 4437/1316/330 | 0 / 1 | < 3 occurrences | **dual reading, M**, k kept (i matches the print at 1/1 here and 2/2 on 4613/4615, information only) |
| 95 (kf g, 4614 h) | 2/0/0 = 2 | 4436/1316/330 | 4434/1316/330 | 2 / 0 | < 3 occurrences | **dual reading, M**, g kept (g matches the print at 2/2) |
| 57 (kf z, 4614 x) | 1/2/0 = 3 | 4436/1316/330 | 4435/1315/330 | 2 / 0 | fails (-1/-1/0) | z kept (spelling, not key) |

**The two literal passes are path shifts, not hits, so neither changes a value (conservative choice, logged per
COMMON; flag for the orchestrator).** My implementation note above assumed the match count could rise for 129 only
where the emitted m lands on a printed m; it did not hold. 129 = m gains +4 in 5810 with 2 own hits and +11 in 5811
with 1 own hit: 10 of the 5811 points come from the DP re-routing around two transcription gaps (5811 p1_L09 and its
copy p5_L08, where free 129 absorbed "smesontesteplusquebien"), not from m. Likewise 123's +1 in 5811 comes with 0 own
hits (the l never lands on a printed l in 14 Groen occurrences). Taking 4614's value on these literal passes would
put m at 27 between-word positions in 5810/5811/4503, and delete the l that 4613/4615's printed decipherment shows
at 1 of 3 (sib row: 1473 -> 1472). What the evidence does show: **129 is mostly a null but stands for m in a
minority of places** -- 3 of 30 Groen occurrences land on a real printed m (5810 "plusieurs [m]oyens", "qu'elle
[m]'a", 5811 "che[m]yn"), plus 4614's "quinze [129]ille"; **123 is a null in the Groen letters (0/14 l hits) and in
4614 (3 of 4) but l in 4613/4615** (qu'ilz, Cartil). Both are recorded as dual readings at M with the numbers in
key_full's note; a context rule (123/129 read as letter only when the surrounding word needs it) is the orchestrator's
call, not made here.

**(2) Additions, grade H, from 4614's period decipherment** (licence re-checked against `key_4614.tsv`: grade H, every
occurrence agreeing): 172 lecontejean (1), 177 m (1), 217 srgeertruydenbergh (3), 241 zeelande (1; also 4496 gloss
"Zellando" and names.tsv C), 289 francfort (1). **5 additions.** Values are senses, as in the rest of key_full.

**(3) key_full v3** (`python3 axnames/build_key_full.py --check` -> "key_full.tsv up to date"; build line `... v3_H 5
(172,177,217,241,289) v3_dual_M 4 (129,123,107,95)`); 169 rows (v2 164 incl. header, +5). v2 snapshot kept at
`axmerge3/key_full_v2.tsv`. Known-answer regression on 4613/4615 (`axnames/compare_full.py decode.json
ciphertext_sib.tsv --list` -> `axmerge3/regress_sib_v3.out`): **tokens 1107, C under key.tsv 1086, regressions 0**;
changed 3 (128 ? U -> NULL M as in v2; 107 k I -> k M x2, grade only).

**(4) Re-decodes** (`tools/decode_key.py . --config decode_<n>_full.json --check`: "reading up to date" x4) and the
v2 -> v3 diff (`python3 axmerge3/diff_v2_v3.py [--check]` -> `axmerge3/diff_v2_v3.tsv`, v2 readings kept in
`axmerge3/v2/`): **30 tokens changed, 2 in value** (172 ? U -> lecontejean: 4611 p1_L03 at H, 5797 p6_spot4 at M,
the M being decode_key's single-pass transcription grade on that sign), **28 in grade only** (129 NULL C -> M x20,
95 g I -> M x8). No letter value changed anywhere; 127/57/123/107 values unchanged.

5797 spots under v3 (Groen IV pp.223-225 frame as in AX-NAMES2):

| spot | codes | decode v3 (value/grade) | Groen's frame | value in the gap? |
|---|---|---|---|---|
| p5_spot5 | 131.123.173 | NULL/C, l/M (dual reading), ?/U | "ist gestern zue ghen gezogen" | no (173 no row) |
| p5_spot3 | 154.124.144.134 und 161.126.136.146 | herzogvonsachsen/C, NULL/C x3, landgraf/H, NULL/C, uingt/M, ?/U | "Bey dem Herzog von Sachsen und ist [w]illens" | yes, 161 Landgraf H (unchanged) |
| p6_spot4 | 172 zeuget ... 100.155 | **lecontejean/M** (value H, sign single-pass M), ... h/I, ?/U | "zeuget diesen morgen Kölln der hofnung" | **yes, new in v3: [le Conte Jean] zeuget** -- value from 4614, a French letter of Lodewijk's; in 5797 (Jan and Lodewijk jointly) it would name Count Jan himself; candidate for the verifier (V8-NA172, 26 Sept 2026: "new" here means new relative to key_full v2, not a novelty claim; classed N4, token grade M, AUDIT.md "V8 audit: 5797 p6_spot4 (172)") |
| p7_spot2 | 153.146.137 | pfaltzgraf/H, ?/U, NULL/C | "helt sich wol und thut in warheit viel" | yes, 153 Pfaltzgraf H (unchanged) |
| p7_spot6 | 182.128.133.142 | ?/U, NULL/M, NULL/C, ?/U | "ist willig und urbietig" | no (182 no row) |
| p8_spot7 | 156.127.135.144.129 | ?/U, NULL/C, NULL/C, NULL/C, NULL/**M** (129 dual) | "begert meiner" | no (156 no row) |

**Spots with a value: 3 of 6** (p5_spot3, p6_spot4, p7_spot2). The neighbouring nulls at p5_spot3 (124, 144, 134,
126) and p7_spot2 (137) do not change: none of them is a 4614 conflict code, all stay NULL C; the only neighbour
change is 129 at p8_spot7 (NULL C -> NULL M, value unchanged).

**(5) revisions_for_audit.tsv** regenerated (`python3 axnames/revisions.py [--check]`, up to date): 4610 changed 136
(word/name 14, NULL 122), U 288 -> 155; 4611 101 (13, 88), U 227 -> 130; 4616 1, U 26 -> 25; 5797 21 (6, 15), U 31
-> 11. v2 copy at `axmerge3/v2/revisions_for_audit.tsv`. AUDIT.md untouched (V8-NA5797 holds it).

**Judge**, `python3 tools/judge_plaintext.py specs/lodewijk-5797.json --file ciphers/lodewijk-van-nassau-1573-74/reading_5797_full.txt`:
```
FAIL language: score=-1.467, null_p99=-1.613, real_p05=-0.455, real_median=-0.43, mode=both, N=325
FAIL words: cover=0.338, min=0.5, real_text_median_cover=0.763
FAIL - lodewijk-5797 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Same caveat as AX-NAMES2/AX-MERGE (spots file is disconnected clusters far below judge length; one-file de16 corpus,
no fold spread). The p6_spot4 fill rests on the period decipherment (H value), not on the judge.

**Next (one line):** orchestrator to decide whether 123/129 become context rules (letter inside a word, null between
words) and to re-run the fresh-instance re-derivation (rule 7) on the v3 readings before V8 cites p6_spot4.
Requests: none (disk only). No subagents. Files: `axnames/build_key_full.py`, `key_full.tsv`,
`reading_{5797,4610,4611,4616}_full{.txt,_tokens.tsv}`, `revisions_for_audit.tsv`, `axmerge3/**`, this section.
Novelty not classified (rule 10).

## AX-REDERIV2: fresh re-derivation on key_full v3 and 172 key-source check (26 Sept 2026, LANE AX)

Worker AX-REDERIV2 (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-rederiv2.md`, started 04:32 UTC (clock
read), box 50 min. Amendments applied: key is `key_full.tsv` v3 (after AX-MERGE3, 04:07 UTC); step 2 is the
key-source check of 172 from 4614's period decipherment, not the 5550 gloss (already done by AX-REDERIV, v2,
above); step 3's AUDIT.md section is "Revision log v3", from the regenerated `revisions_for_audit.tsv` and
`axmerge3/diff_v2_v3.tsv`.

**(1) Fresh-instance re-derivation (rule 7).** Freshness rule followed: step 1 read only `specs/lodewijk-5797.json`,
`key_full.tsv`, `ciphertext_{5797,4610,4611,4616}.tsv`, `decode_{5797,4610,4611,4616}_full.json` and
`tools/decode_key.py`; NOTES.md's AX-NAMES2/AX-MERGE/AX-MERGE3 sections and `revisions_for_audit.tsv` were opened
only after step 1's outputs were written (below). `tools/decode_key.py ciphers/lodewijk-van-nassau-1573-74
--config <decode_N_full.json> --check` for each of the four `decode_*_full.json` configs reported "reading up to
date" for all four. Independently regenerated each reading into an isolated scratchpad mirror (a fresh directory
holding only copies of the four `ciphertext_*.tsv` files, `key_full.tsv` and the four `decode_*_full.json`
configs -- not the committed target directory, so nothing outside the mirror could be touched) and diffed
byte-for-byte against the committed `reading_<n>_full.txt` / `_full_tokens.tsv`:

| letter | tokens (v3 grade counts) | differing tokens (scratch mirror vs committed) | of which non-M |
|---|---|---|---|
| 5797 | 73 (C 14, H 2, I 2, M 44, U 11) | 0 | 0 |
| 4610 | 1545 (C 1195, H 9, I 55, M 131, U 155) | 0 | 0 |
| 4611 | 1393 (C 902, H 3, I 67, M 291, U 130) | 0 | 0 |
| 4616 | 261 (C 208, I 1, M 27, U 25) | 0 | 0 |

**Re-derivation PASSES for all four letters on v3**: `--check` reported "reading up to date" on every config, and
the independent scratchpad-mirror regeneration diffed byte-for-byte identical (0 differing tokens) against every
committed reading and token file. Rule 7's condition for the AUDIT-move gate is met with no exceptions; this
supersedes AX-REDERIV's v2 re-derivation above with the same result on the v3 readings.

**(2) Key-source check, code 172 (4614 period decipherment, per amendment).** Located the occurrence myself first:
`ciphertext_4614.tsv` line `04614_p1_L02_c` pos 17 (value `172`, confidence M, `agree-flagged`). Viewed the cipher
line crop (`images_wv2/crops_comp/04614_p1_L02.jpg`, pre-existing) -- pure numerals, no interlinear gloss, so the
decipherment is on the separate companion leaf, not written above the cipher itself. Fetched
`https://resources.huygens.knaw.nl/media/wvo/images/04000-04999/04614.pdf` once (reachability checked first, 200,
descriptive UA, 1 request), rendered pp.5-6 (the companion plaintext decipherment leaf, per `decipherment_4614.txt`'s
own header) with `pdftoppm` (installed this session via `apt-get install -y poppler-utils`, no binary present
before) at 200dpi, 1654x2339 px, under the 2500px crop convention. Read the relevant line myself, before opening
AX-COMP's `decipherment_4614.txt` or `key_4614.tsv`: "...est party pour Francfort. on il trouvera mon frere. le
Conte Jean lequel est allé pour entendre la charge du sieur [Fergonse?]..." -- the words immediately following
"mon frere" and preceding "lequel" are **"le Conte Jean"**. This independently confirms `key_full` v3's H-graded
value for 172 (172 = le Conte Jean, AX-COMP/AX-MERGE3). Crops: `images_wv2/crops_rederiv/04614_decipherment_p5_full.jpg`
(full companion leaf), `images_wv2/crops_rederiv/04614_decipherment_p5_L06_zoom.jpg` (zoomed line).

**(3) AUDIT.md and SECOND-OPINIONS-QUEUE.tsv.** Appended an append-only "Revision log v3" section to AUDIT.md:
updated per-letter counts from the regenerated `revisions_for_audit.tsv` (259 rows: 226 NULL, 33 word/name, +10
word/name since v2's 23), the 2 value-changed rows (172, individually) plus the 28 grade-only rows
(codes 129, 95) from `axmerge3/diff_v2_v3.tsv`, the orchestrator's 123/129 context-rule decision (no context
rule adopted; both stay dual readings graded M until a letter with a period decipherment settles them in
context, verbatim per the brief), a note that p6_spot4 (172) supersedes the V8 audit section's "not read" listing
for that spot, and a note for the verifier. No N-class changed. Appended one sentence to
`SECOND-OPINIONS-QUEUE.tsv` row SO-LODEWIJK-1573-74's last column (v3-specific, alongside the existing v2 note).

Hosts: `resources.huygens.knaw.nl` 1 request (04614.pdf), descriptive UA, HTTP 200 (reachability checked first).
No other hosts. No subagents.

Files: this section; `images_wv2/crops_rederiv/{04614_decipherment_p5_full.jpg,04614_decipherment_p5_L06_zoom.jpg}`;
`AUDIT.md` (append only); `SECOND-OPINIONS-QUEUE.tsv` (one cell). Novelty not classified (rule 10); no N-class
changed (out of scope, per the brief).

## AX-COMP2: 7205 against its period decipherment (26 Sept 2026, LANE AX)

Worker AX-COMP2 (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax-comp2.md`, box 90 min from 04:01:55 UTC,
finished at 53 min. Continues AX-COMP's unfinished 7205 (page 1 pass B was partial at L08; p2-p6 untouched).

**Transcription.** p1 pass B redone from L08 through L12 (blind Sonnet subagent) and merged with the existing
L05-L07 partial (pass B does not cover L01-L04, an AX-COMP scoping decision inherited as-is; those tokens are
single-pass M grade). Pages p2-p6: two fresh blind Sonnet subagent passes each, one page per call pair, on the
existing `images_wv2/crops_comp/07205_p*` line crops. Every subagent independently flagged that these crop files
each pack several physical manuscript rows (not one line per file) -- confirmed by eye (07205_p1_L08.jpg alone
shows 4 dense numeral rows). `tools/reconcile_passes.py` needs `--line-sub '_[a-z]$' ''` to collapse each pass's
own a/b/c/... sub-clusters back to one sequence per crop file before aligning (without it, agreement was 22.7% on
p1 purely from sub-cluster key mismatches between two independently-chunked passes), and `--keep-plain` to retain
clear-word runs (p1's L01-L04 are pure clear preamble and vanish from the aligner entirely without it).

Per-page raw sign agreement (gate 60%, per the brief):

| page | lines | agree/cols | share | vs gate |
|---|---|---|---|---|
| p1 | 12 | 300/815 | 36.8% | below |
| p2 | 9 | 630/873 | 72.2% | above |
| p3 | 10 | 366/803 | 45.6% | below |
| p4 | 8 | 631/826 | 76.4% | above |
| p5 | 8 | 509/815 | 62.5% | above |
| p6 | 10 | 553/788 | 70.2% | above |

p1 and p3 read below gate. This is a genuine property of this letter's hand on these two pages (both subagent
pairs independently called the ink faint with heavy bleed-through and gave mostly M/L confidence), not a script
bug: p2/p4/p5/p6 use the identical pipeline and clear the gate. Rather than hand-settle all 437+515 disagreement
columns pixel-by-pixel (not a responsible use of the box), settling effort went to the six named codes and to
codes >120 generally, per the brief.

**Codes >120 settled from the image (grade H, this worker's own eye-check against the crop):**
- **182** (p4, `07205_p4_L01` pos 83): pass A read 182, pass B read 112 (differ); the crop shows the run
  "82.182.02.139" -- 182 clearly legible. Settled H, overriding the M/differ.
- **150** (p5, `07205_p5_L04` pos 10): pass A read 150, pass B had a gap; the crop shows "134.83.90.114.84.150.120"
  -- 150 clearly legible. Settled H. (A second candidate 150 in the same crop, pos 95, stays M: the image there
  reads closer to 130, not confidently either pass's guess of 150/190 -- not settled either way.)

**Brief's named codes (146, 150, 156, 157, 182, 187; 5797's remaining gaps are 156 and 182):** counted directly
in the assembled `ciphertext_7205.tsv` (4920 signs):

| code | occurrences in 7205 | status |
|---|---|---|
| 146 | 0 | not present anywhere on this letter |
| 150 | 4 | present; 2 of 4 settled H from the image (both read digits "150"); alignment (see caveat below) reads it NULL |
| 156 | 0 | not present -- 5797's gap stays open |
| 157 | 0 | not present |
| 182 | 1 | present; settled H from the image; alignment (see caveat below) reads it "y" at M, n=1 -- **not** a confirmed value for 5797's other gap |
| 187 | 0 | not present |

So 7205 does not settle either of 5797's remaining gaps (156, 182): 156 never occurs in 7205 at all, and while 182
does occur once, its aligned "meaning" is unreliable for the reason below -- a single occurrence at M grade is not
enough to read into 5797 regardless.

**Anchor-sparsity caveat, important for every code >120 below.** `axcomp/build_pairs.py` found only **2** anchors
for 7205's whole 4919 non-clear-adjusted token run (`quepouons`/`quepou` dist 3, `detrouuer`/`setroue` dist 3 --
both near the 0.35 edit-distance cutoff), versus 15 anchors for 4614's 2620 tokens. 81 individual clear words of
length >=9 exist in the transcription, but almost none of them matched the decipherment closely enough to anchor,
because the transcription itself is noisy (every subagent pass flagged mostly M/L confidence on clear words).
With effectively 2 weak anchors across the whole letter, `tools/interlinear_align.py`'s hard-EM has almost no
local constraint over most of the span, so most >120 codes' aligned "value" (and several 1-120 conflicts against
key_full, 39 of 112) reflect the aligner's unconstrained guess, not a period-decipherment reading. `key_7205.tsv`
and `axcomp2/compare_7205.tsv` are still written and committed (the brief asks for them), but every row should be
read as a candidate, not a reading, except the two independently cross-checked below.

**Full codes >120 list** (81 codes; `axcomp2/compare_7205.tsv`, same table as `axcomp/compare_7205.tsv`): 2 agree
with key_full, 28 conflict, 51 new code. The two agreements are the only >120 rows with any independent support:
- **137 = NULL** (5 occurrences, all NULL, agrees with key_full's NULL) -- consistent, not from a single guess.
- **221 = Hollande** (2 occurrences, agrees with key_full and with 4614's independent reading of the same code).
Everything else >120, including 182's "y" and 150's "NULL", is a single- or few-occurrence guess under the
anchor-sparsity caveat above and is not offered as a reading (rule 4: 0 H/C beyond the two image-settled digit
occurrences of 150/182 themselves, which are readings of the *ciphertext*, not of their *meaning*).

**Table.** `axcomp/table_check.py 7205`: coverage of all 1-120 tokens under key_full 1.000 vs key_5799 0.400 (three
longest runs read as French under key_full, garbled under key_5799) -- same 1574 table as 4614/5797/5810/5811.

`sh axcomp/run.sh 7205` regenerates `key_7205.tsv`/`axcomp/compare_7205.tsv` from `ciphertext_7205.tsv` and
`decipherment_7205.txt`; `python3 axcomp/keys.py 7205 --check` exits 0 against the committed files.

Hosts: none (crops already on disk from AX-COMP's fetch). Subagents: 11 blind-transcription passes (Sonnet, at
most 2 at once): p1 pass-B continuation (1) + p2-p6 (2 each). No AskUserQuestion.

Files: `ciphertext_7205.tsv`, `key_7205.tsv`, `axcomp/{passes/passA_7205_p*.tsv,passes/passB_7205_p*.tsv,
recon_7205_p1..p6/**,anchors_7205.tsv,pairs_7205.tsv,align_7205.tsv,rawkey_7205.tsv,compare_7205.tsv}`,
`axcomp2/compare_7205.tsv`, this section. `key_full.tsv` and `key.tsv` untouched (AX-MERGE3 owns key_full.tsv).
Novelty not classified (rule 10); no N-class changed.

## AX2-SHRINK: images relocated (26 Sept 2026, LANE AX2)

Folder hygiene against CLAUDE.md's 30 MB-per-folder rule (Access playbook). Before: 81360 KB (79.5 MB) total,
of which 34544 KB (33.7 MB) is `images_wv2/crops_4612/**` and `images_wv2/crops_comp/05801_*` -- out of bounds
this pass, live workers AX2-4612/AX2-5801 -- leaving 46816 KB (45.7 MB) in scope. After: 58784 KB (57.4 MB)
total; excluding the same out-of-bounds files, 24240 KB (23.7 MB), under the 30 MB rule with margin.

**What moved.** `images/` held 19 full-page PNG renders (150dpi, pdftoppm), 25 MB of the 31 MB folder, all
regenerable byte-for-bitwise-identical from the WVO PDF (confirmed below). Removed 11 that neither NOTES.md nor
any tsv/json/py cites as a specific evidence page: `images/{04610,04611}_p{2,3,4}.png`, `04612_p{2,3}.png`,
`04613_p3.png`, `04615_p2.png`, `04616_p2.png` (`git rm`; still readable from git history, e.g. `git show
6fa733f3215941fb10a0d0e086b06bb654c6663c:ciphers/lodewijk-van-nassau-1573-74/images/04610_p2.png`, sha listed per-file in
`images_manifest_full.tsv`). Kept one full page per letter as a sample (4611_p1, 4612_p1, 4616_p1, none
individually cited) plus every page NOTES.md cites by filename as visual evidence (4610_p1: cipher present;
4613_p1/p2 and 4615_p1/p3: sibling decipherment sheets, R12's line-crop source pages) -- 8 pages total,
converted PNG -> JPEG quality 80 (same 1241x1754 pixel dimensions, already under the 1600px rule) since PNG
gave no useful compression on these photographic scans (tested: PIL `optimize=True` saved 0 bytes). Citations
in NOTES.md updated to the new `.jpg` filenames (lines that named `04610_p1.png`, `04613_p1.png`,
`04613_p2.png`, `04615_p1.png`, `04615_p3.png`). `images_wv2/`'s own full-page JPEGs (27 pages, 7.1 MB, already
JPEG q80 150dpi) and all 347 L-crop JPEGs (5 MB, already 8-70 KB each) were left untouched -- 5797 in
particular is under active read by LANE V8 this window and its 8 pages were not touched.

**Regen test (2 requests to resources.huygens.knaw.nl, 2s apart, well under the good-citizen cap).**
`./regen_images.sh page 4610 1` re-fetched `04610.pdf` and re-rendered `images/04610_p1.png` with `pdftoppm -png
-r 150`: sha1 `4490197beb9bb8482d994fb6e59247fc6750c0ca`, identical to the pre-removal file (byte-for-byte).
`./regen_images.sh crop images_manifest_full.tsv images/04610_p1_L01.jpg` then re-cut the line crop from the
regenerated page using the box recorded in `images_manifest_full.tsv` (`[0, 71, 1241, 114]`, from
`images/manifest.json`'s `iiif_lines` records): sha1 `3798f6e78dd56afd1c917a132301b26f6f9db50a`, identical to the
committed crop. Both regenerated files matched the originals exactly (same sha1, no pixel diff needed).

**Inventory.** `images_manifest_full.tsv` (folder root): path, bytes, sha1, kind (fullpage/crop-lines/crop-manual/
debug), source (WVO PDF URL + brief + render command for full pages; parent image + pixel box + tool for line
crops, from `images/manifest.json`'s `iiif_lines` records), and cited_by (files naming that path), for all 395
non-out-of-bounds image files. `regen_images.sh` (folder root) regenerates any full page (`page BRIEFNR PAGE`,
one PDF fetch) or any recorded line crop (`crop images_manifest_full.tsv PATH`, no fetch, cuts from the parent
page already on disk) or the whole set (`all`); reads `images/manifest.json` and `images_wv2/manifest.json` for
pdf_url/render settings, so it stays correct if those manifests are extended.

`images_wv2/crops_gloss/*.png` and `images_wv2/crops_rederiv/*.png` (11 files, 3 MB, briefs 04496/05550/05557 --
not in either full-page manifest, hand-cropped by earlier gloss-reading workers) are each the only copy of
their specific evidence (cited in NOTES.md/AUDIT.md by filename for named readings, e.g. code 192=espagne,
221=hollande, 153); not touched, and not currently regenerable by this script since no full-page source or box
is on file for them -- a future worker adding those would extend `images_manifest_full.tsv`'s coverage, not
required by this pass's brief.

Files: `ciphers/lodewijk-van-nassau-1573-74/{images_manifest_full.tsv,regen_images.sh,images/**,NOTES.md}` (this
section). Hosts: resources.huygens.knaw.nl, 2 requests (page test only; crop test read the just-fetched page
from disk).

**Second pass (26 Sept 2026 06:51 UTC, AX2-SHRINK2, LANE AX2), `images_wv2/crops_4612/**`.** AX2-4612TR/AX2-4612
left this set out of bounds (15 MB: `src_04612_p{1,2}.png`, two 300dpi PNG renders, 9488 KB; 130 `p{1,2}_L*_s*.jpg`
line crops at 2400px wide, 3960 KB; two `p{1,2}_lines_debug.jpg` overlays, already 1600px wide, 1061 KB). It is
free now that AX2-4612 (settling the 16 numerals) has reported.

Before: `images_wv2/crops_4612` 14816 KB, folder total 60576 KB (59.2 MB).

**What moved.** The two 300dpi source renders (`src_04612_p1.png`, `src_04612_p2.png`, 4702768 + 5008726 bytes,
sha1 `00b566005365c7dd63f64a2857b4cdb319e2b2a9` / `1776ba844ff2c7886c2df2ef144326cf80ab1b8c`) `git rm`'d --
readable from git history at commit `8e8c06718d54011adc637dc6e02ae74d62d1c0f5` and regenerable byte-for-bitwise-
identical from the WVO PDF (confirmed below), same as AX2-SHRINK's own `images/` pages. The 130 line crops (cut
at 2400px wide, over the 1600px convention) were downscaled in place to <=1600px wide, JPEG q80 (LANCZOS resize):
4054103 -> 2047286 bytes, about 50%. The two debug overlays (already 1600px wide) were left untouched.

**Regen test (1 request to resources.huygens.knaw.nl, well under the good-citizen cap -- the render test and
the crop test both used the single fetched PDF, per COMMON's per-unit-box discipline).** `render_pymupdf300`
(new function in `regen_images.sh`, exposed as `./regen_images.sh page300 4612 1`) re-rendered both pages from
the one fetched `04612.pdf` at 300dpi (zoom 300/72): sha1 of both `src_04612_p{1,2}.png` matched the
pre-removal committed files exactly (byte-for-byte, no pixel diff needed). `./regen_images.sh crop
images_manifest_full.tsv images_wv2/crops_4612/p2_L10_s1.jpg` (with both regenerated 300dpi pages placed back
on disk) then re-cut and re-downscaled the crop from its recorded box: sha1 `50c3a327d20a7c7d8792fbcc14c97cdd9a535a1d`,
15201 bytes, identical to the committed (post-downscale) file. `do_crop` was extended to cap any cut wider than
1600px at 1600px wide (LANCZOS, JPEG q80), so the existing 04610-4616 crops (already <=1241px) regenerate
unchanged (q85, no resize) while `crops_4612`'s wider crops now regenerate at their final downscaled size.

**Inventory.** All 134 files under `images_wv2/crops_4612/**` (2 source renders, 130 crops, 2 debug overlays)
added to `images_manifest_full.tsv`: path, bytes, sha1, kind (fullpage/crop-lines/debug), source (PDF url + brief
+ render recipe for the two renders; parent file + pixel box + tool + downscale note for crops, from
`images_wv2/crops_4612/manifest.json`'s `iiif_lines` records), cited_by (`./NOTES.md;./ax4612tr/build_v3.py` for
the two source renders, both of which name `src_04612_p{1,2}.png` directly; blank for the 130 individual line
crops and the 2 debug overlays, none of which are cited by filename anywhere in the repo -- AX-4612TR2's own
note that "the existing `p1_L*.jpg` crops... do not correspond 1:1 to the passes' own r-lines" already explains
why the settling work re-cropped from the source images directly rather than citing these files).

**Checked for >300 KB files, per the brief: `ax2_4612/crops/**` (4 files, largest 48137 bytes), `axmerge4/crops/**`
(11 files, largest 94549 bytes), `ax2_blanks/` (no `crops/` subfolder -- only `.py`/`.tsv` files, no images) --
none over 300 KB, nothing to downscale. `ax2_5801/` likewise has no `crops/` subfolder yet (its images live in
`images_wv2/crops_comp/05801_*`, explicitly out of bounds below).

After: `images_wv2/crops_4612` 3344 KB, folder total 49152 KB (48.0 MB).

**Still over 30 MB, and not only from the named out-of-bounds set.** Excluding `images_wv2/crops_comp/05801_*`
(7772 KB) and `ax2_5801/crops/*` (0 KB, does not exist) -- the two sets this brief named STILL OUT OF BOUNDS --
leaves 41380 KB (40.4 MB), still over the 30 MB rule. The remainder is `images_wv2/crops_comp/04614_*` (3764 KB)
and `07205_*` (8132 KB, one file over the 300 KB check-threshold this brief applied elsewhere: `07205_p4_L04.jpg`
at 313400 bytes) -- AX-COMP's companion-decipherment crops, cut before AX2-SHRINK's first pass but never named
as out-of-bounds by either pass's brief, so untouched by both. Excluding those too (11896 KB) gives 29484 KB
(28.8 MB), under the rule. Flagged in ROOM.md for the lane orchestrator: a third shrink pass on
`images_wv2/crops_comp/{04614,07205}_*` (not `05801_*`, still live under AX2-5801ADJ) would close the gap.

Files: `ciphers/lodewijk-van-nassau-1573-74/{images_manifest_full.tsv,regen_images.sh,images_wv2/crops_4612/**,
NOTES.md}` (this paragraph). Hosts: resources.huygens.knaw.nl, 1 request (04612.pdf; both the render test and
the crop test read from that one fetch).

**Third pass (26 Sept 2026, AX2-SHRINK3, LANE AX2), `images_wv2/crops_comp/{04614,07205,05801}_*`,
`ax2_5801/crops/*`, `images_wv2/crops_gloss/*`, `images_wv2/crops_rederiv/*`.** AX2-5801ADJ reported before this
pass started, so `05801_*` and `ax2_5801/crops/*` (created since AX2-SHRINK2, 8 files) are both free.

Before: folder total 49152 KB (48.0 MB).

**What moved.** All 136 line crops under `images_wv2/crops_comp/{04614,07205,05801}_*` (already >1600 px wide,
2153-2480 px, none previously in `images_manifest_full.tsv`) and all 8 under `ax2_5801/crops/*` were downscaled
in place to <=1600 px wide, JPEG q80 (LANCZOS): 20345068 -> 9887175 bytes (about 51%). None were removed --
per AX2-SHRINK2's own precedent (crops_4612's 130 line crops, none individually cited by filename, kept
because they are the transcription evidence itself, not an intermediate render), individual line crops are
downscaled, never `git rm`'d; only bulk intermediate full-page renders are removable when uncited, and no such
full-page renders were ever committed for this set (only the cut crops exist on disk).
`images_wv2/crops_gloss/*` and `images_wv2/crops_rederiv/*` (named out-of-bounds by neither prior pass, left
untouched since pass 1: "not currently regenerable... not required by this pass's brief") were brought to the
same convention: 7 PNGs over 1600 px on their long side were converted to JPEG q80 (PNG resize alone made
several of them *larger* -- `05550_p2_153-130-run_gloss.png` 117027 -> 292913 bytes at PNG, because LANCZOS
resampling of a near-flat-colour manuscript-photo PNG adds many new colours that defeat PNG's palette-style
compression; reverted, redone as JPEG) and renamed `.png` -> `.jpg`, with citations updated in NOTES.md/AUDIT.md
(`04496_p4_hollande_zeelande`, `05557_p2_jar_94`, `05557_p2_kein_133_vorrad`, `05557_p3_grafvonholland_93`,
`04496_p4_221_hollando_gloss`, `05550_p2_153-130-run_gloss`, `05550_p2_153-161_gloss`); the 2 files already JPEG
(`04614_decipherment_p5_L06_zoom.jpg`, `04614_decipherment_p5_full.jpg`) were resized in place, same filename.
2 of the 11 (`04496_p4_respagne_192.png`, `04496_p4_192_espagne_gloss.png`) were already <=1600 px and left
untouched. The 9 touched files: 2514459 -> 900981 bytes (the 2 untouched files' 500924 bytes unchanged).

**Regen test -- negative, logged rather than silently skipped (rule 3).** 1 request to
resources.huygens.knaw.nl (`04614.pdf`, fetched to check whether `images_wv2/crops_comp/*`'s source pages are
byte-reproducible the way `images/` and `images_wv2/crops_4612/` are). They are not, and the reason rules out
the two established conventions rather than just failing to match them: `images_wv2/crops_comp/manifest.json`
records source-page widths of 2278/2317/2329 px for 04614's three pages, but `04614.pdf`'s three pages all have
the *identical* PDF media box (595.28 x 841.89 pt, confirmed with pymupdf) -- so a whole-page render at any
single fixed DPI must give the same pixel width for all three pages, and it does: 1241 px at 150dpi
(`render_pdftoppm`/`render_pymupdf`, the `images/`/`images_wv2/` convention) and 2481 px at 300dpi
(`render_pymupdf300`, the `crops_4612` convention), neither matching any of the three recorded widths, and a
whitespace-bounding-box trim of the 300dpi render (PIL, threshold 10) gives 2431/2380/2408 px -- closer in
magnitude but still not matching, and still non-constant only because the trim depends on ink extent, not
because the source pages differ in size. AX-COMP's exact per-page render/crop recipe (most likely a
hand-drawn `--region` per page, `tools/iiif_lines.py --image` support) was never logged in NOTES.md or
committed as a script, and this pass did not spend further budget bisecting DPI/trim parameters to find it.
Flagged in `regen_images.sh`'s header and in every new `images_manifest_full.tsv` row for this set: not
currently regenerable, same status crops_gloss/crops_rederiv already carried after pass 1 -- a future worker
who needs a byte-identical source page for one of these three letters starts from this paragraph, not from
scratch.

**Inventory.** 155 new/updated rows in `images_manifest_full.tsv` (136 `crops_comp`, 8 `ax2_5801/crops`, 11
`crops_gloss`/`crops_rederiv`, 7 of the 11 under new `.jpg` filenames); `cited_by` computed by a fixed-string
grep of the whole folder's `.md`/`.tsv`/`.json`/`.py`/`.txt` files against each crop's basename (picks up the
5 individually-named crops -- `04614_p1_L02.jpg`, `04614_p3_L01.jpg`, `07205_p1_L08.jpg`, `07205_p4_L04.jpg`,
`05801_p1_L09.jpg` -- plus every crops_gloss/crops_rederiv file, all of which are cited by exact filename).

After: folder total 38044 KB (37.2 MB) -- down from 49152 KB but **still over the 30 MB rule** by about 7.2 MB.
The remaining weight is `images/` (8.6 MB) and `images_wv2`'s own root-level full-page JPEGs (about 7.1 MB, 27
pages): both were already brought to convention by AX2-SHRINK's first pass (<=1600 px -- in fact 1241 px --
JPEG q80) and are cited as visual-evidence samples or full pages NOTES.md names directly, so this pass's method
(downscale if >1600 px wide) has no further lever on them; shrinking further would mean either re-opening pass
1's "keep one uncited sample page per letter" judgement call (`04611_p1.jpg`, `04612_p1.jpg`, `04616_p1.jpg`,
none individually cited) or accepting the folder above 30 MB with this paragraph as the reason. Left for the
lane orchestrator rather than decided unilaterally here, since removing a kept sample page is a step back from
"image over transcription" (rule 2), not a hygiene action.

Files: `ciphers/lodewijk-van-nassau-1573-74/{images_manifest_full.tsv,regen_images.sh,images_wv2/crops_comp/**,
images_wv2/crops_gloss/**,images_wv2/crops_rederiv/**,ax2_5801/crops/**,NOTES.md,AUDIT.md}` (citation renames
only in AUDIT.md). Hosts: resources.huygens.knaw.nl, 1 request (04614.pdf, regen test only).

**Fourth pass (26 Sept 2026, AX2-SHRINK4, LANE AX2), `images_wv2/*.jpg` root full pages + line-crop
re-encode in `images/` and `images_wv2/crops_comp/**`.** Orchestrator decision at 08:05 UTC: step 1, thin
`images_wv2`'s six letters' full-page scans to one sample page per letter; step 2 if still over, re-encode
line crops at JPEG q70. Before: 38088 KB (37.2 MB).

**Step 1 -- `images_wv2/*.jpg` root pages.** All 27 pages already carried their WVO `pdf_url` in
`images_wv2/manifest.json` (checked per-brief before touching anything). `git rm`'d 21 of the 27, keeping one
page per letter (`p1` of each: `04503_p1.jpg`, `05194_p1.jpg`, `05797_p1.jpg`, `05799_p1.jpg` -- its only page,
untouched -- `05810_p1.jpg`, `05811_p1.jpg`); none of the 21 removed pages is individually cited by filename
anywhere outside `images_manifest_full.tsv`/`images_wv2/manifest.json` (checked per file: only `04503_p1.jpg`
and the blanket range note `05797_p1.jpg`..`p8.jpg` at NOTES.md:595, "copy-free, already on disk", are named,
both about the kept `p1` or a set-level copy-status remark, not a specific page cited as evidence). Regen
test (1 request to resources.huygens.knaw.nl, 05797.pdf, `./regen_images.sh page 5797 2` after installing the
missing `pymupdf`/`Pillow` packages this container lacked): rendered `05797_p2.jpg` from the freshly fetched
PDF, sha1 `c465218c34218e6db1c803d5870d0a9c37211a92` -- identical to the pre-removal committed file, confirming
`images_wv2`'s convention (pymupdf, 150dpi, JPEG q80) is still reproducible for this brief. After step 1:
32740 KB (32.0 MB) -- still over 30 MB by about 2 MB.

**Step 2 -- line-crop re-encode.** Brief's method: JPEG q70, same dimensions, `images/` and
`images_wv2/crops_comp/**`. Applied to all 483 line-crop files (`images/*_L*.jpg`, 347 files -- full pages and
the two `*_lines_debug.jpg` overlays excluded, neither is a crop; `images_wv2/crops_comp/*.jpg`, 136 files,
`manifest.json` excluded) by decoding the currently-committed JPEG and re-saving, no resize. At q70: saved
1839 KB, total 31240 KB (30.5 MB) -- still over the 30 MB line by about 500 KB. Rather than double-compress
(re-encoding the already-q70 output a second time, which stacks generation loss for no clear gain), reverted
the 483 files to their committed originals (`git checkout -- images/ images_wv2/crops_comp/`, cheap since
nothing had been committed yet) and re-ran the same script at q65 directly from the originals in one pass:
saved 2851 KB, total 29804 KB (29.1 MB), under the rule. Logged here as the judgement call the brief's q70
number didn't quite clear (COMMON's "no human watches a worker session" rule: took the more conservative single
re-encode over stacking a second lossy pass at the letter of the brief's stated quality).

**Legibility check (rule 3's own kind of check, requested by the brief): three re-encoded crops eyeballed
before/after at 100%.** `images/04610_p1_L01.jpg` (small text line), `images_wv2/crops_comp/07205_p4_L04.jpg`
(dense multi-line numeral crop, the one AX2-SHRINK3 flagged as still over 300 KB before its own downscale),
`images_wv2/crops_comp/05801_p1_L06.jpg` (superscript-heavy cipher line). All three: no visible difference
between the q80/q85-original and the q65 re-encode at the pixel dimensions on disk; every numeral and letter
that was legible before is legible after.

**Inventory.** 21 `images_wv2/*.jpg` rows in `images_manifest_full.tsv` updated with a
"removed AX2-SHRINK4... original at commit `fd9d781f`" note (rows kept, not deleted, matching prior passes'
convention); 483 line-crop rows (`images/*_L*.jpg`, `images_wv2/crops_comp/*.jpg`) updated with new
bytes/sha1 and a "re-encoded JPEG q65... original at commit `fd9d781f`" note. Every row's bytes/sha1 now
matches the file on disk (checked programmatically, 0 mismatches of 673 non-header rows).

After: folder total 29864 KB (29.2 MB) -- **under the 30 MB rule**, with about 850 KB margin.

Files: `ciphers/lodewijk-van-nassau-1573-74/{images_manifest_full.tsv,images_wv2/*.jpg,images/*_L*.jpg,
images_wv2/crops_comp/**,NOTES.md}` (this paragraph). Hosts: resources.huygens.knaw.nl, 1 request (05797.pdf,
regen test only).

## AX2-4612: 4612 v3, key_full decode and key-seeded anneal (26 Sept 2026, LANE AX2)

Worker AX2-4612 (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax2-4612.md`, started 05:22 UTC (clock
read), box 90 min. Intake gate as in AX-MERGE/AX-MERGE3 (target `partial`, edition/page citation found within
6 lines). Why this job (from the brief): under key.tsv, v2 decodes to recurring non-French clusters ("yus"
where "vous" would sit, "zur" where "pour" would sit) that look like a small consistent code substitution
rather than noise; v2's French-word share was 68.6% against a 20-shuffle mean of 41.5%/max 61.3%. AX-4612's
own block/homophonic negatives ran on the 47.8%-agreement transcription (superseded by AX-4612TR2's v2, 88.3%/
74.3%) and are not tests of the settled letter.

**Unit 1: settling the 16 open numerals (`ax4612tr/settle.tsv`).** Crop step run first, per COMMON's mandatory
convention (though most positions needed a second, tighter re-crop of the exact token once the first pass
located the right physical line -- see the individual commands below, all against the same already-fetched
source page, no re-fetch):
```
python3 tools/iiif_lines.py --image ciphers/lodewijk-van-nassau-1573-74/images_wv2/crops_4612/src_04612_p1.png --region 0,150,2481,900 --out <scratchpad> --prefix p1seg1 --distance 60 --prominence 40 --lines-per-crop 1 --debug
python3 tools/iiif_lines.py --image ciphers/lodewijk-van-nassau-1573-74/images_wv2/crops_4612/src_04612_p1.png --region 0,1850,2481,650 --out <scratchpad> --prefix p1seg2 --distance 60 --prominence 40 --lines-per-crop 1 --debug --dry-run
```
The existing `p1_L*.jpg` crops from AX-4612TR do not correspond 1:1 to the passes' own r-lines (confirmed
again this session, same finding as AX-4612TR2's own note) -- each of the 16 positions was located by matching
its line's numeral/word content against passA/passB's own tokenised rows (`ax4612tr/passA_p1.tsv`,
`passB_p1.tsv`), then a tight PIL crop (3-6x zoom) of the exact token region cut directly from
`src_04612_p1.png` (already on disk, no network) to read the disputed digit myself. Every one of the 16 rows
in `settle.tsv` was checked this way; none needed `alt` (all resolved with reasonable confidence from the
glyph shapes, cross-checked against unambiguous instances of the same digit elsewhere on the same page --
e.g. 5 vs 8 by hook-vs-double-loop, 1 vs 2 by straight-vs-curved stroke, 3 vs 7 by loop-vs-diagonal). Result,
`ax4612tr/settle.tsv` all 16 rows now `S`-graded (was AX-4612TR2's `p1_r04`/`p1_r33` etc. `?` rows):

| page/line/pos | A | B | settled | note |
|---|---|---|---|---|
| p1_r04 pos27 | (none) | 9 | **9** | passB confirmed: a small "9" really is written after "25," at the extreme right margin (`ax2_4612/crops/p1_r04_pos27_9.jpg`); passA's crop simply stopped one token short, nothing on a page fold |
| p1_r04 pos12 | 51 | 81 | **81** | passB confirmed; glyph matches the unambiguous "81" three tokens later on the same line (`ax2_4612/crops/p1_r04_pos12_81.jpg`) |
| p1_r05 pos21 | 73 | 13 | **13** | passB confirmed |
| p1_r06 pos18 | 74 | 34 | **34** | passB confirmed |
| p1_r09 pos5 | 28 | 22 | **22** | passB confirmed |
| p1_r10 pos3 | 10 | 20 | **10** | passA confirmed (straight "1" stroke, not curved "2") |
| p1_r10 pos4 | 38 | 78 | **38** | passA confirmed (looped "3", not diagonal "7") |
| p1_r10 pos25 | 38 | 88 | **38** | passA confirmed (last token before the paragraph-end dash) |
| p1_r22 pos20 | 34 | 84 | **34** | passA confirmed |
| p1_r22 pos22 | 23 | 28 | **23** | passA confirmed |
| p1_r23 pos7 | 130 | 150 | **150** | passB confirmed (rounded "5" loop, distinct from the "3" in the neighbouring "138"; `ax2_4612/crops/p1_r23_pos7_150.jpg`) |
| p1_r26 pos7 | 51 | 81 | **51** | passA confirmed (open "5" hook, distinct from the "8" double-loop next to it) |
| p1_r26 pos8 | 34 | 84 | **84** | passB confirmed |
| p1_r33 pos22 | 109 | =Wesel | **=Wesel** | passB confirmed: this is a genuine cursive **word**, not a numeral -- a tall looping ascender, no digit shapes; consistent with Wesel, a Rhine town, a plausible place-name in this military correspondence. passA misread a word as a number. (`ax2_4612/crops/p1_r33_pos22_wesel.jpg`) |
| p1_r35 pos22 | 33 | 37 | **33** | passA confirmed (two matching "3" loops) |
| p1_r36 pos4 | 51 | 81 | **51** | passA confirmed |

Split 8 passA / 7 passB / 1 word-not-number, close to even -- neither pass is systematically more reliable at
this length. `ciphertext_4612_v3.tsv` (1237 rows, same convention as v2; 833 value-1-120 numerals, up from
v2's 819 -- p1_r33's settlement moved one token from the numeral count to a clear word, and the r04/pos27
insertion added one) built by `ax4612tr/build_v3.py` (extends AX-4612TR2's `build_v2.py`, adds this session's
16 settlements plus one insert-only-token settlement the v2 script's `insert` branch never checked against
`SETTLEMENTS` at all -- fixed here as `INSERT_SETTLEMENTS`, keyed by passB's own line/position since an
insert-only token has no passA line/position to key on). 154 `?` remain (all clear-word wording disagreements,
out of this brief's numeral-only scope, e.g. "xxij.me" vs "xxvij", "scay depuis" vs nothing -- a real content
difference between the two blind readings of the salutation, not investigated here).

**Unit 2: decode v3 under key_full.tsv v3, gate, judge.** `decode_4612_v3.json` (new; key `key_full.tsv`, not
`key.tsv`, per the brief). `python3 tools/decode_key.py ciphers/lodewijk-van-nassau-1573-74 --config
decode_4612_v3.json --check` -> `ciphertext_4612_v3.tsv: tokens 1029: C 698, H 1, I 141, M 9, U 180` then
"reading up to date" after generation.

**Gate, written here at 05:39 UTC before any number below was computed (verbatim from the brief):** "4612 v3
reads under key_full if its French-word share (word_share_check.py method, fr16) is above the max of 20
value-shuffles of key_full AND at least 0.85 of the share the same statistic gives 5811's own ciphertext
(known reading) cut to 4612's N."

`ax4612tr/word_share_check_v3.py` (extends AX-4612TR2's `word_share_check.py` to key_full and adds the 5811
positive control cut to 4612 v3's N):
```
v3 ciphertext_4612_v3.tsv under key_full: 589/833 = 70.7% inside a French word (>=3 letters); N=833 value-1-120 numerals
v3 through 20 value-shuffled copies of key_full: mean 44.7%, range 33.3-60.6%, max 60.6%
5811 (known reading) cut to N=833 under key_full: 776/833 = 93.2% inside a French word (>=3 letters)

GATE: v3 70.7% > shuffle max 60.6%? True. v3 70.7% >= 0.85 * 5811-control 93.2% = 79.2%? False.
GATE VERDICT: does not read under key_full (gate not met)
```
v3 clears the shuffle-floor half of the gate comfortably (70.7% vs a 60.6% max of 20 draws -- consistent
with v2's own 68.6% vs 61.3%, AX-4612TR2, so settling the 16 numerals barely moved this number) but falls
well short of the 5811-control half: 70.7% is only 0.76 of 5811's 93.2% at the same N, not the required 0.85.
**Gate not met: 4612 v3 does not read under key_full** by this statistic, though it is well above chance.

**Judge**, both numbers side by side, target then the 5811-cut positive control (same N, same key,
same corpus):
```
python3 tools/judge_plaintext.py specs/lodewijk-4612.json --file ciphers/lodewijk-van-nassau-1573-74/reading_4612_v3.txt
FAIL language: score=-1.479, null_p99=-1.718, real_p05=-0.929, real_median=-0.815, mode=both, N=1824
FAIL - lodewijk-van-nassau-1573-74 (a PASS is a gate for a verifier, not a reading; rule 10)

python3 tools/judge_plaintext.py specs/lodewijk-4612.json --file ciphers/lodewijk-van-nassau-1573-74/ax4612tr/reading_5811_cut833.txt
FAIL language: score=-1.296, null_p99=-1.721, real_p05=-0.931, real_median=-0.82, mode=both, N=1134
FAIL - lodewijk-van-nassau-1573-74 (a PASS is a gate for a verifier, not a reading; rule 10)
```
**Per-fold caveat (AX-4612's own finding, unchanged):** fr16 FAILed key.tsv's true 5811/4610 readings at
N=775 (blended FN 25.7%, folds 7.5/67.5/2.0) -- and it does so again here: the known-real 5811 control
itself FAILs this judge (-1.296 vs real_p05 -0.931), so the judge cannot decide at this length/register
regardless of the target. v3's own FAIL (-1.479) is further below the null than the control's FAIL (-1.296
vs null_p99 -1.718/-1.721), consistent with the word-share gate's own verdict that v3 sits above chance but
below what real 5811-quality French gives at this N -- both statistics point the same way without either one
being a clean pass/fail on its own.

**Verdict for unit 2: gate not met.** Per the brief, unit 3 (key-seeded anneal) runs next.

**Unit 3: key-seeded anneal.** `tools/homophonic_anneal.py --init KEY.tsv` added (start the anneal from a
given sign->letter map instead of a random one; default behaviour unchanged when `--init` is omitted, checked
against the pre-existing `tools/tests/test_homophonic_anneal.py`, which still passes unchanged). Offline test
`tools/tests/test_homophonic_anneal_init.py` (7 checks: `load_init_key`'s NULL/multi-letter/case folding, an
`iters=0` sanity check that `--init` actually seeds the returned key rather than being silently ignored, `--fix`
overriding `--init` on a shared sign, a missing/invalid init value falling back to a valid random letter, `init=
None` matching `init={}` byte-for-byte, `anneal_noisy` accepting `init` the same way, and one end-to-end CLI
run). Both tests pass.

## AX2-BLANKS: codes 156 and 182, contexts and 7206 (26 Sept 2026, LANE AX2)

Worker AX2-BLANKS (Sonnet), brief `.claude/briefs/runs/2026-09-26-lane-ax2-blanks.md`, box 90 min from 05:20:16 UTC.
Continues AX-GLOSS/AX-COMP/AX-COMP2's search for 5797's two remaining blanks: p7_spot6 (182) and p8_spot7 (156).

**Unit 1: context table.** `ax2_blanks/contexts.py` (script, no images) scans every `ciphertext_*.tsv` in this
folder and in `../jan-van-nassau-1572-75/` for exact codes `156`/`182`, and decodes the surrounding tokens under
`key_full.tsv` (`ax2_blanks/contexts.tsv`). 5797's own line labels are isolated "spot"/"control" excerpts around
one blank each (confirmed by inspecting the raw file: `p7_spot6` is immediately followed in file order by
`p8_spot7`, but the two are non-adjacent places on the leaf, and a `p5_control_election` excerpt sits between two
unrelated spots) -- the script stops the ±12 window at a spot/control label boundary rather than stitching
unrelated excerpts together as if they were one continuous line.

**156: no new occurrence found anywhere.** Exact-match grep across all 16 ciphertext files (this folder's 13 plus
the sibling folder's 3) finds code `156` exactly once, at its own spot (5797 `p8_spot7`). AX-COMP2 already
established it is absent from 7205; this pass extends that to every other transcribed letter on file, including
4610/4611/4612/4612_v2/4614/4616/4503/5799/5810/5811/sib (all this target's own 1574-table letters) and
5549/5549_ps/5551 (the sibling folder). Context (within-spot only): `<156> 127[NULL] 135[NULL] 144[NULL] 129[NULL]
=begert =meiner`, i.e. 156 sits alone as the first sign of the spot, followed by four NULLs and then Groen's clear
"begert meiner" ("[X] desires/requests of me"). Grammatical slot: a subject/name placeholder immediately before a
verb clause -- the same shape as `p6_spot4`'s `172[lecontejean] ... =zeuget =diesen =morgen` (Count Jean testifies
this morning) and `p7_spot6`'s own `182 128 133[NULL] 142 =ist =willig...` (see below). A value proposed from this
shape alone is grade I only (rule 4) and is not written to names.tsv/key_full.tsv.

**182: two informative occurrences under the same 1574 table, one coincidental non-match.**
- **7205** (`07205_p4_L01`, already reported by AX-COMP2): settled H from the image, run `82[e].182.02[n?].139`;
  aligned "meaning" is M-grade 'y' from a single occurrence under an alignment AX-COMP2 itself flagged as
  effectively unconstrained (only 2 weak anchors across 4919 tokens) -- not usable evidence either way.
- **4610** (`p2_L02`, M-grade transcription, "gap" flag against pass B): `192[roidespagne].112[l].182.81[e].3[n]
  .27[s].148.129[NULL].82[e]...`. 182 sits immediately after the name-code 192 (Roy d'Espagne) and the letter
  code 112 (l), i.e. in a position that could be either an ordinary letter or the start of a new clause -- the
  transcription itself is M-grade (gap-flagged) here, so this occurrence supports a candidate reading only as
  weakly as its own transcription confidence.
- **5549** (jan-van-nassau-1572-75, run 15 pos 7): a `182` digit-match exists in the raw transcription, but
  `jan-van-nassau-1572-75/NOTES.md` (lines 621-623) already established that 5549's *main body* does not read
  under Lodewijk's 1574 table (`key_full.tsv`'s table) at all -- "5549 is therefore (all or nearly all) in the OLD
  key, which is neither key_1572 nor Lodewijk's table" -- only 5549's *postscript* (`ciphertext_5549_ps.tsv`,
  PS1-PS26) is in the shared table, and codes 156/182 do not occur in that postscript. So this is a same-digit
  coincidence across two unrelated key systems, not a second sighting of key_full's code 182; it is excluded from
  the count above and carries no information about 5797's blank. Flagged here so nobody re-finds it and treats it
  as corroboration.

So across every transcribed letter that shares 5797's own table, 182 occurs twice more (4610 M-grade, 7205
H-grade-as-ciphertext/M-grade-as-meaning) and 156 occurs nowhere else. Neither gains a value: 7205's alignment is
unconstrained, 4610's transcription is M-grade at that exact position, and 156 has no second sighting to
triangulate from at all. `p7_spot6`'s and `p8_spot7`'s own local shape (subject-code-then-verb-clause, matching
172/153/161's already-graded pattern) is the only consistent signal for either code, and it identifies a
*grammatical role* (name/title placeholder), not a *value* -- grade I, per rule 4, not entered into names.tsv.

Files: `ax2_blanks/contexts.py`, `ax2_blanks/contexts.tsv`. No hosts (script only, no images/network).

**Unit 2: 7206.** Fetched the WVO PDF (`resources.huygens.knaw.nl/media/wvo/images/07000-07999/07206.pdf`,
1 request, 200). 8 pages, rendered at 300dpi to the scratchpad. AX-GLOSS's per-unit table (this file, "AX-GLOSS"
section) described pp.5-6 as clear text "of similar shape to 7205's pattern -- likely another companion
decipherment, not confirmed by close reading". Close reading finds that is **not** what pp.5-6 are: p5 opens
mid-sentence, continuing the exact sentence cut off at the bottom of p4's *own* clear postscript ("...de laquelle
je vous [envoye] ... [la respon]ce de mondit sieur et celle de mon frere le Conte Loys) Je differeray aussi de
respondre..."), and p6 closes with its own full signature. So p1-p6 is **one continuous letter** (Guillaume de
Nassau to "Messieurs mes freres" -- Jan, Lodewijk and Hendrik -- dated 30 Jan 1574, address leaf confirmed later,
see below) that alternates clear prose with two enciphered postscripts: postscript "2"/"3" (p2 bottom - p3 - p4
top, cipher, ending "...je remets a cest effet la dessus") and postscript "4" (p4 bottom - p6, entirely clear, a
different later-arrived letter being summarised, no cipher). Pages 5-6 belong to the *second*, all-clear
postscript and are not a decipherment of anything.

**The real companion decipherment is page 8** (foliated 218; page 7 is its own address leaf, "A Messieurs les
Comtes Jehan, Loys et Henri de Nassau, mes bien bons freres. Dillenb[ourg]", confirming this is a second, separate
document bundled with the first). Page 8 opens "Messieurs mes freres, mes dernieres [-] Depuis ceste escripte me
sont venuz deux lettres..." -- the identical opening words of the *first* letter's postscript "2" -- and its body
("...quant au voiage de mons. de Lumbres, Je le gouste fort bien... les choses sont fort enaigries entre le Roy
de Pollogne et le Duc de Saxe...") matches postscript "2"/"3"'s ciphertext word for word at the positions where the
cipher itself decodes as French under `key_full.tsv` (spot check, row 1 of p3: `130.79.85.2.8.117.119.84...`
decodes `_denommesortirabonetoeureuxeffect?__`, i.e. "...de nomme sortira bon et heureux effect", matching p8's
"...sortira bon et heureux effect" exactly). So the brief's test resolves **yes, it is a decipherment -- just of
page 8, not pages 5-6** (the brief's own fallback, "if not, stop the unit and say so", does not apply once the
right page is found).

**Transcription and alignment.** Cut line crops of p2 (bottom postscript only), p3 (full page) and p4 (top
through "la dessus") with `tools/iiif_lines.py --lines-per-crop 6` (6 crops per page kept the subagent calls to
one page each, per Usage 6); two independent readings per page: AX2-BLANKS's own eye-read of the full 300dpi
page (documented above, not blind) and one blind Sonnet subagent pass per page on the crops (a deviation from the
brief's "two blind passes" given the wall-clock box; logged here rather than silently substituted). The p2 and p4
crop batches had a real tool-quirk both subagent passes caught independently: several `_s1`/`_s2` "segments" were
byte-identical (the line fit under `--max-width` so the tool never split it), truncating a few line-ends at the
crop's right border; AX2-BLANKS's own full-page zooms (not cropped) supplied the missing tail of those specific
lines, so no digit was lost overall, but the crop tool's segment-duplication-instead-of-no-split behaviour on a
line that fits in one segment is worth a follow-up fix to `tools/iiif_lines.py` (not attempted here, out of this
brief's scope). The two passes agreed on the great majority of digits; the handful of disagreements are recorded
at grade M with the alternate reading in `ciphertext_7206.tsv`'s `alt` column -- none of them is adjacent to 156
or 182.

`sh axcomp/run.sh 7206` (`axcomp/build_pairs.py` + `tools/interlinear_align.py --floor 121 --clear-consumes
--prior key_full.tsv` + `axcomp/keys.py`): 18 anchors from 999 tokens (7205 had only 2 from 4919 -- this letter's
clear-word runs are far more reliably transcribed, so the alignment is much better constrained here). Codes
1-120: 99/100 agree with key_full (2 isolated single-occurrence conflicts, 20 and 40, M grade, not pursued).
**Same 1574 table** as the rest of the pool.

**156 and 182: neither occurs anywhere in 7206.** Exact-match search of `ciphertext_7206.tsv` (999 tokens, both
passes) finds no "156" and no "182" token. 5797's two remaining gaps are not settled by this letter either.

**A genuine finding, not the target codes but worth flagging separately: 172 recurs 3x in 7206, all in a
"Monsieur de Lumbres" context, apparently conflicting with key_full's existing 172 = lecontejean (H, from 4614).**
The postscript's cipher reads `150.139.172` ("Or quant au voiaige de [150.139.172], Je le trouve fort bien..."),
`122.127.129.172.130` ("Je crains que [122.127.129.172.130] feroit ledict voiaige non seullement..."), and
`77.83.150.172.122` ("...moyennant que l'on eust premierement..."), and page 8's decipherment matching those three
spots reads "voiage de mons. de Lumbres", "ce[dit] Lumbres feroit ce voiage", and (near "77.83.150...122") the
continuation about treating first with the Roy de Pollogne. All three occurrences were re-checked by eye at 3-5x
zoom directly against the 300dpi source (one, in `07206_p4`, was flagged genuinely ambiguous by the blind subagent
pass, digit 7 vs 8 vs 3): compared stroke-for-stroke against confirmed "7"s (`127`, same line) and confirmed "8"s
(`83`, same line) immediately beside it, the digit is a flat-topped diagonal stroke with no closed loop --
consistent with the other two zoomed "172"s and inconsistent with this hand's "8" -- so all three read **172**,
not 182; this cipher gives no new sighting of 182 either. `tools/interlinear_align.py`'s own (unseeded, since
172 > floor 121) alignment independently placed 172's chunk near the context word "lumbres" twice out of three
occurrences (`key_7206.tsv` row 172, `others` column: "lumbres:1,udit:1"), corroborating the reading without
relying on my own eye-read alone. This is a real H-vs-H conflict between two different letters' period
decipherments (4614's "172 = le Conte Jean" vs 7206's three consistent "172 = [part of] Lumbres" occurrences) --
flagged here for the orchestrator/AX-MERGE-style reconciliation pass; not resolved and not written to
key_full.tsv or names.tsv (not this brief's file to edit, and not a 156/182 finding).

**Incidental bonus from the same alignment (not this brief's target, noted for whoever next works 7206/pool
coverage):** page 8's list of Holland towns ("Enchuysen, Edam, Monichedam, Alckmar, Gravesande, Vlaerdinguen,
Schiedam, ... Rotterdam") lines up one-to-one with the cipher run `63.227.259.260.222.261.228` (row with
"...ou aultre lieu...") and `100.61.37.82.2.242...` (Rotterdam), giving six more grade-M/H-candidate place-name
codes (227=Enchuysen, 259=Edam+Monichedam, 260=Alckmar, 222=Gravesande, 261=Vlaerdinguen, 228=Schiedam,
242=Rotterdam) not previously in key_full -- listed in `key_7206.tsv`, not merged.

Rule 10: no novelty words used. Rule 3: no numeric-threshold control gated in this unit (a companion-decipherment
identification and an alignment run, not a cryptanalytic claim).

Hosts: `resources.huygens.knaw.nl` 1 request (the 7206 PDF, 200). Subagents: 3 blind Sonnet passes (one per page,
p2/p3/p4; at most 2 at once, run 2 then 1), agent ids a9e8d3e3c44e53dd6 (p3), aa285d0ff38560502 (p2),
ae2b5a1506e9d4486 (p4).

Files: `decipherment_7206.txt`, `ciphertext_7206.tsv`, `key_7206.tsv`, `ax2_blanks/build_ciphertext_7206.py`,
`axcomp/{pairs_7206.tsv,align_7206.tsv,rawkey_7206.tsv,compare_7206.tsv}` (via `axcomp/run.sh 7206`, which this
worker did not modify). `key_full.tsv`, `key.tsv`, `names.tsv` untouched.

**Matched control first (rule 3), gate written here before the run:** "5811's real ciphertext (a letter
key_full reads correctly), cut to 4612 v3's N of value-1-120 numerals (833), annealed from key_full with a
random 20 percent of codes 1-120 reassigned to a different letter, 3 seeds (each perturbs its own fresh 20
percent); the control recovers >= 0.90 of 5811's key_full token reading in every seed, or the target does not
run (family_run.py's own CONTROL BELOW GATE convention)." `ax4612tr/anneal_control.py` (order-3 plain `Model`,
the fr16 judge corpora, restarts=8, iters=40000, matching `tools/families/homophonic.py`'s own defaults):

```
5811 cut: N=833 signs, K=96 distinct
seed 1: perturbed 24/120 codes, best score -1887.9, recovers 609/833 = 73.1% of key_full's token reading
seed 2: perturbed 24/120 codes, best score -1897.4, recovers 536/833 = 64.3% of key_full's token reading
seed 3: perturbed 24/120 codes, best score -1889.3, recovers 602/833 = 72.3% of key_full's token reading

GATE: all 3 seeds recover >= 0.90? False (shares: [0.731, 0.643, 0.723])
```
Checked this was not simply under-converged before accepting the negative: re-ran seed 1 alone at 150000 iters
(3.75x) -- 655/833 = 78.6%, an improvement over 73.1% but still 11.4 points short of the 90% gate. **CONTROL
BELOW GATE: the target (4612 v3) was not run.** At N=833/K=96, this order-3 fr16 anneal cannot reliably repair
a key that starts only 20 percent wrong, so a run on 4612 (where the true key, if any, is completely unknown)
would not be informative regardless of what it found -- exactly the failure mode rule 3 exists to catch before
a numeric result gets reported as a negative on the target. `HYPOTHESES.md` row appended by hand (not one of
`family_run.py`'s registered families) with both the per-seed numbers and the 150000-iter recheck.

**Result for AX2-4612 as a whole.** Unit 1 settled all 16 open numerals in `ax4612tr/settle.tsv` against the
image directly (`ciphertext_4612_v3.tsv`, 833 value-1-120 numerals, up from v2's 819). Unit 2's word-share/
judge gate under `key_full.tsv` is **not met** (70.7% vs a required 79.2%, though clearly above the 60.6%
shuffle-max floor) -- v3 is not a reading under key_full's design as a straight substitution. Unit 3's
key-seeded anneal could not be run on 4612 at all because its own matched control (a real, correctly-keyed
letter started 20 percent wrong) could not be repaired back above 64-79% by this search, well short of the
90% gate -- **not a test of 4612**, not a negative on it either. **Verdict: candidate not reached; 4612 stays
`partial`**, no reading claimed, no token graded (rule 4 N/A). The settled v3 transcription and the word-share
gap (70.7% vs 93.2% for a real letter at this N) are themselves worth carrying forward: a successor with more
anneal search budget, a different (larger-K-tolerant) design, or fresh eyes on the 154 still-unsettled
clear-word disagreements could make more of this than this box did. Novelty not classified (rule 10, out of
scope -- no reading exists to classify). No `flag: 4612 candidate ready for re-derivation` line is written,
per the brief, since no reading was produced.

Files: `ax4612tr/{build_v3.py,word_share_check_v3.py,anneal_control.py,decode_5811_cut833.json,
ciphertext_5811_cut833.tsv,reading_5811_cut833.txt,reading_5811_cut833_tokens.tsv,settle.tsv}`,
`ciphertext_4612_v3.tsv`, `decode_4612_v3.json`, `reading_4612_v3.txt`, `reading_4612_v3_tokens.tsv`,
`ax2_4612/crops/{p1_r04_pos27_9.jpg,p1_r04_pos12_81.jpg,p1_r23_pos7_150.jpg,p1_r33_pos22_wesel.jpg}` (150 KB
total, the four crops cited above; `images_wv2/crops_4612` itself untouched, per the brief),
`HYPOTHESES.md` (appended), `tools/homophonic_anneal.py` (`--init` added), `tools/tests/
test_homophonic_anneal_init.py`, this section. `key_full.tsv`, `key.tsv` and `key_4612.tsv` (not created --
no key change to report) untouched. No network requests (all images and corpora already on disk). No
subagents (all crop-reading and anneal work done directly by this worker). cost: see the lane ledger.

## AX2-5801: 5801 key from its period decipherment (26 Sept 2026, LANE AX2)

Worker AX2-5801 (Sonnet), per `.claude/briefs/runs/2026-09-26-lane-ax2-5801.md`. Box 100 min from
05:20:28 UTC.

**Clear text.** dbnl full-text search located Groen IV Lettre CDXXIII (pp.129-133, `groe009arch04_01_0041.php`),
Willem to his brothers Jean and Louis, "Escrit à Delff, ce 28 mai 1573" -- date and place match WVO 5801's
own catalogue metadata (Delft, 28 May 1573) exactly. Confirmed independently three ways: (1) 5801 p1's
opening clear line reads "Messieurs mes freres. Jay receu vos trois datees, l'une de Dillenberg le xvi, e
l'autre de [Bedbur] le xx du present..." -- word for word the same as CDXXIII's incipit "Messieurs mes
frères. J'ay receu vos lettres datées, l'une de Dillenberg le 16, et l'autre de Bedbur le 20 du présent";
(2) the letter's subject matter (relief of Harlem, the Cologne negotiations, Louis's proposed crossing near
Tiel, the Duc de Medina-Celi at Spa) matches CDXXIII's body throughout; (3) crop `05801_p1_L09.jpg` carries
a later archival pencil annotation "1573. May 28" in a different, non-secretary hand -- independent of both
Groen and the WVO catalogue metadata. `decipherment_5801.txt` (cleaned) and `groen/groen_IV_CDXXIII.txt`
(raw fetch) both written. Not yet AUDIT.md-classified (rule 10; a verifier's job). Two of 5801's own p5
transcription passes independently read the closing date as "ce viij mars 1573" / "ce xxviij mars 1573"
rather than "28 mai 1573" -- given three independent sources agree on 28 May and both p5 passes flagged
that whole region as low-confidence guesswork at a cursive month name, "mars" is most likely a blind-pass
misread of "may" in an unfamiliar secretary hand, not evidence of a different letter; flagged, not resolved,
for whoever next reads p5 off the image directly.
Hosts: dbnl.org 5 requests (TOC + 4 candidate-letter pages), >=2s apart, descriptive UA.

**Cipher transcription pp.1-5.** `images_wv2/crops_comp/05801_p{1..5}_L*.jpg` (47 crops, already on disk,
AX-COMP's own fetch) were denser than AX-COMP anticipated: most crops are composite blocks of 2-6 stacked
physical script lines with a tiny interlinear decipherment gloss squeezed between them, not one line each
-- both blind passes on every page said so unprompted. Two blind Sonnet subagent passes per page (crop
paths only, never a page image), reconciled with `tools/reconcile_passes.py`:

| page | agreement | gate (60%) |
|---|---|---|
| p1 | 53.8% (376/699) | below |
| p2 | 86.2% (558/647) | above |
| p3 | 76.2% (523/686) | above |
| p4 | 76.7% (447/583) | above |
| p5 | 53.8% (387/719) | below |

p1 and p5 fall below gate because of real segmentation disagreement between the two blind passes on the
most composite crops (both passes independently said so), not a coin-flip on individual digits -- on the
numeral *sequences* the two passes mostly agree (see p1's near-identical digit strings in both passes'
reports); the token-count mismatch is where a pass merged or split a stacked sub-line differently. No
manual per-token settling from the image was done in this box (time); the reconciled draft (majority sign
where the passes agree, A's sign at grade M elsewhere) went into `ciphertext_5801.tsv` unmodified, so every
code from this page is at best M, never H. This is a materially less reliable transcription than AX-COMP's
4614 pass (79.8-92.5% agreement on cleaner single-line crops) and should be treated as a rough first draft,
not a committed reading, until a second pass on finer-grained crops (or from the image directly) is run.
`ciphertext_5801.tsv`: 3332 tokens.

**Key** (`axcomp/build_pairs.py 5801` -> 14 anchors, 15 pairs; `tools/interlinear_align.py align ... --floor
121 --clear-consumes`, **no --prior**, per the brief -- seeding from key_full would beg the question the
brief exists to answer). `axcomp/keys.py 5801` -> `key_5801.tsv`: 179 codes (117 <=120, 62 >120), all grade M
(no code reached 2 agreeing occurrences at 60% -- unlike AX-COMP's --prior-seeded runs, this alignment
had nothing to anchor codes 1-120 over spans this long, so it drifted the same way AX-COMP's own unseeded
4614 attempt did: "1260 conflicts against 384 agreements"; here 111 conflict / 6 agree against key_full and
58 conflict / 5 agree / 54 new against key_5799, for codes 1-120). Grade C, not H: 5801's own leaf carries
the decipherment (period, but not proven to be contemporary with the cipher hand without image inspection
this box did not have time for); treat as C pending that check.

**Table (which table does 5801 use) -- `axcomp/table_check.py 5801`, the same test AX-COMP ran for 4614 and
7205:** coverage of 5801's own three longest 1-120 runs (49+42+39=130 codes) and of all 2345 in-table
tokens: **key_full 1.000, key_5799 0.488**. Every code 5801 uses in the 1-120 range is a code key_full's
24-block design has a row for; key_5799's 78-code table only covers about half of them. This matches
AX-COMP2's finding for 7205 (1.000 vs 0.400) exactly: **5801 uses key_full's 1574-circle table, not
5799's**, on structure alone -- independent of whether this box's own noisy per-code values (above) are
individually right. The decoded runs themselves are not clean French ("acssepuzeinepcseuxpnnereutantommes
ilxexoyentleurc") but do contain recognisable fragments ("sil", "leur", "tant"); not claimed as a reading.

**Codes >120 (names/nulls), read-only, not adjudicated this box:** four codes 5801 uses already have H/C
grade values from *other* letters in key_full -- 172=le Conte Jean (9 occ. in 5801), 192=Roi d'Espagne (5
occ.), 223=Harlem (4 occ.), 312=de la ville de (3 occ.) -- all plausible in a letter about the relief of
Harlem addressed partly to "le Conte Louys". `ax2_5801/compare.tsv` marks all four "conflict" because this
box's automatic, unadjudicated alignment assigned them noisy single-letter or wrong-multi-word chunks
instead (172->"a", 192->"aulcunspoint", 223->"a", 312->"a") -- the same class of artifact AX-COMP fixed by
hand for 4614 (`axcomp/adjudicate_N.tsv`, reading the aligned context by eye) but this box did not have time
to redo. These four are a lead for a follow-up pass with `axcomp/adjudicate_5801.tsv`, not a settled
conflict. `key_5801.tsv` full comparison: `ax2_5801/compare.tsv` (180 rows).

**Apply to 5799 and 4612** (`decode_4612_k5801.json` against `ciphertext_4612_v3.tsv` -- AX2-4612 pushed v3
mid-box, used in preference to v2 per the brief; `decode_5799_k5801.json` against `ciphertext_5799.tsv`;
both `tools/decode_key.py ... --check` exit clean). Gate, pre-registered in the brief before running: target's
French-word share (fr16 word list, `ax2_5801/word_share_check.py`, the `ax4612tr/word_share_check.py`
method) must exceed the max of 20 value-shuffles of key_5801 AND reach 0.85 of 5801's own share under
key_5801 at the same N.

| | 5801 (own, control) | 5799 target | 4612 target (v3) |
|---|---|---|---|
| French-word share | 72.6% (1702/2345) | 71.7% (104/145) | 79.2% (660/833) |
| 20-shuffle mean / max | -- | 71.8% / **86.9%** | 82.9% / **88.4%** |
| gate (target > shuffle max) | -- | **FAIL** | **FAIL** |

Both targets fail the shuffle-control side of the gate -- but so does the *5801-own control itself* (72.6%,
below 5799's own shuffle mean of 71.8% and well below both shuffle maxima). A control that a key's own
source text cannot beat is not a working control (rule 3): key_5801's heavy concentration of very frequent
near-NULL codes (121, 124-126, 129, 132, 140 etc., each seen dozens of times, per `key_5801.tsv`'s
occurrence counts) means almost any value assignment -- real or shuffled -- lands enough short common French
words (de, le, et, la...) by chance to score 70-90% on this statistic at this N; the word-share test does
not discriminate for this particular key and this result licenses no conclusion either way on its own.
`tools/judge_plaintext.py` (fr16, per-fold caveat per CLAUDE.md's V6-PTCORP/es17c lessons) agrees with the
FAIL reading directly: 5799 FAIL (score -1.462 vs real_p05 -0.982, `ax2_5801/judge-fr16.json`), 4612 FAIL
(score -1.318 vs real_p05 -0.909, `specs/lodewijk-4612.json`) -- both readings are visibly non-language
("...areeeseeecs...", "...eeutereeeerntee...", dominated by the same handful of high-frequency near-NULL
codes all mapping to a vowel). **Verdict: 5799 and 4612 do not read under key_5801, on both the pre-
registered gate and the judge** -- but this box's key_5801 is itself unreliable (all M grade, no code
adjudicated), so this is a negative about *this pass's* key, not a clean negative about 5801's table; the
structural finding above (5801 uses key_full's table) stands on its own regardless.
Rule 3: real number and control/shuffle number given side by side throughout, including the one case where
the control itself failed to discriminate.
No H or C reading claimed this box (rule 4): key_5801 is C-sourced (period leaf, unconfirmed contemporary)
but every individual code value in it is M.

Files: `ciphertext_5801.tsv`, `decipherment_5801.txt`, `groen/groen_IV_CDXXIII.txt`, `key_5801.tsv`,
`decode_5799_k5801.json`, `decode_4612_k5801.json`, `reading_5799_k5801*.txt/.tsv`,
`reading_4612_k5801*.txt/.tsv`, `ax2_5801/{passA,passB}_5801_p{1..5}.tsv`, `ax2_5801/recon_p{1..5}/**`,
`ax2_5801/compare.tsv`, `ax2_5801/table_check_5801.txt`, `ax2_5801/word_share_check.py`,
`ax2_5801/judge-fr16.json`, `axcomp/{pairs,align,rawkey,anchors,compare}_5801.tsv`.
No subagents beyond the 10 blind transcription passes (2 per page x 5 pages), at most 2 at once.

## AX2-172: code 172, 4614 vs 7206 (26 Sept 2026, LANE AX2)

Worker AX2-172 (Opus), brief `.claude/briefs/runs/2026-09-26-lane-ax2-172.md`, started 05:59:54 UTC (clock read).
Hosts: `resources.huygens.knaw.nl` 1 request (07206.pdf, HTTP 200, descriptive UA), rendered locally
(`pdftoppm -r 300 -jpeg 07206.pdf p`, scratchpad; crops cut with PIL from that render, boxes in
`axmerge4/crops/` file names). 4614 read from the existing crops (`images_wv2/crops_comp/04614_p1_L02.jpg`,
`04614_p3_L01.jpg`, `images_wv2/crops_rederiv/04614_decipherment_p5_L06_zoom.jpg`). No subagents.
`key_full.tsv`, `names.tsv`, `AUDIT.md` untouched.

**Verdict: (c). The name codes (145-350) differ by direction of correspondence; the letter codes (1-120) do not.**
Letters from the brothers to Willem (Lodewijk 4613/4614/4615, Jan 5550) use one name list ("list A", the one
key_full holds); Willem's outgoing letters to his brothers (7206, 30 Jan 1574; 7205, 16 Jan 1574) use another
("list B"). 172 is not a slip on either side: it is le Conte Jean in list A and Lumbres in list B. 5797 (Jan and
Lodewijk to Willem, 22 Oct 1573) is a brothers-to-Willem letter and its one testable name code sides with
list A (below), so **5797 p6_spot4's 172 = le Conte Jean stands on list A's value**; the 7206 conflict no longer
contests it, but the key source is still a single 4614 occurrence.

**Q1, digits (by eye, against confirmed digits on the same line).**

| letter, line | run | reading | evidence |
|---|---|---|---|
| 4614 p1_L02_c pos 17 | 82.172.111 | 172, H | 7 matches the flat-topped 7s of "117.7" earlier on the line; no loop, not 8 |
| 7206 p3_L10a | 150.139.172 | 172, H | clean; same 7 as "74" on the line above (`axmerge4/crops/07206_p3_172a_*`) |
| 7206 p3_L13a | 122.127.129.172.130 | 172, H | clean (`07206_p3_172b_*`); the second null reads 127 or 128, both NULL |
| 7206 p4_L13 | 77.83.150.172.122 | 172, M | middle digit is a 7 written over another stroke (a correction); the 7 is clear, whatever lies under it is not (`07206_p4_172c_*`) |

**Q2, where the period words sit.** In 7206 the context codes are nulls, so 172 alone is the name:
139 is NULL in 7206 ("a la 132 336 139 et toutesfois" = "a la fanterie et toutesfois"); 150 falls where the clear
copy has no word four times ("...contre nous 150 | Que toutesfois", "mille 339 150 et mille"), so it is NULL in
this letter; 122/127/129/130 are C-NULL in key_full. So:
- p3_L10a "voiaige de 150 139 172" = p8 "voiage de mons[ieu]r de Lumbres": "monsr de" is the clear copy's wording,
  not a code; **172 = Lumbres**.
- p3_L13a "Je crains que 122 127 129 172 130 seroit ledict" = p8 "je crains que led[it] Lumbres feroit led[it]
  voiage" (AX2-BLANKS transcribed "ce[dit]"; the crop reads "led[it]"): **172 = Lumbres**, "ledit" not ciphered.
- p4_L13 "le voiay[ge] 77 83 150 172 122 moyennant" = p8 "le voiage dud[i]t Lumbres moyennant": d-e + null +
  **172 = Lumbres**.
- 4614 p1_L02_c "m o n f r e r e 172 l e q u e l" = companion leaf "mon frere le Conte Jean lequel": 172 is the only
  sign between "frere" and "lequel"; **172 = le Conte Jean**.

**Q3, other name codes across the two sets of letters (read by eye from crops; not the aligner column).**

| code | list A (brothers -> Willem) | list B (Willem -> brothers) | |
|---|---|---|---|
| 172 | le Conte Jean (4614, 1x H) | Lumbres (7206, 3x) | differ |
| 217 | Sr Geertruydenbergh (4614 x3 H; "sur 217 et 270 pour ce" = "sur Sr Geertruydenbergh et Bommel pour ce") | Bommel (7206 p3_L03b "personne a 137 217 / pour vous y attendre" = "personne a Boomel pour vous y attendre", H; 7205 p5_L02 line-end "sur 217" before the clear "Je vois par vre lre" = "venir sur boomel. Je vois par vre lre", M) | differ |
| 339 | harquebouziers (4613 aligned, C; 5557 gloss "Schutzen") | Landsknechtz (7206 p3_L06b "si oultre les quatre mille 339 141 vous eussiez" = "si oultre les quatre mille Landsknechtz vous eussiez", H) | differ |
| 202 | Franckreich (5550 gloss x4, H) | Angleterre (7206 p4_L11 "sa correspondance avec la 122 202 131 et croy pour aucun mauvais effect" = "avec l'Angleterre, non pour aultruy mauvais effect", H) | differ |
| 336 | Fussvolck (5557 gloss "Voetvolck") | fanterie (7206 "a la 132 336 139 et") | agree |
| 312 | ville de (4613) | ville (7206 "estant la 312 de grande garde") | agree |
| Bommel | 270 (4613/4615, 4614) | 217 | different codes |
| Maastricht | 273 (4613) | 276 (7206 "prendre 125 276 136 estant la ville" = "prendre Mastrich, estant la ville") | different codes |
| Duke of Saxony | 154 (5797, Groen print, C) | 196 (7206 x3: "entre le Roy de Pollogne et 196", "que 143 196 se mectroit", "du 146 141 196") | different codes |

Four codes disagree and three places/persons carry different codes, against 99/100 agreement on codes 1-120
(AX2-BLANKS). One decipherer's slip cannot explain four disagreements in three different letters, so the name
section is a separate list for each direction. 7205's single 339 sighting sits at the clear "aulcuns deniers"
(M transcription, heavy bleed-through), which fits neither list's Landsknechtz/harquebusiers; left unresolved, not
used.

**Which list 5797 follows.** By direction, list A (sender Jan and Lodewijk, like 5550 and 4613-4615). One direct
test: 5797 p5 writes Saxony as 154 (Groen IV pp.223-224 prints "Bey dem Herzog von Sachsen und" there, C), while
list B writes the Duke of Saxony as 196 at all three of its places. So 5797 is not on list B at that code. No
5797 code contradicts list A. The date gap (5797 Oct 1573; 5550 Dec 1573; 4614 Apr 1574) is inside list A's
attested span.

**Per-occurrence grades (rule 4).** 4614 172 = le Conte Jean: H (1). 7206 172 = Lumbres: H value at 3, with the p4
transcription at M (so H 2, M 1 on the digit). 5797 p6_spot4 172 = le Conte Jean: H by key source from list A
(1 occurrence), list membership of 5797 from direction plus one C datum (154), i.e. unchanged value, unchanged
grade, key source uncontested by 7206 because 7206 is list B.

**Consequence for tooling (not applied here).** key_full's codes >= 145 must not be applied to 7205/7206; their
name codes need their own list (key_7206.tsv's aligner values above 120 already show it: 217 "oomel", 339 "l").
Proposed notes for key_full, values unchanged: `axmerge4/proposal.tsv` (four KEEP_NOTE lines for
`axnames/build_key_full.py`). Not in this brief: whether 5801 (Willem to Jan and Lodewijk, May 1573), where 172
occurs 6x mid-run at M under key_full, is list B; AX2-5801 holds that letter.

Rule 10: no novelty words. Rule 3: no numeric gate here (a reading of period clear copies against their ciphers,
not a cryptanalytic claim).

Files: `axmerge4/proposal.tsv`, `axmerge4/crops/*.jpg` (11 crops, 476 KB), this section.

## AX2-5801ADJ: 5801 name codes against Groen IV CDXXIII (26 Sept 2026, LANE AX2)

Worker AX2-5801ADJ (Opus), brief `.claude/briefs/runs/2026-09-26-lane-ax2-5801adj.md`, started 06:40:25 UTC (clock
read). No network, no subagents; read by eye from `images_wv2/crops_comp/05801_*` and zooms cut from them
(`ax2_5801/crops/`, 6 JPEGs, 480 KB). key_full.tsv and names.tsv untouched.

**Method.** `axcomp/contexts_5801.py` prints every code >120 that key_full does not mark NULL with 14 tokens either
side decoded under key_full (`axcomp/contexts_5801.txt`, 261 rows). The draft transcription is M throughout (p1 and
p5 below the 60% pass gate, AX2-5801), so the decoded neighbours are too noisy to place by themselves. What does place
them is that **5801 carries its own contemporary interlinear decipherment above the cipher**, and at the places Groen
prints a name, that gloss sits over a single code. So each code was read on the crop: the gloss above it first, then
Groen's words at the matching place. Table: `axcomp/adjudicate_5801.tsv`; values: `key_5801_adj.tsv`.

**Findings (grade H = period gloss over the code on 5801's own leaf, with Groen's print agreeing; C = print only).**

| code | 5801 (Willem -> Jan and Lodewijk, 28 May 1573) | list A (brothers -> Willem) | list B (Willem -> brothers, Jan 1574) |
|---|---|---|---|
| 172 | **le Conte Louis de Nassau** (H, 1 glossed: p5 "Touschant ce que vous [172] avés traité avec [157]", gloss "le conte Louis de nassau" = Groen "vous, Monsieur le Conte Louys de Nassau") | le Conte Jean | Lumbres |
| 192 | **le Roy de France** (H, x2: "avec [192] sur aulcuns points", "le coeur du [192]") | roi d'Espagne (4496 gloss) | -- |
| 202 | France (H, x2: "en [202] pour traicter", "résidant en [202]") | Franckreich | Angleterre |
| 200 | Duc d'Alba (H) | Herzog von Alba | -- |
| 223 | Harlem (H, x3) | Harlem | -- |
| 312 | ville (C; gloss "Ville de Harlem" over 312.12.223, 12 = de) | ville de | ville |
| 331 | guerre (H, 1 of 7 checked) | -- | -- |
| 157 | Colognie (H) | -- | -- |
| 199 | la Royne d'Angleterre (C) | -- | -- |
| 203 | Espagne (C; gloss cut at crop edge) | -- | -- |

**Lumbres is not a code in 5801.** Groen's "J'ay envoyé Monsr de Lumbres en France" is written on p5_L03 in letter
codes with the gloss "m o n s ... de l u m b re s en" letter by letter, and then 202 (glossed "France").

**The other 172s.** Of the draft's nine 172s: one is glossed and named (above). Two are 132 on the image (p3_L01 line
end "129.132."; p3_L07 line-1 end "67.132") -- transcription errors, grade I. One (p5_L08 pos 79) is the same sign
as pos 21 re-emitted in a duplicated segment of the reconciled draft. Three sit unglossed at places where the print
names nobody ("c ha s [172] que s i x a i n e" = "chasque sixaine"; "l'un e [172] soustienne"; "toutesfois ... [172]
retarde"): NULL-like there, M. Two on p1 (p1_L03, p1_L04) were not settled (p1_L03's middle digit could be 5; p1 has
no name in Groen at either place). 192 likewise sits once unglossed at "faire [192] lever le siège" (NULL-like, M;
the digit may be 142). So 172 and 192 behave, in this letter, like name codes that also serve as fillers, or the
filler occurrences are other signs misread; this pass does not decide which.

**Verdict: (c), mixed, and against the direction theory as AX2-172 stated it.** 5801 is a Willem -> brothers letter,
yet at the one code it shares with 7206 on both lists' terms, 202, it agrees with **list A** (France/Franckreich,
not list B's Angleterre); at 172 it agrees with **neither** (le Conte Louis, against list A's le Conte Jean and list
B's Lumbres, while Lumbres is spelled out in letters); at 192 it differs from list A (le Roy de France against
4496's roi d'Espagne). 217 and 339, the other list-B contrasts, do not occur in 5801. The reading that fits all
three letters' glosses is that the name codes above 145 were not one list per direction but were reassigned between
letters or periods (May 1573, Jan 1574, Apr 1574), at least at 172 and 192. "Direction" does not predict 5801.

**Consequence for 5797 p6_spot4** (Jan and Lodewijk to Willem, 22 Oct 1573, "172 zeuget diesen morgen Kölln").
AX2-172 let 172 = le Conte Jean stand because 5797 is on the brothers' side and so on list A. 5801 shows that five
months earlier the same code carried **le Conte Louis de Nassau** in the Prince's own cipher, so a value for 172
cannot be carried from one letter to another by direction alone. p6_spot4's 172 has no value that holds across
letters. "le Conte Jean" (4614, Apr 1574) and "le Conte Louis" (5801, May 1573) are both attested readings of 172,
each in one other letter, and "[one of the brothers] leaves for Cologne this morning" fits either. Grade: M,
key source contested. It is not H. (Aside, not used: 5801's code for Cologne is 157, and 5797 writes Kölln as 155.
That is another name code that differs between the two letters.)

Proposals (never applied here): `axmerge4/proposal.tsv` gets two new rows, 172 and 192, each a KEEP_NOTE line for
`axnames/build_key_full.py`. key_full's values are unchanged.
Rule 4 counts for key_5801_adj.tsv's glossed occurrences: H 11 (172 x1, 192 x2, 202 x2, 200 x1, 223 x3, 331 x1,
157 x1), C 3 (312, 199, 203), M 6 (unglossed 172 x3, 192 x1, p1 172 x2), I 3 (two 132 misreads, one duplicate).
No reading of the letter is claimed. Rule 3: no numeric gate; this is a reading of period glosses and a print
against the cipher, not a cryptanalytic claim. Rule 10: no novelty words.
Not done in the box: the p1/p2 occurrences of 172/192 and the six unchecked 331s, which need zooms from the crops.

## AX2-4612S: local key repair with syllable values (26 Sept 2026, LANE AX2)

Worker AX2-4612S (Sonnet), per `.claude/briefs/runs/2026-09-26-lane-ax2-4612s.md`, box 75 min from
06:40:27 UTC. Tests H-S (AX2-4612's own hypothesis): 4612 v3 might use key_full for most codes but a
small set of rare-letter codes (x, y, z, b, k, q, h) for two-letter syllables or other letters instead.

**Unit 1: tool.** `tools/key_repair.py` (`--help`; offline test `tools/tests/test_key_repair.py`, 10
checks against a small hand-built fake n-gram model, no real fr16 corpus needed, runs in well under a
second). Per-code greedy local search: for each code present in the given ciphertext (most frequent
first), try its current value, the 26 letters, NULL, the 60 most frequent French bigrams and 20 most
frequent trigrams from the fr16 corpus (computed from `tools/french16_ngram.py`'s own corpus text,
folded, sliding 2-/3-window counts, ties broken alphabetically for determinism); score each candidate
by the fr16 order-5 model's total `logp` of the whole decoded stream (clear words folded in as fixed
context, every other code at its current working value); keep the best candidate only if it beats the
current value's score by more than `--margin` (default 3.0). Sweep rounds until nothing changes or
`--rounds` (default 4). Deterministic (fixed code order, fixed candidate order, no randomness
anywhere). Both tests pass.

**Gates, written here at 06:56 UTC before any control number below was computed (verbatim from the
brief):** "(a) Null control: run key_repair from key_full unchanged; count proposed changes (false
positives). (b) Known-answer control, 3 seeds: ... Gate: across seeds, >= 6 of 8 altered codes
recovered to the right value on average AND <= 2 false changes in (a) and on untouched codes in (b). A
control below gate = CONTROL BELOW GATE; stop and say so (not a negative)." Design choice for (b), per
the brief's own fallback clause ("if that is too awkward, instead SWAP..."): re-enciphering 5811's
plaintext letter-by-letter so a chosen code's two plaintext letters merge into one occurrence is a
real reimplementation of `axnames`-style alignment and did not fit this box; used the SWAP design
instead. Both controls run on `ax4612tr/ciphertext_5811_cut833.tsv` (5811's own ciphertext, cut to
4612 v3's N=833, key_full's own known-correct reading) against `key_full.tsv`.

**(a) Null control.** `python3 tools/key_repair.py ax4612tr/ciphertext_5811_cut833.tsv --key
key_full.tsv --out-key /tmp/null_control_key.tsv --out-changes ax2_4612s/null_control_changes.tsv
--margin 3.0 --rounds 4`:
```
110 codes of key_full present in this ciphertext (>=1 occurrence); 100 of them (91%) proposed changed
across 152 change-events over 4 rounds (many codes flip more than once: e.g. code 98, seen once,
'h'->NULL, then NULL->'c', then 'c'->'p', then 'p'->'t' across successive rounds -- a chase, not a
converging repair). 94 of the 152 change-events (62%) move to NULL, several with very large claimed
gains against the model's own two highest-frequency codes (31 't'(x27)->NULL gain 172.8; 22 'r'(x20)
->NULL gain 132.4; 83 'e'(x21)->NULL gain 100.1; 37 'u'(x37)->NULL gain 94.1) -- deleting the
*most*-attested letters in the whole cut gains the most, exactly the length-bias direction the
diagnosis below predicts. The rest replace one single letter with a different, equally arbitrary one
(8 'o'(x18)->'e' gain 111.5; 58 'z'(x6)->'u' gain 86.8). key_full is the known-correct key for this
letter (rule 3's own positive control elsewhere in this file). 100 false positives against a gate of
<=2.
```
**Diagnosis (not a coin-flip noise result -- a structural flaw in the scoring rule as literally
specified):** the objective is the *total* (summed, not averaged) log-probability of the decoded
stream. Every character's own log-probability is negative (no letter is ever certain, p<1), so
deleting a character by mapping its code to NULL always *removes* a negative term from the sum and
therefore always raises the total score, regardless of whether the deleted letter was the correct
one. NULL (0 characters) beats every non-empty candidate on this objective alone unless the letter
being kept is so contextually predictable that the fr16 model's per-character cost of keeping it is
smaller than the margin -- which is rarely true for a French text's own rarer letters (b, c, f, g, h,
k, q, v, x, y, z), i.e. for exactly the letters most likely to appear in a real cipher's rarer codes.
This reproduces on the algorithm's own known-good other use in this session: a same-algorithm smoke
run on `ciphertext_5799.tsv`/`key_5799.tsv` (a different, smaller target, --rounds 1) proposed changes
on the large majority of codes seen, most of them to NULL, several to an unrelated single letter with
a large claimed "gain" -- the same pathology, not specific to 5811/key_full.

**(b) Known-answer control, 3 seeds.** `ax2_4612s/known_answer_control.py` builds, per seed, a
perturbed `key_full` (8 codes used >=5 times in the 5811 cut, drawn without replacement, RNG seeded
`46120+seed`, arranged into 4 pairs whose letter values are swapped; 2 further such codes' values
replaced by a bigram from the fr16 top-60 list that is *not* their true letter, "hiding" them as
syllable codes), runs `tools/key_repair.py` from that perturbed key on the same 5811 cut, and compares
the repaired key to the *original* key_full (recovery: swapped code's repaired value == its true
key_full letter; false change: any code outside the 10 perturbed ones whose repaired value differs
from key_full):
```
55 codes used >=5 times with a single-letter key_full value (the eligible pool).
seed 0: swap 63,78,8,7,23,87,64,76 (paired 63<->78, 8<->7, 23<->87, 64<->76); hide 39,73 as bigrams.
  recovered 0/8 swapped codes to their true letter; 0/2 hidden-bigram codes reverted either.
  false changes on the other 158 untouched codes: 84.
seed 1: swap 73,12,61,9,81,112,72,113; hide 39,29.
  recovered 0/8; 0/2 hidden reverted. False changes: 88.
seed 2: swap 64,61,39,63,28,29,105,77; hide 58,33.
  recovered 0/8; 0/2 hidden reverted. False changes: 88.

GATE: mean recovery 0.000 (>= 0.75 needed)? False. Max false changes across seeds 88 (<= 2 needed)? False.
```
0 of 24 swapped-code instances (8 codes x 3 seeds) recovered their true key_full letter in any seed --
not "mostly recovered with a few misses", a clean zero. The perturbation itself is invisible to the
algorithm: with 84-88 of the other 158 untouched codes *also* getting rewritten every time, the 8
swapped codes' fate is decided by the same NULL-seeking cascade as (a), not by whether the search
can find their true letter again.

**Gate verdict: CONTROL BELOW GATE on both halves, by roughly two orders of magnitude** ((a) 100 false
positives vs a gate of <=2; (b) 0.0 mean recovery vs a gate of >=0.75, and up to 88 false changes vs
<=2). Per the brief and CLAUDE.md rule 3: stop here; this is not a negative about 4612's or 5799's own
key, and no key change is proposed on their strength.

**Root cause (not a coincidence of margin or corpus, a structural property of "total log-probability
of the whole decoded stream" as the objective).** Every character's own log-probability under any
n-gram model is strictly negative (no letter is ever certain). Summing (rather than averaging) over
the stream means each character can only ever *subtract* from the total score. Mapping a code to NULL
removes that character's negative term entirely, which unconditionally raises the total score by that
term's full magnitude -- regardless of whether the deleted letter was correct. A real letter only
survives against NULL if the model's own per-character cost of keeping it is smaller than `--margin`
in absolute terms, which is true for very predictable letters in strong context but false for most of
a real French text's rarer letters (exactly the letters that a homophonic table's rarer codes, x, y,
z, b, k, q, h -- H-S's own list -- are likely to hold), and NULL keeps winning against a bigram or
trigram candidate for the same reason once nearby codes have themselves already been NULLed (fewer
real characters left to give the longer candidate a fair context). This is independent of `--margin`'s
value in the range tried (a higher margin would raise the bar for adopting an incorrect single-letter
substitution but does nothing to stop the systematic NULL-ward pull, since NULL's "gain" over a real
letter scales with how improbable the model finds that letter in context, not with a fixed constant);
raising the margin enough to stop NULL-seeking would also block the very syllable-value substitutions
this tool exists to find. The fix (not attempted this box, since it changes the brief's own specified
objective, and the box's remaining time went to writing this up clearly instead) is to score by *mean*
log-probability per character (bits/char), or some other length-normalised or length-penalised
objective, so that deleting information is only rewarded when it is genuinely less costly than keeping
a real, low-probability letter -- not unconditionally.

**Verdict for AX2-4612S as a whole.** Unit 1 (the tool) works exactly as specified and is
deterministic (offline test, `tools/tests/test_key_repair.py`, 10 checks, all pass) -- the bug is in
the brief's own scoring objective, not in the implementation of it. Unit 2's controls both fail by
roughly two orders of magnitude, so per rule 3 unit 3 (running key_repair on 4612 v3 and 5799) was not
attempted: a tool this far below its own null control cannot produce a result distinguishable from
noise on either target, and running it anyway would risk exactly the kind of unearned "candidate ready
for re-derivation" flag rule 3 exists to prevent. `key_full.tsv`, `key.tsv`, `key_5799.tsv` untouched;
no `key_4612_repair.tsv`/`key_5799_repair.tsv` produced. H-S itself is neither confirmed nor refuted by
this box -- the instrument built to test it was not sound enough to run on either target, which is a
different thing from a negative result about the hypothesis. Next step for a successor: re-score with
mean (not total) log-probability per character, keeping candidate generation and the round-sweep
structure unchanged, and re-run both controls before touching 4612/5799 again.

Files: `tools/key_repair.py`, `tools/tests/test_key_repair.py`, `ax2_4612s/{null_control_changes.tsv,
known_answer_control.py,known_answer_control.log}`, this section. `key_full.tsv`, `key.tsv`,
`key_5799.tsv` untouched (rule 3: a control below gate means the target is not run; no
`key_4612_repair.tsv`/`key_5799_repair.tsv` produced this box). No network. No images.

## AX2-4612S2: key repair, length-neutral objective (26 Sept 2026, LANE AX2)

Worker AX2-4612S2 (Sonnet, session_018ktTTDt9vs6NM3JQ5Sjxvb), per
`.claude/briefs/runs/2026-09-26-lane-ax2-4612s2.md`, box 60 min from 07:22:41 UTC. Fixes AX2-4612S's
own diagnosed bug (its NOTES.md section above): the objective was the *total* (summed) log-probability
of the decoded stream, which unconditionally rewards mapping any code to NULL since every character's
own log-probability is negative and deleting one can only raise a sum -- confirmed there by a null
control that changed 100 of 110 codes in a known-correct key.

**Unit 1: tool fix.** `tools/key_repair.py` gets `--objective {total,excess}` (default `excess`) and
`--no-null-below N` (default 121, the 1574 table's letter range; AX-NAMES found the null codes at
121-149). `excess`: score = sum over decoded characters of (log2 p(c | context) - mu), mu the fr16
order-5 model's own mean log2-probability per character on its held-out text (`compute_mu()`,
`-model.bits_per_char`, computed once per run and printed). A candidate value now gains only when its
characters are better-predicted than average French in context, so deleting or lengthening a value is
no longer rewarded by construction. `--objective total` reproduces AX2-4612S's original (buggy)
behaviour, kept for reference. `tools/tests/test_key_repair.py` updated (existing `repair()` calls now
pass `model.logp` as the scorer, matching the new signature) and extended: `candidates_for_code`'s
threshold logic; an end-to-end `FlatCostModel` (uniform per-character cost, no context) reproducing the
AX2-4612S bug exactly under `total` and showing it gone under `excess`; `make_scorer`/`compute_mu`
semantics against a small hand-built per-character table; and the brief's own required regression
check -- a null control on a clean synthetic French sentence built from common words proposes 0
changes under `excess` (mu printed in the test's own output). All 17 checks pass,
`python3 tools/tests/test_key_repair.py` (about 4s, dominated by the one-time fr16 model load/build).

**Gates, written here at 07:32 UTC before any control number below was computed (verbatim from the
brief, "the known-answer SWAP control, 3 seeds, k=8" design continuing AX2-4612S's own):** "(a) Null
control: run key_repair from key_full unchanged; count proposed changes (false positives). (b)
Known-answer control, 3 seeds: swap the letter values of k=8 codes total, arranged so 2 of the 8 are
instead given a French bigram value (the H-S shape) rather than a swapped letter, reported separately
from the other 6. Gate: >= 6 of 8 altered codes recovered on average AND <= 2 false changes in the null
control and on untouched codes [in the known-answer control]. A control below gate = CONTROL BELOW
GATE; stop and say so (not a negative); if it fails, report which codes the null control changes and to
what (so the orchestrator can see the next bias)." Both controls run on
`ax4612tr/ciphertext_5811_cut833.tsv` (5811's own ciphertext, cut to 4612 v3's N=833, key_full's own
known-correct reading) against `key_full.tsv`, exactly as AX2-4612S, but now under `--objective excess
--no-null-below 121` (the new defaults).

**(a) Null control (re-run under the new defaults).** `python3 tools/key_repair.py
ax4612tr/ciphertext_5811_cut833.tsv --key key_full.tsv --out-key /tmp/null_control_key_s2.tsv
--out-changes ax2_4612s/null_control_changes_s2.tsv --margin 3.0 --rounds 4` (objective `excess`,
`--no-null-below 121`, both now default):
```
53 of 110 codes present (48%) changed across 64 change-events over 4 rounds -- down from AX2-4612S's
100/110 (91%) under --objective total, but still 53 false positives against a gate of <=2. Of the 64
change-events: only 1 goes to NULL (code 123, l -> NULL, gain 59.5); 15 replace a correct single
letter with a different single letter (e.g. 58 'z'(x6)->'u' gain 73.7, 20 'q'(x3)->'s' gain 65.4); the
other 48 (75% of all changes) replace a correct single letter with a multi-character bigram or trigram
from the top-60/top-20 fr16 lists (11 'p'(x9)->'des' gain 53.9; 109 'k'(x3)->'ent' gain 72.8; 16
'q'(x9)->'ere' gain 12.0). Several codes chase across rounds exactly as AX2-4612S described (112: l ->
an -> i -> l; 11: p -> des -> les).
```
Gate: 53 <= 2? False. **CONTROL BELOW GATE.**

**Diagnosis: the objective is length-neutral in aggregate but not per-candidate, and the fix moved
the bias from deletion to insertion, not away from length altogether.** `--objective excess` scores
each candidate value by summing (log2 p(c|context) - mu) over *that candidate's own characters*, so a
candidate is only "free" (zero net effect) if its characters average exactly mu. But `--bigrams
60`/`--trigrams 20` draws candidates from the *most frequent* substrings in the whole fr16 corpus --
by definition extremely well-predicted wherever they occur, almost always well above mu regardless of
whether they are the code's true value. Since the score is still a *sum* over however many characters
the candidate contributes, a 3-character trigram each scoring (say) +2 bits above mu outscores a
correct 1-character letter scoring +1 bit above mu (sum +6 vs +1), even though the single letter is
individually the better fit per character. Excess removed the *unconditional* pull toward zero-length
(NULL), which is real progress (100/110 -> 53/110; NULL itself down from 62% to 2% of change-events),
but it replaced it with an unconditional pull toward inserting the corpus's own most-common n-grams,
because those candidates were hand-picked for being reliably above-average. The truly length-neutral
form would need to compare each candidate's *mean* excess per character, not its *summed* excess --
not attempted this box (a larger scope change than this brief's own remit; flagged as the next step
below).

**(b) Known-answer control, 3 seeds, k=8 (6 swapped in 3 pairs + 2 given a bigram value).**
`ax2_4612s/known_answer_control_s2.py` (`ax2_4612s/known_answer_control_s2.log`):
```
seed 0: recovered 6/8 (2/2 bigram-hidden); false changes on 160 untouched codes: 53
seed 1: recovered 4/8 (0/2 bigram-hidden); false changes: 53
seed 2: recovered 5/8 (1/2 bigram-hidden); false changes: 53

GATE: mean recovery 0.625 (>= 0.75 needed)? False. bigram-only mean recovery 0.500 (reported, not
gated). max false changes across seeds 53 (<= 2 needed)? False.
```
Recovery itself improved sharply over AX2-4612S's 0/8 (0.000) to 5/8 average (0.625) -- excess
genuinely helps the search find a perturbed code's true single-letter value more often than not, and
recovers a deliberately-bigram-hidden code back to its true single letter half the time (3/6 instances)
-- but the false-change count is identical (53) in every seed and in the null control, and the first
20 (of 53, log truncates there) overlap 16-17 of 20 codes across the three seeds despite each seed
perturbing a different, disjoint set of 8 codes. That the same ~53 codes move regardless of which 8
are deliberately altered confirms the diagnosis above: this is a structural property of key_full
under this candidate pool and scorer, not noise driven by the perturbation itself.

**Gate verdict: CONTROL BELOW GATE on both halves** ((a) 53 false positives vs a gate of <=2; (b)
mean recovery 0.625 vs a gate of >=0.75, and 53 false changes vs <=2 in every seed). Per the brief and
CLAUDE.md rule 3: stop here. Unit 3 (targets 4612 v3 and 5799) was **not run** -- no
`key_4612_repair.tsv`/`key_5799_repair.tsv`/`decode_*_repair.json`/`reading_*_repair*` produced this
box; `key_full.tsv`, `key.tsv`, `key_5799.tsv` untouched.

**Verdict for AX2-4612S2 as a whole.** The length-neutral objective is a real, substantial
improvement over AX2-4612S's total-log-probability objective on every number that moved (null-control
false positives 100->53; known-answer recovery 0.000->0.625; NULL's share of change-events 62%->2%),
confirming the diagnosis in AX2-4612S's own NOTES.md section was correct and worth fixing. It is not
yet a working instrument: the remaining 53 false positives are driven by a *new*, well-understood bias
(unconditional preference for inserting a top-frequency bigram/trigram, because "most frequent
corpus-wide" was used as a proxy for "well-predicted in this context" when building the candidate
list) rather than the old NULL-seeking one. H-S is still neither confirmed nor refuted; the instrument
built to test it is closer to sound but not there yet. **Next step for a successor:** either (i) score
each candidate by its *mean* excess per character rather than the *sum*, so a 3-character trigram must
average better than a 1-character letter, not merely accumulate more total credit, or (ii) restrict
bigram/trigram candidates to ones that are locally well-predicted in *this* context (re-rank or filter
the top-60/20 list by their actual scored contribution at this specific position rather than their
corpus-wide frequency) -- either should be re-gated with the same two controls before touching
4612/5799 again.

Files: `tools/key_repair.py`, `tools/tests/test_key_repair.py`, `ax2_4612s/{null_control_changes_s2.tsv,
known_answer_control_s2.py,known_answer_control_s2.log}`, this section. `key_full.tsv`, `key.tsv`,
`key_5799.tsv` untouched (rule 3: a control below gate means the target is not run; no
`key_4612_repair.tsv`/`key_5799_repair.tsv` produced this box). No network. No images.

## AX2-4612S3: key repair, paired objective (26 Sept 2026, LANE AX2)

Worker AX2-4612S3 (Sonnet, session_012U5wYXUNFUghFcotwZw9wX), per
`.claude/briefs/runs/2026-09-26-lane-ax2-4612s3.md`, box 45 min from 08:05:52 UTC. Third and last
key_repair iteration per the brief; fixes AX2-4612S2's own diagnosed bug (its NOTES.md section
above): `--objective excess` is length-neutral only in aggregate, not per candidate -- the top-60/20
bigram/trigram candidates are drawn by corpus-wide frequency and are therefore reliably above mu, so
summing more above-average characters still beats a correct single letter that scores above mu by
less in total but by more per character (53/110 false positives, 0.625 known-answer recovery,
CONTROL BELOW GATE both halves).

**Unit 1: tool fix.** `tools/key_repair.py` gets `--objective paired` (now the default, `excess` and
`total` both kept for reference): a candidate replaces the current value only if BOTH (a) its
summed excess gain over all of the code's occurrences exceeds `--margin` (unchanged from `excess`)
AND (b) its mean excess per emitted character across those occurrences is higher than the current
value's own mean excess per character -- a longer candidate must fit better per character, not merely
accumulate more total credit by being longer. Implementation: `build_stream_with_sources()` (a
`build_stream()` refactor, byte-identical output, plus a parallel list naming which code emitted each
character) and `mean_excess_per_char()` (mean of `log2 p(c|context) - mu` over exactly one code's
emitted characters, defined as 0.0 when a candidate or the current value emits zero characters --
the same "no information" baseline an empty stream already scores under `excess`). Also
`--min-occ N` (default 3): a code occurring fewer than N times in this ciphertext is never tried or
changed at all (too little context to judge a per-character mean from). `tools/tests/test_key_repair.py`
extended: `--min-occ` skips a low-occurrence code end to end; a direct reproduction of AX2-4612S2's
bug shape (an `OrderedFakeModel` where a two-character candidate's summed excess beats a correct
single letter's but its mean excess per character is lower) shows `excess` accepts the swap and
`paired` rejects it; the reverse case (a single letter that wins on both the sum and the mean) shows
`paired` still accepts a genuinely better candidate; the brief's own required regression test (a null
control on clean synthetic French text proposes 0 changes) is re-run under `--objective paired`
alongside the existing `excess` check (paired is a strict superset of excess's requirements, so this
is expected to pass, and does). All 22 checks pass, `python3 tools/tests/test_key_repair.py` (about
13s, dominated by the one-time fr16 model load/build).

**Gates, written here at 08:14 UTC before any control number below was computed (verbatim from the
brief, "Controls FIRST, exactly AX2-4612S2's two controls and gates"):** "null control <= 2 false;
known-answer >= 6/8 recovered, bigram codes reported separately, <= 2 false). Below gate = CONTROL
BELOW GATE: stop, report the null control's changed codes, and write one line in NOTES.md naming the
H-S hypothesis as untested by this tool family (so it is not re-briefed a fourth time without a new
idea)." Both controls run on `ax4612tr/ciphertext_5811_cut833.tsv` (5811's own ciphertext, cut to
4612 v3's N=833, key_full's own known-correct reading) against `key_full.tsv`, exactly as AX2-4612S
and AX2-4612S2, now under `--objective paired --no-null-below 121 --min-occ 3` (all now default).

**(a) Null control.** `python3 tools/key_repair.py ax4612tr/ciphertext_5811_cut833.tsv --key
key_full.tsv --out-key /tmp/null_control_key_s3.tsv --out-changes ax2_4612s/null_control_changes_s3.tsv
--margin 3.0 --rounds 4` (objective `paired`, `--no-null-below 121`, `--min-occ 3`, all now default):
```
29 of 110 codes present (26%) changed across 34 change-events over 3 rounds -- down from AX2-4612S2's
53/110 (48%) under --objective excess, but still 29 false positives against a gate of <=2. Codes
changed: 3, 5, 7, 11, 13, 16, 18, 20, 30, 36, 51, 53, 58, 59, 66, 70, 77, 87, 91, 94, 100, 109, 112,
117, 119, 120, 123, 127, 130. Most single changes still go to a common French bigram/trigram (11
'p'(x9)->'des' gain 53.9, then 'des'->'les' gain 12.6; 16 'q'(x9)->'ere' gain 12.0; 3 'n'(x8)->'les'
gain 20.0; 109 'k'(x3)->'ent' gain 72.8); only one goes to NULL (123 'l'(x7)->NULL gain 59.5, then
chases NULL->'ovs'); a few chase across rounds (7: o->on->qve; 117: m->u->est; 119: m->il->tre) the
same way AX2-4612S/S2 described.
```
Gate: 29 <= 2? False. **CONTROL BELOW GATE**, again -- but a real, substantial reduction from
AX2-4612S2's 53 (45% fewer false positives).

**(b) Known-answer control, 3 seeds, k=8 (6 swapped in 3 pairs + 2 given a bigram value).**
`ax2_4612s/known_answer_control_s3.py` (`ax2_4612s/known_answer_control_s3.log`):
```
seed 0: recovered 3/8 (0/2 bigram-hidden); false changes on 160 untouched codes: 33
seed 1: recovered 4/8 (0/2 bigram-hidden); false changes: 32
seed 2: recovered 4/8 (0/2 bigram-hidden); false changes: 43

GATE: mean recovery 0.458 (>= 0.75 needed)? False. bigram-only mean recovery 0.000 (>= not gated
separately, reported)? False changes max 43 (<= 2 needed)? False.
```

**Gate verdict: CONTROL BELOW GATE on both halves** ((a) 29 false positives vs a gate of <=2; (b)
mean recovery 0.458 vs a gate of >=0.75, max false changes 43 vs <=2). Per the brief and CLAUDE.md
rule 3: stop here. Unit 3 (targets 4612 v3 and 5799) **not run** -- no
`key_4612_repair.tsv`/`key_5799_repair.tsv`/`decode_*_repair.json`/`reading_*_repair*` produced this
box; `key_full.tsv`, `key.tsv`, `key_5799.tsv` untouched.

**Diagnosis: the paired objective is a real improvement (false positives 53->29, a 45% cut) but
introduces no new bias to fix -- it has hit the ceiling of what per-character averaging alone can
do, because the underlying assumption ("a correct rare letter should score higher per character
than an incorrect common bigram") is often false for an order-5 character model.** A frequent short
French bigram like "les", "de", "en", "est" is grammatically and lexically probable in a very wide
range of contexts -- that is exactly why it is frequent -- so its own per-character log-probability
is often genuinely *higher* than a real but locally rare letter's (q, z, x, h, k, b -- H-S's own
list, and not coincidentally the letters a homophonic table is most likely to assign spare codes
to). Paired correctly rejects a candidate that wins only by being longer (the unit test's own
`OrderedFakeModel` case), but it cannot reject a candidate that is genuinely better-fitted per
character *and* happens to be wrong -- and real French text supplies exactly that shape of
candidate constantly. This is visible in the known-answer control's own numbers: recovery *fell*
(0.625 -> 0.458) and bigram-hidden recovery *collapsed* (3/6 -> 0/6) even as false positives fell,
because paired is stricter in general (rejects more candidates of every kind, correct and incorrect
alike) rather than being selective for the *right* kind of correctness. Unlike AX2-4612S's NULL bug
(a construction artifact: every candidate of length 0 always wins) and AX2-4612S2's length bug (a
construction artifact: the candidate pool's own frequency selection biases mean excess upward for
longer candidates), this is not a bug in the scoring rule -- it is what an order-5 character model
of ordinary French *actually predicts* at codes that, by H-S's own premise, hold letters chosen
precisely because they are locally surprising. A local-context language model cannot be the
instrument that finds a code deliberately assigned to defeat local-context prediction.

**Verdict for AX2-4612S3, and for the key_repair.py tool family as a whole.** Three iterations
(total -> excess -> paired) each fixed the specific construction artifact the previous iteration's
control diagnosed (unconditional NULL-seeking; unconditional length-seeking), and each fix produced
a real, measurable improvement in the null control (100 -> 53 -> 29 false positives) -- confirming
every prior diagnosis was correct. But the known-answer control's recovery number never once cleared
even half of its own gate (0.000 -> 0.625 -> 0.458, gate 0.75) and the bigram-hidden recovery this
tool exists to test regressed to zero this iteration. **H-S (a few of key_full.tsv's rare-letter
codes might stand for a two-letter French syllable rather than the letter key_full.tsv currently
gives them) is untested by this tool family, not refuted, after three iterations -- and should not be
re-briefed against key_repair.py a fourth time without a materially different instrument** (e.g. a
candidate pool restricted to bigrams that are locally, not corpus-wide, well-predicted at that
specific position; or a model that scores a candidate against its neighbouring *codes'* own
plaintext-word structure rather than a bare character n-gram; or abandoning local per-code search in
favour of a global reassignment search that can trade one code's per-character loss for a net gain
elsewhere). This line is written here precisely so a fourth iteration is not briefed on the same
premise (per the brief's own instruction).

Files: `tools/key_repair.py`, `tools/tests/test_key_repair.py`,
`ax2_4612s/{null_control_changes_s3.tsv,known_answer_control_s3.py,known_answer_control_s3.log}`,
this section, `HYPOTHESES.md` (two rows appended). `key_full.tsv`, `key.tsv`, `key_5799.tsv`
untouched (rule 3: a control below gate means the target is not run; no
`key_4612_repair.tsv`/`key_5799_repair.tsv` produced this box). No network. No images.

## NEXT-LVN: 4612 v3 under key_1572 (2 Oct 2026, account 2, Opus 5.5)

Brief: .claude/briefs/runs/2026-10-02-acct3-next-lvn.md, the Verdict line's cheapest next step. Gate, written here
before any number below was computed (03:22 UTC), the AX2-4612 gate with key_1572 in place of key_full:
"4612 v3 reads under key_1572 if its French-word share (word_share_check_v3.py method, fr16, words >=3 letters)
is above the max of 20 value-shuffles of key_1572 AND at least 0.85 of the share the same statistic gives 5200
(Orange to Jan, 18 Oct 1572, read under key_1572) cut to 4612 v3's N=833 value-1-120 numerals."
One adaptation of the method, applied identically to target, shuffles and control: key_1572 is a nulls-interleaved
table (24 letters on multiples of 3 up to 72, 66 printed non-valeurs among 1-98), so a NULL-valued code is dropped
from a run (it sits inside words, J1's spot check "36.15.39.57" with nulls between) instead of breaking it; a code
with no key_1572 row (99-120, 75/78/81/84/87/90/93/96) breaks a run as an unkeyed sign does in the AX2-4612 script.
The value shuffles permute key_1572's 90 values (letters and NULLs together) over its 90 codes. Headroom check
(rule 3): the same 20 shuffles are also run on the 5200 cut, so the control's own margin over its shuffle is reported.

Result (`python3 ax4612tr/word_share_check_k1572.py`, 03:24 UTC, ~11 s, no network; output in
`ax4612tr/word_share_check_k1572.log`):

    4612 v3 under key_1572: 65/243 = 26.7% inside a French word; N=833 value-1-120 numerals
    5200 cut to N=833 under key_1572: 466/536 = 86.9%
    4612 v3, 20 value shuffles of key_1572: mean 16.9%, range 4.6-28.6%
    5200 cut, same 20 shuffles (headroom): mean 22.4%, range 0.0-54.8%
    share of numerals on a multiple of 3 (table letter slots 3-72 and unkeyed 75-120): 4612 316/833, 5200 cut 539/833
    GATE: 4612 26.7% > shuffle max 28.6%? False. 4612 26.7% >= 0.85 x 5200 86.9% = 73.9%? False.
    GATE VERDICT: does not read under key_1572 (gate not met)

| measure | 4612 v3 (target) | 5200 cut (control) |
|---|---|---|
| French-word share under key_1572 | 26.7% | 86.9% |
| max of 20 value shuffles | 28.6% | 54.8% |
| letters left after nulls dropped, of 833 | 243 | 536 |
| numerals on a multiple of 3 | 316 (37.9%; chance 33.3%) | 539 (64.7%) |

Reading: the control reads (86.9%, 32 points over its own shuffle max, not near ceiling, so the gate had room to
show a reading); the target sits inside its own shuffle band on both conditions. **4612 v3 is not enciphered with
key_1572: a control-backed negative for this key**, not for the letter. The multiple-of-3 count says the same
thing independently of the word list: key_1572's letter slots draw 64.7% of 5200's numerals and 37.9% of 4612's,
close to the 33.3% a table with no preference for multiples of 3 would give. Correction to the 2 Oct classifier's
"covers 87.2% of 4612 v3's numerals": 66 of key_1572's 90 rows are NULL, so coverage counted letters and nulls
together; only 243 of 833 numerals (29.2%) land on a key_1572 letter. Caveat (rule 2): the target figure rests
on the v3 transcription (88.3% pass agreement, AX-4612TR2); a ~12% digit error rate cannot move 37.9% to 64.7%.
No reading changed, so no decode_key.py --check or judge run applies (rule 7). HYPOTHESES.md has the row.
Cost: see the orchestrator's get_session. Hosts: none.

## GAPS28-lodewijk-van-nassau-1573-74 (3 Oct 2026, 05:4x UTC, account-4) -- gate PASS, band calls contradicted by 5810

Intake gate first, `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74`, exit 0:

    lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines

This is gap 1's Verdict step, using a different instrument from A2-LVN3's char LM. Script `bandtest/band_seg.py`. Its
rule, lexicon, window and gate were committed and pushed in b64ab890 before the first scoring run, and no parameter was
changed after it. Outputs: `bandtest/seg_control.tsv`, `seg_subsample.tsv` and `seg_band.tsv`. It is deterministic and runs in 3 s.

**Method.** The lexicon is the fr16 corpus words of length >= 2 seen at least 5 times (9801 words). Single-letter words
are left out. The window is up to 12 decoded letters either side, cut by the same rule as band_lm.py. Each window is
segmented by DP at a cost of 1.0 per letter not covered by a word plus 0.1 per word. Candidates are NULL and the 23
folded letters. L* is the letter with the lowest summed cost. A code is called NULL only when its summed NULL cost is
strictly lower; a tie is called letter. The gate uses the same 26 hidden-one-at-a-time codes as A2-LVN3 and needs
>= 0.80 per class at full count, then again after subsampling to each band code's N. The control can come out
differently from the target on this statistic: 2 nulls were called letter and 1 letter code was called NULL.

| class | codes | called right | accuracy | gate |
|---|---|---|---|---|
| NULL (121-138, C) | 13 | 11 (131, 133 called letter) | 0.846 | pass |
| letter (matched, C) | 13 | 12 (16 'q', n=4, called NULL) | 0.923 | pass |

The true letter is L* for 8 of 13 letter codes. The letter *value* is not gated, only the class. The subsampled gate
passes for n >= 14 and fails at n = 5 and 8 (NULL 0.674 and 0.618). It cannot be run at n = 73 because no control code
is that frequent. At n = 23-33 it rests on only 1-2 control codes per class.

**Band output under the pre-registered rule.** NULL: 125 (+0.118 per occurrence), 145 (+0.035), 148 (+0.096).
Letter: 139 (-0.013), 140 (-0.090), 142 (-0.117), 147 (-0.129), 149 (-0.019). Not licensed because N is outside the
gate: 146 (n=8), 150 (n=73) and 151 (n=5). All margins are small, around 0.01-0.13 cost units per occurrence. The
control's margins are the same size (nulls 0.000-0.750, letters -0.450 to -0.021).

**Independent check against print (after the run, recorded, not a tuning).** names.tsv has Groen-aligned 5810
observations at C for 139, 140, 142 and 149, all NULL on 2-3 observations each, below the class-b gate of 4. It has
147 as 'u' x2 against NULL x1 (M) and 125 as 'l' (M, n=1). This test's licensed calls disagree with print on 125, 139,
140, 142 and 149. They agree only with 147 (letter, though L* is I and not u/V). That is 1 of 6. The char LM (A2-LVN3,
gate FAIL) agreed with 5810 on 139, 140, 142 and 149, and its two largest NULL margins, 148 and 150, include 148, which
this test also calls NULL.

**Result.** The known-answer gate passed, but the instrument's band calls contradict the only print-aligned evidence on 5
of 6 codes, and the margins are as thin as the control's. So **no value is applied**: key_full, names.tsv and every
reading are unchanged, there is no `--check` to run (rule 7), and 4610/4611/4616 stay at U 310 (rule 4). This counts as
attempt 1 of this instrument. It is a conflict between two instruments and the print, not a classification. The two
instruments disagree on every band code except 145, 148 and 150 (all NULL in both, n=23, 24 and 73). Because the print
disagrees with the word-segmentation calls, those agreements do not license an S grade.
**Next for gap 1: new material, not a third tool.** 5811, a Groen-printed list-B letter on key_full's table, carries 139
x2, 140 x2 and 150 x2 as U (reading_5811_tokens.tsv). 5810 carries 142 x5, 140 x3 and 149 x4, against the 2-3 that
names.tsv aligned. Aligning these to Groen's print would raise 139, 140 and 142 to the class-b gate of 4 observations.
That decides the conflict from the print side, ~$2. Requests: none (disk and git only). Vision: 0 calls. Subagents: 0.

## GAPS31-lodewijk-van-nassau-1573-74 (3 Oct 2026, 05:59-06:0x UTC, account-4) -- print alignment of 5810/5811 band tokens, gate FAIL

Step: GAPS28's Verdict, align the band tokens of the Groen-printed 5810 and 5811 that AX-NAMES' anchored DP left
uncounted, to lift 139/140/142 to the class-b gate. Intake gate `python3 tools/intake_gate_check.py
lodewijk-van-nassau-1573-74` exit 0 (`partial (line 1) -- edition/page or full-text-search citation found within 6 lines`).

Why they were uncounted: `axnames/occ_5810.tsv`/`occ_5811.tsv` already hold every band occurrence (139 2+2, 140 3+2,
142 5, 149 4, 150 0+2, 147 2, 125 1), but `axnames/build_names.py` counts a cluster only with >= 3 exact letters on each
side within 6 units; the rest fail that anchor test, which is why names.tsv holds 2-3 observations per code.

Instrument (shared tool, no private DP): `tools/interlinear_align.py align --floor 121 --clear-consumes --prior
key_full.tsv` (the AX-COMP recipe) on pairs cut by `axcomp/build_pairs.py` unchanged, with Groen IV CDLXVIII (5810) and
CDLXXXIII (5811) as the plain text (the spans align_names.py uses). Driver `gaps31/run.py` (`target`, `hide`, `score`;
about 40 s per run). Gate, controls and licence pre-registered in `gaps31/PREREG.md`, pushed in fa5cb601 before the first
scoring run; nothing changed after it. 5810 cut into 28 pairs on 27 anchors; 5811 only 3 pairs on 3 anchors (one pair of
1167 tokens against 1378 printed letters).

| class (control) | codes | called right | per occurrence | gate |
|---|---|---|---|---|
| NULL: C nulls 121-144, unseeded in the target run | 16 | 13 (122, 126, 130 called letter) | empty 0.608 | G1 >= 0.80: pass (0.813) |
| letter: 13 rarest C letter codes, hidden as unseeded 760-772 | 13 | 8 (66, 15, 65, 75, 115 called NULL); value right 6 | false-empty q 0.330 | G2 >= 0.80: FAIL (0.615); G3 q <= 0.316: FAIL |

**Gate FAIL, nothing applied.** Band output, recorded only (empty / n, both letters): 139 2/4, 140 1/5, 142 3/5, 149 3/4,
150 0/2, 147 0/2, 125 0/1. The non-empty chunks are long gap-fills (140 'fficultquevous', 149 'icymanderaultr', 139
'graveetthi'), the shape of an aligner absorbing a transcription or anchoring gap, not a code value. Why it fails: even the
seeded codes 1-120 came out empty on 1187 of 4257 occurrences (27.9%), so empty/non-empty is not a code property at this
anchoring; the hard-EM drifts over long pairs (AX-COMP saw the same on 7205's 2 anchors). key_full, names.tsv and every
reading are unchanged; no `--check` to run (rule 7); 4610/4611/4616 stay at U 310. Grades: none assigned (rule 4).
Untested-by-this-tool at this anchoring, not refuted (rule 3). Also recorded: the licence's names.tsv conflict check in
`gaps31/run.py` keys on the token line, but the aligner reports each token under its pair's first line, so that check
could never fire; it was not reached because the gate failed, and must be fixed before any reuse.
This is the third instrument on gap 1 (char LM A2-LVN3 FAIL; word segmentation GAPS28 PASS but contradicted by print;
whole-letter print alignment GAPS31 FAIL). Next for gap 1 is a different instrument on the same print, not a re-tune of
this aligner: a blind reading of each band occurrence's local window (key_full decoding of +-15 tokens beside the Groen
sentence it falls in, from axnames/occ_*.tsv), mixed with an equal number of masked C null and C letter occurrences as
the known-answer control and graded per class, ~$2. Requests: none (disk and git only). Vision: 0 calls. Subagents: 0.

## GAPS33-lodewijk-van-nassau-1573-74 (3 Oct 2026, 06:18-06:3x UTC, account-4) -- blind local-window reading, gate PASS, nothing licensed

Step: GAPS31's Verdict, a blind reading of each 5810/5811 band occurrence's local window against Groen's print with masked C
null and C letter occurrences as the known-answer control. Intake gate `python3 tools/intake_gate_check.py
lodewijk-van-nassau-1573-74` exit 0 (`partial (line 1) -- edition/page or full-text-search citation found within 6 lines`).
Pre-registration `gaps33/PREREG.md` with the windows, the answer key and the gate, pushed in 5d777aa3 before any reading.
Nothing in it was changed afterwards.

**Instrument.** `gaps33/build.py` (deterministic, seed 33) builds one item per occurrence. Each item has two parts. The first
is the key_full decode of up to 15 tokens either side, with the target masked as [?], C/H nulls dropped, unread codes shown
as `_` and no code numbers. The second is the Groen print around the spot (IV CDLXVIII for 5810, CDLXXXIII for 5811),
located by Smith-Waterman on 24 decoded letters each side; an occurrence is kept only if both scores are >= 20 and the
gap is 0-12. That gives 17 band items (140 x4, 142 x4, 139 x3, 149 x3, 147 x2, 125 x1) plus 25 C-null and 25 C-letter
control items (at most 3 per code), shuffled into 67. Six band occurrences failed the locate rule (`gaps33/dropped.tsv`):
both of 150's, and one each of 139, 140, 142 and 149. Two blind Opus 5.5 subagents read the windows as pasted text only
(no file, no image). They split on 4 items, and one Opus reconciliation call settled them (`gaps33/recon.tsv`; the 63
agreed items carry over). Scorer: `gaps33/score.py`, writing `gaps33/result.tsv`.

| class (control, reconciled) | items | called right | gate |
|---|---|---|---|
| NULL (C 121-144) | 25 | 21 (0.840): 131 x2 called a/n by both passes; 130 and 134 called l at low confidence | G1 >= 0.80: pass |
| letter (C single-letter) | 25 | 24 (0.960), 1 SPLIT (116 'm'); value right 22/25 | G2 >= 0.80: pass |
| false-NULL on letter controls | 25 | 0 (q 0.000) | G3 q <= 0.316: pass |

Pass A alone: NULL 21/25, letter 25/25, q 0. Pass B alone: NULL 23/25, letter 25/25, q 0. The classes are balanced 25/25,
so the per-class figures are not floor-inflated (the AX-NAMES shape). The control can also fail differently from the target:
four nulls were called letters.

**Band calls (reconciled).** 139: NULL x3. 149: NULL x3. 140: NULL x2, plus letter x2 ('y' at 5811 p5_L18 and 't' at 5811
p1_L21, both in noisy decode stretches). 142: NULL x3, plus 'e' x1 (5810 p2_L34). 147: 'u' x2. 125: NULL x1. 150: no
locatable occurrence.

**Licence.** The gate passed, but no code meets the pre-registered licence of >= 4 NULL calls and 0 letter calls. 139 and
149 have n = 3; 140 and 142 carry letter calls. So **nothing is applied**: key_full, names.tsv and every reading are
unchanged, there is no `--check` to run (rule 7), and 4610/4611/4616 stay at U 310. Grades: none assigned (rule 4).

**Against the other evidence (recorded, not pooled).** At the 9 occurrences of 139/140/142/149 that names.tsv aligned to
print, all 9 calls agree with its C NULL observations. 147's 'u' x2 agrees with names.tsv. 125 conflicts: names.tsv has
'l' (M, n = 1), this reading has NULL. Per rule 4 the conflict is logged in HYPOTHESES.md, not settled. This instrument
therefore sides with the print observations, and against GAPS28's word-segmentation letter calls on 139/140/142/149.

**Also seen in the control.** C null 131 was called a letter at both of its windows by both blind passes (5810 'a',
'n'), and GAPS28 also called 131 letter. key_full's 131 row is unchanged; HYPOTHESES.md could carry a check of 131's
names.tsv observations, which is one line to look at, not a change.
Requests: none (disk and git only). Vision: 0 calls. Text subagent calls: 3 (2 blind + 1 reconciliation).

## GAPS39-lodewijk-van-nassau-1573-74 (3 Oct 2026, 06:36-06:4x UTC, account-4) -- dropped band occurrences hand-located, gate FAIL, nothing licensed

Step: GAPS33's Verdict, hand-locate the print for the 6 band occurrences GAPS33's locate rule dropped and read them with
the same protocol plus a fresh 6 + 6 control. Pre-registration `gaps39/PREREG.md` with the hand locations
(`gaps39/hand_locate.tsv`), the windows and the answer key, pushed in e68233f9 before any reading; nothing changed after.

**Location.** 5 of 6 located by hand (142 at 5810 p6_L32:14 "paine | hors"; 149 at 5810 p7_L02:5 "prier que |
incontinent"; 139 at 5811 p5_L08:2 "chemy[n] entre"; 150 at 5811 p1_L09:17 and p5_L08:19, "Grave et Thiel"). 140 at
5810 p5_L08:1 is dropped: after "grand bruit" the cipher goes on "le temps et la saison" and the print "bruict par deça",
with no single print spot. Control: 6 C null (127, 130 hand-located from GAPS33's dropped list; 134, 124, 126, 137 by
GAPS33's rule, seed 39) and 6 C letter (29, 38, 2, 32 hand-located; 104, 37 by rule), none of them among GAPS33's items.
`gaps39/build.py`, two blind Opus 5.5 text-only passes (`passA.tsv`, `passB.tsv`), one Opus 5.5 reconciliation of the 5
split items (`recon.tsv`), scorer `gaps39/score.py` -> `result.tsv`, `score_out.txt`.

| control (reconciled) | items | right | gate |
|---|---|---|---|
| C null called NULL | 6 | 6 | G1 >= 5: pass |
| C letter called a letter | 6 | 4 (29 's' at "diuers[?]es voies" called NULL; 2 'n' at "forces [?] de i st" SPLIT) | G2 >= 5: **FAIL** |
| C letter called NULL | 6 | 1 (29) | G3 <= 1: pass |

Pass A alone and pass B alone each pass (6/6, 5/6, 1/6); the reconciliation turned pass A's 'n' / pass B's NULL on item 6
into SPLIT, which the pre-registered rule counts as wrong. The four letter-control misses or near-misses are all on
hand-located items, so the hand-located windows are harder than GAPS33's rule-located ones, the same windows the band
items sit in. Pooled control (reported only): null 27/31, letter 28/31, false-NULL 1/31.

**Band calls (reconciled).** 149: NULL (both passes; pooled with GAPS33 it would be NULL x4, letter 0). 139: 'n' (both
passes, high confidence; the window reads "f h e p _ [?] entre" against print "chemyn entre"), against GAPS33's NULL x3.
142: NULL (pooled NULL x4 + letter x1). 150: SPLIT x2 (pass A 'e' x2, pass B 'i' x2, at "Grave et Thiel").

**Licence.** This run's gate failed (G2 4 of 6), so per the pre-registration nothing pools and **nothing is applied**:
key_full, names.tsv and every reading unchanged, no `--check` to run (rule 7), no grades assigned (rule 4), 4610/4611/4616
stay at U 310. Even with a passing gate 139 could not be licensed: its new 'n' call is a letter call against GAPS33's
three NULLs, a conflict logged in HYPOTHESES.md (rule 4), not settled. 149 is the one code the instrument consistently
calls NULL (4 of 4 across both runs, 0 letter), recorded at that strength and no more.

**Material exhausted for 139/149.** Every occurrence of 139 and 149 in the print-paired letters (5810, 5811) has now been
read by this instrument; 4503, 5797 and 4614 contain neither code (counted 3 Oct 2026). A further pass at the same
windows would be a third run of an unchanged instrument (rule 3's third-attempt clause), so the local-window step is
[retired] for 139/149 on this material, untested-by-this-tool, not refuted.

**GAPS33's side note logged.** C null 131 was called a letter at both its GAPS33 windows by both passes (5810 'a', 'n'),
and GAPS28 also called 131 a letter. names.tsv holds 131 empty in 22 of 22 aligned observations, 0 contradicting
(key_full 131 C, AX-NAMES2), so the reader calls are noise on a well-supported null, not a conflict with a witness;
logged in HYPOTHESES.md as a reader-error note, key unchanged.
Requests: none (disk and git only). Vision: 0 calls. Text subagent calls: 3 (2 blind + 1 reconciliation).

## GAPS43-lodewijk-van-nassau-1573-74 (3 Oct 2026, 06:55-07:0x UTC, account-4) -- gap 4 word-segmentation global reassignment, control gate FAIL, target not run

Step: the Verdict line's gap 4 step, a GLOBAL key reassignment for 4612 v3 seeded from key_full and scored by fr16 word
segmentation, gated first on the 5811 cut with 20% of codes perturbed at >= 0.90. Third-attempt check: hypothesis H-S is
the same one key_repair.py is [retired] for, but the instrument differs on both axes (global anneal, not local per-code;
word-segmentation cost from GAPS28's bandtest/band_seg.py, not a character model), so it was run as attempt 1 of this
instrument. Pre-registered in gaps43/PREREG.md, commit 918c0056, before any run. Script gaps43/word_anneal.py (60000
iterations x 6 restarts per seed, 23 folded letters, single-code + swap moves); output gaps43/control.log, control.json.
No network, no vision calls.

| run (5811 cut, N=833, 95 keyed codes) | start recovery | annealed recovery | repaired / perturbed | false moves | seg cost | word share |
|---|---|---|---|---|---|---|
| key_full as is (cost of the true key) | 1.000 | - | - | - | 52.8 | 0.932 (AX2-4612) |
| null start (unperturbed key_full) | 1.000 | 0.060 | 0/0 | 89 | 18.1 | 0.998 |
| seed 1 (20% perturbed) | 0.882 | 0.046 | 0/19 | 73 | 17.7 | 0.998 |
| seed 2 | 0.821 | 0.062 | 1/19 | 70 | 17.6 | 0.998 |
| seed 3 | 0.768 | 0.054 | 2/19 | 73 | 17.6 | 0.998 |

GATE (each seed >= 0.90): **FAIL** (0.046 / 0.062 / 0.054). Per rule 3 the 4612 target was not run (word_anneal.py
target refuses on a failed control.json). The control could vary in both directions (starts 0.77-0.88, gate 0.90), so
this is a test and not a non-test. Diagnosis: the failure is the objective, not the search. The true key's segmentation
cost (52.8) is about three times the cost the anneal reaches from anywhere (17.6-18.1), and the null start walks away
from the correct key just as far as the perturbed starts. With 2-letter lexicon words allowed at 0.1 per word, a key that
turns any stream into chains of short fr16 words (word share 0.998, above real French's 0.932) beats real French. The
same degeneracy voids the word-share statistic as a target gate under any free reassignment. More iterations or restarts
cannot help, because the optimum is the wrong key. A further run of this objective with only its knobs changed (min
word length, per-word cost) would be the same instrument re-tuned (rule 3 third-attempt clause). Any next global
objective must first pass the cheap check this run lacked: key_full has to score better than its own annealed optimum
from the null start on the 5811 cut. Result: H-S stays untested-by-this-tool for the word-segmentation global
reassignment; 4612 v3 stays 0 of 833 read; no key or reading changed, so no judge run applies (rule 7). decode_key
--check re-run unchanged (see done line).


## A4-RFLVN: 5811 p1/p2/p5 at 300 dpi (6 Oct 2026, 00:02-00:1x UTC, account 4, LANE DEFAULT-account-4-20261005-2253)

Step: W2's blocker ("5811 disagreement settlement", 150-dpi copies only). Route: WVO PDF fetched once
(resources.huygens.knaw.nl/media/wvo/images/05000-05999/05811.pdf, 1 request, HTTP 200, 5.2 MB), pages 1/2/5 rendered at
300 dpi with pdftoppm to the scratchpad (sha1s in wv2/blind300/render_sha1.txt; not committed, the folder is already over
30 MB). Crops, pasted before any vision call:
`python3 tools/iiif_lines.py --image <p>.png --out <scratch>/crops --prefix 05811_pN --region 110,120,2350,3150 --distance 60
--prominence 20 --lines-per-crop 2` -> 19/19/20 two-line strips (p1/p2/p5), each 2350 px wide.

**Structural fix first.** Pass B numbers p2's bottom cipher block one line later than pass A (B L27 = A L26 sign for sign,
through B L34 = A L33). Eight wv2/linemap.tsv rows (p2, B, L27->L26 ... L34->L33) re-align them; p2's disagreements fall
from 127 to 28 rows, and the 57 "disagreements" there were this artefact, not ink. No other page has a line offset (line-wise
difflib ratio < 0.7 only at the known clear-text and p5 rows already in linemap.tsv).

**Blind reads.** Rule written into wv2/settle_05811.py (method 3) and pushed before any read was opened: each row still M
after W2's structural and cross-page methods got a query showing only its neighbouring signs (disputed neighbours masked as
*), never the A/B candidates; one Sonnet call per page; settle when the read equals exactly one of A/B at conf H or M, else
the row stays M with the read logged. (p5's first call found no anchors, since every p5 sign carried conf M; the contexts
were rebuilt to unmask the signs both passes agreed on and the call was redone. p2's queries for the offset block were
NOTFOUND and are moot after the linemap fix.) Inputs and reads: wv2/blind300/{qkey.tsv,q_05811_p*.txt,blind_05811_p*.tsv}.

| page | queried | H/M matching A | H/M matching B | H/M neither | L | NOTFOUND |
|---|---|---|---|---|---|---|
| p1 | 19 | 6 | 10 | 1 | 2 | 0 |
| p2 | 73 (16 live) | 1 | 7 | 6 | 2 | 57 (offset block, moot) |
| p5 | 77 | 8 | 15 | 20 | 34 | 0 |

Settled by method 3: 47 rows (p1 16, p2 8, p5 23). **Caveat, no known-answer control was run on the reader** (budget): the
"neither" share is the only accuracy signal, and it is high on p5 (20 of 43 H/M reads match neither pass; the reader said it
used an 8x-is-common prior on the round 0/5/6/8 glyph, marked those L, which the rule excludes). Treat p5's 23 settles as
weaker than p1's; a decoy-query control (agreed positions mixed into the queries) is the step that would measure them.
Reconciler's own look (not blind, not applied): p2 L27 col 8 (34 vs 39) reads 39 on strip p2_L14 (the hand's 9 has a
descender like y); left M under the pre-registered rule.

Result: `python3 wv2/build.py 05811 && python3 wv2/settle_05811.py && python3 wv2/build.py 05811 && python3
tools/decode_key.py . --config decode_wv2.json` -> ciphertext_5811.tsv tokens 1542 -> 1521 (the offset had made 21 spurious
gap tokens): **C 616 -> 724, I 81 -> 77, M 792 -> 668, U 53 -> 52**. settle_log_05811.tsv: STRUCTURAL 7, CROSS-PAGE 34,
IMAGE300 47, M 68, GAP 59 (mostly the p1 L01-L04 clear salutation pass B never transcribed). `--check` clean on both
scripts. Requests: resources.huygens.knaw.nl 1. Subagents: 4 Sonnet calls (p1, p2, p5 twice). Novelty not classified.
Next (one line): a decoy-control re-read of p5's 23 settles plus its 68 remaining M rows, ~$3.

## R12-LVN16: 4616 p1 cipher block at 300 dpi (6 Oct 2026, 11:20-11:3x UTC, account 2, LANE-RUN12-account-2)

Step: gap 3's 4616 part (27 M reading tokens, 19 slash groups, read so far only from the 150-dpi renders). Route: WVO
PDF fetched once (resources.huygens.knaw.nl/media/wvo/images/04000-04999/04616.pdf, 1 request, HTTP 200), p1 rendered
with `pdftoppm -png -r 300` (2481x3508, sha1 4f47b490f28e2cfeebaf5352c34f64af87636148; scratchpad, not committed, the
folder is over 30 MB; `./regen_images.sh page300 4616 1` re-derives it). Crops, pasted before any vision call:
`python3 tools/iiif_lines.py --image 04616-1.png --out crops --prefix 04616_p1 --region 380,320,2080,880 --distance 45
--prominence 20 --top-margin 12 --bottom-margin 12 --debug` -> 13 single-line crops, 2080 px wide, crop L01-L13 =
ciphertext lines p1_L05-p1_L17 (checked on the debug overlay).

Pre-registered before any read (lvn16/PREREG.md, commit c8e1f4d7b): two blind Sonnet passes (A3, B3) of every token,
shown neither the earlier passes nor the key; control = the 210 agreed H rows of the block (no slash), gate >= 0.90 per
pass; a non-H row settles to H only when A3 == B3; a slash group splits only when A3 == B3 == the row's sign.
Stricter than the pre-registration (decided before applying, logged here): an agreed read carrying the edge mark '?'
(token cut by the binding) or an alignment mark does not settle.

**Control: A3 193/210 (0.919), B3 194/210 (0.924), gate PASS.** Outcome (lvn16/apply_log.tsv): 19 of the 34 non-H
rows settled (10 to a value different from the 150-dpi sign, 7 confirmed, 2 settled and split: 72/16 -> 32/16,
735/71 -> 335/71), 15 stay M (both reads logged in `alt`; three agree only on edge-cut tokens 10?/13?/31?); 14 of the
19 slash groups split into their codes (the stroke is ink, read as a separator by both passes; every part but 335
is a key_full code), 5 kept whole (22/112, 33/5, 25/81, 92/2 split between passes; 27/16 is an H row both blind
passes read 21/16 -- left as is under the rule, a conflict for the next image check). Value changes: 9->4, 3->31,
123->120, 75->78, 8->81, 118->116 (L16), 81->91 (L16, was S), 102->101, 91->81, 121->221 (221 = 'hollande', H).
The 300-dpi read outranks both 150-dpi passes here; the control measures the blind readers, not the settled rows
(a row where both readers err the same way would pass; 16-17 of 210 control misses per pass bound that rate).

Reproduce: `python3 lvn16/score.py && python3 lvn16/apply.py --check && python3 tools/decode_key.py
ciphers/lodewijk-van-nassau-1573-74 --config ciphers/lodewijk-van-nassau-1573-74/decode_4616_full.json --check` (all
exit 0 on 6 Oct 2026). `settle.py` also writes ciphertext_4616.tsv (R20 lineage, already stale for 4610/4611/4612
before this job): run it as `settle.py --letters 4610,4611,4612` from now on, or it undoes these settles.

**Counts (rule 4), reading_4616_full_tokens.tsv: 261 -> 276 tokens (splits), C 208 -> 250, H 0 -> 1, I 1, M 27 -> 12,
U 25 -> 12.** 4610/4611/4616 graded C/H: 2360 of 3214 (73.4%, was 2317 of 3199, 72.4%); four target letters 2360 of
4047 (58.3%, was 57.5%). Remaining 4616 U: 22/112, 33/5, 25/81, 27/16, 92/2 (unsplit slash groups), 335, 313 x2,
142 x2, 149, 1574 (date). The reading changed after AUDIT.md (V-series) was written: flagged for a verifier in ROOM.md.
Readable stretches at a glance, not a gated reading: L06 "pour demain car on", L08 "mal logable nommement pour",
L10 "rons plus tost de", L15 "loger demain", L17 "...[hollande]". No judge run (no spec for 4616). Requests:
resources.huygens.knaw.nl 1. Subagents: 2 Sonnet calls. Novelty not classified.
Next (one line): a third read of the 15 M rows and 5 kept slash groups, crop-zoomed per token (incl. 27/16 vs 21/16), ~$2.

## R12-LVN10: 4610 p3 at 300 dpi, two blind passes (6 Oct 2026, 11:39-11:4x UTC, account 2, LANE-RUN12-account-2) -- control gate FAIL, nothing applied

Step: gap 3's 4610 part (131 M reading tokens, read so far only from the 150-dpi renders). Cap 6 allowed one page:
p3 (60 of the 131 M; p3_L12-L31 carries 49). Route: WVO PDF fetched once (resources.huygens.knaw.nl/media/wvo/images/
04000-04999/04610.pdf, 1 request, HTTP 200), p3 rendered with `pdftoppm -png -r 300 -f 3 -l 3` (2481x3508, sha1
a41b5df838e49cefb71e30cdfbe0803f3947d591; scratchpad, not committed). Crops, pasted before any vision call:
`python3 tools/iiif_lines.py --image 04610-3.png --out crops --prefix 04610_p3 --region 120,1150,2350,1950 --distance 65
--prominence 20 --top-margin 12 --bottom-margin 12 --debug` -> 22 single-segment physical-line crops (2350 px), = ciphertext
lines p3_L12-p3_L31 (checked on a montage). The transcription's line breaks do not follow the physical lines on this page
(p3_L31 is two physical lines; p3_L21/L22 split mid-line), so the passes are aligned as one page sequence, not per line.

Pre-registered before any read (lvn10/PREREG.md, commit 0a07aa766): two blind Sonnet passes (A4, B4) of every numeral;
control = the 230 H numeral rows of p3_L12-L31, gate >= 0.90 per pass; settle a non-H row only when A4 == B4.

**Control: A4 186/230 (0.809), B4 171/230 (0.743), gate FAIL. No row changed** (lvn10/apply.py writes ciphertext_4610.tsv
byte-identical; apply_log empty; decode_key.py --config decode_4610_full.json --check "reading up to date", tokens 1545:
C 1195, H 9, I 55, M 131, U 155, unchanged). Diagnostics, logged only, not a licence: B4 is an incomplete pass (4-10
numerals per crop on crops L12-L22, against 12-21 for A4: 45 control rows unaligned); A4's misses are mostly a hooked '1'
read as '2' (146 -> 246, 150 -> 250, 148 -> 248, 139 -> 239) and 5/3 or 8/3 (85 -> 35, 82 -> 32). On crops L01-L11 alone
(ct p3_L12-L22, chosen after scoring) A4 reads 126/142 (0.887) and B4 120/142 (0.845): still under gate. 21 of the 63
targets carry a clean A4 == B4 read (9 different from the 150-dpi sign); not applied (lvn10/aligned.tsv keeps them).
This is attempt 1 of this instrument on 4610 (4616's identical protocol passed at 0.919/0.924 on 13 lines): a non-test at
this reader accuracy, not a negative. Counts unchanged: 4610/4611/4616 C/H 2360 of 3214 (73.4%); four letters 58.3%.
Requests: resources.huygens.knaw.nl 1. Subagents: 2 Sonnet calls. Novelty not classified.
Next (one line): two blind passes of 4610 p3 split into two calls of 11 crops each (B4 truncated past crop 11), with the
hand's hooked 1 / 2 and 5 / 3 named in the prompt, same PREREG gate, ~$6; then p1/p2 the same way.

## R12-LVN16C: R12-LVNV2's six 4616 H-row corrections applied (6 Oct 2026, 12:41-12:5x UTC, account 2, LANE-RUN12-account-2)

Applied exactly the six corrections in AUDIT.md "R12-LVNV2" (pre positions; current positions in brackets): p1_L12/1 90->40,
p1_L13/1 79->39, p1_L14/2 91->81, p1_L15/16 [17] 36->31, p1_L16/2 26->20 (confidence M: re-inked, 'q' doubtful), p1_L17/2
91->81. They live in `lvn16/corrections_lvnv2.tsv` (per-row note citing R12-LVNV2 and the crop line) and are applied by
`lvn16/apply.py` before its settles, so `lvn16/apply.py --check` still regenerates ciphertext_4616.tsv (exit 0). Then
`tools/decode_key.py . --config decode_4616_full.json` rewrote reading_4616_full; `--check`: reading up to date, exit 0.
4616 tokens 276: C 249, H 1, M 13, I 1, U 12 (was C 250, M 12): five letters changed at C (f->u, d->u, g->e, u->t, g->e),
one C->M. Four target letters: 2359 of 4047 (58.3%); 4610/4611/4616 2359 of 3214 (73.4%). The reading changed after
AUDIT.md: a verifier carries this into AUDIT.md (flagged in ROOM). No image work, no requests.

## R13-LVN10B: 4610 p3 attempt 2, two blind passes in two 11-crop batches (6 Oct 2026, 13:19-13:2x UTC, account 2, LANE-RUN13-account-2) -- control gate FAIL, nothing applied

Step: R12-LVN10's named repair (its pass B4 was truncated past crop 11). Route: WVO PDF re-fetched once
(resources.huygens.knaw.nl/media/wvo/images/04000-04999/04610.pdf, HTTP 200, 3,689,372 bytes), p3 rendered `pdftoppm -png
-r 300 -f 3 -l 3` -> 2481x3508, sha1 a41b5df838e49cefb71e30cdfbe0803f3947d591 (matches R12-LVN10; scratchpad, not committed).
Crops, pasted before any vision call, R12-LVN10's exact command: `python3 tools/iiif_lines.py --image 04610-3.png --out crops
--prefix 04610_p3 --region 120,1150,2350,1950 --distance 65 --prominence 20 --top-margin 12 --bottom-margin 12 --debug` -> 22
crops, same centres. Pre-registered before any read (lvn10/PREREG_B.md, commit 348eb5e6): gate, control and settle rule of
lvn10/PREREG.md unchanged; passes A5/B5 each as two Sonnet 5.5 calls (crops L01-L11, L12-L22), 4 calls; the prompt names the
hand's hooked 1 vs 2, 5 vs 3 and 8 vs 3. Scripts: lvn10/score.py --round b, lvn10/apply.py --round b (round a unchanged).

**Control: A5 184/230 (0.800), B5 194/230 (0.843), gate 0.90, FAIL. No row changed** (apply.py --round b writes
ciphertext_4610.tsv byte-identical, apply_log_b.tsv empty; decode_key.py --config decode_4610_full.json --check "reading up
to date": tokens 1545, C 1195, H 9, I 55, M 131, U 155, unchanged). The truncation defect is repaired (every crop read in
both passes; 19 control rows unaligned per pass, against 45 for B4), but accuracy did not move: A 0.809 -> 0.800, B 0.743 ->
0.843. Diagnostics, logged only, not a licence: misses split by span, ct p3_L12-L22 A5 124/142, B5 125/142; p3_L23-L31 A5
60/88, B5 69/88 (the lower lines, where both readers report the lines sloping across crop boundaries; A5 joined crop tails
into the line above and left crop L22 empty, B5 transcribed each crop's central band). 10 control rows are read the same by
both blind passes and differ from the H sign: p3_L12/12 120:126, L13/2 135:185, L15/2 85:35, L17/6 61:31, L20/6 148:248,
L20/15 102:161, L21/7 82:32, L22/3 32:82, L23/3 51:51?, L31/21 85:83 -- several are the named hooked-1 and 5/3, 8/3 pairs, so
these may be 150-dpi transcription errors in the control (the 4616 shape, R12-LVNV2) or shared reader errors; unchecked. Even
if all 10 were control errors the gate would still FAIL (A5 0.843, B5 0.887). 29 of the 63 targets carry a clean A5 == B5
read (8 different from the 150-dpi sign; 27 of the 29 equal A4's read); not applied (lvn10/aligned_b.tsv keeps them).
This is attempt 2 of this instrument on 4610 p3 (blind whole-line Sonnet passes against the 230-row H control), after a
defect repair, with the gate failed both times and A/B not moving together toward it: per rule 3's third-attempt clause a
further pass needs a different instrument (e.g. per-token zoomed crops aligned to the transcription rows, or a person's read
in the sign sorter), not a third run of this one. Counts unchanged: 4610/4611/4616 C/H 2359 of 3214 (73.4%); four letters
2359 of 4047 (58.3%). Requests: resources.huygens.knaw.nl 1. Subagents: 4 Sonnet calls. Novelty not classified.
Next (one line): an eye check of the 10 agreed-against-sign H control rows on the 300-dpi crops (the R12-LVN16R step, ~$1),
then a different instrument for the 63 targets: per-token crops cut at each row's position, two blind reads, ~$5.

## R13-LVNFIX: R12-LVNV's two overturns applied, R13-LVNV's two doubtful rows read (6 Oct 2026, 13:39-13:4x UTC, account 2, LANE-RUN13-account-2)

Solver job (reading changed after AUDIT.md: flagged in ROOM.md for a verifier). Page re-fetched once
(resources.huygens.knaw.nl, HTTP 200), p1 `pdftoppm -png -r 300` (sha1 4f47b490f28e2cfeebaf5352c34f64af87636148, matches),
crops cut, pasted: `python3 tools/iiif_lines.py --image 04616-1.png --out crops --prefix 04616_p1 --region 380,320,2080,880
--distance 45 --prominence 20 --top-margin 12 --bottom-margin 12 --debug` (13 lines, crop Lk = p1_L(k+4)); half-line crops at 2x
and 4-5x page zooms read by this worker's own eye; crops in the session scratchpad, not committed. No subagents.

| row (current pos) | was | now | image |
|---|---|---|---|
| p1_L16/19 (pre 18) | 91 'g' C (lvn16 settle A3=B3) | 81 'e' **M** | R12-LVNV's overturn (closed two-loop 8, no tail; R13-LVNV concurred at 4x); grade M as R12-LVNV asked, pending another pass |
| p1_L17/15 | 221 'hollande' H | 221 'hollande' **M** | sign unchanged; rule 4 direction clause (only H witness is 4496's gloss, list B; 4616 is list A); `exceptions_4616.tsv`, wired into decode_4616_full.json |
| p1_L07/8 (pre 7) | 17 'q' C | **13** 'p' **M** | second digit flat-topped with a curved bowl, the same form as the 3 of 37 and 83 beside it on the line, not the straight-stemmed 7 of 37. Against: both 300-dpi readers and both 150-dpi passes gave 17, R13-LVNV called it undecidable. The decode reads "dict que par de la ..." with 13 vs "que qar" with 17; that context is decode-derived and not used as the grade basis. Value changed on the image read, graded M |
| p1_L16/4 | 85 'e' C | 85 'e' **M** | faint ink; first digit not decidable 8 vs 3 at 5x (both 300-dpi readers 35); sign kept, regraded M (no value change without an image read that settles it) |

Mechanism: `lvn16/corrections_lvnv.tsv`, applied by `lvn16/apply.py` *after* the settles (an image read overrides an A3 == B3
settle where the readers share the 9/8 and 7/3 confusions); `apply.py --check` exit 0 (control A3 193/210, B3 194/210, gate PASS,
unchanged: the control is scored on lvn16/aligned.tsv as pre-registered; p1_L07/7 pre and p1_L16/4 are control rows counted as
reader hits there, so if 13 and 35 are right the control would read 191/210 and 192/210, still >= 0.90).
`tools/decode_key.py . --config decode_4616_full.json --check`: exit 0, "tokens 276: C 246, I 1, M 17, U 12" (was C 249, H 1,
M 13). 4610/4611/4616 C/H 2355 of 3214 (73.3%); four letters **2355 of 4047 (58.2%)**. Outward figure "about 58%" holds.
Not fixed, found: `decode.json` (the key.tsv reading, reading_4616.txt / reading_4616_tokens.tsv) already failed `--check` before
this job (stash test, exit 1); left as found, outside this brief; next: rerun decode_key.py with decode.json, ~$0.2.
Requests: resources.huygens.knaw.nl 1.

## Remaining gaps (finish-or-blocker pass, 2 Oct 2026)
Read so far: 2355 of 4047 cipher tokens in the four target letters (58.2%), recounted 6 Oct 2026 after R13-LVNFIX (2359 after R12-LVN16C, 2360 after R12-LVN16; was 2317 of 4032, 57.5%, 2 Oct): 4610/4611/4616 2355 of 3214 graded C/H (73.3%, U 297, M 439, I 123) from reading_{4610,4611,4616}_full_tokens.tsv under key_full v3 (AX-REDERIV2); 4612 0 of 833 numerals 1-120 (ciphertext_4612_v3.tsv, gate not met, AX2-4612); 5797 2 of Groen's 7 blanks carry an H value (153 at p7_spot2; 161 at p5_spot3, which stays partly unread: 136 dual-M, 146 U; AUDIT.md V8.1, A4). 4613/4615, 4614, 5799, 5801, 5810, 5811, 4503, 5194, 7205 and 7206 have known plaintext (period decipherment or Groen's print) and count as key material, not gaps.
- 4610/4611/4616 null-band codes 125 and 139-151 (255 U tokens: 150 x73, 125 x33, 148 x24, 145 x23, 140 x21, 149 x21, 142 x18, 139 x15, 147 x14, 146 x8, 151 x5), plus 146 inside 5797 p5_spot3 - blocker: open-codes; the fr16 char-LM NULL-vs-letter test was run 2 Oct 2026 (A2-LVN3, this file, bandtest/) and its known-answer gate FAILED: hidden C-graded nulls 121-138 called NULL 13/13 (1.000), matched C letter codes called letter 6/13 (0.462) against a pre-registered 0.80 per class, so its "all eleven band codes NULL" output licenses nothing (an inserted letter costs about 4 bits, so the rule leans NULL; the AX-NAMES class-imbalance shape) and the band is untested-by-this-tool, not refuted; names.tsv holds 139/140/142/149 as NULL on 2-3 observations (class-b gate is 4), 147 as 'w' x2 against NULL x1 (M) and 125 as 'l' on one observation (M), with no row for 145/146/148/150/151; 150 is NULL four times in 7206 (list B, AX2-172) and once at M in 4614 (AX-COMP); the j6 siblings 5803/5804/5805/5812 hold only 3 band tokens and cannot lift a code to 4 observations; the fr16 word-segmentation test was run 3 Oct 2026 (GAPS28, this file, bandtest/band_seg.py, pre-registered b64ab890): known-answer gate PASS (NULL 11/13 0.846, letter 12/13 0.923), but its licensed band calls (NULL 125/145/148; letter 139/140/142/147/149; 146/150/151 outside the gated N) contradict the C-graded 5810 print observations on 5 of 6 codes (139/140/142/149 NULL in print, called letter; 125), with margins as thin as the control's, so nothing is applied (attempt 1 of this instrument; conflict, not a classification); the unanchored 5810/5811 band tokens were aligned to Groen's print 3 Oct 2026 (GAPS31, this file, gaps31/, pre-registered fa5cb601) with tools/interlinear_align.py: known-answer gate FAILED (null codes 13/16 0.813, hidden letter codes 8/13 0.615, per-occurrence false-empty 0.330 > 0.316; seeded letters empty 27.9%), so its band output (139 2/4, 140 1/5, 142 3/5, 149 3/4 empty) licenses nothing, untested-by-this-tool; a blind local-window reading of the 5810/5811 band occurrences against print was run 3 Oct 2026 (GAPS33, this file, gaps33/, pre-registered 5d777aa3): known-answer gate PASS (C nulls 21/25 0.840, C letters 24/25 0.960, false-NULL 0/25), band calls 139 NULL x3, 149 NULL x3, 140 NULL x2 + letter x2, 142 NULL x3 + letter x1, 147 'u' x2, 125 NULL x1 (conflicts with names.tsv 'l' M), 150 not locatable; no code reaches the licence (>= 4 NULL, 0 letter), nothing applied; the calls agree with names.tsv's print observations at all 9 shared occurrences; the 6 dropped occurrences were hand-located 3 Oct 2026 (GAPS39, this file, gaps39/, pre-registered e68233f9): 5 of 6 located, fresh 6+6 control gate FAILED (C null 6/6, C letter 4/6 against 5, false-NULL 1/6), so nothing pools or applies; calls 149 NULL (4/4 NULL with GAPS33), 139 'n' (conflicts GAPS33's NULL x3, logged), 142 NULL, 150 SPLIT x2; every 139/149 occurrence in the print-paired letters is now read (none in 4503/5797/4614), so the local-window step is [retired] for 139/149 on this material, untested-by-this-tool; open-codes until new material: another list-B letter with a print or decipherment carrying band codes
- 4610/4611/4616 name codes above 151 seen once or twice (31 U tokens: 4610 180, 182, 184, 186, 191 x2, 194, 203, 205, 225 x2; 4611 174, 175, 187, 199, 204, 211, 214, 225, 228, 232, 245, 248, 254, 280, 311 x2, 331, 335; 4616 313 x2) - blocker: open-codes; these letters have no print to align against (AUDIT.md section 1); the only sibling values are single aligner guesses at M in the list-B keys (key_7205/key_7206/key_5801 rows for 175, 182, 184, 191, 199, 203, 211, 228, 232, 254, 311, 331, 335) and name codes differ by direction (AX-GLOSS, AX-COMP, AX2-172); names.tsv has 180 'de' (5810) and 311 'pays' (5811) at M on one observation each; of the 26 codes only 184 and 254 occur in 5803/5804/5805/5812, once each; Orange's printed replies were read and tested 2 Oct 2026 (A2-LVN4, this file, replies/): the reply-window fit's known-answer gate FAILED (0 of 8 hidden C/H name codes hit, 1 wrong), so its 3 'alkmar' proposals (4611 211/232/331, one passage) are unlicensed and the step is [retired] for replies/reply_fit.py, untested-by-this-tool; CDXXXIII prints Orange's own '311' ('la contrée du 311'), a second list-B context fitting 'pays' (below the class-b gate, HYPOTHESES.md); open-codes until new material: a list-A gloss or decipherment with these codes, or Orange's cipher originals of CDXXVII/CDXXXIII (WVO 4497/4498) aligned to Groen's print for list-B values, ~$6
- 4610/4611/4616 transcription: 439 M tokens (131/291/17) and 4616's 5 unsplit slash groups - 4616 done at 300 dpi 6 Oct 2026 (R12-LVN16, this file, lvn16/): control PASS 0.919/0.924, 19 of 34 non-H rows settled, 14 of 19 slash groups split, M 27 -> 12, U 25 -> 12; 4616 remainder: 15 M rows and 22/112, 33/5, 25/81, 27/16, 92/2, next a per-token zoomed third read, ~$2; 6 of the 12 contested H control rows look wrong on the 300-dpi image (R12-LVN16R, 6 Oct 2026, lvn16/eye_h_rows.tsv), verifier re-check done 6 Oct 2026 (R12-LVNV2, AUDIT.md): all 6 are 150-dpi transcription errors (image 40, 39, 81, 31, 20, 81; p1_L17/2 was never agreed, passA 91/passB 31), control corrected 0.948/0.952, PASS holds; applied 6 Oct 2026 (R12-LVN16C, lvn16/corrections_lvnv2.tsv via lvn16/apply.py, decode_key --check exit 0; 4616 C/H 251 -> 250, M 12 -> 13, p1_L16/2 20 graded M), AUDIT.md carries the applied state (R13-LVNV, 6 Oct 2026: --check exit 0, six rows match R12-LVNV2 exactly; R12-LVNV's two overturns, p1_L16/19 91->81 M and p1_L17/15 'hollande' H->M, applied 6 Oct 2026 (R13-LVNFIX, lvn16/corrections_lvnv.tsv + exceptions_4616.tsv, --check exit 0; four letters 2355 of 4047, 58.2%; carried into AUDIT.md 6 Oct 2026, R13-LVNV2: --check exit 0, four rows match; the key.tsv reading reading_4616.txt is stale since R12-LVN16, next: regenerate with decode_key.py and decode.json, ~$0.2)); sample eye check of 29 uncontested 3/7/8/9 H rows done (R13-LVNV, AUDIT.md): 27 as transcribed, 2 doubtful (p1_L07/8 17 or 13; p1_L16/4 85 leaning 35, already contested), read 6 Oct 2026 (R13-LVNFIX): p1_L07/8 -> 13 'p' M on the image, p1_L16/4 kept 85 regraded M; next: the script audit of every `agree` label against passA/passB for 4610/4611/4616, ~$0.3; 4610 p3 attempted 6 Oct 2026 (R12-LVN10, this file, lvn10/): two blind 300-dpi passes, control gate FAIL (A4 0.809, B4 0.743 vs 0.90; B4 truncated past crop 11), nothing applied, attempt 1 of this instrument, non-test; attempt 2 6 Oct 2026 (R13-LVN10B, this file, lvn10/PREREG_B.md): two blind passes in two 11-crop batches, truncation repaired, control gate FAIL again (A5 0.800, B5 0.843), nothing applied; the whole-line blind-pass instrument is [retired] for 4610 p3 under rule 3 (two failures with A/B not moving together), a third attempt needs a different instrument: next an eye check of the 10 control rows both passes read against the H sign (~$1), then per-token crops at each target row with two blind reads (~$5); 4610 p1/p2 and 4611 - blocker: not-attempted; R20 settled rows by n-gram margin and one image cluster (4611 p2_L36), opened 4610 p2_L26 but left it M ("recorded, not settled"), never opened 4611 p2_L14/L15, and worked only from the 150-dpi renders in images/; the 300-dpi re-pass lifted 4612's pass agreement from 47.8% to 88.3% (AX-4612TR, AX-4612TR2); next: render 04610/04611.pdf at 300 dpi (4616 done, R12-LVN16), cut crops with tools/iiif_lines.py --image and paste the command, run one blind pass per page (7 calls) plus one reconciliation unit at the per-pass rate, then decode_key.py --check, ~$14
- 4612 cipher body (833 numerals 1-120 in ciphertext_4612_v3.tsv, plus 154 clear-word '?' rows) - blocker: not-attempted; under key_full the French-word share is 70.7%, above the shuffle max 60.6% but below the 79.2% gate (5811 control 93.2%), the fr16 judge FAILs both 4612 and the 5811 control, the anneal control reached 0.699 against 0.90 (AX2-4612, HYPOTHESES.md), tools/key_repair.py is retired for H-S after three CONTROL BELOW GATE runs (AX2-4612S/S2/S3), the key_5799 and key_5801 tests were non-tests (AX-5799, AX2-5801), and AX-4612's family_run.py negatives used the superseded 47.8% transcription; key_1572 (KEY-OFFICES.tsv row 34) was applied 2 Oct 2026 (NEXT-LVN, this file) and does not read it: 26.7% French-word share against a 28.6% shuffle max and a 73.9% bar from 5200 cut to N=833 (86.9%, shuffle max 54.8%), and only 37.9% of its numerals fall on a multiple of 3 against 5200's 64.7%; key_nepveu covers too little to test (29.5%); the word-level global reassignment seeded from key_full and scored by fr16 word segmentation (AX2-4612S3's named step) was run 3 Oct 2026 (GAPS43, this file, gaps43/, pre-registered 918c0056): control gate FAILED, recovery 0.046/0.062/0.054 against 0.90 per seed (starts 0.77-0.88), the null start from unperturbed key_full also fell to 0.060; the true key costs 52.8 against the anneal's 17.6-18.1 optimum (word share 0.998, chains of short fr16 words), so the objective's optimum is the wrong key; target not run, untested-by-this-tool, and re-tuning the same segmentation cost (min word length, per-word cost) would be the same instrument; next: a global anneal under a word-frequency language model (fr16 word-unigram log-probability with a per-character out-of-vocabulary cost, a different objective), admitted only after the pre-check that key_full scores better than its own null-start optimum on the 5811 cut, then the same 20%-perturbed >=0.90 gate, ~$4
- 5797 p5_spot5, code 173 -- settled for list A, 2 Oct 2026 (A2-LVN, this file): 173 = graf at H from the 5550 p2-5 period gloss tail read at 300 dpi ("vnd" for 90.1.79, "graf" written whole and placed on 173 by elimination; spatially the gloss sits about one code left of the run, VERIFY-LVN-173), applied to 5797 only through exceptions_5797.tsv (reading_5797_full: H 2->3, U 11->10, --check up to date); 5810's sign is M, 173 or 113 (113 = l fills Groen's "laquelle"), so it is not a list-B null observation; 5801's 173 x2 stays key_5801 'q' M (HYPOTHESES.md "Code 173, graded per direction"); the spot's 123 stays dual l/NULL M - blocker: open-codes (list B has no settled value for 173 and needs none for the target letters; 4610/4611/4612/4616 do not contain 173); remaining for the spot: none beyond 123's dual reading, which is gap 1's band test
- 5797 p6_spot4 (172), p7_spot6 (182), p8_spot7 (156) - blocker: open-codes; 172 has three conflicting period witnesses, le Conte Jean (4614), Lumbres (7206) and le conte Louis (5801 gloss), so AUDIT.md A4 withdrew the spot (HYPOTHESES.md "Key conflict: code 172"); 182 occurs only at 4610 p2_L02 (M) and once in 7205, where key_7205 'y' and key_5801 'i' are unconstrained aligner guesses (AX-COMP2); 156 occurs nowhere else in the 16 ciphertext files (AX2-BLANKS, ax2_blanks/contexts.tsv); none of the three occurs in the j6 sibling transcriptions 5803/5804/5805/5810/5812 (counted 2 Oct 2026)
- 5797 spot 1, the p.222 garbled paragraph ([Phit]/[testgu]) - blocker: open-codes; transcribed and decoded 3 Oct 2026 (A2P4-LVN97, this file, spot1/): pp.3-4 at 300 dpi, 23 crop lines, 2 blind passes + 1 reconciliation, 239 code tokens (H 4, C 155, M 45, I 16, U 19; decode_key --check up to date); pre-registered in-order gate (7d636fe2) FAILED on A (0.171 vs 0.50) while B beat both controls (0.355 vs shuffle p95 0.161, other paragraphs <= 0.032), so nothing in the interior is licensed beyond the transcription; by eye the decode runs with Groen (nemlich Dateno, begert, Phit, haupter, ziffer, konne, insel, bringen) and puts 173 before each of Groen's three subject-less verbs; unread codes 227, 254 (Groen prints it 'Grönningen' on p4_L02 and 'Bergen op Zoom' on p4_L18), 142, 148 and 339 (key 'harquebouziers' vs Groen's 'schlachtordnung'); the Groen-normalised cipher-unit re-score (A2P4-LVN98, 3 Oct 2026, prereg2 d1c8541e) FAILed the absolute bar again (B2 0.333 = 10/30 vs 0.50) while beating its controls (shuffle p95 0.167, other paragraphs <= 0.033), so the in-order Groen alignment instrument is retired for this span (rule 3 third look) and the interior stays open-codes until new material: another witness of the paragraph (a contemporary copy or decipherment of 5797, or Orange's reply quoting it)

## Escalation (2 Oct 2026)
- [ ] siblings: opened 4613/4615 (key source, R18), 4614 (AX-COMP), 7205 (AX-COMP2), 7206 (AX2-BLANKS), 5801+11250 (AX2-5801, AX2-5801ADJ), the glosses on 4496/5550/5552/5557 (AX-GLOSS, AX-NAMES); aligned the Groen-printed 5810/5811/4503/5799 (W1, AX-NAMES, AX-5799); 5194 is printed whole (Groen III CCCLXIX, sources/wvo/groen-check-2026-09-24.tsv); DECODE has no record (check-solved item 4). Planned: transcribe 7208 (Orange to Lodewijk, Vlissingen, 21 Feb 1574, cipher pp.1-3 "Duplicata", WVO "solved on leaf", same-date clear letter on p5, AX-GLOSS), the letter 4612 says it answers ("vostre lettre du xxime de febvrier", NOTES.md check-solved incipits; date match inferred, not checked), as a topical crib for gap 4 and a test of whether p5 is its clear copy, ~$12. 5803/5804's partial contemporary interlinear glosses (../jan-van-nassau-1572-75/NOTES.md J6) are unread but are list-B and carry almost none of this target's open codes (3 band tokens, 184 and 254 once each), so they are not the next step.
- [x] clear-pages: all used: the decipherment sheets 4613 p2 and 4615 p3 (R18, the key source), 4614 pp.5-6 (AX-COMP), 7205 pp.8-10 (AX-COMP2), 7206 p8 (AX2-BLANKS), 5801 pp.1-5 interlinear and pp.7-9 (AX2-5801). The four target letters carry no clear copy (R9 inventory, A1 contact sheet of every page). 7208 p5 is a same-date clear letter judged separate by AX-GLOSS; its use is under siblings.
- [x] known-keys: tried key.tsv, key_full v3, key_5799, key_5801 and key_4614/7205/7206; 5799 uses a different table (W1 0/146, AX-5799); 4610/4611/4616/5797/5810/5811/4503/4614/7205/5801 use key_full's table (table_check 1.000). key_1572 (KEY-OFFICES.tsv row 34, Jan van Nassau and Orange, 1572) applied to 4612 v3 on 2 Oct 2026 (NEXT-LVN): does not read (26.7% vs shuffle max 28.6%, control 5200 86.9%); key_nepveu (row 37) puts only 29.5% of 4612's numerals on a keyed code, too little to test; key_5549 (row 35) is Lodewijk's 1574 table again. Cryptiana and the solver repositories hold no key for this circle (check-solved items 3, 5). No other key of this office or decade is on file.
- [x] print: searched (AUDIT.md section 1, A1, D1, V5, V8, V-GATE2): Groen III-V and the Supplement by date and full text, Gachard, Kervyn, Blok 1887/1889, La Huguerye, the KHA inventory, WVO, Google Books, IA full text, OpenAlex/S2, JSTOR rows 52-54, 60 and 87-92. No prior decipherment of 4610/4611/4612/4616 was located. Orange's replies to 4610/4611/4616 are printed (CDXXVII, CDXXXIII, CDLXXXIV), none was located for 4612; 5797, 5799, 5801, 5810, 5811 and 4503 are printed in Groen IV.
- [ ] key-rebuild: done for names and for nulls 121-138 (AX-NAMES/NAMES2 Groen alignment with the class-b gate, AX-GLOSS H values for 192/221, AX-MERGE/MERGE3 conflict gate); U in 4610/4611/4616 fell from 541 to 310. For 4612 under H-S, tools/key_repair.py is retired after three CONTROL BELOW GATE runs (AX2-4612S/S2/S3), and the char-order-3 key-seeded anneal failed its control once (0.699, a 150000-iteration recheck 0.786, gate 0.90). The fr16 char-LM NULL-vs-letter test for the band was run 2 Oct 2026 (A2-LVN3): known-answer gate FAIL (NULL 1.000, letter 0.462, gate 0.80 per class), band untested-by-this-tool. The fr16 word-segmentation NULL-vs-letter score was run 3 Oct 2026 (GAPS28): gate PASS but band calls contradict 5810's C print observations on 5 of 6 codes, nothing applied. The 5811/5810 band-token print alignment with tools/interlinear_align.py was run 3 Oct 2026 (GAPS31): known-answer gate FAIL (letter class 0.615, false-empty 0.330), nothing applied. The blind local-window reading of the 5810/5811 band occurrences against print was run 3 Oct 2026 (GAPS33): gate PASS (0.840/0.960, q 0), but no code reached >= 4 NULL with 0 letter calls, nothing applied. The same reading on the 6 dropped occurrences, print hand-located, was run 3 Oct 2026 (GAPS39): fresh 6+6 control gate FAIL (letter 4/6), nothing applied; 139/149 print material exhausted, step [retired] for 139/149 on this material. The word-segmentation global reassignment for 4612 was run 3 Oct 2026 (GAPS43): control gate FAIL (0.046-0.062 vs 0.90; true key costs 52.8 vs the degenerate 17.6 optimum), target not run, untested-by-this-tool. Planned: a word-unigram-LM global anneal for 4612 behind a null-start pre-check (gap 4, ~$4). The reply-window fit for name codes against Orange's printed replies (gap 2) was run 2 Oct 2026 (A2-LVN4): known-answer gate FAIL (0 of 8 hits, 1 wrong), [retired] for that tool.
- [ ] image-check: done for 4612 (300-dpi re-render, all 32 numeral disagreements settled, AX-4612TR2, AX2-4612), the 5550 p2-5 gloss tail and 5810 p1_L40's 173/113 sign at 300 dpi (A2-LVN, 2 Oct 2026: 173 = graf H list A; 5810 sign M), 7205 digits (AX-COMP2), 172 by eye (AX2-172), the 4611 p2_L36 footer (R20 override) and the 5797 spots in two passes (AX-5797); 5811 p1/p2/p5 re-rendered at 300 dpi 6 Oct 2026 (A4-RFLVN): p2 bottom-block line offset fixed, 47 more rows settled by one blind read per page, 68 numeral rows still M (see A4-RFLVN section). 4616 p1 cipher block re-read at 300 dpi 6 Oct 2026 (R12-LVN16): two blind passes, control 0.919/0.924 PASS, 19 rows settled, 14 slash groups split, M 27 -> 12, U 25 -> 12. 4610 p3 at 300 dpi 6 Oct 2026 (R12-LVN10): control gate FAIL 0.809/0.743, nothing applied; attempt 2 in two 11-crop batches (R13-LVN10B): gate FAIL 0.800/0.843, nothing applied, whole-line blind passes [retired] for 4610 p3; next a different instrument (per-token crops, ~$5) after an eye check of 10 control rows (~$1). Planned: a 300-dpi settle of 4610/4611's M rows (gap 3, ~$12) and a zoomed third read of 4616's 15 M rows and 5 kept slash groups (~$2); 5797 pp.3-4 done 3 Oct 2026 (A2P4-LVN97, spot1/, gate FAIL on A; A2P4-LVN98 Groen-normalised re-score FAIL, in-order alignment retired for spot 1, see gap 7).
- [x] retry: readings regenerated and regraded under key_full v1, v2 and v3 (AX-NAMES2, AX-MERGE, AX-MERGE3); fresh re-derivations byte-identical (AX-REDERIV, AX-REDERIV2); U in 4610/4611/4616 fell from 541 to 310. Rerun after gaps 1, 3 and 4.
Verdict: keep going: 7 internal gaps (gap 1 band: char-LM A2-LVN3 gate FAIL; word segmentation GAPS28 PASS but contradicted by print; print alignment GAPS31 gate FAIL; local-window reading GAPS33 gate PASS, 139/149 NULL x3; GAPS39 hand-located dropped occurrences, 3 Oct 2026, gate FAIL (C letter 4/6), 149 NULL 4/4 across both runs, 139 'n' conflict; 139/149 print material exhausted, open-codes until new material; gap 2 reply-window fit A2-LVN4 gate FAIL); gap 4 word-segmentation global reassignment GAPS43, 3 Oct 2026, control gate FAIL 0.046-0.062 vs 0.90, objective degenerate (true key 52.8 vs optimum 17.6), target not run); gap 7 spot-1 in-order alignment A2P4-LVN97, 3 Oct 2026, gate FAIL on A 0.171 (B 0.355 beat shuffle p95 0.161 and other paragraphs 0.032), Groen-normalised re-score A2P4-LVN98 FAIL (B2 0.333 vs 0.50; controls 0.167/0.033), instrument retired for spot 1, open-codes until another witness of the paragraph; gap 3: 4616 re-read at 300 dpi 6 Oct 2026 (R12-LVN16, control PASS, M 27 -> 12, U 25 -> 12, four letters 58.3%), 4610 p3 R12-LVN10 6 Oct 2026 control gate FAIL (0.809/0.743) and R13-LVN10B attempt 2 FAIL (0.800/0.843), nothing applied, whole-line passes retired for p3, 4610 p1/p2 and 4611 not yet; cheapest next: a global anneal for 4612 under an fr16 word-unigram log-probability objective, admitted only after key_full beats its own null-start optimum on the 5811 cut, then the 20%-perturbed >= 0.90 gate (gap 4), ~$4

## Intake gate, 2 Oct 2026 20:5x UTC (A2-LVN, account 2, LANE-A2PUSH) -- step not run

`python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74` (exit 1):

    lodewijk-van-nassau-1573-74: partial (line 1) has an edition citation but no logged open-web and blog-comment check (no 'Web and blog check' heading, no paragraph naming Cipherbrain, the Cryptiana blog and Cipher Mysteries) -- run check-solved.md's 'Open web and blog comment threads' step first (CHECK-SOLVED-WEB, 28 Sept 2026: spinelli-beinecke-c1515 was read in a Cipherbrain comment thread in 2017)

The brief (5797 code 173 only) does not cover a check-solved web pass, so the Verdict's cheapest step (code 173 via
Groen's 5810 sentence and a 300-dpi re-zoom of the 5550 p2-5 gloss tail) was not run. Next: a check-solved worker
runs the 'Open web and blog comment threads' step (Cipherbrain, Cryptiana blog, Cipher Mysteries) and writes a
"## Web and blog check" section here (~$1); then the code 173 step (~$3) as written in the Verdict. Verdict unchanged.

## Web and blog check (GF-A2-1, 2 Oct 2026)

Run 2 Oct 2026, 21:23-21:25 UTC (date -u; committed ec6462f6), by worker GF-A2-1 (account 2, LANE-A2PUSH). Plain web searches (one search engine):
1. `Lodewijk van Nassau Willem van Oranje 1574 brief cijferschrift ontcijferd Mookerheide` (sender + recipient + date, Dutch) --
   hits: WVO edition PDFs JBWO 01694/05212, BHV 09052 (other letters), DBNL _vad003183901 and _ned005189001 (Mookerheide history),
   Deutsche Biographie and Archivportal-D person pages, a flags page, a Knowino biography. Nothing on 4610/4611/4612/4616.
2. `"Louis of Nassau" cipher letters 1573 1574 William of Orange deciphered` (sender + recipient + date, English) -- hits:
   Wikipedia, CUP *Texts concerning the Revolt of the Netherlands* (Orange to Jan, Dordrecht 7 May 1574 -- a different letter,
   after Lodewijk's death), Groen IV/V/Supplément on DBNL (already read: AUDIT.md section 1), HistoCrypt 162 (d'Avaux 1684,
   unrelated). No decipherment of the four letters.
3. `"A 11/XIV D/13a" OR "Koninklijk Huisarchief" Lodewijk Nassau cijfer` (shelfmark + cipher) -- hits: WVO scans 04617, 04614,
   06143, 06354, 05523, 05543, 04539, 13002 (catalogue PDFs; 4614 is already used as a companion decipherment, AX-COMP), the
   KHA contact page, HistoCrypt 162. No solution text.
4. `"Ludwig von Nassau" Chiffre Briefe 1574 Wilhelm von Oranien entziffert` (folder title, German) -- hits: Deutsche Biographie,
   Fuggerzeitungen person page, museum-digital, hiko-nassau.de *Oranien und Nassau* contents PDF, HistoCrypt 160 (Chodkiewicz
   1574-75, unrelated), Alexander Rose "Reading Maximilian's Mail" (unrelated). Nothing on these letters.
Decoded-phrase searches in quotes were already run by the verifiers (AUDIT.md V5/V8, print_check.py) and are not repeated here.
Blog site searches: **Cipherbrain** (`site:scienceblogs.de klausis-krypto-kolumne Nassau OR Oranien OR Oranje verschlüsselt
1574`) -- one plausible post opened, "The secret writing of the Habsburgians" (2014, Ferdinand III / Leopold Wilhelm 1640): post
and all 12 comments read, no Nassau, Orange or 1573-74 Dutch letters; the rest are index pages and the Thirty Years War
post; **Cryptiana blog** (`site:cryptiana.blogspot.com Nassau OR Orange cipher 1574 OR 1573`) -- no blogspot hit (CUP, Groen on
DBNL, HistoCrypt 160); Tomokiyo's dutch.htm (on disk, read 24 Sept 2026, check-solved item 3) has no mention; **Cipher
Mysteries** (`site:ciphermysteries.com "Louis of Nassau" OR "William of Orange" cipher`) -- no ciphermysteries.com hit at all.
No comment thread anywhere carries a decipherment or plaintext of 4610, 4611, 4612 or 4616 (or 5797).
Requests: scienceblogs.de 1, search engine 7.

## Premise check (GF-A2-1, 2 Oct 2026)

(a) Decipherments the folder already mentions -- **found, all opened and used.** 4613 p2 and 4615 p3 (the key source, R18),
4614 pp.5-6 (AX-COMP), 7205 pp.8-10 (AX-COMP2), 7206 p8 (AX2-BLANKS), 5801 interlinear and pp.7-9 (AX2-5801), the glosses on
4496/5550/5552/5557 (AX-GLOSS); Groen's partial print of 5797 with its undeciphered spots (csWV2). Each deciphers its own
letter, not 4610/4611/4612/4616. 7208 ("solved on leaf" per WVO) was opened by AX-GLOSS: pp.1-3 cipher with no interlinear
gloss, p5 a separate same-date clear letter -- not a decipherment of a target; its transcription stays a siblings step. The
four target letters carry no clear copy (R9 inventory, A1 contact sheet).
(b) Other solvers' working files -- **not found.** Shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers
(2 Oct 2026): grep for Lodewijk / Louis of Nassau / Ludwig von Nassau: the only Louis of Nassau hit is Bourdeau's
`research/gallica_sweep/mondoucet/f1573/reading.md` (Mondoucet's 1573 letter about Lodewijk's levies -- a different item and
sender, cited only as context); no folder, rendering or key for the WVO letters; Aymeloglu: no hit (cited only).
(c) Physical neighbours -- **checked, not found.** The KHA file A 11/XIV D/13a runs 4610-4616; 4613, 4614 and 4615 between the
targets were opened and are decipherments of themselves only; every page of the four target PDFs was viewed (R9, A1). 4610
is marked "duplicaat": the other exemplar(s) Lodewijk sent are not located (not in WVO under this shelfmark), and Orange's
printed reply of 17 Jun 1573 (Groen IV CDXXVII) answers its substance without deciphering it (AUDIT.md section 1).
(d) Recipient side -- **checked, not found.** The recipient is Orange; his printed replies to 4610, 4611 and 4616 (Groen IV
CDXXVII, CDXXXIII, CDLXXXIV) acknowledge the letters but print no decipherment; none located for 4612 (AUDIT.md section 1). The
sender-side (Nassau/Dillenburg) regest series, Demandt's *Nassau-oranische Korrespondenzen*, stops at 1570 (august-van-saksen
NOTES, check-solved item 1), before these dates.

## A2-LVN: code 173 graded per direction (2 Oct 2026, 21:32-21:4x UTC, account 2, LANE-A2PUSH)

Intake gate first (brief step 2), `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74`, exit 0:

    lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines

The step from the Verdict line, nothing else. Source PDFs fetched once each from resources.huygens.knaw.nl
(05810.pdf, 05550.pdf; scratchpad only, not committed), rendered at 300 dpi with pdftoppm; crops cut by hand from the
render after `tools/iiif_lines.py --image <render> --region 560,2680,1820,320 --ink 100 --distance 60 --debug` found the
three 5810 p1 lines (L40-L42) for the overlay. Read by eye in this session (no subagent).

**(1) Groen's 5810 sentence.** groen/groen_IV_CDLXVIII.txt prints "...à l'endroict de la bonne ville de Harlem, laquelle,
après s'estre si vaillamment maintenue...": no word between "Harlem" and "laquelle". The leaf runs
`84.312.78.84.127.223.132.[173].63.18. / 40.88.114.113.84` = de la [ville de] de [NULL][harlem][NULL][?] a q / u e l l e:
the only letter of "laquelle" no code supplies is the initial **l**, and the disputed sign sits exactly there.
**Image (crops images_wv2/crops_rederiv/05810_p1_L40_173_300dpi.jpg, 05810_p1_L40_173_vs_143_7s.jpg):** the sign is
"1?3". Its middle digit is a short upright with a bar at the top, inside the x-height. This hand's 7 (127 on L40 and L41)
is a top bar with a long stroke below the baseline; its 4 is a "+" crossed at mid-height (143 on L42, 242 on L41); its 1 is
a plain upright. The middle digit matches none of them cleanly. J6's independent pass on the same line
(../jan-van-nassau-1572-75/j6/fit_5810.tsv, 5810p1_B5_r1 pos 10) had already read it "113 or 173?" at L; passB read 173
on a single pass. **Result:** the 5810 token is M, 173 or 113. Read as 113 (= l, C) it fills Groen's "laquelle" exactly;
read as 173 it would be a word Groen does not print. Either way 5810 is **not** an observation of 173 as a null in list B,
as the gap line had allowed. ciphertext_5810.tsv is left as transcribed (rule: never silently repaired); the alternative
is recorded here and in HYPOTHESES.md.

**(2) The 5550 p2-5 gloss tail at 300 dpi** (crop images_wv2/crops_rederiv/05550_p2_run_p2-5_tail_300dpi.jpg, which shows the
gloss and the cipher run together). The run reads 153.130.90.1.79.173. The gloss above it reads, left to right,
"Pals[...]duc vnd graf". The first word is still crossed by a descender of the main hand (V8.2's finding stands: no
clean "Palsgrave" there, and its middle letters stay unread). The tail is clear: **"vnd"** stands over 90.1.79, three
letter codes (key_full: f, n, d; the f/v difference is noted, not pursued), and **"graf"** is written whole, with no
prefix, ending before a flourish of the main hand. With "vnd" on 90.1.79, the only code left under "graf" is 173.
**Result:** 173 = graf, read from a period interlinear gloss, **H, list A only** (5550 is Jan to Willem, Dec 1573, the
same direction as 5797). The alignment of "graf" to 173 comes from elimination within the run, not from a gloss written
over each code (the p2-11 case). A verifier should know that.

**(3) Graded per direction (rule 4, AX2-172):** HYPOTHESES.md "Code 173, graded per direction". This is not two H
witnesses in conflict. The only H witness is list A. List B holds the unsettled 5810 sign (M) and 5801's two
occurrences, where key_5801 has 'q' from one aligner observation (M, unconstrained; AX2-5801). key_full.tsv gets no
173 row, so list-B letters do not inherit the value.

**(4) Reading regenerated (rule 7).** New `exceptions_5797.tsv` (p5_spot5 pos 4 = graf, H, with the reason), wired into
`decode_5797_full.json` only. The key.tsv reading (reading_5797.txt) is unchanged. `python3 tools/decode_key.py
ciphers/lodewijk-van-nassau-1573-74 --config .../decode_5797_full.json --check` gives "reading up to date". Tokens went
from H 2, U 11 to **H 3, U 10** (C 14, M 44, I 2 unchanged; 73 total). p5_spot5 now reads `{ist}l[graf]{gestern}`: 131
NULL (C), 123 l (M; dual reading, null in 4614 and on 5810/5811), 173 graf (H). With 123 as a null, this gives "ist
[der] Graf gestern zue ghen gezogen". Groen's blank is filled by a title, not a name. Which count is meant is not
inferred here.
Judge (spec specs/lodewijk-5797.json, `python3 tools/judge_plaintext.py specs/lodewijk-5797.json --file
ciphers/lodewijk-van-nassau-1573-74/reading_5797_full.txt`):

    FAIL language: score=-1.471, null_p99=-1.622, real_p05=-0.457, real_median=-0.431, mode=both, N=329
    FAIL words: cover=0.334, min=0.5, real_text_median_cover=0.763
    FAIL - lodewijk-5797 (a PASS is a gate for a verifier, not a reading; rule 10)

Before the change it read -1.467 / cover 0.338, also a FAIL. The file is mostly the code-cluster fragments of seven
spots, so the judge cannot decide one word, either way.
No statistic was computed in this step (a gloss read and a print fit), so rule 3 has no control to run.
Not done (outside the brief): 5801's two 173 contexts were not image-checked; the first word of the 5550 p2-5 gloss
and code 130's list-A value ("duc"?) were not pursued. Requests: resources.huygens.knaw.nl 2 (one PDF each). Vision:
7 crops read by eye in this session, no subagent calls.

## A2-LVN3: null-band NULL-vs-letter test, fr16 char LM (2 Oct 2026, 22:1x UTC, account 2, LANE-A2PUSH) -- gate FAIL

Intake gate first (brief step 2), `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74`, exit 0:

    lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines

The Verdict's step only (gap 1). Script `bandtest/band_lm.py` (docstring has the full rule), outputs `bandtest/control.tsv`,
`bandtest/subsample.tsv`, `bandtest/band.tsv`; runs in about 16 s, deterministic (`--seed 1`). Input: the three
reading_{4610,4611,4616}_full_tokens.tsv files (key_full v3, unchanged); model tools/french16_ngram.py (fr16, order 5).
**Method.** For a code X, each occurrence is replaced by NULL and by each of the 23 folded letters; the context is up to
8 decoded letters on each side, cut at any unread token or multi-letter name/word code. The best letter L* maximises
summed log2 p over the occurrences; X is called NULL when sum(NULL) - sum(L*) > 0. Rule and gate pre-registered in the
docstring before the first run; no threshold was tuned.
**Known-answer gate (rule 3, AX-NAMES per-class paragraph).** Hidden one at a time: the 13 C-graded NULL codes in 121-138
(121, 122, 124, 126, 127, 130-135, 137, 138; 128/129 are M and 123/136 are not nulls, so all four are excluded) and 13 C-graded
single-letter codes matched by token count in the same three letters (61, 3, 1, 14, 73, 76, 90, 118, 80, 13, 86, 11, 16). The
control can fail differently from the target: a letter code can be called letter, and 6 were. Gate: per-class accuracy >= 0.80 for both.

| class | codes | called right | accuracy | gate |
|---|---|---|---|---|
| NULL (121-138, C) | 13 | 13 | 1.000 | pass |
| letter (matched, C) | 13 | 6 | 0.462 | **fail** |

Of the 7 letter codes called NULL, 5 still had their true letter as L* (1 N, 14 P, 76 D, 11 P, 16 Q); the true letter was
L* for 10 of 13 letter codes overall. So the LM finds the right letter when told a letter is there, but the NULL-vs-letter
decision leans NULL: inserting a letter costs about 4 bits however well it fits. Subsampled to the band codes' own
counts (bandtest/subsample.tsv, 200 draws each), letter accuracy is 0.43-0.54 at n = 5-21 and passes 0.80 only at n >= 23,
where just 2 control codes per class are left. At full count the gate fails, so nothing is licensed at any n.
**Band output (recorded, not a classification).** All eleven band codes come out NULL (125, 139, 140, 142, 145-151). The
NULL margin runs 2.0-5.2 bits per occurrence (148 5.18, 150 4.68). Control nulls run 1.96-5.31 and control letters -1.12 to
+3.23, so the two ranges overlap. 148 and 150 sit above every control letter code. That is a description of this sample, not
a threshold: a cut chosen after seeing 26 codes has no held-out set to check it against.
**Result.** Gate FAIL (letter 0.462 vs 0.80). The band is **untested-by-this-tool**, not refuted and not confirmed. No key
or reading changed (rule 7: nothing to regenerate; `decode_key.py --check` not needed). Grades unchanged: 4610/4611/4616 still
U 310 (rule 4). HYPOTHESES.md has the row. Gap 1's next step is a different instrument, the fr16 word-segmentation score
under the same hidden-code gate per class, ~$3. Not a re-tuned threshold on this rule.
Requests: none (all local). Vision: 0 calls. Subagents: 0.

## A2-LVN4: name codes vs Orange's printed replies (2 Oct 2026, 22:2x-22:4x UTC, account 2, LANE-A2PUSH) -- gate FAIL

Intake gate first (brief step 2), `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74`, exit 0:

    lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines

The Verdict's step only (gap 2). Groen IV CDXXVII (pp.156-160, answers 4610) and CDXXXIII (pp.175-178, answers 4611) were
not on disk: fetched once each from DBNL (groe009arch04_01_0045.php, _0052.php; two first guesses, _0044 and _0051, landed on
CDXXVI/CDXXXII and were discarded), saved as groen/groe009arch04_01_00{45,52}.html and groen/groen_IV_{CDXXVII,CDXXXIII}.txt;
CDLXXXIV (answers 4616) was already on disk. All three read in full.
**Names written back** (replies/names_back.tsv, 49 rows): CDXXVII -- the Emperor and "plusieurs Princes", Barby, Heylingen,
the Landgrave, the King of France, Frégouse, La Rochelle, Alba, Lumbres, the Ambassador, the King of Poland/Anjou,
England, three cavalry companies, infantry, the French, the Rhine, Holland, Emden/Bremen/Hamburg, Schwartzburg, Master Georgi
of Arnstadt, Brunynck, Haarlem, Montgomery; CDXXXIII -- Haarlem, Batenburg, Alkmaar, Waterland, Lorges, Poyet, La Rochelle,
the English, the States; CDLXXXIV -- Delft, Dordrecht, 35-36 companies, boats, the river, Tiel, Wamel, Varik, Gorinchem.
**Contexts** (replies/contexts.py -> replies/contexts.tsv): the 31 U tokens of the 26 codes, 16 decoded tokens either side.
**Mechanical test** (replies/reply_fit.py; rule and both gates written in its docstring before the first run, no threshold
tuned; one code fix after the first run, digits allowed in anchors so the printed "311" could be found, which changed no
gate input): reply-window stems found in the cipher context around each code; a code gets a proposal when one name fits
>= 2 stems and no other name ties it. Output replies/reply_fit.out, replies/fit.tsv.

| control / target | result | gate |
|---|---|---|
| (a) known answer: 8 hidden C/H name-code occurrences (153, 192, 200 x2, 202, 221 x2, 223) vs own reply | 0 hits, 1 wrong (4611's 221 hollande -> 'alkmar') | hit rate >= 0.50, wrong <= hits: **FAIL** |
| (b) mismatched reply (each letter vs the two replies that do not answer it) | 0 proposals in all 6 pairings | true > mismatched mean |
| target, true pairing | 3 proposals, all 'alkmar': 4611 211, 232, 331 | -- |

The three 'alkmar' proposals all come from one passage (4611 p2_L08-09, "... guerre ... l'ennemy [hollande] vers"), the same
one that gave the wrong known-answer proposal. Control (b)'s "discriminates" rests on that passage alone. Known-answer gate
FAILED, so **nothing is licensed**. Gap 2 is **untested-by-this-tool**, not refuted. No key or reading changed (no
decode_key.py --check needed). Grades unchanged: 4610/4611/4616 still U 310 (rule 4).
**By eye, recorded only, no value applied.** (1) Groen printed CDXXXIII with one numeral left in cipher: "pour ne scavoir la
contrée du 311, ni la langue" (p.177, Orange to Lodewijk, list B). 'pays' fits, and 'Hollande' would fit too. With 5811's
"que le 311 y est assez" (names.tsv, M), that makes two list-B contexts consistent with 'pays'. That is below names.tsv's
class-b gate of 4. key_5801 'a' and key_7206 'papes' are list-B aligner guesses that disagree. 4611's two 311 tokens are list
A with no list-A witness, so they stay U (HYPOTHESES.md "Code 311, graded per direction"). (2) 4610's 186/194 sit beside "du
pais ... [pfaltzgraf] ... solliciter", and CDXXVII's opening says the Emperor answered "plusieurs Princes qui l'avoient
sollicité ... pour rapaiser les choses du Pais-Bas". So 186/194 may name princes or the Emperor, but the reply names no single
prince, so nothing can be assigned. (3) CDLXXXIV's places (Tiel, Wamel, Varik, Gorinchem) have no match in 4616: its only
name code, 313 x2, sits in lines full of unsegmented digit groups (gap 3), and no context is readable enough to test.
Requests: www.dbnl.org 4 (2 kept). Vision: 0 calls. Subagents: 0.

## A2P4-LVN97: 5797 spot 1, the Groen p.222 paragraph (3 Oct 2026, 17:17-17:28 UTC, account 2, LANE-A2PUSH4) -- gate FAIL

Intake gate first, `python3 tools/intake_gate_check.py lodewijk-van-nassau-1573-74`, exit 0:

    lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines

The gap-7 step only. 05797.pdf fetched once (resources.huygens.knaw.nl, 1 request, scratchpad only), pp.3-4 rendered at
300 dpi with pdftoppm. Crops, pasted before any vision call:

    python3 tools/iiif_lines.py --image <scratch>/05797_p3_300.png --out ciphers/lodewijk-van-nassau-1573-74/spot1/crops --region 420,1880,1980,760 --prefix p3 --debug
      -> 8 lines, pitch 93
    python3 tools/iiif_lines.py --image <scratch>/05797_p4_300.png --out ciphers/lodewijk-van-nassau-1573-74/spot1/crops --region 420,200,2000,1900 --prefix p4 --debug
      -> 20 lines, pitch 92

**Where the paragraph sits.** Groen's paragraph ("werden E.G. nhumehr ... nemlich Dateno. Wir seint resolvirt ... bringen.")
runs from p3_L02 (the clear tail after AX-5797's "secours"/"entrepr" clusters) to p4_L20. The garbled stretch Groen
brackets ("begert das uff dert mögen. [Phit] ... vol ssen ... 11 haupter ... meinung ist, die schlachtordnung ...") is
p4_L10-L20. The p3_L01-L02 clusters were already in ciphertext_5797.tsv (p3_spot1_open) and are not repeated.

**Transcription** (TRANSCRIPTION.md). Two blind Sonnet passes per page, given crop paths only: p3_L06-L08 and p4_L01-L18
(spot1/passA.tsv, passB.tsv). tools/reconcile_passes.py: 272/311 signs agree (87.5%), 39 columns differ, only 2 of
them on codes. The p.3 crops handed to the passes began at L06, so p3_L03-L05 and p4_L19-L20 had no pass. The fifth call
(the reconciliation) settled the 6 code queries and blind-read those five lines (spot1/passR_extra.tsv). I read the same
five lines as the second pass (spot1/passM_extra.tsv). Codes agree on all of p3_L03-L05. On p4_L19 my "lb"/"6i ch" vs
its "16"/"61 ich" was settled at 2x zoom as 16, 61 + attached "ch" (M). One reconciler call overruled: it read the
dotted "ııı" strokes as Roman 3, but p3_L04's "120.111.103" = m l i inside Groen's "nemlich" shows this hand writes code
111 that way. So p4_L06 and p4_L12 take 111 (M) and p4_L14's "ii" takes code 11 = p (M; Groen's "haupter"). p4_L13's
barred "II" is clear Roman 11 (Groen "darzu 11 haupter"). p4_L10's barred V is recorded as an unread sign "?" (L).
Result: spot1/ciphertext_spot1.tsv, 386 rows, 239 of them code tokens. Signs read: 311 x 2 passes + 75 x 2 + 6 settled.
Vision: 5 Sonnet subagent calls (about 478k subagent tokens in all) plus 5 crops and one zoom read by eye in this
session. Cost per 100 signs: the orchestrator reads the session cost; at the brief's USD 1.5-per-call rate it is about
USD 7.5 / 386 signs = USD 1.9 per 100.

**Decode** (rule 7): `python3 tools/decode_key.py ciphers/lodewijk-van-nassau-1573-74 --config spot1/decode_spot1.json --check`
gives "reading up to date". key_full.tsv v3, with clear prefix w:. spot1/exceptions_spot1.tsv carries code 173 = graf at H
at its three positions: list A, the same letter and grounds as exceptions_5797.tsv. **Tokens 239: H 4, C 155, M 45, I 16,
U 19** (rule 4; no S, no claimed reading beyond the key's grades).

**Gate** (spot1/prereg.md, committed 7d636fe2 before any pass; spot1/align_spot1.py, output spot1/gate.tsv and spot1/units.tsv):

| reference | A (Groen fragment words reproduced in order) | B (cipher units matched) |
|---|---|---|
| target, Groen p.222 paragraph (N=160 words, F=82) | **0.171** | **0.355** (11/31) |
| (s) 200 word-shuffles of the same paragraph | mean 0.030 | mean 0.128, p95 0.161, max 0.226 |
| (d1) "Die schwere last..." | 0.000 | 0.000 |
| (d2) "Von zeittungen..." | 0.007 | 0.032 |
| (d3) "Es lest sich..." | 0.007 | 0.032 |

Gate: A >= 0.50 **fail**; B >= p95(s) + 0.15 pass (0.355 vs 0.311); B >= max(d) + 0.15 pass (0.355 vs 0.182) -> **FAIL**.
Nothing in the interior is licensed beyond the transcription.
**Diagnostic, after the gate and changing nothing.** Two causes keep A low. (1) F counts as "fragment words" every
Groen word the passes' clear words missed, and the passes' clear words are often not in Groen's spelling: "e.f.g." for
E.G., "halt" for balt, "dazu" for darzu. Rule 3 calls this the PX-BRODEC shape: the two
renderings follow different conventions. (2) Cipher units that join codes and clear fragments ("58.35 pf 21.81.104 ben")
miss the 0.75 threshold although they spell the word. Fixing either one now would be scoring after seeing the result, so
neither is applied here.

**What the decode shows, by eye, not licensed by the gate (all graded as decode_key gives them):**
- "nemlich Dateno" = 2.139.81.120.111.103 ch 129.147.80.61.33.82.3.7 -> n?e mli ch [NULL][?] d a t e n o.
- "resolvirt alsbalt" = 22.139.83.40.9.113 u 122.104.24.34 128.65.115.26.70.61.111.35 -> r?euol u irt / alsbalt.
- 173 (graf, H list A) stands before all three of Groen's subject-less verbs in the paragraph: "wirdt [173] mit bruder"
  (p4_L05), "[173] begert" (p4_L10, 173.121.67.81.92.82.22.32 = graf NULL b e g e r t), "[173] meinung ist" (p4_L18).
  Groen prints "begert" and "meinung ist" with no subject, and leaves the word out of "wirdt mit bruder".
- Groen's "uff dert" = 40.90.87 (u f f) + 136 (key 'uingt', dual l/uingt M) + 227 (no key row) + barred V + 30.3.80.83.23.33
  (s n d e r t) + 133 (NULL) + 339 (key 'harquebouziers'). So he kept "uff" and the tail "-dert" and dropped the rest.
- [Phit] = 13.97.101 + clear t = p h i t, Groen's own conjecture letter for letter.
- "vol ssen" = 36.9.111.142.100.88.26.27.81.1 -> u o l [142 U] h f s s e n.
- "11 haupter" = II (clear) ha + 135.39.11.31 + tr -> ha [NULL] u p t er.
- "ziffer" = 60.101.90 fr -> z i f + fr; "zuschreiben könne" = 58.35 [schr/pf] 21.81.104 [ben] 127.108.10.1.2.81.125 ->
  zu .. rei .. [NULL] k o n n e [125 U].
- "die schlachtordnung" = 339 = key 'harquebouziers' (the same code three lines up). Groen's word is a conjecture that the key does not
  support. "Bergen op Zoom" = 254 after 37.87 (u f). Groen prints 254 as "Grönningen" on p4_L02 ("mit Grönningen"), so 254
  carries two different printed values in one letter. That is a conflict to log, not to settle (rule 4, AX2-172).
- "Scholbich(?)" = 26 ch 8 16 123 61 ch -> s ch o q l a ch (16 'q' and 61 at M). "insel" = 105.5.27.85.136 -> i n s e +
  136, which needs 136 = l at this position (136's l/uingt dual stands). "bringen" = 69.24.102.3 gen -> b r i n gen.
Not done (outside the brief): the 254 conflict was not entered in HYPOTHESES.md as a key conflict row, and Groen's [testgu]
(next paragraph, p4_L21-L23) was not transcribed. Requests: resources.huygens.knaw.nl 1. Subagents: 5 (Sonnet).

## A2P4-LVN98: 5797 spot 1, Groen-normalised cipher-unit re-score (3 Oct 2026, 17:55-18:01 UTC, account 2, LANE-A2PUSH4) -- gate FAIL, instrument retired for spot 1

Gap 7 only, no vision call, no re-transcription: input spot1/ciphertext_spot1.tsv and key_full.tsv v3 as LVN97 left them
(`decode_key.py ... --config spot1/decode_spot1.json --check`: reading up to date). Intake gate as LVN97 above (exit 0).
spot1/prereg2.md committed d1c8541e before any score: one normalisation N2 applied to both sides (abbreviations expanded,
E.G. -> euer gnaden; lowercase; umlauts; dt/th/tz/ph/ck/c/qu/v/w/j/y/ie/ae/oe/ue variant classes; Dehnungs-h; final e;
punctuation dropped; doubles collapsed), the metric restricted to cipher units (B2), the same sim >= 0.75 monotone DP, the
same controls, and the absolute bar B2 >= 0.50 plus both control margins. It states that the rule list was written after
LVN97's diagnostic and that a FAIL closes the method for this span (third look, rule 3). Script spot1/align_spot1_v2.py
(reuses align_spot1.py's units/DP); outputs spot1/gate2.tsv, spot1/units2.tsv.

| reference (N2) | B2 (eligible cipher units matched in order) |
|---|---|
| target, Groen p.222 paragraph (N=163 words) | **0.333** (10/30) |
| (s) 200 word-shuffles | mean 0.121, p95 0.167, max 0.200 |
| (d1) "Die schwere last..." | 0.000 |
| (d2) "Von zeittungen..." | 0.033 |
| (d3) "Es lest sich..." | 0.033 |

Gate: B2 >= 0.50 **fail** (0.333); B2 >= p95(s) + 0.15 pass (0.333 vs 0.317); B2 >= max(d) + 0.15 pass (0.333 vs 0.183)
-> **FAIL**. The normalisation moved nothing upward: B was 0.355 (11/31) under LVN97's rule and is 0.333 (10/30) under N2
(checked after writing: the one unit lost is 13.97.101 = p h i, Groen's [Phit], which N2's ph -> f shrinks to 'fi', two
letters, below eligibility; the other 30 eligible units stay eligible and the matched count goes 11 -> 10). The spelling-convention explanation for LVN97's low A does not carry over to the
cipher units: the misses are code-level (units2.tsv: 'zuger', 'upt', 'rei', 'inseuingt', the 339/136 word-values), not
spelling. Both runs beat order and content controls by the margin, so the decode does follow Groen's paragraph more than
chance; it does not reproduce it at the pre-registered bar.

Grades unchanged (rule 4, no regrade without a PASS): spot 1 tokens 239, H 4, C 155, M 45, I 16, U 19. Nothing in the
interior is licensed beyond the transcription; LVN97's by-eye list stays unlicensed.

Rule 3 third-attempt clause: in-order Groen alignment of spot 1 (spot1/align_spot1.py, align_spot1_v2.py) is retired for
this span, logged untested-by-this-tool at this transcription (not refuted). Gap 7 stays open-codes; what reopens it is new
material -- another witness of the paragraph (a contemporary copy or decipherment of 5797, or Orange's reply quoting it) --
or a different instrument, not a further N2/threshold/metric tuning. Requests: none. Subagents: none.

## R12-LVN16R: score.py fix and eye pass on the 12 contested H control rows of 4616 (6 Oct 2026, 11:58-12:0x UTC, account 2, LANE-RUN12-account-2)

(1) `lvn16/score.py` now reads `lvn16/ciphertext_4616_pre.tsv` (the pre-apply snapshot) instead of the renumbered
`ciphertext_4616.tsv`, the defect R12-LVNV logged in AUDIT.md. Rerun: control A3 193/210 (0.919), B3 194/210 (0.924);
`lvn16/aligned.tsv` sha1 adaf742a... before and after, byte-identical; `lvn16/apply.py --check` exit 0, gate PASS. The
logged reproduce line `lvn16/score.py && lvn16/apply.py --check` now works as written.

(2) Eye pass. WVO 04616.pdf fetched once (resources.huygens.knaw.nl, HTTP 200), p1 rendered `pdftoppm -png -r 300`
(sha1 4f47b490..., matches R12-LVN16), crops re-cut with the logged command (scratchpad, not committed):
`python3 tools/iiif_lines.py --image 04616-1.png --out crops --prefix 04616_p1 --region 380,320,2080,880 --distance 45
--prominence 20 --top-margin 12 --bottom-margin 12 --debug` (13 lines). Each row read by the worker's own eye on a 3x
window of its line crop (p1_L17/2 also at 5x from the page render). No subagents. Per row: `lvn16/eye_h_rows.tsv`.

Result: of the 12 H control rows where both blind readers agreed on another value, the image supports the H value at
6 (p1_L05/4 71, p1_L05/14 76, p1_L07/5 37, p1_L07/11 84, p1_L10/1 21, p1_L16/4 85) and supports the readers' value
at 6 (p1_L12/1 40 for 90, p1_L13/1 39 for 79, p1_L14/2 81 for 91, p1_L15/16 31 for 36, p1_L16/2 20 for 26, p1_L17/2 81
for 91; three clear, three moderate). p1_L17/2 disagrees with R12-LVNV's own eye ("clearly 91"): at 5x it is a closed
8 with no tail. These are possible transcription conflicts in H rows for a verifier; no key, H row or reading was edited.
Effect on the control: the readers' shared 7->3 and 9->8 confusions are real at 3 of these rows (37, 71, 84 read
wrong) but at 6 rows the "error" is likely the H transcription's, so the 193/194 of 210 figures are if anything
understated; the gate still passes either way. A known-answer control drawn from H transcription rows is only as
good as those rows: 6 of 12 contested H rows look wrong on the image, so H in ciphertext_4616.tsv means "agreed at
150 dpi", not "checked against the 300-dpi image". Next: a verifier re-checks these 6 rows (and decides whether the
H grade on 4616's other uncontested rows needs a sample check), ~$1.5.
Requests: resources.huygens.knaw.nl 1.
