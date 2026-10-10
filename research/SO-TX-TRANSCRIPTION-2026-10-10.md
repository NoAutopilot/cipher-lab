# Outside review of transcription measurement — 10 October 2026

Scope: image-to-sign transcription only. No cipher solution attempted. This is an assessment and proposed preregistration, not an executed recognition experiment.

Reviewed snapshot: `0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68`. All eight previously fetched file blobs below were checked against that commit and matched. TX-PROGRAM was also read first. The scorer blob was `5cba25bcc70d55d010ab79ce1ad4924c60aa8556`. Repository access succeeded through the GitHub connector when the web reader failed.

## Verdict

The programme has useful failure records and an unusually active internal reviewer, but its present benchmark does not establish full-page, exact-sign error on unseen hands. A contemporary decipherment can independently fix plaintext without independently fixing the number, boundaries or identities of the cipher signs. The present truth construction sometimes inherits these from a model reading, and accepts different signs with the same value.

The highest-priority work is an independent visual reference plus a corrected scorer. More preregistered reader variants cannot repair a measurement that rewards agreement with the reference builder. The stated 15.0–29.6% is not a mathematical error interval: neither endpoint is a demonstrated bound on full-page sign error.

## 1. Measurement

### Separate the tasks and labels

Maintain distinct records for (a) physical sign instances and locations, (b) visual sign-class IDs and admissible allographs, and (c) key values. Score exact visual IDs for transcription. Keep value-compatible scoring as a separate downstream metric.

TRANSCRIPTION explicitly says the truth is a set of signs compatible with a plaintext value, homophone swaps are invisible, the no.87 reference was aligned on the reconciled reading, and Ceppo S truths depend on the committed readings. These are material limitations of the estimand, not merely caveats about sampling uncertainty.

The S2 recipe describes a value-blind **text-list** sheet, not a visual atlas. Its later repaired adjudication also preserved 167 agreed-uncertain rows. Thus the abstract description of “atlas + adjudication” is insufficient to identify the tested system. Version and retain actual image packets, vocabulary, prompts, models, crop geometry and adjudication implementation.

### Reproduced scorer behavior

A local unmodified snapshot of tools/tx_bench.py was imported and tested with synthetic signs only. No benchmark truth was changed or cipher read.

| Case | Observed behavior | Consequence |
|---|---|---|
| Truth has L1=A, L2=B; output contains L1=A only | 0 errors / 1 scored; L2 merely listed missing | Dropping a difficult line can improve the headline rate. |
| Truth has L1=A; output adds EXTRA=X X | Extra line ignored | Out-of-scope line IDs are not rejected or charged. |
| A second truth position is flagged; baseline wrong only there; candidate correct | CLI with --exclude-flagged --paired still reports n=2, fixed=1 | The displayed exclusion policy is not the paired policy. |
| Truth A B; baseline A X B; candidate A B | SER 0.5 -> 0.0, paired fixed=0, broken=0 | A pure insertion repair is invisible to the adoption test. |
| ref_sign=A, truth=A\|HOMOPHONE; output HOMOPHONE | Zero errors | A wrong visual symbol can be credited through its key value. |
| One reference sign, four extra output signs | Rate 4.0, Wilson interval approximately [0.207,1.0] | The interval is not an interval for that rate. |

The CLI issue follows directly from main(): the ordinary report calls score_item(drop_flagged(truth), ...), but the paired branch calls paired(truth, ...) without dropping flags. The actual S2 report confirms the symptom: the paired denominator is 1,068 although the accompanying flagged-excluded rate uses 500. This does not prove every external experiment harness has the bug; audit each binding gate's actual invocation and input transformations.

Whole-line omissions should count as deletions on a fixed evaluation manifest; unknown line IDs should fail validation. A partial-coverage diagnostic needs a distinct name and declared coverage. A paired test must use the same endpoint and population as the adoption criterion, including insertions.

### Alignment and error taxonomy

Token-level Levenshtein distance is appropriate. Alignment is not itself the problem. Use one atomic token per visual sign and primary SER=(S+D+I)/N with unit edit costs on complete reference lines. Report S, D and I separately.

This scorer chooses alignment with indels costing 0.75, substitutions 1, and a zero-cost match when output equals either ref_sign or a truth-set member; it then counts edits at unit cost. Thus its optimizing objective differs from its reported objective. Any special alignment belongs beside standard SER and needs a ranking-sensitivity check.

