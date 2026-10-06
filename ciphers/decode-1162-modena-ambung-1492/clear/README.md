# Clear text of DECODE R1162 (R10-DEC1162, 6 Oct 2026)

- `clear_text.tsv`: reconciled diplomatic transcription, one row per line; `crop` + `crop_row` locate the line in
  `../images/clear/` (row a = upper line of the crop). Abbreviations kept: `^` superscript, `~` tilde/macron, `p_` p with
  stroke; `?` after a doubtful word; `[?]` unread; `{p1L05_1}` = cipher group by its `ciphertext.tsv` id.
- `p1_passA.tsv`, `p2_passA.tsv`: the blind Sonnet pass, crops only, as returned.
- Reconciliation was not blind (DECODE doc 3593, gloss and cipher reading seen). See NOTES.md "## R10-DEC1162".
- `p1_passB.tsv`, `p2_passB.tsv` (R10-DEC1162B, 6 Oct 2026): a second blind Sonnet pass, crops only, as returned (cipher runs as
  {CIPHER}). `doubts_R10B.tsv`: one row per doubtful word of the R10-DEC1162 text with passA, passB, the crop verdict
  (settled / settled-word / stays / read-doubtful / RAISED) and the text now in `clear_text.tsv` (column `r10b` logs each change).
