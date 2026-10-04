#!/usr/bin/env python3
"""KEY1629-XMATCH (4 Oct 2026): score key_aosb1629.tsv against every on-disk ciphertext flagged by inventory.py,
with aosb_crossmatch.py's functions loaded unchanged (its trailing main() call is not executed). PREREG-KEY1629-XMATCH.md.
    python3 xmatch.py [--check]   writes/compares xmatch_results.json"""
import os, sys, csv, re, json, random
H = os.path.dirname(os.path.abspath(__file__)); A = os.path.dirname(H); REPO = os.path.abspath(os.path.join(H, '../../../..'))
src = open(os.path.join(A, 'aosb_crossmatch.py')).read()
assert src.rstrip().endswith('main()')
CM = {'__file__': os.path.join(A, 'aosb_crossmatch.py'), '__name__': 'aosb_crossmatch'}
exec(compile(src.rstrip()[:-len('main()')], CM['__file__'], 'exec'), CM)
sys.path.insert(0, H); import inventory as INV   # re-writes inventory.tsv deterministically

def canonical():
    rows = list(csv.DictReader(open(os.path.join(H, 'inventory.tsv')), delimiter='\t'))
    by = {}
    for r in rows:
        if r['folder'] == 'riksarkivet-r4282-1628': continue
        if not (r['a_kw'] == '1' or r['b_1620_40'] == '1' or r['c_numeric'] == '1'): continue
        by.setdefault(r['folder'], []).append(r)
    out = []
    for f, rs in sorted(by.items()):
        def rank(r):
            b = os.path.basename(r['file'])
            return (0 if 'verified' in b else 1 if b in ('ciphertext.txt', 'ciphertext.tsv') and r['file'].count('/') == 2 else 2, -int(r['tokens']))
        out.append(sorted(rs, key=rank)[0])
    return out

def stream(path):
    st = []
    for t in INV.tokens(os.path.join(REPO, path)):
        x = t.strip('?.,;:()[]')
        st.append(x if x else None)
    return st

def main():
    rows = CM['load_align'](); lines = sorted({r['cipher_line'] for r in rows})
    pairs = {r['plain_line']: r for r in csv.DictReader(open(os.path.join(A, 'pairs.tsv')), delimiter='\t')}
    folds = [(CM['aosb_stream'](pairs[l]['cipher_raw']), CM['keyfrom'](CM['load_align'](exclude=l))) for l in lines]
    res = {'prereg': 'aosb/xmatch/PREREG-KEY1629-XMATCH.md', 'control_lofo': CM['run_arm'](folds), 'targets': {}}
    c = res['control_lofo']
    if not (c['C'] >= 0.5 and c['S'] is not None and c['S'] > c['null_p99']):
        res['stop'] = 'CONTROL FAIL: untested-by-this-tool'
    else:
        key = CM['keyfrom'](rows)
        for r in canonical():
            a = CM['run_arm']([(stream(r['file']), key)])
            a.update({'file': r['file'], 'flags': ''.join(k for k, f in (('a', 'a_kw'), ('b', 'b_1620_40'), ('c', 'c_numeric')) if r[f] == '1')})
            res['targets'][r['folder']] = a
    txt = json.dumps(res, indent=1, ensure_ascii=False) + '\n'; p = os.path.join(H, 'xmatch_results.json')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print('ok' if ok else 'STALE ' + p); sys.exit(0 if ok else 1)
    open(p, 'w').write(txt)
    print('control', c)
    for f, a in res['targets'].items():
        print('%-36s %-4s C=%.3f S=%s p99=%s geS=%s %s' % (f, a['flags'], a['C'], a['S'], a['null_p99'], a['share_null_ge_S'], a['verdict']))
main()
