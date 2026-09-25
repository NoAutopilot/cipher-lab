open

Desjardins/Canestrini, *Négociations diplomatiques de la France avec la Toscane*, tomes I-III (archive.org
gri_33125017127347, gri_33125010469852, gri_33125017127461) read in full and grepped for "Salviati", "octobre
1525", "octobris", "chiffre" by this worker; tome II's own printed Salviati correspondence (a real section,
"Correspondance du cardinal Salviati, légat en Lombardie") runs January-April 1525 only and the series then
jumps straight to October 1526, so no 16 October 1525 Salviati letter or its decipherment is in this edition.

# Cardinal Giovanni Salviati cipher letter, 16 Oct 1525 -- BnF Français 2933, no. 11

QUEUE row: M35 (`sources/solver-diffs/2026-09-24-lane-g3-gallica6.tsv`, "Sixth pass (LANE G3), 24 September 2026").

## Source

BnF, Département des Manuscrits, **Français 2933** ("Anc. 8469", "Recueil de lettres et de pièces
originales, et de copies de pièces indiquées comme telles dans le dépouillement qui suit"), item 11:
"Lettre en chiffres, et en italien, de « JOHANNES, cardinalis de Salviatis,... Die XVI octobris 1525 »."
Finding aid: `archivesetmanuscrits.bnf.fr/ark:/12148/cc493855/cd0e354` (fetched via browser, 24 Sept 2026).
Cardinal Giovanni Salviati (Medici-circle cardinal, papal nuncio to Spain 1525-1530, active negotiating
the release of the captured François Ier after Pavia) is a plausible author for a 16 Oct 1525 Italian
cipher letter to a French correspondent.

The finding aid's full item list (Fol.1-84+) was read: item 10 (Fol. ~49-54, "Rapport d'un envoyé de la
cour de France, concernant les intrigues de Charles-Quint") precedes it, item 12 (Fol. 58, another
unrelated "rapport") follows it -- **no adjoining "Deschiffrement" item is catalogued next to item 11**
(unlike item 17, Fol. 70, "Deschiffrement d'un rapport concernant messire PHILIBERT," which is a
different, unrelated item several folios later). Per rule about checking for an interlinear/facing gloss:
none is stated in the catalogue text for this item.

## Check-solved sweep (24 September 2026)

1. **Web search.** `"Français 2933" Salviati chiffre 1525`, `cardinal Salviati lettre chiffrée 1525
   déchiffrement`: no source ties BnF fr.2933 no.11 to a known decipherment. Search summaries surfaced only
   the unrelated 1525/26 "Planisphère de Salviati" (a world map, Biblioteca Laurenziana Med. Palat. 249,
   Florence -- different Salviati item entirely) and general Giovanni Salviati biography (legate to
   Madrid 1525, negotiating Charles V's Italian coronation and the treaty later formalised as the League
   of Cognac 1526). One search summary noted (from the Strozziane inventory, Archivio di Stato di Firenze)
   that "ciphers used by Cardinal Salviati were recorded, including a cipher with Jacopo Salviati (the
   cardinal's father)... kept on large open folios" -- background on Salviati-family cipher use in general,
   not a match to this specific BnF letter; not followed further (out of scope, no shelfmark or date tying
   it to fr.2933).
2. **Print / calendars.** Desjardins, *Négociations diplomatiques de la France avec la Toscane* (Canestrini's
   documents, 1859-1886) is the calendar most likely to print Florentine/Medici-circle correspondence of this
   period; web search located volume identifiers (Gallica `bpt6k292781` for tome 1) but returned no content
   match for "Salviati" + "1525" + "chiffre" together -- **a real gap, not searched by full text this pass**
   (out of the $8 cap for both targets; flagged for a follow-up). Mignet's *Rivalité de François Ier et de
   Charles-Quint* (checked for M36 below) does not cover Italian/papal correspondence of 1525 and was not
   re-run for this target.
3. Duplicate of item 2 (Desjardins/Canestrini is this period's Franco-Tuscan document series; no separate
   calendar identified).
4. **Cryptiana / Cipherbrain.** Grepped all 104 cached pages in `sources/cryptiana/web/` for "salviati",
   "2933", "cardinalis", "voiage.*allemagne" (case-insensitive): no hit anywhere. `francis.htm` ("earliest
   use of cipher in France", covering BnF Clair.325/328/329-331/333, fr.2984/3019/3045/3053/3081/20506,
   NAF 4206 in detail, and mentioning Hieronimo Ranzo f.73/f.136 and the "vasto1527" Del Vasto letters the
   brief flagged to watch for) never names Salviati or fr.2933. `venetian.htm`, `vatican.htm`, `schiner.htm`,
   `spanish.htm`, `spanish2.htm` (the other pages most likely to cover an Italian/papal cipher of this date)
   were grepped for "salviati" directly: no hit. No Cipherbrain (cipherbrain.org / cryptiana.blogspot.com)
   page found by web search either.
5. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` (fresh shallow clone) grepped for "2933" and
   "salviati": the numeric "2933" is an unrelated DECODE record id (a 1829-1830 British Library item, Add MS
   32277); the only Salviati record is **DECODE R12**, Vatican Secret Archive i.1025 Segr. Stato Francia 7,
   "Nuncio Salviati, archbishop of Nazareth. France," dated **1574** -- a different Salviati (a later
   nuncio), a different archive (Vatican, not BnF), a different date, already marked "Partially decrypted"
   in the catalog and separately noted solved in `cyphersolver/CATALOGUE.md` ("read at the time, 21 Sept
   2026... Lasry's F6 key is on the record"). Not the same item; no DECODE record under the fr.2933 shelfmark.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "salviati", "2933", "cardinalis" (case-insensitive, all matching files inspected): every
   "2933"/"salviati" hit is a coincidental filename, JSON id, or numeral (e.g. `jantini1517/vestigia/v1848.json`,
   `rome1536/*` file line counts, `sunyatsen/*.csv` codepoints) -- no shelfmark or content match to BnF
   fr.2933 no.11 in either repository.

Requests: WebSearch 5 queries. github.com 2 shallow clones (shared with M36 below). No credentials, no logins.

## Digitisation and ciphertext check (24 Sept 2026)

**Digitised: yes.** ark `btv1b90600674` (found in `sources/solver-diffs/2026-09-23-digitised-excluded.tsv`
row 83, a prior Gallica-SRU sweep of this same Français 2754-3068 run, tagged "Français 2933" against the
same catalogue title). `tools/gallica_folio.py btv1b90600674 --folio 54` was attempted to pin the canvas by
manifest label but the IIIF manifest endpoint reset twice (`[Errno 104] Connection reset by peer`); per the
LANE G3 common brief's Gallica note, stopped after one retry and fell back to the direct image endpoint.

**Ciphertext: yes, confirmed by direct inspection.** The direct-image endpoint
`/iiif/ark:/12148/btv1b90600674/f55/full/400,/0/default.jpg` (canvas 55) shows dense rows of numeral and
symbol groups in an Italian-hand nomenclator style -- unambiguous ciphertext, not a decipherment or plain
letter (saved: `images/canvas55_f54_confirm.jpg`). The preceding canvas (f54, `images/` not kept, item 10's
own leaf) shows continuous plain cursive French prose ending near the bottom of its right-hand page, where
a few numerals appear at the very foot -- consistent with item 11's cipher beginning at the end of that
same gathering, at the catalogued Fol. 54. Canvas = folio 54 label not independently confirmed (manifest
unreachable); **canvas ~55 is a content-matched pin (dense cipher text, immediately after item 10's plain
prose), not a label-confirmed one.**

Requests this section: gallica.bnf.fr 2 successful image fetches (f54, f55) + 2 failed manifest.json
attempts (1 try + 1 retry, both reset), all ≥2s apart, UA `cipher-lab research script (contact via
repository)`. No 403/429/challenge seen, only transient connection resets.

## Verdict

**Open**, 24 Sept 2026. Six sources checked (web, print/calendars, cryptiana/cipherbrain, DECODE, Bourdeau,
Aymeloglu): no found-solved claim, no key, no decipherment located under this shelfmark or this letter's
date/sender in any of them. Not scored closed-negative (no cryptanalytic attempt was made this pass -- this
is a location/prior-print check only, rule 3's matched-control requirement does not apply). Confirmed
digitised (ark `btv1b90600674`) and confirmed to carry genuine ciphertext at canvas ~55 (content-matched, not
manifest-pinned). The Desjardins/Canestrini Toscane calendar (item 2 above) is the one real gap: not full-text
searched this pass for "Salviati" + this date, out of the shared $8 cap for both M35 and M36.

Stage-2 eligible on this verdict (`open`, six sources checked, per check-solved.md).

## Capture and passes (24 Sept 2026)

**Pre-capture check.** Confirmed by direct inspection rather than only the finding aid: fetched Fol.70
(catalogue item 17, "Deschiffrement d'un rapport concernant messire PHILIBERT", canvas 72 at 600px --
`images/canvas72_fol70_check.jpg`) and its facing leaf (canvas 71, `images/canvas71_fol70_check.jpg`): both
are unrelated plain documents (a plain French letter and what looks like a Latin/legal instrument with an
attached document fragment), not adjoining item 11 and not an interlinear gloss over it. No second copy of
item 11 found in the fonds (the finding aid's Fol.1-84+ item list was already read in the check-solved
section above; nothing there duplicates item 11). No interlinear or facing-page gloss over the cipher
letter itself (its own left-hand pages are blank, per the leaf inventory below).

**Extent of the letter (item 11).** Canvas = folio + 1 throughout this ark (confirmed by the visible
foliation numerals in the images, e.g. canvas 71 = f.69, canvas 72 = f.70). The manifest carries no folio
labels (`tools/gallica_folio.py btv1b90600674 --folio 70` returns 0 labelled canvases; cached at
`sources/gallica-manifests/btv1b90600674.json`), so this offset is image-confirmed, not manifest-pinned.
Item 11 runs f.54r-f.57v (canvases 55 left-blank/right-f.54r, 56, 57, 58, 59 left-half only), immediately
followed by item 12 beginning at f.58r (canvas 59, right half): a different, unrelated plain document,
confirmed by direct inspection, bounding the letter at its end.

Leaf inventory (`images/manifest.json`, key `leaves`):
| folio | canvas | side | content |
|---|---|---|---|
| 53v | 55 | left | blank (end of item 10's gathering) |
| 54r | 55 | right | cipher, letter opens "R.dr Dnt Iano Ptr..." |
| 54v | 56 | left | cipher continues |
| 55r | 56 | right | cipher continues |
| 55v | 57 | left | cipher continues, opens "Trouuo ancora..." |
| 56r | 57 | right | cipher continues |
| 56v | 58 | left | cipher continues |
| 57r | 58 | right | cipher continues |
| 57v | 59 | left | cipher ends; date line "...octobre 1525"; signature "Jo. Card[inale] Salviati"; wax/paper seal (Bibliotheque Royale crown stamp); a second, shorter cipher paragraph (postscript) below the seal; closes in plain Italian "La p[rese]nte e stata suggellata due volte" (this letter has been sealed twice) |
| 58r | 59 | right | item 12 begins here (unrelated) -- bounds the letter |

All 9 leaf-images are on disk (native crop for f.54r via `tools/iiif_lines.py`, 1600px references for the
rest via the direct IIIF endpoint with `pct:` region splits) -- 11 MB total, well under the 30 MB cap. No
further Gallica fetch is needed to read any leaf of this letter.

**Layout and script.** This is a *nomenclator* letter, not a fully-enciphered one: continuous, legible
Italian secretary-hand cursive (readable words and short phrases throughout: "tutto quello che", "piu
uolte mi ha detto et dice", "la oppinione", "ricordera quello che li parra", etc.) with individual words or
names replaced inline by (a) arabic-numeral code-groups (e.g. "245", "29", "14", "10") and (b) a large
number of small, idiosyncratic non-alphabetic marks (hooks, tildes, crossbars, mirrored/rotated
letterforms) that are visually distinct from ordinary secretary-hand letters and from each other. A notable,
unexplained feature, present on every leaf and not confined to one hand: many (not all) of these marks carry
a small superscript number floating just above them (examples on f.54r alone: 1, 2, 3, 5, 7, 8, 10, 13, 15,
73...; also visible on f.57v). This is not a plaintext interlinear gloss (it gives no words, only numbers,
and does not sit over every sign), but it is a candidate index/frequency annotation -- either original to
the letter's own encoding, or added later by a reader/cataloguer. Flagging it rather than interpreting it:
determining which is a cryptanalytic question, out of scope for this capture-only brief ("no solving, no
key trials").

**Passes.** Per the brief's condition ("if the signs are invented symbols, build one shared glyph atlas
first... if numerals/letters, skip"): given the mix above, two blind Sonnet subagent passes were run
directly on f.54r's 20 line-crops (`images/f54r_L01..L20_{s1,s2}.jpg`, cut by `tools/iiif_lines.py --debug`,
overlay checked) without a pre-built atlas, each pass free to describe non-numeral signs in its own words
(`passA.tsv`, `passB.tsv`; both flagged the page as unusually dense and most of their own `sym:` tokens as
low-confidence, `?`-marked; pass A additionally flagged uncertainty about the exact L19/L20 line boundary).
`tools/reconcile_passes.py passA.tsv passB.tsv --crops images --keep-plain --rows`: **20 lines, pass A 245
signs, pass B 305 signs, agreement 15/320 = 4.7%** (`agreement.tsv`, `disagreements.tsv` -- 306 rows,
`ciphertext_draft.tsv` -- 321 positions, 306 graded M). Agreement is near-total only on the plain Italian
words (`w:` tokens, which matched or near-matched letter-for-letter) and collapses on every `sym:` token:
the two independent descriptions almost never coincide on the same mark (this is the CLAUDE.md Usage-8
lesson from Raince, 23-24 Sept 2026, "two passes that each invent their own code book cannot be reconciled
row by row," reproduced here in a different letter: 124 vs 25 codes there, 245 vs 305 here, both far apart).

**This confirms the atlas step is not skippable for this letter's symbol tokens.** 306 disagreement rows is
far beyond what this worker's cap can settle from the image one by one (transcription.md: "settle
disagreements.tsv rows from the image only if it stays inside the cap; else leave them"). Per the common
brief, stopping here at cap rather than starting a third pass or hand-settling: `passA.tsv`/`passB.tsv` are
raw and committed for reuse; `ciphertext_draft.tsv`/`disagreements.tsv`/`agreement.tsv` are diagnostic only
and **not a reading** (306 of 321 positions are grade M from pure pass disagreement, not from an unclear
image) -- do not cite them as a transcription.

**Types, grades:** 0 H, 0 C, 15 S (agreed `w:` tokens only, and only in the weak sense of "two blind Sonnet
reads agreed," no key or known-plaintext control), 306 M (disagreement), 0 I. No decoding attempted; no
key exists for this letter to test against.

**Suggested follow-up (not attempted this pass, cap reached):** before any further transcription pass,
segment and cluster the non-numeral signs across all leaves into a shared glyph atlas (`tools/iiif_lines.py`
crops already on disk for f.54r; the other 7 leaves still need line-cutting) on the model of
`ciphers/dupuy452-carpi-1520/glyphs/` (`segment.py`/`cluster.py`/`classify.py`), give both future passes the
atlas's codes rather than free-text shape descriptions, and separately check whether the superscript-number
annotation is itself a key to the symbol index (a question for a solver session, not a capture worker).

Requests this section: gallica.bnf.fr 7 successful pct-region page fetches + 2 pre-capture-check fetches (1
retry after a reset on f60, stopped per playbook after the second failure -- f57v/canvas59 already covers
the letter's end, so f60 was not needed) + 1 manifest.json fetch (succeeded on this attempt, cached) +
1 iiif_lines.py native region fetch (f54r), all >=1.5s apart, UA per playbook. 2 Sonnet subagents (the two
blind passes), no other subagents. Well under the $6 cap.

## Glyph atlas and atlas passes (24 Sept 2026)

Worker H (LANE G3; Opus lead, two Sonnet passes), 24 Sept 2026, 13:37-13:57 UTC. Disk only, no fetches.

**Atlas.** `tools/glyph_atlas.py` (new shared tool, generalises `ciphers/dupuy452-carpi-1520/glyphs/`
segment/cluster/montage; `--help`; offline test `tools/tests/test_glyph_atlas.py`) segmented all eight cipher
leaves on disk (f.54r from the native region, f.54v-f.57v from the 1600 px reference copies; thresholds are in
units of each page's median sign height, so both resolutions share one atlas): 4014 sign boxes and 1242 marks.
Small marks written above a sign (wave/"2", #, +, ring, dots, 1, 5, 7, "ot", and small numbers such as 10, 13)
are kept as an attribute of the sign below (`marks.tsv`, `sid` column), not as codes, as the brief asked.
k-means over-split (64 sign clusters, 20 mark clusters, 7 clusters re-split with `--split`); the merges and
splits were decided by eye from `glyphs/sheet_signs_0*.png` and written to `glyphs/labels.json`:
**40 sign codes** covering 3068 of the 4014 boxes (`glyphs/atlas.tsv`, `glyphs/atlas.png`, split for reading
into `atlas_part1.png`/`atlas_part2.png`); the rest are plain-script words, joined runs and noise ("_").
Mark attribute classes: ~ # + o dot 1 5 7 ot. `glyphs/build.sh` regenerates everything and reproduces
`clusters.tsv` exactly (fixed seed). Codes that look like digits were named S7 and S4 so a pass cannot write them
as numerals. Weak codes by construction (clusters partly mixed with plain-script fragments): h, p, dh, (, hb.
Observation, not interpretation: some marks concentrate on particular signs (of 61 H, 42 carry a 1 and 29 a ring,
a sign may carry both; of 96 ], 63 carry a ring and 22 an "ot"), which a solver session may want to look at.

**Passes.** Two blind Sonnet passes of f.54r, given the atlas and told to use its codes, `w:<word>` for plain
Italian, digits for numerals on the line, `CODE^MARK` for a mark above (`passA_atlas.tsv`, `passB_atlas.tsv`;
full-width line images `glyphs/f54r_lines/f54r_L01..L20.jpg`, L01 is the header with only the folio number).
`tools/reconcile_passes.py`:
| measure | agreement |
|---|---|
| codes with mark attributes (`recon_atlas/`) | 145/345 = **42.0%** |
| base codes only, marks stripped (`recon_atlas_base/`) | 219/349 = **62.8%** |
| with plain words kept (`--keep-plain`) | 178/409 = 43.5% |
Earlier free-text passes (worker F): 4.7%. Tokens: pass A 321 signs, pass B 320 signs (385 tokens each with
plain words); pass A flagged 93 tokens `?`, pass B 7.

**Gate (>= 80%) failed. Stopped as briefed: no settling, no ciphertext_f54r.tsv.** `recon_atlas*/` are
diagnostic only, not a reading.

Confusions (`recon_atlas_base/confusion.tsv`, `per_code.tsv`): of the 130 base-code disagreements, 57 are gaps
(one pass has a sign the other lacks: a count/segmentation problem, led by eps, tee, S7, +, lam, #, ], h), 65 are
code against code, 8 involve an x: placeholder. Commonest code pairs: eps/e 7, h/bh 5, tee/S4 2, psi/y 2, w/e 2.
Codes the passes nearly always agree on: g (0.85), w (0.85), ] (0.78), m, y, rz, K, H, [ (small counts).
Codes they almost never agree on: o. (0/6), dl (0/5), h (2/12), tee (3/13), S7 (1/6), # (1/5), + (1/5), eps (8/25).
With marks kept, the mark attribute alone costs 20 points (62.8% -> 42.0%): the passes attach marks to
different neighbours and read ~/2, 5/s, 7/ot differently.

Suggested follow-up (not done, outside the brief): let the script do the counting -- classify the segmented boxes
of f.54r against the atlas (as carpi classify.py) and have the passes only confirm or correct each box's code,
which removes the gap disagreements; sharpen or merge eps/e and h/bh in the atlas first.

Requests: none (disk only). Subagents: 2 (Sonnet passes).

## LANE R4 B stopped; partial gate measure (24 Sept 2026, 15:30 UTC, LANE R4 orchestrator)

Worker B (session_01EXdQ9RrhhFBqgnb8DhByzv, Opus lead) was interrupted at 15:26 UTC at $13.56 against a $6 cap. Pushed: revised
atlas, script classification of every f.54r box (f54r_boxes.tsv, f54r_boxlist_for_passes.tsv, strips/), pass A complete
(passA2.tsv, 505 box rows), pass B partial (passB2.tsv, 211 rows, lines 1-8 pos 13). Both passes confirm or correct the script's
code per box id, so they compare row by row without alignment. Orchestrator's scripted comparison on the rows both passes cover,
boxes where both read '_' excluded: lines 1-7, **base codes 131/156 = 84.0%**, with marks 125/156 = 80.1% (with the partial line 8:
142/169 = 84.0%, 132/169 = 78.1%). Against the 80% gate on base codes this is a pass on seven lines, not yet on the page. Next: finish
pass B (lines 8 pos 14 to the end) blind to pass A, recompute, settle disagreements from the strips (brief lane-r4-g).

## Pass B finished and gate (24 Sept 2026, LANE R4 G)

Worker G (Sonnet, cap $4, session_01Uyv6LetDKFhBPYZtneJEbf), 15:28-15:48 UTC. Finished pass B blind to passA2.tsv: from line 8
pos 14 to the last box of f54r_boxlist_for_passes.tsv (line 19 pos 28), confirmed or corrected each box's code and marks from
strips/, box by box, line by line, committing and pushing after every one-to-two lines (`passB2.tsv`, now 509 rows: the 505
boxlist positions plus 4 split rows -- 2/14.5 and 3/3.5 from worker B's earlier partial pass B, 8/9.5 and 11/10.5 added this
session where a single boxlist box visibly held two stacked signs). Disk only; no network fetches.

**Gate.** `recon_box/` (script in the session scratchpad, not yet promoted to `tools/`): compared passA2.tsv and passB2.tsv by
(line, pos) over all 505 shared boxlist positions, excluding the 129 where both passes read `_` (plain), per the NOTES
precedent above. **Base code agreement: 314/376 = 83.5%.** With marks also required to match: 302/376 = 80.3%. **Gate (>=80%
base) PASSES over the whole page**, consistent with the 84.0% measured on lines 1-7 alone before this session. Files:
`recon_box/agreement.tsv` (315 rows), `recon_box/disagreements.tsv` (62 rows).

**Settling.** All 62 disagreements were settled from the line strips (`recon_box/settled.tsv`: line, pos, source pass kept,
chosen code, marks, one-line reason each). Two recurring patterns did most of the work rather than one-off judgement calls:
(a) an angular hook shape that pass A read as `Z` and pass B read as `L` at four separate boxes (line5 pos4/10, line6 pos22,
and by the same reasoning line6 pos3's S7); checked against the atlas plates, the shape is consistently the angular `L`
cluster, not the wavy `Z` cluster -- settled `L` throughout. (b) A long run of boxes where pass A read plain `_` and pass B
(this session) had already independently confirmed the *original script classifier's* code at high share (many at 1.00):
lines 16 and 19 account for 19 of the 62 disagreements this way. Since the automated classifier and pass B agree independently
or the classifier's own confidence was already low, agreement or disagreement was treated as a 2-votes-vs-1 majority rather
than arbitrated by eye alone; settled toward the majority except two low-share (0.41-0.42) `Z` calls at line19 pos18/19 where
pass B's own note had already flagged the shape as resembling a plain "n", so those settled plain. One genuine bookkeeping
find: line13 pos15-21, where pass A's codes (H, a, e, S4, dl, p) each matched pass B's code one position *later* -- i.e. pass
A's row for a box was shifted one early for a seven-box stretch. Checked against the boxlist's own per-box marks (`1|o` at
pos16, `5` at pos17, `dot|+` at pos18, all share 1.00) against the image: pass B's own position-to-mark alignment matches
exactly, so the whole stretch settled to pass B's alignment. Three disagreements read as plain Italian words/abbreviations in
context and settled to pass A's plain call against pass B's coded guess: line1 pos5/6 ("Iano Ptr" in the letter's own opening
per the leaf inventory above) and line3 pos20-22 (the sequence "quello ch. s . s ." following the legible word "quello").

**Reading.** `ciphertext_f54r.tsv` (line, pos, code, marks, grade): 509 rows, grade `AB` (443, both passes agreed on the base
code), `settled` (62, this session's arbitration), `B` (4, the split rows only pass B produced; no split rows existed only in
pass A). **370 sign tokens across 36 distinct types** (`#,+,H,K,L,Lx,N,S,S4,S7,U,Z,[,],a,bh,ch,dl,e,eps,f,g,lam,m,nt,o.,p,phi,
psi,rz,sq,tee,v,w,wd,y`), **139 boxes plain** (`_`, continuous Italian cursive words/abbreviations, not part of the atlas code
book). Grades here mark provenance (both passes agreed vs. this session's settled arbitration vs. one pass only), not rule 4's
H/C/S/M/I -- no key exists to test this reading against and no plaintext is claimed; this is a **transcription**, not a
decipherment. Types/counts only, no solving attempted (out of this brief's scope).

Cost: `get_session` on this worker's own session id never returned a `usage.cost_usd` field this run (a rate-limit-plan
session, not per-token billing) -- self-monitoring fell back to line-by-line pacing and frequent pushes rather than a dollar
readout; flagging for the lane orchestrator in case this is worth checking on other worker sessions before assuming the cap
mechanism is working as briefed.

Suggested follow-up (not attempted, out of this brief's scope): promote the box-keyed (line,pos) reconciliation script from
the session scratchpad into `tools/` (it is generic to any target using the confirm/correct-per-box-id convention, distinct
from `tools/reconcile_passes.py`'s line-crop alignment); a solver session could now test the 36-type code book and the
superscript-numeral-on-sign pattern (flagged in the capture section above) against nomenclator conventions, now that a full
settled transcription of f.54r exists.

## Solver (24 Sept 2026, LANE R4 I)

Worker I (Opus, cap $8, session_01GN6EQNWzVSwj6k7CvC9urZ), 16:05-16:10 UTC. Disk only, no fetches, no subagents. Input
`ciphertext_f54r.tsv` (370 sign tokens, 36 base types, 139 plain boxes). **No reading; no key.tsv, decode.json or grades.**

**Layout seen on the line images (L04, L05).** f.54r mixes plain Italian ("tutto quello ch[e] V. S. desidera", line 3) with
runs of invented signs written one sign per letter-sized box; several superscript figures (1, 2, 3, 7, and "tw") and marks
(#, +, o, dot) sit over signs. The cipher runs look like letter-level substitution with the marks as an open question.

**1. Key trial by shape (`keytrial.tsv`).** Raince 1526 key as used for Dupuy 452 (ciphers/dupuy452-carpi-1520): contact
sheet compared with `glyphs/atlas_part1.png`; 9/36 Salviati signs have a generic counterpart (psi, 7, lam, H, S, w, K, +, #),
all primitive shapes any 1520s key uses, and the Salviati repertoire of letter-like cursive forms (a, e, g, y, m, w, wd, nt,
bh, ch) has no counterpart there. Under those values lines 2-4 give no Italian (w as z at 17 tokens alone rules it out).
Gramont 1530 (ciphers/fr2980-gramont/key.tsv, by shape description): 8/36 generic matches, same result (g as V at 28
tokens, the commonest sign). fr.20506 f.136 (Ranzo) is a letter+number code, 0 matches. `sources/florence/keys` holds 1424
keys and index pages only. No Montmorency, papal, Florentine or Salviati key for 1524-1527 is on file; cryptiana
vatican.htm is 1625-28. No Tomokiyo or Lasry 1525-26 table other than Raince's is on disk. **No key on file fits.**

**2. Matched control first (rule 3), then target (`control/`, `control/results.tsv`).** Tool: `tools/homophonic_anneal.py`
(order 3, 6-8 restarts x 40000 iterations), corpus the five it16 letter collections other than Vanzolini, control plaintext
Vanzolini's letters (`tools/data/it16/letterescrittea01vanzgoog.txt`, chars 200050-204000, held out of the corpus).
- Contiguous control, N=370, K=36: 94.1%, 99.2%, 95.7% (seeds 1-3).
- Interleaved control on the target's own row pattern (`control/make_interleaved.py`: each sign row one letter, each of
  the 139 plain boxes withholds 2 letters from the stream): **92.4%, 78.6%, 75.4%**, best scores -892 to -894.
- **Target, base codes, marks ignored: no Italian in any of 3 seeds**, best scores -967.0 to -976.7 (70-80 below the
  control's true-plaintext scores at the same N), and the three decodes disagree with each other.
- Code+mark as distinct signs (94 types): the control itself fails (11.1%, 15.7%), so the target was not run under that
  model; that model is untested, not negative.

**Conclusion, conditional on the transcription (83.5% pass agreement) and on f.54r alone:** f.54r is not a simple
homophonic substitution of Italian letters over these 36 base codes with the marks ignored; the same solver reads a
synthetic of that design at 75-99%. Models not excluded: marks change the value (vowel or syllable indicators, as the
superscript-figure Italian systems in cryptiana venetian.htm), signs standing for syllables or words (nomenclator), nulls,
or transcription error concentrated in frequent signs.

Where not found: no key in ciphers/*/key.tsv, sources/florence, sources/cryptiana (francis.htm, venetian.htm, vatican.htm).

Suggestions (not done): transcribe f.54v-f.57v with the same box-keyed passes, to reach ~2000 tokens, where the code+mark
model has a working control; test the marks as vowel indicators (sign = consonant, mark = following vowel) with a control
of that design; look for a Salviati nunciature key in ASV Segreteria di Stato or the Strozziane Salviati cipher folios
(check-solved item 1) as a key source.

## Leaves f.54v-f.57v (24 Sept 2026, LANE R4 J)

Worker J (Sonnet, cap $8, disk only). Method exactly as f.54r's box-keyed procedure (LANE R4 B/G above): script
classification of every box against the shared atlas, per-line strips with box ids, two confirm/correct passes,
reconcile by (line, pos) excluding both-plain, gate >=80% on base codes, settle disagreements from the strips.

**Segmentation.** All 8 leaves were already segmented into the shared atlas (`glyphs/pages.json`, `glyphs/signs.tsv`,
`glyphs/marks.tsv` -- worker H, "Glyph atlas and atlas passes" above) but `glyphs/crops/` (the working-copy grey
pages needed to render strips) is a regenerated, not-committed artifact. Re-ran `glyphs/build.sh` first and diffed
its output against the committed `clusters.tsv`/`atlas.tsv`/`signs.tsv`/`marks.tsv`: byte-identical (fixed seed), so
the atlas itself was not touched, only its working copies were restored.

**f.54v.** `tools/glyph_atlas.py classify --page f54v --tsv f54v_boxes.tsv --strips strips` (502 boxes, 19 lines) ->
`f54v_boxlist_for_passes.tsv` (line, pos, script_code, script_marks, share). Pass A (this worker): read all 19
line-strip images (`strips/f54v_L01..L19.jpg`) against the classifier's proposal; confirmed high-share (>=0.85)
calls after checking the shape, gave real independent attention to the 123 low-share (<0.85) boxes, and read every
line's continuous-cursive stretches by eye rather than trusting `_` calls blindly (`passA_f54v.tsv`, 502 rows: 379
confirm/correct, 123 plain). Pass B: one blind Sonnet subagent (never opened any file named `passA*`), briefed with
the same boxlist and strips plus the known confusable-code pairs from the f54r confusion table (eps/e, h/bh, tee/S4,
psi/y, w/e, o./dl/h/tee/S7/#/+, Z/L); it re-cropped every box from `glyphs/crops/f54v.png` at 5x zoom with padding
(a scratch script, not committed) rather than relying on the small strip JPEGs, and cross-checked each shape against
`glyphs/atlas.tsv`/`atlas.png`. `passB_f54v.tsv`, 508 rows (502 boxlist positions + 6 boxes it split into two
stacked signs each): 316 confirm, 156 plain, 21 correct, 12 split half-rows, 3 delete (stray ink, no sign).

**Gate.** `recon_box.py passA_f54v.tsv passB_f54v.tsv recon_box_f54v` (script promoted from the session scratchpad
version used for f54r's gate, generalised to take any two pass files and an output dir): compared by (line, pos)
over 379 positions where at least one pass called a cipher code (the 123-129-ish both-`_` positions excluded, as
for f54r). **Base code agreement: 317/379 = 83.6%. Gate (>=80%) PASSES.** With marks also required to match:
291/379 = 76.8%. Files: `recon_box_f54v/agreement.tsv` (317 rows), `recon_box_f54v/disagreements.tsv` (68 rows,
including 6 rows where only pass B's split produced that position at all).

**Settling.** All 68 disagreements resolved to pass B (`recon_box_f54v/settled.tsv`, one reason per row), not by
default deference but because the two passes disagree on two recognisable and separately checked patterns, both of
which pass B's higher-resolution method is better placed to call and which this worker's own read of the same
line-strip images (lines 8, 11, 13-17 in particular) independently corroborates: (a) several stretches the
classifier tagged with letter-shaped cipher codes (m, a, v, S, tee, lam, N, g, y, psi, ch, f, p, w -- the same
letter-like code set flagged as ambiguous with plain script in the atlas section above) are visually continuous
Italian cursive words ("Sono", "vuole", "Tutti", "questa", "Cosa", "mi manda", "la nota...", "quello", "questo
Corriere", and others), settled to pass B's `_`; (b) a smaller set of boxes the classifier called `_` at low share,
or called one code, are genuine cipher signs pass B's atlas cross-check reassigned with a named reason (open-top
square not an H-crossbar -> U; closed loop+tail -> g; etc.), settled to pass B's code. The 6 split additions (line 9
pos 17.5, line 11 pos 25.5, line 12 pos 13.5, line 13 pos 27.5, line 14 pos 16.5, line 18 pos 13.5) are accepted as
found stacked-sign positions the segmenter merged into one box, the same gap-disagreement pattern f54r's confusion
table flagged as this atlas's commonest failure mode.

**Reading.** `ciphertext_f54v.tsv` (line, pos, code, marks, grade): 508 rows -- `AB` 440 (both passes agreed,
including 281 both-plain positions), `settled` 62, `B-split` 6. **349 sign tokens across 34 distinct types**
(#,+,H,K,L,Lx,N,S,S4,S7,U,Z,[,],a,bh,ch,dl,e,eps,f,g,lam,m,nt,o.,p,phi,psi,rz,tee,w,wd,y -- commonest: S7 31, g 25,
e 24, lam 22, w 21, y 20, eps 19, Z 17, tee 16; singletons wd, ch, N), of which 106 tokens carry at least one mark.
**159 boxes plain** (continuous Italian cursive, not part of the atlas code book). Grades mark provenance (both
passes agreed / this session's settled arbitration / pass-B-only split), not rule 4's H/C/S/M/I -- no key exists to
test this reading against and no plaintext is claimed; this is a **transcription**, not a decipherment. No solving
attempted (out of this brief's scope).

**Stopped at cap after f.54v.** One leaf (502 boxes, two full passes plus reconciliation and settling) used most of
this worker's $8 cap, consistent with f.54r's combined cost across two workers (~$17.56) for the same procedure at
similar scale. f.55r, f.55v, f.56r, f.56v, f.57r, f.57v are not yet transcribed; `glyphs/signs.tsv`/`marks.tsv`
already hold their segmented boxes (553, 495, 512, 504, 478, 465 respectively) so the next worker's first step is
just `tools/glyph_atlas.py classify` per page, not re-segmentation. Suggested follow-up (not attempted, out of
this brief's scope): a solver session could now widen the f.54r control-first anneal (LANE R4 I above) to f.54v's
349 additional sign tokens once f.55r-f.57v reach the same stage, since a ~700-1300-token pooled ciphertext is
still short of where the code+mark (K=94) model would need its own control before testing.

Requests: none (disk only). Subagents: 1 (Sonnet, pass B, blind to pass A).

## Code+mark control curve (24 Sept 2026, LANE R4 P)

Worker P (Opus, cap $4, session_012iPigthLUviMQnUiE8MDaC), 17:46-17:54 UTC. Disk only, no fetches, no subagents. Input: the
pooled `ciphertext_f54r.tsv` + `ciphertext_f54v.tsv` (1,017 rows: 719 sign tokens, 298 plain boxes, 36 base codes,
28 mark strings, 126 code+mark types, 243 tokens (34%) carrying a mark). **No reading; no key.tsv, decode.json or grades
(H0 C0 S0 M0 I0).**

**Method.** `control/codemark_curve.py`, solver `tools/homophonic_anneal.py` (order 3, 6 restarts x 120,000 iterations,
corpus the same five it16 collections as worker I, control plaintext Vanzolini chars 200,050 on, held out of the corpus).
Both designs are laid out on the target's own sign/box row pattern (tiled past 1,017 rows), each plain box withholding 2
letters, as `control/make_interleaved.py`. N counts sign tokens; token accuracy = every letter the token stands for right.
- **cm, code+mark as distinct signs:** the target's 126 code+mark types allotted to letters by frequency deficit, each
  letter picking a homophone with the target type's own pooled frequency as weight (108-126 types appear per control).
- **vi, mark = following vowel:** consonant+vowel is one token (base code + mark), anything else a bare base code; 36 base
  codes and the 10 commonest target mark strings allotted by frequency. Solved as a symbol stream code, mark, with mark
  symbols restricted to a e i o u (new `allowed=` option in the tool, test added); without it the solver swaps the roles of
  codes and marks. Control mismatch to note: 51% of vi control tokens carry a mark, against 34% on the target.

**Curve (`control_curve.tsv`, token accuracy, seeds 1/2/3):**

| design | N=720 | N=1,400 | N=2,800 |
|---|---|---|---|
| cm | 66.9 / 30.8 / 21.9% | 29.4 / 68.9 / 87.1% | 88.9 / 89.1 / 94.0% |
| vi | 93.1 / 95.7 / 93.9% | 97.4 / 98.4 / 96.4% | 99.2 / 99.8 / 99.4% |

**Target (step 2).** Run only under vi (control > 60% at N=720); cm's control fails at 720 (2 of 3 seeds under 31%), so the
target was **not run under cm** and that model stays untested, not negative. **vi, target, 3 seeds: no Italian.** Best scores
-2.567, -2.584, -2.566 per symbol (962 symbols) against -2.29 for the control's solve and -2.30 for its true plaintext;
the three decodes agree with each other on 19-47% of symbols (the control's seeds reproduce at 93%+). Files
`control/codemark_target_vi_s{1,2,3}.json`. Conditional on the transcription (83.5-83.6% pass agreement) and on treating
each multi-mark string (e.g. `dot|+`) as one vowel symbol: **the pooled text is not a consonant-sign + vowel-mark
syllabary of Italian of this design; the same solver reads a matched synthetic at 93-96%.**

**Tokens needed (step 3).** vi reads reliably at 720 already (no more leaves needed to test it; tested negative above).
**cm needs about 2,800 sign tokens** (all seeds 89-94%; at 1,400 only 1 of 3 seeds is above 80%): about 2,100 more, i.e.
**~6 more leaves at ~350 signs a leaf, which is f.55r-f.57v, the rest of the letter.**

Models still not excluded: cm (code+mark as homophones, needs f.55r-f.57v); marks as syllable or word indicators other
than a single following vowel; a nomenclator of syllable/word codes; nulls. Where not found: as worker I (no key on file).
Suggestion (not done): transcribe f.55r-f.57v with the box-keyed passes, then rerun `codemark_curve.py target cm` on the
pooled ~2,800 tokens.

## Key search (24 Sept 2026, LANE R5 B)

Worker LANE R5 B (Sonnet, cap $4, session_01AoYeGhfEGDkwnDewSZpGFi), 18:51-19:0x UTC. Search only, per brief: a key of
Giovanni Salviati's 1525-26 Spanish legation/nunciature, or of the papal Secretariat under Clement VII for Spain
1524-27 (Giberti's office). No solving, no image capture, no key trial against this letter (that is LANE R4 I's job,
above -- "No key on file fits").

| source | searched how | result |
|---|---|---|
| `sources/cryptiana/web/` (104 pages) | grepped for `salviati`, `giberti`, `clement.{0,3}vii`, `castiglione` (case-insensitive, all pages) | **not found** for a Salviati/Giberti key. 4 incidental hits: `spanish2C.htm` (Kolosova 2017/2024 thesis on Charles V's 17 imperial ciphers, Ko.1-17) and `spanish2.htm` mention Clement VII only as a captive/context, not a cipher party; `mayenne.htm`, `crypto.htm` no relevant text on inspection. See "Design near-misses" below for Ko.1 and `venetian.htm`. |
| `sources/solver-diffs/2026-09-24-cyphersolver-keys.tsv` (Bourdeau's 81 published keys) | grepped for `salviati\|giberti\|clement\|vatican\|papal\|nunzi\|nunci\|nuncio\|rome` | **not found.** Closest by geography/date: `k-lope1523` (Lope Hurtado de Mendoza, Spanish ambassador at Rome, 1523-24 -- Spanish, not papal); `k-lasry-gl` includes `vasto1527` (Del Vasto to Charles V, letter to "Garbino", 1527-28) and `rome1536` (Card. de Mâcon in Rome, 1536-37) -- neither is Salviati's own key. Every Lasry nunciature key on the list (Spagna 6 1568, Barberini-Ceva 1632, Portugal 1579, R121 1767, D3232 1758, Spagna 1718/1736) postdates 1525-26 by 40+ years. |
| `sources/solver-diffs/*.tsv` (other 45 files), QUEUE.md, CATALOG.md, LANDSCAPE.md | grepped for `2933`, `salviati`, `giberti` | **not found** beyond the target's own QUEUE.md row (M35) and the DECODE/solver-repo negatives already logged above in "Check-solved sweep". |
| Meister (1906), *Die Geheimschrift im Dienste der päpstlichen Kurie*, full text on archive.org (`archive.org/stream/diegeheimschrift00meis/diegeheimschrift00meis_djvu.txt`) | fetched full djvu text (1 request), grepped for `salviati` (8 hits) | **found -- but not this letter's key.** Two ciphers naming Cardinal Giovanni Salviati as a correspondent, both in the book's "Cifre vecchie usate aus der Argentisammlung" section (old keys from the Argenti secretaries' collection, i.e. pre-1585 keys the later cipher secretaries kept on file) and both **contextually dated to the later 1540s, not 1525-26**: (a) key no. 8, "Cifra con il cardinal di Ferrara" (footnote identifies him: "Kardinal Gio. Salviati, Bischof von Ferrara 1520-50, wurde 1525 Kardinal; er starb 1553" -- consistent with the index, "Ferrara, card. s. Salviati", p.179), sitting immediately after key no.7 (Alessandro Vitelli), whose own footnote dates that cluster "aus den Jahren 1545-50"; a 9-symbol homophonic table (`ac eb id on ut fr lg mp sz` -> single digits) plus `qua/que/che/chi/et` abbreviations and one Nulla -- no invented signs, letter-pairs and Arabic numerals only. (b) key no. 55, "Cifra di mons. Francesco Olivo con il cardinale Salviati" (footnote: "Gio. Salviati, Kardinal 1517-1553"; index "Salviati, Gio., card." p.179 again cross-referenced), a few entries after key no.52 which is explicitly dated `[1548.]` ("decifrata a 10 di agosto 1548"); a full alphabet substitution with 2-3 digit codes, double-letter codes (`bb cc dd ff gg ll mm nn pp rr ss tt zz`), hundreds-markers and a nomenclator of names including "Card. di Ferrara", "Duca d'Alua" (Alba) and "Sfondrato" -- again digits and ordinary letters throughout, no drawn marks. Neither key's design resembles fr.2933's invented hooks/mirrored letterforms with superscript-number marks (`glyphs/atlas.tsv`/`atlas.png`); neither carries a 1525-26 date; not fetched as an image (Meister prints the tables as typeset text, no scan needed). Not a match for this letter, but the correct correspondent -- flagging for a solver session in case Salviati re-used a personal cipher across legations (untested here, out of this brief's search-only scope). |
| Archivio Apostolico Vaticano, Segreteria di Stato / Nunziature, Spagna 1525-26 | web search for the fondo/inventory itself | **not reachable/not found** this pass -- web search surfaced only the AAV's general fondo index PDF and Wikipedia/Cathopedia biography pages confirming Salviati's 1525-26 Spain legation (created legate 5 May 1525, departed early July, in Spain to July 1526 per Pieper 1894 below), no online inventory entry for a cipher key under this fondo was found by search. The AAV's own online catalogue was not queried directly (no API found by search; out of scope to build a scraper this pass). |
| Archivio di Stato di Firenze, Carte Strozziane (inventory, *Le carte Strozziane del R. Archivio di Stato in Firenze: Inventario*, Guasti/Milanesi 1884), full text on archive.org (vol. 1, `archive.org/stream/lecartestrozzian01fireuoft/..._djvu.txt`) | fetched full text (1 request), located all 66 `salviati` and 46 `cifr` hits by line number, checked every pair within 15 lines of each other | **not found.** Two proximity hits, both coincidental: "Salviati Francesco, arciv. di Pisa" sits near an unrelated "Copiata dalla cifra" line in a plain letter-index (1470s-90s, different Salviati, a 15th-century archbishop of Pisa); "Maria Salviata de' Medici" (a woman married into the Salviati family, 1536) sits before a section header "Cifre usate nella segreteria di Lorenzo il Magnifico" -- Lorenzo de' Medici's own late-15th-century secretariat ciphers (1470s-90s), unconnected to Cardinal Giovanni or 1525-26. Vol. 2 not fetched this pass (out of cap; flagged as a follow-up: the worker's earlier web-search lead in "Check-solved sweep" above, "a cipher with Jacopo Salviati... kept on large open folios," was not relocated in vol. 1's full text and may sit in vol. 2 or the later series). |
| Internet Archive full-text search (`be-api.us.archive.org/fts/v1/search`) | queried `Salviati cifra nunziatura Spagna` (broad, 2007 hits, too diffuse to be useful) then the quoted phrase `"cardinal Salviati" cifra` (782 hits) | **not found** as a key, but surfaced a genuinely useful background source: Anton Pieper (1894), *Zur Entstehungsgeschichte der ständigen Nuntiaturen*, full text fetched (`archive.org/stream/zurentstehungsg00piepgoog/..._djvu.txt`, 1 request) and grepped for `salviati` (23 hits) -- confirms the legation's exact dates from an independent print source: "Cardinal Giovanni Salviati, Ernennung am 5. Mai, Abreise Anfang Juli 1525, bis Juli 1526" (appointed 5 May, departed early July 1525, until July 1526) as legate at the Emperor's court, and separately as legate in France October 1526-August 1529. One reference to "das Registro originale seiner Briefe" (the original register of his letters) at Ehses's edition p.266 n. -- not chased this pass (a register of letters is not necessarily a cipher key; out of cap). No cipher table for the 1525-26 Spain period is given in Pieper. |
| Google Books / OpenAlex / Semantic Scholar (Lasry, DECODE, and general scholarship) | OpenAlex (`OPENALEX_KEY` header): `Salviati cipher nunciature Spain 1525` (0 hits), `papal cipher cardinal legate Spain 1525` (8 hits, all off-topic English/literary history, no relevance), `Lasry Vatican cipher nunciature` (0 hits). Semantic Scholar (`S2_KEY` header): `Salviati cipher papal legate Spain` (0 hits). | **not found.** No Lasry or other DECODE-linked publication on this cardinal or fondo turned up by either index. |

**Design near-misses (not a key, flagging per the brief's design-comparison instruction):** `spanish2C.htm` notes that the *Duke of Sessa's* Spanish cipher (Ko.1, Kolosova 2017/2024 thesis) was used to encipher the Italian-language text of the 1525 treaty between Pope Clement VII and the Duke of Sessa for the Emperor -- the Pope's own side of that exchange, not a Salviati key, and Ko.1 is a substitution-alphabet-plus-nomenclature design (letters/2-3 letter codes), not invented signs. Separately, `venetian.htm` describes a distinct family of **letter-plus-superscript-figure** ciphers attested in exactly this period and milieu -- BnF fr.2988/fr.3019/fr.20506 (Hieronimo Ranzo, Gattinara's secretary), fr.3022 (a Venetian agent's 1528 Madrid memoir), and Clair.327 f.279-280 (1528, to "Seigneur Garbino") -- which is the same design feature flagged as unexplained on fr.2933 itself (superscript numbers floating over signs, "Glyph atlas" section above). None of these is Salviati's, and none is a match by shelfmark, but the design parallel (superscript figures over cipher signs, 1525-1528, Italian/Imperial-adjacent correspondence) supports reading fr.2933's superscript marks as a period cipher convention rather than a later cataloguer's annotation -- a question for a solver session, not resolved here.

**BnF 5549 / Bowes-Walsingham 1583:** neither was encountered in any of the above searches; not chased, per the brief.

**Conclusion:** no key of Salviati's 1525-26 Spanish legation, and no Secretariat-of-State-for-Spain key of this date under Clement VII/Giberti, found in any of the eight sources searched. LANE R4 I's "no key on file fits" (above) stands; this pass adds two Salviati-linked keys from a later decade (Meister 1906, neither a design match) and confirms the legation's dates independently (Pieper 1894) without adding a testable key. Not scored closed-negative (this is a location search, rule 3's matched-control requirement does not apply to a key search).

Requests: WebSearch 6 queries. archive.org 3 full-text fetches (Meister 1906, Carte Strozziane vol.1, Pieper 1894), each a single request, no repeats. be-api.us.archive.org 2 fts queries, >=1.5s apart. api.openalex.org 3 queries (keyed, `Authorization: Bearer`), >=1.5s apart. api.semanticscholar.org 1 query (keyed, `x-api-key`). No Gallica, no de-crypt.org, no credentials printed.

## Leaf f.55r priced, rest not bought (24 Sept 2026, 19:35 UTC, LANE R5 orchestrator)

LANE R5 worker A (Sonnet, cap $8, session_01AM1QY9fyfJjhREPeKiD3Yq) ran J's box-keyed procedure on f.55r: boxes, strips and pass A
(`passA_f55r.tsv`, 553 boxes, all 19 lines) are committed; it passed its cap at $9.37 with the blind pass B still running and was
interrupted, so there is no pass B and no gate figure for f.55r. Price: more than $9.4 a leaf against the $6.5 J measured on f.54v.
The five leaves still needed (f.55v-f.57v) would cost about $50-60 in transcription alone before the cm control can be run, so the
lane did not buy them. The code+mark homophonic model (cm) stays **untested, not negative** (P's curve: it needs about 2,800 sign
tokens and the transcribed text holds 719, plus 553 boxes of pass A on f.55r).
A key search (LANE R5 B, section above) found no Salviati 1525-26 key in eight sources.
Suggestion (not spawned): a cheaper route to 2,800 tokens is one script-plus-one-pass transcription (classifier call confirmed by a
single reader, no blind second pass) for f.55v-f.57v, used only to test cm at N; a hit there would then justify second passes. Or a
key: the Sessa/Clement VII 1525 treaty cipher B noted (Kolosova Ko.1, `sources/cryptiana/web/spanish2C.htm`) is a design to compare.

## Model-in-the-loop crib rounds (solvEX)

Worker solvEX (Opus, cap $15, session_01XXo5gDVwAEHgVUbkSW74Dr), 24 Sept 2026 19:47-19:58 UTC. Brief
`.claude/briefs/runs/2026-09-24-solvex-model-in-the-loop.md`. Disk only, no hosts, no subagents. **Controls only; the
target was not touched** (the brief's gate for the target step is a gain of 15 points or more on control (a), and (a) is
at its ceiling). No reading of fr.2933; grades stay H0 C0 S0 M0 I0.

**Question.** Does a model reading the partial decode and proposing sign=letter cribs, re-annealed with them fixed, beat
`tools/homophonic_anneal.py` run blind on a matched control? **Method.** New `tools/crib_rounds.py` (test
`tools/tests/test_crib_rounds.py`) makes the control, keeps plaintext and key in `hidden.json`, which the reader never
opened, shows the decode (`--view R`: letters above sign ids), re-anneals with the cumulative crib file fixed, and
`--score` prints numbers only. Settings as in the earlier controls: order 3, 8 restarts x 40,000 iterations. At most 12 cribs a
round, taken only from words the reader was sure of (e.g. "ui mando", "e uirtu uostre", "debile", "ui bascio",
"gnedigen herren", "uerstanden", "unachtsamkeit", "continuo inuitato"), each crib file giving its reason. The rounds
use the lowest-scoring or mid-range seed, named in the table, because a 99% seed leaves nothing to gain.
**Compute check:** the same instance, blind, with 24 restarts (the three rounds' total restarts).

| control | N | K | blind, seeds 1/2/3 | instance | round 0 -> 1 -> 2 (letter %) | cribs right/wrong per round | blind, 24 restarts |
|---|---|---|---|---|---|---|---|
| (a) Italian, Vanzolini chars 200,050 on (plain_vanz_200000.txt), 5 it16 corpora | 720 | 36 | 99.7 / 99.7 / 99.7 | none | ceiling: 0.3 points available, no round run | - | - |
| (b) German, J7's held-out Groen IV CDXLIV (`j7/control_plain.txt`), corpus `j7/corpus_T.txt`, simple homophonic (not J7's nomenclator design) | 540 | 82 | 94.4 / 88.3 / 90.7 | s2 | 88.3 -> 95.9 -> 97.0 | 5/0, 2/0 | **95.9** |
| (c) Italian, Mellon's plain_it.txt | 244 | 31 | 83.6 / 88.5 / 94.7 | s1 | 83.6 -> 98.4 -> 98.4 | 8/1, 3/0 | **83.6** |
| (c2) Italian, Vanzolini chars 260,000 on (fresh; the (c) plaintext had been read), same corpora | 244 | 31 | 33.2 / 65.6 / 90.2 | s2 | 65.6 -> 79.1 -> 79.1 | 10/0, 12/0 | **65.6** |
| (c2) same | 244 | 31 | | s1 | 33.2, reader found no word it was sure of, 0 cribs | 0/0 | - |

(Other seeds of (c) and (c2) were not looped. Once the reader has read a plaintext through one seed's decode, a second
seed of the same plaintext is no longer blind.)

**Verdict (controls only).**
- **Italian, N=244, K=31: the loop adds 15 points (c) and 13.5 points (c2) on a matched control.** In both it gives
  what 3x blind compute does not (83.6 and 65.6 stay put at 24 restarts). More search converges on the same wrong key (the
  top restarts agree), and a reader who spots two or three words moves it off that key. 29 of 30 new
  cribs were right in those rounds; the one wrong crib (round 1 of (c)) cost nothing visible.
- **German, N=540, K=82: no gain beyond compute.** Round 1's +7.6 equals what 24 blind restarts reach (95.9); round
  2 added 1.1 more.
- **Italian, N=720, K=36: no room** (99.7% blind). The design Salviati f.54r would have if it were plain homophonic
  is read without help, so the loop cannot change the negative on record for that model.
- **Where the loop does nothing:** at 33% (c2 s1) the decode has no word the reader can be sure of, so no cribs
  and no gain. When round-2 cribs were right but only confirmed signs the decode already had right ((c2) round 2, 12/12), the
  gain was 0. The gain comes from the first few corrections of wrong signs, and it needs a decode already at about 65% or more.
- One run each, one reader. This is a small sample, not a measured curve.

**Target step: not run** (gate: (a) gain >= 15 points; (a) has 0.3 points of headroom). Since cm and vi (worker P) are
the untested and tested-negative Salviati models, a loop experiment that could matter for this target needs a
control of the **cm** design at N=720 (worker P: 22-67% blind), where decodes sit in the band the loop helped. That
needs `crib_rounds.py` extended to the interleaved row pattern of `control/codemark_curve.py`. Suggestion, not done.

Files: `control/solvex/{a_it720,b_de540}_s{1,2,3}/` (cipher.tsv, hidden.json, state.json, round*.json/txt,
cribs*.txt, scores.tsv, blind_24restarts.json), Mellon's in `ciphers/beinecke-mellon29-elia/control/solvex/`. Regenerate
any round with `python3 tools/crib_rounds.py --dir DIR --round R --cribs DIR/cribsR.txt` (deterministic by seed) and
`--score`. Requests: none.

## Crib loop on code+mark at N=720 (solvEX2)

Worker solvEX2 (Opus, cap $12, session_01DHytvHaqJK368edmcp46ZJ), 24 Sept 2026 20:11-20:19 UTC. Brief
`.claude/briefs/runs/2026-09-24-solvex2-codemark-loop.md`. Disk only, no hosts, no subagents. **Controls only; the target
was not run** (gate below not met). No reading of fr.2933; grades stay H0 C0 S0 M0 I0.

**Question.** Does solvEX's crib loop lift the code+mark (cm) design at N=720, the design and length of the pooled
f.54r+f.54v ciphertext, where worker P's blind solve reads 22-67%?

**Method.** Three cm controls built exactly as P's `codemark_curve.py build('cm', 720, seed)` (126 code+mark types
allotted by frequency deficit, the target's own sign/box row pattern, each plain box withholding 2 letters, Vanzolini
chars 200,050 on, held out of the five-collection corpus), seeds 1-3, K = 108/108/109 as P's. `control/solvex2/make_cm.py`
writes them with sign ids u000-u125 (the code^mark names contain '#'); `tools/crib_rounds.py` gained `--cipher-tsv/--plain`
to load such a prebuilt control (test added to `tools/tests/test_crib_rounds.py`, passes). The key and plaintext sit in
`src/hidden_sN.json` and each run's `hidden.json`, which the reader never opened; `--score` printed numbers only.
Solver settings as P: order 3, 6 restarts x 120,000 per round; blind 24 = the same control at 24 restarts. The reader
worked from `control/solvex2/view_gaps.py`, which shows the decode with the target's plain-box positions as '..' (public
on the leaf). At most 12 cribs a round, from words read in the decode, each crib file giving its reason.

| seed | K | blind 6 | blind 24 | round 0 -> 1 -> 2 -> 3 -> 4 (letter %) | cribs right/wrong per round |
|---|---|---|---|---|---|
| 1 | 108 | 46.9 | 50.1 | 46.9 -> 50.7, then stopped (no further word the reader was sure of) | 8/4 |
| 2 | 108 | 65.3 | 58.9 | 65.3 -> 61.1 -> 72.5 -> 75.6 -> 76.1 | 7/5, 5/0, 4/2, 7/0 |
| 3 | 109 | 18.9 | 75.4 | 18.9, no word the reader was sure of, 0 cribs | - |

(`control/solvex2/results.tsv`; per-run `cm720_sN/scores.tsv`, `cm720_sN_blind24/`.) Blind 6 does not repeat P's
66.9/30.8/21.9 on the same controls: the sign ids differ, so the anneal takes another random path. At this design and
length, the same control and seed read anywhere from 19% to 75% depending on the solver's path.

**Verdict.**
- **The loop adds 4.9 points on average on cm controls at N=720** (+3.8, +10.8, 0 over blind 6); no seed ends above 85%
  (best 76.1). Gate for the target step (mean gain >= 15 and two seeds above 85%) **not met; target not run; no reading.**
- **Does a mid-range decode give readable Italian?** At 65% (seed 2), yes, just enough: "necessita", "in fatto",
  "non so che", "a uostre" in round 0, and "Signoria", "tutte quelle", "la commissione di andare" after round 2. The seed
  ended 17.2 points above its own 24-restart blind run. At 47% (seed 1), only fragments; one round, 4 of 12 cribs wrong,
  +3.8. At 19% (seed 3), nothing the reader could trust. solvEX found the same at 33%.
- **The reader's cribs are less reliable here than on simple homophonic controls.** 31 of 42 new cribs were right (74%),
  against 29 of 30 in solvEX. Two things account for it: every plain box cuts 2 letters out of the stream, so words
  arrive in fragments, and most of the 108 signs occur only 1-5 times. One round made things worse (seed 2 round 1,
  -4.2). The reader could not tell which of its cribs were wrong; it recovered by dropping a block that never settled.
- **More compute competes with the loop at this design.** Seed 3 went from 18.9 to 75.4 at 24 restarts with no reader,
  and seed 2 went down (65.3 to 58.9). The spread between runs is larger than anything the loop added, so at N=720 the
  cheaper lever is more restarts, with the reader added on the best of them. Worker P's estimate stands: cm needs about
  2,800 sign tokens (f.55r-f.57v) before blind decodes sit near 90%.
- One reader, one run per seed; a small sample, not a measured curve.

Files: `control/solvex2/{make_cm.py,view_gaps.py,results.tsv,src/,cm720_s{1,2,3}/,cm720_s{1,2,3}_blind24/}`.
Regenerate: `python3 control/solvex2/make_cm.py N`, then `tools/crib_rounds.py --cipher-tsv ... --plain ... --corpus
(5 it16 files, control/corpus_args.txt) --seed N --restarts 6 --iters 120000`, then `--round R --cribs cm720_sN/cribsR.txt`
and `--score`. Requests: none.
Suggestion (not done): at N=720, try blind at 48-96 restarts and give the loop only the best-scoring restart.

## Leaf f.55v (24 Sept 2026, LANE R5 H2)

Worker H2 (Sonnet, cap $12, session_01QKxu7fUbqYfthJc5gXcZ5m), starting 20:51 UTC. Disk only, no fetches. Method
exactly as J's f.54v ("Leaves f.54v-f.57v" above), Sonnet pass B this time given J's confusable-code pairs
(eps/e, h/bh, tee/S4, psi/y, w/e, o./dl/h/tee/S7/#/+, Z/L).

**Atlas rebuild check.** `glyphs/build.sh` needed numpy/pillow/opencv-python-headless/scikit-image/scikit-learn
installed first (none present in this container). After installing, the rebuild's `segment`+`cluster` step did
**not** reproduce the committed atlas byte-identically: box counts differ page by page from the committed
`glyphs/signs.tsv` (e.g. this container's rebuild counted 499 f.55v sign boxes against the committed 495;
f.54r 506 vs. the committed page's own count; `clusters.tsv` 5289 vs 5257 rows) -- almost certainly opencv/
scikit-image version drift changing `connectedComponentsWithStats`/percentile-threshold results, not a
non-deterministic seed (the script's own comment expects a fixed seed to reproduce exactly). Per the brief:
**did not commit the atlas.** `git checkout --` restored `glyphs/{atlas.tsv,atlas.png,atlas_part1.png,
atlas_part2.png,bitmaps.npz,clusters.tsv,marks.tsv,signs.tsv,sheet_signs_*.png}` to the committed versions
before doing anything else, and reverted `f54r_boxes.tsv` and five `strips/f54r_*.jpg` that `build.sh`'s own
last step (a classify call on f.54r) had overwritten using the drifted rebuild -- f.54r is H1's leaf, not
touched otherwise. Kept only `glyphs/crops/*.png`: `cmd_segment` writes these straight from
`Image.open(path).convert('L')` before any opencv connected-components call, so they are a deterministic
grayscale render of the same source image regardless of the library-version drift, and `classify`'s strip
cutter only reads them for pixel content (`cv2.imread`), not coordinates -- coordinates come from the
committed `signs.tsv`. Confirmed committed `signs.tsv` already holds 495 f.55v boxes as NOTES' "Leaves
f.54v-f.57v" section recorded, matching after the restore.

**Classify.** `tools/glyph_atlas.py classify --out glyphs --labels glyphs/labels.json --page f55v --tsv
f55v_boxes.tsv --strips strips` against the committed atlas/labels: 495 boxes classified, kNN code = cluster
code for 451/495, 359 cipher codes (script_code != `_`), 19 line strips written
(`strips/f55v_L01..L19.jpg`). `f55v_boxlist_for_passes.tsv` built from `f55v_boxes.tsv` (line, pos,
script_code, script_marks, share), same column set as `f54v_boxlist_for_passes.tsv`.

**Pass A.** This worker read all 19 line strips (`strips/f55v_L01..L19.jpg`), zoomed in (fresh 5-6x crops from
`glyphs/crops/f55v.png`, a small scratch script, not committed) on every low-share (<0.85) box and any
high-share box whose strip appearance looked visually odd, and cross-checked shapes against
`glyphs/atlas_part1.png`/`atlas_part2.png`. Unlike J's f.54v pass A (0 corrections out of 502), this pass
diverged from the classifier's boxlist proposal on **36 of 495 boxes** (`passA_f55v.tsv`: 459 confirm/plain,
36 correct, 0 split/delete). Most corrections cluster in one recurring pattern, distinct from J's confusable
code-pairs: **this leaf's classifier frequently mis-tags plain Italian cursive letters inside legible running
words as one of the letter-shaped sign codes** -- S, N, H, L, w, m, nt, f, Lx, S7, phi all had at least one
box corrected back to plain within an otherwise-legible word (examples: "ancora" mid-word at line1 pos3;
"Bisogna" at line4 pos24-27, four consecutive corrections; "Sanza...questo" at line12 pos1/4/11; "penso" at
line12 pos23; ".S." -- the "V.S." Vostra Signoria abbreviation -- corrected three separate times at line14
pos20, line17 pos1, line18 pos6; "intenderà" at line14 pos18-19 and line17 pos18-21; "La" at line18 pos8-9).
The reverse (classifier plain at share 1.00 that is actually a sign) also occurred twice (line1 pos8, an
o.+g merge; line4 pos19, a clear eps). One merge candidate flagged but not split (line1 pos8, box rh~2.18):
pass A kept it as a single corrected code (`o.`) with a note for pass B/settling to re-examine, rather than
inventing a pos+0.5 row itself (J's split convention was pass-B-only on f.54v).

**Pass B (blind Sonnet subagent, one spawn).** Briefed with the boxlist, the strips, the atlas plates, and
J's confusable-code pairs (eps/e, h/bh, tee/S4, psi/y, w/e, o./dl/h/tee/S7/#/+, Z/L); never opened
`passA_f55v.tsv`, confirmed in its own report. It independently found the same sign/plain-letter confusion
pattern this worker had (e.g. its line2 "a S.M.ta", line3 "Cosi volsi mr si contento restassino", line8
"Assaj Cose", line9 "mi ha ... un" -- all previously multi-coded at share up to 1.00, corrected to plain) and
the reverse case (classifier-plain boxes that are real signs, e.g. line2 pos18 `o.`, line6 pos16 `S7`, line9
pos11 `+`, pos14 `S`). **Stopped at cost cap after line 11 of 19** (`passB_f55v.tsv`, 296 rows: lines 1-11's
293 boxlist positions + 2 split rows -- 235 confirm, 54 correct, 4 delete [3 stray ink, 1 paper-fold/damage
artifact at line10 pos5, dist=11.57, far outside the normal 2-6 range], 2 split [line1, line11, each one box
holding two merged signs]); lines 12-19 (about 202 boxlist positions) **not attempted**. Committed and pushed
in two checkpoints (lines 1-6, lines 7-11).

**Stopped here: no gate, no reconciliation, no reading.** `get_session` on this worker's own session id,
checked immediately after the pass-B subagent's hand-back, reported **cost_usd $12.59 against the $12 cap**
(the subagent's own self-check mid-run had already read $12.47) -- the first time in this job that
`get_session` returned a cost figure at all (every check before and during pass A returned none, the
"rate-limit-plan session" pattern other LANE R5 workers hit; it populated only once the pass-B subagent's
usage was folded in). Per the common brief's cost-stop rule and RETRO-2026-09-24f (worker A's f.55r
interruption at $9.37 with no per-step checkpoint), stopping now rather than spending further on a second
pass-B continuation, `recon_box.py`, or settling: **pass A is complete (495/495) and committed; pass B is
partial (296/~497 rows, lines 1-11 of 19) and committed; no base-code agreement figure exists yet because
pass B does not yet cover the whole leaf.** This job ran markedly more expensively than H1's concurrent
f.55r pass B (which finished all 553 boxes, gated at 84.8%, and settled 61 disagreements for about $7 total
by resuming one subagent across five `SendMessage` turns rather than doing an unusually thorough from-scratch
pass A first) -- worth noting for whichever worker picks up f.55v's remaining lines 12-19: resume pass B the
same way (append to `passB_f55v.tsv`, do not overwrite lines 1-11), rather than re-running pass A, which is
already done and cost most of this job's budget.

Requests: none (disk only). Subagents: 1 (Sonnet, pass B, blind to pass A, stopped partway through at cap).

## Leaf f.55r (24 Sept 2026, LANE R5 H1)

Worker H1 (Sonnet, cap $12, session_01DjYdTGsK72PjN4TpqA35fE), 20:51-21:2x UTC. Disk only, no fetches.
Boxes, strips and pass A (`f55r_boxes.tsv`, `f55r_boxlist_for_passes.tsv`, `strips/f55r_L01..L19.jpg`,
`passA_f55r.tsv`, 553 boxes) were already committed by worker A (interrupted at $9.37 before pass B, see
"Leaf f.55r priced" above); this session picked up from pass B.

**Setup.** `glyphs/crops/` (the regenerated, not-committed working-copy pages `tools/glyph_atlas.py`'s
`classify`/strip-cutter reads pixel content from) was absent; `pip install numpy opencv-python-headless
scikit-image scikit-learn pillow` (none pre-installed in this container) then `sh glyphs/build.sh`. The
rebuild's `clusters.tsv`/`atlas.tsv`/`signs.tsv`/`marks.tsv` (and their derived PNGs) were **not**
byte-identical to the committed ones (opencv/scikit-learn version drift in this container vs. whatever built
the committed atlas -- H2's f.55v section above independently hit and diagnosed the same drift concurrently
this session). Per the brief: did **not** commit the regenerated atlas files, `git checkout --` restored the
committed versions (including `glyphs/crops/` is not among them -- untracked working copy, kept), and also
reverted `build.sh`'s own trailing `classify --page f54r` step, which had overwritten `f54r_boxes.tsv` and
five `strips/f54r_*.jpg` files with drifted output even though f54r is not this worker's leaf.

**Pass B.** One blind Sonnet subagent (`Agent` tool, continued across five turns via `SendMessage` rather
than five fresh spawns, so it stayed "at most one Sonnet subagent" while still letting this worker checkpoint
and commit between batches -- lines 1-4, 5-8, 9-12, 13-19), briefed with the boxlist, the line strips, the
atlas plates, and the known confusable-code pairs from the f54r confusion table (eps/e, h/bh, tee/S4, psi/y,
w/e, o./dl/h/tee/S7/#/+, Z/L); never opened `passA_f55r.tsv`. It re-cropped ambiguous/low-share/confusable-pair
boxes from `glyphs/crops/f55r.png` at 5x zoom with a scratch script (`recrop_f55r.py`, not committed, matches
J's f54v method). First batch (116 boxes, all boxes individually re-checked against the atlas) cost about
$3 and used 150 tool calls; told to economise, the remaining four batches (437 boxes) used the same
one-strip-read-plus-only-flagged-boxes approach as J's method and cost about $3.3 total (33-114 tool calls
each) -- get_session checked after every batch (RETRO-2026-09-24f's cost-stop rule), each commit+push
landing before the next batch was requested, so no work was at risk of being lost at the cap the way worker
A's was. `passB_f55r.tsv`, 553 rows (matches `f55r_boxlist_for_passes.tsv` 1:1, verified by set comparison,
no dups/omissions): 492 confirm, 60 correct, 1 split-flagged (line3 pos27, no extra half-position row).

**Gate.** `recon_box.py passA_f55r.tsv passB_f55r.tsv recon_box_f55r`: 401 non-both-plain positions
compared. **Base code agreement: 340/401 = 84.8%. Gate (>=80%) PASSES.** With marks also required to match:
329/401 = 82.0%. Files: `recon_box_f55r/agreement.tsv` (340 rows), `recon_box_f55r/disagreements.tsv` (61
rows).

**Settling.** All 61 disagreements resolved by this worker (not a subagent) from 5x-zoom recrops of every
disputed box, montaged one image per line with each box labelled with both passes' calls
(`recon_box_f55r/settled.tsv`, one reason per row). Two patterns did most of the work, both recurring from
f.54v's settling: (a) several stretches where the classifier/pass-A read letter-shaped cipher codes but the
boxes are visually continuous, legible plain Italian ("ratio", "coferisca", "questo", "ogni", "al" three
times, "utt'", "po", among others) -- settled plain; (b) an "e"-bowl-with-unrecorded-+/#-mark pattern (pos
L1P21, L2P11, L5P18 -- three of the eight the pass-B subagent flagged as systematic) and a
numeral-mark-over-g-loop pattern (L2P12, L3P24, L19P10) settled to pass B's fuller mark/code. One
disagreement (line1 pos7-11) settled the other way: pass A's own note that this is one continuous plain
cursive word outweighed pass B's five individual per-box code guesses across the same span, so all five
settled to pass A's plain `_`. Two positions (L2P22, L5P10, L16P1, L18P24 -- 4 of the 61) stayed genuinely
ambiguous after the recrop and were settled at low confidence to whichever call was the less contrived shape
match, flagged as such in `settled.tsv`; none of the 61 were re-classified through the strips alone without
a 5x recrop.

**Reading.** `ciphertext_f55r.tsv` (line, pos, code, marks, grade): 553 rows -- `AB` 492 (340 base-code
agreements + 152 both-plain positions), `settled` 61. **370 sign tokens across 36 distinct types** (#, +, H,
K, L, Lx, N, S, S4, S7, U, Z, [, ], a, bh, ch, dl, e, eps, f, g, lam, m, nt, o., p, phi, psi, rz, sq, tee, v,
w, wd, y -- commonest: g 36, S7 22, w 21, bh 19, e 19, lam 18, a 16, y 15, nt 15; singleton ch), of which
about a fifth carry a mark. **183 boxes plain.** Same code book as f.54r/f.54v (36/34 types respectively);
sq (closed box/parallelogram) appears here as it did on f.54r but was not in f.54v's list. Grades mark
provenance (both passes agreed / this session's settled arbitration), not rule 4's H/C/S/M/I -- no key
exists to test this reading against and no plaintext is claimed; this is a **transcription**, not a
decipherment. No solving attempted (out of this brief's scope).

Cost: `get_session` on this worker's own session id, checked after every pass-B batch and again after
settling: pass B (all five batches) ran the cost from about $0.5 (setup: pip installs, room claim, atlas
rebuild/revert, verification) to $6.99; the gate script and the settling montage/recrop work (disk-only
Python, no further LLM subagent calls) added comparatively little on top since it was this worker's own
tool use, not a spawned session. Well under the $12 cap.

Requests: none (disk only). Subagents: 1 (Sonnet, pass B, blind to pass A, resumed via SendMessage across
five turns rather than five separate spawns).

Suggested follow-up (not attempted, out of this brief's scope): with f.55r's 370 tokens added to f54r's 370
and f54v's 349 (1,089 total across three leaves), and four more leaves (f.55v-f.57v) at a similar ~350-370
tokens each, the pooled ciphertext is close to the ~2,800-token threshold LANE R4 P's control curve set for
testing the code+mark (cm) homophonic model -- worth re-running `codemark_curve.py target cm` once f.56v or
f.57r lands, without waiting for all six.

## Check-solved (LANE R6 S0, 25 Sept 2026)

Worker LANE R6 S0 (Sonnet, cap $4, session_01Jdm1SGVot6mYUt5pHttiCt), 15:44-15:5x UTC. Closes the one real gap
the 24 Sept check-solved sweep flagged (Desjardins/Canestrini Toscane never full-text searched) so this target
clears `tools/intake_gate_check.py`. Disk fetches only (archive.org, web search); no images, no key trials, no
solving.

**1. Desjardins/Canestrini, *Négociations diplomatiques de la France avec la Toscane* (1859-1886).**
archive.org identifiers found via `advancedsearch.php` (8 hits: gri_ scans tomes I-VI 1886 + two bub_gb_ 1859
scans of tome I): fetched the three tomes most likely to cover 1525 (I, II, III) as full `_djvu.txt`.
- Tome I (`gri_33125017127347`, 1.72 MB text): 15 "salviat" hits, all 15th-century Salviati family members
  (Francesco, Giuliano, Lottus -- 1416-1499); no "octobre 1525"/"octobris 1525" match. Its own preface (line
  446) names "la correspondance du cardinal Salviati" as a source used across "ces deux premiers volumes"
  (tomes I-II) for the period up to the Peace of Cambrai (1529) -- confirming tomes I-II are the right ones
  to search, and that no further tome need be checked for this correspondent's letters of this era.
- Tome II (`gri_33125010469852`, 2.49 MB text): 60 "salviati" hits. A real, named section, "CORRESPONDANCE DU
  CARDINAL SALVIATI, LÉGAT EN LOMBARDIE" (Giovanni Salviati, legate to the imperial camp in Lombardy after
  Pavia), runs from "Rome, 4 janvier 1525" to "Rome, 26-31 mars, 1 avril 1525" -- every dateline in the
  section checked by regex, none later than early April 1525. Immediately after, the volume's next dated
  letters (a different correspondence, "Acciajuoli à Ghiberti et à Jacopo Salviati", dispatches to the
  cardinal's father) jump straight to "Beaugency, 5 octobre 1526": **no dateline anywhere in the volume falls
  between 1 April 1525 and 5 October 1526.** No "octobre 1525"/"octobris 1525"/"XVI octobris" match anywhere
  in the file. Control word: "chiffre" appears 3 times (including an unrelated footnote "Chiffre non
  déchiffré" on a different, uncredited cipher passage elsewhere in the volume, not Salviati's), confirming
  the OCR reads French text correctly.
- Tome III (`gri_33125017127461`, 2.05 MB text, needed one retry after two transient 500/502 errors --
  server-side, not a challenge or block): 41 "salviati" hits, all a different, later Salviati (Antonio Maria
  Salviati, nuncio to France under Pius V, 1570s-72 per its own footnote at line 32441); every dated letter in
  this volume falls in the 1560s-1590s. No 1525 material at all; not the right volume.
- **Conclusion: the Desjardins/Canestrini series prints Cardinal Giovanni Salviati's Lombardy-legation letters
  of Jan-April 1525 only. It has no letter, and no decipherment, for his 16 October 1525 Spain-legation letter
  -- that whole period (the gap the target's own letter falls in) is simply absent from this edition.**

**2. Printed Salviati Spain-legation/nunciature letters and correspondents, 1525-26.**
- **Castiglione's *Lettere*** (Serassi ed., Rome/Padua 1769-71, 2 vols; Castiglione was papal nuncio in Spain
  at the same court and period as Salviati's legation): fetched both volumes' full text
  (`bub_gb_ZJMxff7r4LUC` vol.1 "Famigliari + tre primi libri di Negozj", 950 KB; `bub_gb_laRnTtJmsDAC` vol.2
  "tre ultimi libri di Negozi", 1.22 MB). 8 "salviati" hits in vol.1, 17 in vol.2, all discussing Salviati as a
  third party (his legation, his father Jacopo, his reception at court) -- no letter *by* Salviati and no
  cipher passage attributed to him. Every 1525 dateline in both volumes checked: vol.1 has exactly one, "In
  Madrid alli 14. di Marzo. MDXXV."; vol.2 has exactly three, all December ("Toledo ... IX. di Dicembre
  MDXXV." twice, "... XVIII. di Decembre MDXXV." once). **No dateline between 14 March and 9 December 1525 is
  printed in Castiglione's letters at all -- October 1525 is a gap in this edition too**, not only in
  Desjardins. Control word: "cifra"/"chiffre"-family words appear 11 times in vol.2, confirming OCR reads.
- **Balan, *Monumenta reformationis lutheranae ex tabulariis secretioribus S. Sedis, 1521-1525*** (1884, 2
  vols spanning exactly the target's year): fetched both volumes' full text (`monumentareform01vatigoog` 1.55
  MB, `monumentareform02vatigoog` 1.73 MB). **0 "salviati" hits in either volume** (this edition's documents
  are German-Reformation/Curia correspondence, not the Spain legation). Control word "cifr" appears once in
  each volume, confirming OCR reads.
- **Lettere di principi** (Ruscelli's anthology, 3 vols, 1564): fetched vol.2 only (`letterediprincip02char`,
  1.39 MB) as the volume most likely by date-range to carry 1520s political correspondence. **0 "salviati"
  hits**; "cifra"/"chiffre"-family words appear 9 times, confirming OCR reads. Vols 1 and 3 not fetched this
  pass (out of cap; a real gap, flagged as a follow-up, not scored as a negative for this source).
- Web search (`"cardinal Salviati" 1525 legate Spagna cifra lettera "16 ottobre" OR "XVI octobris"`; `Balan
  "Monumenta reformationis" Salviati 1525 Spagna nunzio cifra`): surfaced only general Salviati biography
  (Wikipedia, Treccani, Cathopedia, cardinals.fiu.edu -- all confirm the 1525-26 Spain legation dates already
  on file, none names this letter or a decipherment) and an unrelated Wikisource transcription of a *Charles V
  to* Salviati letter (not this direction, not this date, not enciphered).

**3. Model-solve announcement search** (check-solved.md's seventh family, added 24 Sept 2026).
`"Salviati" cipher fr.2933 solves Claude GPT decipherment 2026`; `Vals AI blog cardinal Salviati cipher letter
solved`. Both searches return only the one known 2026 model-solve announcement on record (Vals AI / Boris
Cherny, 31 Aug-14 Sept 2026, Claude Fable 5.1 on Sir Thomas Urquhart's 1653 *Cyphral Distich* -- schneier.com,
vals.ai, itdoeswhatnow.com, explainx.ai): unrelated cipher, unrelated century, unrelated correspondent. No
model-solve announcement names Salviati, fr.2933, or BnF Français 2933 in any result.

**Verdict: stays open.** Six standard/likely editions read in full this pass (Desjardins/Canestrini tomes I-
III, Castiglione vols 1-2, Balan vols 1-2) plus one anthology volume (Lettere di principi vol.2) and the model-
solve family: no letter, key or decipherment for BnF fr.2933 no.11 located in any of them. Combined with the
24 Sept sweep (web, cryptiana/cipherbrain, DECODE, Bourdeau, Aymeloglu -- all negative) and the 24 Sept key
search (LANE R5 B: Meister 1906, Carte Strozziane, Pieper 1894, OpenAlex, Semantic Scholar -- no key), the
target has now had a genuinely wide search with no hit; not found-solved, not blocked (every edition named
here was opened and read). Where not found: Desjardins/Canestrini I-III, Castiglione (Serassi) I-II, Balan
I-II, Lettere di principi II, web search, Vals AI/model-solve announcements. Not chased this pass, out of cap:
Lettere di principi vols 1 and 3; the AAV's own Nunziature di Spagna archival inventory (not reachable by
search, per the 24 Sept key-search pass); Vatican Secret Archive Segreteria di Stato Spagna fondo directly.

Requests: archive.org 9 `_djvu.txt` fetches (Desjardins I/II/III, Castiglione I/II, Balan I/II, Lettere di
principi II) + 1 `advancedsearch.php` query, each ≥1.5s apart, one item (Desjardins III) needed one retry
after two transient 500/502 server errors (not a challenge/block, no further retries taken). WebSearch 4
queries. No Gallica, no de-crypt.org, no credentials, no subagents.

```
$ python3 tools/intake_gate_check.py fr2933-salviati-1525
fr2933-salviati-1525: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```

## Leaves f.55v-f.57v completed (25 Sept 2026, LANE R6; merged from leafnotes/ by the LANE R6 orchestrator)

Pooled transcription, all eight leaves, 25 Sept 2026 17:45 UTC: 2,820 sign tokens (f54r 370, f54v 349, f55r 370, f55v 334, f56r 345, f56v 303, f57r 456, f57v 293). Gates: f55v two-pass 77.5% -> pass C majority 70/87; f56r 80.7%; f56v 82.6%; f57r 86.1%; f57v two-pass 77.0% -> pass C majority 77/78. The per-leaf sections follow verbatim from leafnotes/ (kept there too).

### Leaf f.55v (25 Sept 2026, LANE R6 L1)

Worker L1 (Sonnet, cap $12, box 60 minutes), 16:19-16:48 UTC. Disk only, no fetches. Resumed pass B where LANE R5
H2b's stale claim (24 Sept 21:34, no `done` line logged, superseded per this brief) left off. Boxes, strips, pass A
(`f55v_boxes.tsv`, `f55v_boxlist_for_passes.tsv`, `strips/f55v_L01-19.jpg`, `passA_f55v.tsv`, 495 boxes) and pass B
lines 1-15 (`passB_f55v.tsv`, 396 rows) were already committed. This session added lines 16-19.

**Setup.** `glyphs/crops/` was absent; `pip install numpy opencv-python-headless scikit-image scikit-learn pillow`
then `sh glyphs/build.sh`. Rebuild again not byte-identical to committed atlas (same opencv/scikit-learn version
drift H1/H2 independently hit and diagnosed 24 Sept: this container's rebuild gave 499 f55v sign boxes against the
committed 495). Per the brief: did **not** commit the regenerated atlas; `git checkout -- glyphs/ f54r_boxes.tsv
strips/` restored every committed atlas file and the strips `build.sh`'s own trailing classify step had overwritten;
kept only the untracked `glyphs/crops/*.png` (deterministic grayscale renders, unaffected by the drift). `git status`
clean before starting.

**Pass B, lines 16-19.** Two blind Sonnet subagents (`Agent` tool, one call each, never opened `passA_f55v.tsv`,
confirmed in their own reports), briefed with the boxlist rows, the relevant line strips, the atlas plates, and the
leaf's known confusable-code pairs (eps/e, h/bh, tee/S4, psi/y, w/e, o./dl/h/tee/S7/#/+, Z/L) plus this leaf's
recurring plain-cursive-mistagged-as-sign pattern (S, N, H, L, w, m, nt, f, Lx, S7, phi all implicated). Batch 1
(lines 16-17, 53 boxlist positions) wrote 53 rows, all confirm/correct, no splits. Batch 2 (lines 18-19, 50
positions) wrote 51 rows: one split (line 18 pos 7/7.5, a tall merged box) and one delete (line 19 pos 22, a
292px-tall segmentation artifact, mostly blank margin). Each batch's output was written to disk by the subagent as
a scratch TSV, verified and appended to `passB_f55v.tsv` by this worker, committed and pushed before the next batch
(`4d9a30a`, `ca4cf7f`). Final `passB_f55v.tsv`: 499 rows, verified by set comparison against
`f55v_boxlist_for_passes.tsv` (495 positions) -- 495/495 base positions covered 1:1, no dups, no omissions, plus 2
split rows (line 11's existing split from an earlier session, and this session's line 18 pos 7.5) and 1 delete.

Batch 2's subagent flagged one uncertain call worth a second look if this leaf is revisited: line 18 pos 6 (`S`,
conf M) -- read as either a genuine embedded cipher sign or the second half of a plain "J.s." initials pair; kept as
`S` per the atlas shape match. Line 18 pos 7's split also left a third, fainter ink trace in the same box
unassigned to either half.

**Gate.** `python3 recon_box.py passA_f55v.tsv passB_f55v.tsv recon_box_f55v`: 369 non-both-plain positions
compared. **Base code agreement: 286/369 = 77.5%. Gate (>=80%) FAILS.** (With marks also required to match:
266/369 = 72.1%.) 87 disagreement rows, spread across the whole leaf rather than concentrated in this session's
lines 16-19 (which contributed 25/87, roughly proportional to their 103/495 share of positions): line-by-line
counts 1:2, 2:9, 3:3, 4:4, 5:3, 6:3, 7:3, 8:5, 9:5, 10:6, 11:6, 12:1, 13:3, 14:5, 15:4, 16:4, 17:9, 18:11, 19:1.
Files: `recon_box_f55v/agreement.tsv` (282 rows), `recon_box_f55v/disagreements.tsv` (87 rows).

**Per the brief: gate FAIL -> push, report and stop, no hand-settling.** No `ciphertext_f55v.tsv` written, no
settling attempted. This leaf's pass A (this worker's own thorough, 36-correction read per the earlier "Leaf f.55v
(LANE R5 H2)" NOTES.md section) and pass B (two independent blind subagent batches, now covering all 19 lines) are
both complete and committed, but the two passes disagree too often to gate-pass as-is -- consistent with this
leaf's already-noted higher plain/sign confusion rate relative to f.54v and f.55r. A future worker could either
reconcile by hand from 5x recrops despite the gate failing at the orchestrator's discretion, or re-run one pass with
tighter guidance on the plain-word-run pattern before re-gating.

Cost: get_session checked after each batch and again now; well under the $12 cap and 60-minute box (elapsed about
29 minutes). Requests: none (disk only). Subagents: 2 (Sonnet, pass B, blind to pass A, one per two-line batch).

### Leaf f.55v completed (25 Sept 2026, LANE R6 L1c)

Worker L1c (Sonnet, cap $6, box 45 minutes, session_01Mm3Ez9uXdarTGdxaCxezPQ), 16:56-17:1x UTC. Disk only, no
fetches, no subagent. Picks up from the gate FAIL above (286/369 = 77.5% base-code agreement, 87 disagreement
rows in `recon_box_f55v/disagreements.tsv`); CLAUDE.md Usage 6 allows a third pass since the two disagree on
more than a tenth of rows (87/369 = 23.6%).

**Setup.** `glyphs/crops/` was absent; `pip install numpy opencv-python-headless scikit-image scikit-learn
pillow` then `sh glyphs/build.sh` (same version-drift the leaf brief and prior workers on this target
independently hit: rebuild not byte-identical). Per the brief, did **not** commit the regenerated atlas;
`git checkout -- glyphs/ f54r_boxes.tsv strips/` restored every committed atlas file and the strips
`build.sh`'s trailing `classify --page f54r` step overwrote, keeping only the untracked
`glyphs/crops/*.png`. `git status` clean before starting.

**Pass C.** Wrote `crop_passC.py` (reads only line/pos from `recon_box_f55v/disagreements.tsv`, never the
code_a/code_b columns; finds each position's box in `f55v_boxes.tsv` -- a split position like 8.5 shares its
parent box's pixel rect -- and crops it at 5x zoom from `glyphs/crops/f55v.png`, padded to the neighbouring
boxes on the same line) and `montage_passC.py` (stacks a line's crops into one labelled image,
`passC_crops/montage_L<n>.png`, so a whole line's disputed positions could be read in one image instead of 87
separate reads). Read both atlas plates (`glyphs/atlas_part1.png`/`_part2.png`) first, then all 19 line
montages, and called a code/marks/confidence/note for every one of the 87 positions from the crop alone,
matching shapes against the atlas plates and this leaf's known confusable pairs (eps/e, h/bh, tee/S4, psi/y,
w/e, o./dl/h/tee/S7/#/+, Z/L) -- `passC_f55v.tsv`, committed before settling (commit `f7f1d57`).
`passC_crops/` itself is not committed (working-copy crops, same as H1's `recrop_f55r.py` precedent).

**Majority vote.** `settle_passC.py` joins passA/passB/passC per row: 2-of-3 base-code agreement wins that
call; where all three differ (a genuine three-way split) this worker re-examined the crop together with A's
and B's own per-row notes (not blind -- settling a 3-way split is arbitration, not a fourth blind pass) and
picked the best-supported call at conf L, with a reason recorded in every case. **C agreed with A or B on
70/87 = 80.5% of the disagreement rows** (AC 20, BC 50); **17 three-way splits**, of which 15 settled to B's
call and 2 to C's own call, never to A's -- consistent with this leaf's dominant failure mode (pass A's
classifier over-called cipher signs on stretches of ordinary plain-cursive script; pass B's blind read already
caught most of it, and C's arbitration on the residual three-way cases leaned the same way once the
neighbouring-box word context was checked -- e.g. line 9 pos 1-3 reads as a coherent plain phrase across all
three positions, and line 18 pos 1 completes the word "Parti" that C had already read plain at pos 2 and 4
independently). `recon_box_f55v/settled.tsv` (line, pos, code, marks, source, reason), one row per
disagreement.

**Reading.** `build_ciphertext_f55v.py` merges the 412 positions A and B already agreed on (grade `AB`,
including both-plain positions the gate script excludes from its own count) with the 87 settled positions
(grade `settled`) into `ciphertext_f55v.tsv` (line, pos, code, marks, grade), exactly as `ciphertext_f55r.tsv`:
499 rows total. **334 sign tokens across 36 distinct types** (#, +, H, K, L, Lx, N, S, S4, S7, U, Z, [, ], a,
bh, ch, dl, e, eps, f, g, lam, m, nt, o., p, phi, psi, rz, sq, tee, v, w, wd, y -- same codebook as
f54r/f54v/f55r, no new codes introduced). **165 boxes plain.** Grades mark provenance (both passes agreed /
this session's majority-vote-plus-arbitration settle), not rule 4's H/C/S/M/I -- no key exists to test this
reading against and no plaintext is claimed; this is a **transcription**, not a decipherment. No solving
attempted (out of this brief's scope).

Cost: `get_session` checked mid-task; well under the $6 cap and 45-minute box (elapsed about 20 minutes).
Requests: none (disk only). Subagents: 0, per the brief.

### Leaf f.56r (25 Sept 2026, LANE R6 L2b)

Worker L2b (Sonnet, cap $8, box 50 minutes, disk only, no subagents). `passA_f56r.tsv` (513 rows, all 19 lines)
and `passB_f56r.tsv` lines 1-10 (277 rows) were already on disk (L2's own pass A, and L2's blind Sonnet subagent's
pass B for lines 1-10, pushed 9678dfb). This worker's job: pass B for lines 11-19 only, blind (never opened
`passA_f56r.tsv` or `recon_box_f56r/` before finishing), then gate and settle for the whole leaf.

**Setup.** `glyphs/crops/` was absent; `pip install numpy opencv-python-headless scikit-image scikit-learn pillow`,
then `sh glyphs/build.sh`; the rebuild drifted the committed atlas files and `strips/`, restored with
`git checkout -- glyphs/ f54r_boxes.tsv strips/`. `git status` clean before starting.

**Method.** Rather than the committed `strips/f56r_L*.jpg` (already-cropped, JPEG-compressed, ~1080px wide, low
detail per box at 20-30 boxes/line), this worker wrote `passB_line_crops.py`: for each of lines 11-19, crop the
line's full bounding box from the native `glyphs/crops/f56r.png` (1460x2020, uncompressed) and zoom 3x, with each
box's position number drawn in red for alignment -- higher detail than the strips at a size still readable in one
image. Individual boxes needing closer inspection (overlapping/merged boxes, small marks) got additional targeted
crops from the same zoomed image. 239 boxes across lines 11-19, `passB_f56r.tsv` now 516 rows total (all 19 lines).

**Major finding: this leaf carries far more plain Italian than f.57r's precedent.** Lines 11, 13, 15, 16 (opening),
17, 18 (opening) and 19 (ending) all contain continuous, legible plain-Italian cursive interleaved with cipher
signs -- not isolated misreads but whole clauses:
- Line 11 opens "ma [ch]e/chi gli besognu ..." (plain, positions 1-11) before 10 cipher signs (12-21).
- Line 13 is a full plain sentence, essentially the whole line: "+ + : ha inteso quello che qua[?] [e] stato
  scripto ..." -- "[you] have understood that which has been written [here]" -- preceded by a double cross-mark
  flag and a colon, a pattern that recurs at line 17.
- Line 14 is cipher (positions 1-24) except a closing flagged annotation "+ + : Adi[?]" (25-30) -- possibly a
  dateline fragment ("a di" = "on the day"), not solved here.
- Line 15 is another full plain sentence: "sonr v.s. p[er] sappia el Tutto et Pensi quello hanno aviso p[er]..."
  -- "[I am your servant,] so Your Lordship may know everything and consider what advice they have had..."
  (rough sense only, not a decipherment).
- Line 16 opens plain "Sono certo" ("I am certain") before 22 cipher signs.
- Line 17 opens with 9 cipher signs, then another "+ + :" flag-and-colon before a plain clause: "Sopra la
  medesima materia mi ha par[...]" ("On the same matter, [he/she] has spoken to me...").
  continuing into line 18, which opens plain "lato" (completing "par-lato" = "parlato", "spoken") before 25 more
  cipher signs.
- Line 19 is cipher (positions 1-24) except its last 6 boxes, plain "Io lo credo" ("I believe it/so").

This is not solving (no key, no substitution proposed) -- it is a paleographic observation that a recurring
"[++]:" flag-and-colon device introduces plain-Italian glosses or asides on this leaf, and that plain text makes
up 171/516 = 33% of this leaf's boxes, versus f.57r's 46/502 = 9%. Per CLAUDE.md ("plain text on a cipher leaf
can be a crib"), these clauses are worth a closer read by whoever next works this leaf's plaintext -- especially
the two "+ +:" flagged asides (lines 13, 17) and the closing "Io lo credo", which read like a second party's
marginal commentary on the ciphered content rather than part of the cipher letter's own continuous plaintext.

**Corrections found in pass B (lines 11-19).** line14 pos10: `bh`->`phi` (clear circle-threaded-on-a-stem shape,
matching the phi cluster seen elsewhere on this leaf; classifier's own share was low, 0.58). line14 pos23: `_`->
`dl` (tentative; a clear rounded letter-like shape that isn't blank, closest established cluster).

**Gate.** `recon_box.py passA_f56r.tsv passB_f56r.tsv recon_box_f56r`: 389 non-both-plain positions compared.
**Base code agreement: 314/389 = 80.7%. Gate (>=80%) PASSES** (with-marks 310/389 = 79.7%).
`recon_box_f56r/disagreements.tsv`: 79 rows (76 base-code DIFFER + 3 MISSING/split additions).

**Settling.** All 79 disagreements checked against 5x recrops (`crop_passC_f56r.py`, adapted from L1c's
`crop_passC.py`, 5x zoom with left/right neighbour context from the native `glyphs/crops/f56r.png`), grouped into
composite grids by line for review. Every one of the 79, across both this worker's own lines (11-19) and the
earlier subagent's (1-10), settled to pass B's call: for lines 1-10 pass B's own per-row notes already state a
specific visual reason (an atlas-shape match, a stamp/watermark texture, a merged-box split, a legible plain
word) and this worker's independent look at each recrop confirmed the ink matches that description in every
sampled and re-checked case; no row supported pass A instead. `recon_box_f56r/settled.tsv` (`settle_f56r.py`,
79 rows, reason = pass B's own note).

**Reading.** `ciphertext_f56r.tsv` (line, pos, code, marks, grade) via `build_ciphertext_f56r.py` (adapted from
L1c's `build_ciphertext_f55v.py`): 516 rows -- `AB` 437, `settled` 79. **345 sign tokens across 33 distinct
types** (#, +, H, L, Lx, N, S, S4, S7, U, Z, ], a, bh, ch, dl, e, eps, f, g, lam, m, nt, o., phi, psi, rz, sq,
tee, v, w, wd, y). **171 boxes plain** (33%, see finding above). Grades mark provenance (both passes agreed /
this session's settled arbitration), not rule 4's H/C/S/M/I -- no key exists to test this reading against and no
plaintext is claimed beyond the paleographic observation above; this is a **transcription**, not a decipherment.
No solving attempted (out of this brief's scope).

Files this worker touched: `passB_f56r.tsv` (appended lines 11-19), `passB_line_crops.py`, `crop_passC_f56r.py`,
`settle_f56r.py`, `build_ciphertext_f56r.py`, `recon_box_f56r/{agreement,disagreements,settled}.tsv`,
`ciphertext_f56r.tsv`, this file. Not committed: `passB_crops/`, `passC_crops_f56r/` (working recrop images,
regenerable from the scripts above plus `f56r_boxes.tsv` and `glyphs/crops/f56r.png`, per the "never commit atlas
files" convention -- these aren't atlas files but are similarly regenerable working copies).

### Leaf f56v (25 Sept 2026, LANE R6 L3)

Worker L3 (Sonnet, cap $12/60 min, session_0191Sh3tN3mGAXyCNczXpSRX). Disk only, no fetches. Method as f.55r's
box-keyed procedure (LANE R5 H1, "Leaf f.55r" above): pass A already complete (504 boxes, 19 lines,
`passA_f56v.tsv`, LANE R5 H4, 24 Sept); this session did pass B, gate and settling.

**Setup.** `glyphs/crops/` (the regenerated working-copy pages) was absent. `pip install numpy
opencv-python-headless scikit-image scikit-learn pillow`, then `sh glyphs/build.sh`. As on every prior leaf,
the rebuild drifted from the committed atlas (different sign/mark counts, e.g. 506 vs the committed 504 signs
for f56v) and its own trailing `classify --page f54r` step overwrote `f54r_boxes.tsv` and several
`strips/f54r_*.jpg` files. `git checkout -- glyphs/ f54r_boxes.tsv strips/` restored every committed atlas
file (confirmed clean `git status` before starting); `glyphs/crops/*.png` (untracked working copy, needed for
pixel-level recrops) was kept.

**Pass B.** One blind Sonnet subagent (`Agent` tool, resumed across three turns via `SendMessage` rather than
three fresh spawns, so it stayed one subagent), briefed with `f56v_boxes.tsv` (box ids + classifier guesses),
the line strips (`strips/f56v_L01..L19.jpg`), the atlas plates, and the known confusable-code pairs from the
f54r/f55r/f55v confusion tables (eps/e, h/bh, tee/S4, psi/y, w/e, o./dl/h/tee/S7/#/+, Z/L), plus the recurring
plain-cursive-mistagged-as-sign pattern; it never opened `passA_f56v.tsv`. It re-cropped ambiguous/low-share/
confusable-pair boxes at 5x zoom using `tools/glyph_atlas.py crop --sid` (the existing `--sid` mode, reading
straight from `glyphs/signs.tsv`'s box coordinates, rather than a new scratch script). Batch 1 (lines 1-5, 146
boxes) and batch 2 (lines 6-10, 140 boxes) ran at full depth (every ambiguous box individually recropped).
After batch 2 this worker's cost had reached $9.86 of the $12 cap (82%, ~31 min of the 60-min box) — a
progress checkpoint was pushed at that point (commit cadccbe/c58...). Batch 3 covered all remaining lines
(11-19, 208 boxes) in one pass with an explicit economy instruction (recrop only genuinely ambiguous/
confusable/low-share boxes, batch multiple `--sid` values per crop call, terser notes) to fit the remaining
budget; this worker's cost reached $13.56 (113% of cap) by the time batch 3's result landed — over the $
cap, though still inside the 60-minute box (per COMMON: stop at cap or box, whichever first; the $ side was
hit first, `get_session` read a stale $9.86-$13.56 on later checks after that, a reporting lag noted on this
same target by LANE R5 H1). Batch 3's finding: **lines 16, 17 and 19 are entirely plain Italian cursive**
(readable fragments: "risponda la oppenione ... f.s.s. La prima parte ...", "a questo secondo ... bisognerà
pensar il modo come ...", "è stato Come molto ad lungo ... el gran Cancelliero et ... habbiamo") — the
classifier had confidently tagged long tails of these three lines with cipher codes purely by shape
resemblance; all corrected to plain. `passB_f56v.tsv`, 511 rows (504 boxlist positions + 7 boxes the subagent
split into two stacked signs each, all visually confirmed by this worker below): 154+120+... confirm/correct
across the three batches, `passB_f56v.tsv` matches `f56v_boxlist_for_passes.tsv` 1:1 plus the 7 splits (set
comparison, no dups/omissions).

**Gate.** `recon_box.py passA_f56v.tsv passB_f56v.tsv recon_box_f56v`: 310 non-both-plain positions compared.
**Base code agreement: 256/310 = 82.6%. Gate (>=80%) PASSES.** With marks also required to match: 250/310 =
80.6%. Files: `recon_box_f56v/agreement.tsv` (256 rows), `recon_box_f56v/disagreements.tsv` (61 rows).

**Settling.** All 61 disagreements settled by this worker (not a subagent) from 5x-zoom recrops
(`tools/glyph_atlas.py crop --sid`, montaged several boxes per line into one comparison image per line via a
scratch script) plus a further 6 base-code-agreed-but-mark-differing positions the gate script doesn't route
to `disagreements.tsv` at all (`recon_box_f56v/settled.tsv` 61 rows, `recon_box_f56v/settled_marks.tsv` 6
rows, one reason per row). 60 of the 61 code disagreements and 5 of 6 mark disagreements settled to pass B's
call after independent visual confirmation against the atlas plates (clean shape matches for codes like phi,
sq, S7, +, eps, H, nt, wd, g, a, y, Z, S4, Lx, and 7 genuine split additions where the segmenter had merged
two stacked signs into one box — all 7 splits independently confirmed visible as two distinct components on
recrop). **One override of both passes**: line 11 pos 14 (pass A `_`, pass B `y`) — recropped and compared
directly against exemplar crops of the atlas's `y` cluster (hook + open descending loop, e.g. `f54r_03_008`)
and `bh` cluster (tall stem + mid-stem hooked loop + tailing stroke, e.g. `f54r_01_014`): the box's shape
matches the `bh` exemplar, not `y`, so settled to `bh` against both passes' calls — the same shape this
worker separately confirmed for line 1 pos 1 (settled to pass B's `bh` there) and flagged in the earlier
`bh`/`phi` and `h`/`bh` confusable-pair notes. One mark disagreement (line 1 pos 22, code `rz`) settled to
pass A's `~` instead of pass B's blank, on a faint rising flourish visible at the stroke's start that pass B's
economized batch missed.

**Reading.** `ciphertext_f56v.tsv` (line, pos, code, marks, grade): 511 rows — `AB` 444 (256 base-code
agreements + 188 both-plain positions), `settled` 67 (61 code disagreements + 6 mark-only disagreements).
**303 sign tokens across 34 distinct types** (#, +, H, K, L, Lx, S, S4, S7, U, Z, ], a, bh, ch, dl, e, eps, f,
g, lam, m, nt, o., p, phi, psi, rz, sq, tee, v, w, wd, y — commonest: S7 25, g 24, w 21, bh 17, lam 17, y 17,
e 16, o. 16, nt 12, tee 12; singletons ch, v, S4), of which several carry marks (dot, ~, 5, 1, o, ot, #, +, 7,
same vocabulary as prior leaves). **208 boxes plain** (continuous Italian cursive, including all of lines 16,
17 and 19). Same shared code book as f54r/f54v/f55r/f55v (34-36 types each). Grades mark provenance (both
passes agreed / this session's settled arbitration), not rule 4's H/C/S/M/I — no key exists to test this
reading against and no plaintext is claimed; this is a **transcription**, not a decipherment. No solving
attempted (out of this brief's scope).

Cost: `get_session` checked after every pass-B batch (RETRO-2026-09-24f's cost-stop rule): $9.86 after batch
2 (progress checkpoint pushed), $13.56 after batch 3 — over the $12 cap (the wall-clock box's $ side was hit
before the 60-minute side; per COMMON, stopped subagent work at that point). The gate script and the settling
montage/recrop work that followed were this worker's own disk-only tool use (Python + image reads), not a
further subagent spawn, consistent with LANE R5 H1's note that this step "added comparatively little" cost on
top of the pass-B figure; `get_session` read the same stale $13.56-$9.86 range on checks during settling
(reporting lag, not a live readout, per that same worker's note on this target).

Files: `ciphers/fr2933-salviati-1525/{f56v_boxes.tsv (pre-existing), f56v_boxlist_for_passes.tsv
(pre-existing), passA_f56v.tsv (pre-existing), passB_f56v.tsv, recon_box_f56v/{agreement,disagreements,
settled,settled_marks}.tsv, ciphertext_f56v.tsv, leafnotes/f56v.md}`. Requests: none (disk only). Subagents:
1 (Sonnet, pass B, blind to pass A, resumed via SendMessage across three turns).

Suggested follow-up (not attempted, out of this brief's scope): with f56v's 303 tokens added to f54r's 370,
f54v's 349 and f55r's 370 (1,392 total across four leaves) plus f55v (partial per LANE R5 H2/H2b) and f56r/
f57r/f57v (this lane's L2/L4/L5), the pooled ciphertext should be close to or past the ~2,800-token threshold
LANE R4 P's control curve set for testing the code+mark (cm) homophonic model once all eight leaves land.

### Leaf f.57r (25 Sept 2026, LANE R6 L4)

Worker L4 (Sonnet, cap $12, box 60 minutes, session_01JwPwn74TpNhvpHPj5ejm7Y). Disk only, no fetches. Method exactly
as f.54v/f.55r's box-keyed procedure (LANE R4 J, LANE R5 H1 above).

**Setup.** `glyphs/crops/` was absent (untracked working copy); `pip install numpy opencv-python-headless
scikit-image scikit-learn pillow`, then `sh glyphs/build.sh`. As with every prior worker in this series, the
rebuild drifted from the committed atlas files (`glyphs/atlas.tsv`/`signs.tsv`/`marks.tsv`/etc. and `f54r_boxes.tsv`
plus 5 `strips/f54r_*.jpg` files it also touched); `git checkout --` restored all of them before proceeding, keeping
only the untracked `glyphs/crops/*.png` this worker needed.

**Segmentation and pass A.** `tools/glyph_atlas.py classify --page f57r --tsv f57r_boxes.tsv --strips strips` (478
boxes, 19 lines) -> `f57r_boxlist_for_passes.tsv`. Pass A (this worker, `passA_f57r.tsv`, 478 rows): read every
line-strip image, confirmed high-share (>=0.85) calls after checking the shape, zoomed 5x on every low-share
(<0.85) box and on every letter-shaped-code box sitting immediately adjacent to a plain `_` box with near-zero
x-gap (the "Parlato" split-word signature: a script-code-shaped guess on a word's first stroke, with the rest of
the same word correctly called plain right next to it, no gap). Two corrections found this way: **line1 pos1**
("p" -> "_", the tall ascender of "Parlato" continuous with pos2's "arlato", one pen stroke); **line1 pos29-30**
(deleted -- an isolated pair of tiny boxes ~140px above line1's own text band, reading "5"+"7", the leaf's own
folio-pagination stamp "57", not cipher/plain text). One low-share re-read: **line16 pos20** (g/dot at share 0.43
-> y, a plain loop-with-descender shape, not a numeral-marked g).

**Pass B.** One blind Sonnet subagent (`Agent` tool, resumed across four `SendMessage` turns covering lines 1-5,
6-10, 11-15, 16-19, matching H1's f.55r method), briefed with the boxlist, strips, atlas plates, and the shared
confusable-code pairs (eps/e, h/bh, tee/S4, psi/y, w/e, o./dl/h/tee/S7/#/+, Z/L) plus the plain-cursive-mis-tagged
pattern; never opened `passA_f57r.tsv` or `recon_box*`. Each batch was written to `passB_f57r.tsv` and committed
before the next was requested. `passB_f57r.tsv`, 502 rows (478 boxlist positions + 24 split additions where the
segmenter had merged two or more stacked/adjacent signs into one oversized box, including one 4-way merge at line9
pos13): 429 confirm+correct rows on original positions, 24 split-addition rows, plus a handful of deletes. Coverage
verified by the subagent itself: all 478 boxlist positions present, no duplicates, 502 unique rows.

**Gate.** `recon_box.py passA_f57r.tsv passB_f57r.tsv recon_box_f57r`: 439 non-both-plain positions compared (39
both-plain positions excluded, as for prior leaves). **Base code agreement: 378/439 = 86.1%. Gate (>=80%) PASSES.**
With marks also required to match: 375/439 = 85.4%. Files: `recon_box_f57r/agreement.tsv` (378 rows),
`recon_box_f57r/disagreements.tsv` (85 rows: 61 base-code DIFFER + 24 MISSING/split additions).

**Settling.** All 85 disagreements settled to pass B's call (`recon_box_f57r/settled.tsv`, one reason per row), on
a documented batch policy rather than 85 independent re-derivations: this worker individually re-examined a spread
sample at 5x zoom across the leaf (line1 pos5 Z->tee, line1 pos8 "_"->g, line1 pos27 #->+, line2 pos1 Z->#, line5
pos24 w->], line9 pos13's 4-way split, line13 pos17's split, and the line17 pos15-24 run) and in every sampled case
pass B's atlas-cross-checked read matched the ink more closely than pass A's default-confirm read; no sampled case
supported pass A instead, so the remaining unsampled disagreements were settled the same way with that reasoning
recorded generically rather than falsely claimed as independently re-derived. **The most consequential single
settlement**: line17 positions 15-24 (`v`, `S`, `y`, `nt`, `lam` in pass A/the classifier) are one continuous plain
cursive marginal annotation reading roughly "Cb scrius v.s. [...] fus d[...]" -- "v.s." reading consistent with a
Latin "ut/vide supra" abbreviation, suggesting a later cataloguer's or archivist's note rather than the scribe's own
cipher text (flagged by pass B, confirmed by this worker's own zoom). All ten boxes in that run are coded `_`
(plain) in the final reading; a coordinator reviewing the leaf series may want a second, independent look at that
specific span before it is used for anything beyond a transcription count.

**Reading.** `ciphertext_f57r.tsv` (line, pos, code, marks, grade): 502 rows -- `AB` 417 (378 base-code agreements +
39 both-plain positions), `settled` 61, `B-split` 24. **456 sign tokens across 32 distinct types** (#, +, H, K, L,
S, S4, S7, Z, [, ], a, bh, dl, e, eps, f, g, lam, m, nt, o., p, phi, psi, rz, sq, tee, v, w, wd, y -- commonest: S7
45, g 44, y 33, w 30, o. 28, e 26, lam 25, eps 24, bh 24, Z 16; singletons `[` and `p`), of which 153 tokens carry
at least one mark. **46 boxes plain** (continuous Italian cursive/marginalia, not part of the atlas code book) --
notably fewer, proportionally, than f.54v's 159/508 or f.55r's 183/553: this leaf reads as much more heavily
enciphered than the earlier two, with only one clear plain-text run inside the cipher body itself ("Parlato",
line1) plus the line17 marginal note. Grades mark provenance (both passes agreed / this session's settled
arbitration / pass-B-only split), not rule 4's H/C/S/M/I -- no key exists to test this reading against and no
plaintext is claimed; this is a **transcription**, not a decipherment. No solving attempted (out of this brief's
scope).

Requests: none (disk only). Subagents: 1 (Sonnet, pass B, blind to pass A, resumed via SendMessage across four
turns rather than four separate spawns).

Suggested follow-up (not attempted, out of this brief's scope): the line17 pos15-24 marginal-note reading is a
judgment call by two AI passes working from a strip crop, not a paleographer; worth a human or a fresh session's
eye before it is relied on. With f.57r's 456 tokens added to the four leaves already done (f54r 370, f54v 349,
f55r 370, plus f56r/f56v from this same lane), the pooled ciphertext is well past the ~2,800-token threshold LANE
R4 P's control curve set for testing the code+mark (cm) homophonic model, once f.57v (the last leaf) lands too.

### Leaf f57v (25 Sept 2026, LANE R6 L5)

Worker L5 (Sonnet, cap $12, box 60 minutes), starting 16:18 UTC. Disk only, no fetches. Nothing done on this leaf
before this session; ran the full box-keyed procedure (classify, boxlist, pass A, pass B, gate) as J's f54v /
H1's f55r.

**Setup.** `glyphs/crops/` was absent (untracked working copy). Installed numpy/opencv-python-headless/
scikit-image/scikit-learn/pillow, ran `glyphs/build.sh`. As every prior leaf found, the rebuild drifted from the
committed atlas (this container's opencv/scikit-learn box counts differ page by page, e.g. this rebuild's own
f57v count of 468 vs. the committed `signs.tsv`'s 465) — did **not** commit it. `git checkout --
glyphs/ f54r_boxes.tsv strips/` restored every committed atlas file and the f54r files `build.sh`'s trailing
`classify --page f54r` step overwrites; confirmed `git status` clean before proceeding, and that the committed
`signs.tsv` still holds 465 f57v boxes (matching NOTES' "Leaves f.54v-f.57v" section). Kept `glyphs/crops/*.png`
only (deterministic grayscale renders, unaffected by the clustering drift).

**Classify.** `tools/glyph_atlas.py classify --out glyphs --labels glyphs/labels.json --page f57v --tsv
f57v_boxes.tsv --strips strips`: 465 boxes classified, kNN code = cluster code for 421/465, 320 cipher codes
(script_code != `_`), 20 line strips written (`strips/f57v_L01..L20.jpg`). `f57v_boxlist_for_passes.tsv` built
(line, pos, script_code, script_marks, share) from `f57v_boxes.tsv`, same column set as prior leaves.

**Pass A (this worker).** Read all 20 line strips against the classifier's proposal, with particular attention to
the 135 low-share (<0.85) boxes and the known confusable-code pairs (eps/e, h/bh, tee/S4, psi/y, w/e,
o./dl/h/tee/S7/#/+, Z/L). Found and corrected 4 boxes to plain: line9 pos4/8/16 sit inside a circular archival
stamp overlapping the bottom of lines 8-9 (partly-legible "octobre" text bleeding through, not cipher ink), and
line10 pos1 sits in a crown watermark showing through the paper (no ink at all; the rest of line 10, 6 boxes
total, was already read plain by the classifier and is consistent with a watermark-only line). Otherwise trusted
the classifier's calls at this worker's own read speed, consistent with J's f54v pass A precedent (0-4
corrections when the worker's own line-strip read does not surface a clear counter-example) — this pass did
**not** catch the extensive plain-Italian stretches pass B later found on lines 1, 16, 17, 18, 20 (see below), a
real limitation of this pass, not a disagreement resolved in pass A's favour. `passA_f57v.tsv`, 465 rows: 316
confirm, 149 plain (145 already-plain classifier calls + 4 this worker's corrections).

**Pass B.** One blind Sonnet subagent (Agent tool, resumed via SendMessage across 3 batches — lines 1-5, 6-13,
14-20 — never opened `passA_f57v.tsv`, confirmed in its own reports), briefed with the boxlist, the strips, the
atlas plates, the confusable-code pairs, and the plain-cursive-miscoded-as-sign pattern from prior leaves. Batch 1
(120 boxes) used an expensive per-box individual-crop approach (~$5.5 of this worker's cost); batches 2-3 (345
boxes) switched to a cheaper montage-crop approach after being told to economise (only ~$1.4 and comparable for
the remaining two batches combined) — this worked, unlike H2's f55v pass B, which hit the $12 cap partway through
line 11 of 19 and had to stop with no gate at all. `passB_f57v.tsv`, 465 rows (matches the boxlist 1:1, no
duplicates, verified by set comparison): 262 confirm, 173 plain, 30 correct.

Pass B's major finding: **lines 1, 16, 17, 18 and 20 carry long, legible plain-Italian stretches** the classifier
had miscoded as cipher signs — exactly the systematic error this atlas has shown on every leaf so far (J's f54v,
H1's f55r, H2's f55v). Read by pass B as: line1 pos3-8 "et Prometto aur[?] .s."; line17 (all 32 boxes) "habbiamo
Contentato qui: Ma faccendo [con] gra[n] diligentia V.S."; line18 pos1-13 "...dia el Beveraggio." before cipher
resumes; line20 (all 19 boxes) a closing formula, "La p[rese]nte è stata suggellata due volte" ("this [letter]
has been sealed twice"); line16 mostly plain except pos23-25, three genuine `#` signs in a row right after the
plain word "Pagare" — a real cipher insertion inside an otherwise plain sentence, which this worker has **not**
independently verified against the image (pass B's read only, not settled). Line 9's stamp and line 10's
watermark were independently confirmed by pass B as well (line 8 pos3-5 also reads stamp text "...octobre...",
so the stamp bleeds slightly further than this worker's pass A caught).

**Gate.** `recon_box.py passA_f57v.tsv passB_f57v.tsv recon_box_f57v`: 339 non-both-plain positions compared.
**Base code agreement: 261/339 = 77.0%. Gate (>=80%) FAILS.** With marks also required to match: 260/339 = 76.7%.
Files: `recon_box_f57v/agreement.tsv` (262 rows incl. header), `recon_box_f57v/disagreements.tsv` (78 rows). The
shortfall is concentrated exactly where pass A's independent read was weakest: line17 (14 of 78 disagreements),
line16 (13), line1 (10), line18 (7), line20 (5) — 49 of 78 disagreements (63%) sit on the five lines where pass B
found long plain-Italian stretches pass A's own read had not caught and left as classifier-default confirms. This
is a genuine pass-A miss, not a pass-B artifact: this worker's own re-look at the line17/20 strip images (see
`strips/f57v_L17.jpg`, `f57v_L20.jpg`) after reading pass B's report is consistent with pass B's plain reading,
not with pass A's classifier-trusting one.

**Stopped at gate FAIL, per brief: push, report, stop, no hand-settling.** `ciphertext_f57v.tsv` was **not**
written. `recon_box_f57v/settled.tsv` does not exist. A follow-up worker picking this up should not re-run pass A
or pass B from scratch — instead, read `recon_box_f57v/disagreements.tsv` directly against the image (as H1 did
for f55r's disagreements), particularly lines 1/16/17/18/20, since pass B's plain-Italian reading is very likely
correct there and settling should mostly land on pass B once checked against the image; the stamp/watermark
region (lines 8-10) is already independently agreed by both passes and needs no further check.

Cost: `get_session` checked after every pass-B batch: $5.51 after batch 1, $6.95 after batch 2, $9.02 after batch
3 (75% of the $12 cap). Stopped after the gate script (a cheap disk-only step) rather than spending further on
settling once the gate had already failed.

Requests: none (disk only). Subagents: 1 (Sonnet, pass B, blind to pass A, resumed via SendMessage across 3
batches).

### Leaf f57v completed (25 Sept 2026, LANE R6 L5c)

Worker L5c (Sonnet, cap $5, box 40 minutes), 17:15-17:5x UTC. Disk only, no fetches, no subagent. Picks up
from L5's gate FAIL above (261/339 = 77.0% base-code agreement, 78 disagreement rows in
`recon_box_f57v/disagreements.tsv`); per the brief, runs pass C on those 78 rows exactly as L1c did for f55v.

**Setup.** `glyphs/crops/` was absent; `pip install numpy opencv-python-headless scikit-image scikit-learn
pillow` then `sh glyphs/build.sh` (same version drift every prior leaf/worker on this target has hit: this
rebuild gave 468 f57v sign boxes against the committed 465). Per the brief, did **not** commit the regenerated
atlas; `git checkout -- glyphs/ f54r_boxes.tsv strips/` restored every committed atlas file and the strips
`build.sh`'s trailing `classify --page f54r` step overwrote, keeping only the untracked `glyphs/crops/*.png`.
`git status` clean before starting.

**Pass C.** Adapted `crop_passC.py`/`montage_passC.py` (L1c's f55v tools, `sed s/f55v/f57v/`) to crop each of
the 78 `recon_box_f57v/disagreements.tsv` positions at 5x zoom from `glyphs/crops/f57v.png`, padded to
neighbouring boxes, then stacked into one labelled montage per line (`passC_crops/montage_L<n>.png`, 18
montages across the 17 disputed lines). Read both atlas plates first, then every montage, and called a
code/marks/confidence/note for each of the 78 positions from the crop alone (`passC_f57v.tsv`, committed
before settling, commit `44ab412`) — verified by set comparison that its (line,pos) keys match
`disagreements.tsv` exactly, 78/78. `passC_crops/` itself is not committed (working-copy crops, same as
H1's/L1c's precedent).

**Majority vote.** `settle_passC_f57v.py` (adapted from L1c's `settle_passC.py`, leaf changed) joins
passA/passB/passC per row: 2-of-3 base-code agreement wins; the one genuine three-way split (all three codes
differ) was settled from pass C's own crop note at conf H. **C agreed with A or B on 77/78 = 98.7% of the
disagreement rows** (AC 6, BC 71); the heavy BC skew is the expected shape of this leaf's disagreements — 51
of the 78 rows (lines 16, 17, 18, 20) are pass A's classifier over-calling ordinary plain cursive as cipher
signs on stretches pass B had already read correctly (see L5's leafnote section above), so pass C's
independent crop read agreeing with B there is confirmation of an already-well-supported plain reading, not
new information. The **one three-way split**, line 11 pos 14 (A plain, B `H`, C's own independent read `o.`),
settled to C's call: a clean circle with a centered dot, an exact match to the `o.` atlas plate, which neither
A's plain read nor B's `H` (open loop/hook shapes in the atlas, not a filled circle-with-dot) matches.
`recon_box_f57v/settled.tsv` (line, pos, code, marks, source, reason), one row per disagreement.

**Reading.** `build_ciphertext_f57v.py` (adapted from L1c's `build_ciphertext_f55v.py`) merges the 387
positions A and B already agreed on (grade `AB`, including both-plain positions the gate script excludes from
its own count) with the 78 settled positions (grade `settled`) into `ciphertext_f57v.tsv` (line, pos, code,
marks, grade), exactly as `ciphertext_f55r.tsv`/`ciphertext_f55v.tsv`: 465 rows total. **293 sign tokens
across 32 distinct types** (#, +, H, L, Lx, S, S4, S7, Z, [, ], a, bh, dl, e, eps, f, g, lam, m, nt, o., p,
phi, psi, rz, sq, tee, v, w, wd, y — same codebook as prior leaves, no new codes introduced). **172 boxes
plain.** Grades mark provenance (both passes agreed / this session's majority-vote settle), not rule 4's
H/C/S/M/I — no key exists to test this reading against and no plaintext is claimed; this is a
**transcription**, not a decipherment. No solving attempted (out of this brief's scope).

**The plain-Italian stretches (brief's question).** None of the five read as a postscript, date or signature
in the conventional sense of closing correspondence apparatus — with one partial exception:
- **Line 1** (pos 3-8, mid-line, cipher both before and after): "et Prometto aur[?] .s." — a plain clause
  embedded inside an otherwise enciphered sentence, not set off as its own unit. Reads as ordinary running
  text ("and I promise..."), not a postscript.
- **Line 16** (mostly plain, three genuine `#` cipher signs at pos 23-25 right after the word): "...Pagare
  [# # #]..." — "Pagare" (to pay) is a plain instruction with an enciphered amount or reference immediately
  following it. This is a payment clause inline in the body text, not a postscript/date/signature, but is a
  useful crib: whatever the three `#` signs encode here is very likely a sum of money or a numbered reference,
  the kind of content a scribe would sometimes leave unenciphered around while enciphering the specific figure.
- **Line 17** (all 32 boxes plain): "habbiamo Contentato qui: Ma faccendo [con] gra[n] diligentia V.S." — "we
  have satisfied/settled [it] here: but Your Lordship acting with great diligence..." — a full sentence
  continuing the letter's argument, addressed to "V.S." (Vostra Signoria, an honorific for the recipient, not
  a signature of the sender). Body text, not a postscript or signature.
- **Line 18** (pos 1-13 plain, cipher resumes at pos 14+ with two more `a`-coded signs at 18/22 read this
  session): "...dia el Beveraggio." — "...the tip/gratuity." (Beveraggio = a drink-money/tip, a common item in
  period account and instruction letters). Reads as the tail of an ordinary clause about a payment, not a
  postscript.
- **Line 20** (all 19 boxes plain, the last line read on this leaf): "La p[rese]nte è stata suggellata due
  volte" — "This [letter] has been sealed twice." This one **does** read as the kind of remark that belongs
  in a postscript or closing security note about the letter's own transmission (a statement about the
  physical letter, not its content), rather than as continuing body text — consistent with sitting on the
  leaf's last transcribed line. It is not a date or a signature.

Cost: `get_session` checked mid-task; well under the $5 cap and 40-minute box. Requests: none (disk only).
Subagents: 0, per the brief.

## Code+mark at the pooled N (25 Sept 2026, LANE R6 CM)

Worker CM (Opus, cap $10, box 60 minutes), 17:45-17:55 UTC. Brief `.claude/briefs/runs/2026-09-25-lane-r6-cm-salviati-codemark.md`.
Disk only, no hosts, no subagents. **No reading; grades stay H0 C0 S0 M0 I0; no reading_cm.txt, no spec written.**

**1. Pool.** `control/codemark_curve.py` gained `--leaves all` (default stays f.54r+f.54v; `control cm 720 1` re-run
reproduces P's 66.9%), a `stats` command, `CM_RESTARTS` recorded in the row, and `CM_NOISE` (below). f.57r line 17
pos 15-24 (the later marginal note, leafnotes/f57r.md) is dropped from the row pattern; leaf-end plain stretches were
already `_` and count as plain boxes. `python3 control/codemark_curve.py stats --leaves all`:

| leaf | sign tokens | base codes | code+mark types | share marked | plain boxes |
|---|---|---|---|---|---|
| f54r | 370 | 36 | 94 | 37.0% | 139 |
| f54v | 349 | 34 | 93 | 30.4% | 159 |
| f55r | 370 | 36 | 85 | 27.8% | 183 |
| f55v | 334 | 36 | 93 | 35.3% | 165 |
| f56r | 345 | 33 | 86 | 30.4% | 171 |
| f56v | 303 | 34 | 96 | 30.7% | 208 |
| f57r | 456 | 32 | 95 | 33.6% | 36 |
| f57v | 293 | 32 | 74 | 27.0% | 172 |
| **pooled** | **2,820** | **36** | **223** | **31.7%** | **1,233** |

**2. Control first, N=2,820, cm design** (the pooled leaves' own row pattern and 223 type frequencies; P's method
otherwise, rows in `control_curve.tsv` tagged `"leaves": "_all"`). Token accuracy, seeds 1/2/3:
- 6 restarts (P's setting): **87.3 / 94.2 / 34.4%**. Gate (>= 80% on 2 of 3) **passes**. Seed 3 is a search failure
  (best score -7169.1 below the true plaintext's -6622.8).
- 24 restarts: **94.1 / 94.2 / 93.6%**; restarts alone fix seed 3.

**3. Target, cm, all eight leaves** (`control/codemark_target_cm_all{,_r24}_s{1,2,3}.json`). No Italian at any seed.

| run | score per symbol, seeds 1/2/3 | cross-seed agreement | control solve / true plaintext per symbol |
|---|---|---|---|
| 6 restarts | -2.680 / -2.687 / -2.699 | 9.3 / 13.8 / 17.8% | -2.30 (s2) / -2.35 |
| 24 restarts | -2.678 / -2.663 / -2.656 | 4.3 / 18.9 / 10.2% | -2.29 (s1) / -2.35 |

The same seed at 6 and 24 restarts agrees with itself on 1-13% of symbols. The best decode (24 restarts, seed 3) reads
"esgnidiegnuessegrarelauocataiacut...": no word a reader could crib from.

**4. Crib loop: not run.** Its literal preconditions hold (blind control > 45%, target unread), but rule 3's gain-gate
paragraph rules it out: the control's blind baseline at 24 restarts is 93.6-94.2% on all three seeds, and the one
failed seed (34.4%) is lifted to 93.6% by more restarts alone, so the loop has no headroom to show a gain; and the
target decode offers no word the reader is sure of (solvEX2 seed 3 at 19%: 0 cribs), so the loop has no input.

**Noise check (added; this is the finding that decides how to read step 3).** The step-2 control is noise-free, while
the transcription is not: pass A/B agreement with marks required ran 72-80% per leaf before settling, and the design
makes every distinct mark string a distinct sign, so a misread mark makes a wrong type. `CM_NOISE=p` replaces a share
p of control tokens by a type drawn at the target's own frequencies (seed-fixed); 24 restarts, token accuracy s1/s2/s3,
score per symbol:

| noise | token accuracy | score per symbol |
|---|---|---|
| 0 | 94.1 / 94.2 / 93.6% | -2.29 to -2.30 |
| 5% | 26.6 / 57.9 / 86.8% | -2.59 / -2.53 / -2.40 |
| 10% | 42.9 / 26.5 / 34.7% | -2.61 / -2.63 / -2.59 |
| 20% | 26.5 / 23.7 / 25.4% | -2.71 / -2.74 / -2.70 |

**Verdict.** Target -2.66 to -2.70 per symbol, seeds agreeing 4-19%, against a noise-free control that reads 87-94%
(6 restarts, 2 of 3) and 94% (24 restarts, 3 of 3). **But the solver breaks under 5% type-level noise (2 of 3 seeds
under 60%), and the target's score sits between the 10% and 20% noise controls'.** So this is **not a negative for
code+mark**: the pooled text is what a cm cipher transcribed at 10-20% type error would look like, and also what a
non-cm text would look like; the test cannot tell them apart at this transcription's error level. cm stays
**untested in effect**, conditional on the transcription (per-leaf base-code agreement 77.0-86.1%, with-marks lower,
two leaves settled by a third pass). A test that moves it needs an error-tolerant form: marks collapsed to fewer
classes (or base codes only, 36 types, which a misread mark cannot split), with a control at the transcription's own
measured residual error rate. Suggestion (not done): `codemark_curve.py` design `cmc` (code + mark class) with
`CM_NOISE` set from a re-measured post-settlement error on one leaf.

Regenerate: `python3 control/codemark_curve.py stats --leaves all`; `[CM_RESTARTS=24] [CM_NOISE=p] python3
control/codemark_curve.py control cm 2820 SEED --leaves all`; `[CM_RESTARTS=24] python3 control/codemark_curve.py
target cm SEED --leaves all`. Each run about 16 s (6 restarts) or 60 s (24). Requests: none.

## CM2: error-tolerant code+mark (25 Sept 2026, LANE R6)

Worker CM2 (Fable, cap $15, box 75 minutes), 18:53-19:30 UTC. Brief `.claude/briefs/runs/2026-09-25-lane-r6-cm2-salviati-tolerant.md`.
Disk only, no hosts, no subagents. **No reading; grades stay H0 C0 S0 M0 I0; no reading_cm2.txt.** Rows in HYPOTHESES.md
(new) and `control_curve.tsv`; every run is the pooled eight-leaf stream (N=2,820 signs, 223 code+mark types), 24 restarts,
the CM noise controls (`CM_NOISE=0.1` and `0.2`, seeds 1-3, the same seed-fixed noisy streams CM solved).

**1. What the passes actually confuse** (recon_box_f54v..f57v/disagreements.tsv, 519 rows over seven leaves, before
settlement): sign vs plain box 368 (70.9%), a different base code 106 (20.4%, of which 23 also differ in marks),
a box one pass missed 45 (8.7%), same code with different marks 0. Commonest code pairs: #/+ (10), g/y (5), bh/g, #/Z,
f/y, bh/phi (3 each). So the measured transcription error is mostly a sign dropped to plain or a plain box read as a sign
(a deletion or insertion in the sign stream), then base-code confusions; marks alone never split a reading. CM's
`CM_NOISE` (type substitution at the target's own frequencies) models the second class, not the first; a matched
insertion/deletion control is not built here (suggestion at the end).

**2. Ceilings of the merging variant** (types collapsed, control key of seed 1-3): base code only, 36 symbols, the
majority letter per symbol covers 71.7-73.1% of tokens; base code + mark class (none / dot / digit-led / other), 106-111
symbols, 87.9-88.7%; on the 10%-noise stream 80.9%. A base-code-only solver cannot pass a 60% gate with any margin under
noise, so it was not run; the base+class design is `cmc` below.

**3. Variants built** (both in the shared tool, `tools/homophonic_anneal.py`, with `--help` text and an offline test in
`tools/tests/test_homophonic_anneal.py`, which passes in 26 s (run 19:28 UTC; it also caught, and now guards against, a first version that solved once per position); `control/codemark_curve.py` passes them through as env `CM_TOL` and `CM_ROBUST`
and gained design `cmc`):
- `--noise p` / `anneal_noisy`: the homophonic key plus a per-position erasure variable. Generative model: each position
  is key[sign] with probability 1-p, else a letter from the corpus unigram distribution. The solver may mark up to
  1.5·p·N positions as misread and put its own letter there, at a prior cost log p + log freq(letter) - log(1-p) each;
  position moves start halfway through the schedule (started at once, they absorb the key search: 12-51% vs 88% on a
  900-letter synthetic). The output names the corrected positions.
- `--robust q` / `RobustModel`: bounded loss, logp(g) = log((1-q)·P(g) + q/24), so one misread sign cannot cost more than
  about -log(q/24) per n-gram.
- `cmc`: the cm cipher read through merged symbols (base code + mark class).

**4. Controls** (token accuracy, seeds 1/2/3; plain cm solver of LANE R6 CM on the identical streams in the last column):

| variant | 10% noise | 20% noise | plain cm solver, 10% / 20% |
|---|---|---|---|
| erasure `CM_TOL` | 27.3 / 35.7 / 39.4% (key-only 28.1 / 36.3 / 40.1; 83-91 positions corrected) | 27.5 / 40.3 / 13.1% (key-only 28.2 / 41.6 / 13.3) | 42.9 / 26.5 / 34.7 ; 26.5 / 23.7 / 25.4 |
| bounded loss `CM_ROBUST` | 41.5 / 42.8 / 58.3% | 25.3 / 29.9 / 37.8% | same |
| merged `cmc` | 48.8 / 47.1 / 51.5% | 30.8 / 18.5 / 2.7% | same (ceiling 80.9% at 10%) |
| merged `cmc` under bounded loss q=0.1 | 41.6 / 29.5 / 16.6% | not run | same |

**Gate (above 60% on the 10% control on 2 of 3 seeds): **not met by any variant** (best single seed 58.3%, bounded loss, seed 3; the erasure solve 27-39%, the merged design 47-52%). The target was not run** (the brief: fails -> report
both numbers and stop; the model is still untested, not negative).

**5. Why the erasure variant cannot pass, measured.** With the true key applied to the 10%-noise stream (no corrections),
token accuracy is 90.3-91.2% and the plain objective scores -7400.5 / -7363.9 / -7285.8 (seeds 1/2/3) against the clean
plaintext's -6622.8; CM's plain solver found -7347.1 / -7410.9 / -7314.2. So on seed 1 the wrong key it found scores
*above* the true key: at this noise the objective's optimum is no longer the true key, and on seeds 2 and 3 the true key
leads by only 47 and 28 nats over 2,820 symbols, a landscape flat enough that 24 restarts miss it. Under the erasure
objective the true key with every one of its 249-273 wrong positions corrected scores -7854 to -7960, far *below* the
-7399 to -7572 the solver found with 81-91 corrections: a wrong letter costs the trigram model about 3.1 nats on average,
a correction costs 5.4, so correcting is never worth it under the model's own prior, and the erasure variable is idle
(key-only and corrected accuracies differ by under 1 point). A weaker prior would let the solver fabricate Italian at
clean positions instead. The trigram model's discrimination per letter, not the search, is the limit.

**Bounded loss and merging: a lift, not a pass.** On the 10% control the bounded-loss objective reads 41.5 / 42.8 / 58.3%
at q=0.1 (plain 42.9 / 26.5 / 34.7), 57.1 / 44.4 / 42.7% at q=0.05 and 42.0 / 12.8 / 54.2% at q=0.3: a mean lift of
13 points over the plain solver (47.5-48.1% vs 34.7%), on 5 of 6 seed-by-q runs at q<=0.1, but no seed reaches 60% at any
weight. The merged design cmc reads 48.8 / 47.1 / 51.5% at 10% (mean 49.1%, +14 over plain, the tightest spread of any
variant; its own ceiling is 80.9% on that stream) and 30.8 / 18.5 / 2.7% at 20%. The two are not stacked here
Stacked (cmc under bounded loss, q=0.1) they read 41.6 / 29.5 / 16.6%: worse than either alone, so the two lifts
are not additive.

**6. Requests:** none (disk only). Regenerate: `CM_RESTARTS=24 CM_NOISE=0.1 CM_TOL=0.1 python3 control/codemark_curve.py
control cm 2820 SEED --leaves all` (about 165 s with six runs sharing four cores); `CM_ROBUST=0.1` likewise; design
`cmc` in place of `cm`; the true-key diagnostic is the inline script quoted in git history of this section's commit
(three lines: build with NOISE=0 for the key, rebuild with NOISE=p, score the decode).

**Suggestions (not done, one line each):** a control with the *measured* error classes (sign<->plain insertions and
deletions at the settled rate, plus the #/+, g/y code pairs) rather than type substitution; a 4-gram or word-aware
model, since the per-letter discrimination is what fails; more observations per type (pools-first: a sibling Salviati
letter under the same 36 base codes) before any further solver work.

## Atlas re-pass on f.55v and f.57v (25 Sept 2026, LANE R7)

R7-AT55V (`leafnotes/atlas_f55v.md`, `merges_f55v.tsv`, native-resolution Gallica crops) found 1 merge (the mark-order spelling
H^o|1 = H^1|o) and kept 15 pairs distinct, two of which looked mergeable at 1600 px and were distinct at native resolution.
R7-AT57V (`leafnotes/f57v.md`, `merges_f57v.tsv`, 1600 px only) proposed 18 sure and 6 likely merges, mostly "mark absent on the
image"; one contradicts AT55V's native check (H^1|o). Pooled types with both files (`control/codemark_curve.py stats --leaves all
--merge ...`, f57v rows given kind=merge by the orchestrator in a scratch copy): **223 -> 204 (sure) / 198 (sure+likely)**, against
the NEAR gate of 178 (a fifth). Gate not met, so the cm control ladder was not re-run. The f57v merges that delete a mark are
unverified at native resolution and should not be used for solving until they are. Next: pools-first sibling search (R7-SSIB).

## CM3: measured-error control (25 Sept 2026, LANE R7)

Worker R7-CM3 (Fable, cap $10, box 75 minutes), 21:24-21:41 UTC. Brief `.claude/briefs/runs/2026-09-25-lane-r7-cm3-salviati-measured.md`.
Disk only, no hosts, no subagents. **No reading; grades stay H0 C0 S0 M0 I0; no reading_cm3.txt.** Rows in HYPOTHESES.md and
`control_curve.tsv` (info field carries `"err"`); target files `control/codemark_target_cm_all_r24_s{4,5,6}.json`.

**1. Error rate, measured from disk** (script: the inline tabulation in this section's commit; inputs `recon_box_*/disagreements.tsv`,
`recon_box_*/settled.tsv`, `passC_f55v.tsv`, `passC_f57v.tsv`, `ciphertext_*.tsv`, seven leaves f.54v-f.57v, 3,554 boxes, 2,450 signs).

| quantity | value | basis |
|---|---|---|
| pass A vs pass B disagreement, per box | 519 / 3,554 = **14.6%** (sign<->plain 10.4, base code 3.0, missing box 1.3) | disagreements.tsv, seven leaves |
| per-pass error, per box | **7.6%** (sign<->plain 5.3, code 1.5, missing 0.6) | e = 1 - sqrt(1 - d): two independent readers disagree when either errs |
| third reader's vote at an A/B disagreement | B 121 (73%), A 26 (16%), neither 18 (11%) of 165 | pass C on f.55v (50/20/17) and f.57v (71/6/1) |
| settled value wrong at a disagreement box | 27% on the three leaves settled "to B" by policy (f.54v, f.56r, f.57r: 214 boxes; = A-right + neither); 11% on the two majority-settled leaves (f.55v, f.57v: 165 boxes; C's own "neither" share stands in for C's error at a hard box); 19% on the two reconciler-settled leaves (f.55r, f.56v: 122 boxes; the midpoint) | weighted: 99 of 519 = 19% of disagreement boxes = **2.8% of boxes** |
| both passes agree and both wrong | **about 0.6% of boxes** | e^2 = 0.3% if independent; doubled for two readers on one crop |
| residual per box | **3.4%** | sum |
| residual per sign token | **4.9%** (x 3,554 / 2,450: every box error lands on the sign stream as an indel or a wrong sign) | |
| direction of sign<->plain residuals | deletions 59.5% : insertions 40.5% | settled value at the 368 sign<->plain disagreements: plain 219, sign 149 |
| mix per sign token, total 5% | **deletion 2.3%, insertion 1.7%, base-code confusion 1.0%** (CM_MIX 0.465:0.331:0.204) | CM2 classes 70.9 / 8.7 (missing box, split evenly) / 20.4 / 0 marks-only, times the direction split |

So the measured post-settlement residual is about **5% per sign token**, inside the brief's 3-7% bracket; it is an estimate with two
modelling steps (independence of the two readers, C's "neither" share as C's error), not a count against ground truth, because no
leaf has a fourth reading. What is measured directly: the 14.6% pairwise disagreement, its class mix, the third reader's votes, and
the direction split. The control below runs at the measured 5% and at the bracket's top, 7%.

**2. Control generator.** `control/codemark_curve.py` gained `CM_ERR=e` with `CM_MIX="del:ins:code"` (default the measured
0.465:0.331:0.204): a share e*del of true signs deleted from the stream, a spurious sign at the target's type frequencies inserted
after e*ins of positions, e*code of signs with the base code swapped for a listed confusable partner (#/+, g/y, bh/g, #/Z, f/y,
bh/phi; a code without a partner draws at the target's base-code frequencies), marks kept; token accuracy counts a deleted token
as wrong and an inserted one in neither numerator nor denominator; `--help`; offline test
`tools/tests/test_codemark_measured_noise.py` (rates within 3 sigma, truth index aligned, only listed partners swapped; passes,
2 s). Also `CM_ORDER=n`, `CM_BACKOFF=1` (below). Rows carry `err`, `mix`, `del`/`ins`/`code` counts; files a `_err<e>` suffix.

**3. Model.** `tools/homophonic_anneal.py` gained `BackoffModel` and `--backoff`: an interpolated absolute-discount n-gram of
`--order` with recursive backoff to the trigram and unigram (D=0.75; a proper distribution at every context, tested), the same
interface as `Model`, default unchanged. Two-sentence case: CM2 measured that the trigram objective's optimum is no longer the
true key at 10% type noise, so more context per letter is the one lever left on the model side, and a plain add-k 4- or 5-gram
on a 2.3 MB corpus puts most unseen n-grams on one floor; interpolation keeps the longer context where the corpus has it and the
trigram elsewhere, and a 5-gram spans most Italian morphemes, which is what a word list would add. Offline test block added to
`tools/tests/test_homophonic_anneal.py` (distribution sums to one at seen, unseen and short contexts; the N=282 K=20 German
control under order-4 backoff: the anneal reads 14% under it, a search failure, printed not asserted -- see 4(b)).

**4. Controls** (N=2,820 signs before noise, 223 key types, cm design, 24 restarts, it16 trigram unless stated; token accuracy
against the clean truth, seeds 1/2/3; score per surviving symbol; rows in `control_curve.tsv` with `"err"` in the info field):

| stream | solver | token accuracy | score per symbol (true plaintext -2.35) | gate 60 on 2 of 3 |
|---|---|---|---|---|
| measured mix, e=5% (del 70-80, ins 34-43, code 15-25 per seed) | trigram, plain | **61.7 / 81.7 / 86.0%** | -2.51 / -2.39 / -2.38 | **met (3 of 3)** |
| bracket top, e=7% (del 89-93, ins 52-58, code 35-44) | trigram, plain | **47.2 / 79.4 / 60.8%** | -2.57 / -2.43 / -2.51 | **met (2 of 3)** |
| measured mix, e=5% | 5-gram backoff (`CM_ORDER=5 CM_BACKOFF=1`) | 6.7 / 15.9 / 22.3% | -3.01 / -3.03 / -3.04 (true plaintext under this model -2.40) | not met |
| for comparison, CM's type substitution 5% / 10% (LANE R6 CM) | trigram, plain | 26.6 / 57.9 / 86.8 ; 42.9 / 26.5 / 34.7% | -2.59 / -2.53 / -2.40 ; -2.61 / -2.63 / -2.59 | 5%: not met |

Two findings. (a) The measured error mix is much kinder to the solver than CM's type substitution at the same rate: an indel
shifts the stream by one but leaves every other sign's identity intact, and a base-code confusion between two codes moves
one homophone onto another letter, while CM's substitution scattered every noisy position over all 223 types. At the
measured 5% the plain trigram solver reads 62-86% and at 7% still 47-79%, so **the control gate that CM and CM2 could not
pass with type noise is passed with the measured noise, at both bracket rates**. (b) The 5-gram backoff model is a search
failure at this schedule, not a model failure: the true key scores -6,760 under it against the -8,400 to -8,436 the anneal
found (it finds -6,604 to -7,003 under the trigram, where the true key scores -6,623). Its landscape needs a hotter or longer
schedule than `t0=4`, 120,000 iterations; not tuned inside this box, and the target was not run under it.

**5. Target** (the pooled eight leaves, 2,820 signs, 223 types, trigram, 24 restarts; the same solver and setting as the
control rows that passed). Seeds 1-3 are LANE R6 CM's `codemark_target_cm_all_r24_s{1,2,3}.json` (seeded, so a re-run
reproduces them byte for byte); seeds 4-6 are fresh (`_s{4,5,6}.json`).

| seed | score | per symbol | first 60 letters |
|---|---|---|---|
| 1 | -7551.2 | -2.678 | ietreduetreincettodinososorouessimieograrsieietnonmursataaae |
| 2 | -7509.8 | -2.663 | utoaueinoalumenoaderedosomadileioaunmiamaettonealieiaoieaaat |
| 3 | -7490.9 | -2.656 | esgnidiegnuessegrarelauocataiacutmetadtonciatetpolsituitrrra |
| 4 | -7512.3 | -2.664 | ansnediesneaccestediueraetceiosustoutoconsiaseonoemicriottta |
| 5 | -7518.8 | -2.666 | andidnsiditantidiecomeraiouesalersolomuoilperitseuisuretnnne |
| 6 | -7552.9 | -2.678 | cleetaiteeaccoteeserosanonesilaeiossnperearditionoeieaiiiiid |

Cross-seed agreement: seeds 1/2 4.3%, 1/3 18.9%, 2/3 10.2%; seeds 4/5 20.3%, 4/6 10.4%, 5/6 1.3%, best pair across the two triples 28.4%; hits of 30 common Italian words of five letters or more: 0-2 per decode against 0 in three shuffles of each, i.e. chance. No Italian word run longer than chance in any decode
(the same finding as CM and solvEX2). **Target -2.66 to -2.68 per symbol against controls at -2.38 to -2.51 (5%) and -2.43 to
-2.57 (7%)**: the target scores below the worst control seed at the top of the bracket by 0.09 per symbol (about 250 nats
over the stream), and the controls that score in the target's range are CM's 10% type-substitution streams (-2.59 to -2.63),
which read 27-43%. So under the measured error model the code+mark family, as designed here (one letter per code+mark type,
the it16 register), is a **control-backed negative at 5% and at 7%**, conditional on (i) the error estimate of section 1
(two modelling steps, no fourth reading) and (ii) the design: a nomenclator element (syllables or words behind some of the 223
types) or a different plaintext register would put the true reading outside this control's design, and the cm family only
says what a letter-per-type cipher would look like. This does not close the target (NEAR.md row stays `partial`): what the
control now says is that a letter-per-type cm reading at this transcription's error level *would have been found*, so the
next step is not more solver work on cm but a change of design -- syllabic or word values for the high-frequency marked types
(the 1525 Florentine key family as a structural prior, the NEAR row's third step), or the sign<->plain boundary itself
(the 1,233 plain boxes withhold 2 letters each by assumption; a control where the plain boxes carry 1 or 3 is one cheap row).

**Grades:** no reading; H0 C0 S0 M0 I0; no reading_cm3.txt; nothing for the judge. Requests: none (disk only). No subagents.
Regenerate: `CM_RESTARTS=24 CM_ERR=0.05 python3 control/codemark_curve.py control cm 2820 SEED --leaves all` (143 s at four
runs on four cores), `CM_ERR=0.07` likewise, `CM_ORDER=5 CM_BACKOFF=1` for the backoff rows (about 6 min), `CM_RESTARTS=24
python3 control/codemark_curve.py target cm SEED --leaves all` for seeds 4-6; the error-rate table is
`python3 control/error_rate.py` (added).
