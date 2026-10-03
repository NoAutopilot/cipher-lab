#!/usr/bin/env python3
"""GAPS54 (3 Oct 2026): one-part frequency-position test on No 4 + No 6 (vanspaen-vandergoes-1808).
Pre-registration: gaps54/PREREG.md (pushed before any score). Control first: the target is scored in a language
only if the one-part control clears G1 (power) and the two-part null clears G2 there.

  python3 freq_pos.py           controls (40 one-part + 200 two-part seeds x fr/nl), then the target; writes results.tsv
  python3 freq_pos.py --check   exit 1 if the committed results.tsv is stale
Disk only: corpora from tools/data/fr1810 and tools/data/nl18."""
import bisect, gzip, os, random, re, sys, unicodedata
from collections import Counter
from statistics import mean

H = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(H, '../../../tools/data')
LO, HI = 15, 1339
NCODE = HI - LO + 1
NVOC = NCODE - 26
NTOK = 304
NF = 15
ONE_SEEDS, TWO_SEEDS = range(40), range(200)
CORPUS = {'fr': 'fr1810', 'nl': 'nl18'}
LETTERS = [chr(c) for c in range(97, 123)]


def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    return ''.join(c for c in w if 'a' <= c <= 'z')


def load(lang):
    d = os.path.join(DATA, CORPUS[lang])
    out = []
    for f in sorted(f for f in os.listdir(d) if f.endswith('.txt.gz')):
        txt = gzip.open(os.path.join(d, f), 'rt', encoding='utf-8', errors='ignore').read()
        out.append([w for w in (norm(t) for t in re.findall(r"[^\W\d_]+", txt)) if w])
    return out


def vocab(words):
    top = [w for w, _ in Counter(w for w in words if len(w) > 1).most_common(NVOC)]
    return sorted(set(top) | set(LETTERS))


def pred(voc, w):
    return LO + bisect.bisect_left(voc, w) * NCODE / len(voc)


def stat(groups, fpreds, top10=False):
    c = Counter(groups)
    ranked = sorted(c, key=lambda v: (-c[v], v))
    T = ranked[:10] if top10 else [v for v in ranked if c[v] >= 3]
    if len(T) < 5:
        T = ranked[:5]
    return mean(min(abs(t - p) for p in fpreds) for t in T)


def encipher(words, code):
    keys = sorted(k for k in code if len(k) > 1)
    g = []
    for w in words:
        if w in code:
            g.append(code[w])
        else:
            g.append(code[keys[min(bisect.bisect_left(keys, w), len(keys) - 1)]])
        if len(g) >= NTOK:
            break
    return g


def control(lang, files, seed, design):
    rng = random.Random(54000 + 1000 * seed + (0 if lang == 'fr' else 1) + (500 if design == 'two-part' else 0))
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
    g = encipher(bwords[start:start + 5000], code)
    fp = [pred(pvoc, w) for w, _ in Counter(pwords).most_common(NF)]
    return len(set(g)), stat(g, fp), stat(g, fp, True)


def main():
    groups = [int(x) for x in open(os.path.join(H, 'no4_all.txt')).read().split()]
    assert len(groups) == NTOK and len(set(groups)) == 216
    rows = ['lang\tdesign\tseed\tK\tS\tS_top10']
    out = []
    for lang in ('fr', 'nl'):
        files = load(lang)
        one = [control(lang, files, s, 'one-part') for s in ONE_SEEDS]
        two = [control(lang, files, s, 'two-part') for s in TWO_SEEDS]
        for d, res, seeds in (('one-part', one, ONE_SEEDS), ('two-part', two, TWO_SEEDS)):
            rows += [f'{lang}\t{d}\t{s}\t{k}\t{a:.2f}\t{b:.2f}' for s, (k, a, b) in zip(seeds, res)]
        st = sorted(r[1] for r in two)
        p05 = st[int(0.05 * (len(st) - 1))]
        st10 = sorted(r[2] for r in two)
        p05_10 = st10[int(0.05 * (len(st10) - 1))]
        power = sum(r[1] < p05 for r in one) / len(one)
        g1, g2 = power >= 0.80, 25 <= mean(st) <= 75
        line = (f'# {lang}: one-part S mean {mean(r[1] for r in one):.2f} (K mean {mean(r[0] for r in one):.0f}); '
                f'two-part S mean {mean(st):.2f} p05 {p05:.2f} (K mean {mean(r[0] for r in two):.0f}); '
                f'power {power:.3f}; top10: one-part {mean(r[2] for r in one):.2f}, two-part p05 {p05_10:.2f}, '
                f'power {sum(r[2] < p05_10 for r in one) / len(one):.3f}; G1 {"ok" if g1 else "FAIL"} '
                f'G2 {"ok" if g2 else "FAIL"}')
        if g1 and g2:
            voc = vocab([w for f in files for w in f])
            fw = [w for w, _ in Counter(w for f in files for w in f).most_common(NF)]
            fp = [pred(voc, w) for w in fw]
            t, t10 = stat(groups, fp), stat(groups, fp, True)
            line += (f'; target S {t:.2f} S_top10 {t10:.2f} -> {"PASS" if t < p05 else "FAIL"}; F = '
                     + ' '.join(f'{w}:{p:.0f}' for w, p in zip(fw, fp)))
            rows.append(f'{lang}\ttarget\t-\t216\t{t:.2f}\t{t10:.2f}')
        else:
            line += '; target NOT scored: untestable at N 304 by this statistic'
        out.append(line)
    txt = '\n'.join(out + rows) + '\n'
    p = os.path.join(H, 'results.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if os.path.exists(p) and open(p).read() == txt else 1)
    open(p, 'w').write(txt)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
