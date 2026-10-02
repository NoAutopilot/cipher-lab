blocked

# fr.3986 f.198 (Nevers -> Revol, 23 Oct 1593) — Louis de Gonzague, duc de Nevers, to Louis Revol

Status: **open**

Checked by LANE N4 csKSa (check-solved), 24 Sept 2026, following `.claude/briefs/check-solved.md` and
`.claude/briefs/runs/2026-09-24-lane-n4-csKSa.md`. Row KS-03 from
`sources/solver-diffs/2026-09-24-keys-vs-siblings.tsv`.

## 1. What is established

- BnF fr.3986, same "Collection Mémoires de la Ligue" Rome-embassy series as fr.3985. Gallica ark
  `btv1b9060631k` (481 canvases, all "NP").
- Sender: Louis de Gonzague, duc de Nevers. Recipient: Louis Revol.
- Key: Tomokiyo's no.60, same as fr.3985 (see that target's NOTES.md for the key description). Kind:
  **recovery**.

## 2. Leaf confirmation (this session)

The TSV's canvas estimate (397, from a ~1.7-2x-folio guess) was explicitly flagged unconfirmed -- Bourdeau's
own session never reached this canvas (his fetcher was throttled, HTTP 429, and stopped at c.388). Confirmed
this session:

- Canvas 397: no visible folio stamp on the recto itself (top-right corner is blank/cropped at this
  resolution), but the **facing verso, canvas 398, is stamped "199"** top right
  (`images/probe_c398.jpg`, `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060631k/f398/full/,1000/0/native.jpg`)
  -- confirming canvas 397 = **folio 198**, matching KS-03 exactly.
