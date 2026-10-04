#!/bin/sh
# TX-VIEWS (4 Oct 2026): normalise the no.87 view reads (harvest/views87/reads/<view>_<leaf>.tsv, brief format
# passage/pos/sign_id) to tx_bench's line/pos/sign in benchmark-tx/outputs/birago1572-no87/views/<view>.tsv,
# and cut passA/passB/passC to the same leaves (f178r, f179r). Run from the repo root.
R=ciphers/nevers-birago-fr3251-1572/harvest/views87/reads
O=benchmark-tx/outputs/birago1572-no87
mkdir -p $O/views
for v in pad s125 warp s080 contrast; do
  [ -f $R/${v}_f178r.tsv ] || continue
  { printf 'line\tpos\tsign\n'
    for l in f178r f179r; do awk -F'\t' -v l=$l 'NR>1 && $1!="" {print l"_"$1"\t"$2"\t"$3}' $R/${v}_$l.tsv; done; } > $O/views/$v.tsv
done
for p in passA passB passC; do
  awk -F'\t' 'NR==1 || $1 ~ /^f17(8r|9r)_/' $O/$p.tsv > $O/views/${p}_rr.tsv
done
