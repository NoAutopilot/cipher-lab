"""Offline test: work_queue.load/save survive a stray trailing tab and never truncate the file."""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import work_queue as w


def test_trailing_tab_row_round_trips():
    d = tempfile.mkdtemp()
    p = os.path.join(d, 'WQ.tsv')
    hdr = '\t'.join(w.COLS) + '\n'
    good = 'A\taccount-1\tb.md\tOpus\t1\t1\tqueued\t2026-10-03 11:55\tnote\n'
    bad = 'B\taccount-1\tb.md\tOpus\t1\t1\tqueued\t2026-10-03 11:55\tn2\textra\t\n'
    open(p, 'w').write(hdr + good + bad)
    w.PATH = p
    rows = w.load()
    assert len(rows) == 2 and rows[1]['note'] == 'n2 extra'
    w.save(rows)
    assert open(p).read().count('\n') == 3



# Empty-queue auto-fill (LANE-SYS1, 5 Oct 2026)
import datetime, subprocess
T = datetime.datetime(2026, 10, 5, 18, 0)


def row(jid, acct, status, added='2026-10-05 00:00', box='600'):
    return {'job_id': jid, 'account': acct, 'brief': 'b.md', 'model': 'Opus 5.5', 'cap_usd': '60', 'box_min': box,
            'status': status, 'added': added, 'note': ''}


def test_fills_on_empty_queue():
    rows = [row('LANE-A', 'account-1', 'done 2026-10-05 16:30')]
    new, why = w.autofill(rows, 'account-1', T)
    assert why == 'filled' and new['job_id'] == 'DEFAULT-account-1-20261005-1800'
    assert new['brief'] == '.claude/briefs/default-lane.md' and new['cap_usd'] == '60' and new['box_min'] == '600'
    assert new['status'] == 'queued' and new['note'] == 'auto-fill: empty queue'


def test_alias_owner_is_account_1():
    rows = [row('LANE-A', 'owner', 'claimed s1 2026-10-05 17:00')]
    assert w.autofill(rows, 'account-1', T)[0] is None
    rows = [row('X', 'account-2', 'queued')]
    assert w.autofill(rows, 'other', T)[0] is None


def test_no_fill_when_queued_row_exists():
    assert w.autofill([row('J', 'account-1', 'queued')], 'account-1', T) == (None, 'queued row exists')


def test_no_fill_when_lane_closed_under_60_min():
    rows = [row('LANE-A', 'account-1', 'done 2026-10-05 17:1x')]  # fuzzy minute reads 17:19
    assert w.autofill(rows, 'account-1', T)[1] == 'lane closed < 60 min ago'
    rows = [row('LANE-A', 'account-1', 'done 2026-10-05 16:59')]
    assert w.autofill(rows, 'account-1', T)[1] == 'filled'


def test_no_fill_when_lane_claimed_but_stale_claim_does_not_block():
    rows = [row('LANE-A', 'account-1', 'claimed s1 2026-10-05 10:00')]
    assert w.autofill(rows, 'account-1', T)[1].startswith('lane open')
    rows = [row('LANE-A', 'account-1', 'claimed s1 2026-10-04 08:00')]  # 34 h > 600 + 360 min
    assert w.autofill(rows, 'account-1', T)[1] == 'filled'


def test_no_fill_when_paused():
    rows = [row('PAUSE-account-1', 'account-1', 'paused 2026-10-05 12:00')]
    assert w.autofill(rows, 'owner', T)[1] == 'paused'
    rows[0]['status'] = 'done 2026-10-05 13:00'  # resumed
    assert w.autofill(rows, 'owner', T)[1] == 'filled'


def test_no_fill_when_default_lane_added_under_12h():
    rows = [row('DEFAULT-account-1-20261005-0700', 'account-1', 'done 2026-10-05 16:00', added='2026-10-05 07:00')]
    assert w.autofill(rows, 'account-1', T)[1].startswith('default lane < 12 h')
    rows[0]['added'] = '2026-10-05 05:59'
    assert w.autofill(rows, 'account-1', T)[1] == 'filled'


def test_other_accounts_empty_queue_does_not_fill_this_one():
    rows = [row('J', 'account-1', 'queued'), row('LANE-B', 'account-2', 'done 2026-10-05 10:00')]
    assert w.autofill(rows, 'account-1', T)[0] is None
    assert w.autofill(rows, 'account-2', T)[1] == 'filled'


def _cli(p, *args):
    env = dict(os.environ, WQ_PATH=p)
    return subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), '..', 'work_queue.py')] + list(args),
                          capture_output=True, text=True, env=env)


def test_cli_next_fills_once_pause_resume_and_check():
    d = tempfile.mkdtemp(); p = os.path.join(d, 'WQ.tsv')
    open(p, 'w').write('\t'.join(w.COLS) + '\n' + '\t'.join(row('LANE-A', 'account-1', 'done 2026-10-01 00:00').values()) + '\n')
    r = _cli(p, '--next', '--account', 'account-1', '--no-autofill')
    assert r.stdout == '' and open(p).read().count('\n') == 2
    r = _cli(p, '--pause', 'owner', '--note', 'test'); assert 'PAUSE-account-1 paused' in r.stdout
    assert _cli(p, '--next', '--account', 'account-1').stdout == ''
    _cli(p, '--resume', 'account-1')
    r = _cli(p, '--next', '--account', 'owner'); assert r.stdout.startswith('DEFAULT-account-1-')
    r = _cli(p, '--next', '--account', 'owner'); assert r.stdout.count('DEFAULT-') == 1  # queued row blocks a second
    assert _cli(p, '--next', '--account', 'other').stdout.startswith('DEFAULT-account-2-')


def test_check_accepts_pause_row():
    rows = [row('PAUSE-account-1', 'account-1', 'paused 2026-10-05 12:00')]
    rows[0]['brief'] = '-'
    assert w.check(rows)
    rows.append(row('J', 'account-1', 'paused 2026-10-05 12:00')); rows[1]['brief'] = '-'
    assert not w.check(rows)  # paused / no brief only for PAUSE- rows


if __name__ == '__main__':
    for k, f in list(globals().items()):
        if k.startswith('test_'): f()
    print('ok')
