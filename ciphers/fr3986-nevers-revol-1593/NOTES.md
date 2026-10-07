blocked
Blocked on sign identification of the Revol copyist (internal, 2 Oct 2026, GAPS3): Memoires de Nevers (1665) part 2 (Gallica bpt6k64451005) ContentSearch "Desenzan" 0 hits, "Revol" 5 hits (PAG_314, 328, 471, 574, 666, all royal countersignatures) and Berger de Xivrey Lettres missives vol.3 (archive.org recueildeslettre03henr) full-text "Desenzan*/Desanzan*" 0 hits, read 2 Oct 2026, letter absent; web and blog check 2 Oct 2026 found no decipherment; the f.198 verso passes against the 264ext atlas do not read (judge FAIL, below shuffled controls); the recto (fetched 2 Oct 2026, GAPS4) profiles like the verso, not like the atlas's office hand; the Revol-hand sign tiles are cut and on the owner's sign-sorter page (GAPS5, 2 Oct 2026, https://claude.ai/artifact/L2LvyN17GRK4XWwxiBGAFb); next: the owner's sort (ASKS row 102), then two blind passes against the settled list, ~$8.

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

## GAPS-fr3986-nevers-revol-1593-2 (2 Oct 2026, account-4)

Worker GAPS-fr3986-nevers-revol-1593-2 (account-4, Opus 5.5), brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`, the
first part of the Verdict step: widen the held-out answer key on c.298, one blind pass on fresh crops, re-score against the
floor and the 80% gate. Clock read 20:23-20:5x UTC. f.198 itself NOT read. Disk only: 0 network requests (the c.298 native
region was already on disk); 1 vision call of the 2 allowed (the first returned 145 signs, so no second).

**This is a different knob from the retired one.** The coverage knob (the atlas) is untouched: the sheet is GAPS's
`contact_sheet_264ext.png`, no leaf-298 material. What changed is the held-out set and the crops: the answer key now covers
every sign on c.298's first three cipher lines that the worker could align with the interlined gloss, and the crops are whole
lines at native resolution instead of +-42 px sub-spans with signs at the edges.

**Answer key, sealed first.** `atlas_heldout/heldout298_answers.tsv`, committed and pushed (73b2902e) before the read: 65 signs
on cipher lines 1-3 of `tools/keys/key60_atlas/src/f3986_c298_region.jpg` (LIKELY-6's 28 plus 37 new). Each is grade S, with
form, gloss syllable and key no.60 value all agreeing (glosses: qui retardast, arrivee, a, darra, miracle, de, ma-, autres;
touches, las, qui doibt, de dignite; et respect, en droict, et, incompati-). About 150 signs stand on the three lines. The
rest are left out: code words the sheet does not show (the boxed sign under "leur", lxxix under "Rome", com, ll), signs
whose form and gloss value disagree under no.60 (the p-sign written like 4+, y under "arrivee", g under "du"), and stretches
the worker could not align. Lines 4-10 of the region were not aligned; two views of lines 4-5 found only two alignable signs
(ll = bon, 99 = davantage) among code words. Six answer signs carry tags the sheet lacks (ls x3, s', del, 6).

**Crops.** `tools/iiif_lines.py --image tools/keys/key60_atlas/src/f3986_c298_region.jpg --out
ciphers/fr3986-nevers-revol-1593/atlas_heldout/crops298 --prefix ho298 --centres 347,451,564 --max-width 1900 --overlap 150
--debug`. That gives two native segments per line with 188 px overlap. Each band was then trimmed to region y 300-380,
422-485 and 533-595, so the interlined gloss is masked. The trim is recorded in `crops298/manifest.json`. Eye-checked: no
legible gloss, only letter tops of the next gloss line at the bottom edge.

**Blind pass.** One Sonnet subagent was given only the sheet, `atlas264.tsv`, `atlas264ext.tsv`, `tools/keys/key60.tsv` and
the six crops, copied to a scratch folder and told to read nothing else. It read 145 signs (L01 46, L02 47, L03 52), saved as
`atlas_heldout/heldout298_passD.tsv`. Its transcript shows no read, grep or command touching the repository, the answer
file, the full atlas or the c.298 source.

**Score.** `atlas_heldout/score_D.txt`, regenerated by `heldout_score.py --answers heldout298_answers.tsv --pass
heldout298_passD.tsv --expect 65/65`, exit 0. The scorer gained `--answers`, the Wilson interval, the floor's p95 and max and
an old/new split. Passes B and C still reproduce 19/28 and 20/28.

| | LIKELY-6 (264-only atlas) | GAPS (264ext atlas) | this pass (264ext atlas, widened key, whole-line crops) |
|---|---|---|---|
| N (gloss-aligned held-out signs) | 28 | 28 | **65** |
| held-out sign-read rate | 19/28 = 67.9% | 20/28 = 71.4% | **65/65 = 100%** |
| Wilson 95% CI | 49.3-82.1% | 52.9-84.7% | **94.4-100%** |
| shuffle floor, pass tags permuted within unit, 2000 draws | mean 42.4%, p95 50.0%, max 64.3% | mean 44.4%, p95 53.6%, max 60.7% | mean 49.8%, p95 55.4%, max 58.5% |
| LIKELY-6's 28 signs only | 19/28 | 20/28 | 28/28 |
| gate | 80%, not met | 80%, not met | **80%, met (lower bound 94.4%)** |

The match is positional, not an artifact of the order-preserving scorer. Line by line, the pass's sequence runs in step with
the worker's own reading through the excluded signs as well: `? c do y~ to 20 pl y~ del lxxix` against the worker's ⊡ c ꝺo y
to 20 ꝑ y ∂ lxxix, and the p-sign read X+ all three times. The floor rose because whole lines give the permuted tags more
places to land, and the real pass still clears its maximum by 41 points.

**What it licenses and what it does not.** The same 28 signs that read 20/28 in sub-span crops read 28/28 in whole-line crops
with the same atlas. That isolates the crop design as the source of the earlier misses, which GAPS had already diagnosed as
crop-edge and vocabulary misses, not coverage. The gate was defined as the precondition for the f.198 passes, so those
passes are now licensed. Two limits:
- **Leaf 298 is the neater office hand.** The Revol copyist on f.198 is harder (24 Sept 2026: blind agreement 40.9% without
  the atlas), so this result does not predict f.198's rate.
- **The answer key is a model's reading, filtered by the gloss.** The 65 signs are the ones where form, gloss and key agree.
  A sign both readers would misread the same way drops out of the key; it is not scored as a hit. The 80 or so excluded signs
  carry no score, although the pass agrees with the worker's reading on most of them.

Grades: no reading, so no token grade changes. The 24 Sept draft of the verso stands at H 5, M 56, U 5, I 0 (66). The recto
block has no draft yet.

**Status word stays `blocked`; the blocker has changed.** The internal blocker, sign identification for this copyist's
script, is cleared on the held-out leaf. The brief's rule for a cleared gate is to move to `partial`. But
`tools/intake_gate_check.py` tests a `partial` word for a logged web and blog check, and this folder has never had one (owed
since LIKELY-6). Under CLAUDE.md's intake rule a `partial` without it "is `blocked`, whatever word it uses". The gate run on
the `partial` draft exited 1 (pasted below), so the word stays `blocked`. Line 2 names the one remaining blocker: the
web and blog check, ~$1. It is not run here because the brief names only the held-out step and the check would cross 80% of the
box. After that check, and a line-2 citation of the editions already searched, the status can read `partial`. No reading is
claimed. HYPOTHESES.md row added; spec `specs/fr3986-nevers-f198.json` `cheap_test_done.rerun2` written.

Intake gate on the `partial` draft (20:46 UTC):

```
fr3986-nevers-revol-1593: partial (line 1) with no standard-edition citation (page number or full-text-search phrase) within 6 lines -- CLAUDE.md's Pipeline intake gate says this must read `blocked` instead
intake exit 1
```

## GAPS3-fr3986-nevers-revol-1593 (2 Oct 2026, account-4)

Worker GAPS3-fr3986-nevers-revol-1593 (account-4, Opus 5.5), brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`,
the first two steps of the GAPS-2 Verdict: the web and blog check (section at the end of this file: no decipherment or
plaintext of f.198 located, 8 searches, 2 fetches), then the f.198 verso passes. Clock read 20:50-21:1x UTC. The recto
fetch was not done (next worker).

**Intake gate after the web check**, run on a scratch copy with line 1 set to `partial` and line 2 citing the editions:

```
fr3986-nevers-revol-1593: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
intake exit 0
```

**Crops.** `tools/iiif_lines.py --image images/src_ark_12148_btv1b9060631k_f397_850_950_3400_4250.jpg --out images/v2
--prefix f198v --max-width 1900 --overlap 150 --only-lines 4..20 --top-margin 15`. This is the GAPS-2 design: whole lines
at native resolution, two segments of 1900 px, about 400 px overlap. The source is the 24 Sept native region of canvas 397,
already on disk, so Gallica got 0 requests. It gave 34 crops for lines L04-L20, the band that holds every run the 24 Sept
draft found. Lines L01-L03 and L21-L30 were checked by eye at 1600 px and read as clear text: the close "Desanzan ... 23
octobre 1593" and a clear postscript ("Car de demander 200 ...").

**Two blind passes, then reconciliation.** Two Sonnet subagents each got only the 264ext contact sheet,
`atlas264*.tsv`, `tools/keys/key60.tsv` and the 34 crops, in separate scratch folders, in opposite reading orders. Their
outputs are `passes/v2/passA.tsv` (57 cipher signs) and `passes/v2/passB.tsv` (68). The worker then reconciled them on
the crops (L04-L05, L07, L09-L10, L13, L15-L16, L19, viewed natively). Pass B's single '+' on L06, L18 and its L08 run were
rejected: they are insertion marks or clear letters, and pass A had NONE on those lines. The result is `ciphertext_v2.tsv`:
55 signs in 11 runs, in key60.tsv's tag set. Atlas-only tags take their gloss value from `key_atlas_extra.tsv` (grade M).
The two passes give the same tag on **20 of the 55 reconciled signs (36%)**. Both passes graded nearly every sign M. On
leaf 298 the same instrument read 65/65.

**Decode.** `tools/decode_key.py ciphers/fr3986-nevers-revol-1593` uses decode.json job 2, key `tools/keys/key60.tsv` +
`key_atlas_extra.tsv`. Grades are **H 12, M 42, U 1, I 0 (55)**, and `--check` exits 0 ("reading up to date"). The output
is `reading_v2.txt`. The one span with sense is L09: "de [R] [phi] [phi-]" = "de [Duc de Mantoue] [Duc de Ferrare] [Duc
de Ferrare | le grand Duc de Toscane]". That fits a letter written from Desenzano, but it is graded M, and it is a list of
code words, not text. L15's long run decodes "di p de a n li te r la p a le x bo bon la di ri moins so n". "67" read as one
code (affin) would give "affin de ...", but the rest still does not read.

