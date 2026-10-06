#!/usr/bin/env python3
"""R9-HUNT context-fill of unkeyed groups (method pre-registered in fill/PREREG-R9.md).

Usage: python3 fill/context_fill.py [--check]   (run from the target folder)
Writes fill/control.tsv, fill/summary.json, fill/target_fill.tsv; --check exits 1 if they differ from the committed copies.
"""
import csv, gzip, json, math, random, re, sys, unicodedata, os
from collections import Counter, defaultdict
from statistics import median

HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE)
CORPUS = os.path.join(TGT, '..', '..', 'tools', 'data', 'fr18')
N = 6; CTX = 15; SEEDS = (1, 2, 3); BLANK = 0.11

def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r"[^a-z]", '', s)

def load_key():
    k = {}
    for r in csv.DictReader(open(os.path.join(TGT, 'key.tsv')), delimiter='\t'):
        k[int(r['code'])] = r['value'].split('|')[0]
    return k

class LM:
    def __init__(self, text):
        self.c = [Counter() for _ in range(N + 1)]
        for n in range(1, N + 1):
            cn = self.c[n]
            for i in range(len(text) - n + 1):
                cn[text[i:i + n]] += 1
        self.ctx = [Counter() for _ in range(N + 1)]
        for n in range(1, N + 1):
            for g, v in self.c[n].items():
                self.ctx[n][g[:-1]] += v
        self.V = 26
    def p(self, h, ch):
        pr = 1.0 / self.V
        for n in range(1, N + 1):
            hh = h[len(h) - (n - 1):] if n > 1 else ''
            if n > 1 and len(h) < n - 1: break
            den = self.ctx[n][hh]
            if den == 0: break
            lam = den / (den + 0.1 * self.V * 5)
            pr = lam * (self.c[n][hh + ch] + 0.1) / (den + 0.1 * self.V) + (1 - lam) * pr
        return pr
    def logp(self, left, s):
        h = left; t = 0.0
        for ch in s:
            t += math.log(self.p(h, ch)); h = (h + ch)[-(N - 1):] if N > 1 else ''
        return t

def corpus():
    txt = []; words = Counter()
    for f in sorted(os.listdir(CORPUS)):
        if f.endswith('.gz'):
            raw = gzip.open(os.path.join(CORPUS, f), 'rt', errors='ignore').read()
            for w in re.findall(r"[A-Za-zÀ-ÿ]+", raw):
                n = norm(w)
                if n: words[n] += 1
            txt.append(norm(raw))
    return ''.join(txt), words

def bracket(code, key, vocab):
    codes = sorted(c for c in key if c != code)
    lo = [c for c in codes if c < code][-3:]; hi = [c for c in codes if c > code][:3]
    lv = sorted(norm(key[c]) for c in lo); hv = sorted(norm(key[c]) for c in hi)
    for a, b in ((median_s(lv), median_s(hv)), (lv[0] if lv else '', hv[-1] if hv else '~')):
        cands = [w for w in vocab if (a or '') <= w <= (b or '~')]
        if len(cands) >= 5: return cands
    return cands

