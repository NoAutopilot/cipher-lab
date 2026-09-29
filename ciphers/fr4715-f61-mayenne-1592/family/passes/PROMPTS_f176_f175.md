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

## H193 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
`h193_attr.py tiles`: 60 marked strips (10 f.176v CP anchors = agreed 4TRI paired with c/p, 10 f.176v AN anchors = 4TRI|C43 split paired with a/n, 40
f.176r agreed-4TRI targets), seed 193, key `h193_items.tsv`. The runner looked only at the 20 anchors by group (`<scratch>/h193/anchors_by_group.jpg`):
CP signs are a 4 whose stem runs down below the line and ends in a closed b-like bowl; AN signs are a 4 with a small r-like tail at its right on the
line, no bowl below. Attribute fixed now (`h193_yes_group.txt` = CP):
1 Opus vision call, inline reply: "You are a blind shape reader. Use no tool but your image reader on the sheets named; run no command, write no file.
Each item on <h193/sheet_01..03.jpg> (Q01-Q60, 20 per sheet) is a strip of a cipher row with a red triangle under one sign; look only at the sign
directly above the triangle. Question: does that sign's vertical stem run down below the writing line and end in a closed loop or bowl (like the
bottom of a 'b')? Answer yes or no; if the sign above the triangle cannot be told, answer n. No letters are involved. Reply inline ONLY with a TSV
block 'item<TAB>answer', one row per item, nothing else."
GATE: >= 17 of 20 anchors answer in their group's direction (CP yes, AN no), else CONTROL FAIL and stop. Then f.176r's 40 targets are split by the
answer and counted {c,p} vs {a,n} under fol. 177r (Fisher exact test), descriptive of whether the attribute carries the letter split on a second leaf.

## H194 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H193's bowl question on f.61's 4-family (scorer `h194_bowl_f61.py`, committed with this section). Disclosure: the runner looked at one target sheet
(images/f61sheet_L05.jpg) before writing this, to check the sheets are legible; the question is H193's, unchanged.
1 Opus vision call, inline reply: "You are a blind shape reader. Use no tool but your image reader on the images named; run no command, write no file.
Part 1: the items on <h193/sheet_01..03.jpg> (Q01-Q60) as before: for the sign directly above the red triangle, does its vertical stem run down below
the writing line and end in a closed loop or bowl (like the bottom of a 'b')? yes / no / n. Part 2: on each of the five line sheets
<images/f61sheet_L01, L03, L05, L08, L11.jpg> (a cipher line cut into stacked segments, read left to right, top segment first; clear words, if any,
are not signs), list every sign shaped like a figure 4 (a 4 with anything attached), in order, numbered 1, 2, 3..., and answer the same question
for each. No letters are involved. Reply inline ONLY with a TSV block 'id<TAB>answer': rows Q01..Q60, then rows 'L01:1', 'L01:2', ... for part 2."
GATE: repeat control >= 17 of the 20 f.176v anchors, else CONTROL FAIL and stop. Result: matched f.61 positions, bowl vs Tomokiyo's c/p vs a/n
(Fisher), lines with a count mismatch left out. Descriptive, for the verifier.

