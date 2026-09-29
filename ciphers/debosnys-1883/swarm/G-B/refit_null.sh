#!/bin/bash
# Refit null (brief amendment 29 Sept 03:2x UTC): the same fitting command on the fit text with its sign order
# shuffled (fit_key.py --shuffle-seed), 50 refits, each scored held-out by score.py exactly like the real key.
# usage: refit_null.sh FIT TEST N  (e.g. c2 c1 50); 4 in parallel
cd "$(dirname "$0")"
FIT=$1; TEST=$2; N=${3:-50}
for i in $(seq 1 $N); do
  echo "python3 fit_key.py --text $FIT --shuffle-seed $i --seed $i --out refit/refit_${FIT}_$i.tsv >/dev/null && (cd .. && python3 score.py G-B/refit/refit_${FIT}_$i.tsv --fit $FIT --test $TEST > G-B/refit/refit_${FIT}_$i.json 2>&1)"
done | xargs -P 4 -I{} bash -c "cd .. && cd G-B && {}"
