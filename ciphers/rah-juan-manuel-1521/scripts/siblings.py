#!/usr/bin/env python3
"""R11-RJMSIB: shape and table fit of Juan Manuel's 1522 cipher against Alonso Sanchez's (siblings/PREREG.md).
Reads siblings/shapes.tsv, siblings/our_labels.tsv, alphabet.tsv and Tomokiyo's two code tables in sources/cryptiana/keys/.
Writes siblings/results.json; --check exits 1 if the committed file is stale. --all-signs adds firm=0 rows (sensitivity)."""
import csv, json, random, re, sys, os
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
N, SEED = 10000, 1522

def rows(p):
    with open(p) as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))

def tables(firm_only):
    t = {'JM': [], 'AS': []}
    for r in rows(os.path.join(T, 'siblings/shapes.tsv')):
        if firm_only and r['firm'] != '1': continue
        t[r['table']].append((r['shape'], r['letter']))
    return t

def V(jm, asg):
    a = defaultdict(set)
    for s, l in asg: a[s].add(l)
    return len({l for s, l in jm if l in a.get(s, ())})

def perm_null(stat, fixed, moving, rng):
    vals = [l for _, l in moving]; out = []
    for _ in range(N):
        rng.shuffle(vals); out.append(stat(fixed, [(s, v) for (s, _), v in zip(moving, vals)]))
    return out

def summ(real, null):
    s = sorted(null); q = lambda p: s[min(len(s) - 1, int(p * len(s)))]
    return {'real': real, 'null_mean': round(sum(s) / len(s), 3), 'p95': q(0.95), 'p99': q(0.99), 'max': s[-1],
            'p_ge': round(sum(x >= real for x in s) / len(s), 4)}

def W(ours, table):
    m = defaultdict(set)
    for s, l in table: m[s].add(l)
    return sum(1 for shp, val in ours if any(val.startswith(l) or (l == 'null' and val == '') for l in m.get(shp, ())))

def norm(w): return re.sub(r'[()?\[\]]', '', w.lower()).strip()

def codes(p):
    d = {}
    for r in rows(p):
        if r.get('sign') and r.get('value'): d.setdefault(norm(r['value']), r['sign'])
    return d

def spearman(xs, ys):
    def rk(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v)
        for k, i in enumerate(o): r[i] = k
        return r
    a, b = rk(xs), rk(ys); n = len(a)
    return round(1 - 6 * sum((x - y) ** 2 for x, y in zip(a, b)) / (n * (n * n - 1)), 3)

def run(firm_only=True):
    rng = random.Random(SEED); t = tables(firm_only); res = {'firm_only': firm_only, 'n_signs': {k: len(v) for k, v in t.items()}}
    v = V(t['JM'], t['AS']); res['V_shape_value_JM_vs_AS'] = summ(v, perm_null(V, t['JM'], t['AS'], rng))
    a = defaultdict(set); [a[s].add(l) for s, l in t['AS']]
    res['V_matches'] = sorted({f'{s}={l}' for s, l in t['JM'] if l in a.get(s, ())})
    js, ass = {s for s, _ in t['JM']}, {s for s, _ in t['AS']}
    res['inventory_overlap'] = {'shared': sorted(js & ass), 'JM_only': len(js - ass), 'AS_only': len(ass - js),
                                'jaccard': round(len(js & ass) / len(js | ass), 3)}
    res['shared_shape_values'] = {s: {'JM': sorted({l for x, l in t['JM'] if x == s}), 'AS': sorted(a[s])} for s in sorted(js & ass)}
    lab = {r['label']: r['shape'] for r in rows(os.path.join(T, 'siblings/our_labels.tsv'))}
    ours = [(lab.get(r['sign'], 'none'), r['letter']) for r in rows(os.path.join(T, 'alphabet.tsv')) if r['grade'] == 'C']
    res['ours_C'] = [f'{s}={l}' for s, l in ours]
    for k in ('JM', 'AS'):
        res[f'W_alphabet_tsv_vs_{k}'] = summ(W(ours, t[k]), perm_null(lambda o, tb: W(o, tb), ours, t[k], rng))
    jm = codes(os.path.join(ROOT, 'sources/cryptiana/keys/AlonsoSanchez_2.tsv'))
    asx = codes(os.path.join(ROOT, 'sources/cryptiana/keys/AlonsoSanchez_1.tsv'))
    common = sorted(set(jm) & set(asx)); same = [w for w in common if jm[w] == asx[w]]
    nullT = []
    cj = list(jm.values()); wj = list(jm)
    for _ in range(N):
        rng.shuffle(cj); pj = dict(zip(wj, cj)); nullT.append(sum(pj[w] == asx[w] for w in common))
    res['T_code_identity'] = summ(len(same), nullT)
    res['T_detail'] = {'words_in_both': len(common), 'same_code': same,
                       'examples': {w: [jm[w], asx[w]] for w in common[:12]}, 'n_codes': {'JM': len(jm), 'AS': len(asx)}}
    key = lambda c: c
    res['ordering_rho'] = {k: spearman(list(d), [d[w] for w in d]) for k, d in (('JM', jm), ('AS', asx))}
    res['code_finals'] = {k: ''.join(sorted({c[-1] for c in d.values() if len(c) == 3})) for k, d in (('JM', jm), ('AS', asx))}
    res['code_initials'] = {k: ''.join(sorted({c[0] for c in d.values()})) for k, d in (('JM', jm), ('AS', asx))}
    return res

if __name__ == '__main__':
    out = {'primary': run(True), 'sensitivity_all_signs': run(False)}
    p = os.path.join(T, 'siblings/results.json'); txt = json.dumps(out, indent=1, ensure_ascii=False) + '\n'
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(txt); print(txt)
