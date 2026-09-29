#!/usr/bin/env python3
"""DEB-SWARM-C (29 Sept 2026): syllabic / mixed-unit decipherment tooling for the Debosnys swarm, group C.

Hypothesis family: each cipher sign stands for a French unit that is a syllable, a single letter or a short word
(a mixed system; several signs may share one unit, i.e. homophones). Everything here is CPU-only and reads public
files only (tools/data/fr19 corpus, the settled drafts). It never opens swarm/controls/sealed/ (score.py's job).

Pieces
  fold(), words(), syllabify()     accent-folded a-z words; orthographic French syllables (onset-maximal, with the
                                   inseparable clusters bl br ch cl cr dr fl fr gl gn gr ph pl pr qu th tr vr)
  tokenize(words, S, W)            the MIXED unit stream: a word among the top-W multi-syllable words -> one unit;
                                   else each syllable among the top-S syllables -> one unit; else spelled letter by
                                   letter. This is also the plant design of the hand-made controls (plant()).
  UnitLM                           unit bigram model, absolute discounting with unigram back-off, trained on the
                                   corpus tokenized with the same (S, W) as the solver hypothesises
  plant()                          a hand-planted control at a given N and K: held-out corpus window (Pierre et Jean is
                                   kept OUT of the LM), tokenized, units allotted to K signs by frequency (homophones for
                                   the frequent units, fair-share, as GOLD-D1's profile=target does), type noise p
  anneal()                         simulated annealing over sign -> unit, score = unit-bigram log-likelihood of the
                                   decoded stream (N fixed, so no length bias); moves: resample one sign's unit from
                                   the unigram, or swap two signs' units; restarts
  recovery()                       token accuracy on a planted control (share of cipher tokens whose decoded unit is
                                   the planted unit), and character accuracy of the decoded string
Run `python3 syll.py --help`.
"""
import argparse, collections, gzip, json, math, os, random, re, sys, time, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
FR19 = os.path.join(ROOT, 'tools', 'data', 'fr19')
LM_FILES = ['pg11049_Eugenie_Grandet.txt.gz', 'pg14155_Madame_Bovary.txt.gz', 'pg796_La_Chartreuse_de_Parme.txt.gz',
            'pg798_Le_rouge_et_le_noir.txt.gz']
HELD_OUT = 'pg11131_Pierre_et_Jean.txt.gz'
V = set('aeiouy')
INSEP = {'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gn', 'gr', 'ph', 'pl', 'pr', 'qu', 'th', 'tr', 'vr', 'gu'}


def fold(s):
    s = unicodedata.normalize('NFKD', s.lower().replace('œ', 'oe').replace('æ', 'ae'))
    return ''.join(c for c in s if not unicodedata.combining(c))


def strip_gutenberg(t):
    a = t.find('*** START'); b = t.find('*** END')
    if a >= 0:
        t = t[t.find('\n', a) + 1:]
    if b >= 0:
        t = t[:t.find('*** END')]
    return t


def words(fname):
    t = strip_gutenberg(gzip.open(os.path.join(FR19, fname), 'rt', encoding='utf-8', errors='ignore').read())
    return re.findall(r'[a-z]+', fold(t))


def syllabify(w):
    """Orthographic syllables: nuclei are vowel runs; between two nuclei one consonant goes right, an inseparable pair
    goes right, otherwise the last consonant (or last inseparable pair) goes right; trailing consonants stay on the
    last syllable; a word without a vowel is one unit."""
    nuc = [(m.start(), m.end()) for m in re.finditer(r'[aeiouy]+', w)]
    if not nuc:
        return [w]
    cuts = []
    for (a1, b1), (a2, b2) in zip(nuc, nuc[1:]):
        cl = w[b1:a2]
        if len(cl) <= 1:
            cuts.append(b1)
        elif cl[-2:] in INSEP:
            cuts.append(a2 - 2)
        else:
            cuts.append(a2 - 1)
    out, p = [], 0
    for c in cuts:
        out.append(w[p:c]); p = c
    out.append(w[p:])
    return [s for s in out if s]


# The harness's FR-SYLL unit rules (make_controls.py: FUNC list and syllabify(); design only -- the control's plaintext
# source and window were not read). Used when Tokenizer(..., func='harness').
FUNC_H = ['de', 'la', 'le', 'et', 'les', 'que', 'je', 'un', 'des', 'en', 'il', 'est', 'qui', 'pas', 'ne', 'mon', 'vous']