## H195 (runner 7, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
`h195_hash_attr.py tiles`: 60 marked strips (10 f.176v anchors of agreed HASH4 paired with i, 10 paired with d/q, 40 f.176r agreed-HASH4 targets), seed
195, key `h195_items.tsv`. The runner looked only at the 20 anchors by group: d/q signs are a figure-4 head standing on crossed double stems ("4 over #");
i signs are the bare crossed double stems with no 4-head (H162's forms). Attribute fixed (`h195_yes_group.txt` = DQ). 1 Opus vision call, inline reply:
"You are a blind shape reader. Use no tool but your image reader on the sheets named; run no command, write no file. Each item on <h195/sheet_01..03.jpg>
(H01-H60) is a strip of a cipher row with a red triangle under one sign; look only at the sign directly above the triangle. Question: is there a
figure-4 head (an angular 4) standing on top of crossed vertical stems in that sign? Answer yes or no; if it cannot be told, answer n. No letters are
involved. Reply inline ONLY with a TSV block 'item<TAB>answer', one row per item, nothing else." GATE anchors >= 17/20; then f.176r targets i vs d/q.

## H199 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H193's bowl question on fr.3983 f.108v's 4-family (f.61's hand). Script `h199_bowl_108v.py` and key `h199_items.tsv` (74 targets: every H59 draft
column with a 4-family code in the reconciled draft, pass A or pass B; reconciled C43 41, 4STEM 25, 4TRI 6, OTHER 1, ZHOOK 1) committed with this
section. Targets are cut from the native (images/3983_f108v.jpg) because the 3x crops clip the bowl; the marker for these is ABOVE the strip,
pointing down, because under the strip sits the leaf's interlinear gloss. Disclosure: the runner looked at target sheets 01 and 04 for legibility
and marker placement (a few markers sit about half a sign off, e.g. R72, R74); the question is H193's, unchanged. The H193 strips were regenerated
from the natives (canvases 327, 328; hashes as logged) and h193_items.tsv reproduced byte-identical.
1 Opus vision call, inline reply: "You are a blind shape reader. Use no tool but your image reader on the images named; run no command, write no file.
Part 1: each item on <h193/sheet_01..03.jpg> (Q01-Q60, 20 per sheet) is a strip of a cipher row with a red triangle UNDER one sign; look only at the
sign directly above that triangle. Part 2: each item on <h199/sheet_01..04.jpg> (R01-R74) is a strip of a cipher row with a red triangle ABOVE the
strip, pointing down at one sign of the cipher row (the upper row of writing; any smaller writing lower in the strip is not the sign); look only at
the sign the triangle points to. Question for every item: does that sign's vertical stem run down below the writing line and end in a closed loop
or bowl (like the bottom of a 'b')? Answer yes or no; if the marked sign cannot be told, answer n. No letters are involved. Reply inline ONLY with a
TSV block 'id<TAB>answer', rows Q01..Q60 then R01..R74, nothing else."
GATE: repeat control >= 17 of the 20 f.176v anchors in their group's direction (CP yes, AN no), else CONTROL FAIL and targets not scored. Read-out:
bowl answers by reconciled / A / B code; "the readers' split follows the bowl on f.108v" iff reconciled 4TRI yes share >= 0.8 and C43 no share
>= 0.8 (n left out). Descriptive, for the verifier; no key change.

## H202 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H193's bowl question at fr.3983 f.108r's 4-family positions carrying a period-gloss letter (Tomokiyo's overlay reprint; 20 targets: C43 a 4 / n 4,
4STEM a 3, 4TRI c 2 / p 2, 4PI p 1 / d 4). Script `h202_bowl_108r.py`, key `h202_items.tsv`, committed with this section. Strips cut from
images/f108sheetB_L02/L03.jpg bands (descenders kept); marker UNDER the sign as in H193. Disclosure: the runner looked at images/f108sheetB_L02.jpg
for band geometry and at the target sheet for legibility (single-sign views; one or two markers sit off a 4-sign, e.g. S09).
1 Opus vision call, inline reply: "You are a blind shape reader. Use no tool but your image reader on the images named; run no command, write no file.
Each item on <h193/sheet_01..03.jpg> (Q01-Q60) and <h202/sheet_01.jpg> (S01-S20) is a strip of a cipher row with a red triangle UNDER one sign;
look only at the sign directly above that triangle. Question: does that sign's vertical stem run down below the writing line and end in a closed
loop or bowl (like the bottom of a 'b')? Answer yes or no; if the sign above the triangle cannot be told, answer n. No letters are involved. Reply
inline ONLY with a TSV block 'id<TAB>answer', rows Q01..Q60 then S01..S20, nothing else."
GATE: repeat control >= 17/20, else CONTROL FAIL. Read-out as in the script's docstring.

