# PREREG CL1161-S7 (15 Oct 2026, 02:3x UTC by date -u; pushed before any window is built or looked at)

Question: do our labels `S` (275 tokens, ours u, Lasry n) and single `7` (not in a 7 7 pair; ours i, Lasry b) each merge two
written shapes? Key of record: George Lasry's sheet (`sources/cyphersolver/2026-10-14-lasry/clair1161/lasry_p073_1.png`,
"BnF cipher research", 10 Oct 2026, published by D. Bourdeau, cyphersolver dde5b0ea, CC BY 4.0). Disk only, 0 host requests.

## Material (script `s7/s7_windows.py`, seed 1161, fixed before any look)
- 12 S tokens and 12 single-7 tokens drawn at random (seed 1161) from ciphertext.tsv, at most 2 per line.
- Plant (power line): 6 `q` + 6 `qb` tokens (two shapes we know are distinct, both agreeing with Lasry: q i, qb a), drawn the same
  way, shuffled together and shown under one neutral description, exactly as S and 7 are shown.
- Windows: `tools/lookalike_pass.py` helpers (`_line_strips`, `_ink_extent`, `_window`) on the native line crops (images/manifest.json),
  half-width 2.5 estimated sign widths, scale 2, red ticks at the estimated x. Window order shuffled (seed 1161); ids W01..W12.
- Description given to the reader (value-free): S set "a tall hooked S-like sign"; 7 set "a 7-like digit stroke"; plant "a q-like
  sign: round bowl with a long descender". No label names, no key values, no Lasry sheet in the blind passes.

## Passes
Two blind Sonnet subagent calls per set (S, 7, plant) = 6 calls, each sees only its own montage(s). Task: find in each window the
sign matching the description nearest the red tick (or NONE), then sort the found signs into as many shape groups as the reader
sees (1, 2 or more), one line per window `Wnn<TAB>group<TAB>note`, plus one line per group describing it. Reconciliation (this
session, one unit): compares the two passes' partitions, then (non-blind, after the partition is fixed) sets the groups beside
Lasry's exemplars of b / i (7) and n / u (S).

## Gates
- Partition agreement between two partitions on the windows both mark non-NONE: best one-to-one group matching, share of windows
  in matched groups (a 1-group partition against a 2-group one scores the larger group's share).
- POWER (per pass): the plant pass reports >= 2 groups and its partition matches the true q/qb split on >= 10 of 12 windows
  (NONE counts as wrong). A pass whose plant fails cannot license "one shape" for S or 7 (non-test for that pass).
- TWO SHAPES (per set): both passes report >= 2 groups each holding >= 3 windows, and the two passes' partitions agree on >= 10 of
  the windows both mark (and on >= 9 windows). -> "two shapes", then --try (below).
- ONE SHAPE: both passes report 1 group (or a second group of <= 1 window) AND both plant passes passed POWER. -> "one shape at this
  sample", the conflict stays a value conflict (rule 4), not a transcription merge.
- Anything else: UNDECIDED (logged as such, no relabel).

## What follows
- Two shapes: a derived ciphertext `s7/ciphertext_split.tsv` (transcription untouched) relabels only the 12 sampled tokens to
  S_g1/S_g2 (or 7_g1/7_g2); `tools/decode_key.py --try` per group with Lasry's value and ours, at every occurrence of that group;
  a value enters nothing (key.tsv unchanged) unless --try's own control passes; otherwise graded M, logged.
- One shape / undecided: `tools/decode_key.py --try 7=b` and `--try S=n` at every occurrence on the main ciphertext, reported as
  information only (rule 4 data conflict; LM nulls were non-discriminating for n77 in CL1161-KA); no key edit unless --try's
  own control passes.
- Crops and montages committed under s7/ (MANT-EYE63 lesson).

## Pricing
6 Sonnet vision calls at ~0.2-0.3 each (small montages) + 1 reconciliation unit; cap 2 (session cost not readable here; stop
before any unit that would cross 80% of the box, 03:02 UTC).
