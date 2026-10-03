#!/usr/bin/env python3
"""GAPS104: rasm edit-distance fit of formula candidates to ciphertext_fig1.txt vs a Quran-span null (see PREREG.md).

Usage: formula_test.py --quran TANZIL_TXT2 [--seed 1] [--null 2000] [--trials 500] [--out results.json]
The Quran text (Tanzil simple-clean txt-2, URL in ../malay-arabic/manifest.json) is fetched to scratch, not committed.
Offline test: formula_test.py --selftest
"""
import argparse, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CT = os.path.join(HERE, '..', 'ciphertext_fig1.txt')
SIGN = {'ba': 'B', 'ta': 'B', 'tha': 'B', 'nun': 'B', 'ya': 'B', 'tooth': 'B', 'jim': 'H', 'ha2': 'H', 'kha': 'H',
        'dal': 'D', 'dhal': 'D', 'ra': 'R', 'zay': 'R', 'sin': 'S', 'shin': 'S', 'sad': 'C', 'dad': 'C',
        'tta': 'T', 'zza': 'T', 'ain': 'E', 'ghayn': 'E', 'nga': 'E', 'fa': 'F', 'qaf': 'F', 'kaf': 'K',
        'lam': 'L', 'mim': 'M', 'ha': 'O', 'waw': 'W', 'alif': 'A', 'lamalif': 'LA', 'hamza': ''}
AR = {'ب': 'B', 'ت': 'B', 'ث': 'B', 'ن': 'B', 'ي': 'B', 'ى': 'B', 'ئ': 'B', 'ج': 'H', 'ح': 'H', 'خ': 'H', 'د': 'D',
      'ذ': 'D', 'ر': 'R', 'ز': 'R', 'س': 'S', 'ش': 'S', 'ص': 'C', 'ض': 'C', 'ط': 'T', 'ظ': 'T', 'ع': 'E', 'غ': 'E',
      'ف': 'F', 'ق': 'F', 'ك': 'K', 'ل': 'L', 'م': 'M', 'ه': 'O', 'ة': 'O', 'و': 'W', 'ؤ': 'W', 'ا': 'A', 'أ': 'A',
      'إ': 'A', 'آ': 'A', 'ء': ''}
CLASSES = sorted(set(''.join(AR.values())))
CANDS = {'F1': 'على كل شيء قدير', 'F2': 'محمد رسول الله', 'F2b': 'لا إله إلا الله محمد رسول الله'}


def ar_rasm(s):
    return ''.join(AR.get(c, '') for c in s)


def read_lines(path=CT):
    out = {}
    for raw in open(path, encoding='utf-8'):
        m = re.match(r'^(L\d\d):(.*)$', raw)
        if m:
            toks = [t.rstrip('?') for t in m.group(2).split()]
            out[m.group(1)] = ''.join(SIGN[t] for t in toks if t in SIGN)
    return out


def sub_lev(p, t):
    """min edit distance of p against any substring of t (free start/end in t)."""
    prev = [0] * (len(t) + 1)
    for i, pc in enumerate(p, 1):
        cur = [i] + [0] * len(t)
        for j, tc in enumerate(t, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (pc != tc))
        prev = cur
    return min(prev)


def dist(p, texts):
    return min(sub_lev(p, t) for t in texts) / len(p)


def quran_rasm(path):
    s = []
    for l in open(path, encoding='utf-8'):
        q = l.rstrip('\n').split('|')
        if len(q) == 3 and q[0].isdigit():
            s.append(ar_rasm(re.sub(r'[ً-ْٰـ]', '', q[2])))
    return ''.join(s)


def run(quran, lines, seed, nnull, trials):
    rng = random.Random(seed)
    scopes = {'LINE': [lines['L06']], 'ALL': list(lines.values())}
    res = {}
    for name, ar in CANDS.items():
        p = ar_rasm(ar)
        r = {'rasm': p, 'len': len(p)}
        for sc, texts in scopes.items():
            d = dist(p, texts)
            null = []
            for _ in range(nnull):
                o = rng.randrange(0, len(quran) - len(p))
                null.append(dist(quran[o:o + len(p)], texts))
            null.sort()
            r[sc] = {'d': round(d, 4), 'null_mean': round(sum(null) / nnull, 4), 'null_p05': null[int(.05 * nnull)],
                     'p': sum(x <= d for x in null) / nnull}
        # positive control, scope LINE: planted at 18.5 pct substitution noise
        base, hits = lines['L06'], 0
        nulls = sorted(dist(quran[o:o + len(p)], [base]) for o in
                       (rng.randrange(0, len(quran) - len(p)) for _ in range(300)))
        for _ in range(trials):
            noisy = ''.join(rng.choice([c for c in CLASSES if c != ch]) if rng.random() < .185 else ch for ch in p)
            pos = rng.randrange(0, len(base) + 1)
            planted = base[:pos] + noisy + base[pos:]
            dd = dist(p, [planted])
            hits += (sum(x <= dd for x in nulls) / len(nulls)) < .05
        r['power_LINE'] = round(hits / trials, 3)
        pl, pw = r['LINE']['p'], r['power_LINE']
        r['verdict'] = ('fits beyond chance' if pl < .05 and pw >= .8 else 'fit, low power' if pl < .05 else
                        'control-backed negative' if pw >= .8 else 'non-test')
        res[name] = r
    return res


def selftest():
    assert sub_lev('abc', 'xxabcxx') == 0 and sub_lev('abc', 'xxabxx') == 1
    assert ar_rasm('محمد') == 'MHMD' and ar_rasm('على') == 'ELB'
    assert read_lines()['L06'].startswith('SRKWMMWBD')
    print('selftest ok')


if __name__ == '__main__':
    a = argparse.ArgumentParser()
    a.add_argument('--quran'); a.add_argument('--seed', type=int, default=1)
    a.add_argument('--null', type=int, default=2000); a.add_argument('--trials', type=int, default=500)
    a.add_argument('--out'); a.add_argument('--selftest', action='store_true')
    a = a.parse_args()
    if a.selftest:
        selftest(); sys.exit(0)
    lines = read_lines()
    res = {'lines_rasm': lines, 'seed': a.seed, 'results': run(quran_rasm(a.quran), lines, a.seed, a.null, a.trials)}
    js = json.dumps(res, ensure_ascii=False, indent=1)
    open(a.out, 'w').write(js + '\n') if a.out else print(js)