**Controls** (`controls_v2.py`, `controls_v2.txt`; `--check` exits 0):

| | number |
|---|---|
| real decode, mean log10 4-gram per letter (fr = fr16 corpus, 138 letters) | -1.319 |
| 200 value-shuffled keys | mean -1.149, sd 0.087, max -0.947; real rank **194/201**, z **-1.95** |
| fr16 judge on the real decode | **FAIL** (language -1.319 vs real_p05 -0.919, null_p99 -1.708; word cover 0.841 vs 0.5 passes) |
| 20 shuffled-target decodes (sign order permuted, real key) | judge PASS **0/20**; language min -1.347, median -1.273, max -1.130 |

The real decode ranks *below* most value-shuffled keys. That is partly the control's design: shuffled values move whole
nomenclator words (comme, moins, affaires ...) into the syllable slots, and those words score as French. The shuffled-target
column is the cleaner comparison. There the real order scores below the median of its own signs scrambled. Either way the
verso **does not read** under this transcription. The non-reading is conditional on the transcription (rule 2): the blind
passes agree on only 36% of signs, and that is the measured limit.

**What it says about the instrument.** The atlas + whole-line-crop instrument cleared the 80% gate on the neat leaf-298
office hand (65/65). On the Revol copy it does not carry over. This is the fourth pass family on these verso runs: F1/F2
without the atlas (40.9%), G2 with the atlas (39.8% on f.176), LIKELY-6's retired passes, and now this one (36%). Each
changed the instrument, and none moved agreement. Under rule 3's third-attempt clause, a further blind pass on the verso
runs with this atlas is **[retired]** (instrument: 264ext atlas + blind Sonnet passes). Only new material or a different
instrument reopens it. Two candidates: the recto's near-solid block, about 14 lines in the same hand, which is more
ciphertext and gives longer runs and a frequency profile; or an atlas cut from the Revol copyist's own hand.

