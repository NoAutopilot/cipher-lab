"""Offline test for benchmark-tx/truth_variant.py (TXP-REBUILD, PREREG-txeng2-2 R): key_print inverse with merged reader
labels, the keyprint/jackknife classes, and the four build scripts' --variant --check (rule 7)."""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'benchmark-tx'))
import truth_variant as tv  # noqa: E402


def fold(s):
    return ''.join(c for c in s.lower() if c.isalpha())


def test_kp_inverse_merged_labels():
    S = tv.kp_inverse(fold)
    assert '4' in S['a'] and '4' in S['l']          # D -> 4 merged, 4 itself = l
    assert 'a' in S['u'] and 'a' in S['q']          # al -> a merged, a itself = q
    assert '0' not in S.get('e', set()) and '.' in S['e']   # 0: 11/18 < 0.75; '.': 9/9
    assert 'B' not in S.get('a', set())             # n 1 < 3


def test_rows_classes():
    tr = [('L1', 0, '1', 'code', '1', '', 'e', 'agrees'), ('L1', 1, '2', 'code', '2', '', 'e', 'agrees'),
          ('L1', 2, '3', 'code', '3', '', 'z', 'conflict:x'), ('L1', 3, '4', 'code', '4', '', '?', 'agrees'),
          ('L2', 0, '1', 'code', '1', '', 'e', 'agrees'), ('L2', 1, '2', 'code', '2', '', 'e', 'agrees')]
    keys = [('L1', 1, '.'), ('L1', 2, 'y'), ('L1', 3, 'q'), ('L1', 4, 'f'), ('L2', 1, '.'), ('L2', 2, '.')]
    r = tv.keyprint_rows(tr, keys, lambda c: '?' in c, fold)
    assert r[0][5] == 'scored' and '.' in r[0][3].split('|')
    assert r[1][5] == 'excluded:align-uncertain'     # neighbour conflict, whatever its own status
    assert r[3][5] == 'excluded:gloss-unread'
    j = tv.jackknife_rows(tr, keys, lambda c: '?' in c, fold, lambda s: s.startswith('NEW'))
    assert j[0][5] == 'scored' and j[0][3] == '.'    # L1 scored with L2's key: '.' = e, n 2
    assert j[4][5] == 'excluded:letter-no-jackknife-sign'  # L2 scored with L1's key: '.' = e only n 1 < 2


def test_builds_check():
    for f, v in (('build_dint-f89-gloss.py', 'keyprint'), ('build_dint-f98v-gloss.py', 'keyprint'),
                 ('build_dint-f113-gloss.py', 'keyprint'), ('build_bir1591-f23r-gloss.py', 'jackknife')):
        p = subprocess.run([sys.executable, os.path.join(ROOT, 'benchmark-tx', f), '--variant', v, '--check'],
                           capture_output=True, text=True)
        assert p.returncode == 0, (f, p.stdout, p.stderr)


if __name__ == '__main__':
    test_kp_inverse_merged_labels(); test_rows_classes(); test_builds_check(); print('ok')
