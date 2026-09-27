partial

INTAKE-SPINELLI, 27 Sept 2026: solver-ready intake (Layout, no cryptanalysis, no new reading, no class).
Built from KEY-ADJACENT.tsv row 5 (rank 6) and `sources/cryptiana/web/henryvii.htm`, read in full this job
(cp932-decoded per the file's own declared charset, not re-fetched -- already on disk).

# Beinecke Library (Yale), Spinelli Family Papers, GEN MSS 109, Filza 163

Beinecke record/OID 10844890 (the legacy vufind URL Tomokiyo links, `Record/3811294`, 302-redirects here);
fetched this job with `tools/browser_fetch.js` after a plain curl returned an empty 202. Sender and recipient
come from the record's own title (Italian, quoted in full in `images/manifest.json`): "Il Sig. Tommaso scrive
di Barcellona al Sig. Canonico Leonardo..." -- **Thomas ("Tommaso") Spinelli writing to his brother Leonardo
Spinelli, a canon**, dated **7 September 1519**, from Barcelona ("Barchenonia"), where Thomas was resident
ambassador to the Spanish court at the time (per `henryvii.htm`'s own biographical section above the
Spinelli-brothers note). Language Italian; call number GEN MSS 109; provenance "Purchase, 1988"; 3 digitised
canvases (p.[1], p.[2], p.[3: address leaf]) though the record's own title cites "4pp." -- not resolved this
job, see `images/manifest.json`'s note.

## Tomokiyo, verbatim

`henryvii.htm`, "Notes added in August 2018" (the passage this row's own KEY-ADJACENT.tsv sentence is drawn
from):

> "Ekaterina Domnina, "Ciphers in Early Tudor Diplomacy" in *Geheime Post* (2015) (updated pdf) focuses on
> Thomas Spinelly (Thommaso Spinelli in Italian), in particular his private correspondence with his younger
> brother Leonardo Spinelli in Florence or Rome. It was about 1515 that he introduced cipher in his private
> correspondence. In a letter of 3 January 1515, he asked his brother to use cipher to keep some information
> from their other brother, after which they used cipher frequently. (p.184) ..."
>
> "Spinelli brothers' cipher was a homophonic substitution cipher with some nulls (p.185, Fig.1), in which he
> frankly wrote, apart from private matters, critical comments on diplomatic proceedings and political
> figures (p.188-190)."
>
> "Spinelli's private correspondence is in Spinelli Family Papers, among which one letter in cipher is
> available online (Beinecke Digital Collections). (**Note in January 2024**: This particular letter can be
> deciphered with Spinelli brothers' cipher reconstructed by Domnina. Words "la gubernation d'ispagnia" can
> be read.)"

`henryvii.htm`, "Notes added in August 2023" (a separate, later addendum, presenting Tomokiyo's own
reconstruction of the same cipher, not a reproduction of Domnina's Fig.1):

> "Spinelly's cipher can be reconstructed as follows." [image: `spinelly1515.png`, the key of record below]

Tomokiyo does **not** print any reading of this letter beyond the one quoted phrase, "la gubernation
d'ispagnia" -- no transcription, no fuller decode, no image of the leaf with markup (contrast
`ciphers/fr4715-f61-mayenne-1592`, where Tomokiyo's own published image carries five short interlinear
spans). This matches Bourdeau's catalogue entry (already quoted in this row's own `in_repo` cell from
SCOUT-OWN-8, 27 Sept 2026): "Spinelli family private cipher letters (Beinecke Library, GEN MSS 109): Read in
part... Tomokiyo read part of the Beinecke letter online with it. The rest of Gen. MSS 109 has no published
reading."

## Gate verdict (Job 0, this job)

**Not found-solved. Continues to intake** (the same "partially read, most of the letter unread" bucket
`ciphers/fr4715-f61-mayenne-1592` used for the Mayenne cipher on BnF fr.4715 f.61, 27 Sept 2026 -- an existing
published crib is valuable material for a future worker, not grounds to retire the row when it falls short of
a full reading).

- **(a) `henryvii.htm`'s Spinelli passage, read in full this job**: prints only the one phrase, "la
  gubernation d'ispagnia", as evidence the letter "can be deciphered" -- no transcription, no fuller reading.
  Quoted above in full.
