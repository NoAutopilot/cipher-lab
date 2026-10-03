#!/usr/bin/env python3
"""align_f38.py -- known-answer measure for key no.25 on fr.3416 f.38 (canvas f46): decode the blind figure pass
under no.25 (letters keys/key_no25.tsv, overbar figures keys/key_no25_nomenclator.tsv) and score its agreement with
the blind pass of the period interlinear gloss, against a shuffled-gloss and a shuffled-key control.

FILS-F38, 3 Oct 2026. Rules pre-registered in NOTES.md ("FILS-F38 pre-registration", commit db1e90fe) before any read.
Usage: python3 align_f38.py [--check]
  inputs: f38_figures.tsv (pass F: band, run, digits, overbar_positions, uncertain)
          f38_gloss.tsv   (pass G: band, segment, x_fraction, word, confidence, alternatives)
  writes f38_align.txt (per band: tokens, decode, gloss, agreement; then the controls); --check exits 1 if stale (rule 7).
"""
import sys, os, re, random, difflib, unicodedata
H = os.path.dirname(os.path.abspath(__file__))

def tsv(p):
    for l in open(os.path.join(H, p)):
        if l.startswith('#') or not l.strip() or l.startswith('band'): continue
        yield l.rstrip('\n').split('\t')

def load_key():
    K = {}
    for f in tsv('keys/key_no25.tsv'):
        if f[0] != 'code': K[f[0]] = f[1]
    N = {}
    for f in tsv('keys/key_no25_nomenclator.tsv'):
        if f[0] != 'code' and f[0].isdigit(): N[f[0]] = f[1]
    return K, N

def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if c.isalpha() and ord(c) < 128)
    s = s.replace('v', 'u').replace('j', 'i').replace('y', 'i')
    return re.sub(r'(.)\1+', r'\1', s)

def tokens(digits, bars):
    """pair from the first digit of the run (pre-registered); odd run keeps the last digit unpaired."""
    out = []
    for i in range(0, len(digits) - 1, 2):
        out.append((digits[i:i + 2], (i + 1 in bars) or (i + 2 in bars)))
    if len(digits) % 2: out.append((digits[-1], False))
    return out

def decode(toks, K, N):
    s = []
    for t, bar in toks:
        if bar and t in N: s.append(N[t])
        elif t in K and K[t] not in ('-', 'null'): s.append(K[t])
    return ''.join(s)

def agree(pairs):
    M = L = 0
    for d, g in pairs:
        m = sum(b.size for b in difflib.SequenceMatcher(None, d, g, autojunk=False).get_matching_blocks())
        M += m; L += len(d) + len(g)
    return (2 * M / L if L else 0.0), M

def main():
    K, N = load_key()
    bands = {}
    for f in tsv('f38_figures.tsv'):
        bars = set(int(x) for x in f[3].split(',') if x.strip().isdigit())
        bands.setdefault(f[0], []).append(tokens(f[2], bars))
    gloss = {}
    for f in tsv('f38_gloss.tsv'):
        if f[3].startswith('#'): continue
        seg = 0 if f[1] == 's1' else 1
        gloss.setdefault(f[0], []).append((seg, float(f[2] or 0), f[3]))
    keys = sorted(set(bands) | set(gloss))
    out = []
    D = {}; G = {}
    for b in keys:
        toks = [t for run in bands.get(b, []) for t in run]
        D[b] = norm(decode(toks, K, N))
        words = [w for _, _, w in sorted(gloss.get(b, []))]
        G[b] = words
        out.append(f'band {b}: tokens {" ".join(t + ("^" if bar else "") for t, bar in toks)}')
        out.append(f'  decode  {D[b]}')
        out.append(f'  gloss   {" ".join(words)}  -> {norm("".join(words))}')
    real, M = agree([(D[b], norm(''.join(G[b]))) for b in keys])
    glen = sum(len(norm(''.join(G[b]))) for b in keys)
    out.append(f'agreement 2M/(|D|+|G|) = {real:.3f}; matched letters M = {M}; M/|G| = {M / glen if glen else 0:.3f}')
    rng = random.Random(1)
    allw = [w for b in keys for w in G[b]]; cnt = [len(G[b]) for b in keys]
    sg = []
    for _ in range(1000):
        w = allw[:]; rng.shuffle(w); i = 0; pairs = []
        for b, c in zip(keys, cnt):
            pairs.append((D[b], norm(''.join(w[i:i + c])))); i += c
        sg.append(agree(pairs)[0])
    letters = [c for c in K if K[c] not in ('-', 'null')]; sk = []
    for _ in range(200):
        vals = [K[c] for c in letters]; rng.shuffle(vals); K2 = dict(K); K2.update(zip(letters, vals))
        pairs = [(norm(decode([t for run in bands.get(b, []) for t in run], K2, N)), norm(''.join(G[b]))) for b in keys]
        sk.append(agree(pairs)[0])
    def summ(x):
        x = sorted(x); return sum(x) / len(x), x[int(0.95 * len(x)) - 1], x[-1]
    a, p, m = summ(sg); out.append(f'shuffled gloss (1000): mean {a:.3f} p95 {p:.3f} max {m:.3f}; real beats p95: {real > p}')
    a2, p2, m2 = summ(sk); out.append(f'shuffled key (200):   mean {a2:.3f} p95 {p2:.3f} max {m2:.3f}; real beats p95: {real > p2}')
    out.append('VERDICT (pre-registered): ' + ('PASS' if real > p and real > p2 else 'FAIL'))
    txt = '\n'.join(out) + '\n'
    fp = os.path.join(H, 'f38_align.txt')
    if '--check' in sys.argv:
        ok = os.path.exists(fp) and open(fp).read() == txt
        print('check: ' + ('OK' if ok else 'STALE')); sys.exit(0 if ok else 1)
    open(fp, 'w').write(txt); print(txt, end='')

if __name__ == '__main__':
    main()
