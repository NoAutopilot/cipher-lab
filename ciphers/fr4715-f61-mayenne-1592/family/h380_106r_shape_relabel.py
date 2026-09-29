#!/usr/bin/env python3
"""H380 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, written before running: H379's design on fr.3983 f.106r (the secretary's
hand), rows 1-18. Answers: H231 (rows 1-6) then H368 (rows 1-18; later call wins), both at pass-A (line, pos). A token is used only where the pooled
draft passes/recf106rall18 has, at that (line, position), the same sign as pass A's code (the draft and pass A index alike there). Shape draft: bowl
-> 4TRI, no bowl -> C43; control: 20 drafts with the same answers permuted over the same tokens (seed 380); v7 order gain, mean of seeds 342-344
(h374_split_randctl.gains). Pre-stated as H379 (>= 19/20 'carries order information', <= 9/20 'no better than random', else 'unclear'); fixed now:
the order statistic is underpowered at f.106r's 51 runs (H351), so a miss is 'untestable at this N', not a negative.
python3 h380_106r_shape_relabel.py [--check]"""
import csv, os, random, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
sys.argv = [sys.argv[0], "f97r"]
import h374_split_randctl as h374
def answers():
    lab = {}
    a = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h231_reply.tsv")}
    for r in rd(f"{HERE}/h231_items.tsv"): lab[(r["line"], r["pos"])] = (r["code"], a.get(r["item"]))
    for ch in ("c1", "c2"):
        a = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h368_reply_{ch}.tsv")}
        for r in rd(f"{HERE}/h368_items.tsv"):
            if r["chunk"] == ch: lab[(r["line"], r["pos"])] = (r["code"], a.get(r["item"]))
    return lab
def main():
    rows = list(open(f"{P}/recf106rall18/ciphertext_draft.tsv")); D = {tuple(l.split("\t")[:2]): l.split("\t")[2] for l in rows[1:]}
    lab = answers(); keys = [k for k, (c, a) in sorted(lab.items()) if a in ("yes", "no") and D.get(k) == c]; ans = [lab[k][1] for k in keys]
    def write(m, name):
        new = [rows[0]]
        for l in rows[1:]:
            c = l.rstrip("\n").split("\t"); a = m.get((c[0], c[1]))
            if a == "yes": c[2] = "4TRI"
            elif a == "no": c[2] = "C43"
            new.append("\t".join(c) + "\n")
        os.makedirs(f"{P}/{name}", exist_ok=True); open(f"{P}/{name}/ciphertext_draft.tsv", "w").write("".join(new))
    rng = random.Random(380); rand = []
    try:
        g0 = h374.gains("recf106rall18"); write(dict(zip(keys, ans)), "_h380tmp_shape"); gs = h374.gains("_h380tmp_shape")
        for _ in range(20):
            a = ans[:]; rng.shuffle(a); write(dict(zip(keys, a)), "_h380tmp_rand"); rand.append(h374.gains("_h380tmp_rand"))
    finally:
        for t in ("_h380tmp_shape", "_h380tmp_rand"): shutil.rmtree(f"{P}/{t}", ignore_errors=True)
    beat = sum(gs > r for r in rand); ro = "carries order information" if beat >= 19 else "no better than random" if beat <= 9 else "unclear"
    out = [f"f.106r rows 1-18: {len(keys)} answered tokens usable (yes {ans.count('yes')}, no {ans.count('no')}); order gain v7 mean of 3 seeds: "
           f"as transcribed {g0:.4f}, shape-relabelled {gs:.4f}",
           f"20 permuted-answer drafts: mean {sum(rand) / 20:.4f}, min {min(rand):.4f}, max {max(rand):.4f}",
           f"shape draft beats {beat}/20 -> {ro}" + ("" if beat >= 19 else " (untestable at this N per H351, not a negative)" if beat <= 9 else "")]
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h380_106r_shape_relabel_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
