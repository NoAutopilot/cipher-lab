#!/usr/bin/env python3
"""Offline test of SORTER-FIX-R12-R16 (15 Oct 2026; owner rows R12-R16 of tools/data/sorter_owner_requirements.tsv):
tools/sign_sorter.py --piles-from / --later-wins / --drop-conflicts / --certain / --meanings / --box-check, the build-time
piles check (a)-(c), the R14 box-check gate, tools/sorter_preflight.py check 8 (owner rows), and -- when node, playwright and
Chromium are present -- browser_tests/test_r12_r16.js on the page built here (the R12 recut and the R15/R16 page shape).
Must catch: a tile two settled files put in two piles; a waiting tile inside a pile; two piles of one meaning with no note; a
question page under 90% box check; a question card with "Fix the cut". Must NOT block: a pile the person made (z-b) with no
meaning; a tile two files keep in the same pile; a re-answer in a later file under --later-wins; a page with no questions."""
import os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import sign_sorter as ss, sorter_preflight as pf
from PIL import Image, ImageDraw

fails = 0
def check(name, ok, extra=''):
    global fails
    print('PASS' if ok else 'FAIL', name, extra if not ok else ''); fails += not ok

def w(path, text):
    open(path, 'w').write(text); return path

d = tempfile.mkdtemp(prefix='piles_from_')
try:
    # ---- synthetic line images: 3 lines, 8 signs each (three shapes), plus their signs.tsv
    os.makedirs(os.path.join(d, 'pages'))
    rows = ['sid\tpage\tx\ty\tw\th']
    for L in range(1, 4):
        im = Image.new('L', (520, 80), 255); g = ImageDraw.Draw(im)
        for i in range(8):
            x = 20 + i * 60; k = (i + L) % 3
            if k == 0: g.ellipse((x, 22, x + 30, 58), outline=0, width=4)
            elif k == 1: g.line((x + 15, 18, x + 15, 60), fill=0, width=5)
            else: g.polygon([(x, 58), (x + 15, 20), (x + 30, 58)], outline=0, width=4)
            rows.append(f'L{L:02d}_{i:02d}\tL{L:02d}\t{x - 2}\t16\t36\t48')
        im.save(os.path.join(d, 'pages', f'L{L:02d}.png'))
    w(os.path.join(d, 'signs.tsv'), '\n'.join(rows) + '\n')
    w(os.path.join(d, 'cl.tsv'), 'L01\nL02\nL03\n')
    shape = lambda sid: ['o', 'i', 'v'][(int(sid[5:7]) + int(sid[1:3])) % 3]
    sids = [r.split('\t')[0] for r in rows[1:]]
    qs = ['L03_06', 'L03_07']   # the questions
    piled = [s for s in sids if s not in qs]
    # attempt 1 keeps most, moves two; attempt 2 re-answers one tile and leaves one in the waiting box
    a1 = ['sid\told_sign\tnew_sign\tstatus\tmode'] + [f'{s}\t{shape(s)}\t{shape(s)}\tkept\tblind' for s in piled[:-2]] + \
         [f'{piled[-2]}\tx\t{shape(piled[-2])}\tmoved\tblind', f'{piled[-1]}\tx\tunsorted\tkept\tblind']
    a2 = ['sid\told_sign\tnew_sign\tstatus\tmode', f'{piled[0]}\t{shape(piled[0])}\to-b\tmoved\tblind', f'{piled[1]}\t{shape(piled[1])}\t{shape(piled[1])}\tkept\tblind']
    s1, s2 = w(os.path.join(d, 'a1.tsv'), '\n'.join(a1) + '\n'), w(os.path.join(d, 'a2.tsv'), '\n'.join(a2) + '\n')
    focus = w(os.path.join(d, 'focus.tsv'), ''.join(f'{q}\tQ{i + 1:02d}: Which pile holds signs that look like this one?\n' for i, q in enumerate(qs)))
    mean = w(os.path.join(d, 'key.tsv'), 'code\tmeaning\no\ta\ni\ta\nv\tb\n')   # o and i share a meaning; o-b (the person's own pile) has none

    # ---- read_settled
    po, conf, uns = ss.read_settled([s1, s2])
    check('read_settled: a re-answer in a later file is a conflict by default', piled[0] in conf and piled[0] not in po, conf)
    check('read_settled: NOT blocked -- a tile kept in the same pile by both files', piled[1] in po and piled[1] not in conf)
    check('read_settled: the waiting box (unsorted) is never a pile', piled[-1] in uns and piled[-1] not in po)
    po2, rep2, _ = ss.read_settled([s1, s2], later_wins=True)
    check('read_settled --later-wins: the later answer stands, listed', po2.get(piled[0]) == 'o-b' and piled[0] in rep2['replaced'])

    def build(*extra):
        out = os.path.join(d, 'p.html')
        if os.path.exists(out): os.remove(out)
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'sign_sorter.py'), '--signs', os.path.join(d, 'signs.tsv'), '--pages',
                            os.path.join(d, 'pages'), '--piles-from', s1, '--piles-from', s2, '--focus', focus, '--cipher-lines', os.path.join(d, 'cl.tsv'),
                            '--title', 'T', '--out', out, '--no-preflight', *extra], capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr, out
    rc, log, out = build()
    check('CLI: a conflict stops the build (exit 2, no page)', rc == 2 and not os.path.exists(out) and 'conflict' in log + 'settled differently', log[-300:])
    rc, log, out = build('--drop-conflicts', '--meanings', mean)
    check('CLI --drop-conflicts: builds, conflict left off', rc == 0 and os.path.exists(out) and 'left off the page' in log, log[-400:])
    data, html = pf.load_html(out)
    where = {}
    for p in data['piles']:
        for it in p['items']: where.setdefault(it['sid'], []).append(p['id'])
    check('page: the conflicting tile is on no pile', piled[0] not in where)
    check('page: the questions are only in the queue', all(where.get(q) == ['unsorted'] for q in qs) and data['queue'] == ['unsorted'])
    notes = {p['id']: p.get('note', '') for p in data['piles']}
    check('page: o and i (one meaning) carry "same letter, two shapes"; v and o-b none', ss.SAME_LETTER in notes['o'] and ss.SAME_LETTER in notes['i']
          and not notes['v'] and not notes.get('o-b', '') and data['sameLetter'] == [['i', 'o']], notes)
    check('page: no meaning reaches the page (blind)', '_meanings' not in data and '"meaning"' not in html)
    rc, log, out = build('--later-wins', '--meanings', mean)
    data, html = pf.load_html(out)
    check('CLI --later-wins: the re-answered tile is in the person\'s new pile o-b', any(p['id'] == 'o-b' and any(it['sid'] == piled[0] for it in p['items']) for p in data['piles']), log[-300:])
    check('CLI: no box-check file prints the R14 warning', 'WARNING R14' in log)
    check('page: the question card has no Fix the cut', 'id="s2Fix"' not in html and 'id="s2Bad"' in html)

    # ---- piles_check (a), (b), (c) on hand-made data
    it = lambda s: {'sid': s, 'img': '', 'p': 'L01', 'b': [0, 0, 1, 1]}
    good = {'piles': [{'id': 'o', 'items': [it('A')], 'note': 'same letter, two shapes: also pile i'}, {'id': 'i', 'items': [it('B')], 'note': 'same letter, two shapes: also pile o'},
                      {'id': 'unsorted', 'items': [it('Q')]}], 'queue': ['unsorted'], 'focus': [{'sid': 'Q', 'q': 'Q01: ?'}], 'sameLetter': [['i', 'o']]}
    check('piles_check: a clean page passes', ss.piles_check(good) == [])
    import copy
    b = copy.deepcopy(good); b['piles'][1]['items'].append(it('A'))
    check('piles_check (a): a tile in two piles fails', any(f.startswith('(a)') for f in ss.piles_check(b)))
    b = copy.deepcopy(good); b['piles'][0]['items'].append(it('Q'))
    check('piles_check (b): a waiting tile inside a pile fails (the f.191r Q01 shape)', any(f.startswith('(b)') and 'Q' in f for f in ss.piles_check(b)))
    b = copy.deepcopy(good); b['queue'] = []
    check('piles_check (b): questions with no queue fail', any('no waiting box' in f for f in ss.piles_check(b)))
    b = copy.deepcopy(good); del b['piles'][1]['note']
    check('piles_check (c): a shared meaning without the note fails', any(f.startswith('(c)') and 'i' in f for f in ss.piles_check(b)))
    b = copy.deepcopy(good); b['piles'].append({'id': 'z-b', 'items': [it('C')]})
    check('piles_check: NOT blocked -- a person-made pile with no meaning', ss.piles_check(b) == [])

    # ---- R14 box-check gate
    fo = [{'sid': f's{i}', 'q': f'Q{i:02d}: Which pile?'} for i in range(1, 11)]
    bc = lambda npass, key='qid': w(os.path.join(d, 'bc.tsv'), '# box check\n' + key + '\tcheck\n' +
                                    ''.join(f'{(f"Q{i:02d}" if key == "qid" else f"s{i}")}\t{"pass" if i <= npass else "fail"}\n' for i in range(1, 11)))
    ok, line, bad = ss.box_check_gate(bc(8), fo)
    check('box check: 8/10 refused, failing sids printed', ok is False and bad == ['s9', 's10'] and 's9' in line, line)
    ok, line, bad = ss.box_check_gate(bc(9, 'sid'), fo)
    check('box check: 9/10 (by sid) passes', ok is True and '9/10' in line, line)
    ok, line, _ = ss.box_check_gate(None, fo)
    check('box check: no file -> warning naming R14', ok is None and 'R14' in line)
    ok, line, _ = ss.box_check_gate(w(os.path.join(d, 'nc.tsv'), 'qid\tverdict\nQ01\twhole\n'), fo)
    check('box check: a file with no check column is refused', ok is False and 'no `check` column' in line)
    check('box check: NOT blocked -- a page with no questions', ss.box_check_gate(None, [])[0] is True)
    rc, log, out = build('--later-wins', '--meanings', mean, '--box-check', w(os.path.join(d, 'bc2.tsv'), 'qid\tcheck\nQ01\tpass\nQ02\tfail\n'))
    check('CLI: a 1/2 box check refuses the page (exit 2, failing sid named)', rc == 2 and 'L03_07' in log and not os.path.exists(out), log[-300:])
    rc, log, out = build('--later-wins', '--meanings', mean, '--box-check', w(os.path.join(d, 'bc3.tsv'), 'qid\tcheck\nQ01\tpass\nQ02\tpass\n'))
    check('CLI: a 2/2 box check builds and records it', rc == 0 and pf.load_html(out)[0].get('boxCheck') == {'pass': 2, 'of': 2, 'file': 'bc3.tsv'}, log[-300:])

    # ---- preflight check 8
    ok, ls = pf.run(page=out, cipher_lines=os.path.join(d, 'cl.tsv'), quiet=True, owner_page=True)
    get = lambda k: next((l for l in ls if k in l), '')
    check('preflight: the piles-from page passes R12/R16, R13, R14, R15 as an owner page', all(get(k).startswith('PASS') for k in ('R12/R16', 'R13:', 'R14:', 'R15:')), ls)
    data, html = pf.load_html(out)
    old = html.replace('<button type="button" id="s2Mark">', '<button type="button" id="s2Fix">Fix the cut</button><button type="button" id="s2Mark">', 1)
    r = pf.check_owner_rows(old, data, True)
    check('preflight R12/R16: a question card with Fix the cut FAILs', r[0][0] is False and 'R12/R16' in r[0][1])
    lab = dict(data); lab.pop('pilesFrom'); lab.pop('boxCheck'); lab.pop('queue')
    r = {x[1].split(':')[0]: x[0] for x in pf.check_owner_rows(html, lab, False)}
    check('preflight R13/R14: a label-pile question page WARNs (not an owner page)', r.get('R13') == 'warn' and r.get('R14') == 'warn', r)
    r = {x[1].split(':')[0]: x[0] for x in pf.check_owner_rows(html, lab, True)}
    check('preflight R13/R14/R15: the same page FAILs as an owner page', r.get('R13') is False and r.get('R14') is False and r.get('R15') is False, r)
    nq = dict(data); nq['focus'] = []
    check('preflight: NOT blocked -- R13-R15 n/a on a page with no questions', any(x[0] is None and 'n/a' in x[1] for x in pf.check_owner_rows(html, nq, True)))

    # ---- browser: R12 recut + R15/R16 shape on this page (skipped, and said so, without node/playwright/Chromium)
    node = shutil.which('node'); exe = os.environ.get('PW_EXE', '/opt/pw-browsers/chromium')
    if node and os.path.exists(exe):
        env = dict(os.environ, PW_EXE=exe, NODE_PATH=os.environ.get('NODE_PATH') or subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip())
        r = subprocess.run([node, 'test_r12_r16.js', out, os.path.join(d, 'shot')], cwd=os.path.join(ROOT, 'tools', 'sign_sorter', 'browser_tests'),
                           capture_output=True, text=True, env=env, timeout=600)
        check('browser test_r12_r16.js on the built page: ALL PASS', r.returncode == 0 and 'ALL PASS' in r.stdout, (r.stdout + r.stderr)[-1500:])
    else:
        print('SKIP browser test_r12_r16.js (no node or Chromium)')

    # ---- KNOWN GAP, skip-marked (R13): "every pile shown holds ONE sign". No gate above looks at shape: --piles-from trusts the
    # settled rows, and a 'kept' row means only that the person left the tile where a machine label put it. On the f.191r rebuild
    # (ciphers/fr16104-vivonne-spain-1572/tx/sorter_f191b/, 15 Oct 2026) about 15 of 37 piles show a tile of another shape in their
    # opening 16 tiles (worker's eye on piles_0.png / piles_1.png there: z holds x, s and 3 shapes; o holds oo, c and dot marks). Un-skip
    # when a shape-consistency gate exists (per-pile image outliers with a matched control, or a person's done verdict per pile).
    print('SKIP R13 one-shape-per-pile: no shape gate yet (known gap; see the comment above this line)')
finally:
    shutil.rmtree(d, ignore_errors=True)
print('ALL PASS' if not fails else f'{fails} FAILED'); sys.exit(1 if fails else 0)
