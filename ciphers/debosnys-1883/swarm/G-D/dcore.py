#!/usr/bin/env python3
"""DEB-SWARM-D core (29 Sept 2026): target loader, synthetic controls, and the order statistics of group D.

Group D's question: do c1 and c2 carry a readable language at all? Every statistic here is measured against the
text's OWN within-line shuffles (same signs, same counts, same line lengths, order destroyed), so the sign-frequency
curve cannot produce a signal by itself; only sequential order can. A language written in any sign-per-unit or
homophonic system keeps some order (letters/syllables have neighbours they prefer, words recur); iid meaningless
writing keeps none. The controls below are made at c1's and c2's own N, K, sign-count curve and line lengths.
Nothing here reads the harness's sealed controls."""
import os, sys, math, random, collections, gzip, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); DEB = os.path.dirname(os.path.dirname(HERE))
REPO = os.path.dirname(os.path.dirname(DEB))
sys.path.insert(0, os.path.join(DEB, 'scripts')); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}

def target(cid, drop_x=False):
    """Settled lines of c1 or c2, punctuation-class boxes and clear spans dropped (H43), optionally X dropped."""
    raw = settled_lines(DEB, cid, drop_clear=True)
    ls = [[s for s in v if s not in PUNCT and not (drop_x and s == 'X')] for v in raw.values()]
    return [l for l in ls if l]

# ---------------- corpora -----------------
def _clean(t):
    t = unicodedata.normalize('NFD', t.lower()); t = ''.join(c for c in t if not unicodedata.combining(c))
    return re.sub(r'[^a-z]+', ' ', t).split()
