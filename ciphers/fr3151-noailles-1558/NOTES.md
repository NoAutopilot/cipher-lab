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
