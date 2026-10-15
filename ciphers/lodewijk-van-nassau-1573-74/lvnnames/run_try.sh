#!/bin/sh
# LVN-NAMES test B: decode_key.py --try per code (PREREG-LVNNAMES.md). usage: run_try.sh CONFIG OUT CODE=VALUE...
D=ciphers/lodewijk-van-nassau-1573-74; CFG=$1; OUT=$2; shift 2
for h in "$@"; do
  python3 tools/decode_key.py $D --config $CFG --try "$h" 2>&1 | grep -v '^  [0-9]*:[0-9]' | grep '=' >> $OUT
done
