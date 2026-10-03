"""Offline test for tools/account_usage.py (no network, no git writes)."""
import datetime as dt
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import account_usage as au

NOW = dt.datetime(2026, 10, 3, 4, 0, tzinfo=dt.timezone.utc)
ROOM = """2026-10-03 03:00 | A (account-4) | claim: t1
2026-10-03 03:10 | A (account-4) | done, x
2026-10-03 03:20 | B (account 2, LANE) | claim: t2
2026-10-03 03:30 | B (account 2, LANE) | halfway
2026-10-02 18:00 | C (account-4) | claim: stale
"""
USAGE = au.USAGE_HEADER + ('2026-10-03 03:00\t4\t40\t\t70\t\t5\tmod\t\n'
                           '2026-10-03 03:50\t4\t62.5\t2026-10-03T06:00Z\t81\t\t6\tmod\t\n')


def test_live():
    assert au.live(ROOM, NOW) == {'2': ['B (account 2, LANE)']}


def test_usage_rows_latest_and_old_layout_ignored():
    assert au.usage_rows(USAGE)['4']['five_pct'] == '62.5'
    assert au.usage_rows('utc\taccount\trl_status\n2026-10-03 03:00\t3\tx\n') == {}


def test_bar():
    assert au.bar(62.5) == '######....' and au.bar(None) == '??????????' and au.bar(130) == '##########'


def test_summary_text():
    orig = au.read
    au.read = lambda name, ref=None: {'ROOM.md': ROOM, 'USAGE.tsv': USAGE}.get(name, '')
    try:
        s = au.summary(now=NOW)
    finally:
        au.read = orig
    a4 = [r for r in s['accounts'] if r['account'] == '4'][0]
    assert a4['five_pct'] == 62.5 and a4['seven_pct'] == 81 and a4['age_min'] == 10
    assert '$' not in au.text(s)


if __name__ == '__main__':
    test_live(); test_usage_rows_latest_and_old_layout_ignored(); test_bar(); test_summary_text(); print('ok')
