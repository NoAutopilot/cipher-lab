partial

# Pietro de Pusterla's 1447 cipher: key rebuilt from his glossed slips (BnF italien 1584) -- SFZ-P, 7 Oct 2026

Worker SFZ-P for LANE ST-REBUILD (account 2), brief `.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md`
(Wave 2, SFZ-P). Times by `date -u`, 7 Oct 2026, 21:52-22:2x UTC. Status here: `partial` means a known-plaintext key
(grade C values) exists and passed a held-out gate. Its target, f.13, is in `../../sforza-pusterla-1447-f13/`.

## Units

| unit | cipher slip | clear copy | canvases | slip signs (SFZ-P read) | copy letters |
|---|---|---|---|---|---|
| f81 | f.81, Ferrara 10 Mar 1447 (clear dateline "...Martij") | f.80 "1447 10 mars", one page | 78 / 77 right | 664 | 875 |
| f42 | f.42, 14 Feb 1447 (opens "Illustris re[x]."; closes in clear "sempre me recomando. Dat...") | f.41 "1447 14 fevrier" (c38 right page + 5 lines at the top of c39 left page), dated "Mediolani" | 39 / 38, 39 | 837 | ~1,250 |

Commands (pasted): `python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 78 --region 4650,180,2750,2100 --out ciphers/sforza-italien1584-1447/pusterla/images --prefix f81 --overlap 0 --max-width 1400 --debug`
(25 bands; L01 is the header) and `... --canvas 39 --region 4250,330,3350,2600 --prefix f42 --overlap 0 --max-width 1700 --distance 55 --prominence 60 --lines-per-crop 2 --debug`
(15 two-line crops). The copies were fetched as plain regions (c77 4700,150,2900,4850; c38 4700,150,2900,5100; c39 2000,450,1400,1450),
cut locally into `f80_chunk*`/`f41_chunk*`. The overlays were checked.

## Method and deviations

- **Sign reading.** SFZ-P read both slips itself (Opus), sign by sign, from the native crops, in working labels
  (`pusterla_labels.md`, a separate namespace from `../amidani/labels.md`, with a concordance column). No Sonnet pass was
  run on the key units: the inventory had to be fixed first. Both slips are single-reader. err_2reader was not measured
  on them; err_true is not measurable (no benchmark item). f.42 was read after f.81's key had been seen, a possible label
  bias.
- **Word sign.** Pusterla writes "che" as one sign `g÷` (a 9-shape followed by ÷). On f.81, 17 of its 18 occurrences
  fall within 0.03 relative position of the 17 "che" (including perche and siche) of the copy. f.42 also writes "siche"
  once in clear (`w:siche`).
- **Learner (deviation from g1.py, stated in g1p.py).** `tools/stream_align.learn` did not lock on: the within-letter
  half/half hold-out on f.81 gave 0.36-0.40 vs shuffle p95 0.38-0.43. g1p.py therefore treats "che" as one clear-side
  letter, uses the g÷/che pairs as anchors, and runs the same banded DP hard EM between consecutive anchors. On f.81 this
  gives 0.63 / 0.46 within-letter (half/half) vs shuffle p95 0.39-0.40. Scoring is g1.py's own `score`, imported.
- **Nulls.** These are signs the self-alignment leaves unmatched: f.81 203/664, f.42 110/837. They include the name
  codes the copyist left blank and misreads.

## S1: shared-key test against Amidani's key -- FAIL

The f.81 mnemonics were mapped to labels.md by shape (the concordance column of pusterla_labels.md; scratch script, not committed; 237 of 664 signs had no counterpart or no
trained value). The decode was scored with g1.score against f.80: real **0.241**, shuffle mean 0.233, p95 **0.275**
(200 shuffles). FAIL, so Pusterla has his own key and the two keys were not pooled. Visual differences: his ÷ means e,
where Amidani's D is i; there is no Amidani +, 7 or φ in his slips.

## S2: gate G1 (pre-registered, unchanged; `g1p.py`, output `gate_g1.tsv`)

| held out | signs | nulls | trained signs | unseen | real | shuffle mean | shuffle p95 |
|---|---|---|---|---|---|---|---|
| f81 | 664 | 203 | 62 | 17 | **0.733** | 0.355 | 0.393 |
| f42 | 837 | 110 | 65 | 25 | **0.589** | 0.362 | 0.395 |

