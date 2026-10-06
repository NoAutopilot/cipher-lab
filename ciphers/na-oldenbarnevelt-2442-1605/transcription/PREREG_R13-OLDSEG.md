# PREREG R13-OLDSEG (6 Oct 2026, LANE LANE-RUN13-account-2, account 2) -- per-segment es1600 judge of the B/C1 reading

Committed and pushed before any window is scored. Step (e) of NOTES.md section 16's Verdict. No reading, key, grade or corpus change.

1. **Text.** The committed B/C1 reading: `reading_tokens.tsv` rows with block B then C1, in file order, `value` joined by spaces
   (exactly the `BC1_reading` text of `scripts/es17a_rejudge.py`, N=634 folded letters).
2. **Window cut (fixed now).** Four windows on token boundaries: a token belongs to window k (k=0..3) where
   k = min(3, floor(4 * offset / 634)), offset = folded letters before the token's first letter. About 158 letters each; exact N per
   window is whatever this rule gives and is reported. Window 3 includes the end of the text.
3. **Judge.** `tools/judge_plaintext.py` `judge()` with language `es1600`, control_samples 400, on each window alone (its own N).
   Primary statistic: the window's language score vs that call's real_p05 (in-sample real windows of the same N, 400 samples) and
   null_p99 (letter-shuffled real windows). PASS/FAIL per window as judge() rules it.
4. **Matched controls.**
   (a) Held-out real windows: `holdout()` over the seven es1600 files at each window's N, 200 windows per fold (1400 per N): report
       held-out p05 and the share of held-out real windows scoring at or below each target window (the false-negative position).
   (b) Shuffled-decode windows: the B/C1 cipher letters shuffled (seeds 1-3, token lengths kept, as es17a_rejudge.py) and decoded with
       the committed key; cut by the same token-index windows; scored by the same model. (Solver-key shuffles of section 16 are added
       only if time allows; reported as such.)
   Can-vary check (CLAUDE.md rule 3): before reading results, report the held-out score spread at the window N (sd, p05-p95) -- a
   window score is a continuous mean log-probability over a different letter string, so it can fall anywhere in or outside that
   spread; and the gap real_p05 - null_p99 at that N (if the gap is not positive the judge has no power at ~158 letters and the
   whole job is logged as "untestable at this N", not a finding).
5. **Low-confidence load per window (fixed now).** (i) share of window letters in tokens graded M or I in `reading_tokens.tsv`
   (B/C1: 11 M, 3 I); (ii) OLD-PASS2 per-sign disagreement attributed to the window: each B/C1 token takes its line's rate from
   `transcription/diff_pass2.py ciphertext.tsv transcription/passE_blind_OLDPASS2.tsv` (edits/signs), weighted by the token's cipher
   length (`raw_used`). (The "36 uncertain words" of R7-OLDA are A/C2, not B/C1; they do not enter this test.)
6. **Pre-registered call.** "FAIL concentrates in the low-confidence lines" iff at least one window PASSes and at least one FAILs, and
   every FAILing window has a higher load than every PASSing window on BOTH measures (i) and (ii). "Not concentrated" iff the window
   with the lowest load on both measures FAILs (or all four FAIL). Anything else: "mixed / undecided". With four windows this is a
   coarse description, not a significance test; stated as such.
7. **Descriptive only (not gated):** mean per-letter log10 P (es1600, 4-gram, letters scored in the full-text context) for letters in
   M/I tokens vs S tokens, and for lines above vs at/below the median OLD-PASS2 line rate; the same split on held-out real text is not
   available (no grades), so these are not tests.
Script: `scripts/segment_judge.py` (committed with the result).
