#!/usr/bin/env python3
"""OBRED-CTRY (15 Oct 2026), PREREG obred187/PREREG-OBREDCTRY.md.

Context-scored every-occurrence test of OBRED-SEG's 20 word leads on no. 92 + the scan-187 postscript band intervals: a char 4-gram
lattice scorer (nl16 + the letter's clear prose) pins each lead's code->letter assignment at every other occurrence of the same codes
and asks whether the context still accepts it (d <= 3 bits per pinned token). Target vs a shuffled-band null (100 draws, seed 1605;
the null's own OBRED-SEG leads); synthetic control at e = 0.5 and 0.75 (20 sims each, seed 1600) that must show a right lead holds
(>= 0.60) and that holding raises precision by >= 0.10. Writes ctry_gate.json and ctry_leads.tsv beside this script; --check exits 1
if a regeneration differs. Grade M throughout unless the PREREG's S condition holds. Never key.tsv.
Run: python3 ciphers/oldenbarnevelt-brederode-1605/obred187/ctry/ctry.py [--check]
"""
import json, math, os, random, re, sys
from multiprocessing import Pool
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(T, 'obred187', 'seg'))
import seg as SG  # OBRED-SEG's decode(), lexicon(), words_of(), to_ivs(), constants; unchanged
B, ALPHA, fold = SG.B, SG.ALPHA, SG.fold

SYM = ALPHA + ' '
NS = len(SYM); SP = NS - 1
W = (0.1, 0.2, 0.3, 0.4)  # orders 1..4
IN, EDGE, ANY, TAU, CTX = 0.0, -3.0, -7.0, 3.0, 12
NEG = -1e9


def norm_text(s):
    out = []
    for ch in s.lower():
        ch = fold(ch)
        out.append(ch if ch in ALPHA else ' ')
    return re.sub(r' +', ' ', ''.join(out))


def clear_prose():
    lines = open(os.path.join(T, 'ciphertext.txt'), encoding='utf-8').read().split('\n')[17:73]
    t = ' '.join(l for l in lines if not l.startswith('==='))
    return norm_text(re.sub(r'\d+', ' ', t)).strip()


def counts(text):
    s = [SYM.index(c) for c in ' ' + norm_text(text).strip() + ' ']
    c4 = np.zeros((NS,) * 4, dtype=np.float64)
    a = np.array(s)
    if len(a) >= 4:
        np.add.at(c4, (a[:-3], a[1:-2], a[2:-1], a[3:]), 1)
    return c4


def base_counts(fids):
    c4 = np.zeros((NS,) * 4)
    for f in fids:
        c4 += counts(' '.join(SG.words_of(f)))
    return c4


def lm(c4):
    k = 0.1
    c3 = c4.sum(0); c2 = c3.sum(0); c1 = c2.sum(0)
    p4 = (c4 + k) / (c4.sum(3, keepdims=True) + k * NS)
    p3 = (c3 + k) / (c3.sum(2, keepdims=True) + k * NS)
    p2 = (c2 + k) / (c2.sum(1, keepdims=True) + k * NS)
    p1 = (c1 + k) / (c1.sum() + k * NS)
    P = W[3] * p4 + W[2] * p3[None] + W[1] * p2[None, None] + W[0] * p1[None, None, None]
    return np.log2(P).astype(np.float32)


def emis(iv, pin=None):
    e = np.full(NS, NEG, dtype=np.float32)
    if pin is not None:
        e[pin] = 0.0; return e
    lo, hi = iv
    for k in range(NS - 1):
        e[k] = IN if lo <= k <= hi else (EDGE if k in (lo - 1, hi + 1) else ANY)
    return e


def F(L, ivs, pre, suf, pins=None):
    """Best log2 score of a sub-run with pins {pos: letter index}."""
    pins = pins or {}
    p = [SYM.index(c) for c in ('   ' + pre)[-3:]]
    V = np.full((NS,) * 3, NEG, dtype=np.float32); V[p[0], p[1], p[2]] = 0.0
    n = len(ivs)
    for t in range(n):
        X = V[:, :, :, None] + L
        V = X.max(0) + emis(ivs[t], pins.get(t))[None, None, :]
        if t < n - 1:  # optional single space between tokens
            S = (V + L[:, :, :, SP]).max(0)  # state (a,b,c) -> (b,c,SP)
            Vs = np.full_like(V, NEG); Vs[:, :, SP] = S
            V = np.maximum(V, Vs)
    for ch in suf:
        c = SYM.index(ch)
        S = (V + L[:, :, :, c]).max(0)
        V = np.full_like(V, NEG); V[:, :, c] = S
    return float(V.max())


