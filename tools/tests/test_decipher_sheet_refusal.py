#!/usr/bin/env python3
"""Offline test for decipher_sheet.py's open-blind-sort refusal (MQS-SHEET-REFUSAL, 9 Oct 2026; PREREG-MQS-SHEET-REFUSAL.md).
K1-K2: the Birago 1572 family (ASKS 118 open in tools/data/sorter_families.tsv) is refused, key and reading; K3-K4: Gramont and
Danzay render. Controls that can differ: N1 the same Birago targets against a register with the open sorts emptied render; N2
Gramont against a register listing an open sort for --key-family is refused. Needs no cv2 (--tiles none). Writes only to a temp dir.
Run: python3 tools/tests/test_decipher_sheet_refusal.py"""
import csv, os, shutil, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
os.chdir(ROOT)
import decipher_sheet as ds

CFG = os.path.join(ROOT, 'tools', 'tests', 'decode_configs')
GRA = os.path.join(ROOT, 'ciphers', 'fr2980-gramont')
DAN = os.path.join(ROOT, 'ciphers', 'fr20140-danzay-1557')
BIR = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572')
B52 = os.path.join(ROOT, 'ciphers', 'birago-fr3252-1571-72')
TMP = tempfile.mkdtemp()
fails = 0
def t(ok, msg):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', msg)

def run(mode, target, *extra):
    out = os.path.join(TMP, f'{mode}_{os.path.basename(target)}_{len(os.listdir(TMP))}.html')
    try:
        rc = ds.main([mode, target, '--out', out, '--tiles', 'none'] + list(extra))
    except SystemExit as e:
        return 'refused', str(e)
    return ('rendered' if rc == 0 and os.path.exists(out) and os.path.getsize(out) > 0 else f'rc={rc}'), ''

def register(edit):
    with open(ds.FAMILIES, encoding='utf-8') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    cols = list(rows[0].keys())
    rows = edit(rows)
    p = os.path.join(TMP, f'fam{len(os.listdir(TMP))}.tsv')
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, cols, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
    return p

live = {r['family']: r for r in csv.DictReader(open(ds.FAMILIES, encoding='utf-8'), delimiter='\t')}
t((live.get('nevers-birago-1572', {}).get('open_blind_sorts') or '').strip() != '', 'precondition: the live register lists open blind sorts for nevers-birago-1572 (ASKS 118)')

GJ = ['--config', os.path.join(CFG, 'fr2980-gramont.json'), '--job', 'ciphertext.txt']
DJ = ['--config', os.path.join(CFG, 'fr20140-danzay-1557.json'), '--job', 'ciphertext.txt']
BJ = ['--job', 'f178v']

# K1-K4 against the live register
for mode in ('key', 'reading'):
    s, msg = run(mode, BIR, *BJ)
    t(s == 'refused' and 'nevers-birago-1572' in msg and 'ASKS-118' in msg, f'K1 Birago 1572 {mode} sheet refused, naming the family and its open sorts')
s, msg = run('reading', B52)
t(s == 'refused' and 'nevers-birago-1572' in msg, 'K2 birago-fr3252-1571-72 (1572 key by path) refused')
for mode in ('key', 'reading'):
    t(run(mode, GRA, *GJ)[0] == 'rendered', f'K3 Gramont {mode} sheet renders')
    t(run(mode, DAN, *DJ)[0] == 'rendered', f'K4 Danzay {mode} sheet renders')

# key-path route: a sibling folder not in KEY_FAMILY_TARGETS whose job reads a key from a family folder is refused
sib = os.path.join(TMP, 'sibling'); os.makedirs(sib)
open(os.path.join(sib, 'tokens.tsv'), 'w').write('line\tpos\tsign\tvalue\tgrade\nL1\t1\tx1\ta\tH\n')
s, _ = run('key', sib, '--tokens-tsv', os.path.join(sib, 'tokens.tsv'), '--key-tsv', os.path.join(BIR, 'key.tsv'))
t(s == 'refused', 'a folder outside the table using a Birago 1572 key path is refused')
s, _ = run('key', sib, '--tokens-tsv', os.path.join(sib, 'tokens.tsv'))
t(s == 'rendered', 'the same folder with no family key renders')

# N1: same Birago targets, register with the open sorts emptied -> render (the refusal follows the register, not the slug)
n1 = register(lambda rows: [dict(r, open_blind_sorts='') for r in rows])
for mode in ('key', 'reading'):
    s, msg = run(mode, BIR, *BJ, '--families', n1)
    t(s == 'rendered', f'N1 Birago 1572 {mode} sheet renders when the register lists no open sort ({s} {msg[:80]})')
# N2: Gramont, register with an open sort for a family named by --key-family -> refused
n2 = register(lambda rows: rows + [dict(family='test-gramont', open_blind_sorts='TEST-1', nonblind_shown='', note='test')])
s, msg = run('reading', GRA, *GJ, '--families', n2, '--key-family', 'test-gramont')
t(s == 'refused' and 'TEST-1' in msg, 'N2 Gramont refused when its named family has an open sort')
t(run('reading', GRA, *GJ, '--families', n1, '--key-family', 'test-gramont')[0] == 'rendered', 'N2 control: same family absent from the register renders')

shutil.rmtree(TMP)
sys.exit(1 if fails else 0)
