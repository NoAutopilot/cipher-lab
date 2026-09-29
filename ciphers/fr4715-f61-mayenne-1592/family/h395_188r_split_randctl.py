#!/usr/bin/env python3
"""H395 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, written before running: on fr.3984 f.188r (in-sample), H392's 18
no-bowl 4TRI relabelled C43 (passes/recf188r_split/, written here) vs 20 random relabellings of 18 drawn from the same 66 bowl-read tokens (seed 395);
v7 order gain, mean of seeds 342-344 (h374_split_randctl.gains). Pre-stated as H374: >= 19/20 'carries order information' (the minority no-bowl tokens
behave as the a/n sign), <= 9/20 'no better than random' (reader noise or not the a/n sign), else 'unclear'. The as-transcribed gain is reported.
python3 h395_188r_split_randctl.py [--check]"""
import csv, os, random, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
sys.argv = [sys.argv[0], "f97r"]
import h374_split_randctl as h374
ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h392_reply.tsv")}
lab = {(r["line"], r["pos"]): ans.get(r["item"]) for r in rd(f"{HERE}/h392_items.tsv") if r["kind"] == "T"}
pool = sorted(k for k, a in lab.items() if a in ("yes", "no")); no = {k for k in pool if lab[k] == "no"}
rows = list(open(f"{P}/recf188r/ciphertext_draft.tsv"))
def write(pick, name):
    new = [rows[0]]
    for l in rows[1:]:
        c = l.rstrip("\n").split("\t")
        if c[2] == "4TRI" and (c[0], c[1]) in pick: c[2] = "C43"
        new.append("\t".join(c) + "\n")
    os.makedirs(f"{P}/{name}", exist_ok=True); open(f"{P}/{name}/ciphertext_draft.tsv", "w").write("".join(new))
write(no, "recf188r_split"); g0 = h374.gains("recf188r"); gs = h374.gains("recf188r_split"); rng = random.Random(395); rand = []
try:
    for _ in range(20): write(set(rng.sample(pool, len(no))), "_h395tmp"); rand.append(h374.gains("_h395tmp"))
finally:
    shutil.rmtree(f"{P}/_h395tmp", ignore_errors=True)
beat = sum(gs > r for r in rand); ro = "carries order information" if beat >= 19 else "no better than random" if beat <= 9 else "unclear"
out = [f"f.188r: bowl-read 4TRI {len(pool)}, relabelled {len(no)}; order gain v7 mean of 3 seeds: as transcribed {g0:.4f}, shape split {gs:.4f}",
       f"20 random relabellings of {len(no)}: mean {sum(rand) / 20:.4f}, min {min(rand):.4f}, max {max(rand):.4f}",
       f"shape split beats {beat}/20 -> {ro}"]
txt = "\n".join(out) + "\n"; res = f"{HERE}/h395_188r_split_randctl_result.txt"
if CHECK:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
