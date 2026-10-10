#!/bin/sh
# TOOL-SCORER-FIX step 3: corrected audit of prior looks with the fixed scorer (one run per item and mask set).
# Run from the repo root. Verifies the frozen inputs' sha256 first; writes into benchmark-tx/txeng2/scorerfix/.
# Usage: sh benchmark-tx/txeng2/scorerfix/run_audit.sh [S2TRUTH_ITEM]   (default vivonne1573-f103r-confirm2)
set -e
D=benchmark-tx/txeng2/scorerfix
S2=benchmark-tx/outputs/vivonne1573-f103r-confirm2
DV=benchmark-tx/outputs/vivonne1573-f102r-dev
ITEM=${1:-vivonne1573-f103r-confirm2}
(cd $S2 && sha256sum -c ../../txeng2/s2score/SHA256SUMS.prescore) > $D/sha_check_S2.txt
cat benchmark-tx/txeng2/viv102base/SHA256SUMS_pass[ZAB].txt | grep "outputs/vivonne1573-f102r-dev/pass[ZAB]_dv1.tsv" | sha256sum -c > $D/sha_check_DV1b.txt
sha256sum $DV/passZ_dv1.tsv $DV/passA_dv1.tsv $DV/passB_dv1.tsv $DV/committed.tsv benchmark-tx/outputs/vivonne1573-f102r-dev2/committed.tsv > $D/sha_DV1b_inputs.txt
for M in "" "--exclude-flagged"; do
  tag=$( [ -n "$M" ] && echo flagged || echo plain )
  python3 tools/tx_bench.py $S2/passZ_S2b.tsv $S2/passA_S2.tsv $S2/passB_S2.tsv $S2/passA.tsv $S2/passB.tsv $S2/committed.tsv \
    --bench BENCHMARK-TX.tsv --item $ITEM --paired $S2/committed.tsv --strict $M > $D/S2_${tag}.txt 2>&1 || echo "exit $?" >> $D/S2_${tag}.txt
  # DV1b passes against the WITHDRAWN dev truth (paired vs its committed) and against dev2 (paired vs dev2's committed)
  for T in vivonne1573-f102r-dev vivonne1573-f102r-dev2; do
    C=benchmark-tx/outputs/$T/committed.tsv
    python3 tools/tx_bench.py $DV/passZ_dv1.tsv $DV/passA_dv1.tsv $DV/passB_dv1.tsv \
      --bench BENCHMARK-TX.tsv --item $T --paired $C --strict $M > $D/DV1b_${T}_${tag}.txt 2>&1 || echo "exit $?" >> $D/DV1b_${T}_${tag}.txt
  done
done
