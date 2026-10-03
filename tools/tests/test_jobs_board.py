"""Offline test for tools/jobs_board.py."""
import datetime as dt
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import jobs_board as jb

NOW = dt.datetime(2026, 10, 3, 4, 0, tzinfo=dt.timezone.utc)
ROOM = """2026-10-03 03:00 | NV01-READ (account 3): fr3993-gonzague-nevers-1595 | claim: key no.70
2026-10-03 03:10 | TX-BENCH (acct3 worker) | claim: benchmark
2026-10-03 03:40 | TX-BENCH (acct3 worker) | done, for the account-3 orchestrator: err_true 0.053
2026-10-03 03:20 | GAPS-x (account-4) | claim: harley-287-1587 step
2026-10-02 20:00 | OLD (account-4) | claim: stale-one
2026-10-03 03:30 | orchestrator (account 3) | check-in
"""
QUEUE = """job_id\taccount\tbrief\tmodel\tcap_usd\tbox_min\tstatus\tadded\tnote
BIRAGO-NUM4\tother\tb.md\tOpus\t3\t35\tqueued\tt\tBirago numerical crib test
TX-BENCH\tother\tc.md\tOpus\t3\t35\tclaimed s\tt\tbench
"""
PROJ = jb.projects("project\tmatch\nTranscription standard\t(?-i:TX-[A-Z])\nBirago\tbirago\nNevers vein\tNV0\n")


def test_states_and_projects():
    js = {j['id']: j for j in jb.jobs(ROOM, QUEUE, PROJ, NOW, 12, frozenset({'harley-287-1587'}))}
    assert js['NV01-READ']['state'] == 'running' and js['NV01-READ']['project'] == 'Nevers vein'
    assert js['TX-BENCH']['state'] == 'done' and js['TX-BENCH']['project'] == 'Transcription standard'
    assert js['TX-BENCH']['summary'].startswith('err_true')
    assert js['BIRAGO-NUM4']['state'] == 'queued' and js['BIRAGO-NUM4']['project'] == 'Birago'
    assert js['GAPS-x']['project'] == 'harley-287-1587'
    assert js['OLD']['state'] == 'stale'
    assert 'orchestrator' not in js


if __name__ == '__main__':
    test_states_and_projects(); print('ok')
