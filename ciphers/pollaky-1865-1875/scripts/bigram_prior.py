#!/usr/bin/env python3
"""Gap 2 (a), GAPS156 (3 Oct 2026): bigram design prior on ad 2 and the two Pollaky digit siblings.

Pre-registered in NOTES.md ("GAPS156 ... bigram design prior on ad 2"). Splits each digit string into
non-overlapping bigrams, computes bigram IC and repeat count, and compares with 200 uniform random digit
strings (null) and synthetic 10x10 homophonic encipherments of English (positive control, two allocations).
Deterministic (seed 156). Usage: python3 bigram_prior.py [--out results.tsv]
"""
import argparse, random, re, os
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
AD2 = ("56. 717. 9362. 81720. 19736. 14. 618. 9:77314. 390. 400. 272. 20 = 211. 59. 91. 881. 460. - 80. 401. "
       "70. 447 415. 91 437. . 801 10031. 874. 92. 871. 2391. 941. 72050. 67321. 438921. 150.")
S1864 = "209.179.211.181.214.19.512-248.206.1163.861. 81165.1166. - 864-80905-"
S1865 = "5634 (347.'0563) 574,0 - 9865 - 9005,1053 - 21753, 4175, 0,00'175,86 (54732) 8630'275"
TEXTS = [("ad2-1871", AD2), ("sib-1864", S1864), ("sib-1865", S1865)]
SOURCES = ["tools/data/pg1661_holmes.txt", "tools/data/en/pg76_huckfinn.txt",
           "tools/data/en/pg1342_pride.txt", "tools/data/en/pg64317_gatsby.txt"]
FREQ = dict(zip("etaoinshrdlcumwfgypbvkjxqz",
                [12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3, 4.0, 2.8, 2.8, 2.4, 2.4, 2.2, 2.0,
                 2.0, 1.9, 1.5, 1.0, 0.8, 0.15, 0.15, 0.10, 0.07]))
LET = "abcdefghijklmnopqrstuvwxyz"


def digits(t):
    return re.sub(r"\D", "", t)


def bigrams(d, phase=0):
    d = d[phase:]
    return [d[i:i + 2] for i in range(0, len(d) - 1, 2)]


def stats(bg):
    n = len(bg); c = Counter(bg)
    ic = sum(v * (v - 1) for v in c.values()) / (n * (n - 1))
    return ic, n - len(c)


def alloc(variant, rng):
    if variant == "A":
        tot = sum(FREQ.values())
        k = {l: max(1, round(100 * FREQ[l] / tot)) for l in LET}
        order = sorted(LET, key=lambda l: -FREQ[l])
        i = 0
        while sum(k.values()) > 100:
            l = order[i % 26]
            if k[l] > 1: k[l] -= 1
            i += 1
        i = 0
        while sum(k.values()) < 100:
            k[order[i % 26]] += 1; i += 1
    else:
        k = {l: 1 for l in LET}
        for _ in range(74): k[rng.choice(LET)] += 1
    codes = ["%02d" % i for i in range(100)]; rng.shuffle(codes)
    out, j = {}, 0
    for l in LET:
        out[l] = codes[j:j + k[l]]; j += k[l]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "bigram_prior.tsv"))
    a = ap.parse_args()
    rng = random.Random(156)
    corp = {}
    for s in SOURCES:
        corp[s] = re.sub(r"[^a-z]", "", open(os.path.join(ROOT, s), encoding="utf-8", errors="ignore").read().lower())
    rows = []
    for name, t in TEXTS:
        d = digits(t); n = len(d) // 2
        tic, trep = stats(bigrams(d))
        tic1, trep1 = stats(bigrams(d, 1))
        null = sorted(stats(bigrams("".join(rng.choice("0123456789") for _ in range(len(d)))))[0] for _ in range(200))
        nullr = sorted(stats(bigrams("".join(rng.choice("0123456789") for _ in range(len(d)))))[1] for _ in range(200))
        p95, p50 = null[189], null[100]
        tail = sum(x >= tic for x in null) / 200
        print(f"{name}: digits {len(d)} bigrams {n} | IC {tic:.4f} R {trep} (phase1 IC {tic1:.4f} R {trep1}) | "
              f"null IC p50 {p50:.4f} p95 {p95:.4f}, R p50 {nullr[100]} p95 {nullr[189]}, null P(IC>=target) {tail:.3f}")
        rows.append((name, "target", len(d), n, f"{tic:.4f}", trep, f"{p50:.4f}", f"{p95:.4f}", f"{tail:.3f}", ""))
        for var in "AB":
            res = {s: [] for s in SOURCES}
            for i in range(1000):
                s = SOURCES[i % 4]; c = corp[s]; st = rng.randrange(len(c) - n)
                key = alloc(var, rng)
                ct = "".join(rng.choice(key[ch]) for ch in c[st:st + n])
                res[s].append(stats(bigrams(ct)))
            allr = [x for s in SOURCES for x in res[s]]
            first20 = [res[SOURCES[i % 4]][i // 4] for i in range(20)]
            pw = sum(x[0] > p95 for x in allr) / len(allr)
            pw20 = sum(x[0] > p95 for x in first20) / 20
            mic = sum(x[0] for x in allr) / len(allr)
            per = " ".join(f"{os.path.basename(s).split('_')[1].split('.')[0]}={sum(x[0] > p95 for x in res[s]) / len(res[s]):.2f}" for s in SOURCES)
            print(f"   control {var}: mean IC {mic:.4f}, power(20) {pw20:.2f}, power(1000) {pw:.3f}; per source {per}")
            rows.append((name, f"control-{var}", len(d), n, f"{mic:.4f}", "", f"{p50:.4f}", f"{p95:.4f}", "", f"power20={pw20:.2f};power1000={pw:.3f};{per}"))
    with open(a.out, "w") as f:
        f.write("text\trole\tdigits\tbigrams\tbigram_IC\trepeats\tnull_p50\tnull_p95\tnull_tail\tpower\n")
        for r in rows: f.write("\t".join(map(str, r)) + "\n")
    print("wrote", os.path.relpath(a.out, ROOT))


if __name__ == "__main__":
    main()
