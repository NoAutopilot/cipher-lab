#!/bin/sh
# TXE2-OVERLAP (PREREG-txeng2-7 O1, 9 Oct 2026): regenerate every per-item JSON of RESULTS.md. Read-free (no sign values).
# Eval items (eval_heldout, f178r, f152r, Spinelli) run with --no-positions: counts kept, positions opened only.
# MODEL=uniform sh run_overlap.sh writes the *_uniform sensitivity files.
# ceppo-f87-S needs its gitignored lines2x crops first: (cd ciphers/ceppo-nevers-fr3251-1570s/harvest && python3 cut_folio_lines.py)
set -e
M=${MODEL:-ink}; X=$([ "$M" = ink ] && echo '' || echo _$M)
cd "$(dirname "$0")/../../.."
O=benchmark-tx/txeng2/overlap
H=ciphers/nevers-birago-fr3251-1572/harvest
P=benchmark-tx/outputs/birago1572-no87
U=benchmark-tx/txeng/units/README.md
units() { grep "^- $1:" $U | sed "s/^- $1: //; s/ --.*//" | tr ' ' ',' | sed 's/,$//'; }
NO87="--manifest $H/f178r/manifest.json --crop-dir $H/f178r --manifest $H/f178v/manifest.json --crop-dir $H/f178v --manifest $H/f179r/manifest.json --crop-dir $H/f179r --truth benchmark-tx/birago1572-no87.truth.tsv --pass L=$P/labels.tsv --pass A=$P/passA.tsv --pass B=$P/passB.tsv"
for u in dev_tune eval_heldout; do
  NP=$([ $u = eval_heldout ] && echo --no-positions || true)
  python3 tools/overlap_audit.py --model $M $NP $NO87 --lines "$(units $u)" --json $O/no87_$u$X.json > $O/no87_$u$X.txt
done
python3 tools/overlap_audit.py --model $M --no-positions $NO87 --lines f178r_L01,f178r_L02,f178r_L03 --json $O/no87_f178r$X.json > $O/no87_f178r$X.txt
D=ciphers/fr3621-dinteville-1592/images; DP=benchmark-tx/outputs/dint-f128-print
python3 tools/overlap_audit.py --model $M --manifest $D/manifest.json --crop-dir $D --truth benchmark-tx/dint-f128-print.truth.tsv \
  --pass A=$DP/passA.tsv --pass B=$DP/passB.tsv --pass X21_sonnet_pipeline=$DP/passX21_sonnet_pipeline.tsv \
  --json $O/dint_f128$X.json > $O/dint_f128$X.txt
F=benchmark-tx/txeng2/f152r/crops
python3 tools/overlap_audit.py --model $M --no-positions --manifest $F/manifest.json --crop-dir $F --truth benchmark-tx/birago1572-f152r.truth.tsv \
  --pass Z=benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv --json $O/f152r$X.json > $O/f152r$X.txt
S=benchmark-tx/txeng/confirm/crops
python3 tools/overlap_audit.py --model $M --no-positions --manifest $S/manifest.json --crop-dir $S --truth benchmark-tx/spinelli-c1519-confirm.truth.tsv \
  --label-map benchmark-tx/txeng/confirm/collapse_map.tsv \
  --pass Z=benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv --json $O/spinelli$X.json > $O/spinelli$X.txt
C=ciphers/ceppo-nevers-fr3251-1570s/harvest/f87/lines2x
python3 tools/overlap_audit.py --model $M --manifest $C/crops_manifest.json --crop-dir $C --truth benchmark-tx/ceppo-f87-S.truth.tsv \
  --pass C=benchmark-tx/outputs/ceppo-f87-S/passC.tsv \
  --pass A=benchmark-tx/outputs/ceppo-f87-S/passA.tsv --pass B=benchmark-tx/outputs/ceppo-f87-S/passB.tsv --json $O/f87$X.json > $O/f87$X.txt
