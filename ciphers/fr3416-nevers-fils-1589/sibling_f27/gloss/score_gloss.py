"""AM-NEVF27 (PREREG-AMNEVF27.md): known-answer (K) and shuffle (Z) controls for the gloss below fr.4715 f.27r L09.
usage: python3 score_gloss.py "<gloss line pass A>" "<gloss line pass B>"
LCS of each pass's gloss letters (a-z only) with the frame-1 decode 'onnehorscestes' and the frame-0 decode 'aumoins';
Z: the same LCS against 1000 random permutations of each target (seed 20261007), p95 reported. Gate: K1>=10/14, K2>=5/7,
real > shuffle p95 for both, in both passes."""
import random, re, sys

def lcs(a, b):
    p = [0] * (len(b) + 1)
    for x in a:
        q = [0]
        for j, y in enumerate(b):
            q.append(p[j] + 1 if x == y else max(p[j + 1], q[j]))
        p = q
    return p[-1]

TARGETS = [('onnehorscestes', 10), ('aumoins', 5)]
ok_all = True
for name, g in zip('AB', sys.argv[1:3]):
    g = re.sub('[^a-z]', '', g.lower().replace('v', 'u').replace('j', 'i'))
    for t, gate in TARGETS:
        r = random.Random(20261007)
        real = lcs(g, t)
        sh = sorted(lcs(g, ''.join(r.sample(t, len(t)))) for _ in range(1000))
        p95 = sh[949]
        ok = real >= gate and real > p95
        ok_all &= ok
        print(f'pass {name} {t}: LCS {real}/{len(t)} gate {gate} shuffle p95 {p95} mean {sum(sh)/1000:.2f} -> {"ok" if ok else "BELOW"}')
print('controls', 'PASS' if ok_all else 'FAIL -> NON-TEST')
