#!/usr/bin/env python3
"""GAPS43 (3 Oct 2026, account-4): gap 4, word-level GLOBAL key reassignment for 4612 v3, seeded from key_full,
scored by fr16 WORD SEGMENTATION. See PREREG.md beside this file (committed before any run).

Instrument, and why it is not the retired one: tools/key_repair.py (AX2-4612S/S2/S3, [retired] for H-S) searched
LOCALLY, one code at a time, against an fr16 order-5 CHARACTER log-probability; the AX2-4612 anneal searched
globally against an order-3 CHARACTER model. This script searches GLOBALLY (simulated annealing, single-code
reassignments and two-code swaps, Metropolis) against the WORD-SEGMENTATION cost GAPS28 pre-registered in
bandtest/band_seg.py (1.0 per letter not inside an fr16 lexicon word + 0.1 per word used; lexicon = folded fr16
corpus words, length >= 2, count >= 5). The objective is the one AX2-4612S3's postmortem named as untried.

  python3 word_anneal.py control   # 5811 cut to N=833, 20% of codes perturbed, 3 seeds + unperturbed null start
  python3 word_anneal.py target    # only after the control gate passes (refuses otherwise)

SIG-4612 (8 Oct 2026, account 1, LANE SIG-1): `--objective unigram` (PREREG-unigram.md) swaps the cost for the fr16
WORD-UNIGRAM objective: min over segmentations (Viterbi) of sum -log2 P(w) for lexicon words (folded fr16 corpus words,
any length, count >= 2, P = count / total) plus OOV_BITS per character left outside a word, OOV_BITS = 2 x the corpus's
own mean bits per character (computed from the corpus, not the cipher). The default stays GAPS43's segmentation cost.
  python3 word_anneal.py precheck --objective unigram  # key_full vs annealed optima from a random and a key_full start
  python3 word_anneal.py control  --objective unigram  # refuses unless precheck_unigram.json passed
  python3 word_anneal.py target   --objective unigram  # refuses unless control_unigram.json passed
Outputs carry a _unigram suffix; the GAPS43 files are never overwritten.
"""
import csv, json, math, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'bandtest')); sys.path.insert(0, os.path.join(T, 'ax4612tr'))
sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
import band_seg as BS
import word_share_check_v3 as WS
import french16_ngram as fr

ALPHA = sorted(set(WS.fold(c) for c in 'ABCDEFGHIKLMNOPQRSTVXYZ'))   # 23 folded letters (no J/U/W)
ITERS, RESTARTS, T0, T1, PSWAP = 60000, 6, 1.5, 0.05, 0.3
OBJECTIVE = 'seg'          # 'seg' (GAPS43 default) or 'unigram' (SIG-4612)
UNI_MINCOUNT, UNI_OOV_MULT = 2, 2.0

def unigram_lexicon():
    """fr16 word-unigram costs in bits, and OOV_BITS = UNI_OOV_MULT x the corpus's mean bits per character."""
    import collections
    c = collections.Counter(fr.corpus_words())
    c = {w: n for w, n in c.items() if n >= UNI_MINCOUNT}
    N = sum(c.values())
    lex = {w: -math.log2(n / N) for w, n in c.items()}
    mean = sum(lex[w] * n for w, n in c.items()) / sum(len(w) * n for w, n in c.items())
    return lex, max(len(w) for w in lex), UNI_OOV_MULT * mean

def unigram_cost(s, lex, maxlen, oov):
    """Viterbi: least total bits over segmentations of s into lexicon words and single OOV characters."""
    n = len(s); best = [0.0] + [float('inf')] * n
    for i in range(1, n + 1):
        b = best[i - 1] + oov
        for k in range(1, min(maxlen, i) + 1):
            w = lex.get(s[i - k:i])
            if w is not None and best[i - k] + w < b: b = best[i - k] + w
        best[i] = b
    return best[n]

def cost_fn(lex, maxlen):
    """Objective selected by OBJECTIVE; lex is a set (seg) or a (dict, oov) pair (unigram)."""
    if OBJECTIVE == 'unigram':
        d, oov = lex
        return lambda s: unigram_cost(s, d, maxlen, oov)
    return lambda s: BS.seg_cost(s, lex, maxlen)

def suffix(name):
    return name if OBJECTIVE == 'seg' else name.replace('.json', '_unigram.json').replace('.tsv', '_unigram.tsv')

def subruns(runs, key):
    """Split value-1-120 runs at codes with no single-letter key row (same rule as word_share_check_v3)."""
    out = []
    for run in runs:
        cur = []
        for c in run:
            if c in key: cur.append(c)
            elif cur: out.append(cur); cur = []
        if cur: out.append(cur)
    return out

