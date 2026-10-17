#!/usr/bin/env python3
"""ERR-SIM (PREREG-ERR-SIM.md): error-matched synthetic control for ink 63.

    python3 tx/err_sim/err_sim.py [--levels 0.05,0.10,...] [--seeds 1-5] [--controls] [--out result.json]

Encipher clerk-decipherment plaintext with key.tsv at ink 63's per-code frequencies and line/page shape, read it with two simulated
readers from the f.102r dev2 per-pass confusion (confusion_AB.tsv) scaled to an injected error, reconcile as viv63_decode does, grade,
and measure the longest all-H run, the longest all-H all-correct run and V_strict. Every number follows from the seed (random.Random).
"""
import csv, json, os, random, re, sys, unicodedata
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__)); TX = os.path.dirname(H); T = os.path.dirname(TX)
sys.path.insert(0, TX)
sys.argv_saved = list(sys.argv); sys.argv = [sys.argv[0], '--strict']   # viv54L_stretch reads --strict at vocab() time
import viv54L_stretch as vs  # noqa: E402
import viv63_decode as vd  # noqa: E402
sys.argv = sys.argv_saved
AD, AD34, AD_OLD = 94.6, 58.9, 42


def fold(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').replace('v', 'u').replace('j', 'i')


def plaintext(n):
    files = ['dec67_norm.txt', 'dec70_norm.txt'] + [f'dec_{p}_merged.txt' for p in ('f105v', 'f106r', 'f106v', 'f107r', 'f107v', 'f108r', 'f108v')]
    s = ''
    for f in files:
        x = open(os.path.join(TX, f), encoding='utf-8').read()
        x = re.sub(r'\{del:[^}]*\}', '', x); x = re.sub(r'\{add:([^}]*)\}', r'\1', x)
        s += re.sub(r'[^a-z]', '', fold(x))
    src_len = len(s)
    while len(s) < n:
        s += s
    return s[:n], src_len


def target_shape():
    rows = list(csv.DictReader(open(os.path.join(T, 'reading_piece63.tsv')), delimiter='\t'))
    freq = Counter(c for r in rows for c in r['codes'].split())
    return [(r['page'], len(r['codes'].split())) for r in rows], freq, rows


def load_key():
    k = {}
    for r in csv.DictReader(open(os.path.join(T, 'key.tsv')), delimiter='\t'):
        k[r['code']] = (r['meaning'], r['grade'])
    return k


def load_conf():
    M = {'A': defaultdict(dict), 'B': defaultdict(dict)}
    for ln in open(os.path.join(H, 'confusion_AB.tsv')):
        if ln.startswith('#') or ln.startswith('pass\t'):
            continue
        p, t, r, pr = ln.rstrip('\n').split('\t')
        M[p][t][r] = float(pr)
    return M


def runs(grades, letters, truth):
    best = bestc = cur = curc = 0
    for g, l, tr in zip(grades, letters, truth):
        if g == 'H':
            cur += 1; curc = curc + 1 if l == tr else 0
        else:
            cur = curc = 0
        best = max(best, cur); bestc = max(bestc, curc)
    return best, bestc


def v_strict(pages_text, V):
    b = 0
    for s in pages_text:
        st = vs.stretches(s, V, 1)
        if st:
            b = max(b, st[0][1] - st[0][0])
    return b


def run(e, seed, key, freq, shape, M, pt, V, shuffled=False, do_v=True):
    rng = random.Random(f'ERR-SIM-{e}-{seed}-{shuffled}')
    by_letter = defaultdict(list)
    for c, (m, g) in key.items():
        by_letter[m].append(c)
    cipher = []
    for ch in pt:
        cs = by_letter.get(ch)
        cipher.append(rng.choices(cs, weights=[freq.get(c, 0) + 1 for c in cs])[0] if cs else 'X_' + ch)
    signs = sorted(key)
    tf = Counter(cipher)
    err_t = {t: 1 - M['A'][t].get(t, 0) for t in signs}
    # mean over the synthetic's own key-sign frequencies, per pass
    def scale(p):
        et = {t: 1 - M[p][t].get(t, 0) for t in signs}
        mean = sum(et[t] * tf[t] for t in signs) / max(1, sum(tf[t] for t in signs))
        return et, mean
    sc = {p: scale(p) for p in 'AB'}

    def read(p, t):
        if t not in key or e == 0:
            return t
        et, mean = sc[p]
        if rng.random() < min(0.9, e * et[t] / mean):
            row = {r: q for r, q in M[p][t].items() if r != t}
            return rng.choices(list(row), weights=list(row.values()))[0]
        return t
    kv = dict(key)
    if shuffled:
        vals = [key[c][0] for c in signs]; rng.shuffle(vals)
        kv = {c: (v, key[c][1]) for c, v in zip(signs, vals)}
    grades, letters = [], []
    for t in cipher:
        a, b = read('A', t), read('B', t)
        flag = False
        if a != b:
            w = vd.RULES.get(frozenset((a, b)))
            if w:
                a = w
            else:
                flag = True
        if a not in kv:
            grades.append('U'); letters.append('_')
        else:
            grades.append('M' if (flag or kv[a][1] == 'M') else 'H'); letters.append(kv[a][0])
    hrun, hrun_c = runs(grades, letters, pt)
    vstr = None
    if do_v:
        pages, i = defaultdict(str), 0
        for pg, n in shape:
            pages[pg] += ''.join(letters[i:i + n]); i += n
        vstr = v_strict(list(pages.values()), V)
    return {'e': e, 'seed': seed, 'shuffled_key': shuffled, 'hrun': hrun, 'hrun_correct': hrun_c, 'v_strict': vstr,
            'H_share': round(grades.count('H') / len(grades), 3), 'M_share': round(grades.count('M') / len(grades), 3)}


def main():
    a = sys.argv
    levels = [float(x) for x in (a[a.index('--levels') + 1] if '--levels' in a else '0.05,0.10,0.14,0.19,0.23').split(',')]
    s0, s1 = (a[a.index('--seeds') + 1] if '--seeds' in a else '1-5').split('-')
    seeds = range(int(s0), int(s1) + 1)
    out = a[a.index('--out') + 1] if '--out' in a else os.path.join(H, 'result.json')
    shape, freq, rows = target_shape(); key = load_key(); M = load_conf()
    pt, src_len = plaintext(sum(n for _, n in shape))
    sv = sys.argv; sys.argv = [sv[0], '--strict']; V = vs.vocab(); sys.argv = sv   # strict vocabulary (V_strict)
    # self-check: the run function on the target's own grades gives depth_stats' primary_run (40)
    tg = ''.join(r['grades'] for r in rows); td = ''.join(r['decode'] for r in rows)
    chk = runs(tg, td, td)[0]
    res = {'plaintext_source_letters': src_len, 'letters': len(pt), 'AD': AD, 'AD_R34': AD34, 'target_hrun_check': chk, 'runs': []}
    if '--controls' in a:
        for s in seeds:
            res['runs'].append(run(0.0, s, key, freq, shape, M, pt, V))
            res['runs'].append(run(0.0, s, key, freq, shape, M, pt, V, shuffled=True))
    else:
        for e in levels:
            for s in seeds:
                r = run(e, s, key, freq, shape, M, pt, V); res['runs'].append(r)
                print(json.dumps(r), flush=True)
    json.dump(res, open(out, 'w'), indent=1)
    for r in res['runs']:
        print(r)
    print('target hrun check', chk, 'plaintext source letters', src_len)


if __name__ == '__main__':
    main()
