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

## Campaign step H3 (27-28 Sept 2026, 23:41-00:00 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H3: two independent blind Sonnet passes over p.[1]'s eight
cipher lines on the v2 numbered strips (two halves each, 4 vision calls), coded against the v2 atlas, reconciled.

**Result: the pass pair FAILS the transcription brief's 60% agreement gate -- pooled exact agreement 136/233 =
58.4% on p.[1]** (lines 1-4: 66/119 = 55.5%; lines 5-8: 70/114 = 61.4%); whole letter including H10's p.[2] pair
168/283 = 59.4%. Per the brief ("if pass agreement is under 60%, stop and report the blocker; a third pass does not
help"), p.[1] is NOT reconciled this step and no p.[1] sign sequence is written. Files: `passes/p1_L1-4_atlas_passA.tsv`,
`passes/p1_L1-4_atlas_passB.tsv`, `passes/p1_L5-8_atlas_passA.tsv`, `passes/p1_L5-8_atlas_passB.tsv` (as reported; each
pass saw only the strips and `glyphs/atlas.png`), `passes/p1_L1-4_atlas_disagreements.tsv` (53 rows),
`passes/p1_L5-8_atlas_disagreements.tsv` (44 rows). Unboxed additions: pass A added 14 "unboxed" signs on line 1
that sit below the baseline (line 2's signs showing through the strip's bottom edge, which the brief told it to ignore)
and 2 elsewhere; pass B added 12 on lines 5 and 7, mostly tiny ticks it flagged itself as possible noise; one pass
called boxes 8-11 of line 1 plain text (the tail of "mio"), the other cipher fragments -- the plain/cipher boundary on
line 1 needs settling by eye. Both passes agree line 8's strip b carries the plain "La morte" line from about box 30
(pass A) or 20/22 (pass B) onward.

**The blocker, from the disagreement pairs (whole letter, first codes):** ECAP/RHO 7, STROKE/_ 6, ECAP/ELOOP 6,
ELOOP/PHI 4, TWO/TWOFLAT 4, DEE/PHI 3, then FOUR/STROKE, SIX/TLOOP, CARET/STROKE, DIAMOND/PHI, SIX/XCURL,
CARET/SEVENB, MU/UCURL, SEVEN/TEE at 2 each. The atlas's small hook-and-loop codes (ELOOP, ECAP, RHO, TLOOP, UCURL, MU)
cannot be told apart by a pass reading a strip at this scale, and the passes disagree on whether a fragment box is a
sign (STROKE) or nothing (_). **Post-hoc diagnostic, NOT a gate result:** re-scoring the same four passes with those
six hook codes as one family, SEVEN/SEVENB/CARET as one, TWO/TWOFLAT/DEE as one and STROKE = _ gives 203/283 = 71.7%
-- so about two thirds of the disagreement is within-family, which says where the atlas is too fine, not that the
passes agree at 72% (a gate is set before the passes run, not fitted to them afterwards; rule 3's threshold-shopping
lesson).

**Next (into the table, H15):** (a) merge the atlas codes along the confusion families above into a v3 labels.json
(fewer, coarser codes; the family split can be re-attempted later on zoomed crops if it carries information); (b) give
each pass 4x per-box crops from `tools/glyph_atlas.py crop --out glyphs --sid ...` grouped per line, not the strips,
so a small hook is read at a size where its tail is visible; (c) settle the plain/cipher boundary of line 1 and line
8 by this runner's eye before the passes run, so those boxes are excluded rather than argued; (d) TWO FRESH blind
passes under the v3 codes against the same pre-registered 60% gate. The old passes stay on file; they are not
re-scored as the gate.

**Controls:** the gate itself (pre-registered 60% pooled exact agreement, H10 passed it at 64.0%, H3 fails it at
58.4%). No reading, no class change.

**Cost:** 4 Sonnet vision calls (199k + 236k + 213k + 289k subagent tokens, about 940k) plus this runner's
turn -- recorded as 3.0 USD (the est). No network requests. No credentials, no AskUserQuestion, rule 10 wording, no
other target touched.

## Campaign step H15 (28 Sept 2026, 00:01-00:10 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H15: coarser atlas codes, plain/cipher boundaries settled by eye,
4x per-box montages instead of strips, two FRESH blind passes over p.[1] against the pre-registered 60% gate.

**Result: the fresh pass pair PASSES the gate -- pooled exact agreement 145/204 = 71.1% on p.[1]** (lines 1-4:
80/105 = 76.2%; lines 5-8: 65/99 = 65.7%), against H3's 58.4% on the same lines with v2 codes and strips. p.[1] is
reconciled: **213 signs, `passes/p1_reconciled.tsv`**, per sign graded AB (both passes gave the code: 145 boxes) or
R (settled by this runner's direct look at the montage: 68 boxes, 59 disagreements plus 9 extra signs from merged
boxes). Together with H10's p.[2] (52 signs) the letter's cipher is now **265 atlas-coded signs** in two reconciled
files -- a transcription in shape codes, NOT a reading.

**What changed and why it worked:** (1) atlas v3 (`glyphs/labels.json`, v2 kept as `labels_v2.json`): 23 codes,
the six small hook-and-loop codes merged into HOOK, SEVEN/SEVENB/CARET into SEVEN, TWO/TWOFLAT/DEE into TWO,
OMEGABAR/OMEGA2 into OMEGABAR, STROKE = `_`; (2) boundaries settled by eye on the v2 strips before the passes ran:
line 1 boxes 1-11 are the plain "al R.do frate mio" (cipher starts at box 12, a 4), line 8 boxes 18, 22, 24, 25, 27,
28, 30, 32-35 are the plain "La morte" line on a lower baseline -- all excluded from the montages; (3)
`glyphs/montage.py`: every remaining box cut at 4x with `tools/glyph_atlas.py crop --sid` (204 crops, regenerable,
git-ignored) and laid out six to a row with its box number, one image per line (`glyphs/montage/p1_L0*.png`); each
pass read 4 montages + `atlas.png` in one call (about 125k Sonnet tokens per call, half of H3's strip calls).
Passes: `passes/p1_L{1-4,5-8}_v3_pass{C,D}.tsv`, disagreements `passes/p1_L{1-4,5-8}_v3_disagreements.tsv`.

**Settling notes (the R rows carry them):** merged boxes expanded into their signs (L1 30 SIX+NINE, L2 20 HOOK+XCURL,
L3 16 THREE+OMEGABAR, L4 16 SEVEN+HOOK, L4 20 HOOK+OMEGABAR, L5 2 and 14 HOOK+THREE, L6 25 HOOK+SIX, L8 9 NINE+THREE,
L8 15 HOOK+THETA, L8 23 HOOK+EM); two signs outside atlas v3 found on line 8: a reversed E (box 4, code EREV; the
key's null N9 shape) and a bold plain circle (box 5, code CIRCLE; the key's e); two bare strokes on line 7 (boxes
13, 29) set to `_`. Flags for H14/H12: L3 boxes 29-30 (two bare curls, coded HOOK by both passes, AB) may be one
split sign or fragments; the "e + 3 (+ b)" ligature recurs (L5 2, L5 14, L6 25) and may be one compound sign.

**Reconciled p.[1] (atlas codes, 213 signs):**
L1: HOOK SEVEN HOOK THREE HOOK THETA HOOK SEVEN HOOK HOOK NINE NINE HOOK SIX SEVEN HOOK PI OMEGABAR SIX NINE HOOK FOUR
L2: OMEGABAR XCURL OMEGADOT NINE NINE PHI SIX HOOK HCURL EIGHT DIAMOND EM TWO THREE SEVEN OMEGABAR THETA NINE HOOK HOOK
XCURL SEVEN ESS THREE OMEGABAR PHI HOOK FOUR
L3: PLUS HOOK NINE EIGHT HCURL OMEGABAR HOOK HOOK SEVEN TWO HCURL SEVEN THETA HOOK ENN THREE OMEGABAR OMEGADOT DIAMOND
SEVEN HOOK THREE HOOK HOOK SIX NINE FOUR TEE SEVEN HOOK HOOK
L4: PI HOOK HCURL HOOK THREE SEVEN DIAMOND OMEGABAR FOUR HOOK PHI TWO HCURL SEVEN TWO SEVEN HOOK EIGHT ENN XCURL HOOK
OMEGABAR THREE LL TWO DIAMOND HOOK NINE SIX
L5: HOOK HOOK THREE SIX OMEGABAR HOOK SEVEN DIAMOND EIGHT TEE ESS NINE OMEGABAR THETA HOOK THREE SIX HOOK HOOK EIGHT HOOK ESS SIX
L6: SIX OMEGABAR EIGHTBAR SEVEN EM EIGHT LL OMEGABAR XCURL TWO TWO TWO NINE TWO TWO SEVEN HOOK HOOK XCURL TWO PHI SIX
EIGHT THREE HOOK SIX
L7: HOOK SEVEN ENN TWO THREE EM HOOK PHI EIGHT DIAMOND NINE THETA LL TWO ENN HOOK HCURL TWO XCURL EIGHT HOOK PHI HOOK
SEVEN EIGHT XCURL SEVEN
L8: SEVEN PI PHI EREV CIRCLE TWO TWO HOOK NINE THREE HOOK TEE OMEGABAR TEE THREE HOOK THETA TWO HOOK OMEGABAR DIAMOND
HOOK HOOK EM EM FOUR OMEGABAR
Code counts (p.[1]): HOOK 49, SEVEN 19, TWO 17, OMEGABAR 15, THREE 13, NINE 13, SIX 11, EIGHT 10, XCURL 7, PHI 7,
DIAMOND 7, THETA 6, HCURL 6, FOUR 5, EM 5, ENN 4, TEE 4, PI 3, ESS 3, LL 3, OMEGADOT 2, PLUS 1, EIGHTBAR 1, EREV 1,
CIRCLE 1. HOOK at 23% is a family, not one sign; splitting it needs the zoomed crops and is H12/H14's job.

**Controls:** the pre-registered 60% pooled-agreement gate (H10 64.0% pass, H3 58.4% fail, H15 71.1% pass). No
reading, no class change; p2_reconciled.tsv still uses v2 codes (SEVENB, TWOFLAT, RHO, LONGS, UCURL, AMP, ELOOP,
ECAP) -- map them to v3 before any joint count (SEVENB->SEVEN, TWOFLAT->TWO, the hook family->HOOK, AMP->HOOK).

**Cost:** 4 Sonnet vision calls (124k + 127k + 125k + 131k subagent tokens, about 506k) plus this runner's
labelling, montage and settling turns -- recorded as 3.5 USD (the est). No network requests. No credentials, no
AskUserQuestion, rule 10 wording, no other target touched.

## Campaign step H4 (28 Sept 2026, 00:11-00:13 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H4: apply the key on disk (Tomokiyo's reconstruction) to the
atlas-coded transcription and test it against a shuffled-key control (rule 3).

**Result: control-backed negative on the key as read.** `passes/key_control.py` (docstring has the method) maps
each atlas-v3 code to the key value whose drawn shape it matches by eye (`passes/key_atlas_asread.tsv`, grade M
throughout: SEVEN->o, NINE->p, FOUR->c, SIX->n, THREE->d, PHI->a, TEE->b, CIRCLE->e, ESS->s; OMEGABAR, PI, EIGHT, EM,
EREV -> null; HOOK, TWO, XCURL, DIAMOND, THETA, ENN, HCURL, LL, EIGHTBAR, OMEGADOT, PLUS -> no key entry) over the whole
letter (`passes/letter_codes_v3.tsv`, 265 signs: p.[1] 213 from H15, p.[2] 52 from H10 with v2 codes mapped to v3).
Coverage: **94 signs (35%) map to a letter, 44 (17%) to a null, 127 (48%) to nothing in the key.** Score on the mapped
positions, mean log unigram probability under the 16th-century Italian letters corpus `tools/data/it16` (v->u, j->i):
**real key-as-read -2.925; 200 shuffled keys (the same nine letters permuted among the same nine codes) mean -2.982,
sd 0.186, p95 -2.680; 83 of 200 shuffles score at or above the real key.** The key's assignment of these nine shapes
is indistinguishable from a random assignment of the same letters (p about 0.42). Letter profile under the key: o
27.7% (corpus 9.5%), p 18.1% (2.6%), d 14.9% (4.1%), n 12.8% (6.7%), a 9.6% (10.2%), c 8.5% (4.5%), b 4.3% (1.0%),
s 3.2% (5.8%), e 1.1% (12.4%) -- the same shape as H2's finding 2, now on a reconciled transcription.

**What this does and does not say.** It says: the shapes that look like Tomokiyo's 7, 9, 4, 6, 3 do not carry the
values o, p, c, n, d in this letter with anything like Italian frequencies, and half the letter's signs are not in
his table at all -- so the key on disk, read shape-for-shape, does not open this letter, and no decode via
`tools/decode_key.py` is written (there is nothing to grade H). It does not say Tomokiyo or Domnina are wrong: their
table may be right for the 1515 letters and this 1519 letter may use a re-issued or extended key; the shape match by
eye may be wrong for one or two signs (M throughout); and the crib "la gubernation d'ispagnia" that Tomokiyo read has
not been located (H2), so nothing has calibrated any sign against a known letter yet. The control is matched on the
manipulation the key claims (which code gets which letter) and can fail differently from the target (a correct key
would sit above the shuffle p95), so it is a test, not a non-test.

**Next (table):** H12 (cluster frequencies as a homophonic-cipher profile) and a new H16: run the repository's own
substitution families on the 265-code text with the matched control first (`tools/family_run.py` masc/homophonic,
it16 corpus, N=265, K=26), which is the design-matched test the key-as-read could not be.

**Cost:** no subagent; script only -- recorded as 0.5 USD (est 1.0). No network requests. No credentials, no
AskUserQuestion, rule 10 wording, no other target touched.

## Campaign step H12 (28 Sept 2026, 00:14 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H12: the 265-sign code profile against Italian as a homophonic
design, with controls. Script `passes/freq_profile.py`.

**Result: no code is vowel-like above the shuffled-order null; the profile is that of a simple substitution with
nulls and one over-merged family, not a flattened homophonic cipher.** Numbers: 25 distinct codes over N=265;
**index of coincidence 0.0858** against 0.0754 for it16 Italian samples of the same N and 0.0384 for uniform random
26-symbol text -- the cipher text is MORE repetitive than plain Italian, the opposite of what a homophonic key
designed to flatten frequencies produces; the excess is HOOK (59 signs, 22.3%, a family of at least six shapes that
H15 had to merge to pass the agreement gate) plus the nulls (OMEGABAR, PI, EIGHT, EM, EREV: 44 signs, 17%, if the
key's null block is right). Rank/frequency: HOOK 22.3, SEVEN 9.8, TWO 7.5, OMEGABAR 6.8, NINE 6.4, THREE 5.3, EIGHT 5.3,
SIX 4.5, XCURL 3.8, PHI 3.4, FOUR 3.0, DIAMOND 3.0, THETA 2.6, HCURL 2.6, EM 2.6 against it16 e 12.4, i 10.6, a 10.2,
o 9.5, r 6.8, n 6.7, t 6.2, s 5.8, l 5.5, u 4.8, c 4.5, d 4.1. Sukhotin's vowel algorithm: calibrated on 20 it16 samples
of N=265 it finds 4.0 of the 5 vowels with 1.4 false vowels, so it has power at this length on plain substitution;
on the cipher it names HOOK, TWO, OMEGABAR, EIGHT, ESS, PLUS, EREV, OMEGADOT; on 20 order-shuffled copies of the
cipher (no contact structure) it names HOOK 20/20, SEVEN 16/20, TWO 11/20, NINE 10/20, ENN 10/20, EIGHT 9/20,
OMEGABAR 8/20 -- so HOOK and TWO being named on the real text is a frequency artefact the null reproduces, not
evidence. The one signal beyond the null is negative: SEVEN, NINE, ENN and FOUR, which the shuffled null names
vowel-like half the time or more, are NOT named on the real text, so they behave as consonants (or nulls). Nothing
here identifies a vowel code.

**What follows:** with HOOK carrying 22% of the text as one code, no solver can read it (six letters' worth of
signal collapsed into one symbol); H16's family run must either treat HOOK as an unknown-multiplicity homophone
group or wait for H14 to split HOOK on the zoomed crops into its v2 members (ELOOP, ECAP, RHO, TLOOP, UCURL, MU) with
a fresh pass pair at the family level only. Re-rank: H14 (settle the segmentation and split HOOK on the crops4x
montages, rank 5, still open) before H16; H13 (key word-code fix) stays a cheap cleanup.

**Controls:** the it16 same-N calibration (power) and the order-shuffled null (specificity) above. No reading, no
class change.

**Cost:** script only -- recorded as 0.5 USD (est 1.0). No network requests. No credentials, no AskUserQuestion,
rule 10 wording, no other target touched.

## Campaign step H14, second half (28 Sept 2026, 00:15-00:27 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Re-opened H14: split the HOOK family (49 p.[1] signs, 22% of the text) back
into its six v2 member shapes with a blind pass pair on a 4x montage of just those boxes (`glyphs/montage/p1_HOOK.png`,
labels L<line>.<box>) against the v2 atlas image (`glyphs/atlas_v2.png`, kept beside the v3 `atlas.png`).

**Result: FAILS -- the six hook shapes are not separable by blind passes even at 4x.** `passes/p1_HOOK_passE.tsv`,
`passes/p1_HOOK_passF.tsv` (2 vision calls, 103k + 233k subagent tokens): **exact agreement 16/49 = 32.7%** against
the 60% gate; even counting "member vs not a hook at all" as the only distinction, 20/49 = 40.8%. Disagreement pairs:
ELOOP/RHO 7, STROKE/UCURL 3, FRAG/STROKE 3, RHO/UCURL 2, TLOOP/UCURL 2, ELOOP/UCURL 2, ECAP/ELOOP 2, ECAP/UCURL 2, then
singletons. Pass E leaned ELOOP (11) and pass F leaned UCURL (10) and RHO (9) for the same cells: the two readers
drew the family boundaries in different places, which is what a continuum of hand-drawn hooks looks like, not two
noisy readings of six discrete shapes. `passes/p1_HOOK_disagreements.tsv` (33 rows) is on file, unsettled: this
runner does not arbitrate a pair this far under the gate by eye (a reconciler's vote on a 33% pair would be a third
pass, which the transcription brief says does not help).

**What stands:** HOOK stays ONE code in `p1_reconciled.tsv` and `letter_codes_v3.tsv`; the two passes did agree that
a few HOOK cells are not hooks at all (both: L1.16 OMEGA2, L7.24 TWO, L6.18/L1.20 MU, L3.7/L3.29/L3.30 bare strokes)
-- those seven are corrected in `p1_reconciled.tsv` only where BOTH passes agree (grade AB), the rest untouched:
L1.16 -> OMEGABAR (v3 for OMEGA2), L7.24 -> TWO, L3.7 / L3.29 / L3.30 -> `_` (fragments; the two bare curls of L3.29-30
flagged in H15 are confirmed fragments by both passes). MU is a HOOK member in v3, so L1.20 and L6.18 stay HOOK.

**Consequence for the solver step (H16):** the letter cannot be attacked as a plain simple substitution: one symbol
(HOOK, now 20% of the text after the corrections) stands for an unknown set of several plaintext letters, and 17%
of the signs are probable nulls. A matched control for that design is Italian text under a substitution with about
six letters' signs merged into one symbol plus nulls -- not a family `tools/family_run.py` has; running masc or
homophonic against a standard control would be a design-mismatched test (rule 3, Salviati headline). H16 is
re-worded to name that control (a `--param merge=` option on the homophonic family, or a purpose-built control
generator) before any target run, and moved behind the two cheap document steps (H6, H7) that could bring in
Domnina's original Fig.1, which may show a fuller key than Tomokiyo's table and settle the sign inventory from
outside.

**Controls:** the 60% gate (pre-registered). No reading, no class change.

**Cost:** 2 Sonnet vision calls plus this runner's turn -- recorded as 1.5 USD (est 2.5). No network requests.
No credentials, no AskUserQuestion, rule 10 wording, no other target touched.

## Campaign step H6 (28 Sept 2026, 00:28-00:30 UTC) -- not testable this hour

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H6: a Wayback Machine snapshot of Domnina's PDF
(`istina.msu.ru/media/publications/article/a81/378/11992054/Domnina_Spinelli_cipher_EnglishRussian_-_kopiya.pdf`,
the URL `henryvii.htm` links; live 404 to INTAKE-SPINELLI on 27 Sept).

**Result: untestable at 00:29 UTC** -- `web.archive.org/cdx/search/cdx` answered every query (the exact URL, the
`.../11992054/*` prefix) with the Internet Archive's own "Temporarily Offline" page instead of the index, and the
third CDX query plus one live request to the istina publication page (`istina.msu.ru/publications/article/11992054/`,
a different URL from the file, allowed as this step's one istina request) both timed out with no response (curl 28,
HTTP 000). Nothing was learned about whether a snapshot exists. Requests: web.archive.org 3, istina.msu.ru 1.
H6 goes to a `needs: doc` branch ("web.archive.org back online") rather than being re-run every firing against an
offline host (good-citizen rule: no retry loop); the next runner that finds IA answering flips it back to `nobody`.

**Cost:** four curl calls -- recorded as 0.2 USD (est 0.5). No credentials, no AskUserQuestion, no other target touched.

## Campaign step H7 (28 Sept 2026, 00:31-00:34 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H7: the Archives at Yale item-level record and finding aid for
sender, recipient and date corroboration or a transcription note.

**Done.** `archives.yale.edu/repositories/11/archival_objects/2787659` answers curl with 403 but renders in headless
Chromium (`tools/browser_fetch.js`, first try); text saved to `sources/archives-yale/2787659_spinelli_1519-09-07.txt`.
It repeats the Beinecke record's title, dates the item **1519 Sep 7**, places it Spinelli archive (GEN MSS 109) >
Spinelli family papers I > Spinelli Family Papers > Filze 161-168 "Lettere" > **Filza 163**, links the digital object
(218136 -> catalog 10844890, our three canvases) and carries **no transcription or decipherment note**. The parent
Filza 163 page (2785151) answered 503 twice (one retry after a pause; not hit again). The collection's PDF finding aid
(`ead-pdfs.library.yale.edu/11076.pdf`, 4.6 MB, 357 pages, one fetch) is saved as
`sources/archives-yale/11076_spinelli_archive_finding_aid.pdf` with its text extracted by PyMuPDF
(`..._finding_aid.txt`, 27,734 lines) -- a script read it, per Usage 2.

**What the finding aid adds (pp.139-142 of 357):**
- Filza 163 (b. 123, ff. 2462-2467) is a run of Tommaso Spinelli's letters to "il Sig. Canonico Leonardo suo
  fratello" -- **sender and recipient corroborated as brothers**, Tommaso writing as royal orator (1514 Ghent, 1517
  London: "se ne vadi in Spagna per suo Oratore") -- with FOUR Barcelona letters of 1519: 24 Jan (2pp.), 29 May (4pp.),
  6 Jul (4pp.) and **7 Sep (4pp., "part in cipher")** -- ours, f. 2466. The finding aid's "4pp." for a 3-canvas
  digitisation matches H1's reading (the address leaf's blank side is the fourth page).
- The phrase "part in cipher" occurs exactly TWICE in the whole 357-page finding aid: our letter, and **b. 126,
  ff. 2560-65: "Spinelli, Piero. 30 letters; Anversa, Bruggia, Rignalla, Venezia. 90pp. part in cipher. 1514-26"**,
  in the section "Lettere scritte...al...Leonardo Spinelli". The same section holds **b. 126, ff. 2566-87: "Spinelli,
  Tommaso. 86 letters; ... Barchenonia (Barcelona), Seragosa, Villafrancha ... 254pp. 1492-1522"** -- Tommaso's own
  letters to Leonardo, the correspondence Domnina describes as enciphered from 3 January 1515 onward, catalogued
  without a per-item cipher flag. This is the **sign pool** the selection rule asks for (CLAUDE.md pipeline 3: one
  sender, office and key family with 2,000 or more signs): 116 letters, 344 pp., of which an unknown share carries
  cipher in the brothers' key. None of it is known to be digitised (only the Filza 163 item is online per Tomokiyo
  and per the Archives at Yale digital-object link).

