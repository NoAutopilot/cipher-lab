#!/usr/bin/env python3
"""H205 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026): does the H85/H94 model judge prefer f.108v read with H199's bowl labels over
the same text read with the H59 pass codes? Written before any call.
Why head-to-head: under the pass codes f.108v already ranked 1 of 21 in every earlier judge run (H85 s101-103, H94 s104, H100 swap s105/106), so a
rank-1 gate cannot tell the two labellings apart.
 control: `f61judge108v.py build known_h51 --seed 207 --swap` (the H100 one-swap hard null on the known f.61 span lines, fresh seed), H94 no-leak
   prompt; gate target rank 1 of 21, ties against. A FAIL stops the step (target not built).
 target: `f61judge108v_bowl.py build --seed 207`: 21 sets of the f.108v draft relabelled by bowl (family/h199_bowl_positions.tsv: yes -> 4BOWL c/p,
   no -> 4NOB a/n, n -> pass code): SET target = the 14 cells + 4BOWL c/p + 4NOB a/n; SET R = the same tokens read with the pass codes' own cells
   (4STEM a/n, 4TRI c/p, C43 a/n: the H85 decode); 19 sets = the target map with one swap of two classes whose cells differ (distinct, seed 207).
   Order shuffled (seed 207); key never named. One call, H94 no-leak prompt, file name and line list changed.
 read-out (pre-stated): "the judge prefers the bowl labelling" iff the target ranks 1 of 21 (ties against) AND scores strictly above R; "prefers
   the pass codes" iff R scores strictly above the target; else "no preference shown". Descriptive; no key change.
H208 (same runner, written before its calls): --present draws the 19 one-swap neighbours only from class pairs that both occur in the relabelled
   text (H205's pool included 4TRI/4PI/C43, absent after the relabel, so two neighbours equalled the target); files f61judge_f108v_bowlp_s<N>_*;
   seeds 208 and 209; read-out per seed as above; "prefers the bowl labelling" overall only if both seeds say so.
  python3 f61judge108v_bowl.py build --seed N [--present] | score --seed N [--present] [--check]"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
FAM = ("4TRI", "C43", "4STEM", "4PI"); PRES = "--present" in sys.argv
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def data():
    import f61judge108v as J
    C = J.cells(); ans = {(r["line"], r["column"]): r["bowl"] for r in rd(f"{HERE}/../family/h199_bowl_positions.tsv")}
    D = {}
    for r in rd(f"{HERE}/../family/passes/f108v3z_draft_reconciled.tsv"): D.setdefault(r["line"], []).append((r["position"], r["sign"]))
    orig = {l: [s for _, s in v] for l, v in D.items()}
    assert orig == J.lines("f108v")
    rel = {l: [("4BOWL" if ans.get((l, p)) == "yes" else "4NOB" if ans.get((l, p)) == "no" else s) if s in FAM else s for p, s in v] for l, v in D.items()}
    return C, orig, rel
def build(seed):
    C, orig, rel = data(); M = dict(C, **{"4BOWL": "c/p", "4NOB": "a/n"}); labs = sorted(M); rng = random.Random(seed)
    pres = {c for v in rel.values() for c in v}
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:] if M[a] != M[b] and (not PRES or (a in pres and b in pres))]; rng.shuffle(pairs)
    assert len(pairs) >= 19
    def dec(L, m): return {l: [m[c] for c in s if c in m] for l, s in L.items()}
    sets = [("T", dec(rel, M)), ("R", dec(orig, C))]
    for a, b in pairs[:19]:
        m = dict(M); m[a], m[b] = M[b], M[a]; sets.append((f"swap {a}<->{b}", dec(rel, m)))
    assert all(len(sets[0][1][l]) == len(sets[1][1][l]) for l in rel)
    order = list(range(21)); random.Random(seed).shuffle(order); key = {}; txt = []; name = f"f108v_bowl{'p' if PRES else ''}_s{seed}"
    for k, i in enumerate(order):
        lab = f"SET-{k+1:02d}"; key[lab] = sets[i][0]; txt.append(f"== {lab}")
        for l, cells in sets[i][1].items(): txt.append(f"{l}: " + " ".join(f"[{c}]" for c in cells))
    open(f"{HERE}/f61judge_{name}_sets.txt", "w").write("\n".join(txt) + "\n")
    json.dump({"tag": name, "key": key}, open(f"{HERE}/f61judge_{name}_key.json", "w"), indent=1)
    diff = sum(1 for l in rel for x, y in zip(sets[0][1][l], sets[1][1][l]) if x != y)
    print(f"wrote f61judge_{name}_sets.txt: {sum(len(v) for v in sets[0][1].values())} positions per set; target and R differ at {diff}")
def score(seed):
    name = f"f108v_bowl{'p' if PRES else ''}_s{seed}"; key = json.load(open(f"{HERE}/f61judge_{name}_key.json"))["key"]
    rows = rd(f"{HERE}/f61judge_{name}_verdict.tsv"); sc = {r["label"].strip(): float(r["score_0_10"]) for r in rows}
    assert set(sc) == set(key)
    t = [l for l, v in key.items() if v == "T"][0]; r_ = [l for l, v in key.items() if v == "R"][0]
    rank = 1 + sum(1 for l, v in sc.items() if l != t and v >= sc[t])
    ro = ("the judge prefers the bowl labelling" if rank == 1 and sc[t] > sc[r_] else
          "the judge prefers the pass codes" if sc[r_] > sc[t] else "no preference shown")
    out = [f"{name}: target {t} scored {sc[t]:.1f}, rank {rank} of 21 (ties against); pass-code set {r_} scored {sc[r_]:.1f}",
           "all scores: " + " ".join(f"{l}({key[l].split()[0]}):{sc[l]:.1f}" for l in sorted(sc, key=lambda l: -sc[l])),
           "target reading as given by the judge: " + next(r["reading"] for r in rows if r["label"].strip() == t),
           f"read-out: {ro}"]
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61judge_{name}_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    s = int(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else 207
    build(s) if sys.argv[1] == "build" else score(s)
