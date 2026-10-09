"""Offline test for tools/tx_pair_clf.py (TXE2-PAIR, 9 Oct 2026): synthetic 2-class tiles (vertical vs horizontal bar)
over four training leaves; train enables the pair with LOLO accuracy 1.0 (threshold chosen leave-one-leaf-out); apply
flips a no.87 position whose L read is the wrong pair member and keeps the rest; the map's truth column is refused;
a permuted-label control is near chance. No network, no model."""
import io, os, sys, tempfile, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import tx_pair_clf as T


def _w(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as f:
        f.write(text)


def _tile(kind, rng):
    a = np.zeros((48, 48), np.uint8)
    o = rng.integers(-3, 4)
    if kind == 'V':
        a[8:40, 22 + o:26 + o] = 255
    else:
        a[22 + o:26 + o, 8:40] = 255
    a[rng.integers(0, 48, 20), rng.integers(0, 48, 20)] = 255
    return a


def _setup(d):
    rng = np.random.default_rng(0)
    at = os.path.join(d, 'atlas')
    sig, sec, bms = 'sid\tpage\n', 'sid\tcode\tpage\tgrade\n', []
    for leaf in ('f100r', 'f101r', 'f102r', 'f103r'):
        for k in range(6):
            sid = f'{leaf}_01_{k:03d}'
            code = 'T18' if k % 2 else 'T98'
            bms.append(_tile('V' if code == 'T18' else 'H', rng))
            sig += f'{sid}\t{leaf}\n'
            sec += f'{sid}\t{code}\t{leaf}\tS\n'
    # unit boxes on f178v: pos1 vertical read as T98 (L wrong), pos2 horizontal read T98, pos3 not in a pair
    for k, kind in enumerate('VHV', 1):
        bms.append(_tile(kind, rng))
        sig += f'f178v_01_{k:03d}\tf178v\n'
    _w(os.path.join(at, 'signs.tsv'), sig)
    _w(os.path.join(at, 'secure_tokens.tsv'), sec)
    np.savez_compressed(os.path.join(at, 'bitmaps.npz'), signs=np.stack(bms), marks=np.zeros((0, 48, 48), np.uint8))
    _w(os.path.join(at, 'map.tsv'), 'sid\tfol\tline\tpos\tidx\tsign\ttruth\top\tsplit\n' +
       ''.join(f'f178v_01_{k:03d}\tf178v\tf178v_L01\t{k}\t{k}\tX\tSECRET\t1:1\ttune\n' for k in (1, 2, 3)))
    _w(os.path.join(d, 'units', 'labels_dev_tune.tsv'), 'line\tpos\tsign\nf178v_L01\t1\tT98\nf178v_L01\t2\tT98\nf178v_L01\t3\tT37\n')
    return at


def _rd(p):
    return [l.split('\t') for l in open(p).read().split('\n')[1:] if l]


def test_train_apply_control():
    with tempfile.TemporaryDirectory() as d:
        at = _setup(d)
        res, *_ = T.train_pairs(at)
        m, info = res['T18/T98']
        assert info['enabled'] == 1 and info['lolo_acc'] == '1.000' and info['leaves'] == 4, info
        assert res['T90/T53'][1]['enabled'] == 0
        args = ['--atlas', at, '--unit', 'dev_tune', '--units', os.path.join(d, 'units'), '--map',
                os.path.join(at, 'map.tsv'), '--out-dir', d, '--touched-dir', d]
        with contextlib.redirect_stdout(io.StringIO()):
            assert T.main(['apply'] + args) == 0
        out = _rd(os.path.join(d, 'passX2_pair_dev_tune.tsv'))
        assert [r[2] for r in out] == ['T18', 'T98', 'T37'], out
        # permuted-label control: LOLO accuracy near chance over seeds
        accs = [float(T.train_pairs(at, s)[0]['T18/T98'][1]['lolo_acc'] or 0.5) for s in range(1, 6)]
        assert np.mean(accs) < 0.85, accs


def test_truth_refused():
    with tempfile.TemporaryDirectory() as d:
        at = _setup(d)
        try:
            T.read_named(os.path.join(at, 'map.tsv'), ('sid', 'truth'))
        except SystemExit:
            pass
        else:
            raise AssertionError('truth column was read')
        rows = T.read_named(os.path.join(at, 'map.tsv'), T.MAP_COLS)
        assert 'truth' not in rows[0] and rows[0]['sid'] == 'f178v_01_001'


if __name__ == '__main__':
    test_train_apply_control(); test_truth_refused(); print('ok')
