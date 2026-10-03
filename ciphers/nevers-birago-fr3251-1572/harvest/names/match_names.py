#!/usr/bin/env python3
"""NEVBIR-NAMES: whole-name gap fill against the letter pattern around each gap, with two matched controls.

Rule fixed in PREREG.md (pushed before any gap was inventoried). Disk only.
  python3 match_names.py            # pre-registered run, fr.3251 nos.71/86/90 -> gaps.tsv, fills.tsv, summary.txt
  python3 match_names.py --f117     # exploratory (NOT pre-registered): fr.3252 f.117r, M letters treated as fixed
Seed 1, 200 draws per control.
"""
import argparse, csv, gzip, json, os, random, re, sys, unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
H = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(HERE, '../../../..'))
F3252 = os.path.join(ROOT, 'ciphers/birago-fr3252-1571-72/harvest/f117')


def norm(w):
    w = ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn').lower()
    return w.replace('v', 'u').replace('j', 'i').replace('y', 'i')


def load_gaz():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'gazetteer.tsv')), delimiter='\t'))
    return [(r['form'], r['canonical']) for r in rows]


def load_letter_tsv(paths):
    toks = []
    for p in paths:
        for r in csv.DictReader(open(os.path.join(H, p)), delimiter='\t'):
            v, g = r['value'], r['grade']
            kind = 'bar' if (len(v) != 1 or not v.isalpha()) and g != 'U' else ('U' if g == 'U' else g)
            if kind in ('S', 'C'):
                kind = 'F'
            toks.append(dict(line=r['line'], pos=r['pos'], sign=r['sign'], val=v, kind=kind))
    return toks


def load_f117():
    m = {d['id']: d for d in json.load(open(os.path.join(F3252, 'map_printed.json')))}
    toks = []
    for r in csv.DictReader(open(os.path.join(F3252, 'la/recon_f117_3r.tsv')), delimiter='\t'):
        d = m.get(r['sign_id'])
        if d is None:
            toks.append(dict(line=r['passage'], pos=r['pos'], sign=r['sign_id'], val='?', kind='U'))
        elif d['kind'] != 'letter' or len(d['value']) != 1:
            toks.append(dict(line=r['passage'], pos=r['pos'], sign=r['sign_id'], val=d['value'], kind='bar'))
        else:  # exploratory: M letters of f.117 treated as fixed (no S exists on this leaf)
            toks.append(dict(line=r['passage'], pos=r['pos'], sign=r['sign_id'], val=d['value'], kind='F'))
    return toks


def gaps_of(toks, gapkinds):
    out, i = [], 0
    while i < len(toks):
        if toks[i]['kind'] in gapkinds:
            j = i
            while j < len(toks) and toks[j]['kind'] in gapkinds:
                j += 1
            if j - i >= 3:
                out.append((i, j))
            i = j
        else:
            i += 1
    return out


def best(toks, gap, forms, vals=None):
    """max score over admissible placements; returns (score, fixed_matched, form, start)"""
    a, b = gap
    vals = vals or [t['val'] for t in toks]
    res = (0.0, 0, None, None)
    n = len(toks)
    for f, _ in forms:
        L = len(f)
        need = min(3, L)
        for s in range(max(0, a - L + need), min(b - need, n - L) + 1):
            e = s + L
            ov = min(e, b) - max(s, a)
            if ov < need:
                continue
            ok, fx, mm = True, 0, 0
            for k in range(L):
                t = toks[s + k]
                if t['kind'] == 'bar':
                    ok = False; break
                if t['kind'] == 'F':
                    if vals[s + k] != f[k]:
                        ok = False; break
                    fx += 1
                elif t['kind'] == 'M' and vals[s + k] == f[k]:
                    mm += 1
            if not ok or fx < 3:
                continue
            sc = fx + 0.5 * mm
            if sc > res[0]:
                res = (sc, fx, f, s)
    return res


def corpus_words():
    words = Counter()
    for d, share in (('it16dip', 'it'), ('fr16', 'fr')):
        dd = os.path.join(ROOT, 'tools/data', d)
        for fn in sorted(os.listdir(dd)):
            if fn.endswith('.gz'):
                txt = gzip.open(os.path.join(dd, fn), 'rt', errors='ignore').read()
                for w in re.findall(r'[^\W\d_]+', txt):
                    words[(share, norm(w))] += 1
    return words


def random_gaz(rng, gaz, pools):
    forms = set(f for f, _ in gaz)
    out = []
    for f, _ in gaz:
        lang = 'it' if rng.random() < 0.8 else 'fr'
        pool = pools[(lang, len(f))] or pools[('it', len(f))]
        while True:
            w = rng.choice(pool)
            if w not in forms:
                break
        out.append((w, '_'))
    return out


