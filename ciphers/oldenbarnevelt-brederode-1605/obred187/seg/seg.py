#!/usr/bin/env python3
"""OBRED-SEG (15 Oct 2026), PREREG obred187/PREREG-OBREDSEG.md.

Constrained segmentation of no. 92 + the scan-187 postscript band intervals (OBRED-BAND) into nl16 words: one DP decoder (lexicon word
cost -log10 p, edge-tolerance +1.0 per letter one step outside its interval, unknown letter 4.0), statistic I = sum of log2(23/width)
over tokens covered by lexicon words of length >= 4. Target vs shuffled-band (200, seed 1605) and order (200, seed 92) nulls; synthetic
control (20 sims, seed 1600, held-out nl16 file, e = 0 and 0.25). Writes seg_gate.json and seg_92_187.tsv beside this script; --check
exits 1 if a regeneration differs. Grade M throughout unless the PREREG's S condition holds.
Run: python3 ciphers/oldenbarnevelt-brederode-1605/obred187/seg/seg.py [--check]
"""
import gzip, json, math, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, '..', '..'))
ROOT = os.path.normpath(os.path.join(T, '..', '..'))
sys.path.insert(0, os.path.join(T, 'obred187', 'band'))
sys.path.insert(0, os.path.join(T, 'obred187', 'try'))
import band as B  # OBRED-BAND's interval(), leaf_pairs(), synth_list(), unchanged
from run_try import pairs556, fold, ALPHA

NA = len(ALPHA)
NL16 = os.path.join(ROOT, 'tools', 'data', 'nl16')
FILES = ('marn001bien01', 'marn001trou01', 'coor001zede01', 'spie001twes01', 'coor001boev01')
HELD = 'coor001boev01'
EDGE, UNK, MINW = 1.0, 4.0, 4


def words_of(fid):
    t = gzip.open(os.path.join(NL16, fid + '.txt.gz'), 'rt', encoding='utf-8', errors='ignore').read().lower()
    out = []
    for w in re.findall(r'[a-z]+', t):
        f = ''.join(fold(c) for c in w)
        if f and all(c in ALPHA for c in f):
            out.append(f)
    return out


def lexicon(fids):
    c = Counter()
    for f in fids:
        c.update(words_of(f))
    c = {w: n for w, n in c.items() if n >= 2}
    tot = sum(c.values())
    trie = {}
    for w, n in c.items():
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = -math.log10(n / tot)
    return trie


def decode(ivs, trie):
    """ivs: list of (lo, hi). Returns best path as list of (start, end, word or None, n_edge)."""
    n = len(ivs)
    best = [math.inf] * (n + 1); back = [None] * (n + 1); best[0] = 0.0
    for i in range(n):
        if best[i] == math.inf:
            continue
        # unknown letter
        c = best[i] + UNK
        if c < best[i + 1]:
            best[i + 1] = c; back[i + 1] = (i, None, 0)
        stack = [(trie, i, '', 0.0, 0)]
        while stack:
            node, j, pre, pen, ne = stack.pop()
            if '$' in node and j > i:
                c = best[i] + node['$'] + pen
                if c < best[j]:
                    best[j] = c; back[j] = (i, pre, ne)
            if j >= n:
                continue
            lo, hi = ivs[j]
            for ch, sub in node.items():
                if ch == '$':
                    continue
                k = ALPHA.index(ch)
                if lo <= k <= hi:
                    stack.append((sub, j + 1, pre + ch, pen, ne))
                elif k == lo - 1 or k == hi + 1:
                    stack.append((sub, j + 1, pre + ch, pen + EDGE, ne + 1))
    path, j = [], n
    while j > 0:
        i, w, ne = back[j]; path.append((i, j, w, ne)); j = i
    return path[::-1]


def stat(subruns, trie):
    """subruns: list of interval lists. Returns I and per-subrun paths."""
    I = 0.0; paths = []
    for ivs in subruns:
        p = decode(ivs, trie); paths.append(p)
        for i, j, w, ne in p:
            if w and len(w) >= MINW:
                for k in range(i, j):
                    lo, hi = ivs[k]
                    if lo <= ALPHA.index(w[k - i]) <= hi:
                        I += math.log2(NA / (hi - lo + 1))
    return I, paths


def target_subruns():
    st = json.load(open(os.path.join(T, 'obred187', 'structure.json')))
    subs = []
    for key, name in (('runs92', '92'), ('runs187', '187')):
        for r_i, r in enumerate(st[key], 1):
            cur = []
            for v in r['vals']:
                if B.NAME_LO <= v <= B.NAME_HI:
                    if cur: subs.append((name, r_i, cur)); cur = []
                else:
                    cur.append(v)
            if cur: subs.append((name, r_i, cur))
    return subs


def to_ivs(pool, subs):
    pool = sorted(pool)
    return [[B.interval(pool, v) for v in codes] for _, _, codes in subs]


def p95(xs):
    xs = sorted(xs); return xs[int(0.95 * len(xs))]


def target(trie, pool, subs, nd=200):
    real_ivs = to_ivs(pool, subs)
    I, paths = stat(real_ivs, trie)
    rng = random.Random(1605); codes = [c for c, _ in pool]; lets = [g for _, g in pool]; na = []
    for _ in range(nd):
        rng.shuffle(lets); na.append(stat(to_ivs(list(zip(codes, lets)), subs), trie)[0])
    rng = random.Random(92); flat = [iv for s in real_ivs for iv in s]; nb = []
    for _ in range(nd):
        rng.shuffle(flat); it = iter(flat)
        nb.append(stat([[next(it) for _ in s] for s in real_ivs], trie)[0])
    res = dict(I=I, nullA_mean=sum(na) / nd, nullA_p95=p95(na), pA=sum(x >= I for x in na) / nd,
               nullB_mean=sum(nb) / nd, nullB_p95=p95(nb), pB=sum(x >= I for x in nb) / nd, draws=nd)
    res['pass'] = I > res['nullA_p95'] and I > res['nullB_p95']
    return res, real_ivs, paths


