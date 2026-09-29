#!/usr/bin/env python3
"""VERIFY-F61-V6 task 3a: H201 re-scored with the verifier's seeds. Same draft, cells and gain as scripts/f61bowl_108v_seq.py, but:
 within-line shuffle seeds 6000-6019 (not 1270-1289); 30 bootstrap resamples seed 6201; null = 1000 random relabels (seed 6202) giving
 c/p to exactly as many answered 4-family columns as the H199 yes count, the rest a/n (same yes/no counts); plus two named alternatives:
 CODE = reader code only (4STEM c/p, every other 4-family a/n -- what a code-level rule would do on this leaf) and READERS (the skeleton's
 cells). Read-out as H201's: bowl rank <= 1% of the null and bootstrap wins >= 29/30 over READERS. The bowl-vs-CODE margin is reported
 because on f.108v the bowl coincides with 4STEM on most columns.  python3 rescore_h201.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, S)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61bowl_108v_seq as B
G = B.G
def shuffles(L):
    out = []
    for seed in range(6000, 6020):
        rng = random.Random(seed); SS = {}
        for l, v in L.items(): v = list(v); rng.shuffle(v); SS[l] = v
        out.append(SS)
    return out
def gain(L, m): SH = shuffles(L); return G.H.score(L, m) - sum(G.H.score(x, m) for x in SH) / len(SH)
def main():
    D = B.draft(); L0 = {l: [s for _, s in v] for l, v in D.items()}
    ans = {(r["line"], r["column"]): r["bowl"] for r in B.rd(f"{HERE}/../family/h199_bowl_positions.tsv")}
    base = G.J.cells(); MB = dict(base, **{"4BOWL": "c/p", "4NOB": "a/n"}); LB = B.relabel(D, ans)
    cols = [(l, p) for l, v in D.items() for p, s in v if s in B.FAM and ans.get((l, p)) in ("yes", "no")]; ny = sum(ans[c] == "yes" for c in cols)
    code = {c: ("yes" if dict(D[c[0]])[c[1]] == "4STEM" else "no") for c in cols}; LC = B.relabel(D, code)
    gB, g0, gC = gain(LB, MB), gain(L0, base), gain(LC, MB)
    out = [f"f.108v answered 4-family columns {len(cols)}, bowl yes {ny}; CODE relabel yes {sum(v == 'yes' for v in code.values())}, agreeing with bowl on {sum(code[c] == ans[c] for c in cols)}/{len(cols)}",
           f"gain (shuffle seeds 6000-6019): bowl {gB:.3f}, CODE {gC:.3f}, READERS {g0:.3f}"]
    keys = sorted(L0); rng = random.Random(6201); w = wc = 0
    for _ in range(30):
        pick = [rng.choice(keys) for _ in keys]
        RB = {f"r{i}": LB[k] for i, k in enumerate(pick)}; R0 = {f"r{i}": L0[k] for i, k in enumerate(pick)}; RC = {f"r{i}": LC[k] for i, k in enumerate(pick)}
        b = gain(RB, MB); w += b > gain(R0, base); wc += b > gain(RC, MB)
    out.append(f"bootstrap (seed 6201): bowl beats READERS {w}/30, beats CODE {wc}/30")
    rn = random.Random(6202); null = []
    for _ in range(1000):
        yes = set(rn.sample(cols, ny)); LR = B.relabel(D, {c: ("yes" if c in yes else "no") for c in cols}); null.append(gain(LR, MB))
    null.sort(reverse=True); rank = 1 + sum(x >= gB for x in null); rc = 1 + sum(x >= gC for x in null)
    out.append(f"null, 1000 random relabels with the same yes/no counts (seed 6202): bowl rank {rank} of 1001, CODE rank {rc}; best {null[0]:.3f}, p99 {null[9]:.3f}, median {null[500]:.3f}")
    out.append("read-out: " + ("bowl relabel carries sequence information on f.108v (reproduced)" if w >= 29 and rank <= 10 else "NOT reproduced at the verifier's seeds"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/rescore_h201_result.txt"
    if "--check" in ARGS:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
