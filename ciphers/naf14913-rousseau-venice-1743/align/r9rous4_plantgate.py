#!/usr/bin/env python3
"""R9-ROUS4 (6 Oct 2026): count-vector gate re-registered with a same-class planted known-answer (align/PREREG-R9-ROUS4.md).
Reuses align/r8rous3_countgate.py's units, normalisation and controls. Run from the target folder:
python3 align/r9rous4_plantgate.py > align/r9rous4_plantgate.out"""
import itertools, random, csv
from collections import Counter

src = open("align/r8rous3_countgate.py").read().split("rng = random")[0]
exec(src)  # PAIRS, groups(), words(), G, W, redeal(), DRAWS, ALPHA, codes

C_CODES = {r["code"] for r in csv.DictReader(open("key.tsv"), delimiter="\t") if r["grade"] == "C"}
PROTECT = C_CODES | {"605", "739", "52"}
CANDS = [("605", "republique"), ("739", "venise")]
NPLANT, LIC = 40, 32

def gate(Gs, Ws, c, w, seed):
    gc_ = [Counter(g) for g in Gs]; wc_ = [Counter(x) for x in Ws]
    v = tuple(x[c] for x in gc_); u = tuple(x[w] for x in wc_)
    allc = set().union(*Gs)
    same = [k for k in allc if tuple(x[k] for x in gc_) == u]
    rng = random.Random(seed)
    S = [redeal(Ws, rng) for _ in range(DRAWS)]
    Gd = [redeal(Gs, rng) for _ in range(DRAWS)]
    ps = sum(v == tuple(d[i][w] for i in range(4)) for d in S) / DRAWS
    pg = sum(tuple(d[i][c] for i in range(4)) == u for d in Gd) / DRAWS
    match = v == u and sum(u) >= 3
    uniq = same == [c]
    return dict(v=v, u=u, match=match, unique=uniq, same=sorted(same)[:6], ps=ps, pg=pg,
                rec=match and uniq and ps <= ALPHA and pg <= ALPHA)

def klass(u):
    t = sum(u)
    return [vv for vv in itertools.product(range(1, 4), repeat=4) if abs(sum(vv) - t) <= 1]

prng = random.Random(9)
print(f"# sizes groups {[len(g) for g in G]} slip tokens {[len(w) for w in W]} draws {DRAWS}; protected codes {len(PROTECT)}")
idx = 0
for c, w in CANDS:
    real = gate(G, W, c, w, 8)
    u = real["u"]; K = klass(u)
    print(f"CAND\t{c}={w}\tcode {real['v']} word {u}\tMATCH {real['match']} UNIQUE {real['unique']}\tp_s {real['ps']:.4f} p_g {real['pg']:.4f}"
          f"\t{'recovered' if real['rec'] else 'not recovered'}\tclass size {len(K)} (totals {min(map(sum,K))}-{max(map(sum,K))})")
    nrec = 0
    for k in range(NPLANT):
        vv = prng.choice(K)
        Gp = [list(g) for g in G]; Wp = [list(x) for x in W]
        for p in range(4):
            free = [i for i, t in enumerate(Gp[p]) if t not in PROTECT]
            for i in prng.sample(free, vv[p]): Gp[p][i] = "9999"
            for _ in range(vv[p]): Wp[p].insert(prng.randint(0, len(Wp[p])), "zzplant")
        r = gate(Gp, Wp, "9999", "zzplant", 9 + idx); idx += 1
        nrec += r["rec"]
        print(f"plant\t{c}\t{k}\tvec {vv}\tMATCH {r['match']} UNIQUE {r['unique']} {'' if r['unique'] else r['same']}\tp_s {r['ps']:.4f} p_g {r['pg']:.4f}\t{'REC' if r['rec'] else '-'}")
    lic = nrec >= LIC
    verdict = "FAIL" if not real["match"] else ("PASS" if real["rec"] and lic else "NON-INFORMATIVE")
    print(f"LICENCE\t{c}={w}\tplanted recovered {nrec}/{NPLANT} (need {LIC}) -> {'MET' if lic else 'NOT MET'}")
    print(f"VERDICT\t{c}={w}\t{verdict}\tcandidate p_s {real['ps']:.4f} p_g {real['pg']:.4f}; class recovery {nrec}/{NPLANT}")
