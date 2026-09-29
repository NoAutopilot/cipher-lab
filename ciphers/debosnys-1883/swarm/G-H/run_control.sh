#!/bin/sh
# Known-answer control: blind pipeline on real Copiale windows at Debosnys sizes (all four ~1200, c2 ~770, c1 ~135),
# five windows per size spread through the 73k-token transcription, plus a token-order-shuffled null per window.
cd "$(dirname "$0")"
for n in 1200 770 135; do
  for st in 3000 15000 30000 45000 60000; do
    echo "python3 pipeline.py copiale --n $n --start $st --seed $st --out control/blind_n${n}_s${st}.json"
    echo "python3 pipeline.py copiale --n $n --start $st --seed $st --shuffle --out control/null_n${n}_s${st}.json"
  done
done | xargs -P 4 -I{} sh -c '{} >/dev/null'