“Deletion” and “insertion” in an edit alignment are not verified physical segmentation causes. Repeated symbols, uncertain truth, line seams and reading-order errors can change the edit path. Diagnose merges, splits, detached marks, line omissions, seam duplications and plain-text intrusion from image coordinates. Audit a random sample of correct as well as incorrect regions.

### Flags are two different things

The prompt describes reader uncertainty, but the implemented --exclude-flagged uses **truth-file verifier flags**. These must not be combined.

* Reference uncertainty: freeze image-supported, model-independent masks before predictions. Publish how much ink and which sign classes remain unscorable.
* Reader abstention: keep unknowns in the full-output error measure, and separately report accepted-token error versus coverage and actual correction effort. Compare systems at fixed coverage, not just at whatever fraction each chooses to answer. This is the risk–coverage framework [R5].

For S2, 500 of 1,068 initially scored positions remain, but the reference contains 2,033 raw positions: about 24.6% of reference positions enter the flagged-excluded denominator. Its flags preferentially remove disagreements of the earlier reference builder. A fresh reader can inherit this selection advantage without ever opening the truth file.

There is also an asymmetric numerator: all line insertions remain when reference positions are excluded. S2's 75/500 is (54 position errors + 21 line insertions)/500; f.102r's 80/403 is (38 + 42)/403. These are not clean conditional error rates. Dividing line insertions by all predicted tokens can be a useful extra diagnostic, but does not fix the primary endpoint. Prefer complete independently labelled lines or physically delimited spans with a fixed inclusion rule.

The “bracket” language in PREREG-S2/TX-RED should be withdrawn. Doubtful truth does not guarantee upward bias; it can accidentally favor a prediction. Homophone acceptance and missing-line exclusions also act downward, while charging all insertions to a reduced denominator can act upward. Report the two operational scores with their masks, without claiming the true page error lies between them.

### Statistics, sealing and reuse

The fixed/broken sign test is the conditional exact McNemar test for paired binary outcomes. It is defensible for independently sampled fixed classification units. Here signs repeat within classes, lines and hands, alignments vary across readers, and insertion errors are excluded. A hand-specific misunderstanding repeated 20 times is not 20 independent demonstrations of generalization.

Compare complete-line/page edit totals, with paired resampling at the independent sampling unit; report per-hand results and a hand-macro average. For generalization to hands, the relevant outer sample is hands, not signs. Bootstrap many signs from one hand does not manufacture more hands. With very few hands, acknowledge descriptive uncertainty instead of claiming a tight population interval. Paired bootstrap has precedent for sequence-level metrics [R6]; choosing the cluster level here is a design requirement, not a result of that paper.

Wilson intervals apply to binomial proportions under suitable assumptions. Edit totals with insertions are not binomial successes; the code's clipping of errors at N for the interval exposes the mismatch.

A single sealed final evaluation is valuable **after** independent reference construction and pipeline freeze. S2 was one fresh-reader test on a previously built item, not an image never seen by the project. Separate these notions. Sealing cannot cure biased truth, and n=1 hand cannot support an across-hand performance guarantee.

“One look per experiment” does not protect a reused benchmark across experiments. Error tables, verifier findings, baseline reruns and “read-free” scripts all transmit evaluation information when they guide later design. TX-RED itself documents this. Once inspected, a set can remain a useful regression/dev set; it should cease to support fresh confirmatory claims. Use a final untouched hand set after model selection, or a genuinely prespecified multiple-testing/sequential scheme.

Do not ban correction of invalid scoring merely to preserve “one score.” Rescore **frozen existing predictions** after an independently justified scorer/truth repair; preserve old versions and declare the corrected audit. This does not restore the item's unseen status or license another tuned reader pass.

Finally, power depends on breaks as well as fixes and on correlation. At N=1000 with 32 baseline errors, fixing 30% yields 9.6 expected repairs; breaking just 1% of the 968 correct signs yields 9.68 expected new errors. A “clean fixer” power calculation is optimistic. Selecting leaves chiefly because they supply baseline errors also changes the population being evaluated.

## 2. Is 5% realistic?

Yes as an engineering objective for some hands, especially with adaptation and human correction. The papers do not establish it for arbitrary unfamiliar alphabets/hands with only a few hundred labelled signs.

