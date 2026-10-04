#!/usr/bin/env python3
"""Offline test for tools/lookalike_pass.py `windows` and the --hide-passc option (N7-LKTOOL, 4 Oct 2026; no network,
synthetic crops written to a temporary folder only).
1. Placement (case it must catch): on a stitched two-segment line of 10 evenly spaced ink blocks, the red tick of the
   window for sign k falls inside block k, for every k; the segments are pasted at their manifest source x.
2. --tiles: only 'split' rows are windowed by default (case it must NOT window: a one-reader 'gap' row, which has no A/B
   pair for the 2-of-3 rule); --status all takes it. The written <run>_tiles.tsv keeps the input columns and is accepted
   by `reconcile` unchanged. The prompt lists candidates alphabetically and carries no passC line sequence.
3. --items: one window per audit item, captioned by item, context built with the shown (planted) label; refuses to
   overwrite its input tiles file and refuses both/neither of --tiles/--items.
4. --hide-passc: packet's prompt drops the line sequences and sorts candidates; audit's brackets read [n:?]; the default
   prompts carry the echo note.
5. When ciphers/fr16104-vivonne-spain-1572/tx/viv53L_windows.py exists, its window() and the tool give pixel-identical
   windows on the same synthetic crops (the promotion changed nothing in the instrument).
Run: python3 tools/tests/test_lookalike_windows.py"""
import contextlib, csv, io, json, os, shutil, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import lookalike_pass as lp
from PIL import Image

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

def tsv(path, header, rows):
    with open(path, 'w') as o:
        o.write('\t'.join(header) + '\n')
        for r in rows:
            o.write('\t'.join(str(x) for x in r) + '\n')

def read(p):
    return list(csv.DictReader(open(p), delimiter='\t'))

def run(*args):
    with contextlib.redirect_stdout(io.StringIO()):
        return lp.main(list(args))

def fails_with(*args):
    try:
        run(*args)
    except SystemExit as e:
        return e.code not in (0, None)
    return False

