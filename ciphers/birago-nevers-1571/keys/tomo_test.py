"""TOMO-NUM (5 Oct 2026): test Tomokiyo's two numerical systems against the pooled Nov 1571 Birago digits.
PREREG-TOMO-NUM.md, Test 1 (segmentation fit, both systems) and Test 2 (key_crossmatch gate, system A).
python3 tomo_test.py  (from this folder; writes tomo_test_out.txt)"""
import sys, math, random, re, glob, gzip
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import key_crossmatch as kx
from judge_plaintext import fold

NUM = ROOT / 'ciphers/birago-fr3252-1571-72/num'
STRAY, NULLC, BEAM, NSHUF = -2.0, -0.5, 300, 20

def load(p):
    k = {}
    for l in open(p):
        if l.startswith('#') or l.startswith('code\t') or not l.strip(): continue
        c, v = l.rstrip('\n').split('\t')
        k[c] = [] if v.startswith('_') else v.split('|')
    return k
A = load(HERE / 'tomo_colbert398.tsv'); B = load(HERE / 'tomo_nevers_no23.tsv')
B.pop('x')  # l is the letter x: not in a digit stream

runs = [''.join(l.split()) for l in open(NUM / 'pooled_tokens.txt').read().split('\n') if l.strip()]
model = kx.get_model('it')
def lp(ctx, ch):
    g = (ctx + ch)[-model.n:]
    if len(g) < model.n: return -1.3
    return math.log10((model.c.get(g, 0) + model.k) / (model.ctx.get(g[:-1], 0) + model.V * model.k))

def parse(run, key):
    """beam over (pos); state = last 3 letters; returns best (score, letters, strays, nulls)."""
    beams = {0: {'': (0.0, '', 0, 0)}}
    for i in range(len(run) + 1):
        cur = beams.pop(i, None)
        if not cur: continue
        if i == len(run):
            return max(cur.values(), key=lambda t: t[0])
        cur = dict(sorted(cur.items(), key=lambda kv: -kv[1][0])[:BEAM])
        for st, (sc, txt, ns, nn) in cur.items():
            opts = [(1, None, STRAY)]
            for L in (1, 2):
                c = run[i:i + L]
                if len(c) == L and c in key:
                    vals = key[c]
                    if not vals: opts.append((L, '', NULLC))
                    else:
                        for v in vals: opts.append((L, fold(v), 0.0))
            for L, v, pen in opts:
                nsc, ctx = sc + pen, st
                if v:
                    for ch in v: nsc += lp(ctx, ch); ctx = (ctx + ch)[-3:]
                ntxt = txt + (v or '')
                d = beams.setdefault(i + L, {})
                rec = (nsc, ntxt, ns + (v is None), nn + (v == ''))
                if ctx not in d or d[ctx][0] < nsc: d[ctx] = rec

def fit(rs, key):
    tot = n = st = nl = 0; letters = ''
    for r in rs:
        sc, t, s, x = parse(r, key); tot += sc; n += len(r); st += s; nl += x; letters += t
    return tot / n, st / n, model.score(letters) if letters else -9.9, letters

def shuffles(rs, seed):
    rnd = random.Random(seed); d = list(''.join(rs)); rnd.shuffle(d); out, p = [], 0
    for r in rs: out.append(''.join(d[p:p + len(r)])); p += len(r)
    return out

CORP = None
def corpus():
    global CORP
    if CORP is None:
        t = ''.join(gzip.open(f, 'rt', errors='ignore').read() for f in sorted(glob.glob(str(ROOT / 'tools/data/it16dip/*.txt.gz'))))
        t = t.lower().replace('j', 'i').replace('k', 'c').replace('w', 'u').replace('y', 'i').replace('x', 's')
        CORP = re.sub(' +', ' ', re.sub('[^a-z ]', ' ', t))
    return CORP

