# RUN6-BIR3637 reconciliation (5 Oct 2026)

Two blind readers matched the cipher signs of 22 manuscript rows (BnF fr.3252 f.36r, f.36v, f.37r) to cells of a sign sheet and
disagreed at the 193 positions in `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f3637/adjudicate_in.tsv`. For each row there, look at the sign in the crop and decide.

Read ONLY: that TSV, the sheet `/home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/sign_sheet_blind.png`, and the crops
`/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36/crops/<line>_s1.png .. _s4.png` (non-overlapping left-to-right segments of one row, 2x; the clerk's small letters sit in
the band above; read only the large signs of the main line in the lower middle). Open no other file. The sheet gives no values;
decide by shape only. Open only the crops the TSV's segment hints point to (and a neighbour segment if the context is not there).
Locate the position with the left/right context (the reconciled sign ids of the neighbours; '?' = unsettled) and the segment hint.

Write `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f3637/adjudicate_out.tsv` with header `line	pos	choice	conf	note` (one row per input row, same line/pos): choice =
cand_1's id, cand_2's id, another cell id (say why in note), NONE (no sign there), or ? if you cannot decide; conf H/M/L; note at
most six words. Reply with only the row count.
