#!/usr/bin/env python3
"""Offline test of SORTER-PILES-ANSWERED (15 Oct 2026): tools/sign_sorter.py --piles-from ... --answered-only.
A settled row counts only if the person MOVED it, CHECKED it (db/checked/<sid>.json beside SETTLED.tsv) or it sits in a pile the
person MADE (db/newpiles); --certain tiles still join only a pile the person's answered rows formed.
Must catch: a 'kept' row with no checked record (a tile never touched, left in its reader-label pile) shown as a pile member; a pile
founded only by untouched kept rows; an untouched kept row on a later page replacing an earlier move under --later-wins.
Must NOT drop: a moved row; a kept row with a checked record; a kept row in a person-made pile; a certain tile joining a pile the
person formed by a move. Without --answered-only the old behaviour (kept rows count) is unchanged."""
import json, os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import sign_sorter as ss, sorter_preflight as pf
from PIL import Image, ImageDraw

fails = 0
def check(name, ok, extra=''):
    global fails
    print('PASS' if ok else 'FAIL', name, extra if not ok else ''); fails += not ok

def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(text); return path

def rec(db, coll, name, doc):
    w(os.path.join(db, coll, name + '.json'), json.dumps(doc))

d = tempfile.mkdtemp(prefix='answered_only_')
try:
    os.makedirs(os.path.join(d, 'pages'))
    rows = ['sid\tpage\tx\ty\tw\th']
    im = Image.new('L', (520, 80), 255); g = ImageDraw.Draw(im)
    for i in range(8):
        x = 20 + i * 60; g.ellipse((x, 22, x + 30, 58), outline=0, width=4)
        rows.append(f'L01_{i:02d}\tL01\t{x - 2}\t16\t36\t48')
    im.save(os.path.join(d, 'pages', 'L01.png'))
    w(os.path.join(d, 'signs.tsv'), '\n'.join(rows) + '\n')
    H = 'sid\told_sign\tnew_sign\tstatus\tmode\n'
    # attempt 1: 00 moved to z; 01 kept in z untouched; 02 kept in o but checked; 03 kept in o untouched; 04 kept in his own pile z-b;
    #            05 moved to o; 06 kept in y untouched (y is founded by untouched rows only)
    s1 = w(os.path.join(d, 'a1', 'settled.tsv'), H + 'L01_00\tx\tz\tmoved\tblind\nL01_01\tz\tz\tkept\tblind\nL01_02\to\to\tkept\tblind\n'
           'L01_03\to\to\tkept\tblind\nL01_04\tz-b\tz-b\tkept\tblind\nL01_05\tx\to\tmoved\tblind\nL01_06\ty\ty\tkept\tblind\n')
    rec(os.path.join(d, 'a1', 'db'), 'checked', 'L01_02', {'sid': 'L01_02', 'pile': 'o'})
    rec(os.path.join(d, 'a1', 'db'), 'newpiles', 'zb', {'id': 'z-b', 'from': 'z'})
    # attempt 2 (later): 00 left untouched in a reader pile s (must NOT replace the attempt-1 move); 05 re-moved to s (replaces)
    s2 = w(os.path.join(d, 'a2', 'settled.tsv'), H + 'L01_00\ts\ts\tkept\tblind\nL01_05\to\ts\tmoved\tblind\n')
    os.makedirs(os.path.join(d, 'a2', 'db', 'moves'))

    a, _ = ss.answered_sids(s1)
    check('answered: a moved row counts', 'L01_00' in a and 'L01_05' in a)
    check('answered: a kept row with a checked record counts', 'L01_02' in a)
    check('answered: a kept row in a pile the person made counts', 'L01_04' in a)
    check('answered: an untouched kept row is not an answer', not {'L01_01', 'L01_03', 'L01_06'} & a, sorted(a))
    nodb = w(os.path.join(d, 'a3', 'settled.tsv'), H + 'L01_00\tx\tz\tmoved\tblind\nL01_02\to\to\tkept\tblind\n')
    a3, note = ss.answered_sids(nodb)
    check('answered: no db/ beside the file -> only moved rows count, said so', a3 == {'L01_00'} and 'only moved' in note, (a3, note))

    ans = {s1: ss.answered_sids(s1)[0], s2: ss.answered_sids(s2)[0]}
    po, rep, _ = ss.read_settled([s1, s2], later_wins=True, answered=ans)
    check('read_settled: an untouched row on a later page never replaces an earlier move', po.get('L01_00') == 'z' and 'L01_00' not in rep['replaced'], po)
    check('read_settled: a later move replaces an earlier one', po.get('L01_05') == 's' and 'L01_05' in rep['replaced'])
    check('read_settled: untouched kept rows are left off', not {'L01_01', 'L01_03', 'L01_06'} & set(po), po)
    po0, _, _ = ss.read_settled([s1, s2], later_wins=True)
    check('without --answered-only: kept rows still count (old behaviour unchanged)', po0.get('L01_01') == 'z' and po0.get('L01_00') == 's')

    cert = w(os.path.join(d, 'certain.tsv'), 'sid\tsign\nL01_07\tz\n')
    out = os.path.join(d, 'p.html')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'sign_sorter.py'), '--signs', os.path.join(d, 'signs.tsv'), '--pages',
                        os.path.join(d, 'pages'), '--piles-from', s1, '--piles-from', s2, '--later-wins', '--answered-only', '--certain', cert,
                        '--title', 'T', '--out', out, '--no-preflight'], capture_output=True, text=True)
    log = r.stdout + r.stderr
    check('CLI --answered-only builds and reports per file', r.returncode == 0 and os.path.exists(out) and '--answered-only:' in log, log[-500:])
    if os.path.exists(out):
        data, _ = pf.load_html(out)
        piles = {p['id']: sorted(it['sid'] for it in p['items']) for p in data['piles']}
        check('page: z holds the move and the certain tile only', piles.get('z') == ['L01_00', 'L01_07'], piles)
        check('page: o holds only the checked tile', piles.get('o') == ['L01_02'], piles)
        check('page: the person-made pile z-b is kept', piles.get('z-b') == ['L01_04'], piles)
        check('page: no pile founded by untouched rows (y)', 'y' not in piles, piles)
finally:
    shutil.rmtree(d, ignore_errors=True)
print('ALL PASS' if not fails else f'{fails} FAILED'); sys.exit(1 if fails else 0)