def control(lens, sims=20, nd=50, seed=1600):
    trie = lexicon([f for f in FILES if f != HELD])
    held = words_of(HELD)
    seq = [ALPHA.index(c) for w in held for c in w]
    out = {}
    for e in (0.0, 0.25, 0.5, 0.75):  # 0.5/0.75: not registered, sensitivity to bracket the real hit rate (rule 3)
        rng = random.Random(seed)
        beat = 0; tp = fp = tp5 = fp5 = rec = tot_true = 0; hit = ntok = 0
        for _ in range(sims):
            bands = B.synth_list(seq, rng)
            enc = lambda g: rng.choice(bands[g])
            pool = []
            for _ in range(41):
                g = rng.choice(seq); c = enc(g)
                if rng.random() < e:
                    g = max(0, min(NA - 1, g + rng.choice((-1, 1))))
                pool.append((c, g))
            pool.sort()
            subs, truth = [], []
            for L in lens:
                k = rng.randrange(0, len(held) - 200); ws = []
                while sum(map(len, ws)) < L:
                    ws.append(held[k]); k += 1
                codes = [enc(ALPHA.index(ch)) for w in ws for ch in w]
                subs.append(('s', 0, codes)); truth.append(ws)
            ivs = to_ivs(pool, subs)
            for s_iv, ws in zip(ivs, truth):
                for (lo, hi), ch in zip(s_iv, ''.join(ws)):
                    hit += lo <= ALPHA.index(ch) <= hi; ntok += 1
            I, paths = stat(ivs, trie)
            codes_p = [c for c, _ in pool]; lets = [g for _, g in pool]; nul = []
            for _ in range(nd):
                rng.shuffle(lets); nul.append(stat(to_ivs(list(zip(codes_p, lets)), subs), trie)[0])
            beat += I > p95(nul)
            for p, ws in zip(paths, truth):
                spans, k = {}, 0
                for w in ws:
                    spans[(k, k + len(w))] = w; k += len(w)
                tw = {sp: w for sp, w in spans.items() if len(w) >= MINW}; tot_true += len(tw)
                for i, j, w, ne in p:
                    if w and len(w) >= MINW:
                        ok = spans.get((i, j)) == w
                        tp += ok; fp += not ok
                        if len(w) >= 5:
                            tp5 += ok; fp5 += not ok
                        rec += ok and (i, j) in tw
        out[f'e{e}'] = dict(sims=sims, null_draws=nd, beat_null_share=beat / sims,
                            precision=tp / max(1, tp + fp), n_recovered=tp + fp,
                            precision_len5=tp5 / max(1, tp5 + fp5), n_recovered_len5=tp5 + fp5,
                            recall=rec / max(1, tot_true), interval_hit=hit / max(1, ntok))
    c = out['e0.25']
    out['note'] = 'gate on e0.25 only (PREREG); e0.5/e0.75 added after the registered run, ungated, to bracket the real held-out hit 0.73-0.80'
    out['gate'] = 'PASS' if c['beat_null_share'] >= 0.70 and c['precision'] >= 0.50 else 'BELOW GATE'
    return out


def build():
    P = pairs556()
    pool = B.leaf_pairs(P, '555') + B.leaf_pairs(P, '556')
    subs = target_subruns()
    ctrl = control([len(c) for _, _, c in subs])
    trie = lexicon(FILES)
    tgt, ivs, paths = target(trie, pool, subs)
    s_ok = ctrl['gate'] == 'PASS' and tgt['pass'] and ctrl['e0.25']['precision_len5'] >= 0.80
    rows = ['text\trun\tsubrun\tspan\tcodes\tintervals\tword\tedge_letters\tgrade']
    words = []
    for n, ((t, r, codes), iv, p) in enumerate(zip(subs, ivs, paths), 1):
        for i, j, w, ne in p:
            if not w or len(w) < MINW:
                continue
            g = 'S' if (s_ok and len(w) >= 5) else 'M'
            rows.append(f'{t}\t{r}\t{n}\t{i + 1}-{j}\t{" ".join(map(str, codes[i:j]))}\t'
                        f'{" ".join(ALPHA[a:b + 1] for a, b in iv[i:j])}\t{w}\t{ne}\t{g}')
            words.append(w)
    res = dict(control=ctrl, target=tgt, subruns=len(subs), letter_tokens=sum(len(c) for _, _, c in subs),
               words_recovered=len(words), tokens_in_words=sum(map(len, words)),
               S_condition=s_ok, lexicon='nl16 (1569-1589 prose), >= 2 occurrences, folded',
               decoder=dict(edge=EDGE, unk=UNK, min_word=MINW))
    res = json.loads(json.dumps(res), parse_float=lambda x: round(float(x), 4))
    return json.dumps(res, indent=1, sort_keys=True) + '\n', '\n'.join(rows) + '\n'


def main():
    gate, rows = build()
    gp, rp = os.path.join(HERE, 'seg_gate.json'), os.path.join(HERE, 'seg_92_187.tsv')
    if '--check' in sys.argv:
        bad = any((open(f).read() != s) if os.path.exists(f) else True for f, s in ((gp, gate), (rp, rows)))
        print('stale' if bad else 'up to date'); sys.exit(1 if bad else 0)
    open(gp, 'w').write(gate); open(rp, 'w').write(rows)
    print(gate); print(rows)


if __name__ == '__main__':
    main()
