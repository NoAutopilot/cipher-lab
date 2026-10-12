# TXE4-7 PILE-LM -- RESULTS (12 Oct 2026, 01:18-01:5x UTC by date -u)

Worker TXE4-7 (account 3, Fable 5.1, session_017cQg5u4KuyzdGguJKfb3yR), brief `.claude/briefs/runs/2026-10-11-acct3-txe4-7.md`
(93b7bb32), for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). PREREG `benchmark-tx/PREREG-txeng4-7.md` committed
86a382d1 before any map check, Delta or score (`tx_register.py --check`: `OK benchmark-tx/PREREG-txeng4-7.md: names register
rows and states a difference`); tool, test and maps e78c5e3a; every built output committed with `SHA256SUMS.prescore` 9eb0af62
before any tx_bench call. Read-free: no vision call, no reader, no subagent, no network beyond git and one `pip install
scikit-learn scikit-image opencv-python-headless` (glyph_atlas.py's own imports, absent from this container; 0 requests to any
archive host). No truth or flags file edited; truth opened only by tx_bench.py and tx_power.py (scorer side). No frozen confirm
item opened.

**Verdict (pre-registered rule): dev-FAIL -- the positive control is not met (1 of 20 planted piles restored, gate >= 12), so the
job STOPPED before any eval look. Non-test on the targets: no.87 eval_heldout and f152r were never scored, no LOOKS.tsv row
was written. The tool as the brief specified it cannot see a planted whole-pile error against its own shuffled-key null.**

