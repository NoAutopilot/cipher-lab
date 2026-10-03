#!/usr/bin/env python3
"""Consistency search: f.205v/f.207r numeral passage against Rousseau's f.206r slip (NAF 14913).

FT4-naf14913-rousseau-venice-1743 (account-4), 3 Oct 2026. Companion to tools/interlinear_align.py, which from a flat
start on this single long pair only spreads letters evenly (logged in NOTES.md): with one pair, the only evidence is
that a code repeated in the cipher must take the same plain chunk at every occurrence. This script enumerates every
segmentation of the slip's letters into the 62 groups in which (a) every group takes 1..MAXLEN letters and (b) every
repeated group takes the identical chunk each time, and reports the distinct value->chunk maps for the repeated groups.
Free groups between two repeated occurrences are not split (their stretch is reported whole).

Per-unit control (CLAUDE.md rule 3, pairing shuffle): the same search on N shuffles of the group order (same multiset,
same plain text). The statistic -- does a fully consistent map exist, and how many -- depends on where the repeats
fall, so a shuffle can change it (not a non-test). Pass: real has >=1 consistent map and the shuffle rate of >=1 map
is below 5%.

  python3 consistency_search.py [--shuffles 1000] [--maxlen 9] [--seed 1]
"""
import argparse, os, random, re, sys, time, unicodedata
from multiprocessing import Pool
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)


def load():
    toks = []
    for l in open(os.path.join(TARGET, 'ciphertext.txt'), encoding='utf-8'):
        if l.startswith('#'):
            continue
        toks += [t.split('?')[0] for t in l.split()]
    plain = [l for l in open(os.path.join(TARGET, 'slip_f206r.txt'), encoding='utf-8') if not l.startswith('#')][0]
    p = unicodedata.normalize('NFKD', plain.lower())
    letters = re.sub(r'[^a-z]', '', p)
    words = re.findall(r'[a-z]+', re.sub(r"[^a-z ]", ' ', p.replace("'", ' ')))
    bounds = set()
    pos = 0
    for w in words:
        bounds.add(pos); pos += len(w); bounds.add(pos)
    return toks, letters, bounds


def feasible(toks, text, maxlen, amap):
    """Reachable-positions DP: can the groups cover text exactly, with every group in amap taking its fixed chunk
    and every other group (repeated-but-unassigned ones included, a relaxation) taking 1..maxlen letters?"""
    L = len(text)
    reach = {0}
    for t in toks:
        nxt = set()
        s = amap.get(t)
        for p in reach:
            if s is not None:
                if text.startswith(s, p):
                    nxt.add(p + len(s))
            else:
                nxt.update(range(p + 1, min(p + maxlen, L) + 1))
        reach = nxt
        if not reach:
            return False
    return L in reach


def nonoverlap_count(text, s):
    c = i = 0
    while True:
        i = text.find(s, i)
        if i < 0: return c
        c += 1; i += len(s)


def search(toks, text, maxlen, cap=10000, deadline=None):
    """Branch-and-bound over chunk assignments to the repeated values. Statistic S = letters carried by repeated
    groups (sum over occurrences of chunk length) in the best fully consistent assignment. Returns (S, best maps)."""
    cnt = Counter(toks)
    rep = sorted((t for t, c in cnt.items() if c > 1), key=lambda t: (-cnt[t], toks.index(t)))
    subs = {text[i:i + l] for l in range(1, maxlen + 1) for i in range(len(text) - l + 1)}
    cands = {}
    for t in rep:
        cs = [s for s in subs if nonoverlap_count(text, s) >= cnt[t] and feasible(toks, text, maxlen, {t: s})]
        cands[t] = sorted(cs, key=lambda s: (-len(s), s))
    if any(not cands[t] for t in rep):
        return -1, []
    ub = {t: cnt[t] * len(cands[t][0]) for t in rep}
    best = [-1, []]

    class Timeout(Exception):
        pass

    def rec(j, amap, cur):
        if deadline and time.time() > deadline:
            raise Timeout
        if j == len(rep):
            if cur > best[0]: best[0], best[1] = cur, [dict(amap)]
            elif cur == best[0] and len(best[1]) < cap: best[1].append(dict(amap))
            return
        if cur + sum(ub[t] for t in rep[j:]) < best[0]:
            return
        t = rep[j]
        for s in cands[t]:
            if cur + cnt[t] * len(s) + sum(ub[u] for u in rep[j + 1:]) < best[0]:
                break
            amap[t] = s
            if feasible(toks, text, maxlen, amap):
                rec(j + 1, amap, cur + cnt[t] * len(s))
            del amap[t]

    try:
        rec(0, {}, 0)
    except Timeout:
        return None, best[1]
    return best[0], best[1]


def distinct_maps(sols, rep):
    return {tuple(sorted(m.items())): None for m, _ in sols}


def _one(job):
    s, text, maxlen, limit = job
    return search(s, text, maxlen, 1, time.time() + limit)[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shuffles', type=int, default=200)
    ap.add_argument('--maxlen', type=int, default=6)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--cap', type=int, default=20)
    ap.add_argument('--limit', type=float, default=3.0, help='seconds per shuffle')
    a = ap.parse_args()
    toks, text, bounds = load()
    print(f'groups {len(toks)}, distinct {len(set(toks))}, plain letters {len(text)}, maxlen {a.maxlen}')
    S, maps = search(toks, text, a.maxlen, a.cap)
    print(f'REAL: S = {S} letters carried by repeated groups; {len(maps)} best map(s)')
    for m in maps[:a.cap]:
        print('  map:', ' '.join(f'{t}={s}' for t, s in sorted(m.items(), key=lambda x: int(x[0]))))
    rng = random.Random(a.seed)
    jobs = []
    for _ in range(a.shuffles):
        s = toks[:]
        rng.shuffle(s)
        jobs.append((s, text, a.maxlen, a.limit))
    with Pool(4) as pool:
        raw = pool.map(_one, jobs)
    to = sum(1 for x in raw if x is None)
    done = sorted(x for x in raw if x is not None and x >= 0)
    print(f'completed feasible shuffles: {len(done)}, S values {done}')
    sh = [S if x is None else x for x in raw]   # a timed-out shuffle counts as >= real (conservative)
    print(f'shuffles timed out at {a.limit}s (counted as >= real): {to}; infeasible (no consistent map, S=-1): '
          f'{sum(1 for x in raw if x == -1)}')
    if sh:
        sh.sort()
        p95 = sh[int(0.95 * len(sh)) - 1]
        ge = sum(1 for x in sh if x >= S)
        print(f'SHUFFLE (pairing shuffle, group order, n={len(sh)}): mean {sum(sh)/len(sh):.1f}, p95 {p95}, max {sh[-1]}; '
              f'shuffles >= real: {ge} (p = {(ge + 1) / (len(sh) + 1):.4f})')
        ok = S > p95
        print('GATE', 'PASS' if ok else 'FAIL', '(real S above shuffle p95)')
        return 0 if ok else 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
