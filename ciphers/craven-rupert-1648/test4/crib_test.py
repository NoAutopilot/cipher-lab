#!/usr/bin/env python3
"""CRAV-CRIB (PREREG-D2-CRAV.md amendment A5): clear-context crib test on R3 "write to [40 97 52 35 85] & they will".
Model M2: code < 100 = one letter, >= 100 = one word. R3 is five letter codes. Writes test4/crib_results.tsv; --check re-derives."""
import sys, os, re, random, math, glob, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
R3 = [40, 97, 52, 35, 85]
R4 = [72, 60, 52, 65, 63, 78, 95, 77, 167, 404, 68, 90, 64, 99, 85, 97, 86, 65, 29, 107, 1067, 922, 429]
CRIBS = ("states scots dutch lords queen orange holland zealand amsterdam rotterdam admiralty merchants herbert hague jermyn hyde "
         "culpeper cottington hopton nicholas batten lauderdale lanark ormond inchiquin maurice york brill helvoet french irish danes "
         "swede bohemia elizabeth craven").split()
def corpus():
    t = ''
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools/data/en/*.txt'))):
        t += open(f, encoding='utf-8', errors='ignore').read().lower()
    return re.findall(r'[a-z]+', t)
WORDS = corpus()
LET = collections.Counter(''.join(WORDS)); NL = sum(LET.values())
BI = collections.Counter(); 
for w in WORDS:
    for a, b in zip(w, w[1:]): BI[a + b] += 1
NB = sum(BI.values())
def lp1(c): return math.log((LET[c] + 1) / (NL + 26))
def lp2(a, b): return math.log((BI[a + b] + 1) / (NB + 676))
def s_h(c): return len(c) == len(R3)
def s_i(c, run=R3):
    if not s_h(c): return False
    m = {}; inv = {}
    for code, ch in zip(run, c):
        if m.setdefault(code, ch) != ch or inv.setdefault(ch, code) != code: return False
    return True
def forced(c):
    """letters a crib forces on R4 through the shared codes; returns (R4 position -> letter)."""
    m = dict(zip(R3, c)); return {i: m[x] for i, x in enumerate(R4) if x in m}
def c3score(c):
    f = forced(c)   # R4 index 2 (52), 14 (85), 15 (97): 14,15 adjacent letter codes -> one bigram
    s = sum(lp1(ch) for ch in f.values())
    if 14 in f and 15 in f: s += lp2(f[14], f[15]) - lp1(f[15])
    return s
def run():
    rnd = random.Random(2026); rows = []
    for c in CRIBS:
        perms = []
        for _ in range(1000):
            l = list(c); rnd.shuffle(l); perms.append(''.join(l))
        c1h = sum(map(s_h, perms)) / 1000; c1i = sum(map(s_i, perms)) / 1000
        if s_i(c):
            sc = c3score(c); ps = sorted(c3score(p) for p in perms)
            pct = sum(p < sc for p in ps) / 1000; p95 = ps[949]
            out = 'lead (M)' if sc > p95 else 'not discriminated'
            rows.append((c, len(c), int(s_h(c)), int(s_i(c)), c1h, c1i, '%.3f' % sc, '%.3f' % p95, '%.3f' % pct,
                         ''.join(forced(c).get(i, '.') for i in range(len(R4)) if R4[i] < 100), out))
        else:
            rows.append((c, len(c), int(s_h(c)), int(s_i(c)), c1h, c1i, '', '', '', '', 'fails S_i' if s_h(c) else 'fails S_h (length)'))
    # C2 random-word base rate
    pool = [w for w in WORDS if len(w) >= 3]; r2 = random.Random(2026); draw = [r2.choice(pool) for _ in range(1000)]
    b_h = sum(map(s_h, draw)) / 1000; b_i = sum(map(s_i, draw)) / 1000
    lines = ['crib\tlen\tS_h\tS_i\tC1_shuffled_S_h\tC1_shuffled_S_i\tC3_score\tC3_p95\tC3_pctile\tR4_letter_codes_forced\toutcome']
    lines += ['\t'.join(map(str, r)) for r in rows]
    lines.append('#C2 random-word base rate (1000 words, tools/data/en, len>=3): S_h %.3f S_i %.3f' % (b_h, b_i))
    return '\n'.join(lines) + '\n'
if __name__ == '__main__':
    out = run(); path = os.path.join(HERE, 'crib_results.tsv')
    if '--check' in sys.argv:
        ok = open(path).read() == out; print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w').write(out); print(out)
