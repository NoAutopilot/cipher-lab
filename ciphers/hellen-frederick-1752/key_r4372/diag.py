#!/usr/bin/env python3
"""N4-HEL6 (4 Oct 2026): pre-registered diagnosis of R4372 LR100's bigram-only signal on R1953 (PREREG_diag.md).
Part A: which of the 42 adjacent covered pairs carry the junction-PMI excess over the order shuffle; leave-out curve; mechanism tags.
Part B: per-code context check -- junction PMI of each R4372-decoded token (codes 1-800) with its R4369-decoded H/S neighbours,
against (i) R4372 values permuted among its codes, (ii) R4370 values (size-matched sample) assigned to R4372's codes, and a positive
control (R4369's own 801+ values, held out, subsampled to the target's junction count).
Model, words() and pmi() are imported from ../sibling_michell/test_sibling.py unchanged.
Usage: python3 diag.py [--seed 1] [--check]   (writes diag_output.txt for seed 1, diag_output_seed2.txt for seed 2;
--check recomputes and exits 1 if the committed output differs)."""
import os, sys, re, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'sibling_michell'))
import test_sibling as ts

N = 200

def load(path):
    return {c: v for c, v in ts.load_key(path).items() if v.strip()}

def tsv_stream():
    rows = []
    for l in open(os.path.join(T, 'key_r4369/reading_R1953_tokens.tsv'), encoding='utf-8').read().splitlines()[1:]:
        line, pos, sign, conf, value, grade = l.split('\t')
        rows.append((re.sub(r'[_^]', '', sign), value, grade))
    return rows

