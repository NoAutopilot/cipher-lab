# VERIFY TXE3-6 UNIT (pen strokes or signs): verifier's audit, 11 Oct 2026 (written 15:1x UTC by date -u)

Verifier: an Opus 5.5 subagent of the account-3 parent's workflow (parent session_0198Cv8ypBfBVfRToKVWx33M). It did not
run TXE3-6 (session_0168bM3qJgyNJdKy6fE6dMAr) and does not protect its conclusions. Method: committed files only, at
origin/main 4b3920055. The committed `tools/tx_bench.py` and the offline test of the new `glyph_atlas.py segment` option
were re-run into a scratch directory. No model reading pass, no image, no network beyond git. No owner sorter page, L74
oracle answer or frozen confirm item was opened (the experiment's scripts reference none of them either: grep of seg.py,
labels.py and classify.py for oracle1, f103r, confirm2, settled, merges and recuts finds nothing). The experiment's own files
are unchanged; this file is the only one added.

## Verdict in one line

Every number reproduces byte for byte, the prereg came first, and the registered gate was applied as written: FAIL for
sign units, so pen units stay the default. The owner was told more than that, though. The kNN reads barely better than
chance here, and a reader with **shuffled labels** shows the same pen-vs-split gap (+0.084 to +0.086 against the real
+0.091). The score rose because there were more boxes, not because the reading got worse. So "splitting joined shapes made
the reading worse" is **wrong** as a statement about reading. "The owner's pen-stroke rule holds" is **overstated**: this is a
dev null that keeps the status quo, not a confirmation, and the owner's own cuts were never tested.

## 1. Re-derivation (committed tool, committed outputs)

`tools/tx_bench.py outputs/<c>.<k>.tsv --bench bench_test.tsv --exclude-flagged` for the 5 box sets x {top1, dec}, plus
`--paired ... --ci` for sign vs pen and each random seed vs sign. All 14 regenerated files are **byte-identical** to
`scores/*.txt`. `truth_test.tsv` matches the 662 rows of the 13 test lines in
`benchmark-tx/vivonne1573-f102r-dev2.truth.tsv` byte for byte (source sha256 007a8be9... confirmed). Its status counts
are 417 scored (201 of them flagged) and 245 excluded. The box counts per line in `seg/*/boxes.tsv` and `outputs/*.top1.tsv`
match RESULTS (pen 569, every split set 653). The (c) boxes that differ from (b) number 150 / 150 / 144, as reported. The
split cut 66 pen boxes into 150 pieces, as reported. `tools/tests/test_glyph_atlas.py` passes (`ok`).

| figure (13 test lines, 417 scored) | reported | re-derived |
|---|---|---|
| top-1 err_true as measured: pen / sign / rand1 / rand2 / rand3 | 0.772 / 0.863 / 0.830 / 0.854 / 0.861 | same (322 / 360 / 346 / 356 / 359 of 417) |
| top-1 flagged-excluded err_true (216 scored) | 0.875 / 1.069 / 1.005 / 1.014 / 1.069 | same |
| standard SER (S/D/I), pen; sign | 0.712 (219/64/14); 0.799 (264/28/41) | same |
| standard SER, rand1 / rand2 / rand3 | 0.782 / 0.813 / 0.789 | same |
| Wilson 95% on err_true (pen; sign) | 0.730-0.810; 0.827-0.893 | same arithmetic (`tx_bench.wilson`), but see objection 6 |
| after decode: pen / sign / rand1-3 | 0.770 / 0.825 / 0.801, 0.849, 0.847 | same |
| decode control, real-key rank of 101 (lattice; top-1) | 8-12; 2 | pen 8, sign 12, rand 8/11/8; top-1 2 in all five |
| sign vs pen: lines improved / worsened / tied, line p | 3 / 8 / 2, 0.227 | same (0.2266) |
| sign vs pen: unit-cost edits; McNemar fixed/broken (p) | 297 -> 333; 46 / 39 (0.52) | same (0.5154). Position errors pen 262, sign 255 |
| sign vs pen: paired SER bootstrap | +0.024 .. +0.160 | same |
| rand1/2/3 vs sign: line p; McNemar p | 0.727/0.344/0.774; 0.74/1.00/0.54 | same |
| grid choice W, P (train sum abs diff) | 1.5, 0.85 (66) | same (grid.tsv) |
| exemplars | 364, 27 codes (154 round 0 + 210 round 1) | same (labels_report.txt) |