def syllabify_h(w):
    parts = re.findall(r'[^aeiouy]*[aeiouy]+(?:[^aeiouy]+$|[^aeiouy](?=[^aeiouy]))?', w)
    return parts if ''.join(parts) == w else [w]


class Tokenizer:
    def __init__(self, ws, S, W, func=False):
        """func=True: the W word units are the W most frequent words of any length (the harness FR-SYLL design,
        '17 function words'); else the W most frequent words of two or more syllables."""
        self.sy = syllabify_h if func == 'harness' else syllabify
        if func == 'harness':
            self.wrd = set(FUNC_H[:W])
            sc = collections.Counter(s for w in ws if w not in self.wrd for s in self.sy(w))
        else:
            sc = collections.Counter(s for w in ws for s in self.sy(w))
            wc = collections.Counter(w for w in ws if func or len(self.sy(w)) >= 2)
            self.wrd = set(w for w, _ in wc.most_common(W))
        self.S, self.W = S, W
        self.syl = set(s for s, _ in sc.most_common(S))
        self.cache = {}

    def word(self, w):
        r = self.cache.get(w)
        if r is None:
            if w in self.wrd:
                r = [w]
            else:
                r = []
                for s in self.sy(w):
                    r.extend([s] if s in self.syl else list(s))
            self.cache[w] = r
        return r

    def stream(self, ws):
        return [u for w in ws for u in self.word(w)]


class UnitLM:
    """Unit bigram, absolute discount d with unigram back-off (the unigram add-0.5 smoothed over the vocabulary)."""
    def __init__(self, units, d=0.75):
        self.uni = collections.Counter(units)
        self.vocab = sorted(self.uni)
        self.idx = {u: i for i, u in enumerate(self.vocab)}
        tot = sum(self.uni.values()) + 0.5 * len(self.vocab)
        self.lp_uni = [math.log((self.uni[u] + 0.5) / tot) for u in self.vocab]
        big = collections.Counter(zip(units, units[1:]))
        ctx = collections.Counter(units[:-1]); types = collections.Counter(a for a, b in big)
        self.bi = {}
        self.bo = {}
        for (a, b), c in big.items():
            ia, ib = self.idx[a], self.idx[b]
            self.bi[(ia, ib)] = (c - d) / ctx[a]
        for a in ctx:
            self.bo[self.idx[a]] = d * types[a] / ctx[a]
        self.puni = [math.exp(x) for x in self.lp_uni]
        self.cache = {}

    def lp(self, a, b):
        k = (a, b)
        r = self.cache.get(k)
        if r is None:
            r = math.log(self.bi.get(k, 0.0) + self.bo.get(a, 1.0) * self.puni[b])
            self.cache[k] = r
        return r


class UnitLM3(UnitLM):
    """Unit trigram on top of UnitLM's bigram: absolute discount d3, back-off to the bigram."""
    def __init__(self, units, d=0.75, d3=0.8):
        super().__init__(units, d)
        ix = [self.idx[u] for u in units]
        tri = collections.Counter(zip(ix, ix[1:], ix[2:]))
        ctx = collections.Counter(zip(ix, ix[1:-1])); types = collections.Counter((a, b) for a, b, c in tri)
        self.tri = {k: (c - d3) / ctx[k[:2]] for k, c in tri.items()}
        self.bo3 = {k: d3 * types[k] / ctx[k] for k in ctx}
        self.cache3 = {}

    def lp3(self, a, b, c):
        k = (a, b, c)
        r = self.cache3.get(k)
        if r is None:
            p2 = math.exp(self.lp(b, c))
            r = math.log(self.tri.get(k, 0.0) + self.bo3.get((a, b), 1.0) * p2)
            self.cache3[k] = r
        return r


def fair_share(counts, K):
    """Allot K signs to units (every unit present gets one; the rest go to whichever unit's count per sign is highest)."""
    units = [u for u, _ in counts.most_common()]
    if K < len(units):
        raise ValueError('K below unit count')
    alloc = {u: 1 for u in units}
    import heapq
    h = [(-counts[u], u) for u in units]; heapq.heapify(h)
    for _ in range(K - len(units)):
        c, u = heapq.heappop(h); alloc[u] += 1
        heapq.heappush(h, (-counts[u] / alloc[u], u))
    return alloc


