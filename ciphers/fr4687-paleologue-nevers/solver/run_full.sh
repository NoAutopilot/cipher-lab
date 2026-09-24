#!/bin/sh
# Full-text rerun, 24 Sept 2026 (NOTES.md, "Full text: extras reconciled and solver rerun"). Same designs, guard
# (--kl 3, the default), restarts and seeds as run.sh, on signs_full.txt (900 signs); controls at --units 540,
# which gives 870-900 signs over the target's line lengths. Needs numpy. Models rebuilt from tools/data/it16.
set -e
cd "$(dirname "$0")"
T=../../../tools
W=${W:-${TMPDIR:-/tmp}/fr4687_it16}; mkdir -p "$W" runs_full
[ -f "$W/it16_all.npz" ] || {
  python3 $T/italian16_corpus.py $T/data/it16/*.txt --out "$W/it16_all.txt"
  awk 'NR%10!=3' "$W/it16_all.txt" > "$W/it16_train.txt"
  python3 $T/italian_ngram.py build "$W/it16_train.txt" --out "$W/it16_train.npz"
  python3 $T/italian_ngram.py build "$W/it16_all.txt" --out "$W/it16_all.npz"; }
python3 make_signs_full.py --check
S=$T/seg_homophonic.py
for n in 0 0.05 0.10 0.15; do
  python3 $S control --plain control_heldout.txt --model "$W/it16_train.npz" --cipher signs_full.txt \
    --units 540 --seeds 5 --restarts 5 --noise $n --design 12:letter > runs_full/control_12letter_n$n.txt &
done
wait
python3 $S control --plain control_heldout.txt --model "$W/it16_train.npz" --cipher signs_full.txt \
  --units 495 --seeds 5 --restarts 5 --noise 0.05 --design 12:null > runs_full/control_12null_n0.05.txt &
python3 $S solve --cipher signs_full.txt --model "$W/it16_all.npz" \
  --designs 12:letter,12:null,1:letter,2:letter --restarts 6 --nulls 3 --out runs_full/target > runs_full/target_solve.txt &
python3 $S solve --cipher signs_full.txt --model "$W/it16_all.npz" --designs 12:letter \
  --restarts 6 --nulls 4 --null-kind units --out runs_full/target_unitnull > runs_full/target_unitnull.txt &
wait
