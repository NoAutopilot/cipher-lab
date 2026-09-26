open

Charrière, Négociations de la France dans le Levant, tome II (Paris, 1848; archive.org `ngociationsdel02charuoft`) read as full text (grep, whole volume) by this worker for "Noailles"/"Acqs"/date and place terms, 26 Sept 2026: no decipherment or clear-text rendering of this letter. Ribier, Lettres et mémoires d'estat (Paris, 1666), both tomes, already cached full text on disk (`sources/ia-fulltext/print-check/bub_gb_{bOnmNv2ZLVoC,qWTswSr32NYC}_djvu.txt.gz`) re-grepped by this worker for "Noailles"/"d'Acqs": zero hits in either tome.

# BnF fr. 3151 no. 33 — François de Noailles (Venice) to the Cardinal de Lorraine, 13 Nov 1558

QUEUE row: G10 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`), catalogue item 10 at
dbourdeau.github.io/cyphersolver/catalogue.html. This target and `ciphers/fr3151-seure-1558` (Seure, nos. 39-44)
and La Guiche fr. 3138 no. 22 share Bourdeau's catalogue entry 10 but are three separate items/keys. This job
(LANE NX, `.claude/briefs/runs/2026-09-26-lane-nx-3151n33.md`) covers only no. 33. Do not edit
`ciphers/fr3151-seure-1558/`.

**Correction to the job brief's guess of the addressee.** The brief guesses "likely Montmorency"; Bourdeau's own
`guiche1551/NOTES.md` (fetched fresh from GitHub raw, `dbourdeau/cyphersolver@main`, 26 Sept 2026 08:52 UTC, so
current, not the stale 21 Sept snapshot) identifies the letter precisely: **"Noailles → Cardinal de Lorraine,
Venice, 13 Nov 1558 (fr. 3151 no. 33)."** François de Noailles, bishop of Dax (Acqs), was French ambassador at
Venice from Sept 1557 (WebSearch, confirmed against Charrière's introduction to his correspondence, tome II
p.405-406: Henri II's 26 Sept 1557 letter names him taking over the Venice post from the bishop of Lodève).

## Six-source search log (26 Sept 2026, this worker)

1. **Standard edition / calendar.** François de Noailles's Venice correspondence with **La Vigne** (his
   opposite number at Constantinople) is printed at length in Charrière's *Négociations de la France dans le
   Levant* (4 vols, 1848-1860); tome II covers 1547-1566 and includes about 20 "Venise, [date] 1558" letter
   headers running January-November 1558 (lines located by grep: 10 janv., 1 févr., 26 févr., 4/26 avril, 8/28
   juin, 5 juil., 23/30 juil., 18/27 août, 20/28 sept., 7 nov., 15 nov. 1558). None is dated 13 November, and none
   of the surrounding correspondence (which is Noailles-La Vigne Ottoman-affairs traffic, not Noailles-to-Lorraine)
   mentions Candia, Corfu or the Levant galleys in the terms Bourdeau's note describes for no. 33. Full-volume grep
   for "chiffr"/"déchiffr" finds no printed decipherment near any 1558 Venice letter (one hit, "mectre en chiffre"
   in the 4/26 April letter, is Noailles asking to *have something enciphered*, not a printed clear reading).
   Ribier (1666, both tomes) never names Noailles or "d'Acqs" at all (zero hits either tome) — consistent with
   `ciphers/fr3151-seure-1558/NOTES.md`'s prior finding that Ribier does not cover this ambassador. Vertot/Villaret,
   *Ambassades de Messieurs de Noailles en Angleterre* (1763), is Antoine/Gilles de Noailles's **England** embassy,
   a different brother and a different posting (WebSearch turns up nothing connecting it to François at Venice);
   not opened this pass, flagged if this target is promoted. **Cuisiat's 1998 edition of the Cardinal de Lorraine's
   own letters (*Lettres du cardinal Charles de Lorraine, 1525-1574*, Droz) is his outgoing correspondence, not
   letters he received** (per the publisher's and reviewers' description, WebSearch) — the wrong direction for a
   letter Noailles *sent to* the Cardinal, so it is not a candidate edition for this item even though the
   correspondent matches; not opened (no accessible full text found this pass; flagged, not claimed as read).
2. **Tomokiyo (sources/cryptiana/ on disk).** No page for François de Noailles's Venice posting or fr. 3151 found
   in the local mirror. henryiii.htm covers François de Noailles's *later* Constantinople embassy (from 1571) and
   his cipher there (BnF fr. 16142) — a different posting, different cipher, more than a decade later; not the
   same key. The one "3151"-adjacent string match (codebreaking.htm, "31511" inside a Zimmermann-telegram code
   group) is a false positive.
3. **Lasry's publications.** No Lasry solution of fr. 3151 or a Noailles/Venice 1558 cipher found via Tomokiyo or
   web search.
4. **DECODE + both solver-repo clones.** No DECODE record for fr. 3151 in the local snapshot (`sources/decode/`)
   or in Aymeloglu's DECODE catalogue scrape (`catalogue/decode-catalog.csv` in his repo, re-cloned this pass —
   the one numeric "3151" hit there is DECODE record id 3151, an unrelated 1919 US postcard). Bourdeau's repository
   (re-fetched fresh from GitHub raw at 08:52 UTC and from the live catalogue page at 08:55 UTC, both 26 Sept
   2026, so current): `guiche1551/NOTES.md` §2 states plainly for no. 33 — "Read at the time; the cipher itself
   (about 150 signs, a different symbol alphabet) was not attacked. A full reading would need the page opened
   flat, or a solve using the visible gloss words as cribs." The live catalogue's item-10 row (fetched 08:55 UTC)
   repeats this unchanged: "Noailles (no. 33) read at the time: see guiche1551/" — confirms the escalation log's
   "not-attempted" for the cipher itself still holds as of today, not stale. Aymeloglu's `unsolved-ciphers` repo
   (re-cloned shallow, 26 Sept 2026): no fr.3151/Noailles hit (the two string matches, "3151" in the DECODE-catalog
   CSV and "noailles" in a French word-frequency lexicon file, are both unrelated).
5. **Web-search / model-solve announcements.** "fr.3151" + Noailles/Venice cipher: no hit (only unrelated Venetian
   cryptography scholarship, e.g. Pasini 1872, Amadi manuscript studies). Vals AI / "Claude solves" model-solve
   coverage since Sept 2026: the only historical-cipher item found is Claude Fable 5.1's Urquhart *Cyphral
   Distich*/*Octastich* (1653, unrelated target, unrelated cipher).
6. **Ciphertext confirmed present, and the marginal gloss independently read from the image (this worker, step 2
   below).**

## Verdict

**Open.** No source of the six, nor a fresh direct check of the live Bourdeau catalogue, shows the ~150-sign
cipher of no. 33 itself ever attacked or solved; only the manuscript's own contemporary marginal decipherment
of parts of the two short cipher blocks exists (confirmed independently from the image, see below), and it does
not by itself constitute a modern reading of the cipher. Rule 10: no novelty claim made; this is a search result,
not a verifier's classification.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 10, `guiche1551/`
working folder), CC BY 4.0 — identified the letter, its addressee and date, and the marginal gloss; not an attempt
at the cipher itself.

`python3 tools/intake_gate_check.py fr3151-noailles-1558` output:
```
fr3151-noailles-1558: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit: 0
```

## Leaf view (26 Sept 2026, this worker)

Gallica `btv1b9059865k` manifest has every canvas labelled `NP` (unlabelled), like fr.16092/fr.5160/fr.20140
(playbook). `tools/gallica_folio.py --folio` cannot place it from labels alone; placed instead from Bourdeau's
own view numbers ("views 60–61", `guiche1551/NOTES.md`), confirmed by eye: canvas 61's right page carries the
printed folio number "60" in its top corner. Canvas 60 = opening f.58v/f.59r; canvas 61 = f.59v/f.60r; canvas 62
= f.60v/f.61r. 500px survey of canvases 59–62 (`images/survey/f59.jpg`..`f62.jpg`), native-resolution capture of
the f.60r right leaf (`tools/iiif_lines.py --ark btv1b9059865k --canvas 61 --region 3900,0,4030,5659 --debug`,
one fetch, 4030x5659; the tool's own per-line crops and debug overlay were made then deleted, not needed since
this job does no transcription), and 1500-2000px fetches of canvas 62 (`images/survey/f62_1500.jpg`,
`f62_left_2000.jpg`) for the verso/address panel. Requests: gallica.bnf.fr 8 (manifest already cached from the
Seure job; 4 survey fetches at 500px, 1 native region fetch, 2 fetches at 1500/2000px), >=1.5s apart, no
403/429/challenge.

**Date and addressee.** The job brief's own guess ("likely Montmorency") is wrong; corrected above from
Bourdeau's note. Independently confirmed from the image, canvas 62 right page (f.61r, the letter's own outer
address panel, folded-letter convention): reads **"A Monseigneur ... Monseigneur le Cardinal de Lorraine"**
(`images/survey/f62_1500.jpg`), with **"1558"** docketed lower on the same panel and again as a side-note in a
second, smaller hand. The closing paragraph on f.60v (`images/survey/f62_left_2000.jpg`) ends "...vous [supplie?]
... du [ ] Nouembre" before the valediction and signature — "Nouembre" independently confirmed; this worker did
not resolve the day digit from the image in the time available, so "13 Nov 1558" is carried from Bourdeau's
reading, not independently re-derived here. Grade for the date: M (day), H (month/year, this worker's own read of
the image).

**Cipher signs.** **Three cipher blocks, not two** — Bourdeau's note ("two short cipher passages, 3 and 3 lines,
on f. 60r") covers only the two blocks he could see within "views 60–61"; canvas 62 (f.60v), one view past his
range, carries a third, longer block that his note does not mention. On f.60r (`cipher_blocks_full.jpg`): block 1
is 3 lines, block 2 is about 5 lines, separated by one line of plain French ("Dieu vous ... a tous aultres qui
[n'y ont? part?]"). On f.60v (`images/survey/f62_left_2000.jpg`): a third block of about 7 lines, braced as one
unit in the margin. Rough visual count (not a transcription): roughly 14-16 tokens per line x 15 lines total ≈
200-230 sign-tokens, more than the brief's "about 150" figure (which appears to be Bourdeau's f.60r-only count).
Sign type: invented pen-drawn symbols (loops, crosses, hooks, geometric marks) interleaved with two-digit Arabic
numerals (7, 20, 30, 40, 70 seen), the same mixed symbol-plus-numeral nomenclator shape as the Seure letters
bound in the same recueil (`fr3151-seure-1558/NOTES.md`) — consistent with, but not confirmed as, the same key.

**The marginal gloss is a period decipherment (a crib), not an archivist's note.** Written in a distinct, smaller,
more cramped hand than both the letter's own secretary hand and any later archival endorsement, positioned in the
narrow inner margin immediately beside each cipher block, with the first character(s) of every gloss line cut off
by the binding (matches Bourdeau's "swallowed by the binding"). Independently read from the image, first gloss
(beside f.60r block 1, `margin_gloss1_zoom.jpg`): **"...en mauluaise / ...gouuernemet / ...de q affaires"** —
matches Bourdeau's citation "mauluaise … gouvernement … affaires" word for word. Second gloss (beside f.60r block
2): partially legible, "grand" and "fortune" both read, consistent with Bourdeau's "grand seigneur … ne luy … de
la fortune". Third gloss (beside the newly-found f.60v block): present, several words long, not transcribed here
(out of scope: no transcription in this job) — flagged for whoever takes the cipher itself. The visible-word
content (bureaucratic/diplomatic register, plausible mid-sentence) and precise physical placement rule out an
archivist's shelfmark or provenance note; this is the court's own contemporary reading of at least parts of the
cipher, written at the time, not a modern reading of it.

**Subject (from the clear text, f.60r top and f.60v top, read by eye, not transcribed).** Levant galleys, "gallees
du pape", "Candye" (Candia), "Corfou" (Corfu), naval/maritime matters — consistent with Bourdeau's summary and
with a Venice-posted ambassador's dispatch in the weeks after the fall of Calais (Jan 1558) and amid the
Cateau-Cambrésis run-up, the same season as the Charrière-printed Noailles-La Vigne Ottoman correspondence
searched under check-solved above, but addressed to a different, domestic correspondent (the Cardinal de
Lorraine, Henri II's chief minister-cardinal) rather than to La Vigne at Constantinople.

## Next step

Not attempted this job (out of scope: check-solved + leaf view only). For a future solve pass: transcribe all
three cipher blocks (about 200+ signs) and the three gloss passages at native resolution; use the legible gloss
words as cribs against the symbol+numeral nomenclator, the same approach Bourdeau's own escalation log proposes.
The f.60v block and its gloss are new information not in `guiche1551/NOTES.md` — worth a note back to Bourdeau's
project (see the outreach gates in CLAUDE.md) once this target has a verifier's N-class, not before.

QUEUE row for the orchestrator to file (do not edit QUEUE.md/G10 directly — see final paragraph):
G10's row already covers this item; the correction is that Noailles no. 33 has **three** cipher blocks
(~200-230 signs) across f.60r/f.60v, not two (~150 signs) confined to f.60r, each with its own period marginal
gloss (crib), addressee independently confirmed as the Cardinal de Lorraine.

## Transcription + gloss alignment attempt (26 Sept 2026, LANE NX NX-3151G)

Intake gate re-checked: `python3 tools/intake_gate_check.py fr3151-noailles-1558` still exits 0 (the NX-3151N33
verdict above already names the edition/full-text search read). Claimed in ROOM.md before starting.

### 1. Crops

`tools/iiif_lines.py`, native resolution, one new Gallica fetch (1 connection-reset retried once, per the
good-citizen rule), the rest cut from sources already on disk:

```
python3 tools/iiif_lines.py --image images/src_ark_12148_btv1b9059865k_f61_3900_0_4030_5659.jpg \
  --region 0,2800,4030,2000 --out images/crops --prefix f60r --top-margin 40 --debug