- Canvas 397 (`images/f198_canvas397_try.jpg`,
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060631k/f397/full/,1000/0/native.jpg`) carries running clear
  French text with short cipher passages inserted inline (not a full-page cipher block like fr.3985's two
  leaves) -- e.g. one line of Tomokiyo's no.60 symbol/figure mix, `images/f198_crop_mid.jpg` (native crop,
  `.../f397/0,2500,4948,1200/2200/0/native.jpg`): "...45 10 5 H p 4 61 g d H v q 11 3 7 d + o 4 q 11 3 6 g 4 44
  4T...". Margin "+" marks appear beside some lines (insertion/correction marks, not a decipherment). Checked a
  second high-res crop of the page's top third (`images/f198_crop_top.jpg`,
  `.../f397/0,450,4948,1300/2200/0/native.jpg`): pure clear text there, no cipher, no interlinear gloss over
  any cipher group anywhere checked on this leaf (the Thurloe/Birch/Gondi check).
- Could not independently confirm the date "23 Octobre 1593" from the crops taken (the date line, if present,
  is likely at the top of the letter's first leaf, not on f.198 which reads as a continuation page); the
  folio-198 identification itself is solid via the facing-verso stamp.

## 3. Six-source check-solved sweep

Same sweep as fr.3985 (see that target's NOTES.md section 3 for full detail on each source); result for this
specific letter:

1. **Web**: no hit for fr.3986 f.198 specifically.
2. **Print**: Gomberville seconde partie (Google Books `H2eV4wAmIr0C`) search-within for "Revol" (5 hits, none
   dated Oct 1593) and "Octobre 1593" (not separately queried this pass -- see gap note below); Berger de
   Xivrey vol.3 (archive.org `recueildeslettre03henr`) and Memoires de la ligue v.5-6 (archive.org
   `memoiresdelaligu05goul`/`06goul`) full-text "Revol" hits are all different letters (see fr.3985 NOTES.md).
   Letter absent from all three as far as searched.
3. **Cryptiana**: `nevers.htm` names no.60 only generically ("used in many letters in BnF fr.3985 etc."),
   `henryiv2.htm` not cached, not fetched this session.
4. **DECODE**: `sources/decode/` grepped, no hit.
5. **Bourdeau**: `nevers1593/NOTES.md`, "Remaining gaps", verbatim: "fr. 3985 f. 88 (21 Aug), f. 115 (27 Aug,
   one line), f. 176 (2 Sept, no. 88/94), **fr. 3986 f. 198 (23 Oct, no. 101)** - blocker: not-attempted;
   located and cut but never transcribed; key no. 60 is fully in hand." His session located and cropped this
   leaf but never transcribed or decoded it.
6. **Aymeloglu**: repo grepped for "3986"/"Revol"/"Nevers", no hit (his Nevers-cipher rows are fr.3623, fr.3616,
   fr.3975, fr.3979, fr.3976 -- different items).

**Gap for the next pass**: an "Octobre 1593" / "23. iour d'Octobre" date-phrase search in Gomberville was not
run this session (budget); worth a quick follow-up before this leaf is transcribed.

## Verdict

KS-03: **open -- Gomberville seconde partie (Google Books H2eV4wAmIr0C) search-within read for "Revol", Berger
de Xivrey Recueil des lettres missives de Henri IV vol.3 (archive.org recueildeslettre03henr) full-text read for
"Revol", Memoires de la ligue (Goujet) v.5-6 (archive.org memoiresdelaligu05goul/06goul) full-text read for
"Revol", letter absent from all three; Bourdeau's own "not-attempted" gap list confirms unread.**

Grade: no reading exists yet. Kind: **recovery**. This session does not apply the key or read the letter.

## Credit

Key no.60: Satoshi Tomokiyo (`nevers.htm`), Daniel Bourdeau (CC BY 4.0, `key60.txt`; also the folio-198
location, cropped but unread in his session scratch).

## Next step (one line)

Run the "Octobre 1593" date-phrase search in Gomberville before transcribing; then transcribe against
`key60.txt` (LANE R5), noting the leaf mixes clear and cipher rather than being solid cipher throughout.

## Key no.60 applied (24 Sept 2026, LANE R5 F2)

Key: `key.tsv`, cipher no.60 (Satoshi Tomokiyo's reconstruction and numbering, BnF fr.3995 ff.109-111, henryiv2.htm), from
Daniel Bourdeau's transcription `nevers1593/key60.txt` (github.com/dbourdeau/cyphersolver @a0d5a07, text CC BY 4.0), mapped
to the ASCII sign tags of `sign_guide.md`; a row carries H where the table gives one value, M where the table gives two
(e.g. `4` x in the table, i in Bourdeau's crib atlas; `#`, renamed `dbl`, n or m). Shared content with fr3987/fr3986 (same
file in both folders). Images: Gallica IIIF image API only, one native region per leaf (`images/manifest.json`), line cuts
by `tools/iiif_lines.py` (debug overlay checked). Pass A: Opus worker F2, read against the key's sign list; pass B: one blind
Sonnet subagent; `tools/reconcile_passes.py` gave `passes/ciphertext_draft.tsv`, copied unchanged to `ciphertext.tsv`
(disagreements NOT settled on the image: at this agreement rate settling them is a glyph-atlas job, see below).
Reading: `python3 tools/decode_key.py ciphers/<t>` (decode.json), `--check` exits 0. No interlinear or marginal
decipherment on the leaf (the margin '+' marks are insertion marks).

fr.3986 f.198 (canvas 397): continuation leaf, clear text with short inline cipher runs; the letter's close ("... le 23
[octobre] 1593") is at crop line L21-22, then a postscript in clear. Cipher found in crop lines L05, L07, L09, L10, L13,
L15 (the longest run, ~32 signs), L16, L18, L19. Pass agreement 27/66 = 40.9% (A 64 signs, B 53). Tokens graded:
**H 5, M 56, U 5, I 0** (66). L09 ends "de R phi phi+" = "de [Duc de Mantoue] [Duc de Ferrare|ca] [?]" (M: the passes
disagree on R). The rest gives letter strings only.

