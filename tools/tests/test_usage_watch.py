import subprocess, sys, os, tempfile, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
ROOM = """2026-10-15 01:00 | orchestrator (owner account) | check-in 113 (01:0x UTC): nothing in flight. Account 1 allowed, five-hour window resets 21:20 UTC.
2026-10-15 01:10 | LANE DEFAULT-account-2-20261015-0110 (account 2, lane orchestrator) | claim: lane, cap 60, box 600
2026-10-15 01:20 | LANE X (account 4, parent) | check-in: BUDGETS.md scaling rule stands: allowed_warning anywhere -> no new workers anywhere; five_hour window read by get_session: allowed.
2026-10-15 01:30 | LANE DEFAULT-account-2-20261015-0110 (account 2, lane orchestrator) | check-in 1: 5 workers live; five_hour allowed_warning by get_session, resets 03:10 UTC
"""
def run(room, now, extra=()):
    d = tempfile.mkdtemp(); p = os.path.join(d, 'ROOM.md'); open(p, 'w').write(room)
    r = subprocess.run([sys.executable, str(ROOT / 'tools/usage_watch.py'), '--room', p, '--usage', os.path.join(d, 'none.tsv'), '--now', now, '--json', *extra], capture_output=True, text=True)
    import json; return r.returncode, {x['account']: x for x in json.loads(r.stdout)}
def test_warning_stops():
    rc, rows = run(ROOM, '2026-10-15 01:40')
    assert rc == 2 and rows['2']['word'] == 'allowed_warning' and rows['2']['flag'].startswith('STOP')
    assert rows['1']['word'] == 'allowed' and rows['1']['flag'] == ''
def test_rule_quote_not_a_reading():
    rc, rows = run(ROOM.splitlines()[2] + '\n', '2026-10-15 01:40')
    assert rows['4']['word'] == '--'
def test_stale_only_when_live():
    room = ROOM.splitlines()[1] + '\n'  # a live claim on account 2, no status word
    rc, rows = run(room, '2026-10-15 03:00')
    assert rc == 1 and rows['2']['flag'].startswith('STALE')
    rc, rows = run(ROOM.splitlines()[0] + '\n', '2026-10-15 09:00')  # idle account 1 with an old word: not flagged
    assert rc == 0 and rows['1']['flag'] == ''
def test_old_warning_idle_not_stop():
    rc, rows = run("2026-10-11 01:00 | LANE Y (account 3, lane orchestrator) | done: five_hour allowed_warning at close\n", '2026-10-15 01:40')
    assert rc == 0 and rows['3']['word'] == 'allowed_warning' and rows['3']['flag'].startswith('old warning')