python3 tools/iiif_lines.py --ark btv1b9059865k --canvas 62 --region 0,0,3966,5655 \
  --out images/crops --prefix f60v_full --debug
python3 tools/iiif_lines.py --image images/crops/src_ark_12148_btv1b9059865k_f62_0_0_3966_5655.jpg \
  --region 0,2050,3966,1400 --out images/crops --prefix f60v --top-margin 30 --debug
```

Debug overlays (`f60r_lines_debug.jpg`, `f60v_lines_debug.jpg`) checked before any pass. A provisional
sign-shape legend (`images/crops/sign_legend.md`) was written by this worker from one visual skim, so both
blind passes on each block would use the same code vocabulary for non-numeral pen-drawn signs (numerals are
always read as literal digits); this is the same role `tools/glyph_atlas.py` plays elsewhere, done by hand
here because the corpus is small (~200 signs across 3 blocks).

**Block-boundary correction to the NX-3151N33 intake note above:** block 2 is **3 lines** (f60r L05-L07), not
"about 5" — the line-detector's bands, confirmed against the debug overlay, show block1 = 3 lines (L01-L03,
gloss1 beside it) + one plain-French separator line (L04) + block2 = 3 lines (L05-L07, gloss2 beside it),
then plain prose resumes (L08-L10, not part of any cipher block). Block 3 (f.60v) is 7 lines as the intake
note said: L03 is a plain/cipher transition line (gloss3 begins beside it), L04-L09 are six lines of pure
cipher, L09 ends in a clear plaintext tail ("...tant vn hongrie...").

### 2. Transcription: two blind Sonnet passes per block, `tools/reconcile_passes.py`

| block | lines | agreement | worst line | best line |
|---|---|---|---|---|
| 1 (f60r L01-L03) | 3 | 45.8% (38/83) | L03 17% | L01 65% |
| 2 (f60r L05-L07) | 3 | 30.8% (20/65) | L06 11% | L05 50% |
| 3 (f60v L03-L09) | 7 | 51.3% (81/158) | L05 36% | L06/L07 58% |
| **all three** | 13 | **45.4% (139/306)** | | |

Both passes on every block independently reported low confidence (heavy `?`/`unkN` use), citing faint ink, a
gray bleed-through/ghost text from the facing leaf's ink showing through the paper, and difficulty separating
several of the legend's hook/loop-family codes at this resolution — the same failure mode CLAUDE.md and
LESSONS.md record for `fr3151-seure-1558`, the sibling cipher bound in the same recueil (38.5-51.7% agreement
on comparable material, "not box-keyable at this image quality"). Per that precedent: **no hand-settling from
the image was attempted at any of the three gates above** (all well under the usual 80% bar); `disagreements_
block{1,2,3}.tsv`/`ciphertext_draft_block{1,2,3}.tsv`/`agreement_block{1,2,3}.tsv` are diagnostic only, kept
for a future pass with a better image or a key. Numerals fare somewhat better than pen-signs (20, 70, 9, 10, 6
recur at H-grade agreement in block1), consistent with a nomenclator mixing invented symbols with numeral
codes — the same convention `fr3151-seure-1558/NOTES.md` describes for its own cipher in this recueil.

Plain-hand words squeezed onto the same physical line as the cipher (both passes noticed independently,
disagreed on exact spelling, grade M): block1 L03 ends "...mon Seigneur ... muy." (the letter's own clear
hand resuming mid-line, not a decoded value); block3 L09 ends "...tant vn hongrie[...]" (H-grade for "tant vn
hongrie", legible on direct inspection, continuing into the next plain paragraph about Italy/Hungary that
follows the cipher block).

Block2 pass B ran long (49 tool calls, 516s, repeated upscaling) for no gain in agreement over pass A's
single-look approach (30.8% either way) — a usage-rule note for future briefs of this shape, not a reading
problem.

### 3. Marginal gloss

One independent Sonnet multimodal read of all three zoomed gloss crops, plus this worker's own direct check
(the brief's "one careful pass per gloss plus your own check") — both cut off at the same point by the
binding, disagreeing occasionally on the word itself:

- **Gloss 1** (beside block1, clearest of the three, 3 lines matching L01/L02/L03 1:1 by margin position):
  "[..] en mal[u]aise" / "[..] gouuernemet" / "[..] de q [iustice?]". Lines 1-2 confirm the intake NOTES's
  secondhand citation from `guiche1551/NOTES.md` ("en mauluaise", "gouuernemet"). Line 3 disagrees with that
  citation's "affaires": both this worker's own two direct reads and the independent subagent read the word
  after "de q" as opening with a tall ascender more consistent with "iustice" than a lowercase "a" — flagged,
  not resolved.
- **Gloss 2** (beside block2, L05-L07): markedly lower contrast than the other two; this worker's own two
  reads and the subagent's read do not agree on a single word ("seigneurie"/"Loysanne"/"fin luy" all floated,
  none confident). Effectively illegible; not usable for alignment.
- **Gloss 3** (beside block3, 7 gloss lines, longest of the three): lines 1-4 give partial legible fragments
  ("chascune chose" the single clearest phrase); lines 5-7 are essentially unreadable. The final fragment
  ("hongroy[?]") sits beside the block's last line and is topically consistent with the plaintext tail's "un
  Hongrois", but this is the period reader's own summary word, not necessarily a decode of the adjacent group.
  Unlike gloss1, **which of the 7 cipher lines each gloss3 fragment sits beside is this worker's own visual
  inference from vertical position, not a secure pairing** — the margin handwriting cascades continuously and
  does not visibly break into 7 discrete units aligned one-to-one with the cipher bands.

Full transcript: `align/gloss_read_subagent.md`.

### 4. Alignment attempt and control (gate written before running, per the brief)

**Gate:** leave-one-block-out mean accuracy on cipher values attested at least twice elsewhere >= 0.60 (under
5 qualifying tokens: the control cannot fail, say so), plus a 10-permutation shuffled-gloss control side by
side.

**This could not be run as specified.** The brief's design needs, for each of the 3 blocks, an independent
usable (gloss, cipher) pairing to train on or hold out. On the data actually recovered in step 3: only block
1 has a gloss legible enough to extract any word at all, and even there each line keeps only 1-3 words (the
rest lost to the binding). Block 2's gloss is illegible past unconfident fragments; block 3's gloss has a few
legible words but no secure line-level pairing to specific cipher lines. So there is no second or third block
with usable gloss data to leave out — the leave-one-**block**-out design has nothing to run on beyond block 1.

**What was run instead, and reported as an honest substitute, not the brief's design:** a leave-one-**line**-
out self-consistency check within block 1's own 3 (gloss fragment, cipher line) pairs, using
`tools/interlinear_align.py`'s DP (`--floor 0`, each block1 reconciled-draft sign mapped to a synthetic
surrogate code, same method `fr3625-lauriere-1593/align/control_lau.py` used for its own sign-heavy
nomenclator). Script: `align/control_3151.py`.

| held-out line | qualifying values | correct | accuracy |
|---|---|---|---|
| f60r_L01 | 12 | 0 | 0.000 |
| f60r_L02 | 10 | 0 | 0.000 |
| f60r_L03 | 11 | 0 | 0.000 |
| **total** | **33** | **0** | **mean 0.000** |

33 qualifying values (>=5, so not a can't-fail non-test by the brief's own caveat) — this is a real test, and
it returned a clean zero. **Shuffled-pairing control**, 10 permutations of which line's gloss fragment trains
which (seed 20260926): every permutation also scored exactly 0.000 (22-35 qualifying tokens each). **The true
pairing is not merely below the 0.60 gate — it is tied with the shuffled-pairing floor at 0.000**, i.e. this
specific DP/floor-0 method extracts no signal from gloss1's 1-3-word-per-line fragments at all, real pairing
or scrambled. (Mechanically: each line's gloss is 1-3 words spread by the DP over 10-30 signs, so most signs
get no chunk; the few generic high-frequency signs — `tbar`, `hash`, `slash` — that do qualify as "attested
twice" are common enough across all three lines that their DP-assigned top meaning essentially never happens
to coincide with the specific 1-3 words left in a given held-out line's own fragment, whether the pairing is
true or scrambled.)

**Verdict: CONTROL BELOW GATE, and additionally not the brief's leave-one-block-out design at all** (only one
block had any usable gloss). Per the brief ("Only if the control meets its gate"), step 4 (`decode.json`,
`key.tsv`, `specs/fr3151-noailles-1558.json`, `tools/judge_plaintext.py`) was **not run** — there is no
control-backed group-level key to apply, and forcing a decode without one would be exactly the kind of
uncontrolled reading rule 3 exists to prevent. This mirrors `fr3625-lauriere-1593`'s NX-LAU result the same
morning (0.200 vs 0.60 gate, true pairing not separated from its own shuffle mean of 0.085) with an even
weaker starting position: Lauriere had an independently published 12-value ground-truth table across 7 runs;
Noailles has no prior key at all and legible gloss text on only one of its three blocks.

### 5. What this job establishes and what it does not

Established, reproducible from files in this folder: the corrected 3/3/7-line block structure; two blind
Sonnet transcription passes per block with their reconciled agreement figures (diagnostic, not a reading);
independent reads of all three marginal glosses with a disagreement flagged against the one existing
secondhand citation (gloss1 line 3, "iustice" vs "affaires"); a leave-one-line-out self-consistency control
on the one block with any usable gloss, tied with its own shuffle floor at 0.000.

Not established: any group-level cipher key from this gloss (the data does not support one at the
confidence this job's own gate requires); a full transcription of any block (all three gates well under the
usual 80% settling bar); which specific gloss3 fragment belongs to which specific cipher3 line (visual
inference only). Status stays `open` (rule 5: this is neither a control-backed negative covering the whole
target's ladder — cryptanalysis without the gloss has not been tried at all — nor a margin that would make it
`partial`).

### 6. Next step

Not a next step for this job (brief: transcribe, align, gate, stop). For a future pass on this target: (a) a
higher-contrast or raking-light capture of the inner margin specifically (both f60r glosses and f60v's would
benefit — the binding-cut text is the bottleneck, not the transcription method) would do more than further
transcription passes at this image quality, matching `fr3151-seure-1558/NOTES.md`'s own "needs a different
capture" conclusion on the neighbouring item in this recueil; (b) a plain cryptanalytic attempt on the ~200
transcribed-but-unsettled signs (homophonic/nomenclator family, matched control, per rule 3) is untried and
does not depend on the gloss at all — the transcription drafts in `align/ciphertext_draft_block{1,2,3}.tsv`
are a starting point for it, with the caveat that they are themselves only ~45% agreed and would need
resettling first.

Files: `images/crops/**` (line crops, debug overlays, sign_legend.md), `images/margin_gloss{1,2,3}_zoom.jpg`,
`align/**` (pass A/B TSVs per block, reconciler outputs per block, gloss_read_subagent.md, control_3151.py).
Hosts: gallica.bnf.fr 2 (1 info.json probe, 1 native region fetch, 1 connection-reset retried once). Subagents:
7 (2 blind transcription passes x 3 blocks + 1 combined gloss read), all Sonnet, one exceeded the usual
per-call budget (block2 pass B, noted in step 2) — flagged for the lane orchestrator, not itself a finding.
