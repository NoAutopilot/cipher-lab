open


**Edition check (LANE N3 csED, 24 Sept 2026 15:45 UTC):** hold lifted -- verdict `open`. Ribier's *Lettres et
mémoires d'estat* (both surviving tomes, archive.org, full text) and Francisque-Michel's *Les Portugais en
France, les Français en Portugal* (1882, archive.org, full text) both read; neither carries Seure's name in
connection with these letters (section 2 below). Brief `.claude/briefs/runs/2026-09-24-lane-n3-csED.md`.
# Chevalier de Seure (Lisbon) to de Fresne and to Henri II, six letters, 12-27 Dec 1558 — BnF fr. 3151 nos. 39-44

QUEUE row: CS2-02 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 10 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026
by LANE N3 csCS2a (session_01JrahDoApcsEHgiQigjaJPY), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2a.md`.

## What it is

Six letters of the Chevalier de Seure, French agent in Lisbon, dated 12 and 27 December 1558: to Monsieur de
Fresne (Florimond II Robertet, seigneur du Fresne) and to King Henri II. Nos. 40/41 and 43/44 are duplicate
copies (confirmed by Bourdeau's repository -- see below). Bound in the same BnF fr. 3151 recueil as two other,
unrelated ambassadors' ciphers (La Guiche to Montmorency, Rome 1551, no. 22; Noailles, Venice, no. 33) which
Bourdeau's repository treats as one catalogue entry (no. 10) but are separate keys and separate items from
Seure's.

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk).** No mention of BnF fr. 3151, "Seure", "de Fresne" or a 1558
   Lisbon-Henri II correspondence found in any of the 104 locally snapshotted cryptiana pages (grep by shelfmark
   and by name across sources/cryptiana/web/*.htm). No live fetch was needed to reach this negative, since the
   name/shelfmark grep covers the full local mirror; not separately confirmed against the live site this pass
   (in budget, not run -- flagged for a future pass if this target is promoted).
2. **Standard printed edition / calendar (edition check, LANE N3 csED, 24 Sept 2026).** Guillaume Ribier,
   *Lettres et mémoires d'estat ... sous les regnes de François premier, Henry 2. & François 2.* (Paris, 1666)
   -- both tomes located on archive.org and read as full djvu text: `bub_gb_bOnmNv2ZLVoC` (runs to April 1559,
   covers late 1558 -- the one entry dated December 1558, p.23988 in the OCR, is an unrelated ambassador's
   letter from Andrinople/Constantinople, not Seure) and `bub_gb_qWTswSr32NYC` (runs only to 1557, too early).
   Grepped both for "Seure", "Fresne" and "Lisbonne": no genuine hit in either (the one "Seure" string match in
   `bOnmNv2ZLVoC` is the false positive "prédecejfeurseurent"; "Fresne" and "Lisbonne" do not appear at all).
   Ribier does not print these letters. R. Francisque-Michel, *Les Portugais en France, les Français en
   Portugal* (Paris, 1882) -- full text read from archive.org (`lesportugaisenf00michgoog`): no genuine "Seure"
   or "Fresne" hit (only false positives on "asseure(ment)"/"seureté"). WebSearch independently confirms Seure
   served as French ambassador resident in Portugal 1557-1559 and returned to France on the eve of
   Cateau-Cambrésis (1559), consistent with this dispatch, but surfaces no printed edition of his letters.
   Vertot/Villaret, *Ambassades de Messieurs de Noailles en Angleterre* (5 vols, 1763) -- not read directly this
   pass (an England embassy edition, not Portugal; a targeted WebSearch combining "Ambassades de messieurs de
   Noailles" with "Seure"/Lisbonne/Portugal found no connection); flagged as not fully checked if this target is
   promoted. Jules Mathorez's writing found by WebSearch concerns the Portuguese colony at Nantes, a different
   subject, not Seure's embassy. One modern secondary source was found but not read (Cairn.info paywalled,
   HTTP 403 to WebFetch): a 2021 article on Franco-Portuguese relations in the Saint Petersburg manuscript
   collections, 1557-1572 -- title gives no indication it prints or transcribes this correspondence; not
   pursued (Cairn is not in this brief's route and the article is about manuscript collections, not a printed
   edition of the letters).
3. **Lasry's publications.** No Lasry solution of fr. 3151 or a Seure/Lisbon 1558 cipher found in Tomokiyo's
   pages or web search.
4. **DECODE (sources/decode/ on disk) + both solver-repo clones (grepped by shelfmark).** No DECODE record for
   fr. 3151 in the local snapshot. dbourdeau/cyphersolver (shallow clone, 24 Sept 2026): `guiche1551/NOTES.md`
   (catalogue no. 10, worked 21 Sept 2026) covers the whole recueil and states of Seure specifically: *"The
   catalogue says 'no siblings', which is wrong. The volume holds six Seure letters of 12 and 27 Dec 1558 (nos.
   39-44, Gallica views ~72-88), and nos. 40/41 and 43/44 are duplicate copies. Each mixes clear text with long
   cipher blocks, about eight pages and roughly 2,000 signs in all: a homophonic symbol alphabet of about 60
   signs plus numerals (12, 13, 23, 100), so a nomenclator. There is no decipherment on the leaves... This is
   solvable in principle with a full transcription (large corpus, one key), but that is a multi-session job."*
   Escalation log for the item: *"Seure fr. 3151 nos. 39-44 (about 2,000 signs, homophonic with numerals) --
   blocker: not-attempted; left as a multi-session job; not transcribed"*; and *"known-keys: not done -- no
   French diplomatic key of the 1550s (Tomokiyo's Henri II pages, Lasry's GL.htm) was tried on ... Seure."*
   So Bourdeau's own repository confirms Seure was never even attempted, let alone solved. aaymeloglu/
   unsolved-ciphers: no hit for fr.3151 in this shallow clone. WebSearch ("fr.3151 Seure Fresne Henri II
   chiffre"; "Seure ambassadeur Lisbonne 1558 chiffre dechiffre Henri II"): both confirm the manuscript and the
   Chevalier de Seure's Lisbon letters exist in fr.3151, no hit for a decipherment.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9059865k/f75/full/500,/0/native.jpg` (view 75, within the ~72-88
   range). Image shows a two-page opening: the left leaf is a dense block of closely-set text distinct in
   character from the ordinary secretary hand on the right leaf, and the right leaf carries a clearly separate
   symbol/cipher paragraph mid-page -- consistent with Bourdeau's "clear text with long cipher blocks" account.
   Leaf: https://gallica.bnf.fr/ark:/12148/btv1b9059865k/f75.item

