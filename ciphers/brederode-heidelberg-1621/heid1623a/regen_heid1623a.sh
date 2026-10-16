#!/bin/bash
# HEID-1623A (16 Oct 2026): re-derive scans 166/171 at 1200 px, the 5 native regions and the line crops, then the tables and the
# alignment. Run from ciphers/oldenbarnevelt-brederode-1605. Usage: bash ../brederode-heidelberg-1621/heid1623a/regen_heid1623a.sh OUTDIR
# (8 service.archief.nl requests at >= 3.1 s; take/release lines in ROOM.md first; images stay outside git; sha1s in ../images/manifest.json heid_6022_1623a)
set -e; O=${1:-scratch_heid1623a}; D=../brederode-heidelberg-1621/heid1623a
python3 screen_tools/na_fetch.py 412b1414-afa2-42fe-b56d-2b5f705e5005 $O/i6022 1200 166 171
python3 $D/fetch_regions.py $O
python3 ../../tools/iiif_lines.py --image $O/u1_166_block.jpg --out $O/c_h166 --prefix h166 --debug
python3 ../../tools/iiif_lines.py --image $O/u2w_171_block.jpg --out $O/c_h171 --prefix h171 --debug
python3 ../../tools/iiif_lines.py --image $O/u3w_171_note.jpg --out $O/c_n171 --prefix n171 --debug
sha1sum $O/i6022/s0166_1200.jpg $O/i6022/s0171_1200.jpg $O/u*.jpg
(cd $D && python3 build.py --check)
(cd ../.. && python3 tools/interlinear_align.py align $D/pairs_1623.tsv $O/align_1623.tsv $O/align_key_1623.tsv --code-prefix @ --code-chunk 6 --wildcard '?' --keep-fs --shuffle 200 --seed 1623)
