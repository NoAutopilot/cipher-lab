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

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/guiche1551/NOTES.md (catalogue 10)
- Their extent, in their words: no. 33 found "read at the time": marginal period decipherment, partly lost in the gutter; no reading of their own
- Their date: 21 Sept 2026 (updated 30 Sept)
- Note: already cited in our NOTES.md (26 Sept)
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## LIKELY-5 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`, row 5 of `ciphers/_triage/likely-solves-2026-10-02.tsv`:
first cheap test = `tools/interlinear_align.py` on the surviving margin gloss vs the three cipher blocks, key from the
alignment, shuffled-gloss control; decode and fr16 judge only if the control is cleared. Cap USD 8, box 60 min, at most
2 vision calls, no family run. Intake gate at start: exit 1 for the missing web/blog check only (section below), exit 0
after it. No Gallica request this job: every image was already on disk (images/manifest.json, crops/manifest.json).

**What the two vision calls showed (both spent on the gloss crops, none on the sign drafts -- the alignment hinges on
the gloss, not on single sign disagreements; a choice logged here, not in the brief).**
- `images/margin_gloss1_zoom.jpg`: three margin lines braced to the right ("}") beside block 1, cut at the gutter on
  the left. My read: "[..]he en mauluaise / [..] gouuerneme[n]t / [..]a de q[ue] iustice[?]" -- lines 1-2 as the
  26 Sept subagent and Bourdeau's citation have them; the last word of line 3 stays unresolved between "iustice"
  (26 Sept subagent, and the tall opening ascender I see too), "duction" and Bourdeau's "affaires". Grade M.
  What survives is about 35 letters beside 83 signs.
- `images/margin_gloss3_zoom.jpg`: seven margin lines of running French prose beside block 3's six cipher lines.
  My read (grade M, most words unsure): "Mais ie me doubte / que le S[eigneu]r Che[..] / [..]a sur a prou[?] fait /
  ch[..] oue [..] une allee[?] / [..]ssee le 3 me / [..]nuieuure p[our] et [..] / psua haydr[?] ..". The 26 Sept
  subagent read the same crop as "a mre a chiffre / auec le Sr Chef / a prou prest / a me chascune chose / stoffee de
  mo / p a Hyai / baucy a". The two witnesses agree on "le S..r Che" and "a prou" and on little else, so gloss 3 is two
  M-grade witnesses of about 72 letters each beside 158 signs, not a text.
- Structural point for the test design: the gloss wraps on the margin's own line widths (7 gloss lines beside 6
  cipher lines in block 3; 1-2 surviving words per line in block 1), so there is no physical basis for pairing
  gloss line i with cipher line i. The fair unit is one (gloss, block) pair per block.

**Design (pre-registered, `align/likely5_align.py`, output `align/likely5_run.txt`).** One pair per block, cipher lines
concatenated in order, surviving gloss words concatenated in order; symbol signs as surrogate codes below the floor
(one letter or null), numerals as word codes above it; no prior. Statistic: consistency = share of aligned
occurrences (codes seen >= 2 times) that carry the code's top chunk, and n_cons = codes with >= 3 occurrences agreeing
on two thirds of them -- both can differ between the true gloss and a shuffled one. Controls: (a) shuffled-gloss, the
gloss words permuted, 200 permutations; (b) cipher-line order shuffled, 100. Gate: consistency above control (a)'s
p95 and n_cons >= 5. Matched positive control (rule 3): synthetic French (fr16 corpus) blocks of the same sign counts
(83/65/158), homophonic symbol cipher (25 symbols over 20 letters, 8% nulls), gloss cut the way the real one is (block-1
shape: the last 41% of each line's plaintext survives; block-3 shape: 55% of the words legible), 5 seeds each vs 100
word-shuffles.

| run | gloss letters / signs | consistency (n_cons) | shuffled-gloss mean / p95 / max | shuffled-lines mean / p95 | gate |
|---|---|---|---|---|---|
| block 1, gloss as read | 35 / 83 | 0.500 (2) | 0.569 / 0.655 / 0.704 | 0.496 / 0.538 | miss |
| block 2, subagent fragments | 33 / 65 | 0.435 (0) | 0.499 / 0.609 / 0.696 | 0.415 / 0.500 | miss |
| block 3, subagent witness | 73 / 158 | 0.455 (4) | 0.520 / 0.625 / 0.656 | 0.496 / 0.574 | miss |
| block 3, this worker's witness | 72 / 158 | 0.583 (4) | 0.525 / 0.625 / 0.661 | 0.471 / 0.578 | miss |
| block 1, NX-3151G line-to-line pairing, same statistic | 35 / 83 | 0.500 (1) | 0.534 / 0.667 / 0.667 | -- | miss |
| **positive control, block-1 shape, 5 seeds** | 35-36 / 83 | 0.444-0.654 | each at or under its own p95 | -- | **0/5 clear** |
| **positive control, block-3 shape, 5 seeds** | 62-97 / 158 | 0.415-0.607 | each under its own p95 | -- | **0/5 clear** |

**Verdict: non-test, not a negative.** The target misses the gate on every block (every true-gloss consistency sits
inside its own shuffled-gloss band), but so does the positive control on 10 of 10 seeds -- a synthetic block with the
correct decipherment beside it, at this gloss coverage (about 0.4 letters per sign surviving) and this N (83-158
signs), is not separated from a scrambled gloss by this instrument. The gloss alignment therefore cannot be tested
on this target with `tools/interlinear_align.py` until the coverage changes; rule 3 (control-before-target) and its
third-attempt clause both apply: this is the second attempt at the same instrument (NX-3151G, 26 Sept, line pairs,
tied its shuffle at 0.000; today, block pairs with a positive control, tied again) and is logged "untestable by
this method at this gloss coverage and N", not refuted. No key.tsv, no decode, no judge run (the gate was not
cleared, so running them would have produced numbers nobody can use). Tokens read this job: 0 (H 0, C 0, S 0, M 0,
I 0); the 306 draft signs stay a 45%-agreed transcription with an unsettled alphabet (22 symbol codes plus unk1-8).

