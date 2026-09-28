# PROMPTS_f124r_gloss.md -- F61-FAMILY-5 (28 Sept 2026, 05:0x UTC, written BEFORE any call). The letter-aligned gloss recipe for
# de Diou's hand (fr.3982 f.124r, then f.97r): H45's word passes agreed on 42% of words at 2x and 3x, but the gloss on these leaves
# is a letter-by-letter interlinear decipherment, so it is read as LETTERS ALIGNED TO SIGN POSITIONS, not as words. Segments are cut
# by cut_segments.py (8 signs per segment, 3x, a band from cipher centre - 82 to + 42 native px, a numbered red tick under every
# sign's x); each reader gets, per segment, the image and the v3 skeleton of that segment (the period letter SET already attested for
# the sign's class on the other leaves, '?' where none or where the position is HIDDEN for the control). Hidden positions: cut_segments.py
# --mask hides a random share of the covered positions as '?' (seed per segment); the reader cannot tell a hidden covered position
# from a truly uncovered one, so agreement on the hidden positions measures reading, not copying. Positive control (brief step 1):
# chunk c0 = 8 fully-covered segments of L01-L02 at --mask 0.4, two blind Opus passes; PASS if the reconciled letters at the hidden
# positions fall in the v3 set at 0.8 or better (per pass and reconciled; '-' = no letter counts as a miss; also reported without '-').
# Target chunks: --mask 0.3 (the hidden positions keep a running control on every chunk); rows carrying an uncovered class first.
# Two blind Opus passes per chunk (A, B), independent, same prompt; reconciled per (segment, position) by tools/reconcile_passes.py
# (nw, letters as 'signs'); the exact text of every call is in passes/prompts_f5/<call>.txt (gen_prompts_f5.py from this template).
# Output columns: how = r (the letter is read from the ink above the tick) or i (inferred from the word the neighbouring letters
# form, the ink itself unclear) -- a pair from an 'i' position is graded M, from an 'r' position C.

## Letter pass template

