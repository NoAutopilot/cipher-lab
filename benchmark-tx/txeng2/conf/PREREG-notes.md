# TXE2-CONF pass conduct (written 9 Oct 2026 16:5x UTC by date -u, BEFORE any reader call; PREREG-txeng2-2.md X4 binding)

- Readers: 3 blind Opus 5.5 subagents (`model: opus`), one call each: L01-04, L05-08, L09-12 (12 crops each, 2x LANCZOS PNG
  from `harvest/make_2x.py --folio f178v --lines 1-12`, gitignored lines2x/). Task texts frozen in `tasks/`.
- Disclosed deviation: the PREREG says "3 calls, pass-A grouping". Pass A read f.178v in two calls split at L10/L11
  (L01-10, L11-23), and the later Opus dev_tune passes (M2, shift) used two calls L01-06 / L07-12; no 3-call grouping of
  dev_tune is on file. The PREREG's call count (3) is kept as binding (cost, per-call load); lines are split evenly 4/4/4.
- Brief: `harvest/blind_pass_brief_1572.md` unchanged + `conf_block.md` (the top-3-with-probabilities block, one extra column).
  Readers see the brief, the block, the blind sheet and the crops only: never truth, passes, decodes, labels or values.
- Raw reads committed in `raw/` and pushed before any score; the worker opens no truth before that push.
