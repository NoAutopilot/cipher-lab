#!/bin/bash
# Reproduces LANE R6 Y8's first cheap test (25 Sept 2026). Run from the repo root.
# Needs tools/data/es17/*.txt.gz decompressed to plain text first (homophonic_anneal.py has no gzip support).
set -e
cd "$(git rev-parse --show-toplevel)"
tmp=$(mktemp -d)
zcat tools/data/es17/donquijote00cervuoft.txt.gz > "$tmp/donquijote.txt"
zcat tools/data/es17/vidadelbuscn01quevuoft.txt.gz > "$tmp/buscon.txt"

echo "=== target, marks as separate symbols, N=521 K=38 ==="
for s in 2 3 5; do
  python3 tools/homophonic_anneal.py ciphers/espagnol142-mercy-1648/cipher_codes.tsv \
    --corpus "$tmp/donquijote.txt" --corpus "$tmp/buscon.txt" --skip NONE \
    --seed "$s" --restarts 8 --iters 40000 | head -1
done

echo "=== matched control, same N/K, 5 seeds ==="
for s in 1 2 3 4 5; do
  python3 tools/homophonic_anneal.py --control "$tmp/donquijote.txt" --signs 38 --length 521 \
    --corpus "$tmp/donquijote.txt" --corpus "$tmp/buscon.txt" --seed "$s" --restarts 8 --iters 40000 | head -1
done

rm -rf "$tmp"
# Expect: target best score ~-1154 (reproducible across seeds 2,3,5,7); control scores ~-1322 to -1357.
