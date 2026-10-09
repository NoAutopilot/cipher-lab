# PREREG-MANT-0109 (MANT-0109, 9 Oct 2026, LANE FAMILY-A2g account 2; written and pushed in its own commit BEFORE any pass is read or any score computed)

Leaf: HStA Dresden 10026 Loc. 694/08, file 0109 (f.80, "beschaedigt"), mant0608/rank_unglossed_08.tsv rank 1 (MANT-INV08B eye estimate
70-90 tokens, no gloss seen at 1600 px). URL from mant0608/fetch_b.tsv (.../3a83f921-9a43-485f-874b-34653ed59b68/fullsize/0109.jpg); ONE GET;
sha256 prefix compared with mant0608/inv08b.tsv (8a1c710cee1d3f56). Key: key.tsv at origin/main as of this commit, unchanged by this job.
Design = PREREG-MANT-0454 (f0454_08/), scripts copied into f0109_08/ (f0454_08/, f0136_09/, ungl09/ not edited). Differences below are the
only changes, and each is fixed here before any number exists.

Crops (committed in f0109_08/crops/ with manifest.json): `python3 tools/iiif_lines.py --image 0109.jpg --out f0109_08/crops --region <x,y,w,h>
--prefix f0109[L|R] --lines-per-crop 2 --overlap 60 --debug` per page (two pages), region chosen by eye from a downscaled view before any pass;
commands pasted in NOTES. Line/strip crops only; one page per subagent call.

Transcription: two blind Sonnet code passes per page (A crop order, B reversed), crop paths only, enlarged 2x, readers told to ignore
interlinear letters, to report every number with its neighbouring clear words, and whether any small interlinear/sub-linear letters sit over or
under the codes. Worker reconciliation from the image (one unit) -> f0109_08/ciphertext.tsv (line/pos/sign/conf; one run id per code group in
page order; conf low where the passes disagree and the image does not settle it).

Gate (a): exactly as PREREG-MANT-0454 (only if a pass or the worker's look finds interlinear letters on a run; two blind gloss passes; S >
p99 of 1000 key-permuted draws, seed 8, and S >= 0.5 x keyed codes; both passes). The worker never settles a gloss. If no gloss: (a) n/a.

Repeated-pair handling (fixed now, from the MANT-INV08B eye note: 55.44 ~14x, 7.60 ~9x): a maximal run of exactly 2 or 3 codes whose code
sequence occurs as a whole run 3 or more times on the leaf is a NAME-ABBREVIATION group: excluded from gate (b)'s letter stream (like a name
code), graded M with its key letters shown (e.g. 55.44 = 'bl'/'al'), identification I at best. The same sequence inside a longer run stays in
the stream. Reported: each such group's count, its key letters, and its clear-word contexts.

Gate (b) (f0109_08/judge_gate.py, design of f0454_08/judge_gate.py): tokens = every token of ciphertext.tsv not in a gloss span and not in a
name-abbreviation group, page order; letter string = key.tsv letter values (first '|' alternative, 1-3 letters a-z; word/name codes and codes
absent from key.tsv dropped); statistic = tools/judge_plaintext.py NgramModel score, corpus fr18. Control: letter values permuted among
key.tsv's letter-valued codes, same token sequence. Power from the brief's positive-control streams only (694/09 0085 runs 9+10, 694/09 0136
unglossed tokens, under key.tsv; windows truncated to the scored length; 200 permuted keys seed 7 per window; pass if real > 190th of 200).
Block rule (new, because those streams hold at most 62 letters: 11 windows reach 52, 3 reach 60, 0 reach 70): let L = the leaf's letter count.
If L <= 52 the leaf is scored whole exactly as MANT-0454 (1000 permuted, seed 109; power at L). If L > 52 the letter string is cut into
consecutive non-overlapping blocks of B = 52 letters from the start (block k = letters 52(k-1)+1 .. 52k); the tail remainder (< 52 letters) is
reported only, not gated. Each block: 1000 permuted keys (seed 109+k) on the tokens covering that block, score truncated to the block; power
at B = 52 from the same streams. Gate (b) is a TEST only if power >= 0.80 (else "too-short": neither PASS nor negative; stop there and say
so). A block PASSes if real > p95 of its permuted scores (p99 reported). Leaf-level (b) = PASS if every block PASSes; MIXED if some do; FAIL
if none. If L < 4, too-short unscored.
Also reported (not gates): each maximal run's own score; the whole-leaf letter string score vs 1000 permuted (seed 109) with p95/p99 (no
power behind it if L > 62).

Grades (rule 4): glossed tokens as PREREG-MANT-0136. An unglossed letter token = S only if gate (b) is a TEST and the block containing its
letters PASSes (and gate (a) PASSes if the leaf is glossed); tokens whose letters sit in a failing block or the ungated tail = M. A token
straddling two blocks takes the worse block. Name/word codes (key value 4+ letters) = M with the key value, I for any identification beyond
the table. Name-abbreviation groups = M. Codes not in key.tsv = U. low-conf tokens M at best. The S grade is this PREREG's mechanical grade,
not per-token certification; NOTES says which S tokens sit in stretches that read.
No key.tsv change; candidate values go to HYPOTHESES.md as rule-4 slots.
Decode: tools/decode_key.py f0109_08 (decode.json, reading.txt, reading_tokens.tsv, --check). Check 5: tools/print_check.py on decoded and
clear phrases (Google Books answers today). Rule 7: every script here has --check.