**Status.** Status word stays **`blocked`** (internal: this copyist's sign identification). Line 2 now names the editions
read and the next step. The intake-gate blocker is cleared, as shown above. Requests: web search 8 queries, WebFetch 2
(dbourdeau.github.io 1, github.com 1), gallica.bnf.fr 0. Vision calls: 2 subagent passes, plus the worker's own
reconciliation views of the crops (the third unit).

## GAPS4-fr3986-nevers-revol-1593 (2 Oct 2026, account-4)

Worker GAPS4-fr3986-nevers-revol-1593 (account-4, Opus 5.5), brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`,
the GAPS3 Verdict step: the recto fetch, then a sign-frequency profile to decide whether the recto shares the 264ext atlas's
signs (only then two blind passes). Clock read 21:10-21:2x UTC. Intake gate at start: `blocked (line 1) -- already terminal,
nothing to gate`, exit 0.

**Fetch.** `tools/gallica_folio.py btv1b9060631k --anchor 395=198r --anchor 398=199r --folio 198` (cached manifest, 0
requests; canvas 395 is 4949x6961; slope 3 between the anchors is the verso's double scan, canvases 396/397). Then
`tools/iiif_lines.py --ark btv1b9060631k --canvas 395 --region 800,780,3450,3250 --out
ciphers/fr3986-nevers-revol-1593/images/recto --prefix f198r --max-width 1900 --overlap 150 --debug`: 1 Gallica request, 27
lines, 54 whole-line crops, `images/recto/manifest.json`, debug overlay checked (bands on every line). Folder images 14 MB.
Cipher runs by eye on the overlay: L03 (end), L04, L05, L09, L11-L16, L19 (11 lines); L01 is the head "23 octobre 1593",
L02 "...ons de Revol, ..." opens the letter; L20-L27 are clear text with at most isolated signs (not cut for the pass).

**Profile (one blind Sonnet pass, vision call 1 of 3).** Given only the 264ext contact sheet, `atlas264*.tsv`,
`tools/keys/key60.tsv` and the 22 crops of those 11 lines, with `NEW:<shape>` allowed where no tag fits:
`passes/recto/passA.tsv`, 264 signs (L03 19, L04 52, L05 37, L09 11, L11 39, L12 22, L13 24, L14 7, L15 16, L16 17, L19
20). The pass itself called its reading low fidelity: 0 H, 167 M, 97 L. Counts by script, `recto_profile.py` ->
`recto_profile.txt` (`--check` exits 0):

| blind pass (same sheet, same tag list) | N | on atlas tags | on key60 tags | NEW / described | H-confidence |
|---|---|---|---|---|---|
| leaf 298 office hand, passD (instrument read 65/65) | 145 | 75.9% | 91.0% | 0.0% | 57.2% |
| f.198 verso passA (GAPS3, agreement 36%) | 66 | 6.1% | 34.8% | 19.7% | 21.2% |
| f.198 verso passB (GAPS3) | 73 | 46.6% | 68.5% | 9.6% | 13.7% |
| **f.198 recto passA (this step)** | **264** | **45.5%** | 84.5% | **9.1%** | **0.0%** |

Recto: 83 distinct tags, 21 of the atlas's 41 tags used; 24 NEW tokens in 19 distinct shapes (semicolon-dot x4, r-hook x2,
curl x2, barred and dotted phi, z-hooks, a slashed vertical ...); 17 tokens tagged with plain letters outside key60 (a, h,
i, u, gamma, a mid-dot x7). Top tags x 23, ++ 12, y 12, 4+ 9, T 8, n 8, L 8. Shared with the verso's 55 signs: 22 distinct
tags, covering 33/55 verso tokens; Pearson r of tag frequencies recto vs verso 0.0001 over 82 tags (the verso's N=55 makes
that a weak test, reported for completeness, not as a finding).

**Decision.** The recto profiles like the verso passes (atlas share 45.5% vs 46.6%, NEW 9.1% vs 9.6%), not like the
leaf-298 hand where the instrument works (75.9%, 0 NEW, 57% H), and it carries the lowest confidence of the four. It does
**not** share the atlas's signs to the degree the atlas instrument needs, so step 3 (two blind passes + reconciliation,
decode, controls) was **not run**: by the brief's own condition it is not licensed, and on the verso the same profile went
with 36% agreement. That is the comparison this step was for: the next instrument is a copyist-specific sign list, not a
different atlas from the office hand. Under Usage 6 an unsettled sign inventory goes to a person's pass, the owner's sign
sorter (`tools/sign_sorter.py` -> `tools/sign_sorter_apply.py`), not a third machine pass; the sorter needs one tile per
sign, which `passA.tsv` does not give (no boxes), so the cheap step that depends on nobody is cutting the tiles.

Grades: no reading, so no token grade changes (the verso v2 draft stands at H 12, M 42, U 1, I 0). Rule 10: nothing claimed.
Vision calls: 1 subagent (of 3). Requests: gallica.bnf.fr 1 (the IIIF region); manifest cached.

`tools/gaps_check.py` after the in-place update:

```
OK keep-going fr3986-nevers-revol-1593: keep going: 2 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
```

## GAPS5-fr3986-nevers-revol-1593 (2 Oct 2026, account-4)

Worker GAPS5-fr3986-nevers-revol-1593 (account-4, Opus 5.5), brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`,
the GAPS4 Verdict step: one sign tile per recto and verso sign into a `tools/sign_sorter.py` page for the owner. Clock read
21:46-21:5x UTC. Intake gate at start: `blocked (line 1) -- already terminal, nothing to gate`, exit 0. No vision calls, no
passes, no reading; requests 0 (everything from images on disk).

**Lines.** `sorter/stitch_lines.py` rebuilds 23 whole-line images (`sorter/lines/`): the 11 recto cipher-bearing lines of
GAPS4 (L03 L04 L05 L09 L11-L16 L19) stitched from their committed s1/s2 native crops (the recto source region was not kept),
and the 12 verso lines that carry v2 signs (L04-L10 L13 L15 L16 L18 L19) cut from the committed verso source image at the v2
crop boxes.

**Boxes.** `sorter/build_tiles.py` runs `tools/iiif_lines.py --image <line> --centres <h/2> --groups 6` on each line (gap 6
from the blank-run histogram: runs of 1-5 px fall inside letters and signs) and writes every piece box to `sorter/signs.tsv`:
**1,018 tiles** (the debug overlay of recto L12 was checked once for cut quality, as the tool requires: one box per sign in the
cipher stretch, one per letter or letter group in the clear French). Pieces wider than 1.6x the band height (7) go to pile
`wide`.

**Labels: a deviation from the brief, stated.** The brief said labels from `passes/recto/passA.tsv` and `passes/v2`. Those
files record line, run and position but no x coordinate, and each line's pieces include its clear-French letters (recto L12:
53 pieces for 22 pass signs), so a pass tag cannot be tied to a piece without reading the image, which this step was not to
do; any such tie would be an I-grade guess handed to the owner as a label. The piles are therefore provisional image clusters
(k-means k=40, seed 1, on the 24x24 normalised tile the sorter itself uses), `c01`-`c40` plus `wide`, in `sorter/labels.tsv`;
the pass tags per line ride in the focus questions instead.

