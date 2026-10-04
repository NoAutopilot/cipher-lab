#!/usr/bin/env python3
"""Score the f.206 key on a new cipher+slip pair from NAF 14913 under FT4b's pre-registered gate (NOTES.md, 3 Oct 2026).

FT4c-naf14913-rousseau-venice-1743 (account-4), 3 Oct 2026. Written and committed before the f.216v/f.217r
transcription was scored. Extends align/consistency_search.py (same exact-coverage model) to a pair given on the
command line, with FT4's ten C-graded codes as pins.

Statistic H (as registered): the number of pinned C-code occurrences in the best fully consistent exact-coverage
segmentation of the slip's letters into the passage's groups. A pinned code is pinned per code, not per occurrence
(every occurrence takes its f.206 value or the code is left free); every other repeated code, a C code left free
included, takes one identical chunk at each of its occurrences; every free group takes 1..MAXLEN letters. H is the
largest sum of occurrences over a set of pinned codes for which such a segmentation exists (0 if none).
Search: pin sets in order of decreasing H, each first checked by the relaxed DP (repeats unconstrained), then by a
depth-first existence search over chunk assignments for the free repeated codes, with a time limit per run. A run
whose search times out on a pin set is treated conservatively: for a control it counts as reaching that pin set's H
(>= real), for the real pair it counts as not reaching it.

Controls (as registered): (a) value permutation, the ten f.206 values deranged among the ten codes, 200;
(b) pairing shuffle, the passage's group order shuffled, the same pins, 200. Gate: H >= 5 AND H > p95(a) AND
H > p95(b); fewer than 5 occurrences of the ten codes in the passage = non-test.
MAXLEN (fixed before scoring, FT4c): 12, since the f.217r slip has words of up to 11 letters (considerant) and a
nomenclator word group must be able to carry one; FT4 used 9 for a slip whose longest word group was 7.

  python3 gate_pair.py --cipher ../ciphertext_f216v.txt --slip ../slip_f217r.txt [--n 200] [--limit 20] [--seed 1]

--coverage (A3V2-ROUS, 4 Oct 2026, account 3): a passage that has NO plain side (no Rousseau slip, no interlinear gloss --
ff.165r-165v and ff.197v-198r) cannot be scored by the registered gate at all: H needs a slip to segment, so the registered
gate is a NON-TEST (no plain side), not a FAIL, and this mode says so first. It then reports what a cipher-only passage can
say: occurrences of the ten C codes, of every key.tsv code, and of 338/534/722, and one unregistered secondary statistic,
K = occurrences of key.tsv codes in the passage, against two controls that can vary on the same axis (rule 3): (a) N groups
drawn uniformly from 1..--range (default 850, the volume's code range), (b) N groups drawn uniformly from the distinct codes
of the other transcribed NAF 14913 passages (--vocab files), so a K above both p95 says only that key.tsv's codes are
high-frequency codes of the same nomenclator -- consistent with the same key, never a test of its values. No key change
can follow from this mode (NOTES.md "Pre-registered gate": values enter key.tsv only from a pair that PASSes).

  python3 gate_pair.py --cipher ../ciphertext_f165.txt --coverage [--vocab ../ciphertext.txt ...] [--n 200] [--seed 1]
"""
import argparse, itertools, os, random, re, sys, time, unicodedata
from collections import Counter
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)

PINS = {'22': 'de', '66': 'r', '279': 'plus', '581': 'au', '722': 'ti', '501': 'et',
        '31': 'lareine', '628': 'hongrie', '172': 'quils', '379': 'interets'}


def letters(s):
    return re.sub(r'[^a-z]', '', unicodedata.normalize('NFKD', s.lower()))


def load(cipher, slip):
    toks = []
    for l in open(cipher, encoding='utf-8'):
        l = l.split('#')[0]
        toks += [t.split('|')[0].split('?')[0] for t in l.split()[1:] if t[0].isdigit()] if l[:1] == 'L' else \
                [t.split('|')[0].split('?')[0] for t in l.split() if t[0].isdigit()]
    text = letters(' '.join(l for l in open(slip, encoding='utf-8') if not l.startswith('#')))
    return toks, text