Status stays `open` (rule 5): not `partial` (no margin over a control anywhere), not `closed-negative` (nothing here
is a passed-control negative, and cryptanalysis without the gloss is untried). Not a NEAR.md row.

**Next step (new material, not another knob).** Two things would change the coverage figure the positive control
says is the limit, and either is a job for a person or an archive, not a further machine pass: (a) the gutter-lost
gloss text -- a flat-opened or raking-light capture of f.60r/f.60v's inner margin (BnF reading room or a copy order,
REQUEST.md-shaped; the Gallica scan is the only image and the binding cut is in it); (b) the sign alphabet settled in
`tools/sign_sorter.py` by the owner (Usage 6: two machine passes disagree on 55% of the signs, well past the one-tenth
line that makes the next pass a person's). Re-run `align/likely5_align.py` only after one of these, and only if its
positive control clears at the new coverage first. Independently of the gloss, a homophonic/nomenclator family run
(`tools/family_run.py`, matched control) on the drafts is untried but would need (b) first for the same reason.
Row 15 (fr3151-seure-1558) was gated on this row clearing its control; it did not, so that row's Noailles-derived-key
step has no key to test.

Vision calls: 2 (gloss1 zoom, gloss3 zoom). Subagents: 0. Hosts this job: scienceblogs.de 1 (200),
archivesetmanuscrits.bnf.fr 1 (403, not retried), web search engine 7 queries; gallica.bnf.fr 0. Credit: D. Bourdeau,
cyphersolver (CC BY 4.0 text) for the letter's identification and the gloss citation; the 26 Sept NX-3151G worker for
the drafts and the subagent gloss read reused here.

## Web and blog check (LIKELY-5, 2 Oct 2026)

Run first because `tools/intake_gate_check.py` exited 1 on this step alone. Plain web searches (4): `Noailles "cardinal de
Lorraine" Venise 1558 chiffre`; `"fr. 3151" OR "français 3151" chiffre Noailles`; `"en mauluaise" "gouvernement" Noailles
Venise 1558 déchiffrement` (the most distinctive gloss phrase); `François de Noailles évêque de Dax ambassadeur Venise 1558
lettre chiffrée cardinal de Lorraine` (the folder's descriptive title). Hits: the BnF Archives et manuscrits record for
Français 3151 (ark:/12148/cc496140), whose search snippet lists a "lettre en chiffre" of François de Noailles, bishop of
Acqs, to the Cardinal de Lorraine, Venice, 13 Nov 1558 (and one to Henri II, 17 Oct 1558) -- the direct fetch answered
HTTP 403 so the record itself was not opened this job; the snippet names the item, not a decipherment. Wikipedia pages on
the Noailles brothers and the Lorraine cardinals; Charrière's Négociations (already read, above); the BnF copies volume
btv1b52527305r (Noailles/La Vigne Venice-Constantinople copies 1557-59, not opened: a copies register of the Levant
traffic, no cipher named). No hit carries a plaintext or decipherment of this letter.
Blog site searches (3): **Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne): no post names Noailles, Venice 1558 or
fr. 3151; the one plausible hit, "Wer löst diesen verschlüsselten Brief aus dem französischen Nationalarchiv" (17 May
2016), was opened with its comment thread -- it is an English-plaintext letter to Henry VIII read by Torbjörn Andersson
(29 Mar 2017), unrelated. **Cryptiana blog** (cryptiana.blogspot.com, cryptiana.web.fc2.com): the site search returned
nothing from either host for Noailles/Venice/1558/Lorraine; the local mirror (`sources/cryptiana/`) has no page for the
Venice posting (26 Sept check above). **Cipher Mysteries** (ciphermysteries.com): hits are Venetian/Milanese
fifteenth-century cipher posts, none naming Noailles or 1558; none opened beyond the result list since no title or
snippet touched the item. Result: no decipherment or plaintext of fr. 3151 no. 33 found in any open-web or blog comment
thread searched on 2 Oct 2026 (a search result, rule 10, not a novelty class).

## Premise check (GF4-BATCH5, 3 Oct 2026)

The adversarial pre-reading pass (`.claude/briefs/check-solved.md` "## Premise check"). Its aim was to show this
item is already read. No cryptanalysis or transcription was done. Result: **not found**. No decipherment, clear
copy or printed plaintext of no. 33's cipher turned up, apart from the period marginal gloss the folder already
records. Status unchanged (`open`).

- **(a) Decipherments the folder already mentions: found, already known, not a full reading.** The only one is
  the contemporary marginal gloss beside the three blocks. The 26 Sept and 2 Oct jobs above opened it on every
  block and read it as partial: gutter-cut, about 0.4 letters per sign surviving. It gives no full plaintext.
  Then the BnF finding-aid record for Français 3151 (ark:/12148/cc496140). Its search snippet calls the item
  "lettre en chiffre", not "avec déchiffrement" (2 Oct; direct fetch 403). Bourdeau's `bnf_candidates.txt` line
  quotes the same catalogue entry: "33 Lettre, avec chiffre, de F[rançois] de Noailles ... au cardinal de
  Lorraine ... De Venise, ce XIIIe jour de novembre 1558". This is the catalogue's wording, and the catalogue
  says "avec chiffre et déchiffrement" when a decipherment is bound with a letter (see fr. 4127 below). So the
  BnF does not record a separate decipherment for no. 33.
- **(b) Other solvers' working files: not found.** Fresh shallow clones on 3 Oct 2026: dbourdeau/cyphersolver
  HEAD a4292cb (2 Oct) and aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept). I grepped every file in both,
  case-insensitive, for "noailles", "3151", "français 3151" and "4127".
  - Bourdeau `targets/guiche1551/`: files NOTES.md, guiche_ct.txt, reading_raw.txt, solve.py, solve1.py,
    refine.py and profile.json. `reading_raw.txt` and the solvers are La Guiche's text only. NOTES.md §2 and
    Remaining gaps still read "the cipher itself (about 150 signs) ... not attacked" and "known-keys: not done --
    no French diplomatic key of the 1550s ... was tried on ... Noailles". Nothing in the repository renders
    no. 33.
  - Bourdeau's other "noailles" hits are unrelated: the gallica_sweep candidate lists and shelfmark JSON, a
    Mondoucet key JSON, and the Napoleon sources.
  - Aymeloglu: only false positives. A French lexicon word-list hit, and DECODE record id 4127 (a Riksarkivet
    key, not fr. 4127).
