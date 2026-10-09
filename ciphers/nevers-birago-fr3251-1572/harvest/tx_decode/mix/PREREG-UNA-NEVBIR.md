# PREREG UNA-NEVBIR (9 Oct 2026, written 06:2x UTC by date -u, before any score)

Brief: `.claude/briefs/runs/2026-10-09-account4-orch-unassigned-jobs.md`, section UNA-NEVBIR (account-4 orchestrator).
Source of the step: NOTES.md TX-DECODE, "Next (1)": the three lam-4 re-tests with the 0.8/0.2 atlas mix.

## Lattice (fixed here)
- Two-pass lattice: `tx_decode/<L>_topk.tsv` as committed (f144r, f168, f117).
- Atlas: `atlas/topk/no73.tsv` (f144r), `no85.tsv` (f168r+f168v), `fr3252-no77.tsv` (f117r). Per box, k1..k3 with share
  floor 0.05, `_` (MIXED) dropped, normalised to 1 -- the rule in `tx_decode/atlas_mix.py`.
- Mix per position: 0.8 x two-pass + 0.2 x atlas (weight as in atlas_mix.py, not re-tuned). A position with no mapped
  atlas box keeps its two-pass candidates unchanged.
- Box -> position map, LABEL-BLIND (only geometry, no sign labels): the line-read position's tile in the line-strip
  sorter (`sorter/signs.tsv` for f144r/f168, `../birago-fr3252-1571-72/sorter/signs.tsv` for f117; position from
  `tx_decode/eye/open/sorter/owner_positions.tsv`) is placed in source-image coordinates by its strip origin (the
  build_inputs.py strip rule of each sorter), and takes the atlas box on the same source page with the largest 2-D
  IoU; IoU < 0.2 = no atlas box (two-pass only). The tiles are approximate (one position off is possible); that noise is
  the same for target and control. Coverage (positions mapped) is reported.

## Decode and control (fixed here)
- `tools/key_decode_lattice.py decode`, printed key `harvest/key_1572_sheet.tsv`, lam 4, beam 64, 200 value-shuffled
  keys, seed 1; f144r and f168 `it16dip`, f117 `fr` (as TX-DECODE).
- Control (rule 3): the same mixed lattice position-shuffled, `random.Random(100+s)`, s = 0..4, same decode + 200
  value-shuffled keys (as `tx_decode/shuffled_target.py`). It can differ from the target (it failed on the two-pass lattices).

## Gate, per letter
"rank 1 holds" iff real-order mixed lattice: key rank 1/201 AND every one of the 5 shuffled-target seeds: best rank > 1.
Otherwise "does not hold". Reported beside the two-pass figures (1/3.10, 1/2.77, 1/3.66). No grade moves; changed
positions are S at best, for a verifier.
