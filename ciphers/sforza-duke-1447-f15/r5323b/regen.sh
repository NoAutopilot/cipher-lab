#!/bin/sh
# SFZ-R5323B reader packets (images NOT committed). Needs ../r5323/regen.sh's output dir (DECODE PDFs + crops) as $1, and the
# Duke f.8 line crops on disk (../../sforza-italien1584-1447/duke/images/). Writes $2/{b1,b2,ex}: neutral sheet names per sheet_map.tsv.
set -e; IMG=$1; R=${2:-./readers}; H=$(cd "$(dirname "$0")" && pwd); mkdir -p "$R/b1" "$R/b2" "$R/ex"
python3 - "$H" "$IMG" "$R" <<'PY'
import json, shutil, sys
H, IMG, R = sys.argv[1:]
s = json.load(open(f'{H}/exemplars.json'))
G2 = ["N2", "#", "N11", "8", "N4", "D", "t", "l", "N1", "b"]
json.dump({k: s[k] for k in G2}, open(f'{R}/ex/g2.json', 'w')); json.dump({k: s[k] for k in s if k not in G2}, open(f'{R}/ex/g1.json', 'w'))
for l in open(f'{H}/sheet_map.tsv').read().split('\n')[1:]:
    if not l: continue
    sh, rec, b = l.split('\t'); r = rec[1:]
    if r == '5323':
        shutil.copy(f'{IMG}/c5323_left.png', f'{R}/b{b}/{sh}_part1.png'); shutil.copy(f'{IMG}/c5323_right.png', f'{R}/b{b}/{sh}_part2.png')
    else:
        shutil.copy(f'{IMG}/ctl_{r}.png', f'{R}/b{b}/{sh}.png')
PY
cd "$H"; python3 exemplar_sheet.py "$R/ex/g1.json" "$R/ex/exemplars_G1.png"; python3 exemplar_sheet.py "$R/ex/g2.json" "$R/ex/exemplars_G2.png"
cp labels_G1.md labels_G2.md "$R/ex/"
