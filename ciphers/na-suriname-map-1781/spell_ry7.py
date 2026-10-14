#!/usr/bin/env python3
"""SUR-RY7 (14 Oct 2026): pre-registered r-vs-7 spelling test at 2039 legend k6 and l3 (PREREG-SUR-RY7.md).
Trigram word-fit on the 2038/2042 plain cribs, leave-one-row-out known-answer check, letter-shuffle control.
Usage: python3 spell_ry7.py [--check]   (writes spell_ry7.tsv; --check exits 1 if the committed TSV differs)."""
import csv, math, random, re, statistics, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
ALPHA = 27

def norm_words(text):
    t = text.lower().replace('ij', 'y').replace('ÿ', 'y')
    return [w for w in re.split(r'[^a-z]+', t) if w]

def rows():
    out = []
    for f in ('crib_2038_legend.tsv', 'crib_2042_legend.tsv'):
        lines = [l for l in (HERE / f).read_text(encoding='utf-8').splitlines() if not l.startswith('#')]
        for r in csv.DictReader(lines, delimiter='\t'):
            ws = norm_words(r.get('text') or '')
            if ws:
                out.append((f + ':' + r['entry'], ws))
    return out

class Model:
    def __init__(self, words):
        self.c3, self.c2, self.c1 = Counter(), Counter(), Counter()
        self.h2, self.h1 = Counter(), Counter()
        for w in words:
            p = '^^' + w + '$'
            for k in range(2, len(p)):
                a, b, c = p[k-2], p[k-1], p[k]
                self.c3[a+b+c] += 1; self.h2[a+b] += 1
                self.c2[b+c] += 1; self.h1[b] += 1
                self.c1[c] += 1
        self.n1 = sum(self.c1.values())
    def lp(self, a, b, c):
        p3 = (self.c3[a+b+c] + .5) / (self.h2[a+b] + .5*ALPHA)
        p2 = (self.c2[b+c] + .5) / (self.h1[b] + .5*ALPHA)
        p1 = (self.c1[c] + .5) / (self.n1 + .5*ALPHA)
        return math.log(.6*p3 + .3*p2 + .1*p1)

def slot_score(m, word, i, ch):
    p = '^^' + word[:i] + ch + word[i+1:] + '$'
    j = i + 2
    return sum(m.lp(p[k-2], p[k-1], p[k]) for k in range(j, min(j+3, len(p))))

def delta(m, word, i):
    return slot_score(m, word, i, 'e') - slot_score(m, word, i, 't')

TARGETS = [('k6', 'snedertyen', 6), ('l3', 'baktrey', 3)]

def shuffled(words, rng):
    out = []
    for w in words:
        l = list(w); rng.shuffle(l); out.append(''.join(l))
    return out

def known_answer(rs, rng=None):
    calls = []
    for ri, (rid, ws) in enumerate(rs):
        train = [w for rj, (_, v) in enumerate(rs) if rj != ri for w in v]
        if rng is not None:
            train = shuffled(train, rng)
        m = Model(train)
        for w in ws:
            for i, ch in enumerate(w):
                if ch in 'te':
                    d = delta(m, w, i)
                    calls.append((rid, w, i, ch, d, 'e' if d > 0 else 't'))
    return calls

def acc(calls, cls=None):
    c = [x for x in calls if cls is None or x[3] == cls]
    return sum(x[3] == x[5] for x in c) / len(c), len(c)

def pct(xs, q):
    xs = sorted(xs); k = (len(xs)-1)*q; f = int(k); c = min(f+1, len(xs)-1)
    return xs[f] + (xs[c]-xs[f])*(k-f)

def main():
    rs = rows()
    allw = [w for _, ws in rs for w in ws]
    # sanity: targets as decoded
    real = known_answer(rs)
    ra, n = acc(real); rt, nt = acc(real, 't'); re_, ne = acc(real, 'e')
    med = statistics.median(abs(x[4]) for x in real if x[3] == x[5])
    mreal = Model(allw)
    tdel = {k: delta(mreal, w, i) for k, w, i in TARGETS}
    sh_acc, sh_t = [], {k: [] for k, _, _ in TARGETS}
    for s in range(200):
        rng = random.Random(20261014 + s)
        sh_acc.append(acc(known_answer(rs, rng))[0])
        rng2 = random.Random(20261014 + s)
        ms = Model(shuffled(allw, rng2))
        for k, w, i in TARGETS:
            sh_t[k].append(delta(ms, w, i))
    sp95 = pct(sh_acc, .95)
    g1 = ra >= .80 and rt >= .60 and re_ >= .60 and ra >= sp95 + .10
    out = [['item', 'value', 'note'],
           ['corpus_rows', str(len(rs)), 'crib_2038 + crib_2042, normalised'],
           ['corpus_words', str(len(allw)), ''],
           ['ka_N', str(n), f't {nt}, e {ne}'],
           ['ka_acc_real', f'{ra:.3f}', ''],
           ['ka_acc_real_t', f'{rt:.3f}', ''],
           ['ka_acc_real_e', f'{re_:.3f}', ''],
           ['ka_acc_shuffle_mean', f'{statistics.mean(sh_acc):.3f}', '200 seeds'],
           ['ka_acc_shuffle_p95', f'{sp95:.3f}', ''],
           ['ka_median_abs_delta_correct', f'{med:.3f}', ''],
           ['G1', 'PASS' if g1 else 'FAIL', 'acc>=0.80, per-class>=0.60, acc>=shuffle p95+0.10']]
    for k, w, i in TARGETS:
        d = tdel[k]; lo, hi = pct(sh_t[k], .05), pct(sh_t[k], .95)
        beyond = d > hi if d > 0 else d < lo
        g2 = g1 and beyond and abs(d) >= med
        out.append([f'{k}_word', w, f'slot {i}'])
        out.append([f'{k}_delta_real', f'{d:.3f}', '>0 favours e (sign 7), <0 t (sign r)'])
        out.append([f'{k}_delta_shuffle_p05_p95', f'{lo:.3f};{hi:.3f}', ''])
        out.append([f'{k}_G2', ('PASS' if g2 else 'FAIL') if g1 else 'NOT SCORED (G1 FAIL)',
                    ('favours ' + ('e' if d > 0 else 't')) if g2 else ''])
    text = '\n'.join('\t'.join(r) for r in out) + '\n'
    dest = HERE / 'spell_ry7.tsv'
    if '--check' in sys.argv:
        ok = dest.exists() and dest.read_text() == text
        print('spell_ry7.tsv up to date' if ok else 'spell_ry7.tsv STALE'); sys.exit(0 if ok else 1)
    dest.write_text(text); print(text)
    # per-call log for the known-answer check
    with open(HERE / 'spell_ry7_calls.tsv', 'w') as f:
        f.write('row\tword\tpos\ttruth\tdelta\tcall\n')
        for x in real:
            f.write(f'{x[0]}\t{x[1]}\t{x[2]}\t{x[3]}\t{x[4]:.3f}\t{x[5]}\n')

if __name__ == '__main__':
    main()
