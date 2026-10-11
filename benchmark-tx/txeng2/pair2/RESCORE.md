# TXE2-PAIR2 X2b -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

Measurement correction: box-to-position map fixed (off by one), not a new gate look. X2b was re-run with only `--map` changed, together
with X2: commands, table and reading in `../pair/RESCORE.md`; outputs in `rescore_boxmapLA/` here.

X2b dev gate, paired vs L_dev_tune: before fixed 3 / broken 0 (p 0.25), **after fixed 3 / broken 1 (p 0.63)**; permuted-label controls
break 17-29 (before 26-31). Verdict unchanged: dev FAIL in the right direction, not reachable at this N; "fixed 3 and broke none"
becomes "fixed 3, broke 1" (the break, f178v L10.14 T60 -> T86, is on a line the map fix did not touch: the training tiles moved, and
with them one fold's T76/T86 threshold, 0.9 -> 0.4).
