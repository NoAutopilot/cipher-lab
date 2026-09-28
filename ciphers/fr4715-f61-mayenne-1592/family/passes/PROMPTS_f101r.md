# PROMPTS_f101r.md -- F61-FAMILY-2 (28 Sept 2026, written before any call). Two prompt templates; the exact text sent for each
# chunk and pass is in passes/prompts_f101r/<pass>_c<k>.txt (generated from these templates by this file's own script block below).
# Chunks of 8 bands (5 segments each, 40 images per call): c1 = L01-L08; c2 = L09-L16; c3 = L17-L24; c4 = L25-L32; c5 = L33-L40; c6 = L41-L46.
# Amended after chunk 1 (01:33 UTC, before any chunk-2 call): atlas rows LOOPS, ZBAR, RSIGN added (pass A's OTHER notes 'loop chain no stem' x60 / 'z-like with bar' x38 / 'r-like' x11 vs pass B's PHI/ZHOOK/BETA were one systematic split, 67.8% raw agreement), and the row-droop paragraph added to both templates (both chunk-1 sign readers found L01's row dropping out of s5 and read it from the top of L02). Chunk 1 ran on the templates as first written (the c1 files are unchanged).
# Per chunk: gloss passes A and B (Sonnet, blind, independent), sign passes A and B (Opus, blind, independent): 4 vision calls per chunk, 24 in all.

## Sign pass template

You are a blind transcriber of a 16th-century French cipher manuscript (BnF fr.3982 f.101r, Rome, 27 Oct 1592). You will list every CIPHER SIGN, left to right, in each of {nb} line bands ({bands}). Each band is one cipher row of the leaf and is given as FIVE image segments s1..s5 (left to right), each 1520 px wide and 280 px tall, scaled 2x from the native scan. Consecutive segments of a band OVERLAP by 120 px: the last 120 px of segment sN show the same signs as the first 120 px of segment sN+1 (red tick marks at the top edge mark the overlap zone). List a sign that falls in the overlap ONCE ONLY, in the earlier segment; in the later segment start listing after the red tick.

What a band shows: the cipher row runs across the middle of the band (a sequence of invented signs: 4-like figures with loops, chains of small loops on stems, triangles with a bar, brackets, 43-like marks); ABOVE it, a line of small ordinary handwriting (French clear words and long dashes) -- IGNORE that clear line entirely, it is not signs. The rows are not perfectly level: towards the right of the leaf the cipher row may sit a little higher or lower in the band than on the left. The band's bottom edge may cut through the NEXT clear line or the tops of the next cipher row, and its top edge may cut through the descenders of the previous cipher row: transcribe only the ONE complete cipher row of this band, never marks cut by the top or bottom edge. Some bands carry an ordinary clear word INSIDE the cipher row (in the row itself, not above it): list such a word as one row with sign = PLAIN and the word in the note. A long horizontal dash inside the cipher row (a stroke with no sign shape) is listed as sign = DASH.