## Verdict

**Stage 2, open.** No source of the six names a decipherment of the Seure letters. This is a genuinely untried
target, not merely unsolved: Bourdeau's own repository explicitly left it as "not attempted... a multi-session
job", distinct from the La Guiche and Noailles items in the same recueil (which were partly read in the same
session). ~2,000 signs across six letters (two duplicate pairs) of a single homophonic-plus-numeral nomenclator
is a substantial corpus for one key -- a plausible cryptanalysis or key-recovery candidate once transcribed.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 10; `guiche1551/`
working folder), CC BY 4.0 -- prior scoping, not an attempt at Seure specifically.

Not decoded, not transcribed here (out of scope for check-solved). Rule 10: no novelty claim made; this is a
search result, not a verifier's classification.

## Capture and passes (24 Sept 2026, LANE R4 K)

Worker K (Sonnet, cap $8), brief `.claude/briefs/runs/2026-09-24-lane-r4-k-seure-capture.md`. No solving.

**Leaf survey, views 72-88.** Manifest `btv1b9059865k/manifest.json` labels every canvas `NP` (unlabelled,
like fr.16092/fr.5160 in the playbook); folio/item boundaries below are read by eye from 500px scans
(`images/survey/f72.jpg`..`f88.jpg`), not manifest-pinned. Six docket/title-page openings found in this
range, at canvas f72, f74, f77, f79, f81, f85 -- one per item, matching the six letters nos. 39-44:

