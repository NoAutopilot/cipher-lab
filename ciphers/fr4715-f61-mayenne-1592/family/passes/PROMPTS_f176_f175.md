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

## H177b stage 2c (runner 6, 28 Sept 2026) -- WRITTEN BEFORE THE CALLS
3 Opus vision calls, inline replies (runner writes the files verbatim): passes A/B of f.176r L34-L40 (stage 2a prompt, rows changed) and one
read of fol. 177v strips 1-4 (`sheets/f177v_strips/`, crops in scratch) -> `passes/f177v_clearA_S01-S04.tsv`, lines numbered V01...
in reading order. build_f176_key.py now appends fol. 177v lines after fol. 177r's (code change pushed with this section; L01-L33 output
unchanged, --check OK before the calls).
Strip prompt: "You are a reader of 16th-century French secretary hand. Use no tool other than your image reader on the files named
here; run no command, write no file. Read four overlapping horizontal strips of one manuscript page, in order: <strip01..04>. Each strip
shows about four lines of writing and overlaps the next by about one line. Transcribe every line whose writing is fully inside a strip,
top to bottom; a line cut at a strip's top or bottom edge is skipped there (it appears whole in the neighbouring strip); a line that
appears whole in two strips is written once. Letter by letter, period spelling, abbreviations not expanded (superscripts as '^'), '?' for
an illegible letter, [brackets] for an uncertain word; ignore marginal notes left of the text block. Reply inline ONLY with a TSV block,
header 'line<TAB>text<TAB>conf', lines numbered V01, V02, ... in reading order. Nothing else."

## H177b stage 2d (runner 6, 28 Sept 2026) -- WRITTEN BEFORE THE CALLS
3 Opus vision calls, inline replies written verbatim: passes A/B of f.176r L41-L47 (stage 2a prompt; L47 is the short last row) and a read
of fol. 177v strips 5-8 (stage 2c strip prompt, strips 05-08, lines numbered V15, V16, ... continuing, and the first line of strip 05
skipped if it repeats V14) -> `passes/f177v_clearA_S05-S08.tsv`. Then build_f176_key.py L01-L47 (the whole of f.176r).

## H177c stage 1 (runner 7 session_012nGionjAX21NRbpi4TP69b, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
f.176v (canvas 328) against the rest of its decipherment, into a SEPARATE file (`key_period_f176v.tsv`, `build_f176v_key.py`), because
VERIFY-F61-V5 is auditing `key_period_f176.tsv`: nothing here edits that file, `build_f176_key.py` or v4. Crops: `sheets/f176v_full/README.md`.
Where f.176v's clear starts: f.176r's 3,095 signs at 0.8 letters per sign are about 2,480 letters, and fol. 177r holds 2,589, so f.176v's
text should begin at or near fol. 177v V01; V01-V27 (2,118 letters) are already read (stages 2c/2d), so no clear read is needed for f.176v
L01-L08. 2 Opus vision calls: blind sign passes A/B of f.176v L01-L08 (H170 calls (1)(2) prompt; rows L01..L08; crops s1..s3 at
`<scratch>/f176v/f176v_Lnn_sK.jpg`; neighbouring crops share about 120 px; inline reply ONLY with the TSV block, same header) ->
`passes/f176v_signs{A|B}_L01-L08.tsv`, written verbatim by the runner.
GATE: build_f176v_key.py L01-L08: match(true: fol. 177v from V01) - max(match(a) f.184r from word 0, match(b) fol. 177r from L01) >= +0.10.
Control (b) was dry-run on f.176r's own L01-L08 passes before any f.176v call (fol. 177r 0.569 vs fol. 177v 0.384): it separates the right
passage from the wrong one in this decipherment. PASS -> the rows go to key_period_f176v.tsv (not merged); FAIL -> logged, and the start
line is not shopped: one pre-named alternative only, --start V01 replaced by fol. 177r's last lines is NOT tried (control (b) is 177r).

## H177d (runner 7, 29 Sept 2026) -- the scan was RUN BEFORE this section was committed (disclosed)
`h177d_scan.py` was written as a pre-registration for after the fol. 178r / fol. 177v strips 9-12 reads, but its first run (meant to test the
positive control) scored f.176v too, on the clear already on disk (fol. 177r L01 to fol. 177v V27, 4,707 letters). So its gate was not
blind. Result (`h177d_scan_result.txt`): control f.176r L01-L08 peaks at letter 0 (0.569; best non-overlapping 0.419; null p99 0.414);
f.176v L01-L08 peaks at letter 3000 (0.545; best non-overlapping 0.354; null p99 0.370). A descriptive fine scan at step 20 over letters
2780-3020 peaks at 2960 (0.571), the head of fol. 177v V06 (2,957). No new reads were needed and none were made.

## H177e (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE RUN
`build_f176v_key.py L01-L08 --start V06` (the H177c builder and gate unchanged, controls (a) f.184r and (b) fol. 177r from L01): GATE margin
>= +0.10. The start comes from H177d's scan, so this confirms the location with the fixed controls. It is not an independent test. PASS: stages
continue from V06 with f.176v L09-... (the clear on disk runs to V27; fol. 177v strips 9-12 and fol. 178r are read when the rows need them).
FAIL: the location stays at H177d's descriptive level.

## H177f stage 1 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
4 Opus vision calls: blind sign passes A/B of f.176v L09-L16 and of L17-L24 (H177c prompt, rows changed, inline replies written verbatim)
-> `passes/f176v_signs{A|B}_L09-L16.tsv`, `..._L17-L24.tsv`. Then `build_f176v_key.py L01-L24 --start V06` (the clear on disk runs to V27,
about 1,750 letters from V06; N = 0.8 x signs will be about 1,250). Gate as H177c (margin >= +0.10 over both fixed controls).

