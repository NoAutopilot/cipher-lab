# PREREG C1161-SORT2 (account-4 worker, LANE DEFAULT-A4-0645-15, 15 Oct 2026, written 08:3x UTC by date -u, before any window is built or seen)

Question (unchanged from PREREG-C1161-SSPLIT.md): does label `S` (275 tokens, key u) merge an *open* S (Lasry's sheet: u) and a
*looped* S (Lasry's sheet: n); if split, does looped read n at every occurrence where open stays u? Credit: George Lasry's key sheet (rule 8).

This worker has not opened `ssplit/sort.tsv` and will not open it until `sort2/sort_B.tsv` is written and pushed. It has read only
the counts in NOTES.md (A: O 77, L 121, ? 77; K 7/7 decided, 2 ?).

## Step 1: sort B (blind, independent of sort A)
- Windows: `ssplit/ss_windows.py SCRATCH` unchanged (same seed 1688, same ids X001-X275, 14 montages, scratchpad only, never in git).
- Readers: Sonnet subagents, montage images only. The prompt carries the shape definitions (open: single top hook / unclosed top, long
  swept tail; looped: top or waist closed into a loop, 8-like), the reading rule of SSPLIT addendum A (the S on the main line nearest the
  red tick, within about one sign; two S equidistant, no S, or illegible -> ?), and NO label, value, decode, sort A class, or
  windows_key entry. Montages are split across at most 4 calls (3-4 montages each). Output O / L / ? per window id.
- The 14 montages go to the readers in id order; no window is re-read after a first answer except where a reader returns no label
  (then that window only, same prompt).

## Gates (all on fixed definitions written here)
- **K-B** (as registered in SSPLIT, applied to sort B alone): of the 9 CL1161-S7 known-answer windows, >= 8 of those B decides are in
  the agreed class AND at most 1 is marked ?.
- **K-AB** (on the agreed split: a window is O/L in the agreed split only if A and B both decided it and agree; else ?): 0 known-answer
  windows decided against their class, and >= 6 of the 9 decided.
- **A** (inter-reader agreement on windows both A and B decided): raw agreement >= 0.85 AND Cohen's kappa >= 0.60.
- **T** (non-trivial): the agreed split holds >= 20 O and >= 20 L.
Any gate FAIL -> the agreed split is a NON-TEST; step 2 not run as a test; nothing into key.tsv or ciphertext.tsv.

## Step 2 (only if K-B, K-AB, A and T all PASS): registered --try on the agreed split
- Harness `sort2/ciphertext_split.tsv` (S -> So for agreed O, Sl for agreed L, S otherwise) and `sort2/key_split.tsv` (So, Sl, S all u),
  `sort2/decode_try.json`; ciphertext.tsv and key.tsv untouched for the try; main `--check` must stay exit 0.
- Power controls first, same harness, tool defaults (fr16 LM, window 8, nulls 100): P1 `p=e` must be REJECTED; P2 harness with
  `a` set to `o`, `--try a=u` must be ACCEPTED. Either misbehaving -> NON-TEST.
- H1 `Sl=n`, H2 `So=n`, each at every occurrence. H1 accept + H2 reject -> split supported; H1 reject -> no support; both accept -> undecided.
- On support only: the agreed-L tokens may be relabelled `Sl` in ciphertext.tsv with key `Sl=n` at grade M (two blind sorts + --try with
  passed power controls, but Lasry's value is a key-sheet reading in data conflict history, rule 4), decode_key --check regenerated;
  the agreed-O and disagreeing tokens stay `S` (u). Logged in crossword_log.tsv.
Cap USD 5, box 75 min (08:3x-09:48 UTC); stop before a unit that would cross 80% of either.
