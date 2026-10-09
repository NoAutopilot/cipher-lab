# PREREG MQS-LOCK: `family_run.py --param lock=FILE`, one fidelity check (K1) and one gain control (K2)

Written 9 Oct 2026, 04:30 UTC by date -u, by MQS-LOCK (LANE MQS, account 4), and pushed before either control runs.
Brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-lock.md`. Option: `tools/family_run.py` (`read_lock`,
`choose_control_lock`, `unlocked_recovery`, the `lock` path in `main`) and the family hooks in `tools/families/`
(homophonic `fixed=`, nomenclator cribs, wordcode and syllabary held maps, seeded_code `pins` alias). Offline test:
`tools/tests/test_family_run_lock.py`. Driver for both controls: `tools/tests/mqs_lock_controls.py k1|k2`; results to
`tools/tests/MQS-LOCK-controls.tsv`. No target is run in this job.

## Why this is not a fourth try of crib_rounds' held re-anneal (rule 3, third-attempt clause)

`tools/crib_rounds.py` measures a *reader* loop: cribs proposed from a partial decode, round by round; its three runs
(solvEX, solvEX2, ARM3-LOOP, 24-26 Sept 2026) failed because the cribs were too few or too wrong below a ~45% decode.
`lock` measures only the harness step: values confirmed *outside* the run are held, the rest re-run, scored on the
unlocked positions against a control locked at the same token share. It makes no claim that a reader can find the
locks. Promoted from `ciphers/clair1161-avis-flandre-1688/two/reanneal.py` stage 1 as run by `two/lolo_diag.py`
(C1161-LOLO, 4 Oct 2026, PASS 3/3); stage 2 (word cover), which is what failed there, is left behind.

## K1: C1161-LOLO stage 1 through the shared family (fidelity at ceiling; licenses nothing about gain)

- **Material, read-only:** the stream `two_instr.stream()` via `lolo_diag.leaf_stream(drop)` for the six leaves
  (c185R c186R c186L c187L c187R c188L); held signs = every key.tsv sign outside FREE (27 M + `4`, `S`) and the planted
  three (`a`, `p`, `d`, true values u, c, n). Nothing under `ciphers/clair1161-*` is written: keys and rows go to the
  scratchpad and `tools/tests/MQS-LOCK-controls.tsv`.
- **Run:** `families.homophonic.solve([stream], {}, 1, 32, fr17 texts, {"lock": held, "order": "4", "iters": "40000"})`,
  one per leaf stream, seed 1, serial (no Pool). The lock is exactly lolo_diag's `fixed`.
- **Scoring, lolo_diag's own rule (imported, not copied):** consensus letter of a planted sign = its letter in >= 5 of
  6 leaf keys; recovered when consensus = true value AND dL4 (consensus vs `e`, over K* = key.tsv + leaf-1 key +
  consensus) > the p95 of `lolo_diag.lolo_null`'s 50 shuffled-value contexts.
- **Known differences from the local script** (the shared family cannot express them): (1) no `init` -- lolo_diag
  started the planted signs at `e` (PLANT), the family starts every free sign at a corpus-frequency random letter;
  (2) none other: same `homophonic_anneal.solve`, same model (`ha.Model(fr17, 4)`), same 32 restarts x 40000 iters,
  uni_weight 1.0, norm none, seed 1; the MQS-SOLVER kwargs are at their defaults, which call the same `anneal`.
- **Expected 3/3 (the local result, `two/lolo/lolo_ctl_gate.txt`). Gate: 3/3.** A miss grades the option `weak` with
  the reason. A pass shows only that the harness wiring matches the local script.
- **Why its null can fail differently:** the shuffled-value null permutes the *other free signs'* values around the
  planted sign, so dL4 under the null changes with the context while the consensus key's dL4 is fixed; a planted sign
  whose recovered letter is not context-supported falls under the null's p95.
- **Headroom:** none, by design -- this is a licence/fidelity gate (the local PREREG's own point 3), not a gain gate.

## K2: synthetic gain on unlocked positions (the only gain evidence)

- **Design:** MQS-SOLVER published `tools/tests/MQS-SOLVER-controls.tsv`, but its matched design reads 0.947-0.965
  blind at N 800-2600 (no headroom), so K2 uses the fallback: fr16, the homophonic family's default control
  (`homophonic_anneal.make_control`, K signs allotted by letter frequency), **K = 35** (about 1.5 homophones per letter
  over the ~23 letters in use: 1-2 per letter). Corpus: `tools/data/fr16/lettresdecatheri01cathuoft` +
  `lettresindites00marg` (`--corpus`, two files); the family cuts each control window out of the training text.
  Model: order 3, 40000 iters (family defaults). Spec fixture: `tools/tests/fixtures/mqs-lock-k2-N<N>.json`
  (N placeholder tokens, K distinct); rows to `tools/tests/MQS-LOCK-K2-HYPOTHESES.md`.
- **N, chosen before any lock arm runs:** the smallest N in {150, 200, 300, 400} whose blind mean (arm B below, seeds
  1-3, draw 0) lies in [0.30, 0.80]. If none does, stop: non-test, `weak`. Ceiling check: the chosen N's blind mean must
  also be < 0.95 (solvEX's failure shape).
- **Arms** (every arm: `--control-only --seeds 3 --seed 1`, draws `lockdraw` 0, 1, 2 = 3 draws x 3 seeds = 9 runs,
  `lockshare=0.3`, i.e. 30% of the true key's token share, types drawn with weight count^2):
  - **A lock:** restarts 8, lock held (right values).
  - **B blind, same positions:** restarts 8, `lockapply=0` (the same types selected and excluded from scoring, not held).
  - **C blind, 2x restarts:** restarts 16, `lockapply=0`.
  - **D wrong-key null:** restarts 8, `lockperm=1` (the same types held at values permuted among themselves).
  Every arm is scored on the unlocked token positions of its own (seed, draw) selection, identical across arms.
- **Gate (all three):** let gA = mean(A - B), gC = mean(C - B) over the 9 (seed, draw) pairs and sdB = the SD of B
  over the same 9. PASS when gA > gC AND gA > 2 x sdB; **and** the null does not show the gain: mean(D - B) <= 2 x sdB.
  A pass grades the option `controlled-only` on the shelf (synthetic controls passed, not yet a known answer on a target); a miss on any part grades it `weak` with all numbers.
- **Why the null can fail differently from A:** D holds the same signs at the same share, so a gain that came only
  from shrinking the search (fewer free signs) would appear in D too; D's held values put wrong letters into every
  n-gram window that touches a held token, which a right-value lock does not, so D can lose where A gains.
- **Why 2x restarts:** solvEX's German case (24 Sept 2026) showed no gain where more blind restarts already reach
  the same; C is that comparison at equal compute.

## Prior-work step (clair1161-avis-flandre-1688 as the K1 known answer)

`python3 tools/prior_work.py clair1161-avis-flandre-1688 --item-spec 'shelfmark=BnF Clairambault 1161;folio=185r-188r'
--step-type decode --known-answer gate:MQS-LOCK --fetch`, 04:32 UTC: **exit 4** -- "owed before this step: LEAD
1-own:0cac47 (this job's own ROOM claim), LEAD 1-own:8e0bfd (an audited reading of ours exists, status.json), LOOK
2-leaf:82b5dd (no gloss/clear-copy check recorded for this leaf)". Proceeding: the known answer is our own earlier work
on purpose (C1161-LOLO's planted control), K1 decodes no unread text and reads the stream only, so neither LEAD nor the
leaf LOOK bears on a harness fidelity check. (`--derive` and the run above wrote `items.pending.tsv`, `look.tsv` and
`prior-work.tsv` into the clair1161 folder; all three were removed at once -- moved to this job's scratchpad -- since this
job writes nothing there.)

## Amendments

(none yet)