| Primary work | Relevant scale and reported performance | Limitation |
|---|---|---|
| Souibgui et al., ICPR 2020/2021 [R1] | At confidence 0.4, five support examples/class and two labelled fine-tuning pages: Copiale SER 11.4%, missing 0.5%; Borg SER 23.6%, missing 0.8%. | Support examples and fine-tuning pages are different supervision budgets; the paper also reports threshold-dependent missing rates. |
| Baena, Kalleli & Aubry, NeurIPS 2024 [R2] | DTLR: Copiale 2.2% with 711 training lines; Borg 8.5% with 195 training lines. Competition variants reach 6.76% Borg and 1.73% BnF for DTLR. | Different dataset splits/versions; these are trained-on-collection results, not a 300-sign unfamiliar-hand guarantee. |
| Lasry, HistoCrypt 2026 [R3] | Strong box+class supervision: Borg 6.6% at 2,500 symbols and 4.26% at 10,000 (TIMM); Copiale 4.46% at 2,500 (DINO). | Larger than a few hundred labels; different supervision and curated datasets, explicitly not directly comparable with competition rates. |

A few hundred labels might give a useful support atlas or bootstrap. It is not enough to assume coverage of a long-tailed 50–100-class inventory. Report token count, class coverage, examples/class and unseen-class token mass. Measure a fixed 0/100/300/1000-label adaptation curve using separate pages and an equal annotation-time budget.

“Unseen hand” needs three declared regimes: no hand-specific examples; a fixed support budget from that hand; and ongoing human correction. A key drawing that only specifies shapes may be allowed support. A sign-to-plaintext mapping is additional semantic information. Do not present those regimes as equivalent.

## 3. Segmentation approaches worth testing

1. **Location-preserving detection.** Predict symbol centers/boxes with a pretrained detector or exemplar-conditioned matching, retaining original page coordinates. Recognition can jointly propose locations and classes, avoiding irreversible connected-component cuts. R1 and R3 are directly about this problem. R3 additionally reports generic detectors with 90–95% location precision/recall on unseen symbol types; this is localization, not 95% exact transcription.
2. **Line recognition with CTC.** Train line image to visual-ID sequence without pre-cutting every symbol; CTC marginalizes unknown alignments [R4]. Transfer learning or synthetic training is needed at small N. Omit plaintext/key language models in a visual-transcription baseline. Check repeated-symbol collapse and rare marks explicitly.
3. **A cheap geometry audit before a new model.** On annotated lines retain small disconnected marks, test alternative joins/splits, and reconcile overlap predictions by page coordinates. One ink component need not be one sign; two dots can be one sign, and a connected blob can contain several. Treat component rules as proposals, not truth.
4. **An oracle-location diagnostic.** Give the same reader human-verified boxes, with labels hidden. If recognition remains poor, a better segmenter alone will not get close to 5%. This is distinct from X12's model-generated count constraint, X19's count anomaly flags, and X13's proposed cell names. It introduces verified spatial information, not another guess from the same reader.

For a learned detector, test a released model before building an architecture. HTRbyMatching publishes code/checkpoints [R7]. Lasry reports 6–25 minute TIMM training runs on an RTX 3090, although annotation and integration are additional costs [R3]. Evaluate localization precision/recall with one-to-one matches plus exact class accuracy and end-to-end SER; good localization alone is insufficient.

## 4. Proposed next one-week preregistration: ORACLE-LOCATION-1

Purpose: decide whether reliable spatial support substantially improves the present reader. This is a finite-benchmark diagnostic and investment decision, not S1/S2 certification of an automatic unseen-hand system.

**Sampling.** Fix three hands before annotation from the already explored benchmark material: Vivonne f.102r, Birago no.87 and one third hand with available images. Name the third hand and its full candidate-line list in the final registration before sampling. Exclude S2 f.103r. Using seed 20261010, select 12 complete lines per hand; if fewer than 12 are available use all, with a minimum of six. Do not select error locations. Commit the exact line manifest before annotation or fresh reader calls. Expected scale: hundreds to roughly 1,500 signs. If three hands cannot supply the minimum, the result is feasibility-only, not a pass.

**Reference.** Build physical boxes, reading order and neutral visual IDs from images. A human checks every line without seeing either arm's predictions or the old reference transcription. A second independent image pass flags discrepancies for human adjudication; report its initial disagreement. Consult decipherment/key values only after the visual reference is frozen, as a separate audit. A frozen atlas specifies visual equivalences; sharing a plaintext value is never an equivalence rule.