def encipher(key, seed, ndig=985, stray=0.05):
    rnd = random.Random(seed); c = corpus(); s = rnd.randrange(0, len(c) - 20000)
    inv = {}
    for code, vals in key.items():
        for v in vals: inv.setdefault(v, []).append(code)
    space = [c_ for c_, v in key.items() if not v]
    digits = ''
    i = s
    while len(digits) < ndig:
        ch = c[i]; i += 1
        if rnd.random() < stray: digits += rnd.choice('0123456789')
        if ch == ' ':
            if key is A: digits += '7'
            continue
        if ch == 'q' and 'qu' in inv and c[i] == 'u': digits += rnd.choice(inv['qu']); i += 1; continue
        if ch in inv: digits += rnd.choice(inv[ch])
        if key is B and rnd.random() < 0.08: digits += '0'   # nulls, 'use 0 most often'
    digits = digits[:ndig]; out, p = [], 0
    for r in runs: out.append(digits[p:p + len(r)]); p += len(r)
    return out

lines = []
def say(s): print(s, flush=True); lines.append(s)
say(f'target: {len(runs)} runs, {sum(map(len, runs))} digits; stray {STRAY} null {NULLC} beam {BEAM} shuffles {NSHUF}')
for name, key in (('A colbert398', A), ('B nevers_no23', B)):
    gate_ok = 0
    for seed in (1, 2, 3):
        cr = encipher(key, seed); f = fit(cr, key)
        nulls = [fit(shuffles(cr, 100 + j), key)[0] for j in range(NSHUF)]
        ok = f[0] > max(nulls); gate_ok += ok
        say(f'{name} CONTROL seed {seed}: obj {f[0]:.3f} strays {f[1]:.3f} lm {f[2]:.3f} | shuffle max {max(nulls):.3f} mean {sum(nulls)/len(nulls):.3f} -> {"above" if ok else "NOT above"}')
    f = fit(runs, key)
    nulls = [fit(shuffles(runs, 200 + j), key)[0] for j in range(NSHUF)]
    rank = sum(x >= f[0] for x in nulls)
    verdict = ('NON-TEST (control gate %d/3)' % gate_ok) if gate_ok < 3 else ('FITS' if f[0] > max(nulls) else 'NO FIT (control-backed)')
    say(f'{name} TARGET: obj {f[0]:.3f} strays {f[1]:.3f} lm {f[2]:.3f} | shuffle max {max(nulls):.3f} mean {sum(nulls)/len(nulls):.3f}, {rank}/{NSHUF} shuffles >= target -> {verdict}')
    say(f'{name} TARGET decode head (not a reading): {f[3][:80]}')

# Test 2: key_crossmatch gate, system A, on the phase.py pair files + matched control
gate = kx.load_gate(); say(f'Test 2 gate stat_min {gate["stat_min"]} min_coverage {gate["min_coverage"]}')
kA = {c: {'value': v[0]} for c, v in A.items() if v and len(c) == 2}
for fn in ('ciphers/birago-nevers-1571/ciphertext_f119_pairs.txt', 'ciphers/birago-fr3252-1571-72/num/ciphertext_f100_pairs.txt'):
    signs = [t for l in open(ROOT / fn) if not l.startswith('#') for t in l.split() if len(t) == 2 and t.isdigit()]
    ps = kx.pair_stats(kA, signs, model, n_shuffle=20, seed=0)['own']; cov = kx.coverage_of(kA, signs)
    say(f'Test 2 TARGET {Path(fn).name}: n={len(signs)} coverage {cov:.2f} stat {ps["stat"] if ps["stat"] is None else round(ps["stat"],2)} -> {kx.gate_verdict(ps["stat"], cov, len(signs), gate)}')
sys.path.insert(0, str(NUM)); import phase
for seed in (1, 2, 3):
    cr = encipher(A, seed, ndig=500)
    best = None
    for s in range(5):
        got = phase.em(cr, seed=s); sc = phase.summary(got)
        if best is None or sc['H'] < best[1]['H']: best = (got, sc)
    signs = [x for t in best[0] for x in t if len(x) == 2]
    ps = kx.pair_stats(kA, signs, model, n_shuffle=20, seed=0)['own']; cov = kx.coverage_of(kA, signs)
    say(f'Test 2 CONTROL seed {seed} (em-phase, ~250 pairs): n={len(signs)} coverage {cov:.2f} stat {ps["stat"] if ps["stat"] is None else round(ps["stat"],2)} -> {kx.gate_verdict(ps["stat"], cov, len(signs), gate)}')
(HERE / 'tomo_test_out.txt').write_text('\n'.join(lines) + '\n')
