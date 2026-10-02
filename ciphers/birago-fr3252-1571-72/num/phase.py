"""Phase recovery for a two-digit homophonic stream with stray single digits (BIRAGO-NUM, 2 Oct 2026).
Hard-EM Viterbi: each plain-digit run (letters dropped; dotted two-digit groups, the wavy sign and CLEAR as breaks)
is cut into two-digit tokens or single 'stray' digits; pair log-probs re-estimated from the last cut; stray cost fixed.
Control first (synthetic Italian, one key of NCELL cells, stray digits inserted at a known rate): phase accuracy =
share of true pairs recovered exactly. python3 phase.py [--control] f119_ct2_bourdeau.txt f100_recon.txt"""
import sys, math, random
from collections import Counter
sys.path.insert(0, '.')
import analyze

def runs_from(path):
    t = open(path).read().split()
    dot = lambda x: x == 'i' and False or (len(x) == 2 and x[0].isdigit() and x[1] in '.:~-+')
    out, cur, codes = [], '', []
    for k, x in enumerate(t):
        if x.isalpha() and x not in ('i', 'CLEAR'): continue
        nxt_dot = k + 1 < len(t) and dot(t[k + 1])
        prv_dot = k > 0 and dot(t[k - 1])
        if x in ('|', 'CLEAR') or dot(x) or (x == 'i' and (nxt_dot or prv_dot)):
            if cur: out.append(cur)
            cur = ''
            if x not in ('|', 'CLEAR'): codes.append(x)
            continue
        cur += '1' if x == 'i' else x
    if cur: out.append(cur)
    return out, codes

def viterbi(run, lp, stray):
    n = len(run); best = [0.0] + [-1e18] * n; back = [0] * (n + 1)
    for i in range(1, n + 1):
        c = best[i - 1] + stray
        if c > best[i]: best[i], back[i] = c, 1
        if i >= 2:
            c = best[i - 2] + lp.get(run[i - 2:i], -12)
            if c > best[i]: best[i], back[i] = c, 2
    toks, i = [], n
    while i > 0:
        toks.append(run[i - back[i]:i]); i -= back[i]
    return toks[::-1]

def em(runs, stray=-7.0, iters=30, seed=0):
    rng = random.Random(seed)
    toks = []
    for r in runs:                      # random initial phase per run
        s = rng.randrange(2); t = ([r[0]] if s and r else []) + [r[i:i + 2] for i in range(s, len(r) - 1, 2)]
        toks.append(t)
    for _ in range(iters):
        c = Counter(x for t in toks for x in t if len(x) == 2); tot = sum(c.values())
        lp = {k: math.log((v + 0.1) / (tot + 10)) for k, v in c.items()}
        toks = [viterbi(r, lp, stray) for r in runs]
    return toks

def summary(toks):
    p = Counter(x for t in toks for x in t if len(x) == 2); s = sum(len(x) == 1 for t in toks for x in t)
    H = -sum(v / sum(p.values()) * math.log2(v / sum(p.values())) for v in p.values())
    return dict(pairs=sum(p.values()), types=len(p), types_ge3=sum(v >= 3 for v in p.values()), hapax=sum(v == 1 for v in p.values()), strays=s, H=round(H, 3))

def control(ncell=30, nlet=520, stray_rate=0.05, seed=1):
    rng = random.Random(seed)
    txt = analyze.italian(nlet, rng)
    from collections import Counter as C
    letters = sorted(set(txt)); fr = C(txt); cells = analyze.CELLS[:]; rng.shuffle(cells)
    key = {l: [cells.pop()] for l in letters}; extra = ncell - len(letters)
    while extra > 0:
        l = max(letters, key=lambda l: fr[l] / len(key[l])); key[l].append(cells.pop()); extra -= 1
    toks = []
    for ch in txt:
        if rng.random() < stray_rate: toks.append(rng.choice('0123456789'))
        toks.append(rng.choice(key[ch]))
    # break into runs of ~40 digits at random token boundaries (as dotted codes/wavy break the target)
    runs, truth, cur, ct = [], [], '', []
    for t in toks:
        cur += t; ct.append(t)
        if len(cur) > 40 and rng.random() < 0.15: runs.append(cur); truth.append(ct); cur, ct = '', []
    if cur: runs.append(cur); truth.append(ct)
    best = None
    for s in range(5):
        got = em(runs, seed=s); sc = summary(got)
        if best is None or sc['H'] < best[1]['H']: best = (got, sc)
    got = best[0]
    def spans(ts):
        out, p = set(), 0
        for t in ts:
            if len(t) == 2: out.add((p, t))
            p += len(t)
        return out
    hit = sum(len(spans(a) & spans(b)) for a, b in zip(got, truth)); tot = sum(len(spans(b)) for b in truth)
    true_sc = summary(truth)
    return round(hit / tot, 3), best[1], true_sc

if __name__ == '__main__':
    if '--control' in sys.argv:
        for nc in (30, 40, 62):
            for sd in (1, 2, 3):
                acc, sc, tr = control(ncell=nc, seed=sd)
                print(f'control ncell={nc} seed={sd}: phase acc {acc}; recovered {sc}; truth {tr}')
        sys.exit()
    allruns = []
    for p in sys.argv[1:]:
        r, codes = runs_from(p); allruns += r
        print(p, 'runs', len(r), 'digits', sum(map(len, r)), 'marked codes', codes)
    best = None
    for s in range(8):
        got = em(allruns, seed=s); sc = summary(got)
        print('seed', s, sc)
        if best is None or sc['H'] < best[1]['H']: best = (got, sc)
    p = Counter(x for t in best[0] for x in t if len(x) == 2)
    print('best', best[1]); print('pair counts', p.most_common())
    open('pooled_tokens.txt', 'w').write('\n'.join(' '.join(t) for t in best[0]) + '\n')
