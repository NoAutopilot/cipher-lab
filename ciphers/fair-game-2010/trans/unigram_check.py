"""G0 of PREREG-FAIR-TRANS: letter-count log-likelihood of the fair-game marks vs 2000 English word-start windows.
Run: python3 ciphers/fair-game-2010/trans/unigram_check.py [--check]  (--check: exit 1 if unigram.json is stale)"""
import json, math, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "../../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
from families.transposition import fold26, word_window  # noqa: E402

raw = "\n".join(open(p, encoding="utf-8", errors="ignore").read() for p in jp.LANG_CORPORA["en"])
s = fold26(raw)
c = Counter(s)
lp = {a: math.log((c[a] + 0.5) / (len(s) + 13)) for a in "abcdefghijklmnopqrstuvwxyz"}
ll = lambda t: sum(lp[x] for x in t) / len(t)
tgt = fold26(open(os.path.join(HERE, "../test2/order_scroll.txt")).read())
vals = sorted(ll(word_window(raw, len(tgt), seed, margin=0, want_rest=False)[0]) for seed in range(1, 2001))
t = ll(tgt)
out = {"N": len(tgt), "target_ll_per_letter": round(t, 4), "pct_rank": round(sum(v < t for v in vals) / len(vals), 4),
       "p01": round(vals[19], 4), "p05": round(vals[99], 4), "median": round(vals[1000], 4), "windows": len(vals)}
path = os.path.join(HERE, "unigram.json")
if "--check" in sys.argv:
    sys.exit(0 if json.load(open(path)) == out else 1)
json.dump(out, open(path, "w"), indent=1)
print(out)