| item (inferred order) | docket canvas | docket text (as read, uncertain) | content canvas(es) | cipher seen? |
|---|---|---|---|---|
| 39 | f72L | "...commandement de... au... Roy" | f72R, f73L | no -- plain prose, ends with signature/date f73L, f73R blank verso |
| 40 | f74L | "Lettre de...Seure au Roy...Portugal" | f74R, f75L, f75R | **yes, f75L**; f75R checked at native res and is plain prose (see below) |
| 41 | f77L | "Autre lettre du dict Seure au dict Roy 1558" | f77R, f78L, f78R | yes -- f77R (bottom), f78L (full page), f78R (top, then seal+signature) all show dense cipher at 500px |
| 42 | f79L | "Lettre de...Sr de...au Roy..." | f79R, f80L | no -- plain prose at 500px, f80R blank verso |
| 43 | f81L | "Autre lettre du dict Sr de Seure au Roy Henry second..." | f81R, f82L, f82R, f83L, f83R | yes -- all five show dense cipher at 500px (the longest cipher run of the six) |
| 44 | f85L | "Autre lettre Seure...au Roy 1558" | f85R, f86L, f86R, f87L, f87R | yes -- f85R (bottom), f86L (full page), f86R (top), f87R (top+bottom) at 500px; f87L plain |
| (next item, outside range) | f88L | new docket, unrelated to Seure | -- | -- |

**Duplicate pairs, per the "Autre lettre" docket wording and matched content length/position: 40<->41 and
43<->44 (consistent with Bourdeau's repository note already in this file).** 39 and 42 read as plain letters
with no cipher visible even at native resolution's neighbour (39's own pages) or 500px (42) -- if this holds,
the ~2,000 signs described in the brief come entirely from the four enciphered items (40/41, 43/44), not all
six; **flagging this as inferred from a quick visual survey, not confirmed by transcription of every page**,
since 42 in particular was only checked at 500px. This whole table is item-boundary inference from docket
wording and page appearance, not a read of any catalogue description -- a future pass should confirm against
the archivesetmanuscrits.bnf.fr finding aid if one exists for this recueil.

**Codicological caveat.** f75L (item 40's cipher, captured below) ends with a full valediction and signature
("Vostre treshumble et tresobeissant serviteur et subject ... de Seure"), but the facing/following page f75R
is plain prose on an unrelated topic (Portuguese/Spanish/Moroccan news) with no docket header of its own --
i.e. a letter's ending and the next page's un-docketed opening sit in what looks like the wrong order for a
simple recto/verso page-turn. Not resolved this pass (out of scope, capture-only); flagged for whoever reads
item 40 in full.

**f75L capture.** `tools/iiif_lines.py --ark btv1b9059865k --canvas 75 --region 100,100,3800,5450 --debug`:
one native fetch (7933x5650 canvas, left-leaf region), 33 line-bands cut into 66 crops (`images/f75L_L01..L33_s{1,2}.jpg`),
debug overlay checked (`images/f75L_lines_debug.jpg`) -- line detection tracks the visible rows well aside from
the top ~350px margin (faint bleed-through from the facing page, see below). Content: a dense invented-sign
nomenclator block (~28 real lines), a plain closing formula with the date ("...Decembre 15..."), a second,
shorter cipher paragraph (postscript, same pattern as fr2933-salviati-1525's f57v), then the valediction and
signature. Numerals (12, 100, 30, etc.) appear inline within the cipher rows, consistent with the brief's
"~60 invented signs plus numerals".

**f75R checked and excluded.** Native-resolution capture of the facing right leaf (same region method) showed
continuous plain French cursive prose throughout, no invented signs anywhere -- corrected from the 500px
survey's read of "mixed prose+cipher" (a resolution artefact: what looked like a cipher paragraph at 500px is
ordinary secretary-hand cursive at native res). Its crops and native source were deleted after confirmation
(common-rules "natives of cipher pages only"); the 500px survey copy (`images/survey/f75.jpg`, covers both
leaves of the canvas 75 opening) is kept as the record.

**Glyph atlas.** `tools/glyph_atlas.py segment` on f75L's native source: 1177 sign boxes, 1143 "marks" (mostly
binding-gutter shadow and faint bleed-through noise picked up by the height threshold, not genuine diacritics
-- unlike fr2933-salviati-1525, no clean recurring superscript-mark shapes were found on this page, so every
mark cluster is labelled `_` in `glyphs/labels.json`). `cluster --k 50 --k-marks 14` then hand-labelled from
the contact sheets (`glyphs/sheet_signs_00/01/02.png`, `glyphs/sheet_marks.png`): **21 sign codes** covering
515 of 1177 boxes (`glyphs/atlas.tsv`, `glyphs/atlas.png`); the rest (662) are noise/junk clusters (binding-gutter
texture, dust specks, the faint top-margin bleed-through) labelled `_`. Weak codes by construction (mixed
clusters, kept anyway per the "over-split, don't force" rule): circ, hook2, hookS, hook7, loopMN. `classify`
against this atlas: 1177 boxes, 455 given a real code, kNN vote matched the box's own cluster label for 997/1177;
108 line-strip images written to `images/strips/` for the box-keyed passes.