tmp = tempfile.mkdtemp()
try:
    # a line of 10 signs: blocks 20 px wide every 40 px from x=30 (inked span 30..409), split in two segments at x=200
    N, X0, PITCH, BW, H = 10, 30, 40, 20, 60
    full = Image.new('L', (440, H), 255)
    for k in range(N):
        full.paste(0, (X0 + k * PITCH, 15, X0 + k * PITCH + BW, 45))
    img = os.path.join(tmp, 'images'); os.makedirs(img)
    SX = 5000   # source x of the strip's left edge
    full.crop((0, 0, 200, H)).save(os.path.join(img, 'c9_fX_L01_s1.png'))
    full.crop((200, 0, 440, H)).save(os.path.join(img, 'c9_fX_L01_s2.png'))
    json.dump({'iiif_lines': [{'crop': 'c9_fX_L01_s2.png', 'box': [SX + 200, 0, SX + 440, H]},
                              {'crop': 'c9_fX_L01_s1.png', 'box': [SX, 0, SX + 200, H]},
                              {'crop': 'c9_fX_lines_debug.jpg', 'box': [0, 0, 1, 1]}]},
              open(os.path.join(img, 'manifest.json'), 'w'))
    labs = ['a', 'b', 'u', 'a', 'z', '3', 'S', 'd', 'a', 'b']
    passc = os.path.join(tmp, 'passC.tsv')
    tsv(passc, ['passage', 'pos', 'sign_id'], [('fX_L01', i + 1, s) for i, s in enumerate(labs)])
    man = os.path.join(img, 'manifest.json')

    # 1. placement
    S = lp._line_strips(man, '', '*_{line}_s*')('fX_L01')
    a, b = lp._ink_extent(S, 110, 2)
    check(S.size == (440, H) and (a, b) == (30, 409), f'1 stitched on source x, inked span {a}..{b}')
    ok = True
    for k in range(1, N + 1):
        x = a + (k - 0.5) * (b - a) / N
        ok &= X0 + (k - 1) * PITCH <= x < X0 + (k - 1) * PITCH + BW
        w = lp._window(S, a, b, N, k, 6.5, 2)
        lo = int(max(0, x - 6.5 * (b - a) / N)); tx = int((x - lo) * 2)
        ok &= w.getpixel((tx, 5)) == (255, 0, 0) and w.getpixel((tx, H))[0] < 128   # tick red, block ink under it
    check(ok, '1 every sign k: estimate and red tick inside block k')

    # 2. --tiles
    TH = ['run', 'passage', 'pos', 'passC', 'A', 'B', 'status', 'why', 'candidates', 'before', 'after', 'noteA', 'noteB']
    tiles = os.path.join(tmp, 'pk_tiles.tsv')
    tsv(tiles, TH, [('pk', 'fX_L01', 3, 'u', 'u', 'a', 'split', 'split', 'u,a,n', 'a b', 'a z 3', '', ''),
                    ('pk', 'fX_L01', 5, 'z', 'z', '3', 'split', 'split', 'z,3', 'b u a', '3 S d', '', ''),
                    ('pk', 'fX_L01', 7, 'S', 'S', '', 'gap', 'split', 'S,d', 'a z 3', 'd a b', '', '')])
    out = os.path.join(tmp, 'win')
    desc = os.path.join(tmp, 'desc.tsv'); tsv(desc, ['#id', 'description'], [('z', 'FLAT-topped z'), ('3', 'ROUND-topped 3')])
    res = run('windows', '--tiles', tiles, '--passc', passc, '--manifest', man, '--out', out, '--desc', desc)
    wt = read(os.path.join(out, 'pk_win_tiles.tsv'))
    check(res['windows'] == 2 and [t['pos'] for t in wt] == ['3', '5'] and list(wt[0]) == TH,
          f"2 default windows the 2 split rows, not the gap; tiles file keeps the columns {res}")
    pr = open(os.path.join(out, 'pk_win_prompt.md')).read()
    check('candidates: a = a (free description); n = n (free description); u = u' in pr and 'candidates: 3 = ROUND-topped 3; z = FLAT-topped z' in pr
          and ' '.join(labs) not in pr and 'Line sequences' not in pr and len(res and os.listdir(os.path.join(out, 'win'))) == 1,
          '2 prompt: candidates alphabetical with descriptions, no passC sequence, one montage')
    rr = os.path.join(tmp, 'rr.tsv')
    tsv(rr, ['passage', 'pos', 'label', 'conf', 'second', 'note'], [('fX_L01', 3, 'a', 'H', '', ''), ('fX_L01', 5, '3', 'L', '', '')])
    rec = run('reconcile', '--tiles', os.path.join(out, 'pk_win_tiles.tsv'), '--passc', passc, '--reread', rr,
              '--out', os.path.join(tmp, 'passD.tsv'))
    check(rec['relabelled'] == 1 and rec['unsettled'] == 1, f'2 reconcile reads the windows tiles file {rec}')
    res = run('windows', '--tiles', tiles, '--passc', passc, '--manifest', man, '--out', out, '--status', 'all', '--run', 'all')
    check(res['windows'] == 3, '2 --status all includes the gap row')

    # 3. --items
    items = os.path.join(tmp, 'au_audit_items.tsv')
    tsv(items, ['run', 'item', 'line', 'pos', 'original', 'shown', 'planted', 'forced', 'candidates'],
        [('au', 2, 'fX_L01', 9, 'a', 'a', 0, 0, 'u,a,@'), ('au', 1, 'fX_L01', 8, 'd', 'S', 1, 0, 'S,d,V')])
    res = run('windows', '--items', items, '--passc', passc, '--manifest', man, '--out', out, '--per', '1')
    pr = open(os.path.join(out, 'au_audit_win_prompt.md')).read()
    check(res['windows'] == 2 and res['montages'] == 2 and pr.index('\n1\tbefore') < pr.index('\n2\tbefore')
          and '2\tbefore: 3 S S | after: b' in pr and 'candidates: S; V; d' in pr,
          f'3 items: one window each, item order, shown label in context, candidates alphabetical {res}')
    check(fails_with('windows', '--tiles', tiles, '--passc', passc, '--manifest', man, '--out', tmp, '--run', 'pk'),
          '3 refuses to overwrite its input tiles file')
    check(fails_with('windows', '--passc', passc, '--manifest', man, '--out', out)
          and fails_with('windows', '--tiles', tiles, '--items', items, '--passc', passc, '--manifest', man, '--out', out),
          '3 refuses neither / both of --tiles and --items')
    res = run('windows', '--tiles', tiles, '--passc', passc, '--crops-glob', os.path.join(img, 'c9_{line}_s?.png'),
              '--out', out, '--run', 'glob')
    check(res['windows'] == 2, '3 --crops-glob route (segments abutted in name order)')

    # 4. --hide-passc on packet and audit
    AH = ['passage', 'posA', 'idA', 'confA', 'posB', 'idB', 'confB', 'status', 'merged', 'merged_conf']
    leaf = os.path.join(tmp, 'leaf'); os.makedirs(leaf)
    tsv(os.path.join(leaf, 'agreement.tsv'), AH,
        [('L01', i + 1, s, 'H', i + 1, ('a' if s == 'u' else s), 'H', 'split' if s == 'u' else 'agree', s, 'H')
         for i, s in enumerate(labs)])
    tsv(os.path.join(leaf, 'passC.tsv'), ['passage', 'pos', 'sign_id'], [('L01', i + 1, s) for i, s in enumerate(labs)])
    conf = os.path.join(tmp, 'conf.tsv'); tsv(conf, ['label_a', 'label_b', 'n', 'n_target', 'examples'], [('a', 'u', 3, 0, '')])
    sheet = os.path.join(tmp, 'sheet.png'); Image.new('RGB', (220, 110), 'white').save(sheet)
    smap = os.path.join(tmp, 'map.json'); json.dump([{'id': 'u'}, {'id': 'a'}], open(smap, 'w'))
    common = ['--agreement', os.path.join(leaf, 'agreement.tsv'), '--confusion', conf, '--sheet', sheet, '--sheet-map', smap]
    run('packet', *common, '--out', os.path.join(tmp, 'p0'), '--run', 'p0')
    run('packet', *common, '--out', os.path.join(tmp, 'p1'), '--run', 'p1', '--hide-passc')
    p0 = open(os.path.join(tmp, 'p0', 'p0_prompt.md')).read(); p1 = open(os.path.join(tmp, 'p1', 'p1_prompt.md')).read()
    check('Line sequences' in p0 and 'echoed passC' in p0 and 'Line sequences' not in p1 and 'echoed passC' not in p1
          and 'L01\t3\ta,u\t' in p1 and 'L01\t3\tu,a\t' in p0, '4 packet --hide-passc: no sequences, sorted candidates; default carries the echo note')
    pa = os.path.join(tmp, 'pa.tsv'); tsv(pa, ['line', 'pos', 'sign'], [('L01', i + 1, s) for i, s in enumerate(labs)])
    acommon = ['--passa', pa, '--passb', pa, '--passc', pa, '--confusion', conf, '--sample', '3', '--sheet', sheet,
               '--sheet-map', smap]
    run('audit', *acommon, '--out', os.path.join(tmp, 'a0'), '--run', 'a0')
    run('audit', *acommon, '--out', os.path.join(tmp, 'a1'), '--run', 'a1', '--hide-passc')
    a0 = open(os.path.join(tmp, 'a0', 'a0_audit_prompt.md')).read(); a1 = open(os.path.join(tmp, 'a1', 'a1_audit_prompt.md')).read()
    check('[1:' in a0 and '[1:?]' not in a0 and '[1:?]' in a1 and 'echoed passC' in a0 and 'echoed passC' not in a1,
          '4 audit --hide-passc: [n:?] brackets; default carries the echo note')

    # 5. equivalence with the private instrument it was promoted from
    priv = os.path.join(ROOT, 'ciphers', 'fr16104-vivonne-spain-1572', 'tx')
    if os.path.exists(os.path.join(priv, 'viv53L_windows.py')):
        sys.path.insert(0, priv)
        import viv53L_windows as w53
        w53.IMG = img
        bx = {'fX': w53.boxes('fX')}
        same = True
        for k in range(1, N + 1):
            wp = w53.window({}, bx, {'fX_L01': N}, 'fX_L01', k)
            wt_ = lp._window(S, a, b, N, k, 6.5, 2)
            same &= wp.size == wt_.size and wp.tobytes() == wt_.tobytes()
        check(same, '5 pixel-identical to viv53L_windows.window() on the same crops')
    else:
        print('SKIP 5 private viv53L_windows.py not present')
finally:
    shutil.rmtree(tmp)
print('ALL PASS' if not fails else f'{fails} FAILED')
sys.exit(1 if fails else 0)
