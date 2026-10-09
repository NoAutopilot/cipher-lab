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


def _windows(out):
    rows = (out / 'contexts.tsv').read_text().splitlines()
    h = rows[0].split('\t')
    return [dict(zip(h, r.split('\t'))) for r in rows[1:]]


def test_clear_aware_island_leaf(tmp_path=None):
    """Synthetic island leaf: code 200 sits in one-token cipher runs between clear words. Without --clear-aware its
    window splices letters of the neighbouring cipher runs; with it, the window is the real clear context. Runs,
    AD and control (i) must not change between the two modes."""
    d = Path(tempfile.mkdtemp())
    corp = d / 'corp'; corp.mkdir()
    with gzip.open(corp / 'c.txt.gz', 'wt') as f:
        f.write('on dit que la reine touchant le prince ne donne contentement a personne et la paix\n' * 200)
    key = d / 'key.tsv'
    letters = 'abcdefghilmnopqrstuvxyz'
    key.write_text('code\tvalue\tgrade\n' + ''.join(f'{i}\t{c}\tC\n' for i, c in enumerate(letters, 1)) + '200\tla reine\tC\n')
    code = {c: str(i) for i, c in enumerate(letters, 1)}
    runs = [('R1', ['la reine']), ('R2', list('paix')), ('R3', ['la reine']), ('R4', list('xyz'))]
    tok = ['line\tpos\tsign\tconf\tvalue\tgrade']
    for line, vals in runs:
        for i, v in enumerate(vals, 1):
            tok.append(f'{line}\t{i}\t{code.get(v, "200")}\tmed\t{v}\tC')
    (d / 't.tsv').write_text('\n'.join(tok) + '\n')
    (d / 'stream.tsv').write_text('kind\tvalue\n' + '\n'.join([
        'clear\ton dit que', 'run\tR1', 'clear\ttouchant le prince', 'gap', 'clear\tet la', 'run\tR2',
        'gap', 'clear\tcontentement a', 'run\tR3', 'clear\tne donne', 'gap', 'run\tR4']) + '\n')
    base = ['--tokens', str(d / 't.tsv'), '--key', str(key), '--cipher-class', 'code<=120',
            '--shuffle', 'classes', '--seeds', '1-20', '--corpus', str(corp)]
    assert ds.main(base + ['--out', str(d / 'plain')]) == 0
    assert ds.main(base + ['--out', str(d / 'clear'), '--clear-aware', str(d / 'stream.tsv')]) == 0
    wp, wc = _windows(d / 'plain'), _windows(d / 'clear')
    assert [r['window'] for r in wp] == ['lareinepaixlare', 'einepaixlareinexyz']
    assert [r['window'] for r in wc] == ['onditquelareinetouchant', 'ntementalareinenedonne|x']
    assert all(a['window'] != b['window'] and a['target'] != b['target'] for a, b in zip(wp, wc))
    sp, sc = (json.load(open(d / m / 'summary.json')) for m in ('plain', 'clear'))
    assert sc['clear_aware'] and sp['clear_aware'] is None
    # code 200 is the only code-class value, so under --shuffle classes the all-clear first window cannot move
    assert [r['shuffle_varies'] for r in wc] == ['False', 'True'] and wp[0]['shuffle_varies'] == 'True'
    for k in ('primary_run', 'secondary_run', 'AD', 'stat_i_target', 'stat_i_p95', 'H_K'):
        assert sp[k] == sc[k], k
    # a run line left out of the stream is an error, not a silent splice
    (d / 'bad.tsv').write_text('run\tR1\nrun\tR2\nrun\tR3\n')
    try:
        ds.main(base + ['--out', str(d / 'bad'), '--clear-aware', str(d / 'bad.tsv')])
        assert False, 'missing run line accepted'
    except SystemExit as e:
        assert 'R4' in str(e)


if __name__ == '__main__':
    test_longest_segmentable(); test_window_skips_gaps(); test_end_to_end(); test_m_through()
    test_clear_aware_island_leaf(); print('ok')