## H207 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H193's bowl question on fr.3982 f.101r's 4TRI and 4STEM (supports MIXED, H203) against the leaf's period gloss letters (passes/f101r_align_v4.tsv, grade C).
Script `h207_bowl_101r.py`, key `h207_items.tsv` (39 targets: 4TRI c/p 10 a/n 10, 4STEM c/p 9 a/n 10, seed 207), committed with this section. Strips
cut from a fresh Gallica native of f210 (bytes differ from the 28 Sept fetch, 5,562,778 vs 5,562,607; pixel correlation with the committed band
crop f101r_L01_s1 0.9996, so the same image re-encoded). Disclosure: the runner looked at three versions of target sheet 01 while fixing the strip
geometry (rows drift; the first two cuts put the marker under the next row's gloss or clipped the row); the question is H193's, unchanged. In U13
and U15 two cipher rows cross the column.
1 Opus vision call, inline reply: "You are a blind shape reader. Use no tool but your image reader on the images named; run no command, write no file.
Part 1: each item on <h193/sheet_01..03.jpg> (Q01-Q60) is a strip of a cipher row with a red triangle UNDER one sign; look only at the sign directly
above that triangle. Part 2: each item on <h207/sheet_01..02.jpg> (U01-U39) is a strip of a manuscript page with ordinary handwritten words and a
row of cipher signs; one column is marked by a red triangle above the strip (pointing down) and one below it (pointing up); look only at the cipher
sign (not the ordinary words) in that column; if two rows of cipher signs cross the column, or the sign cannot be told, answer n. Question for every
item: does that sign's vertical stem run down below the writing line and end in a closed loop or bowl (like the bottom of a 'b')? Answer yes or no,
or n as above. No letters are involved. Reply inline ONLY with a TSV block 'id<TAB>answer', rows Q01..Q60 then U01..U39, nothing else."
GATE: repeat control >= 17/20, else CONTROL FAIL. Read-out as in the script's docstring.

## H212 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
Blind shape sort (the H89 design) of the 24 HASH4 signs of fr.3983 f.108v (14) and f.108r L06 (10), leaf hidden. Script `h212_hash_sort.py`, key
`h212_items.tsv` committed with this section. Disclosure: the runner looked at the tile sheet for legibility (tiles 2 and 11 faint or near an edge)
and saw that the tiles differ in form; the grouping is the reader's, and the score is fixed in the script.
1 Opus vision call, inline reply: "You are a palaeography assistant. Use no tool but your image reader on the one image named; run no command, write no
file: <h212/sheet_01.jpg>. The sheet holds 24 numbered tiles (tile 1 .. tile 24), each an enlarged crop from a line of invented cipher signs in a
16th-century French manuscript. In each tile TWO SHORT RED TICKS, one at the top edge and one at the bottom edge, mark the horizontal position of ONE
target sign; neighbouring signs and the ordinary handwritten words must be ignored. The target signs are all built on a hash or lattice (crossing
strokes). For each tile describe the target sign only, with fixed attributes: (a) what sits on or above the hash (nothing, a figure-4 head, loops,
other); (b) the loops, if any: how many and where; (c) the verticals: how many, and whether one runs well below the line; (d) anything else
distinctive. If the ticks mark no hash-like sign, put group 'none' and say why. Then sort all target signs into 2 to 4 groups by shape using these
attributes, and state in one sentence the criterion that separates the groups. Do not guess letters; do not decode. Reply inline ONLY with a TSV
block with the header tile<TAB>group<TAB>head<TAB>loops<TAB>verticals<TAB>note, one row per tile (tile 1 .. tile 24, written 'tile N'), then the
one-sentence criterion, then one line 'signs described: N'. Nothing else."
Read-out fixed in the script's docstring (group G = the group holding most f.108v tiles; Fisher G x leaf).

## H214 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H212's looped-hash attribute against period letters, on H195's unchanged 60 strips (<scratch>/h195/sheet_01..03, regenerated; h195_items.tsv
byte-identical). Scorer `h214_loops.py` committed with this section; direction fixed: yes = the i group. The runner has not looked at these strips.
1 Opus vision call, inline reply: "You are a blind shape reader. Use no tool but your image reader on the images named; run no command, write no file.
Each item on <h195/sheet_01..03.jpg> (H01-H60, 20 per sheet) is a strip of a cipher row with a red triangle under one sign; look only at the sign
directly above the triangle. Question: does that sign carry two small closed loops sitting on a hash (crossing strokes), rather than a figure-4
stroke rising above it or nothing? Answer yes or no; if the sign above the triangle is not hash-like or cannot be told, answer n. No letters are
involved. Reply inline ONLY with a TSV block 'item<TAB>answer', one row per item, nothing else."
GATE >= 17/20 anchors in the pre-stated direction, else CONTROL FAIL and stop.

