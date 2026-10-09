# TXE2-CONF pass conduct (written 9 Oct 2026 16:5x UTC by date -u, BEFORE any reader call; PREREG-txeng2-2.md X4 binding)

- Readers: 3 blind Opus 5.5 subagents (`model: opus`), one call each: L01-04, L05-08, L09-12 (12 crops each, 2x LANCZOS PNG
  from `harvest/make_2x.py --folio f178v --lines 1-12`, gitignored lines2x/). Task texts frozen in `tasks/`.
- Disclosed deviation: the PREREG says "3 calls, pass-A grouping". Pass A read f.178v in two calls split at L10/L11
  (L01-10, L11-23), and the later Opus dev_tune passes (M2, shift) used two calls L01-06 / L07-12; no 3-call grouping of
  dev_tune is on file. The PREREG's call count (3) is kept as binding (cost, per-call load); lines are split evenly 4/4/4.
- Brief: `harvest/blind_pass_brief_1572.md` unchanged + `conf_block.md` (the top-3-with-probabilities block, one extra column).
  Readers see the brief, the block, the blind sheet and the crops only: never truth, passes, decodes, labels or values.
- Raw reads committed in `raw/` and pushed before any score; the worker opens no truth before that push.

## Recorded after the reads, before any score (16:4x UTC by date -u)
- 3 calls returned 108 / 123 / 125 = 356 signs (L positions 354). X_ rows 5 (X_K 1, X_NEW 3 on L05-08; X_A 1 on L12), '?' 2
  (L09, L10 line ends at the gutter).
- Call 3 (L09-12) disclosed that its top-3 probabilities follow a fixed per-grade scheme (H 0.85/0.10/0.05, M 0.60/0.30/0.10,
  L 0.40/0.30/0.30), not per-sign estimates; distinct probability triples per call: 24, 21, 3. Calls 1-2 give graded values.
  Scored as registered over all 12 lines; the per-call calibration is reported beside it so the fixed scheme is visible.
- Harness `run_x4.py` (scoring rules in its docstring) and the decodes in `out/` (conf, conftop1, 20 shuffled-key controls)
  are committed with this note; the lattice arm uses 41 doubt positions (disagree OR latt), all with an aligned X sign.
