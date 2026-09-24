#!/usr/bin/env python3
"""R18 (24 Sept 2026): align the sibling cipher letters 4613 p1 and 4615 p1 (eye-read against the image,
r18/cipher_<briefnr>.txt) to their contemporary decipherments (plaintext_<briefnr>.txt, body given in
r18/segments.tsv), and derive key.tsv from the pairs.

The cipher is a regular homophonic table, five numbers per letter in alphabetical blocks starting at n:
n 1-5, o 6-10, p 11-15, q 16-20, r 21-25, s 26-30, t 31-35, u 36-40, v 41-45, x 46-50, y 51-55, z 56-60,
a 61-65, b 66-70, c 71-75, d 76-80, e 81-85, f 86-90, g 91-95, h 96-100, i 101-105, k 106-110, l 111-115,
m 116-120; numbers above 120 and roman ii/iii are words, names or nulls. The block rule was found from the
alignment itself (seg 'ne perdions pas le temps ... court' of 4613 reads 37 tokens for 37 letters) and is
tested here: every aligned numeral is compared with its block letter.

Writes ciphertext_sib.tsv, pairs_sib.tsv, key.tsv, key_conflicts.tsv. --check exits 1 if any differs."""
import sys, re, csv, io, os, collections
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BLOCKS = 'nopqrstuvxyzabcdefghiklm'
def block(n):
    n = int(n); return BLOCKS[(n-1)//5] if 1 <= n <= 120 else None
def norm(s):
    s = re.sub(r'\[struck:[^\]]*\]', '', s).lower().replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z0-9]', '', s)
def nb(c): return {'v': 'u', 'j': 'i'}.get(c, c)
def numeral(t): return re.fullmatch(r'\d{1,3}', t) is not None and int(t) <= 120

out = {}
WORDS = {r['code']: r for r in csv.DictReader(open('r18/words.tsv'), delimiter='\t')}
cipher = {}
for B in ('4613', '4615'):
    rows = []
    for l in open(f'r18/cipher_{B}.txt'):
        p = l.split()
        for i, t in enumerate(p[1:], 1):
            rows.append((f'{B}_{p[0]}', i, t.rstrip('?') if not t.startswith('=') else 'w:' + t[1:],
                         'M' if t.endswith('?') else ''))
    cipher[B] = rows
f = io.StringIO(); f.write('line\tidx\ttoken\tconf\tbriefnr\n')
for B in cipher:
    for ln, i, t, c in cipher[B]: f.write(f'{ln}\t{i}\t{t}\t{c}\t{B}\n')
out['ciphertext_sib.tsv'] = f.getvalue()

MATCH, MIS, NULL, SKIP = 0.0, -3.0, -2.5, -2.5
def align(toks, pt):
    n, m = len(toks), len(pt); NEG = -1e9
    S = [[NEG]*(m+1) for _ in range(n+1)]; BK = {}
    S[0][0] = 0.0
    for i in range(n+1):
        for j in range(m+1):
            v = S[i][j]
            if v == NEG: continue
            if j < m and v+SKIP > S[i][j+1]: S[i][j+1] = v+SKIP; BK[i, j+1] = (i, j)
            if i == n: continue
            t = toks[i][2]; opts = []
            if t.startswith('w:'):
                w = norm(t[2:]); opts.append((0, -1.0))
                if w and pt[j:j+len(w)] == w: opts.append((len(w), 0.0))
            elif numeral(t):
                opts.append((0, NULL))
                if j < m: opts.append((1, MATCH if nb(block(t)) == pt[j] else MIS))
            elif t in WORDS:   # keyed word, name or null sign
                w = WORDS[t]['value']; w = '' if w == 'NULL' else norm(w) if w != '?' else None
                if w is not None and pt[j:j+len(w)] == w: opts.append((len(w), 0.0))
                opts += [(L, -3.0 - 0.05*L) for L in range(0, 25)]
            else:   # blot, spot
                opts += [(L, -1.0 - 0.05*L) for L in range(0, 25)]
            for L, sc in opts:
                if j+L <= m and v+sc > S[i+1][j+L]: S[i+1][j+L] = v+sc; BK[i+1, j+L] = (i, j)
    path, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj = BK[i, j]
        path.append((toks[pi] if pi < i else None, pt[pj:j]))
        i, j = pi, pj
    return path[::-1]

pairs = io.StringIO(); pairs.write('briefnr\tline\tidx\ttoken\tplain\tblock\tstatus\n')
obs = collections.defaultdict(collections.Counter); where = collections.defaultdict(list)
for r in csv.DictReader(open('r18/segments.tsv'), delimiter='\t'):
    B = r['briefnr']; plain = open(r['plaintext']).read()
    a = norm(plain).find(norm(r['start'])); b = norm(plain).find(norm(r['end']), a)
    pt = norm(plain)[a:b+len(norm(r['end']))]
    for tk, s in align(cipher[B], pt):
        if tk is None:
            pairs.write(f'{B}\t\t\t\t{s}\t\tplain-only\n'); continue
        ln, i, t, c = tk
        if t.startswith('w:'):
            pairs.write(f'{B}\t{ln}\t{i}\t{t}\t{s}\t\t{"clear" if s else "clear-unmatched"}\n'); continue
        bl = block(t) if numeral(t) else ''
        st = ('null' if not s else 'match' if bl and nb(bl) == s else 'conflict' if bl else 'word')
        pairs.write(f'{B}\t{ln}\t{i}\t{t}\t{s}\t{bl or ""}\t{st}\n')
        if not t.startswith('['): obs[t][s or 'NULL'] += 1; where[t, s or 'NULL'].append(f'{ln}.{i}')
out['pairs_sib.tsv'] = pairs.getvalue()

key = io.StringIO(); key.write('code\tvalue\tgrade\tsource\tnote\n')
conf = io.StringIO(); conf.write('code\tblock_value\tobserved\tcount\twhere\tnote\n')
for n in range(1, 121):
    t, bl = str(n), block(n); o = obs.get(t, {})
    good = o.get(bl, 0) + (o.get('u', 0) if bl == 'v' else 0)
    if good:
        key.write(f'{t}\t{bl}\tC\taligned 4613/4615\tmatches plaintext {good}x of {sum(o.values())}\n')
    elif o:
        key.write(f'{t}\t{bl}\tI\ttable rule\tobserved only off-block: {dict(o)}\n')
    else:
        key.write(f'{t}\t{bl}\tI\ttable rule\tnot observed in 4613/4615\n')
    for v, c in sorted(o.items()):
        if v != bl and not (bl == 'v' and v == 'u'):
            conf.write(f'{t}\t{bl}\t{v}\t{c}\t{" ".join(where[t, v])}\t\n')
for t, r in WORDS.items():
    o = obs.get(t, {}); w = 'NULL' if r['value'] == 'NULL' else norm(r['value']) if r['value'] != '?' else '?'
    key.write(f"{t}\t{r['value']}\t{r['grade']}\taligned 4613/4615 (r18/words.tsv)\t{r['evidence']}\n")
    for v2, c2 in o.items():
        if v2 != w: conf.write(f'{t}\t\t{v2}\t{c2}\t{" ".join(where[t, v2])}\tword/null sign, key value {r["value"]}\n')
out['key.tsv'] = key.getvalue(); out['key_conflicts.tsv'] = conf.getvalue()

stale = [k for k, v in out.items() if not os.path.exists(k) or open(k).read() != v]
if '--check' in sys.argv:
    print('stale:', stale or 'none'); sys.exit(1 if stale else 0)
for k, v in out.items(): open(k, 'w').write(v)
print('wrote', ', '.join(out))