**Scale note.** One page (f75L) alone segments to 1177 boxes across 44 script-detected line-bands (finer than
the 33 bands used for line-crop cutting) -- far more than this worker's $8 cap can box-key-pass end to end (the
fr2933-salviati precedent spent a full separate worker's cap on 505 boxes of one comparable page). **Scoped down
to one line (line 9, 28 boxes, y~1010-1103 of the crop, well into the dense cipher block) for a complete
demonstration of the method**; the rest of f75L's box list and strips are captured and classified, ready for a
future pass, but not yet box-keyed.

**Box-keyed pass, f75L line 9.** Pass A (worker K, `passA.tsv`): read every box from `images/strips/f75L_L09{a,b,c}.jpg`
against `glyphs/atlas.tsv`, confirming or correcting the classifier's code. One correction (box 16: `inf`, not
the classifier's weak-share `hash`); one shape not matched by any atlas code (box 27, a distinct "W" double-loop,
flagged `W?` -- a candidate 22nd sign for a future atlas revision). Pass B: one blind Sonnet subagent, same
strips and atlas, no access to passA.tsv (`passB.tsv`). Pass B's own notes flag the root cause of most
disagreement before reconciliation was even run: line 9 crosses the binding-gutter shadow (positions 1-5,
9, 19-22) and three box pairs overlap the same mark (3/4, 21/22, 23/24) -- known segmentation weaknesses on
this page, not a difference in what the two readers saw.

`tools/reconcile_passes.py passA.tsv passB.tsv --rows`: **line 9, 15/29 aligned columns = 51.7% agreement**
(`disagreements.tsv`, `ciphertext_draft.tsv`, `agreement.tsv`). 22 of 29 draft positions are grade M. **Gate
(>=80%) failed.** Per the fr2933-salviati-1525 precedent when its gate failed: stopped here, no hand-settling
from the image, no `ciphertext_f75L.tsv` -- `disagreements.tsv`/`ciphertext_draft.tsv`/`agreement.tsv` are
diagnostic only, not a reading. Both passes independently called positions 12 (`plus`), 13 (`tcross`) and 18
(`hash`) with H confidence -- the three most visually distinctive shapes on the line -- and agreed on 9 of the
14 pure-noise (`_`) calls; every other position disagrees. Pass B, reading blind, converged on two of pass A's
own uncertain flags: position 27 (pass A's unmatched "W" shape) as `loopMN?`, and position 16 as a real sign
(disagreeing on which one, `b8?` vs pass A's `inf`).

**Types, grades (line 9 only, 28 positions):** 0 H-from-key (no key exists to test against), 0 C, 3 S (both
passes agreed independently: `plus`, `tcross`, `hash`, positions 12/13/18), 9 S-weak (both passes agreed the
position is blank/noise), 16 M (disagreement, unsettled). No I. No decoding attempted.

**Why the gate failed, and what would fix it:** this page's atlas (21 codes, built and labelled by one worker
in one pass) is far less mature than fr2933-salviati-1525's after its own dedicated worker session, and the
segmenter's box list for this line specifically crosses the gutter shadow and double-boxes three marks --
before a next pass, re-run `glyph_atlas.py segment` with the region's left margin trimmed a bit further (the
gutter starts around x=0-200 of this region) to drop the shadow boxes, and re-split or merge the atlas clusters
that the confusion here implicates (`hook7`/`circ`, `inf`/`b8`, `bar` vs `_` at low contrast).

**Scope not attempted this session (cap reached):** the rest of f75L (lines 1-8, 10-44, already segmented and
classified, strips on disk) and every page of the other enciphered item (43/44 pair: f81R, f82L, f82R, f83L,
f83R, at 500px survey level only, no native capture). item 39/42 (apparently plain) not re-checked at native
resolution. The codicological ordering question (f75L's ending vs f75R's un-docketed plain opening) is
unresolved. Suggested next step: a worker with a larger cap either (a) re-runs the atlas with a trimmed region
and works through f75L's remaining lines against the existing classified box list, or (b) captures item
43/44's native pages fresh (longer cipher run, per the 500px survey the cleanest full-page cipher blocks of
the six) and builds a second atlas, merging codes with this one where they visibly match.

