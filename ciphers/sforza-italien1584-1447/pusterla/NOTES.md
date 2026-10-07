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

## Remaining gaps (SFZ-P, 7 Oct 2026)
Read so far: 0 unglossed letters read as text; key passes G1 at 0.661 mean held-out accuracy over 2 glossed units (1,501 slip signs)
- f.71/copy and f.67/copy as units 3-4 - blocker: not-attempted; would raise key coverage and accuracy; next: same per-unit procedure, add to g1p.py UNITS, ~$4 each
- second reader for f.81 and f.42 - blocker: not-attempted; single-reader; next: one Sonnet pass per slip on deskewed single-line crops with pusterla_labels.md, reconcile, ~$1.5 each
- Cerioni 1970 / ASMi cipher registers for a period Pusterla key - blocker: not-attempted; next: a key-hunt row for the lane, ~$2

## Escalation (SFZ-P, 7 Oct 2026)
- [x] siblings: f.81/f.80 and f.42/f.41 used; f.67, f.71, f.72, f.75, f.77 remain
- [x] clear-pages: later-hand copies f.80, f.41 used
- [ ] known-keys: Cerioni 1970 not checked
- [x] print: Osio III searched (f.71's text printed)
- [x] key-rebuild: key.tsv rebuilt, G1 PASS
- [ ] image-check: second readers for the two slips
- [ ] retry: G1 rerun with units 3-4
Verdict: keep going: 3 internal gaps; cheapest next: second reader on f.81, ~$1.5

## Requests

gallica.bnf.fr: 15 (8 overview canvases at 1000-1400 px, 3 info.json, 4 native regions for slips and copies, plus the
f.15 region for f.13 and its info.json), one at a time, at least 1.5 s apart, no errors. archive.org 1 (Osio III djvu
text). WebSearch 7, WebFetch 1 (ciphermysteries.com).
