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
