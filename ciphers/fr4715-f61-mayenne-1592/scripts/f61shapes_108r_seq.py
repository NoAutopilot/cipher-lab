#!/usr/bin/env python3
"""H217 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026), script-only, written before the run. f.108r L04-L06 (H108 draft, J.lines
'f108r_L04_L06_h108' order = scripts/f61recon108r_draft.tsv rows with DBL -> PHI) relabelled by shape: 4TRI/C43/4STEM by H216's bowl answer (yes ->
4BOWL c/p, no -> 4NOB a/n; 4PI left as coded, it is not a bowl-question sign), HASH4 by H212's form (A -> HASHA d/q, B -> HASHB i/x; matched on
line, segment, x). Map = the 14 cells + 4BOWL c/p + 4NOB a/n + HASHA d/q + HASHB i/x; against the pass codes under the 14 cells + HASH4 i/x (H127's
best f.108r row). H201's design: (1) 30 bootstrap resamples (seed 217), shapes CONFIRMED at >= 29/30, pass codes PREFERRED at <= 1/30, else OPEN;
(2) the same shape counts placed at random among the answered 4-family and HASH4 positions, 200 draws (seed 2171), rank of the real placement.
Descriptive.  -> scripts/f61shapes_108r_seq_result.txt [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def main():
    F = f"{HERE}/../family"; rows = rd(f"{HERE}/f61recon108r_draft.tsv")
    L0 = {}
    for r in rows: L0.setdefault(r["line"], []).append("PHI" if r["sign"] == "DBL" else r["sign"])
    assert L0 == G.J.lines("f108r_L04_L06_h108")
    bowl = {(r["line"], r["position"]): r["bowl"] for r in rd(f"{F}/h216_bowl_positions.tsv")}
    key = {r["item"]: r for r in rd(f"{F}/h212_items.tsv")}; grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{F}/passes/h212_sort.tsv")}
    form = {(k["line"], k["segment"], k["x_px"]): grp[m] for m, k in key.items() if k["leaf"] == "108r"}
    def lab(r, b, f):
        s = "PHI" if r["sign"] == "DBL" else r["sign"]
        if s in ("4TRI", "C43", "4STEM") and b in ("yes", "no"): return "4BOWL" if b == "yes" else "4NOB"
        if s == "HASH4" and f in ("A", "B"): return "HASH" + f
        return s
    pos = [(r, bowl.get((r["line"], r["position"])), form.get((r["line"], r["segment"], r["x_px"]))) for r in rows]
    def build(P):
        L = {}
        for r, b, f in P: L.setdefault(r["line"], []).append(lab(r, b, f))
        return L
    LS = build(pos); C = G.J.cells(); M0 = dict(C, HASH4="i/x"); MS = dict(C, **{"4BOWL": "c/p", "4NOB": "a/n", "HASHA": "d/q", "HASHB": "i/x"})
    out = [f"shape labels: 4BOWL {sum(v.count('4BOWL') for v in LS.values())}, 4NOB {sum(v.count('4NOB') for v in LS.values())}, HASHA {sum(v.count('HASHA') for v in LS.values())}, HASHB {sum(v.count('HASHB') for v in LS.values())}"]
    keys = sorted(L0); rng = random.Random(217); w = 0
    for _ in range(30):
        pick = [rng.choice(keys) for _ in keys]; R0 = {f"r{i}": L0[k] for i, k in enumerate(pick)}; RS = {f"r{i}": LS[k] for i, k in enumerate(pick)}
        w += G.gain(RS, G.shuffles(RS), MS) > G.gain(R0, G.shuffles(R0), M0)
    out.append(f"(1) shapes vs pass codes (HASH4 i/x), 30 resamples: shapes win {w}/30 -> " + ("shapes CONFIRMED" if w >= 29 else ("pass codes PREFERRED" if w <= 1 else "OPEN")))
    gS = G.gain(LS, G.shuffles(LS), MS); g0 = G.gain(L0, G.shuffles(L0), M0)
    fb = [i for i, (r, b, f) in enumerate(pos) if r["sign"] in ("4TRI", "C43", "4STEM") and b in ("yes", "no")]; fh = [i for i, (r, b, f) in enumerate(pos) if r["sign"] == "HASH4" and f in ("A", "B")]
    nb = sum(1 for i in fb if pos[i][1] == "yes"); na = sum(1 for i in fh if pos[i][2] == "A"); rn = random.Random(2171); null = []
    for _ in range(200):
        yb = set(rn.sample(fb, nb)); ya = set(rn.sample(fh, na)); P = list(pos)
        for i in fb: P[i] = (pos[i][0], "yes" if i in yb else "no", pos[i][2])
        for i in fh: P[i] = (pos[i][0], pos[i][1], "A" if i in ya else "B")
        L = build(P); null.append(G.gain(L, G.shuffles(L), MS))
    rank = 1 + sum(1 for x in null if x >= gS); null.sort(reverse=True)
    out.append(f"(2) whole rows: shapes gain {gS:.3f}, pass codes {g0:.3f}; rank of the real shape placement among 200 random placements {rank} of 201 (best {null[0]:.3f}, median {null[100]:.3f})")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61shapes_108r_seq_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
