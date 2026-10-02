#!/bin/sh
# NEVBIR-117C: same test as ../run_tests.sh on the 2-of-3 transcription la/recon_f117_3r.tsv, power at the TWO-READER
# error (0.25, never the 2-of-3 residual). Run from harvest/f117:  sh la/run_tests_3r.sh 0.25
set -e
ERR=${1:-0.25}
G=../../../ceppo-nevers-fr3251-1570s/harvest
N=../../../nevers-birago-fr3251-1572/harvest
for v in printed T42m clerkvar T88q; do
  python3 $G/decode_control.py la/recon_f117_3r.tsv --map map_$v.json --corpus fr --err $ERR --seed 1 --out la/reading_3r_$v.txt > la/test_3r_$v.txt
  echo "== $v"; tail -2 la/test_3r_$v.txt
done
for v in printed T88q; do
  echo "judge $v:"; python3 $N/shuffled_judge.py ../../../../specs/birago-fr3252-f117.json map_$v.json la/recon_f117_3r.tsv --seeds 20 --real | tail -4
done
