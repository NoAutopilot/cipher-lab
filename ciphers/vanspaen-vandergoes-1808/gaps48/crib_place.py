#!/usr/bin/env python3
"""GAPS48 (3 Oct 2026): crib placement against No 4 + No 6 (vanspaen-vandergoes-1808) under a one-part code
hypothesis, with a matched synthetic one-part control and a two-part control that can fail differently.
Pre-registration: gaps48/PREREG.md (pushed before this script scored the target).

  python3 crib_place.py              controls (20 seeds x fr/nl, one-part + two-part) then the target; writes results.tsv
  python3 crib_place.py --check      exit 1 if the committed results.tsv is stale
Disk only: corpora from tools/data/fr1810 and tools/data/nl18."""
import gzip, os, random, re, sys, unicodedata, bisect
from collections import Counter
from statistics import mean

H = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(H, '../../../tools/data')
LO, HI = 15, 1339
NCODE = HI - LO + 1          # 1325 values
NVOC = NCODE - 26            # word types + 26 letters
NTOK = 304
SEEDS = range(20)
NCRIB = 12
NDECOY = 300
CRIBS = {
    'fr': 'agar grand duc empereur roi sevenaar traite ratifications paris utrecht note limites'.split(),
    'nl': 'agar groot hertog keizer koning zevenaar tractaat ratificatie parijs utrecht nota grenzen'.split(),
}
CORPUS = {'fr': 'fr1810', 'nl': 'nl18'}
LETTERS = [chr(c) for c in range(97, 123)]


def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    return ''.join(c for c in w if 'a' <= c <= 'z')


def load(lang):
    d = os.path.join(DATA, CORPUS[lang])
    files = sorted(f for f in os.listdir(d) if f.endswith('.txt.gz'))
    out = []
    for f in files:
        txt = gzip.open(os.path.join(d, f), 'rt', encoding='utf-8', errors='ignore').read()
        out.append([w for w in (norm(t) for t in re.findall(r"[^\W\d_]+", txt)) if w])
    return out


def vocab(words):
    top = [w for w, _ in Counter(w for w in words if len(w) > 1).most_common(NVOC)]
    return sorted(set(top) | set(LETTERS))


def value_of(sorted_voc, w):
    """predicted value: bisect rank in the sorted vocabulary mapped linearly to LO..HI"""
    r = bisect.bisect_left(sorted_voc, w)
    return LO + r * NCODE / len(sorted_voc)


def dists(groups, preds, min_count):
    c = Counter(groups)
    vs = sorted(v for v, n in c.items() if n >= min_count)
    out = []
    for p in preds:
        i = bisect.bisect_left(vs, p)
        cand = [abs(vs[j] - p) for j in (i - 1, i) if 0 <= j < len(vs)]
        out.append(min(cand) if cand else 9999)
    return out


def auc(a, b):
    s = 0.0
    for x in a:
        for y in b:
            s += 1.0 if x < y else 0.5 if x == y else 0.0
    return s / (len(a) * len(b)) if a and b else float('nan')


def encipher(passage_words, code):
    groups, plain = [], []
    for w in passage_words:
        if w in code:
            groups.append(code[w]); plain.append(w)
        else:
            for ch in w:
                groups.append(code[ch]); plain.append(ch)
        if len(groups) >= NTOK:
            break
    return groups[:NTOK], plain