**Next (table):** H18 (runnable): query the Beinecke digital catalogue for every digitised GEN MSS 109 item, to see
whether any other Filza 163 / b. 126 letter is online (more ciphertext in the same hand would change the whole
campaign); H17 (`needs: person`): a REQUEST.md / ASKS row for a Beinecke reproduction quote of b. 126 ff. 2560-87
(Piero's 30 "part in cipher" and Tommaso's 86), the pool -- the first one that goes on the card only at stage 2,
which this target has (check-solved verdict INTAKE-SPINELLI, 27 Sept).

**Requests this step:** archives.yale.edu 4 (1 curl 403, 3 browser renders: item page 200, Filza page 503 x2),
ead-pdfs.library.yale.edu 2 (HEAD, GET). No credentials, no AskUserQuestion, rule 10 wording, no other target touched.
**Cost:** browser and curl only -- recorded as 0.5 USD (the est).

## Campaign step H18 (28 Sept 2026, 00:35-00:37 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H18: which GEN MSS 109 items are digitised?

**Result: the pool is partly online.** The Beinecke catalogue answers curl with a 202 challenge (as INTAKE-SPINELLI
found) but renders in headless Chromium: the search `"GEN MSS 109"` returns **92 digitised items**, parsed into
`digitised_genmss109.tsv` (oid, title, image count, date). Among them:
- **all four 1519 Barcelona letters of Filza 163**: 10844891 (24 Jan, 2 images), 10844888 (29 May, 4 images), 10844889
  (6 Jul, 4 images) and ours, 10844890 (7 Sep, 3 images) -- three more letters in the same hand, same year, same
  correspondent, not yet looked at for cipher passages (the finding aid flags only the 7 Sep letter, but its flag is a
  cataloguer's description, not a page-by-page survey);
- eight earlier Tommaso -> Leonardo letters, 1512-1517 (10844878/79/80/81/83/85/86/87), 2-5 images each -- 1517 Jul 22
  (10844886, 4 images) and the undated 10844887 (5 images) fall in the years Domnina says the brothers used cipher;
- **17296147: "Spinelli, Tommaso. 86 letters; ... 1492-1522, n.d." -- 62 images**: the b. 126 ff. 2566-87 bundle
  named in H7 as the pool is itself (partly: 62 images against 254 pp.) digitised;
- 10641921 Filzetta 13, Tommaso's will of 29 Aug 1522, 19 images (context, not cipher).
Requests: collections.library.yale.edu 2 (1 curl 202, 1 browser render). No credentials, no AskUserQuestion, rule 10
wording, no other target touched. **Cost:** recorded as 0.3 USD (est 0.5).

**Consequence:** the campaign's material is no longer one letter of 265 signs. Next: H19 (the three other 1519
Barcelona letters, manifests + page images, direct look for cipher lines, 6 requests), then H20 (the 86-letter
bundle's manifest and a first look at its 62 images, in request-capped batches).

## Campaign step H19 (28 Sept 2026, 00:37-00:38 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H19: the three other 1519 Barcelona letters -- do they carry
cipher? Six requests (3 manifests, 3 first pages at 1500px), all HTTP 200, written into `images/manifest.json`
under `sibling_letters_filza163` with sha1s; manifests saved as `images/manifest_<oid>.json`.

**Result so far (first pages only, direct look, no vision call):**
- **10844891, 24 Jan 1519** (2 canvases, recto + verso): the recto is one page of plain Italian recommending Don
  Giovanni Manuel, dated "Barchinonie xxiiij Ianuarij MDXIX", signed "Vr Thomas de Spinellis Or[ator]" -- **no
  cipher**; the verso is the address side (not fetched). A same-hand plaintext specimen, useful for the hand.
- **10844888, 29 May 1519** (4 canvases): p.[1] is dense plain Italian (court news), **no cipher on p.[1]**; pp.[2]-[3]
  not yet fetched.
- **10844889, 6 Jul 1519** (4 canvases; same 3577x4997 scan size as ours): p.[1] plain Italian (the Electors, the
  audience), **no cipher on p.[1]**; pp.[2]-[3] not yet fetched.
So on the pages seen the cataloguer's "part in cipher" flag on the 7 Sep letter alone holds; the four inner pages of
the May and July letters are the remaining places cipher could sit -- H19b, four requests.

**Requests:** collections.library.yale.edu 6 (this step's cap). No credentials, no AskUserQuestion, rule 10 wording,
no other target touched. **Cost:** recorded as 0.5 USD (est 1.0).

## Campaign step H19b (28 Sept 2026, 00:38-00:41 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. The four inner pages of the 29 May (10867291, 10867292) and 6 Jul
(10867295, 10867296) 1519 letters, at 1500px (4 requests, all HTTP 200, sha1s in `images/manifest.json`).

**Result: negative -- none of the three other 1519 Barcelona letters carries cipher.** All four pages are plain
Italian by direct look (no vision call): the May letter runs to its dated close on p.[3] ("Barchinonie xxviiij Maii
MDXVIIIJ", signed) and the July letter to its dated close on p.[2] ("Barchinonie vj Iulij MDXIX", signed) with a
six-line plain postscript on p.[3]. So within Filza 163's digitised 1519 run the cataloguer's flag is exact: the
7 Sep letter is the only one "part in cipher". Two things worth keeping: the four plain letters are same-hand
plaintext specimens (about 150 lines of Tommaso's Italian, useful for a register-matched judge corpus later, rule
3's era lesson), and the May letter's p.[3] has the plain words "Gubernatori dello Archiepiscopato del nostro R.mo
de Medici" -- Tommaso writes "gubernatori" in clear, which is at least consistent with a "gubernation" in the cipher
passage of the September letter (Tomokiyo's crib), though it locates nothing.

**Requests:** collections.library.yale.edu 4. No credentials, no AskUserQuestion, rule 10 wording, no other target
touched. **Cost:** recorded as 0.3 USD (est 0.5).

## Campaign step H20, batch 1 (28 Sept 2026, 00:39-00:41 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H20: a cipher census of the digitised 86-letter Tommaso bundle
(catalog 17296147, b. 126 ff. 2566-87). Manifest fetched (`images/manifest_17296147.json`): **62 canvases, no
labels**, mixed sizes -- nine wide canvases (about 4400-5350 x 2900-3980: nos. 8, 21, 23, 35, 37, 46, 49, 51, 59)
between runs of portrait pages, i.e. folder covers or openings between letter runs. Canvases 1-5 fetched at 800px
into `images/bundle17296147/` (5 requests):
- c1 (17296293): the archival folder cover, pencilled "Box 126, Folder 2566 ... (3) Spinelli, Tommaso 1492-93" -- the
  first folder holds three letters of 1492-93;
- c2 (17296294): a full page of plain Italian, dated "... octobris MCCCCLXXXXII" and signed "Vr fr Tommaso Spinelli";
  c3 (17296295): its address side, "Ven. Dno Leonardo ... canonico Flor[entino] honorando", Florence; no cipher;
- c4 (17296296): a full page of plain Italian, dated "in Anversa adi xiij di luglio MCCCCLXXXXIII", signed the same;
  c5 (17296297): its address side, "Ven. Domino Leonardo Spinelli canonico Floren[tino]"; no cipher.
So the digitised run begins with the 1492-93 folder, in chronological order; the cipher years (1515 onward, per
Domnina) sit further in, if the 62 images reach them at all. **Next batch: the wide canvases first** (8, 21, 23, 35,
37, then 46, 49, 51, 59), since each is a folder cover pencilled with its folio range and dates -- nine requests map the
whole bundle's chronology and say which portrait pages to look at for cipher, instead of paging through all 57.

**Requests:** collections.library.yale.edu 6 (manifest + 5 images). No credentials, no AskUserQuestion, rule 10
wording, no other target touched. **Cost:** recorded as 0.3 USD (of est 3 for the whole census).

## Campaign step H20b (28 Sept 2026, 00:42-00:43 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Covers-first census: canvases 8, 21, 23, 35, 37 of the bundle at 1000px
(5 requests, `images/bundle17296147/`). Direct look:
- c8 (17296300): folder cover, "Box 126, Folder 2567 -- (6) Spinelli Tommas[o] 1494-95";
- c21 (17296313): folder cover, "Folder 2568 -- Spinelli Tommas 1497";
- c23 (17296315): not a cover: a wide opening, a plain Italian letter page beside a blank leaf (no cipher);
- c35 (17296327): folder cover, "Folder 2569 -- Spinelli Tommas 1505-9";
- c37 (17296329): not a cover: a plain Italian letter page dated "in Bruggia ... di gennaio 1505", signed "T. de
  Spinellis" (no cipher).
So canvases 1-7 = folder 2566 (1492-93, 3 letters), 8-20 = folder 2567 (1494-95, 6 letters), 21-34 = folder 2568
(1497), 35-? = folder 2569 (1505-9). The digitised run is chronological and, at canvas 35 of 62, has reached 1505;
whether it reaches the cipher years (1515 onward) depends on the four remaining wide canvases (46, 49, 51, 59) --
H20c fetches those plus the last canvas (62).

**Requests:** collections.library.yale.edu 5. **Cost:** recorded as 0.3 USD. No credentials, no AskUserQuestion,
rule 10 wording, no other target touched.

## Campaign step H20c (28 Sept 2026, 00:43-00:45 UTC) -- census closed

Runner session_016fvFiTTAhQng2VqbiBDmRE. Canvases 46, 49, 51, 59 and 62 of the bundle at 1000px (5 requests).
Direct look: c46 (17296338) a plain letter opening, no cipher; c49 (17296341) a plain letter dated "... ultimo di
luglio 1507" with a long postscript, no cipher; **c51 (17296343) folder cover "Box 126, Folder 2570 -- Spinelli
Tommas[o] 1505-09"**; c59 (17296351) a plain letter opening, no cipher; **c62 (17296354), the last canvas, an address
side pencilled "1509"**.

**Result: negative for the pool. The 62 digitised images of catalog item 17296147 cover only folders 2566-2570,
Tommaso's letters of 1492-1509** (2566: 1492-93, 3 letters; 2567: 1494-95, 6; 2568: 1497; 2569 and 2570: 1505-09);
every page seen (14 of 62, both text pages and covers) is plain Italian, and the run ends in 1509 -- six years before
the brothers began to use cipher (January 1515, per Domnina). The enciphered correspondence, ff. 2571-2587 (about
1510-1522), is NOT online. So the sign pool named in H7 stays a reproduction request (H17, `needs: person`), now with
its folio range narrowed to ff. 2571-87 plus Piero's ff. 2560-65, and the digitised 1492-1509 pages are one more
same-hand plaintext resource. The census is closed; no H20d.

**Requests:** collections.library.yale.edu 5 (this campaign's Beinecke total today: 6+4+6+5+5 = 26 across five
steps, always 2 s apart, all HTTP 200). **Cost:** recorded as 0.3 USD. No credentials, no AskUserQuestion, rule 10
wording, no other target touched.

## Campaign step H13 (28 Sept 2026, 00:44-00:45 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H13: correct `keys/key_spinelli_c1515.tsv`'s word-code rows from
the key image (H2's discrepancy).

**Done.** From this runner's direct look at `sources/cryptiana/web/img/spinelly1515.png` (H2): the image has SIX
word-code symbols under its five headers. Edits, all grade M (read by eye, no calibration): (1) the 4-with-plus
ladder INTAKE-SPINELLI filed under "Prince of Castile" moves to "Emperor King of Arragon" as that header's second
symbol (with the 2-with-bar, now marked row 1 of 2); (2) a new row, "capital H shape with curled serifs" = "Prince of
Castile" -- the sixth symbol, missed by INTAKE's two blind passes (both counted five); it is the atlas code HCURL,
which occurs 7 times in the 1519 letter, the only key word-code shape seen there; (3) a header paragraph recording
that the letter's own inventory goes beyond the table (about 48% of signs unmapped) and that the shape-for-shape
application fails a shuffled-key control (H4), so the table is a period-adjacent reconstruction of the 1515 cipher,
not a key that opens the 1519 letter as read; total symbols 43 (was 42). `tools/key_design.py` rebuilt
KEY-DESIGN.tsv (164 rows, 108 usable) and `--check` passes; `tools/decode_key.py`'s loader reads the table (44 rows).
No reading, no class change. **Cost:** recorded as 0.3 USD (est 0.5). No requests.

## Campaign step H5 (28 Sept 2026, 00:45 UTC) -- dropped as moot

Hypothesis H5 asked whether q, x, z (the key's three blank columns) appear in H4's decode. H4 produced no decode: the
key as read maps 35% of the signs and fails its shuffled-key control, so nothing can be said about q/x/z from it; the
question only becomes testable with a key that reads the letter (or Domnina's own Fig.1, H8). Dropped with that
reason; the plaintext frequency argument stands on its own (q, x, z together are under 1% of Italian text, so their
absence from a 45-row reconstruction built from a few letters is expected either way).

## Campaign step H16 (28 Sept 2026, 00:46-00:49 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H16: the repository's substitution families on the 262-code
letter, matched control first (rule 3, `tools/family_run.py`).

**Done: spec written, control run, target run as a labelled non-test.** `specs/spinelli-beinecke-c1515.json` (262
atlas-v3 codes as space-separated symbols, 25 types, it16 judge corpora, the constraints and cheap tests recorded);
`ciphertext.txt` (the coded sequence, ten lines, header says it is not a reading). `family_run.py --family masc`:
- **CONTROL** (it16 Italian windows of N=262 under a random simple substitution, K=20-21 letters, 3 seeds, 8 restarts):
  recovery **0.959 (0.927-0.989)**, gate 0.6 met -- a plain substitution IS readable by the tool at this length, so
  length alone does not excuse a failure on this letter.
- **TARGET** masc: best score -701.9, worse than every control decode (-547 to -657); judge FAIL (language score
  -1.259 vs real_p05 -0.964, above null_p99 -1.753); the decode is not Italian ("eiesoreieettetie..."). **Logged as a
  non-test for the letter, not a negative**: the control is a one-sign-per-letter substitution, the letter (as coded)
  has one symbol, HOOK, standing for several letters (22% of the text; the H14 split failed at 32.7%) and about 17%
  probable nulls, a design masc cannot represent -- the Salviati lesson (rule 3): match the design, not only N and K.
Both rows are in `HYPOTHESES.md` (the tool's own table) and the spec's `cheap_test_done`.

**What a real test needs (H22):** a control generator that takes Italian text of N=262, applies a substitution, merges
the signs of about six letters into one symbol and inserts about 17% nulls, then runs the same anneal -- either a
`--param merge=6 nulls=0.17` on `tools/families/homophonic.py` (Usage 8: an option, not a private script) or the
family `block_homophonic`/`nomenclator` if one of them already models many-to-one symbols (not checked this step). If
that control reads under the gate, the single letter is untestable by this route at its own length, and the campaign's
remaining routes are documents: Domnina's Fig.1 (H6/H8/H23) and the reproduction order for the enciphered years (H17).

**Controls:** the masc control above (0.959). No reading, no class change. **Cost:** three family_run invocations,
seconds of CPU -- recorded as 1.0 USD (est 5). No requests. No credentials, no AskUserQuestion, rule 10 wording.

## Campaign step H23 (28 Sept 2026, 00:50-00:51 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H23: an open-index copy of Domnina's paper. Keys checked by
name only (CORE_API_KEY, OPENALEX_KEY, S2_KEY, GOOGLE_BOOKS_KEY all present), sent as headers or query parameter per
CLAUDE.md's access playbook, never printed. Five requests, all HTTP 200.

**Result: no open-access copy located; two later works that cite the paper found.**
- CORE `"Ciphers in Early Tudor Diplomacy" OR (Domnina Spinelli cipher)`: 0 hits.
- OpenAlex `Domnina "Early Tudor Diplomacy" ciphers`: 1 hit, not Domnina's -- **Sergey M. Ryabov, "Secrets of the
  Foreign Policy of the Last Valois in Northern Europe: The Diplomatic Cipher of Charle[s IX?]...", Quaestio Rossica
  2025, doi 10.15826/qr.2025.4.1034, open access at the DOI** -- a 2025 paper on 16th-century diplomatic ciphers that
  OpenAlex matches to the query, so it likely cites Domnina; not fetched this step (H24).
- Semantic Scholar: 1 hit, a 2013 review of Adams and Cox, *Diplomacy and Early Modern Culture* -- not it.
- Google Books API (`country=US`): 3 hits; one relevant -- **Georg R. Kaulfersch, *Ein Gesandter in der ersten
  Sattelzeit der Diplomatie* (2025), PARTIAL view, id y1ZVEQAAQBAJ**, whose snippet reads "Domnina, Ekaterina, Ciphers
  in Early Tudor Diplomacy. The Case of Tommaso Spinelli's Private Le[tters ...]" -- the paper's full title, and a
  2025 monograph on an early-16th-century envoy (Spinelli?) that cites it; the two 1848 *Documenti infami* hits are
  noise. A second query (`"Ciphers in Early Tudor Diplomacy" Spinelli`) returned 0.
So Domnina's PDF stays unreachable (istina 404 / timeout, IA offline, no OA mirror in three indexes); the paper's full
title is now on file for the verifier's search log and a JSTOR row (H9), and two 2025 works cite it -- Kaulfersch's
book may quote or reproduce her cipher table (a Google Books snippet search inside that volume for "Spinelli" and
"cipher" is one cheap next request), and Ryabov's OA paper can be fetched and grepped (H24).

**Requests:** api.core.ac.uk 1, api.openalex.org 1, api.semanticscholar.org 1, www.googleapis.com 2. **Cost:** recorded
as 0.3 USD (est 0.5). No credentials printed, no AskUserQuestion, rule 10 wording, no other target touched.

## Campaign step H24 (28 Sept 2026, 00:51-00:53 UTC)

Runner session_016fvFiTTAhQng2VqbiBDmRE. Hypothesis H24: do the two 2025 works that cite Domnina quote her table or
her reading? Three requests (the Ryabov DOI landing page; two Google Books API snippet queries with `inauthor:Kaulfersch`).

**Result: neither quotes the key, but both fix the citation and one adds a fact about the key's use.**
- Ryabov 2025 (Quaestio Rossica, `qr.urfu.ru/ojs/index.php/qr/article/view/qr.1034`): the landing page carries the
  reference list only (no PDF link visible to curl); it gives Domnina's citation in full -- **Domnina, E. (2015).
  "Ciphers in Early Tudor Diplomacy: The Case of Tommaso Spinelli's Private Letters", in *Geheime Post. Kryptologie und
  Stenographie der diplomatischen Korrespondenz europäischer Höfe während der Frühen Neuzeit* (Historische
  Forschungen, vol. 106), pp. 181-194** -- and a second Domnina paper, "Nicodemo Tranchedini's Diplomatic Cipher: New
  Evidence", *HistoCrypt 2018*, pp. 3-7 (open proceedings, a possible route to her contact details or method).
- Kaulfersch 2025 (*Ein Gesandter in der ersten Sattelzeit der Diplomatie. Die Vielfalt der Rollen und Praktiken bei
  Johann Maria Warschitz (d. 1541/42)*, Böhlau, 526 pp., Google Books id y1ZVEQAAQBAJ, partial view): two snippets --
  "... Spinelli, der dreimal um die konsequente Anwendung seines Schlüssels bitten musste, bevor ihm Lordkanzler
  Thomas [Wolsey?] ... Chiffre konversierte" and "... Spinelli für den Rest seiner diplomatischen Laufbahn auf einen
  Schlüssel zu verlassen schien ... Domnina, Ciphers, 185" -- i.e. Kaulfersch reads Domnina p.185 as saying **Spinelli
  seems to have relied on ONE key for the rest of his diplomatic career**. If that is right, the 1519 letter should
  use the same key as the 1515 letters Domnina reconstructed, and the failure of the key as read (H4) points at the
  transcription and atlas (HOOK, the 48% of unmapped shapes) or at Tomokiyo's redrawing being incomplete relative to
  Domnina's Fig.1 -- not at a re-issued key. That sharpens H8 (Domnina's own Fig.1 is the document to get) and H21/H22.
Both are secondary sources for the verifier's log and for a JSTOR row on *Geheime Post* (H9); neither prints a reading
of the 7 Sept 1519 letter.

**Requests:** doi.org -> qr.urfu.ru 1, www.googleapis.com 2. **Cost:** recorded as 0.3 USD (est 0.5). No credentials
printed, no AskUserQuestion, rule 10 wording, no other target touched.

## Campaign step H22 (28 Sept 2026, 01:50-02:02 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S (replacing session_016fvFiTTAhQng2VqbiBDmRE, which stopped at 00:55 UTC at
717k context). Hypothesis H22: a design-matched control for the solver route -- Italian text under a substitution in
which the signs of about six letters have collapsed into one symbol (the letter's HOOK family, 54 of 262 signs, the
H14 split failed at 32.7%) and about 17% of the tokens are nulls (44 of 262 by the key-as-read map, H4) -- so that a
solver failure on the letter can be read against a control of the same design, not only the same N and K (rule 3,
the Salviati lesson; H16 logged the masc run as a design-mismatched non-test for exactly this reason).

**Tool change (Usage 8: an option, not a private script):** `tools/families/homophonic.py` now takes `--param merge=k
nulls=p` (`null_types`, `merge_share` optional). The control window is N - round(N*p) letters; the k merged letters
are the random k-subset of the window's letters whose combined share is nearest the target's own top-sign share
over its letter tokens (HOOK 54/218 = 0.248); the rest get K - 1 - null_types signs by the ordinary allotment; nulls
sit at random positions, drawn uniformly over the null signs; the returned plain string carries '-' at null
positions and `score_recovery` skips them (recovery = letter positions read correctly). Because the merged symbol
can read at most one of its letters right, `make_control` prints the design's recovery ceiling beside the merged
letters. Offline test `tools/tests/test_homophonic_merge.py` (shape, exact null count, one shared sign, null signs
map to '-', ceiling arithmetic, `merge=0 nulls=0` byte-identical to the old control) passes; the older
`test_homophonic_family.py` still passes. `tools/family_run.py`'s family listing names the option. Neither
`block_homophonic` nor `nomenclator` models a many-letters-to-one-sign symbol (docstrings read first, as the row
asked), so the option went on the homophonic family.

**Result: the design-matched CONTROL reads far under the gate -- the annealer cannot read this design at the
letter's own length, so the target was never run (exit 3, rule 3 mechanically).** All rows are in HYPOTHESES.md
(the tool's own table, 01:50-01:5x UTC), it16 corpora, N=262 (the target's own, `--tokens space`), K=25, 8
restarts, seeds 1-3:

| control design | recovery mean (range) | ceiling | gate 0.6 |
|---|---|---|---|
| merge=6 nulls=0.17 (the letter's design) | **0.120 (0.009-0.258)** | 0.84-0.86 | NOT met |
| merge=6 nulls=0 (merge alone) | 0.388 (0.340-0.462) | 0.86-0.90 | NOT met |
| merge=0 nulls=0.17 (nulls alone) | 0.966 (0.963-0.972) | 1.00 | met |
| plain substitution (H16, for reference) | 0.959 (0.927-0.989) | 1.00 | met |
| merge=6 nulls=0.17 at projected pool N=1000 (--control-n) | 0.479 (0.304-0.763) | 0.82-0.83 | NOT met |
| merge=6 nulls=0.17 at projected pool N=2000, iters 40000 | 0.294 (0.000-0.566) | 0.83-0.85 | NOT met (seed 1 unconverged: 0.000, score 400 worse than seed 2) |
| merge=6 nulls=0.17 at projected pool N=2000, iters 150000 (scaled to N) | **0.706 (0.610-0.761)** | 0.83-0.85 | **met** |

Reading of the ablation: **nulls alone cost the solver nothing (0.966); the merged symbol alone drops it to 0.388,
and the two together to 0.120** -- the limit is the one-sign-for-several-letters symbol (HOOK at 21-25% of the
letter tokens), not the nulls and not the length as such. The design-matched control's best scores (-702 to -710)
bracket the target's own masc score from H16 (-701.9), where the clean masc controls scored -547 to -657: to the
annealer the letter looks like this design, not like a plain substitution. At a projected pool of 1000 signs one
seed of three read 0.763, so the design is not unreadable in principle; at a projected pool of 2000 signs with the anneal's iterations scaled to the length (150000, the 40000 default is unconverged there: seed 1 read 0.000 at 40000 and 0.610 at 150000 on the same window), all three seeds clear the gate, mean 0.706 -- the sign pool the selection rule already asks for (2,000 or more signs of one sender, office and key) is about where this design becomes readable by the tool, which prices H17's reproduction order (Tommaso's 1510-22 letters, ff.2571-87, and Piero's 30 'part in cipher').

**What this settles for the campaign:** the solver route on the single letter as coded is **untestable at its
length by this family** (rule 3: a control under its own gate licenses no reading of a target FAIL either way), a
result logged, not a negative on the letter. The routes that remain are (a) shrinking the HOOK share in the
transcription itself (the boxes both H14 passes agreed on -- 16 of 49 -- are a partial split at grade AB; H27), (b) a
solver that treats the merged sign as a per-position wildcard scored under the n-gram model, whose ceiling is 1.0
(H25), (c) the known phrase as a pattern crib on the atlas codes (H28), and (d) the documents and the pool (H6/H8,
H17). No reading, no class change, rule 10 wording throughout.

**Controls:** every number above is a control; no target run happened. **Files:** `tools/families/homophonic.py`,
`tools/tests/test_homophonic_merge.py`, `tools/family_run.py` (listing line), `HYPOTHESES.md` rows of 01:50-01:5x,
no decode files (control-only and gated runs write none). **Cost:** CPU only (each 3-seed battery 20 s to a few
minutes), no vision calls, no network requests, no credentials -- recorded as 2.0 USD against the 4 est (the
runner's own turns). No AskUserQuestion, no other target touched.

## Campaign step H28 (28 Sept 2026, 02:04-02:07 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. Hypothesis H28: the known answer -- the one phrase Tomokiyo reads from this
letter, "la gubernation d'ispagnia" (22 letters after folding, v->u) -- dragged along the 262 atlas-coded signs
(`passes/letter_codes_v3.tsv`, H15/H10) as a PATTERN, not through the key: same code -> same letter within a
placement (and, unless homophones are allowed, different codes -> different letters), HOOK a per-position wildcard
(the H14 split failed; 54 tokens), the five shapes the key-as-read calls null (OMEGABAR, EIGHT, EM, PI, ESS; 47
tokens) skippable up to six times per placement, and, in relaxed runs, up to two positions whose code conflicts with
the placement (a misread sign) tolerated. A different instrument from H2's `crib_search.py`, which needed key-coded
passes (the Raince/Salviati lesson) and read 3/22 at best.

**Tool (Usage 8, shared):** `tools/crib_pattern.py` (`--wild`, `--skip --max-skip`, `--homophones`, `--max-err`,
`--group-col page` so no placement crosses the p.[1]/p.[2] boundary, `--compare` counts agreements with a key as
read). Each consistent placement implies a partial key; its score is that key applied to the WHOLE text, the mean
log unigram probability of the letters produced under it16 (the H4 statistic), so a true placement is one whose
codes carry Italian frequencies over the rest of the letter too. Control (rule 3): the same drag over 200
shuffled-ORDER copies of each page's sequence (N, K, HOOK and null shares unchanged; the placement count and the
best score both depend on order, so the control can differ from the target). Offline test
`tools/tests/test_crib_pattern.py`: a synthetic it16 text of this design (six letters merged into one wild code,
17% nulls over five skip codes, the crib embedded) yields exactly one consistent placement, the true one, its
implied key right on all 11 non-wild codes, score above every one of 30 shuffles (which place nothing) -- also with
homophones and one tolerated error. The instrument has power on a clean design-matched synthetic; passes.

**Result: negative with control -- the phrase does not place in the letter as coded, at any tolerance, above
chance.** it16 corpora, 200 shuffles per row:

| constraints | REAL placements (distinct starts) | shuffles: placements mean / p95 / max | REAL best score | shuffles best score mean / p95 | rank of real |
|---|---|---|---|---|---|
| strict, max-skip 6 | **0** | 0.0 / 0 / 4 | -- | -2.920 / -- | 200/200 shuffles at or above (0 = floor) |
| strict, max-err 1 | 0 | 1.3 / 6 / 91 | -- | -2.800 / -2.725 | 200/200 |
| strict, max-err 2 | 0 | 10.9 / 42 / 454 | -- | -2.764 / -2.570 | 200/200 |
| homophones | 0 | 5.2 / 13 / 352 | -- | -2.687 / -2.565 | 200/200 |
| homophones, max-err 1 | 12 (5 starts) | 46.6 / 186 / 1074 | -2.547 (cov 162) | -2.616 / -2.413 | placements 104/200, score 51/200 at or above |
| homophones, max-err 2 | 161 (23 starts) | 255.4 / 923 / 1804 | -2.547 | -2.499 / -2.367 | placements 98/200, score 148/200 |

Reading: under the strict pattern the real sequence admits NO placement even with two misreads tolerated, while
shuffled copies of the same tokens admit some (mean 10.9 at two errors) -- the real order is, if anything, more
hostile to the crib's letter-repeat pattern than a random order, consistent with H12's finding that the coded text
is more repetitive than Italian (IC 0.0858 vs 0.0754). With homophones allowed and one or two misreads tolerated,
placements appear (the best at start 46-47, p.[1] line 2, implied key DIAMOND=n NINE=e OMEGABAR=a SEVEN=i THREE=a
TWO=o ...) but their number and their best score sit at the shuffled controls' median, and the best placement's
key agrees with the key-as-read on 0 of 14 codes. Nothing here is an anchor. A caveat measured on the synthetic while writing the test: with `--max-err` above 0 the unigram score can be gamed -- a variant of the true placement that declares one rare-letter code an error outscores the true placement (true placement at rank 3 of 9 at one error, 5 of 19 at two, on the synthetic; first of 1 strict and first of 3 with homophones alone) -- so the two `max-err` rows above are read by their placement COUNT against the shuffled control (at the median both times), not by their best score; the strict and homophones-only rows, which rank the true placement first on the synthetic, both read zero on the letter. **Conditional on the transcription
(rule 2):** the pass pair behind p.[1] agreed at 71.1% and p.[2] at 64.0%, so a 22-letter run with 3+ misread
non-HOOK signs, or a null shape outside the five assumed, or a HOOK-family sign transcribed as a distinct code,
would be missed at max-err 2; the negative is "the phrase is not findable as a pattern in this coding," not
"the phrase is not in the letter." It also weakens the assumption behind the campaign's early steps that Tomokiyo's
phrase sits in the p.[2] block or an early p.[1] line as a run of shapes readable shape-for-shape from his table.

**What this suggests:** the coding, not the search, is now the limit on the crib route too -- the same conclusion
as H22 from the solver side. H27 (partial HOOK split from the 16 agreed boxes) and a third-eye pass on the 68
R-graded p.[1] boxes are the transcription steps; a re-run of this tool is one command once either lands.

**Controls:** the shuffled-order battery in every row and the synthetic positive control in the test. No reading, no
class change, rule 10 wording. **Files:** `tools/crib_pattern.py`, `tools/tests/test_crib_pattern.py`, SYSTEM.md
row; outputs in the table above (seconds of CPU per row). **Cost:** CPU only, no vision calls, no requests, no
credentials -- recorded as 1.0 USD (the est). No AskUserQuestion, no other target touched.

## Campaign step H27 (28 Sept 2026, 02:09-02:12 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. Hypothesis H27: shrink the HOOK share in the coded transcription with the
part of the H14 HOOK split that IS supported -- the p.[1] HOOK boxes both blind passes (`passes/p1_HOOK_passE.tsv`,
`passes/p1_HOOK_passF.tsv`) coded as the same v2 member shape -- and re-run H22's design-matched control on the
reduced coding; one gated target run only if the control clears 0.6.

**Built:** `passes/build_letter_codes.py` (rule 7 for a transcription: regenerates `letter_codes_v3.tsv` from the two
reconciled files -- verified byte-identical to the committed H15/H10 file before anything else was written -- and
`letter_codes_v3b.tsv`, plus `ciphertext_v3.txt` / `ciphertext_v3b.txt` as space tokens for family_run's `--cipher`;
`--check` exits 1 if any is stale). v3b: 11 boxes both passes agreed on move from HOOK to their member sub-code at
grade AB (L1.14, L1.31 ELOOP; L1.20, L6.18, L8.10 MU; L1.24, L4.4 TLOOP; L2.8 RHO; L3.2, L8.17 UCURL; L5.16 ECAP) and
L7.17, which both passes called FRAG, is dropped as a fragment (the H14b corrections to L1.16/L7.24/L3.7/L3.29/L3.30
were already in p1_reconciled). The other 33 HOOK boxes (the disagreements) stay HOOK. v3b: **261 codes, K=31, HOOK
40 (15.3% of tokens, 18.7% of the letter tokens after the 47 null-shape tokens; v3 was 54 / 20.6% / 24.8%)**.

**Result: negative with control -- the reduced coding does not make the solver route testable.** `family_run.py
--family homophonic --cipher ciphertext_v3b.txt --param merge=5 nulls=0.17` (merge_share defaults to the new top
share, 0.184): CONTROL recovery **0.066 (0.000-0.129)**, ceilings 0.88-0.92, gate 0.6 NOT met, target not run (exit 3;
HYPOTHESES.md row 02:10). Lower than v3's 0.120: five extra sign types with 1-3 tokens each raise K to 31 and give
the annealer more rare signs to place, which costs more than the smaller merged share saves. The pattern crib re-run
on v3b (`tools/crib_pattern.py`, 200 shuffles each): strict 0 placements (shuffles mean 0.0, max 0), homophones 0
(shuffles mean 2.5), homophones + 1 error 12 placements at the same 5 starts as v3 (start 46-47 and 112; shuffles
mean 33.7, 70/200 at or above; best score -2.572, 45/200 at or above; 0/15 agreement with the key-as-read) -- unchanged
from H28, at chance.

**What this settles:** the supported part of the HOOK split is too small (11 of 54 boxes) to change either route,
and the transcription brief's own rule stands against a third pass on the 33 disagreements (H14b: a 32.7% pair is a
continuum, not two noisy readings), so no third-eye row is added. The coding is now as good as blind passes make it;
what remains on the solver side is a solver that models the family sign (H25), and on the length side the pool (H26 ->
H17). `ciphertext.txt` (H16, the spec's copy with a header) and `ciphertext_v3.txt` carry the same 262 tokens.

**Controls:** the design-matched control battery (3 seeds) and the shuffled-order crib control (200) above. No reading,
no class change, rule 10 wording. **Files:** `passes/build_letter_codes.py`, `passes/letter_codes_v3b.tsv`,
`passes/ciphertext_v3.txt`, `passes/ciphertext_v3b.txt`, HYPOTHESES.md row. **Cost:** CPU only, no vision calls, no
requests, no credentials -- recorded as 1.0 USD (est 1.5). No AskUserQuestion, no other target touched.

## Campaign step H25 (28 Sept 2026, 02:13-02:17 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. Hypothesis H25: the solver side of the design that H22 showed the annealer
cannot read -- let the family sign (HOOK; the control's merged sign sM) be a per-position free letter, so its ceiling
is 1.0 instead of the merge= control's 0.84, and re-run the design-matched control; one gated target run only if it
clears 0.6.

**Tool change (Usage 8):** `--param wild=<sign>[,<sign>]` on `tools/families/homophonic.py`: every occurrence of a
wild sign becomes its own pseudo-sign before `homophonic_anneal.solve`, so the anneal assigns it a letter of its own
under the n-gram model and the unigram KL term; the same param reaches control and target, hence `wild=sM,HOOK`. The
info dict reports the letters each wild sign was read as. Offline test `tools/tests/test_homophonic_wild.py` (shape:
N letters out, the merged sign read as several letters, no pseudo-sign in the key, the no-wild path unchanged)
passes; `test_homophonic_merge.py` still passes; family_run's listing names the option.

**Result: negative with control -- the wild-sign solver lifts the design-matched control from 0.12 to about 0.28
at the letter's length, still far under the gate, and neither more iterations, more restarts nor a projected pool
of 1000 signs brings it there; the target was never run** (HYPOTHESES.md rows 02:14-02:15, it16, merge=6 nulls=0.17,
3 seeds, wild=sM,HOOK):

| run | recovery mean (range) | best scores | gate 0.6 |
|---|---|---|---|
| N=262, iters 40000, 8 restarts | 0.281 (0.134-0.562) | -565 to -592 | NOT met |
| N=262, iters 150000, 8 restarts | 0.272 (0.078-0.406) | -558 to -581 | NOT met |
| N=262, iters 40000, 24 restarts | 0.255 (0.069-0.562) | -565 to -591 (seeds 1 and 3 identical to 8 restarts) | NOT met |
| projected pool N=1000, iters 150000, 8 restarts | 0.379 (0.090-0.558) | -2289 to -2295 | NOT met |
| for reference, no wild (H22): N=262 0.120; N=1000 0.479 (iters 40000); N=2000 0.706 (iters 150000) | | | |

Reading: with the family sign free, the annealer finds decodes that SCORE far better than the true key's neighbourhood
(-565 vs the no-wild -702 at N=262) but read worse -- 54 free positions let the objective be satisfied by wrong
per-position fills, and 24 restarts return the same best-scoring restart as 8 (the objective, not the search, is the
limit; the "more restarts alone" check of rule 3 is negative). At N=1000 the wild control reads LOWER than the no-wild
one (0.379 vs 0.479): the freedom costs more than the ceiling gains once the text is long enough for the merged sign
to be placed as one letter. A per-position wildcard under an n-gram objective is therefore logged as untestable /
not a route for this design at these lengths -- a different instrument (a Viterbi fill of the wild positions given the
key, or a model that scores the family sign as a distribution over its members) would be a new hypothesis, not a
re-tuning of this one; not added, since H22's pool result (0.706 at N=2000 without any of this) already names the
cheaper route: length.

**Controls:** every number above is a control run; no target run. No reading, no class change, rule 10 wording.
**Files:** `tools/families/homophonic.py`, `tools/tests/test_homophonic_wild.py`, `tools/family_run.py` (listing),
HYPOTHESES.md rows. **Cost:** CPU only (about 3 minutes in all), no vision calls, no requests, no credentials --
recorded as 2.0 USD (est 4). No AskUserQuestion, no other target touched.

## Campaign step H26 (28 Sept 2026, 02:18-02:40 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. Hypothesis H26: the pool-length curve of the design-matched control
(merge=6 nulls=0.17, it16, K=25, 3 seeds, 8 restarts, iterations scaled at 75 per sign), to price H17's
reproduction order by the tool rather than by guess.

**Result: the curve is noisy and NOT monotone at 3 seeds -- a pool of 1500-2000 signs gives the solver route a
real chance (single seeds read 0.59-0.83 from N=1000 up, and all three seeds cleared the gate once, at N=2000), but
the mean clears 0.6 at one length only and the N=3000 run does not confirm it.** HYPOTHESES.md rows 02:18-02:39
(this step) and 01:53-02:02 (H22):

| projected N | iters | recovery mean (range) | gate 0.6 |
|---|---|---|---|
| 262 (the letter) | 40000 | 0.120 (0.009-0.258) | no |
| 500 | 37500 | 0.145 (0.000-0.253) | no |
| 1000 | 40000 (H22) / 75000 | 0.479 (0.304-0.763) / 0.377 (0.180-0.593) | no |
| 1500 | 112500 | 0.425 (0.124-0.829) | no |
| 2000 | 40000 (H22) / 150000 (H22) | 0.294 (0.000-0.566) / **0.706 (0.610-0.761)** | no / **yes** |
| 3000 | 225000 | 0.187 (0.054-0.291) | no |

Reading: (1) the letter alone never reads -- the best single seed over every N=262 run this session is 0.258; (2) from
N=1000 up, individual seeds read the design (0.593, 0.829, 0.763, 0.761, 0.747, 0.610), so the design is readable at
pool length, but which seed reads is not predicted by the annealer's own score (at N=3000 the best-scoring seed,
-8771, read worst, 0.054; at N=1500 the seed that read 0.829 had the lowest score) -- the anneal is landing in
wrong optima that the objective prefers, the same shape H25 saw with the wild sign; (3) the N=3000 figure is
therefore likely iteration- or restart-limited, not a property of the length, but that is untested here (a 300-per-sign
run at N=3000 is about half an hour of CPU, beyond this step's box) -- logged as H26b, not asserted. A 3-seed mean is
too few folds to be a gate figure for this curve (rule 3, the es17c fold-count paragraph): the per-seed spread at
every N from 1000 up is wider than the gap to the gate.

**Sizing for H17 (the honest sentence):** with the transcription as coded, the solver route is closed on the single
letter (262 signs) and OPEN but unreliable at a pool of 1500-2000 or more signs -- the sign pool the selection rule
already asks for -- provided the pool is transcribed to the same design (one hook family, the same null shapes). The
reproduction order that would give it: GEN MSS 109 b.126 ff.2571-87 (Tommaso to Leonardo, the 1510-1522 letters of the
86-letter run, whose 1492-1509 folders are online and plain, H20c; 254 pp. for the whole run) and ff.2560-65 (Piero
Spinelli, 30 letters, 90 pp., "part in cipher", 1514-26), both from the finding aid on disk
(`sources/archives-yale/11076_spinelli_archive_finding_aid.txt`). Written into H17's row; REQUEST.md is H17's own
job, whose writing part needs no person (the order and payment do), so H17's needs is flipped to `nobody` for the
next runner with the ASKS row as the hand-off to the owner.

**Controls:** every number is a control run; no target run, no reading, no class change, rule 10 wording.
**Files:** HYPOTHESES.md rows only. **Cost:** CPU only (about 21 minutes for the four batteries), no vision calls,
no requests, no credentials -- recorded as 1.0 USD (the est). No AskUserQuestion, no other target touched.

## Campaign step H29 dropped and H29b (28 Sept 2026, 02:42-02:47 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. The parent's rank-1 row H29 (02:30 UTC) held that every pass so far read
1500-px canvases and asked for native-size fetches. **Checked before spending: the premise is false.** Since H2 the
passes, the atlas and the montages come from two native-size IIIF region fetches --
`images/src_2_10867298_450_440_3000_1740.jpg` (3000x1740 px) and `images/src_2_10867299_360_1997_3055_456.jpg`
(3055x456 px), region requests at `/full/0/` of the 3577x4997 canvas (manifest `iiif_lines` entries) -- which
`glyphs/prepare.py` cleans into `p1_clean.png` (3000x1740) and `p2_clean.png`, the inputs to the atlas, the strips
and the 4x montages (a sign of median height 93 native px shown at about 370 px). Only H1's 1500-px whole-canvas
files served direct looks and the census. No further server pixels exist to fetch; H29 dropped as moot (0.2 USD, no
request). Its untested half -- the reader tier -- became H29b.

**H29b: one blind Opus pass pair on the SAME native 4x montages of p.[1] lines 1-4** (`glyphs/montage/p1_L01-04.png`
+ `atlas.png`, the images H15's Sonnet pair C/D read), same protocol (box-numbered TSV, "+" for a box holding two
signs, NEW:<description> for a shape outside the atlas, no plaintext or key shown), `passes/p1_L1-4_v3_passG.tsv`
and `passH.tsv` (2 vision calls, about 110k tokens each).

**Result: the Opus pair agrees on 94/105 boxes = 89.5%, against the Sonnet pair's 76.2% on the identical images
(gate 60%, pre-registered).** The reader tier, not the pixels, was the larger part of the disagreement. Cross-tier
agreement is 68.6-71.4% (G/H against C/D), and each Opus pass agrees with the current reconciled file on 77-79% of
boxes (the Sonnet passes on 81-84% -- but that file was settled FROM the Sonnet passes, so the comparison is biased
toward them; on the AB-graded boxes the Opus passes read 82-84%). `passes/p1_L1-4_v3_GH_disagreements.tsv` (11
rows, unsettled). Three findings for the transcription:
1. **A shape the atlas lacks:** both Opus readers independently flag boxes L1.18, L1.21 and L3.30 as the same
   non-atlas sign (a bold vertical stroke turning left at the foot, "J-hook"); the Sonnet passes coded them HOOK,
   and H14b's HOOK-split passes had already called L3.30 "not a hook". A JHOOK code is missing from labels.json.
2. **Thirteen boxes where the Opus pair AGREES against the reconciled file**, six of them at grade AB from the Sonnet
   pair: L1.12 FOUR (the previous runner's own direct look in H15 also called box 12 "a 4"; reconciled HOOK), L1.25 and
   L3.24 ESS (reconciled SIX), L2.17 EIGHTBAR (reconciled THETA), L3.14 and L4.2 PHI (reconciled HOOK), L2.5 HOOK
   (reconciled NINE); the rest are merged boxes the Opus pair reads as two signs the way H15's settling notes did
   (L1.30 SIX+NINE, L2.20 HOOK+XCURL, L4.20 HOOK+OMEGABAR; L3.16 TWO+OMEGABAR where H15 settled THREE+OMEGABAR).
3. The 11 Opus disagreements sit in the same places as before: HOOK vs EIGHT (L1.27, L3.2), SIX vs PHI (L1.24, L3.23,
   L4.4), and the J-hook naming.
An AB grade from a pass pair at 76% is not the same grade as one at 89.5%: the reconciled p.[1] should be rebuilt from
Opus passes over all eight lines and p.[2] (H29c, then H30), with JHOOK added to the atlas, before any further
solver or crib run uses it. No reading, no class change; this is a transcription-agreement result only.

**Controls:** the pre-registered 60% gate and H15's own figure on the identical images (76.2%) as the comparison; the
NEW-code and merged-box findings rest on two independent blind readers agreeing. **Cost:** 2 Opus vision calls plus
this runner's turns -- recorded as 6.0 USD (the est). No network requests, no credentials, no AskUserQuestion, rule 10
wording, no other target touched.

## Campaign step H29c (28 Sept 2026, 02:50-02:52 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. Hypothesis H29c: the Opus reader pair on the rest of the letter -- p.[1] lines
5-8 on the existing native 4x montages, and p.[2] on 4x montages cut this step (`glyphs/montage.py p2`, the p2L1/p2L2
segment units of atlas v2, 33 + 24 boxes, no exclusions; `glyphs/montage/p2_L01.png`, `p2_L02.png`, committed; Pillow,
numpy, opencv and scikit-image installed in this container for the crop step). Same blind protocol as H29b, JHOOK
offered as a code for the shape H29b found. Four Opus vision calls (about 108k, 108k, 97k, 97k tokens):
`passes/p1_L5-8_v3_passI.tsv`, `passJ.tsv`, `passes/p2_v3_passK.tsv`, `passL.tsv`.

**Result: the Opus pairs clear the gate everywhere, far above the Sonnet pairs on the same or equivalent images.**

| unit | boxes | Opus pair exact agreement | Sonnet pair on the same images (H15 / H10) | disagreements file |
|---|---|---|---|---|
| p.[1] lines 1-4 (H29b) | 105 | 94 = **89.5%** | 76.2% (C/D) | `p1_L1-4_v3_GH_disagreements.tsv` (11) |
| p.[1] lines 5-8 | 99 | 94 = **94.9%** | 65.7% (C/D) | `p1_L5-8_v3_IJ_disagreements.tsv` (5) |
| p.[2] lines 1-2 (v2 boxes) | 57 | 55 = **96.5%** (98.2% first code) | 64.0% (H10, on the v1 strips; not the same boxes) | `p2_v3_KL_disagreements.tsv` (2) |
| whole letter | 261 | 243 = **93.1%** | 71.1% p.[1] / 64.0% p.[2] | 18 boxes to settle |

Cross-tier agreement on lines 5-8 is 63.6-72.7%, and each Opus pass agrees with the current reconciled file on
76-79% of boxes (88-89% of its AB boxes) -- the reconciled file was settled from the Sonnet passes, so this is the
expected direction. Findings for the rebuild (H30):
1. Lines 5-8: the Opus pair agrees against the reconciled file on 19 boxes, six of them AB from the Sonnet pair
   (L5.1 TEE, L5.13 PHI, L8.10 SIX, and L7.17, L8.1, L8.8, L8.13 read as fragments `_`); the merged boxes it reads
   as two signs match H15's settling notes (L5.2, L5.14 HOOK+THREE; L6.25 HOOK+SIX; L8.9 NINE+THREE; L8.15 HOOK+THETA;
   L8.23 HOOK+EM). Both readers call L8.4 a bold epsilon opening RIGHT, not the reversed E the atlas named EREV: the
   code is renamed in H30 (EPSILON). JHOOK was used once (L7.13, pass I; pass J read a fragment).
2. p.[2]: 48 signs and 7 fragments agreed; the two disagreements are L2.4 (HOOK vs fragment) and L2.10 (HOOK+EIGHT vs
   HOOK). The agreed code counts (SEVEN 7, NINE 4, PHI 4, EIGHT 4, FOUR 3, TWO 3, XCURL 3, OMEGABAR 3, HOOK 3 ...) put
   HOOK at 3 of 48 on p.[2] against 10 of 52 in H10's v2-coded reconciliation -- the Sonnet passes had been reading
   several distinct shapes as hooks.
3. The 18 unsettled boxes are the H30 reconciler's direct-look work, graded R; everything agreed is AB at a pair
   agreement of 89.5-96.5% rather than 64-76%.

**Controls:** the pre-registered 60% gate and the Sonnet pairs' figures on the same images. No reading, no class
change, rule 10 wording. **Cost:** 4 Opus vision calls plus this runner's turns -- recorded as 12.0 USD (the est).
No network requests, no credentials, no AskUserQuestion, no other target touched.

## Campaign step H30 (28 Sept 2026, 02:54-02:58 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. Hypothesis H30: rebuild the coded transcription from the Opus blind pass pairs
(H29b/H29c), then re-run the two instruments that had failed on the Sonnet coding.

**Built (all regenerable, `--check` on each):** `passes/opus_settled.tsv` (this runner's direct-look decision for each
of the 18 pair disagreements, from the 4x montages, one line of reasoning per box), `passes/reconcile_opus.py` (pair
agrees -> AB; disagrees -> the settled code, grade R unless both readers agreed on a shape outside the atlas; "A+B"
boxes expanded into two rows) -> `p1_reconciled_v4.tsv` (216 rows) and `p2_reconciled_v4.tsv` (58 rows): **257 AB,
17 R**, against v3's 145 AB / 68 R on p.[1] alone. `passes/build_letter_codes.py` now also emits `letter_codes_v4.tsv`
and `ciphertext_v4.txt` (fragments dropped): **259 codes, K=26** -- HOOK 38 (14.7% of tokens, 18.2% of the letter
tokens; v3 54 / 20.6% / 24.8%), SEVEN 25, TWO 21, OMEGABAR 19, NINE 17, PHI 17, EIGHT 15, THREE 13, SIX 12, XCURL 10,
DIAMOND 10, FOUR 9, EM 7, HCURL 6, ENN 6, THETA 5, ESS 5, OMEGADOT 4, PI 4, JHOOK 3, PLUS 3, TEE 3, LL 3, EIGHTBAR 2,
EPSILON 1, CIRCLE 1; null-shape tokens (OMEGABAR, EIGHT, EM, PI, ESS) 50 = 19.3%. `glyphs/labels.json` gains JHOOK and
EPSILON descriptions (EREV marked superseded for L8.4); `atlas.png` itself is not regenerated (the two new codes have
3 and 1 tokens). Settling notes worth keeping: the SIX/PHI split both readers made in the same three boxes (L1.24,
L3.23, L4.4) was settled by the presence of a cross bar (bar = PHI); a "large lower loop with a curled top" (g-loop)
recurs at L1.27, L3.2, L7.22, L8.17 and is kept inside HOOK, as the atlas's own rightmost HOOK exemplar, rather than
given a code on one runner's eye; L4.16 is two signs (SEVEN+NINE); L7.13 is a bare stroke.

**Re-runs on v4:**
1. **Design-matched control** (`family_run.py --family homophonic --cipher ciphertext_v4.txt --param merge=5
   nulls=0.19`, it16, 3 seeds, 8 restarts): recovery **0.197 (0.071-0.262)**, ceilings 0.87-0.93, gate NOT met, target
   not run (HYPOTHESES.md row 02:5x). Better than v3's 0.120 and v3b's 0.066, still far under 0.6: the solver route
   stays closed on the single letter (H22/H26 stand).
2. **Pattern crib** (`tools/crib_pattern.py`, 200 shuffles each): strict **0** placements (shuffles mean 0.1, max 13);
   **homophones allowed: 4 placements at ONE start, index 13 = p.[1] line 1 pos 14 (box 25) running into line 2, best
   score -2.523 -- 2 of 200 shuffled-order copies reach that score and 13 of 200 reach 4 placements**; homophones +
   1 error: 48 placements at 5 starts, best still the same -2.523 (12/200 at or above), count 24/200. On v3 and v3b
   the same runs gave nothing above the shuffled median (H28, H27).

**The placement, stated with its caveats (a candidate anchor under the tool's own rule, never a reading):** the window
ESS SEVEN HOOK HOOK PI OMEGABAR SIX NINE HOOK FOUR [OMEGABAR skipped] XCURL OMEGADOT NINE HOOK PHI HOOK HOOK HCURL
[EIGHT skipped] DIAMOND EM TWO THREE reads the 22 letters with six HOOK wildcards (g, u, a, d, s, p) and two null
skips; the implied partial key is ESS=l, SEVEN=a, PI=b, OMEGABAR=e, SIX=r, NINE=n, FOUR=t, XCURL=i, OMEGADOT=o,
PHI=i, HCURL=a, DIAMOND=g, EM=n, TWO=i, THREE=a. Against it: (a) it needs three codes for a (SEVEN, THREE, HCURL)
and three for i (TWO, PHI, XCURL) where Tomokiyo's table has at most pairs, and agrees with the key-as-read on 0 of
15 codes (SEVEN o, NINE p, THREE d, FOUR c, PHI a, SIX n, ESS s there); (b) applied to the whole letter it puts about
44% of the letter tokens on a and i (Italian about 23%) -- a mean log unigram of -2.523 is BETTER than real Italian's
own entropy (about -2.6 nats), the signature of a key that games the unigram statistic by loading frequent codes
onto frequent vowels, which is exactly what the selection statistic rewards; (c) it was found on the third coding
tried and in the second of three constraint settings, so the 2/200 is not a clean p-value; (d) it consumes
OMEGABAR as a letter (e) although the key-as-read calls that shape a null. For it: the shuffled-order control at the
same statistic was passed at both the count and the score for the first time, the placement is unique (one start),
and it sits where a first sentence's opening business would sit (line 1, after the plain "al R.do frate mio" and 13
signs). What would settle it is a statistic NOT used to select it: H31 -- the bigram/trigram log-probability of the
adjacent mapped pairs under the implied key against 200 shuffled-KEY controls (the same 15 letters permuted over the
same 15 codes, the H4 design) and the Italian letter-distribution distance of the mapped text against the same
controls; a placement that survives both is worth a subagent's blind look at the partial decode, and one that does
not is logged as the unigram artefact (b) predicts. No reading is claimed; status unchanged; rule 10 wording.

**Controls:** the design-matched control battery; the shuffled-order crib control (200 per row); the pass pairs'
agreement (89.5-96.5%) behind the AB grades. **Files:** `passes/opus_settled.tsv`, `passes/reconcile_opus.py`,
`passes/p1_reconciled_v4.tsv`, `passes/p2_reconciled_v4.tsv`, `passes/build_letter_codes.py`,
`passes/letter_codes_v4.tsv`, `passes/ciphertext_v4.txt`, `glyphs/labels.json`, HYPOTHESES.md row. **Cost:** this
runner's direct-look turns over six montages and CPU -- recorded as 2.0 USD (the est). No vision calls, no requests,
no credentials, no AskUserQuestion, no other target touched.

## Campaign step H31 (28 Sept 2026, 03:57-03:58 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. Hypothesis H31: test the H30 crib placement (p.[1] line 1 pos 14, the 15-code
partial key ESS=l SEVEN=a PI=b OMEGABAR=e SIX=r NINE=n FOUR=t XCURL=i OMEGADOT=o PHI=i HCURL=a DIAMOND=g EM=n TWO=i
THREE=a) with a statistic it was NOT selected by. Pre-registered pass: above the shuffled-key p95 on the bigram
statistic and not worse than Italian on the letter distribution; else the placement is logged as the unigram artefact
H30 predicted and the crib route on this coding is closed.

**Tool (Usage 8, shared):** `tools/partial_key_test.py` -- mean log P(b|a) over adjacent mapped pairs and log
P(c|ab) over mapped triples under the it16 bigram/trigram model (add-0.5), and KL(mapped letters || Italian);
controls: 200 shuffled KEYS (the same 15 letters permuted over the same 15 codes -- unigram total unchanged, only the
order structure can move) and the best crib placement of each of 50 shuffled-ORDER copies scored on its own text
(placements selected exactly as the real one was). Offline test `tools/tests/test_partial_key_test.py`: on a real
Italian window under a substitution, the true 15-code partial key scores bigram -2.367 against a shuffled-key p95 of
-3.319, and a wrong assignment (-3.538) is not flagged -- the instrument has power on a clean case. SYSTEM.md row added.

**Result: FAIL on the pre-registered criterion -- the placement carries no letter-order structure beyond what a
random assignment of its own letters gives.** 179 mapped tokens of 259, 119 adjacent pairs, 79 triples:

| statistic | real | shuffled-key (200): mean / p95 / max | rank of real | shuffled-order placements (5 of 50 copies placed) |
|---|---|---|---|---|
| bigram mean log P(b\|a) | -2.903 | -3.046 / -2.859 / -2.724 | 26/200 at or above (p about 0.13) | mean -3.153, max -2.765; real 1/5 at or above |
| trigram mean log P(c\|ab) | -3.031 | -3.297 / -3.002 / -2.780 | 17/200 at or above (p about 0.085) | mean -3.469, max -2.779; 1/5 |
| KL from Italian (nats) | 0.555 | 0.614 / p05 0.477 / min 0.449 | 60/200 at or below | mean 0.554; 2/5 |

Reading: the bigram and trigram means sit above the shuffled-key mean but under the p95 (a real Italian partial key
of this size clears the p95 by about one nat on the synthetic), and the letter distribution is no closer to Italian
than a random permutation of the same letters (KL 0.555 against a control mean of 0.614 and a p05 of 0.477). With the
selection caveats already logged in H30 (third coding tried, second of three settings, 0/15 agreement with the
key-as-read, three codes each for a and i), this is the unigram artefact: a 22-letter crib rich in a, i, n placed so
that the letter's most frequent codes carry the most frequent Italian vowels. **The crib route on the v4 coding is
closed** as pre-registered; no anchor, no reading, no class change. What remains for the crib is a different
instrument, not a re-tuning: Domnina's Fig.1 (H6/H8, needs: doc) would fix which shapes are letters and which nulls,
after which the same drag runs as a key test rather than a pattern search.

**Controls:** the two control families above and the tool's synthetic positive/negative test. **Files:**
`tools/partial_key_test.py`, `tools/tests/test_partial_key_test.py`, SYSTEM.md. **Cost:** CPU only (seconds) --
recorded as 1.0 USD (the est). No vision calls, no requests, no credentials, no AskUserQuestion, no other target touched.

## Campaign step H17 (28 Sept 2026, 03:59-04:00 UTC)

Runner session_01213SyYPVrRii7MWRZbyU3S. Hypothesis H17: the pool access request, sized by H22/H26.

**Done: `REQUEST.md` written and ASKS.md row 87 filed.** Route found on Yale's own pages (3 requests this step,
collections not touched): the finding aid (p. 13) says reproductions are ordered by email to beinecke.images@yale.edu
with call number, box and folder numbers; Yale Library's "Request Digitization" page (library.yale.edu, read 28 Sept
2026) says the digitization service is **free of charge**, **up to 4 folders per request** for unbound documents,
**TIFF 400-600 ppi or PDF 300 ppi**, MASV delivery, **10-14 weeks**, no rush orders, requested through Archives at
Yale's Request button ("Request Digitization" in the unsubmitted-requests list). The order: b. 126 f. 2560-65 (Piero,
30 letters, 90 pp., "part in cipher", 1514-26) first, then f. 2571-87 (Tommaso's 1510-1522 letters) in four-folder
batches, TIFF, every leaf. The request quotes the numbers that size it (single letter 0.12-0.20 on the design-matched
control vs 0.6; the design reads at about 2,000 signs, noisily) and promises nothing about a reading.

**Status of the campaign after this step:** every cheap route on the single letter is closed with a control
(solver: H22/H25/H27/H30; crib: H28/H31; transcription: rebuilt at 93% pair agreement, H29b/H29c/H30); the open rows
are the pool (this request, needs: person), H26b (firming the pool-length figure, CPU), H21 (same-hand plaintext
corpus, useful only once there is something to judge), and the document branches (Domnina's Fig.1: H6/H8; H9 the
JSTOR row). No reading, no class change, rule 10 wording.

**Cost:** 3 network requests (library.yale.edu, beinecke.library.yale.edu; 2 s apart), no vision calls, no
credentials -- recorded as 0.5 USD (the est). No AskUserQuestion, no other target touched.
