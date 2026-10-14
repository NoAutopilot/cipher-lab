"""P0 of PREREG-FAIR-IC: IC and sorted-frequency-profile rank of the fair-game marks per LANG_CORPORA key
(2000 word-start windows each, 200 uniform-random strings as the floor).
Run: python3 ciphers/fair-game-2010/ic/ic_rank.py [--check]  (--check: exit 1 if ic_rank.json is stale)"""
import json, os, random, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "../../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
from families.transposition import word_window  # noqa: E402

AZ = "abcdefghijklmnopqrstuvwxyz"


def nfkd(t):
    return unicodedata.normalize("NFKD", t)


def fold(t):
    return "".join(c for c in nfkd(t).lower() if "a" <= c <= "z")


def ic(t):
    n = len(t)
    return sum(v * (v - 1) for v in Counter(t).values()) / (n * (n - 1))


def prof(t):
    c = Counter(t)
    return sorted((c[a] for a in AZ), reverse=True)


tgt = fold(open(os.path.join(HERE, "../test2/order_scroll.txt")).read())
N = len(tgt)
rng = random.Random(20261014)
uni = ["".join(rng.choice(AZ) for _ in tgt) for _ in range(200)]
out = {"N": N, "windows": 2000, "target_ic": round(ic(tgt), 5), "langs": {}}
for L, paths in jp.LANG_CORPORA.items():
    raw = nfkd("\n".join(jp.read_corpus(p) for p in paths))
    wins = [fold(word_window(raw, N, seed, margin=0, want_rest=False)[0]) for seed in range(1, 2001)]
    wins = [w[:N] for w in wins]
    ics = sorted(ic(w) for w in wins)
    profs = [prof(w) for w in wins]
    ref = [sum(p[i] for p in profs) / len(profs) for i in range(26)]
    d = lambda t: sum(abs(a - b) for a, b in zip(prof(t), ref))
    ds = sorted(d(w) for w in wins)
    ti, td = ic(tgt), d(tgt)
    ui = sorted(ic(u) for u in uni)
    ud = sorted(d(u) for u in uni)
    s1 = sum(v < ti for v in ics) / len(ics)
    s2 = sum(v > td for v in ds) / len(ds)
    out["langs"][L] = {
        "ic": {"target": round(ti, 5), "pct_rank": round(s1, 4), "p01": round(ics[19], 5), "median": round(ics[1000], 5),
               "random_median": round(ui[100], 5), "random_share_below_p01": round(sum(u < ics[19] for u in ui) / 200, 3)},
        "profile": {"target": round(td, 3), "pct_rank": round(s2, 4), "p99": round(ds[1979], 3), "median": round(ds[1000], 3),
                    "random_median": round(ud[100], 3), "random_share_above_p99": round(sum(u > ds[1979] for u in ud) / 200, 3)},
        "survives": s1 >= 0.01 and s2 >= 0.01, "min_rank": round(min(s1, s2), 4)}
path = os.path.join(HERE, "ic_rank.json")
if "--check" in sys.argv:
    sys.exit(0 if json.load(open(path)) == out else 1)
json.dump(out, open(path, "w"), indent=1)
print("target IC", out["target_ic"])
for L, r in sorted(out["langs"].items(), key=lambda kv: -kv[1]["min_rank"]):
    print(L, r["survives"], r["ic"]["pct_rank"], r["ic"]["p01"], r["ic"]["median"], r["ic"]["random_share_below_p01"],
          r["profile"]["pct_rank"], r["profile"]["target"], r["profile"]["p99"], r["profile"]["random_share_above_p99"], sep="\t")
