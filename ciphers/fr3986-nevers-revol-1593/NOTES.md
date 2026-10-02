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

## Remaining gaps (LIKELY-6, 2 Oct 2026)
Read so far: 0 of 66 drafted signs read to a continuous text; the held-out atlas test reads 19/28 = 67.9% on the neater leaf 298 (atlas_heldout/score.txt), under the 80% gate
- f.198 cipher runs (66 signs, 9 runs) - blocker: not-attempted; the atlas held-out gate failed (67.9% vs 80%, HYPOTHESES.md row of 2 Oct 2026) so the row's f.198 passes were not run; next: extend the atlas to the eight uncovered tags `// 20 8 = L40 c r ue` from c.264's unused lines (tools/keys/key60_atlas/src/c264_region.jpg, on disk, gloss above each sign line, pairs.txt format) and re-run atlas_heldout/ with one Sonnet call, ~$8
- web and blog check (check-solved.md required step) - blocker: not-attempted; the gate did not test for it because `blocked` is terminal, owed before any open/partial verdict; next: the four web searches and three blog site searches logged under "## Web and blog check", ~$1

## Escalation (LIKELY-6, 2 Oct 2026)
- [x] siblings: fr.3985 ff.126-130 and fr.3986 ff.151-152 (the interlined leaves) are the atlas source; leaf 298 used as the held-out answer key this pass; c.264's lower lines still unused (the next step above)
- [n/a] clear-pages: the leaf is itself a clear-French continuation with inline cipher runs; no separate clear copy of this letter is known (Bourdeau's f.157v clear copy is a different letter)
- [x] known-keys: key no.60 is in hand (key.tsv) and applied mechanically on 24 Sept 2026; the key is not the blocker
- [x] print: Gomberville seconde partie, Berger de Xivrey vol.3 and Memoires de la Ligue v.5-6 read for the letter on 24 Sept 2026, absent; the "Octobre 1593" date-phrase search in Gomberville is still owed with the web check
- [ ] key-rebuild: the copyist's sign-form atlas is the rebuild this hand needs; planned step: coverage of the eight uncovered tags from c.264's unused lines, then the held-out re-run (gate 80%)
- [x] image-check: canvas 397 = f.198 confirmed by the facing stamp on canvas 398 (24 Sept 2026); native region on disk, line crops in images/
- [retired] retry: a third blind pass on a Revol copy against the atlas as it stands (instrument: tools/keys/key60_atlas at 52+28 pairs; F1/F2 without it, G2 with it on f.176, this held-out at 67.9%) -- reopened only by the coverage step above
Verdict: keep going: 2 internal gaps; cheapest next: atlas coverage of the eight uncovered tags from c.264's unused lines + held-out re-run, ~$8
