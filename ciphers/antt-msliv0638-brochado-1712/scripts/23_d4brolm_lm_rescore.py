"""D4-BROLM (8 Oct 2026): LM-context rescoring of letter 134's open tokens, known-answer control first.
Pre-registered in PREREG-D4-BROLM.md (pushed e530832d8 before this script ran). Exact Viterbi over a span with a
pt18 letter 4-gram (tools/judge_plaintext.py NgramModel) + per-token prior; unmasked letters fixed.

  python3 scripts/23_d4brolm_lm_rescore.py            control (pt18), then the target only if a gate passes
  python3 scripts/23_d4brolm_lm_rescore.py --corpus pt17   secondary run (no gate uses it)
Writes align/brolm_control.tsv (per masked control token) and align/brolm_target.tsv; prints the gate lines.
"""
import csv, json, math, random, sys
from collections import Counter, defaultdict
sys.path.insert(0, '/home/user/cipher-lab/tools')
import judge_plaintext as J

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
AL = 'abcdefghijklmnopqrstuvwxyz'
corpus = sys.argv[sys.argv.index('--corpus') + 1] if '--corpus' in sys.argv else 'pt18'   # 'pt' = pt17 (Vieira)
LM = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA[corpus]], n=4, k=0.01)


import numpy as np
T = np.empty((26, 26, 26, 26))           # T[i,j,k,l] = log10 P(l | ijk)
_den = {}
for i, a in enumerate(AL):
    for j, b in enumerate(AL):
        for k_, c in enumerate(AL):
            ctx = a + b + c; d = LM.ctx.get(ctx, 0) + LM.V * LM.k
            for l, e in enumerate(AL):
                T[i, j, k_, l] = math.log10((LM.c.get(ctx + e, 0) + LM.k) / d)
NEG = -1e18


def viterbi(letters, priors):
    """letters: list of a letter or None (masked); priors: dict pos -> {letter: log10 p}. Exact MAP under the
    4-gram (first three letters carry no LM term, as in NgramModel.score), vectorised over the 26^3 states."""
    def emit(i):
        e = np.full(26, NEG)
        if letters[i] is not None:
            e[AL.index(letters[i])] = 0.0
        else:
            for a, v in priors[i].items():
                e[AL.index(a)] = v
        return e
    n = len(letters)
    e0, e1, e2 = emit(0), emit(1), emit(2)
    V = e0[:, None, None] + e1[None, :, None] + e2[None, None, :]
    back = []
    for t in range(3, n):
        cand = V[:, :, :, None] + T                      # i,j,k,l
        bi = cand.argmax(axis=0)                         # j,k,l
        V = np.take_along_axis(cand, bi[None], axis=0)[0] + emit(t)[None, None, :]
        back.append(bi)
    j, k_, l = np.unravel_index(V.argmax(), V.shape)
    path = [l, k_, j]
    for bi in reversed(back):
        i = bi[j, k_, l]; path.append(i); j, k_, l = i, j, k_
    return [AL[x] for x in reversed(path)]


if '--selftest' in sys.argv:   # brute force vs viterbi on a 7-letter span with 2 masked slots
    import itertools
    lt = list('dilatar'); lt[2] = None; lt[5] = None
    pr = {2: {a: math.log10(1 / 26) for a in AL}, 5: {a: math.log10(1 / 26) for a in AL}}
    def sc(w): return sum(T[AL.index(w[t-3]), AL.index(w[t-2]), AL.index(w[t-1]), AL.index(w[t])] for t in range(3, len(w)))
    best = max((''.join(a if a else x.pop(0) for a in lt) for x in ([p, q] for p in AL for q in AL)), key=sc)
    v = ''.join(viterbi(lt, pr)); print('selftest', best, v, 'OK' if best == v else 'MISMATCH'); sys.exit(0 if best == v else 1)


def smooth(cnt):
    tot = sum(cnt.values()) + 0.5 * 26
    return {a: math.log10((cnt.get(a, 0) + 0.5) / tot) for a in AL}


