#!/usr/bin/env python3
"""N5-HEL7 (4 Oct 2026): context-fit key-rebuild of R1953 codes 1-800, control first (PREREG-HEL7.md).
Gibbs anneal of a single fr18 word (top 800 types) per free code, objective = sum of junction scores with the R4369 H/S context
(arm P: PMI with the OOV floor; arm L: log conditional probability). Control: R4369's own 801+ codes blanked one fold at a time
(10 folds), recovery profile-weighted to the target's occurrence profile, against a shuffled-assignment baseline.
The target run happens only for an arm whose control met the gate.
Usage: python3 rebuild.py [--check]   (writes rebuild_output.txt and target_candidates.tsv; --check exits 1 if stale)"""
import os, sys, re, math, random, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'sibling_michell'))
import test_sibling as ts

SEEDS = (1, 2, 3); NV = 800; SWEEPS = 80; ICM = 5; T0, T1 = 1.5, 0.05; NFOLD = 10; NPERM = 200
BINS = (1, 2, 3, 4, 5)  # 5 = 5+
binof = lambda n: min(n, 5)

def load_stream():
    rows = []
    for l in open(os.path.join(T, 'key_r4369/reading_R1953_tokens.tsv'), encoding='utf-8').read().splitlines()[1:]:
        line, pos, sign, conf, value, grade = l.split('\t')
        rows.append((re.sub(r'[_^]', '', sign), value, grade))
    return rows

def build_scores(u, b, V, ctx_words):
    tot = sum(u.values()); fl = math.log(0.3)
    def pmi(a, c):
        pc = (u.get(c, 0) + 0.5) / tot
        if not u.get(a): return fl
        return math.log((0.7 * b.get((a, c), 0) / u[a] + 0.3 * pc) / pc)
    def lcp(a, c):
        pc = (u.get(c, 0) + 0.5) / tot
        if not u.get(a): return math.log(pc)
        return math.log(0.7 * b.get((a, c), 0) / u[a] + 0.3 * pc)
    out = {}
    for arm, f in (('P', pmi), ('L', lcp)):
        VV = np.array([[f(a, c) for c in V] for a in V])
        KV = {w: np.array([f(w, c) for c in V]) for w in ctx_words}   # known left, candidate right
        VK = {w: np.array([f(a, w) for a in V]) for w in ctx_words}   # candidate left, known right
        out[arm] = (VV, KV, VK)
    return out

def anneal(rows, free, known, sc, nV, rng):
    """free: set of codes to assign; known: position -> (first word, last word) for context tokens. Returns code -> V index."""
    VV, KV, VK = sc
    codes = sorted(free, key=int)
    occ = collections.defaultdict(list)
    for j, (s, v, g) in enumerate(rows):
        if s in free: occ[s].append(j)
    # per code: list of neighbour descriptors ('K', side, word) or ('F', side, code)
    nbrs = {}
    for c in codes:
        lst = []
        for j in occ[c]:
            for side, k in (('L', j - 1), ('R', j + 1)):
                if not 0 <= k < len(rows): continue
                if k in known: lst.append(('K', side, known[k][1] if side == 'L' else known[k][0]))
                elif rows[k][0] in free: lst.append(('F', side, rows[k][0]))
        nbrs[c] = lst
    a = {c: rng.randrange(nV) for c in codes}
    nrng = np.random.default_rng(rng.randrange(2**32))
    total = SWEEPS + ICM
    for sw in range(total):
        temp = T0 * (T1 / T0) ** (sw / (SWEEPS - 1)) if sw < SWEEPS else 0
        order = codes[:]; rng.shuffle(order)
        for c in order:
            s = np.zeros(nV)
            for kind, side, x in nbrs[c]:
                if kind == 'K':
                    s += KV[x] if side == 'L' else VK[x]
                elif x == c:
                    s += np.diag(VV) * 0.5  # a doubled code: the pair is seen from both sides, count it once
                else:
                    s += VV[a[x]] if side == 'L' else VV[:, a[x]]
            if temp == 0:
                a[c] = int(np.argmax(s))
            else:
                z = s / temp; z -= z.max(); p = np.exp(z); p /= p.sum()
                a[c] = int(nrng.choice(nV, p=p))
    return a

