"""L0 of PREREG-FAIR-LANG: letter-count rank of the fair-game marks per LANG_CORPORA key (2000 word-start windows each).
Run: python3 ciphers/fair-game-2010/lang/lang_rank.py [--check]  (--check: exit 1 if lang_rank.json is stale)"""
import json, math, os, random, sys, unicodedata
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


tgt = fold(open(os.path.join(HERE, "../test2/order_scroll.txt")).read())
out = {"N": len(tgt), "windows": 2000, "langs": {}}
for L, paths in jp.LANG_CORPORA.items():
    raw = nfkd("\n".join(jp.read_corpus(p) for p in paths))
    s = fold(raw)
    c = Counter(s)
    lp = {a: math.log((c[a] + 0.5) / (len(s) + 13)) for a in AZ}
    ll = lambda t: sum(lp[x] for x in t) / len(t)
    vals = sorted(ll(word_window(raw, len(tgt), seed, margin=0, want_rest=False)[0]) for seed in range(1, 2001))
    t = ll(tgt)
    rng = random.Random(20261014)  # reference: 200 uniform-random 26-letter strings of length N (flat letter counts)
    uni = sorted(ll("".join(rng.choice(AZ) for _ in tgt)) for _ in range(200))
    out["langs"][L] = {"target": round(t, 4), "pct_rank": round(sum(v < t for v in vals) / len(vals), 4),
                       "p01": round(vals[19], 4), "p05": round(vals[99], 4), "median": round(vals[1000], 4),
                       "uniform_median": round(uni[100], 4),
                       "uniform_share_below_p01": round(sum(u < vals[19] for u in uni) / len(uni), 3)}
path = os.path.join(HERE, "lang_rank.json")
if "--check" in sys.argv:
    sys.exit(0 if json.load(open(path)) == out else 1)
json.dump(out, open(path, "w"), indent=1)
for L, r in sorted(out["langs"].items(), key=lambda kv: -kv[1]["pct_rank"]):
    print(L, r["pct_rank"], r["target"], r["p01"], r["median"], r["uniform_median"], r["uniform_share_below_p01"], sep="\t")
