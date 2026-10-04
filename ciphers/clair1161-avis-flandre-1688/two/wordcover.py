#!/usr/bin/env python3
"""RUN5-C1161WC (4 Oct 2026): word-cover value test of the M and contested S key signs, pre-registered in
tx/PREREG_wordcover.md. Cover = max fraction of decoded letters covered by non-overlapping fr17+fr16 vocabulary words
(len>=3, freq>=3). Nulls: 200 token-order shuffles (max-over-26 gain), the 50 shuffled-order anneal keys of
two/cons, and the 26-letter rank. Planted-value control (p, a set to 'e') runs first. Writes two/wordcover_headroom.tsv,
two/wordcover.tsv, two/wordcover_gate.tsv.

  python3 two/wordcover.py [--procs 4]
"""
import csv, glob, gzip, os, random, re, string, sys, unicodedata
from collections import Counter
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
FR17 = sorted(glob.glob(os.path.join(ROOT, "tools/data/fr17/*.txt.gz")))
FR16 = sorted(glob.glob(os.path.join(ROOT, "tools/data/fr16/*.txt.gz")))
HELD = os.path.join(ROOT, "tools/data/fr17/lettresducardina01maza.txt.gz")
TESTED = "2 6 6r 8 K L Sorn blot c dia eloop iib l ls o phi psi rc rot spiralG sqc th to tz vdash x z 4 S qb".split()
PLANT = [("p", "e"), ("a", "e")]
L = string.ascii_lowercase

def fold(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if not unicodedata.combining(c))
    return s.replace("j", "i").replace("v", "u")
def words(path): return re.findall("[a-z]+", fold(gzip.open(path, "rt", errors="ignore").read()))
def vocab(paths):
    c = Counter(w for p in paths for w in words(p) if len(w) >= 3)
    bylen = {}
    for w, n in c.items():
        if n >= 3 and len(w) <= 15: bylen.setdefault(len(w), set()).add(w)
    return bylen
VOC = None
def cover(t):
    n = len(t); b = [0] * (n + 1)
    for i in range(1, n + 1):
        m = b[i - 1]
        for ln, ws in VOC.items():
            if ln <= i and t[i - ln:i] in ws:
                v = b[i - ln] + ln
                if v > m: m = v
        b[i] = m
    return b[n] / n if n else 0.0

