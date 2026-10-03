# Sign sorter (3 Oct 2026, GAPS138, account-4)

The owner's page: https://claude.ai/artifact/6MT1CLAbNx3iTMpa1yzSCJ (private to the owner; db capability). ASKS row 119.
9 tiles around the three positions in `../tx2/focus.tsv` (all three in "Check these first"): L02.3 (dotted stem, no
bar), L02.2+ (the speck below-right of S10's foot), L01.5-6 (open P and the dot as one tile, S3+S4 vs S18), plus
reference tiles L01.4 (S2 with its bar), L01.5 S3, L01.6 S4, L01.7 S5, L02.1 S9, L02.2 S10.

Boxes in `signs.tsv` are ink-component cuts from `ink_boxes.py` (background-subtracted threshold on
images/MLH-Cryptogram.jpg, connected components, read off by position and size against the reconciled stream), not
eye-checked -- no vision call was made. A tile cut wrong is marked BAD-CUT on the page.

    python3 tools/sign_sorter.py --signs ciphers/mlh-1976/sorter/signs.tsv --labels ciphers/mlh-1976/sorter/labels.tsv \
      --pages ciphers/mlh-1976/images --focus ciphers/mlh-1976/tx2/focus.tsv --title "MLH Sign Sorter" \
      --out <scratch>/mlh-sign-sorter.html --data-out ciphers/mlh-1976/sorter/sorter_data.json

Republish to the URL above (`url=`). After the owner sorts: export the db collections (piles, moves, newpiles) with
ArtifactData list ... out_dir=DIR, then `python3 tools/sign_sorter_apply.py --labels ciphers/mlh-1976/sorter/labels.tsv
--db DIR --out ciphers/mlh-1976/sorter/settled_labels.tsv`, and carry the three answers into tx2/ciphertext_reconciled.tsv.
