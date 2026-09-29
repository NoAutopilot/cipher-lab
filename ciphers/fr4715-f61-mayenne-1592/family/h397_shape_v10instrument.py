#!/usr/bin/env python3
"""H397 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, written before running: runner 14's shape-split order results
(H374/H375/H377/H378 random relabellings; H379/H380 permuted answers; H395 f.188r) re-scored with a SECOND instrument -- VERIFY-F61-V10's own order
statistic (verify_v10/order_v10.py: its letter model, exact Viterbi, gain = S(real) - mean S over its 10 within-run shuffles, seed 10010), imported,
not copied. Key v7 (order_v10.v7cell). Per leaf: gain on the as-transcribed draft, on the shape draft, and on 20 control drafts drawn afresh (seed 397
+ leaf index) in the same design the runner used on that leaf:
  equal-count random relabellings from the bowl-read pool (4TRI -> C43): f.124r (H359/H360), f.101r (H362/H365), f.97r enlarged (H370/H371/H373/H377),
  f.188r (H392);  permuted answers over the same tokens (bowl -> 4TRI, no -> C43): f.108v (H199 on H59's draft), f.106r (H231/H368/H385).
Pre-stated per leaf, as H374/H379: shape beats >= 19/20 controls 'carries order information (second instrument)'; <= 9/20 'no better than random';
else 'unclear'. Reported beside the runner's instrument's figure from the result files. Descriptive.   python3 h397_shape_v10instrument.py [--check]"""
import csv, os, random, shutil, sys
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv
sys.path.insert(0, HERE); sys.path.insert(0, f"{HERE}/../verify_v10")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def rep(f): return {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/{f}")}
def lab_items(pairs):
    lab = {}
    for items, reply, chunk in pairs:
        a = rep(reply)
        for r in rd(f"{HERE}/{items}"):
            if r.get("chunk", "") == chunk and r.get("code", "4TRI") == "4TRI" and r.get("kind", "T") == "T": lab[(r["line"], r["pos"])] = a.get(r["item"])
    return lab
def leaves():
    L = []
    L.append(("f.124r", "recf124r", "relabel", lab_items([("h359_items.tsv", "h359_reply.tsv", "")] + [("h360_items.tsv", f"h360_reply_c{k}.tsv", f"c{k}") for k in range(1, 5)])))
    L.append(("f.101r", "recf101r", "relabel", lab_items([("h362_items.tsv", "h362_reply.tsv", "")] + [("h365_items.tsv", f"h365_reply_c{k}.tsv", f"c{k}") for k in range(1, 5)])))
    L.append(("f.97r", "recf97r", "relabel", lab_items([("h370_items.tsv", "h370_reply.tsv", ""), ("h371_items.tsv", "h371_reply_c1.tsv", "c1"),
                                                         ("h371_items.tsv", "h371_reply_c2.tsv", "c2"), ("h377_items.tsv", "h377_reply.tsv", "")])))
    L.append(("f.188r", "recf188r", "relabel", lab_items([("h392_items.tsv", "h392_reply.tsv", "")])))
    H = rd(f"{HERE}/h199_bowl_positions.tsv")
    L.append(("f.108v", "H59:f108v3z_draft_reconciled.tsv", "permute", {(h["line"], h["column"]): h["bowl"] for h in H}))
    sys.argv = [sys.argv[0], "f97r"]
    import h380_106r_shape_relabel as h380
    raw = {tuple(l.split("\t")[:2]): l.split("\t")[2] for l in list(open(f"{P}/recf106rall18/ciphertext_draft.tsv"))[1:]}
    a = h380.answers(); lab = {k: v for k, (c, v) in a.items() if raw.get(k) == c}
    for r in rd(f"{HERE}/h385_items.tsv"):
        if r["kind"] == "T" and raw.get((r["line"], r["pos"])) == "C43": lab[(r["line"], r["pos"])] = rep("h385_reply.tsv").get(r["item"])   # draft-match rule, as H380/H385 (fixed after the first run: it lacked this filter, 109 tokens instead of 99)
    L.append(("f.106r", "recf106rall18", "permute", lab))
    return L
def base_rows(src):
    if src.startswith("H59:"):
        rows = rd(f"{P}/{src[4:]}"); cols = list(rows[0]); return ["\t".join(cols) + "\n"] + ["\t".join(r[c] for c in cols) + "\n" for r in rows]
    return list(open(f"{P}/{src}/ciphertext_draft.tsv"))
def write(rows, m, mode, name):
    new = [rows[0]]
    for l in rows[1:]:
        c = l.rstrip("\n").split("\t"); a = m.get((c[0], c[1]))
        if mode == "relabel":
            if c[2] == "4TRI" and a == "no": c[2] = "C43"
        elif a in ("yes", "no"): c[2] = "4TRI" if a == "yes" else "C43"
        new.append("\t".join(c) + "\n")
    os.makedirs(f"{P}/{name}", exist_ok=True); open(f"{P}/{name}/ciphertext_draft.tsv", "w").write("".join(new))
def g(prefix):
    import order_v10 as V
    runs, classes = V.leafdata(prefix); key = V.basekey(classes); return V.gain(key, runs, V.shuffles(runs, 10010))
def one(args):
    idx, (name, src, mode, lab) = args; rows = base_rows(src); tag = f"_h397tmp_{idx}"; out = []
    try:
        if mode == "relabel":
            d4 = {tuple(l.split("\t")[:2]) for l in rows[1:] if l.split("\t")[2] == "4TRI"}
            pool = sorted(k for k, a in lab.items() if a in ("yes", "no") and k in d4); k_no = sum(lab[k] == "no" for k in pool)
            write(rows, {}, mode, tag + "_base"); g0 = g(tag + "_base"); write(rows, {k: lab[k] for k in pool}, mode, tag + "_shape"); gs = g(tag + "_shape")
            rng = random.Random(397 + idx); ctl = []
            for _ in range(20):
                pick = set(rng.sample(pool, k_no)); write(rows, {k: ("no" if k in pick else "yes") for k in pool}, mode, tag + "_c"); ctl.append(g(tag + "_c"))
            desc = f"pool {len(pool)}, relabelled {k_no}"
        else:
            keys = sorted(k for k, a in lab.items() if a in ("yes", "no")); av = [lab[k] for k in keys]
            write(rows, {}, mode, tag + "_base"); g0 = g(tag + "_base"); write(rows, dict(zip(keys, av)), mode, tag + "_shape"); gs = g(tag + "_shape")
            rng = random.Random(397 + idx); ctl = []
            for _ in range(20):
                a = av[:]; rng.shuffle(a); write(rows, dict(zip(keys, a)), mode, tag + "_c"); ctl.append(g(tag + "_c"))
            desc = f"{len(keys)} answered (yes {av.count('yes')}, no {av.count('no')})"
    finally:
        for t in ("_base", "_shape", "_c"): shutil.rmtree(f"{P}/{tag}{t}", ignore_errors=True)
    beat = sum(gs > c for c in ctl); ro = "carries order information (second instrument)" if beat >= 19 else "no better than random" if beat <= 9 else "unclear"
    return f"{name} ({mode}; {desc}): V10 gain as transcribed {g0:.4f}, shape {gs:.4f}; 20 controls mean {sum(ctl) / 20:.4f}, max {max(ctl):.4f} -> beats {beat}/20 -> {ro}"
if __name__ == "__main__":
    L = leaves()
    with Pool(6) as p: out = p.map(one, list(enumerate(L)))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h397_shape_v10instrument_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
