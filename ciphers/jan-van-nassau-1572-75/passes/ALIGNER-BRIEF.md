# Aligner brief (LANE R2 worker J1, 24 Sept 2026)

You transcribe the numeral cipher of one Willem van Oranje letter (to Jan van Nassau, 1575, French) and align each
cipher group with the plaintext Groen van Prinsterer printed for it. The printed plaintext is in the same PDF
(bundled print pages). The cipher is a numeral nomenclator: groups separated by dots, values 1-~350; low values are
probably letters (homophones), higher values may be syllables or whole words (names, "que", "duc"...), and some may be
nulls. Clear French text runs between cipher runs.

Images: ciphers/jan-van-nassau-1572-75/images/<briefnr>_p<N>.jpg (150 dpi). Zoom with
`python3 ciphers/jan-van-nassau-1572-75/crop.py IMG OUT.png --yfrac 0.40 0.50 --xfrac 0.2 1 --scale 2` (write OUT to
/tmp/<yourname>/). Read digits only from zoomed crops, never from the whole page. Do not use the network.

Output: ciphers/jan-van-nassau-1572-75/passes/align_<briefnr>.tsv, header
`page	line	idx	group	doubt	plain	note`
one row per cipher group, in reading order; `line` = manuscript line number on that page counting from the first
written line (1-based); `idx` = position of the group in that line (1-based); `group` = the number as written
(digits only; if unreadable write `?`; if you are unsure of a digit write your best reading and set doubt=1);
`plain` = the letter(s) or word of Groen's printed text that this group stands for, lower case, no accents
(`-` if the group looks like a null, `?` if you cannot place it); `note` free (e.g. "code for Hans Casimir?",
"print omits this passage", "print differs: ..."). Before the first group of each cipher run add one row with
group=`RUN` and plain = the clear words just before the run on the manuscript and the print's words for the whole run
(so a reader can check the span). Write the file incrementally: append the rows of each manuscript page as soon as
that page is done (one page at a time, to disk), so nothing is lost if you are interrupted.

Method: for each cipher run, first find the matching span in the print (the clear words before and after the run
anchor it), then write the plaintext letters of that span in order and assign cipher groups left to right. Where the
count does not match (a group standing for a syllable or word, a null, a print that paraphrases or omits with "....."),
say so in `note` and keep going; never invent plaintext the print does not have. If the print omits the passage
entirely, still transcribe every group with plain `?` and note "not printed".

Finish with a 5-line report: pages done, groups transcribed, groups aligned to plain, runs not printed, any
consistent value->letter pairs you noticed (e.g. "88 = e seen 5x"). Do not decode beyond the print, do not edit any
other file, do not commit (the worker commits).
