#!/usr/bin/env python3
"""N8-BAL known-answer score (PREREG-N8BAL.md, pushed before any score): Baluze 168 f.246-247 bare passage decoded with key.tsv
against Tomokiyo's two quoted fragments (louisxiii.htm). Tomokiyo's quote is the test only; it is never used to read or label signs.
  python3 score_f247.py TRANSCRIPTION.tsv [more.tsv ...]   (tsv: 'line<TAB>tokens', tokens as in ciphertext.txt; {clear words} or w:word)
Each file is scored separately. Normalization (both sides): lowercase, accents stripped, j->i, v->u, letters only.
Passage string: tokens in reading order; a cipher token contributes its key value (unknown/unread -> '#', never matches);
clear words contribute their letters, flagged 'clear'. Each fragment is fitted (whole fragment, free passage ends; match +2,
mismatch -1, gap -2) into the passage string. Columns where the passage side is a clear-word letter are excluded. Agreement =
fragment letters equal to a cipher-derived letter / fragment letters in non-clear columns. A fragment with < 10 fragment letters
in cipher-derived columns counts as not overlapping (0 of its letters enter the pooled figure; reported). Pooled = sum/sum.
Null: key values shuffled within sign class (acute ' / diaeresis : / overbar = / plain / letter L:), 2000 draws, seed 1, same
procedure per draw. Gate (fixed before scoring): PASS iff pooled >= 0.60 and pooled > null p99.
"""
import csv, os, random, re, sys, unicodedata
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAGS = ["c'est ce qu'on pouvoit desirer dudit Salvius pour ce regard",
         "de ne consentir aucune suspension d'armes quand on viendra a traiter si ce n'est que le"]
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', s.replace('j', 'i').replace('v', 'u'))
def load_key():
    k = {}
    for r in csv.reader((l for l in open(f'{D}/key.tsv') if not l.startswith('#')), delimiter='\t'):
        if r and r[0] != 'code': k[r[0]] = r[1]
    return k
def tokens(path):
    out = []
    for r in csv.reader(open(path), delimiter='\t'):
        if not r or r[0] == 'line' or r[0].startswith('#'): continue
        s = r[1]
        for m in re.finditer(r'\{([^}]*)\}|(\S+)', s):
            if m.group(1) is not None: out.append(('clear', m.group(1)))
            else:
                t = m.group(2)
                if t.startswith('w:'): out.append(('clear', t[2:]))
                else: out.append(('cipher', re.sub(r'\?.*$', '', t.split('|')[0]) if not t.startswith('L:?') else '?'))
    return out
def passage(toks, key):
    s, flag = [], []
    for kind, t in toks:
        if kind == 'clear':
            for c in norm(t): s.append(c); flag.append(1)
        else:
            v = key.get(t)
            v = norm(v) if v and not v.startswith('(') else ''
            if not v: v = '#'
            for c in v: s.append(c); flag.append(0)
    return s, flag
def fit(frag, s, flag):
    n, m = len(frag), len(s)
    NEG = -10**9
    H = [[0] * (m + 1)] + [[NEG] * (m + 1) for _ in range(n)]
    P = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        H[i][0] = H[i-1][0] - 2; P[i][0] = 1
        for j in range(1, m + 1):
            d = H[i-1][j-1] + (2 if frag[i-1] == s[j-1] else -1)
            u = H[i-1][j] - 2; l = H[i][j-1] - 2
            b = max(d, u, l); H[i][j] = b; P[i][j] = 0 if b == d else 1 if b == u else 2
    j = max(range(m + 1), key=lambda x: H[n][x]); i = n
    ok = den = 0; prev_clear = None
    while i > 0:
        p = P[i][j]
        if p == 0:
            if not flag[j-1]:
                den += 1; ok += frag[i-1] == s[j-1]
            i -= 1; j -= 1
        elif p == 1:
            # fragment letter opposite a gap: excluded only if flanked by clear letters
            if not (j > 0 and flag[j-1] and j < m and flag[j]): den += 1
            i -= 1
        else: j -= 1
    return ok, den
def score(toks, key):
    s, flag = passage(toks, key)
    res = []
    for f in FRAGS:
        ok, den = fit(norm(f), s, flag)
        res.append((ok, den) if den >= 10 else (0, 0))
    return res
def cls(c): return 'L' if c.startswith('L:') else c[-1] if c[-1] in "':=" else 'plain'
def main():
    key = load_key()
    groups = {}
    for c in key: groups.setdefault(cls(c), []).append(c)
    for path in sys.argv[1:]:
        toks = tokens(path)
        res = score(toks, key); ok = sum(a for a, b in res); den = sum(b for a, b in res)
        real = ok / den if den else 0.0
        rng = random.Random(1); nulls = []
        for _ in range(2000):
            k2 = {}
            for g, cs in groups.items():
                vs = [key[c] for c in cs]; rng.shuffle(vs); k2.update(zip(cs, vs))
            r2 = score(toks, k2); d2 = sum(b for a, b in r2)
            nulls.append(sum(a for a, b in r2) / d2 if d2 else 0.0)
        nulls.sort(); p99 = nulls[int(0.99 * len(nulls))]
        per = '; '.join(f'F{i+1} {a}/{b}' + (' (not overlapping)' if b == 0 else '') for i, (a, b) in enumerate(res))
        verdict = 'PASS' if real >= 0.60 and real > p99 else 'FAIL'
        print(f'{os.path.basename(path)}: pooled {ok}/{den} = {real:.3f} [{per}]; shuffled-key null mean '
              f'{sum(nulls)/len(nulls):.3f}, p99 {p99:.3f} -> {verdict}')
if __name__ == '__main__': main()
