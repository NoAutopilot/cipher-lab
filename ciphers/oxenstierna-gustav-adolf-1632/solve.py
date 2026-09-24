#!/usr/bin/env python3
"""W1 solver with matched control (LANE R worker R3, 24 Sept 2026).

Design inferred from ciphertext_verified.tsv (see NOTES.md "Design"): numerals <=100 are letter
symbols (homophonic, 59 values, 694 tokens), numerals >100 are nomenclator codes (30 values, 39
tokens), printed letter-signs (SYM: r rr nn ...) are unknown signs. Cipher runs sit inside Swedish
clear text with no word divisions.

Solver: simulated annealing over value->letter maps (at most MAX_HOMO values per letter), scored by
the interpolated letter 4-gram model of tools/subst_hillclimb.py (24 letters, i=j, u=v; a/ä/å, o/ö
folded), with the clear words on both sides of every run fixed as context. Codes and SYM break the
stream. Language model: the djvu text of the same volume (Styffe, Rikskansleren Axel Oxenstiernas
skrifter och brefvexling II:1), with the target letter (602) and the control letter (604) removed.

Control: letter 604 (Gustav Adolf to Oxenstierna, 1 Aug 1632, own hand, Swedish with Latin) laid onto
the target's exact token layout (same clear-word slots, same number of letter tokens per run, one
code token per code slot), enciphered with a homophonic key whose value frequencies copy the target's
rank-frequency profile (59 letter values, same homophone spread), then solved blind.

    python3 solve.py control [--seeds 3]      control accuracy + score
    python3 solve.py target  [--seeds 3]      target best key, score, shuffled null
Needs sources/ia-fulltext/rikskanslerenax00styfgoog_djvu.txt (gitignored; re-fetch URL in extract.py).
"""
import argparse, csv, json, math, os, random, re, sys
from collections import Counter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from subst_hillclimb import Model, ALPHA, IDX, A  # noqa: E402

DJVU = os.path.join(ROOT, 'sources/ia-fulltext/rikskanslerenax00styfgoog_djvu.txt')
TARGET_LINES = (39871, 39947)
CONTROL_LINES = (39983, 40322)   # letter 604 body
MAX_HOMO = 6


def fold(s):
    s = s.lower()
    for a, b in (('å', 'a'), ('ä', 'a'), ('æ', 'a'), ('ö', 'o'), ('ø', 'o'), ('ü', 'u'), ('ß', 'ss'), ('j', 'i'), ('v', 'u')):
        s = s.replace(a, b)
    return ''.join(c for c in s if c in IDX)


def djvu():
    return open(DJVU, encoding='utf-8', errors='replace').read().split('\n')


def model():
    L = djvu()
    keep = [l for i, l in enumerate(L, 1)
            if not (TARGET_LINES[0] <= i <= TARGET_LINES[1] or CONTROL_LINES[0] <= i <= CONTROL_LINES[1])]
    return Model([fold('\n'.join(keep))])


def target_stream():
    """List of items: ('C', word) clear, ('L', value) letter symbol, ('B', raw) break (code or SYM)."""
    out = []
    for r in csv.DictReader(open(os.path.join(HERE, 'ciphertext_verified.tsv'), encoding='utf-8'), delimiter='\t'):
        if r['class'] == 'CLEAR':
            out.append(('C', r['value']))
        elif r['class'] == 'NUM' and int(r['value']) <= 100:
            out.append(('L', r['value'] + r['mark'].replace('"', "''")))
        else:
            out.append(('B', r['raw']))
    return out


def frags_of(stream):
    """Fragments of symbols; clear letters become fixed symbols '=x'. Split at breaks."""
    frags, cur = [], []
    for kind, v in stream:
        if kind == 'B':
            if cur:
                frags.append(cur); cur = []
        elif kind == 'C':
            cur += ['=' + c for c in fold(v)]
        else:
            cur.append(v)
    if cur:
        frags.append(cur)
    # keep only fragments that contain cipher symbols; trim clear context to 12 letters each side
    out = []
    for f in frags:
        idx = [i for i, t in enumerate(f) if not t.startswith('=')]
        if not idx:
            continue
        out.append(f[max(0, idx[0] - 12): idx[-1] + 13])
    return out


