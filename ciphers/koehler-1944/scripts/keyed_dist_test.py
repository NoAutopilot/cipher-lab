#!/usr/bin/env python3
"""Step 1 of family B' (keyed-tableau running key), GOLD-2C, 25 Sept 2026: a permutation-invariant distribution test.

Under any keyed tableau c = S3(S1(p) + S2(k)) (unknown alphabet permutations S1, S2, S3; the special cases are a
keyed plain alphabet, a keyword-mixed Vigenere tableau, a Beaufort/Porta variant) the ciphertext letter
distribution is a permutation of a circular convolution of the (permuted) plaintext and key distributions. So the
SORTED frequency profile, the index of coincidence, the entropy and the chi-square against uniform of a
keyed-tableau running-key ciphertext do not depend on S3, and depend on S1, S2 only through which letters happen
to combine. This script simulates that family and the one-time-key family at the target's five lengths and reports
where the target falls in each.

  python3 ciphers/koehler-1944/scripts/keyed_dist_test.py [--trials 1000] [--seed 1] [--out RESULT.json]

Simulation per trial (keyed family): plaintext windows cut from one de20 book at the five target lengths (a random
start per message, as the real messages are five separate texts), key windows from a different book of de20 or
nl20 (Dutch or German book key, each half the trials), three independent uniformly random permutations, vig
arithmetic (beau/varbeau give the same sorted profile up to a relabelling of the key permutation). One-time-key
family: uniform random letters at the same lengths. Also reported, for reference: the STANDARD tableau (identity
permutations) with the same texts, which is Bourdeau's family 4 (excluded 15 Sept 2026 by a unigram likelihood test).

Statistics per ciphertext (pooled 924 letters): IC, entropy (bits), chi-square vs uniform (25 df), max count, min
count, and the L1 distance between the sorted count profile and the mean sorted profile of the one-time-key
family. Percentiles: the share of simulated ciphertexts whose statistic is <= the target's. A family is excluded
by this test only if the target sits outside its central 99 percent band on a statistic (the brief's gate).
Nothing here reads plaintext; it is a statistic, not a family run (parent rule 18:18, 25 Sept 2026).
"""
import argparse, json, math, os, random, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import running_key as rk  # noqa: E402

A = rk.A
LENGTHS = [237, 178, 140, 140, 229]


def stats(cipher, ref_sorted=None):
    n = len(cipher)
    cnt = Counter(cipher)
    counts = [cnt.get(a, 0) for a in A]
    ic = sum(v * (v - 1) for v in counts) / (n * (n - 1))
    ent = -sum(v / n * math.log2(v / n) for v in counts if v)
    e = n / 26
    chi = sum((v - e) ** 2 / e for v in counts)
    srt = sorted(counts, reverse=True)
    d = {"ic": ic, "entropy": ent, "chi2": chi, "max": srt[0], "min": srt[-1], "sorted": srt}
    if ref_sorted is not None:
        d["l1_sorted"] = sum(abs(a - b) for a, b in zip(srt, ref_sorted))
    return d


def windows(text, lengths, rng):
    out = []
    for n in lengths:
        s = rng.randrange(len(text) // 20, len(text) * 19 // 20 - n)
        out.append(text[s:s + n])
    return out


def keyed_cipher(P, K, s1, s2, s3):
    return "".join(A[s3[(s1[rk.IDX[p]] + s2[rk.IDX[k]]) % 26]] for p, k in zip(P, K))


def percentile(vals, x):
    return sum(1 for v in vals if v <= x) / len(vals)


def band(vals, lo=0.005, hi=0.995):
    v = sorted(vals)
    return v[int(lo * len(v))], v[min(len(v) - 1, int(hi * len(v)))]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--trials", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--spec", default=os.path.join(ROOT, "specs", "koehler-1944.json"))
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    rng = random.Random(a.seed)
    de = rk.load_books(rk.list_books([os.path.join(ROOT, "tools", "data", "de20")]))
    nl = rk.load_books(rk.list_books([os.path.join(ROOT, "tools", "data", "nl20")]))
    msgs = rk.read_cipher(a.spec)
    lengths = [len(m) for m in msgs]
    target = "".join(msgs)
    n = len(target)
    fams = {"onetime": [], "keyed": [], "standard": []}
    ident = list(range(26))
    for t in range(a.trials):
        # one-time key: uniform letters
        fams["onetime"].append("".join(rng.choice(A) for _ in range(n)))
        pb = rng.choice(list(de))
        kpool = de if t % 2 == 0 else nl
        kb = rng.choice([b for b in kpool if b != pb])
        P = windows(de[pb], lengths, rng)
        K = windows(kpool[kb], lengths, rng)
        perms = []
        for _ in range(3):
            p = ident[:]
            rng.shuffle(p)
            perms.append(p)
        fams["keyed"].append("".join(keyed_cipher(p, k, *perms) for p, k in zip(P, K)))
        fams["standard"].append("".join(keyed_cipher(p, k, ident, ident, ident) for p, k in zip(P, K)))
    ref = [0.0] * 26
    ones = [stats(c) for c in fams["onetime"]]
    for s in ones:
        for i, v in enumerate(s["sorted"]):
            ref[i] += v / len(ones)
    res = {"target": stats(target, ref), "trials": a.trials, "seed": a.seed, "lengths": lengths,
           "families": {}}
    keys = ["ic", "entropy", "chi2", "max", "min", "l1_sorted"]
    print(f"target n={n} lengths={lengths}: " + " ".join(f"{k}={res['target'][k]:.4g}" for k in keys))
    print(f"target sorted counts: {res['target']['sorted']}")
    print("family      stat        band99(lo,hi)          median   target   percentile  inside99")
    for fam, ciphers in fams.items():
        ss = [stats(c, ref) for c in ciphers]
        fr = {}
        for k in keys:
            vals = [s[k] for s in ss]
            lo, hi = band(vals)
            med = sorted(vals)[len(vals) // 2]
            x = res["target"][k]
            pc = percentile(vals, x)
            inside = lo <= x <= hi
            fr[k] = {"band99": [lo, hi], "median": med, "percentile": pc, "inside99": inside}
            print(f"{fam:10s}  {k:10s}  ({lo:8.4g}, {hi:8.4g})   {med:8.4g}  {x:8.4g}   {pc:6.3f}      {'yes' if inside else 'NO'}")
        msrt = [sum(s["sorted"][i] for s in ss) / len(ss) for i in range(26)]
        fr["mean_sorted"] = [round(v, 1) for v in msrt]
        print(f"{fam:10s}  mean sorted counts: {[round(v) for v in msrt]}")
        res["families"][fam] = fr
    if a.out:
        json.dump(res, open(a.out, "w"), indent=1)
    return res


if __name__ == "__main__":
    main()
