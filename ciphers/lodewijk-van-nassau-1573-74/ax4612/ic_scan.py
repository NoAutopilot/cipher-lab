"""AX-4612: IC of 4612's numerals 1-120 grouped by (a) contiguous blocks of width w at offset o, (b) residue
classes v mod m, against a null of random partitions of 1..120 into classes of the same sizes (200 draws).
Also the same statistic on 4613/4615 (the known key.tsv letters, w=5 o=0) as a positive reference."""
import csv, random, collections, sys
D = 'ciphers/lodewijk-van-nassau-1573-74/'
def nums(nr):
    rows = csv.DictReader(open(D + f'ciphertext_{nr}.tsv'), delimiter='\t')
    k = 'sign' if nr != 'sib' else 'token'
    return [int(r[k]) for r in rows if r[k].isdigit() and 1 <= int(r[k]) <= 120]
def ic(seq, cls):
    c = collections.Counter(cls[v] for v in seq); n = len(seq)
    return sum(x * (x - 1) for x in c.values()) / (n * (n - 1))
def null(seq, sizes, draws=200, seed=1):
    rng = random.Random(seed); vals = list(range(1, 121)); out = []
    for _ in range(draws):
        rng.shuffle(vals); cls = {}; i = 0
        for k, s in enumerate(sizes):
            for v in vals[i:i + s]: cls[v] = k
            i += s
        out.append(ic(seq, cls))
    out.sort(); return out[len(out) // 2], out[int(len(out) * .95)], out[-1]
def blocks(w, o):
    return {v: ((v - 1 - o) % 120) // w for v in range(1, 121)}
for nr in sys.argv[1:] or ['4612', 'sib']:
    s = nums(nr); print(f'== {nr}: N(1-120)={len(s)}')
    for w in (4, 5, 6, 8):
        nm = null(s, [w] * (120 // w))
        best = max(range(w), key=lambda o: ic(s, blocks(w, o)))
        row = ' '.join(f'o{o}:{ic(s, blocks(w, o)):.4f}' for o in range(w))
        print(f' blocks w={w}: {row} | null med/p95/max {nm[0]:.4f}/{nm[1]:.4f}/{nm[2]:.4f}')
    for m in (20, 24, 30):
        cls = {v: v % m for v in range(1, 121)}
        nm = null(s, [120 // m] * m)
        print(f' mod {m}: {ic(s, cls):.4f} | null med/p95/max {nm[0]:.4f}/{nm[1]:.4f}/{nm[2]:.4f}')