## H216 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H193's bowl question on f.108r L04-L06's 15 4-family signs (H108 draft codes 4STEM 6, C43 4, 4PI 4, 4TRI 1). Script `h216_bowl_108r.py`, key
`h216_items.tsv` committed with this section. Disclosure: the runner looked at the target sheet twice (legibility; item labels were clipped and the
strip shortened by 10 px). The hash half of the row is H212's (these L06 HASH4 positions: A 1, B 9).
1 Opus vision call, inline reply: H199's prompt with part 2 changed to "<h216/sheet_01.jpg> (P01-P15)", i.e.: "You are a blind shape reader. Use no
tool but your image reader on the images named; run no command, write no file. Part 1: each item on <h193/sheet_01..03.jpg> (Q01-Q60, 20 per sheet) is
a strip of a cipher row with a red triangle UNDER one sign; look only at the sign directly above that triangle. Part 2: each item on
<h216/sheet_01.jpg> (P01-P15) is a strip of a cipher row with a red triangle ABOVE the strip, pointing down at one sign of the cipher row (any smaller
writing above or below the row is not the sign); look only at the sign the triangle points to. Question for every item: does that sign's vertical stem
run down below the writing line and end in a closed loop or bowl (like the bottom of a 'b')? Answer yes or no; if the marked sign cannot be told,
answer n. No letters are involved. Reply inline ONLY with a TSV block 'id<TAB>answer', rows Q01..Q60 then P01..P15, nothing else."
GATE: repeat control >= 17/20, else CONTROL FAIL.

## H359 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H193's bowl question on de Diou's fr.3982 f.124r 4TRI (50) and C43 (20) tokens, H199's design and prompt verbatim; script `h359_bowl_124r.py`, key
`h359_items.tsv` committed with this section. Part 1 = H193's 60 strips regenerated from natives f327/f328 (sha1 a2b0d98e..., 4a13be67..., as H230;
h193_items.tsv byte-identical). Part 2 cut from the native f.124r (sha1 8b7e91c7...). Disclosure: the runner looked at the top of target sheets 01 and
02 for marker placement only; seeing the gloss sit below f.124r's cipher rows, it moved the marker above the strip (H199's layout) before the call.
1 Opus vision call, inline reply, the text exactly as H199's with part 2's sheets and ids: "You are a blind shape reader. Use no tool but your image
reader on the images named; run no command, write no file. Part 1: each item on <h193/sheet_01..03.jpg> (Q01-Q60, 20 per sheet) is a strip of a
cipher row with a red triangle UNDER one sign; look only at the sign directly above that triangle. Part 2: each item on <h359/sheet_01..04.jpg>
(R01-R70) is a strip of a cipher row with a red triangle ABOVE the strip, pointing down at one sign of the cipher row (the upper row of writing; any
smaller writing lower in the strip is not the sign); look only at the sign the triangle points to. Question for every item: does that sign's vertical
stem run down below the writing line and end in a closed loop or bowl (like the bottom of a 'b')? Answer yes or no; if the marked sign cannot be told,
answer n. No letters are involved. Reply inline ONLY with a TSV block 'id<TAB>answer', rows Q01..Q60 then R01..R70, nothing else."
GATE and read-out as in the script's docstring.

