#!/usr/bin/env python3
"""BNF-Q7-TEST step 1 control: can the structural parse-share check (structural.py) see a true no.62 encipherment
at f.25's length and error band? Synthetic: it16dip held-out file letterediprincip03char, windows enciphered with
key_no62.tsv as transcribed (word codes where the window has the word, letters by the alphabet row, polyphonic
cells shared, letters with NO figure (h, s, u/v, z, x, j, k, y) DROPPED -- the only encipherment the transcribed key
permits), nulls 227/294/295 at 3% of tokens, continuous string cut to 260 digits, digit substitution errors at
0/5/10/15%. Power = share of 100 texts whose parse share exceeds the p95 of 200 digit-order shuffles of itself.
Negative control: random strings with f.25's digit frequencies. Seed 62."""
import gzip, random, os, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from structural import load_codes, load_ct, T
CORP = os.path.join(T, '..', '..', 'tools', 'data', 'it16dip', 'letterediprincip03char.txt.gz')
LETTERS = {'a':'1','b':'34','c':'34','d':'32','e':'9','f':'35','g':'35','i':'4','l':'36','m':'8','n':'37','o':'5',
           'p':'38','q':'6','r':'31','t':'7'}
def words_map():
    import csv; m = {}
    for r in csv.reader(open(os.path.join(T,'key_no62.tsv')), delimiter='\t'):
        if not r or r[0].startswith('#') or r[0]=='value' or len(r[0])!=3 or r[1]=='NULL': continue
        for alt in r[1].replace(',', ' o ').split(' o '):
            w = ''.join(ch for ch in unicodedata.normalize('NFD', alt.strip().lower()) if ch.isalpha())
            if w and ' ' not in alt.strip(): m.setdefault(w, r[0])
    return m
def fast_share(s, c1, c2, c3):
    n = len(s); best = [0]*(n+1)
    for i in range(n-1, -1, -1):
        b = best[i+1]
        if s[i] in c1: b = max(b, 1+best[i+1])
        if i+2 <= n and s[i:i+2] in c2: b = max(b, 2+best[i+2])
        if i+3 <= n and s[i:i+3] in c3: b = max(b, 3+best[i+3])
        best[i] = b
    return best[0]/n
def encipher(words, wm, rng, null_share=0.03):
    out = []
    for w in words:
        if w in wm: toks = [wm[w]]
        else:
            toks = []
            for ch in w:
                if ch == 'u' and toks and toks[-1] == '6': continue  # qu = 6
                if ch in LETTERS: toks.append(LETTERS[ch])
        for t in toks:
            if rng.random() < null_share: out.append(rng.choice(['227','294','295']))
            out.append(t)
    return ''.join(out)
def windows(rng, n_texts, ndig, wm):
    chunks = [l.split() for l in gzip.open(CORP, 'rt')]
    chunks = [c for c in chunks if len(c) > 400]
    res = []
    while len(res) < n_texts:
        c = rng.choice(chunks); st = rng.randrange(0, len(c)-300)
        s = encipher(c[st:st+300], wm, rng)
        if len(s) >= ndig: res.append(s[:ndig])
    return res
def corrupt(s, rate, rng):
    return ''.join(rng.choice([d for d in '0123456789' if d != x]) if rng.random() < rate else x for x in s)
def power(texts, c1, c2, c3, rng, nshuf=200):
    hits = 0; vals = []
    for s in texts:
        obs = fast_share(s, c1, c2, c3); null = []
        for _ in range(nshuf):
            l = list(s); rng.shuffle(l); null.append(fast_share(''.join(l), c1, c2, c3))
        null.sort(); vals.append(obs); hits += obs > null[int(0.95*nshuf)-1]
    return hits/len(texts), sum(vals)/len(vals)
if __name__ == '__main__':
    codes = load_codes(); c1 = {c for c in codes if len(c)==1}; c2 = {c for c in codes if len(c)==2}; c3 = {c for c in codes if len(c)==3}
    rng = random.Random(62); wm = words_map(); ct = load_ct().replace('?','')
    base = windows(rng, 100, len(ct), wm)
    for rate in (0.0, 0.05, 0.10, 0.15):
        tx = [corrupt(s, rate, rng) for s in base]
        pw, mean = power(tx, c1, c2, c3, rng)
        print(f'error {rate:.2f}: power(>own shuffle p95)={pw:.2f} mean parse share={mean:.3f}')
    neg = [''.join(rng.sample(ct, len(ct))) for _ in range(100)]
    pw, mean = power(neg, c1, c2, c3, rng)
    print(f'negative (f.25 digit freqs, random order): rate>p95={pw:.2f} mean parse share={mean:.3f}')
    print('word codes used:', len(wm))
