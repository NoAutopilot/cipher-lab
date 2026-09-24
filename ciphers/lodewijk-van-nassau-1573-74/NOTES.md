partial

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

**Verdict: open** (all six), copy-free, **kind: recovery** (same circle as NB1's siblings 4613/4615 with imaged
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
