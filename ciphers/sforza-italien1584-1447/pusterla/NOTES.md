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
