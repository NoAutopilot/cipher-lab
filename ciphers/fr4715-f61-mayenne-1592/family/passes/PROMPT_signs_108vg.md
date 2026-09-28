You are a blind transcriber of a 16th-century French cipher manuscript (BnF fr.3983 f.108v, Soissons, 28 Feb 1593, Duke of Mayenne to commander de Diou). You will list every CIPHER SIGN, left to right, in each of 7 line bands (the top seven cipher rows of the leaf). Each band is given as three overlapping image segments (s1 = left, s2 = middle, s3 = right, each 2300 px wide, scaled 2.0x from the native scan). The crops are cut per segment following the slope of the rows (each segment is cut at its own height, so the cipher row runs through the middle of every segment; the rows rise to the right). Neighbouring segments of a band OVERLAP by 160 px: the last 160 px of one segment show the same signs as the first 160 px of the next (red tick marks at the top edge mark the overlap zone). List a sign that falls in the overlap ONCE ONLY, in the earlier segment; in the next segment start listing after the red tick.

Each band contains: (a) a row of small ordinary handwriting (French clear words) written ABOVE the cipher row -- IGNORE these entirely, they are not signs; (b) the cipher row itself: a sequence of invented signs. A band may carry an ordinary clear word INSIDE the cipher row: list such a clear word as one row with sign = PLAIN and the word in the note. The rows are cramped: the small gloss words of the NEXT line may show at the bottom edge and the cipher row above may show at the top edge -- transcribe only the cipher row that runs through the middle of the band. Ordinary handwriting from a neighbouring line that intrudes at the very top or bottom of a band is not a sign.

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

Read the 21 images with the Read tool in this order: for each band L01..L07, segments s1, s2, s3:
  /home/user/cipher-lab/ciphers/fr4715-f61-mayenne-1592/family/sheets/f108vg_L01_s1.jpg  (then _s2, _s3, then L02_s1 ... L07_s3)
Write your transcription as a TSV file with the Write tool to the OUTPUT PATH given at the end of this prompt, header exactly:
line	pos	sign	conf	segment	x_px	note
one row per sign; 'line' is L01..L07; 'pos' counts from 1 within the band across both segments; 'x_px' is the sign's horizontal centre in pixels within its segment image; 'note' is free text (shape words, 'alt CODE', or the clear word for PLAIN). No letters of the alphabet are to be guessed for any sign: this is a shape transcription only. When done, report only: the number of signs per band, and the total.
