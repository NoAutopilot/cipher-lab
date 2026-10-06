#!/usr/bin/env python3
"""Offline test for tools/sorter_preflight.py (SORTER-PREFLIGHT, 6 Oct 2026). Three fixture pages built through
tools/sign_sorter.py on a synthetic two-line page: a good page (PASS); a wrong-line page, the Oldenbarnevelt v1 shape
(tiles on a line that is not in the cipher-line list, clear words before the cipher part, strip-height boxes) (FAIL);
an unanswerable page, the Dinteville shape (every tile in one UNREAD pile, questions offering labels with no pile)
(FAIL). Then the cases it must NOT block: focus tiles all one family, free-prose questions, a '-' reader split, a tall
sign touching one strip edge. Run: python3 tools/tests/test_sorter_preflight.py"""
import os, re, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sign_sorter as ss
import sorter_preflight as pf
from PIL import Image, ImageDraw

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok


def strip(path, n=8, h=60):
    """A line strip with n signs, each a 14x26 ring-ish glyph at x = 20 + 30 i, y 17..43."""
    im = Image.new('L', (30 * n + 40, h), 255); g = ImageDraw.Draw(im)
    for i in range(n):
        x = 20 + 30 * i
        g.ellipse((x, 17, x + 14, 43), outline=0, width=3)
        if i % 2: g.line((x + 7, 17, x + 7, 43), fill=0, width=2)
    im.save(path)


def page(d, signs, labels, focus, name='p.html'):
    (d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in signs))
    (d / 'labels.tsv').write_text('sid\tsign\tfamily\n' + ''.join('\t'.join(r) + '\n' for r in labels))
    (d / 'focus.tsv').write_text(''.join('\t'.join(r) + '\n' for r in focus))
    data = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages'))
    data['focus'] = [{'sid': s, 'q': q} for s, q in focus]
    out = d / name
    out.write_text(ss.render(data, 'T', 'L'))
    return str(out)


def run(p, cl, **kw):
    ok, lines = pf.run(page=p, cipher_lines=cl, quiet=True, **kw)
    return ok, lines


def line(lines, key):
    return next(l for l in lines if l.split(' ', 1)[1].lstrip().startswith(key))


