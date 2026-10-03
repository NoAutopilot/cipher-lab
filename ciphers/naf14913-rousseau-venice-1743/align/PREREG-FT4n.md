# PREREG-FT4n (account-4, 3 Oct 2026, written ~10:33 UTC by the clock, pushed before any score)

Target: naf14913-rousseau-venice-1743. Worker FT4n. Two steps, both disk only, no vision.

## Step A: f.213/f.214r pair scored by the pooled key gate with group 73 dropped
- Instrument: `align/pooled_gate3.py` (FT4e design, itself the three-pair successor of FT4d's pooled_gate.py), amendment
  FT4n: `--pair3 f213 --drop 73`. Pair 3 = ciphertext_f213.txt / slip_f214r.txt, maxlen 12 (longest slip word
  "garantissoit", 12 letters), with 0-based group 73 (the second 368, f.213v L02) removed before anything is scored --
  FT4m's unmarked extra group, grade I. Pairs 1 and 2 (f.206/f.206r, f.216v/f.217r), pins (ten C codes, 379 as
  xinterets), statistic Hp, controls (a) value permutation of pairs 2-3 non-C labels, (b) group-order shuffle of all three,
  (c) wrong-slip decoy reported not gated, n 100, limit 5, seed 7: all unchanged.
- Command: `python3 align/pooled_gate3.py --pair3 f213 --drop 73` (n 100, limit 5, seed 7 defaults), output
  `align/pooled_gate3_f213drop73.out`.
- Gate (unchanged): Hp >= 5 AND Hp > p95(a) AND Hp > p95(b); fewer than 5 shared occurrences = NON-TEST.
- Key rule (unchanged, FT4d/FT4e): only on a gate PASS, a shared code with exactly one joint chunk that is in the real
  best tied set enters key.tsv at C; then `tools/decode_key.py --check` must exit 0. On FAIL/NON-TEST nothing moves.
- Caveat stated now: control (b) scored 0 for every shuffle in FT4d/FT4e because the pins fit only the real order; if so
  again, (b) cannot vary and the gate rests on (a); reported as such.

## Step B: f.249/f.250 one-edit controls under the FT4l solver
- Exactly as amendment FT4l in PREREG-FT4i.md (75bf2422): `python3 align/one_edit_seg.py --pair f249 --ctrl s|g --dec
  --draws i-j` (seed 3, n 40, sublimit 10 s), plus `--real`. Foreground, in blocks with a commit and push after each.
- Order: real, then (s) draws, then (g) draws. Stop before a block that would cross 80 pct of the 45-min box
  (10:32-11:17 UTC; line 11:08). A control not completed is reported as not scored with its draw count, never as a
  partial gate (FT4l rule).
- Gate (unchanged, PREREG-FT4i): PASS iff E_real = 1 AND each control's E=1 share <= 0.05, unresolved counted E = 1.
- Order note: step A is run first (short, ~8 min) so that a box cut lands on step B, which is reported by draw count.
