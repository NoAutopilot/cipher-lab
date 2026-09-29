#!/usr/bin/env python3
"""H379 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, written before running: fr.3983 f.108v (f.61's hand) relabelled by
shape. Base draft: H59's reconciled draft passes/f108v3z_draft_reconciled.tsv (the draft H199's columns index, 74/74 checked), not rec108v (27/74).
Shape draft: each of H199's 74 targets (h199_bowl_positions.tsv) answered 'yes' becomes 4TRI (v7's c/p/t cell), 'no' becomes C43 (a/n); 'n' unchanged.
Control: 20 drafts with H199's yes/no answers permuted across the same answered targets (seed 379) -- same counts, random placement. Each draft scored
with H360/H374's order gain for v7 (mean of seeds 342-344), drafts written to temporary passes/_h379tmp_*/ and removed. Pre-stated as H374: the shape
draft 'carries order information' iff it beats >= 19/20 permuted drafts; 'no better than random' iff <= 9/20; else 'unclear'; the as-transcribed
gain is reported beside it. Caveat fixed now: f.108v's order signal for v7 is thin (H353, 8 runs), so a miss here is weak evidence either way.
python3 h379_108v_shape_relabel.py [--check]"""
import csv, os, random, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
sys.argv = [sys.argv[0], "f97r"]
import h374_split_randctl as h374
def draft(lab, name):
    rows = rd(f"{P}/f108v3z_draft_reconciled.tsv"); os.makedirs(f"{P}/{name}", exist_ok=True); cols = list(rows[0])
    with open(f"{P}/{name}/ciphertext_draft.tsv", "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            a = lab.get((r["line"], r["position"]))
            if a == "yes": r["sign"] = "4TRI"
            elif a == "no": r["sign"] = "C43"
            f.write("\t".join(r[c] for c in cols) + "\n")
def main():
    H = rd(f"{HERE}/h199_bowl_positions.tsv"); keys = [(h["line"], h["column"]) for h in H if h["bowl"] in ("yes", "no")]
    ans = [h["bowl"] for h in H if h["bowl"] in ("yes", "no")]; rng = random.Random(379); tmp = []
    try:
        draft({}, "_h379tmp_base"); tmp.append("_h379tmp_base"); g0 = h374.gains("_h379tmp_base")
        draft(dict(zip(keys, ans)), "_h379tmp_shape"); tmp.append("_h379tmp_shape"); gs = h374.gains("_h379tmp_shape"); rand = []
        for d in range(20):
            a = ans[:]; rng.shuffle(a); draft(dict(zip(keys, a)), "_h379tmp_rand"); tmp.append("_h379tmp_rand"); rand.append(h374.gains("_h379tmp_rand"))
    finally:
        for t in set(tmp): shutil.rmtree(f"{P}/{t}", ignore_errors=True)
    beat = sum(gs > r for r in rand); ro = "carries order information" if beat >= 19 else "no better than random" if beat <= 9 else "unclear"
    out = [f"f.108v H59 draft: {len(keys)} H199 targets answered (yes {ans.count('yes')}, no {ans.count('no')}); order gain v7 (mean of 3 seeds): "
           f"as transcribed {g0:.4f}, shape-relabelled {gs:.4f}",
           f"20 permuted-answer drafts: mean {sum(rand) / 20:.4f}, min {min(rand):.4f}, max {max(rand):.4f}; values " + " ".join(f"{r:.4f}" for r in rand),
           f"shape draft beats {beat}/20 -> {ro}"]
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h379_108v_shape_relabel_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