### 1b. What the reported numbers do not show: the chance level (new here, read-free, from committed outputs)

`tools/tx_bench.score_item` was applied to each set's committed top-1 output with the labels destroyed and the boxes kept.
Null A permutes each set's own labels across its test boxes. Null B draws every label i.i.d. from the 364 exemplar labels.
Each null used 200 draws (script in the appendix).

| box set | real err_true | null A mean [2.5-97.5%] | real's gain over chance (A; B) | real SER | null A SER mean |
|---|---|---|---|---|---|
| (a) pen | 0.772 | 0.818 [0.784-0.861] | 0.046; 0.050 | 0.712 | 0.768 |
| (b) sign | 0.863 | 0.902 [0.866-0.940] | 0.039; 0.045 | 0.799 | 0.841 |
| (c) rand1 / 2 / 3 | 0.830 / 0.854 / 0.861 | 0.899 / 0.904 / 0.899 | 0.069 / 0.051 / 0.038 (A) | 0.782 / 0.813 / 0.789 | 0.839-0.843 |

- **Sign minus pen**: real err_true **+0.091**. With labels that carry no shape information: null A **+0.084**
  [0.031, 0.139], null B **+0.086** [0.031, 0.146]. SER: real +0.086, null A +0.073 [0.029, 0.113]. The whole gap the
  RESULTS attribute to the split is reproduced by box count alone. What remains attributable to reading is about
  0.005-0.007, inside the noise.
- The kNN beats chance by only about 0.04-0.05 in both units. Sign's real err_true ranks 5th of 201 against its own null A,
  and pen ranks 2nd. The reader is barely above chance in either unit.
- Where the gap comes from: insertions (pen 60, sign 105 under the 0.75-indel alignment). Null A expects 67.5 vs 113.9 at
  chance. Position errors (wrong + deleted) are *lower* for sign units (255 vs 262, McNemar fixed 46 / broken 39), as they
  are at chance (265 vs 274). Three lines where the split made more boxes than truth positions carry 25 of the 36-edit
  difference: L02 (69 boxes for 56 positions, +9 edits), L10 (54 for 47, +10) and L34 (45 for 40, +6).
- Illustration only, a model rather than evidence about cut quality: take the truth's own ref_sign sequence per test line,
  bring it to the pen and the sign box counts per line by random merges or inserts, and add label noise q. The scorer then
  gives pen 0.322 vs sign 0.321 at q = 0, and the sign penalty grows to +0.063 at q = 0.75 and +0.084 at q = 0.9. On these
  box counts the scorer's preference for fewer boxes is a function of reader noise. (The floor of 0.204 at q = 0 comes from
  85 scored positions whose ref_sign lies outside the truth set.)

## 2. Prereg order and deviations

- Times (%cI): PREREG 853c1a1a6 at 05:59:37. Tool option f7406b2a9 at 06:03:58. Results, outputs, scores and amendment
  164f4c006 at 06:12:58. ROOM claim 05:50, done 06:13. The prereg precedes every committed output. Nothing contradicts
  its "before any segment, classify or score", but git cannot prove it, because no intermediate artifact was committed.
- Amendment 1 (L14 dropped; it has no truth rows) was committed in the same commit as the scores, so "before any score was
  read" rests on the worker's word. It is consistent with the scorer: `tx_bench` exits 2 on an output line id absent from
  the truth, so the first scoring call could not have printed a figure. Benign: L14 cannot be scored at all.
- Small undeclared drifts. The option is named `--split-piece`, not `--piece`. The rule-3 check reports "different
  geometry" where the prereg says "pixel content", which is equivalent in effect. `bench_test.tsv`'s notes still say
  "14 TEST lines". `seg.py` still lists L14 in TEST, which is harmless because it carries no truth.
- Cost and time: the ledger shows USD 12.79 against the USD 15 cap; 05:48-06:13 UTC against the 2 h box. Inside both.

## 3. Gate as registered and what it yields