- **(c) Physical neighbours: not found.** Gallica btv1b9059865k, at 1000 px, fetched this pass:
  - Canvas 61, left page f.59v: plain-hand text in the same secretary hand. No cipher, no interlinear, no
    pasted slip. Facing page f.60r: the cipher blocks and gloss already recorded.
  - Canvas 63: f.61v carries a later title "Lettre du prince d'Est au duc de Guise" over a bleed-through ghost
    of f.62r. f.62r is an Italian letter from the prince d'Este, the next item. Neither leaf holds a decipherment
    or clear copy of no. 33.
  - Canvases 59, 60 and 62 were already surveyed on 26 Sept (survey/f59-f62). Canvas 62 holds f.60v, block 3
    with gloss 3, and f.61r, the address panel. The 26 Sept survey found no slip on either.
  - The f.60r/f.60v gutter is still the one unread place: the gloss starts are lost in the binding. That needs
    physical access and is already logged.
- **(d) Recipient side: no edition found; one sibling source located.** The recipient is the Cardinal de
  Lorraine. Cuisiat 1998 holds his outgoing letters only (26 Sept). The IA full-text search (be-api, all items)
  found no edition of letters received by Lorraine that prints this letter. Queries run: `"evesque d Acqs" Venise
  1558`, `"Noailles" "Corfou" "Candie" 1558` and `"de Venise ce" "novembre 1558"`. Hits were de Thou, Charrière's
  Levant volume, Jurien de La Gravière, and a Library and Archives Canada Noailles-collection catalogue
  (baclac_1007364698_002, England embassy). None prints the 13 Nov letter. Three things came out of the search:
  - The third query hit the **BnF Catalogue des manuscrits français, ancien fonds, tome III** (1881; IA
    `p1cataloguegnr03bibluoft`, djvu text grepped whole). Its entry for **Français 4127** reads "Recueil de
    lettres originales et de copies de lettres adressées au S' de La Vigne, de 1557 à 1559". That is 68 letters
    from François de Noailles at Venice to La Vigne at Constantinople, dozens marked "Avec chiffre et
    déchiffrement" or paired with a "Copie et déchiffrement de la lettre précédente". Nearest in date:
    - no. 50, 7 Nov 1558, "avec chiffre et déchiffrement", fol. 137;
    - no. 51, 15 Nov 1558, fol. 142;
    - no. 53, 3 Dec 1558, chiffre et déchiffrement, fol. 147.
    These are **not** this item; they are another correspondent's letters, and the key may differ. They are the
    same sender in the same weeks, with period decipherments bound beside the ciphertext. That is a candidate
    key source (a sibling pool), not a reading of no. 33.
  - A Gallica SRU query for "Français 4127" (title/identifier) returned no record. That is a search result, not
    proof the volume is undigitised. Its catalogue record's availability flag was not read this pass.
  - The same catalogue lists a register of La Vigne's own outgoing letters, Henri II to Lorraine 1558. It is not
    a decipherment of Noailles.

