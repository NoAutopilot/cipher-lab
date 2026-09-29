#!/bin/sh
# F61-FAMILY-13 (29 Sept 2026): key v8 order gain, tools/partial_key_test.py --cells --shuffle-target 3 (VERIFY-F61-V11 part C's settings).
# pkt_v8_<leaf>_split.txt: runner 13's split drafts under key_v8_cells.tsv (must equal verify_v11/pkt_<leaf>_split.txt; build_key_v8.py checks);
# pkt_v8_<leaf>_split_nb.txt: the same tokens labelled 4TRI_NB; pkt_v8_<leaf>_v8.txt: build_key_v8.py's token assignment (conflicts left 4TRI).
set -e
F=$(dirname "$0"); T="$F/../../../tools/partial_key_test.py"
for leaf in f101r f124r; do
  for suf in split split_nb v8; do
    python3 "$T" --cells "$F/key_v8_cells.tsv" --draft "$F/passes/rec${leaf}_${suf}/ciphertext_draft.tsv" --shuffle-target 3 > "$F/pkt_v8_${leaf}_${suf}.txt"
  done
done
