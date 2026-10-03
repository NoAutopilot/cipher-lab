# A1-POSNULL results (3 Oct 2026, account-1 worker for LANE-A1)

Pre-registration `PREREG.md` pushed at d05de564 before any score; script `posnull.py` (622edcb0); output `posnull.json`
(per-seed rows). Disk only: 0 requests, 0 vision calls; 654 s on 4 cores. Tool `tools/key_decode_lattice.py` unchanged.
Null: 200 position-shuffled lattices per leaf (seeds 1000-1199; each position keeps its own candidates and priors), printed
1572 key, lam 4, beam 64; on each, the printed key's score S and its rank among 200 value-shuffled keys (seed 1).

| leaf | real S | shuffled S p95 / max / mean | real S rank among 200 shuffled | real rank /201 | shuffled: rank-1 share, median rank | real z vs shuffled z p95 / max | gate |
|---|---|---|---|---|---|---|---|
| f.144r (no.73, 90 signs) | -0.945 | -1.096 / -0.956 / -1.241 | 1 | 1 | 2 of 200, 58.5 | 3.10 vs 1.82 / 3.07 | PASS |
| f.168 (no.85, 122 signs) | -1.019 | -1.299 / -1.209 / -1.413 | 1 | 1 | 0 of 200, 94 | 2.77 vs 0.95 / 1.57 | PASS |
| f.117r (fr.3252 no.77, 279 signs) | -1.081 | -1.334 / -1.297 / -1.414 | 1 | 1 | 0 of 200, 33 | 3.66 vs 1.65 / 1.96 | PASS |

Verdict (pre-registered rule: real rank 1/201 AND real S > shuffled p95): **PASS on all three leaves.** The printed key's
lam-4 decode of the real sign order scores above every one of 200 position-shuffled lattices on each leaf, so the TX-DECODE
rank 1 is separable from the position-shuffled null at these lengths. Margins differ: f.168 and f.117r clear the shuffled
max by 0.19 and 0.22; f.144r clears the shuffled max by only 0.011, and 2 of its 200 shuffled lattices also gave the key
rank 1 (its shuffled z max 3.07 is within 0.03 of the real 3.10) -- the weakest of the three, as in TXD-HOLDOUT.
Not a reading: this licenses only that the sign order carries the key's language signal. No grade changes without a separate
verifier; no reading committed; nothing above S; no novelty classed.
