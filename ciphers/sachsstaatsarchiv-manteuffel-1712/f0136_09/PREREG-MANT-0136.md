# PREREG-MANT-0136 (MANT-0136, 9 Oct 2026, LANE FAMILY-A2f account 2; written and committed BEFORE any pass is read or any score computed)

Leaf: HStA Dresden 10026 Loc. 694/09, file 0136 (film label 0137), page "102", P.S. in a clerk hand ("Je me servirai du chiffre que
nous appellons celuy du procès"); frames.tsv URL .../c5158a8f-281c-49a8-985a-b0aa75400e17/fullsize/0136.jpg, 4339x3866, sha256
prefix ff5e898d384dbfbb (same bytes as MANT-0609Y's fetch). Key: key.tsv at origin/main as of this commit, unchanged by this job.
The earlier MANT-0136 identity look (NOTES, 9 Oct 01:08) saw a faint gloss under one ~14-code run agreeing with key.tsv 11-12 of 13
by eye; that look is NOT used as the known answer here -- the known answer comes only from the two blind gloss passes below.

Crops (committed in f0136_09/crops/, manifest.json): `python3 tools/iiif_lines.py --image 0136.jpg --out <dir> --region
600,1000,1550,2450 --prefix f0136 --lines-per-crop 2 --overlap 60 --debug` (17 two-line crops; the code-bearing ones L03 L07 L09 L10
L11 L12 L13 L14 L16 kept) and `--region 2150,1080,1450,340 --prefix f0136R` (right page, L01 kept: "à 39"). Readers get the crops
enlarged 2x, crop paths only.

Transcription: two blind Sonnet code passes (A in crop order, B reversed), readers told to ignore interlinear letters; this worker
reconciles disagreements from the image -> f0136_09/ciphertext.tsv (decode_key.py format, conf high/low). Two blind Sonnet GLOSS
passes (gloss_pass_A.tsv, gloss_pass_B.tsv): each reader reports every small interlinear/sub-linear letter group and the code
numbers it sits under/over, from the crops alone (no key, no other pass). Spans: gloss_A.tsv / gloss_B.tsv, one row per gloss
group, codes = the reader's own named codes mapped to tokens of ciphertext.tsv in order; a group whose reader names no codes, or
whose named codes cannot be found in the reconciled run, is left out and listed. The worker does NOT settle or edit the gloss text.

(a) Known-answer gate, per blind gloss pass separately (V-BRANDT rule): f0136_09/gloss_gate.py (f0063_09/gloss_gate.py, unchanged
alignment): statistic S = codes whose key value (any '|' alternative) matches the next gloss letters under the DP alignment;
control = key.tsv values permuted over codes, 1000 draws, seed 8; PASS iff S > p99 AND S >= 0.5 x keyed codes in spans. (a)
PASSES only if BOTH gloss passes PASS. If a pass yields no placeable span, that pass is a non-test and (a) cannot PASS.

(b) Unglossed tokens (rule 3: a control that CAN differ on its statistic): f0136_09/judge_gate.py, design of PREREG-MANT15
(f0015_09/shuffle_gate_0015.py): tokens = every token of ciphertext.tsv NOT inside a span of gloss_A.tsv or gloss_B.tsv, in page
order; letter string = their key.tsv letter values (value of 1-3 letters a-z, first alternative; word/name codes and codes absent
from key.tsv dropped); statistic = mean log10 4-gram probability per letter, tools/judge_plaintext.py NgramModel on corpus fr18
(French diplomatic/official prose c.1680-1790, Torcy/Villars/Gazette: era-matched to a 1713 letter; its README reports an 18-19%
real-prose false-negative rate, so (b) uses the permuted-key control, not judge PASS alone). Control: letter values permuted among
key.tsv's letter-valued codes, 1000 draws, seed 136, same token sequence. Gate: real > p95 of the permuted scores (brief's gate);
p99 reported beside it. Non-test if the letter string is under 20 letters. Power control (run first, same script): 694/09 0085 runs
9+10 (f0085_09/reconciled.tsv), as PREREG-MANT15; if it is not above its own p95, (b) is logged "non-test". Also reported, not a
gate: `tools/judge_plaintext.py specs/sachsstaatsarchiv-manteuffel-1712.json --file f0136_09/reading.txt` on the whole leaf reading.

Grades (rule 4): a glossed token whose key value matches its gloss in BOTH passes = C; in one pass only = M. Unglossed letter tokens
= S only if (a) and (b) both PASS, else M. Name/word codes (key.tsv values of 4+ letters) = M with the key value shown, I for any
identification beyond the table. Codes not in key.tsv = U (no value proposed unless a gloss in both passes gives it: then listed in
key_add_0136.tsv as a candidate, not merged). low-conf transcription tokens are M at best.
Decode: tools/decode_key.py conventions (f0136_09/decode.json, reading.txt, reading_tokens.tsv, --check); prior-work check 5
(tools/print_check.py on decoded phrases) after decode.