with tempfile.TemporaryDirectory() as d:
    d = Path(d); (d / 'pages').mkdir()
    strip(d / 'pages' / 'L01.png'); strip(d / 'pages' / 'L02.png'); strip(d / 'pages' / 'L00.png')
    (d / 'lists').mkdir(); cl = d / 'lists' / 'cipher_lines.tsv'; cl.write_text('# test\nL01\nL02\n')
    sg = [(f'L{l}_{i}', f'L{l}', 20 + 30 * i, 17, 15, 27) for l in ('01', '02') for i in range(8)]
    lab = [(s[0], 'o' if i % 2 == 0 else 'p', 'o' if i % 2 == 0 else 'p') for i, s in enumerate(sg)]

    # 1. good page
    good = page(d, sg, lab, [('L01_1', 'L1 sign 2: readers o / p. Which sign?'), ('L02_3', 'pass A p, pass B -; which?')])
    ok, ls = run(good, str(cl))
    check('good page: PASS', ok)
    check('good page: template line passes (Fix the cut + current marker)', line(ls, 'template').startswith('PASS'))
    sheet = Path(good).with_suffix('.preflight.png')
    check('good page: contact sheet written with up to 24 tiles', sheet.exists() and Image.open(sheet).size[0] > 0)

    # 2. wrong line (Oldenbarnevelt v1): a third strip not in the list, strip-height boxes, a clear part before x0
    sg2 = sg + [(f'L00_{i}', 'L00', 20 + 30 * i, 17, 15, 27) for i in range(4)]
    lab2 = lab + [(f'L00_{i}', 'o', 'o') for i in range(4)]
    wrong = page(d, sg2, lab2, [('L01_1', 'readers o / p')], 'wrong.html')
    ok, ls = run(wrong, str(cl))
    check('wrong-line page: FAIL on right line (tiles off the list)', not ok and line(ls, 'right line').startswith('FAIL')
          and '4 tile(s) off the cipher lines (L00)' in line(ls, 'right line'))
    tall = [(s, p, x, 0, w, 60) for (s, p, x, y, w, h) in sg]           # every box the height of the strip
    tallp = page(d, tall, lab, [('L01_1', 'readers o / p')], 'tall.html')
    ok, ls = run(tallp, str(cl))
    check('strip-height boxes: FAIL (Oldenbarnevelt v1 shape)', not ok and '16 strip-height boxes' in line(ls, 'right line'))
    clx = d / 'cl_x.tsv'; clx.write_text('L01\t100\nL02\n')                # L01's cipher part starts at x 100
    ok, ls = run(good, str(clx))
    check('clear words before the cipher x-range: FAIL', not ok and '3 tile(s) off the cipher lines' in line(ls, 'right line'))
    ok, ls = run(good, None)
    check('no cipher-line list: FAIL (the builder must state the lines)', not ok and 'no cipher-line list' in line(ls, 'right line'))

    # 3. unanswerable (Dinteville): every tile in UNREAD, questions offer labels with no pile
    unread = [(s[0], 'UNREAD', 'UNREAD') for s in sg]
    un = page(d, sg, unread, [('L01_1', 'R4.2: pass A 9, pass B 0\'; which sheet label?')], 'unread.html')
    ok, ls = run(un, str(cl))
    check('one-pile page: FAIL on answerable', not ok and line(ls, 'answerable').startswith('FAIL')
          and '0 named pile(s)' in line(ls, 'answerable'))
    din = page(d, sg, lab, [('L01_1', 'R4.10: pass A D, pass B -; which sheet label?')], 'din.html')
    ok, ls = run(din, str(cl))
    check('question offers a label with no pile: FAIL', not ok and 'offers D, no such pile' in line(ls, 'answerable'))
    nof = page(d, sg, lab, [], 'nofocus.html')
    ok, ls = run(nof, str(cl))
    check('empty focus box: FAIL', not ok and 'focus box empty' in line(ls, 'answerable'))
    ghost = page(d, sg, lab, [('L09_9', 'readers o / p')], 'ghost.html')
    check('focus sid not on the page: FAIL', not run(ghost, str(cl))[0])

    # template marker
    old = Path(good).read_text()
    stale = d / 'stale.html'; stale.write_text(re.sub(r'<meta name="sign-sorter-template" content="[^"]+">', '', old))
    ok, ls = run(str(stale), str(cl))
    check('page without the template marker: FAIL', not ok and 'marker missing' in line(ls, 'template'))
    nofix = d / 'nofix.html'; nofix.write_text(old.replace('id="ctxFix"', 'id="ctxX"'))
    check('page without Fix the cut: FAIL', 'no "Fix the cut"' in line(run(str(nofix), str(cl))[1], 'template'))

    # must NOT block
    onefam = page(d, sg, lab, [(f'L01_{i}', f'L1 sign {i}: tt or a single crossed t? Split the t piles: tt / tb')
                                for i in (0, 2, 4, 6)], 'onefam.html')
    check('NOT blocked: focus tiles all one pile/family, free-prose question', run(onefam, str(cl))[0])
    check('NOT blocked: a "-" reader split ("pass A -, pass B p")', run(good, str(cl))[0])
    one_tall = [(s, p, x, (0 if s == 'L01_0' else y), w, (43 if s == 'L01_0' else h)) for (s, p, x, y, w, h) in sg]
    ot = page(d, one_tall, lab, [('L01_1', 'readers o / p')], 'onetall.html')
    ok, ls = run(ot, str(cl))
    check('NOT blocked: a tall sign touching one edge only', ok and '0 strip-height boxes' in line(ls, 'right line'))
    check('offered_labels: "No draft sign lines up here" offers nothing',
          pf.offered_labels('No draft sign lines up here; started in l by shape. Right pile, other sign, or bad cut?') == [])

    # text inputs mode and the account switch
    ok, ls = pf.run(inputs=str(d), cipher_lines=str(cl), quiet=True)
    check('--inputs: template n/a, page images measured, PASS', ok and line(ls, 'template').startswith('n/a'))
    os.environ['CIPHERLAB_ACCOUNT'] = 'acct4'
    check('--expect-owner-account on another account: FAIL', not run(good, str(cl), expect_owner=True)[0])
    os.environ['CIPHERLAB_ACCOUNT'] = 'owner'
    check('--expect-owner-account on the owner account: PASS', run(good, str(cl), expect_owner=True)[0])
    seg = d / 'segment_pages.txt'; seg.write_text('--page L01=<s>/a.jpg --page L02=<s>/b.jpg@0,0,9,9\n')
    check('segment_pages.txt read as a cipher-line list', pf.read_cipher_lines(str(seg)) == {'L01': None, 'L02': None})

print('ALL PASS' if not fails else f'{fails} FAILED')
sys.exit(1 if fails else 0)