- **(b) Domnina's PDF (istina.msu.ru)**: **not fetchable this job**. The URL `henryvii.htm` links
  ("updated pdf", `istina.msu.ru/media/publications/article/a81/378/11992054/Domnina_Spinelli_cipher_
  EnglishRussian_-_kopiya.pdf`) returns a plain nginx 404 (this job's one allowed request to that host, per
  the good-citizen rule a 404 is not retried). Her Fig.1 (p.185), the cipher table this row's `key_location`
  cell names, and any fuller reading she may print, could **not** be checked this job -- an access gap, not
  a "no" answer. Flagged as the first thing a future worker with a working route to this PDF (a mirror, a
  different URL, a library route) should check before relying on this folder's key beyond calibration.
- **(c) the Beinecke record (OID 10844890) and its IIIF manifest**, read in full this job: no transcription
  or decipherment named anywhere in the record's own metadata (title, date, language, provenance, collection
  note, finding-aid link) or in the manifest's `metadata`/`seeAlso`/`rendering` fields. The Archives at Yale
  item-level finding-aid page the record links (`archives.yale.edu/repositories/11/archival_objects/2787659`)
  was **not** fetched this job -- a different host, out of this job's allowed network scope (brbl-dl.library.
  yale.edu / collections.library.yale.edu only); a future worker could check it.

No vision subagent call was needed for the gate itself -- the record's own text and metadata settled it, the
same way INTAKE-MC108 and INTAKE-4715-F61 settled their own gates from text plus a direct look.

## The key (key of record) -- with an important substitution flagged

`keys/key_spinelli_c1515.tsv`, transcribed from `spinelly1515.png`, embedded in `henryvii.htm`'s "Notes added
in August 2023" section (quoted above). **This is Tomokiyo's own independent reconstruction of the cipher,
not Domnina's Fig.1 itself** -- her PDF being unreachable this job (gate item (b) above) meant her actual
table image could not be fetched or cross-checked. Tomokiyo's own page treats the two as the same cipher
(the January 2024 note explicitly credits "Spinelli brothers' cipher reconstructed by Domnina" as what makes
the online letter readable, and the August 2023 table is presented on the same page as his own reconstruction
of "Spinelly's cipher" -- singular, no indication of a second, different cipher), but this has not been
independently verified against Domnina's own Fig.1 this job. The same substitution was already precedented
this same day: `ciphers/fr4715-f61-mayenne-1592` used Tomokiyo's own `mayenne.png` table rather than any
period original, for the same reason (it was what was actually published and fetchable).

Design, from this worker's own careful transcription (not stated in prose anywhere on `henryvii.htm` --
see the key file's own header comment for the full method): 23 plaintext-letter columns (a b c d e f g h i k
l m n o p q r s t u x y z, the period Italian/Latin set omitting j, v, w). **Three columns (q, x, z) are
blank** -- no symbol drawn in this reconstruction, confirmed by this worker's own 4x zoomed crop of each
(not a transcription gap; genuinely no ink in the source image). **Five columns (d, i, l, n, t) carry two
stacked symbols each** -- homophones for that one letter (not a letter-PAIR the way the Mayenne table in
`ciphers/fr4715-f61-mayenne-1592` stacks two different letters per column; flagged so the two are not
confused). The other 15 non-blank columns carry one symbol each. A block of **12 null symbols** (this
worker's own crop-based count; both blind Sonnet subagent reads independently reported 10 and 11 and both
explicitly flagged their own count as uncertain -- the 12 is this worker's careful recount from a 6x zoomed
crop, not an average of the two guesses) and **5 word-code entries** ("I", "of", "Emperor King of Arragon",
"Prince of Castile", "new amity") round out the table. Total hand-drawn symbols: 15 + 10 + 12 + 5 = 42.

