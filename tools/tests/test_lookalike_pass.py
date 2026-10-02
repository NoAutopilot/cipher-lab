#!/usr/bin/env python3
"""Offline test for tools/lookalike_pass.py (no network; writes only to a temporary folder).
1. confusion: swaps counted per unordered pair on 'split*' rows only; gaps and 'agree' rows ignored; n_target per leaf.
2. packet: a split tile and a top-pair tile are flagged, an agreed tile outside the top pairs is not; a passC row past
   the end of its passage (one reader only) is flagged 'single'; the candidate sheet and a value-blind prompt are written
   (the prompt carries ids only: no sheet-map value appears in it).
3. reconcile, the fixed rule (case it must catch): a firm re-read matching reader A or B relabels at 2-of-3; (case it
   must NOT do) a firm re-read matching neither reader, an L re-read, or a SPLIT leaves the passC label and goes to
   focus.tsv; --alt takes every firm re-read label.
4. Reproduces the NEVBIR-LOOKALIKE f.168 passD on disk byte-for-byte (line endings aside) when that folder exists.
Run: python3 tools/tests/test_lookalike_pass.py"""
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

tmp = tempfile.mkdtemp()
try:
    AH = ['passage', 'posA', 'idA', 'confA', 'posB', 'idB', 'confB', 'status', 'merged', 'merged_conf']
    leaf = os.path.join(tmp, 'leaf1'); os.makedirs(leaf)
    tsv(os.path.join(leaf, 'passC_agreement.tsv'), AH, [
        ['L01', 1, 'T1', 'H', 1, 'T1', 'H', 'agree', 'T1', 'H'],
        ['L01', 2, 'T2', 'H', 2, 'T3', 'H', 'split+adj', 'T2', 'H'],
        ['L01', 3, 'T4', 'H', 3, 'T4', 'H', 'agree', 'T4', 'H'],
        ['L01', 4, 'T5', 'H', 4, 'T6', 'M', 'split+adj', 'T6', 'M'],
        ['L01', '', '', '', 5, 'T7', 'H', 'gapA', 'NONE', ''],
        ['L02', 1, 'T2', 'H', 1, 'T3', 'H', 'split', 'T3', 'M']])
    leaf2 = os.path.join(tmp, 'leaf2'); os.makedirs(leaf2)
    tsv(os.path.join(leaf2, 'passC_agreement.tsv'), AH, [['L01', 1, 'T3', 'H', 1, 'T2', 'H', 'split', 'T2', 'H']])
    conf = os.path.join(tmp, 'confusion.tsv')
    res = run('confusion', os.path.join(leaf, 'passC_agreement.tsv'), os.path.join(leaf2, 'passC_agreement.tsv'),
              '--out', conf, '--target', 'leaf2')
    c = read(conf)
    check(res['pairs_read'] == 6 and res['swaps'] == 4 and c[0]['label_a'] == 'T2' and c[0]['label_b'] == 'T3'
          and c[0]['n'] == '3' and c[0]['n_target'] == '1' and len(c) == 2, f'1 confusion counts {res} {c[:1]}')

    # packet: passC follows the agreement merged column, plus one single-reader tail row on L02
    PH = ['passage', 'pos', 'sign_id', 'conf', 'note']
    tsv(os.path.join(leaf, 'passC.tsv'), PH, [['L01', 1, 'T1', 'H', ''], ['L01', 2, 'T2', 'H', ''],
                                              ['L01', 3, 'T4', 'H', ''], ['L01', 4, 'T6', 'M', ''],
                                              ['L02', 1, 'T3', 'M', ''], ['L02', 2, 'T5', 'M', 'tail']])
    cells = [dict(id=f'T{i}', value=v, kind='letter') for i, v in enumerate('abcdefgh', 1)]
    json.dump(cells, open(os.path.join(tmp, 'map.json'), 'w'))
    Image.new('RGB', (9 * 20, 20), 'white').save(os.path.join(tmp, 'sheet.png'))
    tsv(os.path.join(tmp, 'crop_L01.jpg'), ['x'], [])
    out = os.path.join(tmp, 'pk')
    res = run('packet', '--agreement', os.path.join(leaf, 'passC_agreement.tsv'), '--confusion', conf, '--top', '1',
              '--sheet', os.path.join(tmp, 'sheet.png'), '--sheet-map', os.path.join(tmp, 'map.json'),
              '--out', out, '--run', 'leaf1', '--cell', '20', '--crops', tmp)
    t = read(os.path.join(out, 'leaf1_tiles.tsv'))
    why = {(r['passage'], r['pos']): r['why'] for r in t}
    check(why == {('L01', '2'): 'split', ('L01', '4'): 'split', ('L02', '1'): 'split', ('L02', '2'): 'single'},
          f'2 flagged tiles {why}')
    prompt = open(os.path.join(out, 'leaf1_prompt.md')).read()
    check(os.path.exists(os.path.join(out, 'leaf1_candidates.png')) and 'crop_L01.jpg' in prompt
          and not any(f'\t{v}\t' in prompt or f' {v} ' in prompt for v in 'bcdef'), '2 candidate sheet + value-blind prompt')

    # reconcile
    tsv(os.path.join(out, 'leaf1_reread.tsv'), ['passage', 'pos', 'label', 'conf', 'second', 'note'], [
        ['L01', 2, 'T3', 'H', '', 'matches B'],       # 2-of-3 -> T3
        ['L01', 4, 'T8', 'H', '', 'matches neither'],   # unsettled, keeps T6
        ['L02', 1, 'T2', 'L', '', 'low'],               # unsettled (L), keeps T3
        ['L02', 2, 'SPLIT:T5|T6', 'M', '', 'split']])   # unsettled, keeps T5
    pd, alt, foc = (os.path.join(out, x) for x in ('passD.tsv', 'passD_alt.tsv', 'focus.tsv'))
    res = run('reconcile', '--tiles', os.path.join(out, 'leaf1_tiles.tsv'), '--passc', os.path.join(leaf, 'passC.tsv'),
              '--reread', os.path.join(out, 'leaf1_reread.tsv'), '--out', pd, '--alt', alt, '--focus', foc)
    d = [r['sign_id'] for r in read(pd)]; da = [r['sign_id'] for r in read(alt)]
    f = open(foc).read().splitlines()
    check(d == ['T1', 'T3', 'T4', 'T6', 'T3', 'T5'], f'3 primary 2-of-3 only {d}')
    check(da == ['T1', 'T3', 'T4', 'T8', 'T3', 'T5'], f'3 alt takes every firm label {da}')
    check(res['relabelled'] == 1 and res['unsettled'] == 3 and len(f) == 3 and f[0].startswith('leaf1_L01_4\t'),
          f'3 counts + focus {res} {f[:1]}')

    # 4. reproduce the target-local output
    H = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/harvest')
    if os.path.exists(os.path.join(H, 'lookalike/f168_reread.tsv')):
        o = os.path.join(tmp, 'f168_passD.tsv')
        run('reconcile', '--tiles', os.path.join(H, 'lookalike/f168_tiles.tsv'), '--passc', os.path.join(H, 'f168/passC.tsv'),
            '--reread', os.path.join(H, 'lookalike/f168_reread.tsv'), '--out', o)
        a = open(o).read().replace('\r\n', '\n'); b = open(os.path.join(H, 'lookalike/f168_passD.tsv')).read().replace('\r\n', '\n')
        check(a == b, '4 reproduces NEVBIR-LOOKALIKE f168_passD.tsv')
    else:
        print('SKIP 4 (target folder absent)')
finally:
    shutil.rmtree(tmp)
print('ALL PASS' if not fails else f'{fails} FAIL')
sys.exit(1 if fails else 0)