Result: the key applied sign by sign does **not** give a continuous reading. The blocker is the one Bourdeau recorded on
17 Sept 2026 ("the copyist's cursive forms map to two or three table entries each"): the Revol copyist writes no.60 in
a cursive whose shapes the two passes cannot even agree on, and many shapes have more than one table value. Status stays
`open` (no reading; a mechanical application is not one). Grade I: 0 (nothing repaired).

Suggestion (one line, not done): build the copyist glyph atlas from the interlined Instruction of 31 Aug 1593 (fr.3985
c.264-268, same hand, printed in Memoires de Nevers ii 492-499) as Bourdeau's 'Next pass' says, then re-run both passes
with atlas tags instead of table shapes; only then settle `passes/disagreements.tsv` on the image.

## Status blocked (24 Sept 2026, 20:52 UTC, LANE R5 orchestrator)

Key no.60 applied mechanically by LANE R5 F1-F3 does not read: blind pass agreement 37-55%, blocked on identifying this copyist's sign forms, not on the key. Next: LANE R5 G builds a no.60 sign atlas from the interlined leaves of the same copyist (fr.3985 f.126-130, fr.3986 f.151/152) and re-runs F1's leaves; if that passes 80%, this letter follows.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/nevers1593/NOTES.md
- Their extent, in their words: as fr3985 above: Revol letters in cipher no. 60, not read; f. 157v copy in clear
- Their date: 17 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## LIKELY-6 (2 Oct 2026, account-4)

Worker LIKELY-6-fr3986-nevers-revol-1593 (Fable 5.1, session_01JK2W3H3Pu8P9Y9DftjnerN), brief
`.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`, row 6 of `ciphers/_triage/likely-solves-2026-10-02.tsv`.
Clock read 06:06-06:2x UTC. Disk only: 0 requests to Gallica or any host; 1 vision call (of 5 allowed).

