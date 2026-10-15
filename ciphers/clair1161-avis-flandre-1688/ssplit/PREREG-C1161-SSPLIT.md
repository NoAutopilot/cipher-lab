# PREREG C1161-SSPLIT (account-4 worker, LANE DEFAULT-A4-0645-15, 15 Oct 2026, written 08:0x UTC by date -u, before any window is built or seen)

Question: does our label `S` (275 tokens, key u, grade S) merge two shapes -- CL1161-S7's blind *open* S (single top hook, long swept
tail; Lasry's sheet: u/v) and *looped* 8-like S (top or waist closed into a loop; Lasry's sheet: n) -- and, if split, does the looped
part read n at every occurrence where the open part stays u?

Prior work: `tools/prior_work.py clair1161-avis-flandre-1688 --item-spec 'S split' --step-type key --offline` exit 4, LEAD x2, both
own-work claims (CL1161-S7, done in NOTES.md; this job's own claim): proceed. Lasry's key sheet is the source of the n/u hypothesis
(credit, rule 8). Not repeated: CL1161-S7's 12-window exemplar check.

## Step 1: sort every S token (one reader)
- `ssplit/ss_windows.py` cuts one window per S token (all 275, ciphertext.tsv order) from `la/crops` with tools/lookalike_pass.py helpers
  (half-width 2.5 sign widths, scale 1, red tick at the estimate, as CL1161-S7), shuffles them (seed 1688) under opaque ids X001...,
  writes montages to the session scratchpad only (images never go into git) and the id->token key to `ssplit/windows_key.tsv`.
- One reader (this worker, Opus) sorts every window by shape only: O open, L looped, ? unsure / no S at the tick / blot. The reader
  does not open windows_key.tsv, the decode or the reading until the sort is written and pushed (`ssplit/sort.tsv`).
- Known-answer gate (K): the 9 CL1161-S7 windows both blind passes agreed on (looped: c188L_L24/19, c185R_L23/19, c187L_L15/27,
  c188L_L07/18; open: c185R_L18/5, c187R_L22/6, c187R_L25/12, c188L_L27/20, c187R_L22/4) sit among the 275 under fresh ids. PASS iff
  >= 8 of the 9 that the reader does not mark ? are sorted to the agreed class AND at most 1 of the 9 is marked ?. FAIL -> the sort is
  a non-test, step 2 not run.
- Non-trivial gate (T): each of O and L holds >= 20 tokens. Else "no split at this resolution", step 2 not run.

## Step 2: --try per split (derived harness, ciphertext.tsv and key.tsv untouched)
- `ssplit/ciphertext_split.tsv`: S -> So (O), Sl (L), S kept for ?; `ssplit/key_split.tsv`: So, Sl, S all u (current value, grade as S).
  `ssplit/decode_try.json` points decode_key.py at them. `--check` of the main reading must stay exit 0.
- Power control first, on the same harness, fr16 LM, window 8, nulls 100 (tool defaults):
  (P1) known wrong value on a C code must be REJECTED: `p=e` (p is c, C grade, n 112).
  (P2) hidden right value must be ACCEPTED: harness key with `a` (C grade, u, n 98) set to `o`; `--try a=u` must be accepted.
  If P1 is not rejected or P2 is not accepted, the try is a NON-TEST: nothing beyond the log line, no value recorded.
- Hypotheses, each at every occurrence: H1 `Sl=n`; H2 `So=n` (contrast). Reading of results:
  H1 accept and H2 reject -> the split carries the n/u distinction: Lasry's n for looped S supported, grade M (single reader; a
  second blind sort of all S windows is the next step before any transcription or key edit).
  H1 reject -> no support for looped = n at this sort. H1 accept and H2 accept -> the try cannot tell the shapes apart (undecided).
- This job edits neither ciphertext.tsv nor key.tsv in any branch (one reader is not two blind passes; TRANSCRIPTION.md).
Cap USD 4, box 75 min (07:55-09:10 UTC); stop before a unit that would cross 80% of either.
