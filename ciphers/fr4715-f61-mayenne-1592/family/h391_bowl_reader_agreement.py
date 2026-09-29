#!/usr/bin/env python3
"""H391 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only: the bowl reader's repeatability from re-reads already on disk, beside
VERIFY-F61-V11's inter-reader kappa 0.35-0.49. Pairs (items answered yes/no both times): H194 vs H367 (f.61, same 15 positions, different designs);
H231 vs H368 (f.106r, shared pass-A positions); H371 c2 original vs H373 (f.97r, same sheets). Anchors: H193's 60 strips carried unchanged in every
H359-design call (H359 onward, 21 calls, same prompt): mean pairwise agreement and kappa over all call pairs, and each call's agreement with the
per-strip majority. Cohen's kappa on yes/no. Descriptive.   python3 h391_bowl_reader_agreement.py [--check]"""
import csv, glob, itertools, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def rep(f): return {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/{f}")}
def kappa(a, b):
    ks = [k for k in a if k in b and a[k] in ("yes", "no") and b[k] in ("yes", "no")]; n = len(ks)
    if not n: return 0, 0, float("nan")
    po = sum(a[k] == b[k] for k in ks) / n; pa = sum(a[k] == "yes" for k in ks) / n; pb = sum(b[k] == "yes" for k in ks) / n
    pe = pa * pb + (1 - pa) * (1 - pb); return n, po, (po - pe) / (1 - pe) if pe < 1 else float("nan")
out = ["pair\tn\tagreement\tkappa"]
import h367_bowl_f61 as h367
a = {(r["line"], r["pos"]): rep("h367_reply.tsv").get(r["item"]) for r in rd(f"{HERE}/h367_items.tsv")}
n, po, k = kappa(h367.h194(), a); out.append(f"H194 vs H367 (f.61)\t{n}\t{po:.2f}\t{k:.2f}")
x = rep("h231_reply.tsv"); a231 = {(r["line"], r["pos"]): x.get(r["item"]) for r in rd(f"{HERE}/h231_items.tsv")}; a368 = {}
for ch in ("c1", "c2"):
    x = rep(f"h368_reply_{ch}.tsv"); a368.update({(r["line"], r["pos"]): x.get(r["item"]) for r in rd(f"{HERE}/h368_items.tsv") if r["chunk"] == ch})
n, po, k = kappa(a231, a368); out.append(f"H231 vs H368 (f.106r)\t{n}\t{po:.2f}\t{k:.2f}")
c2 = [r["item"] for r in rd(f"{HERE}/h371_items.tsv") if r["chunk"] == "c2"]; o = rep("h371_reply_c2_orig.tsv"); nn = rep("h373_reply.tsv")
n, po, k = kappa({i: o.get(i) for i in c2}, {i: nn.get(i) for i in c2}); out.append(f"H371 c2 original vs H373 (f.97r)\t{n}\t{po:.2f}\t{k:.2f}")
files = sorted(os.path.basename(f) for f in glob.glob(f"{P}/h3[5-9][0-9]_reply*.tsv") if int(os.path.basename(f)[1:4]) >= 359)
Q = {f: {k: v for k, v in rep(f).items() if k.startswith("Q")} for f in files}
pk = [kappa(Q[f], Q[g]) for f, g in itertools.combinations(files, 2)]
out.append(f"H193 anchor strips across {len(files)} H359-design calls ({len(pk)} pairs)\tmean n {sum(p[0] for p in pk) / len(pk):.1f}\t"
           f"mean {sum(p[1] for p in pk) / len(pk):.2f}\tmean {sum(p[2] for p in pk) / len(pk):.2f} (min {min(p[2] for p in pk):.2f})")
maj = {}
for q in [f"Q{i:02d}" for i in range(1, 61)]:
    v = [Q[f].get(q) for f in files if Q[f].get(q) in ("yes", "no")]; maj[q] = "yes" if v.count("yes") > v.count("no") else "no"
out.append("each call vs the per-strip majority (agreement): " + " ".join(f"{f.replace('_reply', '').replace('.tsv', '')} {kappa(Q[f], maj)[1]:.2f}" for f in files))
txt = "\n".join(out) + "\n"; res = f"{HERE}/h391_bowl_reader_agreement_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
