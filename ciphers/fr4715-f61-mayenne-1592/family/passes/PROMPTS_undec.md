# PROMPTS_undec.md -- F61-FAMILY-4 (28 Sept 2026, 03:5x UTC, written BEFORE any call). Prompt templates for the family's four
# "undeciphered" leaves (brief step 1). The exact text sent for each call is in passes/prompts_f4/<call>.txt, generated from these
# templates by gen_prompts_f4.py. f.124r turned out on the native image to be interlined THROUGHOUT (45 cipher rows, a period gloss
# above each; the manifest's "partly interlined" came from a 1200-px thumbnail look), so it is treated the f.101r way: chunks of
# 8 bands (c1 = L01-L08, c2 = L09-L16, c3 = L17-L24, c4 = L25-L32, c5 = L33-L40, c6 = L41-L45), per chunk two blind Opus sign
# passes (A, B) and two blind Opus gloss passes (A, B), 4 vision calls per chunk. The sign atlas is f.101r's (PROMPTS_f101r.md,
# with the LOOPS/ZBAR/RSIGN/H24 rows), unchanged, so the classes are comparable across leaves. Bands: sheets/f124r, cut by
# cut_bands.py from the native leaf (region 950,1250,3450,4750; hand-set cipher-row centres from a long-stroke profile of the
# left quarter, checked by eye on three debug strips, one missed row inserted at y 4392; --up 70 --down 55 --track 18, 2x), five
# segments per band of 1520 x 250 px (s5 1300 px), 120-px overlap at 2x.
# The sign-only template (leaves with no gloss: f.97r, f.186r, f.189r) is the f.188r template shape (clear words INSIDE the rows).

## Sign pass template (f.124r)

You are a blind transcriber of a 16th-century French cipher manuscript (BnF fr.3982 f.124r, Rome, dated on the leaf 7 November 1592). You will list every CIPHER SIGN, left to right, in each of {nb} line bands ({bands}). Each band is one cipher row of the leaf and is given as FIVE image segments s1..s5 (left to right), each 1520 px wide (s5 1300 px) and 250 px tall, scaled 2x from the native scan. Consecutive segments of a band OVERLAP by 120 px: the last 120 px of segment sN show the same signs as the first 120 px of segment sN+1 (red tick marks at the top edge mark the overlap zone). List a sign that falls in the overlap ONCE ONLY, in the earlier segment; in the later segment start listing after the red tick.

What a band shows: the cipher row runs across the middle of the band (a sequence of invented signs: 4-like figures with loops, chains of small loops on stems, triangles with a bar, brackets, 43-like marks); ABOVE it, a line of small ordinary handwriting (French clear words and long dashes) -- IGNORE that clear line entirely, it is not signs. The rows are not perfectly level (they rise a little towards the right), and each segment was centred on the row separately, so the row may sit slightly higher or lower from one segment to the next. The band's bottom edge may cut through the NEXT clear line or the tops of the next cipher row, and its top edge may cut through the descenders of the previous cipher row: transcribe only the ONE complete cipher row of this band, never marks cut by the top or bottom edge. Some bands carry an ordinary clear word INSIDE the cipher row (in the row itself, not above it): list such a word as one row with sign = PLAIN and the word in the note. A long horizontal dash inside the cipher row (a stroke with no sign shape) is listed as sign = DASH. A stroke that crosses out signs (a cancellation) is noted on the signs it crosses ('struck') and the signs are still listed.

Code every sign with the shape atlas below (the 'code' column). Use OTHER for a sign matching none, with a shape description in the note. If a sign is between two codes, give the best code and name the alternative in the note as 'alt CODE'. A chain of several small loops on one stem or bar is ONE sign (PHI) -- but two separate stems are two signs. Confidence h/m/l.

Atlas (code TAB shape):
{atlas}

Read the {ni} images with the Read tool in this order: for each band, segment s1, s2, s3, s4, s5:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	sign	conf	segment	x_px	note
one row per sign; 'line' is the band id (L01..L45); 'pos' counts from 1 within the band across all five segments; 'segment' is s1..s5; 'x_px' is the sign's horizontal centre in pixels within its segment image (0-1520); 'note' is free text (shape words, 'alt CODE', or the clear word for PLAIN). No letters of the alphabet are to be guessed for any sign: this is a shape transcription only, and no key or reading is to be attempted. When done, report only: the number of signs per band, and the total.
OUTPUT PATH: {out}

## Gloss pass template (f.124r)

