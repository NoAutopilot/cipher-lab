#!/usr/bin/env python3
"""D2-HELR words-level frequency-fit test of R4386 on the 1763 1201-2000 band (PREREG-D2HELR.md).

  --control   R4369-on-R1953 power check (200 subsamples at ~121 tokens) and the wrong-key (permuted values) check
  --score     read words_read.tsv (order, code, word) and print S, value-shuffle null, verdict
"""
import argparse, collections, csv, glob, gzip, math, os, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); UP = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(UP))
LO, HI = 1201, 2000
LETTERS = ['R1045', 'R1046', 'R1047', 'R1048', 'R1060', 'R1061']

def corpus():
    c = collections.Counter()
    for f in glob.glob(os.path.join(ROOT, 'tools', 'data', 'fr18', '*.txt*')):
        op = gzip.open if f.endswith('.gz') else open
        with op(f, 'rt', errors='ignore') as fh:
            c.update(re.findall(r"[a-zàâäçéèêëîïôöùûüœ]+", fh.read().lower()))
    return c

FREQ = None
def f(w):
    global FREQ
    if FREQ is None:
        FREQ = corpus(); FREQ['_tot'] = sum(FREQ.values())
    tot = FREQ['_tot']
    w = (w or '').strip().lower().rstrip('?')
    if w in ('', 'blank', 'crossed', 'zero', '?', 'x', 'b'): return math.log10(1 / tot)
    m = re.findall(r"[a-zàâäçéèêëîïôöùûüœ]+", w.split()[0] if w.split() else '')
    return math.log10((FREQ.get(m[0], 0) + 1) / tot) if m else math.log10(1 / tot)

def S_of(mult, words):  # mult: list of token counts per target cell; words: list of scores, first len(mult) are targets
    return sum(m * words[i] for i, m in enumerate(mult)) / sum(mult)

def perm_null(mult, scores, n, rng):
    out = []
    for _ in range(n):
        s = scores[:]; rng.shuffle(s); out.append(S_of(mult, s))
    return sorted(out)

def pct(xs, p): return xs[min(len(xs) - 1, int(p * len(xs)))]

def control(wrong=False):
    rng = random.Random(4369)
    toks = [r for r in csv.DictReader(open(os.path.join(UP, 'key_r4369', 'reading_R1953_tokens.tsv')), delimiter='\t')
            if r['sign'].isdigit() and r['grade'] in ('H', 'S')]
    val = {}; mult = collections.Counter()
    for r in toks: val[int(r['sign'])] = r['value']; mult[int(r['sign'])] += 1
    key = {int(r['code']): r['left'] for r in csv.DictReader(open(os.path.join(UP, 'key_r4369', 'key.tsv')), delimiter='\t')
           if r['code'].isdigit() and r['left']}
    codes = sorted(mult)
    if wrong:  # a wrong key of the same design: permute R4369's values over codes
        allc = sorted(set(codes) | set(key)); vs = [val.get(c, key.get(c)) for c in allc]; rng.shuffle(vs)
        perm = dict(zip(allc, vs)); val = {c: perm[c] for c in codes}; key = {c: perm[c] for c in key}
    hits = 0; ss = []
    for _ in range(200):
        cs = codes[:]; rng.shuffle(cs); pick = []; n = 0
        for c in cs:
            if n >= 121: break
            pick.append(c); n += mult[c]
        others = rng.sample([c for c in key if c not in pick and c not in mult], 100)
        scores = [f(val[c]) for c in pick] + [f(key[c]) for c in others]
        m = [mult[c] for c in pick]; S = S_of(m, scores); nl = perm_null(m, scores, 1000, rng)
        hits += S > pct(nl, .99); ss.append(S - pct(nl, .5))
    print(f"control{' (WRONG KEY)' if wrong else ''}: share S > null p99 = {hits / 200:.3f} over 200 subsamples "
          f"(gate {'<= 0.05' if wrong else '>= 0.80'}); median S - null median = {sorted(ss)[100]:.3f}")
    return hits / 200

def score():
    c = collections.Counter()
    for r in LETTERS:
        for t in open(os.path.join(UP, f'ciphertext_{r}.txt')).read().split():
            if re.fullmatch(r'\d+', t) and LO <= int(t) <= HI: c[int(t)] += 1
    rows = {int(r['code']): r['word'] for r in csv.DictReader(open(os.path.join(HERE, 'words_read.tsv')), delimiter='\t')}
    tg = sorted(c); others = [k for k in rows if k not in c]
    scores = [f(rows[k]) for k in tg] + [f(rows[k]) for k in others]
    m = [c[k] for k in tg]; S = S_of(m, scores)
    nl = perm_null(m, scores, 10000, random.Random(1752))
    p = sum(x >= S for x in nl) / len(nl)
    print(f"target: {sum(m)} tokens / {len(tg)} codes, {len(others)} null cells; S = {S:.3f}; null median {pct(nl, .5):.3f} "
          f"p95 {pct(nl, .95):.3f} p99 {pct(nl, .99):.3f}; P(null >= S) = {p:.4f}")
    floor = f('')
    print(f"floor-scored target tokens: {sum(c[k] for k in tg if f(rows[k]) == floor)}/{sum(m)}")
    print('top target codes:', ', '.join(f"{k}x{c[k]}={rows[k]}" for k in sorted(tg, key=lambda k: -c[k])[:15]))
    return S, nl, p

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--control', action='store_true'); ap.add_argument('--score', action='store_true')
    a = ap.parse_args()
    if a.control: control(); control(wrong=True)
    if a.score: score()
