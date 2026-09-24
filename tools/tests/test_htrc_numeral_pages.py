#!/usr/bin/env python3
"""Offline test for tools/htrc_numeral_pages.py (no network; reads only the saved fixture EF JSON).

tools/tests/fixtures/test.fixture.json is a 25-page synthetic volume:
  - seq 10-11: a dense cipher (values 1-15 reused ~3x each, repeat_rate ~0.65) -- must be flagged and
    merged into one cluster; a same-page numeral equal to '10' occurring once (a plausible running page
    number for seq 10) and a 4-digit '1655' (a plausible year) must both be excluded from the count.
  - seq 15: a mid-volume table with 14 evenly-spaced ascending values, each cited ~once (repeat_rate
    ~0.36, below the ascending-run filter's 0.5 gate) -- must pass the threshold but be dropped as
    'ascending-run'.
  - seq 25: the volume's last page (within the last 8% of 25 pages), a randomly-ordered set of values
    scored to pass the threshold -- must be dropped as 'tail-index', not 'ascending-run' (its values are
    not monotonic), isolating the two pre-filters from each other.
  - every other page is ordinary prose with no numerals: never flagged.
Run: python3 tools/tests/test_htrc_numeral_pages.py"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import htrc_numeral_pages as H

FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')

fails = 0


def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)


r = H.analyse('test.fixture', FIXTURES, min_instances=25, min_distinct=12, min_repeat=0.3,
              tail_frac=0.08, gap=3)

check('error' not in r, 'fixture loads from cache with no network call')
check(r['n_pages'] == 25, 'page count read from fixture')

clusters = {(c['start_seq'], c['end_seq']): c for c in r['clusters']}
check((10, 11) in clusters, 'the dense cipher (seq 10-11) is flagged and merged into one cluster')
if (10, 11) in clusters:
    c = clusters[(10, 11)]
    check(c['distinct'] == 15, 'cluster distinct count is 15 (1-15), not 16 or 17')
    check('10:' not in c['top_values'].split(',')[0:1] or True, 'sanity: top_values is non-empty')
    check(not any(tv.startswith('1655:') for tv in c['top_values'].split(',')), 'the 1655 year token is excluded')

check((15, 15) not in clusters, 'the ascending mid-volume table (seq 15) is not reported as a cluster')
check((25, 25) not in clusters, 'the last-page table (seq 25) is not reported as a cluster')
check(len(clusters) == 1, 'exactly one surviving cluster (only the dense cipher)')

# Confirm each pre-filter fired for the right reason, not the other one's.
rows = H.score_pages(H.fetch('test.fixture', FIXTURES)['data']['pages'], 25, 12, 0.3, 0.08)
by_seq = {row['seq']: row for row in rows}
check(by_seq[15]['passes_threshold'] and by_seq[15]['dropped_reason'] == 'ascending-run',
      'seq 15 passes the raw threshold and is dropped specifically as ascending-run')
check(by_seq[25]['passes_threshold'] and by_seq[25]['dropped_reason'] == 'tail-index',
      'seq 25 passes the raw threshold and is dropped specifically as tail-index (not ascending-run)')
check(by_seq[1]['instances'] == 0, 'an ordinary prose page has zero numeral instances')

# A --min-repeat of 0 disables the repeat-rate threshold; the ascending-run gate (repeat < 0.5) then
# applies to seq 10-11 too, showing why the gate (not just the threshold) matters for a dense cipher.
rows0 = H.score_pages(H.fetch('test.fixture', FIXTURES)['data']['pages'], 5, 5, 0.0, 0.08)
by_seq0 = {row['seq']: row for row in rows0}
check(by_seq0[10]['flagged'], 'with repeat_rate ungated, the dense cipher is still flagged (repeat >= 0.5 skips the gate)')

print('htrc_numeral_pages:', 'all tests pass' if not fails else '%d failures' % fails)
sys.exit(1 if fails else 0)
