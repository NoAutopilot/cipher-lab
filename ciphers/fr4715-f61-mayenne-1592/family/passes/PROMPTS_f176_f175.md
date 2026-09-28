# H170 (28 Sept 2026, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- WRITTEN BEFORE THE CALLS

Question: does fr.3984 fol. 175r (canvas 326, clear French, headed "22 de Juillet 1593") render the cipher of fr.3984 f.176r
(canvas 327, Desportes to Clement VIII, same date) -- i.e. is it f.176r's separate-sheet decipherment (Tomokiyo, mayenne.htm)?
Material: native Gallica images (1 request each, requests.log), not committed (4-5 MB each); crops committed:
`sheets/f176r/f176_L01..L04_s1..s4.jpg` (f.176r's first four cipher rows below "Tres saint pere", cut_bands.py, native px,
boxes in f176_bands.json) and `sheets/f175r/f175_L01..L08_s1..s3.jpg` (fol. 175r's first eight clear lines under its title).
Calls, 3 vision in all: (1)(2) two independent blind Opus sign passes of f.176r L01-L04 (identical prompt, output A or B);
(3) one blind Opus read of fol. 175r L01-L08 as written.
Scorer: `h170_gate.py` (pushed with this file). Key: `key_period_v4.tsv` as the f.61 tests use it (--min 2, --frac 0.1,
EBR_A/EBR_B collapsed to EBR), plus: a pass code 4TRI takes the union of v4's 4TRI and 4HOOK sets (the atlas has no 4HOOK
code; the split is a tile-sort class, H69). Statistic: F61-CAL's DP (`scripts/f61crib.align`, local, match +1, gap -1) of the
first N folded letters of a clear text against a pass's sign sequence, N = min(letters read, floor(0.8 x signs)); fraction
= matched / N. Controls: (a) 200 keys with the letter sets permuted across classes (seed 1); (b) two wrong texts of the same
writer and day in the same key: fr.3984 f.184r (the clear of f.188r, `passes/f184r_clear_rec.tsv`) from its first word and from
its word 120, first N letters each.
GATE (both passes separately): fraction(f.175) > max of the 200 permuted keys AND fraction(f.175) - max(wrong texts) >= 0.10.
Both pass -> fol. 175r is f.176r's decipherment at its head (H170 continues: full passes, align_separate-style key rows).
Either fails -> not shown; logged with the numbers, no key rows.

### Calls (1) and (2): blind shape passes of f.176r L01-L04 (identical prompt, output A or B)

You are a blind transcriber of a 16th-century French cipher manuscript. Use no tool other than your image/file reader on the files named here and the Write tool for the one output file; run no command or script. Read first the shape atlas ciphers/fr4715-f61-mayenne-1592/scripts/f61_atlas.tsv (a TSV of code and shape). Then list every CIPHER SIGN, left to right, in four cipher rows L01..L04, each given as four overlapping crops s1..s4 (left to right; neighbouring crops share about 120 px, marked by red ticks at the top edge -- list a sign in an overlap ONCE, in the earlier crop): ciphers/fr4715-f61-mayenne-1592/family/sheets/f176r/f176_L01_s1.jpg (then _s2, _s3, _s4, then L02_s1 ... L04_s4). Parts of the rows above and below may intrude at the top or bottom edge of a crop: list only the row centred in the crop. A few ordinary clear letters or words may stand inside a row (for example at the very start of L01): list such a word as one row with sign = PLAIN and the word in the note. Code every sign with the atlas; use OTHER for a sign matching none, with a shape description in the note; if a sign is between two codes, give the best code and name the alternative in the note as 'alt CODE'. Confidence h/m/l. No letters of the alphabet are to be guessed for any sign: this is a shape transcription only.
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	sign	conf	segment	x_px	note
one row per sign (PLAIN rows included); 'pos' counts from 1 along the whole row; 'segment' is s1..s4; 'x_px' the sign's horizontal centre within its crop. When done, report only the number of signs per row and the total.
OUTPUT PATH: ciphers/fr4715-f61-mayenne-1592/family/passes/f176r_signs{A|B}_h170.tsv

### Call (3): blind read of fol. 175r L01-L08