class State:
    def __init__(self, subs, key, lex, maxlen):
        self.subs, self.key, self.lex, self.maxlen = subs, dict(key), lex, maxlen
        self.f = cost_fn(lex, maxlen)
        self.where = {}
        for i, s in enumerate(subs):
            for c in set(s): self.where.setdefault(c, []).append(i)
        self.cost = [self.sc(i) for i in range(len(subs))]
        self.total = sum(self.cost)
    def sc(self, i, key=None):
        k = key or self.key
        return self.f(''.join(k[c] for c in self.subs[i]))
    def propose(self, changes):
        trial = dict(self.key); trial.update(changes)
        idx = sorted(set(i for c in changes for i in self.where.get(c, [])))
        new = {i: self.sc(i, trial) for i in idx}
        return sum(new.values()) - sum(self.cost[i] for i in idx), new
    def accept(self, changes, new, d):
        self.key.update(changes)
        for i, v in new.items(): self.cost[i] = v
        self.total += d

def anneal(subs, init, lex, maxlen, seed, iters=ITERS, restarts=RESTARTS):
    codes = sorted(c for c in init if any(c in s for s in subs))
    best = None
    for r in range(restarts):
        rng = random.Random(seed * 1000 + r)
        st = State(subs, init, lex, maxlen)
        for it in range(iters):
            temp = T0 * (T1 / T0) ** (it / iters)
            if rng.random() < PSWAP:
                a, b = rng.sample(codes, 2)
                if st.key[a] == st.key[b]: continue
                ch = {a: st.key[b], b: st.key[a]}
            else:
                a = rng.choice(codes); ch = {a: rng.choice([l for l in ALPHA if l != st.key[a]])}
            d, new = st.propose(ch)
            if d <= 0 or rng.random() < math.exp(-d / temp): st.accept(ch, new, d)
        if best is None or st.total < best[0]: best = (st.total, dict(st.key))
    return best

def recovery(subs, key, ref):
    occ = [c for s in subs for c in s]
    return sum(key[c] == ref[c] for c in occ) / len(occ)

def perturb(key, frac, rng, codes):
    ch = rng.sample(codes, round(frac * len(codes))); out = dict(key)
    for c in ch: out[c] = rng.choice([l for l in ALPHA if l != key[c]])
    return out, ch

def setup():
    if OBJECTIVE == 'unigram':
        d, maxlen, oov = unigram_lexicon(); lex = (d, oov)
        print(f'unigram lexicon {len(d)} words, maxlen {maxlen}, OOV {oov:.3f} bits/char', flush=True)
    else:
        lex, maxlen = BS.lexicon()
    m = fr.load(); words = {w for w in m.words if len(w) >= 3}
    key_full = WS.load_key_full(os.path.join(T, 'key_full.tsv'))
    key_full = {c: v for c, v in key_full.items() if v in ALPHA}
    return lex, maxlen, words, key_full

def precheck():
    """SIG-4612 pre-check (PREREG-unigram.md): on the 5811 cut, key_full's cost must be <= the annealed optimum from a
    uniformly random key (seeds 1-3) and from unperturbed key_full (seed 0). Ties pass; any lower optimum fails."""
    lex, maxlen, words, kf = setup()
    runs = WS.load_runs(os.path.join(T, 'ciphertext_5811.tsv'), max_numerals=833)
    subs = subruns(runs, kf); codes = sorted(set(c for s in subs for c in s))
    kcost = State(subs, kf, lex, maxlen).total
    print(f'5811 cut: {sum(len(s) for s in subs)} keyed, {len(codes)} codes; key_full cost {kcost:.1f}', flush=True)
    inits = [('key_full', 0, kf)]
    for seed in (1, 2, 3):
        rng = random.Random(100 + seed); inits.append(('random', seed, {c: (rng.choice(ALPHA) if c in codes else v) for c, v in kf.items()}))
    from multiprocessing import Pool
    with Pool(4) as pool:
        outs = pool.starmap(anneal, [(subs, init, lex, maxlen, seed) for kind, seed, init in inits])
    res = {'objective': OBJECTIVE, 'key_full_cost': kcost, 'runs': []}
    for (kind, seed, init), (c, k) in zip(inits, outs):
        cw, tw = WS.word_share(runs, k, words)
        row = {'start': kind, 'seed': seed, 'start_recovery': recovery(subs, init, kf), 'cost': c,
               'recovery': recovery(subs, k, kf), 'word_share': cw / tw}
        res['runs'].append(row); print(row, flush=True)
    res['min_annealed_cost'] = min(r['cost'] for r in res['runs'])
    res['pass'] = kcost <= res['min_annealed_cost'] + 1e-9
    cw, tw = WS.word_share(runs, kf, words); res['key_full_word_share'] = cw / tw
    print(f'PRECHECK (key_full {kcost:.1f} <= min annealed {res["min_annealed_cost"]:.1f}): {"PASS" if res["pass"] else "FAIL"}')
    json.dump(res, open(os.path.join(HERE, suffix('precheck.json')), 'w'), indent=1)

