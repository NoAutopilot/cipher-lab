# PREREG MQS-CLASSIFY-ROUNDS (LANE MQS-2, account 4) -- written 9 Oct 2026 06:34 UTC by date -u, pushed before any score

Option under test: `tools/glyph_atlas.py classify --train-labels TSV [--round R]` -- a person's sorted piles (box id ->
code, optional `round` column) are applied as per-box label overrides on top of labels.json and the kNN classifier is
re-run; `--round R` uses only rows with round <= R (no round column: every row is round 1; R=0 = no train labels).
This is the "train, correct, retrain" loop of Lasry 2026 (HistoCrypt, "Location Matters", hdl 10062/122074, p.4-5)
measured as err_true per round (research/MARY-STUART-TALK-2026-10-09.tsv row M34). Tool job only: no status, key,
reading or AUDIT.md changes; no value-bearing page for the owner (ASKS 118 open). Hosts: none. Vision calls: none.

Atlas: `ciphers/nevers-birago-fr3251-1572/atlas` as committed (labels.json: cluster names + 309 tune-tile overrides;
4,209 boxes). Held-out scoring set: no.87 f.178v L13-L23 + f.179r L01-L03 (all kept out of the vote by `--holdout`,
exactly as atlas/README.md; never trained on in the target arm).

## Metrics (both reported; gate on M1)
- **M1** tools/tx_bench.py, item birago1572-no87 (BENCHMARK-TX.tsv eval), output = k1 of each held-out box per line in x
  order, `_` dropped (the NOTES.md "TX-ATLAS-B72" recipe for atlas/topk/no87_heldout_bench.tsv); `--paired` round 0 as
  BASE gives fixed/broken and the sign-test p.
- **M2** atlas/score_no87.py (label-blind, 1:1 box map, clerk letter) atlas top-1 err_true.
- Expected round 0 (reproduction of committed numbers): M1 0.162 (61/376), M2 0.322. If round 0 differs by more than
  0.005 from either, stop: non-test (environment drift), nothing gated.
- Ceiling check: round 0 is 0.162 / 0.322 err -- far from ceiling; kNN is deterministic, so "more restarts alone" cannot
  move it (no restarts exist).

## Arm C -- positive control, same design and hand (simulated careful person)
Train labels = the no.87 held-out boxes of **half A** (f.178v L13-L18) whose `no87_box_token.tsv` row is `op 1:1` and
whose line-read sign's value (atlas/name_clusters.value_map) equals the clerk truth letter: code = that line-read sign
(a correct sort of one round). Half A is then un-held (votes); **scored on half B only** (f.178v L19-L23 + f.179r
L01-L03, still `--holdout`), M1 restricted to half-B lines (tx_bench scores only lines the output covers), round 0 =
the same half-B lines with nothing trained.
- Null C0: the same boxes, codes permuted among them (seeds 1-20); gain_null = err0 - err1_null.
- Can-differ: the permutation changes which code each trained box carries, hence its neighbours' votes on half B and
  therefore M1; it holds box set, count and code distribution fixed, so it isolates label correctness.
- **Gate C (PASS all three):** gain = err0 - err1 >= 0.02 on M1; gain > p95 of the 20 null gains; paired fixed > broken
  with sign-test p < 0.05.

## Arm T -- the target: the owner's real Birago sort (BIR-OWNER, 3 Oct 2026)
Train labels = `harvest/tx_decode/eye/open/sorter/owner_settled.tsv` (488 tiles on f.117r, f.168r/v, f.144r) mapped to
atlas boxes by the committed label-blind IoU maps `harvest/tx_decode/mix/{f117,f168,f144r}_mixmap.tsv` (tile -> box,
IoU >= 0.2 as recorded there). Code: `new_sign` verbatim for kept and moved (the owner's new piles such as T60-c stay
their own class -- not merged to a parent); taken-out -> `_`; bad-cut, aside and UNREAD -> no row. A box hit by two
tiles keeps the first in file order (counted). Round 1 = all rows. Scored on all 15 held-out no.87 lines (other hand
pages; no no.87 box is trained).
- Null T0: same boxes, owner codes permuted among them (seeds 1-20). Can-differ: as for C0.
- **Gate T (PASS both):** gain >= 0.01 on M1 and gain > p95 of the 20 null gains. A negative gain is reported as such.
- Expected (a guess written before scoring): small, |gain| < 0.02 -- the owner sorted other leaves of a mixed-hand
  family and no.87 is scored by its own hand's labels.

## Outcomes
- C PASS: the loop is shown able to lower err_true when the sort is correct and on the scored hand; T is then read on
  its own gate. Shelf grade at most `ok` only if C and T both PASS; else `weak` with every number (brief: a control
  that misses its gate ships at most weak and is not re-briefed).
- C FAIL: option ships `weak`, T reported as a number only, nothing run on any target from it.
- No further rounds of the owner sort exist on disk (one sort, 3 Oct 2026); multi-round use is the option's
  `round` column, tested offline in tools/tests/test_glyph_atlas.py.