**Intake gate**: `python3 tools/intake_gate_check.py fr3986-nevers-revol-1593` -> "blocked (line 1) -- already terminal,
nothing to gate", exit 0. The status word is `blocked` with an internal blocker (sign identification for this copyist, LANE
R5, 24 Sept 2026), which is the row's own first cheap test, so the test ran. Note for the next check-solved pass: this
NOTES.md has no "## Web and blog check" section (check-solved.md's required step of 28 Sept 2026); the gate did not test
for it because `blocked` is terminal, and it is owed before any `open`/`partial` verdict.

**Test as the row names it, known answer first.** The no.60 atlas already on disk (`tools/keys/key60_atlas/`, LANE R5 G,
80 pairs from fr.3985 c.264 and fr.3986 c.298) had been measured only by pass agreement (G2: 39.8% on f.176), never
against a known answer. Leaf-level hold-out: the atlas was reduced to its 52 leaf-264 pairs
(`tools/keys/key60_atlas/contact_sheet_264only.png`, `atlas264.tsv`; the 298-derived conflict rows 20/ro and L40/Lo
withheld too), and leaf 298 (f.152, Henri IV to Nevers, Oct 1593; 28 signs with G's gloss alignment, grade S) was the
held-out answer key. Five sub-span crops at +-42 px native around the sign row (gloss masked; eye-checked, only stray
ascenders leak at the edge), x3, in `atlas_heldout/ho_*.png`. One blind Sonnet pass (`atlas_heldout/heldout_passB.tsv`),
given only the sheet, the table and the crops. Score (`atlas_heldout/score.txt`, regenerated by
`atlas_heldout/heldout_score.py`, exit 0):

| | number |
|---|---|
| held-out sign-read rate (order-preserving tag match) | **19/28 = 67.9%**, Wilson 95% CI 49-82% |
| matched control: the pass's own tags permuted within crop, 2000 draws | mean 42.4%, p95 50.0%, max 64.3% |
| gate (row 6) | 80% |
| on tags the 264-only atlas shows | 9/10 = 90% |
| on the 8 tags it lacks (`// 20 8 = L40 c r ue`) | 10/18 = 56% |

Reading: the pass sits above its shuffle floor (so the atlas carries real information) and below the gate. The split is
the useful part: where the atlas has an exemplar the blind pass reads the neat 298 hand at 90%; the misses are almost all
signs the 52 leaf-264 pairs never show (`r`, `20`, `ue`, `//`, a final `8` twice, `do` taken for `alpha`). The gap is atlas
coverage, not the method -- and 298 is the neater hand; the Revol copies (f.198) are harder, so an f.198 pass against this
atlas would read below 68%.

**f.198 passes not run.** The gate failed before the target, so the two blind passes + adjudication, the decode vs 20
shuffled keys and the fr16 judge were not run (rule 3's control-first order, the ARM-S3 paragraph: a calibration that
misses its tolerance stops the job before any candidate is scored). Rule 3's third-attempt clause now applies to "another
pass on a Revol copy with the atlas as it stands" (F1/F2 without the atlas, G2 with it, this held-out): that step is
[retired] until the atlas changes. Grades: no new reading, so no new token grades; the 24 Sept draft stands at H 5, M 56,
U 5, I 0 (66), unchanged.

Status word stays **blocked** (internal: sign identification), the blocker now measured. Spec written:
`specs/fr3986-nevers-f198.json` with `cheap_test_done`. HYPOTHESES.md row added.

## Premise check (GAPS-fr3986-nevers-revol-1593, 2 Oct 2026)

Adversarial pre-reading pass per `.claude/briefs/check-solved.md` "Premise check" (a)-(d), run before the Verdict step. Clock
read 14:19-14:4x UTC 2 Oct 2026. Rule 10 wording throughout: "not found" is a search result, never a novelty verdict.

- **(a) the folder's own mentions -- found, none of them a decipherment of f.198.** The two "interlined" sources this folder
  and fr3985's name are period office decipherments of *other* leaves: fr.3985 ff.126-130 is Henri IV's Instruction to
  Nevers of 31 Aug 1593 (cipher from f.130, canvases 264/266/268, gloss above each cipher line), printed in clear in
  Memoires de Nevers (1665) ii 492-499 -- Bourdeau's `instruction_31aug_print.txt` carries the OCR of Gallica
  bpt6k64451005 views 541-548, and the gloss on c.264 matches p.498 word for word (checked this pass on the lines
  "soient quites et absoulz du serment de fidelite qu'ilz luy auront preste / La troisiesme ... / que a l'advenir
  promettre et jurer a leur sacre"); fr.3986 ff.151-152 is Henri IV to Nevers, Chartres 7 Oct 1593 (canvases 296-298),
  interlined. Tomokiyo's henryiv2.htm lists further interlined Henri IV letters in no.60 (fr.3985 f.204; fr.3986 ff.58,
  174, 191) -- all king-to-Nevers, none is f.198. f.198 itself: Tomokiyo's league.htm lists it as "no.101 (fol.198)
  Duke of Nevers to Revol, Desanzan, 23 October 1593" among the letters "partially in cipher no.60" with no
  decipherment noted; the 24 Sept 2026 native crops of the verso show no interlinear or marginal gloss (the '+' marks
  are insertion marks); Bourdeau's "f. 157v copy in clear" is no.75 (Coire, 9 Oct 1593), a different letter.
- **(b) other solvers' working files -- not found.** Fresh shallow clones 2 Oct 2026: dbourdeau/cyphersolver HEAD
  34e0fc8 (1 Oct 2026): `targets/nevers1593/` holds transcriptions only for f.209, f.146v, f.157v, f.168 and the two
  decoders; f.198 appears only in the "not-attempted; located and cut but never transcribed" gap line (his canvases
  396-398 for no.101 came from his folio ratio, his fetcher stopped at c.388); `atlas60.md` and `key60.txt` are key
  material, not a reading. aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept 2026): no fr.3986 row anywhere (his
  Nevers rows are fr.3623, 3616, 3975 and Spanish-archive calendar entries).
- **(c) physical neighbours -- found: the letter's own first page, unread.** Canvas 395 (`images/probe_c395.jpg`,
  1000 px, fetched this pass) is stamped **198** top right and headed "23 d'octobre 1593": it is **f.198 recto**, the
  start of no.101, with a block of about 14 near-solid cipher lines in its upper half and clear-with-inline-cipher
  below. Canvases 396 and 397 are two scans of the same page, **f.198 verso** (`images/probe_c396.jpg` vs
  `images/f198_canvas397_try.jpg`: same lines, same '+' marks; grey difference 15/255 at 1000 px, a registration
  offset), the continuation leaf the 24 Sept 2026 F2 pass cut and drafted (66 signs). Canvas 398 is f.199r, blank.
  So the 24 Sept draft covers the verso only; the recto's cipher block (several hundred signs, same hand) is
  untranscribed and carries no visible gloss or clear copy at 1000 px (conditional on that resolution; a native
  crop is the check). No clear copy or decipherment is bound beside the letter.
