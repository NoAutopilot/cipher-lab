"""VERIFY-MONLUC: committed C-graded tokens split by the confirm-run they sit in (run = consecutive confirms on consecutive clear letters)."""
import sys, csv, collections
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, sys.argv[1] + '/c269')
import align_c268 as A, align_c269 as B
def runlen(rows):
    out = {}; seq = []; last = None
    def flush():
        for r in seq: out[(r['line'], r['pos'])] = len(seq)
    for r in rows:
        if r['value'] is None and not r['clear']: continue
        if r['kind'] == 'confirm' and last is not None and r['cpos'] == last + 1: seq.append(r)
        else:
            flush(); seq = [r] if r['kind'] == 'confirm' else []
        last = r['cpos'] if r['kind'] == 'confirm' else None
    flush(); return out
words = A.load_clear(); clear = ''.join(w[2] for w in words); unsure = [w[3] for w in words for _ in w[2]]
_, p, _, end = A.align(A.load_tokens(), clear); r268 = runlen(A.classify(A.load_tokens(), clear, p, unsure))
key = {l.split('\t')[0]: l.split('\t')[2] for l in list(open(A.HERE / 'key.tsv'))[1:]}
toks = [{'line': f[0], 'pos': int(f[1]), 'sign': f[2], 'conf': f[3], 'value': A.fold(key[f[2]]) if key.get(f[2]) else None}
        for fn, g in B.BANDS for f in [l.rstrip('\n').split('\t') for l in open(B.HERE / fn)][1:]]
_, p, _, _ = A.align(toks, clear[end:]); r269 = runlen(A.classify(toks, clear[end:], p, unsure[end:]))
for job, rl in (('c268', r268), ('c269', r269)):
    T = list(csv.DictReader(open(A.HERE / f'reading_tokens_{job}.tsv'), delimiter='\t'))
    c = collections.Counter()
    band = collections.Counter()
    for t in T:
        if t['grade'] != 'C': continue
        n = rl.get((t['line'], int(t['pos'])), 0)
        k = 'run>=3' if n >= 3 else ('run1-2' if n else 'not-confirm(fill)')
        c[k] += 1
    print(job, dict(c), flush=True)
