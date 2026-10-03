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


if __name__ == '__main__':
    test_trailing_tab_row_round_trips(); print('ok')
