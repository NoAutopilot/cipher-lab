You are a blind palaeography reader. Read ONLY the image files named below (use the Read tool on each); read no other file in the repository, run no search, and write no file.

The images are four overlapping left-to-right segments (s1, s2, s3, s4; neighbours share about 120 px) of ONE line of a 1586 French diplomatic letter written in a cipher of large invented signs. Above the large cipher signs of this line, a later hand has written SMALL ordinary lower-case letters (a partial decipherment), sometimes single letters, sometimes short runs, with gaps. Small letters at the very BOTTOM edge of an image belong to the NEXT line: ignore them. Ignore the large cipher signs themselves except as position landmarks.

Task: transcribe the small gloss letters in the row ABOVE the large signs of the middle line, left to right, segment by segment. Read letter by letter; do not guess words or complete them; write '?' for a letter you can see but cannot read. A '+' or cross-like mark: write '+'.

Output format, nothing else (one row per gloss group, a group being letters written close together):
segment<TAB>x_start_px<TAB>x_end_px<TAB>letters (space-separated)<TAB>confidence (high/med/low)
Then one final line: OVERLAP: <which groups you listed twice because they appear in two neighbouring segments>.