## H360 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
H359's prompt verbatim, four calls, one per chunk c1..c4 (part 2 = SCRATCH/h360_cK/sheet_01..03.jpg, R01-R55); script `h360_124r_4tri_split.py`, key
`h360_items.tsv` committed with this section. The runner did not look at the H360 sheets.

## H362 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h362/sheet_01..04.jpg (R01-R70), fr.3982 f.101r targets; script `h362_bowl_101r.py`, key `h362_items.tsv`.
The runner did not look at the H362 sheets.

## H365 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
H359's prompt verbatim, four calls (part 2 = SCRATCH/h365_cK/sheet_01..03.jpg; R01-R48, c4 R01-R47), f.101r; script `h365_101r_4tri_split.py`, key `h365_items.tsv`.
The runner did not look at the H365 sheets.

## H367 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h367/sheet_01.jpg (R01-R18), f.61's own 18 4-family signs (6 4TRI, 9 C43, 1 4STEM, 2 4PI) cut from the
native f.61 region image; script `h367_bowl_f61.py`, key `h367_items.tsv`. H193's 60 strips regenerated from natives f327/f328 (sha1 a2b0d98e...,
4a13be67..., as H230/H359; h193_items.tsv byte-identical). Disclosure: the runner looked at the whole H367 sheet for marker placement (twice): the
markers sat on the intended signs, but at H359's -60/+55 window every stem was clipped just below the line, so the window was moved to -45/+92 before
the call (the runner has therefore seen the target shapes; the reader has not). 1 Opus vision call.

## H368 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
H359's prompt verbatim, two calls (part 2 = SCRATCH/h368_c1/sheet_01..03.jpg R01-R49, SCRATCH/h368_c2/sheet_01..03.jpg R01-R49), fr.3983 f.106r rows
1-18 (every pass-A 4TRI and 4STEM, 20 C43), cut at H231's geometry; script `h368_bowl_106r.py`, key `h368_items.tsv`. H193's strips as in H367
(same regeneration, byte-identical). The runner did not look at the H368 sheets.

## H370 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h370/sheet_01..04.jpg (R01-R70), fr.3982 f.97r recut rows L17-L43, 50 agreed 4TRI + 20 C43 (pools 127 / 39),
native canvas 202 (sha1 87d4236c as MANIFEST.tsv); script `h370_bowl_97r.py`, key `h370_items.tsv`; H193's strips as in H367. The runner did not look
at the H370 sheets.

## H371 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALLS
H359's prompt verbatim, two calls (part 2 = SCRATCH/h371_c1/sheet_01..02.jpg R01-R39, SCRATCH/h371_c2/sheet_01..02.jpg R01-R38), the other 77 agreed 4TRI
of f.97r L17-L43; script `h371_97r_4tri_split.py`, key `h371_items.tsv`. The runner did not look at the H371 sheets.