def test_lead(L, subs, cache, lead):
    """subs: list of (ivs, codes, pre, suf); lead: (s, i, j, word). Returns dict."""
    s0, i0, j0, w = lead
    codes = subs[s0][1]
    m = {}
    for k in range(i0, j0):
        c, l = codes[k], ALPHA.index(w[k - i0])
        if m.get(c, l) != l:
            return dict(testable=True, holds=False, conflict=True, occ=[])
        m[c] = l
    occ = []
    for s, (ivs, cds, pre, suf) in enumerate(subs):
        pins = {p: m[c] for p, c in enumerate(cds) if c in m and not (s == s0 and i0 <= p < j0)}
        if not pins:
            continue
        if s not in cache:
            cache[s] = F(L, ivs, pre, suf)
        d = cache[s] - F(L, ivs, pre, suf, pins)
        occ.append((s, sorted(pins), round(d, 3), d <= TAU * len(pins)))
    return dict(testable=bool(occ), holds=bool(occ) and all(o[3] for o in occ), conflict=False, occ=occ)


def self_score(L, subs, cache, lead):
    s0, i0, j0, w = lead
    ivs, cds, pre, suf = subs[s0]
    if s0 not in cache:
        cache[s0] = F(L, ivs, pre, suf)
    pins = {k: ALPHA.index(w[k - i0]) for k in range(i0, j0)}
    return (cache[s0] - F(L, ivs, pre, suf, pins)) / (j0 - i0)


def seg_leads(trie, subs):
    out = []
    for s, (ivs, *_rest) in enumerate(subs):
        for i, j, w, ne in SG.decode(ivs, trie):
            if w and len(w) >= SG.MINW:
                out.append((s, i, j, w))
    return out


# ---------------- target ----------------

def target_subs():
    st = json.load(open(os.path.join(T, 'obred187', 'structure.json')))
    subs = []
    for key in ('runs92', 'runs187'):
        for r in st[key]:
            parts, cur, starts_name = [], [], []
            vals = r['vals']
            seg_start = 0
            for idx, v in enumerate(vals):
                if B.NAME_LO <= v <= B.NAME_HI:
                    if cur: parts.append((seg_start, idx, cur)); cur = []
                    seg_start = idx + 1
                else:
                    cur.append(v)
            if cur: parts.append((seg_start, len(vals), cur))
            for a, b, codes in parts:
                pre = norm_text(r.get('before', ''))[-CTX:] if a == 0 else ' '
                pre = pre if pre.endswith(' ') else pre + ' '
                aft = '' if r.get('after', '(end)') == '(end)' else r['after']  # '(end)': no clear text follows
                suf = (' ' + norm_text(aft).strip())[:CTX + 1] if b == len(vals) else ' '
                subs.append([None, codes, pre, suf])
    return subs


def null_draw(args):
    k, = args
    rng = random.Random(1605 * 1000 + k)
    P = SG.pairs556(); pool = B.leaf_pairs(P, '555') + B.leaf_pairs(P, '556')
    codes = [c for c, _ in pool]; lets = [g for _, g in pool]; rng.shuffle(lets)
    subs = target_subs(); ivs = SG.to_ivs(list(zip(codes, lets)), [(0, 0, s[1]) for s in subs])
    for s, iv in zip(subs, ivs): s[0] = iv
    L = _G['Lt']; trie = _G['trie_t']; cache = {}
    res = [test_lead(L, subs, cache, ld) for ld in seg_leads(trie, subs)]
    t = [r for r in res if r['testable']]
    return dict(leads=len(res), testable=len(t), holds=sum(r['holds'] for r in t))


def rand_null(args):
    li, = args
    L = _G['Lt']; subs = _G['subs_t']; lead = _G['leads_t'][li]
    s0, i0, j0, w = lead
    rng = random.Random(187 * 100 + li); n = 0; cache = {}
    for _ in range(_G['RN']):
        m = {}
        for k in range(i0, j0):
            c = subs[s0][1][k]
            if c not in m:
                lo, hi = subs[s0][0][k]; m[c] = rng.randint(lo, hi)
        word = ''.join(ALPHA[m[subs[s0][1][k]]] for k in range(i0, j0))
        n += test_lead(L, subs, cache, (s0, i0, j0, word))['holds']
    return n / _G['RN']