def main():
    rows = load_stream()
    u, b = ts.fr18_counts()
    V = [w for w, _ in u.most_common(NV)]; Vset = set(V)
    known = {}
    for j, (s, v, g) in enumerate(rows):
        w = ts.words(v)
        if g in ('H', 'S') and w: known[j] = (w[0], w[-1])
    ctx = {w for f, l in known.values() for w in (f, l)}
    scores = build_scores(u, b, V, ctx)
    cnt = collections.Counter(s for s, v, g in rows)
    target = {s for s, v, g in rows if re.fullmatch(r'\d+', s) and int(s) <= 800}
    tprof = collections.Counter(binof(cnt[c]) for c in target)
    w = {n: tprof[n] / len(target) for n in BINS}
    truth = {}
    for j, (s, v, g) in enumerate(rows):
        if j in known and re.fullmatch(r'\d+', s) and int(s) > 800: truth[s] = ts.words(v)
    ctrl_codes = sorted(truth, key=int)
    o = [f'# N5-HEL7 rebuild (PREREG-HEL7.md). Target: {sum(cnt[c] for c in target)} tokens, {len(target)} codes, profile '
         + ' '.join(f'{n}:{tprof[n]}' for n in BINS) + f' (5 = 5+). Known context tokens: {len(known)}. V = fr18 top {NV}.',
         f'# Control pool: {len(ctrl_codes)} codes 801+ with an H/S token; ceiling (true value one word in V): '
         f'{sum(len(truth[c]) == 1 and truth[c][0] in Vset for c in ctrl_codes)}/{len(ctrl_codes)}']
    def rw(hit, codes):  # profile-weighted recovery
        r = 0.0
        for n in BINS:
            cs = [c for c in codes if binof(cnt[c]) == n]
            if cs: r += w[n] * sum(hit[c] for c in cs) / len(cs)
        return r
    gate = {}
    for arm in ('P', 'L'):
        o.append(f'## arm {arm}: control')
        o.append('seed\tR_w\tbaseline_w\tunweighted\ttoken_weighted\tper-bin r_n (1/2/3/4/5+)')
        Rws, Bs = [], []
        for seed in SEEDS:
            rng = random.Random(seed * 100 + ord(arm))
            cc = ctrl_codes[:]; rng.shuffle(cc)
            folds = [cc[i::NFOLD] for i in range(NFOLD)]
            hit = {}; base = []
            for fold in folds:
                a = anneal(rows, target | set(fold), {k: x for k, x in known.items() if rows[k][0] not in fold},
                           scores[arm], NV, rng)
                for c in fold: hit[c] = truth[c] == [V[a[c]]]
                vals = [a[c] for c in fold]
                for _ in range(NPERM):
                    rng.shuffle(vals)
                    base.append((fold, {c: truth[c] == [V[x]] for c, x in zip(fold, vals)}))
            Rw = rw(hit, ctrl_codes)
            # baseline: mean over permutations of the profile-weighted recovery across all folds
            per_perm = collections.defaultdict(dict)
            for i, (fold, h) in enumerate(base):
                per_perm[i % NPERM].update(h)
            B = sum(rw(h, ctrl_codes) for h in per_perm.values()) / NPERM
            unw = sum(hit.values()) / len(hit); tokw = sum(hit[c] * cnt[c] for c in hit) / sum(cnt[c] for c in hit)
            rn = []
            for n in BINS:
                cs = [c for c in ctrl_codes if binof(cnt[c]) == n]
                rn.append(f'{sum(hit[c] for c in cs)}/{len(cs)}')
            o.append(f'{seed}\t{Rw:.3f}\t{B:.4f}\t{unw:.3f}\t{tokw:.3f}\t{" ".join(rn)}')
            o.append('  recovered: ' + ', '.join(f'{c}={truth[c][0]}(x{cnt[c]})' for c in ctrl_codes if hit[c]))
            Rws.append(Rw); Bs.append(B)
        mR, mB = sum(Rws) / len(Rws), sum(Bs) / len(Bs)
        ok = mR >= 0.20 and mR >= 3 * mB
        gate[arm] = ok
        o.append(f'arm {arm} control: mean R_w {mR:.3f} vs mean baseline {mB:.4f} (3x = {3*mB:.4f}); gate R_w>=0.20 and >=3x baseline: '
                 f'{"PASS" if ok else "FAIL"}')
    cand = ['arm\tcode\toccurrences\tvalue_seed1\tvalue_seed2\tvalue_seed3\tstable']
    for arm in ('P', 'L'):
        if not gate[arm]:
            o.append(f'## arm {arm}: CONTROL BELOW GATE -- target not run (PREREG 4)')
            continue
        o.append(f'## arm {arm}: target run')
        res = []
        for seed in SEEDS:
            res.append(anneal(rows, target, known, scores[arm], NV, random.Random(seed * 1000 + ord(arm))))
        st = 0
        for c in sorted(target, key=int):
            vs = [V[r[c]] for r in res]; s = len(set(vs)) == 1; st += s
            cand.append(f'{arm}\t{c}\t{cnt[c]}\t' + '\t'.join(vs) + f'\t{"yes" if s else "no"}')
        o.append(f'stable across all seeds: {st} of {len(target)} codes')
    return '\n'.join(o) + '\n', '\n'.join(cand) + '\n'

if __name__ == '__main__':
    txt, cand = main()
    po, pc = os.path.join(HERE, 'rebuild_output.txt'), os.path.join(HERE, 'target_candidates.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(po) and open(po).read() == txt and open(pc).read() == cand
        print('rebuild output up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(po, 'w').write(txt); open(pc, 'w').write(cand); print(txt)