UNIF = {a: math.log10(1 / 26) for a in AL}

# key values and aligned gloss letters
key = {r['code']: r for r in csv.DictReader(open(f'{ROOT}/key.tsv'), delimiter='\t')}
def keyval(c):
    r = key.get(c) or key.get(c.rstrip('±'))
    return r['value'] if r else None

rows = list(csv.DictReader(open(f'{ROOT}/align/align_mask_9.tsv'), delimiter='\t'))
counts = defaultdict(lambda: defaultdict(Counter))   # code -> entry -> Counter(letter)
for r in rows:
    if r['kind'] == 'code' and len(r['plain_chunk']) == 1 and r['plain_chunk'] in AL:
        counts[r['value'].rstrip('±')][r['cipher_line']][r['plain_chunk']] += 1

def prior_counts(code, exclude=None):
    c = Counter()
    for e, k in counts.get(code.rstrip('±'), {}).items():
        if e != exclude:
            c.update(k)
    if not c and code in key:
        c.update(json.loads(key[code]['all_observed_letters']))
    return c

# ---- target tokens
tok = [r for r in csv.DictReader(open(f'{ROOT}/reading_body_tokens.tsv'), delimiter='\t')
       if r['line'] in ('m0275-r1', 'm0276-r1', 'm0276-r2')]
THIN = {'x', 'z', 'd', 'f', '16', '9', 'ff'}
ALT = {('m0275-r1', '4'): ['10', '16'], ('m0275-r1', '2'): ['8', '9']}
spans = {'A': [t for t in tok if t['line'] in ('m0275-r1', 'm0276-r1')], 'B': [t for t in tok if t['line'] == 'm0276-r2']}
tmask = {}
for sp, ts in spans.items():
    for i, t in enumerate(ts):
        if t['grade'] in ('M', 'U') or t['sign'] in THIN:
            tmask[(sp, i)] = 'U' if t['grade'] == 'U' and t['sign'] not in key else 'K'
load = {sp: (sum(1 for (s, _), c in tmask.items() if s == sp and c == 'K'),
             sum(1 for (s, _), c in tmask.items() if s == sp and c == 'U')) for sp in spans}
print(f'[{corpus}] target masked tokens: {len(tmask)}; load per span (K, U): {load}')

# ---- control
streams = defaultdict(list)    # entry -> list of (letter, truth or None, code or None)
for r in rows:
    if r['kind'] == 'clear':
        for ch in J.fold(r['raw']):
            streams[r['cipher_line']].append((ch, None, None))
    elif r['kind'] == 'code':
        v = keyval(r['value'])
        if v is None:
            continue
        tr = r['plain_chunk'] if len(r['plain_chunk']) == 1 and r['plain_chunk'] in AL else None
        streams[r['cipher_line']].append((v, tr, r['value']))
windows = {'A': 50, 'B': 20}
rng = random.Random(20261008); rng_sh = random.Random(20261009)
out = []
res = {m: {'U': [0, 0], 'K': [0, 0], 'Kprior': [0, 0], 'ov': [0, 0]} for m in ('real', 'shuf')}
entries = sorted(streams)
for sp, W in windows.items():
    nK, nU = load[sp]
    made = tries = 0
    while made < 300 and tries < 20000:
        tries += 1
        e = rng.choice(entries); s = streams[e]
        if len(s) < W:
            continue
        a = rng.randrange(len(s) - W + 1); win = s[a:a + W]
        elig = [i for i, (_, tr, c) in enumerate(win) if tr is not None]
        if len(elig) < nK + nU:
            continue
        pick = rng.sample(elig, nK + nU); cls = {i: ('U' if j < nU else 'K') for j, i in enumerate(pick)}
        pri = {i: (UNIF if cls[i] == 'U' else smooth(prior_counts(win[i][2], exclude=e))) for i in pick}
        made += 1
        base = [ch for ch, _, _ in win]
        free = [i for i in range(W) if i not in cls]
        shuf_vals = [base[i] for i in free]; rng_sh.shuffle(shuf_vals)
        shuf = list(base)
        for i, v in zip(free, shuf_vals):
            shuf[i] = v
        for mode, ctx in (('real', base), ('shuf', shuf)):
            letters = [None if i in cls else ctx[i] for i in range(W)]
            dec = viterbi(letters, pri)
            for i in pick:
                tr = win[i][1]; ok = dec[i] == tr; R = res[mode]
                R[cls[i]][0] += ok; R[cls[i]][1] += 1
                if cls[i] == 'K':
                    pa = max(pri[i], key=pri[i].get)
                    R['Kprior'][0] += pa == tr; R['Kprior'][1] += 1
                    if dec[i] != pa:
                        R['ov'][0] += ok; R['ov'][1] += 1
                out.append([mode, sp, e, a, i, cls[i], win[i][2], tr, dec[i]])
