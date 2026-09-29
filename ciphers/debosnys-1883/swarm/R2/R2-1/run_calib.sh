#!/bin/sh
# Regenerates every calib_*.jsonl (12 jobs, 4 at a time; about 10 min on 4 cores).
cd "$(dirname "$0")" && xargs -P 4 -n 2 sh -c 'python3 r21.py calib $0 $1 40 calib_$0_$1.jsonl' < jobs.txt
