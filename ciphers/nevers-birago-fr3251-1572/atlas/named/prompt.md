You are naming clusters of handwritten cipher-sign tiles (16th-century Italian/French letters, a symbol cipher). Read two images:
1. REFERENCE: /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png -- the cipher's printed sign table, each cell labelled with an ID (T10 ... T98). No values are given and none are wanted.
2. SHEET: {SHEET} -- one row per cluster, labelled C<n> at the left, then up to 10 tiles cut from the manuscript (the first five are the most typical, the rest spread across the cluster).

For each row decide what the tiles are:
- one ID from the reference if at least 7 of the visible tiles are clearly that sign (handwriting varies; match the shape, strokes and loops, not exact size);
- "_" if most tiles are ordinary handwriting (Latin-alphabet letters/words of prose), page edges, blots, blanks or fragments, not cipher signs;
- "MIXED" if the tiles are cipher signs but of two or more different IDs, with no single ID on 7 or more.
Also give the second most likely ID (or "-"), and a confidence H/M/L.

Do not look at any other file. Answer ONLY with lines of TSV, no header, no commentary:
C<n><TAB>answer<TAB>second<TAB>conf<TAB>short note (max 8 words)
