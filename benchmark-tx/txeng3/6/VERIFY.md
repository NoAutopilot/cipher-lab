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

## Second check (11 Oct 2026, written 16:28 UTC by date -u, by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **agree**: 1. Chance-level confound (material): the +0.091 pen-vs-split err_true gap is reproduced by shuffled-label readers (+0.084 / +0.086), so 'made the downstream read worse' reads a box-count effect as a reading effect.
  - Evidence: Second check run 11 Oct 2026 about 15:55 UTC in a sparse worktree at origin/main d1fdd0ba8. The VERIFY.md appendix script, re-run (200 draws), gives the same digits. Null A: pen 0.818 [0.784, 0.861], sign 0.902 [0.866, 0.940], sign-pen +0.084 [0.031, 0.139]. Null B: +0.086 [0.031, 0.146]. Real gap +0.091.

My own split of the null into its parts (100 draws, a different seed):
- Correct scored positions: real pen 155 vs null 143.4; real sign 162 vs null 153.3. So the reader beats chance by only about 9-12 of 417 positions in either unit.
- Insertions: real 60 / 105 vs null 68.4 / 113.0.
- Position errors: real 262 / 255 vs null 273.6 / 263.7.

The tool's own two-rate breakdown sits in the committed scores/pen.top1.txt and scores/sign.top1.txt (flagged mask) and is not quoted in RESULTS: position errors pen 129/216 = 0.597, sign 126/216 = 0.583; insertions pen 60/569 = 0.105, sign 105/653 = 0.161.

The tool's headline paired test does not show 'worse' either: line sign test 3 / 8 / 2, p 0.2266; McNemar 46 / 39, p 0.5154. Only the SER bootstrap (+0.024..+0.160) leaves out zero.

One point of wording: 'scorer artifact' is loaded. The extra insertions are real errors in this pipeline's output. On the over-split lines some cost any reader: 28 surplus boxes on L02 (69 vs 56), L10 (54 vs 47), L34 (45 vs 40) and L32 (53 vs 50). Call it a box-count effect at a near-chance reader, not a scorer bug.

VERIFY.md's q-noise illustration has no committed script, so I could not reproduce it. It is labelled as illustration only.
- **agree**: 2. Control without power (material): the kNN sits 0.04-0.07 above chance and the random-cut seeds spread 0.031, so 'the column-ink minimum is not finding sign boundaries', 'it does not know where one sign ends' and 'only a person's cut can be trusted there' are untestable from this run.
  - Evidence: - Reader's gain over null A (re-run): sign 0.039, rand1 0.069, rand2 0.050, rand3 0.038. Against null B: pen 0.050, sign 0.045.
