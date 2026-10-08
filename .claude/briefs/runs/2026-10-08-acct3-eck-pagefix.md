# ECK-PAGEFIX (account 3 parent, 8 Oct 2026): Eckert mssEC 19 page numbers from the holder's titles

Model Sonnet. Cap USD 2, box 40 min. One job; stop when met (CLAUDE.md Usage 7).

Why: PROP-HUNT (8 Oct 2026, ciphers/eckert-1864/NOTES.md "## PROP-HUNT: record corrections") found that the page column of
`ciphers/eckert-1864/entries-mssEC19.tsv` is pointer minus 8892, which runs 1 high from pointer 9031 and 2 high from 9048
because the Huntington's own page titles repeat Page 138 and Page 154. E122/E123 are already fixed. 29 headers remain (list
in that section): E55, E56, E63, E64, E73, E74, E76, E77, E103, E105, E120, E121, E124, E125 (ciphertext.txt); N2-BU, N2-BV,
N2-BW, N2-BX, N2-BY, N2-CA, N2-CB, N2-CF, N2-CG, N2-CH, N2-CI, N2-CJ, N2-CK, N2-DB, N2-EA (ciphertext-no2.txt).

Steps:
0. `python3 tools/room.py "ECK-PAGEFIX (worker, account 3)" "claim: eckert-1864 mssEC19 page column from holder titles" --push`.
1. Rebuild the page column of entries-mssEC19.tsv from the holder titles already on disk (sources/mssEC19/p<pointer>.json,
   field title "Page N"); no network. Report any pointer whose title is blank or not "Page N" rather than guessing.
2. Correct the 29 headers (and any other header the corrected column changes), regenerate the readings, and run
   `python3 ciphers/eckert-1864/decode.py --check`, `decode_no2.py --check`, `decode_no9.py --check` (all must exit 0).
3. Rename the four status.json document_ids (E74 p.179->177, E76 p.219->217, N2-BY p.234->232, E103 p.237->235) in
   document_id, documents and phrases; first grep the whole repo for each old string and change every live reference
   (AUDIT.md quotations of a past state stay as written, add "[page corrected ECK-PAGEFIX]" beside them instead). Also the
   E26 "p.161" line in research/PRIOR-WORK-LEAK-2026-10-08.tsv.
4. Confirm outreach/huntington-decipherments-list-2026-10-08.tsv is unaffected (none of the four is on it) -- report, do not edit.
5. `python3 tools/file_shrink_guard.py <every file touched>`, pull --rebase --autostash, commit by explicit path (attribution
   lines per the session's rules), push, ROOM done line, five-line report.
Do not decode anything new, do not classify novelty, do not touch other targets.
