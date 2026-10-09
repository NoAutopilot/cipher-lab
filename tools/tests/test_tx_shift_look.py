#!/usr/bin/env python3
"""Offline test for tools/tx_shift_look.py (TXE-N): a synthetic page cut by tools/iiif_lines.py into S0 and a
shifted S1 set; two reads differing in one substitution and one deletion give two rows, the row images exist, the
option order is in key.tsv only, and resolve applies 1/2, a third cell and ? (-> S0) correctly.
Run: python3 tools/tests/test_tx_shift_look.py"""
import contextlib, io, os, shutil, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import iiif_lines as il, tx_shift_look as tl
from PIL import Image, ImageDraw
fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)
tmp = tempfile.mkdtemp()
try:
    W, P = 1800, 100
    im = Image.new('L', (W, 4 * P), 235); d = ImageDraw.Draw(im)
    rows = ['sid\tpage\tline\tpos\tx\ty\tw\th']
    for li in range(3):
        cy = 80 + li * P
        for k, x in enumerate(range(40, W - 60, 70)):
            d.rectangle([x, cy - 22, x + 30, cy + 22], fill=20)
            rows.append(f'z_{li}_{k}\tz\t{li + 1}\t{k + 1}\t{x}\t{cy - 22}\t30\t44')
    src = os.path.join(tmp, 'p.png'); im.save(src)
    sig = os.path.join(tmp, 'signs.tsv'); open(sig, 'w').write('\n'.join(rows) + '\n')
    c0, c1 = os.path.join(tmp, 's0'), os.path.join(tmp, 's1')
    with contextlib.redirect_stdout(io.StringIO()):
        il.main(['--image', src, '--out', c0, '--prefix', 'z', '--max-width', '800', '--centres', '80,180,280',
                 '--band-extent', '0.1', '--mask-neighbours', '--only-lines', '1,2'])
        il.main(['--image', src, '--out', c1, '--prefix', 'z', '--max-width', '800', '--centres', '80,180,280',
                 '--band-extent', '0.1', '--mask-neighbours', '--shift-bands', '0.5', '--shift-segments', '0.5',
                 '--only-lines', '1,2'])
    n = len(range(40, W - 60, 70))
    a0 = ['line\tpos\tsign'] + [f'z_L01\t{k + 1}\tT{10 + k % 5}' for k in range(n)]
    s1 = [f'T{10 + k % 5}' for k in range(n)]; s1[5] = 'T99'; del s1[12]
    a1 = ['line\tpos\tsign'] + [f'z_L01\t{k + 1}\t{s}' for k, s in enumerate(s1)]
    p0, p1 = os.path.join(tmp, 'a0.tsv'), os.path.join(tmp, 'a1.tsv')
    open(p0, 'w').write('\n'.join(a0) + '\n'); open(p1, 'w').write('\n'.join(a1) + '\n')
    out = os.path.join(tmp, 'look')
    with contextlib.redirect_stdout(io.StringIO()):
        r = tl.main(['build', '--s0', p0, '--s1', p1, '--crops0', c0, '--crops1', c1, '--signs', sig, '--page', 'z',
                     '--out', out, '--seed', '3'])
    check(len(r) == 2, f'two disagreement rows (got {len(r)})')
    check(all(os.path.exists(x['img']) for x in r), 'row images written')
    sh = open(os.path.join(out, 'sheet_01.md')).read()
    check('s0' not in sh and 's1' not in sh.replace('_s1', ''), 'sheet does not say which read is which')
    check(abs(r[0]['xc'] - (40 + 5 * 70 + 15)) < 5, f"x estimate on the right box ({r[0]['xc']})")
    key = {x['row']: x for x in r}
    sub = [x for x in r if x['s1'] == 'T99'][0]; dele = [x for x in r if not x['s1']][0]
    pick_sub = '1' if sub['opt1'][0] == 's1' else '2'
    ans = os.path.join(tmp, 'ans.tsv'); open(ans, 'w').write(f"row\tpick\n{sub['row']}\t{pick_sub}\n{dele['row']}\t?\n")
    w = os.path.join(tmp, 'out.tsv')
    with contextlib.redirect_stdout(io.StringIO()):
        o, picks = tl.main(['resolve', '--s0', p0, '--s1', p1, '--out', out, '--answers', ans, '--write', w])
    seq = [s for _, _, s in o]
    check(seq[5] == 'T99' and len(seq) == n, 'pick of the S1 option applied; ? keeps the S0 sign')
    open(ans, 'w').write(f"row\tpick\n{sub['row']}\tT42\n{dele['row']}\t{'1' if dele['opt1'][0] == 's1' else '2'}\n")
    with contextlib.redirect_stdout(io.StringIO()):
        o, _ = tl.main(['resolve', '--s0', p0, '--s1', p1, '--out', out, '--answers', ans, '--write', w])
    seq = [s for _, _, s in o]
    check(seq[5] == 'T42' and len(seq) == n - 1, 'a third cell applied; choosing the gap drops the sign')
finally:
    shutil.rmtree(tmp)
print('tx_shift_look:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
