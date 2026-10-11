#!/bin/sh
# BOXMAP-RESCORE (others), 11 Oct 2026, account 3: the tools/tests consumers of atlas/no87_box_token.tsv re-run with only the map
# changed (atlas/no87_box_token_labelaware.tsv). The compat map (old columns with the clerk-alignment truth column, from
# atlas/no87_map.py --compat) goes to a temp dir only. From the repo root:  sh tools/tests/rescore_boxmapLA/rescore.sh
set -e
R=tools/tests/rescore_boxmapLA; A=ciphers/nevers-birago-fr3251-1572/atlas; NEW=$A/no87_box_token_labelaware.tsv; T=$(mktemp -d)
python3 $A/no87_map.py --compat $T/compat_map.tsv > /dev/null
# MQS-SHEETS G3 KM (km_rescore.py = km_birago_map.py without the Python 3.12-only decipher_sheet import; same statistic)
python3 $R/km_rescore.py --json $R/km_oldmap.json || true
python3 $R/km_rescore.py --map $NEW --json $R/km_boxmapLA.json || true
# MQS-SORTER section B (owner's 4 Oct no.87 sort vs BENCHMARK-TX)
python3 tools/tests/mqs_sorter_score_owner.py > $R/mqs_sorter_score_owner_oldmap_today.json
python3 tools/tests/mqs_sorter_score_owner.py --map $T/compat_map.tsv > $R/mqs_sorter_score_owner_boxmapLA.json
# MQS-SORTER section A (--oddness-audit on the no.87 clean tiles), page order and both variants, random and look-alike plants
for M in old new; do
  if [ $M = old ]; then python3 tools/tests/oddness_no87_inputs.py $T/odd_$M > /dev/null
  else python3 tools/tests/oddness_no87_inputs.py --map $T/compat_map.tsv $T/odd_$M > /dev/null; fi
  for v in mean medoid knn3; do for pl in random lookalike; do
    X=""; [ $pl = lookalike ] && X="--confusion ciphers/nevers-birago-fr3251-1572/harvest/confusion_1572.tsv"
    printf '%s\t%s\t%s\t' $M $v $pl
    python3 tools/sign_sorter.py --signs $T/odd_$M/signs.tsv --labels $T/odd_$M/labels.tsv --pages $A/pages.json --oddness-audit \
      --plants $pl --oddness-variant $v $X 2>/dev/null | tail -1
  done; done
done > $R/oddness_audit.tsv
# MQS-CLASSIFY-ROUNDS (about 15 min each; the runner gained --map/--labels/--out and tx_bench --legacy, see its source)
python3 tools/tests/mqs_classify_rounds_run.py --map $T/compat_map.tsv --out $R/MQS-CLASSIFY-ROUNDS-results_boxmapLA.tsv
python3 tools/tests/mqs_classify_rounds_run.py --map $T/compat_map.tsv --labels $A/rescore_boxmapLA/named/labels.json \
  --out $R/MQS-CLASSIFY-ROUNDS-results_boxmapLA_named.tsv
rm -rf $T
