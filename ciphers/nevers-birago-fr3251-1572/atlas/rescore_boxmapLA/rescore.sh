#!/bin/sh
# BOXMAP-RESCORE (others), 11 Oct 2026, account 3: TX-ATLAS-B72's naming and scoring re-run with only the no.87 box map changed.
# From the repo root:  sh ciphers/nevers-birago-fr3251-1572/atlas/rescore_boxmapLA/rescore.sh
# The compat maps (old columns + the clerk-sheet truth column, as atlas/no87_box_token.tsv carries it) are written to a temp dir and
# never committed. Outputs here: named/ (labels.json, cluster_names.tsv from the label-aware map), no87_heldout_LA.tsv (held-out
# classify with those names, no.87 pages), no87_heldout_LA_bench.tsv, rescore.txt. Read-free; no image is viewed.
set -e
A=ciphers/nevers-birago-fr3251-1572/atlas; R=$A/rescore_boxmapLA; T=$(mktemp -d)
python3 $A/no87_map.py --compat $T/compat_map.tsv > /dev/null
python3 $R/variants.py $T > /dev/null                         # $T/compat_statusonly.tsv, $T/compat_sorteronly.tsv
python3 $A/name_clusters.py --map $T/compat_map.tsv --out $R/named
HO=$(for i in $(seq 13 23); do printf ' --holdout f178v_%s_' $i; done; for i in 01 02 03; do printf ' --holdout f179r_%s_' $i; done)
python3 tools/glyph_atlas.py classify --out $A --labels $R/named/labels.json --page all --tsv $T/ho.tsv --topk 3 $HO > /dev/null
(head -1 $T/ho.tsv; awk -F'\t' 'NR>1 && ($1=="f178r"||$1=="f178v"||$1=="f179r")' $T/ho.tsv) > $R/no87_heldout_LA.tsv
python3 - $R <<'PY'
import csv, sys
R = sys.argv[1]
HELD = [f'f178v_{i}_' for i in range(13, 24)] + [f'f179r_{i:02d}_' for i in (1, 2, 3)]
rows = [r for r in csv.DictReader(open(R + '/no87_heldout_LA.tsv'), delimiter='\t') if r['box'].startswith(tuple(HELD)) and r['k1'] != '_']
with open(R + '/no87_heldout_LA_bench.tsv', 'w') as f:
    f.write('line\tpos\tsign\n' + ''.join(f"{r['page']}_L{int(r['line']):02d}\t{r['x']}\t{r['k1']}\n"
                                         for r in sorted(rows, key=lambda r: (r['page'], int(r['line']), int(r['x'])))))
PY
{
  for M in "old:$A/no87_box_token.tsv" "label-aware:$T/compat_map.tsv" "sorter-only:$T/compat_sorteronly.tsv" "status-only:$T/compat_statusonly.tsv"; do
    for K in "committed atlas names (topk/no87_heldout.tsv):$A/topk/no87_heldout.tsv" "names re-derived on the label-aware map (no87_heldout_LA.tsv):$R/no87_heldout_LA.tsv"; do
      echo "== map ${M%%:*}; topk ${K%%:*}"; python3 $A/score_no87.py --map ${M#*:} ${K#*:}
    done
  done
  echo "== tx_bench --legacy (map-free: atlas boxes in x order, '_' dropped), committed names"
  python3 tools/tx_bench.py $A/topk/no87_heldout_bench.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --legacy | head -1
  echo "== tx_bench --legacy, names re-derived on the label-aware map"
  python3 tools/tx_bench.py $R/no87_heldout_LA_bench.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --legacy | head -1
} > $R/rescore.txt
rm -rf $T
cat $R/rescore.txt