# ---------------- control ----------------

def control_sim(args):
    e, sim = args
    rng = random.Random(1600 * 1000 + int(e * 100) * 100 + sim)
    held = _G['held']; seq = _G['seq']
    bands = B.synth_list(seq, rng)
    enc = lambda g: rng.choice(bands[g])
    pool = []
    for _ in range(41):
        g = rng.choice(seq); c = enc(g)
        if rng.random() < e:
            g = max(0, min(len(ALPHA) - 1, g + rng.choice((-1, 1))))
        pool.append((c, g))
    pool.sort()
    subs, truth, used = [], [], set()
    for Ln in _G['lens']:
        k0 = rng.randrange(50, len(held) - 250); k = k0; ws = []
        while sum(map(len, ws)) < Ln:
            ws.append(held[k]); k += 1
        codes = [enc(ALPHA.index(ch)) for w in ws for ch in w]
        pre = norm_text(' '.join(held[k0 - 4:k0]))[-CTX:] + ' '
        suf = (' ' + ' '.join(held[k:k + 4]))[:CTX + 1]
        subs.append([None, codes, pre, suf]); truth.append(ws)
        used.update(range(k0 - 40, k0)); used.update(range(k, k + 40)); used.difference_update(range(k0, k))
    ivs = SG.to_ivs(pool, [(0, 0, s[1]) for s in subs])
    for s, iv in zip(subs, ivs): s[0] = iv
    exc = [held[i] for i in sorted(used) if 0 <= i < len(held)][:_G['n_clear']]
    L = lm(_G['c4_ctrl'] + counts(' '.join(exc)))
    cache = {}; out = []
    for ld in seg_leads(_G['trie_c'], subs):
        s, i, j, w = ld
        spans, kk = {}, 0
        for tw in truth[s]:
            spans[(kk, kk + len(tw))] = tw; kk += len(tw)
        r = test_lead(L, subs, cache, ld)
        out.append(dict(right=spans.get((i, j)) == w, testable=r['testable'], holds=r['holds'], n=len(w)))
    hit = sum(lo <= ALPHA.index(ch) <= hi for s, ws in zip(subs, truth) for (lo, hi), ch in zip(s[0], ''.join(ws)))
    return out, hit, sum(len(s[1]) for s in subs)


_G = {}


def init_globals():
    files_c = [f for f in SG.FILES if f != SG.HELD]
    _G['trie_t'] = SG.lexicon(SG.FILES)
    _G['trie_c'] = SG.lexicon(files_c)
    prose = clear_prose()
    _G['n_clear'] = len(prose.split())
    _G['Lt'] = lm(base_counts(SG.FILES) + counts(prose))
    _G['c4_ctrl'] = base_counts(files_c)
    _G['held'] = SG.words_of(SG.HELD)
    _G['seq'] = [ALPHA.index(c) for w in _G['held'] for c in w]
    P = SG.pairs556(); pool = B.leaf_pairs(P, '555') + B.leaf_pairs(P, '556')
    subs = target_subs(); ivs = SG.to_ivs(pool, [(0, 0, s[1]) for s in subs])
    for s, iv in zip(subs, ivs): s[0] = iv
    _G['subs_t'] = subs
    _G['lens'] = [len(s[1]) for s in subs]
    leads = []
    for l in open(os.path.join(T, 'obred187', 'seg', 'seg_92_187.tsv')).read().strip().split('\n')[1:]:
        f = l.split('\t'); a, b = map(int, f[3].split('-'))
        leads.append((int(f[2]) - 1, a - 1, b, f[6]))
    _G['leads_t'] = leads
    _G['RN'] = 200


def p95(xs):
    xs = sorted(xs); return xs[int(0.95 * len(xs))] if xs else None