**Requests this session:** gallica.bnf.fr 24 (1 manifest.json fetch + 2 reachability-test attempts, one reset
and retried once per playbook + 19 page-image fetches [17 survey at 500px, 2 with one reset each retried once
= 19 attempts for 17 successes, plus the 2 native-region fetches for f75L/f75R] -- all UA `cipher-lab research
script (contact via repository)`, >=1.5s apart, no 403/429/challenge seen, only transient connection resets).
No other hosts. Subagents: 1 (Sonnet, blind pass B on line 9 only). Folder size 16 MB (images/ + glyphs/,
after removing glyphs/crops/f75L.png, a reproducible grey-normalised full-page intermediate not needed by any
committed file).

## Re-segmentation and passes f75L (24 Sept 2026, LANE R4 O)

Worker O (Sonnet, cap $8), brief `.claude/briefs/runs/2026-09-24-lane-r4-o-seure-segment.md`, following worker
K's gate failure above (51.7% on line 9, root-caused to gutter/bleed-through noise and under-merged boxes). No
solving, no fetches (disk-first; the native source `images/src_ark_12148_btv1b9059865k_f75_100_100_3800_5450.jpg`
K already captured was reused, 0 new gallica.bnf.fr requests).

**Segmenter fix (`tools/glyph_atlas.py`, offline test `tools/tests/test_glyph_atlas.py` extended, both commits
before this one).** Two changes, both exposed as options rather than hardcoded, per rule 8:
1. `--min-area` (was a hardcoded `0.12 x median height`, now a CLI float) so a noisy page can raise its minimum
   component size.
2. `--merge-vgap` (new, default 0.6x median height): the same-line merge step only checked x-overlap, never a
   vertical gap, and could chain a whole column of unrelated dust specks (a line's "nearest peak" assignment
   has no distance cap) into one giant box. On this page it produced two boxes 993px and 1084px tall (23-25x
   the median sign height) in the blank margin below the cipher block, both empty paper with a scan-edge line
   at the bottom, not signs. Root cause and fix confirmed by cropping both boxes from the source image (blank).
   The new test constructs exactly this case (one real sign sets the median height, two dust specks with the
   same x-range but 500px apart vertically, same "line") and asserts they no longer merge into one box.

**Re-segmentation.** Cropped the gutter and top bleed-through by cropping the existing native source in place
(`--page f75L=<source>@420,350,3800,5450`, no new fetch: the region syntax already supported in the tool covers
this, so no new crop option was needed) -- column-mean intensity confirmed the gutter shadow spans x=50-375 of
the original capture (mean 86-136 vs ~200 background) and row-mean confirmed the bleed-through band is y=0-70
(mean 112-165 vs ~200); 420/350 gives margin on both. Result: 1033 signs + 177 marks (was 1178 signs + 1144
marks). Noise, measured the way K's gate quoted it (unlabelled `_` share of signs.tsv only, marks excluded):
**94/1033 = 9.1%**, against the brief's <20% target and K's 662/1177 = 56.2% baseline -- both the crop and the
merge-vgap fix contributed (the crop alone, tested first, gave 1014 signs but still had the two giant boxes;
the vgap fix removed those and re-normalised the count to 1033).

