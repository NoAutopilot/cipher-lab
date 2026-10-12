#!/bin/bash
# TXE4-2: the read-free tile pipeline, end to end, into TILE_DIR (the registered run is tiles/; tiles_x/ is the post-registration
# read-free exploration with --split-wide, which prices the next step and is NOT a result). Usage:
#   bash run_tiles.sh TOOLS_DIR TILE_DIR [extra segment args, e.g. --split-wide 1.3]
set -e
TOOLS=$1; TD=$2; shift 2; EXTRA="$@"
HERE=$(cd "$(dirname "$0")" && pwd); cd "$HERE/../../.."
IMG=ciphers/fr3621-dinteville-1592/images
mkdir -p "$HERE/$TD"
ARGS=""; for seg in L02_s1 L04_s2 L05_s1 L07_s1 L07_s2 L08_s1 L08_s2 L09_s1 L09_s2 L10_s1 L10_s2 L11_s1; do ARGS="$ARGS --page f130_$seg=$IMG/f130_$seg.jpg"; done
python3 $TOOLS/glyph_atlas.py segment $ARGS --out "$HERE/$TD/atlas" --median-h pool $EXTRA
# f130_L02_s1 at its own median (the PREREG addendum's declared deviation), merged in
python3 $TOOLS/glyph_atlas.py segment --page f130_L02_s1=$IMG/f130_L02_s1.jpg --out "$HERE/$TD/atlas_l02" $EXTRA
python3 "$HERE/merge_l02.py" "$HERE/$TD"
rm -rf "$HERE/$TD/atlas_l02"
python3 "$HERE/middle_row.py" "$TD"
mkdir -p "$HERE/$TD/reads"; cp "$HERE/tiles/reads/wideA.tsv" "$HERE/tiles/reads/wideB.tsv" "$HERE/$TD/reads/"
python3 tools/reconcile_passes.py "$HERE/$TD/reads/wideA.tsv" "$HERE/$TD/reads/wideB.tsv" --method nw --keep-dots --out-dir "$HERE/$TD/reads" | grep -E "^lines"
python3 "$HERE/line_reads.py" "$TD"
T="$HERE/$TD"
python3 $TOOLS/box_token_align.py --signs $T/line_signs.tsv --read $T/read.tsv --read-alt $T/read_alt.tsv --lam 0 --keep-pos $T/keep.tsv --count-tol 0.10 --tokens-out $T/r1_tokens.tsv --out $T/r1_map.tsv --lines-out $T/r1_lines.tsv
python3 $TOOLS/glyph_atlas.py cluster --out $T/atlas --k 40 --pca-scale shared | tail -1
echo '{"signs": {}, "marks": {}, "desc": {}}' > $T/labels_empty.json
python3 - "$T" <<'PY'
import csv, sys; T=sys.argv[1]
rows=list(csv.DictReader(open(f'{T}/r1_tokens.tsv'),delimiter='\t'))
open(f'{T}/r1_train.tsv','w').write('sid\tcode\n'+''.join(r['sid']+'\t'+r['label']+'\n' for r in rows))
PY
python3 $TOOLS/glyph_atlas.py classify --out $T/atlas --labels $T/labels_empty.json --train-labels $T/r1_train.tsv --only-train-labels --page all --knn 5 --topk 3 --pca-scale shared --tsv $T/r2_classify.tsv | tail -1
python3 - "$T" <<'PY'
import csv, sys; T=sys.argv[1]
ls={r['sid'] for r in csv.DictReader(open(f'{T}/line_signs.tsv'),delimiter='\t')}
rows=[r for r in csv.DictReader(open(f'{T}/r2_classify.tsv'),delimiter='\t') if r['box'] in ls and r['k1'] not in ('','_held')]
open(f'{T}/r2_k1.tsv','w').write('sid\tlabel\n'+''.join(f"{r['box']}\t{r['k1']}\n" for r in rows))
PY
python3 $TOOLS/box_token_align.py --signs $T/line_signs.tsv --read $T/read.tsv --read-alt $T/read_alt.tsv --topk $T/r2_classify.tsv --keep-pos $T/keep.tsv --count-tol 0.10 --tokens-out $T/r2_tokens.tsv --out $T/r2_map.tsv --lines-out $T/r2_lines.tsv --check-labels $T/r2_k1.tsv --check-bound | grep -v "^count-tol" | tee $T/r2_check_console.txt || true
python3 tools/join_check.py --map $T/r2_map.tsv --check-labels $T/r2_k1.tsv --read $T/read.tsv --read $T/read_alt.tsv --steered | tee $T/r2_joincheck_steered.txt || true
python3 "$HERE/purity.py" "$TD" | tee $T/purity_console.txt
