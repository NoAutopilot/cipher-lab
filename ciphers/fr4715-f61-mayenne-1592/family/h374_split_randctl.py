#!/usr/bin/env python3
"""H374 / H375 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, written before running: H358's random-variant control applied
to the bowl split itself. For a leaf, the shape split (H360 on f.124r: 202 of 270 bowl-read agreed 4TRI relabelled C43; H371/H373 on f.97r: 78 of 127)
is compared with 20 random relabellings (seed 374 for f97r, 375 for f124r) of the SAME number of tokens drawn from the SAME bowl-read pool (so only the
choice of which tokens, not how many, differs). Each draft is scored with H360/H371's order gain for v7 (H342's statistic: real minus mean of 10
within-run shuffles, seeds 342/343/344, mean of the three). Pre-stated: the shape split 'carries order information' iff its mean gain beats >= 95% of
the random relabellings (>= 19 of 20); 'no better than random' iff it beats < 50% (<= 9 of 20); else 'unclear'. Random drafts are written to a
temporary passes/_h374tmp_<leaf>/ and removed. Descriptive; no key change.   python3 h374_split_randctl.py f97r|f124r [--check]"""
import csv, os, random, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
LEAF = sys.argv[1]; CHECK = "--check" in sys.argv
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool_and_split():
    if LEAF == "f97r":
        items = [(r["chunk"] if "chunk" in r else "", r) for r in rd(f"{HERE}/h370_items.tsv")] + [(r["chunk"], r) for r in rd(f"{HERE}/h371_items.tsv")]
        reps = {"": "h370_reply.tsv", "c1": "h371_reply_c1.tsv", "c2": "h371_reply_c2.tsv"}; base = "recf97r"; split = "recf97r_split"; seed = 374
    else:
        items = [("", r) for r in rd(f"{HERE}/h359_items.tsv")] + [(r["chunk"], r) for r in rd(f"{HERE}/h360_items.tsv")]
        reps = {"": "h359_reply.tsv", **{f"c{k}": f"h360_reply_c{k}.tsv" for k in range(1, 5)}}; base = "recf124r"; split = "recf124r_split"; seed = 375
    ans = {ch: {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/{f}")} for ch, f in reps.items()}
    read = {(r["line"], r["pos"]): ans[ch].get(r["item"], "missing") for ch, r in items if r["code"] == "4TRI"}
    return sorted(read), sum(v == "no" for v in read.values()), base, split, seed
def gains(prefix):
    src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h374"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
    runs, cell, score_ = g["runs"], g["cell"], g["score"]; res = []
    for sd in (342, 343, 344):
        rng = random.Random(sd); ss = []
        for _ in range(10):
            s = []
            for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
            ss.append(s)
        g["runs"] = runs; real = score_(cell); sh = []
        for s in ss: g["runs"] = s; sh.append(score_(cell))
        res.append(real - sum(sh) / len(sh))
    return sum(res) / 3
def main():
    pool, k, base, split, seed = pool_and_split(); rows = list(open(f"{P}/{base}/ciphertext_draft.tsv"))
    gs = gains(split); g0 = gains(base); rng = random.Random(seed); rand = []; tmp = f"_h374tmp_{LEAF}"
    try:
        for d in range(20):
            pick = set(rng.sample(pool, k)); new = [rows[0]]
            for l in rows[1:]:
                c = l.rstrip("\n").split("\t")
                if c[2] == "4TRI" and (c[0], c[1]) in pick: c[2] = "C43"
                new.append("\t".join(c) + "\n")
            os.makedirs(f"{P}/{tmp}", exist_ok=True); open(f"{P}/{tmp}/ciphertext_draft.tsv", "w").write("".join(new)); rand.append(gains(tmp))
    finally:
        shutil.rmtree(f"{P}/{tmp}", ignore_errors=True)
    beat = sum(gs > r for r in rand)
    ro = "carries order information" if beat >= 19 else "no better than random" if beat <= 9 else "unclear"
    out = [f"{LEAF}: bowl-read 4TRI pool {len(pool)}, relabelled {k}; order gain v7 (mean of 3 seeds): as transcribed {g0:.4f}, shape split {gs:.4f}",
           f"20 random relabellings of {k}: mean {sum(rand) / 20:.4f}, min {min(rand):.4f}, max {max(rand):.4f}; values " + " ".join(f"{r:.4f}" for r in rand),
           f"shape split beats {beat}/20 -> {ro}"]
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h374_split_randctl_{LEAF}_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
