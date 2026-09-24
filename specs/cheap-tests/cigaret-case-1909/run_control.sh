#!/bin/sh
# Regenerates the 80/20 Faust train/holdout split and reruns the matched control
# (rule 3: German plaintext, N=45, K=18, same solver, 3 seeds) for cigaret-case-1909's
# cheap test 1. See specs/cigaret-case-1909.json cheap_test_done for the numbers this produced.
set -e
python3 -c "
t = open('goethe_faust_2229.txt', encoding='utf-8').read()
n = len(t); split = int(n*0.8)
open('faust_train.txt','w',encoding='utf-8').write(t[:split])
open('faust_holdout.txt','w',encoding='utf-8').write(t[split:])
"
for seed in 1 2 3; do
  python3 ../../../tools/homophonic_anneal.py --control faust_holdout.txt --signs 18 --length 45 \
    --corpus ../../../tools/data/de16/composed_enhg.txt --corpus faust_train.txt --seed "$seed"
done
rm -f faust_train.txt faust_holdout.txt
