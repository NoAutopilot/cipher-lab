#!/usr/bin/env python3
"""Word-placement (dictionary-constrained) search for the 1653 syllabic table (F5160-WORD, LANE DEFAULT-account-4-20261009-1340,
9 Oct 2026). Pre-registered in PREREG-F5160-WORD.md.

The score is tools/nomenclator_anneal.py's Problem, unchanged (order-5 model, prior, caps). Only the search differs: half
the moves place a whole French word from the fr17 lexicon over a window of k = 1..6 consecutive cipher tokens, split into
k values the design allows; the other half are nomenclator_anneal.anneal's own single-sign / swap moves. Why a private
script: tools/family_run.py builds its own control and cannot score against control_pool.truth.json, and its wordcode
family has no syllable values (see PREREG-F5160-WORD.md).

  python3 word_solve.py FILE --model fr_model.npz --fix S8=de ... --iters N --restarts 4 --seed 7 --out result.json
  python3 word_solve.py FILE ... --time 20000        timing run only (prints iterations/s, no score, no output file)
Evaluate with: python3 ../../tools/nomenclator_anneal.py eval result.json control_pool.truth.json
"""
import argparse, glob, gzip, json, math, os, random, re, sys, time
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(H, '..', '..', 'tools')
sys.path.insert(0, T)
import italian_ngram as ing
import nomenclator_anneal as na

DESIGN_WORDS = 'que les des uous pour roi nous auec mais dans estre point monsieur sa son il'.split()


def lexicon(n=4000, mincount=3):
    c = Counter()
    for fn in sorted(glob.glob(os.path.join(T, 'data', 'fr17', '*.txt.gz'))):
        txt = re.sub(r'-\s*\n\s*', '', gzip.open(fn, 'rt', encoding='utf-8', errors='replace').read())
        for line in txt.splitlines():
            for w in ing.norm(line).split('#'):
                if w:
                    c[w] += 1
    words = [(w, k) for w, k in c.most_common() if k >= mincount and (len(w) >= 2 or w in ('a', 'y'))]
    return words[:n]


def splits(word, allowed, maxk=6, cap=40):
    """All ways to write word as k pieces from allowed values, k <= maxk (at most cap per k)."""
    out = defaultdict(list)
    def rec(i, acc):
        if len(acc) > maxk:
            return
        if i == len(word):
            if len(out[len(acc)]) < cap:
                out[len(acc)].append(tuple(acc))
            return
        for j in range(min(len(word), i + 9), i, -1):
            p = word[i:j]
            if p in allowed:
                rec(j, acc + [p])
    rec(0, [])
    return out


def build_buckets(pb, lex, caps):
    allowed = {v for i, v in enumerate(pb.values) if pb.vkind[i] in 'lsw'}
    buckets = defaultdict(lambda: ([], []))
    for w, cnt in lex:
        for k, segs in splits(w, allowed).items():
            for seg in segs:
                buckets[k][0].append(tuple(pb.vid[p] for p in seg))
                buckets[k][1].append(math.sqrt(cnt) / len(segs))
    out = {}
    for k, (segs, wts) in buckets.items():
        cum, s = [], 0.0
        for x in wts:
            s += x
            cum.append(s)
        out[k] = (segs, cum)
    return out


def windows(pb):
    """Cipher runs as lists of stream positions (each a sign token)."""
    runs = []
    for name, lay in pb.layout:
        for kind, x in lay:
            if kind == 'c' and x:
                runs.append(x)
    return runs


