#!/usr/bin/env python3
"""BAL103-200: f.200r blind passes vs its period decipherment (registered in b200/PREREG-BAL103-200.md; copy of b189/score189.py, file names only).
Decodes each transcription (passA, passB, reconciliation) with key_decode.tsv (first value of a|b; =N word codes expand;
[clear words] enter the alignment as letters but are excluded from A), semi-global-aligns it to the decipherment
(calib.py's unit-cost DP), A = matched cipher-derived letters / cipher-derived letters; control = 200 permutations of the
single-letter cell values (seed 1644); wrong-span null descriptive. Per-sign table classes and the 9 counts as registered.
Writes b200/result.tsv, b200/sign_table.tsv, b200/nines.tsv; --check exits 1 if the committed files are stale."""
import sys, os, random, unicodedata
from collections import defaultdict
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if c.isalpha() and ord(c) < 128)
    return s.replace('j', 'i').replace('v', 'u')
key = {}
for ln in open(os.path.join(T, 'key_decode.tsv')):
    if ln.startswith('#') or ln.startswith('code\t'): continue
    c, v = ln.rstrip('\n').split('\t')[:2]; key[c] = v
first = {c: v.split('|')[0] for c, v in key.items()}
def tokens(path):
    """(line, token) in page order; s2 rows start at their |> marker (overlap dropped)."""
    out_all = []
    rows = [ln for ln in open(path) if not (ln.startswith('#') or not ln.strip() or '\t' not in ln)]
    # BAL103-200: pass B was written in its reading order (L20 first); sort rows into page order (line, segment) as the
    # docstring requires -- the only change from score189.py besides file names (NOTES.md BAL103-200 section).
    rows.sort(key=lambda ln: (int(ln.split('\t', 1)[0].split('_')[-2][1:]), ln.split('\t', 1)[0].split('_')[-1]))
    for ln in rows:
        cid, tt = ln.rstrip('\n').split('\t', 1); parts = cid.split('_'); line = int(parts[-2][1:]); seg = parts[-1]
        out, buf = [], None
        for t in tt.split(' '):
            if not t: continue
            if buf is not None:
                buf += ' ' + t
                if buf.count('{') <= buf.count('}') and buf.count('[') <= buf.count(']'): out.append(buf); buf = None
            elif (t.startswith('?{') and '}' not in t) or (t.startswith('[') and ']' not in t) or \
                 (t.startswith('|>[') and ']' not in t) or (t.startswith('|>?{') and '}' not in t): buf = t
            else: out.append(t)
        if buf: out.append(buf)
        if seg == 's2':
            i = next((k for k, t in enumerate(out) if t.startswith('|>')), None)
            out = [] if i is None else [out[i][2:]] + out[i + 1:]
        for t in out: out_all.append((line, t if t.startswith(('?', '[')) else t.split('|')[0]))
    return out_all
def expand(toks, km):
    """E = [(token index, sign, letter, is_clear)]"""
    E = []
    for ti, (line, s) in enumerate(toks):
        if s.startswith('['): v, clear = s.strip('[]'), True
        elif s.startswith('?'): continue
        else:
            v = km.get(s) if s in km else first.get(s); clear = False
            if not v or v.startswith('?') or v.upper() == 'U': continue
        for ch in norm(v): E.append((ti, s, ch, clear))
    return E
P = norm(''.join(l for l in open(os.path.join(H, 'f205r_decipherment.txt')) if not l.startswith('#')))
def align(D, P):
    n, m = len(D), len(P)
    sc = [[0] * (m + 1) for _ in range(n + 1)]; bt = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): sc[i][0] = i; bt[i][0] = 1
    for i in range(1, n + 1):
        Di = D[i-1]; prev = sc[i-1]; cur = sc[i]; b = bt[i]
        for j in range(1, m + 1):
            a = prev[j-1] + (0 if Di == P[j-1] else 1); d = prev[j] + 1; c = cur[j-1] + 1
            if a <= d and a <= c: cur[j] = a; b[j] = 0
            elif d <= c: cur[j] = d; b[j] = 1
            else: cur[j] = c; b[j] = 2
    j = min(range(m + 1), key=lambda j: sc[n][j]); i = n; pairs = []
    while i > 0:
        if j > 0 and bt[i][j] == 0: pairs.append((i-1, j-1)); i -= 1; j -= 1
        elif bt[i][j] == 1 or j == 0: pairs.append((i-1, None)); i -= 1
        else: j -= 1
    return dict(pairs[::-1])
def stat(toks, km, PP):
    E = expand(toks, km); D = ''.join(e[2] for e in E); pr = align(D, PP)
    cip = [i for i, e in enumerate(E) if not e[3]]
    hit = sum(1 for i in cip if pr.get(i) is not None and D[i] == PP[pr[i]])
    return hit / max(1, len(cip)), E, pr, D
cells = sorted(c for c, v in first.items() if len(key[c]) == 1 and key[c].isalpha())
vals = [first[c] for c in cells]
def perm_job(args):
    toks, seed = args; rng = random.Random(seed); v2 = vals[:]; rng.shuffle(v2)
    km = dict(zip(cells, v2)); A, E, pr, D = stat(toks, km, P)
    per = defaultdict(lambda: [0, 0])
    for i, e in enumerate(E):
        if e[3] or e[1] not in km: continue
        per[e[1]][1] += 1
        if pr.get(i) is not None and D[i] == P[pr[i]]: per[e[1]][0] += 1
    return A, {s: tuple(v) for s, v in per.items()}
