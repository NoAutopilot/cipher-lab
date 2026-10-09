"""Offline test for tools/tx_taxonomy.py (LANE TX-ENGINEER round 1, 9 Oct 2026): per-position features and error classes."""
import io, os, sys, tempfile, contextlib, csv
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_taxonomy


def _w(d, name, text):
    p = os.path.join(d, name)
    with open(p, 'w') as f:
        f.write(text)
    return p


def test_positions_and_classes():
    with tempfile.TemporaryDirectory() as d:
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\n'
           'f1_L01\t1\tA\tA\ta\tscored\nf1_L01\t2\tB\tB|C\tb\tscored\nf1_L01\t3\tD\tD\td\tscored\n'
           'f1_L01\t4\tE\tE\te\tscored\nf1_L01\t5\tX\t\t\texcluded:off-sheet\nf1_L02\t1\tF\tF\tf\tscored\nf1_L02\t2\tG\tG\tg\tscored\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\t%s\teval\n' % os.path.join(d, 't.truth.tsv'))
        pa = _w(d, 'A.tsv', 'line\tpos\tsign\nf1_L01\t1\tA\nf1_L01\t2\tC\nf1_L01\t3\tZ\nf1_L01\t4\tE\nf1_L01\t5\tX\nf1_L02\t1\tQ\nf1_L02\t2\tG\n')
        pb = _w(d, 'B.tsv2', 'line\tpos\tsign\nf1_L01\t1\tA\nf1_L01\t2\tB\nf1_L01\t3\tZ\nf1_L01\t4\tE\nf1_L01\t5\tX\nf1_L02\t2\tG\n')
        out = os.path.join(d, 'o.tsv'); md = os.path.join(d, 'o.md')
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = tx_taxonomy.main(['--bench', bench, '--item', 'it1', '--pass', 'A=' + pa, '--pass', 'B=' + pb,
                                   '--call-lines', 'f1_L01-02', '--out-tsv', out, '--md', md])
        assert rc == 0
        rows = list(csv.DictReader(open(out), delimiter='\t'))
        assert len(rows) == 6, rows                      # 6 scored, the excluded one dropped
        by = {(r['line'], r['pos']): r for r in rows}
        assert by[('f1_L01', '2')]['err_A'] == '0'       # homophone C is in the truth set
        assert by[('f1_L01', '3')]['err_A'] == '1' and by[('f1_L01', '3')]['err_B'] == '1'
        assert by[('f1_L01', '3')]['same_wrong'] == '1' and by[('f1_L01', '3')]['n_wrong'] == '2'
        assert by[('f1_L02', '1')]['read_B'] == '<deleted>' and by[('f1_L02', '1')]['pos_class'] == 'first'
        assert by[('f1_L01', '4')]['pos_class'] == 'inner'  # pos 5 (excluded) is the line's last position
        assert by[('f1_L02', '2')]['pos_class'] == 'last'
        assert by[('f1_L02', '1')]['line_in_call'] == '2' and by[('f1_L01', '1')]['line_in_call'] == '1'
        assert by[('f1_L01', '1')]['seg_edge'] == '-'     # no geometry given
        text = open(md).read()
        assert 'd <- Z' in text and 'Error correlation' in text and '2/2 (1)' in text


def test_geometry_and_label_map():
    import numpy as np
    from PIL import Image
    with tempfile.TemporaryDirectory() as d:
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\n'
           'f1_L01\t1\tA\tA\ta\tscored\nf1_L01\t2\tB\tB\tb\tscored\nf1_L01\t3\tD\tD\td\tscored\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\t%s\teval\n' % os.path.join(d, 't.truth.tsv'))
        pa = _w(d, 'A.tsv', 'line\tpos\tsign\nf1_L01\t1\tA\nf1_L01\t2\tB\nf1_L01\t3\tDD\n')
        lm = _w(d, 'lm.tsv', 'from\tto\nDD\tD\n')
        boxes = _w(d, 'signs.tsv', 'sid\tpage\tline\tpos\tx\ty\tw\th\n'
                   'f1_01_001\tf1\t1\t1\t5\t20\t20\t20\nf1_01_002\tf1\t1\t2\t185\t10\t10\t20\nf1_01_003\tf1\t1\t3\t300\t5\t20\t60\n')
        bt = _w(d, 'bt.tsv', 'sid\tfol\tline\tpos\tidx\tsign\ttruth\top\tsplit\n'
                'f1_01_001\tf1\tf1_L01\t1\t0\tA\ta\t1:1\ttune\nf1_01_002\tf1\tf1_L01\t2\t1\tB\tb\t2:1\ttune\nf1_01_003\tf1\tf1_L01\t3\t2\tD\td\t1:1\ttune\n')
        os.makedirs(os.path.join(d, 'h', 'f1'))
        # page origin (100, 100); two segment crops of width 200 overlapping 20 px, band y 100..160 in canvas = 0..60 page
        _w(os.path.join(d, 'h', 'f1'), 'manifest.json', '{"iiif_lines": [' +
           '{"crop": "f1_L01_s1.jpg", "source_file": "src_ark_x_f1_100_100_500_200.jpg", "box": [100, 100, 300, 160]},' +
           '{"crop": "f1_L01_s2.jpg", "source_file": "src_ark_x_f1_100_100_500_200.jpg", "box": [280, 100, 480, 160]}]}')
        page = np.full((200, 500), 255, np.uint8)
        page[25:35, 5:25] = 0           # a thick blob for sign 1
        page[15:16, 185:195] = 0         # a hairline for sign 2
        page[10:60, 305:312] = 0         # a mid stroke for sign 3
        Image.fromarray(page).save(os.path.join(d, 'h', 'f1', 'src_ark_x_f1_100_100_500_200.jpg'))
        out = os.path.join(d, 'o.tsv')
        with contextlib.redirect_stdout(io.StringIO()):
            rc = tx_taxonomy.main(['--bench', bench, '--item', 'it1', '--pass', 'A=' + pa, '--label-map', lm,
                                   '--boxes', boxes, '--box-token', bt, '--harvest', os.path.join(d, 'h'), '--out-tsv', out])
        assert rc == 0
        by = {r['pos']: r for r in csv.DictReader(open(out), delimiter='\t')}
        assert by['3']['err_A'] == '0'                  # label map DD -> D
        assert by['1']['seg_edge'] == 'edge'            # x 5 is within 5% (10 px) of the s1 left border (page x 0)
        assert by['2']['seg_edge'] == 'overlap'         # centre x 190 lies in s1 (0..200) and s2 (180..380)
        assert by['2']['glued'] == '2:1'
        assert by['3']['band_edge'] == 'cut'            # y 5..65 exceeds the band 0..60
        assert by['1']['stroke'] == 'heavy' and by['2']['stroke'] == 'thin'


