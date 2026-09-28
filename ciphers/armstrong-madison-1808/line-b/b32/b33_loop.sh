#!/bin/bash
# relaunch the resumable B33 script until all nine runs are logged (a CPU-time limit kills long python processes)
cd /home/user/cipher-lab/ciphers/armstrong-madison-1808/line-b/b32
for i in $(seq 1 12); do
  n=$(grep -c '^error' b33_log.txt 2>/dev/null); [ "$n" -ge 9 ] && break
  python3 b33_errors.py >> b33_log.txt 2>&1
  sleep 5
done
echo "b33 loop finished, $(grep -c '^error' b33_log.txt) runs" >> b33_log.txt
