# BKLOG-0507 per-page reconciliation (7 Oct 2026); RUN6-BIR3637's prompt_R.md, one page per call

Two blind readers matched the cipher signs of manuscript rows (BnF fr.3252, page v36mid) to cells of a sign sheet and disagreed at
the 52 positions in `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f3637/bypage/in_v36mid.tsv`. For EACH row there, open the crop the segment hint names, find the sign, and decide by shape.

Read ONLY: that TSV, the sheet `/home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/sign_sheet_blind.png`, and the crops
`/tmp/claude-0/-home-user-cipher-lab/080ba8c5-7dff-59c8-bc34-d57a34f05895/scratchpad/crops/<line>_s1.png .. _s4.png` (non-overlapping left-to-right segments of one row, 2x; the clerk's small letters sit in the band
above; read only the large signs of the main line in the lower middle). Open no other file. The sheet gives no values; decide by
shape only. You must open every crop the hints point to (a neighbour segment too if the context is not there); a row you did not
look at is '?'. Locate the position with the left/right context (neighbour sign ids; '?' = unsettled) and the "pos k of n" hint.
For each candidate pair, compare the sign in the crop against BOTH candidate cells on the sheet before choosing.

Write `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f3637/bypage/out_v36mid.tsv` with header `line	pos	choice	conf	note` (one row per input row, same line/pos): choice = cand_1's id, cand_2's id,
another cell id (say why in note), NONE (no sign there), or ? if you cannot decide; conf H/M/L; note at most six words, naming the
shape feature that decided. Reply with only the row count and how many crops you opened.