**Focus ("Check these first").** `sorter/focus.tsv`, 23 rows: one per line, on the line's darkest piece (the cipher runs are
written heavier than the clear text), each question quoting the readers' tags for that line -- verso lines where passes A and B
split (all 12 split) and every recto line (one reader). `tools/lookalike_pass.py` was not used: it needs a two-reader alignment
with tile ids (reconcile_passes.py agreement files), which these passes do not have, and its own docstring rules it out for an
unsettled inventory.

**Page.** `python3 tools/sign_sorter.py --signs sorter/signs.tsv --labels sorter/labels.tsv --pages sorter/lines --focus
sorter/focus.tsv --title "Revol Hand Sign Sorter" ...`: 41 piles, 1,018 tiles, 0 skipped, 5.1 MB, published private to the
owner with `capabilities {"db": {}}` at https://claude.ai/artifact/L2LvyN17GRK4XWwxiBGAFb (db collections piles/moves/newpiles
empty at publish, checked by one list). The HTML is not committed (regenerate with the commands in `sorter/README.md`). Folder
22 MB, under 30.

Grades: no reading, no token grade changes (verso v2 draft stands at H 12, M 42, U 1, I 0). Rule 10: nothing claimed.

`tools/gaps_check.py` after the in-place update, and `tools/next_steps.py --wait-only | grep fr3986-nevers-revol-1593` (empty):

