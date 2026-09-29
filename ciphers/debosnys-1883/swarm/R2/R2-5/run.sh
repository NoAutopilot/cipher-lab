#!/bin/sh
# Regenerates every calib_*.jsonl, ctrl_*.json and real_*.json of R2-5 (4 parallel jobs).
cd "$(dirname "$0")"; xargs -P 4 -L 1 python3 r25.py < jobs.txt
