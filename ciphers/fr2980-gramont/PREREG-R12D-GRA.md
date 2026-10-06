# PREREG R12D-GRA, addendum to PREREG-N9-GRA4 (6 Oct 2026, written 15:45 UTC by date -u, before any slot crop is cut or read and before any score)

Brief: `.claude/briefs/runs/2026-10-06-account4-run12-jobs.md`, job R12D-GRA (account 4, LANE-RUN12-account-4).
**Same instrument, gate and control as N9-GRA4, no knob changed**: `n12gra/score5.py` is `n9gra4/score4.py` with only the
input path changed (`n12gra/recon_settled.tsv` instead of `n9gra4/recon.tsv`); statistic `agree`, key.tsv as committed
(z = A, zb = NULL, d = V, n6 = N), N1/N2 200 reps p99, planted control at 13% at the target's keyed N, 20 seeds; control gate
mean >= max(N1,N2 p99) + 0.15; target gate agree >= 0.50 and > max(N1,N2 p99). Control run first.

## What changes
Only the reconciled '?' slots of `n9gra4/recon.tsv` whose pass A / pass B labels are the pair {z, zb} (16) or {d, n6} (11),
as tagged by `n9gra4/split_slots.py`'s opcodes. Each is settled from a per-slot crop (window of the half-line crop at the
slot's estimated x, neighbours visible) by ONE blind Sonnet subagent call (budget: cap 3 leaves room for one call, not one per
line), given only the slot crops and reference crops of the four shapes, never the print, the key values or the post-hoc
alignment. Answer per slot: z (plain), zb (barred z), d, n6, or "cannot tell". "cannot tell" or a label outside the slot's own
pair stays '?'. Every other slot of recon.tsv is unchanged.

## Expectation stated before scoring
key.tsv gives z = A and zb = NULL; the post-hoc listing aligned R at 15 of 16 z/zb slots, so settling them cannot raise
`agree` at those slots under the committed key (A != R; NULL is a gap) and may lower it. d/n6: n6 = N matched the print at 9 of
11, d = V does not. The score is reported whatever it is; no key change rests on this run (zb = R would be a separate,
registered open-code test, not this one).