def control():
    if OBJECTIVE == 'unigram' and not json.load(open(os.path.join(HERE, suffix('precheck.json'))))['pass']:
        sys.exit('PRECHECK FAILED: control not run (PREREG-unigram.md)')
    lex, maxlen, words, kf = setup()
    runs = WS.load_runs(os.path.join(T, 'ciphertext_5811.tsv'), max_numerals=833)
    subs = subruns(runs, kf)
    codes = sorted(set(c for s in subs for c in s))
    print(f'5811 cut: {sum(len(r) for r in runs)} numerals 1-120, {sum(len(s) for s in subs)} keyed, {len(codes)} distinct keyed codes')
    st0 = State(subs, kf, lex, maxlen); print(f'key_full seg cost {st0.total:.1f}')
    res = {'null': None, 'seeds': []}
    inits = [(0, kf, [])]
    for seed in (1, 2, 3):
        init, ch = perturb(kf, 0.20, random.Random(seed), codes); inits.append((seed, init, ch))
    from multiprocessing import Pool
    with Pool(4) as pool:
        outs = pool.starmap(anneal, [(subs, init, lex, maxlen, seed) for seed, init, ch in inits])
    for (seed, init, ch), (c, k) in zip(inits, outs):
        r0, r = recovery(subs, init, kf), recovery(subs, k, kf)
        fixed = sum(k[x] == kf[x] for x in ch); false = sum(k[x] != kf[x] for x in codes if x not in ch)
        cw, tw = WS.word_share(runs, k, words)
        row = {'seed': seed, 'start': r0, 'recovery': r, 'perturbed': len(ch), 'repaired': fixed,
               'false_moves': false, 'cost': c, 'word_share': cw / tw}
        print(('null start' if seed == 0 else f'seed {seed}') + f': perturbed {len(ch)}/{len(codes)}, start {r0:.3f} -> recovery {r:.3f}; '
              f'repaired {fixed}/{len(ch)}, false moves {false}; cost {c:.1f}; word share {cw/tw:.3f}', flush=True)
        if seed == 0: res['null'] = row
        else: res['seeds'].append(row)
    res['gate'] = all(s['recovery'] >= 0.90 for s in res['seeds'])
    cw, tw = WS.word_share(runs, kf, words); res['key_full_word_share'] = cw / tw
    print(f'GATE (each of 3 seeds recovery >= 0.90): {"PASS" if res["gate"] else "FAIL"}')
    json.dump(res, open(os.path.join(HERE, suffix('control.json')), 'w'), indent=1)

def target():
    ctl = json.load(open(os.path.join(HERE, suffix('control.json'))))
    if not ctl['gate']: sys.exit('CONTROL BELOW GATE: target not run (rule 3)')
    lex, maxlen, words, kf = setup()
    runs = WS.load_runs(os.path.join(T, 'ciphertext_4612_v3.tsv')); subs = subruns(runs, kf)
    codes = sorted(set(c for s in subs for c in s))
    out = {'seeds': [], 'shuffles': []}
    flat = [c for r in runs for c in r]; jobs = []
    for seed in (1, 2, 3): jobs.append(('real', seed, runs))
    for s in (1, 2, 3):
        rng = random.Random(4612 + s); sh = flat[:]; rng.shuffle(sh); it = iter(sh)
        jobs.append(('shuffle', s, [[next(it) for _ in r] for r in runs]))
    from multiprocessing import Pool
    with Pool(4) as pool:
        outs = pool.starmap(anneal, [(subruns(r, kf), kf, lex, maxlen, seed) for kind, seed, r in jobs])
    keys = []
    for (kind, seed, r), (c, k) in zip(jobs, outs):
        cw, tw = WS.word_share(r, k, words)
        row = {'seed': seed, 'cost': c, 'word_share': cw / tw, 'moved': sum(k[x] != kf[x] for x in codes if x in k)}
        if kind == 'real': keys.append(k); out['seeds'].append(row)
        else: out['shuffles'].append(row)
        print(kind, row, flush=True)
    ctl_share = sum(x['word_share'] for x in ctl['seeds']) / 3
    best = max(x['word_share'] for x in out['seeds']); shmax = max(x['word_share'] for x in out['shuffles'])
    out['reads'] = best > shmax and best >= 0.85 * ctl_share
    print(f'TARGET: best word share {best:.3f}; shuffle max {shmax:.3f}; 0.85 x control mean {0.85*ctl_share:.3f} -> {"READS" if out["reads"] else "does not read"}')
    with open(os.path.join(HERE, suffix('target_key_moves.tsv')), 'w') as f:
        f.write('code\tkey_full\tseed1\tseed2\tseed3\tall_agree\n')
        for x in codes:
            v = [k[x] for k in keys]
            if any(y != kf[x] for y in v): f.write(f'{x}\t{kf[x]}\t' + '\t'.join(v) + f'\t{int(len(set(v)) == 1)}\n')
    json.dump(out, open(os.path.join(HERE, suffix('target.json')), 'w'), indent=1)

if __name__ == '__main__':
    if '--objective' in sys.argv: OBJECTIVE = sys.argv[sys.argv.index('--objective') + 1]
    assert OBJECTIVE in ('seg', 'unigram')
    {'precheck': precheck, 'control': control, 'target': target}[sys.argv[1]]()
