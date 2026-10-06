partial
Status revised 4 Oct 2026 ~19:0x UTC (account-3 orchestrator): found-solved (SEURE-WEB) withdrawn. SEURE-DEC pinned fos 84-87 by eye and found no interlinear, marginal or separate decipher; the sentence Potter 2014 prints as deciphered is clear text on fo. 85r l.1-5, so his "in cipher, with decipher" does not show a printed decipherment of the cipher passages. Open question: whether Serrao 1969 (Arq. Centro Cultural Port. 1, 455-458) or Falgairolle 1896 prints them (LOCAL-QUEUE L53).
Potter, A Knight of Malta at the Court of Elizabeth I (Camden 5th ser. 45, 2014), introduction footnotes on de Seure's Lisbon despatches, read by this worker (Cambridge Core PDF + Google Books snippet QtbeBgAAQBAJ): fr. 3151 fo. 84-87 is cited 'in cipher, with decipher' and a deciphered sentence is printed (SEURE-WEB section below).


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

## Status set to blocked (24 Sept 2026, 19:35 UTC, LANE R5 orchestrator)

After LANE R5 C's coarse-bucket gate (42.9%, lines 9/5/15 at 38.1/52.4/38.1%, nine loop/hook codes merged to three), f75L is not
box-keyable at this image quality. Status `blocked`: it needs a different capture (a higher-contrast or multispectral image from
BnF) or a key of Seure's 1558 embassy. No reconciler was spawned, per the lane brief.

## GAPS102-fr3151-seure-1558 (3 Oct 2026, account-4)

Worker GAPS102 (Opus 5.5, cap USD 9), brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, row from
NEXT-STEPS.tsv (worker K's 24 Sept "suggested next step": (a) re-atlas f75L and work through its remaining lines, or
(b) capture items 43/44 natively). Intake gate: `fr3151-seure-1558: blocked (line 1) -- already terminal, nothing to
gate`, exit 0. No other account's claim or commit on this folder in the 6 h before 12:03 UTC.

**Step (a) is not current and was not run.** Its first half (trimmed-region re-atlas) is what LANE R4 O already did;
its second half (machine box-reads of f75L's remaining lines) is the same instrument that failed its own >=80% gate
three times (K 51.7%, O 38.5%, C 42.9%) -- rule 3's third-attempt clause retires it for f75L at this image
[retired: two-reader box-keyed pass on f75L], and TRANSCRIPTION.md / CLAUDE.md Usage 6 send a >10% reader split to
the owner's sign sorter, not to a fourth machine pass.

**Step (b), cheapest unit: do the "duplicate" copies 43 and 44 really carry the same cipher text?** If yes, the two
copies give a reader-independent consistency check on every sign; if 44's clear passages are the plaintext of 43's
cipher, they are known plaintext. Three native region fetches (canvas 83 left-leaf closing, canvas 83 right leaf =
43's cipher postscript, canvas 87 right-leaf lower half = 44's closing and cipher postscript), cut with
`python3 tools/iiif_lines.py --ark btv1b9059865k --canvas {83,87} --region ... --out images/dup --prefix
{f83L_close,f83R_ps,f87R_close} --debug` (crops and overlays in `images/dup/`, manifest `images/dup/manifest.json`).
Read by eye from the debug overlays and two date-line crops (no subagent calls):

| what | item 43 (f83L / f83R) | item 44 (f87R) |
|---|---|---|
| body | fully enciphered, f81R-f83L (one short clear opener on f81R line 1) | mixed: clear prose with cipher blocks (f85R lower, f86L, f87R upper) |
| closing formula | "...ce p[rése]nt a v[ost]re Magesté ... Sire je prie n[ost]re Seigneur donner ... en parfaicte santé treshewreuse et treslongue vie. De Lisbonne le xij(?)ᵉ jour de decembre 1558", signed "de Seure" | same formula, same line breaks in substance; "De Lisbonne le xij(?)ᵉ jour de decembre 1558", signed "de Seure" |
| cipher postscript after the closing | f83R, 19 lines of ~28 signs (~530 signs), signed "Seure" | f87R, 13 lines of ~28 signs (~370 signs), before the signature |
| PS first signs | `f 40 n R 100 B ...` | `# ∆ o n R ∆ * ...` |
| PS last signs | `... R ∆ n 40 13 30 [loop] A ∆ s` | `... 1 . 40 n R ∆ 11 13 30 12` |

Grades: the closing words are read at M (secretary hand, by eye, one reader); the day numeral is M in both copies.

**Result.** The two closings carry the same plain formula and (at M) the same date, consistent with the docket's
"Autre lettre" and with Bourdeau's duplicate note. But the two cipher postscripts are **not sign-identical**: their
lengths differ by about 40% (~530 vs ~370 signs) and neither the opening nor the closing run matches; they share
recurring groups (`40 n R`, `n R ∆`, `13 30`), which is what one key on related text gives, not what a copy of one
ciphertext gives. So "duplicate" is not confirmed at the cipher level: 43 and 44 are at best the same dispatch
enciphered differently (43 throughout, 44 in part), and the cross-copy sign check cannot be run as a straight
position-by-position diff. Rule 3 note: no control is needed for this observation (a length and run comparison, no
solver), and no negative is claimed about the key. Not found: any position-aligned identity between the two PSs;
any key or decipherment on these leaves.

**Image side note.** f83R's signs are well spaced and the line overlay tracks them cleanly, but measured contrast
(60th-percentile background minus 2nd-percentile ink, same method on all three) is f75L 91, f83R 101, f87R 85: no
large quality gain over the leaf that blocked the target, so the "different capture" blocker is not lifted by
item 43's own leaves on this evidence.

Requests: gallica.bnf.fr 3 (IIIF native regions, descriptive UA, >=1.5 s apart, no error). Vision: 0 subagent
calls; worker's own reads of 3 overlays + 2 date crops + 4 500px survey views already on disk. Folder 24 MB.

## SEURE-KP: item 44's clear opening as known plaintext for item 43's cipher (3 Oct 2026, account 2)

Worker SEURE-KP (LANE-A2PUSH3, account 2, Opus 5.5, cap USD 6, box 14:38-15:23 UTC), brief
`.claude/briefs/runs/2026-10-03-acct2-seure-kp.md`. Intake gate, pasted: `fr3151-seure-1558: blocked (line 1) --
already terminal, nothing to gate`, exit 0. Pre-registration `kp/PREREG.md` (5c5c30b3; amendment A1 d5ccb88d before
any read, A2 acabc850 after the reads and before any score; all three were committed before the score they govern).

**Crops** (one native region each, gallica.bnf.fr 2 requests, descriptive UA, no error):
`python3 tools/iiif_lines.py --ark btv1b9059865k --canvas 85 --region 4100,200,3500,2300 --out images/kp --prefix f85R_clear --debug`
(23 lines) and `python3 tools/iiif_lines.py --ark btv1b9059865k --canvas 81 --region 4100,200,3500,4500 --out images/kp --prefix f81R --debug`
(39 lines). Overlays checked. Only the crops used are committed (f85R L01-08, f81R L01-20); the native sources are
gitignored and can be fetched again from `images/kp/manifest.json`.

**Reads** (one Opus subagent call each, line crops only): `kp/f85R_clear_read.tsv` covers f85R L01-08 in clear,
about 407 letters from "(que je donnay ..." (self-rated confidence 0.6). `kp/f81R_cipher_read.tsv` covers f81R
L01-20 in cipher, 461 signs and about 80 distinct labels in the first 407 (self-rated 0.55). There was one reader
per side and no reconciliation unit was run (A2). **Observation (M):** the clear opener on f81R line 1, "Sire, Je
vous escrivis par mes dernieres ... doctobre", matches f85R line 1 word for word, including the October date. Both
letters are answers to the same earlier dispatch, so the start anchor of the span hypothesis has a basis. f85R
continues in clear with "(que je donnay a ung courrier portugais nomme Anthoine Galuan) le {decez} de la Royne
Marie ... la flotte quilz attendoient du {peru} ... don {Aluaro} de bassan ... arrivee a Seville". The words in
braces are uncertain (M).

**Test** (`kp/kp_test.py P.txt f81R_cipher_read.tsv result.json --draws 200 --ctl-seeds 3 --ctl-draws 30`). The
script imports `tools/interlinear_align.run_align` in `--code-prefix` mode (each sign takes 0 or 1 letters) with
the default null cost. S is the share of code tokens whose status is `agrees`; S* is the maximum over cipher
spans r = 0.70, 0.85 and 1.00 signs per plain letter. The control ran first.

| run | S* | null p95 / max (shuffled gloss) | null p95 / max (rotated gloss) | pass |
|---|---|---|---|---|
| control, P enciphered homophonically, K=80, 0% error (3 keys) | 0.993-0.995 | 0.266-0.287 / 0.280-0.297 (30 draws each) | -- | 3/3 |
| control, 15% sign error | 0.830-0.850 | 0.270-0.284 / 0.273-0.285 | -- | 3/3 |
| control, 40% sign error | 0.568-0.609 | 0.263-0.277 / 0.265-0.295 | -- | 3/3 |
| **target**, f85R P (407 letters) vs f81R C (461 signs) | **0.239** (S_r 0.239 / 0.225 / 0.226) | 0.257 / 0.272 (mean 0.235, 200 draws) | 0.253 / 0.270 (mean 0.234, 200 draws) | **no** |

**Result: gate FAIL.** The target's consistency equals the null mean, and its alignment is no better than a gloss
whose letters are shuffled or rotated. The matched control clears its nulls by a wide margin at 0%, 15% and 40%
sign error. This is therefore a real test of the stated model at this N and at reader errors up to about 40%.
No key fragment was drafted, and key.tsv, decode.json and decode_key.py were not run (the gate governs them).

**What the negative is conditional on** (it is not a design-family negative):
(1) the span hypothesis: 43's cipher after the opener enciphers the same words as 44's clear text, in the same
order. The two letters could share only the opener, with 44 abridging or reordering the body.
(2) the alignment model: one sign takes at most one letter. The control enciphered letters only. A nomenclator
with word or syllable codes, or with nulls at a density that shifts the sign:letter ratio outside 0.70-1.00, is
not covered. This folder's f75L and the GAPS102 postscripts show numerals 12-100 and recurring groups (`40 n R`)
inline, which is consistent with a nomenclator. The control could not fail on that axis, so this test does not
exclude it.
(3) the two single-reader reads (unreconciled).
Rule 3's third-attempt clause does not apply: this is the first attempt with this instrument.

Not found: any alignment of f85R's clear prose to f81R's cipher above the shuffled or rotated null. Reads: 461 cipher
signs + 407 clear letters in two Opus calls. Cost per 100 signs comes from the orchestrator's get_session, which this
worker cannot read.

## Remaining gaps (SEURE-KP, 3 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); 63 positions of f75L lines 5/9/15 two-reader drafted at 42.9% agreement, diagnostic only; f81R L01-20 (461 signs) and f85R L01-08 clear (407 letters) single-reader reads in kp/, diagnostic only.
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%, NOTES sections above), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, f85R-f87R) - blocker: not-attempted; letter-substitution known-plaintext alignment of f85R clear L01-08 vs f81R L01-20 FAILed its gate (S* 0.239 vs shuffled null p95 0.257, control 3/3 at 40% error; SEURE-KP section), conditional on span and one-sign-one-letter; next: same pair with word/name codes allowed (interlinear_align numeral floor for the 12-100 numerals, --max-chunk/--len-prior) plus a matched nomenclator control, and a second reader of f81R L01-10, ~$4
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located (six-source log above; Bourdeau: known keys not tried)

