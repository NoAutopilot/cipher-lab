"""Offline test for tools/tx_pair_reread.py (TXE-C, LANE TX-ENGINEER round 2, 9 Oct 2026): a synthetic page with a
hairline, a mid stroke and a blob; the hairline's line-read sign is in a listed pair, so select returns exactly that
box, build writes one sheet and its key, resolve applies A/B and keeps L on neither. No network, no model."""
import io, os, sys, csv, tempfile, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from PIL import Image
import tx_pair_reread as T


def _w(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as f:
        f.write(text)


def _page(shape, draw):
    a = np.full(shape, 245, np.uint8)
    for fn in draw:
        fn(a)
    return a


def _setup(d):
    folder = os.path.join(d, 'tgt')
    # unit page f178v: line 1 has three 40x40 boxes at x=20, 80, 140
    def hair(a): a[25:55, 39] = 20; a[39, 25:55] = 20            # 1-px cross: nothing survives a 3x3 erosion
    def mid(a): a[25:55, 98:101] = 20; a[38:41, 85:115] = 20     # 3-px cross: the centre lines survive
    def blob(a): a[25:55, 145:175] = 20                          # solid block: almost all survives
    pg = _page((80, 200), [hair, mid, blob])
    os.makedirs(os.path.join(folder, 'harvest', 'f178v'))
    Image.fromarray(pg).save(os.path.join(folder, 'harvest', 'f178v', 'src_page.jpg'), quality=98)
    # exemplar page f100r with four boxes
    ex = _page((80, 260), [lambda a: a.__setitem__((slice(25, 55), slice(30 + 60 * i, 33 + 60 * i)), 20) for i in range(4)])
    os.makedirs(os.path.join(folder, 'harvest', 'f100r'))
    Image.fromarray(ex).save(os.path.join(folder, 'harvest', 'f100r', 'src_page.jpg'), quality=98)
    sig = 'sid\tpage\tline\tpos\tx\ty\tw\th\trh\trw\tdy\tmarks\n'
    for i, x in enumerate((20, 80, 140), 1):
        sig += f'f178v_01_00{i}\tf178v\t1\t{i}\t{x}\t20\t40\t40\t1\t1\t0\t\n'
    for i in range(4):
        sig += f'f100r_01_00{i + 1}\tf100r\t1\t{i + 1}\t{20 + 60 * i}\t20\t40\t40\t1\t1\t0\t\n'
    _w(os.path.join(folder, 'atlas', 'signs.tsv'), sig)
    _w(os.path.join(folder, 'atlas', 'sheet_truth', 'sheet.tsv'),
       'code\tn_secure\tshown\texemplars\nT18\t2\thand\tf100r_01_001,f100r_01_002,f178v_01_003\n'
       'T98\t2\thand\tf100r_01_003,f100r_01_004\nT60\t1\thand\tf100r_01_001\nT86\t1\thand\tf100r_01_002\n')
    lr = os.path.join(d, 'L.tsv')
    # the hairline reads T18 (pair T18/T98); the mid stroke reads T60 (a pair too, but not thin); the blob T37
    _w(lr, 'line\tpos\tsign\nf178v_L01\t1\tT18\nf178v_L01\t2\tT60\nf178v_L01\t3\tT37\nf178v_L02\t1\tT37\n')
    units = os.path.join(d, 'units')
    _w(os.path.join(units, 'labels_dev_tune.tsv'), 'line\tpos\tsign\nf178v_L01\t1\tT18\nf178v_L01\t2\tT60\nf178v_L01\t3\tT37\n')
    out = os.path.join(d, 'out')
    return ['--unit', 'dev_tune', '--folder', folder, '--line-read', lr, '--units', units, '--out', out,
            '--confusion', os.path.join(d, 'none.tsv')], out


def _run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = T.main(argv)
    return rc, buf.getvalue()


def test_select_build_resolve():
    with tempfile.TemporaryDirectory() as d:
        common, out = _setup(d)
        rc, txt = _run(['select'] + common)
        assert rc == 0, txt
        rows = list(csv.DictReader(open(os.path.join(out, 'dev_tune', 'box_pos.tsv')), delimiter='\t'))
        es = {r['sid']: float(r['es']) for r in rows}
        assert es['f178v_01_001'] < es['f178v_01_002'] < es['f178v_01_003'], es
        sel = list(csv.DictReader(open(os.path.join(out, 'dev_tune', 'selected.tsv')), delimiter='\t'))
        assert [(r['sid'], r['L'], r['partner']) for r in sel] == [('f178v_01_001', 'T18', 'T98')], sel
        rc, txt = _run(['build'] + common)
        assert rc == 0 and '1 rows on 1 sheet' in txt, txt
        key = list(csv.DictReader(open(os.path.join(out, 'dev_tune', 'sheet_01.tsv')), delimiter='\t'))
        assert len(key) == 1 and {key[0]['A'], key[0]['B']} == {'T18', 'T98'}
        assert os.path.exists(os.path.join(out, 'dev_tune', 'sheet_01.png'))
        dest = os.path.join(d, 'J.tsv')
        partner_row = 'A' if key[0]['A'] == 'T98' else 'B'
        for pick, want in ((partner_row, 'T98'), ('neither', 'T18'), ('?', 'T18')):
            _w(os.path.join(out, 'dev_tune', 'reads_01.tsv'), f'row\tpick\tconf\tfeature\n1\t{pick}\tH\tx\n')
            rc, txt = _run(['resolve'] + common + ['--dest', dest])
            assert rc == 0, txt
            got = {(r['line'], r['pos']): r['sign'] for r in csv.DictReader(open(dest), delimiter='\t')}
            assert got == {('f178v_L01', '1'): want, ('f178v_L01', '2'): 'T60', ('f178v_L01', '3'): 'T37'}, (pick, got)


def test_partner_rule():
    part, unusable = T.pair_partners({'T76', 'T86', 'T45', 'T18', 'T98'}, None)
    assert part['T76'] == 'T86'            # tie at count 0 -> pair-list order (T76/T86 before T76/T45)
    assert part['T45'] == 'T76' and part['T18'] == 'T98'
    assert 'T76/T66' in unusable and 'T64' not in part


if __name__ == '__main__':
    test_select_build_resolve(); test_partner_rule(); print('ok')