Row droop at the right end: on this leaf a cipher row can drop below the band's bottom edge in segments s4-s5 (the row curves down towards the right margin). Where that happens, the same row is visible, cut by the TOP edge, in segment s4/s5 of the NEXT band: read this band's dropped signs there and list them under THIS band (segment s4/s5, x within that image), and never list them again under the next band. For the last band of this chunk the two extra images at the end of the list (the next band's s4 and s5) are given for that purpose only: nothing in them is transcribed except this band's dropped row.

Code every sign with the shape atlas below (the 'code' column). Use OTHER for a sign matching none, with a shape description in the note. If a sign is between two codes, give the best code and name the alternative in the note as 'alt CODE'. A chain of several small loops on one stem or bar is ONE sign (PHI) -- but two separate stems are two signs. Confidence h/m/l.

Atlas (code TAB shape):
PHI	loops (one or several) on a long vertical stem, phi-like
C43	a mark shaped like the digits 43 written together
CA	a mark shaped like a cursive a
VBAR_A	closed down-pointing triangle whose top side is a horizontal bar, nothing above the bar, no second bar
VBAR_B	closed down-pointing triangle with a top bar AND a second horizontal bar crossing its bottom point
C6	a mark shaped like the digit 6
4TRI	a 4-shaped element (4 with a crossbar) sitting above a small triangle or V
INF	an infinity sign or figure-8 lying on a horizontal bar
DBL	two loops on a stem, one above the other (o-T-o)
LOOPBAR	a loop on a stem with a bar at the foot
EBR_A	an E-like bracket open to the right whose top bar is joined to the foot of the vertical by a fine hairline diagonal, the foot bar longer than the top bar and tapering into a tail (H22 group A)
EBR_B	a plain squared C or gamma open to the right: top bar and foot bar on a vertical, no diagonal, the top bar longest, often a short spur of the vertical above the top bar (H22 group B)
ISH	a closed capital I: a thin vertical with a bar on both sides at top and foot (H22 group C)
ZHOOK	a 7 or Z hook over two close slanted stems, crossed
CROSS	a plain plus or cross, possibly with a stroke rising to the upper right
ELOOP	a dark e-shaped loop with a curling tail
4PI	a 4-shaped element above two stems on a bar (4 over pi)
HASH4	a dense crossed-4 cluster, hash-like, with stems
LOOPSTEM1	a single loop on a long stem (not phi-like, not double)
CH	a mark shaped like a cursive h
BETA	a beta-like shape: a loop at the top of a stem with a 3-like bowl below it
LL	a mark shaped like ll
4STEM	a 4 with a long crossed stem and no triangle below
OTHER	any cipher sign matching none of the above (describe it in the note)
H24	a 2-like curl joined to a crossed 4 (the '24' sign); distinct from HASH4, the plain dense crossed-4/hash cluster
LOOPS	a chain of two or more small loops written side by side with NO stem and NO bar (like 'oo' or 'ooo'); a chain that sits on a vertical stem is PHI, not LOOPS
ZBAR	a z-like or 2-like zigzag stroke with a horizontal bar through or under it and no stems; distinct from ZHOOK (a 7/Z hook over two slanted stems)
RSIGN	a small r-like or 5-like sign, a short stem with a hook to the right, no loop (pass A of chunk 1 called it 'r-like, alt beta')

Read the {ni} images with the Read tool in this order: for each band, segment s1, s2, s3, s4, s5:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	sign	conf	segment	x_px	note
one row per sign; 'line' is the band id (L01..L46); 'pos' counts from 1 within the band across all five segments; 'segment' is s1..s5; 'x_px' is the sign's horizontal centre in pixels within its segment image (0-1520); 'note' is free text (shape words, 'alt CODE', or the clear word for PLAIN). No letters of the alphabet are to be guessed for any sign: this is a shape transcription only, and no key or reading is to be attempted. When done, report only: the number of signs per band, and the total.
OUTPUT PATH: {out}

## Gloss pass template

You are a blind transcriber of the small clear (ordinary handwriting) French words written ABOVE the cipher rows on a 16th-century manuscript leaf (BnF fr.3982 f.101r, Rome, 27 October 1592; a contemporary interlinear decipherment written by a secretary above each cipher line). You will transcribe the clear line above the cipher row in each of {nb} line bands ({bands}). Each band is given as FIVE image segments s1..s5 (left to right), each 1520 px wide and 280 px tall, scaled 2x from the native scan. Consecutive segments of a band overlap by 120 px (red tick marks at the top edge): a word in the overlap is listed ONCE ONLY, in the earlier segment; in the later segment start listing after the red tick.

What a band shows: the cipher row (invented signs: 4-like figures with loops, chains of loops, triangles, brackets) runs across the middle of the band -- do not transcribe these; ABOVE it, the small clear words of the decipherment -- transcribe every one of them, left to right, exactly as written (16th-century spelling kept, e.g. 'nostre', 'aultre', 'tousiours', 'saincteté'; abbreviation marks expanded in square brackets, e.g. 'Cardin[al]', 's[ainc]te[té]'; an illegible word as '?' with as many letters as you can read, e.g. 'na?ent'). The clear line also carries long horizontal DASHES (a stroke with no letters, sometimes an underline as long as several words): list each dash as its own row with word = '-' and kind = dash, with its x-range, in its place in the sequence -- they matter for alignment. A clear word written INSIDE the cipher row (in the row itself, not above it) is listed with kind = inline; the words above the row have kind = gloss. The rows are not perfectly level: towards the right of the leaf the clear line and its cipher row may sit a little higher or lower than on the left. The band's bottom edge may cut through the NEXT clear line (the one belonging to the next band): skip anything cut by the bottom edge; the top edge may show the descenders of the previous cipher row: skip those too. Transcribe only the one complete clear line that sits directly above this band's cipher row.

Row droop at the right end: on this leaf a cipher row and its clear line can drop towards the band's bottom edge in segments s4-s5 (they curve down near the right margin); the clear line of THIS band is always the one written directly above this band's cipher row, even when a second clear line (the next band's) appears at the bottom edge -- skip that one. If the clear line itself drops out of the bottom edge at the far right, its continuation is visible, cut by the top edge, in segment s4/s5 of the NEXT band: read the dropped words there and list them under THIS band (segment s4/s5, x within that image). For the last band of this chunk the two extra images at the end of the list (the next band's s4 and s5) are given for that purpose only.

Read the {ni} images with the Read tool in this order: for each band, segment s1, s2, s3, s4, s5:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	kind	word	conf	segment	x0_px	x1_px
one row per word or dash; 'line' is the band id (L01..L46); 'pos' counts from 1 within the band across all five segments; 'segment' is s1..s5; x0_px/x1_px are the word's left and right edges in pixels within its segment image (0-1520); conf h/m/l. No cipher sign is to be transcribed and no reading of the cipher is to be attempted. When done, report only: the number of words per band and the total.
OUTPUT PATH: {out}