class Problem:
    def __init__(self, frags, m):
        self.m = m
        self.syms = sorted({t for f in frags for t in f if not t.startswith('=')})
        self.sidx = {s: i for i, s in enumerate(self.syms)}
        n = len(self.syms)
        # encode: cipher symbol i -> i; clear letter x -> n + IDX[x]
        seq, starts = [], []
        for f in frags:
            starts.append(len(seq))
            seq += [self.sidx[t] if not t.startswith('=') else n + IDX[t[1]] for t in f]
        self.seq = np.array(seq, dtype=np.int64)
        valid = np.ones(len(seq), dtype=bool)
        for s in starts:
            valid[s:s + 3] = False  # quad windows ending at positions >= start+3 inside a fragment
        ends = starts[1:] + [len(seq)]
        self.q_end = np.array([i for s, e in zip(starts, ends) for i in range(s + 3, e)], dtype=np.int64)
        self.heads = np.array(starts, dtype=np.int64)
        self.n = n
        self.ntok = int((self.seq < n).sum())
        self.counts = Counter(t for f in frags for t in f if not t.startswith('='))

    def score(self, key):
        full = np.concatenate([key, np.arange(A)])
        d = full[self.seq]
        e = self.q_end
        m = self.m
        s = m.quad[d[e - 3], d[e - 2], d[e - 1], d[e]].sum()
        h = self.heads
        s += m.uni[d[h]].sum() + m.bi[d[h], d[h + 1]].sum() + m.tri[d[h], d[h + 1], d[h + 2]].sum()
        return s

    def _windows(self):
        if hasattr(self, '_win'):
            return
        e = self.q_end
        W = np.stack([self.seq[e - 3], self.seq[e - 2], self.seq[e - 1], self.seq[e]], axis=1)
        self._W = W
        self._win = [np.where((W == i).any(axis=1))[0] for i in range(self.n)]
        self._q = self.m.quad.reshape(-1)

    def _wscore(self, full, idx):
        W = full[self._W[idx]]
        return self._q[((W[:, 0] * A + W[:, 1]) * A + W[:, 2]) * A + W[:, 3]].sum()

    def anneal(self, seed, iters=60000, t0=3.0, t1=0.05):
        """Annealing with incremental 4-gram scoring (heads are scored only in the final total)."""
        self._windows()
        rng = random.Random(seed)
        n = self.n
        uni = np.exp(self.m.uni * math.log(10))
        order = sorted(range(n), key=lambda i: -self.counts[self.syms[i]])
        lorder = list(np.argsort(-uni))
        full = np.concatenate([np.zeros(n, dtype=np.int64), np.arange(A)])
        for r, i in enumerate(order):
            full[i] = lorder[min(len(lorder) - 1, int(abs(rng.gauss(r * 0.4, 2))))] if rng.random() < 0.8 else rng.randrange(A)
        cnt = np.bincount(full[:n], minlength=A)
        while cnt.max() > MAX_HOMO:
            i = rng.choice([j for j in range(n) if cnt[full[j]] > MAX_HOMO])
            cnt[full[i]] -= 1; full[i] = int(np.argmin(cnt)); cnt[full[i]] += 1
        allw = np.arange(len(self._W))
        cur = self._wscore(full, allw); best, bfull = cur, full.copy()
        for it in range(iters):
            T = t0 * (t1 / t0) ** (it / iters)
            if rng.random() < 0.8:
                i = rng.randrange(n); v = rng.randrange(A); old = full[i]
                if v == old or cnt[v] >= MAX_HOMO:
                    continue
                idx = self._win[i]
                before = self._wscore(full, idx); full[i] = v; after = self._wscore(full, idx)
                d = after - before
                if d >= 0 or rng.random() < math.exp(d / T):
                    cur += d; cnt[old] -= 1; cnt[v] += 1
                else:
                    full[i] = old
            else:
                i, j = rng.sample(range(n), 2)
                if full[i] == full[j]:
                    continue
                idx = np.union1d(self._win[i], self._win[j])
                before = self._wscore(full, idx); full[i], full[j] = full[j], full[i]; after = self._wscore(full, idx)
                d = after - before
                if d >= 0 or rng.random() < math.exp(d / T):
                    cur += d
                else:
                    full[i], full[j] = full[j], full[i]
            if cur > best + 1e-9:
                best, bfull = cur, full.copy()
        full = bfull.copy(); cnt = np.bincount(full[:n], minlength=A); cur = self._wscore(full, allw)
        improved = True
        while improved:
            improved = False
            for i in range(n):
                for v in range(A):
                    old = full[i]
                    if v == old or cnt[v] >= MAX_HOMO:
                        continue
                    idx = self._win[i]
                    before = self._wscore(full, idx); full[i] = v; d = self._wscore(full, idx) - before
                    if d > 1e-9:
                        cur += d; cnt[old] -= 1; cnt[v] += 1; improved = True
                    else:
                        full[i] = old
        key = full[:n].copy()
        return self.score(key) / self.ntok, key

    def keymap(self, key):
        return {s: ALPHA[key[i]] for s, i in self.sidx.items()}


def render(stream, km):
    out = []
    for kind, v in stream:
        if kind == 'C':
            out.append(v)
        elif kind == 'B':
            out.append('[' + v + ']')
        else:
            out.append(km.get(v, '?').upper())
    # join consecutive letters
    s, prev = '', None
    for kind_v, tok in zip(stream, out):
        if kind_v[0] == 'L' and prev == 'L':
            s += tok
        else:
            s += (' ' if s else '') + tok
        prev = kind_v[0]
    return s


