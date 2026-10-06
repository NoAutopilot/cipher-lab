#!/usr/bin/env python3
"""Spec cheap test 3 for cylob-c1995: fixed discrete alphabet structural check (R12D-CYL3, 6 Oct 2026).

Pre-registration: PREREG-test3.md (pushed before the scored run). Reads ciphertext.tsv (Rotering 2015 transcription),
builds the main sequence (p.1 once, pp.5-16; p.20 descriptive only), computes S1 (IC), S2 (repeated within-page trigram
tokens), S3 (repeated grid rows), and compares with (a) English through a random fixed 26->K map, (b) uniform random over
K signs, (c) order shuffle of the target's tokens -- all poured into the target's own page/row skeleton.

Usage: python3 structural_test3.py [--out test3_results.json] [--check]
--check regenerates and exits 1 if the committed results file differs (rule 7).
"""
import argparse, collections, csv, glob, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = ['pg64317_gatsby.txt', 'pg76_huckfinn.txt', 'pg1342_pride.txt']
SEED = 20261006
N_EN, N_UNI, N_SHUF, N_EN_SHUF = 300, 2000, 2000, 200


def load_target():
    rows = [r for r in csv.reader(open(os.path.join(HERE, 'ciphertext.tsv')), delimiter='\t')
            if r and not r[0].startswith('#')][1:]
    pages = collections.OrderedDict()
    for p, r, c, k, s in rows:
        pages.setdefault(int(p), []).append((int(r), int(c), k, s))
    skel, toks = [], []  # skel: per page, list of segments: ('h',1) or ('r',3)
    for p in [1] + list(range(5, 17)):
        if p not in pages:
            continue
        v = pages[p]
        segs, seq = [], []
        for r, c, k, s in sorted(v, key=lambda x: (x[0], x[1])):
            if k == 'header':
                segs.append(['h', 1]); seq.append(s)
        grid = collections.OrderedDict()
        for r, c, k, s in sorted(v, key=lambda x: (x[0], x[1])):
            if k == 'grid':
                grid.setdefault(r, []).append(s)
        for r, g in grid.items():
            segs.append(['r', len(g)]); seq.extend(g)
        if seq:
            skel.append(segs); toks.extend(seq)
    p20 = [s for r, c, k, s in pages.get(20, []) if s != '-']
    return skel, toks, p20


def pour(skel, toks):
    """Split a flat token list into pages -> (page_seq, [rows])."""
    out, i = [], 0
    for segs in skel:
        seq, rows = [], []
        for kind, n in segs:
            chunk = toks[i:i + n]; i += n
            seq.extend(chunk)
            if kind == 'r':
                rows.append(tuple(chunk))
        out.append((seq, rows))
    return out


def stats(skel, toks):
    n = len(toks)
    cnt = collections.Counter(toks)
    ic = sum(v * (v - 1) for v in cnt.values()) / (n * (n - 1))
    pages = pour(skel, toks)
    tri = [tuple(seq[j:j + 3]) for seq, _ in pages for j in range(len(seq) - 2)]
    tc = collections.Counter(tri)
    s2 = sum(1 for t in tri if tc[t] >= 2)
    bi = [tuple(seq[j:j + 2]) for seq, _ in pages for j in range(len(seq) - 1)]
    bc = collections.Counter(bi)
    b2 = sum(1 for t in bi if bc[t] >= 2)
    rows = [r for _, rs in pages for r in rs if len(r) == 3]
    rc = collections.Counter(rows)
    s3 = sum(1 for r in rows if rc[r] >= 2)
    half = n // 2
    new2 = len(set(toks[half:]) - set(toks[:half]))
    return {'S1_ic': ic, 'S2_rep_tri': s2, 'S3_rep_rows': s3, 'bigram_rep': b2, 'types': len(cnt), 'new_types_2nd_half': new2}


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def english_text():
    s = []
    for f in CORPUS:
        t = open(os.path.join(ROOT, 'tools', 'data', 'en', f), encoding='utf-8', errors='ignore').read()
        a, b = t.find('*** START'), t.find('*** END')
        t = t[t.find('\n', a) if a >= 0 else 0: b if b > 0 else len(t)]
        s.append(re.sub('[^a-z]', '', t.lower()))
    return ''.join(s)


