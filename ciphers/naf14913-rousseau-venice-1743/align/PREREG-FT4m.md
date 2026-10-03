# PREREG-FT4m: eye check of f.213v L02 group 73 (the second 368), 3 Oct 2026 (account-4)

Written and pushed before any look at the group (by the worker or a subagent). Pair: f.213r-v groups (`ciphertext_f213.txt`)
<-> f.214r slip (`slip_f214r.txt`). FT4l: the registered one-edit gate PASSED, and the only single edit that fits is W at group 73
(f.213v L02 "10 368 426", the second occurrence of 368; the first is f.213r L06 "468 368 46").

## Pre-image deduction (script, `align/eye73_variants.py` -> `eye73_variants.out`, one_edit_seg.solve unchanged, 60 s, all resolved)
Every single-digit substitution of 368 (27), every two-digit drop (36, 38, 68): **E0 False** (no fit with no edit).
Group 73 deleted: **E0 True**. So the fit needs group 73 to carry **zero letters** of the slip. A misread digit (the group is then
a different code carrying >= 1 letter) and a polyvalent use of 368 (>= 1 letter, other letters than the first 368) are both
**excluded by the model** at MAXLEN 12; the one explanation the alignment leaves is an **extra group** (nothing in the slip
corresponds to it). The eye check asks whether the manuscript marks it as such.

## Readings and what each means (decided before the look)
The blind reader sees 5 masked crops (group 73 + 4 decoys, shuffled, neutral names) and reports, per crop: the digits; any
strike-through, cancel line, dots under, overwriting, smaller/interlinear writing, different ink, or unusual spacing.
- **R1, cancel mark on group 73** (struck, dotted out, overwritten, or written as a correction), and no such mark on the decoys:
  the extra group is marked in the MS; transcription error by omission of the mark confirmed. Action: `ciphertext_f213.txt` gets
  group 73 as `[368]` (cancelled) with a comment; the pair then fits with no edit (E0 True, the DEL line above). Key unchanged.
- **R2, 368 read plainly, no mark** (same as decoys): the transcription stands; the extra group is unmarked in the MS:
  an **encipherer's slip** (an extra/null group) at grade I. Transcription unchanged, key unchanged. Polyvalent use and misread
  are not supported (deduction above + read).
- **R3, a different number read on group 73** (any of the 30 variants, or other): misread confirmed at that group, but the
  pair still needs one edit there (every variant E0 False); record the reading as `368|<read>` in `ciphertext_f213.txt` only if
  the reader's read differs and its confidence is stated high; otherwise as R4. Key unchanged.
- **R4, reader cannot decide** (illegible, or reads a mark also on decoys): no change; logged as undecided.
A mark reported on 2 or more decoys as well is not a mark (R2/R4 by the digits). Any change to a transcription file is followed by
`tools/decode_key.py ... --check` (f.206 reading; must exit 0) and the pair's E0 re-run.

Vision: 1 blind Opus 5.5 subagent call on the 5 masked crops. Cap USD 5, box 30 min. The f249 gate is not run in this job.
