#!/usr/bin/env python3
"""One-line summary of a score.py JSON: coverage, read letters, recovery on test, and every statistic that beats all
1000 shuffles under both nulls (the bar), plus fr_quad pct / pct_strat."""
import json, sys
d = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else json.load(sys.stdin)
st = d['stats']; ok = [k for k, v in st.items() if v.get('beats_all') and v.get('beats_all_strat')]
fq = st['fr_quad']
print(f"{d.get('fit')}->{d.get('test')} cov {d.get('coverage_test')} read {d.get('read_letters')} recov_test {d.get('recovery_pct_test')} "
      f"fr_quad {fq['pct']}/{fq['pct_strat']} both-null stats: {ok or 'none'}")