def plant(N, K, S, W, noise=0.0, seed=1, ho_words=None, zipf=True, tok=None):
    """Hand-planted mixed-unit control: N tokens of the held-out novel, K signs. S and W are chosen by the caller (or by
    fit_SW) so that the unit type count sits below K; the remaining signs become homophones."""
    rng = random.Random(seed)
    ws = ho_words or words(HELD_OUT)
    tok = tok or Tokenizer(ws, S, W)
    start = rng.randrange(0, len(ws) - 5 * N)
    units, i = [], start
    while len(units) < N:
        units.extend(tok.word(ws[i])); i += 1
    units = units[:N]
    cnt = collections.Counter(units)
    alloc = fair_share(cnt, K or len(cnt))
    signs, sid = {}, 0
    for u in sorted(alloc, key=lambda x: -cnt[x]):
        signs[u] = list(range(sid, sid + alloc[u])); sid += alloc[u]
    cipher = []
    for u in units:
        opts = signs[u]
        if zipf and len(opts) > 1:
            wts = [1.0 / (j + 1) for j in range(len(opts))]
            cipher.append(rng.choices(opts, wts)[0])
        else:
            cipher.append(rng.choice(opts))
    truth = list(units)
    if noise > 0:
        freq = collections.Counter(cipher); pool = list(freq); wts = [freq[p] for p in pool]
        for j in range(N):
            if rng.random() < noise:
                cipher[j] = rng.choices(pool, wts)[0]
    return cipher, truth, dict(N=N, K_real=len(set(cipher)), unit_types=len(cnt), start=start, S=S, W=W)


