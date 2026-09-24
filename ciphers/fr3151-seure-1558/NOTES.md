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
