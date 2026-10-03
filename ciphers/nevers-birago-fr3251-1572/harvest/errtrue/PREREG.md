# NEVBIR-ERRTRUE pre-registration (3 Oct 2026, 09:3x UTC, account-1 worker for LANE-A1)

Written and pushed before any score below is computed. Brief `.claude/briefs/runs/2026-10-03-acct1-nevbir-errtrue.md`.

## Error levels for the power control

Source row: NOTES.md "TX-DECODE (3 Oct 2026)", known-answer table, row "top-1 of the two passes" on no.87 (853 signs,
truth = clerk clear sheet, `harvest/align87/align_real.tsv`; BENCHMARK-TX.tsv item `birago1572-no87`):
err_true (wrong) **0.0807**, wrong + U **0.1151**. This is the benchmarked true per-sign error of this hand (Birago 1572)
under this reader pipeline (two value-blind Sonnet line reads on 1572 sheet ids). The reconciled passC sequences used for
f.144r/f.168/f.174r add a third adjudicating read, so top-1 is if anything a pessimistic stand-in for them.

Bracket (rule 3 bracketing paragraph):
- E1 = err_true = **0.081**
- E2 = err_true + U = **0.115**
- E3 = 1.5 x err_true = **0.121**

Supplementary (reported, not part of the gate): E4 = err_true + the leaf's own off-sheet (X_NEW) fraction, which the
no.87 benchmark does not carry (no.87: 25/853 = 3% off-sheet; f.144r 14/90 = 0.16; f.168 11/121 = 0.09; pool 32/296 = 0.11):
f.144r 0.24, f.168 0.17, pool 0.19. These are the same as or near the old two-reader figures. If E1-E3 clear the gate but E4
does not, the verdict is written as conditional on the off-sheet signs being valueless noise rather than readable signs.

## Tools, inputs, seeds (unchanged from NEVBIR-144 / NEVBIR-168 / NEVBIR-POOL)

`python3 ciphers/ceppo-nevers-fr3251-1570s/harvest/decode_control.py SEQ --map harvest/sign_id_map_1572_fit.json
--corpus it16dip --shuffles 200 --windows 20 --seed S --err E` (printed 1572 key + T42=m; 200 value-shuffled keys;
20 power windows at the target's own passage lengths). SEQ: `harvest/f144r/passC.tsv`, `harvest/f168/passC.tsv`,
`harvest/pool/pool_all.tsv` (f.144r + f.168 + f.174r). Seed 1 for every power run (as the originals). Real-key rank at
seeds 1-3 for f.144r and f.168, seeds 1-4 for the pool, with inputs unchanged (re-run to confirm the committed figures).
No change to the decoder, the key, the map, the corpus or the sequences; no lattice (that is TX-DECODE's separate instrument).

## Gate and verdict rule

Gate: power >= 16/20 (real key rank 1 of 201 in at least 16 of 20 synthetic windows) at a bracket level.
- Power >= 16/20 at all of E1-E3, real key not rank 1-2 at a majority of seeds -> control-backed negative for the printed
  key (as single reconciled read) on that leaf.
- Power >= 16/20 at all of E1-E3, real key rank 1 at a majority of seeds -> "key fits, licensed at err X"; no reading
  committed; grades S at best.
- Power < 16/20 at any of E1-E3 -> the leaf stays too-short, with the new numbers (the level at which power clears, if any,
  is reported).
- Real key rank 1-2 but not rank 1 at a majority -> neither: reported as rank, no verdict beyond the numbers.
