#!/usr/bin/env python3
"""R12A-SEUT (6 Oct 2026): PREREG-SEUT gate. Do the blind Tournon passes align with the slip decipherment into a key?
Runs the power control first (synthetic homophonic+word-code cipher of the slip text at err 0.32), then each pass vs its
wrong-text null. Writes result_seut.json and, if both passes PASS, key_seut.tsv. --check re-runs and compares to the JSON."""
import sys, os, re, gzip, json, random
import numpy as np
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '../../../..'))
sys.path.insert(0, os.path.join(root, 'tools'))
import stream_align as sa
SET = dict(band=80, step=100, iters=3)
def letters(t): return [ord(c) - 97 for c in re.sub('[^a-z]', '', t.lower())]
def slip_text():
    t = ' '.join(l.split(' ', 1)[1] for l in open(os.path.join(here, 'slip_read.txt')) if l[:1].isdigit())
    return re.sub(r'[\[\]?]', '', t)
def stream(p):
    toks = []
    for l in open(os.path.join(here, p)):
        if not l.startswith('L'): continue
        toks += [x for x in l.rstrip('\n').split('\t')[1].split() if x != 'NONE']
    ids, out = {}, []
    for k, x in enumerate(toks):
        key = x if x != '??' else '??%d' % k
        out.append(ids.setdefault(key, len(ids)))
    return out, ids
def S(sym, let):
    counts, _ = sa.learn(sym, let, max(sym) + 1, slope=len(let) / len(sym), **SET)
    return float(sa.nw_score(sa.decode(counts), let))
def corpus():
    t = ''
    for f in sorted(os.listdir(os.path.join(root, 'tools/data/fr16'))):
        if f.endswith('.gz'): t += gzip.open(os.path.join(root, 'tools/data/fr16', f), 'rt', errors='ignore').read()
    return letters(t)
def nulls(sym, words, n_let, C):
    r = random.Random(12); out = []
    for _ in range(20):
        s = r.randrange(len(C) - n_let); out.append(S(sym, C[s:s + n_let]))
    r = random.Random(13)
    for _ in range(20):
        w = words[:]; r.shuffle(w); out.append(S(sym, letters(' '.join(w))))
    return out
CODES = ['de', 'le', 'la', 'que', 'qui', 'et', 'du', 'par', 'il', 'a', 'est']
def synth(words, seed, err=0.32):
    r = random.Random(seed); let = letters(' '.join(words))
    freq = np.bincount(let, minlength=26).astype(float)
    k = np.maximum(1, np.round(freq / freq.sum() * 40)).astype(int)
    while k.sum() > 40: k[k.argmax()] -= 1
    hom, nid = {}, 0
    for a in range(26):
        hom[a] = list(range(nid, nid + k[a])); nid += k[a]
    code = {w: nid + i for i, w in enumerate(CODES)}; nsym = nid + len(CODES)
    sym = []
    for w in words:
        lw = re.sub('[^a-z]', '', w.lower())
        if lw in code: sym.append(code[lw]); continue
        sym += [r.choice(hom[c]) for c in letters(lw)]
    sym = [x if r.random() >= err else r.choice([y for y in range(nsym) if y != x]) for x in sym]
    return sym, let
def main():
    words = slip_text().split(); let = letters(' '.join(words)); C = corpus()
    res = {'settings': SET, 'n_letters': len(let), 'control': [], 'targets': {}}
    for seed in (21, 22, 23):
        sym, sl = synth(words, seed); s = S(sym, sl); nl = nulls(sym, words, len(sl), C)
        res['control'].append({'seed': seed, 'n_sym': len(sym), 'S': round(s, 4), 'null_mean': round(float(np.mean(nl)), 4),
                               'null_p95': round(float(np.percentile(nl, 95)), 4), 'pass': s > np.percentile(nl, 95)})
    res['power'] = bool(sum(bool(c['pass']) for c in res['control']) >= 2)
    for c in res['control']: c['pass'] = bool(c['pass'])
    if res['power']:
        for p in ('passA.tsv', 'passB.tsv'):
            sym, ids = stream(p); s = S(sym, let); nl = nulls(sym, words, len(let), C)
            res['targets'][p] = {'n_sym': len(sym), 'n_ids': len(ids), 'S': round(s, 4), 'null_mean': round(float(np.mean(nl)), 4),
                                 'null_p95': round(float(np.percentile(nl, 95)), 4), 'null_max': round(float(max(nl)), 4),
                                 'pass': bool(s > np.percentile(nl, 95))}
    return res
if __name__ == '__main__':
    r = main(); out = os.path.join(here, 'result_seut.json')
    if '--check' in sys.argv:
        old = json.load(open(out)); ok = old == json.loads(json.dumps(r)); print('check', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    json.dump(r, open(out, 'w'), indent=1); print(json.dumps(r, indent=1))