```
OK parked fr3986-nevers-revol-1593: parked: 2 gap(s), all outside blockers
gaps_check: 1 checked: 1 parked, 0 keep-going, 0 FAIL, 0 skipped
```

## Remaining gaps (GAPS3, 2 Oct 2026; GAPS-2 list updated in place; GAPS4, GAPS5 updated in place)
Read so far: 0 signs to a continuous text. f.198 recto: 264 signs profiled (GAPS4, one blind pass, 45.5% on atlas tags, 9.1% new shapes, 0 H), no draft. f.198 verso v2 draft: 55 signs in 11 runs (ciphertext_v2.tsv; H 12, M 42, U 1), pass agreement 20/55 = 36%, judge FAIL (-1.319 vs real_p05 -0.919), shuffled-target 0/20, rank 194/201 vs value-shuffled keys. The recto block (canvas 395, several hundred signs) is still undrafted. The atlas held-out gate clears on leaf 298 (65/65) but does not carry over to the Revol hand. The web and blog check is done (2 Oct 2026, GAPS3: no decipherment located; scratch intake gate with `partial` exits 0).
- f.198 verso cipher runs (55 signs, 11 runs) - blocker: waiting-on ASKS row 102 (the owner's sort of the Revol-hand sign-sorter page); passes run 2 Oct 2026 (GAPS3): blind agreement 36%, judge FAIL, below shuffled-target median; a further blind pass with the 264ext atlas is retired (rule 3); tiles cut 2 Oct 2026 (GAPS5, 12 verso lines in the sorter page); next: re-read against the owner-settled Revol-hand sign list, ~$4
- f.198 recto cipher block (canvas 395, 11 cipher-bearing lines, 264 signs in one blind profile pass) - blocker: waiting-on ASKS row 102 (the owner's sort of the Revol-hand sign-sorter page); fetched and profiled 2 Oct 2026 (GAPS4: atlas share 45.5%, NEW 9.1%, 0 H, the verso's profile, not leaf 298's 75.9%/0%/57%), atlas passes not licensed; tiles cut 2 Oct 2026 (GAPS5: 1,018 tiles from 23 lines, 41 provisional piles, 23 focus rows, https://claude.ai/artifact/L2LvyN17GRK4XWwxiBGAFb); next after the sort: two blind passes against the settled Revol-hand list, ~$8

## Escalation (GAPS3, 2 Oct 2026; GAPS-2 list updated in place)
- [x] siblings: fr.3985 ff.126-130 and fr.3986 ff.151-152 (the interlined leaves) are the atlas source and the held-out; c.264's lower lines are in the atlas (A53-A62); c.298 lines 1-3 aligned as the held-out (65 signs, 2 Oct 2026); lines 4-10 left (mostly code words); the two other "avec chiffre" Revol copies, items 68 (f.146v, c.287) and 75 (ff.157r-v, c.308-309), located and cut 7 Oct 2026 (AM-REV68): same sign family, no gloss, no clear twin, 15 cipher-bearing line crops in images/siblings/ for the owner's sorter
- [n/a] clear-pages: the leaf is a clear-French letter with inline cipher runs (verso) and a cipher block (recto); no clear copy of this letter is known (Bourdeau's f.157v clear copy is no.75, 9 Oct; premise check (a)-(d) and the web and blog check, 2 Oct 2026, found none)
- [x] known-keys: key no.60 is in hand (key.tsv; tools/keys/key60.tsv + key_atlas_extra.tsv for the v2 draft); the key is not the blocker
- [x] print: Gomberville seconde partie, Berger de Xivrey vol.3 and Memoires de la Ligue v.5-6 read 24 Sept 2026; Memoires de Nevers ii ContentSearch ("Desenzan", "Revol"), Lettres missives vol.3 full text, Rott 1882/1900 read 2 Oct 2026; absent
- [x] key-rebuild: atlas extended (A53-A62), held-out widened to 65 signs on whole-line crops, 65/65 on leaf 298 (2 Oct 2026, GAPS-2), but the Revol hand does not profile like the atlas's office hand (GAPS4); the Revol-hand tile cut and sorter page are done (GAPS5, 2 Oct 2026); the sort itself is the owner's, waiting-on ASKS row 102
- [x] image-check: canvas 395 = f.198 recto (stamp 198, head "23 d'octobre 1593"), canvases 396/397 = f.198 verso (two scans), 398 = f.199r blank (2 Oct 2026, images/probes.json); recto native region fetched and cut 2 Oct 2026 (GAPS4, images/recto, 54 crops), profiled: Revol-hand profile, atlas passes not licensed
- [retired] retry: blind passes on the verso runs with the 264ext atlas (instrument: atlas + whole-line crops + blind Sonnet passes), 2 Oct 2026 GAPS3, agreement 36%, judge FAIL, the fourth pass family that failed to move agreement; reopened only by new material (the recto) or an atlas from this copyist's own hand
Verdict: parked: every gap has an outside blocker (waiting-on ASKS row 102, the sibling tiles of items 68/75 cut 7 Oct 2026 for adding to it; the owner's sort of https://claude.ai/artifact/L2LvyN17GRK4XWwxiBGAFb; then two blind passes against the settled Revol-hand list, ~$8)

## While waiting

- DONE (AM-LOOK, 7 Oct 2026; fr.3986 list of 15 items, fr.3985 not parsed): list the other Nevers-to-Revol letters of 1593 in fr.3985/fr.3986 from the BnF finding aid (catalogue only, no images), to name sibling leaves in the same copyist's hand that would add tiles to the sorter or a crib, ~$2.
- DONE (AM-REV68, 7 Oct 2026): items 68 (f.146v) and 75 (ff.157r-v) located, same sign family, 15 cipher line crops cut (images/siblings/). Open: tiles into ASKS 102's sorter (~$1.5, account-3 hand-off); crib test of f.146r (to the King, same day, clear) against item 68, ~$2.

## Web and blog check (GAPS3-fr3986-nevers-revol-1593, 2 Oct 2026)

Worker GAPS3-fr3986-nevers-revol-1593 (account-4, Opus 5.5), `.claude/briefs/check-solved.md` "Required step: Open web and
blog comment threads". Clock read 20:51-20:5x UTC 2 Oct 2026. Web search tool (US index) plus WebFetch on the hits that could
bear on this letter. Rule 10: a search result, not a novelty verdict.

(a) Plain web searches:
1. `duc de Nevers Revol 23 octobre 1593 Desenzano lettre chiffre` (sender + recipient + date + place): BnF
   archivesetmanuscrits finding aids (Français 3625, 3315, 3631, 3974-3995, 4715, 3624, 3634, 3646, 3362) and Wikipedia
   (Louis de Gonzague). The finding aids catalogue letters and cipher keys; none carries a decipherment of f.198.
2. `"fr. 3986" chiffre Nevers 1593` (shelfmark + chiffre): the same BnF finding aids (3974-3995 is the fr.3986 inventory),
   a Biblissima IIIF manifest of fr.4687, and a Cairn chapter ("La conversion religieuse d'Henri de Navarre", Reconcilier
   les Francais). No decipherment of this letter in any snippet.
3. `"Desanzan" Nevers 1593 Revol` (the endorsement's distinctive place spelling, Tomokiyo league.htm): the finding-aid
   entry for this letter ("a Mr de Revol ... Desanzan, 23 octobre 1593", a copy) and a sister letter to Retz the same day;
   catalogue description only, no plaintext of the cipher.
4. `Nevers to Revol 1593 cipher no.60 Henry IV embassy Rome decipherment` (descriptive title): Bourdeau's cyphersolver
   site and repository, its forks (aryasn2026, setsunaatto), his issue #13 (Lauriere to Nevers, fr.3625 no.55, a different
   letter and key), the Tartu paper "An early French digit cipher: deciphering a letter from the King of France to the Duke
   of Nevers (1592)" (a different letter, 1592), Wikipedia (Revol, d'Ossat, Vigenere).
5. `Nevers Revol 1593 cipher solved Claude OR GPT` (model-solve announcements): press items on other ciphers (Urquhart,
   Napoleon letter), Bourdeau's issue #13 and site again; nothing on this letter.
6. `dbourdeau cyphersolver Revol Nevers 1593 issue`: Bourdeau issue #13, arya1515 pull requests #7 (Maisse), #8 (Spanish
   despatches), #9 (fr.3977 intercepts), forks, el-descifrador/cabinet-noir. None names fr.3986 f.198.

Hits opened: dbourdeau.github.io/cyphersolver/index.html (no mention of Revol, fr.3986, f.198, 23 Oct 1593 or Desenzano;
no decipherment of f.198 claimed); github.com/arya1515/cyphersolver README (nevers1593 row: "The five letters to Revol are
in the Court's symbol cipher no. 60, not no. 46" -- unread; no reading of f.198 claimed). Bourdeau's own nevers1593
NOTES.md (17 Sept 2026, already cited above, "fr. 3986 f. 198 (23 Oct, no. 101) - blocker: not-attempted") is the
"partial Nevers to Revol" item the search summaries mention; it covers other leaves.

(b) Blog site searches:
- Cipherbrain: `site:scienceblogs.de/klausis-krypto-kolumne Nevers 1593` -- solved-cryptograms feed, Top-25 posts, the
  16th-century crypto book post, Biermann's solve, and "A king's encrypted letter on Satoshi Tomokiyo's list of unsolved
  cryptograms" (14 Jun 2020: the Henri IV to Nevers 1592 letter, the Tartu paper's subject, a different letter). No post
  or thread on fr.3986 or Nevers to Revol.
- Cryptiana: on-disk snapshot `sources/cryptiana/` grepped first (0 requests): league.htm lists "no.101 (fol.198) Duke of
  Nevers to Revol, Desanzan, 23 October 1593" among letters partially in cipher no.60, no decipherment given; nevers.htm
  names no.60 generically. `site:cryptiana.blogspot.com Nevers Revol`: only the 2018 forum archive and the fr.3995 cipher
  catalogue post; nothing on this letter.
- Cipher Mysteries: `site:ciphermysteries.com Nevers 1593 cipher` -- Colorni, fifteenth-century cryptography, van Heeck,
  Rohonc posts; nothing on Nevers or Revol.

(c) Comment threads: no hit was about this letter, so no thread bore on it; the one Cipherbrain post touching Nevers (14 Jun
2020) concerns the 1592 royal letter, solved in the Tartu paper, not f.198.

Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026. Requests: web search 8 queries,
WebFetch 2 (dbourdeau.github.io 1, github.com 1); no 403/429.

## AM-LOOK (7 Oct 2026)

Item: Nevers-to-Revol letters of 1593 from the BnF archivesetmanuscrits finding aid, 10:4x UTC, for LANE LANE-AM-0914 (catalogue only, no images). Route: POST to `/resultatRechercheSimple.html` with `TEXTE_LIBRE_INPUT` "Nevers Revol 1593 Français 3986" (the bare root URL answers 405 to a POST; the form posts to that results page), 15 results, one page. Fr.3986 entries (item no. as printed, then letter): 3 Nevers to Revol, Nevers 14 Sept 1593 (copy); 8 Revol to Nevers, Fontainebleau 15 Sept; 15 Nevers to Revol, Nevers 13 Sept (copy); 30 Revol to Nevers, Fontainebleau 22 Sept; 39 Nevers to Revol, Fovan 26 Sept (copy); 41 Revol to Nevers, Fontainebleau 17 Sept; 47 Nevers to Revol, Montbeliard 29 Sept (copy); 54 Nevers to Revol, Basle 1 Oct (copy); 58 Nevers to Revol, Bade 4 Oct (copy); **68 Nevers to Revol, "avec chiffre", Vese 7 Oct (copy)**; 72 Pisani to Nevers, Dezensan 8 Oct; **75 Nevers to Revol, "avec chiffre", Coire 9 Oct (copy)**; 77 Revol to Nevers, Chartres 7 Oct; 92 Revol to Nevers, Mante 21 Oct; **101 Nevers to Revol, "avec chiffre", Desanzan 23 Oct (copy)**. The finding aid's numbers are the volume's item numbers, not confirmed folios; the item-to-folio map was not tested here. Candidates for the copyist's hand: the three "avec chiffre" copies (68, 75, 101) are the cipher-bearing siblings the finding aid itself marks; whether they are the same copyist as f.198/f.298 needs the image. Not covered: a second search for fr.3985 gave a result page whose entries this worker did not parse, so no fr.3985 list is given; search returns only entries whose notice matches the query terms, so other 1593 letters in the volume may exist. Requests: archivesetmanuscrits.bnf.fr 5 (1 home page, 1 rejected POST, 3 results).


## AM-REV68 (7 Oct 2026): census of sibling items 68 and 75

Worker AM-REV68 (account 2, for LANE LANE-AM-0914), brief `.claude/briefs/runs/2026-10-07-account2-laneam-0914-jobs.md`. Clock 10:36-10:4x UTC
7 Oct 2026 (date -u). Census only; no reading, no transcription, no gate (nothing scored, so no PREREG/control).

Location. Tomokiyo's league.htm (on disk, `sources/cryptiana/web/league.htm`) gives no.68 = fol.146v (Vese, 7 Oct) and no.75 = fol.157
(Coyre, 9 Oct); Bourdeau's `targets/nevers1593/` (shallow clone adbf9a1, 5 Oct 2026, grepped for this target only) has transcription drafts
of f.146v (c.287) and f.157v (c.309) and the canvas = 2 x folio rule. Eye-checked at 1000 px and 2000 px this pass (`images/siblings/probes.json`):
- **Item 68** = canvas 287, **f.146v**: opens "Monsr de Revol" in the copyist's cursive; the facing f.146r (c.286, stamped 146, head
  "7 d'octobre 1593") is a different letter in a looser hand, "Sire, je croy que V.M. se pourra un peu esbair des nouvelles...", to the King,
  same day, clear. Endorsement at the foot of f.146v ("... 1593 7 oct ... a Revol ..."). Cipher: **7 cipher-bearing lines** in mid-page (2 whole,
  5 mixed), about 190 signs by eye (estimate, +-25%).
- **Item 75** = canvases 308-309, **ff.157r-157v**: f.157r (stamp 157, head "9 octobre 1593") opens "Monsieur de Revol"; f.157v closes "...Coyre
  ... 9 octobre 1593". The preceding f.156r (c.306, stamp 156, head "9 d'octobre 1593") is another 9 Oct letter, not checked beyond its head
  (Bourdeau's "ff.156-157v" for no.75 is not confirmed by this pass; the "Monsieur de Revol" opening is on f.157r). Cipher: **8 cipher-bearing
  lines**, f.157r 4 (two mid-page runs, two lines near the foot) and f.157v 4 (the top two lines, two runs in lines 4-5), about 175 signs by
  eye (estimate). Bourdeau's caution that his f.157v draft over-reads cipher holds: the cipher there is runs inside clear cursive.

Sign family and hand (by eye, `images/siblings/hand_compare_sheet.jpg`: f.198r lines 3-4 from the GAPS4 source region, f.146v L05-L06,
f.157v L01, f.157r L08). Same sign family as f.198 (key no.60 symbols: the double-cross, the d-loop/delta sign, T, pi with perp, 20/14/4 figures,
xx/xxx, lambda, the tailed q, superscript dots and accents). Same cursive copyist as f.198r-v for the clear text ("Monsr de Revol" openings,
the hooked 'que' sign) by eye; ink and pen are heavier on 146v/157 than on f.198 (scan or pen, not established). Not the office hand of the
interlined leaves (c.264/c.298). Verdict: **same family, same copyist by eye** -- unmeasured; a sorter pile check would test it.

Gloss / twin. No interlinear decipherment over any cipher run on f.146v, f.157r or f.157v at 2000 px and in the native line crops; marginal
marks are clear-text corrections. No clear-text copy of either letter bound beside it. One possible content parallel, not a twin: f.146r, the
same-day clear letter to the King (c.286), may cover the same news ("des nouvelles", Montbeliard/Swiss route) -- a crib candidate to test, not
established. Tomokiyo's henryiv2.htm notes f.146v "partly reads 'demander l'absolution', 'a la verite', 'interest'" (his anchors, uncredited
as a reading by this pass).

Crops for the owner's sorter (do not publish; no sorter built): `images/siblings/f146v/` (11 lines, c.287 region 700,1900,3600,1260),
`f157r/` (8 lines, c.308 region 400,4600,4100,1250), `f157v/` (6 lines, c.309 region 850,950,3600,820), each with manifest.json and
debug overlay; `images/siblings/cipher_lines.tsv` lists the 15 cipher-bearing crops with extent and estimated sign counts. Crop commands:
`python3 tools/iiif_lines.py --ark btv1b9060631k --canvas 287 --region 700,1900,3600,1260 --out images/siblings/f146v --prefix f146v --debug`
(likewise canvas 309 / 308 with the regions above) -> 11, 6 and 8 lines.

Next step (named, not run): add the 15 sibling cipher lines' tiles to ASKS 102's Revol-hand sorter (build_tiles.py on these crops, ~$1.5,
an account-3 orchestrator hand-off; the sort stays the owner's), which roughly doubles the Revol-hand sign sample (~365 more signs);
second, a cheap crib test of f.146r (to the King, same day) against item 68's cipher runs, ~$2.

Requests: gallica.bnf.fr 21 (11 canvas probes at 1000 px, 5 at 2000 px, 2 info.json, 3 native regions; >= 2 s apart, all 200); github.com 1
shallow clone. No 403/429/challenge.

## Keyhunt 7 Oct 2026

KH1-B (LANE KH-1), 17:47-17:59 UTC 7 Oct 2026 by date -u, for key no.60 (key.tsv, shared by fr3985/fr3986/fr3987).
Searched: BnF archivesetmanuscrits finding aid Français 3974-3995 (ark cc504266, full inventory, 169 cipher items parsed),
Tomokiyo henryiv2.htm/league.htm/nevers.htm on disk, the folders' own NOTES, QUEUE.md, sources/; Gallica fr.3988 (canvases
287-305, 8 requests); print: Lettres missives de Henri IV iv (archive.org recueildeslettre04henr, djvu text, Dec 1593 entries)
and Gomberville Memoires de Nevers (Gallica bpt6k64451005 ContentSearch).
Unread no.60 siblings without a folder of their own: 5 -- fr.3985 f.115 (27 Aug 1593), fr.3986 f.146v and f.157 (AM-REV68
census), fr.3989 f.3 (1 Jan 1594), and **fr.3988 f.143r-v** (Henri IV to Nevers, catalogued 22 Dec 1593, leaf headed "24 de Dec
1593"; Gallica btv1b9060634t canvases 304-305): two full pages of symbol cipher in the court hand, no interlinear gloss at 1800 px
although Tomokiyo's list says "Interlined deciphering"; not found in Lettres missives iv or by the Gomberville ContentSearch
queries. It is in no folder and not in QUEUE.md. No test run (cap); next: six-line crop, two blind passes + reconcile against
fr3986's sign_guide/atlas, decode, shuffled-key control, about USD 7. Note: the finding aid under-flags cipher (fr.3985 f.88
carries cipher per Tomokiyo but is not marked "avec chiffre"), so the count is a lower bound. Every candidate:
keyhunt/2026-10-07-KH1B.tsv.
