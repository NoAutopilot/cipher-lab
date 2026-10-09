# Third-reader adjudication, fr.3252 f.117r (TXE-R, 9 Oct 2026). VALUE-BLIND.

Two independent readers transcribed the cipher signs of a 16th-century letter by matching each hand-drawn sign to a cell of
the blind sign sheet (cells T10..T98). You settle the positions where they disagree, or where both were unsure, from the
images. You do not know, and must not look up, what any sign means.

Open ONLY: this brief; `adjudicate_queue.tsv` (beside it); the sign sheet
`/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f117/sign_sheet_blind_1572.png`; and the crops named in the
queue's `crops` column, in `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/images/f117_txer/lines2x/`. Open no other file.

Crops: one manuscript line per crop, upscaled 2x; L01-L09 in three segments s1, s2, s3 left to right whose edges overlap by
150 px (about one sign, read it once); L10 one crop. Transcribe only the line in the middle of the crop.

Each queue row: `line`, `col` (the sign's position counted from the line start), `reader1` and `reader2` (each reader's cell;
`-` = that reader saw no sign there; X_NEW / X_S / X_K / X_EQ = no matching cell), `left_neighbours` / `right_neighbours`
(the signs both readers agreed on just before and after: use them to find the spot), `segment` (approximate).
For each row, find the sign, compare it with the sheet, and decide.

Output: write exactly one TSV, `/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f117/txer/adjudication.tsv`, header

    qid	choice	sign	conf	note

- `choice`: `1` (reader1 is right), `2` (reader2 is right), `other` (a different cell, put it in `sign`), `none` (no sign
  at this spot, for a `-` row), `unsure`.
- `sign`: the cell you settle on (T##, X_NEW, X_S, X_K, X_EQ), blank for none.
- `conf`: H clear, M plausible, L guess.  `note`: a few words on the deciding feature (bar count, dot, foot, loop, lean).
One row per queue row, 45 rows. Do not decode or guess at meanings. Report in a short paragraph: counts of 1 / 2 / other /
none / unsure, and the cell pairs that were hardest.
