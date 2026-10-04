"""RUN3-SANG diagnostic (control-only, not a gate): recovery of the crib=drag control when the planted crib's
signs are pinned to their TRUE letters (no drag) -- the ceiling a perfect crib guess could reach at N=232, K~62.
Run from the repo root: python3 ciphers/sanguszkow-mniszech-dunin-1714/crib/oracle_ceiling.py"""
import glob, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp
import homophonic_anneal as ha
from families import homophonic as h

spec = json.load(open(os.path.join(ROOT, "specs/sanguszkow-mniszech-dunin-1714.json")))
t = spec["ciphertext"].split()
corp = [jp.read_corpus(p) for p in sorted(glob.glob(os.path.join(ROOT, "tools/data/pl18/*.txt.gz")))]
out = []
for s in (1, 2, 3):
    P = {"N": 232, "K": 77, "target_msgs": [t], "profile": "target", "crib": "drag"}
    cm, plain, train = h.make_control(spec, s, corp, P)
    seq = cm[0]
    g, s6, b, s2 = h._plant_targets(plain)
    fx = {seq[i + j]: plain[i + j] for i in s6[:1] for j in range(6)}
    fx.update({seq[i + j]: plain[i + j] for i in s2[:1] for j in range(2)})
    model = ha.Model(train, 3)
    sc, key = ha.solve(seq, model, 8, 40000, s, 1.0, fixed=fx)[0]
    dec = "".join(key[x] for x in seq)
    rec = h.score_recovery(dec, plain)
    un = [(key[x], a) for x, a in zip(seq, plain) if x not in fx]
    out.append({"seed": s, "planted": [g, b], "pinned_tokens": sum(1 for x in seq if x in fx),
                "recovery": round(rec, 3), "unpinned": round(sum(u == v for u, v in un) / len(un), 3)})
    print(json.dumps(out[-1]))
print("mean recovery %.3f" % (sum(o["recovery"] for o in out) / 3))
