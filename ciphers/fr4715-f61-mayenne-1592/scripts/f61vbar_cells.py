#!/usr/bin/env python3
"""F61-VBAR-CELLS (campaign step H146, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H145's two
genuine cell conflicts between key v4 and the 14-cell map: VBAR_A t/s (v4) vs g/t (14 cells), VBAR_B s (v4) vs f/s. Four
maps (the 14-cell map with the KEY.md equivalences LOOPS = h/u, H24 = i/x, ZBAR = f/s, and VBAR_A x VBAR_B varied) scored by
the H127 sequence gain (null on shuffled text, H128) on: the pooled family drafts (f.97r, f.101r, f.188r, f.124r; H132's
pool) with 30 bootstrap resamples of its lines (seed 146; each resample gets its own 20 shuffles, seeds as H127); f.108v and
the known f.61 lines reported without bootstrap (too short). Pre-registered: on the pool a map is PREFERRED over another when
it has the higher gain in >= 95% of resamples (>= 29 of 30); otherwise the pair is undecided.
  -> scripts/f61vbar_cells_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61seqgain_family as F
G = F.G
def maps():
    base = dict(G.J.cells(), LOOPS="h/u", H24="i/x", ZBAR="f/s"); out = {}
    for a in ("g/t", "t/s"):
        for b in ("f/s", "s/s"): out[f"VBAR_A {a}, VBAR_B {b if b != 's/s' else 's'}"] = dict(base, VBAR_A=a, VBAR_B=b)
    return out
def main():
    M = maps(); pool = {}
    for leaf in ("f97r", "f101r", "f188r", "f124r"):
        for k, v in F.draft(leaf).items(): pool[f"{leaf}_{k}"] = v
    out = []; SH = G.shuffles(pool); full = {n: G.gain(pool, SH, m) for n, m in M.items()}
    out.append("pool gains: " + "; ".join(f"{n} {g:.4f}" for n, g in full.items()))
    keys = sorted(pool); rng = random.Random(146); wins = {(a, b): 0 for a in M for b in M if a != b}
    for _ in range(30):
        R = {f"r{i}": pool[rng.choice(keys)] for i in range(len(keys))}; SR = G.shuffles(R); g = {n: G.gain(R, SR, m) for n, m in M.items()}
        for a, b in wins: wins[(a, b)] += g[a] > g[b]
    names = list(M)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            w = wins[(a, b)]; out.append(f"  {a}  vs  {b}: first wins {w}/30 -> " + ("first PREFERRED" if w >= 29 else ("second PREFERRED" if w <= 1 else "undecided")))
    for tag, name in (("f108v", "f.108v"), ("known_h51", "known f.61 lines")):
        L = G.J.lines(tag); S = G.shuffles(L)
        out.append(f"{name} gains: " + "; ".join(f"{n} {G.gain(L, S, m):.4f}" for n, m in M.items()))
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61vbar_cells_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
