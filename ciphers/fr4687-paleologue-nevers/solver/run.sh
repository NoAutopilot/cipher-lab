#!/bin/sh
# Reproduces the joint-segmentation solver runs of 24 Sept 2026 (NOTES.md, "Joint-segmentation solver").
# Needs numpy. Models are rebuilt from tools/data/it16 (not committed, 14 MB each).
set -e
cd "$(dirname "$0")"
T=../../../tools
W=${TMPDIR:-/tmp}/fr4687_it16; mkdir -p "$W" runs
python3 $T/italian16_corpus.py $T/data/it16/*.txt --out "$W/it16_all.txt"
awk 'NR%10==3' "$W/it16_all.txt" > control_heldout.txt
awk 'NR%10!=3' "$W/it16_all.txt" > "$W/it16_train.txt"
python3 $T/italian_ngram.py build "$W/it16_train.txt" --out "$W/it16_train.npz"
python3 $T/italian_ngram.py build "$W/it16_all.txt" --out "$W/it16_all.npz"
python3 structure.py > runs/structure.txt
for n in 0 0.05 0.10 0.15; do
  python3 $T/seg_homophonic.py control --plain control_heldout.txt --model "$W/it16_train.npz" --cipher signs.txt \
    --units 360 --seeds 5 --restarts 5 --noise $n --design 12:letter > runs/control_12letter_n$n.txt
done
python3 $T/seg_homophonic.py control --plain control_heldout.txt --model "$W/it16_train.npz" --cipher signs.txt \
  --units 330 --seeds 5 --restarts 5 --noise 0.05 --design 12:null > runs/control_12null_n0.05.txt
python3 $T/seg_homophonic.py solve --cipher signs.txt --model "$W/it16_all.npz" \
  --designs 12:letter,12:null,1:letter,2:letter --restarts 6 --nulls 3 --out runs/target > runs/target_solve.txt
python3 $T/seg_homophonic.py solve --cipher signs.txt --model "$W/it16_all.npz" --designs 12:letter \
  --restarts 6 --nulls 4 --null-kind units --out runs/target_unitnull > runs/target_unitnull.txt
python3 $T/seg_homophonic.py solve --cipher runs/control_cipher_n0.1.txt --model "$W/it16_train.npz" \
  --designs 12:letter --restarts 6 --nulls 4 --null-kind units --out runs/ctl_unitnull_n0.1 > runs/ctl_unitnull_n0.1.txt
python3 $T/seg_homophonic.py solve --cipher signs_ab.txt --model "$W/it16_all.npz" --designs 12:letter,12:null \
  --restarts 6 --nulls 3 --null-kind units --out runs/target_ab > runs/target_ab.txt
