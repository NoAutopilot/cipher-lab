#!/usr/bin/env python3
"""F61-108R-HASH4 (campaign step H114, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only, no model call.
H112's judge found no French on f.108r L04-L06 under the 14-cell map, which drops HASH4 (10 of 85 draft signs; d/q under
the 4-over-hash on the family leaves, H98 17/19). Does adding HASH4 = d/q move these rows toward French?

Instrument: for a map, each line is resolved by a beam search (width 400) over the x/y choice at each covered sign,
maximising tools/judge_plaintext.NgramModel (fr16, 4-gram) log10 probability; a map's score is the letter-weighted mean
per-letter log10 over the lines. Null: 200 permutations of the map's cell values across its classes (seed 114); statistic:
the fitted map's rank among the 201. Pre-registered gates (this docstring, pushed before the first run):
  CONTROL -- the known f.61 span lines (f61judge108v.lines("known_h51"), the H85/H94 control text) under the 14-cell map:
            the fitted map must rank in the top 5% (rank <= 10 of 201). Below it the instrument cannot see a known key at
            this length and the target figures are reported as a non-test.
  TARGET  -- f.108r L04-L06 (the H108 draft as H112 built it) under (a) the 14 cells, (b) the 14 cells + HASH4 = d/q.
            Reported: rank and percentile of each; "moves toward French" only if (b) ranks in the top 5% and (a) does not.
  python3 scripts/f61hash4_108r.py [--check]   -> scripts/f61hash4_108r_result.txt
"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); sys.path.insert(0, f"{ROOT}/tools"); sys.path.insert(0, HERE)
sys.argv, ARGS = sys.argv[:1], sys.argv[1:]
import judge_plaintext as jp
import f61judge108v as J
M = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr"]])
import math
def lp(g): return math.log10((M.c.get(g, 0) + M.k) / (M.ctx.get(g[:-1], 0) + 26 * M.k))
def resolve(pairs, W=400):
    beam = [("", 0.0)]
    for a, b in pairs:
        nb = {}
        for s, v in beam:
            for ch in (a, b):
                t = s + ch; w = v + (lp(t[-4:]) if len(t) >= 4 else 0.0)
                if t[-3:] not in nb or nb[t[-3:]][1] < w: nb[t[-3:]] = (t, w)   # recombine on the 3-letter state
        beam = sorted(nb.values(), key=lambda x: -x[1])[:W]
    s, v = beam[0]; return s, v, max(len(s) - 3, 0)
def score(lines, m):
    tot = n = 0
    for seq in lines.values():
        pairs = [tuple(jp.fold(x) for x in m[c].split("/")) for c in seq if c in m]
        _, v, k = resolve(pairs); tot += v; n += k
    return tot / n if n else -9.9
def rank(lines, C, seed=114, N=200):
    labs = sorted(C); rng = random.Random(seed); t = score(lines, C); null = []
    for _ in range(N):
        v = [C[l] for l in labs]; rng.shuffle(v); null.append(score(lines, dict(zip(labs, v))))
    r = 1 + sum(1 for x in null if x >= t); null.sort(reverse=True)
    return t, r, null[0], null[len(null) // 2], null[int(0.05 * N)]
def main():
    C = J.cells(); CH = dict(C, HASH4="d/q"); out = []
    known = J.lines("known_h51"); tgt = J.lines("f108r_L04_L06_h108")
    t, r, b, med, p5 = rank(known, C); ok = r <= 10
    out.append(f"CONTROL known f.61 span lines, 14 cells: fitted {t:.3f}, rank {r} of 201 (best permuted {b:.3f}, median {med:.3f}, 5th-best {p5:.3f}) -> {'PASS' if ok else 'FAIL'} (rank <= 10)")
    res = {}
    for name, m in (("(a) 14 cells", C), ("(b) 14 cells + HASH4=d/q", CH)):
        cov = sum(1 for s in tgt.values() for c in s if c in m); t, r, b, med, p5 = rank(tgt, m); res[name] = r
        out.append(f"TARGET f.108r L04-L06 {name}: {cov} covered signs; fitted {t:.3f}, rank {r} of 201 (percentile {100 * (r - 1) / 201:.1f}); best permuted {b:.3f}, median {med:.3f}")
    moved = res["(b) 14 cells + HASH4=d/q"] <= 10 and res["(a) 14 cells"] > 10
    out.append("VERDICT: " + ("control FAIL -- target figures are a non-test" if not ok else
               ("HASH4 = d/q moves f.108r L04-L06 into the top 5%" if moved else "HASH4 = d/q does not move f.108r L04-L06 into the top 5% where the 14 cells were not already")))
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61hash4_108r_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
