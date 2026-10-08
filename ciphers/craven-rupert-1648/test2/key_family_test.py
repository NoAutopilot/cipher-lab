#!/usr/bin/env python3
"""D2-CRAV, 8 Oct 2026: spec test 2 for craven-rupert-1648 (R8447) as registered in ../PREREG-D2-CRAV.md.
Applies each candidate table test2/T_*.tsv to the 41 legible tokens; COV vs a random-code control, WL vs a shuffled-key control,
gate p99 on both; a matched-design self-enciphered control (20 synthetic letters per table). Writes results.tsv.
--check re-derives and exits 1 if the committed results.tsv differs."""
import sys, os, re, glob, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TABLES = ['T_8446', 'T_8446x', 'T_8448', 'T_8445', 'T_NR']
def fold(s): return s.lower().replace('v', 'u').replace('j', 'i')
def load_target():
    lines = []
    for ln in open(os.path.join(HERE, '..', 'ciphertext.txt')):
        if ln.startswith('#') or not ln.strip(): continue
        toks = []
        for t in ln.split('\t')[1].split():
            if t == 'X': continue
            toks.append(int(re.sub(r'[^0-9]', '', t)))
        lines.append(toks)
    return lines
def load_table(name):
    d = {}
    for ln in open(os.path.join(HERE, name + '.tsv')):
        if ln.startswith('#') or ln.startswith('code\t') or not ln.strip(): continue
        c, v = ln.split('\t')[:2]
        d[int(c)] = '' if v == '[null]' else fold(v)
    return d
def corpus_text():
    return ' '.join(open(f, errors='ignore').read() for f in sorted(glob.glob(os.path.join(ROOT, 'tools/data/en/pg*.txt'))))
TEXT = fold(corpus_text()); WORDS = re.findall(r'[a-z]+', TEXT)
CNT = collections.Counter(WORDS); DICT = {w for w, n in CNT.items() if len(w) >= 3 and n >= 2}; MAXW = max(map(len, DICT))
def wl_run(s):
    n = len(s); best = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        b = best[i + 1]
        for L in range(3, min(MAXW, n - i) + 1):
            if s[i:i + L] in DICT: b = max(b, L + best[i + L])
        best[i] = b
    return best[0]
def score(lines, T):
    cov = 0; wl = 0
    for toks in lines:
        run = ''
        for t in toks:
            if t in T: cov += 1; run += T[t]
            else: wl += wl_run(run); run = ''
        wl += wl_run(run)
    return cov, wl
def pct(xs, p): xs = sorted(xs); return xs[min(len(xs) - 1, int(p * len(xs)))]
def controls(lines, T, rng, n=1000):
    codes = list(T); vals = list(T.values()); mx = max(codes); c1 = []; c2 = []
    for _ in range(n):
        cs = rng.sample(range(1, mx + 1), len(codes)); c1.append(score(lines, dict(zip(cs, vals)))[0])
        v = vals[:]; rng.shuffle(v); c2.append(score(lines, dict(zip(codes, v)))[1])
    return pct(c1, 0.99), pct(c2, 0.99)
def synth(T, lens, rng):
    inv = collections.defaultdict(list)
    for c, v in T.items():
        if v: inv[v].append(c)
    words = [w for w in inv if len(w) > 1]; outside = [c for c in range(1, 2000) if c not in T]
    N = sum(lens); start = rng.randrange(0, len(WORDS) - 400); toks = []; i = start
    while len(toks) < N:
        w = WORDS[i]; i += 1
        if w in words: toks.append(rng.choice(inv[w])); continue
        for ch in w:
            toks.append(rng.choice(inv[ch]) if ch in inv else rng.choice(outside))
    toks = toks[:N]; out = []; k = 0
    for L in lens: out.append(toks[k:k + L]); k += L
    return out
def run():
    rng = random.Random(2026); target = load_target(); lens = [len(l) for l in target]; rows = []
    for name in TABLES:
        T = load_table(name); cov, wl = score(target, T); p1, p2 = controls(target, T, rng)
        verdict = 'PASS' if cov > p1 and wl > p2 else 'FAIL'
        cp = 0
        for s in range(20):
            sl = synth(T, lens, rng); c, w = score(sl, T); q1, q2 = controls(sl, T, rng, 200)
            cp += (c > q1 and w > q2)
        if verdict == 'FAIL' and cp < 16: verdict = 'non-test'
        dec = ' / '.join(' '.join(T.get(t, '.') or '0' for t in l) for l in target)
        rows.append([name, str(len(T)), str(sum(lens)), str(cov), str(p1), str(wl), str(p2), f'{cp}/20', verdict, dec])
    return 'table\tn_codes\tN\tCOV\tC1_p99\tWL\tC2_p99\tdesign_ctrl_pass\tverdict\tdecode\n' + '\n'.join('\t'.join(r) for r in rows) + '\n'
if __name__ == '__main__':
    out = run(); path = os.path.join(HERE, 'results.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == out; print('check OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w').write(out); print(out)
