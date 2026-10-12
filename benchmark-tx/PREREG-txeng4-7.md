# PREREG TXE4-7 PILE-LM (account 3, worker TXE4-7, Fable 5.1; written 12 Oct 2026 01:3x UTC by date -u; committed BEFORE any map is checked, any Delta is computed or any output is scored)

Brief `.claude/briefs/runs/2026-10-11-acct3-txe4-7.md` (commit 93b7bb32). One of ten TXE4 experiments the account-3 parent
(session_0198Cv8ypBfBVfRToKVWx33M) launched on 12 Oct 2026 for the owner's ask of 11 Oct ("what can our tools do better").
Read-free: no vision call, no reader, no network beyond git and one pip install of scikit-learn/scikit-image/opencv
(glyph_atlas.py's own imports, absent from this container). Work folder `benchmark-tx/txeng4/7/`. Items: birago1572-no87
(dev_tune f178v L01-12 for the controls and the safety gate; eval_heldout f178v L13-23 + f179r L01-03 for the report) and
birago1572-f152r (L01-04, eval). No frozen confirm item is opened; no truth or flags file is edited or read by any arm;
truth is opened only by tools/tx_bench.py and tools/tx_power.py (scorer side).

## Hypothesis
The owner today decides in the sorter, one pile at a time, whether a group of look-alike tiles the machine has piled
together was misread. Hypothesis: the printed key and an Italian language model can make that pile decision instead --
summing, over every occurrence of a pile (one atlas cluster x one read sign), the language-model gain of relabelling the
whole pile to a look-alike candidate, and accepting the relabel only when the gain beats the same statistic under 20
value-shuffled keys -- and doing so fixes more unseen-line signs than it breaks, beyond what TXE3-10's d/s classifier
already fixes.

## Nearest prior and what differs (register ids)
- TXE3-9 PINS (dev-FAIL, null): a per-position key-constrained lattice decode read 0.049 against L at 0.042; pins inside
  the decode did the same as applying them after. Differs: no lattice and no per-position choice here; the decision unit is
  the pile, the statistic is a sum over all its occurrences, and the null is per candidate, not per decode.
- MQS-TX-CROSSWORD (retired, "not re-briefed against no.87"): LM gain flagged single positions and a Sonnet reader re-read
  them open-choice, fixing 1 and breaking 1. This job is a different instrument at the decision end: there is no reader and
  no per-position flag; each pile gets one decision from the summed evidence of all its occurrences against a per-candidate
  shuffled-key null, and the owner's time is replaced by the key and the language, not by another reader.
- TXE3-1 (sorter question order; measured): under pile propagation one pile held 5 of passC's 10 flagged-excluded eval
  errors, the d-read-as-s pile (T98 for T18). Differs: TXE3-1 simulated the owner answering; here no answer is simulated
  and the pile is decided by the key and the LM alone.
- TXE3-10 PAIR (d/s classifier; 6 fixed / 0 broken on the label-aware map, verifier ruling pending): a one-pair image
  discriminator trained on secure tiles. Differs: this tool uses no image feature at decision time, only the cluster
  grouping, the key and the LM; its gate is reported with the six positions TXE3-10 fixes set aside (declared knowledge
  below).
- BOXMAP-LA / TXE4-0 REPAIR (measured): the label-aware aligner and the join gate (tools/join_check.py) this job's map goes
  through. Differs: nothing re-derived; the map is built with those tools and pasted below as an addendum.
- The look-alike pass (LOOKALIKE-TOOL, retired as an accuracy step) is not run; the ':' mark rule, M24 and err_2reader are
  not used (R4).

## Declared knowledge
The brief's writer and this worker know from TXE3-1 and TXE3-10 that a five/six-tile d-read-as-s pile (T98 for T18) exists
on no.87 eval_heldout and that TXE3-10's classifier fixes those six positions (benchmark-tx/txeng3/10/rescore_boxmapLA/
apply_T18_T98_eval.tsv). Nothing in the rule below is tuned on eval; the dev gates come first. tools/tx_power.py is run on
the gate twice, with those positions in and with them set aside, before any eval score; RESULTS report every eval figure
both ways and say how many of the tool's fixes fall on those positions. A pass that rests on them is "weak: the d/s pile
only".

## Fixed inputs (none chosen after a score)
- Bases: `benchmark-tx/outputs/birago1572-no87/passC.tsv` (no.87) and `benchmark-tx/outputs/birago1572-f152r/
  passZ_pipeline.tsv` (f152r). Never labels.tsv, passX20*, key_pins.tsv.
- Other pass (candidate source at disagreement rows): passA/passB of each item (`benchmark-tx/outputs/<item>/passA.tsv`,
  `passB.tsv`), aligned to the base by tools/key_decode_lattice.py's own difflib rule.