real = {r["sign"]: r["value"] for r in csv.DictReader(open(os.path.join(HERE, "key_pre_joint9.tsv")), delimiter="\t")}
allt = [r["sign"] for r in csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t") if r["sign"] != "/"]
def dec(k, toks): return "".join(k.get(t, "") for t in toks)
def w(k, s, v): k2 = dict(k); k2[s] = v; return k2
SHUF = []
for i in range(200):
    t = list(allt); random.Random(1000 + i).shuffle(t); SHUF.append(t)
KEYS = []
for p in sorted(glob.glob(os.path.join(HERE, "cons", "key_shuf*_s*.tsv"))):
    k = dict(real); k.update({r["sign"]: r["value"] for r in csv.DictReader(open(p), delimiter="\t")}); KEYS.append(k)

def init(voc):
    global VOC; VOC = voc
def job(a):  # (key, sign, value, toks-index or -1)
    k, s, v, i = a
    return cover(dec(w(k, s, v), allt if i < 0 else SHUF[i]))
def job_text(t): return cover(t)

def test_sign(pool, base, s, A):
    """Returns per-value real covers, gate row."""
    rc = dict(zip(L, pool.map(job, [(base, s, v, -1) for v in L])))
    V = max(L, key=lambda v: (rc[v], v == A)); R = max((v for v in L if v != A), key=lambda v: rc[v])
    sh = pool.map(job, [(base, s, v, i) for i in range(200) for v in L], chunksize=26)
    Dn, Mn = [], []
    for i in range(200):
        c = dict(zip(L, sh[i * 26:(i + 1) * 26]))
        Dn.append(max(c.values()) - c[A]); Mn.append(c[A] - max(c[v] for v in L if v != A))
    other = V if V != A else R
    kk = pool.map(job, [(k, s, x, -1) for k in KEYS for x in (A, other)])
    dn = [kk[2 * j + 1] - kk[2 * j] for j in range(50)]
    p99 = lambda xs: sorted(xs)[197]; p95 = lambda xs: sorted(xs)[47]
    ntok = allt.count(s); rank = {v: 1 + sum(1 for x in L if rc[x] > rc[v]) for v in L}
    if V != A:
        D = rc[V] - rc[A]; c = [D > 0, D > p99(Dn), D > p95(dn), ntok >= 3]
        kind, stat, n1, n2 = "change", D, p99(Dn), p95(dn)
    else:
        M = rc[A] - rc[R]; c = [M > 0, M > p99(Mn), M > p95([-x for x in dn]), ntok >= 3]
        kind, stat, n1, n2 = "confirm", M, p99(Mn), p95([-x for x in dn])
    row = [s, A, ntok, f"{rc[A]:.5f}", V, R, rank[A], kind, f"{stat:.5f}", f"{n1:.5f}", f"{n2:.5f}",
           *map(int, c), "PASS" if all(c) else "fail"]
    return rc, row

if __name__ == "__main__":
    procs = int(sys.argv[sys.argv.index("--procs") + 1]) if "--procs" in sys.argv else 4
    assert dec(real, allt) == re.sub("[^a-z]", "", open(os.path.join(HERE, "full_decode.txt")).read())
    assert len(KEYS) == 50, len(KEYS)
    voc = vocab(FR17 + FR16); init(voc)
    print("vocab", sum(len(x) for x in voc.values()), flush=True)
    with Pool(procs, initializer=init, initargs=(voc,)) as pool:
        # headroom
        C0 = cover(dec(real, allt)); Cs = pool.map(job, [(real, "a", real["a"], i) for i in range(200)])
        voc_lo = vocab([p for p in FR17 + FR16 if p != HELD])
        g = "".join(words(HELD))[300000:303375]
        gs = []
        for i in range(50):
            x = list(g); random.Random(i).shuffle(x); gs.append("".join(x))
        init(voc_lo); Cg = cover(g); Cgs = sum(map(cover, gs)) / 50; init(voc)
        Csm = sum(Cs) / 200
        bad = [C0 >= 0.95, Csm >= 0.90, Cg - Cgs < 0.10, C0 - Csm < 0.02]
        with open(os.path.join(HERE, "wordcover_headroom.tsv"), "w") as f:
            f.write("C0\tCs_mean\tCs_p99\tCg_heldout\tCgs_mean\tceiling\tnoise_ceiling\tno_discrim\tdecode_eq_shuffle\tverdict\n")
            f.write(f"{C0:.5f}\t{Csm:.5f}\t{sorted(Cs)[197]:.5f}\t{Cg:.5f}\t{Cgs:.5f}\t" + "\t".join(map(str, map(int, bad)))
                    + "\t" + ("NON-TEST" if any(bad) else "ok") + "\n")
        print(open(os.path.join(HERE, "wordcover_headroom.tsv")).read(), flush=True)
        if any(bad): sys.exit(3)
        hdr = "sign\tA\ttokens\tcover_A\targmax\trunner_up\trank_A\tkind\tstat\tshuffle_p99\tkey50_p95\ti\tii\tiii\tiv\tverdict\n"
        rows, gate = [], []
        ctl_ok = True
        for s, wrong in PLANT:
            rc, row = test_sign(pool, w(real, s, wrong), s, wrong)
            ok = row[4] == real[s] and row[-1] == "PASS"; ctl_ok &= ok
            gate.append(["CONTROL:" + s + "=" + real[s]] + row[1:] + [("recovered" if ok else "NOT recovered")])
            rows += [[f"CONTROL:{s}", v, f"{rc[v]:.5f}"] for v in L]; print("\t".join(map(str, gate[-1])), flush=True)
        if ctl_ok:
            for s in TESTED:
                rc, row = test_sign(pool, real, s, real[s]); gate.append(row + [""])
                rows += [[s, v, f"{rc[v]:.5f}"] for v in L]; print("\t".join(map(str, row)), flush=True)
        else:
            print("planted control failed: NON-TEST, target signs not gated", flush=True)
    with open(os.path.join(HERE, "wordcover.tsv"), "w") as f:
        f.write("sign\tvalue\tcover\n" + "".join("\t".join(r) + "\n" for r in rows))
    with open(os.path.join(HERE, "wordcover_gate.tsv"), "w") as f:
        f.write(hdr.rstrip("\n") + "\tnote\n" + "".join("\t".join(map(str, r)) + "\n" for r in gate))
