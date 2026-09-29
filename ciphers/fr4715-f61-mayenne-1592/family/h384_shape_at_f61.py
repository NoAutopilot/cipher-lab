#!/usr/bin/env python3
"""H384 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, for VERIFY-F61-V11: f.61's exposure to PROPOSAL_v8_4tri.md. For each of
f.61's 18 4-family tokens (scripts/f61_positions_all.tsv): readers' code, key v7's pooled cell and its f.61 READING cell (load_key_v7(f61=True) with F61TOK for the 4-over-Pi; added after the first run, which compared with the pooled key only and so overstated the exposure), H367's bowl answer, the
cell under the shape rule (bowl -> v7's 4TRI cell, no bowl -> v7's C43 cell, n -> unchanged), and Tomokiyo's letter where H194's span alignment gives
one. Lists the positions whose cell would change, separating the proposal's own scope (4TRI) from the rule stretched to 4STEM/4PI. No grade, cell or reading is changed.   python3 h384_shape_at_f61.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
import build_key_v7 as b, h367_bowl_f61 as h
K = b.load_key_v7(ebr="B"); cell = lambda c: "/".join(sorted(K.get(c, ()))) or "-"
KF = b.load_key_v7(ebr="B", f61=True); F61TOK = b.F61TOK   # CORRECTION (runner 14, 18:0x): the f.61 reading key, which the first version omitted
def rcell(code, line, pos):
    if code == "4PI": v = F61TOK.get((line, int(pos))); return "/".join(sorted(KF["4PIPI"])) if v else "unread"
    return "/".join(sorted(KF.get(code, ()))) or "-"
fam = {}
for r in rd(f"{HERE}/../scripts/f61_positions_all.tsv"):
    if r["class"] in h.FAM: fam.setdefault(r["line"], []).append(r["pos"])
tom = {}
for l in open(f"{HERE}/h194_bowl_f61_result.txt"):
    f = l.rstrip("\n").split("\t")
    if len(f) == 5 and f[0].startswith("L") and f[1].isdigit(): tom[(f[0], fam[f[0]][int(f[1]) - 1])] = f[4]
ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h367_reply.tsv")}
out = ["line\tpos\tcode\tv7_pooled\tv7_f61_reading\tbowl\tshape_cell\ttomokiyo\tchange_vs_reading"]; ch = []
for r in sorted(rd(f"{HERE}/h367_items.tsv"), key=lambda r: (r["line"], int(r["pos"]))):
    a = ans.get(r["item"], "missing"); vp = cell(r["code"]); v = rcell(r["code"], r["line"], r["pos"]); s = "/".join(sorted(KF["4TRI"])) if a == "yes" else "/".join(sorted(KF["C43"])) if a == "no" else v
    t = tom.get((r["line"], r["pos"]), "-"); c = "CHANGE" if s != v else ""
    if c: ch.append(f"{r['line']}/{r['pos']} {r['code']} {v} -> {s} (Tomokiyo {t})")
    out.append(f"{r['line']}\t{r['pos']}\t{r['code']}\t{vp}\t{v}\t{a}\t{s}\t{t}\t{c}")
inp = [c for c in ch if " 4TRI " in c]; beyond = [c for c in ch if " 4TRI " not in c]
out.append(f"within PROPOSAL_v8_4tri.md's scope (4TRI only): {len(inp)} of 6 4TRI would change" + ("; " + "; ".join(inp) if inp else ""))
out.append(f"beyond its scope (the rule stretched to 4STEM/4PI, which the proposal does not cover; shown only as exposure): {len(beyond)}" + ("; " + "; ".join(beyond) if beyond else ""))
txt = "\n".join(out) + "\n"; res = f"{HERE}/h384_shape_at_f61_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