**Next step this premise check names (not run, outside this brief).** Read the holding record of BnF fr. 4127
and quote its availability flag. If it is digitised, test whether the Noailles-La Vigne decipherment pairs of
Nov 1558 (nos. 50 and 53) share no. 33's symbol+numeral alphabet. Use a sign-inventory comparison, not a decode.
If the alphabets match, a period key (`period`) exists for this item and the target moves to the recovery
route. Estimated cost: about $3 for the catalogue read and one leaf survey.

Hosts this pass: archive.org advancedsearch 3, be-api.us.archive.org 3, archive.org download 1 (catalogue djvu
text), gallica.bnf.fr 3 (SRU 1, IIIF 2 at 1000 px), github.com 2 clones. All requests were at least 1.6 s apart,
with no 403, 429 or challenge. Rule 10: this is a search log; it makes no novelty claim.

`python3 tools/intake_gate_check.py fr3151-noailles-1558` (after this section):
```
fr3151-noailles-1558: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## FT4-fr3151-noailles-1558 (3 Oct 2026, account-4)

The step: the step the Premise check above names. Read BnF fr. 4127's holding record and quote its availability
flag. If it is digitised, compare the design of its Nov 1558 cipher-and-decipherment letters with no. 33's. Do not
build a key or decode anything.

**Holding record, read 3 Oct 2026, ~02:1x UTC.** BnF Archives et manuscrits, **Français 4127**,
`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc50527m` (FRBNFEAD000050527). It reads "Anc. 9291(17), de La Mare 151 •
Recueil de lettres originales et de copies de lettres adressées au Sr de La Vigne, de 1557 à 1559". Items 1-68 are
"Soixante-huit lettres de « F[RANÇOIS] DE NOAILLES, e[vêque] d'Acqs... ambassadeur de France à Venise... à Mr de La
Vigne »". The notice was "créée à partir de la conversion rétrospective du Catalogue des manuscrits français, tome
troisième ... 1881". The record confirms the folio list the Premise check read from the 1881 print. Items nearest the
target's date, quoted from the record:
- Fol. 131, no. 48: "Avec chiffre et déchiffrement", 7 Oct 1558
- Fol. 135, no. 49: same, 20 Oct 1558
- **Fol. 137, no. 50: same, 7 Nov 1558**
- Fol. 142, no. 51: 15 Nov 1558, no cipher noted
- Fol. 145, no. 52: 24 Nov 1558
- **Fol. 147, no. 53: chiffre et déchiffrement, 3 Dec 1558**
- Fol. 152, no. 54: same, 10 Dec 1558

The series runs from Dec 1557, with separate "Copie et déchiffrement" items (e.g. nos. 3, 4, 6, 9, 12, 14, 17, 22,
38). By the catalogue's count about 45 of the 68 letters carry cipher.

**Availability flag: no digitisation link.** Neither the record page nor its "Informations bibliographiques" panel
(`ajaxGetCompDisplay.html?eadCompId=FRBNFEAD000050527_info`) carries a Gallica link or a `DaoGal` element: 0
matches for `gallica.bnf.fr/ark` or a `DaoGal` class. The class appears only in the page's CSS.
- **Control that can differ:** the same fetch and grep on the record for **Français 3151**
  (`ark:/12148/cc496140`), which is known to be digitised, finds 4 matches and the link
  `gallica.bnf.fr/ark:/12148/btv1b9059865k`.
- **Second test:** a Gallica SRU query `dc.source all "Français 4127"` returns 0 records. The identical query for
  `"Français 3151"` returns 1 (btv1b9059865k). Title queries ("La Vigne" + manuscrit, 51 records; "Vigne 1557")
  return no record for fr. 4127. They do find a different, digitised Noailles volume: **Français 10773**, "Copies de
  pièces et de dépêches relatives aux négociations à Venise et à Constantinople de François DE NOAILLES ..."
  (`https://gallica.bnf.fr/ark:/12148/btv1b52527305r`).