def run_control(lang, files, seed, design):
    rng = random.Random(1000 * seed + (0 if lang == 'fr' else 1))
    idx = list(range(len(files)))
    rng.shuffle(idx)
    half = max(1, len(idx) // 2)
    bwords = [w for i in idx[:half] for w in files[i]]
    pwords = [w for i in idx[half:] for w in files[i]]
    bvoc, pvoc = vocab(bwords), vocab(pwords)
    order = list(bvoc)
    if design == 'two-part':
        rng.shuffle(order)
    code = {w: LO + k for k, w in enumerate(order)}
    start = rng.randrange(0, len(bwords) - 5000)
    groups, plain = encipher(bwords[start:start + 5000], code)
    pc = Counter(plain)
    content = [w for w in pc if len(w) >= 4]
    rng.shuffle(content)
    cr1 = content[:NCRIB]
    cr2 = [w for w in content if pc[w] >= 2][:NCRIB]
    dec_pool = [w for w in pvoc if len(w) >= 4 and w not in pc]
    dec = rng.sample(dec_pool, min(NDECOY, len(dec_pool)))
    pv = lambda ws: [value_of(pvoc, w) for w in ws]
    d1c, d1d = dists(groups, pv(cr1), 1), dists(groups, pv(dec), 1)
    d2c, d2d = dists(groups, pv(cr2), 2), dists(groups, pv(dec), 2)
    return dict(K=len(set(groups)), a1=auc(d1c, d1d), a2=auc(d2c, d2d), n2=len(cr2),
                hit3=sum(x <= 3 for x in d1d) / len(d1d))


def main():
    groups = [int(x) for x in open(os.path.join(H, 'no4_all.txt')).read().split()]
    assert len(groups) == NTOK, len(groups)
    rows = ['lang\tdesign\tseed\tK\tauc_S1\tauc_S2\tn_cribs_S2\tdecoy_hit_d<=3']
    summ = {}
    for lang in ('fr', 'nl'):
        files = load(lang)
        for design in ('one-part', 'two-part'):
            res = [run_control(lang, files, s, design) for s in SEEDS]
            for s, r in zip(SEEDS, res):
                rows.append(f"{lang}\t{design}\t{s}\t{r['K']}\t{r['a1']:.3f}\t{r['a2']:.3f}\t{r['n2']}\t{r['hit3']:.3f}")
            summ[(lang, design)] = res
        # target
        voc = vocab([w for f in files for w in f])
        rng = random.Random(48)
        dec = rng.sample([w for w in voc if len(w) >= 4 and w not in CRIBS[lang]], NDECOY)
        cp = [value_of(voc, w) for w in CRIBS[lang]]
        dp = [value_of(voc, w) for w in dec]
        t1 = auc(dists(groups, cp, 1), dists(groups, dp, 1))
        t2 = auc(dists(groups, cp, 2), dists(groups, dp, 2))
        near = []
        for w, p, d in zip(CRIBS[lang], cp, dists(groups, cp, 1)):
            near.append(f'{w}:{p:.0f}/d{d:.0f}')
        rows.append(f"{lang}\ttarget\t-\t{len(set(groups))}\t{t1:.3f}\t{t2:.3f}\t{NCRIB}\t-\t{' '.join(near)}")
        summ[(lang, 'target')] = (t1, t2)
    out = []
    for lang in ('fr', 'nl'):
        one, two = summ[(lang, 'one-part')], summ[(lang, 'two-part')]
        a1o = [r['a1'] for r in one]; a1t = sorted(r['a1'] for r in two)
        a2o = [r['a2'] for r in one]; a2t = sorted(r['a2'] for r in two)
        p95_1 = a1t[int(0.95 * (len(a1t) - 1))]; p95_2 = a2t[int(0.95 * (len(a2t) - 1))]
        g0 = 0.40 <= mean(a1t) <= 0.60
        g1 = mean(a1o) >= 0.75
        t1, t2 = summ[(lang, 'target')]
        verdict = ('PASS' if t1 > p95_1 else 'FAIL') if (g0 and g1) else 'NON-TEST (control below gate)'
        out.append(f"# {lang}: one-part S1 mean {mean(a1o):.3f} (min {min(a1o):.3f}) S2 mean {mean(a2o):.3f}; "
                   f"two-part S1 mean {mean(a1t):.3f} p95 {p95_1:.3f}, S2 mean {mean(a2t):.3f} p95 {p95_2:.3f}; "
                   f"synthetic K mean {mean(r['K'] for r in one):.0f}; decoy d<=3 rate {mean(r['hit3'] for r in one):.3f}; "
                   f"G0 {'ok' if g0 else 'FAIL'} G1 {'ok' if g1 else 'FAIL'}; target S1 {t1:.3f} S2 {t2:.3f} -> {verdict}")
    txt = '\n'.join(out + rows) + '\n'
    p = os.path.join(H, 'results.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if os.path.exists(p) and open(p).read() == txt else 1)
    open(p, 'w').write(txt)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
