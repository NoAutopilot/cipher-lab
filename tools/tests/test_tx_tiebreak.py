"""Offline test for tools/tx_tiebreak.py (TXE4-6, 12 Oct 2026): a synthetic two-class atlas with planted splits.
The 24-tile atlas uses --pca-scale shared: under 'unit' every PCA component is standardised and a 24-tile atlas makes all
tiles equidistant (glyph_atlas.feats's own small-sample caveat); the real runs keep classify's default 'unit'."""
import contextlib, io, json, os, sys, tempfile
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_tiebreak as TT
import join_check as JC


def _w(d, name, text):
    p = os.path.join(d, name)
    with open(p, 'w') as f:
        f.write(text)
    return p


def _bitmap(kind, rnd):
    b = np.zeros((48, 48), np.uint8)
    if kind == 'V':
        b[6:42, 20:28] = 255
    else:
        b[20:28, 6:42] = 255
    noise = rnd.random((48, 48)) < 0.03
    b[noise] = 255 - b[noise]
    return b


def _atlas(d, n_lines=4, per_line=6, seed=1):
    """Lines L01..L0n of page p; pos 1..per_line; even pos 'V' (sign a), odd pos 'H' (sign b)."""
    rnd = np.random.default_rng(seed)
    rows, bms, kinds = [], [], {}
    for li in range(1, n_lines + 1):
        for pos in range(1, per_line + 1):
            kind = 'V' if pos % 2 == 0 else 'H'
            sid = f'p_{li:02d}_{pos:03d}'
            rows.append(f'{sid}\tp\t{li}\t{pos}\t{pos * 60}\t{li * 80}\t40\t40\t1.0\t1.0\t0.0\t')
            bms.append(_bitmap(kind, rnd)); kinds[sid] = kind
    _w(d, 'signs.tsv', 'sid\tpage\tline\tpos\tx\ty\tw\th\trh\trw\tdy\tmarks\n' + '\n'.join(rows) + '\n')
    np.savez(os.path.join(d, 'bitmaps.npz'), signs=np.array(bms), marks=np.zeros((0, 48, 48), np.uint8))
    return kinds


def _setup(d):
    kinds = _atlas(d)
    # map: every box 1:1 at its own pos; PASS sidecar
    mp = _w(d, 'map.tsv', 'sid\tpage\tline\tpos\top\tlabels\tstatus\tloo_pos\told_pos\n' + ''.join(
        f'{sid}\tp\tp_L{sid[2:4]}\t{int(sid[5:])}\t1:1\t\t\t\t\n' for sid in kinds))
    JC.write_sidecar(mp, dict(verdict='PASS', n=24, overall={}, share0=1.0, sharepm1=0.0, lines={}, draws=0, seed=0))
    # readers agree everywhere (sign a at even pos, b at odd) except planted splits:
    #   L01 pos 2 (V box): A says a, B says b  -> a is right (V = a)
    #   L02 pos 3 (H box): A says a, B says b  -> b is right
    #   L03 pos 4 (V box): A says c (no agreed tile of c anywhere) -> undecidable
    draft, dis, base = [], [], []
    splits = {('p_L01', 2): ('a', 'b'), ('p_L02', 3): ('a', 'b'), ('p_L03', 4): ('c', 'b')}
    for li in range(1, 5):
        line = f'p_L{li:02d}'
        for pos in range(1, 7):
            truth = 'a' if pos % 2 == 0 else 'b'
            if (line, pos) in splits:
                A, B = splits[(line, pos)]
                draft.append(f'{line}\t{pos}\t{A}\tM\t{B}\tdisagree')
                dis.append(f'{line}\t{pos}\t{A}\t{B}\t\t')
                base.append(f'{line}\t{pos}\t{B}')      # the committed adjudicator took B everywhere
            else:
                draft.append(f'{line}\t{pos}\t{truth}\tH\t\tagree')
                base.append(f'{line}\t{pos}\t{truth}')
    _w(d, 'ciphertext_draft.tsv', 'line\tposition\tsign\tconfidence\talt\twhy\n' + '\n'.join(draft) + '\n')
    _w(d, 'disagreements.tsv', 'line\tcol\tA\tB\tflagged\tcrop\n' + '\n'.join(dis) + '\n')
    bp = _w(d, 'base.tsv', 'line\tpos\tsign\n' + '\n'.join(base) + '\n')
    return mp, bp


