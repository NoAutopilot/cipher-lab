#!/bin/sh
# Regenerates d2_*.json (diagnostic D2) and bgap_*.json (B's fit gap; needs G-B's model5_en.bin and hsolve5b).
cd "$(dirname "$0")"; xargs -P 4 -L 1 python3 < jobs2.txt
