import subprocess, sys, os, tempfile, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
ROOM = """2026-10-15 02:09 | LANE DEFAULT-A2-0209-15 (account 2, lane orchestrator) | claim: lane, cap 60; usage: five_hour allowed by get_session, resets 05:20 UTC
2026-10-15 02:30 | worker X | done (02:20-02:30 UTC) for LANE DEFAULT-A2-0209-15 (account 2): a result; usage: not readable here
2026-10-15 02:35 | worker VIV-67C | flag: for the parent, crops missing; usage: not readable here
2026-10-15 02:40 | worker VIV-F191C | done (02:10-02:40) for LANE VIV-KEYSTONE (account 4): drift 15/15; usage: five_hour allowed by get_session, resets 07:20 UTC
"""
def test_sections_and_counts():
    d = tempfile.mkdtemp(); p = os.path.join(d, 'ROOM.md'); open(p, 'w').write(ROOM)
    r = subprocess.run([sys.executable, str(ROOT / 'tools/parent_report.py'), '--room', p, '--now', '2026-10-15 03:00', '--since', '2026-10-15 02:00'], capture_output=True, text=True)
    out = r.stdout
    for s in ('1 USAGE', '2 LANES', '3 KEYSTONE', '4 FINISHED', '5 WAITING', '6 FLAGS'):
        assert s in out, s
    assert 'account 2: DEFAULT-A2-0209-15 open since 02:09; workers done in window 1' in out
    assert 'VIV-F191C' in out and 'drift 15/15' in out
    assert '02:35' in out and 'crops missing' in out