class Solver:
    def __init__(self, lm):
        self.lm = lm
        vocab = lm.vocab
        # proposal: unit unigram, cumulative
        tot = sum(lm.uni.values())
        self.cum = []
        acc = 0
        for u in vocab:
            acc += lm.uni[u] / tot; self.cum.append(acc)

    def draw(self, rng):
        import bisect
        return min(bisect.bisect_left(self.cum, rng.random()), len(self.cum) - 1)

    def score(self, units, breaks=(), cipher=None):
        lm = self.lm; d = [lm.idx[u] for u in units]; tot = 0.0
        if cipher is not None:  # channel term, same convention as run()
            cs = collections.Counter(cipher); m = {}
            for c_, u_ in zip(cipher, units):
                m[c_] = u_
            Cu = collections.Counter()
            for c_, u_ in m.items():
                Cu[u_] += cs[c_]
            tot -= sum(v * math.log(v) for v in Cu.values() if v > 0)
        for j in range(1, len(d)):
            if j in breaks:
                continue
            if hasattr(lm, 'lp3') and j >= 2 and (j - 1) not in breaks:
                tot += lm.lp3(d[j - 2], d[j - 1], d[j])
            else:
                tot += lm.lp(d[j - 1], d[j])
        return tot

    def run(self, cipher, iters=200000, restarts=4, seed=1, T0=3.0, T1=0.05, fixed=None, init=None, breaks=None,
            injective=False, channel=True):
        """cipher: list of sign ids (hashable); breaks: set of positions i where the bigram (i-1,i) is cut (line or text
        breaks between separate texts). fixed: sign -> unit forced. Returns (best score, key sign->unit)."""
        lm = self.lm
        signs = sorted(set(cipher), key=str)
        pos = {s: [] for s in signs}
        for i, s in enumerate(cipher):
            pos[s].append(i)
        n = len(cipher)
        breaks = breaks or set()
        best = (-1e18, None)
        for r in range(restarts):
            rng = random.Random(seed * 1000 + r)
            if injective:  # one sign per unit: start from frequency-rank matching, jittered per restart
                sc_ = collections.Counter(cipher)
                order_s = sorted(signs, key=lambda x: (-sc_[x], rng.random()))
                order_u = sorted(range(len(lm.vocab)), key=lambda u: -lm.uni[lm.vocab[u]])
                if r > 0:
                    for _ in range(len(order_u) // 4):
                        a_, b_ = rng.randrange(len(order_u)), rng.randrange(len(order_u))
                        if abs(a_ - b_) < 8:
                            order_u[a_], order_u[b_] = order_u[b_], order_u[a_]
                key = dict(zip(order_s, order_u))
                used = set(key.values())
            else:
                key = {s: self.draw(rng) for s in signs}
            if init:
                key.update({s: lm.idx[u] for s, u in init.items() if u in lm.idx and s in key})
            if fixed:
                key.update({s: lm.idx[u] for s, u in fixed.items() if s in key})
            used = set(key.values())
            free = [s for s in signs if not fixed or s not in fixed]
            dec = [key[s] for s in cipher]
            # homophone channel term (MLE p(sign|unit)): - sum_u C_u log C_u (+ a constant); zero change when injective
            csig = collections.Counter(cipher)
            Cu = collections.Counter()
            for s_ in signs:
                Cu[key[s_]] += csig[s_]
            xl = lambda x: x * math.log(x) if x > 0 else 0.0

            tri = hasattr(lm, 'lp3')

            def bg(j):  # term j: log P(dec[j] | up to two previous units, cut at a break)
                if j < 1 or j >= n or j in breaks:
                    return 0.0
                if tri and j >= 2 and (j - 1) not in breaks:
                    return lm.lp3(dec[j - 2], dec[j - 1], dec[j])
                return lm.lp(dec[j - 1], dec[j])
            span = (0, 1, 2) if tri else (0, 1)
            cur = sum(bg(j) for j in range(n)) - (sum(xl(v) for v in Cu.values()) if channel else 0.0)
            for it in range(iters):
                T = T0 * (T1 / T0) ** (it / iters)
                if rng.random() < 0.8 or len(free) < 2:
                    s = rng.choice(free); new = self.draw(rng) if rng.random() < 0.7 else rng.randrange(len(lm.vocab))
                    if new == key[s] or (injective and new in used):
                        continue
                    js = set()
                    for i in pos[s]:
                        js.update(i + k for k in span)
                    old = sum(bg(j) for j in js)
                    oldv = key[s]
                    for i in pos[s]:
                        dec[i] = new
                    nw = sum(bg(j) for j in js)
                    d = nw - old
                    if channel:
                        c_ = csig[s]
                        d -= xl(Cu[oldv] - c_) - xl(Cu[oldv]) + xl(Cu[new] + c_) - xl(Cu[new])
                    if d >= 0 or rng.random() < math.exp(d / T):
                        if channel:
                            Cu[oldv] -= c_; Cu[new] += c_
                        if injective:
                            used.discard(key[s]); used.add(new)
                        key[s] = new; cur += d
                    else:
                        for i in pos[s]:
                            dec[i] = oldv
                else:
                    s1, s2 = rng.sample(free, 2)
                    if key[s1] == key[s2]:
                        continue
                    js = set()
                    for i in pos[s1] + pos[s2]:
                        js.update(i + k for k in span)
                    old = sum(bg(j) for j in js)
                    a, b = key[s1], key[s2]
                    for i in pos[s1]:
                        dec[i] = b
                    for i in pos[s2]:
                        dec[i] = a
                    nw = sum(bg(j) for j in js)
                    d = nw - old
                    if channel:
                        dc = csig[s2] - csig[s1]
                        d -= xl(Cu[a] + dc) - xl(Cu[a]) + xl(Cu[b] - dc) - xl(Cu[b])
                    if d >= 0 or rng.random() < math.exp(d / T):
                        if channel:
                            Cu[a] += dc; Cu[b] -= dc
                        key[s1], key[s2] = b, a; cur += d
                    else:
                        for i in pos[s1]:
                            dec[i] = a
                        for i in pos[s2]:
                            dec[i] = b
            if cur > best[0]:
                best = (cur, {s: lm.vocab[key[s]] for s in signs})
        return best


def recovery(cipher, truth, key):
    dec = [key.get(s) for s in cipher]
    tok = sum(d == t for d, t in zip(dec, truth)) / len(truth)
    a, b = ''.join(d or '?' for d in dec), ''.join(truth)
    # character accuracy by token-aligned comparison (a wrong-length unit counts all its truth letters wrong)
    ok = sum(len(t) for d, t in zip(dec, truth) if d == t)
    return tok, ok / len(b)


_LMCACHE = {}


def build_lm(S, W, d=0.75, order=2, func=False, verse=False):
    k = (S, W, d, order, func, verse)
    if k in _LMCACHE:
        return _LMCACHE[k]
    ws = []
    for f in LM_FILES:
        ws.extend(words(f))
    if verse:  # Baudelaire (tools/data/fr19v), not in the harness's control plaintexts (Hugo)
        global FR19
        keep = FR19; FR19 = os.path.join(ROOT, 'tools', 'data', 'fr19v')
        ws.extend(words('pg6099_Les_Fleurs_du_Mal.txt.gz') * 3); FR19 = keep
    tok = Tokenizer(ws, S, W, func)
    lm = (UnitLM3 if order == 3 else UnitLM)(tok.stream(ws), d)
    _LMCACHE[k] = (tok, lm)
    return tok, lm


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--plant', action='store_true', help='run the hand-planted control')
    ap.add_argument('--N', type=int, default=658)
    ap.add_argument('--K', type=int, default=124)
    ap.add_argument('--S', type=int, default=60, help='plant: syllables with own units')
    ap.add_argument('--W', type=int, default=10, help='plant: multi-syllable words with own units')
    ap.add_argument('--solveS', type=int, default=None)
    ap.add_argument('--solveW', type=int, default=None)
    ap.add_argument('--noise', type=float, default=0.0)
    ap.add_argument('--seeds', type=int, default=2)
    ap.add_argument('--iters', type=int, default=200000)
    ap.add_argument('--restarts', type=int, default=4)
    ap.add_argument('--oracle', type=float, default=0.0, help='give the solver this share of signs fixed to truth (crib power)')
    ap.add_argument('--order', type=int, default=2)
    ap.add_argument('--func', default='0', help='0, 1 (top-W words) or harness (FR-SYLL rules)')
    ap.add_argument('--inj', type=int, default=0)
    ap.add_argument('--verse', type=int, default=0)
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    sS = a.solveS if a.solveS is not None else a.S
    sW = a.solveW if a.solveW is not None else a.W
    t0 = time.time()
    tok, lm = build_lm(sS, sW, order=a.order, func=(a.func if a.func == 'harness' else a.func == '1'), verse=bool(a.verse))
    print(f'LM S={sS} W={sW} vocab={len(lm.vocab)} built {time.time()-t0:.0f}s', file=sys.stderr)
    ho = words(HELD_OUT)
    rows = []
    for seed in range(1, a.seeds + 1):
        cipher, truth, meta = plant(a.N, a.K, a.S, a.W, a.noise, seed, ho, tok=build_lm(a.S, a.W, order=a.order, func=(a.func if a.func == 'harness' else a.func == '1'), verse=bool(a.verse))[0])
        fixed = None
        if a.oracle > 0:
            rng = random.Random(seed + 77)
            sg = sorted(set(cipher)); rng.shuffle(sg)
            tmap = {}
            for c, t in zip(cipher, truth):
                tmap.setdefault(c, collections.Counter())[t] += 1
            fixed = {s: tmap[s].most_common(1)[0][0] for s in sg[:int(a.oracle * len(sg))]}
        sc, key = Solver(lm).run(cipher, a.iters, a.restarts, seed, fixed=fixed, injective=bool(a.inj))
        # truth score for reference: key = majority truth per sign
        tmap = {}
        for c, t in zip(cipher, truth):
            tmap.setdefault(c, collections.Counter())[t] += 1
        tkey = {s: c.most_common(1)[0][0] for s, c in tmap.items()}
        dec = [lm.idx.get(tkey[s]) for s in cipher]
        tsc = Solver(lm).score([tkey[s] for s in cipher], cipher=cipher) if None not in dec else None
        rec_tok, rec_chr = recovery(cipher, truth, key)
        row = dict(seed=seed, **meta, order=a.order, solveS=sS, solveW=sW, noise=a.noise, oracle=a.oracle, iters=a.iters,
                   restarts=a.restarts, found_score=round(sc, 1), truthkey_score=None if tsc is None else round(tsc, 1),
                   rec_token=round(rec_tok, 3), rec_char=round(rec_chr, 3))
        rows.append(row)
        print(json.dumps(row), flush=True)
    if a.out:
        json.dump(rows, open(a.out, 'w'), indent=1)


if __name__ == '__main__':
    main()