- **(d) the recipient's side -- not found.** Revol (secretary of state) has no printed correspondence; the royal
  side's editions were read: Gallica ContentSearch on Memoires de Nevers part 2 (bpt6k64451005): "Desenzan" 0 hits,
  "Revol" 5 hits, all "Et plus bas, REVOL" countersignatures of royal letters (PAG_314, 328, 471, 574, 666) -- the
  letter is not printed there; archive.org full text on Berger de Xivrey's Lettres missives vol.3
  (recueildeslettre03henr): "Desenzan*/Dezenzan*/Desanzan*" 0 hits; Google Books API ("Desenzan" "Revol"; "Octobre
  1593" "Revol" Nevers): only Folengo's Histoire maccaronique and the BnF catalogues, plus Rott's Inventaire sommaire
  (1882) and Histoire de la representation diplomatique de la France aupres des cantons suisses vol.2 (1900,
  archive.org histoiredelarepr02rottuoft, OCR fetched): Rott pp.580-581 cites fr.3986 ff.112, 113, 132, 143, 156,
  161, 168 (the Swiss leg, 1-14 Oct 1593) and "Revol a Nevers, Mantes, 23 octobre 1593, BN 500 Colbert XXXI 587"
  (same date, opposite direction, a different letter); f.198 is not cited. The owed "Octobre 1593" date-phrase search
  in Gomberville (24 Sept gap) is thereby run: no hit.
- Requests this pass: gallica.bnf.fr 4 (2 ContentSearch, 2 IIIF canvases, 1.6 s apart, all 200); archive.org 5
  (2 advancedsearch, 3 djvu.txt, one 503 on a wrong identifier, not retried); be-api.us.archive.org 3; googleapis 2;
  github.com 2 clones. No 403/429.

**Premise verdict: not found / not found / found (the recto, unread, no gloss) / not found -- CLEAR TO TEST**, and the
target is larger than the folder recorded: f.198r (canvas 395) is the bulk of the cipher, f.198v (canvases 396/397) the
tail. `python3 tools/intake_gate_check.py fr3986-nevers-revol-1593` -> "blocked (line 1) -- already terminal, nothing to
gate", exit 0, before and after this section (the status word is `blocked`, so the gate does not test for the section).

## GAPS-fr3986-nevers-revol-1593 (2 Oct 2026, account-4)

Worker GAPS-fr3986-nevers-revol-1593 (Fable 5.1), brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, the Verdict
step of LIKELY-6's "Remaining gaps": atlas coverage of the eight uncovered tags from c.264's unused lines, then the held-out
re-run. Clock read 14:19-14:5x UTC. Known answer first; f.198 itself NOT read (the gate below did not clear).

**Atlas extension (disk only, no fetch).** The lower lines of `tools/keys/key60_atlas/src/c264_region.jpg` (gloss above each
cipher line, matching Memoires de Nevers ii 498 word for word) were read at native resolution by the worker and ten
exemplars cut for the eight tags the 264-only atlas lacked: `tools/keys/key60_atlas/atlas264ext.tsv` (A53-A62, native boxes
and the print word each sits under) and `contact_sheet_264ext.png` (the 264-only sheet plus one block; `build_ext264.py`
regenerates both). Alignment is the worker's, grade S, same as A01-A52: L40 = qui and 8 = t and r = s in "quites"; r = s in
"lors"; c = s in "ses"; ue = e in "subjects" and "troisiesme"; 20 = u in "roy[a-u-me]" (∂ a, 20 u, ro me, three table
values in sequence); = d (the table's =/= form) in "l'ad-ve-ni-r" (λ, =/=, y, 50, ꝺo); // = c in "sacre" (y, //, E). No
leaf-298 material entered the atlas. Bonus pairs seen but not cut: pi = que, theta = des, ∬ = qu'ilz, ꝛ = luy, 8+ = tous,
∞+ = Le Roy, .xx. = t, oo = c, 50 = ni (all table values).

**Held-out re-run.** Same 28 gloss-aligned leaf-298 signs, same five masked crops, one blind Sonnet pass given only the
extended sheet, the two tag tables and the crops (`atlas_heldout/heldout_passC.tsv`; 1 vision call of 3 allowed). Score
(`atlas_heldout/score_C.txt`, regenerated by `heldout_score.py --pass heldout_passC.tsv --expect 20/28`, exit 0; the scorer's
suffix-stripping now removes a trailing ' and ? together, which pass B did not need -- 19/28 unchanged):

| | before (LIKELY-6, 264-only) | after (264 + 8 tags) |
|---|---|---|
| held-out sign-read rate | 19/28 = 67.9%, Wilson 49-82% | **20/28 = 71.4%**, Wilson 95% CI 52.9-84.7% |
| shuffle floor (pass tags permuted within crop, 2000 draws) | mean 42.4%, p95 50.0% | mean 44.4%, p95 53.6%, max 60.7% |
| on the eight added tags | 10/18 = 55.6% | 11/18 = 61.1% |
| on the other tags | 9/10 = 90.0% | 9/10 = 90.0% |
| gate | 80% | 80%, **not met** |

Reading: above the floor, below the gate, one sign better than before (`ue` in K3a). The remaining eight misses are not
coverage: two `r` were written `<r-shaped>` (the exemplar's own form word, the tag not used), `20` at a crop edge was read
`<r-shaped>`, one `//` was read `X+`, two final `8` sit at crop edges (one dropped, one `<x-shaped>`), one `g` inserted. Rule
3's third-attempt clause: this is the second pass of the same instrument (atlas + one blind Sonnet pass on these crops) with
only the coverage knob changed, and it moved one sign; the coverage knob is [retired] for this held-out. The held-out itself
is too small to decide an 80% gate either way (the interval straddles it both times), so the next step is a different
instrument, not a third pass: widen the answer key to the rest of c.298 (on disk, gloss above, about 100 more signs) and
cut crops with margins so no sign is at an edge. Grades: no new reading, no token grade changes; the 24 Sept draft of the
verso stands at H 5, M 56, U 5, I 0 (66); the recto's block (premise check (c)) has no draft yet.

Status word stays **blocked** (internal: sign identification), now with the target's full extent known. Spec
`specs/fr3986-nevers-f198.json` `cheap_test_done.rerun` written; HYPOTHESES.md row added. Vision calls: 1 subagent (of 3);
the worker's own eye-checks of the c.264 lines and probes are not subagent calls. Requests: see the Premise check section
(gallica 4, archive.org 5, be-api 3, googleapis 2, github 2); none for this step.

## Remaining gaps (GAPS, 2 Oct 2026; LIKELY-6 rewrite updated in place)
Read so far: 0 of 66 drafted verso signs read to a continuous text, and the recto block (canvas 395, several hundred signs) undrafted; the held-out atlas test reads 20/28 = 71.4% on the neater leaf 298 (atlas_heldout/score_C.txt; 19/28 before the eight-tag extension), under the 80% gate
- f.198 verso cipher runs (66 signs, 9 runs) - blocker: not-attempted; the atlas held-out gate failed twice (67.9% then 71.4% vs 80%, HYPOTHESES.md rows of 2 Oct 2026), so the f.198 passes were not run; coverage of the eight missing tags done 2 Oct 2026 (A53-A62) and [retired] as the knob; next: widen the held-out answer key to the rest of c.298 (src/f3986_c298_region.jpg, gloss above, ~100 signs, grade S alignment) and re-run one blind pass on uncut crops (+80 px margins, sign count given), ~$7
- f.198 recto cipher block (canvas 395, about 14 near-solid lines, found by the premise check 2 Oct 2026) - blocker: not-attempted; no gloss or clear copy visible at 1000 px; next: one native region fetch (Gallica IIIF, browser UA) + tools/iiif_lines.py crops + manifest entry, ~$2, no pass until the held-out clears 80%
- web and blog check (check-solved.md required step) - blocker: not-attempted; the gate did not test for it because `blocked` is terminal, owed before any open/partial verdict; next: the four web searches and three blog site searches logged under "## Web and blog check", ~$1

## Escalation (GAPS, 2 Oct 2026; LIKELY-6 list updated in place)
- [x] siblings: fr.3985 ff.126-130 and fr.3986 ff.151-152 (the interlined leaves) are the atlas source; leaf 298 is the held-out answer key; c.264's lower lines now in the atlas (A53-A62, 2 Oct 2026); the rest of c.298 is the next held-out material
- [n/a] clear-pages: the leaf is a clear-French letter with inline cipher runs (verso) and a cipher block (recto); no clear copy of this letter is known (Bourdeau's f.157v clear copy is no.75, 9 Oct; premise check (a)-(d) 2 Oct 2026 found none)
- [x] known-keys: key no.60 is in hand (key.tsv) and applied mechanically on 24 Sept 2026; the key is not the blocker
- [x] print: Gomberville seconde partie, Berger de Xivrey vol.3 and Memoires de la Ligue v.5-6 read 24 Sept 2026; Memoires de Nevers ii ContentSearch ("Desenzan", "Revol"), Lettres missives vol.3 full text, Rott 1882/1900 read 2 Oct 2026; absent
- [ ] key-rebuild: the coverage knob is retired (the eight uncovered tags added from c.264, A53-A62, moved the held-out by one sign, 19 -> 20 of 28, instrument tools/keys/key60_atlas + one blind Sonnet pass on the five LIKELY-6 crops); the untried instrument is a wider held-out: widen the answer key to the rest of c.298 and re-run one blind pass on uncut crops, ~$7 (the next step above)
- [ ] image-check: canvas 395 = f.198 recto (stamp 198, head "23 d'octobre 1593"), canvases 396/397 = f.198 verso (two scans), 398 = f.199r blank (2 Oct 2026, images/probes.json); the 24 Sept draft covers the verso only; the recto's native region fetch (~$2) is untried, see the gap above
- [retired] retry: a third blind pass on a Revol copy against the atlas as it stands (F1/F2 without it, G2 with it on f.176, LIKELY-6 and GAPS held-out at 67.9% and 71.4%) -- reopened only by a held-out that clears 80%
Verdict: keep going: 3 internal gaps; cheapest next: widen the held-out answer key to the rest of c.298 + one blind pass on uncut crops, ~$7 (then the recto fetch ~$2; the eight-tag coverage knob is [retired])
