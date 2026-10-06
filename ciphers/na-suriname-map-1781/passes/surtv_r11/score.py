"""R11-SURTV: score reads.tsv against anon_key.tsv under PREREG.md (T = A - B, MAPY vs DREF Y-form share, 10,000 label permutations)."""
import csv, random, sys
def rows(f): return list(csv.DictReader((l for l in open(f) if not l.startswith('#')), delimiter='\t'))
key = {r['anon']: r for r in rows('anon_key.tsv')}; reads = {r['anon']: r for r in rows('reads.tsv')}
flip = set(sys.argv[1:])  # sensitivity: anon ids whose F1 is set to 0
def call(r, a):
    f1 = 0 if a in flip else int(r['F1']); f2 = int(r['F2'])
    return 'Y' if f1 and not f2 else ('V' if not f1 else 'other')
cls = {}
for a, k in key.items(): cls.setdefault(k['cls'], []).append((a, call(reads[a], a), int(reads[a]['F3'])))
share = lambda L: sum(c == 'Y' for _, c, _ in L) / len(L)
for c in ('MAPY', 'LETY', 'DREF'):
    L = cls[c]; print(f"{c}: n={len(L)} Y-form {sum(x=='Y' for _,x,_ in L)} ({share(L):.3f}), V-form {sum(x=='V' for _,x,_ in L)}, other {sum(x=='other' for _,x,_ in L)}, two dots {sum(d for *_, d in L)}")
A, B = share(cls['MAPY']), share(cls['DREF']); T = A - B
pool = [x for _, x, _ in cls['MAPY'] + cls['DREF']]; n = len(cls['MAPY']); random.seed(1781); null = []
for _ in range(10000):
    random.shuffle(pool); null.append(sum(x == 'Y' for x in pool[:n]) / n - sum(x == 'Y' for x in pool[n:]) / (len(pool) - n))
null.sort(); p99 = null[int(0.99 * len(null))]; mean = sum(null) / len(null); p = sum(v >= T for v in null) / len(null)
print(f"A (MAPY Y-form) {A:.3f}  B (DREF Y-form) {B:.3f}  T {T:.3f}  control mean {mean:.3f} p99 {p99:.3f}  P(null>=T) {p:.4f}")
L = share(cls['LETY'])
v = 'SAME SIGN' if (T > p99 and A >= 0.8 and L >= 0.8) else ('DIFFERENT' if A <= 0.2 else 'UNDECIDED')
print(f"LETY Y-form {L:.3f}  -> {v}" + (f"  [sensitivity: F1=0 for {sorted(flip)}]" if flip else ''))
