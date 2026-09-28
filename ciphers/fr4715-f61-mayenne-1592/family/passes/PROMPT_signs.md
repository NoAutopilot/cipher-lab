You are a blind transcriber of a 16th-century French cipher manuscript (BnF fr.3984 f.274r, 1593). You will list every CIPHER SIGN, left to right, in each of 6 line bands. Each band is given as two overlapping image segments (segment 1 = left part, segment 2 = right part, each 2240 px wide, scaled 1.6x from the native scan). The two segments of a band OVERLAP by 160 px: the last 160 px of segment 1 show the same signs as the first 160 px of segment 2 (red tick marks at the top edge mark the overlap zone). List a sign that falls in the overlap ONCE ONLY, in segment 1; in segment 2 start listing after the red tick.

Each band contains: (a) a row of small ordinary handwriting (French clear words) written ABOVE the cipher row -- IGNORE these entirely, they are not signs; (b) the cipher row itself: a sequence of invented signs. Some bands may also carry a few ordinary clear words INSIDE the cipher row (e.g. "si vous" at the end of band 6): list such a clear word as one row with sign = PLAIN and the word in the note. Ordinary handwriting from a neighbouring line that intrudes at the very top or bottom of a band is not a sign.

Code every sign with the shape atlas below (the 'code' column). Use OTHER for a sign matching none, with a shape description in the note. If a sign is between two codes, give the best code and name the alternative in the note as 'alt CODE'. Confidence h/m/l.

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
EBR	an E-like bracket open to the right
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

Read the 12 images with the Read tool in this order: for each band L01..L06, segment s1 then s2:
  /home/user/cipher-lab/ciphers/fr4715-f61-mayenne-1592/family/sheets/f274_L01_s1.jpg  (then _s2, then L02_s1 ... L06_s2)
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	sign	conf	segment	x_px	note
one row per sign; 'line' is L01..L06; 'pos' counts from 1 within the band across both segments; 'x_px' is the sign's horizontal centre in pixels within its segment image; 'note' is free text (shape words, 'alt CODE', or the clear word for PLAIN). No letters of the alphabet are to be guessed for any sign: this is a shape transcription only. When done, report only: the number of signs per band, and the total.
