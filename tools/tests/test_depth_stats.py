"""Offline test for tools/depth_stats.py (no network): segmentation, windows, runs and the end-to-end shuffle control."""
import gzip, json, os, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import depth_stats as ds


def test_longest_segmentable():
    w = {'la', 'reine', 'de', 'paix', 'a'}
    assert ds.longest_segmentable('xxlareinedexx', w) == 9
    assert ds.longest_segmentable('qqqq', w) == 0
    assert ds.stat_i('lapaix|reine', w) == 6


def test_window_skips_gaps():
    s, sp = ds.build_stream(['ab', None, 'cd', 'xyz', 'ef'])
    assert ds.window(s, sp[3], k=2) == 'cdxyzef'


def test_end_to_end(tmp_path=None):
    d = Path(tempfile.mkdtemp())
    corp = d / 'corp'; corp.mkdir()
    text = ('la reine a dit que la paix ne donne contentement a personne et la reine touchant le prince\n' * 200)
    with gzip.open(corp / 'c.txt.gz', 'wt') as f:
        f.write(text)
    key = d / 'key.tsv'
    rows = ['code\tvalue\tgrade'] + [f'{i}\t{c}\tC' for i, c in enumerate('abcdefghilmnopqrstuvxyz', 1)] + ['200\tla reine\tC']
    key.write_text('\n'.join(rows) + '\n')
    code = {v: k for k, v in (r.split('\t')[:2] for r in rows[1:])}
    seq = list('touchant') + ['la reine'] + list('ledit') + ['?'] + list('paix') + ['la reine'] + list('touchant')
    tok = ['line\tpos\tsign\tconf\tvalue\tgrade']
    for i, v in enumerate(seq):
        tok.append(f'L1\t{i}\t{code.get(v, "999")}\tmed\t{v}\t{"U" if v == "?" else "C"}')
    (d / 't.tsv').write_text('\n'.join(tok) + '\n')
    out = d / 'out'
    rc = ds.main(['--tokens', str(d / 't.tsv'), '--key', str(key), '--cipher-class', 'code<=120',
                  '--shuffle', 'classes', '--seeds', '1-20', '--out', str(out), '--corpus', str(corp)])
    assert rc == 0
    s = json.load(open(out / 'summary.json'))
    assert s['tokens'] == len(seq) and s['primary_run'] == 8 and s['secondary_run'] == 20 and s['cipher_clause'] is False
    assert s['recurring_codes']['200']['independent_contexts'] == 2
    assert s['primary_run_m_through'] == s['primary_run']  # no M token in this item


def test_m_through(tmp_path=None):
    d = Path(tempfile.mkdtemp())
    corp = d / 'corp'; corp.mkdir()
    with gzip.open(corp / 'c.txt.gz', 'wt') as f:
        f.write('la paix ne donne contentement a personne\n' * 300)
    key = d / 'key.tsv'
    key.write_text('code\tvalue\tgrade\n' + ''.join(f'{i}\t{c}\tC\n' for i, c in enumerate('abcdefghilmnopqrstuvxyz', 1)))
    code = {c: str(i) for i, c in enumerate('abcdefghilmnopqrstuvxyz', 1)}
    tok = ['line\tpos\tsign\tconf\tvalue\tgrade']
    for i, (v, g) in enumerate([(c, 'S') for c in 'paix'] + [('n', 'M')] + [(c, 'S') for c in 'edonne']):
        tok.append(f'L1\t{i}\t{code[v]}\tmed\t{v}\t{g}')
    (d / 't.tsv').write_text('\n'.join(tok) + '\n')
    out = d / 'out'
    assert ds.main(['--tokens', str(d / 't.tsv'), '--key', str(key), '--cipher-class', 'code<=120',
                    '--shuffle', 'all', '--seeds', '1-5', '--out', str(out), '--corpus', str(corp)]) == 0
    s = json.load(open(out / 'summary.json'))
    assert s['primary_run'] == 6 and s['primary_run_m_through'] == 11
    toks = (d / 't.tsv').read_text().splitlines()
    (d / 't2.tsv').write_text('\n'.join([toks[0]] + [r.replace('L1', 'L2', 1) if i > 2 else r for i, r in enumerate(toks[1:])]) + '\n')
    assert ds.main(['--tokens', str(d / 't2.tsv'), '--key', str(key), '--cipher-class', 'code<=120', '--break-lines',
                    '--shuffle', 'all', '--seeds', '1-5', '--out', str(out), '--corpus', str(corp)]) == 0
    s = json.load(open(out / 'summary.json'))
    assert s['primary_run'] == 6 and s['primary_run_m_through'] == 8
    assert s['stat_i_target'] >= s['stat_i_p95']


if __name__ == '__main__':
    test_longest_segmentable(); test_window_skips_gaps(); test_end_to_end(); test_m_through(); print('ok')
