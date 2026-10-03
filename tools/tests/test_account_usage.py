"""Offline test for tools/account_usage.py."""
import datetime as dt
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import account_usage as au

NOW = dt.datetime(2026, 10, 3, 4, 0, tzinfo=dt.timezone.utc)
LEDGER = """| 3 Oct 2026 | W1 | s1 | account-4 | Opus 5.5 | 4.50 | D | x |
| 3 Oct 2026 | W2 | s2 | account 2 (LANE-A2PUSH) | Opus 5.5 | 1.25 | D | x |
| 2 Oct 2026 | W3 | s3 | account-4 | Opus 5.5 | 2.00 | D | x |
| 1 Oct 2026 | W4 | s4 | account-4 | Opus 5.5 | 9.00 | D | x |
| 3 Oct 2026 | W5 | s5 | account-4 | Opus 5.5 | n/a | D | x |
"""
ROOM = """2026-10-03 03:00 | A (account-4) | claim: t1
2026-10-03 03:10 | A (account-4) | done, x
2026-10-03 03:20 | B (account 2, LANE) | claim: t2
2026-10-03 03:30 | B (account 2, LANE) | halfway
2026-10-02 18:00 | C (account-4) | claim: stale
"""

def test_ledger():
    d = au.ledger(LEDGER, {'3 Oct 2026', '2 Oct 2026'})
    assert d['4']['3 Oct 2026'] == [4.5, 1] and d['4']['2 Oct 2026'] == [2.0, 1]
    assert d['2']['3 Oct 2026'] == [1.25, 1]
    assert '1 Oct 2026' not in d['4']

def test_live():
    lv = au.live(ROOM, NOW)
    assert lv == {'2': ['B (account 2, LANE)']}, lv

def test_usage_rows():
    t = au.USAGE_HEADER + '2026-10-03 03:00\t3\tallowed\tfive_hour\t\t\t1\t\n2026-10-03 04:00\t3\tallowed_warning\tseven_day\t\t\t0\tn\n'
    assert au.usage_rows(t)['3']['rl_status'] == 'allowed_warning'

if __name__ == '__main__':
    test_ledger(); test_live(); test_usage_rows(); print('ok')