Registered: "err_true(b) < err_true(a) AND paired fixed > broken with the tool's exact p < 0.05 AND err_true(b) below every
one of the three (c) seeds. ... If (a) <= (b): pen units stand; a null is a result."
On the numbers: 0.863 is not below 0.772 (fail). Fixed 46 > broken 39, but p 0.52 (fail). 0.863 is not below 0.830 / 0.854
/ 0.861 (fail). **Gate FAIL. Case "(a) <= (b): pen units stand", a null.** RESULTS reports this correctly. The registered
verdict is a null that keeps the status quo. It is not a finding that the split harms reading, and the gate has no chance
level check that could tell those two apart (section 1b).

## 4. Control (rule 3)

- (c) random cuts **can** vary on the statistic: the same box count, cuts moved, and 144-150 of 653 boxes with different
  pixels. It **did** vary: err_true 0.830-0.861, a seed spread of 0.031.
- It has **no discriminating power** at this reader strength, which is the bMAT2 shape. The kNN sits only 0.04-0.07 above
  its own chance level in every split set, about the size of the seed spread. A cut-placement effect would have to show up
  inside that margin. No positive control shows that correctly placed sign boundaries read better than random ones under
  this classifier. "(b) ties (c)" is therefore a non-test of whether the column-ink minimum finds sign boundaries. It is
  not evidence that it fails to find them.
- The primary (a)-vs-(b) contrast had **no control for the box-count confound**. The paired bootstrap tests the SER
  difference against zero. At chance the expected difference is +0.07 to +0.08, not zero (section 1b).

## 5. Split

The run is dev only, as registered. The item is vivonne1573-f102r-dev2, and its 13 test lines were never used in the
(W, P) grid (`seg.py grid` sums train lines only) or for labels (`labels.py` and `classify.py round1` iterate TRAIN). No
eval item was looked at, and confirm2 was not touched. Per TRANSCRIPTION.md ("tune on dev, report on eval") this is a dev
result. RESULTS says so, but the owner-facing sentence drops it.

## 6. Claims told to the owner

| claim | verdict | evidence | corrected sentence |
|---|---|---|---|
| 1a "The owner's pen-stroke rule for boxes holds" | **overstated** | The registered gate yields a null: no evidence to change the default, which is not a confirmation. One dev leaf, 13 lines, a kNN at chance + 0.05. The owner's own cuts (L74 recuts) were never scored. Pen units were the segmenter's connected components, and the alternative tested was a machine split. | "On 13 Vivonne lines, a machine split of joined shapes gave no reason to change the pen-stroke rule, so it stays the default. The test could not tell the two units apart, and your own cuts were not tested." |
| 1b "splitting joined shapes made the reading worse" | **wrong** (as a statement about reading) | The score did rise (err_true 0.772 -> 0.863). Shuffled-label readers show the same rise (+0.084/+0.086 vs +0.091), and the reader's gain over chance is the same in both units (0.046 vs 0.039). Position errors fell (262 -> 255; fixed 46 / broken 39). The rise is the scorer charging extra boxes at near-chance labels. | "Splitting raised the error score only because it added boxes that a near-random reader fills with wrong signs. Whether splitting helps or hurts reading is untested until a reader well above chance is tried." |

## 7. Objections and rule issues

1. **Chance-level confound (material).** The headline contrast is box-count-driven at a near-chance reader (section 1b).
   RESULTS' "Splitting ... made the downstream read worse" and its recommendation line "a non-improvement ... 8 of 13 lines
   worse, paired bootstrap +0.02 .. +0.16" read a scorer artifact as a reading effect.
2. **Control without power (material).** "The column-ink minimum is not finding sign boundaries on this hand", "it does
   not know where one sign ends", "only a person's cut can be trusted there" (RESULTS, Gate and owner paragraphs). This
   classifier cannot see cut placement (section 4), so these sentences are untestable from this run, not findings.
3. **Owner-facing sentence drops the conditions RESULTS itself lists:** weak classifier, dev result, one leaf, machine
   split only. The owner-account orchestrator's ROOM line (06:49) and the LEDGER row repeat it as "confirms pen-unit boxes
   beat ink-minimum splits ... matching the owner convention" and "a split that fixes the count can still lose -- score
   the read, not the count". Here the score penalised the count, not the read.
4. **Possible misreading by the owner.** "Splitting joined shapes made the reading worse" can be heard as "don't cut joined
   shapes yourself". RESULTS' own recommendation is the opposite: show the 9 "likely several" shapes to the owner as cut
   questions. The owner-facing sentence should not discourage the owner's cuts.