def p95(xs):
    xs = sorted(xs)
    return xs[int(0.95 * (len(xs) - 1))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--f117', action='store_true')
    ap.add_argument('--draws', type=int, default=200)
    a = ap.parse_args()
    rng = random.Random(1)
    gaz = load_gaz()
    if a.f117:
        letters = {'f117r': load_f117()}
        gapkinds, tag = ('U',), 'f117_explore'
    else:
        letters = {'no71': load_letter_tsv(['reading_f139v_tokens.tsv']),
                   'no86': load_letter_tsv(['reading_no86_tokens.tsv']),
                   'no90': load_letter_tsv(['reading_no90_tokens.tsv'])}
        gapkinds, tag = ('U', 'M'), 'prereg'
    cw = corpus_words()
    pools = defaultdict(list)
    for (lang, w), c in cw.items():
        if c >= 3 and 2 <= len(w) <= 16:
            pools[(lang, len(w))].append(w)
    for k in pools:
        pools[k].sort()
    rgaz = [random_gaz(rng, gaz, pools) for _ in range(a.draws)]
    grows, frows = [], []
    for lt, toks in letters.items():
        fixed_idx = [i for i, t in enumerate(toks) if t['kind'] == 'F']
        fixed_vals = [toks[i]['val'] for i in fixed_idx]
        shuf = []
        for _ in range(a.draws):
            v = fixed_vals[:]; rng.shuffle(v)
            vals = [t['val'] for t in toks]
            for i, x in zip(fixed_idx, v):
                vals[i] = x
            shuf.append(vals)
        for g in gaps_of(toks, gapkinds):
            sc, fx, f, s = best(toks, g, gaz)
            c1 = [best(toks, g, rg)[0] for rg in rgaz]
            c2 = [best(toks, g, gaz, vals=v)[0] for v in shuf]
            p1, p2 = p95(c1), p95(c2)
            lo, hi = max(0, g[0] - 6), min(len(toks), g[1] + 6)
            ctx = ''.join((t['val'] if t['kind'] == 'F' else ('[' + t['val'] + ']' if t['kind'] == 'bar' else ('.' if t['kind'] == 'U' else t['val'].upper()))) for t in toks[lo:hi])
            surv = sc > 0 and sc > p1 and sc > p2
            grows.append([lt, toks[g[0]]['line'], toks[g[0]]['pos'], g[1] - g[0], ctx, f or '', sc, fx, p1, max(c1), p2, max(c2), 'yes' if surv else 'no'])
            if surv:
                win = toks[s:s + len(f)]
                frows.append([lt, toks[g[0]]['line'], toks[g[0]]['pos'], f, dict(gaz)[f], sc, fx, p1, p2,
                              ' '.join(f"{t['sign']}={f[k]}" for k, t in enumerate(win) if t['kind'] in ('U', 'M'))])
    hdr = ['letter', 'line', 'pos', 'gap_len', 'context(fixed lower, M UPPER, U .)', 'best_form', 'score', 'fixed_matched',
           'ctrl_randgaz_p95', 'ctrl_randgaz_max', 'ctrl_flankshuf_p95', 'ctrl_flankshuf_max', 'survives']
    with open(os.path.join(HERE, f'gaps_{tag}.tsv'), 'w') as fh:
        fh.write('\t'.join(hdr) + '\n')
        for r in grows:
            fh.write('\t'.join(str(x) for x in r) + '\n')
    with open(os.path.join(HERE, f'fills_{tag}.tsv'), 'w') as fh:
        fh.write('letter\tline\tpos\tform\tcanonical\tscore\tfixed_matched\tctrl1_p95\tctrl2_p95\tunfixed_sign_values\n')
        for r in frows:
            fh.write('\t'.join(str(x) for x in r) + '\n')
    # bonus: U sign ids given one letter by >=2 surviving fills
    sv = defaultdict(list)
    for r in frows:
        for kv in r[-1].split():
            sgn, v = kv.split('=')
            if sgn.startswith('X_') or sgn == '?':
                sv[sgn].append(v)
    nb = sum(1 for r in grows if r[6] > 0)
    summ = [f'{tag}: gaps {len(grows)}; gaps with any admissible gazetteer fill (>=3 fixed) {nb}; surviving both controls {len(frows)}',
            'bonus (U sign ids, letters from surviving fills): ' + (', '.join(f'{k}:{dict(Counter(v))}' for k, v in sv.items()) or 'none')]
    open(os.path.join(HERE, f'summary_{tag}.txt'), 'w').write('\n'.join(summ) + '\n')
    print('\n'.join(summ))


if __name__ == '__main__':
    main()