Conclusion: as of 3 Oct 2026, fr. 4127 has **no online reproduction**. The holding record carries no viewer link,
and Gallica's index has no record. This is an availability result, not a statement about the manuscript.

**Design comparison: not run (non-test).** There are no fr. 4127 leaves to look at, so I made no vision calls and
fetched no IIIF image. The pre-registered comparison was a shape inventory of no. 33's pen-signs (sign_legend.md
codes) plus two-digit numerals against fr. 4127 no. 50's cipher. The control was an unrelated 1550s table. That
comparison stays unrun; it is not a negative. Whether fr. 4127 uses no. 33's key is still unknown.

**Next step, cheapest first.**
- (a) **Depends on nobody, ~$2.** Survey Gallica's fr. 10773 (digitised copies of Noailles's Venice and
  Constantinople dispatches) for:
  - a copied cipher alphabet or key table;
  - deciphered copies of the Nov 1558 letters;
  - any copy of the 13 Nov 1558 letter to Lorraine.
  Method: canvas labels first, then at most 2 vision calls at 1000 px on the leaves whose labels point there. This
  is a shape-free search for a key source or clear text. It is not a design test.
- (b) **The owner's step.** Order a reproduction of fr. 4127 fols. 131-151 (nos. 48-54), at least fol. 137 (no. 50,
  7 Nov 1558, chiffre + déchiffrement), through the BnF reproduction service (manuscrits@bnf.fr / SINDBAD). Once the
  images arrive, the design comparison above runs as pre-registered (~$3). If the designs match, a `period` key
  rebuild from the cipher/decipherment pairs follows (~$6-10).

I did not write an ASKS row in this job: step (a) comes first, and the parent decides whether to put (b) on the
owner's card.

Requests this job: archivesetmanuscrits.bnf.fr 5 (home, 1 search POST, 2 record pages, 1 info panel); gallica.bnf.fr
6 (SRU only: 5 queries plus 1 control; no IIIF). All were at least 1.6 s apart, with no 403, 429 or challenge.
Vision calls: 0. Rule 10: this is a search and availability log; it makes no novelty claim.

## While waiting (FT4-fr3151-noailles-1558, 3 Oct 2026)

