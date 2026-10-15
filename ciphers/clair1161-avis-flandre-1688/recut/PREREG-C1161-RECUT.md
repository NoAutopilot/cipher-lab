# PREREG C1161-RECUT (account-4 worker, LANE DEFAULT-A4-0645-15, 15 Oct 2026, written 09:1x UTC by date -u, before any window is re-cut or read)

Brief `.claude/briefs/runs/2026-10-15-acct4-default-0645-jobs.md` (C1161-RECUT, Wave 5). Disk only. Re-cut only the three K windows the
two sorts failed on (X165 c185R_L23/19, X235 c185R_L18/5, X088 c188L_L07/18): localisation only, shape definitions unchanged.

## Re-cut (localisation)
- The worker places the tick on token POS of the line by counting signs on the line strip against the line's own ciphertext.tsv sign
  sequence (labels of the neighbouring signs are used to count, never the S class; CL1161-S7/SSPLIT/SORT2 classes are not consulted for
  placement). Window +-2 sign pitches, band +-90 px, upscaled to >= 300 px, red tick top and bottom, as ss_windows.py.
- If the worker cannot place the tick on a single S by counting (count ambiguous, S not visible), that window is cut at its best
  estimate anyway and the ambiguity is recorded here before any read; it is not dropped.

## Blind re-read (both sorts' readers' method)
- Reader A' (sort A's method: an Opus reader) and reader B' (sort B's method: a Sonnet reader), each a separate subagent call with the
  same shape definitions sort A/B used (O open: single top hook, long swept tail; L looped: 8-like, top or waist closed into a loop;
  ? unsure / no S at the tick / two S equidistant / blot). Each gets one montage: the three re-cut windows shuffled among three decoy
  S windows (other S tokens, re-cut the same way) under fresh opaque ids. No label, value, decode, key, prior class or which ids are K.
- Readers' outputs are pushed (recut/read_A.tsv, recut/read_B.tsv) before recut/recut_key.tsv is opened to score.

## Gate K exactly as registered in ssplit/PREREG-C1161-SSPLIT.md (no threshold change)
K per sort: of the 9 CL1161-S7 known-answer windows, PASS iff >= 8 of those not marked ? are sorted to the agreed class AND at most 1
of the 9 is marked ?. Applied to sort A with A's row for X165/X235/X088 replaced by reader A'; and to sort B with B's rows replaced by
reader B' (K-B, the same rule). The other six K windows keep their original sort A/B classes.
- K(A') PASS -> the registered SSPLIT step 2 --try (P1 p=e, P2 a=u on a=o harness, H1 Sl=n, H2 So=n; fr16 LM, window 8, nulls 100,
  power controls first) runs as a test on sort A's split with the three re-read windows applied; logged to crossword_log.tsv.
- K(A') FAIL (and so a third attempt at this gate) -> logged "untested-by-this-tool" per rule 3's third-attempt clause; the S-split
  image step is [retired] with the instrument named (window montage + blind sort + gate K); reopens only with a different instrument
  (owner's sign sorter) or new material.
- K(B') is reported; if it also passes, sort2/sort2_score.py's K-AB/A/T gates are recomputed with the replaced rows and reported.
Caveat recorded in advance: only the three K windows get the corrected localisation; the other 272 keep SSPLIT's, so a K PASS here
certifies the reader on correctly placed windows, not the placement of the rest.
Cap USD 2, box 45 min (09:11-09:56 UTC); stop before a unit that would cross 80% of either.
