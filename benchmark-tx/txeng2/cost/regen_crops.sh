#!/bin/sh
# re-derive arm a's 2x crops (32 PNG, ~16 MB, not committed): needs opencv-python-headless
python3 tools/tx_prep.py lines --crops ciphers/fr3621-dinteville-1592/images --only f128_ --setting sr2 \
  --out benchmark-tx/txeng2/cost/crops_2x --segments 4 --max-w 1500 --overlap 150