## H377 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h377/sheet_01..04.jpg (R01-R70): 64 remaining pass-A 4TRI of f.97r L17-L43 and 6 known f.61 strips in
part-2 format (H376's fix; gate 2 >= 5/6); script `h377_97r_4tri_more.py`, key `h377_items.tsv`. The runner did not look at the H377 sheets.

## H385 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h385/sheet_01..03.jpg: f.106r's remaining pass-A C43 (H368 geometry) and H377's 6 known f.61 strips
(gate 2); script `h385_106r_c43_bowl.py`, key `h385_items.tsv`. The runner did not look at the H385 sheets.

## H387 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h387/sheet_01..03.jpg: f.101r's agreed 4STEM (H365 geometry) and H377's 6 known f.61 strips (gate 2);
script `h387_101r_4stem_bowl.py`, key `h387_items.tsv`; native canvas 210 refetched once. The runner did not look at the H387 sheets.

## H390 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h390/sheet_01..03.jpg (R01-R56): 50 f.124r 4TRI already answered by H359/H360 (25 yes, 25 no), re-cut at
H359's geometry from native f256 (sha1 8b7e91c7, as H359), and H377's 6 known f.61 strips; script `h390_bowl_kappa_gated.py`, key `h390_items.tsv`.
The runner did not look at the H390 sheets.

## H392 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h392/sheet_01..04.jpg (R01-R72): fr.3984 f.188r's 66 agreed 4TRI (no agreed C43 exists on the leaf) and
H377's 6 known f.61 strips; native f351 (sha1 1c584b0f as MANIFEST.tsv); script `h392_bowl_188r.py`, key `h392_items.tsv`. The runner did not look
at the H392 sheets.

## H396 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h396/sheet_01.jpg (R01-R20): f.61 L05/14 at three windows and the other 17 f.61 4-family tiles (H367
geometry); script `h396_l05_14_tiebreak.py`, key `h396_items.tsv`. The runner saw the f.61 target shapes in H367's placement check (disclosed there);
it did not look at the H396 sheet.

## H398 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h398/sheet_01..08.jpg (R01-R86): VERIFY-F61-V11's own 80 f.101r target tokens (c1, c2, c4, c5; first
occurrences) in V11's own tile format (v11_bowl.tile geometry, 12 per sheet), marker recoloured red (V11 drew it blue; the only change to V11's tiles,
so H359's wording is true of them), plus H377's 6 known f.61 strips in the same tile format at H367's window. Script `h398_bowl_design.py`, key
`h398_items.tsv`. Natives fetched once each this session: f327 sha1 115f9923 (differs from a2b0d98e on record: a server-side re-encode, as the
F61-FAMILY-4 note on f.124r; H193's strips regenerated from it, h193_items.tsv byte-identical), f328 4a13be67 (as H230), f210 313f92b3 (as H367's
fetch). The runner has not looked at any sheet.

## H399 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H359's prompt verbatim with part 2 = SCRATCH/h399/sheet_01..04.jpg (R01-R71): the 65 agreed draft 4TRI of fr.3982 f.97r L01-L16 (first cut, draft
position mapped to pass A's row by per-line sequence alignment) at H359 geometry, plus H377's 6 known f.61 strips. Script `h399_97r_firstcut.py`, key
`h399_items.tsv`. Native f202 fetched once (sha1 87d4236c as MANIFEST.tsv; 1 request). Disclosure: the runner looked at sheet_01 for marker placement
(the row's placement-sheet step): markers sit on or beside the intended 4-sign, some up to about 25 native px off (pass A/B x estimates differ by
about 11 native px on average, no bias); x changed to the mean of pass A and pass B where both read the sign in the same segment -- few tiles moved.

## H407 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
Two transcription questions on f.61's own hand with controls (script `h407_span_miss.py`, key `h407_items.tsv`). Disclosure: the runner looked at the
target lines (L03's end, L07/4, L11/1) before writing the row, and at the three sheets for marker placement; two changes before the call, both in
the script's docstring (control B3 moved from L08 pos 9 to pos 11, the letter-shaped CA at pos 10 being a clear-word lookalike; known PHI L08/1
replaced by L08/6, marker between two signs). Prompt (one blind Opus call, inline reply):
"You are a blind shape reader. Use no tool but your image reader on the images named; run no command, write no file. The images are strips of a
16th-century cipher letter written in a mix of ordinary handwriting and cipher signs. PART A: <A1_references.jpg> shows two reference signs, REF X and
REF Y, each under a red triangle. <A2_items.jpg> shows items A01-A12, each with a red triangle pointing down at one sign; look only at that sign.
For each item answer X if it is the same sign as REF X, Y if it is the same sign as REF Y, neither if it is a different sign from both, n if it
cannot be told. PART B: <B_strips.jpg> shows three strips B1-B3; in each a red triangle marks one cipher sign at the left. Count the cipher signs
from the marked one (counting it) rightwards along the same line, stopping before the first word of ordinary handwriting; also describe the last
cipher sign you counted in a few words. Reply ONLY with a TSV block 'id<TAB>answer<TAB>note': rows A01..A12 (answer X, Y, neither or n; note empty),
then B1..B3 (answer = the count as a number; note = the description of the last sign)."

