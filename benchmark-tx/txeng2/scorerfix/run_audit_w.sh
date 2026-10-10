#!/bin/sh
# PREREG-txeng2-21 WIT-FLAGS step 6: ONE corrected-audit re-score of the frozen S2 outputs under the witness-revised mask
# (item vivonne1573-f103r-confirm2-w). The S2_* names of run_audit.sh are suffixed _w; CA-S2's files are untouched.
# Run from the repo root: sh benchmark-tx/txeng2/scorerfix/run_audit_w.sh
set -e
D=benchmark-tx/txeng2/scorerfix
S2=benchmark-tx/outputs/vivonne1573-f103r-confirm2-w
ITEM=vivonne1573-f103r-confirm2-w
(cd $S2 && sha256sum -c ../../txeng2/s2score/SHA256SUMS.prescore) > $D/sha_check_S2_w.txt
sha256sum benchmark-tx/$ITEM.truth.tsv >> $D/sha_check_S2_w.txt
for M in "" "--exclude-flagged"; do
  tag=$( [ -n "$M" ] && echo flagged || echo plain )
  python3 tools/tx_bench.py $S2/passZ_S2b.tsv $S2/passA_S2.tsv $S2/passB_S2.tsv $S2/passA.tsv $S2/passB.tsv $S2/committed.tsv \
    --bench BENCHMARK-TX.tsv --item $ITEM --paired $S2/committed.tsv --strict $M > $D/S2_${tag}_w.txt 2>&1 || echo "exit $?" >> $D/S2_${tag}_w.txt
done