def classify(n, letters, s):
    vals_s = set(key.get(s, '').split('|'))
    if n < 2: return 'too-few'
    al = [x for x in letters if x != '-']
    inkey = sum(1 for x in letters if x in vals_s)
    if inkey >= (2 * n) / 3: return 'confirmed'
    if al:
        top = max(set(al), key=al.count); cnt = al.count(top)
        if top not in vals_s and (cnt == n or (n >= 4 and cnt >= 0.75 * n)): return 'contradicted:' + top
    return 'undecided'
def run():
    srcs = [('passA', 'f200r_passA.tsv'), ('passB', 'f200r_passB.tsv'), ('rec', 'f200r_rec.tsv')]
    res = ['transcription\tN_tokens\tcipher_letters\tclear_letters\tA\tperm_mean\tperm_p95\tperm_p99\twrong_span_A\tgate_part']
    tables = {}; nines_rows = ['transcription\tline\ttoken_index\taligned_letter\tcontext_D\tcontext_P\tstrict_known']
    pool = Pool(4)
    for name, fn in srcs:
        path = os.path.join(H, fn)
        if not os.path.exists(path): continue
        toks = tokens(path); A, E, pr, D = stat(toks, {}, P)
        perms = pool.map(perm_job, [(toks, 1644 * 1000 + k) for k in range(200)])
        pa = sorted(p[0] for p in perms); p95, p99 = pa[189], pa[197]; mean = sum(pa) / len(pa)
        Pw = P[len(P) // 2:] + P[:len(P) // 2]; Aw = stat(toks, {}, Pw)[0]
        ncl = sum(1 for e in E if e[3]); ncip = len(E) - ncl
        res.append(f"{name}\t{len(toks)}\t{ncip}\t{ncl}\t{A:.3f}\t{mean:.3f}\t{p95:.3f}\t{p99:.3f}\t{Aw:.3f}\t"
                   f"{'PASS' if A >= 0.60 and A > p99 else 'FAIL'}")
        st = defaultdict(list)
        for i, e in enumerate(E):
            if e[3]: continue
            j = pr.get(i); st[e[1]].append(P[j] if j is not None else '-')
        obs = {s: sum(1 for i, e in enumerate(E) if e[1] == s and not e[3] and pr.get(i) is not None and D[i] == P[pr[i]])
               for s in st}
        share = {}
        for s in st:
            if s not in cells: share[s] = ''; continue
            ge = sum(1 for _, per in perms if per.get(s, (0, 1))[0] >= obs[s]); share[s] = f"{ge / 200:.3f}"
        tables[name] = (st, share)
        for i, e in enumerate(E):
            if e[1] != '9' or e[3]: continue
            j = pr.get(i); al = P[j] if j is not None else '-'
            nb = j is not None and all(pr.get(i + d) is not None and D[i + d] == P[pr[i + d]] and pr[i + d] == j + d
                                       for d in (-2, -1, 1, 2) if 0 <= i + d < len(D))
            cD = D[max(0, i-5):i] + '[' + D[i] + ']' + D[i+1:i+6]
            cP = (P[max(0, j-5):j] + '[' + P[j] + ']' + P[j+1:j+6]) if j is not None else '-'
            nines_rows.append(f"{name}\t{toks[e[0]][0]}\t{e[0]}\t{al}\t{cD}\t{cP}\t{'yes' if nb and al in 'irs' else 'no'}")
    pool.close()
    rows = ['sign\tkey_value\tn_rec\taligned_rec\tclass_rec\tperm_share_ge_rec\tn_A\taligned_A\tclass_A\tn_B\taligned_B\tclass_B']
    allsigns = set()
    for st, _ in tables.values(): allsigns |= set(st)
    def cell(name, s):
        if name not in tables or s not in tables[name][0]: return ['0', '', '']
        L = tables[name][0][s]; return [str(len(L)), ''.join(L), classify(len(L), L, s)]
    for s in sorted(allsigns, key=lambda s: (-len(tables.get('rec', ({}, {}))[0].get(s, [])), s)):
        r = cell('rec', s); sh = tables.get('rec', ({}, {}))[1].get(s, '')
        rows.append('\t'.join([s, key.get(s, '?'), *r, sh, *cell('passA', s), *cell('passB', s)]))
    return '\n'.join(res) + '\n', '\n'.join(rows) + '\n', '\n'.join(nines_rows) + '\n'
if __name__ == '__main__':
    out = dict(zip(['result.tsv', 'sign_table.tsv', 'nines.tsv'], run()))
    if '--check' in sys.argv:
        stale = [f for f, t in out.items() if not os.path.exists(os.path.join(H, f)) or open(os.path.join(H, f)).read() != t]
        print('stale: ' + ', '.join(stale) if stale else 'up to date'); sys.exit(1 if stale else 0)
    for f, t in out.items(): open(os.path.join(H, f), 'w').write(t)
    print(out['result.tsv'])
