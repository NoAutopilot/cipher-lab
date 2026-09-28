# PROMPTS_f188_f184_f106.md -- F61-FAMILY-3 (28 Sept 2026, written before any call). Three prompt templates; the exact text sent for each
# call is in passes/prompts_f3/<call>.txt (generated from these templates by gen_prompts_f3.py). Every call is a blind, independent Opus
# subagent (claude-opus-5-5) with no key, no letters for any sign and no other pass's output.
# Calls (12 in all, at most 4 at once): f184_clearA, f184_clearB (f.184r, 12 strips x 2 halves = 24 images each); f188_signsA_c1..c3,
# f188_signsB_c1..c3 (f.188r bands L01-L08, L09-L16, L17-L23; 5 segments per band, 1520 x 216 px at 2x); f106_signsA, f106_signsB,
# f106_glossA, f106_glossB (f.106r bands L01-L06, 7 segments per band, 1560 x 360 px at 3x).
# Cuts: sheets/f188r (cut_bands.py, region 900,1800,3550,2300 of images/3984_f188r.jpg, hand-set centres = the ink-profile rows 13-35 of
# the leaf, --up 58 --down 50 --seg 760 --overlap 60 --scale 2.0 --local 18); sheets/f184r (strips, sheets/f184r_strips.json: 12 strips
# 460 px tall stepping 375 px from y 470, two halves 1230-2930 and 2830-4430 native, scale 1); sheets/f106r (cut_bands.py, region
# 1540,600,3060,900 of images/3983_f106r.jpg, hand-set centres 90,196,296,396,500,610, --up 78 --down 42 --seg 520 --overlap 60 --scale 3.0 --local 15).

## f.188r sign pass template (Desportes' hand, no gloss on the leaf: the clear words are INSIDE the rows)

You are a blind transcriber of a 16th-century French manuscript letter that mixes ordinary handwriting with CIPHER SIGNS in the same lines (BnF fr.3984 f.188r, Paris, 22 July 1593). You will list, left to right, every cipher sign AND every ordinary clear word in each of {nb} line bands ({bands}). Each band is one line of the leaf and is given as FIVE image segments s1..s5 (left to right), each 1520 px wide and about 216 px tall, scaled 2x from the native scan. Consecutive segments of a band OVERLAP by 120 px: the last 120 px of segment sN show the same marks as the first 120 px of segment sN+1 (red tick marks at the top edge mark the overlap zone). List a mark that falls in the overlap ONCE ONLY, in the earlier segment; in the later segment start listing after the red tick.

What a band shows: one line of the letter runs across the middle of the band. The line is a mixture: stretches of invented cipher signs (4-like figures with loops, chains of small loops on stems, triangles with a bar, brackets, 43-like marks, crossed 4s) and stretches of ordinary French words in the writer's hand, in any order. The band's top and bottom edges may cut through the descenders or ascenders of the neighbouring lines: transcribe only the ONE line that runs through the middle of the band, never marks cut by the top or bottom edge. An ordinary clear word in the line is listed as ONE row with sign = PLAIN and the word, exactly as written (16th-century spelling kept, abbreviation marks expanded in square brackets), in the note; a clear word is never split into signs and a cipher sign is never read as a letter. A long horizontal dash inside the line (a stroke with no sign shape) is listed as sign = DASH. A small superscript letter or mark written above a sign is part of that sign: name it in the note ('superscript x above').

Code every cipher sign with the shape atlas below (the 'code' column). Use OTHER for a sign matching none, with a shape description in the note. If a sign is between two codes, give the best code and name the alternative in the note as 'alt CODE'. A chain of several small loops on one stem or bar is ONE sign (PHI) -- but two separate stems are two signs. Confidence h/m/l.

Atlas (code TAB shape):
{atlas}

Read the {ni} images with the Read tool in this order: for each band, segment s1, s2, s3, s4, s5:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	sign	conf	segment	x_px	note
one row per sign or clear word; 'line' is the band id (L01..L23); 'pos' counts from 1 within the band across all five segments; 'segment' is s1..s5; 'x_px' is the mark's horizontal centre in pixels within its segment image (0-1520); 'note' is free text (shape words, 'alt CODE', or the clear word for PLAIN). No letters of the alphabet are to be guessed for any cipher sign: this is a shape transcription only, and no key or reading is to be attempted. When done, report only: the number of signs and the number of PLAIN words per band, and the totals.
OUTPUT PATH: {out}

## f.184r clear-text pass template (the separate-sheet decipherment of f.188, plain French, one hand)

You are a blind transcriber of a 16th-century French manuscript page in ordinary handwriting (BnF fr.3984 f.184r, a contemporary clear copy, 1593; about 46 lines). You will transcribe every line of the page, exactly as written. The page is given as 12 horizontal strips S01..S12 from top to bottom, each about 4 lines tall, and each strip as TWO halves h1 (left) and h2 (right), each 1700 px wide and 460 px tall at the native scan resolution. The two halves of a strip overlap by 100 px (a red tick at the top edge marks the overlap): the words in the overlap are read once, as part of the line. Consecutive strips overlap by 85 px vertically: a line cut by the TOP edge of a strip is skipped (it is complete in the previous strip); a line cut by the BOTTOM edge is skipped too (it is complete in the next strip); a line that is complete near the bottom of strip k AND complete near the top of strip k+1 is listed once, under strip k. Number the lines of the page consecutively from 1 across all strips.

Transcription rules: 16th-century spelling kept exactly (nostre, aultre, tousiours, ie/je as written, u/v as written); abbreviation marks expanded in square brackets (Mons[eigneu]r, s[ainc]te[té], q[ue]); a word you cannot read as '?' with the letters you can read (na?ent); a word or stretch that is UNDERLINED on the page is wrapped in curly braces, {like this} -- mark every underline exactly (word by word if the underline starts or stops mid-word, write the underlined part inside the braces); a word crossed out on the page is wrapped in double square brackets [[like this]]; a long dash written as a filler is written as '--'. Keep the writer's word order and line breaks; do not modernise, do not correct, do not add punctuation the page does not carry.

