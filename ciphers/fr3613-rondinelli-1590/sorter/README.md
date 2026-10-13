# BNF-RONDI-SORT sorter inputs (13 Oct 2026, account 2, LANE BNF-FOCUS)
Blind sign sorter for BnF fr.3613 f.62r, cipher lines L01-L17 (crops: ../images/f62/). Built, not published.
`sh ciphers/fr3613-rondinelli-1590/sorter/build.sh OUTDIR` runs `cut.py` (tiles from the committed crops; the two overlapping segments of
each line are joined, tiles are ink groups from tools/sorter_recut.py, over-split a little on purpose), then tools/sign_sorter.py in its
default blind mode (no key, no value, no machine label; starting piles are 10 shape clusters) and tools/sorter_preflight.py.
Focus tiles (312) line up with a column where tx/passA.tsv and tx/passB.tsv differ (alignment is by position, so a few may be a neighbour).
The page asks: one pile per distinct sign, fix bad cuts, BAD-CUT for junk. Publish with capabilities {"db": {}}, eye the preflight contact
sheet, export, then `tools/sign_sorter_apply.py` turns the piles into settled labels for the next machine pass. ASKS 164.