with open(f'{ROOT}/align/brolm_control_{corpus}.tsv', 'w') as f:
    f.write('mode\tspan\tentry\tstart\tpos\tclass\tcode\ttruth\tdecoded\n')
    for r in out:
        f.write('\t'.join(map(str, r)) + '\n')

fr = lambda p: p[0] / p[1] if p[1] else float('nan')
for m in ('real', 'shuf'):
    R = res[m]
    print(f'[{corpus}] control {m}: U {R["U"][0]}/{R["U"][1]} = {fr(R["U"]):.3f}; K decoder {fr(R["K"]):.3f} '
          f'vs prior-only {fr(R["Kprior"]):.3f} (n={R["K"][1]}); overrides {R["ov"][1]}, correct {R["ov"][0]} = {fr(R["ov"]):.3f}')
R, S = res['real'], res['shuf']
gU = fr(R['U']) >= 0.40 and fr(R['U']) - fr(S['U']) >= 0.15
headroom = fr(R['Kprior']) < 0.95
gK = headroom and R['ov'][1] >= 20 and fr(R['ov']) >= 0.60 and fr(R['K']) >= fr(R['Kprior'])
print(f'[{corpus}] G-U {"PASS" if gU else "FAIL"}; G-K {"PASS" if gK else "FAIL"}{"" if headroom else " (no headroom: prior-only >= 0.95)"}')
if '--control-only' in sys.argv or corpus != 'pt18' and '--target' not in sys.argv:
    sys.exit(0)
if not (gU or gK):
    print('both gates FAIL: non-test at this N; target not scored'); sys.exit(3)

# ---- target (only after a gate passed)
lines = ['span\tline\tpos\tsign\tcurrent\tgrade\tclass\tprior_argmax\tdecoded\tchange']
for sp, ts in spans.items():
    letters, pri = [], {}
    for i, t in enumerate(ts):
        c = tmask.get((sp, i))
        if c is None:
            letters.append(t['value']); continue
        letters.append(None)
        if c == 'U':
            pri[i] = UNIF
        else:
            codes = ALT.get((t['line'], t['pos']), [t['sign']])
            ps = [smooth(prior_counts(cd)) for cd in codes]
            pri[i] = {a: math.log10(sum(10 ** p[a] for p in ps) / len(ps)) for a in AL}
    dec = viterbi(letters, pri)
    for i, t in enumerate(ts):
        c = tmask.get((sp, i))
        if c is None:
            continue
        pa = max(pri[i], key=pri[i].get)
        licensed = (c == 'U' and gU) or (c == 'K' and gK)
        ch = 'yes' if licensed and dec[i] != t['value'] else ('unlicensed' if dec[i] != t['value'] else '')
        lines.append(f'{sp}\t{t["line"]}\t{t["pos"]}\t{t["sign"]}\t{t["value"]}\t{t["grade"]}\t{c}\t{pa}\t{dec[i]}\t{ch}')
    print(f'[{corpus}] span {sp} decoded: {"".join(dec)}')
open(f'{ROOT}/align/brolm_target_{corpus}.tsv', 'w').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