def median_s(v):
    return v[len(v) // 2] if v else ''

def context(seq, i, key, blanked):
    def val(j):
        g = seq[j]
        if j in blanked or g not in key: return None
        return norm(key[g])
    left = ''; j = i - 1
    while j >= 0 and len(left) < CTX:
        v = val(j)
        if v is None: break
        left = v + left; j -= 1
    right = ''; j = i + 1
    while j < len(seq) and len(right) < CTX:
        v = val(j)
        if v is None: break
        right += v; j += 1
    return left[-CTX:], right[:CTX]

def predict(lm, code, left, right, key, vocab):
    cands = bracket(code, key, vocab)
    sc = sorted(((lm.logp(left, w + right), w) for w in cands), reverse=True)
    if not sc: return '', 0.0, []
    m = sc[0][0] - sc[1][0] if len(sc) > 1 else 99.0
    return sc[0][1], m, [w for _, w in sc[:5]]

def items(prefix):
    rows = [r for r in csv.DictReader(open(os.path.join(TGT, 'ciphertext.tsv')), delimiter='\t') if r['line'].startswith(prefix)]
    return rows

def main():
    key0 = load_key(); text, words = corpus(); lm = LM(text)
    keyvals = {norm(v) for v in key0.values()}
    vocab = sorted({w for w, c in words.items() if c >= 3} | keyvals)
    rows = items('BLA185')
    seq = [int(r['group']) for r in rows]
    test = [i for i, r in enumerate(rows) if r['conf'] == 'H' and r['gloss'] and int(r['group']) in key0]
    out = []; summ = {}
    for mode in ('control', 'shuffled'):
        accs = []
        for s in SEEDS:
            rnd = random.Random(s); ok = 0
            for i in test:
                code = seq[i]; key = {c: v for c, v in key0.items() if c != code}
                others = [j for j in range(len(seq)) if j != i]
                blanked = set(rnd.sample(others, round(BLANK * len(others))))
                if mode == 'shuffled':
                    k = rnd.choice([j for j in test if seq[j] != code])
                    left, right = context(seq, k, key, blanked)
                else:
                    left, right = context(seq, i, key, blanked)
                pred, m, top = predict(lm, code, left, right, key, vocab)
                gold = norm(rows[i]['gloss']); hit = int(pred == gold); ok += hit
                out.append([mode, s, rows[i]['line'], rows[i]['pos'], code, gold, pred, round(m, 3), hit, ' '.join(top)])
            accs.append(ok / len(test))
        summ[mode] = {'per_seed': [round(a, 4) for a in accs], 'mean': round(sum(accs) / len(accs), 4), 'n': len(test)}
    g1 = summ['control']['mean'] >= 0.40; g2 = summ['control']['mean'] - summ['shuffled']['mean'] >= 0.10
    summ['gate'] = {'control>=0.40': g1, 'control-shuffled>=0.10': g2, 'pass': g1 and g2}
    ctl = sorted([(r[7], r[8]) for r in out if r[0] == 'control'], reverse=True)
    tstar = None
    for t in sorted({m for m, _ in ctl}):
        sel = [h for m, h in ctl if m >= t]
        if len(sel) >= 15 and sum(sel) / len(sel) >= 0.70: tstar = t; break
    summ['t_star'] = tstar
    # target
    tgt = list(csv.DictReader(open(os.path.join(TGT, 'reading_tokens.tsv')), delimiter='\t'))
    tout = []
    for item in ('BLA186_p1', 'BLA186_p3', 'BLA191_p5'):
        rr = [r for r in tgt if r['line'].startswith(item)]; sq = [int(r['group']) for r in rr]
        for i, r in enumerate(rr):
            if r['grade'] != 'U' or int(r['group']) in (585,): continue
            left, right = context(sq, i, key0, set())
            pred, m, top = predict(lm, sq[i], left, right, key0, vocab)
            grade = ('S' if (summ['gate']['pass'] and tstar is not None and m >= tstar) else
                     'M' if summ['gate']['pass'] else 'ungraded')
            tout.append([r['line'], r['pos'], sq[i], left, right, pred, round(m, 3), grade, ' '.join(top)])
    files = {'control.tsv': ['mode\tseed\tline\tpos\tcode\tgold\tpred\tmargin\thit\ttop5'] + ['\t'.join(map(str, r)) for r in out],
             'target_fill.tsv': ['line\tpos\tgroup\tleft\tright\tpred\tmargin\tgrade\ttop5'] + ['\t'.join(map(str, r)) for r in tout]}
    blobs = {k: '\n'.join(v) + '\n' for k, v in files.items()}; blobs['summary.json'] = json.dumps(summ, indent=1) + '\n'
    if '--check' in sys.argv:
        bad = [k for k, v in blobs.items() if not os.path.exists(os.path.join(HERE, k)) or open(os.path.join(HERE, k)).read() != v]
        print('stale:' if bad else 'ok', *bad); sys.exit(1 if bad else 0)
    for k, v in blobs.items(): open(os.path.join(HERE, k), 'w').write(v)
    print(json.dumps(summ))

if __name__ == '__main__':
    main()