**Atlas.** `cluster --k 50 --k-marks 10` then hand-labelled from the contact sheets (`glyphs/sheet_signs_00/01/02.png`,
`glyphs/sheet_marks.png`): 27 sign codes (all 21 of K's codes reused by shape where a cluster matched, plus
`hash2`, `num1`, `signR`, `signA`, `signN`, `hookJ`, `wedge`, and **`W`** -- the double-loop shape K flagged from
line 9 position 27 as an unmatched 22nd sign candidate, confirmed here as its own cluster (9 boxes) rather than
scattered noise. `z3` and `apos` from K's atlas found no matching cluster this pass and are dropped (their few
exemplars now fall inside `hookL`/`chook`). All 10 mark clusters stayed noise (`_`), same finding as K's: no
clean recurring diacritic shape on this page. `classify`: 1033 boxes, kNN vote matched the box's own cluster
label for 816/1033 (79.0%, comparable to K's 997/1177 = 84.7%); strips written to `images/strips/` (42 lines,
83 strip images, replacing K's 108 line-9-only strips).

**Gate test, three lines (9, 5, 15; 63 boxes).** Pass A (worker O, `passA.tsv`): read every box against
`glyphs/atlas.tsv`, noting agreement or a correction with a `?` where the classifier's call looked wrong on the
image. Pass B: one blind Sonnet subagent (images and atlas only, explicitly told not to open passA), writing
`passB.tsv` line by line. `tools/reconcile_passes.py passA.tsv passB.tsv --rows`: **25/65 aligned columns =
38.5% overall** (line 9: 7/21 = 33.3%; line 5: 9/22 = 40.9%; line 15: 9/22 = 40.9%) -- `disagreements.tsv`,
`ciphertext_draft.tsv`, `agreement.tsv`. **Gate (>=80%) failed, worse than K's single-line 51.7%.**

**Why the gate failed despite the segmentation fix, and what that separates out:** the two problems are
different. Segmentation (does a box correctly bound one sign) is now good -- 9.1% noise, clean boxes on
inspection. Sign *identification* (which of the atlas's codes a box is) is not: even the clearest single case,
line 9 position 14 (the new `W` double-loop, called `W` at H confidence by pass A specifically because it
looked unambiguous), was read `loopMN` by pass B -- both are plausible readings of a faint looping shape, and
this atlas has several codes for looping/hooking shapes (`loopMN`, `W`, `hookL`, `hookS`, `hookJ`, `hook`,
`hook2`, `hook7`, `chook`) that a k=50 over-split clustering does not obviously separate on a low-contrast
image. Pass B's own tally (7 H / 56 M of 63) says the same thing independently: most positions on this page
are not confidently classifiable into one atlas code from the image alone, whoever is reading. Per the
fr2933-salviati-1525 and K-line-9 precedent when a gate fails: stopped here, no hand-settling from the image,
no `ciphertext_f75L.tsv`. `disagreements.tsv`/`ciphertext_draft.tsv`/`agreement.tsv` are diagnostic only.

**Types, grades (3 lines, 63 positions, from `agreement.tsv`/`disagreements.tsv`):** 0 H-from-key (no key
exists), 0 C, 25 S (both passes independently agreed, most at M confidence on at least one side), 38 M
(disagreement, unsettled). No I. No decoding attempted.

**What would move this, for a future pass:** not more segmentation work (already under the noise target) --
either (a) a smaller, coarser atlas (merge the hook/loop family down from 9 codes to 2-3 broad shape buckets a
reader can actually tell apart on this image, accepting less precision per sign, and re-run the gate), or (b) a
better image (the Gallica capture is native-resolution but still low-contrast for pencil-thin ink; a different
light/exposure capture of the same leaf, if the holding library offers one, would help more than any further
software tuning). Recommending (a) first since it costs no new fetch.

**Scope not attempted (gate failed, stopped per brief step 2):** lines 1-4, 6-8, 10-14, 16-44 of f75L (already
segmented, classified and stripped, ready for a future pass); the 43/44 pair (still 500px survey only, no
native capture); no ciphertext file for any line.

**Requests this session:** no fetches (disk-first; native source already on disk from worker K). Subagents: 1
(Sonnet, blind pass B on 3 lines, 63 boxes). Folder size 17 MB (images/ + glyphs/, after removing
`glyphs/crops/f75L.png`, the same reproducible full-page intermediate K's note flags; superseded the whole of
K's `glyphs/` and `images/strips/` with this pass's re-segmentation rather than keeping both, to stay under the
30 MB/folder budget -- K's per-line-9 box IDs and codes are preserved above in this file's own text, not lost).

## Coarse buckets and gate (24 Sept 2026, LANE R5 C)

Worker C (Sonnet, cap $5), brief `.claude/briefs/runs/2026-09-24-lane-r5-c-seure-buckets.md`, following worker
O's gate failure above (38.5% on lines 9/5/15, root-caused to nine easily-confused hook/loop codes: `loopMN`,
`W`, `hookL`, `hookS`, `hookJ`, `hook`, `hook2`, `hook7`, `chook`). No solving, no fetches (disk-first; O's
native source and page config reused, 0 new gallica.bnf.fr requests).

**Merge.** `glyphs/buckets.tsv` maps the nine codes to three shape buckets defined by one feature a reader can
actually see on a strip at this ink density: does the pen close into a loop, stay open with no descender, or
stay open but drop a tail below the line.
- `loop` (was `W`, `loopMN`, `hook2`) -- the pen visibly closes into one or more full loops (a double-hump
  cursive w, a repeated wave of small loops, or a closed P-shape).
- `hook` (was `chook`, `hook`, `hookS`) -- a simple open curve or hook, no closure, no tail below the line.
- `hookdesc` (was `hook7`, `hookJ`, `hookL`) -- an open hook (7-shaped, J-shaped, or a tall hook-topped
  stroke) whose stroke drops clearly below the line into a descender.

Re-labelled via `glyph_atlas.py atlas`/`classify` (edited `labels.json`'s cluster->code map, not the
segmenter): **21 codes (was 27)**. kNN self-match on reclassification: 818/1033 = 79.2% (was 816/1033 = 79.0%
before the merge) -- unchanged within noise, as expected for a relabelling that does not touch segmentation.
Commit 74c5623.

**Free check: old passA/passB (worker O's fine-grained pass, 38.5%) mapped through `buckets.tsv`.** Every
sign in `passA.tsv`/`passB.tsv` with one of the nine old codes was rewritten to its bucket name (trailing `?`
kept) and re-reconciled with no new reading: **27/65 = 41.5%** (up from 38.5%, `reconcile_passes.py` run
against the remapped copies, not committed -- a scratch check, not a new pass). The merge recovers some
agreement even on the old, finer-grained reads, but nowhere near the 80% gate.

**Fresh gate, coarse atlas, same three lines (9, 5, 15; 63 boxes).** Pass A (worker C, `passA_coarse.tsv`):
read every box directly from `glyphs/atlas.png`/`atlas.tsv` and the line strips, independent of the old
fine-grained passes. Pass B: one blind Sonnet subagent (`passB_coarse.tsv`), given only the strip images,
`glyphs/atlas.tsv`/`atlas.png`/`buckets.tsv`, explicitly told not to open `passA_coarse.tsv`, any
`disagreement`/`ciphertext_draft`/`agreement` file, or this NOTES.md. `tools/reconcile_passes.py
passA_coarse.tsv passB_coarse.tsv --rows`: **27/63 = 42.9% overall** (line 9: 8/21 = 38.1%; line 5: 11/21 =
52.4%; line 15: 8/21 = 38.1%) -- `disagreements.tsv`, `ciphertext_draft.tsv`, `agreement.tsv` (overwriting
worker O's fine-grained-gate versions of the same three diagnostic files, per the K->O precedent of
superseding rather than keeping both; the fine-grained numbers stay on the record in this file's text above).
**Gate (>=80%) failed**, marginally better than the fine-grained 38.5% and than the free-check 41.5%, but not
close to the target, and worse than worker K's original single-line 51.7%.

**Grades (3 lines, 63 positions, from `ciphertext_draft.tsv`):** 0 H-from-key (no key exists), 0 C, 13 S (both
passes independently agreed at H confidence -- all 13 are real signs, none a noise/`_` agreement, unlike the
fine-grained gate's 9 noise agreements out of 25), 50 M (disagreement, or agreed but flagged by a pass). No I.
No decoding attempted. 20 of the 21 coarse codes appear somewhere in the 63-position draft (only `signR` does
not) -- the coarse atlas narrows the confusion only a little; most individual boxes are still not confidently
one code over another from the image alone.

**f75L is not box-keyable at this image quality even with coarse buckets (42.9%); needs a different capture or
a key.**

No hand-settling from the image either way, per the brief. Scope not attempted: lines other than 9, 5, 15 (already
segmented/classified/stripped from worker O's pass, ready for a future pass if a better image or a key changes
the calculus); no ciphertext file for any line.

**Requests this session:** no fetches (disk-first; native source and page region already on disk from workers
K/O). Subagents: 1 (Sonnet, blind pass B on the same 3 lines, 63 boxes, general-purpose agent, model override
sonnet). Folder size unchanged from worker O's pass (no new images).