You are a blind transcriber of a 16th-century French manuscript leaf (BnF fr.3982 f.124r, Rome, dated on the leaf 7 November 1592). The leaf carries a cipher (invented signs: 4-like figures with loops, chains of small loops, triangles, brackets, 43-like marks) and, ABOVE each cipher row, a contemporary interlinear decipherment written in small ordinary handwriting: the decipherer wrote each clear letter above the cipher sign it stands for, so the clear text runs letter by letter above the signs (sometimes a whole short word, such as 'que' or 'M[onsieu]r', sits above ONE sign; sometimes a sign has nothing above it; the letters are not perfectly centred over their signs, and a word's letters may drift a little to the right of its signs). 16th-century spelling and letterforms: u and v are the same letter written u, i and j written i, long s, 'nostre', 'aultre', 'faict'.

You will read {ns} SEGMENTS ({segs}). Each segment is one image, 3x the native scan, showing a short stretch of one cipher row (6 to 10 signs) across the lower-middle of the image with the decipherer's clear letters above it; the descenders of the previous row may hang in from the top edge and the tops of the next row's signs may show at the bottom edge (ignore both). Under the image is a white strip with red ticks numbered 1..k: each tick stands directly under ONE cipher sign of the row (at the sign's horizontal centre). Your job, for every tick number, is to report the clear letter or letters the decipherer wrote ABOVE THAT SIGN.

For each segment you are also given a SKELETON: for some positions the letter set already established for that sign's shape from other leaves of the same cipher, written 3:[a/n] (position 3 is a or n) -- a check on your reading, never a substitute for it; ? means no set is available for that position. Report what you SEE above the tick; if the ink clearly shows a letter outside the set, report the letter you see and say so in the note. Where the ink at a position is unclear but the neighbouring letters make the word plain, you may complete it and mark how = i (inferred); a letter you actually read in the ink is how = r. Give '-' where nothing is written above a sign (a null or a gap), and the whole word where one word sits above one sign. Do not transcribe the cipher signs and do not attempt any key or reading of the cipher beyond the clear letters that are written on the leaf.

Read the {ns} images with the Read tool in this order:
{paths}
Skeletons (segment: position:set ...):
{skeletons}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
segment	pos	letters	conf	how	note
one row per (segment, tick number), every tick of every segment listed, in order; 'segment' is the image's stem (e.g. f124s_L01_g1); 'pos' the tick number; 'letters' the letter(s) above that sign ('-' for none, a word for a word above one sign, lower case, u for u/v, i for i/j, no accents); conf h/m/l; how r or i; 'note' free text (e.g. 'outside the set: reads o', 'struck through', 'tall s'). When done, report only: the number of rows written and the number of '-' rows.
OUTPUT PATH: {out}

## f.97r sign passes (05:1x UTC, written before any f.97r call)

fr.3982 f.97r cut by cut_bands.py from the native leaf (region 880,560,3450,4540; 42 cipher-row centres = the ink-weight detector at pitch 90 over the left 1600 px, plus three rows it missed (native y 2157, 3005, 4092) taken from a long-stroke profile and checked on four ruler panels by eye; --up 70 --down 55 --seg 760 --overlap 60 --scale 2 --track 18, as f.124r). Sign passes use PROMPTS_undec.md's "Sign pass template (f.124r)" verbatim with the leaf description replaced by "BnF fr.3982 f.97r, de Diou to president Jeannin, Rome, dated on the leaf 27 October 1592" and the band range L01..L42; chunks of 8 bands (c1 = L01-L08 ... c6 = L41-L42), two blind Opus passes per chunk, prompt files passes/prompts_f5/f97r_signs<A|B>_c<k>.txt.

## Knob change after the letter-per-tick control (05:2x UTC, before any further gloss call)

Control c0 (letter per tick) FAILED: hidden-position agreement 12/32 = 0.375 (pass A) and 10/32 = 0.312 (B), 0.545 / 0.455
without the '-' rows; shown positions 0.536 for both; the passes agree with each other on 34/51 positions. Cause, seen on
f124s_L01_g8: the decipherer writes each clear WORD compactly over a span of signs ("tisfaict" over four struck signs, then a
dash), so a letter does not sit above each sign. The one knob changed: the reporting unit becomes the WORD with its tick span
(first and last tick under it); letters are placed on the signs of the span afterwards by the family's DP (align_period.py
--segments: tools/interlinear_align.py per segment, the v3 sets as the initial key, hidden and uncovered positions free).
Same segments, same control chunk c0, two fresh blind Opus passes; gate unchanged (0.8 on the hidden positions, after DP
placement); if it fails again the leaf is held and reported (brief step 1).

## Word-span pass template

You are a blind transcriber of a 16th-century French manuscript leaf (BnF fr.3982 f.124r, Rome, dated on the leaf 7 November 1592). The leaf carries a cipher (invented signs: 4-like figures with loops, chains of small loops, triangles, brackets, 43-like marks) and, ABOVE each cipher row, a contemporary interlinear decipherment in small ordinary handwriting: the decipherer wrote the clear words above the signs they stand for, roughly letter by letter but compactly, so a word sits over a span of a few signs (a short word such as 'que' or 'M[onsieu]r' can sit over ONE sign). 16th-century spelling and letterforms: u and v both written u, i and j written i, long s, 'nostre', 'aultre', 'faict', 'satisfaict'.

You will read {ns} SEGMENTS ({segs}). Each segment is one image, 3x the native scan, showing a short stretch of one cipher row (6 to 10 signs) across the lower-middle of the image with the decipherer's clear words above it; the descenders of the previous row may hang in from the top edge and the tops of the next row's signs may show at the bottom edge (ignore both). Under the image is a white strip with red ticks numbered 1..k, one tick directly under each cipher sign of the row. Your job: list every clear word (or part of a word) written above this stretch of the row, left to right, exactly as written (16th-century spelling kept; an illegible letter as ?; a word cut by the left or right edge of the image as the letters you see, marked cut_left or cut_right in the note), and for each give the tick span it sits over: tick_from = the tick nearest to the word's first letter, tick_to = the tick nearest to its last letter (a word over one sign has tick_from = tick_to). A long horizontal dash with no letters is listed as word '-' with kind dash and its tick span. A word the decipherer crossed out is listed with kind struck. Report only what is written on the leaf: do not guess French from the signs, and do not attempt any key or reading of the cipher.

For each segment a SKELETON is also given: for some positions the letter set already established for that sign's shape from other leaves, written 3:[a/n] (position 3 is a or n); ? means no set. It is a check on your reading only; report what the ink shows, and note a word whose letters contradict the sets.

Read the {ns} images with the Read tool in this order:
{paths}
Skeletons (segment: position:set ...):
{skeletons}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
segment	pos	kind	word	tick_from	tick_to	conf	note
one row per word or dash, 'pos' counting from 1 within the segment; kind = gloss, dash or struck; word in lower case, u for u/v, i for i/j, no accents, abbreviation marks expanded in square brackets; conf h/m/l. When done, report only: the number of words per segment and the total.
OUTPUT PATH: {out}