def _run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        dec = TT.main(argv)
    return dec, buf.getvalue()


def _rd(p):
    return TT.rd(p)


def test_planted_splits_settled_by_agreed_ink():
    with tempfile.TemporaryDirectory() as d:
        mp, bp = _setup(d)
        out = os.path.join(d, 'out.tsv')
        dec, txt = _run(['--atlas', d, '--map', mp, '--rec', d, '--base', bp, '--out', out, '--pca-scale', 'shared'])
        by = {(r['line'], r['col']): r for r in dec}
        assert by[('p_L01', '2')]['pick'] == 'a' and by[('p_L01', '2')]['applied'] == 'yes', by[('p_L01', '2')]
        assert by[('p_L02', '3')]['pick'] == 'b' and by[('p_L02', '3')]['applied'] == 'same', by[('p_L02', '3')]
        assert by[('p_L03', '4')]['reason'] == 'undecidable' and by[('p_L03', '4')]['applied'] == 'no'
        o = {(r['line'], r['pos']): r['sign'] for r in _rd(out)}
        assert o[('p_L01', '2')] == 'a' and o[('p_L02', '3')] == 'b' and o[('p_L03', '4')] == 'b'
        assert '1 overrides written' in txt, txt
        assert os.path.exists(os.path.join(d, 'out.decisions.tsv'))


def test_margin_above_every_row_writes_nothing():
    with tempfile.TemporaryDirectory() as d:
        mp, bp = _setup(d)
        out = os.path.join(d, 'out.tsv')
        dec, txt = _run(['--atlas', d, '--map', mp, '--rec', d, '--base', bp, '--out', out, '--margin', '1e9', '--pca-scale', 'shared'])
        assert all(r['applied'] == 'no' for r in dec)
        assert [r['sign'] for r in _rd(out)] == [r['sign'] for r in _rd(bp)]


def test_permuted_labels_and_coin_controls():
    with tempfile.TemporaryDirectory() as d:
        mp, bp = _setup(d)
        out = os.path.join(d, 'out.tsv')
        dec0, _ = _run(['--atlas', d, '--map', mp, '--rec', d, '--base', bp, '--out', out, '--pca-scale', 'shared'])
        picks = set()
        for s in range(1, 9):
            dec, _ = _run(['--atlas', d, '--map', mp, '--rec', d, '--base', bp, '--out', os.path.join(d, f'perm{s}.tsv'),
                           '--permute-seed', str(s), '--pca-scale', 'shared'])
            picks.add(tuple(r['pick'] for r in dec))
        assert len(picks) > 1, 'permuting the agreed labels never changed a pick'
        decc, txt = _run(['--atlas', d, '--map', mp, '--rec', d, '--base', bp, '--out', os.path.join(d, 'coin.tsv'),
                          '--coin-seed', '3', '--coin-from', os.path.join(d, 'out.decisions.tsv'), '--pca-scale', 'shared'])
        byc = {(r['line'], r['col']): r for r in decc}
        assert byc[('p_L01', '2')]['reason'] == 'coin' and byc[('p_L01', '2')]['pick'] in ('a', 'b')
        assert byc[('p_L02', '3')]['pick'] == '' and byc[('p_L03', '4')]['pick'] == ''   # only applied rows get a coin


def test_requires_checked_join():
    with tempfile.TemporaryDirectory() as d:
        mp, bp = _setup(d)
        os.remove(JC.sidecar_path(mp))
        try:
            _run(['--atlas', d, '--map', mp, '--rec', d, '--base', bp, '--out', os.path.join(d, 'o.tsv')])
        except SystemExit as e:
            assert e.code == 2
        else:
            raise AssertionError('a map without a join_check sidecar was accepted')


if __name__ == '__main__':
    for n, f in sorted(globals().items()):
        if n.startswith('test_') and callable(f):
            f(); print('ok', n)
    print('test_tx_tiebreak: all passed')