Transcription method: two independent blind Sonnet subagent reads (2 of this job's 4 allowed vision calls),
each shown only the image and the table's own printed column headers, asked for a literal ink-shape
description per cell with no letter-guessing beyond what the image's own printed labels already give. Both
passes read the first several columns (a-p) reasonably consistently but had low confidence or missed marks
entirely from column q onward, disagreed on the null count, and did not reliably catch the five stacked
homophone columns. This worker settled every cell with its own zoomed/cropped re-examination (column x-ranges
located mechanically from the header row's own white-pixel runs, not eyeballed), which is what actually
resolved the blank columns, the homophone stacking, and the null count -- recorded per-row in the key file
with grade AB (blind passes agreed, crop confirms) / M (blind passes disagreed or missed it, crop settled
it) / ? (one null symbol, an irregularly-placed 12th mark neither blind pass reported at all, whose exact
place in the table's intended grid stays unresolved even after the crop). Grade counts: **23 AB / 21 M / 1
?** (45 rows total).

## The target leaf

`images/manifest.json`: IIIF Presentation API 3.0 manifest, `collections.library.yale.edu/manifests/
10844890`, 3 canvases at 3577x4997 native resolution. Page 1 (canvas 10867298) fetched this job at 1500px
width (`images/beinecke3811294_p1_canvas10867298.jpg`). A direct look at this image (no vision subagent call
needed) shows the catalogue's "4pp. part in cipher" is literally true of this one page: roughly the top 9
written lines are continuous hand-drawn cipher symbols (several shapes visibly resemble this folder's own key
table on sight -- a pi-like mark, a w/omega-like double-hump mark, an H-like ladder mark, numeral-like marks
-- promising for calibration), with a few plain words at the very top ("Scrissi un'altra..."), then the text
switches to plain Italian prose from "L'amorte del Car[dinale]..." onward. Pages 2 and 3 (address leaf) were
not fetched this job (out of this job's cost/time budget; next worker's first step per "What remains" below).
No transcription or decoding attempted this job -- out of scope for an intake job, per the fr61/3251/mc108
pattern.

## Check-solved header (not a formal `.claude/briefs/check-solved.md` pass -- see "What remains")

- `henryvii.htm`'s Spinelli passage read and quoted in full above; prints only the one phrase, no fuller
  reading.
- `KEY-ADJACENT.tsv` row 5's own `in_repo` cell already records a solver-repository grep (SCOUT-OWN-8, 27
  Sept 2026, quoting Bourdeau's catalogue entry 306 in full) -- not re-run this job (GitHub was not in this
  job's allowed network scope).
- `CATALOG.md` and `LESSONS-LASRY.md` grepped this job (offline, already on disk) for "Spinelli"/"spinelly":
  no row for this item in either.
- No full-text/phrase search run this job (out of scope for an intake job; a phrase search on "la gubernation
  d'ispagnia" is the kind of check rule 10 and `tools/print_check.py` are for, once/if a fuller reading
  exists -- Tomokiyo's own one phrase would not be novel to us either way, and this job made no reading
  claim of its own to search for).
- The Beinecke record and its IIIF manifest metadata read in full this job (gate item (c) above): no
  transcription or decipherment named.

What remains before any class (rule 10) or any deep-work brief:
- Domnina's PDF itself, unreachable this job (gate item (b)) -- a future worker with a working route (a
  mirror, a different URL at istina.msu.ru, a library database) should fetch it, read her p.185 Fig.1 and
  p.188-190, and cross-check this folder's Tomokiyo-sourced key against her original before trusting it
  beyond calibration.
- The Archives at Yale item-level finding-aid page (`archives.yale.edu/repositories/11/archival_objects/
  2787659`) -- a different host, not checked this job (out of allowed network scope).
- Pages 2 and 3 (address leaf) of the Beinecke letter, not fetched this job.
- A formal `.claude/briefs/check-solved.md` pass proper; `tools/intake_gate_check.py spinelli-beinecke-c1515`
  run once below.
- Once any reading exists: `tools/print_check.py` on the decoded phrases (rule 10).

**Next step:** locate "la gubernation d'ispagnia" on the image (Tomokiyo's own known-answer span, the "known
answer first" discipline in `.claude/briefs/README.md`'s common tail) and calibrate `keys/
key_spinelli_c1515.tsv` against it -- likely on page 2 or 3, since the phrase was not obviously visible in
this job's direct look at page 1's cipher lines, though it was not searched for systematically. Then two
blind passes on the whole letter (all 3 canvases) and a 20-shuffled-key control (rule 3); reading to a
verifier. Given the three blank letter columns (q, x, z) and five homophone columns already known from this
transcription, a calibration pass should also try to resolve q/x/z (do they appear in the plaintext at all
within this one short business/family letter, making their absence unsurprising, or does the source material
Tomokiyo drew on for the reconstruction simply not attest them yet).

**Requests this job:** cryptiana.web.fc2.com 1 (`spinelly1515.png`; `henryvii.htm` itself already on disk,
no re-fetch needed). istina.msu.ru 1 (Domnina's PDF, 404 -- see gate item (b); not retried, per the
good-citizen rule). brbl-dl.library.yale.edu 1 (initial vufind Record URL, 302 redirect to
collections.library.yale.edu, empty body); collections.library.yale.edu 3 (1 browser-rendered catalog page,
1 IIIF manifest JSON, 1 page-1 image at 1500px) -- 4 of the allowed 6 combined for that host pair, 2s apart,
descriptive/browser user agent per the brief. No other hosts. No credentials. No AskUserQuestion. No
novelty/first/unpublished wording (rule 10) -- Tomokiyo's own one phrase is credited to him throughout, not
claimed as ours; Domnina's cipher reconstruction is credited to her by name even though her own PDF could not
itself be read this job.

## Campaign step H1 (27 Sept 2026, 21:57-22:00 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE (standing campaign runner, SPRINT.md). Hypothesis H1: fetch the two
unfetched canvases and flag by direct look where the cipher lines sit, before any vision call is spent.

**Done.** Both canvases fetched at 1500px from the same IIIF image API as p.[1], two curl requests to
collections.library.yale.edu, 2 s apart, browser UA, both HTTP 200 `image/jpeg`; written into
`images/manifest.json` with sha1, byte size and a content_note each. No vision subagent call this step
(0 of 4). Folder images now 1.7 MB.

| canvas | file | bytes | sha1 | cipher |
|---|---|---|---|---|
| p.[2] 10867299 | `images/beinecke3811294_p2_canvas10867299.jpg` (1500x2096) | 596831 | 36972a12ab5566e275ebc567d2ed45fa0aa5ea7c | yes: 2 lines |
| p.[3: address leaf] 10867300 | `images/beinecke3811294_p3_canvas10867300.jpg` (1500x2096) | 478844 | 1d563b18beec007bf6bacaa266dcf8f7fd1d6930 | none |

**Where the cipher sits (direct look, no transcription, grade I for every plain word named here):**

- **p.[1]**: the top ~9 written lines, continuous cipher (INTAKE-SPINELLI's look, unchanged).
- **p.[2]**: about 13 lines of plain Italian continuing p.[1]'s clear text ("alcuna promessa ...", on sight
  "Regno di Napoli et Sardigna", galleys arriving and the fleet "fra quattro giorni", a marriage "pero non e
  ancora publicato /"), then **two lines of continuous cipher**, about 35 and about 20 signs by eye (+-5), the
  shapes matching the key table on sight (4-like, N-like, 8/9-like, omega, pi-like, x, +, 7), then the plain
  closing "Rispondetemi con qualche fondamento circa il ritorno mio et valete", the date line "Barchinonia ...
  septembris M.D.XIX" and a signature. Region of the two-line block: 1500px image x,y,w,h = 168,854,1247,158;
  native (3577x4997) x,y,w,h = 401,2037,2973,376 (line 1 y 2037-2225, line 2 y 2225-2413), measured by eye and
  scaled by 3577/1500 -- pad ~40 native px before cropping with `tools/iiif_lines.py --image`.
- **p.[3]**: address leaf, **no cipher**. A 5-line later archival summary at the top (the text the Beinecke
  record's title quotes), the address "...no Leonardo de Spinellis Floren[tie] ... hon[oran]do" lower left, seal
  remnant, "1519" and a sideways filing note lower right.

**The "4pp." question narrowed:** the letter's own text ends on p.[2] with the date line and signature, and
p.[3] is the address leaf, so the three digitised canvases carry every written side that bears text; the
record's "4pp." most likely counts the blank side of the address leaf. No cipher line is missing from the
digitised set. Total cipher in the letter: ~9 lines (p.[1]) + 2 lines (p.[2]).

**What this changes for the ranking:** the p.[2] block is a small, isolated unit (~55 signs, two lines, clear
text on both sides giving context: "...non e ancora publicato / [cipher] / Rispondetemi ...") -- the cheapest
place to calibrate the key and the natural first blind-transcription unit, priced at about a third of p.[1]'s
nine lines. Tomokiyo's known phrase "la gubernation d'ispagnia" (22 letters plus any nulls) could sit in either
block; H2 now starts on the p.[2] crops and falls back to p.[1]. New H10 (two blind passes on the p.[2] block,
reconciled) inserted at rank 3 ahead of H3 (p.[1]'s nine lines); H3-H9 shift down one rank each, order among
them unchanged.

**Requests this step:** collections.library.yale.edu 2 (of the allowed 6). No other host. No credentials,
no AskUserQuestion, no class change, no reading claimed; rule 10 wording.

## Campaign step H2 (27 Sept 2026, 22:57-23:25 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H2: locate the symbol run the key predicts for Tomokiyo's
known-answer span "la gubernation d'ispagnia" on line crops of the cipher blocks and calibrate the key on it.

**Result: not located.** One blind Sonnet vision pass per block (3 of 4 vision calls; crops + Tomokiyo's key image
only, no plaintext or crib shown to any pass, so each pass is usable as pass A of H10/H3) coded 251 signs across
the letter's ten cipher lines; `passes/crib_search.py` (offline self-test: an embedded synthetic crib reads 22/22,
a noise line 1/22) finds no alignment above **3/22** letters for the crib anywhere, per line or across line
breaks (best per-line 2/22 on p.[2] line 1; "ispagnia" alone best 2/8; "gubernation" best 2/11). Chance-level.
This is conditional on pass A's sign coding, not a negative on the key: a direct look by this runner at
`p1c_L01_s2.jpg` agreed with pass A's codes on roughly two signs in three, and pass A's per-line sign counts
(20-33) run 10-30% under a direct count (about 30-35 signs per full line), so a 22-sign run could be missed on
coding error alone.

**Files:** `images/p2c_L0{1,2}_s{1,2}.jpg` (p.[2] block, region 360,1997,3055,456 native) and
`images/p1c_L0{1..8}_s{1,2}.jpg` (p.[1] block, region 450,440,3000,1740 native), cut with `tools/iiif_lines.py`
from two native IIIF region fetches (`images/src_2_*.jpg`, manifest entries under `iiif_lines`); debug overlays
`images/p*c_lines_debug.jpg` checked before the passes ran (p.[1]: 8 cipher lines, the first partial after the
plain "al R.do frate mio"; p.[2]: 2 lines). `passes/p2_passA_raw.tsv`, `passes/p1_L1-4_passA_raw.tsv`,
`passes/p1_L5-8_passA_raw.tsv` (as reported, per segment), the `*_joined.tsv` files (segments de-duplicated per
each pass's own join note -- the tool's two 2400-px segments of a 3000-3055-px region overlap by 1745-1800 px,
not the ~150 px the briefs said, a brief error the passes each caught themselves), `passes/all_passA_joined.tsv`
(251 signs), `passes/crib_search.py`.

**Two findings that change the ranking:**

1. **The letter's sign inventory exceeds the key on disk.** 55 of 251 signs (22%) match nothing in
   `keys/key_spinelli_c1515.tsv` and recur consistently across all three passes: a plain numeral-2 shape (13),
   an x-cross (12), a "ll" pair of strokes (6-7), a rotated diamond (5), a plus sign (2), a numeral 8 (2), a
   D-shape (2), a circle bisected by a bar (2), a box with a bar (1). Tomokiyo's reconstruction leaves q, x and z
   blank and gives one or two signs per letter; this 1519 letter's hand uses at least 8-9 further sign types.
2. **Under the key as read, the letter frequencies are not Italian.** Of the 145 letter-coded signs, o reads
   15.2% (Italian ~9.8%), p 13.1% (~3.1%), d 10.3% (~3.7%), k 4.8% (~0), while a reads 3.4% (~11.7%), e 2.1%
   (~11.8%), i 0.7% (~11.3%) and b 0 -- the three commonest Italian vowels are nearly absent and three rare
   letters are the commonest. Nulls read 49/251 = 20%. Either pass A's shape-to-code matching is unreliable at
   this resolution, or the frequent shapes the key labels o (7-hook), p (9-loop), d (zigzag) carry different values
   in this letter than in Tomokiyo's table, or the unmapped shapes are the missing vowel homophones. Any of the
   three means a key-coded pass cannot be reconciled row by row (the transcription brief's Raince/Salviati lesson):
   the next transcription step codes signs against a glyph atlas built from this letter's own ink
   (`tools/glyph_atlas.py`, the dupuy452-carpi-1520 method), not against the key.

**Key discrepancy logged (grade M):** the key image `spinelly1515.png` shows SIX word-code symbols under five
headers -- a b-with-bottom-loop ("I"), a note-shape ("of"), a 2-with-bar AND a 4-with-plus both under "Emperor
King of Arragon", a capital-H shape under "Prince of Castile", two adjoining boxes ("new amity"). The tsv on disk
records five, with the 4-with-plus ladder under "Prince of Castile" and no H. The H-shape occurs in the letter
(pass A: 2 on p.[1] line 7; this runner's direct look: several more on p.[1] lines 3-4 and p.[2] line 1). Not
corrected this step (a key edit is its own step, H13).

**Controls:** the crib matcher's synthetic positive control (22/22) and noise control (1/22) above; the Italian
frequency table as the reference for finding 2 (no shuffle control needed for a frequency profile). No reading
claimed; no class change.

**Cost:** 3 Sonnet vision calls, about 680k subagent tokens in total (192k / 243k / 247k), plus the runner's own
turn -- recorded as 3.0 USD against the row's 2.0 est (1.5x; the p.[1] block was run as two calls this step
rather than left to H3, to settle the crib question in one step -- the overrun is this runner's choice, logged).
Requests: collections.library.yale.edu 2 (native region fetches) of the allowed 6. No credentials, no
AskUserQuestion, rule 10 wording, no other target touched.

## Campaign step H11 (27 Sept 2026, 23:21-23:27 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H11: a glyph atlas from the letter's own ink, so that blind
passes code against this hand's sign types rather than against Tomokiyo's key (H2 showed 22% of signs unmapped).

**Done: first atlas, 39 shape codes over 263 segmented boxes (213 on p.[1], 50 on p.[2]), 229 of them labelled
as cipher signs, in `glyphs/`.** No vision subagent call (0 of 4); labelling was this runner's own direct look at
the four contact sheets. Files: `glyphs/prepare.py` (reproducible cleaning step, see below) -> `glyphs/p1_clean.png`,
`glyphs/p2_clean.png`; `tools/glyph_atlas.py segment` -> `glyphs/signs.tsv` (263 boxes), `marks.tsv` (23),
`bitmaps.npz`, `debug_p1.jpg`, `debug_p2.jpg`; `cluster --k 60` with eleven `--split`s -> `clusters.tsv`,
`sheet_signs_00..03.png`; `glyphs/labels.json` (cluster -> code, 60 clusters, 13 marked `_` as fragments, merged
pairs or plain text) -> `glyphs/atlas.tsv`, `glyphs/atlas.png`; `classify --strips` -> `glyphs/boxes_p1.tsv`,
`boxes_p2.tsv` (one row per box in reading order with the kNN code) and `glyphs/strips/p{1,2}_L*{a,b}.jpg` (numbered
per-line strips for the passes). p.[2]'s two lines, which `segment` merged into one (two lines defeat its pitch
autocorrelation), were split by y at the `iiif_lines` band edge (region y 214) and re-numbered.

**Cleaning step, needed and logged (`glyphs/prepare.py`):** on the native region crops the tool's own binarisation
read the brown bleed-through as thousands of specks (median sign height 4 px, 68 "lines" on p.[1]). Using the red
channel only (brown reads light in red, black ink stays dark), background-normalising, thresholding at 0.55 and
dropping components under 200 px area leaves 283 + 69 components at median height ~75 px, from which `segment`
finds 213 + 50 signs in 8 + 1(->2) lines -- the right line count. Worth an option on `tools/glyph_atlas.py`
(Usage 8: an option, not a private copy) -- named as a follow-up, not done this step.

**Atlas by count (code: n; key hint):** SEVEN 25 (7-hook; key o) | OMEGABAR 15 (key null N10) | STROKE 14
(fragments) | TWO 13 (round 2; NOT in key) | NINE 12 (key p) | SIX 12 (6/b; key n) | EIGHT 11 (key null N7) |
PHI 10 (key a) | DIAMOND 9 (NOT in key) | THREE 9 (zigzag; key d) | THETA 8 (circle with bar; NOT in key) | ELOOP 7
(key h/i2) | FOUR 7 (key c) | HCURL 6 (H with curled serifs; the key image's sixth word code) | ECAP, ENN, TWOFLAT,
XCURL 5 each | EM, EX, RHO, TLOOP 4 | AMP, EIGHTBAR, LL, OMEGA2, PI 3 | CBOLD, ESS, LONGS, MU, OMEGADOT, PLUS,
RSTROKE, UCURL 2 | CHOOK, CIRCLE, ENARCH, TEE 1. Signs with no key entry (TWO, TWOFLAT, DIAMOND, THETA, EX, XCURL,
EIGHTBAR, LL, PLUS, ENN) total about 60 of 229 (26%), consistent with H2's 22% from the key-coded passes.

**Quality, honestly:** a direct look at `glyphs/strips/p2_L01a.jpg` shows the segmentation misses some signs (a
small diamond and a 9 unboxed on that strip, the line's opening 4 not boxed) and merges others (box 14 there spans a
phi and the M below it; `_` clusters 23, 25, 34, 41 are merged pairs). Segmented boxes 263 against a direct-look
estimate of about 320-330 signs: **roughly 80-85% of the signs are boxed**, and some clusters are mixed (9.0 flat-2
with two D-shapes; 6.x six with fragments; 19 bold 7 folded into SEVEN). This atlas is a working first inventory for
coding the blind passes, not a settled sign list: a pass that reads the strips must be told to ADD unboxed signs and
SPLIT merged boxes, and the `_`/STROKE rows must be settled by eye before any count is used for cryptanalysis (H12).

**Controls:** none needed for an inventory step (no reading, no class). kNN self-consistency: the classifier's code
equals the cluster label for 170/213 (p.[1]) and 36/50 (p.[2]) boxes -- a measure of cluster tightness, not of
correctness.

**Cost:** no subagent; this runner's own turn only -- recorded as 2.0 USD by estimate (est 3.0). No network
requests this step. No credentials, no AskUserQuestion, rule 10 wording, no other target touched.

## Campaign step H10 (27 Sept 2026, 23:28-23:36 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H10: two independent blind Sonnet passes over p.[2]'s two
cipher lines on H11's numbered strips, coded against the atlas, then reconciled.

**Done: p.[2] reconciled to 52 signs (line 1: 32, line 2: 20), `passes/p2_reconciled.tsv`,** per sign graded AB
(both passes gave the code: 29 signs) or R (settled by this runner's direct look at the strips: 23 signs). Passes:
`passes/p2_atlas_passA.tsv`, `passes/p2_atlas_passB.tsv` (2 of 4 vision calls; each pass saw only the four strips and
`glyphs/atlas.png`; no plaintext, no key, no classifier codes). `passes/compare_box_passes.py` (self-tested on two
fixtures): **boxes coded by both 50; exact agreement 32/50 = 64.0%**, against the transcription brief's 60% gate --
passes, narrowly; 18 disagreements in `passes/p2_atlas_disagreements.tsv`; 4 signs added by pass A only (3 real:
an unboxed diamond and two unboxed 9s; 1 a scribble), 0 by pass B.

**What the disagreements were (all settled from the strips, not by majority):** (1) the p.[2] strips are poor: H11's
`segment` saw p.[2] as ONE line, so its merge rule joined line-1 and line-2 components that overlap in x -- box 2
of line 2 holds line 1's opening 4 plus line 2's long s, box 10 a line-1 diamond plus a line-2 long s, box 13 line
1's "2 9" plus line 2's ampersand, box 16 line 1's q plus line 2's 8, box 14 of line 1 a phi plus line 2's M; both
passes coded these as merges of the wrong signs; (2) pass B's numbering ran one behind from box 10 to 14 of line 1
because it counted the unboxed diamond as box 10, so its codes there are right but mis-addressed; (3) five signs were
unboxed (two 9s, a diamond, an M, an 8) -- pass A added three, pass B none; (4) real shape disagreements: box 6
(PHI vs ELOOP -> PHI), box 20 (ELOOP vs ECAP -> ELOOP), box 22 (LONGS vs RHO -> LONGS), the bold "7 with a long top
bar and hooked foot" (TEE / PI / SEVEN -> SEVEN, atlas cluster 19's shape, three times) -- flagged: the bold 7 may be
a sign distinct from the thin 7, and EX vs XCURL (plain x vs cursive x) may be one sign; both stay separate codes
until the p.[1] counts say otherwise.

**Reconciled sequence (atlas codes; NOT a reading):**
L1: FOUR ENN SEVEN SIX NINE PLUS PHI ENN EIGHT OMEGADOT DIAMOND SEVEN TWO NINE SEVEN THREE PHI EM TWOFLAT NINE EX
HCURL OMEGABAR ELOOP EIGHT LONGS NINE THETA SEVEN PLUS XCURL SEVEN
L2: LONGS LONGS FOUR OMEGABAR ELOOP PI FOUR RHO LONGS OMEGABAR AMP TWOFLAT EM SEVEN EIGHT EIGHT SEVEN XCURL AMP UCURL
Sign count 52 agrees with H2's key-coded pass A (53) and this runner's direct count (about 55).

**Controls:** the pooled-agreement figure above (64.0% vs the 60% gate) is the control this step has; it is low
because of the strip faults in (1)-(3), not only shape confusion -- 11 of the 18 disagreements are cross-line merges,
numbering drift or unboxed signs. No reading, no class change.

**Next (into the table):** H14 now comes before H3 -- re-segment p.[2] as two separate pages (`--page
p2L1=glyphs/p2_clean.png@0,0,3055,214 --page p2L2=...@0,214,3055,456`) so no box spans two lines, add the five
unboxed signs, and re-cut the strips; check p.[1]'s strips for the same fault before H3's passes run on them (p.[1]
was segmented as 8 lines, so cross-line merges should be rare there, but one strip is looked at first).

**Cost:** 2 Sonnet vision calls (114k + 106k subagent tokens) plus this runner's reconciliation turn -- recorded as
1.5 USD (the est). No network requests. No credentials, no AskUserQuestion, rule 10 wording, no other target touched.

## Campaign step H14 (27 Sept 2026, 23:37-23:39 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H14: settle the atlas's segmentation faults before p.[1]'s
passes run on its strips.

**Done: atlas v2.** p.[2] is now segmented as two separate page units (`--page p2L1=glyphs/p2_clean.png@0,0,3055,214`
and `p2L2=...@0,214,3055,456`), so no box can span its two lines; `--merge-vgap 0.3` (was 0.6) stops a descender
from the line above being merged into a p.[1] sign (the fault seen on `p1_L03a` box 1, a plus sign joined to the
zigzag's tail from line 2). Three settings compared on the same cleaned images: vgap 0.6 -> 269 boxes, 0.3 -> 283,
0.2 -> 283 (no further change), so 0.3 is where the cross-line merges stop. Boxes per line now: p.[1] 32, 27, 30,
27, 21, 25, 29, 35 (line 8 includes plain-text fragments from the "La morte" line below); p.[2] 33 and 24 against
H10's reconciled 32 and 20 (the excess is fragments: 1 and 2 boxes classified `_` there, plus one within-line merge,
box 10 of p.[2] line 2, a rho and a long s in one box). Re-clustered (k 60, eighteen `--split`s), relabelled from the
four contact sheets by this runner's direct look: **34 codes, 237 boxes labelled as signs, 20 clusters marked `_`**
(fragments, merged pairs, plain text). `glyphs/labels_v1.json` keeps the v1 labelling. Codes changed from v1: SEVENB
(bold 7 with a long top bar and hooked foot, 11) split from SEVEN (thin 7, 13) so H12 can test whether they are one
sign; DEE (2) split from TWOFLAT (3); CARET (2, key k) new; v1's LONGS and RHO merged into RHO (6); CIRCLE, ENARCH,
CHOOK, RSTROKE, CBOLD, AMP dropped (no cluster of their own in v2). A direct look at the re-cut `p2L2_L01a.jpg`
confirms no box spans two lines any more.

**Atlas v2 by count:** STROKE 20 (fragments, not signs) | OMEGABAR 15 | NINE 14 | TWO 14 | SEVEN 13 | EIGHT 12 |
PHI 11 | SEVENB 11 | SIX 11 | DIAMOND 10 | ELOOP 9 | THREE 9 | XCURL 8 | FOUR 7 | EM 6 | HCURL 6 | RHO 6 | THETA 6 |
TLOOP 6 | ECAP 5 | ENN 5 | TEE 4 | UCURL 4 | LL 3 | MU 3 | TWOFLAT 3 | CARET 2 | DEE 2 | EIGHTBAR 2 | ESS 2 |
OMEGA2 2 | OMEGADOT 2 | PI 2 | PLUS 2. kNN code equals cluster label for 180/226 (p.[1]), 27/33, 15/24.

**Files:** `glyphs/signs.tsv`, `marks.tsv`, `bitmaps.npz`, `clusters.tsv`, `labels.json`, `atlas.tsv`, `atlas.png`,
`boxes_p1.tsv`, `boxes_p2L1.tsv`, `boxes_p2L2.tsv`, `strips/p1_L0*{a,b}.jpg` (16), `strips/p2L{1,2}_L01{a,b}.jpg` (4),
`debug_p*.jpg`. The `prepare.py` cleaning step is unchanged. The tool option for the red-channel/min-area cleaning
(Usage 8) is not written this step -- still a follow-up, named in the table.

**Controls:** none needed (inventory step); the box-per-line counts against H10's reconciled p.[2] counts are the
check (33 vs 32, 24 vs 20, excess explained above). No reading, no class change.

**Cost:** no subagent; this runner's own turn -- recorded as 1.0 USD (est 1.5). No network requests. No credentials,
no AskUserQuestion, rule 10 wording, no other target touched.
