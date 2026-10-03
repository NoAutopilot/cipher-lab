# PREREG-FT4p (account-4, 3 Oct 2026, clock read 11:3x UTC, pushed before any blind read)

Target: naf14913-rousseau-venice-1743. Worker FT4p. Question (FT4o's post-hoc cluster): are any of the six f.213 groups
using the twice-occurring codes 63 / 444 / 664 misread or marked, so that a misread rather than a key conflict explains why
the f.206 pin 722 = ti does not fit f.213 (FT4n, FT4o)?

Targets (as transcribed, FT4h passes A/B agreed on all six): 63 (213r L02, 4th group), 444 / 664 / 63 (213r L06, groups
4-6), 664 (213v L01, 3rd), 444 (213v L02, 2nd). Decoys (6, same lines, same transcription status): 347, 834 (L02r), 268,
306 (L06r), 746 (L01v), 329 (L02v). Crops cut from the FT4h native regions on disk (`tools/iiif_lines.py --image`, then
single-group boxes; identities in `align/eye_ft4p_mask.tsv`, shuffled, written only after the read is saved). One blind
Opus 5.5 subagent call, masked crops only: per crop the number, confidence (high/medium/low), and any mark (strike,
overwrite, dot, erasure, unusual spacing, ligature).

Control gate: the decoys must read as transcribed in >= 5 of 6 (edge-clipped digits, as FT4m's 426/468, are a crop fault
and are re-cut once, not counted). Below that the reader is not reliable at this crop size: report, interpret nothing.

Outcomes:
- P1 all six targets read as transcribed (any confidence), no marks: the transcription stands; the 722 = ti / f.213
  conflict is not a misread among these six. Logged per rule 4 as a key conflict (722 C rests on f.206 alone for ti; f.213
  needs something else); no key change; next instrument is different (slip-as-paraphrase alignment, or 722 polyvalence
  tested against f.216v/f.249), not another eye check of these groups.
- P2 a target reads as a different number at high confidence: written into ciphertext_f213.txt as `orig|new` (the file's
  unsettled convention; orig stays first because two earlier passes agreed on it); then one scripted check, offline:
  FT4o's model (pins 22/501/722, group 73 dropped) with `new` substituted, no second edit. Fit -> the conflict is located
  at that group (misread candidate, grade I until a second blind pass agrees); no fit -> P1's reading for the conflict.
  No key.tsv change either way (registered key rule); decode_key --check must still exit 0.
- P3 a target carries a mark (correction, overwrite, cancel): logged as a candidate encipherer slip at that group, grade I;
  same scripted check as P2 with the group dropped; no transcription change.
- Medium/low-confidence differing reads: reported only, no file change.