If any selected line cannot obtain a defensible complete visual reference, preserve it as unresolved and declare the diagnostic incomplete rather than dropping it after seeing outputs or filling it from language. f.102r may enter by this independent visual route despite its failed plaintext anchor; the old 80/403 is not reused as truth.

**Arms.** A: current two-reader/adjudication pipeline with the same verified visual atlas. B: same model versions, sampling parameters, atlas and source line images, plus the verified numbered boxes; output one visual ID or UNKNOWN per box. B receives location/order/count information but never gold identities. Preserve the unmarked line alongside the overlay to avoid obscuring ink. Run three fresh-context repetitions per arm, in randomized arm order; average all three, never select the best.

This is deliberately oracle-assisted. Forcing one output per known box trivially removes some count uncertainty; that fact is not itself an experimental success. The primary endpoint is the total strict sequence error after identity recognition.

**Scoring.** Use unit-cost token Levenshtein distance on every selected complete line; UNKNOWN is wrong; missing lines are deletions; unexpected line IDs fail validation. Freeze scorer, manifest, reference, atlas, prompts and both arms' output hashes before the single comparative reveal. Let E_Ah and E_Bh be each hand's total edits/reference signs, averaged across the three repetitions. Let M_A and M_B be the unweighted means across the three hands. Report S/D/I and per-line/repetition rates beside these.

**Exact diagnostic PASS: all three conditions.**

* M_B <= 0.70 × M_A.
* M_A − M_B >= 0.03 (at least three percentage points).
* E_Bh < E_Ah for every one of the three hands.

A missing arm, protocol failure or incomplete reference means INCOMPLETE. Valid data missing any numerical condition means NOT PASSED. No pooling substitutions or threshold changes after the result. These thresholds are chosen engineering requirements, not literature-derived significance thresholds.

This small, already explored set does not justify p<0.01 for a population of unseen hands. Report its finite-set effect and repeat variation. Any line-bootstrap interval must be explicitly conditional on these hands/pages; it is not the adoption gate. This avoids replacing sign pseudoreplication with line pseudoreplication while still answering a useful one-week question.

**Decision.** A pass justifies investing in automatic detection or a measured boundary-correction workflow. If B remains above 5%, classification still needs work. A non-pass rejects this reader-plus-location intervention at the chosen effect size, not all segmentation methods. Human annotation minutes/100 reference signs and all model costs are reported separately; B is never called automated.

**Schedule.** Days 1–2 scorer repair/tests and manifest; days 2–4 visual reference/atlas; day 5 freeze and blinded reads; day 6 one score and image-level error audit; day 7 report and choose the next instrument. Do not claim the one-week run has been performed here.

## 5. False-improvement checks

| Risk | Concrete check |
|---|---|
| Truth built from one arm's reading | Record provenance per boundary, label and mask. Re-annotate random complete lines from images without model output. Never let baseline agreement determine inclusion. |
| Semantic key or gloss leakage | Deliver allowlisted image/prompt bundles without plaintext values, names, glosses or decipherments; inspect actual crops. Replace semantic sign names with neutral IDs. |
| Test exemplars in support/training | Record source page/coordinates for every exemplar; compare hashes and perceptual duplicates across splits, including overlapping crops. Declare transductive access separately. |
| Evaluation feedback under “read-free” labels | Maintain a dataset exposure ledger for scores, confusion tables, verifier notes and human corrections. Exposure follows information, not whether the file itself was printed. |
| Full-repository access by “blind” agents | Restrict reader access to the exact bundle and logs. A fresh conversation with access to truth files is not enforced blinding. Do not assert leakage merely because access exists. |
| Selective omissions/flags | Fixed manifest and denominator, missing-line penalty, rejected extra IDs, separate reference masks and reader abstentions; compare at matched coverage. |
| Adaptive label merging | Freeze visual equivalences before evaluation; audit maps that collapse different glyphs, even when values agree. |
| Repeated test use or multiple attempts | Mark exposed material development; reserve fresh hands for the final chosen method. Log all trials, changed endpoints and model updates. |
| Selection by baseline error/headroom | Include a representative manifest selected without scores; keep enriched hard-case diagnostics separate. Report macro-hand and micro-sign metrics. |
| Shared model bias | Measure correlated errors, including agreed-but-wrong regions, against image-grounded reference; fresh calls are not independent scientific witnesses. |
| Stochastic or protocol differences | Fixed versions, equal information/cost budgets, repeated runs, actual file-access logs, and images rather than self-reported “viewed=yes” as compliance evidence. |
| Bogus confidence from small N | Simulate correlated errors and realistic break rates. Do not treat a single hand or few repeat sign classes as hundreds of independent samples. |