- Key: `ciphers/nevers-birago-fr3251-1572/harvest/key_1572_sheet.tsv` as printed (X_CE absent, so never a candidate).
- LM: it16dip (tools/judge_plaintext.py LANG_CORPORA), per-letter bonus and unk_cost exactly as the `decode` subcommand.
- Candidates per pile: the read sign's top-3 neighbours in `harvest/confusion_1572.tsv` (by pair count n) plus the other
  pass's sign at the pile's disagreement rows; a candidate must be a key sign and differ from the read sign.
- Pile = (atlas cluster of the 1:1 box at the position, read sign), over positions whose box is 1:1 on a line that passed
  the join check. Unmapped positions (no 1:1 box, or a line that failed) are never relabelled. Min pile size 2.
- Statistic: Delta(p, c) = sum over lines containing p of [LM score of the line with every position of p relabelled to c]
  - [LM score of the line as read]; the line LM score is the sum over its positions of (log10 P(letter | context) +
  bonus) over the key value's letters, unk_cost for a sign not in the key (state unchanged). Degenerate optimum named: a
  relabel to a longer key value (a word code) adds more bonus-corrected letters; the bonus makes a typical real letter cost
  about 0, so a word code is not favoured by length alone, and the shuffled-key null carries the same candidate set.
- Null: Delta(p, c) under 20 value-shuffled keys (the key's value column permuted over its signs; seeds 1-20).
- Accept the best c for p when Delta_real > 0 AND Delta_real > max of its 20 shuffled Deltas AND |p| >= 2. Each pile's
  Delta is computed against the base read (independent); accepted piles are applied together to the base. A position
  belongs to exactly one pile, so two acceptances never touch one position.
- Output: the relabelled reading (grade S, never H) and a per-pile table (cluster, sign, n, best c, Delta_real, null
  max/mean, accepted).
- Tool: `tools/key_decode_lattice.py pile-relabel` (new subcommand, offline test with a planted pile corruption,
  tools/tests/test_key_decode_lattice.py). If `git log origin/main --since='1 hour ago' -- tools/key_decode_lattice.py`
  shows a sibling TXE4 commit at edit time, the change is kept as `benchmark-tx/txeng4/7/key_decode_lattice.patch` instead
  (R7).

## Box map (R4a), machine-only, pasted as an addendum below once built
- Round 1 training labels: `atlas/secure_tokens.tsv` (636 sibling boxes whose code the two blind readers agreed on, S
  grade; no no.87 leaf; declared limit: its box<->token LCS used the family atlas's kNN under labels.json as a filter,
  which was partly named on no.87 tune lines -- it never supplied a label, and no f152r/f178r/f178v/f179r box is in it;
  f152r rows are dropped from training since f152r is an eval item here).
- kNN: `tools/glyph_atlas.py classify --only-train-labels --train-labels R.tsv --holdout f152r_ --holdout f178r_
  --holdout f178v_ --holdout f179r_ --page all --topk 3` (the held-out pages never vote; labels.json contributes nothing).
- Round 2: on the sibling pages whose segmenter lines match the readers' passage lines one to one (f174v L01-11, f174vB
  L01-11; the other siblings' segmenter line numbering does not match their passages and they stay round-1 only), align
  boxes to the sibling's agreed read (`harvest/<sib>/passC_agreement.tsv` merged signs) with box_token_align --topk (round-1
  kNN) --loo --check-labels (round-1 top-1) --check-bound; 1:1 boxes on PASS lines join the training set; the round-1 ->
  round-2 shift check is pasted. The round-2 kNN classifies f178v, f179r and f152r.
- Target maps: box_token_align --read passC (no.87: atlas pages f178v, f179r, lines L01-23 / L01-03) and --read
  passZ_pipeline (f152r: atlas page f152r lines 2-5 = L01-L04 with TXE3-7's x bounds, benchmark-tx/txeng3/7/map_f152r.py,
  unchanged) with --topk (round-2 kNN) --loo --check-labels (its top-1) --check-bound; the check labels steered the map, so
  the leave-one-out row is the one that counts. tools/join_check.py rows and verdict pasted. On FAIL: failing lines dropped,
  listed, re-checked once; still FAIL -> nothing from that join scored. On UNCHECKABLE: the join is unverified and the
  non-test rule applies (the job stops before any Delta, "non-test: join uncheckable").
