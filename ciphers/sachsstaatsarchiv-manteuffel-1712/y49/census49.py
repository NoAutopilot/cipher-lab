#!/usr/bin/env python3
"""MANT-Y49 census (10 Oct 2026): every committed token carrying a 4 or 9 digit on the glossed/printed leaves of
694/08-09 that have token-level TSVs and committed native line strips, and the known-answer subset where a gloss or
print span fixes the digit (the 4-variant and 9-variant codes give different key values and exactly one matches the
aligned gloss letter). Script only, no image read. Writes y49/census.tsv and y49/known.tsv.
--check: exit 1 if the committed outputs are stale."""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
def rows(p):
    with open(os.path.join(ROOT, p)) as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))
KEY = {}
for r in rows('key.tsv'):
    v = (r['value'] or '').strip()
    KEY[r['code']] = v
def vals(code):
    """letter values of a code: split alternatives, keep short lowercase letter strings; names as 'NAME:x'."""
    v = KEY.get(code)
    if v is None: return None
    out = set()
    for a in re.split(r'[|/]', v):
        a = a.strip()
        if re.fullmatch(r'[a-z]{1,3}', a): out.add(a)
        elif a: out.add('NAME:' + a.lower())
    return out
def variants(code):
    pos = [i for i, c in enumerate(code) if c in '49']
    if len(pos) != 1: return None
    i = pos[0]
    return code[:i] + '4' + code[i+1:], code[:i] + '9' + code[i+1:]
# ---- leaves -> token lists [tokid, crop, settled, passA, passB]
LEAVES = []
def addA(leaf, vol, ct, croppat):
    toks = []
    for r in rows(ct):
        crop = r['crop']; crop = croppat.format(crop=crop, run=r.get('run', ''))
        toks.append(dict(tokid=r['tokid'], crop=crop, settled=r.get('settled') or r.get('token'),
                         passA=r.get('passA', ''), passB=r.get('passB', '')))
    LEAVES.append((leaf, vol, ct, toks))
addA('0494', '694/08', 'f0494_08/ciphertext.tsv', '{crop}')
addA('0474', '694/08', 'f0474_08/ciphertext.tsv', '{crop}')
addA('0089', '694/08', 'f0089_08/ciphertext.tsv', '{crop}')
addA('0136', '694/08', 'f0136_08/ciphertext.tsv', 'c0136{crop}_L01')
for lf in ('0309', '0312', '0314', '0317'):
    toks = [dict(tokid=r['tokid'], crop='c%s%s_L01' % (lf, r['run']), settled=r['settled'], passA=r['passA'],
                 passB=r['passB'], run=r['run']) for r in rows('f%s_08/ciphertext.tsv' % lf)]
    LEAVES.append((lf, '694/08', 'f%s_08/ciphertext.tsv' % lf, toks))
# 0490 right page: settled in 'token'; passes in passA/passB.tsv not joined (crop-level), left blank
LEAVES.append(('0490', '694/08', 'f0490_08/ciphertext.tsv',
               [dict(tokid=r['tokid'], crop=r['crop'] + '_L01', settled=r['token'], passA='', passB='') for r in rows('f0490_08/ciphertext.tsv')]))
LEAVES.append(('0490L', '694/08', 'f0490_08/ciphertext_L.tsv',
               [dict(tokid=r['tokid'], crop=r['crop'] + '_L01', settled=r['token'], passA='', passB='') for r in rows('f0490_08/ciphertext_L.tsv')]))
# ---- spans [leaf, span_id, tier, gloss, token-index list]
SPANS = []
def find(toks, codes, crops=None):
    seq = [t['settled'] for t in toks]
    n = len(codes)
    for i in range(len(seq) - n + 1):
        if seq[i:i+n] == codes and (crops is None or toks[i]['crop'] in crops):
            return list(range(i, i+n))
    return None
idx = {lf: {t['tokid']: i for i, t in enumerate(toks)} for lf, _, _, toks in LEAVES}
tl = {lf: toks for lf, _, _, toks in LEAVES}
for lf, p in (('0494', 'f0494_08/gloss.tsv'), ('0474', 'f0474_08/gloss.tsv'), ('0089', 'f0089_08/gloss_spans.tsv'),
              ('0136', 'f0136_08/gloss_spans.tsv')):
    for r in rows(p):
        ii = [idx[lf][t] for t in r['tokids'].split() if t in idx[lf]]
        if ii: SPANS.append((lf, r['span_id'], 'G', r['gloss'], ii))
for lf in ('0309', '0312', '0314', '0317'):
    for g in ('G1', 'G2'):
        for r in rows('f%s_08/spans_%s.tsv' % (lf, g)):
            ii = find(tl[lf], r['codes'].split(), {'c%s%s_L01' % (lf, r['run'])})
            if ii: SPANS.append((lf, r['span_id'], 'G' + g[-1], r['gloss'], ii))
for p, lf in (('f0490_08/gloss_spans.tsv', '0490'), ('f0490_08/gloss_spans_L.tsv', '0490L')):
    for r in rows(p):
        ii = find(tl[lf], r['codes'].split())
        if ii: SPANS.append((lf, r['span_id'], 'G', r['gloss'], ii))
# ---- alignment: DP of span tokens vs gloss letters
def norm(g):
    g = g.lower()
    for a, b in (('à', 'a'), ('é', 'e'), ('è', 'e'), ('ê', 'e'), ('ç', 'c'), ('ô', 'o'), ('û', 'u'), ('î', 'i'), ('ï', 'i')):
        g = g.replace(a, b)
    return re.sub(r'[^a-z]', '', g)
