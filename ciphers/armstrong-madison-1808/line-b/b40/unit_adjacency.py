"""B40: sequential dependence of the units digit. For consecutive tokens both >= 100 (in the full reading order, and
separately in the >=100 subsequence with particles skipped), the 10x10 table of (unit_i, unit_{i+1}); statistic = mutual
information in bits. Null: permute the values among the >=100 positions (order shuffle, 1000 draws), percentile of the
observed MI. Controls: designs A/A2 (inflection slots, positive) and B/Bf/C/C2 (alphabetical or frequency members,
negative) simulated on en18 at N=369, 60 windows each, same statistic and null (200 draws per window); reported as the
share of windows whose MI exceeds their own null p95 (power at this N). Run: python3 unit_adjacency.py"""
import math, random, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE.parent / "b2")); sys.path.insert(0, str(HERE.parent / "b1"))
from designs import build, simulate
from padding_test import target_tokens, en18_words
def mi(pairs):
    n = len(pairs); c = Counter(pairs); a = Counter(x for x, _ in pairs); b = Counter(y for _, y in pairs)
    return sum(v / n * math.log2(v * n / (a[x] * b[y])) for (x, y), v in c.items()) if n else 0.0
def pairs_full(t): return [(t[i] % 10, t[i+1] % 10) for i in range(len(t) - 1) if t[i] >= 100 and t[i+1] >= 100]
def pairs_sub(t):
    s = [v for v in t if v >= 100]; return [(s[i] % 10, s[i+1] % 10) for i in range(len(s) - 1)]
def test(t, rng, draws):
    out = {}
    for name, f in (("full", pairs_full), ("sub", pairs_sub)):
        obs = mi(f(t)); pos = [i for i, v in enumerate(t) if v >= 100]; vals = [t[i] for i in pos]; null = []
        for _ in range(draws):
            rng.shuffle(vals); u = list(t)
            for i, v in zip(pos, vals): u[i] = v
            null.append(mi(f(u)))
        null.sort(); out[name] = (obs, len(f(t)), sum(1 for x in null if x < obs) / draws, null[int(.95 * draws)], sum(null) / draws)
    return out
if __name__ == "__main__":
    t = target_tokens(); rng = random.Random(3); r = test(t, rng, 1000)
    for k, (obs, n, pct, p95, mean) in r.items():
        print(f"TARGET {k}: pairs {n}, MI {obs:.3f} bits, null mean {mean:.3f}, p95 {p95:.3f}, percentile {100*pct:.1f}")
    words = en18_words()
    print(f"\n{'design':7s}{'stat':5s}{'windows':>8s}{'mean MI':>8s}{'mean null':>10s}{'share>p95':>10s}{'share>p99':>10s}")
    for design in ("A", "A2", "B", "Bf", "C", "C2"):
        code = build(words, design, random.Random(7)); res = {"full": [], "sub": []}
        for i in range(60):
            s = simulate(words, code, random.Random(1000 + i)); rr = test(s, random.Random(i), 200)
            for k in res: res[k].append(rr[k])
        for k in res:
            arr = res[k]; print(f"{design:7s}{k:5s}{len(arr):8d}{sum(a[0] for a in arr)/60:8.3f}{sum(a[4] for a in arr)/60:10.3f}{sum(1 for a in arr if a[2] >= .95)/60:10.2f}{sum(1 for a in arr if a[2] >= .99)/60:10.2f}")
