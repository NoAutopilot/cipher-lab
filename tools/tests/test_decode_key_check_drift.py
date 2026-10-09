"""Offline test (TOOL-CHK, 9 Oct 2026): decode_key.py --check exits 1 on grade-only drift (a key.tsv grade changed, the
committed reading not regenerated), also when --check is combined with a report mode (--consistency, --split-check, ...);
and exits 0 on an unchanged regeneration. Must NOT block: an up-to-date reading, with or without a report flag."""
import os, shutil, subprocess, sys, tempfile
TOOL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'decode_key.py')
KEY = 'code\tvalue\tgrade\tsource\tnote\n1\ta\tC\tt\t\n2\tb\tC\tt\t\n'
CT = 'line\tpos\tsign\tconf\n' + ''.join(f'L{i}\t1\t{c}\thigh\n' for i, c in enumerate('1212', 1))


def run(d, *flags):
    return subprocess.run([sys.executable, TOOL, d, *flags], capture_output=True, text=True).returncode


def mk():
    d = tempfile.mkdtemp()
    open(os.path.join(d, 'ciphertext.tsv'), 'w').write(CT)
    open(os.path.join(d, 'key.tsv'), 'w').write(KEY)
    open(os.path.join(d, 'decode.json'), 'w').write(
        '{"jobs": [{"ciphertext": "ciphertext.tsv", "key": "key.tsv", "reading": "reading.txt", '
        '"tokens": "reading_tokens.tsv", "style": "spaced"}]}')
    assert run(d) == 0
    return d


def test_unchanged_not_blocked():
    d = mk()
    try:
        assert run(d, '--check') == 0
        assert run(d, '--check', '--split-check') == 0
    finally:
        shutil.rmtree(d)


def test_grade_only_drift_caught():
    d = mk()
    try:
        k = os.path.join(d, 'key.tsv')
        open(k, 'w').write(open(k).read().replace('1\ta\tC', '1\ta\tM'))
        assert run(d, '--check') == 1
        assert run(d, '--check', '--split-check') == 1
        assert run(d, '--check', '--consistency') == 1
    finally:
        shutil.rmtree(d)


if __name__ == '__main__':
    test_unchanged_not_blocked(); test_grade_only_drift_caught(); print('ok')
