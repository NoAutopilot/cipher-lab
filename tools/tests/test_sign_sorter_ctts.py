#!/usr/bin/env python3
"""Offline test + control for sign_sorter_apply.py --icons / --ctts-out (MQS-CTTS-EXPORT, 9 Oct 2026; PREREG-MQS-CTTS-EXPORT.md).
Synthetic pages and sorter db, 20 seeds; no network. Writes tools/tests/RESULTS-MQS-CTTS-EXPORT.tsv with --write.
Run: python3 tools/tests/test_sign_sorter_ctts.py [--write]"""
import csv, json, os, random, sys, tempfile
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import sign_sorter_apply as sa
from PIL import Image, ImageDraw, ImageChops

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok


def world(seed, tmp):
    rnd = random.Random(seed)
    pages, signs, labels = os.path.join(tmp, 'pages'), {}, []
    os.makedirs(pages, exist_ok=True)
    names = ['S%02d' % i for i in range(40)]
    wts = [1.0 / (i + 1) for i in range(40)]
    for p in range(3):
        pg = 'pg%d' % p
        im = Image.new('RGB', (640, 420), 'white'); d = ImageDraw.Draw(im)
        for i in range(100):
            cx, cy = 60 * (i % 10) + 8, 40 * (i // 10) + 4
            x, y, w, h = cx + rnd.randint(0, 6), cy + rnd.randint(0, 4), rnd.randint(22, 40), rnd.randint(18, 30)
            for _ in range(4):
                d.line([(x + rnd.randint(0, w), y + rnd.randint(0, h)), (x + rnd.randint(0, w), y + rnd.randint(0, h))],
                       fill=(rnd.randint(0, 90),) * 3, width=rnd.randint(1, 3))
            sid = '%s_%03d' % (pg, i)
            signs[sid] = {'sid': sid, 'page': pg, 'x': str(x), 'y': str(y), 'w': str(w), 'h': str(h)}
            labels.append({'sid': sid, 'sign': rnd.choices(names, wts)[0]})
        im.save(os.path.join(pages, pg + ('.jpeg' if p == 2 else '.png')))  # one .jpeg: CTTS needs it as .jpg
    used = sorted({l['sign'] for l in labels})
    piles = [{'pile': used[-1], 'merge_into': used[-2]}, {'pile': used[-3], 'verdict': 'mark'}, {'pile': used[0], 'verdict': 'same'}]
    sids = [l['sid'] for l in labels]; rnd.shuffle(sids)
    moves = [{'sid': s, 'to': t} for s, t in zip(sids[:16], ['ASIDE'] * 4 + ['BAD-CUT'] * 4 + ['OUT'] * 4 + [used[1]] * 2 + ['NEW-b'] * 2)]
    rows, _ = sa.apply(labels, piles, moves, [{'id': 'NEW-b'}])
    return rows, signs, pages


def truth(rows, signs):
    return Counter((signs[s]['page'], float(signs[s]['x']), float(signs[s]['y']), float(signs[s]['w']), float(signs[s]['h']),
                    sa.CTTS_STATUS.get(st) or new) for s, _o, new, st in rows)


def s1(rows, signs, write_signs, write_rows, tmp, tag):
    out = os.path.join(tmp, 'ctts_' + tag)
    sa.write_ctts(write_rows, write_signs, os.path.join(tmp, 'pages'), out)
    got, _ = sa.read_ctts(out)
    t = truth(rows, signs)
    return sum((t & Counter(got)).values()) / len(rows), out


def s2(rows, signs, crop_signs, tmp, tag):
    d = os.path.join(tmp, 'icons_' + tag)
    ic = sa.write_icons(rows, crop_signs, os.path.join(tmp, 'pages'), d)
    ex = sa.icon_exemplars(rows)
    ok = 0
    for sign, fn in ic.items():
        s = signs[ex[sign][0]]
        page = Image.open(sa.page_path(os.path.join(tmp, 'pages'), s['page'])).convert('RGB')
        x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h'))
        ref, got = page.crop((x, y, x + w, y + h)), Image.open(os.path.join(d, fn)).convert('RGB')
        ok += ref.size == got.size and ImageChops.difference(ref, got).getbbox() is None
    return ok / max(1, len(ex)), ic, d


res = []
for seed in range(1, 21):
    with tempfile.TemporaryDirectory() as tmp:
        rows, signs, pages = world(seed, tmp)
        k1, out = s1(rows, signs, signs, rows, tmp, 'known')
        vals = [sa.CTTS_STATUS.get(st) or new for *_x, new, st in rows]
        rnd = random.Random(1000 + seed); rnd.shuffle(vals)
        perm = [(r[0], r[1], v, 'kept') for r, v in zip(rows, vals)]
        perm = [(s, o, v, 'kept') if not v.startswith('~') else (s, o, '', next(k for k, vv in sa.CTTS_STATUS.items() if vv == v))
                for s, o, v, _ in perm]
        n1, _ = s1(rows, signs, signs, perm, tmp, 'perm')
        conv = {k: dict(v, w=str(int(v['x']) + int(v['w'])), h=str(int(v['y']) + int(v['h']))) for k, v in signs.items()}
        n2, _ = s1(rows, signs, conv, rows, tmp, 'conv')
        k2, ic, idir = s2(rows, signs, signs, tmp, 'known')
        shift = {k: dict(v, x=str(int(v['x']) + 3)) for k, v in signs.items()}
        n3, _, _ = s2(rows, signs, shift, tmp, 'shift')
        if seed == 1:
            col = sa.write_ctts(rows, signs, pages, os.path.join(tmp, 'full'), ic, idir)
            fl = sorted(os.listdir(os.path.join(tmp, 'full')))
            check('working dir has the three page images, .jpeg copied as .jpg', [f for f in fl if f.startswith('pg')] == ['pg0.png', 'pg1.png', 'pg2.jpg'])
            check('colors.txt has 431 lines, colour;value;order', len(open(os.path.join(tmp, 'full', 'colors.txt')).read().splitlines()) == 431
                  and all(len(l.split(';')) == 3 for l in open(os.path.join(tmp, 'full', 'colors.txt'))))
            check('second copies written', os.path.exists(os.path.join(tmp, 'full', 'colors_SECOND_COPY.txt'))
                  and os.listdir(os.path.join(tmp, 'full', 'positions_SECOND_COPY')) == os.listdir(os.path.join(tmp, 'full', 'positions')))
            check('one icon per settled sign, named by its colour', sorted(os.listdir(os.path.join(tmp, 'full', 'icons'))) == sorted(col[s] + '.png' for s in ic))
            settled = {new for _s, _o, new, st in rows if new and st not in sa.UNSETTLED}
            check('must not: an unsettled tile never carries a sign (types = settled signs + reserved only)',
                  set(col) <= settled | set(sa.CTTS_STATUS.values()) and all(v in col for v in ('~aside', '~bad-cut', '~taken-out')))
            check('must not: no icon for a reserved type', not any(s.startswith('~') for s in ic))
            # CLI end to end
            db = os.path.join(tmp, 'db'); os.makedirs(os.path.join(db, 'moves'))
            json.dump({'sid': 'pg0_000', 'to': 'ASIDE'}, open(os.path.join(db, 'moves', 'm.json'), 'w'))
            lp, sp = os.path.join(tmp, 'labels.tsv'), os.path.join(tmp, 'signs.tsv')
            with open(lp, 'w') as f:
                f.write('sid\tsign\n' + ''.join('%s\t%s\n' % (s, 'A' if i % 2 else 'B') for i, s in enumerate(signs)))
            with open(sp, 'w') as f:
                f.write('sid\tpage\tx\ty\tw\th\n' + ''.join('\t'.join(v[k] for k in ('sid', 'page', 'x', 'y', 'w', 'h')) + '\n' for v in signs.values()))
            sa.main(['--labels', lp, '--db', db, '--out', os.path.join(tmp, 'set.tsv'), '--signs', sp, '--pages', pages,
                     '--icons', os.path.join(tmp, 'cli_icons'), '--ctts-out', os.path.join(tmp, 'cli_ctts'), '--summary', os.path.join(tmp, 's.json')])
            sm = json.load(open(os.path.join(tmp, 's.json')))
            got, _ = sa.read_ctts(os.path.join(tmp, 'cli_ctts'))
            check('CLI: icons A,B; types A,B,~aside; 300 boxes back', sm.get('icons') == 2 and sm.get('ctts_types') == 3 and len(got) == 300
                  and sum(1 for g in got if g[5] == '~aside') == 1)
            try:
                sa.main(['--labels', lp, '--db', db, '--out', os.path.join(tmp, 'x.tsv'), '--icons', os.path.join(tmp, 'x')]); ok = False
            except SystemExit:
                ok = True
            check('--icons without --signs/--pages refused', ok)
            for nm, rr, sg in [('a value with ;', [('pg0_000', 'A', 'A;B', 'kept')], signs),
                               ('a page name with .', [('q', 'A', 'A', 'kept')], {'q': dict(signs['pg0_000'], sid='q', page='f.12r')}),
                               ('more than 431 types', [(s, 'A', 'T%d' % i, 'kept') for i, s in enumerate(list(signs) * 2)],
                                {**signs})]:
                try:
                    sa.write_ctts(rr, sg, pages, os.path.join(tmp, 'bad')); ok = False
                except ValueError:
                    ok = True
                check('must not: refused ' + nm, ok)
            bad = os.path.join(tmp, 'badidx'); os.makedirs(os.path.join(bad, 'positions'))
            open(os.path.join(bad, 'colors.txt'), 'w').write('')
            open(os.path.join(bad, 'positions', 'p_positions.txt'), 'w').write('1 2 3 4 0\n1 2 3 4 999\n')
            check('reader follows CTTS: a colour index past the set drops the file', sa.read_ctts(bad)[0] == [])
        res.append((seed, round(k1, 4), round(n1, 4), round(n2, 4), round(k2, 4), round(n3, 4)))

for r in res:
    print('seed %2d  S1 known %.4f  perm %.4f  conv %.4f  |  S2 known %.4f  shift %.4f' % r)
gate = all(r[1] == 1.0 and r[4] == 1.0 and r[2] < 0.5 and r[3] < 0.5 and r[5] < 0.5 for r in res)
m = lambda i: sum(r[i] for r in res) / len(res)
print('means: S1 known %.4f perm %.4f conv %.4f; S2 known %.4f shift %.4f; GATE %s' % (m(1), m(2), m(3), m(4), m(5), 'PASS' if gate else 'FAIL'))
check('PREREG gate: S1 = S2 = 1.000 on 20/20 seeds, every null < 0.5', gate)
if '--write' in sys.argv:
    with open(Path(__file__).resolve().parent / 'RESULTS-MQS-CTTS-EXPORT.tsv', 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t'); w.writerow(['seed', 'S1_known', 'S1_null_label_permuted', 'S1_null_box_convention', 'S2_known', 'S2_null_icon_offset'])
        w.writerows(res)
print('ALL PASS' if not fails else 'FAILS %d' % fails)
sys.exit(1 if fails else 0)
