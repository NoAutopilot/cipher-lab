"""Offline test for tools/tx_calibrate.py (TXE4-9 CALIB, 12 Oct 2026). Must catch: a substitution, a deletion and an insertion
each give one feedback row; must NOT block: a flagged position, an excluded position and a right position give none; no row
carries a plain-text letter; CLEAR rows are dropped; the task files name no truth path."""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_calibrate  # noqa: E402

BRIEF = ('# brief\n\nrules\n\nSign labels (use these exact labels):\n  A  shape a   B  shape b\n  C  shape c\n\n'
         'Output: TSV\npassage\tpos\tsign_id\n')


def _w(d, name, text):
    p = os.path.join(d, name)
    with open(p, 'w') as f:
        f.write(text)
    return p


def test_feedback_rows():
    with tempfile.TemporaryDirectory() as d:
        truth = _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n'
                   'it_L01\t1\tA\tA\tq\tscored\t\n'          # right
                   'it_L01\t2\tB\tB|C\tr\tscored\t\n'        # read D: wrong -> allowed B | C
                   'it_L01\t3\tA\tA\ts\tscored\talign-conflict\n'  # read B: wrong but flagged -> no row
                   'it_L01\t4\tX\t\t\texcluded:off-sheet\t\n'      # excluded -> no row
                   'it_L01\t5\tC\tC\tt\tscored\t\n'          # deleted -> missed
                   'it_L01\t6\tA\tA\tu\tscored\t\n'          # right
                   'it_L01\t7\tA\tA\tv\tscored\t\n')         # right, after an extra sign
        read = _w(d, 'read.tsv', 'passage\tpos\tsign_id\talt\tconf\tnote\n'
                  'L01\t1\tCLEAR\t\tH\tword\nL01\t2\tA\t\tH\t\nL01\t3\tD\t\tM\t\nL01\t4\tA\t\tH\t\nL01\t5\tX\t\tH\t\n'
                  'L01\t6\tA\t\tH\t\nL01\t7\tZ\t\tL\textra\nL01\t8\tA\t\tH\t\n')
        out = os.path.join(d, 'fb.tsv')
        tx_calibrate.main(['feedback', '--read', read, '--truth', 'it=%s:it' % truth, '--out', out, '--context', '2'])
        rows = [l.rstrip('\n').split('\t') for l in open(out)][1:]
        kinds = [r[3] for r in rows]
        assert len(rows) == 3, rows
        assert any(k.startswith('[your label D -> allowed labels B | C]') for k in kinds), kinds
        assert any(k.startswith('a sign missed here [allowed labels C]') for k in kinds), kinds
        assert any(k.startswith('extra sign here [your label Z]') for k in kinds), kinds
        text = open(out).read()
        for letter in 'qrstuv':
            assert ('\t%s' % letter) not in text and (' %s ' % letter) not in text, text
        assert 'CLEAR' not in text and all(r[0] == 'it' and r[1] == 'it_L01' for r in rows)


def test_build_and_target_name_no_truth():
    with tempfile.TemporaryDirectory() as d:
        brief = _w(d, 'brief.md', BRIEF)
        crop = _w(d, 'c_L01.jpg', 'x'); tcrop = _w(d, 'f_L01.jpg', 'y')
        notes = _w(d, 'notes.md', 'crop notes\n')
        b = os.path.join(d, 'b')
        tx_calibrate.main(['build', '--out', b, '--label-brief', brief, '--crop', crop, '--notes', notes])
        task = open(os.path.join(b, 'task.txt')).read()
        assert 'A  shape a' in task and 'crop notes' in task and 'truth' not in task.lower()
        assert os.path.exists(os.path.join(b, 'calib', 'c_L01.jpg'))
        read = _w(b, 'read.tsv', 'passage\tpos\tsign_id\n')
        fb = _w(d, 'fb.tsv', 'item\tline\tyour_sequence\tfeedback\n')
        for arm, extra in (('F', ['--feedback', fb]), ('C', [])):
            t = os.path.join(d, 't' + arm)
            tx_calibrate.main(['target', '--out', t, '--brief', brief, '--calib-dir', b, '--calib-read', read,
                               '--crop', tcrop] + extra)
            task = open(os.path.join(t, 'task.txt')).read()
            assert BRIEF in task and 'truth' not in task.lower()
            assert ('feedback.tsv' in task) == (arm == 'F') and ('wrong' in task) == (arm == 'F')
            assert os.path.exists(os.path.join(t, 'feedback.tsv')) == (arm == 'F')
            assert os.path.exists(os.path.join(t, 'target', 'f_L01.jpg')) and os.path.exists(os.path.join(t, 'calib', 'c_L01.jpg'))


if __name__ == '__main__':
    test_feedback_rows(); test_build_and_target_name_no_truth(); print('ok')
