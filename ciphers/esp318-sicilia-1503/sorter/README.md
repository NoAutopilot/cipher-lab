# Sicily 1503 sign sorter (FT4b, 3 Oct 2026)

The owner's page: https://claude.ai/artifact/92bH8f981H2M95JNM3PVBL (private to the owner; ASKS row 104).
1,937 tiles, every ink piece on the 33 lines of BnF Espagnol 318 no. 94, f.120r (Gallica btv1b52503046q, canvas 452),
in 40 provisional piles by image likeness (c01-c40; one piece in `wide`). No reader label is attached: the two FT4
passes give line and position but no x coordinate, and the lines mix clear Spanish, code groups and single signs
(build_tiles.py docstring). Clear-Spanish letters are on these lines too: the owner marks them not-a-letter.
"Check these first": 40 tiles, one per (reader A, reader B) tag pair the passes split on, commonest first
(`?x`/`r1` 62x, `a4`/`?p` 51x, ...), each placed by proportional position, so the split sign is that tile or a neighbour.

Rebuild (from the repository root; neither the HTML nor the line images are committed -- both regenerate from
images/src_ark_12148_btv1b52503046q_f452_full.jpg and images/manifest.json):

    python3 ciphers/esp318-sicilia-1503/sorter/build_tiles.py <scratch dir>
    cd ciphers/esp318-sicilia-1503/sorter && python3 ../../../tools/sign_sorter.py --signs signs.tsv \
      --labels labels.tsv --pages <scratch dir>/lines --focus focus.tsv --title "Sicily 1503 Sign Sorter" \
      --out <scratch>/sicily-sign-sorter.html

then publish to the URL above with capabilities {"db": {}}. After the sort: export piles/moves/newpiles with ArtifactData
`list ... out_dir=DIR`, then `python3 tools/sign_sorter_apply.py --labels ciphers/esp318-sicilia-1503/sorter/labels.tsv
--db DIR --out ciphers/esp318-sicilia-1503/sorter/settled_labels.tsv --summary ciphers/esp318-sicilia-1503/sorter/summary.json`;
next, two blind passes of f.120r against the settled list (~$3), then ff.120v-121v.