Read the 24 images with the Read tool in this order: for each strip, half h1 then h2:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	strip	conf	text
one row per line of the page; 'line' counts from 1 across the page; 'strip' is the strip id (S01..S12) the line was read in; conf h/m/l for the line; 'text' is the line exactly as written under the rules above (no tab characters inside it). When done, report only: the number of lines per strip and the total.
OUTPUT PATH: {out}

## f.106r sign pass template (Mayenne's secretary, dense, sparse gloss, heavy bleed-through)

You are a blind transcriber of a 16th-century French cipher manuscript (BnF fr.3983 f.106r, headed '4 de mars 1593'). You will list every CIPHER SIGN, left to right, in each of 6 line bands (L01..L06, the first six cipher rows of the leaf). Each band is one cipher row of the leaf and is given as SEVEN image segments s1..s7 (left to right), each 1560 px wide and about 360 px tall, scaled 3x from the native scan. Consecutive segments of a band OVERLAP by 180 px: the last 180 px of segment sN show the same marks as the first 180 px of segment sN+1 (red tick marks at the top edge mark the overlap zone). List a sign that falls in the overlap ONCE ONLY, in the earlier segment; in the later segment start listing after the red tick.

What a band shows: the cipher row runs across the LOWER-MIDDLE of the band, about 125 px above the bottom edge (a sequence of invented signs: 4-like figures with loops, chains of small loops on stems, triangles with a bar, brackets, 43-like marks, crossed 4s, '24'-like marks); ABOVE it, in the upper part of the band, a few small ordinary clear words (a sparse French decipherment) and the descenders of the previous cipher row -- IGNORE the clear words entirely, they are not signs, and never transcribe marks cut by the top or bottom edge. The leaf is thin: the writing of the other side shows through as a lighter, mirror-image grey ghost between and behind the signs -- transcribe only the dark, right-reading ink of this side, never the ghost. The signs are written close together; a sign is one connected ink figure with its own stem or body. A clear word written INSIDE the cipher row (in the row itself) is listed as one row with sign = PLAIN and the word in the note. A long horizontal dash inside the row is listed as sign = DASH.

Code every sign with the shape atlas below (the 'code' column). Use OTHER for a sign matching none, with a shape description in the note. If a sign is between two codes, give the best code and name the alternative in the note as 'alt CODE'. A chain of several small loops on one stem or bar is ONE sign (PHI) -- but two separate stems are two signs. Confidence h/m/l.

Atlas (code TAB shape):
{atlas}

Read the 42 images with the Read tool in this order: for each band, segment s1 .. s7:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	sign	conf	segment	x_px	note
one row per sign; 'line' is the band id (L01..L06); 'pos' counts from 1 within the band across all seven segments; 'segment' is s1..s7; 'x_px' is the sign's horizontal centre in pixels within its segment image (0-1560); 'note' is free text. No letters of the alphabet are to be guessed for any sign: this is a shape transcription only, and no key or reading is to be attempted. When done, report only: the number of signs per band, and the total.
OUTPUT PATH: {out}

## f.106r gloss pass template

You are a blind transcriber of the small clear (ordinary handwriting) French words written ABOVE and BETWEEN the cipher rows on a 16th-century manuscript leaf (BnF fr.3983 f.106r, headed '4 de mars 1593'; a sparse contemporary decipherment written by a secretary over parts of each cipher line). You will transcribe the clear words that belong to the cipher row in each of 6 line bands (L01..L06). Each band is given as SEVEN image segments s1..s7 (left to right), each 1560 px wide and about 360 px tall, scaled 3x from the native scan. Consecutive segments overlap by 180 px (red tick marks at the top edge): a word in the overlap is listed ONCE ONLY, in the earlier segment; in the later segment start listing after the red tick.

What a band shows: the cipher row (invented signs: 4-like figures with loops, chains of loops, triangles, brackets, '24' and '43'-like marks) runs across the LOWER-MIDDLE of the band, about 125 px above the bottom edge -- do not transcribe the signs; ABOVE the row, in the gap between it and the previous row, the small clear words of the decipherment, sparse (a few words per line, over the signs they decipher) -- transcribe every one of them, left to right, exactly as written (16th-century spelling kept, e.g. 'nostre', 'aultre', 'tousiours'; abbreviation marks expanded in square brackets, e.g. 'Cardin[al]'; an illegible word as '?' with as many letters as you can read, e.g. 'na?ent'). The leaf is thin: the writing of the other side shows through as a lighter, mirror-image grey ghost -- read only the dark, right-reading ink. The band's top edge may cut through the previous cipher row and the bottom edge through the NEXT row's clear words: skip anything cut by an edge, and transcribe only the clear words that sit directly above THIS band's cipher row (between the row and the previous row). A clear word written INSIDE the cipher row is listed with kind = inline; the words above the row have kind = gloss. A long horizontal dash written in the clear layer is listed as its own row with word = '-' and kind = dash.

Read the 42 images with the Read tool in this order: for each band, segment s1 .. s7:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	kind	word	conf	segment	x0_px	x1_px
one row per word or dash; 'line' is the band id (L01..L06); 'pos' counts from 1 within the band across all seven segments; 'segment' is s1..s7; x0_px/x1_px are the word's left and right edges in pixels within its segment image (0-1560); conf h/m/l. No cipher sign is to be transcribed and no reading of the cipher is to be attempted. When done, report only: the number of words per band and the total.
OUTPUT PATH: {out}
