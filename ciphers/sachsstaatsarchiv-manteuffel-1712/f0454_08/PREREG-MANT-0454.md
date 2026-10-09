# PREREG-MANT-0454 (MANT-0454, 9 Oct 2026, LANE FAMILY-A2f account 2; written and committed BEFORE the frame is fetched, any pass is read or any score computed)

Leaf: HStA Dresden 10026 Loc. 694/08, file 0454 (ff.~360v-361, stamp 361), mant0608/rank_unglossed_08.tsv rank 1 (MANT-INV08 eye estimate
60-75 tokens, no gloss seen at 1500 px). URL from images/loc694-08-09/frames.tsv (.../3a83f921-9a43-485f-874b-34653ed59b68/fullsize/0454.jpg);
ONE GET; sha256 prefix compared with mant0608/inventory_stride4.tsv (036a486ce5ef810f). Key: key.tsv at origin/main as of this commit,
unchanged by this job. Design = PREREG-MANT-0136 (f0136_09/) and PREREG-MANT-UNGL (ungl09/); scripts copied into f0454_08/ (f0136_09/ and
ungl09/ are not edited).

Crops (committed in f0454_08/crops/ with manifest.json): `python3 tools/iiif_lines.py --image 0454.jpg --out f0454_08/crops --region
<x,y,w,h> --prefix f0454 --lines-per-crop 2 --overlap 60 --debug` around the code-bearing area(s), region chosen by eye from a downscaled
view before any pass; commands pasted in NOTES. Line/strip crops only.

Transcription: two blind Sonnet code passes (A crop order, B reversed), crop paths only, enlarged 2x, readers told to ignore interlinear
letters and to report every number with its neighbouring clear words, and whether any small interlinear/sub-linear letters sit over or
under the codes. Worker reconciliation from the image -> f0454_08/ciphertext.tsv (decode_key.py format line/pos/sign/conf; conf low where the
passes disagree and the image does not settle it, or the settle is doubtful).

Gate (a) (only if EITHER code pass or the worker's look finds interlinear letters on any run): two blind Sonnet GLOSS passes; spans
gloss_A.tsv / gloss_B.tsv as PREREG-MANT-0136; f0454_08/gloss_gate.py (copy of f0136_09/gloss_gate.py, unchanged alignment and gate): S =
matched codes under the DP alignment; key values permuted over codes, 1000 draws, seed 8; PASS iff S > p99 AND S >= 0.5 x keyed codes in
spans; per blind pass; (a) PASS only if both pass. The worker never settles a gloss. If no gloss: (a) n/a.

Gate (b) (f0454_08/judge_gate.py, design of ungl09/judge_gate.py): tokens = every token of ciphertext.tsv not inside a gloss span, page order;
letter string = key.tsv letter values (first '|' alternative, 1-3 letters a-z; word/name codes and codes absent from key.tsv dropped);
statistic = tools/judge_plaintext.py NgramModel score, corpus fr18 (mean log10 4-gram per letter). Control: letter values permuted among
key.tsv's letter-valued codes, 1000 draws, seed 454, same token sequence. Gate: real > p95 of the permuted scores; p99 reported.
Power control AT THIS LEAF'S N (rule 3 last paragraph), run first by the same script: positive-control streams 694/09 0085 runs 9+10
(f0085_09/reconciled.tsv) and 694/09 0136 unglossed tokens (f0136_09/ciphertext.tsv minus gloss_A/gloss_B spans), under key.tsv; every
window of consecutive letter-valued tokens reaching L letters (L = this leaf's letter count), truncated to L; 200 permuted keys (seed 7) per
window; window passes if real > the 190th of 200 sorted permuted scores; power = passing / windows. Gate (b) is a TEST only if power >= 0.80;
else "too-short" (neither PASS nor negative). If L < 4, too-short unscored.
Also reported (not gates): each maximal run of letter tokens scored separately (no verdict); the repeated 11-code run (MANT-INV08 eye:
26|60.33.82.60.66.73.10.69.51.11.92) compared token by token between its two witnesses as a transcription consistency figure.

Grades (rule 4): glossed tokens as PREREG-MANT-0136 (C if key value matches gloss in both blind passes; M otherwise). Unglossed letter token
= S only if gate (b) is a TEST and PASSes (and, if the leaf is glossed, gate (a) PASSes); else M. Name/word codes (key value 4+ letters) = M
with the key value shown, I for any identification beyond the table. Codes not in key.tsv = U. low-conf tokens M at best. The S grade is the
mechanical grade of this PREREG for the leaf, not per-token certification; NOTES says which S tokens sit in stretches that read.
No key.tsv change; candidate values go to HYPOTHESES.md as rule-4 slots.
Decode: tools/decode_key.py f0454_08 (decode.json, reading.txt, reading_tokens.tsv, --check); check 5 (tools/print_check.py on decoded
phrases) after decode. Rule 7: every script here has --check.