def control_stream(tstream, seed=7):
    """Lay letter 604 onto the target's token layout and encipher with a rank-matched homophonic key."""
    rng = random.Random(seed)
    L = djvu()[CONTROL_LINES[0] - 1: CONTROL_LINES[1]]
    words = [w for l in L if not re.fullmatch(r'\s*\d+\s*', l) for w in l.split()]
    words = [w for w in words if fold(w)]
    wi = 0
    plain = []           # list of (kind, value, plaintext letter or word)
    i = 0
    while i < len(tstream):
        kind, v = tstream[i]
        if kind == 'C':
            plain.append(('C', words[wi], None)); wi += 1; i += 1
        elif kind == 'B':
            plain.append(('B', 'code', fold(words[wi]))); wi += 1; i += 1
        else:
            j = i
            while j < len(tstream) and tstream[j][0] == 'L':
                j += 1
            need = j - i
            letters = ''
            while len(letters) < need:
                letters += fold(words[wi]); wi += 1
            for c in letters[:need]:   # the last word may be cut: the run length is kept exact
                plain.append(('L', None, c))
            i = j
    # rank-matched key: target value counts sorted, assigned to letters greedily by remaining mass
    tcounts = sorted(Counter(v for k, v in tstream if k == 'L').values(), reverse=True)
    pl = Counter(c for k, _, c in plain if k == 'L')
    remaining = dict(pl)
    homos = {c: [] for c in pl}
    for idx, cnt in enumerate(tcounts):
        c = max(remaining, key=lambda x: (remaining[x], -len(homos[x])))
        if len(homos[c]) >= MAX_HOMO:
            c = max((x for x in remaining if len(homos[x]) < MAX_HOMO), key=lambda x: remaining[x])
        homos[c].append((f'v{idx:02d}', cnt)); remaining[c] -= cnt
    for c in homos:
        if not homos[c]:
            raise SystemExit(f'letter {c} got no value')
    stream, truth = [], []
    for k, v, c in plain:
        if k == 'L':
            vals, w = zip(*homos[c])
            sym = rng.choices(vals, weights=w)[0]
            stream.append(('L', sym)); truth.append(c)
        elif k == 'B':
            stream.append(('B', v))
        else:
            stream.append(('C', v))
    return stream, truth, homos


def shuffled(stream, seed):
    rng = random.Random(seed)
    vals = [v for k, v in stream if k == 'L']
    rng.shuffle(vals)
    it = iter(vals)
    return [(k, next(it)) if k == 'L' else (k, v) for k, v in stream]


_P = None


def _anneal(seed, iters):
    return _P.anneal(seed, iters)


def run(stream, m, seeds, iters):
    P = Problem(frags_of(stream), m)
    from multiprocessing import Pool
    global _P
    _P = P
    with Pool(min(4, seeds)) as pool:
        res = pool.starmap(_anneal, [(s, iters) for s in range(seeds)])
    sc, key = max(res, key=lambda t: t[0])
    return P, sc, key, [r[0] for r in res]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('what', choices=['control', 'target'])
    ap.add_argument('--seeds', type=int, default=3)
    ap.add_argument('--iters', type=int, default=60000)
    ap.add_argument('--out')
    a = ap.parse_args()
    m = model()
    ts = target_stream()
    report = {}
    if a.what == 'control':
        cs, truth, homos = control_stream(ts)
        P, sc, key, all_sc = run(cs, m, a.seeds, a.iters)
        km = P.keymap(key)
        dec = [km[v] for k, v in cs if k == 'L']
        acc = sum(x == y for x, y in zip(dec, truth)) / len(truth)
        true_km = {s: c for c in homos for s, _ in homos[c]}
        true_sc = P.score(np.array([IDX[true_km[s]] for s in P.syms])) / P.ntok
        Ps, ssc, _, _ = run(shuffled(cs, 1), m, a.seeds, a.iters)
        report = dict(control_letter_tokens=len(truth), control_values=len(true_km), accuracy=round(acc, 4),
                      solver_score=round(sc, 4), true_key_score=round(true_sc, 4), shuffled_null=round(ssc, 4),
                      restart_scores=[round(x, 4) for x in all_sc], reading=render(cs, km)[:1500])
    else:
        P, sc, key, all_sc = run(ts, m, a.seeds, a.iters)
        km = P.keymap(key)
        Ps, ssc, _, _ = run(shuffled(ts, 1), m, a.seeds, a.iters)
        report = dict(target_letter_tokens=P.ntok, values=P.n, solver_score=round(sc, 4), shuffled_null=round(ssc, 4),
                      restart_scores=[round(x, 4) for x in all_sc], key=km, reading=render(ts, km))
    print(json.dumps(report, indent=1, ensure_ascii=False))
    if a.out:
        json.dump(report, open(a.out, 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