- Survey the digitised Gallica fr. 10773 (btv1b52527305r: copies of Noailles's Venice/Constantinople dispatches) for a copied cipher alphabet, a key table or deciphered copies of the Nov 1558 letters: canvas labels first, then at most 2 vision calls at 1000 px, ~$2. This depends on nobody, unlike the fr. 4127 reproduction order. Done: IMG-GALLICA1 (3 Oct 2026) and D22-F3151D (6 Oct 2026, below): fr. 10773 is La Vigne's Constantinople register and holds no copy of the 13 Nov 1558 letter.

## IMG-GALLICA1: fr. 10773 survey (3 Oct 2026, account 2 worker for LANE-IMAGES)

Step (a) of the FT4 next-step list. Brief `.claude/briefs/runs/2026-10-03-acct2-img-gallica1.md`. No transcription,
no decoding.

**Availability flag quoted.** Gallica ark:/12148/btv1b52527305r, manifest
`https://gallica.bnf.fr/iiif/ark:/12148/btv1b52527305r/manifest.json`. The manifest metadata reads: "Français 10773
... Copies de pièces et de dépêches relatives aux négociations à Venise et à Constantinople de François DE NOAILLES,
évêque de Dax, et de Jean DE LA VIGNE. (1557-1559)"; Date "1601-1700"; "Papier. - 104 feuillets". The catalogue
record is archivesetmanuscrits.bnf.fr ark:/12148/cc42278j (FRBNFEAD000042278, "Supplément français 252"), fetched
once, HTTP 200. It is a single-level record with **no item list and no folio-by-date breakdown**.

**Canvas labels.** `tools/gallica_folio.py btv1b52527305r --list` gives 226 canvases: 208 with a folio label
(1r-104v, consecutive) and 18 without (binding, endleaves, and two NP slips at c116-117).

**Survey.** I fetched all 226 canvases at 200 px. Two contact sheets at 996 px wide (113 canvases each, about 83 px
per page) used the 2 vision calls. They are committed as `images/fr10773_survey/sheet_f10773_{1,2}.jpg`, with
per-canvas classes in `images/fr10773_survey/canvas_classes.tsv`.

| class | canvases |
|---|---|
| clear (continuous prose) | 200 |
| blank | 11 |
| binding | 13 |
| NP slip | 2 |

**Result.** At this scale no canvas shows a key table, a cipher alphabet, a grid or a numeral-dense block. Every
written page is the same 17th-century copy hand in continuous prose, with occasional marginal notes. That fits a
register of clear copies, not of cipher.

**Not found and not tested:**
- Dates. At about 83 px per page no date heading can be read, so whether fr. 10773 holds a clear copy of the Nov 1558
  letters, including no. 33 of 13 Nov 1558 to Lorraine, is **not established**.
- Images. No native image or crop was fetched, because the brief allows that only for a key table or a Nov 1558
  cipher or decipherment page, and none was identified.

A clear copy of no. 33 would be a C-grade crib source. Finding one needs a date-locating pass that reads the copy
headings at about 1000 px. This is a separate job, not this brief.

**Requests:**
- gallica.bnf.fr: 227, all one at a time and at least 2 s apart: 1 manifest plus 226 thumbnails. The thumbnail run
  was paused once at 108/226 to serve the clair1161 job and then resumed. There was one transient
  "RemoteDisconnected" on c19, which succeeded on its single retry. No 403, 429 or altcha.
- archivesetmanuscrits.bnf.fr: 1.

Vision calls: 2.

Next step (one line, not actioned): a date-locating pass over fr. 10773, reading copy headings at about 1000 px by
bisection on the folio labels (about 6-8 leaf views, about $2). Its aim is a clear copy of the 13 Nov 1558 letter to
Lorraine, or of fr. 4127's Nov 1558 letters. FT4's (b), the fr. 4127 reproduction order, stands unchanged.

## D22-F3151D: fr. 10773 date-locating pass (6 Oct 2026, 22:17-22:2x UTC, account 2 worker for LANE DEFAULT-account-2-20261006-2209)

The step IMG-GALLICA1 named: locate Nov 1558 in Gallica fr. 10773 (btv1b52527305r) by reading copy headings and date
lines, and find a clear copy of no. 33 (Noailles at Venice to the Cardinal de Lorraine, 13 Nov 1558) if it is there. No
alignment to the cipher, no decoding.

**What the volume is.** Every heading read is a letter *by* Jean de La Vigne at Constantinople (to the king or to
Noailles) or a letter *to* La Vigne; none is a letter by Noailles. Read by this worker at about 900-1000 px:

| folio (canvas, 0-based) | heading or date line read | date |
|---|---|---|
| 1r (c6) | "Discours que je donnai au Grand Seigneur a l'occasion de la venue du sieur de Boistaille" (top margin "Nouvelles acq. D.") | undated |
| 13r (c30) | Italian letter ending "Constantinopoli. Alli 24 di Maio 1558" | 24 May 1558 |
| 27r (c58) | "Lettre a Monsieur l'Evesque Dags Ambassadeur a Venise du 4 fevrier 1557" | 4 Feb 1557 (old style, = 1558) |
| 31r (c66) | "Extrait d'une lettre de Monsieur de La Vigne escritte au Roi le 28 decemb. 1557 d'Andrinopoli" | 28 Dec 1557 |
| 52r (c108) | mid-letter, no date on the leaf top | -- |
| 65r (c136) | "Lettre a Monsr l'Evesque Dags du 19 Juin 1558" | 19 Jun 1558 |
| 71v (c149) | king to La Vigne, "Escrit a Laon le treizieme jour d'Aoust 1558", signed Henry / Duthier, then a postscript to La Vigne | 13 Aug 1558 |
| 77r (c160) | "Autre au meme du 29 septemb. 1558" | 29 Sep 1558 |
| **83r (c172)** | letter ends "A Constantinople le 10 Novemb. 1558"; next heading "Autre au Roy du 14 novembre 1558" | **10 and 14 Nov 1558** |
| **85r (c176)** | that letter ends "A Constantinople le 14 novemb. 1558"; next heading "Depesche au Roy du 7 fevrier 1559" | **14 Nov 1558, then 7 Feb 1559** |
| 89r (c184) | mid-letter (the 7 Feb 1559 dispatch) | -- |
| 93v (c193) | "Lettre du Monsr de La Vigne Ambassadeur pour le Roy de France vers le Grand Seigneur, A Monsr l'Evesque d'Acques, escritte le 20 mars 1559 de Constantinople" | 20 Mar 1559 |
| 97r (c200) | "Lettre de Monsr de La Vigne a Monsr d'Acques du 19 may 1559" | 19 May 1559 |

From f.17r on the copies run in date order (Dec 1557 to May 1559). Folios 1-16 are a front section of discourse and
documents; only one date was read there (24 May 1558, f.13r). Leaves 84r-90v (c174-c192, 17 leaves) were viewed whole
at 500 px by this worker's own eye for headings only. The only Nov 1558 copies in the volume are La Vigne's own two
letters, 10 Nov 1558 (ending f.83r) and 14 Nov 1558 to the king (f.83r-85r). Then the volume jumps to 7 Feb 1559.

**Result: fr. 10773 holds no copy of no. 33.** It contains no Noailles-to-Lorraine letter of 13 Nov 1558, and no other
Nov 1558 letter by Noailles. This is conditional on the 13 heading and date points above and the 17-leaf heading scan
of f.84-90. Folios 1-16 and the stretches between bisection points were not read line by line. But the dated run is
monotone and is one sender's register, so a Noailles dispatch to Lorraine would be out of genre there. Two
cross-references were seen in passing and not transcribed in full. On f.85v-86r, La Vigne's 7 Feb 1559 dispatch
mentions letters received from "Mons. Dax" of 10 Dec and "vos depesches du 26 novemb." These are other letters, not
no. 33.

**Crops saved** (`tools/iiif_lines.py --ark btv1b52527305r --canvas N --region ... --debug`, manifest
`images/fr10773_dates/manifest.json`; the overlays were checked by eye):
- f.83r, canvas 173 (1-based), region 300,950,2600,750. This is the end of the 10 Nov letter plus the "Autre au Roy du
  14 novembre 1558" heading: 5 lines, 10 crops.
- f.85r, canvas 177 (1-based), region 200,2700,2800,700. This is "A Constantinople le 14 novemb. 1558" plus the
  "Depesche au Roy du 7 fevrier 1559" heading: 4 lines, 8 crops.

First and last lines of a no. 33 copy are not transcribed, since none was found.

**Requests.** gallica.bnf.fr 37, one at a time and at least 2 s apart:
- 31 leaf views (IIIF, 500-1000 px, the heading region or the whole leaf);
- 2 info.json;
- 3 native region fetches by iiif_lines. One of them missed the date line and was deleted and refetched.

There was no 403, 429 or altcha. Vision subagent calls: 0, since every view was read by this worker's own eye. Rule
10: this is a search log; it makes no novelty claim.

[done 6 Oct 2026, D22-FTS2: no other digitised Noailles Venice register found; see section D22-FTS2 below] Next step (was): Gallica SRU search for another digitised register of Noailles's own Venice dispatches of 1558 (dc.title or dc.source with "Noailles" and "Venise", plus BnF archivesetmanuscrits for "Noailles" "1558" copies), then a date check of any hit's Nov 1558 copies, ~$1.5; FT4's (b), the owner-side fr. 4127 fols. 131-151 reproduction order, stands unchanged and is still the route to a period cipher+decipherment pair of the same weeks.

## D22-FTS2 (6 Oct 2026)

Item 2 of D22-FTS2 (Sonnet worker, 22:4x UTC, for LANE DEFAULT-account-2-20261006-2209): the step D22-F3151D named, catalogue search and heading checks only, no alignment to the cipher. Grade I.
**Gallica SRU** (`gallica.bnf.fr/SRU`, version 1.2, 4 queries, 2.2 s apart): `gallica all "Noailles Venise 1558"` 3935 (noise; includes Tamizey de Larroque, *Lettres inedites de Francois de Noailles, eveque de Dax*, 1865, `bpt6k97359942`, an edition of his letters, not opened this job); `dc.title all Noailles and dc.title all Venise` 4 records: (a) `btv1b52527305r` = fr. 10773, already read (D22-F3151D: La Vigne's Constantinople register, no Noailles letter, no 13 Nov 1558 copy); (b) `btv1b9057247z`, Collection du marechal de Noailles, *Lettres adressees au president de Thou ... de Venise* (1601-1631), wrong period; (c, d) `btv1b10089718w` (387 canvases, no folio labels, all "NP") and `btv1b105073498` (753 canvases, 717 labelled, printed page 1 = canvas 7), two copies of Vertot's *Relation des ambassades des seigneurs de Noailles en Angleterre, en Ecosse, a Venise, en Pologne, a Constantinople* (ms made 1714, 708 pp.); `dc.title Noailles and dc.date 1558` 0; `dc.title depeches and Noailles and dc.type manuscrit` 1 (= fr. 10773 again).
**Vertot ms heading checks** (`btv1b105073498`, IIIF native 800-900 px full leaves, read by this worker's own eye, 5 views): p.1 (canvas 7) is "Le dessein de cet ouvrage avec une Relation sommaire de la vie et des principales actions des trois seigneurs de Noailles", a prose narrative; p.292 (canvas 300) and p.430 (canvas 450) are narrative on the English embassy (Cranmer/Gardiner, 1550s marriage negotiations) with marginal notes giving the dates of the dispatches used ("Dep. du 23 xbre", "Dep. du 26 xbre"; Rymer cited). It is a narrative with marginal citations, not a register of Francois's Venice dispatches, and the Venice section was not located in these 5 views (not bisected further). No copy of no. 33 seen.
**BnF Archives et manuscrits** (browser tool: curl POST answered 405 on `/` and `/pageAccueil.html`, one retry on a second path, then `tools/browser_fetch.js --type "#TEXTE_LIBRE_ID1=..."`; the first two browser tries failed on fill/navigation, the third returned): `Noailles Venise 1558` 82 results. Items bearing on Francois's own letters: (i) fr. 3151 itself (cc496140: no. 14, 17 Oct 1558 to the king; no. 33, "Lettre, avec chiffre ... au cardinal de Lorraine ... De Venise, ce XIIIe jour de novembre 1558", the target); (ii) fr. 4127 (cc50527m, 68 letters of Noailles to La Vigne, already FT4's); (iii) **Cinq cents de Colbert 391** (cc91752x, Bochetel correspondence vol. II, Gallica `btv1b100339431`, 134 canvases, none labelled): "p. 81: Francois de Noailles, eveque de Dax, ambassadeur a Venise, 1558" (one item); (iv) Cinq cents de Colbert 395 (Gallica `btv1b10033947t`): a report by Noailles on the precedence quarrel with the Spanish ambassador, 23 Apr 1558 (p.345, in the finding-aid text); (v) Cinq cents de Colbert 394 (`btv1b10033960h`): "F. de Noailles, e. d'Acqs, 1559" (one item); (vi) a second La Vigne register, cc50523n (letters *from* La Vigne to Noailles, Jan-Dec 1558, including 10, 20 Nov and 19 Dec 1558: letters to him, not by him).
**Heading check for (iii)**: spread views of canvases 42, 44, 46 (the page numbers 81, 85, 89 are written on the right-hand leaf; canvas 42 = p.81). p.81 opens "Sire, Lundy dernier voyant ces seigneurs que la feste de l'ascension approchoit ..." (a letter to the king about the Spanish ambassador's precedence at the Ascension ceremony, i.e. May 1558, original script, no cipher seen); p.85 is a letter to the cardinal de Tournon; p.89 is a 1560 letter. So it is neither a Noailles letter to Lorraine nor a Nov 1558 copy. No other digitised Noailles Venice register found for Nov 1558.
Result: no other digitised register of Noailles's own Venice dispatches turned up in these searches (Gallica SRU, BnF A&M `Noailles Venise 1558`, 82 results scanned by title); fr. 10773 and the two Vertot copies and Colbert 391 p.81 do not hold no. 33; fr. 4127 ff.131-151 (owner-side reproduction) stays the route to a cipher/decipherment pair of the same weeks. One untried digitised lead: the Colbert 395 p.345 report (23 Apr 1558, not Nov). One edition not opened: Tamizey de Larroque 1865 (`bpt6k97359942`; ~USD 0.5 to grep its letters for Nov 1558 by IA/Gallica full text). Not a novelty verdict (rule 10). Requests: gallica.bnf.fr 15 (SRU 4, manifests 3, native/IIIF images 8), archivesetmanuscrits.bnf.fr 9 (2 GETs, 2 POSTs refused 405, 3 browser attempts, 1 record page, 1 more GET), no 403/429/altcha.