## Escalation (SEURE-KP, 3 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102): not sign-identical; f81R/f85R openers identical in clear (SEURE-KP)
- [ ] clear-pages: 44's clear opening vs 43's cipher, letter-substitution model FAILed with control (SEURE-KP); nomenclator-model alignment untried
- [ ] known-keys: no Henri II-era French key (Tomokiyo's Henri II pages, Lasry GL) tried on Seure yet
- [n/a] print: Ribier and Francisque-Michel read in full, neither prints these letters
- [n/a] key-rebuild: no decipherment, key sheet or deciphered copy found to rebuild from
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85, no material quality gain on item 43's leaves
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 1 internal gaps; cheapest next: 44-clear vs 43-cipher alignment with word/name codes allowed plus matched nomenclator control and a second f81R reader, ~$4

## N8-SEU: nomenclator-model alignment, matched control, second f81R reader (4 Oct 2026, account 2)

Worker N8-SEU (LANE-NEAR8, account 2, Opus 5.5; reader subagent Sonnet), brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave1.md`.
Same pair as SEURE-KP (f85R clear L01-08, 407 letters, vs f81R cipher L01-20), different alignment model, so this is not
a re-tuning of the letter model (rule 3 third-attempt clause not engaged). Pre-registration `kp/PREREG-N8.md`, pushed
7e3ff54c after reader B returned and before err_2reader or any score. Script `kp/nom_test.py` (imports
`tools/interlinear_align.run_align`, `--code-prefix @` + `--word-code-prefix %`: numerals >= 12 are word/name codes taking
0..8 letters, every other sign 0-1 letter; default null cost). `python3 kp/nom_test.py P.txt f81R_cipher_read.tsv
f81R_cipher_readB.tsv result_n8.json --err 0,0.242,0.484 --nulls 0,0.10 --ctl-seeds 3 --ctl-draws 20 --draws 200`;
log `kp/nom_run.log`, numbers `kp/result_n8.json`.

**Second reader.** One blind Sonnet call on the existing `images/kp/f81R_L01..L20` crops (no access to reader A):
`kp/f81R_cipher_readB.tsv`, 451 signs, 95 labels, self-rated 0.35 (legend `kp/f81R_cipher_readB_legend.txt`).
`kp/err2.py` (method in PREREG-N8): **err_2reader = 0.484** after a greedy 1:1 mapping of ad-hoc labels (11 pairs),
0.631 by label identity alone (`kp/err2.json`). Numerals >= 12: 11 in A (2.4%), 13 in B.

**Matched nomenclator control (ran first).** P enciphered with numeral word codes 12-100 on its most frequent words to
A's 2.4% code share, letters homophonic over K = 72, at null share 0% / 10% and injected sign error 0 / e2/2 / e2;
3 keys x 20 shuffled-gloss draws per cell.

| control cell | S* per key | pass (S* > own null p95 and max) |
|---|---|---|
| 0% nulls, 0 error | 0.992 / 0.995 / 0.995 | 3/3 |
| 0% nulls, 0.242 error | 0.266 / 0.438 / 0.752 | 2/3 |
| 0% nulls, 0.484 error (= e2) | 0.228 / 0.271 / 0.258 | **0/3** |
| 10% nulls, 0 / 0.242 / 0.484 error | 0.246-0.263 / 0.237-0.280 / 0.229-0.256 | **0/3 at every level** |

**Target vs nulls (200 draws each).**

| reader | S* (S_r at r = 0.85 / 1.00 / 1.13) | shuffled null mean / p95 / max | rotated null mean / p95 / max | gate |
|---|---|---|---|---|
| A (Opus, SEURE-KP) | 0.226 (0.197 / 0.226 / 0.224) | 0.234 / 0.254 / 0.266 | 0.234 / 0.252 / 0.269 | no |
| B (Sonnet, this job) | 0.228 (0.228 / 0.189 / 0.224) | 0.217 / 0.238 / 0.257 | 0.222 / 0.248 / 0.254 | no |

**Result: non-test at this reader error (PREREG-N8 power condition), not a negative.** Neither reader's alignment beats
its nulls (A sits below its null mean; B 0.228 vs p95 0.238), but the design-matched control passes 0/3 at the measured
two-reader disagreement (0.484) and only 2/3 at half of it, so the instrument has no power at the reads' own error. The
10%-null arm fails even at 0% error: `run_align` at its default null cost does not recover a cipher with interspersed
nulls at this N, so null-bearing designs are untested by this tool here (an instrument limit, not a target finding).
**Bearing on SEURE-KP (3 Oct):** its letter-model control was bracketed at 40% error, below the 48.4% now measured between
two readers of the same crops; under rule 3's SALV-DIAG paragraph its FAIL is drawn from an error band the reads cannot
back up and is better read as a non-test too (its own section is left as written; flagged here for the lane).
No key fragment drafted; key.tsv / decode --check not run (the gate governs them). Not found: any alignment of f85R's
clear prose to f81R's cipher above the shuffled or rotated null under either model or either reader. Vision: 1 Sonnet
subagent call (40 half-line crops, one leaf); 0 network requests.
Suggestion (one line, not done): lower the f81R reader error first (the owner's sign sorter on f81R tiles, or a
reconciliation pass with the two reads), then re-run `kp/nom_test.py` unchanged; separately, a null-tolerant aligner
setting (null cost ~-1) needs its own 10%-null control before any target run.

## Remaining gaps (N8-SEU, 4 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); 63 positions of f75L lines 5/9/15 two-reader drafted at 42.9% agreement, diagnostic only; f81R L01-20 read twice (A 461 signs, B 451 signs, err_2reader 0.484) and f85R L01-08 clear (407 letters) in kp/, diagnostic only.
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%, NOTES sections above), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, f85R-f87R) - blocker: not-attempted; known-plaintext alignment of f85R clear vs f81R cipher is a non-test at the reads' measured error (letter model SEURE-KP, nomenclator model N8-SEU: matched control 0/3 at err_2reader 0.484, kp/result_n8.json); next: reconcile readers A and B on the f81R crops (or a sign-sorter pass on f81R tiles) to bring err below ~0.24 where the control passes 2/3, then re-run kp/nom_test.py unchanged, ~$3
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located (six-source log above; Bourdeau: known keys not tried)

## Escalation (N8-SEU, 4 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102): not sign-identical; f81R/f85R openers identical in clear (SEURE-KP)
- [ ] clear-pages: 44's clear opening vs 43's cipher tried under the letter model (SEURE-KP) and the nomenclator model (N8-SEU); both non-tests at err_2reader 0.484; needs a lower-error f81R read
- [ ] known-keys: no Henri II-era French key (Tomokiyo's Henri II pages, Lasry GL) tried on Seure yet
- [n/a] print: Ribier and Francisque-Michel read in full, neither prints these letters
- [n/a] key-rebuild: no decipherment, key sheet or deciphered copy found to rebuild from
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85, no material quality gain on item 43's leaves
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 1 internal gaps; cheapest next: reconcile f81R readers A/B (or sorter pass) to err < ~0.24, then re-run kp/nom_test.py unchanged, ~$3

## Web and blog check (SEURE-WEB, account 3, 4 Oct 2026, 18:16-18:2x UTC by date -u)

Brief `.claude/briefs/runs/2026-10-04-acct3-seure-web.md`. Per .claude/briefs/check-solved.md "Open web and blog comment
threads". Every query and hit:

(a) Plain web searches (WebSearch, 4 Oct 2026):
1. `chevalier de Seure Lisbonne 1558 lettres Henri II de Fresne chiffre` -- hits: Biblissima record for BnF Français 3151;
   **Potter (ed.), *A Knight of Malta at the Court of Elizabeth I: the correspondence of Michel de Seure, French ambassador,
   1560-1561*, Camden Fifth Series 45 (Cambridge, 2014)**, introduction PDF on Cambridge Core; CiNii/MIT bookstore records
   of the same; Cambridge "Appendix III: the subsequent career of Michel de Seure". Opened (below).
2. `"fr. 3151" BnF chiffre OR cipher OR déchiffrement` -- no hit about this item (HistoCrypt Henri IV/Nevers digit cipher,
   ARCSI bulletin; generic pages).
3. `"Anthoine Galuan" OR "Antoine Galvão" courrier portugais Seure 1558` (distinctive clear-text phrase, f85R line 1-2) --
   only the explorer António Galvão (d. 1557); nothing on this letter.
4. `Seure ambassadeur Portugal 1558 lettres chiffrées Henri II Bibliothèque nationale français 3151` (folder title) --
   same Potter/Biblissima hits, plus a Huygens WVO PDF and a Folger record (catalogue entries for Potter 2014).
5. `"oster à vostre enemy" OR "oster a vostre ennemy" Seure` (phrase from Potter's footnote) -- no web hit.
6. `Serrão "Michel de Seure, embaixador francês em Portugal" duas cartas epistolário` -- CSIC *Culture & History* article
   citing Serrão 1969 on Seure's embassy; Potter again. Serrão's article itself not reached.
7. `Falgairolle "chevalier de Seure" ambassadeur de France en Portugal` -- Online Books Page (Falgairolle), Potter, Droz HCL
   article; no online copy of Falgairolle 1896.

(b) Blog site searches (WebSearch with allowed_domains): `Seure 1558 Lisbon cipher Henri II` on scienceblogs.de
(Cipherbrain), cryptiana.blogspot.com, cryptiana.web.fc2.com, ciphermysteries.com -- two hits, neither about Seure (Cipher
Mysteries "Fifteenth century cryptography", 2016; Cipherbrain "A cipher device used by king Henry II", 17 July 2018, about
the Écouen cipher book). `"fr. 3151" OR "français 3151" OR "Seure" cipher` on the same blogs + dbourdeau.github.io,
github.com, de-crypt.org -- only Bourdeau's site and forks of his repository. No comment thread found on any blog
mentioning Seure, fr. 3151 nos. 39-44, or a decipherment. Local mirror sources/cryptiana/ re-grepped (`3151`, `de Seure`,
`chevalier de seure`): only `seurete` false positives in bazeries3.htm and cross-reference rows in keys/IMAGE-QUEUE.tsv.

(c) Hits opened:
- **Potter 2014, introduction** (Cambridge Core PDF, read via WebFetch; curl got an HTML challenge page). Two
  footnotes cite this recueil: "De Seure to Henri II, Lisbon, 12 October 1558, BnF, fr. 3151, fos 84-87, passage in
  cipher on fo. 85r-v" and **"De Seure to Henri II, 12 December 1559 [sic], BnF, fr. 3151, fo. 84-87, in cipher, with
  decipher: 'il seroit aisé d'oster à vostre enemy ce grant soullaigement qu'il a de ce monde de delà, ou pour myeulx
  dire, tout le nerf et tout le moyen qu'il a desormais de maintenir la guerre contre vous.'"** Both checked word for word
  against the Google Books API snippets of the same volume (`QtbeBgAAQBAJ`, queries `"Seure" "3151"` and `"in cipher, with
  decipher" Seure`; key + country=US), so these are not summariser artefacts. The same apparatus says Luis de Matos
  (*Les Portugais en France au XVIe siècle*, Coimbra 1952) did not find de Seure's late-1558 originals in fr. 3151, and that
  they "appeared in" J. V. Serrão, 'Michel de Seure, embaixador francês em Portugal (1557-1559): duas cartas para o seu
  epistolário', *Arquivos do Centro Cultural Português* 1 (1969), 455-458; and that E. Falgairolle, *Le Chevalier de Seure,
  ambassadeur de France en Portugal au XVIe siècle* (Paris, 1896) printed letters from Portugal found at St Petersburg (one
  of 30 Jan 1559, pp. 15-29).
- Falgairolle, *Jean Nicot ... sa correspondance diplomatique inédite* (1897), archive.org `jeannicotambassa00nico`, full
  djvu text grepped for `Seure`, `3151`, `chiffr`, `décembre 1558`: Seure only as Nicot's predecessor; its index says Seure's
  own correspondence was published in *Le chevalier de Seure* (1896). No fr. 3151 letter printed there.
- Falgairolle 1896 itself: archive.org advancedsearch (creator Falgairolle, 7 items, not among them), Gallica SRU (not
  digitised; the SRU did list a different manuscript, btv1b525105423, "Dépêches originales du chevalier DE SEURE et du Sr DE
  NICOT" 1559-1561), Google Books `6P4RYAAACAAJ` NO_PAGES. **Not opened.** Serrão 1969: not opened (no online copy found).
- *Knowledge Exchanges Between Portugal and Europe* (2025, Google Books `DnGLEQAAQBAJ`, snippet only): names "Seure: BNF,
  Français 3151 and 15871. Français 6638 contains copies of the letters held today in Saint Petersburg".

DECODE: local snapshots in sources/decode/ (10 TSVs, latest 2 Oct 2026) grepped for `3151` and `Seure`: no record.
Solver repositories, fresh shallow clones 4 Oct 2026: dbourdeau/cyphersolver (head 3 Oct 2026) README row for catalogue item 10
still reads "Seure's six Lisbon letters (~2,000 signs, homophonic) left open", and `research/gallica_sweep/bnf_candidates.txt`
lists nos. 39-44 as "Lettre, avec chiffre"; no decipherment. aaymeloglu/unsolved-ciphers (head 27 Sept 2026): no hit
(`seure` only as an Old French word in forster-1644 lexicon files).

Requests: WebSearch 9; WebFetch cambridge.org 5 (one 503 on assets.cambridge.org excerpt); curl cambridge.org 1 (HTML
challenge), assets.cambridge.org 1 (connection reset); googleapis.com/books 6; archive.org 3; gallica.bnf.fr SRU 3;
openlibrary.org 1; github.com 2 clones. No 429.

## Premise check (SEURE-WEB, account 3, 4 Oct 2026)

(a) Folder's own mentions: NOTES.md says "no decipherment on the leaves" (Bourdeau, quoted) and "Not found ... any key or
decipherment on these leaves" (GAPS102); SEURE-KP/N8-SEU treated item 44's clear prose as a *possible* plaintext of item 43's
cipher. **Found, against those statements:** Potter 2014 (above) describes fr. 3151 fo. 84-87, the 12 Dec 1558 letter, as
"in cipher, with decipher" and prints a deciphered sentence. Where the decipher sits (interlinear, margin, or item 44's clear
prose being a deciphered copy of item 43) was not seen by this worker; folio 84-87 vs canvas f81-f87 is not pinned (manifest
labels are all NP).
(b) Other solvers' working files: Bourdeau's guiche1551 notes and README (no attempt, no decipherment); Aymeloglu: nothing.
Not found.
(c) Physical neighbours: no new image fetched (brief: no decoding; the decipher's location is the next step). Earlier
workers viewed f72-f88 at 500px and native crops of f81R, f83L/R, f85R, f87R; none reported an interlinear decipher.
Not resolved by this pass.
(d) Recipient's/receiving side: Potter 2014 (the English embassy edition, which surveys the Portugal embassy), Matos 1952,
Serrão 1969 (Portuguese side), Falgairolle 1896. Found: Potter's quoted decipher; Serrão 1969 reportedly prints de Seure's
fr. 3151 late-1558 despatches (not opened).

## Verdict (SEURE-WEB, 4 Oct 2026)

**found-solved**, for the 12 Dec 1558 letter at least: an editor (Potter 2014, Camden 5th ser. 45) cites fr. 3151 fo. 84-87
as "in cipher, with decipher" and prints the deciphered plaintext of one passage; Serrão 1969 is cited as printing de
Seure's late-1558 fr. 3151 despatches. Scope caveat: the 27 Dec letters (items 40/41) are not named in these footnotes, and
this worker has not seen the decipher on the leaves. Who did not know (README): **F0** for the 12 Dec letter -- the specialist
edition links this manuscript to its decipher; the list keeper (Bourdeau's catalogue item 10, "left open"; his notes "no
decipherment on the leaves") and this repository did not. Contribution left to hand on: a correction to Bourdeau's catalogue
item 10 citing Potter 2014. Any key we rebuild from the decipher is `period`, not `ours`; any reading of these letters is N0/N1
territory for a verifier (rule 10), not a novelty. Prior KP/N8 tests stand as written (they tested an alignment, not novelty).
Suggested next steps (one line each, not done): locate the decipher on the leaves (native view of the canvases holding fos
84-87, ~$1); get Serrão 1969 pp. 455-458 and Falgairolle 1896 (LOCAL-QUEUE / owner); check items 40/41 (27 Dec) against the
same decipher's key before any further cryptanalysis.

Intake gate after this pass (pasted, 4 Oct 2026): `python3 tools/intake_gate_check.py fr3151-seure-1558` ->
`fr3151-seure-1558: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

## SEURE-DEC: where is Potter's "decipher"? (account 3, 4 Oct 2026, 18:39-18:5x UTC by date -u)

Brief `.claude/briefs/runs/2026-10-04-acct3-seure-dec.md`. No cryptanalysis, no key rebuild. Gallica 10 requests
(IIIF image API, descriptive UA, >=2 s apart, all HTTP 200): canvases 84-88 whole at 2000 px, top-right corners of
canvases 85/86/87/88 (folio numbers), canvas 86 left-leaf mid cipher block at 1800 px, canvas 86 right-leaf top lines
at 2200 px. Evidence crops kept in `images/dec/` (412 KB).

**Folios pinned by eye** (modern foliation, ink, top right of each right leaf; struck older foliation beside it):
c84R = fo. 83 (blank but for show-through and an endorsement), **c85R = fo. 84** (old 219), **c86R = fo. 85** (no old
number seen), **c87R = fo. 87** (old 221 struck), c88R = fo. 88 (old 22[4?] struck). Each canvas is an opening, so
fo. Nv = canvas N+2 left leaf: 84r c85R, 84v c86L, 85r c86R, 85v c87L, 87r c87R. **The modern foliation skips 86**;
the old foliation runs 219 (84) -> 221 (87) with no gap, so on this evidence fo. 86 is a numbering slip, not a missing
leaf (M: old number on fo. 85 not read). `tools/gallica_folio.py` anchors: 85=84r, 86=85r, 87=87r (not a linear map
at the 85/87 skip).
So Potter's fos 84-87 = item 44 exactly (docket c85L "Autre lettre du dict commandeur de Seure au mesme Roy"; c88L is the
next item's docket, Guise to Henri II).

**What the leaves carry.** fo. 84r: 21 lines clear ("Sire, Je vous escrivis par ma derniere ... d'octobre ... Anthoine
Galuan"), then ~16 lines cipher to the foot; fo. 84v: ~37 lines cipher, then 7 lines clear ("La Royne Marie laissa plus de
quatre cens mille escuz ..."); fo. 85r: ~32 lines clear; fo. 85v: ~17 lines clear; fo. 87r: 4 lines clear ("Diego
Dazevedo gentilhomme Castellan ..."), ~18 lines cipher, 2 lines clear, the closing formula "De Lisbonne le [xij]e de
decembre 1558", ~13 lines cipher postscript, signature. **No interlinear decipher** over any cipher line (the 1800 px
crop of fo. 84v shows lines packed with no writing between them, and no lighter or later hand), **no marginal
decipher** (margins carry only paragraph marks), and no separate decipher sheet among canvases 84-88.

**Potter's quoted sentence is clear text in the original, not a decipher.** fo. 85r lines 1-5 (c86R, crop
`images/dec/c86R_top.jpg`, read by eye at M): "Et par la [?] v[ost]re Ma[jes]te poult assez evidemment congnoistre
combien, suyvant ce que je vous en ay aultresfoys escript, il seroit aisé d'oster a v[ost]re ennemy ce grant
soullaigement qu'il a de ce monde de dela, ou p[our] myeulx dire tout le nerf et tout le moyen qu'il a desormais de
maintenir la guerre contre vous." Same secretary hand as the rest of the letter, written in the line, not over cipher. This
is Potter's printed "decipher" word for word. It follows the cipher block of fo. 84r-v after 7 clear lines, so it is not
even the line that the cipher block ends on.

**Item 44 as a deciphered copy of item 43?** Not on this evidence: 44 is itself a signed original with its own cipher
blocks (fo. 84r-v, 87r) and its own cipher postscript, which GAPS102 found not sign-identical to 43's (~370 vs ~530
signs). Gross structure does track: both open with the same clear "Sire, Je vous escrivis ... d'octobre" line, both close
with the same formula and date, and 43's ~4 pages of continuous cipher (f81R-f83L) are of the order of 44's 5 written
pages of mixed clear and cipher. That fits "the same dispatch sent twice, 43 enciphered throughout, 44 partly in
clear", which is SEURE-KP's span hypothesis. It makes 44's clear passages candidate plaintext for parts of 43. It does
not make 44 a decipher, and it says nothing about what 44's own cipher blocks say.

**Result.** No period decipher is located on fos 84-87 (canvases 85-87) or on the neighbouring canvases 84 and 88. Potter's
"in cipher, with decipher" is best read as "partly in cipher, partly in clear". The sentence he prints is from the clear
part. **FLAG for the orchestrator/verifier:** SEURE-WEB's `found-solved` rests on that phrase. On the leaves, no cipher
passage of fo. 84-87 is shown deciphered anywhere. The status line is left as written; this worker does not set status.
Serrão 1969 and Falgairolle 1896 may still print a decipherment from another witness (the St Petersburg / fr. 6638
copies), so the question stays open until one is opened. Not found: any interlinear, marginal or separate decipher on canvases 84-88;
any old foliation on fo. 85.

## Remaining gaps (SEURE-DEC, 4 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); diagnostic reads only (kp/, f75L); fo. 85r lines 1-5 clear read at M (SEURE-DEC).
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, fo. 84r-v and 87r of item 44) - blocker: not-attempted; no decipher on fos 84-87 (SEURE-DEC: canvases 84-88 viewed, Potter's sentence is clear text on fo. 85r); 44-clear vs 43-cipher alignment a non-test at err_2reader 0.484 (N8-SEU); next: reconcile f81R readers A/B to err < ~0.24 and re-run kp/nom_test.py unchanged, ~$3
- printed decipherment, if any - blocker: not-attempted; Serrão 1969 pp. 455-458 and Falgairolle 1896 not opened, no LOCAL-QUEUE row yet (SEURE-WEB); they may print the letters from the St Petersburg / fr. 6638 copies; next: orchestrator queues a LOCAL-QUEUE row for both, ~$0.3
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located and no decipher on the leaves to rebuild one from

## Escalation (SEURE-DEC, 4 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102); 44 = fos 84-87 pinned (SEURE-DEC)
- [ ] clear-pages: 44's clear text vs 43's cipher, letter and nomenclator models both non-tests at err_2reader 0.484; needs a lower-error f81R read
- [ ] known-keys: no Henri II-era French key (Tomokiyo's Henri II pages, Lasry GL) tried on Seure yet
- [ ] print: Ribier and Francisque-Michel read (no); Serrão 1969 and Falgairolle 1896 not opened (LOCAL-QUEUE)
- [n/a] key-rebuild: no decipherment on fos 84-87 or canvases 84/88 (SEURE-DEC); Potter's "decipher" sentence is clear text on fo. 85r
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85; fos 84-87 viewed at 1800-2200 px for a decipher (SEURE-DEC), none
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 2 internal gaps; cheapest next: reconcile f81R readers A/B to err < ~0.24, then re-run kp/nom_test.py unchanged, ~$3

## RUN6-SEURE: f81R A/B reconciliation pilot (5 Oct 2026, 05:05-05:08 UTC by date -u, account 1)
Worker RUN6-SEURE (LANE-RUN6, Opus 5.5; reconcilers Sonnet), brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave2.md`.
Prereg `kp/PREREG-RUN6.md` pushed 5e763f1f before any call (its header says ~05:10; date -u at commit was 05:05:53).
Scope: per-line A/B err (err2.py method) is 0.26-0.72 on all 20 lines, so full reconciliation = 20 calls x 0.35 + 1 = ~USD 7.4 >
cap 3.5; this job ran a PILOT, lines L04 (A/B 0.538) and L06 (0.480) fixed by rule (first two within +-0.10 of pooled 0.484).
Units: 4 Sonnet calls (2 independent reconcilers x 2 lines, each given the line's two half-crops, A, and B in A's labels) + 1
reconciliation unit (scoring). 0 network requests. Files: `kp/run6_recon.tsv`, `kp/run6_err.py`, `kp/run6_result.json`.

| measure | value |
|---|---|
| err_R (R1 vs R2, pooled L04+L06, 50 signs) | **0.080** (L04 0.08, L06 0.08) vs gate 0.24 -> pilot PASS |
| A/B err on the same two lines (before) | 0.538 / 0.480 |
| reconciled sign source share | AB 0.52, A 0.26, B 0.21, neither 0.01 |
| residual R1/R2 splits | L04: x/1, n1/s7 (one double-scroll sign: A read 2 signs, B 1); L06: s1/bs7, J/I |

Reading: PASS is necessary, not sufficient (registered caveat): both reconcilers saw A and B and took 99% of signs from one of
them, so their agreement is anchoring-inflated and is agreement, not accuracy (TRANSCRIPTION.md). Notably they converged on
B's L04 middle (oe t 3 # ... ca ... oe) and B's L06 opening (5, Z, #) but A's L06 tail (h 7 t/ ... J s2), i.e. a genuine
per-sign choice, not copying one reader. kp/nom_test.py NOT re-run: it needs all 20 lines and 2 reconciled lines cannot feed it
(prereg). Not found: any measure of the reconciled read's true error (no benchmark sheet for this hand).

## Remaining gaps (RUN6-SEURE, 5 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); diagnostic reads only (kp/, f75L); f81R L04/L06 reconciled by two Sonnet reconcilers (err_R 0.08, kp/run6_result.json); fo. 85r lines 1-5 clear read at M (SEURE-DEC).
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, fo. 84r-v and 87r of item 44) - blocker: not-attempted; reconciliation pilot PASSed on L04/L06 (RUN6-SEURE); next: reconcile the other 18 f81R lines (one Sonnet reconciler per line, same prompt as kp/run6_recon.tsv's, plus a second reconciler on 2-3 lines to re-measure err_R), then re-run kp/nom_test.py unchanged with e = the measured err_R, ~$7.5
- printed decipherment, if any - blocker: not-attempted; Serrão 1969 pp. 455-458 and Falgairolle 1896 not opened (SEURE-WEB); next: orchestrator queues a LOCAL-QUEUE row for both, ~$0.3
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located and no decipher on the leaves to rebuild one from

## Escalation (RUN6-SEURE, 5 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102); 44 = fos 84-87 pinned (SEURE-DEC)
- [ ] clear-pages: 44's clear text vs 43's cipher; both models non-tests at err_2reader 0.484; reconciliation pilot err_R 0.08 on 2 lines (RUN6-SEURE); needs the other 18 lines reconciled
- [ ] known-keys: no Henri II-era French key (Tomokiyo's Henri II pages, Lasry GL) tried on Seure yet
- [ ] print: Ribier and Francisque-Michel read (no); Serrão 1969 and Falgairolle 1896 not opened (LOCAL-QUEUE)
- [n/a] key-rebuild: no decipherment on fos 84-87 or canvases 84/88 (SEURE-DEC)
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85; fos 84-87 viewed at 1800-2200 px for a decipher (SEURE-DEC), none
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 2 internal gaps; cheapest next: reconcile f81R L01-03, L05, L07-20 (18 Sonnet calls + 1 unit), re-measure err_R on a sample, re-run kp/nom_test.py unchanged, ~$7.5

## RUN6-SEURE2: all 20 f81R lines reconciled, err_R re-measured, nom_test re-run (5 Oct 2026, 05:21-06:05 UTC by date -u, account 1)
Worker RUN6-SEURE2 (LANE-RUN6, Opus 5.5; reconcilers Sonnet), brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave3.md`.
Prereg `kp/PREREG-RUN6B.md` pushed 3654942e (05:23) before any reconciler call. Units: 36 Sonnet reconciler calls (2 blind
reconcilers x 18 lines, prompt `kp/run6b_prompt.txt`, inputs `kp/run6b_inputs.tsv`, one line's two half-crops per call) + 1 scoring
unit; the pilot's L04/L06 rows carried in. About 95k subagent tokens per call (mostly cached system prompt); the true cost is the
orchestrator's to read. 0 network requests. Files: `kp/run6b_recon.tsv`, `kp/run6b_err.py` (`--check` OK), `kp/f81R_recon_R1.tsv`,
`kp/f81R_recon_R2.tsv`, `kp/run6b_result.json`, `kp/nom_run6b.log`.

| measure | value |
|---|---|
| err_R (R1 vs R2, all 20 lines, 464 max-len signs) | **0.095** (44 edits); per line 0.00-0.24; 4 lines identical (L01, L09, L10, L12) |
| A/B err on the same lines, A's labels, identity | 0.484 (before) |
| reconciled sign source share (both R) | AB 0.559, A 0.267, B 0.169, neither 0.004 (L05 R1's source list is one entry too long, so it is left out of the shares) |
| R1 / R2 length | 461 / 461 signs; word codes (numerals >= 12) in R1: 12 |

Anchoring caveat (registered): both reconcilers saw A and B, and on L09/L10/L12 they returned identical sequences (L10 = reader A
verbatim). So err_R 0.095 is agreement, not accuracy, and is a lower bound on the true error of the reconciled read (TRANSCRIPTION.md).

**nom_test** (`kp/nom_test.py` unchanged; `--err 0,0.047,0.095,0.242 --ctl-seeds 3 --ctl-draws 20 --draws 200`, readers R1, R2):
the process was killed at the 30-minute background-command limit after the controls and R1 had printed, before R2 and before the JSON
was written. `kp/nom_run6b.log` is the record.

| control cell (nomenclator, matched to R1: word share, K) | pass share | S per key |
|---|---|---|
| 0% nulls, err 0 / 0.047 | 3/3 / 3/3 | 0.99 0.99 0.98 / 0.95 0.94 0.95 |
| 0% nulls, err 0.095 (= E) | **2/3** | 0.891 0.906 0.238 |
| 0% nulls, err 0.242 (anchoring bracket) | **2/3** | 0.257 0.248 0.304 (barely above their own nulls) |
| 10% nulls, err 0 / 0.047 / 0.095 / 0.242 | 0/3, 1/3, 0/3, 1/3 | all 0.22-0.28 |

Power condition (prereg): >=2/3 at E AND >=2/3 at 0.242, both met, so the R1 result counts as a test. Weak spot: the 0.242 passes are
by S margins of a few hundredths, and the control falls away entirely with 10% nulls.

| target | S* | shuffled p95 / max | rotated p95 / max | gate |
|---|---|---|---|---|
| R1 (`f81R_recon_R1.tsv`) | 0.230 (S_r 0.205, 0.221, 0.230) | 0.246 / 0.269 | 0.246 / 0.249 | **FAIL** |
| R2 | not run (process killed) | | | |

Reading: R1 sits inside its own null band (null mean 0.226) and fails, with the control showing power down to the 0.242 bracket. That
makes it a negative for the start-anchored H-span under the nomenclator model as `nom_test.py` defines it, conditional on: the
reconciled read (agreement 0.095, true error unmeasured), no null signs (the 10%-null control has no power at any error), and this
one model. It is not a design-family negative, and it is not complete: the prereg licenses the H-span if R1 OR R2 passes, and R2 has
not been scored. No grades changed; 0 tokens read.
Not found: any sign of the f85R clear prefix in the f81R reconciled cipher under this model; a measure of the reconciled read's true
error (no benchmark sheet for this hand).

## Remaining gaps (RUN6-SEURE2, 5 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); f81R L01-L20 reconciled by two Sonnet reconcilers (err_R 0.095 agreement, kp/run6b_result.json); fo. 85r lines 1-5 clear read at M (SEURE-DEC).
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, fo. 84r-v and 87r of item 44) - blocker: not-attempted; f81R fully reconciled and nom_test R1 FAILs with control power at E 0.095 and 0.242 (RUN6-SEURE2, kp/nom_run6b.log), R2 unscored because the run was killed at the 30-min background limit; next: re-run kp/nom_test.py with the same arguments and a background timeout >= 45 min (or R2 alone), write kp/result_run6b.json, ~$0.3
- printed decipherment, if any - blocker: waiting-on LOCAL-QUEUE L53; Serrão 1969 pp. 455-458 and Falgairolle 1896 not opened
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located and no decipher on the leaves to rebuild one from

## Escalation (RUN6-SEURE2, 5 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102); 44 = fos 84-87 pinned (SEURE-DEC)
- [ ] clear-pages: 44's clear text vs 43's cipher under nom_test: R1 FAIL with control power (RUN6-SEURE2); R2 unscored, needs one re-run
- [ ] known-keys: no Henri II-era French key (Tomokiyo's Henri II pages, Lasry GL) tried on Seure yet
- [ ] print: Ribier and Francisque-Michel read (no); Serrão 1969 and Falgairolle 1896 not opened (LOCAL-QUEUE L53)
- [n/a] key-rebuild: no decipherment on fos 84-87 or canvases 84/88 (SEURE-DEC)
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85; fos 84-87 viewed at 1800-2200 px for a decipher (SEURE-DEC), none
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 1 internal gap; cheapest next: re-run kp/nom_test.py (same args) with a >= 45 min background timeout to score R2 and write result_run6b.json, ~$0.3

## D2-SEURE: R2 scored under nom_test (5 Oct 2026, 23:01-23:30 UTC by date -u, account 1, LANE DEFAULT-account-1-20261005-2217)
Re-ran `kp/nom_test.py` unchanged with PREREG-RUN6B.md's registered arguments (`python3 kp/nom_test.py kp/P.txt kp/f81R_recon_R1.tsv
kp/f81R_recon_R2.tsv kp/result_run6b.json --err 0,0.047,0.095,0.242 --ctl-seeds 3 --ctl-draws 20 --draws 200`), in the background with a
60-min timeout; it finished in 26 min (23:03-23:29 UTC). No new thresholds. Log: `kp/nom_run6b_rerun.log`; JSON: `kp/result_run6b.json`.
The script is seeded (`--seed` default 1): the eight control rows and the R1 row are byte-identical to RUN6-SEURE2's `kp/nom_run6b.log`,
so the earlier numbers reproduce. 0 network requests, 0 subagent calls.

| target | S* | S_r (3 rotations) | shuffled mean / p95 / max | rotated mean / p95 / max | gate |
|---|---|---|---|---|---|
| R1 (`f81R_recon_R1.tsv`, 461 signs, 12 word codes) | 0.230 | 0.205, 0.221, 0.230 | 0.226 / 0.246 / 0.269 | 0.226 / 0.246 / 0.249 | **FAIL** |
| R2 (`f81R_recon_R2.tsv`, 461 signs, 12 word codes) | 0.231 | 0.223, 0.231, 0.196 | 0.225 / 0.248 / 0.265 | 0.226 / 0.243 / 0.253 | **FAIL** |

Control (unchanged, matched to R1): 0%-null arm 3/3 at err 0 and 0.047, 2/3 at E 0.095 and 2/3 at the 0.242 bracket, so the prereg's
power condition holds and the result counts as a test; the 10%-null arm reads 0/3-1/3 at every error. Both reconciled reads sit inside
their own null bands (S* within 0.006 of the null mean). The prereg licenses the H-span if R1 OR R2 passes: neither does, so the
start-anchored f85R clear prefix is not found in the f81R cipher under the nomenclator model as `nom_test.py` defines it. Conditional
on: the reconciled reads (agreement 0.095, true error unmeasured; the 0.242 control passes by a few hundredths only), no null signs
(the 10%-null control has no power), this one model and this H-span. Not a design-family negative. No key fragment drafted; key.tsv
and decode --check not run (the gate governs them). No grades changed; 0 tokens read.
Not found: any alignment of the f85R clear prefix to either reconciled f81R read above the shuffled or rotated null.

## Remaining gaps (D2-SEURE, 5 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); f81R L01-L20 reconciled by two Sonnet reconcilers (err_R 0.095 agreement, kp/run6b_result.json); nom_test R1 and R2 both FAIL with control power (kp/result_run6b.json); fo. 85r lines 1-5 clear read at M (SEURE-DEC).
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, fo. 84r-v and 87r of item 44) - blocker: not-attempted; the 44-clear vs 43-cipher alignment under nom_test FAILs for both reconciled reads with control power (D2-SEURE, kp/result_run6b.json), conditional on no null signs; next: a null-tolerant nom_test setting (null cost about -1) with its own 10%-null matched control first, run on R1/R2 only if that control passes >= 2/3, ~$2
- printed decipherment, if any - blocker: waiting-on LOCAL-QUEUE L53; Serrão 1969 pp. 455-458 and Falgairolle 1896 not opened
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located and no decipher on the leaves to rebuild one from

## Escalation (D2-SEURE, 5 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102); 44 = fos 84-87 pinned (SEURE-DEC)
- [ ] clear-pages: 44's clear text vs 43's cipher: nom_test (no nulls) R1 and R2 FAIL with control power (D2-SEURE); untried: null-tolerant setting with its own 10%-null control
- [ ] known-keys: no Henri II-era French key (Tomokiyo's Henri II pages, Lasry GL) tried on Seure yet
- [ ] print: Ribier and Francisque-Michel read (no); Serrão 1969 and Falgairolle 1896 not opened (LOCAL-QUEUE L53)
- [n/a] key-rebuild: no decipherment on fos 84-87 or canvases 84/88 (SEURE-DEC)
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85; fos 84-87 viewed at 1800-2200 px for a decipher (SEURE-DEC), none
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 1 internal gap; cheapest next: null-tolerant nom_test setting with its own 10%-null matched control first, then R1/R2 if the control passes, ~$2

## R8-SEURE: null-tolerant nom_test, 10%-null control first (6 Oct 2026, 04:04-04:17 UTC by date -u, account 1, LANE-RUN8-account-1)
Named next step of D2-SEURE. `kp/nom_test.py` gained `--null-cost` (passed to `tools/interlinear_align.run_align`; default -3.0, so
every earlier run is unchanged) and `--control-gate ERR:SHARE` (exit 3 before any target alignment). Pre-registered in `kp/PREREG-R8.md`
(commit 8c158b3cd, before the run): one setting, null cost -1.0, not swept; control gate >= 2/3 keys at err 0.095 in both the 10%-null
and 0%-null arms. Command as in the prereg; log `kp/nom_run_r8.log`, JSON `kp/result_r8.json`; ran 04:07-04:16 UTC, 0 network
requests, 0 subagent calls.

| control arm (null cost -1.0) | err 0 | err 0.095 | err 0.242 |
|---|---|---|---|
| 10% nulls: pass / S per key | 0/3: 0.243, 0.270, 0.246 | 1/3: 0.263, 0.265, 0.231 | 0/3: 0.238, 0.260, 0.243 |
| 0% nulls: pass / S per key | 3/3: 0.987, 0.992, 0.987 | 3/3: 0.894, 0.924, 0.894 | 1/3: 0.780, 0.261, 0.263 |

Shuffled-null p95 per key 0.25-0.28 in every cell. **CONTROL BELOW GATE**: the 10%-null arm sits inside its own null band even at zero
error (the same 0.23-0.27 it read at null cost -3.0), so R1/R2 were not run and nothing about the target is concluded. Cheaper nulls
also cost the no-null design power at the 0.242 bracket (1/3 here vs 2/3 at -3.0). With N8-SEU and RUN6-SEURE2/D2-SEURE this is the
third run of `nom_test` against a null-bearing design and the first to change the null knob; every 10%-null number stayed at the null
band, none moved toward the gate, so under rule 3's third-attempt clause the null-bearing nomenclator hypothesis is
**untested-by-this-tool** (`kp/nom_test.py` / `run_align` alignment at P = 407 letters), not refuted; it reopens only with a different
instrument (an aligner that models nulls explicitly, e.g. per-sign null classes learnt jointly) or more clear/cipher pairs.
Rows in `HYPOTHESES.md` (created here, with the D2-SEURE rows carried in). No grades changed; 0 tokens read; key.tsv and decode not run.
Not found: a null-cost setting of `nom_test` under which a 10%-null nomenclator control at this N separates from its shuffled nulls.

## Remaining gaps (R8-SEURE, 6 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); f81R L01-L20 reconciled (err_R 0.095 agreement); nom_test R1/R2 FAIL without nulls (D2-SEURE); null-tolerant setting retired at control (R8-SEURE, kp/result_r8.json); fo. 85r lines 1-5 clear read at M (SEURE-DEC).
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, fo. 84r-v and 87r of item 44) - blocker: not-attempted; 44-clear vs 43-cipher alignment FAILs without nulls (D2-SEURE) and the null-bearing design is untested-by-this-tool (R8-SEURE, control 0/3 at err 0); next: test Henri II-era French keys (Tomokiyo's Henri II pages, Lasry GL) against the reconciled f81R reads, ~$3
- printed decipherment, if any - blocker: waiting-on LOCAL-QUEUE L53; Serrão 1969 pp. 455-458 and Falgairolle 1896 not opened
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located and no decipher on the leaves to rebuild one from

## Escalation (R8-SEURE, 6 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102); 44 = fos 84-87 pinned (SEURE-DEC)
- [retired] clear-pages: kp/nom_test.py alignment instrument; no-null FAIL with control power (D2-SEURE), null-bearing design control 0/3 at null cost -3.0 and -1.0 (N8-SEU, D2-SEURE, R8-SEURE)
- [ ] known-keys: no Henri II-era French key (Tomokiyo's Henri II pages, Lasry GL) tried on Seure yet
- [ ] print: Ribier and Francisque-Michel read (no); Serrão 1969 and Falgairolle 1896 not opened (LOCAL-QUEUE L53)
- [n/a] key-rebuild: no decipherment on fos 84-87 or canvases 84/88 (SEURE-DEC)
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85; fos 84-87 viewed at 1800-2200 px for a decipher (SEURE-DEC), none
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 1 internal gap; cheapest next: test Henri II-era French keys (Tomokiyo, Lasry GL) against the reconciled f81R reads, ~$3

## R9-SEURE: Henri II-era known key (Danzay 1557) vs the reconciled f81R reads (6 Oct 2026, 06:06-06:1x UTC by date -u, account 1, LANE-RUN9-account-1)
Named next step of R8-SEURE (known-keys). Brief `.claude/briefs/runs/2026-10-06-account1-run9-jobs.md` ### R9-SEURE. Prereg
`keytest/PREREG-R9.md` (commit fd7b23c74, pushed before any decode or score). Script `keytest/key_fit.py` (`--check` OK), output
`keytest/result_r9.json`. 0 network requests, 0 subagent calls; images viewed by this worker: Tomokiyo's `danzay_1557.png` and one
f81R half-line crop (`images/kp/f81R_L02_s1.jpg`), to fix the label map.

**Candidate keys on disk.** Only one Henri II-era French symbol key is transcribed in this repository: Danzay 1557 (BnF fr.20140,
Tomokiyo's reconstruction, `ciphers/fr20140-danzay-1557/key.tsv`). The other Henri II-era keys on Tomokiyo's GL page (Marillac 1550,
La Guiche 1551, Babou) are images that are not on disk; the two Lasry GL tables on disk are fr.3071 (1530s) and fr.15564 (1580s),
both the wrong era. Bourdeau's `guiche1551` (fr.3151 no.22, same recueil) is not in sources/cyphersolver.
**Design note (observation, not scored):** Seure uses numerals >= 12 as word codes (70, 100, 13, 17, 30, 40 ...) and plain digits as
signs; Danzay's key has no numeral word codes, and only its digit-like glyphs (2, 4, 6, 7, 8, 9, 3) and a few symbols resemble
Seure's. The map (24 labels -> 19 glyph codes, PREREG table) covers 230/461 R1 signs.

| run (shuffled-key null, 1000 draws) | F (fr16 trigram mean) | trigrams | null p95 | pass |
|---|---|---|---|---|
| control: Danzay text, true key on the same 19 codes, err 0 (3 seeds) | -1.074 | 8 | -1.069 / -0.993 / -1.021 | 0/3 |
| control, err 0.095 | -1.25 to -1.27 | 6-8 | -1.05 to -1.10 | 0/3 |
| control, err 0.242 | -1.52 to -2.29 | 3-11 | -0.98 to -1.15 | 0/3 |
| target R1 | -1.465 | 64 | -1.439 (mean -1.772) | no |
| target R2 | -1.435 | 63 | -1.469 (mean -1.770) | nominal yes |

**Result: non-test (PREREG-R9 power condition failed).** The 19 codes the map can reach cover only 27% of Danzay's own ciphertext, so
even the true key on its own text gives 8 trigrams and does not beat its shuffled-key null at zero error. R2's nominal pass over its
null (by 0.034) therefore licenses nothing. Read by eye, its runs are not French: "m" (Seure '#') is the most frequent output, and
the runs include "dgmm", "iiphhlesym" and "hmpim" (M). No reading claimed, no grades changed, key.tsv and decode not run. Per the prereg,
this is not a negative for the Danzay key, and not for the key family, under any map.
Not found: any Henri II-era key other than Danzay's transcribed on disk; any French run in the f81R reads under Danzay's key with this map.
Lesson (one line): a known-key fit gated on n-grams needs the map to cover enough of the control's own text. Check the control's
covered trigram count before running the target, or use a coverage-free statistic such as unigram fit over the mapped signs.

## Remaining gaps (R9-SEURE, 6 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); f81R L01-L20 reconciled (err_R 0.095 agreement); nom_test R1/R2 FAIL without nulls (D2-SEURE); null-tolerant setting retired at control (R8-SEURE); Danzay 1557 key under one shape map is a non-test (R9-SEURE, keytest/result_r9.json); fo. 85r lines 1-5 clear read at M (SEURE-DEC).
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, fo. 84r-v and 87r of item 44) - blocker: not-attempted; Danzay 1557 key test is a non-test (power control 0/3, R9-SEURE); next: fetch Bourdeau's guiche1551 key (fr.3151 no.22, same recueil, MIT) and test it with a coverage-checked statistic (unigram fit over mapped signs, shuffled-key null, Danzay-style own-text power control first), ~$2.5
- printed decipherment, if any - blocker: waiting-on LOCAL-QUEUE L53; Serrão 1969 pp. 455-458 and Falgairolle 1896 not opened
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located and no decipher on the leaves to rebuild one from

## Escalation (R9-SEURE, 6 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102); 44 = fos 84-87 pinned (SEURE-DEC)
- [retired] clear-pages: kp/nom_test.py alignment instrument; no-null FAIL with control power (D2-SEURE), null-bearing design control 0/3 at null cost -3.0 and -1.0 (N8-SEU, D2-SEURE, R8-SEURE)
- [ ] known-keys: Danzay 1557 tried, non-test (R9-SEURE, power control 0/3 at 27% coverage); La Guiche 1551 (Bourdeau guiche1551, same recueil) untried
- [ ] print: Ribier and Francisque-Michel read (no); Serrão 1969 and Falgairolle 1896 not opened (LOCAL-QUEUE L53)
- [n/a] key-rebuild: no decipherment on fos 84-87 or canvases 84/88 (SEURE-DEC)
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85; fos 84-87 viewed at 1800-2200 px for a decipher (SEURE-DEC), none
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 1 internal gap; cheapest next: fetch Bourdeau's guiche1551 key and test it against R1/R2 with a coverage-checked statistic and own-text power control first, ~$2.5

## R9-SEURE2: Bourdeau's La Guiche 1551 key vs the reconciled f81R reads (6 Oct 2026, 06:42-06:47 UTC by date -u, account 1, LANE-RUN9-account-1)
Named next step of R9-SEURE (known-keys). Brief `.claude/briefs/runs/2026-10-06-account1-run9-jobs.md` ### R9-SEURE2. Key and own text
from D. Bourdeau, cyphersolver `targets/guiche1551/` (NOTES.md key line + 30 Sept corrections; `guiche_ct.txt`), fetched from
raw.githubusercontent.com 6 Oct 2026 (5 requests) and copied with credit (`keytest/guiche_key.tsv`, `keytest/guiche_ct.txt`; CC BY 4.0).
Prereg `keytest/PREREG-R9B.md` (commit cc6eec8b4, pushed before any score). Script `keytest/guiche_fit.py` (`--check` OK), output
`keytest/result_r9b.json`. Images viewed by this worker: Gallica btv1b90601662 f65 (1 request, 2000 px) and `images/kp/f81R_L03_s1.jpg`,
to fix the shape map. 0 subagent calls.

Design note (before scoring): La Guiche is a 22-sign simple substitution with no numerals; the f81R reads have 93 labels and 12 numeral
word codes. The La Guiche key cannot be Seure's key as a whole; the test asks only whether the shared shapes carry La Guiche's values.
Statistic: coverage-free unigram fit (R9-SEURE's lesson), U = mean fr16 log10 P(letter) over mapped signs, vs a 1000-draw shuffled-key
null (values permuted across the 17 mapped codes; U depends on value-at-position, so the null can differ).

| run | U | mapped signs | null mean / p95 | pass |
|---|---|---|---|---|
| control: La Guiche own text, true key on the 17 codes, err 0 (3 seeds) | -1.173 | 348 of 430 | -1.417 / -1.29 | 3/3 |
| control, err 0.095 | -1.19 to -1.20 | 342-349 | -1.42 / -1.30 | 3/3 |
| control, err 0.242 | -1.22 to -1.25 | 334-348 | -1.41 / -1.31 to -1.32 | 3/3 |
| target R1 | -1.351 | 198 of 461 | -1.419 / -1.289 | **no** |
| target R2 | -1.374 | 200 of 461 | -1.419 / -1.295 | **no** |

**Result: power condition holds (3/3 at E 0.095 and at 0.242); both reads FAIL, sitting near their null mean.** A negative for the La
Guiche 1551 key under this one shape map only: not for the key family, not for other maps. The control is design-matched to La Guiche
(simple substitution), not to Seure (homophonic + word codes), so it measures the statistic's power for this key on its own text.
Observation (M): under the map Seure's frequent `ff` (20) reads q and `#` (38) reads i, a profile no French text has. No reading claimed,
no grades changed, key.tsv and decode not run.
Not found: any fit of the La Guiche values to the shared shapes of the f81R reads above the shuffled-key null.
Lead (not acted on): Tomokiyo's Henri II page (`sources/cryptiana/web/henryii.htm`, l.129) lists BnF fr. 3138 no. 13, f. 32 (pp. 38-44),
"Lettre avec chiffre et dechiffrement de Philibert Babou ... au roy ... De Romme, XIme jour de jung 1558": a same-year French
diplomatic cipher with its period decipherment, from which a key can be rebuilt (Gallica btv1b90601662, same volume as La Guiche).

## Remaining gaps (R9-SEURE2, 6 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); f81R L01-L20 reconciled (err_R 0.095 agreement); nom_test R1/R2 FAIL without nulls (D2-SEURE); null-tolerant setting retired at control (R8-SEURE); Danzay 1557 key non-test (R9-SEURE); La Guiche 1551 key FAIL with control power under one map (R9-SEURE2, keytest/result_r9b.json); fo. 85r lines 1-5 clear read at M (SEURE-DEC).
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, fo. 84r-v and 87r of item 44) - blocker: not-attempted; Danzay 1557 non-test (R9-SEURE), La Guiche 1551 FAIL under one map (R9-SEURE2); next: rebuild the Babou 1558 key from fr. 3138 no. 13 f. 32 (cipher + period decipherment, Gallica btv1b90601662) and test it with keytest/guiche_fit.py's unigram statistic and own-text power control, ~$3
- printed decipherment, if any - blocker: waiting-on LOCAL-QUEUE L53; Serrão 1969 pp. 455-458 and Falgairolle 1896 not opened
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located and no decipher on the leaves to rebuild one from

## Escalation (R9-SEURE2, 6 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102); 44 = fos 84-87 pinned (SEURE-DEC)
- [retired] clear-pages: kp/nom_test.py alignment instrument; no-null FAIL with control power (D2-SEURE), null-bearing design control 0/3 at null cost -3.0 and -1.0 (N8-SEU, D2-SEURE, R8-SEURE)
- [ ] known-keys: Danzay 1557 non-test (R9-SEURE); La Guiche 1551 FAIL with control power under one map (R9-SEURE2); Babou 1558 (fr. 3138 no. 13, cipher with period decipherment) untried
- [ ] print: Ribier and Francisque-Michel read (no); Serrão 1969 and Falgairolle 1896 not opened (LOCAL-QUEUE L53)
- [n/a] key-rebuild: no decipherment on fos 84-87 or canvases 84/88 (SEURE-DEC)
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85; fos 84-87 viewed at 1800-2200 px for a decipher (SEURE-DEC), none
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 1 internal gap; cheapest next: rebuild the Babou 1558 key (fr. 3138 no. 13 f. 32, cipher + decipherment) and test it on R1/R2 with the unigram statistic and own-text power control first, ~$3

## R10-SEURE3: Babou 1558 leaf located and captured; decipherment too faint to rebuild a key (6 Oct 2026, 09:47-09:5x UTC by date -u, account 1, LANE-RUN10-account-1)
Named next step of R9-SEURE2 (known-keys). Brief `.claude/briefs/runs/2026-10-06-account1-run10-jobs.md` ### R10-SEURE3.
**Leaf.** BnF fr. 3138 (Gallica btv1b90601662, 102 canvases, black-and-white microfilm scan, the only Gallica copy: SRU on
"Français 3138" returns 0 other records; manifest has no folio labels, `tools/gallica_folio.py` cannot map it). Thumbnails of canvases
36-45 at 1000 px: item 13 (Babou to Henri II, Rome, 11 June 1558) runs canvas 36 right (fo. 32r) to canvas 41 right (fo. 37r, signed
"Babou"), address on canvas 42. The letter is clear text except **two cipher blocks on fo. 35v (canvas 40, left page)**: block A, 4 lines,
mid-page; block B, 4-5 lines, lower page; together about 250 signs. Both blocks are struck through with a horizontal line.
Crops: `babou/images/` (`tools/iiif_lines.py --ark btv1b90601662 --canvas 40 --region 550,1250,3650,800 --prefix c40A --debug` and
`--region 550,3700,3650,750 --prefix c40B`; 2 regions, 20 line crops, debug overlays, manifest.json).
**The decipherment.** Two forms, both period: (1) an interlinear letter decipher between the cipher lines, in a light hand and itself
struck through; (2) a marginal paraphrase in the left margin beside each block (A, read at M: "Mays ... declare ... pour respect de
l'armee turquesque"; B, M: "Le pape se declaroit ... entre ... Sire / Et tost qu'il seroit ..."). The marginal text is a summary, not
letter-aligned, so it cannot carry a key. The interlinear decipher was viewed at native resolution with contrast stretching
(percentile 1-45) and 2x zoom on block A line 2 and block B line 2: fewer than about one gloss letter in five is legible, none can be
placed under a specific cipher sign with confidence, and 0 cipher/clear pairs were recorded. A pair table for
`tools/interlinear_align.py` therefore cannot be built from this capture; no key rebuilt, so no PREREG, no power control and no score
on R1/R2 (nothing to gate). Not a negative for the Babou key.
**Design observation (M, shapes only, not scored):** Babou's signs are letter-like and symbol forms with two-digit numerals among them
(A, M, E, N, R, h, z, x, q, g, a lying 8, crosses, a barred circle, "23", "11", "16", "10"), the same mixed letter/symbol/numeral
look as Seure's f81R inventory (R, oo, A, M, N, h, z, x, + and numeral codes). The shared look is what makes the key worth having,
not evidence that it is Seure's.
Requests: gallica.bnf.fr 14 (1 manifest, 10 thumbnails, 2 IIIF regions, 1 SRU); 0 subagent calls.
Not found: a legible letter-by-letter decipher of the Babou cipher at the Gallica microfilm capture; any other digitisation of fr. 3138.

## Remaining gaps (R10-SEURE3, 6 Oct 2026)
Read so far: 0 tokens read (0 H, 0 C); f81R L01-L20 reconciled (err_R 0.095 agreement); nom_test R1/R2 FAIL without nulls (D2-SEURE); null-tolerant setting retired at control (R8-SEURE); Danzay 1557 key non-test (R9-SEURE); La Guiche 1551 key FAIL with control power under one map (R9-SEURE2); Babou 1558 key not rebuildable from the microfilm capture (R10-SEURE3, babou/images); fo. 85r lines 1-5 clear read at M (SEURE-DEC).
- f75L line reads (lines 1-44) - blocker: illegible; three two-reader box-keyed gates failed (K 51.7%, O 38.5%, C 42.9%), instrument retired under rule 3; reopens only with the owner's sign-sorter alphabet or a better capture
- items 43/44 cipher body (f81R-f83L, fo. 84r-v and 87r of item 44) - blocker: not-attempted; Danzay non-test, La Guiche FAIL under one map, Babou key not rebuildable from the capture (interlinear decipher struck through and faint); next: test Tournon 1556 (fr. 3138 no. 9, fo. 21, "chiffre et dechiffrement", canvases ~25-30) and Morvilliers 1549 (no. 24, fo. 66, canvases ~72-74) in the same volume for a legible decipher before any further key rebuild, ~$1.5
- Babou 1558 interlinear decipher (fr. 3138 fo. 35v) - blocker: illegible at the Gallica microfilm scan; reopens with a colour capture (BnF reproduction request) or a person's read in the reading room
- printed decipherment, if any - blocker: waiting-on LOCAL-QUEUE L53; Serrão 1969 pp. 455-458 and Falgairolle 1896 not opened
- key of the cipher - blocker: no-key-material; no key of Seure's 1558 Lisbon embassy located and no decipher on the leaves to rebuild one from

## Escalation (R10-SEURE3, 6 Oct 2026)
- [x] siblings: items 40/41 and 43/44 surveyed (K), 43/44 compared at closing and postscript (GAPS102); 44 = fos 84-87 pinned (SEURE-DEC)
- [retired] clear-pages: kp/nom_test.py alignment instrument; no-null FAIL with control power (D2-SEURE), null-bearing design control 0/3 at null cost -3.0 and -1.0 (N8-SEU, D2-SEURE, R8-SEURE)
- [ ] known-keys: Danzay 1557 non-test (R9-SEURE); La Guiche 1551 FAIL under one map (R9-SEURE2); Babou 1558 decipher illegible at capture (R10-SEURE3); Tournon 1556 and Morvilliers 1549 (fr. 3138 nos. 9, 24, "avec chiffre et dechiffrement") untried
- [ ] print: Ribier and Francisque-Michel read (no); Serrão 1969 and Falgairolle 1896 not opened (LOCAL-QUEUE L53)
- [n/a] key-rebuild: no decipherment on fos 84-87 or canvases 84/88 (SEURE-DEC)
- [x] image-check: f83R contrast 101 vs f75L 91 vs f87R 85; fos 84-87 viewed at 1800-2200 px for a decipher (SEURE-DEC), none; Babou fo. 35v contrast-stretched at native res (R10-SEURE3), decipher illegible
- [retired] retry: two-reader box-keyed pass on f75L failed three gates
Verdict: keep going: 1 internal gap; cheapest next: look at fr. 3138 nos. 9 (Tournon 1556) and 24 (Morvilliers 1549) for a legible decipher, then rebuild and test whichever reads, ~$1.5