The mean is 0.661 >= 0.60 and both units are above their p95: **PASS**. Robustness checks (scratch, not committed):
- Without null exclusion: 0.720 / 0.581.
- With the che sign removed from both sides: 0.715 / 0.579.
- Shuffle p95 is at or below 0.40 in all of these.

With g1.py's stock learner (`g1p.py --stock`, `gate_g1_stock.tsv`) the gate FAILs: 0.447 / 0.390. Both rows are reported.

**Key** (`key.tsv`, pooled; values from the later-hand copies, so grade C at best; C = count >= 2 and share >= 0.6).
Main values: ÷ e, :|: e, h7 e, q a, a a, b- a (shared with o), coo a, b i, dio i, fo s, ze s, pi s, o# c, h c, d t,
gto t, t r, zo r, x o, B o, pq o, pez o, y n, q= n, 3 m, V d, to d, bo d, g÷ che, .. p, :||: g. This is a homophonic
letter substitution with a word sign for "che", and the multi-letter-looking signs ("fo", "dio", "pez") stand for single
letters. Alignments: `align_f81.tsv`, `align_f42.tsv`.

Reproduce: `python3 ciphers/sforza-italien1584-1447/pusterla/g1p.py --check` (and `--stock --check`).

## Print note

Osio, Documenti diplomatici III, prints Pusterla's Ferrara letter of 7 Mar 1447 (no. CCCXCI, pp. 485-486). Its text is
the clear copy beside cipher slip f.71. That copy can serve as a third witness, and f.71 itself is not an unread target.
The OCR spells the name "Posteria"/"Puslcrla", which is why a "Pusterla" grep misses it.

## Grading (rule 4)

Key values are C (from the later-hand copies) or M. There is no H. The f.81 and f.42 slips have their decipherments beside
them, so nothing here is claimed as a reading.

## Units 3-4: f.71 and f.67 (SFZ-NEXT, account 2, 8 Oct 2026, 00:11-00:4x UTC by date -u)

Brief `.claude/briefs/runs/2026-10-07-acct3-sfz-next.md`, units 1-2.