class Scorer:
    def __init__(self, text, maxlen):
        self.text, self.L, self.maxlen = text, len(text), maxlen
        self.full = (1 << (self.L + 1)) - 1
        self.starts = {}

    def smask(self, s):
        m = self.starts.get(s)
        if m is None:
            m = 0
            i = self.text.find(s)
            while i >= 0:
                m |= 1 << i
                i = self.text.find(s, i + 1)
            self.starts[s] = m
        return m

    def feasible(self, toks, amap):
        reach = 1
        for t in toks:
            s = amap.get(t)
            if s is not None:
                reach = ((reach & self.smask(s)) << len(s)) & self.full
            else:
                nxt = 0
                for k in range(1, self.maxlen + 1):
                    nxt |= reach << k
                reach = nxt & self.full
            if not reach:
                return False
        return bool(reach >> self.L & 1)

    def consistent(self, toks, pinmap, deadline):
        """True / False / None (timed out): a segmentation with pinmap fixed and every free repeated code consistent."""
        if not self.feasible(toks, pinmap):
            return False
        cnt = Counter(toks)
        rep = [t for t, c in cnt.items() if c > 1 and t not in pinmap]
        rep.sort(key=lambda t: -cnt[t])
        text, ml = self.text, self.maxlen
        subs = {text[i:i + l] for l in range(1, ml + 1) for i in range(len(text) - l + 1)}
        cands = {}
        for t in rep:
            cs = []
            for s in subs:
                if bin(self.smask(s)).count('1') >= cnt[t] and self.feasible(toks, dict(pinmap, **{t: s})):
                    cs.append(s)
                if time.time() > deadline:
                    return None
            if not cs:
                return False
            cands[t] = sorted(cs, key=lambda s: (len(s), s))
        rep.sort(key=lambda t: len(cands[t]))
        amap = dict(pinmap)

        def rec(j):
            if time.time() > deadline:
                raise TimeoutError
            if j == len(rep):
                return True
            t = rep[j]
            for s in cands[t]:
                amap[t] = s
                if self.feasible(toks, amap) and rec(j + 1):
                    return True
                del amap[t]
            return False
        try:
            return rec(0)
        except TimeoutError:
            return None

    def H(self, toks, pins, limit, conservative_high):
        cnt = Counter(toks)
        present = [c for c in pins if c in cnt]
        subsets = []
        for r in range(len(present), 0, -1):
            for sub in itertools.combinations(present, r):
                subsets.append((sum(cnt[c] for c in sub), sub))
        subsets.sort(key=lambda x: -x[0])
        deadline = time.time() + limit
        for h, sub in subsets:
            pm = {c: pins[c] for c in sub}
            if not self.feasible(toks, pm):
                continue
            ok = self.consistent(toks, pm, deadline)
            if ok:
                return h, pm, False
            if ok is None:
                if conservative_high:
                    return h, pm, True
                deadline = time.time() + limit  # real: a timed-out pin set counts as not reached; go on
        ok = self.consistent(toks, {}, time.time() + limit)
        return 0, {}, ok is None


def derangements(keys, rng):
    while True:
        p = keys[:]
        rng.shuffle(p)
        if all(a != b for a, b in zip(keys, p)):
            return p


def _job(args):
    toks, text, maxlen, pins, limit = args
    h, _, to = Scorer(text, maxlen).H(toks, pins, limit, True)
    return h, to


def load_cipher(cipher):
    return load(cipher, os.devnull)[0]