- Never: atlas/no87_box_token.tsv, atlas/no87_box_token_labelaware.tsv (its labels include the owner's statuses and seeds),
  benchmark-tx/txeng3/7/f152r_box_token.tsv, txeng/compare/box_pos.tsv, pair/*/box_pos.tsv, --status, --tile-labels.

## Arms
- REAL: the tool on the base with the real key.
- SHUFFLED-KEY arm: the whole tool run 20 times with shuffled key i (seeds 1-20) used as if it were real, each with its own
  20 shuffled nulls (seeds 100i+1..100i+20). Can vary: every Delta changes with the key, so which piles are accepted
  changes.
- SHUFFLED-CLUSTER arm: the whole tool run 20 times (seeds 1-20) with the cluster ids permuted among the mapped positions
  of the same read sign (pile sizes and read signs kept, the shape grouping broken), real key, 20 shuffled nulls. Can vary:
  the piles are different sets of positions, so the summed Deltas and the acceptances differ. This is the chance null for
  the machine grouping (R4a: every arm whose grouping comes from a classifier carries a shuffled-label null in its gate).
- Random-alternative (look-alike) control, dev only: for each (p, c) the real arm accepts on dev, the same pile is
  relabelled in the base to a random key sign that is NOT among the read sign's top-3 confusion neighbours and not c; the
  tool runs on that read with the original sign excluded from the planted pile's candidates (so the only possible
  acceptance is a false one). Acceptance rate over these runs must be <= 0.05. If the real arm accepts nothing on dev, the
  same control runs on the 20 positive-control piles instead (declared here).
- Positive control (synthetic, dev only): 20 seeded corruptions (seeds 1-20) of the dev_tune base: a pile of >= 3 mapped
  positions whose read sign has a key-sign top confusion neighbour is drawn at random, every position relabelled to that
  neighbour, and the tool run. Restored = the corrupted pile accepted back to the original sign or a same-value homophone.
  False acceptance = any other pile accepted in that run (the real arm's own dev acceptances are counted as false here,
  conservatively). Gate P: restored >= 12 of 20 AND false acceptances average <= 1 per run. STOP before eval if P fails.

## Endpoint and gate
Score with `tools/tx_bench.py --coverage-diagnostic --exclude-flagged --strict --paired <base>` (the unit file holds the
unit's lines only; --coverage-diagnostic scores the covered lines, as TXE3-1 did) on no.87 eval_heldout (376 scored / 371
flagged-excluded) and f152r (73 / 70), separately and pooled. Every figure on both masks, with Wilson 95% intervals, never
the flagged-excluded figure alone; unit-cost edits and S/D/I beside; value level with --strict beside.
Dev safety gate (before eval): the real arm on dev_tune scores net (fixed - broken) >= 0 against passC. Else STOP.
Eval gate (all four must hold, pooled eval_heldout + f152r):
1. fixed > broken, exact two-sided sign-test p < 0.05, at value level;
2. real net > the 95th percentile of the 20 shuffled-key arm nets;
3. --strict not worse than the base on either item (a relabel to a same-value homophone is a value fix, not a visual one;
   the count of strict fixes among the fixes is reported);
4. real net > the 95th percentile of the 20 shuffled-cluster arm nets.
Reported twice: on all positions, and with the six no.87 eval_heldout positions TXE3-10's d/s classifier fixes set aside
(the relabelled reading and the base both scored with those six positions set to the TXE3-10 corrected sign, so neither
side can gain or lose there). How many of the tool's fixes fall on those six positions is stated. tx_power.py runs on the
pooled unit before any eval score, with and without those positions.
Declared reading per outcome: all four hold on all positions and still hold with the six set aside -> "pass: the key and
the LM decide piles on unseen lines" (shelf grade still weak at this N); all four hold only with the six in -> "weak: the
d/s pile only"; gate 1 fails with net <= 0 -> "null: the pile decision does not transfer"; gate 2 or 4 fails -> "non-test
at this N: the real arm is inside the chance band" (a chance-band result, never a negative); P or the dev gate fails ->
stop, "dev-FAIL", no eval look.
Circularity note (for RESULTS): on letters whose key is the open question (the f.144 and f.168 rank tests) the tool uses
the key under test; any later key test must pass the shuffled keys through the same relabel first.

## Eval looks (R6)
One row appended to benchmark-tx/txeng4/LOOKS.tsv per eval unit before its first tx_bench call (job, item, unit, sha256,
UTC). Outputs committed with sha256 (benchmark-tx/txeng4/7/SHA256SUMS.prescore) before any score; each scored once by a
committed script (benchmark-tx/txeng4/7/run.py score).

## Units, stop rule and declared reading per units done
Box 01:18-03:18 UTC 12 Oct 2026 (claim 01:18); no unit starts after 02:54 UTC (96 min) or past a running estimate of
USD 12 (Fable floor about USD 9.5 + units done); cap USD 15 (the parent reads it). Units and estimates: (1) map with
shift checks, 25 min; (2) tool and test, 35 min; (3) positive, look-alike and shuffled-cluster controls, 20 min; (4)
tx_power, dev and eval scoring, 15 min. Reading if stopped after unit 1: "map built, tool untested: non-test"; after 2:
"tool built, controls unrun: non-test"; after 3: "controls as logged, no eval look: dev result only"; after 4: the gate.
A null is a result.

## Register check
`python3 tools/tx_register.py --check benchmark-tx/PREREG-txeng4-7.md` output pasted in RESULTS.md.
