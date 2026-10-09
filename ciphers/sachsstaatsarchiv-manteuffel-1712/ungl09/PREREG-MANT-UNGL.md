# PREREG-MANT-UNGL (MANT-UNGL, 9 Oct 2026, LANE FAMILY-A2f account 2; written and committed BEFORE any frame is fetched, any pass is read or any score computed)

Leaves: HStA Dresden 10026 Loc. 694/09 files 0103 (p.106-107 spread, four short runs on the left page), 0046 (letter end, one run
+ 'par 11'), 0233 (p.176-177, clerk hand as 0136, isolated codes) -- mant0609/rank_unglossed.tsv rows 24-26 (MANT-0609Y eye
estimates ~20, ~8, ~8 tokens). URLs from images/loc694-08-09/frames.tsv; ONE GET per frame (3), sha256 prefixes recorded and
compared with mant0609/inventory_stride3.tsv. Key: key.tsv at origin/main as of this commit, unchanged by this job.
Design = PREREG-MANT-0136 (f0136_09/), applied per leaf; scripts copied into ungl09/ (f0136_09/ is not edited).

Crops (committed in f<frame>_09/crops/ with manifest.json): `python3 tools/iiif_lines.py --image <frame>.jpg --out <dir> --region
<x,y,w,h> --prefix f<frame> ...` around each code-bearing area, line or strip crops only, region chosen by eye from a downscaled view
before any pass; the commands are pasted in NOTES.

Transcription: two blind Sonnet code passes per leaf (A crop order, B reversed; 0046 and 0233 may share one call per pass), crop paths
only, enlarged 2x, readers told to ignore interlinear letters and to report every number written in the text with its neighbours'
words; worker reconciliation from the image -> f<frame>_09/ciphertext.tsv (decode_key.py format, line/pos/sign/conf; conf low where
the passes disagree and the image does not settle it, or the worker's settle is doubtful). Each code pass also reports whether any
small interlinear/sub-linear letters sit over or under the codes. If EITHER pass, or the worker's look, finds such letters on a leaf,
two blind Sonnet GLOSS passes are run for that leaf and gate (a) of PREREG-MANT-0136 is applied unchanged (ungl09/gloss_gate.py, a
copy of f0136_09/gloss_gate.py: S = matched codes under the DP alignment, key values permuted over codes, 1000 draws, seed 8; PASS iff
S > p99 AND S >= 0.5 x keyed codes in spans; per blind pass; (a) PASS only if both pass). The worker never settles a gloss.

(b) Unglossed letter tokens, per leaf AND pooled (ungl09/judge_gate.py, design of f0136_09/judge_gate.py): tokens = every token of
the leaf's ciphertext.tsv not inside a gloss span, in page order; letter string = key.tsv letter values (first '|' alternative,
1-3 letters a-z; word/name codes and codes absent from key.tsv dropped); statistic = tools/judge_plaintext.py NgramModel score on
corpus fr18 (mean log10 4-gram per letter). Control: letter values permuted among key.tsv's letter-valued codes, 1000 draws, same
token sequence; seeds 103 (0103), 46 (0046), 233 (0233), 9 (pooled). Gate: real > p95 of the permuted scores; p99 reported. Pooled
string = the three leaves' strings joined in frame order 0046, 0103, 0233.
Power control AT EACH N (CLAUDE.md rule 3 last paragraph), run first by the same script: positive-control token streams = 694/09
0085 runs 9+10 (f0085_09/reconciled.tsv) and 694/09 0136 unglossed tokens (f0136_09/ciphertext.tsv minus gloss_A/gloss_B spans),
each read under key.tsv. For a target letter count L: every window of consecutive letter-valued tokens starting at each token of each
stream whose letter string reaches L letters, truncated to exactly L letters; each window scored against 200 permuted keys (seed 7,
same permutation procedure); a window passes if its real score > the 190th of the 200 sorted permuted scores (p95). Power = passing
windows / windows. The leaf's (or the pool's) gate (b) is a TEST only if power >= 0.80; otherwise that leaf/pool is logged
"too-short" (neither PASS nor negative), whatever its own score. If L < 4, too-short without scoring.
Reported, not a gate: tools/judge_plaintext.py on each leaf's reading.txt where a spec judge applies.

Grades (rule 4), per leaf: glossed tokens as PREREG-MANT-0136 (C both passes match, M otherwise); unglossed letter token = S only if
that leaf's own gate (b) is a TEST and PASSes (and, where the leaf is glossed, its gate (a) PASSes); else M. A pooled PASS (with
power) is reported as a statement about the three leaves together and does not by itself grade any token S. Name/word codes (key
value 4+ letters) = M with the key value shown; codes not in key.tsv = U; low-conf transcription tokens are M at best. No key.tsv
change; any candidate value goes to HYPOTHESES.md as a rule-4 slot.
Decode: tools/decode_key.py per leaf folder (decode.json, reading.txt, reading_tokens.tsv, --check); check 5 (tools/print_check.py
on decoded phrases) after decode. Rule 7: every script here has --check.