def anneal(pb, rng, iters, T0, T1, caps, fixed, buckets, runs, p_word=0.5):
    n = pb.nsign
    lvals = pb.byk['l']
    key = [pb.vid[rng.choice(na.FREQ_LETTERS[:12])] for _ in range(n)]
    for s, v in fixed.items():
        key[s] = v
    mutable = [s for s in range(n) if s not in fixed]
    wts = [math.sqrt(pb.counts[pb.signs[s]]) for s in mutable]
    flat = [(ri, j) for ri, r in enumerate(runs) for j in range(len(r))]
    vk = pb.vkind

    def kinds_ok(k):
        c = Counter(vk[v] for v in k)
        if c['s'] > caps['syl'] or c['w'] > caps['word'] or c['n'] > caps['null']:
            return False
        if caps['homo']:
            lc = Counter(v for v in k if vk[v] == 'l')
            if lc and max(lc.values()) > caps['homo']:
                return False
        return True

    cur = pb.score(key)
    best, bestkey = cur, key[:]
    acc_w = tried_w = 0
    for it in range(iters):
        Tm = T0 * (T1 / T0) ** (it / max(1, iters - 1))
        changes = None
        if rng.random() < p_word:
            ri, j = rng.choice(flat)
            r = runs[ri]
            k = rng.randint(1, 6)
            if j + k > len(r) or k not in buckets:
                continue
            segs, cum = buckets[k]
            seg = segs[rng.choices(range(len(segs)), cum_weights=cum)[0]]
            want = {}
            ok = True
            for pos, v in zip(r[j:j + k], seg):
                s = pb.sidx_of(pos)
                if want.get(s, v) != v or (s in fixed and fixed[s] != v):
                    ok = False
                    break
                want[s] = v
            if not ok:
                continue
            changes = [(s, key[s]) for s, v in want.items() if key[s] != v]
            if not changes:
                continue
            for s, v in want.items():
                key[s] = v
            if not kinds_ok(key):
                for s, o in changes:
                    key[s] = o
                continue
            tried_w += 1
        else:
            s = rng.choices(mutable, wts)[0]
            old = key[s]
            if rng.random() < 0.3:
                s2 = rng.choice(mutable)
                if key[s2] == old:
                    continue
                changes = [(s, old), (s2, key[s2])]
                key[s], key[s2] = key[s2], old
            else:
                q = rng.random()
                p_syl = caps.get('p_syl', 0.45)
                if q < 0.9 - p_syl:
                    nv = rng.choice(lvals)
                elif q < 0.9:
                    nv = rng.choice(pb.byk['s'])
                elif q < 0.96:
                    nv = rng.choice(pb.byk['w'])
                else:
                    nv = pb.null_v
                if nv == old:
                    continue
                changes = [(s, old)]
                key[s] = nv
                if not kinds_ok(key):
                    key[s] = old
                    continue
        new = pb.score(key)
        if new >= cur or rng.random() < math.exp((new - cur) / Tm):
            cur = new
            if changes and len(changes) and p_word and tried_w:
                pass
            if cur > best:
                best, bestkey = cur, key[:]
        else:
            for s, o in reversed(changes):
                key[s] = o
    return best, bestkey


def setup(a):
    texts = na.load_texts(a.files)
    model = ing.Model(a.model)
    pb = na.Problem(texts, model, context='clear', syl='cv', words=DESIGN_WORDS,
                    extra_syl=open(os.path.join(H, 'control_1653_syl.txt')).read().split())
    caps = dict(syl=100, word=16, null=3, homo=4, p_syl=0.45)
    fixed = {}
    for f in a.fix:
        s, v = f.split('=')
        if s in pb.sidx:
            fixed[pb.sidx[s]] = pb.vid[v]
    return pb, caps, fixed


def worker(args):
    a, seed = args
    pb, caps, fixed = setup(a)
    lex = lexicon()
    buckets = build_buckets(pb, lex, caps)
    runs = windows(pb)
    rng = random.Random(seed)
    b, k = anneal(pb, rng, a.iters, a.T0, a.T1, caps, fixed, buckets, runs, a.p_word)
    b, k = na.polish(pb, k, caps, fixed)
    return seed, b, k


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('files', nargs='+')
    ap.add_argument('--model', required=True)
    ap.add_argument('--fix', nargs='*', default=[])
    ap.add_argument('--iters', type=int, default=100000)
    ap.add_argument('--restarts', type=int, default=4)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--T0', type=float, default=2.0)
    ap.add_argument('--T1', type=float, default=0.02)
    ap.add_argument('--p-word', type=float, default=0.5)
    ap.add_argument('--time', type=int, default=0, help='timing run of N iterations; prints it/s only')
    ap.add_argument('--out')
    a = ap.parse_args()
    if a.time:
        pb, caps, fixed = setup(a)
        t0 = time.time()
        buckets = build_buckets(pb, lexicon(), caps)
        t1 = time.time()
        anneal(pb, random.Random(1), a.time, a.T0, a.T1, caps, fixed, buckets, windows(pb), a.p_word)
        dt = time.time() - t1
        print(f'lexicon+buckets {t1 - t0:.1f}s; {a.time} iters in {dt:.1f}s = {a.time / dt:.0f} it/s; '
              f'buckets k: ' + ' '.join(f'{k}:{len(v[0])}' for k, v in sorted(buckets.items())))
        return
    import multiprocessing as mp
    jobs = [(a, a.seed * 1000 + r) for r in range(a.restarts)]
    with mp.Pool(min(4, a.restarts)) as pool:
        res = pool.map(worker, jobs)
    pb, caps, fixed = setup(a)
    runs = []
    for seed, b, k in res:
        runs.append(dict(seed=seed, score=b, lm=pb.lm_score(k), prior=pb.prior(k),
                         key={pb.signs[s]: pb.values[k[s]] for s in range(pb.nsign)}, reading=pb.reading(k)))
    runs.sort(key=lambda r: -r['score'])
    out = dict(tool='word_solve.py (F5160-WORD)', files=[os.path.basename(f) for f in a.files], iters=a.iters,
               restarts=a.restarts, seed=a.seed, T0=a.T0, T1=a.T1, p_word=a.p_word, fix=a.fix,
               scores=[r['score'] for r in runs], best=runs[0], runs=runs)
    json.dump(out, open(a.out, 'w'), ensure_ascii=False, indent=1)
    print('scores', ' '.join(f"{r['score']:.1f}" for r in runs))


if __name__ == '__main__':
    main()
