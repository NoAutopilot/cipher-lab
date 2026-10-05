#!/usr/bin/env python3
"""Offline test for tools/lookalike_pass.py audit / audit-score (TX-AGREEAUDIT, 4 Oct 2026; no network, temp folder only).
1. agreed_positions: a C position counts as agreed only when A, B and C carry the same label after per-line alignment
   (a sign dropped by reader A shifts the alignment instead of breaking the rest of the line).
2. audit (case it must catch): --include positions are always audited and never planted; plants are swapped to the
   label's top confusion partner and keep the original among the candidates; the prompt carries ids only (no sheet-map
   value) and brackets the audited positions; (case it must NOT trip on) a [PLAIN:...] token in the reading is context.
3. audit-score, the fixed rule: a firm pick != shown flags; a planted item is caught only when the pick is the original;
   (case it must NOT count) an L, SPLIT or X_NEW answer is never a flag; a catch below the gate reports NON-TEST and the
   CLI exits 3; with a truth file, fixed / broken are counted on unplanted items only and --out-corrected applies flags.
Run: python3 tools/tests/test_lookalike_audit.py"""
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
    H = ['line', 'pos', 'sign']
    C = [('X_L01', i + 1, s) for i, s in enumerate(['T1', 'T2', 'T3', 'T4', 'T5', 'T1', 'T2', 'T3'])] + \
        [('X_L02', i + 1, s) for i, s in enumerate(['T2', 'T3', 'T1', 'T4'])]
    A = [r for r in C if (r[0], r[1]) != ('X_L01', 2)]                     # reader A drops one sign
    B = [(l, p, 'T9' if (l, p) == ('X_L01', 4) else s) for l, p, s in C]   # reader B differs at L01.4
    for n, rows in (('A', A), ('B', B), ('C', C)):
        tsv(os.path.join(tmp, f'p{n}.tsv'), H, rows)
    ag = lp.agreed_positions(lp._norm(os.path.join(tmp, 'pA.tsv')), lp._norm(os.path.join(tmp, 'pB.tsv')),
                             lp._norm(os.path.join(tmp, 'pC.tsv')))
    notag = [(l, p) for l, p, s, ok in ag if not ok]
    check(notag == [('X_L01', 2), ('X_L01', 4)], f'1 agreed positions exclude the dropped and the split sign {notag}')

    conf = os.path.join(tmp, 'conf.tsv')
    tsv(conf, ['label_a', 'label_b', 'n', 'n_target', 'examples'],
        [['T1', 'T7', 5, 0, ''], ['T2', 'T8', 4, 0, ''], ['T3', 'T6', 3, 0, ''], ['T4', 'T5', 2, 0, '']])
    sheet = os.path.join(tmp, 'sheet.png'); Image.new('RGB', (990, 660), 'white').save(sheet)
    smap = os.path.join(tmp, 'map.json')
    json.dump([{'id': f'T{i}', 'value': f'VAL{i}', 'kind': 'letter'} for i in range(1, 10)], open(smap, 'w'))
    inc = os.path.join(tmp, 'inc.tsv'); tsv(inc, ['line', 'pos'], [['X_L02', 3]])
    out = os.path.join(tmp, 'out')
    res = run('audit', '--passa', os.path.join(tmp, 'pA.tsv'), '--passb', os.path.join(tmp, 'pB.tsv'),
              '--passc', os.path.join(tmp, 'pC.tsv'), '--confusion', conf, '--sample', '9', '--plant', '0.5',
              '--seed', '3', '--include', inc, '--sheet', sheet, '--sheet-map', smap, '--out', out, '--run', 'T')
    items = read(os.path.join(out, 'T_audit_items.tsv'))
    forced = [i for i in items if i['forced'] == '1']
    planted = [i for i in items if i['planted'] == '1']
    check(res['agreed'] == 10 and len(items) == 10 and len(forced) == 1 and forced[0]['planted'] == '0'
          and forced[0]['line'] == 'X_L02' and forced[0]['pos'] == '3', f'2a include forced, never planted {res}')
    pmap = {'T1': 'T7', 'T2': 'T8', 'T3': 'T6', 'T4': 'T5', 'T5': 'T4'}
    check(len(planted) == 5 and all(i['shown'] == pmap[i['original']] and i['original'] in i['candidates'].split(',')
                                    for i in planted), '2b plants swapped to top partner, original kept as candidate')
    prompt = open(os.path.join(out, 'T_audit_prompt.md')).read()
    check('VAL' not in prompt and prompt.count('[') >= 10, '2c prompt value-blind, audited positions bracketed')

    # 2d (case it must NOT trip on): a transcription's own bracketed token ([PLAIN:Et], D2-C1161AUD 5 Oct 2026) beside an
    # audited position under --hide-passc is context, not an audit bracket
    Cp = [('X_L01', 1, '[PLAIN:Et]')] + [(l, p + 1, s) for l, p, s in C if l == 'X_L01']
    tsv(os.path.join(tmp, 'pP.tsv'), H, Cp)
    resp = run('audit', '--passa', os.path.join(tmp, 'pP.tsv'), '--passb', os.path.join(tmp, 'pP.tsv'),
               '--passc', os.path.join(tmp, 'pP.tsv'), '--confusion', conf, '--sample', '9', '--plant', '0',
               '--seed', '3', '--sheet', sheet, '--sheet-map', smap, '--out', os.path.join(tmp, 'outP'), '--run', 'P',
               '--hide-passc')
    check(resp['items'] == 9, f'2d [PLAIN:..] token in the reading does not break the audit prompt {resp}')

    # 3. score: answer every item; planted: catch all but one; unplanted: flag one firm, one L, one SPLIT, one X_NEW
    rows, unpl = [], [i for i in items if i['planted'] == '0']
    for i in items:
        lab, cf = i['shown'], 'H'
        if i['planted'] == '1':
            lab = i['original'] if i is not planted[-1] else i['shown']
        rows.append([i['item'], lab, cf, '', ''])
    alt = {unpl[0]['item']: [pmap.get(unpl[0]['original'], 'T9'), 'H'], unpl[1]['item']: ['T9', 'L'],
           unpl[2]['item']: ['SPLIT:T1|T2', 'M'], unpl[3]['item']: ['X_NEW', 'H']}
    rows = [[r[0], *alt[r[0]], '', ''] if r[0] in alt else r for r in rows]
    rr = os.path.join(tmp, 'rr.tsv'); tsv(rr, ['item', 'label', 'conf', 'second', 'note'], rows)
    truth = os.path.join(tmp, 'truth.tsv')
    trows = []
    for l, p, s in C:
        tr = s
        if (l, str(p)) == (unpl[0]['line'], unpl[0]['pos']):
            tr = alt[unpl[0]['item']][0]                                  # the one firm flag is a real fix
        trows.append([l, p, s, tr, 'x', 'scored'])
    tsv(truth, ['line', 'pos', 'ref_sign', 'truth', 'plain', 'status'], trows)
    corr = os.path.join(tmp, 'corr.tsv')
    sc = lp.audit_score(os.path.join(out, 'T_audit_items.tsv'), rr, truth, os.path.join(tmp, 'pC.tsv'), corr)
    check(sc['planted'] == 5 and sc['planted_caught'] == 4 and sc['catch'] == 0.8 and sc['control'] == 'PASS',
          f'3a catch 4/5 = gate {sc}')
    check(sc['unplanted_flagged'] == 1 and sc['fixed'] == 1 and sc['broken'] == 0, '3b L/SPLIT/X_NEW never flag; fix counted')
    cr = {(r['line'], r['pos']): r['sign'] for r in read(corr)}
    check(cr[(unpl[0]['line'], unpl[0]['pos'])] == alt[unpl[0]['item']][0], '3c --out-corrected applies the flag')
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            lp.main(['audit-score', '--items', os.path.join(out, 'T_audit_items.tsv'), '--reread', rr, '--gate', '0.9'])
        check(False, '3d below gate exits 3')
    except SystemExit as e:
        check(e.code == 3, f'3d below gate exits 3 ({e.code})')
finally:
    shutil.rmtree(tmp)
print('ALL PASS' if not fails else f'{fails} FAIL'); sys.exit(1 if fails else 0)
