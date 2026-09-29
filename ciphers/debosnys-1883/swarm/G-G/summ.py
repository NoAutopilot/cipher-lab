#!/usr/bin/env python3
"""One line per score.py JSON (stdin): coverage, read letters, recovery if any, and pct/pct_strat per statistic."""
import json, sys
d = json.load(sys.stdin); st = d.get('stats', {})
cells = ' '.join('%s %s/%s%s' % (k, v['pct'], v['pct_strat'], '*' if v['beats_all'] and v['beats_all_strat'] else '') for k, v in st.items())
print('cov %s read %s rec %s | %s' % (d.get('coverage_test', d.get('coverage')), d.get('read_letters'), d.get('recovery_pct_test', d.get('recovery_pct')), cells))