## What was built
- `tools/key_decode_lattice.py pile-relabel` (new subcommand; offline test `tools/tests/test_key_decode_lattice.py::
  test_pile_relabel_restores_planted_pile`, 15/15 tests pass): piles = (atlas cluster of the position's 1:1 box, read sign);
  candidates = the read sign's top-3 confusion neighbours + the other pass's sign at the pile's disagreement rows, key signs
  only; Delta(p, c) = summed line-LM gain of relabelling the whole pile; null = the same Delta under 20 value-shuffled keys;
  accept when Delta > 0, Delta > the null max, |p| >= 2. Controls as options: `--key-shuffle S`, `--cluster-shuffle S`,
  `--plant CLUSTER:SIGN:NEW [--plant-exclude-original]`. Output grade S, never H.
- Machine-only box map (R4a; `build_map.py`): round-1 kNN from 588 sibling reader-agreed boxes (atlas/secure_tokens.tsv minus
  f152r), round 2 adds 94 f174v boxes whose page passed the join check (f174vB UNCHECKABLE, excluded), then
  `box_token_align.py --topk --check-labels <its top-1> --check-bound` (steered -> leave-one-out). **no.87: PASS**, leave-one-out
  571 / 5 / 2 of 702 at 0 / -1 / +1 (+-2 9, none 115), share0 0.813 vs null p95 0.049, all 26 lines pass; 699 1:1 boxes.
  **f152r: PASS**, 66 / 1 / 1 of 88, share0 0.750 vs null p95 0.080, all 4 lines pass; 88 1:1 boxes. (Reference rows: label-aware
  map 187 / 2 / 2 of 203 PASS; old map 157 / 24 / 14 of 208 FAIL.) Full rows in the PREREG addendum; sidecars in `map/`.
- Harness `run.py` (build, score), diagnostic `diag.py`.

## Positive control (dev_tune, synthetic, pre-registered gate P) -- FAIL
20 seeded corruptions: a dev pile of >= 3 mapped positions relabelled to its read sign's top confusion neighbour, tool run on
the 12 dev lines (`out/build.json` positive_control; per-plant table `score/diag_positive.json`).

| | registered rule (value-shuffled key null, max of 20) |
|---|---|
| restored (to the original sign or a same-value homophone) | **1 / 20** (seed 5: pile (32, T86 e) -> T60 n, n=3, Delta 12.19 vs null max 9.50) |
| false acceptances per run | mean **0.00** (0 in every run) |
| gate P: restored >= 12 AND false <= 1 | **FAIL** |

Why (diag.py, same 20 plants): the real restoring Delta is positive in 18 of 20 plants (0.5 to 20.5, median 5.0) but the
null's maximum over 20 shuffled keys exceeds it in 19 of 20 (null max 7.7 to 43.4). In 10 of 20 plants the null maximum comes
from a shuffle that hands the candidate or the planted sign a multi-letter word value (8 of the key's 51 signs are words,
e.g. T11 carmagnola, T84 quello): relabelling n positions to a word inserts n copies of a well-predicted Italian word into the
line, which scores far above n single letters whatever the context -- the degenerate optimum the PREREG named and judged
neutral because "the shuffled-key null carries the same candidate set"; it is not neutral, because the shuffle moves word
values onto letter signs and the null max is driven by those draws. Even with that removed (EXPLORATORY, declared in diag.py,
dev only, never applied to a target: nulls drawn by permuting values among the 43 single-letter signs only), the null max
(4.3 to 21.4) still exceeds the real Delta in 17 of 20 plants: restored 3 / 20. A max-of-20 null on a sum over 3-11 random
letter changes has a spread the real gain of a 3-11-position fix does not clear. The instrument as specified has no power at
the pile sizes this hand produces (84 piles of >= 2 on no.87, median size 3).

## Look-alike control (dev) -- non-discriminating by construction, not a pass
The real arm accepted 3 piles on no.87; 2 of them have a dev position. Each was re-planted to a random non-neighbour key sign
with its original excluded: 0 / 2 accepted (rate 0.0 <= 0.05). But each planted pile holds exactly 1 dev position, below the
registered minimum pile size of 2, so the tool could not have accepted either whatever the key or LM said: the control cannot
fail differently from the target here (CLAUDE.md rule 3, the bMAT2 / bCAS shape) and licenses nothing.

## Real arm (built, committed, scored on dev only)
- no.87: 699 mapped positions, 137 piles (84 with >= 2 positions), 194 (pile, candidate) pairs scored, **3 piles accepted,
  6 positions changed**: (134, T90 p) -> T84 *quello* at f178v L05.4 (dev) and L22.24 (eval), Delta 13.05 vs null max 6.23 --
  a word-code relabel of two letters, the same degenerate optimum as above; (42, T95 s) -> T51 l at L11.4 (dev) and L15.11
  (eval), 3.43 vs 3.23; (53, X_NEW) -> T92 s at f179r L01.27 and L03.19 (eval), 1.51 vs 1.37.
- f152r: 88 mapped positions, 55 piles (22 with >= 2), 74 pairs scored, **0 accepted**.
- Shuffled-key arms (20): accepted 2-9 piles each on no.87 (mean 4.5), 0-4 on f152r; shuffled-cluster arms (20): 0-4 on no.87
  (mean 1.6), 0-1 on f152r. The real arm's 3 acceptances sit inside the shuffled-key band (built, not scored on eval: the
  outputs are in `out/` with their hashes for anyone who later registers an eval look).
- **Dev safety score** (`tx_bench.py --coverage-diagnostic --exclude-flagged --strict --paired`, no.87 dev_tune, 12 lines; base =
  passC restricted): as measured 19/343 = 0.055 (Wilson 0.036-0.085) -> 19/343 (same), **fixed 0, broken 0, p 1.0**; flagged
  excluded 14/338 = 0.041 (0.025-0.068) -> 14/338, fixed 0 broken 0; strict (visual identity) 9/343 = 0.026 (0.014-0.049) ->
  9/343 and 8/338 -> 8/338; S/D/I base 19/0/0 -> 19/0/0 (m), 14/0/0 -> 14/0/0 (x). The two dev changes: L05.4 T90 -> T84 is
  wrong -> wrong (truth t, flagged alignment-doubtful); L11.4 T95 -> T51 is right -> right (both in the truth set). Net 0
  (the dev safety gate "net >= 0" is met, moot after P).

