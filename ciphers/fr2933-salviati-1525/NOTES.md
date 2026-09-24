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
