# PREREG R12D-GRAZB (6 Oct 2026, written 16:07 UTC by date -u, before any strip is cut or looked at)

Job: LANE-RUN12-account-4 R12D-GRAZB (`.claude/briefs/runs/2026-10-06-account4-run12-jobs.md`). Question: is the f.30 `zb`
(key.tsv `zb NULL M`) the same sign as the fr.3040 no.6 barred z (N9-GRAZ class K2; reads R in 25 of 27 aligned places)?

## Material (all from crops on disk; no network)
- T1 f.30 `zb`: 24 of the 39 `ciphertext_f30.tsv` zb tokens, seeded sample (random.Random(20261006)), strips from `images/crops_f30`.
- T2 fr.3040 barred z: (a) the 17 n9graz strips the N9-GRAZ sort put in K2 (z_occ.tsv rows), re-cut by the same method;
  (b) the 11 tokens reconciled `zb` in `n8gra3/recon.tsv` (f.18v/f.19r).
- P plain z: 10 f.30 `z` strips N9-GRAZ sorted K1 (seeded sample) + the 2 fr.3040 K1 strips.
- Decoys (known-distinct signs keyed H in both key tables, present in both letters): `fh` (D) 6 from f.30 + 6 from fr.3040 (n8gra3),
  `n6` (N) 6 from f.30 + 6 from fr.3040 (n8gra2/n8gra3). Seeded samples.
- Strips: one per token, +-3 sign widths, target ticked, proportional position (the n9graz/z_occ.py method), shuffled, numbered,
  no source, line, code or value shown. Answer sheet `r12zb/occ.tsv` kept from the subagent.

## Instrument
One Sonnet blind shape-sort call (strip sheets only): sort the ticked signs into classes (as many as it sees, max 8) by visible
stroke features, describe each class, mark OFF where the tick misses a clear sign. This worker then scores against the answer sheet.
All counts below are over on-target (non-OFF) strips.

## Gate (decided in order)
- G0: OFF <= 30% of all strips, else UNDECIDED.
- G1 decoy control (must pass, else NON-TEST, no conclusion): for fh and for n6 separately, the plurality class holds >= 75% of
  that decoy's strips AND >= 60% of each source's (f.30, fr.3040) strips of that decoy (shows the sort merges one sign across
  the two letters despite different ink and scan); fh's and n6's plurality classes differ from each other and from P's
  plurality class; each decoy's plurality class holds <= 20% of the z-family strips (T1+T2+P).
- SAME: T1's plurality class holds >= 70% of T1, T2's plurality class holds >= 70% of T2, the two are the same class, and it
  differs from P's plurality class.
- DIFFERENT: T1's and T2's plurality classes differ, each holding >= 60% of its set.
- otherwise UNDECIDED.

## Consequences
key.tsv is unchanged under every outcome: a shape match does not give f.30 a value (the letters differ; N9-GRAZ's post-hoc
zb_test ranked R 10th of 23 on f.30). SAME -> next step is a registered zb = R rank test on f.30 with its power control (the
N9-GRAZ f30_test design), noting the post-hoc result already against it. DIFFERENT -> the f.30 zb is a separate sign; its NULL
(L14 closing run, L01 'baille') stands and the fr.3040 barred z gets its own code. NON-TEST/UNDECIDED -> logged as such.
