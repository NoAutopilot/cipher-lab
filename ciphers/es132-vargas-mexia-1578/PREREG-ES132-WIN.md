# PREREG ES132-WIN -- es132-vargas-mexia-1578: native-resolution token windows on the f.89 side with image-checked decoys (account 2 worker for LANE DEFAULT-A2-0509-15, 15 Oct 2026, written 05:3x UTC by `date -u`, before any read call is made or any score computed)

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md` "### ES132-WIN". Follows ES132-F89 (two-crop look, decoys 8/12) and ES132-BLIND
(blind whole-line crops, decoys 9/12, decoy truths rule-settled, not image-checked). Different instrument: (1) the reader sees a native-resolution
window of about seven tokens around the target, not a whole line downscaled to 2600 px; (2) every decoy's truth is settled by this worker's eye on the
same native window and listed below before any read. Not a third pass of the whole-line instrument.

## Images (scratchpad only, not committed)
f.89 side only, from the committed native `src_*` regions (no network): `tools/iiif_lines.py --image images/src_ark_12148_btv1b10032556x_<f86_3450_1580_2950_3200|
f87_520_880_2720_3980|f87_3580_900_2680_3900|f88_3650_860_2650_1020>.jpg --prefix <f89r|f89v|f90r|f91r> --follow-slope 300 --slope-margin 40` (the ES132-40
commands; 23/26/27/7 lines). `win_f89/build.py` joins a line's two halves at the manifest seam and cuts the window: token centre estimated proportionally
along the inked span, +-3.2 token widths, native pixels (no resize). Each window carries a neutral id only.

## Decoys (image-checked truths, fixed here)
Order: the 25 `flag-removed` rows of `dup_settled.tsv` shuffled with `random.Random(2026)`; the first 16 were viewed as native windows (decoys_sheet1/2);
the worker saw the rule truth while checking (the sheet printed it), so the check is "image agrees with the truth, unambiguously" or reject.
Accepted (12, truth = image-checked token):
| id | pos | truth |
|---|---|---|
| D01 | f89r:L07:14 | 6.@n |
| D02 | f89v:L05:8 | 22.@s |
| D04 | f90r:L25:14 | 22.@n |
| D05 | f90r:L22:15 | 91@s |
| D06 | f90r:L26:20 | 4@l |
| D07 | f89r:L15:14 | 13@s |
| D08 | f90r:L02:11 | 15ρ@s |
| D09 | f89v:L15:17 | 15.@s |
| D11 | f89v:L13:14 | 6.@s |
| D14 | f90r:L18:1 | 15. |
| D15 | f90r:L19:14 | 7ρ@n |
| D16 | f89r:L01:17 | 24ρ |
Rejected before any read: D03 f90r:L02:8 (35+@m; a curved stroke under 35+ may be an underline or the next line's ascender), D10 f89v:L22:16 (10; token
at the binding edge, not clear in the window), D12 f89v:L16:2 ({pam}; a word token, candidates exclude words), D13 f89r:L21:10 (rule truth 38, but the
window shows a cross-like mark above 38 that the notation has no symbol for: the rule truth may be wrong, so not usable as a truth).

## Candidates
The 36 non-word `keep:` rows of `dup_settled.tsv` (words {Sim}, {Xom}, {quam}, {V}/{a} rows excluded); 24 drawn with `random.Random(89)` (cap: 3 calls x 12).
One read each, f.89 side only.

## Reads
36 windows (12 decoys + 24 candidates) shuffled with `random.Random(132132)` into 3 batches of 12 (4 decoys each); one Sonnet vision subagent per batch.
The reader sees the window, two transcribed neighbours before and after ('?' stripped), and the notation of `blind_f89/prompt.md`; never the current
token, the duplicate token, any proposal, or the read's kind. It writes one token in the notation, or `unclear`.

## Gate (computed once, before anything is applied)
Decoy right = exact equality (number, vowel sign, mark); `unclear` = wrong. Gate: >= 10 of 12. Fail -> nothing applied, logged as a non-test of this
instrument at this N.

## Settlement (only if the gate passes)
A candidate settles only where the window read (pass 1) equals the duplicate copy's token `dup_tok` exactly (pass 2: the duplicate's own reconciled
two-pass transcription). The f.89 token then becomes that value, unflagged, grade M. A window read equal to the current f.89 token but not the duplicate,
or equal to neither, changes nothing. Reconcile: this worker looks at every settling window before applying; any it disagrees with is held back.
Applied through `dup_settled.tsv` (decision `win-agreed`), ciphertext files position-checked, `test2.py` regenerating the f.89 readings, every `--check`.
