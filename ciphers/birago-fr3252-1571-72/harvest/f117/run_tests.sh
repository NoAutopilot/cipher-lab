#!/bin/sh
# f.117r first test (NEVBIR-3252-B, 2 Oct 2026): decode + 200-shuffle control + power control at the measured two-reader
# error, for the printed 1572 key, the T42=m variant and the C-grade clerk variant; then judge (fr16) and shuffled-target
# judge.  sh run_tests.sh ERR   (run from this folder; writes test_*.txt)
set -e
ERR=${1:-0.12}
G=../../../ceppo-nevers-fr3251-1570s/harvest
N=../../../nevers-birago-fr3251-1572/harvest
for v in printed T42m clerkvar; do
  python3 $G/decode_control.py recon_f117.tsv --map map_$v.json --corpus fr --err $ERR --seed 1 --out reading_f117_$v.txt > test_$v.txt
  tail -2 test_$v.txt
done
for v in printed T42m clerkvar; do
  echo "judge $v:"; python3 $N/shuffled_judge.py ../../../../specs/birago-fr3252-f117.json map_$v.json recon_f117.tsv --seeds 20 --real | tail -4
done