def main(seed, out):
    rng = random.Random(seed); pmi = ts.bigram(); o = []
    k72 = load(os.path.join(HERE, 'key_LR100.tsv'))
    k70 = load(os.path.join(T, 'key_r4370/key_LR100.tsv'))
    k69 = load(os.path.join(T, 'key_r4369/key_LR100.tsv'))
    toks = ts.target_tokens(os.path.join(T, 'ciphertext_R1953.txt'))
    # ---------------- Part A ----------------
    real, npairs = ts.stat_bi(k72, toks, pmi)
    pairs = []
    for i, (x, y) in enumerate(zip(toks, toks[1:])):
        if x in k72 and y in k72:
            a, c = ts.words(k72[x]), ts.words(k72[y])
            if a and c: pairs.append((i, x, y, a[-1], c[0], pmi(a[-1], c[0])))
    null = []
    for _ in range(N):
        t2 = toks[:]; rng.shuffle(t2); null.append(ts.stat_bi(k72, t2, pmi)[0])
    mu0 = sum(null) / N
    p = lambda xs, r: sum(x >= r for x in xs) / len(xs)
    o.append(f'# Part A: R4372 key_LR100 on R1953, seed {seed}')
    o.append(f'bi real {real:.3f} on {npairs} pairs; order-shuffle mean {mu0:.3f}; order p {p(null, real):.3f}')
    pc = collections.Counter((x, y) for _, x, y, *_ in pairs)
    import gzip, glob
    uc = collections.Counter()
    for f in sorted(glob.glob(os.path.join(ts.ROOT, 'tools/data/fr18/*.txt.gz'))):
        uc.update(re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read().lower()))
    top30 = {w for w, _ in uc.most_common(30)}
    def tags(x, y, a, c):
        t = []
        if pc[(x, y)] > 1: t.append('m1')
        if 'zero' in (k72[x], k72[y]) or a == 'zero' or c == 'zero': t.append('m2')
        if x == y: t.append('m3')
        if a in top30 and c in top30: t.append('m4')
        return ','.join(t) or '-'
    srt = sorted(pairs, key=lambda r: -(r[5] - mu0))
    o.append('pos\tx\ty\tv(x)\tv(y)\tjunction\tpmi\texcess\ttags')
    for i, x, y, a, c, s in srt:
        o.append(f'{i}\t{x}\t{y}\t{k72[x]}\t{k72[y]}\t{a}|{c}\t{s:.3f}\t{s - mu0:+.3f}\t{tags(x, y, a, c)}')
    kstar = None; curve = []
    for k in range(0, len(srt) + 1):
        rest = [r[5] for r in srt[k:]]
        if not rest: break
        r_k = sum(rest) / len(rest); pk = p(null, r_k); curve.append(f'{k}:{r_k:.3f}/p{pk:.3f}')
        if kstar is None and pk > 0.0125: kstar = k
        if k >= 10 and kstar is not None: break
    o.append('leave-out curve (k pairs dropped: real / order p): ' + ' '.join(curve))
    first = srt[:kstar] if kstar else []
    ft = [tags(x, y, a, c) for _, x, y, a, c, _ in first]
    mech = None
    if kstar is not None and kstar <= 3:
        for m in ('m1', 'm2', 'm3', 'm4'):
            if all(m in t for t in ft): mech = m; break
    o.append(f'k* = {kstar}; tags of the first k* pairs: {ft}; artefact rule fired: {mech or "no"}')
    o.append(f'repeated code pairs among the {npairs}: ' + ', '.join(f'{x}-{y} x{n}' for (x, y), n in pc.items() if n > 1))
    # ---------------- Part B ----------------
    rows = tsv_stream()
    def is72(s, key): return re.fullmatch(r'\d+', s) and int(s) <= 800 and s in key and ts.words(key[s]) and key[s] != 'zero'
    def nb(j):
        if 0 <= j < len(rows) and rows[j][2] in ('H', 'S') and ts.words(rows[j][1]): return ts.words(rows[j][1])
    units = []  # (code, side, neighbour words)
    for j, (s, v, g) in enumerate(rows):
        if not is72(s, k72): continue
        L, R = nb(j - 1), nb(j + 1)
        if L: units.append((s, 'L', L[-1]))
        if R: units.append((s, 'R', R[0]))
    def jscore(val, side, w):
        vw = ts.words(val)
        if not vw: return None
        return pmi(w, vw[0]) if side == 'L' else pmi(vw[-1], w)
    def SB(key):
        sc = [jscore(key[c], sd, w) for c, sd, w in units if c in key]
        sc = [x for x in sc if x is not None]
        return sum(sc) / len(sc) if sc else float('nan')
    def per_code(key):
        d = collections.defaultdict(list)
        for c, sd, w in units:
            x = jscore(key[c], sd, w) if c in key else None
            if x is not None: d[c].append(x)
        return {c: sum(v) / len(v) for c, v in d.items()}
    J = len(units); s_real = SB(k72); pc_real = per_code(k72)
    codes72 = sorted(k72, key=int); vals72 = [k72[c] for c in codes72]
    nullA, pcn = [], collections.defaultdict(list)
    for _ in range(N):
        vs = vals72[:]; rng.shuffle(vs); kk = dict(zip(codes72, vs))
        nullA.append(SB(kk))
        for c, x in per_code(kk).items(): pcn[c].append(x)
    pool70 = [v for c, v in k70.items() if int(re.sub(r'\D', '', c) or 0) <= 800]
    nullB = []
    for _ in range(N):
        vs = rng.sample(pool70, min(len(codes72), len(pool70)))
        vs += rng.sample(pool70, len(codes72) - len(vs)) if len(vs) < len(codes72) else []
        nullB.append(SB(dict(zip(codes72, vs))))
    nullA = [x for x in nullA if x == x]; nullB = [x for x in nullB if x == x]
    q99 = lambda xs: sorted(xs)[int(.99 * len(xs)) - 1]
    o.append(f'# Part B: junctions of R4372-decoded tokens (codes 1-800, zero excluded) with R4369 H/S neighbours')
    o.append(f'units: {len(set(c for c, *_ in units))} codes, {sum(1 for j,(s,_,_) in enumerate(rows) if is72(s,k72) and (nb(j-1) or nb(j+1)))} tokens, J = {J} junctions')
    o.append(f'S_B real {s_real:.3f} | (i) R4372 permuted: mean {sum(nullA)/len(nullA):.3f}, p99 {q99(nullA):.3f}, p {p(nullA, s_real):.3f}'
             f' | (ii) R4370 size-matched: mean {sum(nullB)/len(nullB):.3f}, p99 {q99(nullB):.3f}, p {p(nullB, s_real):.3f}')
    # positive control: R4369 801+ tokens with H/S neighbours, held out
    pos = []
    for j, (s, v, g) in enumerate(rows):
        if not (re.fullmatch(r'\d+', s) and int(s) > 800 and s in k69 and g in ('H', 'S') and ts.words(k69[s])): continue
        L, R = nb(j - 1), nb(j + 1)
        if L: pos.append((s, 'L', L[-1]))
        if R: pos.append((s, 'R', R[0]))
    codes69 = sorted(k69, key=int); vals69 = [k69[c] for c in codes69]
    def SBu(key, us):
        sc = [jscore(key[c], sd, w) for c, sd, w in us]; sc = [x for x in sc if x is not None]
        return sum(sc) / len(sc)
    hits = 0
    for _ in range(N):
        us = rng.sample(pos, J); r = SBu(k69, us); sh = []
        for _ in range(50):
            vs = vals69[:]; rng.shuffle(vs); sh.append(SBu(dict(zip(codes69, vs)), us))
        hits += p(sh, r) <= 0.01
    full_r = SBu(k69, pos)
    o.append(f'positive control: R4369 own values, {len(pos)} junctions available (full-pool real {full_r:.3f}); subsampled to J={J}: '
             f'power (p<=0.01 vs 50 permutations) {hits/N:.2f}')
    gate = p(nullA, s_real) <= 0.01 and p(nullB, s_real) <= 0.01 and hits / N >= 0.8
    o.append(f'gate (seed {seed}): {"PASS" if gate else "FAIL"}')
    o.append('per-code (s_c, n junctions, per-code (i) p), sorted by p:')
    rowsc = []
    for c, x in pc_real.items():
        n = sum(1 for cc, *_ in units if cc == c)
        pcp = p(pcn[c], x) if pcn[c] else float('nan'); rowsc.append((pcp, c, x, n))
    for pcp, c, x, n in sorted(rowsc):
        if pcp <= 0.10: o.append(f'  {c}\t{k72[c]}\ts_c {x:.3f}\tn {n}\tp {pcp:.3f}{"  <- candidate (n>=2, p<=0.05)" if n >= 2 and pcp <= 0.05 else ""}')
    o.append(f'per-code candidates (n>=2, p<=0.05): {sum(1 for pcp,c,x,n in rowsc if n>=2 and pcp<=0.05)} of {len(rowsc)} codes;'
             f' expected by chance about {0.05*sum(1 for r in rowsc if r[3]>=2):.1f}')
    txt = '\n'.join(o) + '\n'
    return txt

if __name__ == '__main__':
    a = sys.argv
    seed = int(a[a.index('--seed') + 1]) if '--seed' in a else 1
    path = os.path.join(HERE, 'diag_output.txt' if seed == 1 else f'diag_output_seed{seed}.txt')
    txt = main(seed, path)
    if '--check' in a:
        ok = os.path.exists(path) and open(path).read() == txt
        print('diag output up to date' if ok else 'STALE: ' + path); sys.exit(0 if ok else 1)
    open(path, 'w').write(txt); print(txt)
