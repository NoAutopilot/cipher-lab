BLIND TRANSCRIPTION PASS of a 1628 letter-cipher page (7 line crops). Work alone: read NO other file in the
repository, look at no key, no other transcription, no NOTES. Only the 7 images listed below.

Images (read each with the Read tool, in order):
  /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/lc_L01.jpg
  /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/lc_L02.jpg
  /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/lc_L03.jpg
  /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/lc_L04.jpg
  /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/lc_L05.jpg
  /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/lc_L06.jpg
  /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/lc_L07.jpg
Each crop holds one manuscript line (a crop may show a sliver of the neighbouring line at its top or bottom edge;
transcribe only the line centred in the crop). Line ids: L01 ... L07 from the file names.

The page is a cipher written in single signs that mostly look like Latin minuscule letters, digits and a few
other shapes. Line L01 begins with three words in CLEAR Latin, then the cipher starts.

Labelling convention (follow exactly, so that two independent readers' labels are comparable):
- One row per sign, in reading order. Label a sign by the lowercase Latin letter or digit it most resembles
  (a b c d e f g h i k l m n o p q r s t u x y z, 0-9). Use an uppercase letter only if the sign is clearly a
  capital form.
- Shapes that are not a Latin letter or digit: use these names -- lambda (inverted V / Greek capital lambda),
  delta (triangle), sqx (square with a diagonal or cross inside), phi (circle crossed by a vertical stroke),
  mu (Greek mu, an m/u with a descender on the left), longs (long s), z3 (a z with a 3-like descender tail),
  plus (+ / cross). For any other shape invent a short lowercase name and define it in the legend file.
- A superscript mark or abbreviation stroke above a sign: put it in the sign label after a caret, e.g. y^m.
- Word gaps: a row with sign "/" between words (conf H).
- Clear Latin words: one row per clear word with the sign written as [clear:word] (e.g. [clear:nobis]).
- A final period or dot: a row with sign "." only if it is clearly written.
- Confidence per sign: H (sure), M (probable), L (guess). If two readings are plausible, give the more likely as
  the sign and the other in the note column.

Output: write a TSV file (tab-separated, header line exactly as shown) to /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/passA_opus.tsv:
line	pos	sign	conf	note
L01	1	[clear:Mittatur]	M	
...
Positions restart at 1 on each line; "/" rows take positions too. Also write a short legend (any invented sign
names, one per line, with a description) to /home/user/cipher-lab/ciphers/riksarkivet-r4282-1628/gaps92/legendA.txt. Then reply with: rows written per line, count of H/M/L
signs, and the invented names. Nothing else.