5. **Over-split from per-crop scale (design, as registered).** The split threshold is W x each crop's own median height.
   f102r_L02_s2's median is 36 px and L10_s1's is 51 px, against a leaf median of 62.5 px over 72 crops. These two lines
   took the largest losses (+9 and +10 edits; L02 got 69 boxes for 56 truth positions). The tool already has
   `segment --median-h pool` for this case. This is not a fault in executing the prereg, but a sign-unit set built with a
   pooled scale was never tried.
6. **Wilson intervals on err_true.** RESULTS quotes Wilson 95% intervals on a rate whose numerator includes insertions.
   `tx_bench`'s own note (7) withholds them for that reason, and the flagged-excluded err_true exceeds 1. The prereg asked
   for them; the arithmetic is right, but the intervals are not valid for this rate. The line bootstrap of SER is the
   valid one.
7. **Exemplar asymmetry (noted, not decisive).** The frozen exemplars were cut from the train lines' (b) sign-unit boxes,
   which biases the classifier toward (b) if anything. (b) still did not win, so this does not flip the direction. Round 1
   labels come from 210 of about 980 boxes the round-0 kNN already matched, which RESULTS states.
8. Flagged-excluded figures are always quoted beside the as-measured ones (TRANSCRIPTION.md met). There is no novelty
   wording (rule 10 n/a). Cost is under the cap. There is no third-attempt issue: this is a first attempt, and RESULTS
   correctly forbids re-tuning W/P.

## 8. One sentence the parent can safely tell the owner

"On 13 Vivonne lines, a machine split of joined shapes gave no reason to change your one-box-per-pen-stroke rule, so it
stays the default. The shape matcher used reads barely better than chance, and its worse score after splitting comes only
from having more boxes, so this test cannot say which unit reads better or whether your own cuts would help. That waits for
a stronger reader (about USD 6)."

## Appendix: the chance-level null (re-run from committed files; about 1 minute)

```python
# python3 null.py <checkout> 200   -- null A: each set's own labels permuted across its test boxes; null B: labels drawn
# i.i.d. from labels_train.tsv's 364 exemplar codes. Boxes per line kept. Scored with tools/tx_bench.score_item.
import sys, random, statistics
sys.path.insert(0, sys.argv[1] + '/tools'); import tx_bench as tb
base = sys.argv[1] + '/benchmark-tx/txeng3/6/'; truth = tb.read_tsv(base + 'truth_test.tsv'); NP = int(sys.argv[2])
def errs(o):
    r = tb.score_item(truth, o, 'delete', G=0.75); u = tb.score_item(truth, o, 'delete', G=1.0)
    return dict(et=(r['wrong']+r['deleted']+r['inserted'])/r['scored'], ser=(u['wrong']+u['deleted']+u['inserted'])/u['scored'])
outs = {c: tb.load_output([base + 'outputs/%s.top1.tsv' % c]) for c in ['pen', 'sign', 'rand1', 'rand2', 'rand3']}
pool = [r['code'] for r in tb.read_tsv(base + 'labels_train.tsv')]
def perm(out, rng, pl):
    flat = [(l, i) for l in out for i in range(len(out[l]))]
    labs = [out[l][i] for l, i in flat] if pl is None else [rng.choice(pl) for _ in flat]
    if pl is None: rng.shuffle(labs)
    o2 = {l: list(v) for l, v in out.items()}
    for (l, i), s in zip(flat, labs): o2[l][i] = s
    return o2
real = {c: errs(o) for c, o in outs.items()}
for name, pl in [('A', None), ('B', pool)]:
    rng = random.Random(11); nl = {c: [errs(perm(outs[c], rng, pl)) for _ in range(NP)] for c in outs}
    for c in outs:
        e = sorted(x['et'] for x in nl[c]); print(name, c, 'real %.3f null mean %.3f [%.3f, %.3f]' % (real[c]['et'], statistics.mean(e), e[int(.025*NP)], e[int(.975*NP)-1]))
    d = sorted(a['et'] - b['et'] for a, b in zip(nl['sign'], nl['pen']))
    print(name, 'sign-pen real %+.3f null %+.3f [%.3f, %.3f]' % (real['sign']['et'] - real['pen']['et'], statistics.mean(d), d[int(.025*NP)], d[int(.975*NP)-1]))
```
