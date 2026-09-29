#!/bin/sh
# DEB-SWARM-F: score every G-F key with the frozen score.py, held-out both directions; one summary line per run.
cd "$(dirname "$0")/.." || exit 1
for k in "$@"; do for d in "c1 c2" "c2 c1"; do set -- $d
  python3 score.py "G-F/$k" --fit $1 --test $2 > "G-F/scores/$(basename $k .tsv)_$1-$2.json"
  python3 -c "
import json,sys; r=json.load(open('G-F/scores/$(basename $k .tsv)_$1-$2.json'))
best=max(r['stats'].items(), key=lambda kv: kv[1]['pct'])
print('$k', '$1->$2', 'cov', r['coverage_test'], 'read', r['read_letters'], 'best', best[0], best[1]['pct'], best[1]['pct_strat'], 'passes', any(v['beats_all'] and v['beats_all_strat'] for v in r['stats'].values()) and r['coverage_test']>=.5 and r['read_letters']>=60)"
done; done
