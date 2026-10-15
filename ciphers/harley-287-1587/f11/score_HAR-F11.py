#!/usr/bin/env python3
"""HAR-F11 score (PREREG f11/PREREG-HAR-F11.md). Fit A: R328 alphabet decode of f.11 groups of >=3 letter signs vs
20 label permutations; Fit B: f.11 numerals defined by R328/R330 vs 20 same-digit-count random draws. --check: exit 1 if
score_HAR-F11.tsv is stale."""
import collections, glob, itertools, os, random, re, sys
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, '..', '..', '..')
def rows(p):
    return [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')][1:]
groups = [r for r in rows(os.path.join(H, 'ciphertext_f11.tsv')) if r[1].startswith('G')]
match = {r[0]: r[1].split(',') for r in rows(os.path.join(H, 'match_f11.tsv'))}
words = collections.Counter()
for f in glob.glob(os.path.join(R, 'tools/data/en16_repo/*.txt')):
    words.update(re.findall(r'[a-z]+', open(f, encoding='utf-8', errors='ignore').read().lower()))
lex = {w for w, c in words.items() if c >= 2 and len(w) >= 4}
r328 = sorted({r[2] for r in rows(os.path.join(H, '..', 'keys', 'period_signs_HAR-KEYS.tsv')) if r[0] == 'R328'})
def has_word(cands):
    n = len(cands)
    for i in range(n):
        for j in range(i + 4, n + 1):
            for t in itertools.product(*cands[i:j]):
                if ''.join(t) in lex: return True
    return False
def fitA(perm):
    s = 0; tot = 0; cov = 0
    for g in groups:
        sig = [t for t in g[2].split() if not t.isdigit()]
        tot += len(sig); cov += sum(1 for t in sig if match.get(t, ['?']) != ['?'])
        if len(sig) < 3: continue
        cands = [[perm.get(x, x) for x in match.get(t, ['?'])] if match.get(t, ['?']) != ['?'] else list('abcdefghiklmnopqrstuxyz') for t in sig]
        s += has_word(cands)
    return s, cov, tot
idp = {c: c for c in r328}
a, cov, tot = fitA(idp)
rng = random.Random(0); actl = []
for _ in range(20):
    p = r328[:]; rng.shuffle(p); actl.append(fitA(dict(zip(r328, p)))[0])
nA = sum(1 for g in groups if len([t for t in g[2].split() if not t.isdigit()]) >= 3)
nums = sorted({int(t) for g in groups for t in g[2].split() if t.isdigit()})
defined = set()
for r in rows(os.path.join(H, '..', 'keys', 'codes_HAR-KEYS.tsv')):
    if r[0] in ('R328', 'R330') and r[1].isdigit(): defined.add(int(r[1]))
b = sum(1 for n in nums if n in defined)
rng = random.Random(0); bctl = []
for _ in range(20):
    bctl.append(sum(1 for n in nums if rng.randint(10 ** (len(str(n)) - 1) if n >= 10 else 0, 10 ** len(str(n)) - 1) in defined))
hits = ','.join(f'{n}' for n in nums if n in defined)
out = ['fit\tscore\tcontrol_max\tcontrol_mean\tn_units\tverdict\tnote',
 f"A_R328_alphabet\t{a}\t{max(actl)}\t{sum(actl)/20:.2f}\t{nA}\t{'NON-TEST' if nA < 2 else ('FIT' if a >= 2 and a > max(actl) else 'NO FIT')}\tcoverage {cov}/{tot} letter signs matched to an R328 shape",
 f"B_R328_R330_codes\t{b}\t{max(bctl)}\t{sum(bctl)/20:.2f}\t{len(nums)}\t{'NON-TEST' if len(nums) < 2 else ('FIT' if b >= 2 and b > max(bctl) else 'NO FIT')}\tnumerals {','.join(map(str, nums))}; defined: {hits}"]
txt = '\n'.join(out) + '\n'; P = os.path.join(H, 'score_HAR-F11.tsv')
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(P) and open(P, encoding='utf-8').read() == txt else 1)
open(P, 'w', encoding='utf-8').write(txt); print(txt, end='')
