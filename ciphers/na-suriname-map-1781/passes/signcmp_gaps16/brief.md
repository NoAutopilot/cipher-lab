# Blind sign comparison (GAPS16-na-suriname-map-1781, account-4, 2 Oct 2026)

Queries: 2061 battery-list lines L04, L06, L10 (tools/iiif_lines.py --image images/2061_battery_legend_native.jpg --centres
79,124,182,229,331,375,496,553,640,726 --only-lines 4,6,10 --max-width 1300 --overlap 200), renamed Q1a/b, Q2a/b, Q3a/b.
References: GAPS15's value-blind sheet passes/signcmp_gaps15/blind_refs.jpg (29 tiles R1-R29 from the Nieuw Secreet sheet,
inv86 scan 0003, with look-alikes: G 9, L g, P q, M y, N ij, D tall v, I 8, S 6, ...; mapping in
passes/signcmp_gaps15/blind_key.json). The subagent was told only "handwritten signs": no letters, values or repo files.
Targets (10 tokens, 2061 L04:10 y, L04:15/21/24/37/39 g, L06:18/22 y, L10:11 y, L10:21/26/29 g) are not named to the call:
it reports every sign with a descender, so look-alikes (q, p, f, psi, ...) are mixed in by construction.
Settle rule, stated before mapping back (same as GAPS15): a token's identity changes only when best conf >= 0.6 and the
runner-up carries a different value; the mapping from the call's ordinal positions to tokens is accepted only when the
call's neighbour shapes agree with the transcription.

## Prompt given to the call
You are comparing handwritten signs by shape only. Files in SCRATCH/sg16/: refs.jpg is a sheet of 29 reference sign tiles,
each labelled R1..R29 above it. Q1a.jpg + Q1b.jpg are one line of handwriting cut into two overlapping segments (about 200 px
overlap: do not count the overlapping signs twice); likewise Q2a+Q2b and Q3a+Q3b. Read each image with the Read tool.
For each query line, go left to right and number every separate sign 0, 1, 2, ... (every letter-like sign, digit or symbol
counts as one; an abbreviation like "No" counts as one; ignore punctuation and ruled lines). Then, for EVERY sign that has a
stroke going clearly below the writing line (a descender), report one row:
line (Q1/Q2/Q3), index, a short shape description, the shapes of the sign before and after it, the best-matching
reference tile, a confidence 0-1, the second-best reference tile, its confidence.
Also say which reference tiles you think are the same sign as each other, if any. Write the rows as a TSV to
SCRATCH/sg16/result.tsv (header: line index shape before after best conf second conf2) and reply with the row count.
