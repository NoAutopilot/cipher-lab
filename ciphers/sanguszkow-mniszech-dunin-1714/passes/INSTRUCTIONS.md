BLIND TRANSCRIPTION PASS -- numerical cipher, 1714 Polish letter, 300 dpi line crops.

You are one of two independent blind readers. Do NOT look for, open, or read any other transcription of this
document (no other pass file, no file under ciphers/, no web search, no git log): read only the crop images listed
below, one by one, with the image reader, and write what you see.

What the lines contain: cipher groups of 2 or 3 digits (range about 12 to 157), each group followed by a point
("110.36.31.157.") and sometimes a wider gap; interspersed with clear-text words in Latin/Polish cursive
(e.g. "praetextu consilii", "Congressow"). Some lines begin with a short "=" hyphenation mark at the left margin
(a continuation mark, not a sign) and some end with a stroke "/" or "=" (also not a sign). An 18th-century "1" is
written with a long foot like "A" or "J"; a "7" has a crossbar; a "4" is open; "5" and "3" can look alike;
"0" and "6" can look alike. Read every digit yourself from the pixels -- never infer a group from a group that
looks similar elsewhere.

OUTPUT: write ONE tab-separated file at the path given below, header line exactly:
line	pos	sign	conf
then one row per token, in reading order, left to right, per crop:
  line  = the crop's line id (e.g. p1_L01)
  pos   = 1, 2, 3 ... within the line
  sign  = a cipher group's digits only (no point), e.g. 110 ; or a clear word as [PLAIN:word] (one token per
          clear word, spelled as you read it; a punctuation mark in the clear is left out)
  conf  = H (certain), M (fairly sure), or L (a guess). If you hesitate between two readings of a group write
          the first choice in sign and mark conf M or L, and add the alternative in a fifth column "alt"
          (header: line	pos	sign	conf	alt) -- the alt column may be empty for other rows.
Each point-separated group is one token: "107.101." is two tokens 107 and 101. If two groups appear to run
together without a point, write them as one token and mark conf L.
Do not skip any crop. Do not merge or re-cut crops. After writing the file, reply with only: the file path, the
number of rows, and the number of rows marked M or L. No other output, no commentary on what the cipher might mean.
