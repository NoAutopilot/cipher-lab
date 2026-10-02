# Revol-hand sign sorter (GAPS5, 2 Oct 2026)

The owner's page: https://claude.ai/artifact/L2LvyN17GRK4XWwxiBGAFb (private to the owner; ASKS row 102).
1,018 tiles, every ink piece on the 23 cipher-bearing lines of BnF fr.3986 f.198 (Gallica btv1b9060631k, canvas 395 recto,
397 verso), in 41 provisional piles by image likeness (c01-c40, `wide`). No reader label is attached (the passes give no
positions; NOTES.md "GAPS5"). Clear-French letters are on these lines too: the owner marks them not-a-letter.

Rebuild (from the repository root; the HTML is not committed):

    python3 ciphers/fr3986-nevers-revol-1593/sorter/stitch_lines.py
    python3 ciphers/fr3986-nevers-revol-1593/sorter/build_tiles.py <scratch dir>
    cd ciphers/fr3986-nevers-revol-1593/sorter && python3 ../../../tools/sign_sorter.py --signs signs.tsv \
      --labels labels.tsv --pages lines --focus focus.tsv --title "Revol Hand Sign Sorter" --out <scratch>/revol-sign-sorter.html

then publish to the URL above with capabilities {"db": {}}. After the sort: export piles/moves/newpiles with ArtifactData
`list ... out_dir=DIR`, then `python3 tools/sign_sorter_apply.py --labels ciphers/fr3986-nevers-revol-1593/sorter/labels.tsv
--db DIR --out ciphers/fr3986-nevers-revol-1593/sorter/settled_labels.tsv --summary .../summary.json`; next, two blind
passes against the settled Revol-hand list (~$8).