_CORP = {}
def words(lang):
    if lang in _CORP: return _CORP[lang]
    d = os.path.join(REPO, 'tools', 'data', {'fr': 'fr19', 'frv': 'fr19v', 'en': 'en', 'pt': 'pt18', 'la': 'la18'}[lang])
    txt = []
    for f in sorted(os.listdir(d)):
        p = os.path.join(d, f)
        if f.endswith('.txt.gz'): txt.append(gzip.open(p, 'rt', errors='ignore').read())
        elif f.endswith('.txt') and f != 'LICENSE-gutenberg.txt': txt.append(open(p, errors='ignore').read())
    w = []
    for t in txt:
        n = len(t); w += _clean(t[n // 20: n - n // 20])  # trim licence boilerplate at both ends
    _CORP[lang] = w; return w

V = set('aeiouy')
def syllables(w):
    return re.findall(r'[^aeiouy]*[aeiouy]+(?:[^aeiouy]+$|[^aeiouy](?=[^aeiouy]))?', w) or [w]

def units(lang, n, rng, kind):
    """n plaintext units from a random window: letters, or FR-SYLL style (frequent syllables as units, the rest spelled)."""
    W = words(lang)
    while True:
        o = rng.randrange(len(W) - 4 * n); out = []
        for w in W[o:]:
            if kind == 'letters': out += list(w)
            else: out += syllables(w)
            if len(out) >= n: return out[:n]

# ---------------- encoders -----------------
def alloc(units_seq, curve, rng, common=None):
    """Homophonic key matched to the target's sign-count curve (fair-share greedy, as GOLD-D1 profile=target):
    buckets in descending size go to the unit furthest below its own share; every unit gets at least one bucket
    if the curve is long enough. Returns unit -> [(sign, weight)]."""
    N = len(units_seq); f = collections.Counter(units_seq); us = [u for u, _ in f.most_common()]
    K = len(curve); key = collections.defaultdict(list); got = collections.Counter()
    reserve = min(len(us), K); big = curve[:K - reserve] if K > reserve else []
    small = curve[K - reserve:]
    # rarest units get the smallest reserved buckets
    for u, c in zip(us, small): key[u].append([c, c]); got[u] += c
    for c in big:
        u = max(us[:K], key=lambda u: f[u] - got[u] * N / sum(curve)); key[u].append([c, c]); got[u] += c * N / sum(curve)
    units_without = [u for u in us if u not in key]
    return key, units_without

def encode(useq, curve, rng):
    key, missing = alloc(useq, curve, rng)
    signs = {}; nid = 0; out = []
    for u in key:
        for b in key[u]: signs[id(b)] = f'S{nid}'; nid += 1
    for u in useq:
        if u not in key:  # a unit with no bucket (curve shorter than inventory): borrow the nearest-sized unit's key
            u = rng.choice(list(key))
        bs = key[u]; b = rng.choices(bs, [x[1] for x in bs])[0]; out.append(signs[id(b)])
    return out

def noise(seq, p, rng, fresh=0.5):
    cnt = collections.Counter(seq); ids = list(cnt); w = [cnt[i] for i in ids]; out = []; k = 0
    for s in seq:
        if rng.random() < p:
            if rng.random() < fresh: out.append(f'N{k}'); k += 1
            else: out.append(rng.choices(ids, w)[0])
        else: out.append(s)
    return out

def cut(seq, lens):
    out = []; j = 0
    for n in lens: out.append(seq[j:j + n]); j += n
    return out

def make(design, lens, curve, rng, p=0.15):
    """design: FR-HOMO EN-HOMO PT-HOMO FRV-HOMO LA-HOMO FR-SYLL | NULL-IID NULL-HABIT NULL-AVOID"""
    N = sum(lens)
    if design.startswith('NULL'):
        signs = [f'S{i}' for i in range(len(curve))]
        if design == 'NULL-IID':
            seq = rng.choices(signs, curve, k=N)
        elif design == 'NULL-HABIT':
            # a writer with habits: each sign has 1-2 favourite successors taken with prob 0.25, else iid
            fav = {s: rng.choices(signs, curve, k=2) for s in signs}; seq = [rng.choices(signs, curve)[0]]
            while len(seq) < N:
                seq.append(rng.choice(fav[seq[-1]]) if rng.random() < 0.25 else rng.choices(signs, curve)[0])
        elif design == 'NULL-AVOID':
            # a writer avoiding recent signs (no sign repeated within the last 3), otherwise frequency-weighted
            seq = []
            while len(seq) < N:
                s = rng.choices(signs, curve)[0]
                if s in seq[-3:] and rng.random() < 0.9: continue
                seq.append(s)
        return cut(noise(seq, p, rng) if p else seq, lens)
    lang = {'FR': 'fr', 'EN': 'en', 'PT': 'pt', 'FRV': 'frv', 'LA': 'la'}[design.split('-')[0]]
    kind = 'syll' if design.endswith('SYLL') else 'letters'
    u = units(lang, N, rng, kind); seq = encode(u, curve, rng)
    return cut(noise(seq, p, rng) if p else seq, lens)

# ---------------- statistics -----------------
def _mi(lines, d):
    bg = collections.Counter(); L = collections.Counter(); R = collections.Counter()
    for l in lines:
        for a, b in zip(l, l[d:]): bg[(a, b)] += 1; L[a] += 1; R[b] += 1
    n = sum(bg.values())
    if not n: return 0.0, bg
    return sum(c / n * math.log2(c * n / (L[a] * R[b])) for (a, b), c in bg.items()), bg

def raw_stats(lines):
    mi1, bg = _mi(lines, 1); mi2, _ = _mi(lines, 2); mi3, _ = _mi(lines, 3)
    tri = collections.Counter(tuple(l[i:i + 3]) for l in lines for i in range(len(l) - 2))
    dbl = sum(1 for l in lines for a, b in zip(l, l[1:]) if a == b)
    return dict(mi1=mi1, mi2=mi2, mi3=mi3, bg2=sum(1 for c in bg.values() if c >= 2),
                bgmax=max(bg.values()) if bg else 0, rep3=sum(1 for c in tri.values() if c >= 2), dbl=dbl)

def zstats(lines, rng, trials=200):
    obs = raw_stats(lines); sh = collections.defaultdict(list)
    for _ in range(trials):
        s = []
        for l in lines: c = l[:]; rng.shuffle(c); s.append(c)
        for k, v in raw_stats(s).items(): sh[k].append(v)
    out = {}
    for k, v in obs.items():
        m = sum(sh[k]) / trials; sd = (sum((x - m) ** 2 for x in sh[k]) / trials) ** 0.5
        out[k] = dict(obs=round(v, 4), z=round((v - m) / sd, 2) if sd > 0 else 0.0, p_ge=round(sum(x >= v for x in sh[k]) / trials, 4))
    return out

def transfer(fit_lines, test_lines, alpha=0.5):
    """Held-out order transfer: bits/token gained on test by a bigram model fitted on the other text over a unigram
    model fitted on the same text (both add-alpha over the joint inventory). Positive = the order seen in one text
    predicts the other. Compare with the same number after shuffling the fit text within lines."""
    V = {s for l in fit_lines + test_lines for s in l}; nV = len(V)
    uni = collections.Counter(s for l in fit_lines for s in l); nu = sum(uni.values())
    bg = collections.Counter((a, b) for l in fit_lines for a, b in zip(l, l[1:])); ctx = collections.Counter(a for l in fit_lines for a in l[:-1])
    gain = 0.0; n = 0
    for l in test_lines:
        for a, b in zip(l, l[1:]):
            pu = (uni[b] + alpha) / (nu + alpha * nV)
            # interpolated bigram: back off to the unigram
            lam = ctx[a] / (ctx[a] + 5.0)
            pb = lam * (bg[(a, b)] / ctx[a] if ctx[a] else 0) + (1 - lam) * pu
            gain += math.log2(pb / pu); n += 1
    return gain / n if n else 0.0

def transfer_z(fit, test, rng, trials=200):
    obs = transfer(fit, test); sh = []
    for _ in range(trials):
        s = []
        for l in fit: c = l[:]; rng.shuffle(c); s.append(c)
        sh.append(transfer(s, test))
    m = sum(sh) / trials; sd = (sum((x - m) ** 2 for x in sh) / trials) ** 0.5
    return dict(obs=round(obs, 5), z=round((obs - m) / sd, 2) if sd else 0.0, p_ge=round(sum(x >= obs for x in sh) / trials, 4))

def curve_of(lines):
    return sorted(collections.Counter(s for l in lines for s in l).values(), reverse=True)

# ---------------- paired controls (one key or one writer for both texts) -----------------
def make_pair(design, lens1, lens2, curve, rng, p=0.15, xnull=0.0):
    """A c1-shaped and a c2-shaped text made with ONE key (language) or ONE writing process (null), from two separate
    plaintext windows, then type noise p (half fresh ids). xnull: share of an extra null sign 'XN' inserted at random
    (the X-as-null model of H39), applied before cutting so N stays the target's."""
    N1, N2 = sum(lens1), sum(lens2)
    if design.startswith('NULL'):
        a = [s for l in make(design, [N1 + N2], curve, rng, 0.0) for s in l]
        s1, s2 = a[:N1], a[N1:]
    else:
        lang = {'FR': 'fr', 'EN': 'en', 'PT': 'pt', 'FRV': 'frv', 'LA': 'la'}[design.split('-')[0]]
        kind = 'syll' if design.endswith('SYLL') else 'letters'
        u1 = units(lang, N1, rng, kind); u2 = units(lang, N2, rng, kind)
        key, _ = alloc(u1 + u2, curve, rng); names = {}; k = 0
        for u in key:
            for b in key[u]: names[id(b)] = f'S{k}'; k += 1
        def enc(us):
            o = []
            for u in us:
                if u not in key: u = rng.choice(list(key))
                b = rng.choices(key[u], [x[1] for x in key[u]])[0]; o.append(names[id(b)])
            return o
        s1, s2 = enc(u1), enc(u2)
    def fin(s):
        if xnull: s = ['XN' if rng.random() < xnull else x for x in s]
        return noise(s, p, rng) if p else s
    return cut(fin(s1), lens1), cut(fin(s2), lens2)

FEATS = ('mi1', 'bg2', 'rep3', 'dbl')
def features(t1, t2, rng, trials=100):
    z1 = zstats(t1, rng, trials); z2 = zstats(t2, rng, trials)
    x21 = transfer_z(t2, t1, rng, trials); x12 = transfer_z(t1, t2, rng, trials)
    f = {f'c1_{k}': z1[k]['z'] for k in z1}; f.update({f'c2_{k}': z2[k]['z'] for k in z2})
    f['x21'] = x21['z']; f['x12'] = x12['z']
    return f

def score(f, which):
    """The frozen language score (written before the blind set was made): order in the direction language pushes it.
    which = 'c1', 'c2' or 'pair' (c1 + c2 + both transfer z)."""
    def one(c): return f[f'{c}_mi1'] + f[f'{c}_bg2'] + f[f'{c}_rep3'] - f[f'{c}_dbl']
    if which == 'pair': return one('c1') + one('c2') + f['x21'] + f['x12']
    return one(which)