## Reproduction snippet

Run against the reviewed scorer (or retrieve it at the snapshot commit). Synthetic labels only:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("tx", "tools/tx_bench.py")
tx = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tx)

def rows(seq, line="L1"):
    return [dict(line=line, pos=str(i+1), ref_sign=s, truth=s,
                 plain=s, status="scored", flag="")
            for i, s in enumerate(seq)]

truth = rows(["A"]) + rows(["B"], "L2")
r = tx.score_item(truth, {"L1": ["A"]})
assert (r["scored"], r["deleted"], r["lines_missing"]) == (1, 0, ["L2"])

truth = rows(["A", "B"])
truth[1]["flag"] = "alignment-doubtful"
base, out = {"L1": ["A", "X"]}, {"L1": ["A", "B"]}
assert tx.paired(truth, base, out)["fixed"] == 1
assert tx.paired(tx.drop_flagged(truth), base, out)["fixed"] == 0

truth = rows(["A", "B"])
p = tx.paired(truth, {"L1": ["A", "X", "B"]}, {"L1": ["A", "B"]})
assert (p["fixed"], p["broken"]) == (0, 0)
```

The separate CLI probe used a two-row truth TSV, with only row 2 flagged, and the same base/output sequences above. Invocation `tx_bench.py out.tsv --bench bench.tsv --paired base.tsv --exclude-flagged` printed flagged-excluded denominator 1 but paired denominator 2 and fixed 1. The S2 production log's 500-versus-1068 denominator discrepancy is consistent with that exact code path.

## Repository evidence

* [Charter](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/research/TX-PROGRAM.md)
* [Transcription standard](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/TRANSCRIPTION.md)
* [S2 preregistration and amendments](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/benchmark-tx/PREREG-txeng2-S2.md)
* [S2 score](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/benchmark-tx/txeng2/s2score/tx_bench_S2.txt)
* [f.102r baseline](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/benchmark-tx/txeng2/viv102base/RESULTS.md)
* [f.102r anchor check](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/benchmark-tx/txeng2/viv102anchor/RESULTS.md)
* [TX-RED findings](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/research/TX-RED-2026-10-09.md), particularly F6, F15, F20, F33–F34, F39, F43, F45, F47–F48
* [Experiment register](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/research/TX-REGISTER.tsv)
* [Scorer](https://github.com/NoAutopilot/cipher-lab/blob/0dc3cf4bd4eed5bd562913cf0cdde3d657e5ac68/tools/tx_bench.py)

## Primary literature

R1. Souibgui et al. A Few-shot Learning Approach for Historical Ciphered Manuscript Recognition. ICPR 2020, proceedings 2021, Table I. https://arxiv.org/abs/2009.12577

R2. Baena, Kalleli and Aubry. General Detection-based Text Line Recognition. NeurIPS 2024; Tables 3 and 5 and cipher dataset splits. https://arxiv.org/html/2409.17095v2

R3. Lasry. Location Matters: Accelerating Historical Cipher Transcription with Detection-Based Models. HistoCrypt 2026; Table 1 and sections 8–11. https://dspace.ut.ee/items/04e66e62-8549-4b1d-b630-24b88a8f9662 ; PDF: https://dspace.ut.ee/bitstreams/0421bad3-ac07-42b6-9489-e5e306d00589/download

R4. Graves et al. Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks. ICML 2006. https://www.cs.toronto.edu/~graves/icml_2006.pdf

R5. El-Yaniv and Wiener. On the Foundations of Noise-free Selective Classification. JMLR 2010. https://www.jmlr.org/papers/v11/el-yaniv10a.html

R6. Koehn. Statistical Significance Tests for Machine Translation Evaluation. EMNLP 2004. https://aclanthology.org/W04-3250/

R7. Authors' HTRbyMatching implementation and checkpoints. https://github.com/dali92002/HTRbyMatching
