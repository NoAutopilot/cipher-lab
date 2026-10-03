#!/usr/bin/env python3
"""test0.py -- es132-vargas-mexia-1578 first cheap test (LANE-POOLS FT-B, 3 Oct 2026).

Decodes ciphertext.tsv (and the blind passes) with key.tsv (Cp.30, Tomokiyo table + cabinet-noir 35=pr correction).
Known answer: lines L07-L13 vs Teulet's printed official decipherment (teulet_15oct1578.txt), per-token agreement after
normalising both sides to one convention (lower case, accents/cedilla stripped, v->u, j->i, double letters collapsed:
rule 3's notation paragraph). Target: L02-L06 (not printed by Teulet), Spanish word-cover (tools/data/es17 vocabulary).
Null for both: 200 keys with the letter values permuted among the numeric base symbols (changes the decoded letters,
so it can change both statistics: rule 3 orthogonality). Writes reading.txt / reading_known.txt; --check exits 1 if stale.
"""
import re, sys, gzip, random, difflib, unicodedata, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VOW = {'+': 'a', '.': 'e', 'σ': 'i', 'ρ': 'o', '⊣': 'u'}
TOK = re.compile(r'^(\{[^}]+\}|\d+|[A-Za-z]+)(_?)([+.σρ⊣]?)((?:@[lmnrsc2])*)(\??)$')

def load_key():
    k = {}
    for l in open(HERE / 'key.tsv', encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        s, v = l.rstrip('\n').split('\t')[:2]
        k[s] = v
    k['35_'] = 'pl'; k['31_'] = 'cl'; k['33_'] = 'fl'; k['34_'] = 'gl'
    return k

def load_lines(p):
    out = {}
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or l.startswith('line\t') or not l.strip(): continue
        a, b = l.rstrip('\n').split('\t', 1)
        out[a] = b.split()
    return out

def dec_tok(t, key):
    """returns (text or None for code/unreadable, kind)"""
    if t in ('/',): return ('', 'punct')
    m = TOK.match(t)
    if not m: return (None, 'bad')
    base, und, vow, above, q = m.groups()
    if base.startswith('{') or '@c' in above: return (None, 'code')
    v = key.get(base + und) or (key.get(base) if not und else None)
    if v is None: return (None, 'code')
    s = v
    if vow:
        s += ('u' if s == 'q' else '') + VOW[vow]
    for a in re.findall(r'@([lmnrs])', above): s += a
    return (s, 'key')

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('ç', 'c').replace('v', 'u').replace('j', 'i')
    s = re.sub(r'[^a-z]', '', s)
    return re.sub(r'(.)\1+', r'\1', s)

def known_agreement(toks, key, ref):
    segs = []
    for t in toks:
        txt, kind = dec_tok(t, key)
        if kind == 'key': segs.append(norm(txt))
    dec = ''.join(segs)
    sm = difflib.SequenceMatcher(None, dec, ref, autojunk=False)
    ok = [False] * len(dec)
    for b in sm.get_matching_blocks():
        for i in range(b.a, b.a + b.size): ok[i] = True
    pos, good = 0, 0
    for s in segs:
        if s and all(ok[pos:pos + len(s)]): good += 1
        pos += len(s)
    return good, len(segs)

_vocab = None
def vocab():
    global _vocab
    if _vocab is None:
        from collections import Counter
        c = Counter()
        for f in (ROOT / 'tools/data/es17').glob('*.txt.gz'):
            for w in re.findall(r'[A-Za-zÀ-ÿ]+', gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read()):
                c[norm(w)] += 1
        _vocab = {w for w, n in c.items() if (len(w) >= 2 and n >= 3) or w in ('a', 'y', 'o', 'e')}
    return _vocab

def cover(s, V, maxw=16):
    n = len(s); best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for j in range(max(0, i - maxw), i):
            if s[j:i] in V: best[i] = max(best[i], best[j] + i - j)
    return best[n]

def target_cover(toks, key):
    V = vocab(); segs = []; cur = ''
    for t in toks:
        txt, kind = dec_tok(t, key)
        if kind == 'key': cur += norm(txt)
        elif kind == 'code':
            if cur: segs.append(cur); cur = ''
    if cur: segs.append(cur)
    tot = sum(len(s) for s in segs)
    return sum(cover(s, V) for s in segs) / tot if tot else 0.0, tot

def shuffled(key, rng):
    nums = [s for s in key if s.isdigit()]
    vals = [key[s] for s in nums]; rng.shuffle(vals)
    k = dict(key); k.update(zip(nums, vals))
    for u in ('35_', '31_', '33_', '34_'): k.pop(u, None)
    return k

def reading(lines, key, which):
    out = []
    for ln in which:
        if ln not in lines: continue
        words = []
        for t in lines[ln]:
            txt, kind = dec_tok(t, key)
            words.append(txt if kind in ('key', 'punct') else '[' + t + ']')
        out.append(ln + '\t' + ' '.join(w for w in words if w))
    return '\n'.join(out) + '\n'

def main():
    key = load_key()
    ref = norm(''.join(l for l in open(HERE / 'teulet_15oct1578.txt', encoding='utf-8') if not l.startswith('#')))
    KN = ['L%02d' % i for i in range(7, 14)]; TG = ['L%02d' % i for i in range(2, 7)]
    res = {}
    rng = random.Random(1578)
    shuf = [shuffled(key, rng) for _ in range(200)]
    for name, p in [('reconciled', HERE / 'ciphertext.tsv'), ('passA', HERE / 'passes/passA.tsv'), ('passB', HERE / 'passes/passB.tsv')]:
        L = load_lines(p)
        kt = [t for ln in KN if ln in L for t in L[ln]]
        g, n = known_agreement(kt, key, ref)
        null = sorted(known_agreement(kt, k, ref)[0] / max(1, known_agreement(kt, k, ref)[1]) for k in shuf)
        tt = [t for ln in TG if ln in L for t in L[ln]]
        cv, nl = target_cover(tt, key)
        cnull = sorted(target_cover(tt, k)[0] for k in shuf)
        res[name] = dict(known_good=g, known_n=n, known_agree=round(g / n, 3), known_null_mean=round(sum(null) / 200, 3),
                         known_null_p95=round(null[189], 3), known_null_max=round(null[-1], 3),
                         target_letters=nl, target_cover=round(cv, 3), target_null_mean=round(sum(cnull) / 200, 3),
                         target_null_p95=round(cnull[189], 3), target_null_max=round(cnull[-1], 3),
                         target_rank=1 + sum(1 for x in cnull if x >= cv))
    Lr = load_lines(HERE / 'ciphertext.tsv')
    out = {'reading_target.txt': reading(Lr, key, TG), 'reading_known.txt': reading(Lr, key, KN),
           'test0_result.json': json.dumps(res, indent=1) + '\n'}
    if '--check' in sys.argv:
        stale = [f for f, s in out.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != s]
        print('stale:' if stale else 'OK: committed outputs match', *stale); sys.exit(1 if stale else 0)
    for f, s in out.items(): (HERE / f).write_text(s, encoding='utf-8')
    print(out['test0_result.json']); print(out['reading_known.txt']); print(out['reading_target.txt'])

if __name__ == '__main__':
    main()