| unit | cipher slip | clear side | canvas | lines | signs (reconciled) | passes agree | nulls |
|---|---|---|---|---|---|---|---|
| f71 | f.71, Ferrara 7 Mar 1447 (header "1447 7 Mars") | Osio III no. CCCXCI pp. 485-486 (`clear_f71_osio.txt`, IA OCR corrected by eye; Osio's spelling) | 68 right | 46 | 1,338 | 995/1,348 = 73.8% | 562/1,333 |
| f67 | f.67, Ferrara 6 Mar 1447 (header "1447 6 Mars") | later-hand copy f.66 (c63 right + top of c64 left; `clear_f66.txt`, read by SFZ-NEXT from native regions) | 64 right | 28 (L28 = signature group) | 801 | 611/822 = 74.3% | 126/800 |

Crops (pasted): `python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 68 --region 4250,1330,2850,3900 --out ciphers/sforza-italien1584-1447/pusterla/f71 --prefix f71 --overlap 0 --max-width 1500 --distance 60 --prominence 40 --deskew --debug`
(fetched the region; its auto bands missed 3 lines and its deskew fits snapped to neighbours, so the crops were not used); line
centres then read with `--columns 0:600` and `--columns 2200:2800 --distance 50 --prominence 25 --dry-run` on the same source, paired,
and sheared level by `f71/level_crops.py` (46 lines, two halves each, eye-checked on a montage). f.67: `--canvas 64 --region
4250,480,2850,2500`, the same two-strip centres, `f67/level_crops.py` (28 lines). The source regions are not committed (folder size);
re-fetch with the iiif_lines command, then run level_crops.py. `f71/manifest.json` lists the first iiif_lines crops, which were deleted (not used).
Passes: two blind Sonnet subagent calls per slip (pass A top-down, pass B bottom-up), pusterla_labels.md only, no key; then
`tools/reconcile_passes.py --method nw` and one Sonnet reconciler call per slip settling every disagreement column from the crops
(`f71/rec/settled.tsv`: A 128, B 221, other 4; `f67/rec/settled.tsv`: A 143, B 40, other 21, seam 7). Systematic splits: T= vs b-
(f71 75, f67 28), d vs g (f71 57), q vs V (f67 17). err_true not measurable (no benchmark item for this hand).
f.71's high null count (562) means the self-alignment leaves much of the slip unmatched against Osio's print: spelling differences
between the slip's text and the edition, and transcription error, both contribute; not separated here.

**G1 (pre-registered, unchanged), 4 units** (`gate_g1.tsv`; the 2-unit run kept as `gate_g1_2units_20261007.tsv`; a 3-unit run
f81+f42+f67 gave 0.759/0.838/0.760, mean 0.786):

| held out | signs | nulls | trained signs | unseen | real | shuffle mean | shuffle p95 |
|---|---|---|---|---|---|---|---|
| f81 | 664 | 203 | 74 | 9 | **0.746** | 0.375 | 0.410 |
| f42 | 837 | 110 | 79 | 2 | **0.821** | 0.361 | 0.406 |
| f71 | 1333 | 562 | 79 | 5 | **0.686** | 0.369 | 0.406 |
| f67 | 800 | 126 | 77 | 5 | **0.794** | 0.368 | 0.399 |

Mean 0.762, every unit above its p95: **PASS**. The stock learner (`g1p.py --stock`, `gate_g1_stock.tsv`) FAILs on the same 4 units, 0.426 mean (0.443/0.401/0.451/0.409 vs p95 0.443-0.451), as it did on 2 (0.447/0.390); both rows reported. `tools/interlinear_align.py stream` is tools/stream_align.learn, the stock learner
that does not lock on here (S2 above), so g1p.py's che-anchored learner was used, as the brief's handoff names.

**Pooled key** (`key.tsv`, 82 signs): C 24, M 57 (before: C 42, M 30). 14 values changed, including b- a -> e, g v -> t, h- l -> e,
pi s -> t, m n -> t. On f.13 this made the independent signature check worse ("depvsterla" -> "deptsterea") and the lattice decode's
shuffled-key rank fell 1 -> 2 (it16dip) / 4 (it15); see ../../sforza-pusterla-1447-f13/NOTES.md S5. Read: the held-out gate rewards
the units agreeing with each other's texts, but the Opus-read and Sonnet-read slips label some shapes differently, so pooled values
mix two conventions. A single reading convention across all four slips is the named next step.

## Remaining gaps (SFZ-NEXT, 8 Oct 2026; supersedes SFZ-P's list)
Read so far: 0 unglossed letters read as text; key passes G1 at 0.762 mean held-out accuracy over 4 glossed units (3,634 slip signs)
- one sign-label convention across the four key slips - blocker: not-attempted; Opus vs Sonnet readers split T=/b- and d/g; next: owner sign sorter on those shapes (focus pairs from f71/rec and f67/rec), relabel, rerun g1p.py, ~$2 plus owner time
- second reader for f.81 and f.42 - blocker: not-attempted; single (Opus) reader; next: one blind Sonnet pass per slip on level crops + reconciliation, ~$1.5 each
- f.72, f.75, f.77 with copies f.73, f.74, f.76 as units 5-7 - blocker: not-attempted; pairing not eye-checked; next: pair check, two passes + reconciliation per slip, ~$3 each
- Cerioni 1970 / ASMi cipher registers for a period Pusterla key - blocker: not-attempted; no period key located yet; next: a key-hunt row for the lane, ~$2

## Escalation (SFZ-NEXT, 8 Oct 2026)
- [x] siblings: f.81/f.80, f.42/f.41, f.71/Osio CCCXCI, f.67/f.66 used; f.72, f.75, f.77 remain
- [x] clear-pages: later-hand copies f.80, f.41, f.66 used; Osio's print for f.71
- [ ] known-keys: Cerioni 1970 not checked
- [x] print: Osio III searched (f.71's text printed)
- [x] key-rebuild: key.tsv rebuilt from 4 units, G1 PASS 0.762
- [ ] image-check: second readers for f.81/f.42 and a single label convention
- [x] retry: G1 rerun with units 3-4
Verdict: keep going: 4 internal gaps; cheapest next: second Sonnet reader on f.81 and f.42, ~$3

## Requests

gallica.bnf.fr: 15 (SFZ-P, 7 Oct). SFZ-NEXT (8 Oct): 4 overview canvases (c63, c64, c65, c68) at 1400 px, 1 info.json, 2 native
regions via iiif_lines (c68, c64), 2 native regions for f.66 = 9, one at a time, >= 2 s apart, no errors. archive.org 5 (Osio III and II
djvu text, 2 advancedsearch, 0 errors); raw.githubusercontent.com 2 (asl1883.txt; one 404 on a wrong path).

## Second reader on f.81 and f.42 (SFZ-READ2, account 4, 9 Oct 2026, 11:43 UTC- by date -u)

Worker SFZ-READ2 (Opus; Sonnet subagents for the reads) for LANE DEFAULT-account-4-20261009-1051, brief
`.claude/briefs/runs/2026-10-09-account4-default-1051-jobs.md` J12. Prior-work step (pasted, abridged; full rows in
`../prior-work.tsv`): `tools/prior_work.py sforza-italien1584-1447 --item-spec 'shelfmark=BnF italien 1584;folio=81r;date=1447-03-10;...' --step-type transcribe`
-> exit 4 LOOK 2-leaf (no gloss/clear-copy check recorded); answered `--record ... 'KNOWN: f.81 has its later-hand clear copy f.80 ... consumer gate G1'`
(and the same for f.42 / f.41, 1447-02-14); rerun with `--known-answer gate:G1` -> "exit 0: KNOWN, known-answer work for consumer gate:G1" (both).
Crops: the committed ones, no new cut (images/f81_L02..L25_s1/s2 single-line; images/f42_L01..L15_s1/s2 two-line, the ones SFZ-P read).
A single-line re-cut of f.42 (`python3 tools/iiif_lines.py --image images/src_ark_12148_btv1b100373864_f39_4250_330_3350_2600.jpg --out <scratch> --prefix f42 --overlap 0 --max-width 1700 --distance 55 --prominence 60 --debug`)
found 29 lines against SFZ-P's 30 rows, so it was not used (scratch only).

Reads: one blind Sonnet subagent call per slip, pusterla_labels.md and the crops only (`ciphertext_f81_passB_sonnet.tsv`,
`ciphertext_f42_passB_sonnet.tsv`).
- **f.42: not usable.** The reader returned 494 signs against SFZ-P's 837, lost the upper/lower row mapping of the two-line
  crops (A02 empty, A21-A30 "not mapped one-to-one", its own note) and put its own accuracy at 40-50%. Kept on disk as a
  record; f.42 stays a single (Opus) reader. Next: single-line level crops for f.42 (the 29-vs-30 line count settled by eye on
  the debug overlay) and a fresh blind pass, ~$1.5 plus ~$0.5 for the cut.
- **f.81:** 669 signs vs 664 (both with `g ÷` joined to `g÷`, g1p.py's own rule); `tools/reconcile_passes.py --method nw`
  agreement 510/671 = **76.0%** (f.71 73.8%, f.67 74.3%); 161 disagreement columns (`f81rec/`). Systematic splits, A (Opus) -> B
  (Sonnet): d -> g 25, b- -> b 12, b- -> T= 11, V -> q 7 / q -> V 2, d <-> d' 7, h -> h- 3, n <-> y 10.

**Reconciliation rule, fixed before any gate was rerun** (rule-based, no image look; one unit): agreed columns kept; a split on a
pair the f.71/f.67 reconcilers settled takes their majority label -- {d,g} -> g (f.71 45:12), {T=,b-} -> b- (f.71 75:0; f.67
went the other way 26:2, the owner-sorter gap), {q,V} -> V (22:17 over both), {h,h-} -> h- (11:1), {d,d'} -> d' (6:1); every other
split and every one-sided gap keeps A (the incumbent reading), graded M. Adoption rule: the reconciled f.81 replaces
ciphertext_f81.tsv only if G1 still PASSes with it (mean >= 0.60, every unit > its shuffle p95); f.13's lattice numbers are
reported either way.

**Result (G1, rule 3: real vs 200-shuffle control, both numbers).** Adopted under the adoption rule: `ciphertext_f81.tsv` is now
the reconciled f.81 (661 signs: 510 agreed, 55 settled by the convention, 96 kept from A; the single-reader file is kept as
`ciphertext_f81_passA_opus.tsv`); `gate_g1.tsv`, `key.tsv`, `align_f81.tsv` regenerated by `g1p.py` (`--check` ok).

| held out | before (SFZ-NEXT) real / p95 | after (SFZ-READ2) real / p95 | nulls before -> after |
|---|---|---|---|
| f81 | 0.746 / 0.410 | **0.768** / 0.420 | 203 -> 192 |
| f42 | 0.821 / 0.406 | 0.834 / 0.411 | 110 |
| f71 | 0.686 / 0.406 | 0.686 / 0.403 | 562 |
| f67 | 0.794 / 0.399 | 0.792 / 0.396 | 126 |
| mean | 0.762 PASS | **0.770 PASS** | |

Key values changed (8 of 82): h- e -> l, q= s -> n, n a -> b, ao d -> m, =y v -> o, :b o -> l, rho h -> b, `?` s -> (none).
h- -> l undoes one of SFZ-NEXT's 14 changes (h- l -> e). All key values stay C or M (rule 4); no H.
Which pairs still split (owner-sorter gap, not touched): T=/b- (f.81: Sonnet reads T= where Opus reads b- 11 times; f.67's
reconciler went T=, f.71's b-), b/b- (12), n/y (10), q/V (9), d/d' (7) -- the f81rec/disagreements.tsv columns are the focus list.
f.81's own d/g split (25 of 161) is now settled to g, matching f.71; f.42 (single reader) still writes d for that shape (d 3.5%,
g 0.5%) against f.71's g 5.9% / d 1.4%.

## Second reader on f.42, single-line crops (SFZ-F42, account 4, 9 Oct 2026, 12:32-12:4x UTC by date -u)

Worker SFZ-F42 (Opus; one Sonnet subagent for the read) for LANE DEFAULT-account-4-20261009-1051, brief
`.claude/briefs/runs/2026-10-09-account4-default-1051-jobs.md` J16. Prior-work step (pasted):
`python3 tools/prior_work.py sforza-italien1584-1447 --item-spec 'shelfmark=BnF italien 1584;folio=42r;date=1447-02-14;sender=Pietro de Pusterla;recipient=Francesco Sforza' --step-type transcribe --known-answer gate:G1 --fetch`
-> 3-tomokiyo CLEAR, 3-solver CLEAR (cached) / UNCHECKED-NET (aaymeloglu, no clone), 4-editions UNCHECKED-NET, 2-leaf KNOWN
(f.41 later-hand clear copy, recorded 11:44) -> "exit 0: KNOWN, known-answer work for consumer gate:G1".

**Crops (scratch only, never committed).** The auto line finder gives 29 bands on this leaf at any distance/prominence tried
(55-62 / 30-60; its auto pitch 77 px against a real ~73 px), and its centres sit between lines. Settled by eye on a ruler
render of the source: **27 cipher lines** (L01 opens "Illustris re[x]."; L27 ends in the clear "sempre me recomando..."),
the clear "febry..." line and the cipher signature group below them; 27 matches SFZ-P's ciphertext_f42.tsv rows A01-A27.
A fixed-y cut lost the right halves (lines slope up to +44 px across the region), so the cut follows the slope:

    python3 tools/iiif_lines.py --image images/src_ark_12148_btv1b100373864_f39_4250_330_3350_2600.jpg --out <scratch>/f42d --prefix f42 --overlap 0 --max-width 1700 --centres 150,266,360,426,516,594,660,730,820,910,984,1090,1156,1240,1320,1380,1460,1540,1610,1680,1750,1830,1920,2000,2080,2160,2220 --follow-slope 300 --top-margin 12 --bottom-margin 12 --debug

54 crops (27 lines x 2 halves, 1700 x 92-96 px); debug overlay and five crops (L06s2, L07s2, L16s1, L26s2, L27s1) eye-checked: the
target line is the central row in each.

**Read (1 unit).** One blind Sonnet call shown only pusterla_labels.md and the 54 crop paths: 842 signs, self-confidence ~55%
(`ciphertext_f42_passB2_sonnet.tsv`; the failed two-line pass stays as `ciphertext_f42_passB_sonnet.tsv`). SFZ-P's single read is
kept as `ciphertext_f42_passA_opus.tsv`. With `g ÷` joined to `g÷` in both (g1p.py's rule), `tools/reconcile_passes.py --method nw
--keep-plain` (`f42rec/`): **agreement 692/850 = 81.4%** (f.81 76.0%, f.71 73.8%, f.67 74.3%); 158 disagreement columns. Top splits
A (Opus) -> B (Sonnet): d -> g 21, q= -> go 7, b- -> b 6, h- -> h 5, go -> o 4, d -> gap 4, b- -> T= 3, z- -> ze/z 6.

**Reconciliation (1 unit), the SFZ-READ2 rule unchanged** (`f42rec/apply_rule.py`, `--check`): agreed 692, settled by the
f.71/f.67 convention 35, kept from A 110 (graded M), B-only columns dropped 13 -> **837 signs** (`f42rec/ciphertext_f42_reconciled.tsv`,
now `ciphertext_f42.tsv`). Adoption rule (G1 still PASS): **met, adopted.** A first run without `--keep-plain` dropped the clear word
`w:siche` (L11) and gave G1 0.772 (f42 0.841); it was rerun with the word kept, and only that run is reported below and on disk.

**G1 (rule 3: real vs 200-shuffle control, both numbers).**

| held out | before (SFZ-READ2) real / p95 | after (SFZ-F42) real / p95 | nulls |
|---|---|---|---|
| f81 | 0.768 / 0.420 | 0.768 / 0.407 | 192 |
| f42 | 0.834 / 0.411 | **0.826** / 0.410 | 110 -> 111 |
| f71 | 0.686 / 0.403 | 0.686 / 0.403 | 562 |
| f67 | 0.792 / 0.396 | 0.794 / 0.401 | 126 |
| mean | 0.770 PASS | **0.768 PASS** | |

Key values changed (4 of 82): L f -> l, So l -> a, ae a -> q, bz e -> c; d (t) fell from C to M (34 -> 15 supporting pairs, the d -> g
settlement moved f.42's d-shape into g: g t 65 -> 85, C), den i C -> M. All values C or M, no H (rule 4).
f.42's d/g convention now matches f.71 and f.81 (g); T=/b-, b/b-, q=/go remain the owner-sorter pairs (`f42rec/disagreements.tsv` is a
fourth focus list).

## Remaining gaps (SFZ-F42, 9 Oct 2026; supersedes SFZ-READ2's list)
Read so far: 0 unglossed letters read as text; key passes G1 at 0.768 mean held-out accuracy over 4 glossed units (f.81 and f.42 now two readers each)
- one sign-label convention across the four key slips - blocker: not-attempted; f.71 and f.67 reconcilers settled T=/b- opposite ways; f.81 and f.42 still split T=/b-, b/b-, q=/go, n/y; next: owner sign sorter on those shapes (focus pairs from f71/rec, f67/rec, f81rec, f42rec disagreements.tsv), relabel, rerun g1p.py, ~$2 plus owner time
- f.72, f.75, f.77 with copies f.73, f.74, f.76 as units 5-7 - blocker: not-attempted; pairing not eye-checked; next: pair check, two passes + reconciliation per slip, ~$3 each
- Cerioni 1970 / ASMi cipher registers for a period Pusterla key - blocker: not-attempted; no period key located yet; next: a key-hunt row for the lane, ~$2

## Escalation (SFZ-F42, 9 Oct 2026)
- [x] siblings: f.81/f.80, f.42/f.41, f.71/Osio CCCXCI, f.67/f.66 used; f.72, f.75, f.77 remain
- [x] clear-pages: later-hand copies f.80, f.41, f.66 used; Osio's print for f.71
- [ ] known-keys: Cerioni 1970 not checked
- [x] print: Osio III searched (f.71's text printed)
- [x] key-rebuild: key.tsv rebuilt from 4 units (f.81 and f.42 two readers), G1 PASS 0.768
- [ ] image-check: single label convention across the four slips (owner sorter); second readers done for f.81 and f.42
- [x] retry: G1 rerun with the reconciled f.42
Verdict: keep going: 3 internal gaps; cheapest next: f.72/f.73 pair check and two passes as unit 5, ~$3