def coverage(a):
    toks = load_cipher(a.cipher)
    cnt = Counter(toks)
    key = {}
    for l in open(a.key, encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if f[0] == 'code' or not f[0].strip():
            continue
        key[f[0]] = (f[1], f[2])
    print(f'groups {len(toks)}, distinct {len(cnt)}; registered gate: NON-TEST (no plain side: H undefined without a slip)')
    occ = sum(cnt[c] for c in PINS)
    print('C-code occurrences in passage:', {c: cnt[c] for c in PINS if c in cnt}, 'total', occ)
    print('338/534/722:', {c: cnt.get(c, 0) for c in ('338', '534', '722')})
    hits = {c: cnt[c] for c in key if c in cnt}
    K = sum(hits.values())
    print(f'key.tsv codes present: {len(hits)} of {len(key)}, occurrences K = {K} of {len(toks)} groups '
          f'({100.0 * K / len(toks):.1f}%)')
    for c in sorted(hits, key=lambda c: -hits[c]):
        print(f'  {c}\t{key[c][0]}\t{key[c][1]}\tx{hits[c]}')
    print('repeated codes:', {t: c for t, c in cnt.items() if c > 1})
    rng = random.Random(a.seed)
    vocab = set()
    for f in a.vocab:
        vocab |= set(load_cipher(f))
    keyset = set(key)
    res = {}
    draws = [('a uniform 1..%d' % a.range, lambda: str(rng.randint(1, a.range)))]
    if vocab:
        vl = sorted(vocab)
        draws.append(('b vocabulary of %d other-passage codes (%d files)' % (len(vl), len(a.vocab)), lambda: rng.choice(vl)))
    for name, draw in draws:
        ks = sorted(sum(1 for _ in range(len(toks)) if draw() in keyset) for _ in range(a.n))
        p95 = ks[int(0.95 * len(ks)) - 1]
        ge = sum(1 for k in ks if k >= K)
        print(f'CONTROL ({name}, n={len(ks)}): mean {sum(ks)/len(ks):.2f}, p95 {p95}, max {ks[-1]}, '
              f'>= real {ge} (p = {(ge+1)/(len(ks)+1):.4f})')
        res[name] = p95
    above = all(K > p for p in res.values())
    print('SECONDARY (unregistered, vocabulary-level, no key change can follow):', 'K above both p95' if above else
          'K not above every control p95', f'(K={K}, p95s {res})')
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cipher', required=True)
    ap.add_argument('--slip', help='clear text of the passage (a Rousseau slip); required unless --coverage')
    ap.add_argument('--coverage', action='store_true', help='no plain side: registered gate NON-TEST; cipher-only counts + secondary K')
    ap.add_argument('--vocab', nargs='*', default=[], help='other transcribed passages (control b vocabulary)')
    ap.add_argument('--range', type=int, default=850, help='code range for control (a), 1..range')
    ap.add_argument('--key', default=os.path.join(TARGET, 'key.tsv'))
    ap.add_argument('--maxlen', type=int, default=12)
    ap.add_argument('--n', type=int, default=200)
    ap.add_argument('--limit', type=float, default=20.0, help='seconds per run (per pin set for the real pair)')
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    if a.coverage:
        return coverage(a)
    if not a.slip:
        ap.error('--slip is required unless --coverage')
    toks, text = load(a.cipher, a.slip)
    cnt = Counter(toks)
    occ = sum(cnt[c] for c in PINS)
    print(f'groups {len(toks)}, distinct {len(cnt)}, slip letters {len(text)}, maxlen {a.maxlen}')
    print('C-code occurrences in passage:', {c: cnt[c] for c in PINS if c in cnt}, 'total', occ)
    print('repeated codes:', {t: c for t, c in cnt.items() if c > 1})
    if occ < 5:
        print('NON-TEST: fewer than 5 occurrences of the ten C codes (power floor, as registered)')
        return 4
    sc = Scorer(text, a.maxlen)
    H, pm, to = sc.H(toks, PINS, a.limit * 3, False)
    print(f'REAL: H = {H}; pinned set {pm}; timeouts on higher pin sets: {to}')
    rng = random.Random(a.seed)
    keys = list(PINS)
    jobs_a = []
    for _ in range(a.n):
        p = derangements(keys, rng)
        jobs_a.append((toks, text, a.maxlen, {k: PINS[v] for k, v in zip(keys, p)}, a.limit))
    jobs_b = []
    for _ in range(a.n):
        s = toks[:]
        rng.shuffle(s)
        jobs_b.append((s, text, a.maxlen, PINS, a.limit))
    res = {}
    with Pool(4) as pool:
        for name, jobs in (('a value permutation', jobs_a), ('b pairing shuffle', jobs_b)):
            raw = pool.map(_job, jobs)
            hs = sorted(h for h, _ in raw)
            p95 = hs[int(0.95 * len(hs)) - 1]
            ge = sum(1 for h in hs if h >= H)
            print(f'CONTROL ({name}, n={len(hs)}): mean {sum(hs)/len(hs):.2f}, p95 {p95}, max {hs[-1]}, '
                  f'timeouts (counted high) {sum(1 for _, t in raw if t)}, >= real {ge} (p = {(ge+1)/(len(hs)+1):.4f})')
            print('  H distribution:', sorted(Counter(hs).items()))
            res[name] = p95
    ok = H >= 5 and all(H > p for p in res.values())
    print('GATE', 'PASS' if ok else 'FAIL', f'(H={H} >= 5 and > p95 of both controls: {res})')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
