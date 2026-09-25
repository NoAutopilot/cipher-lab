#!/bin/sh
# Reproduces LANE B2 worker bCPH's cheap test 1 for copenhagen-1835 (25 Sept 2026).
# Run from the repo root.
set -e
cd "$(dirname "$0")/../../.."
OUT=specs/cheap-tests/copenhagen-1835
CIPHER=$OUT/cipher.tsv

# target: anneal the 98-letter transcription against each language's corpus
python3 tools/homophonic_anneal.py "$CIPHER" --corpus tools/data/da19/historisktidsskriftdk1s6.txt \
  --restarts 8 --iters 40000 --seed 1 --skip DOT,COL --out $OUT/target_da_seed1.json
python3 tools/homophonic_anneal.py "$CIPHER" --corpus tools/data/de16/composed_enhg.txt \
  --restarts 8 --iters 40000 --seed 1 --skip DOT,COL --out $OUT/target_de_seed1.json
python3 tools/homophonic_anneal.py "$CIPHER" --corpus tools/data/pg1661_holmes.txt \
  --corpus tools/data/pg2701_mobydick.txt --restarts 8 --iters 40000 --seed 1 --skip DOT,COL \
  --out $OUT/target_en_seed1.json

# matched controls: same script, same N=98/K=23, 3 seeds each, real plaintext of the same language
# enciphered and solved blind
for seed in 1 2 3; do
  python3 tools/homophonic_anneal.py --control tools/data/da19/historisktidsskriftdk1s6.txt \
    --corpus tools/data/da19/historisktidsskriftdk1s6.txt --signs 23 --length 98 \
    --restarts 8 --iters 40000 --seed $seed --out $OUT/control_da_seed${seed}.json
  python3 tools/homophonic_anneal.py --control tools/data/de16/composed_enhg.txt \
    --corpus tools/data/de16/composed_enhg.txt --signs 23 --length 98 \
    --restarts 8 --iters 40000 --seed $seed --out $OUT/control_de_seed${seed}.json
  python3 tools/homophonic_anneal.py --control tools/data/pg1661_holmes.txt \
    --corpus tools/data/pg1661_holmes.txt --corpus tools/data/pg2701_mobydick.txt --signs 23 --length 98 \
    --restarts 8 --iters 40000 --seed $seed --out $OUT/control_en_seed${seed}.json
done