def build():
    init_globals()
    L, subs, leads = _G['Lt'], _G['subs_t'], _G['leads_t']
    # the 20 leads must be OBRED-SEG's own decode of these intervals
    assert seg_leads(_G['trie_t'], subs) == leads, 'leads differ from seg_92_187.tsv'
    cache = {}
    res = [test_lead(L, subs, cache, ld) for ld in leads]
    selfs = [self_score(L, subs, cache, ld) for ld in leads]
    with Pool(4) as pool:
        rn = pool.map(rand_null, [(i,) for i in range(len(leads))])
        nd = pool.map(null_draw, [(k,) for k in range(100)])
        ctrl = {}
        for e in (0.5, 0.75):
            sims = pool.map(control_sim, [(e, s) for s in range(20)])
            rows = [r for o, _, _ in sims for r in o]; hit = sum(h for _, h, _ in sims) / sum(n for _, _, n in sims)
            t = [r for r in rows if r['testable']]; h = [r for r in t if r['holds']]
            rt = [r for r in t if r['right']]; wt = [r for r in t if not r['right']]
            prec_t = sum(r['right'] for r in t) / max(1, len(t)); prec_h = sum(r['right'] for r in h) / max(1, len(h))
            rhold = sum(r['holds'] for r in rt) / max(1, len(rt)); whold = sum(r['holds'] for r in wt) / max(1, len(wt))
            ctrl[f'e{e}'] = dict(sims=20, interval_hit=hit, leads=len(rows), testable=len(t), holders=len(h),
                                 right_testable=len(rt), right_hold_rate=rhold, wrong_hold_rate=whold,
                                 precision_testable=prec_t, precision_holders=prec_h,
                                 precision_holders_len5=sum(r['right'] for r in h if r['n'] >= 5) / max(1, sum(r['n'] >= 5 for r in h)),
                                 gate=rhold >= 0.60 and prec_h >= prec_t + 0.10)
    ctrl['gate'] = 'PASS' if all(ctrl[k]['gate'] for k in ('e0.5', 'e0.75')) else 'BELOW GATE'
    t = [r for r in res if r['testable']]
    h_real = sum(r['holds'] for r in t) / max(1, len(t))
    hn = [d['holds'] / d['testable'] for d in nd if d['testable']]
    tgt = dict(leads=len(leads), testable=len(t), holders=sum(r['holds'] for r in t), h=h_real,
               null_draws=len(nd), null_defined=len(hn), null_mean=sum(hn) / max(1, len(hn)), null_p95=p95(hn),
               p=sum(x >= h_real for x in hn) / max(1, len(hn)),
               null_mean_leads=sum(d['leads'] for d in nd) / len(nd), null_mean_testable=sum(d['testable'] for d in nd) / len(nd))
    tgt['pass'] = tgt['null_p95'] is not None and h_real > tgt['null_p95']
    s_ok = ctrl['gate'] == 'PASS' and tgt['pass'] and ctrl['e0.75']['precision_holders'] >= 0.80
    rows = ['subrun\tspan\tcodes\tword\tself_bits_per_letter\ttestable\tresult\toccurrences(subrun:pos:d_bits)\trandom_assign_hold\tgrade']
    for ld, r, sf, q in zip(leads, res, selfs, rn):
        s, i, j, w = ld
        st = 'conflict' if r['conflict'] else ('untestable' if not r['testable'] else ('holds' if r['holds'] else 'breaks'))
        occ = ' '.join(f'{o[0] + 1}:{",".join(str(p + 1) for p in o[1])}:{o[2]}' for o in r['occ']) or '-'
        g = 'S' if (s_ok and r['holds'] and len(w) >= 5) else 'M'
        rows.append(f'{s + 1}\t{i + 1}-{j}\t{" ".join(map(str, subs[s][1][i:j]))}\t{w}\t{sf:.3f}\t{r["testable"]}\t{st}\t{occ}\t{q:.3f}\t{g}')
    out = dict(control=ctrl, target=tgt, S_condition=s_ok, tau_bits_per_pin=TAU,
               lm='char 4-gram, nl16 x5 + the letter clear prose (%d words), interp 0.4/0.3/0.2/0.1, add-0.1' % _G['n_clear'],
               emission=dict(inside=IN, edge=EDGE, other=ANY), context_chars=CTX)
    out = json.loads(json.dumps(out), parse_float=lambda x: round(float(x), 4))
    return json.dumps(out, indent=1, sort_keys=True) + '\n', '\n'.join(rows) + '\n'


def main():
    gate, rows = build()
    gp, rp = os.path.join(HERE, 'ctry_gate.json'), os.path.join(HERE, 'ctry_leads.tsv')
    if '--check' in sys.argv:
        bad = any((open(f).read() != s) if os.path.exists(f) else True for f, s in ((gp, gate), (rp, rows)))
        print('stale' if bad else 'up to date'); sys.exit(1 if bad else 0)
    open(gp, 'w').write(gate); open(rp, 'w').write(rows)
    print(gate); print(rows)


if __name__ == '__main__':
    main()