## H410 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
Class check of f.61 L10 (script `h410_l10_class_qa.py`, key `h410_items.tsv`). Disclosure: the runner looked at the reference and item sheets for
marker placement (all markers on their signs; no change). Prompt (one blind Opus call, inline reply): "You are a blind shape reader. Use no tool but
your image reader on the images named; run no command, write no file. <references.jpg> shows eight reference signs R1-R8 of a 16th-century cipher,
each under a red triangle (look only at the marked sign in each). <items_01.jpg> and <items_02.jpg> show items I01-I29, each with a red triangle
pointing down at one sign; look only at that sign. For each item answer the reference (R1 to R8) whose sign it is the same sign as; answer none if it
matches no reference, n if it cannot be told. Small differences of size and slant within one hand do not make a different sign; an extra stroke or
loop does. Reply ONLY with a TSV block 'id<TAB>answer', rows I01..I29."

## H411 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H410's prompt verbatim with twelve references (R1-R12, references.jpg) and items I01-I32 (items_01..02.jpg); script `h411_class_qa.py`, key
`h411_items.tsv`. The runner looked at the sheets for marker placement only (no change).

## H413 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H410/H411 prompt verbatim with twelve references (SCRATCH/h411/references.jpg, unchanged) and items I01-I22 (SCRATCH/h413/items_01..02.jpg);
script `h413_l05_1_reread.py`, key `h413_items.tsv`. Same tile geometry as H411 (markers already checked there); no new look.

## H414 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H410 prompt with fifteen references (SCRATCH/h414/references.jpg, R1-R15), items I01-I24 (items_01..02.jpg), and one added option: answer P
if the marked mark is punctuation or not a cipher sign. Script `h414_other_two.py`, key `h414_items.tsv`. Target positions set by the runner's eye
(disclosed in the script); the runner checked marker placement on the target and new reference tiles.

## H418 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
fr.3983 f.108r class check (script `h418_108r_qa.py`, key `h418_items.tsv`): ten references R1-R10 (references.jpg) and items I01-I37
(items_01..02.jpg), marker UNDER the sign (H202 format). The runner looked at the sheets for placement; one fix before the call (edge tiles padded
instead of clamped). Prompt: "You are a blind shape reader. Use no tool but your image reader on the images named; run no command, write no file.
<references.jpg> shows ten reference signs R1-R10 of a 16th-century cipher, each above a red triangle (look only at the sign directly above the
triangle). <items_01.jpg> and <items_02.jpg> show items I01-I37, each with a red triangle under one sign; look only at the sign directly above it.
For each item answer the reference (R1 to R10) whose sign it is the same sign as; answer none if it matches no reference, P if the marked mark is
punctuation or ordinary handwriting, n if it cannot be told. Small differences of size and slant within one hand do not make a different sign; an
extra stroke or loop does. Reply ONLY with a TSV block id<TAB>answer, rows I01..I37."

## H420 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026) -- WRITTEN BEFORE THE CALL
H418 prompt verbatim with nine references (R1-R9, SCRATCH/h420/references.jpg) and items I01-I35 (h420/items_01..02.jpg); script
`h420_108r_qa2.py`, key `h420_items.tsv`. Changes from H418 in the docstring (no 4STEM class; edge tiles skipped; seed 420). Known items are H418's
non-edge ones (the row said re-drawn; with the edge filter the first two per class are kept -- disclosed). No new look at the sheets.