- I re-counted from seg/*/boxes.tsv: the (c) boxes that differ from (b) number 150 / 150 / 144 of 653.
- The reader is only about 9-12 positions above chance over the whole test set, and only 23% of boxes change between (b) and (c). Any cut-placement effect this reader could show is therefore a few positions at most, which this test cannot detect.
- Observed McNemar for (c) vs (b): 42 / 38, 39 / 39, 52 / 45 (p 0.74 / 1.00 / 0.54).
- No positive control shows that correct cuts beat random ones under this kNN.
- The descriptive fact holds: under this kNN, ink-minimum pieces classified no better than random pieces. The inferences about sign boundaries and 'only a person's cut' are not findings.
- The tie is non-discriminating (the bMAT2 shape), not a non-test by construction: the control can and did vary.
- **agree**: 3. The owner-facing sentence drops the conditions RESULTS lists (weak classifier, dev, one leaf, machine split only). ROOM.md:14684 repeats it as 'confirms pen-unit boxes beat ink-minimum splits... matching the owner convention'. The LEDGER.md:4257 lesson is inverted.
  - Evidence: - ROOM.md:14684, the owner-account orchestrator at 06:49, verbatim: 'TXE3-6 confirms pen-unit boxes beat ink-minimum splits (0.772 vs 0.863), matching the owner convention'.
- LEDGER.md:4257 is written by the TXE3-6 worker's own session (session_0168bM3q), not by an orchestrator. It says 'the segmenter's column minimum is not a sign boundary on this hand' and gives the lesson 'a split that fixes the count can still lose -- score the read, not the count'.
- The run did score the read. What objection 1 shows is that at a near-chance reader the read score is driven by box count. So the lesson draws the opposite moral from the evidence. 'Inverted' is fair in substance.
- Both claims as told to the owner carry none of RESULTS' own Limits: the weak kNN (0.77 on pen units), dev only, one leaf, machine split only.
- **agree**: 4. Owner-misreading risk: 'Splitting joined shapes made the reading worse' can be heard as 'don't cut joined shapes yourself', the opposite of RESULTS' recommendation.
  - Evidence: - RESULTS' Recommendation says to show the 9 'likely several' shapes to the owner as cut questions in the sorter, with the owner's cut recorded as geometry.
- RESULTS' Next step names the owner's L74 recuts as a third set to score, still unscored.
- The claim as told to the owner gives no such caveat. The only cuts actually tested were the machine's (--split-wide, seg/sign) and random ones.
- **agree**: 5. Over-split from per-crop scale: the threshold is W x each crop's own median height. L02_s2 (36 px) and L10_s1 (51 px), against a leaf median of 62.5 px, took the largest losses. --median-h pool exists and was never tried.
  - Evidence: - seg/sign/segment.log lists 72 crops, median of medians 62.5 px, minimum 36 px (f102r_L02_s2). L10_s1 is 51 px.
- Pen to sign box counts per crop: L02_s2 30 -> 42, L10_s1 21 -> 31.
- Per-line edits, which I recomputed with tx_bench.paired: L02 +9, L10 +10, L34 +6, which is 25 of the +36.
- In glyph_atlas.py, segment_page sets mh from the page (line 235) unless shared_mh is set (line 237, from --median-h pool, default mode). --split-wide uses that same mh (line 274).
- The per-crop scale was registered (PREREG: 'W x the page's median sign height'), so this is a design limit, not an execution fault, as VERIFY.md says.
- Nuance: it explains only 2 of the 4 over-split lines. L34_s2 (16 -> 22 boxes at a 70 px median) and L32 (53 vs 50) are not scale-driven.
- A pooled-scale rerun would tell nothing at this near-chance reader (objections 1-2). It is worth doing only under a stronger reader.
- **agree**: 6. Wilson 95% intervals are quoted on err_true, a rate that includes insertions, which tx_bench note (7) withholds.
  - Evidence: - tools/tx_bench.py docstring, note (7): 'No Wilson interval is printed on a rate that carries insertions (any new-mode rate)'.
- The committed scores/*.txt carry no Wilson interval, so RESULTS computed them outside the tool. tb.wilson(322,417) = 0.7295-0.8098 and tb.wilson(360,417) = 0.8270-0.8930, so the arithmetic matches.
- The flagged-excluded err_true exceeds 1 (231/216).
- The worker was following the PREREG, which asked for 'Wilson 95%'. The fault is a PREREG request that conflicts with the tool's rule.
- LEDGER.md:4257 repeats '0.730-0.810'. The valid interval is the line bootstrap of SER: pen 0.712 with no CI quoted; sign 0.743-0.872.
- **agree**: 7. Amendment 1 (dropping L14) landed in the same commit as the scores (164f4c006), so 'before any score was read' cannot be proved from git. It is benign.
  - Evidence: - git log on benchmark-tx/PREREG-txeng3-6.md shows two commits: 853c1a1a6 at 2026-10-11T05:59:37Z, then 164f4c006 at 06:12:58Z (+6 lines, the amendment, together with outputs, scores and RESULTS).
- The tool commit f7406b2a9 is at 06:03:58Z.
- Benign: f102r_L14 has no truth rows, and tx_bench exits 2 on an unknown output line id.
- The first verifier missed one thing: RESULTS cites the prereg as 'committed fdb7a4fec', but git cannot resolve fdb7a4fec ('unknown revision'). The real commit is 853c1a1a6, so RESULTS' provenance hash is wrong.
- Also minor: RESULTS says 74 crops, while segment.log shows 72 segmented.
- **agree**: 8. Minor: the exemplars were cut from the train lines' sign-unit (b) boxes, a bias toward (b); bench_test.tsv's notes still say 14 TEST lines; seg.py still lists L14 in TEST.
  - Evidence: - labels.py line 15 reads seg/sign/boxes.tsv.
- labels_report.txt: round 0 labels 1:1 on the count-matched lines L03, L25 and L33. A one-box shift on such a line mislabels the rest of it, which also helps explain the near-chance reader.
- seg.py:16 TEST includes 14.
- bench_test.tsv's notes column reads 'TXE3-6 scoring subset: 14 TEST lines'.
- None of these changes a number. glyph_atlas's offline test (tools/tests/test_glyph_atlas.py) passes ('ok').
- **agree**: Verifier's verdict on claim 1a ('The owner's pen-stroke rule for boxes holds'): overstated.
  - Evidence: - The registered gate failed on all three conditions: 0.863 is not below 0.772; McNemar 46 / 39, p 0.52; 0.863 is not below 0.830 / 0.854 / 0.861. The PREREG's own wording for that case is 'pen units stand; a null is a result', meaning the status quo stays, not that it is confirmed.
- The pen units were glyph_atlas connected components, not the owner's boxes. The owner's L74 recuts were never scored.
- One leaf, 13 lines, dev only (no eval item in a joining hand is unfrozen).
- Per objections 1-2, the test cannot tell the units apart at this reader.
- **partly**: Verifier's verdict on claim 1b ('Splitting joined shapes made the reading worse'): wrong.
  - Evidence: I agree the claim must not reach the owner as stated. As a statement about reading, nothing supports it:
- The null reproduces +0.084 to +0.086 of the +0.091.
- Per-position errors did not rise: 262 -> 255 as measured, 129 -> 126 of 216 on the flagged mask.
- Above-chance correct positions are about equal: pen +11.6, sign +8.7.

But 'wrong' says more than the run can. The measured score did rise (SER bootstrap +0.024..+0.160 excludes zero), and the reader is too weak to show either direction for reading. So the run cannot establish the opposite claim, that splitting does not hurt reading. The verifier's own corrected sentence says reading is 'untested', which is an overstated/untestable verdict, not a wrong one.

The corrected sentence's 'only because' is also slightly too strong:
- The null's 95% range is [0.031, 0.139].
- Some surplus boxes on the over-split lines (28 on L02, L10, L32 and L34) would cost any reader.
- 'About as much as the extra boxes alone' is the defensible wording.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **overstated**: 1a. The owner's pen-stroke rule for boxes holds
  - Evidence: - Registered gate: FAIL on all three conditions (0.863 vs 0.772; McNemar 46 / 39, p 0.5154; 0.863 vs seeds 0.830 / 0.854 / 0.861). The PREREG's case for this outcome is 'pen units stand; a null is a result'.
- Re-derived byte-identical: 10 single-output scores and 4 paired files, all against the committed outputs.
- Dev only: one leaf, 13 test lines, 417 scored.
- The pen units were the segmenter's connected components, and the owner's own cuts were not scored.
- The kNN is only about 9-12 correct positions above chance, so it cannot tell the units apart.
  - Corrected: On 13 practice lines of one Vivonne leaf, a machine split of joined shapes gave no reason to change your one-box-per-pen-stroke rule, so it stays the default. The test could not tell the two units apart, and your own cuts were not tested.
- **overstated**: 1b. Splitting joined shapes made the reading worse
  - Evidence: True kernel: the measured error score rose, err_true 0.772 -> 0.863 and SER 0.712 -> 0.799. The SER line bootstrap of +0.024..+0.160 excludes zero, but the tool's headline line sign test does not (3 / 8 / 2, p 0.2266).

Unsupported as a reading effect:
- Shuffled-label readers with the same boxes give +0.084 [0.031, 0.139] (null A) and +0.086 (null B), against the real +0.091.
- Per-position misreads plus misses fell: 262 -> 255 (McNemar fixed 46, broken 39, p 0.52), and 129 -> 126 of 216 on the flagged mask.
- The rise is insertions: 60 -> 105, against 68 -> 113 at chance.
- 25 of the +36 edits come from the over-split lines L02, L10 and L34.

Not 'wrong': the run is too weak to show that splitting does not hurt reading either.
  - Corrected: Splitting raised the machine's error score by about as much as the extra boxes alone would cost a reader this close to chance (+0.084 of the +0.091), and the per-sign misreads did not rise (255 vs 262 of 417). Whether splitting helps or hurts reading is untested until a stronger reader is tried (about USD 6).

### Sentence the parent may give the owner

On 13 practice lines of one Vivonne leaf, a machine split of joined shapes gave no reason to change your one-box-per-pen-stroke rule, so it stays the default. But the shape matcher we used reads barely better than chance, and its worse score after splitting is about what the extra boxes alone would cost it. So this test cannot say whether splitting, or your own cuts of joined shapes, would read better; that needs a stronger reader (about USD 6).
