#!/usr/bin/env python3
"""GAPS112 (3 Oct 2026): is c.70 (filza 7) consistent with Gabbrielli key 4? See PREREG-GAPS112.md.

Statistic: mean per-char log-prob (char 4-gram, add-k, la18 corpus) of the key-4 decode of each '?'-free run of
c70_tokens.tsv, real values vs N decodes with the values permuted among the distinct sign entries (shuffled-key
control). Positive control: a la18 span of the same total length, cut into entries with the same value-length mix,
scored the same way against its own permutations. Coverage is printed, not gated (a permutation cannot change it).
Usage: python3 key4_check.py [--n 1000] [--seed 1]"""
import argparse, gzip, math, random, re, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
DATA = HERE.parents[2] / "tools" / "data" / "la18"

def corpus():
    t = "".join(gzip.open(p, "rt", errors="ignore").read() for p in sorted(DATA.glob("*.txt.gz")))
    t = re.sub(r"[^a-z]", "", t.lower().replace("j", "i").replace("v", "u").replace("k", "c").replace("w", "u")
               .replace("y", "i"))
    return t

class Model:
    def __init__(self, t, n=4, k=0.5):
        self.n, self.k = n, k
        self.c = collections.Counter(t[i:i+n] for i in range(len(t)-n+1))
        self.p = collections.Counter(t[i:i+n-1] for i in range(len(t)-n+2))
    def score(self, s):
        n, k = self.n, self.k
        if len(s) < n: return None
        tot = 0.0
        for i in range(len(s)-n+1):
            tot += math.log((self.c[s[i:i+n]] + k) / (self.p[s[i:i+n-1]] + 23*k))
        return tot / (len(s)-n+1)

def norm(v): return v.lower().replace("j","i").replace("v","u").replace("y","i")

def runs_of(tokens):
    out, cur = [], []
    for s, v in tokens:
        if v == "?":
            if cur: out.append(cur); cur = []
        else: cur.append((s, v))
    if cur: out.append(cur)
    return out

def stat(m, runs, mapping):
    sc, w = 0.0, 0
    for r in runs:
        s = "".join(norm(mapping[x]) for x, _ in r)
        v = m.score(s)
        if v is not None: sc += v*(len(s)-3); w += len(s)-3
    return sc / w if w else float("nan")

def test(m, runs, n, rng):
    mapping = {s: v for r in runs for s, v in r}
    real = stat(m, runs, mapping)
    signs, vals = list(mapping), list(mapping.values())
    null = []
    for _ in range(n):
        rng.shuffle(vals); null.append(stat(m, runs, dict(zip(signs, vals))))
    null.sort()
    return real, null[int(0.95*n)], sum(x >= real for x in null)/n, len(signs)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=1000); ap.add_argument("--seed", type=int, default=1); ap.add_argument("--noise", type=float, default=0.0, help="fraction of positive-control tokens whose sign is swapped for a random other sign (reader error)")
    a = ap.parse_args(); rng = random.Random(a.seed)
    rows = [l.rstrip("\n").split("\t") for l in open(HERE/"c70_tokens.tsv") if not l.startswith("#")][1:]
    toks = [(s, v) for _, s, v in rows]
    matched = sum(v != "?" for _, v in toks)
    print(f"coverage (not gated): {matched}/{len(toks)} = {matched/len(toks):.3f}")
    t = corpus(); m = Model(t)
    runs = runs_of(toks)
    real, p95, p, ent = test(m, runs, a.n, rng)
    nchar = sum(len(norm(v)) for r in runs for _, v in r)
    print(f"target: runs {len(runs)}, chars {nchar}, entries {ent}: real {real:.3f} shuffled p95 {p95:.3f} p {p:.3f} -> {'PASS' if real > p95 else 'FAIL'}")
    # positive control: same run lengths (in entries) and value lengths, cut from la18 text, entries = distinct values
    passes = 0
    for c in range(5):
        start = rng.randrange(len(t)//2); pos = start; cruns = []
        for r in runs:
            cr = []
            for _, v in r:
                L = len(norm(v)); chunk = t[pos:pos+L]; pos += L; cr.append((chunk, chunk))
            cruns.append(cr); pos += 7
        # reader error: a token's plaintext chunk is replaced by another token's chunk (wrong sign read)
        allc = [x for r in cruns for x in r]
        cruns = [[(allc[rng.randrange(len(allc))][0],)*2 if rng.random() < a.noise else x for x in r] for r in cruns]
        cr_real, cr_p95, cr_p, cr_ent = test(m, cruns, a.n, rng)
        passes += cr_real > cr_p95
        print(f"positive control {c}: entries {cr_ent}: real {cr_real:.3f} p95 {cr_p95:.3f} -> {'PASS' if cr_real > cr_p95 else 'FAIL'}")
    print(f"positive controls passing: {passes}/5")

if __name__ == "__main__": main()
