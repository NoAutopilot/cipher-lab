# A1-POSNULL pre-registration (3 Oct 2026, 11:4x UTC, account-1 worker for LANE-A1)

Written and pushed before any score below is computed. Brief: `.claude/briefs/runs/2026-10-03-acct3-a1-wave7.md` job 1.
Why: TXD-HOLDOUT's gate (a) (printed key vs partition-preserving wrong keys) PASSed on 9 of 15 position-shuffled
lattices (`../holdout/RESULTS.md`), so it cannot license anything. This replaces it with a position-shuffled-lattice null.

Inputs, unchanged: the committed TX-DECODE lattices `../f144r_topk.tsv`, `../f117_topk.tsv`, `../f168_topk.tsv`; the
printed 1572 key `../../key_1572_sheet.tsv`; `tools/key_decode_lattice.py` (viterbi, beam 64, lam 4, unchanged);
languages as TX-DECODE (f144r, f168: it16dip; f117r: fr). Score = `judge_plaintext.NgramModel.score` of the decoded
text (the same statistic TX-DECODE's judge lines report: f144r -0.945, f168 -1.019, f117r -1.081). Script `posnull.py`.

## Null
200 position-shuffled lattices per leaf, seeds 1000-1199 (`random.Random(seed).shuffle` of the lattice's position list):
each position keeps its own candidate set and reader priors, only the order of positions is permuted. Same key, same lam,
same beam, same LM. On each shuffled lattice compute:
- S_shuf = score of the printed key's decode;
- R_shuf = rank of the printed key among itself + 200 value-shuffled keys (`K.control`, seed 1, as TX-DECODE).

## Gate, per leaf (stated in advance)
PASS iff (i) real R = 1/201 (the printed key ranks first among 200 value-shuffled keys on the real lattice) AND
(ii) real S > p95 of the 200 S_shuf (p95 = the value at sorted index 189, i.e. the 190th of 200 ascending).
Reported beside it, descriptive only: real S's rank among the 200 S_shuf; the fraction of shuffled lattices with
R_shuf = 1; real z vs the shuffled z distribution (p95 of z_shuf).
FAIL logs "not separable from position-shuffled null at this length". PASS changes no grade (a separate verifier would be
needed); no reading committed; nothing graded above S; no novelty classed.