def test_agreement_columns():
    """3 passes (A baseline): pos 1 all-same-wrong, pos 2 all-wrong-split, pos 3 baseline-only, pos 4 right,
    pos 5 majority-wrong; L02 is covered by A only (no-other-pass); pos 1's pair recurs at L02 -> look-alike."""
    with tempfile.TemporaryDirectory() as d:
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\n'
           'f1_L01\t1\tA\tA\ta\tscored\nf1_L01\t2\tB\tB\tb\tscored\nf1_L01\t3\tD\tD\td\tscored\n'
           'f1_L01\t4\tE\tE\te\tscored\nf1_L01\t5\tG\tG\tg\tscored\nf1_L02\t1\tA\tA\ta\tscored\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\t%s\teval\n' % os.path.join(d, 't.truth.tsv'))
        pa = _w(d, 'a.tsv', 'line\tpos\tsign\nf1_L01\t1\tZ\nf1_L01\t2\tY\nf1_L01\t3\tW\nf1_L01\t4\tE\nf1_L01\t5\tV\nf1_L02\t1\tZ\n')
        pb = _w(d, 'b.tsv', 'line\tpos\tsign\nf1_L01\t1\tZ\nf1_L01\t2\tX\nf1_L01\t3\tD\nf1_L01\t4\tE\nf1_L01\t5\tV\n')
        pc = _w(d, 'c.tsv', 'line\tpos\tsign\nf1_L01\t1\tZ\nf1_L01\t2\tY\nf1_L01\t3\tD\nf1_L01\t4\tE\nf1_L01\t5\tG\n')
        out = os.path.join(d, 'o.tsv'); md = os.path.join(d, 'o.md')
        with contextlib.redirect_stdout(io.StringIO()):
            rc = tx_taxonomy.main(['--bench', bench, '--item', 'it1', '--pass', 'A=' + pa, '--pass', 'B=' + pb,
                                   '--pass', 'C=' + pc, '--out-tsv', out, '--md', md])
        assert rc == 0
        rows = list(csv.DictReader(open(out), delimiter='\t'))
        assert list(rows[0])[-4:] == ['n_pass_wrong', 'n_same_wrong', 'agree_class', 'err_class']
        by = {(r['line'], r['pos']): r for r in rows}
        r = by[('f1_L01', '1')]
        assert (r['agree_class'], r['n_pass_wrong'], r['n_same_wrong'], r['err_class']) == ('all-same-wrong', '3', '3', 'look-alike')
        r = by[('f1_L01', '2')]
        assert (r['agree_class'], r['n_pass_wrong'], r['n_same_wrong']) == ('all-wrong-split', '3', '2')
        r = by[('f1_L01', '3')]
        assert (r['agree_class'], r['n_pass_wrong'], r['n_same_wrong'], r['err_class']) == ('baseline-only', '1', '1', 'other')
        assert by[('f1_L01', '4')]['agree_class'] == 'right' and by[('f1_L01', '4')]['err_class'] == ''
        assert by[('f1_L01', '5')]['agree_class'] == 'majority-wrong'
        assert by[('f1_L02', '1')]['agree_class'] == 'no-other-pass'
        text = open(md).read()
        assert 'Reader agreement on the baseline\'s errors (baseline A; 5 errors' in text
        assert '| all-same-wrong | 1 | 20.0% |' in text and '| a <- Z | 2 | look-alike 2 |' in text


if __name__ == '__main__':
    test_positions_and_classes(); test_geometry_and_label_map(); test_agreement_columns(); print('ok')