You are a blind transcriber of the small clear (ordinary handwriting) French words written ABOVE the cipher rows on a 16th-century manuscript leaf (BnF fr.3982 f.124r, Rome, dated on the leaf 7 November 1592; a contemporary interlinear decipherment written by a secretary above each cipher line). You will transcribe the clear line above the cipher row in each of {nb} line bands ({bands}). Each band is given as FIVE image segments s1..s5 (left to right), each 1520 px wide (s5 1300 px) and 250 px tall, scaled 2x from the native scan. Consecutive segments of a band overlap by 120 px (red tick marks at the top edge): a word in the overlap is listed ONCE ONLY, in the earlier segment; in the later segment start listing after the red tick.

What a band shows: the cipher row (invented signs: 4-like figures with loops, chains of loops, triangles, brackets) runs across the middle of the band -- do not transcribe these; ABOVE it, the small clear words of the decipherment -- transcribe every one of them, left to right, exactly as written (16th-century spelling kept, e.g. 'nostre', 'aultre', 'tousiours', 'saincteté'; abbreviation marks expanded in square brackets, e.g. 'Cardin[al]', 's[ainc]te[té]'; an illegible word as '?' with as many letters as you can read, e.g. 'na?ent'). The clear line also carries long horizontal DASHES (a stroke with no letters, sometimes as long as several words): list each dash as its own row with word = '-' and kind = dash, with its x-range, in its place in the sequence -- they matter for alignment. A clear word written INSIDE the cipher row (in the row itself, not above it) is listed with kind = inline; the words above the row have kind = gloss; a word the decipherer crossed out is listed with '_struck' appended. The rows are not perfectly level (they rise a little towards the right) and each segment was centred on the row separately, so the clear line may sit slightly higher or lower from one segment to the next. The band's bottom edge may cut through the NEXT clear line (the one belonging to the next band): skip anything cut by the bottom edge; the top edge may show the descenders of the previous cipher row: skip those too. Transcribe only the one complete clear line that sits directly above this band's cipher row.

Read the {ni} images with the Read tool in this order: for each band, segment s1, s2, s3, s4, s5:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	kind	word	conf	segment	x0_px	x1_px
one row per word or dash; 'line' is the band id (L01..L45); 'pos' counts from 1 within the band across all five segments; 'segment' is s1..s5; x0_px/x1_px are the word's left and right edges in pixels within its segment image (0-1520); conf h/m/l. No cipher sign is to be transcribed and no reading of the cipher is to be attempted. When done, report only: the number of words per band and the total.
OUTPUT PATH: {out}

## Sign pass template (leaves without gloss: f.97r, f.186r, f.189r)

You are a blind transcriber of a 16th-century French cipher manuscript ({leafdesc}). You will list every CIPHER SIGN, left to right, in each of {nb} line bands ({bands}). Each band is one row of the leaf and is given as image segments s1..s{ns} (left to right), each {segw} px wide (the last one narrower) and {segh} px tall, scaled 2x from the native scan. Consecutive segments of a band OVERLAP by 120 px (red tick marks at the top edge mark the overlap zone). List a sign that falls in the overlap ONCE ONLY, in the earlier segment; in the later segment start listing after the red tick.

What a band shows: one row of the letter across the middle of the band. The row is cipher (invented signs: 4-like figures with loops, chains of small loops on stems, triangles with a bar, brackets, 43-like marks), sometimes with ordinary clear French words or names written INSIDE the row between the signs: list such a word as one row with sign = PLAIN and the word in the note. There is no clear line above the rows on this leaf. The band's top and bottom edges may cut through the neighbouring rows: transcribe only the ONE complete row of this band, never marks cut by the top or bottom edge. A long horizontal dash inside the row (a stroke with no sign shape) is listed as sign = DASH.

Code every sign with the shape atlas below (the 'code' column). Use OTHER for a sign matching none, with a shape description in the note. If a sign is between two codes, give the best code and name the alternative in the note as 'alt CODE'. A chain of several small loops on one stem or bar is ONE sign (PHI) -- but two separate stems are two signs. Confidence h/m/l.

Atlas (code TAB shape):
{atlas}

Read the {ni} images with the Read tool in this order: for each band, its segments s1..s{ns}:
{paths}
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	sign	conf	segment	x_px	note
one row per sign; 'line' is the band id; 'pos' counts from 1 within the band across all segments; 'segment' is s1..s{ns}; 'x_px' is the sign's horizontal centre in pixels within its segment image; 'note' is free text (shape words, 'alt CODE', or the clear word for PLAIN). No letters of the alphabet are to be guessed for any sign: this is a shape transcription only, and no key or reading is to be attempted. When done, report only: the number of signs per band, and the total.
OUTPUT PATH: {out}