You are a reader of 16th-century French secretary hand. Use no tool other than your image/file reader on the files named here and the Write tool for the one output file; run no command or script. Read eight lines of one manuscript page, each given as three overlapping crops s1..s3 (left to right; neighbouring crops share about 120 px -- read a word in an overlap once): ciphers/fr4715-f61-mayenne-1592/family/sheets/f175r/f175_L01_s1.jpg (then _s2, _s3, then L02_s1 ... L08_s3). Parts of the lines above and below may intrude at the edges: read only the line centred in the crop. Transcribe each line exactly as written, letter by letter: keep the period spelling, do not modernise, do not expand abbreviations (write a superscript as it stands, e.g. "no^s"), mark an illegible letter '?' and an uncertain word by putting it in [brackets]. Do not guess what the text is about beyond what the letters show.
Write a TSV file with the Write tool to ciphers/fr4715-f61-mayenne-1592/family/passes/f175r_clearA_h170.tsv, header exactly:
line	text	conf
one row per line (L01..L08), conf h/m/l for the line as a whole. When done, report only "8 lines".

## H175 (runner 6, 28 Sept 2026) -- WRITTEN BEFORE THE CALL
One blind Opus read of fol. 177r L01-L08 (canvas 329, native, crops `sheets/f177r/f177_L01..L08_s1..s3.jpg`), prompt = call (3)
above with the paths f175 -> f177 and output `passes/f177r_clearA_h175.tsv`. Scorer `h175_gate.py`: h170_gate.py's statistic, N,
key, 200 permuted keys (seed 1) and gate on the two f.176r passes on disk, the candidate text being fol. 177r's read and the
wrong texts f.184r @0, f.184r @120 and fol. 175r's read (gate: candidate > permuted max AND candidate - max(wrong) >= 0.10, both passes).
Amended before the call (runner 6, 22:40 UTC by commit time): f.176r writes its salutation "Tres saint pere" in clear above the cipher, so the
candidate text drops everything on fol. 177r L01 up to and including the first '/' (the scribe's own separator after the
salutation); if the read has no '/', the words up to and including 'pere' are dropped. Implemented in h175_gate.py before the call.

## H177a (runner 6, 28 Sept 2026) -- WRITTEN BEFORE THE CALLS
Stage 1 of H177: 3 Opus vision calls. (1)(2) blind sign passes A/B of f.176r rows L05-L12 (crops cut by `sheets/f176r_full/README.md`,
in scratch, not committed): the H170 calls (1)(2) prompt with rows L05..L12 and crops s1..s4, outputs
`passes/f176r_signs{A|B}_L05-L12.tsv`. (3) blind read of fol. 177r lines L09-L20 (crops by `sheets/f177r_full/README.md`): the
H170 call (3) prompt with lines L09..L20, output `passes/f177r_clearA_L09-L20.tsv`. No gate at this stage: the rows feed the
align_separate-style key build (H177's step 4), which carries the checks align_separate.py already reports (anchors, letters
per sign, share of assigned plain in the decipherer's underlines) and whose per-class rows are then compared with key v4.

## H177b stage 2a (runner 6, 28 Sept 2026) -- WRITTEN BEFORE THE CALLS
3 Opus vision calls, inline replies (the 22:45 firing's rule: no tool use but reading the named images; the runner writes the files
verbatim): (1)(2) blind sign passes A/B of f.176r L13-L19 -> `passes/f176r_signs{A|B}_L13-L19.tsv`; (3) blind read of fol. 177r
L21-L34 -> `passes/f177r_clearA_L21-L34.tsv`. Prompts = H177a's with the row ranges changed and "Write your transcription ... with the
Write tool" replaced by "Reply inline ONLY with the TSV block (same header), nothing else". No gate at this stage; build_f176_key.py
L01-L19 afterwards (same design, same wrong-text control).

## H177b stage 2b (runner 6, 28 Sept 2026) -- WRITTEN BEFORE THE CALLS
fol. 177r L01-L34 (2,589 letters read) covers about 39 cipher rows, so no clear read is needed for f.176r L20-L33. 4 Opus vision calls,
inline replies (runner writes the files from the hand-back text): passes A/B of f.176r L20-L26 and of L27-L33, prompt = stage 2a's with the
row range changed. Then build_f176_key.py L01-L33 (same design, same wrong-text control). fol. 177v is cut as strips for a later stage
(`sheets/f177v_strips/`).
