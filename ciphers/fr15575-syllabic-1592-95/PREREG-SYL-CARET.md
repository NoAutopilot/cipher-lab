# PREREG SYL-CARET (account-4 worker for LANE DEFAULT-A4-0235-15), 15 Oct 2026 03:1x UTC by date -u, pushed before any score

Question: which value does the no.54 legend mark `^` carry on BnF fr.15575 f.228 -- s (key_no54_legend.tsv row 2, H) or l (row 9, M)?
Instrument (different from SYL54-TRY / SYL-1LC's `decode_key.py --try`, both control-failed): the leaf's own L01-L04 interlinear
gloss (f228/gloss_v2.tsv; gate PASS 0.674 vs control p99 0.233, N8-NV05) as known plaintext at the 8 `^` tokens of L01-L04
(L01 pos 9, 17, 36; L02 19; L03 20, 28, 32, 35; none on L04). No image, no host, 0 subagent calls. No decode of L09+.

Script: f228/caret_tally.py (committed with this file, not yet run). Decode stream per line: syllable codes -> key_syllabary.tsv;
H-graded header letter signs of key_no54.tsv -> their letter; every other token unkeyed. Gloss normalised by the NV05C normaliser
(control_fr3641/score_control.py `norm`, imported). LCS alignment: tools/decode_witness.lcs_align.

Statistic: T(v) = number of the 8 `^` tokens whose inserted letter v (at the `^` token's place in the stream, i.e. after the
preceding character, as the legend's "S apres") is in the line's LCS matching with the gloss. Computed for v = s and v = l;
T for all 26 letters is reported as description only.

Control (primary, null A, 200 seeds 1..200): `^` tokens set unkeyed; v is placed instead at 8 positions drawn without replacement
from the H-read single-letter sign positions of L01-L04 (their own value replaced by v); the same matched count. No H letter sign
has value s or l, so a draw never places a true value. Null B (secondary, reported): 8 extra v tokens inserted at random token
gaps. Calibration (reported): the H single-letter signs at their own values, matched share -- the power ceiling for a true
single-letter value at this alignment.

Gate (PASS for value v): T(v) > null A p95 for v, AND T(v) > T(other candidate), AND no conflicting H: if l wins, the H row 2 (s)
contradicts it and the result is logged as a data conflict (rule 4), not a PASS. A tie between s and l, or neither above its p95,
is FAIL (non-discriminating at this N if the calibration share is itself below the null A p95 rate). A PASS makes `^`=v a C-grade
lead for key_no54_legend.tsv row 2/9 only: the gloss is the period clerk's interlined decipherment (PREREG.md NV05E; AUDIT.md:80,
"16th-c. clerk"), but its L01-L04 reading is a machine-pass reconstruction (two Sonnet passes, gloss_v2), so any lead stays M until
a person or a verifier reads the gloss letter at each `^` place. No key file, decode.json or reading is edited by this job.