## Eval -- not scored (registered stop)
No eval unit was scored and no `benchmark-tx/txeng4/LOOKS.tsv` row written (the file does not exist; TXE4 eval looks on
no.87 eval_heldout and f152r by this job: 0). The 11 Oct TXE3 looks on record: TXE3-7 and TXE3-9 on the whole of no.87,
TXE3-10 on no.87 eval_heldout, TXE3-7 on f152r, TXE3-3 on gunther. The six no.87 eval positions TXE3-10's d/s classifier
fixes (f178v L13.20, L15.9, L19.6, L19.24, L21.1, L23.21) are untouched by the real arm (0 of its 6 changes fall on them), and
the d-read-as-s pile itself (102, T18/T98) was one of the 20 planted piles (seed 2, n=11): its restoring Delta 6.17 against a
null max 43.39 (letter-only null 21.35) -- the tool would not have decided that pile either.

## tx_power on the registered pooled gate (run before any eval score, as pre-registered)
Pool eval_heldout (passC, E 15 of 376) + f152r (passZ_pipeline, E 4 of 73): E 19, N 449. A clean fixer of 50% of the errors
passes "fixed > broken, p < 0.05" in 0.971 of draws (30% fixer 0.543); noisy 0.5 fixers 0.009; WORSE, NO-OP and RANDOM-3%
controls 0.000 (`score/tx_power_all.md`). With the six d/s positions set aside (base and output both set to T18 there): E 13,
N 449; 50% fixer 0.692, 30% fixer 0.180, negatives 0.000 (`score/tx_power_ds.md`). The gate had headroom for a real
instrument; the instrument did not reach it.

## Circularity note
On letters whose key is the open question (the f.144 and f.168 rank tests), this tool uses the key under test; any later key
test must pass the shuffled keys through the same relabel first. Moot while the tool stays retired-at-this-design.

## Three sentences for the owner
The key and the language model, used the way this job specified (one decision per pile, accepted only when the gain beats
the best of 20 shuffled keys), cannot make the pile decisions you make in the sorter: on 20 planted pile misreadings it
recognised one. It changed six signs on no.87 and none on f.152r, two of them a word code in place of two letters (the
language model likes inserting a real word anywhere), none of them a fix on the unseen lines it could show, and it would
not have caught the d/s pile either. The sorter's question list cannot shrink on this evidence; the control says why
(the shuffled-key null is wider than any whole-pile gain at piles of 3-11 tiles), which is what a next design has to fix.

## Next step (named, not run)
Not the Birago 1571 f.36/f.47 run the brief names (that was conditional on a pass). A different null for the same pile
statistic, pre-registered before any dev run: (a) shuffle values among single-letter signs only, keeping word codes fixed,
and (b) a z-score or rank rule over 100 shuffles instead of max-of-20 -- diag.py's exploratory letter-only null reached only
3 / 20, so (a) alone is not enough and (b) must be tested on the same 20 plants first; about USD 4, read-free, 20 minutes,
with the same maps (`map/`, join_check PASS) and the same positive-control plants (seeds 1-20). Shelf row: weak.

## Files and reproduction
`benchmark-tx/PREREG-txeng4-7.md` (+ addendum); `build_map.py` (r1, r2, targets) -> `knn/`, `map/` (sidecars); `run.py build`
-> `out/` (133 files: real, base, 20 keyshuf, 20 clshuf per unit, `_ds` twins, `build.json`), `SHA256SUMS.prescore`;
`diag.py` -> `score/diag_positive.json`; `run.py score` was NOT run on eval (registered stop); dev score by the tx_bench CLI
line above; `score/tx_power_all.md`, `score/tx_power_ds.md`. Pre-existing, not this job's: `tools/system_map_check.py` FAILs
on tx_selfcheck.py / tx_tiebreak.py (sibling TXE4 jobs); `tool_shelf.py --check` reports two STALE iiif_lines.py rows.
Request counts per host: 0 (pypi.org via pip for three Python packages: 3 installs).
