open

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

Progress continues below as pass A / pass B / reconciliation land.

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
