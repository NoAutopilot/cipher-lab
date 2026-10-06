# PREREG R11A-AVSK: homophonic_anneal on the native 53 transcription (6 Oct 2026, worker R11A-AVSK, account 1)

Written and pushed before any scored run. Script: `anneal_53n.py` (S1's settings: order 3, w as uu, corpus
tools/data/de16/composed_enhg.txt + plaintext_98.txt, skip DOT,COL, 200000 iters, 6 restarts, uni-weight 1.0).
Input: `ciphertext_53.tsv` as settled by R11A-AVS53 (p1+p2, N = letters after DOT/COL dropped, K = 21 with sign 9 as its own sign).

Questions: (Q1) does the annealer give sign 9 = f (now M by context, 2 occurrences)? (Q2) do G1 and G7 both come out s?

Runs (order: controls first, target only if gate C passes):
1. Control, seeds 1, 2, 3: exact-profile control (`make_profile_control`, the target's own sign-count multiset) from the
   cipher's own 1562 German (align_74.txt words). Statistic: best-key letter share; per-sign recovery.
2. Target, seed 1. 3. Shuffled-order target, seed 1 (same multiset, positions shuffled): a null for per-sign agreement, which
   can differ from the target because sign values under shuffle are driven by frequency only.

Gates:
- **C** (control reads): mean control share over seeds 1-3 >= 0.90. Fail -> stop, "non-test at this N/design", no target run.
- **L** (low-count signs readable): pooled over the 3 control seeds, the share of control signs with count <= 3 recovered
  correctly by the best key >= 0.80. Fail -> Q1 is "untestable at this N" (no grade change for sign 9), Q2 still read.
- **T** (target converges): >= 3 of 6 target restarts within 2.0 of the best score ("converged set").
- **S** (null): in the shuffled run, the share of the 6 restarts giving 9 = f is < 0.5.

Decision rules (no other key change is allowed by this run):
- Q1: if C, L, T, S pass and every restart in the converged set gives 9 = f, sign 9 enters key_53.tsv at grade S (source
  R11A-AVSK) and its two exceptions_53.tsv rows are dropped. If the converged set gives another letter or disagrees, sign 9
  stays M by context and the conflict is logged.
- Q2: if C and T pass and every converged restart gives G1 = G7 = s, recorded as confirmed on the native transcription
  (no key change; already S). Otherwise logged, no change.
- Any other sign whose converged value differs from key_53.tsv (G6 = k by context included): reported, no change.

## Deviation 1 (14:5x UTC, before any scored run)
The exact-profile control could not be built: `make_profile_control` found no 364-letter window of align_74's text whose letter
counts partition exactly by the target's sign counts (5000 tries each, seeds 1-3; no anneal ran). Run 1 uses the tool's standard
matched control instead (`make_control`, K = 21, N = 364, homophones allotted to letters by corpus frequency): S1's own control
design, same N and K as the target, same language and era. Gates and decision rules unchanged. Gate L is read on control signs
with count <= 3 under this design.
