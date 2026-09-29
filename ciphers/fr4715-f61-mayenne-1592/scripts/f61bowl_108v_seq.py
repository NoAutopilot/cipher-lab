#!/usr/bin/env python3
"""H201 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026), script-only, written before the run. H199 found that on fr.3983 f.108v the bowl
(c/p) sign is the H59 passes' 4STEM (19 of 21 answered), while the skeleton/judge cells key 4STEM a/n. Here the f.108v draft (J.lines('f108v'))
is relabelled by H199's blind bowl answer at every 4-family column (family/h199_bowl_positions.tsv: yes -> c/p, no -> a/n, n -> the readers' cell)
and compared, by H127 sequence gain under the same 14 cells otherwise, with the readers' own cells (4STEM a/n, 4TRI c/p, C43 a/n).
 (1) 30 bootstrap resamples of f.108v's lines (seed 201, H157/H198 design): bowl-relabel CONFIRMED over the readers' cells at >= 29/30 wins,
     readers' PREFERRED at <= 1/30, else OPEN.
 (2) null for the relabel itself: 200 random relabels (seed 2011) that give the same number of c/p (the H199 yes count) to random 4-family columns
     among those H199 answered yes or no; on the whole of f.108v, the bowl relabel's gain is ranked among them. Read-out: "bowl relabel carries
     sequence information" only if (1) is CONFIRMED and (2) ranks it in the top 10 of 201. Otherwise it is logged as untestable/unsupported by
     sequence gain at this N, not as evidence against the bowl rule (which rests on H193/H194's period letters). Descriptive; no key change.
  -> scripts/f61bowl_108v_seq_result.txt [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
FAM = ("4TRI", "C43", "4STEM", "4PI")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def draft():
    D = {}
    for r in rd(f"{HERE}/../family/passes/f108v3z_draft_reconciled.tsv"): D.setdefault(r["line"], []).append((r["position"], r["sign"]))
    return D
def relabel(D, ans):
    return {l: [("4BOWL" if ans.get((l, p)) == "yes" else "4NOB" if ans.get((l, p)) == "no" else s) if s in FAM else s for p, s in v] for l, v in D.items()}
def main():
    D = draft(); L0 = {l: [s for _, s in v] for l, v in D.items()}
    assert L0 == G.J.lines("f108v"), "draft order differs from J.lines('f108v')"
    ans = {(r["line"], r["column"]): r["bowl"] for r in rd(f"{HERE}/../family/h199_bowl_positions.tsv")}
    base = G.J.cells(); MB = dict(base, **{"4BOWL": "c/p", "4NOB": "a/n"}); LB = relabel(D, ans)
    fam_cols = [(l, p) for l, v in D.items() for p, s in v if s in FAM and ans.get((l, p)) in ("yes", "no")]
    ny = sum(1 for c in fam_cols if ans[c] == "yes")
    out = [f"f.108v 4-family columns answered yes/no: {len(fam_cols)} (bowl yes {ny}); relabelled tokens: 4BOWL {sum(s.count('4BOWL') for s in LB.values())}, 4NOB {sum(s.count('4NOB') for s in LB.values())}"]
    keys = sorted(L0); rng = random.Random(201); w = 0
    for _ in range(30):
        pick = [rng.choice(keys) for _ in keys]
        R0 = {f"r{i}": L0[k] for i, k in enumerate(pick)}; RB = {f"r{i}": LB[k] for i, k in enumerate(pick)}
        w += G.gain(RB, G.shuffles(RB), MB) > G.gain(R0, G.shuffles(R0), base)
    v1 = "bowl relabel CONFIRMED" if w >= 29 else ("readers' cells PREFERRED" if w <= 1 else "OPEN")
    out.append(f"(1) bowl relabel vs readers' cells, 30 resamples: bowl wins {w}/30 -> {v1}")
    gB = G.gain(LB, G.shuffles(LB), MB); g0 = G.gain(L0, G.shuffles(L0), base); rn = random.Random(2011); null = []
    for _ in range(200):
        yes = set(rn.sample(fam_cols, ny)); a2 = {c: ("yes" if c in yes else "no") for c in fam_cols}
        LR = relabel(D, a2); null.append(G.gain(LR, G.shuffles(LR), MB))
    rank = 1 + sum(1 for x in null if x >= gB); null.sort(reverse=True)
    out.append(f"(2) whole f.108v: bowl relabel gain {gB:.3f}, readers' cells {g0:.3f}; rank of bowl relabel among 200 random relabels {rank} of 201 (best {null[0]:.3f}, median {null[100]:.3f})")
    ok = w >= 29 and rank <= 10
    out.append("read-out: " + ("bowl relabel carries sequence information on f.108v" if ok else "not supported by sequence gain at this N (untestable/unsupported, not evidence against the bowl rule)"))
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61bowl_108v_seq_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
