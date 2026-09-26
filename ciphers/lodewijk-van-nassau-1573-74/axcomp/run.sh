#!/bin/sh
# AX-COMP: regenerate pairs, alignment and key for letter $1 (4614, 7205) from ciphertext_$1.tsv + decipherment_$1.txt
set -e
cd "$(dirname "$0")/.."
python3 axcomp/build_pairs.py "$1"
python3 ../../tools/interlinear_align.py align axcomp/pairs_"$1".tsv axcomp/align_"$1".tsv axcomp/rawkey_"$1".tsv \
    --floor 121 --clear-consumes --prior key_full.tsv
python3 axcomp/keys.py "$1"