def run():
    rng = random.Random(SEED)
    skel, toks, p20 = load_target()
    n, signs = len(toks), sorted(set(toks))
    k = len(signs)
    tgt = stats(skel, toks)
    uni = [stats(skel, [rng.choice(signs) for _ in range(n)]) for _ in range(N_UNI)]
    shuf = []
    for _ in range(N_SHUF):
        t = toks[:]; rng.shuffle(t); shuf.append(stats(skel, t))
    eng = english_text()
    uni_ic95 = pct([u['S1_ic'] for u in uni], 0.95)
    en_rows, g0_s1, g0_s2 = [], 0, 0
    for _ in range(N_EN):
        letters = list('abcdefghijklmnopqrstuvwxyz'); rng.shuffle(letters)
        m = {letters[i]: signs[i] for i in range(k)}  # each sign >= 1 letter
        for L in letters[k:]:
            m[L] = rng.choice(signs)
        st = rng.randrange(0, len(eng) - n)
        et = [m[c] for c in eng[st:st + n]]
        s = stats(skel, et)
        own = []
        for _ in range(N_EN_SHUF):
            t = et[:]; rng.shuffle(t); own.append(stats(skel, t)['S2_rep_tri'])
        s['own_shuf_S2_p95'] = pct(own, 0.95)
        g0_s1 += s['S1_ic'] > uni_ic95
        g0_s2 += s['S2_rep_tri'] > s['own_shuf_S2_p95']
        en_rows.append(s)

    def summ(rows, key):
        xs = [r[key] for r in rows]
        return {'mean': round(sum(xs) / len(xs), 4), 'p05': pct(xs, 0.05), 'p50': pct(xs, 0.5), 'p95': pct(xs, 0.95), 'p99': pct(xs, 0.99)}

    keys = ['S1_ic', 'S2_rep_tri', 'S3_rep_rows', 'bigram_rep', 'new_types_2nd_half']
    res = {
        'N': n, 'K': k, 'signs': ''.join(signs), 'seed': SEED,
        'target': {kk: (round(v, 4) if isinstance(v, float) else v) for kk, v in tgt.items()},
        'english_fixed_map': {kk: summ(en_rows, kk) for kk in keys},
        'uniform_null': {kk: summ(uni, kk) for kk in keys},
        'shuffle_null': {kk: summ(shuf, kk) for kk in keys[1:4]},
        'G0_power': {'S1_frac': round(g0_s1 / N_EN, 3), 'S2_frac': round(g0_s2 / N_EN, 3)},
        'p_shuffle': {kk: round(sum(s[kk] >= tgt[kk] for s in shuf) / N_SHUF, 4) for kk in keys[1:4]},
        'p_uniform_S1': round(sum(u['S1_ic'] >= tgt['S1_ic'] for u in uni) / N_UNI, 4),
        'frac_english_ge_target': {kk: round(sum(r[kk] >= tgt[kk] for r in en_rows) / N_EN, 4) for kk in keys[:4]},
        'p20_descriptive': {'tokens': len(p20), 'types': len(set(p20)), 'seq': ''.join(p20)},
    }
    for kk in ('english_fixed_map', 'uniform_null'):
        for s in res[kk].values():
            for q in s:
                s[q] = round(s[q], 4)
    for s in res['shuffle_null'].values():
        for q in s:
            s[q] = round(s[q], 4)
    G0s1, G0s2 = res['G0_power']['S1_frac'] >= 0.8, res['G0_power']['S2_frac'] >= 0.8
    G1 = tgt['S1_ic'] > res['uniform_null']['S1_ic']['p95']
    G2 = tgt['S2_rep_tri'] > res['shuffle_null']['S2_rep_tri']['p95']
    res['gates'] = {'G0_S1': G0s1, 'G0_S2': G0s2, 'G1': G1, 'G2': G2,
                    'S3_above_shuffle_p95': tgt['S3_rep_rows'] > res['shuffle_null']['S3_rep_rows']['p95'],
                    'S2_above_english_p99': tgt['S2_rep_tri'] > res['english_fixed_map']['S2_rep_tri']['p99'],
                    'S3_above_english_p99': tgt['S3_rep_rows'] > res['english_fixed_map']['S3_rep_rows']['p99']}
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', default=os.path.join(HERE, 'test3_results.json'))
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    txt = json.dumps(run(), indent=1) + '\n'
    if a.check:
        ok = os.path.exists(a.out) and open(a.out).read() == txt
        print('test3_results.json', 'current' if ok else 'STALE')
        sys.exit(0 if ok else 1)
    open(a.out, 'w').write(txt)
    print(txt)


if __name__ == '__main__':
    main()