def align(codes, gloss):
    G = norm(gloss); n, m = len(codes), len(G)
    opts = []
    for c in codes:
        vv = variants(c)
        o = []
        cand = [(c, None)] if vv is None else [(vv[0], '4'), (vv[1], '9')]
        for cc, lab in cand:
            for v in (vals(cc) or ()):
                if not v.startswith('NAME:'): o.append((v, lab))
        opts.append(o)
    NEG = -10**9
    S = [[NEG] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    S[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if S[i][j] == NEG: continue
            s = S[i][j]
            if i < n:
                for v, lab in opts[i]:
                    if G[j:j+len(v)] == v and s + 2 > S[i+1][j+len(v)]:
                        S[i+1][j+len(v)] = s + 2; B[i+1][j+len(v)] = (i, j, 'M', v, lab)
                if j < m and s - 1 > S[i+1][j+1]: S[i+1][j+1] = s - 1; B[i+1][j+1] = (i, j, 'X', G[j], None)
                if s - 1 > S[i+1][j]: S[i+1][j] = s - 1; B[i+1][j] = (i, j, 'D', '', None)
            if j < m and s - 1 > S[i][j+1]: S[i][j+1] = s - 1; B[i][j+1] = (i, j, 'I', G[j], None)
    i, j = n, m; path = [None] * n
    while (i, j) != (0, 0):
        pi, pj, op, v, lab = B[i][j]
        if op in 'MXD': path[pi] = (op, v, lab)
        i, j = pi, pj
    return path
census, known = [], []
for lf, vol, ct, toks in LEAVES:
    for k, t in enumerate(toks):
        c = t['settled'] or ''
        if re.fullmatch(r'\d+', c) and any(d in '49' for d in c):
            vv = variants(c)
            census.append([lf, vol, ct, t['tokid'], t['crop'], c, t['passA'], t['passB'],
                           vv[0] if vv else '', ','.join(sorted(vals(vv[0]) or [])) if vv else '',
                           vv[1] if vv else '', ','.join(sorted(vals(vv[1]) or [])) if vv else '',
                           'single' if vv else 'multi'])
seen = {}
for lf, sid, tier, gloss, ii in SPANS:
    toks = tl[lf]; codes = [toks[i]['settled'] for i in ii]
    vol = [v for l, v, _, _ in LEAVES if l == lf][0]
    if len(ii) == 1 and variants(codes[0]):            # single-code name span (e.g. 9/39 Ilgen)
        v4, v9 = variants(codes[0]); g = norm(gloss)
        n4 = [x[5:] for x in (vals(v4) or ()) if x.startswith('NAME:')]; n9 = [x[5:] for x in (vals(v9) or ()) if x.startswith('NAME:')]
        h4 = any(len(g) >= 3 and nm.startswith(g[:3]) for nm in n4); h9 = any(len(g) >= 3 and nm.startswith(g[:3]) for nm in n9)
        if h4 != h9:
            seen.setdefault((lf, toks[ii[0]]['tokid']), []).append((tier, sid, gloss, '4' if h4 else '9', 'name'))
        continue
    path = align(codes, gloss)
    plain = [p for i, p in zip(ii, path) if not variants(toks[i]['settled'])]
    if not plain: continue
    agree = sum(1 for p in plain if p and p[0] == 'M') / len(plain)
    if agree < 0.6: continue                             # span not anchored
    for pos, (i, p) in enumerate(zip(ii, path)):
        c = toks[i]['settled']; vv = variants(c)
        if not vv or not p or p[0] != 'M' or p[2] is None: continue
        other = vv[1] if p[2] == '4' else vv[0]
        if p[1] in (vals(other) or ()): continue          # both variants fit: not a known answer
        nb = [path[q] for q in (pos - 1, pos + 1) if 0 <= q < len(path) and not variants(toks[ii[q]]['settled'])]
        if not any(x and x[0] == 'M' for x in nb): continue   # need a matched keyed neighbour
        seen.setdefault((lf, toks[i]['tokid']), []).append((tier, sid, gloss, p[2], 'letter=%s span_agree=%.2f' % (p[1], agree)))
crow = {(r[0], r[3]): r for r in census}
for (lf, tid), ws in sorted(seen.items()):
    labs = {w[3] for w in ws}
    if len(labs) != 1: continue                          # witnesses conflict: dropped
    r = crow[(lf, tid)]
    known.append([lf, r[1], tid, r[4], r[5], labs.pop(), ';'.join('%s:%s' % (w[0], w[1]) for w in ws),
                  ' | '.join('%s %s' % (w[2][:40], w[4]) for w in ws)])
H1 = ['leaf', 'vol', 'file', 'tokid', 'crop', 'settled', 'passA', 'passB', 'as4', 'val4', 'as9', 'val9', 'kind']
H2 = ['leaf', 'vol', 'tokid', 'crop', 'settled', 'known', 'witness', 'evidence']
def tsv(h, rs): return '\t'.join(h) + '\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rs)
out = {'census.tsv': tsv(H1, census), 'known.tsv': tsv(H2, known)}
if __name__ == '__main__':
    stale = False
    for fn, txt in out.items():
        p = os.path.join(HERE, fn)
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p).read() != txt: print('STALE', fn); stale = True
        else: open(p, 'w').write(txt)
    print('census tokens', len(census), 'single', sum(r[12] == 'single' for r in census), 'known', len(known),
          'known4', sum(k[5] == '4' for k in known), 'known9', sum(k[5] == '9' for k in known))
    sys.exit(1 if stale else 0)