## H177f stage 2 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
3 Opus vision calls, inline replies written verbatim: passes A/B of f.176v L25-L32 (H177c prompt, rows changed) and one read of fol. 177v strips
9-12 (the stage 2c strip prompt, strips 09-12 regenerated from `sheets/f177v_strips/boxes.tsv`, lines numbered V28, V29, ... continuing, the first
line of strip 09 skipped if it repeats V27) -> `passes/f177v_clearA_S09-S12.tsv`. Then `build_f176v_key.py L01-L32 --start V06`, gate as H177c.

## H177f stage 3 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
5 Opus vision calls, inline replies written verbatim: passes A/B of f.176v L33-L39 and of L40-L45 (H177c prompt, rows changed) and one read of
fol. 178r strips 1-7 (`sheets/f178r_strips/`; the stage 2c strip prompt, lines numbered R01, R02, ...) -> `passes/f178r_clearA_S01-S07.tsv`.
Then `build_f176v_key.py L01-L45 --start V06` (the whole of f.176v; clear V06-V40 + R01-), gate as H177c.

## H184 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
Is fol. 178r the decipherment of fol. 179's cipher? Crops: `sheets/f179_full/README.md` (21 rows, s1..s3). 2 Opus vision calls: blind sign passes
A/B of fol. 179 L01-L08 (H177c prompt, file pattern f179_Lnn_sK.jpg) -> `passes/f179_signs{A|B}_L01-L08.tsv`. Then `build_f179_key.py L01-L08`.
GATE (both parts, in the builder's docstring): (1) location scan peak at or after fol. 178r R01 - 300 letters, beating the null p99 and the best
non-overlapping window by >= 0.05; (2) build from R01, margin >= +0.10 over f.184r, fol. 177r and fol. 177v V06- (f.176v's clear).
Dry run before the calls, with f.176v L01-L08 standing in: the scan peaks at letter 3000 (V06), (2) margin -0.164 (control (c) 0.487 catches it): FAIL,
as it should. PASS -> the remaining 13 rows next; FAIL -> logged, fol. 179's decipherment is not shown to be fol. 178r.

## H185 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE RUN
`build_f179_key.py L01-L08 --start R03` (H184's builder with a --start option; H184's own R01 result reproduces unchanged, --check OK): part (2) only,
the build from fol. 178r R03 (H184's scan peak, head of R03 at letter 5,770), controls (a) f.184r, (b) fol. 177r, (c) fol. 177v V06-, margin >= +0.10.
The start comes from H184's scan, so this confirms the location with fixed controls. It is not an independent test. No calls.

## H186 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
A different instrument for fol. 179 (rule 3), after H185 failed on a 0.52 pass consensus. `h186_adj.py tiles` paired pass A and B signs by position
(line, segment, x within 30 px): 489 of 522 pair, 279 agree, 210 split (4TRI/C43 76, HASH4/ZHOOK 35, 4PI/4TRI 28, DBL/PHI 13 ...). 230 tiles (210 splits
+ 20 agreed anchors shown with a decoy code, seed 186, shuffled) on 7 sheets; the key is `h186_tiles.tsv` (committed before the call).
1 Opus vision call, inline reply: "You are a blind shape adjudicator for a 16th-century cipher manuscript. Use no tool but your image reader on the
atlas and sheets named; run no command, write no file. Read the shape atlas <scripts/f61_atlas.tsv>. Each tile on the sheets <h186/sheet_01..07.jpg>
shows one cipher sign centred under the small tick at its top edge, with neighbours cut at the sides; judge only the centred sign. For each tile
you are given two atlas codes (option 1, option 2, listed below); answer A if option 1 fits the centred sign better, B if option 2 does, N if neither
or the centred sign cannot be told. No letters are involved. Reply inline ONLY with a TSV block 'tile<TAB>choice', one row per tile, nothing else."
followed by the list tile / option1 / option2.
CONTROL GATE: >= 17 of 20 anchors pick the agreed code, else CONTROL FAIL and stop (no merge, no build). Then `h186_adj.py merge` ->
`passes/f179_signsC_L01-L08.tsv`, and `build_f179_key.py L01-L08 --start R03 --adj`: GATE margin >= +0.10 over f.184r, fol. 177r, fol. 177v V06-.

## H189 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
A second different instrument for fol. 179 after H186's CONTROL FAIL: `h189_mark.py items` -- 230 items (the 210 fol. 179 splits, same options as
H186, + 20 anchors from f.176v L01-L08 signs both f.176v passes coded alike, decoy from the same confusion family, seed 189), each a 300-px context
strip at 1.2x with a red triangle under the target; 12 sheets of 20; key `h189_items.tsv` committed before the call.
1 Opus vision call, inline reply: the H186 prompt with "the centred sign" replaced by "the sign standing directly above the red triangle (the sign
nearest to it)" and tiles T by items M001-M230 (list file in scratch).
CONTROL GATE: >= 17 of 20 anchors pick the agreed code, else CONTROL FAIL and stop. Then `h189_mark.py merge` -> `passes/f179_signsC_L01-L08.tsv` and
`build_f179_key.py L01-L08 --start R03 --adj`: GATE margin >= +0.10. If this control also fails, fol. 179 is closed for this campaign at
"untested at this transcription", and no fifth approach is briefed without new material.
