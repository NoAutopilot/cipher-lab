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
cipher present on 4610 (`images/04610_p1.png`); the sibling 4613's contemporary decipherment confirmed
present and imaged (`images/04613_p2.png`). No REQUEST.md needed.

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
Pass B additionally read a second, previously-unnoticed gloss in the 05557_p2_jar_94.png crop ("beritten"(?), i.e.
"mounted"/"on horseback", over the second occurrence of 82) and refined "Graf von Holl[andt]" as one phrase
spanning several numbers rather than a single word over 93 -- both <=120, out of this brief's >120 scope, noted
for whoever next looks at 5557's low-code annotations (see the flag above).

Rule 10: no novelty words used. Rule 3: no controls run this pass (no numeric threshold gated); the two new
values (192, 221) are grade H per rule 4 (read from a contemporary key source, i.e. a period gloss), not
cryptanalytic.

Hosts: `resources.huygens.knaw.nl` 9 requests (04496, 04614, 07205, 07206, 07208, 05801, 11250, 05552, 05557
PDFs), >=2s apart, descriptive UA, all HTTP 200. No other hosts.

Files: `axgloss/gloss_attest.tsv`, `images_wv2/crops_gloss/{04496_p4_hollande_zeelande.png,
04496_p4_respagne_192.png,05557_p3_grafvonholland_93.png,05557_p2_jar_94.png,05557_p2_kein_133_vorrad.png}`.
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
