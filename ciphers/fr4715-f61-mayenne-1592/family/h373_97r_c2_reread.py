#!/usr/bin/env python3
"""H373 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: H371's chunk c2 answered 'no' to all 37 items it could
read (every other chunk on f.124r, f.101r, f.97r lay at 0.59-0.77 no-bowl). One fresh blind Opus call on the SAME c2 sheets (SCRATCH/h371_c2/, made in
this session by h371_97r_4tri_split.py tiles; key h371_items.tsv unchanged), H359's prompt verbatim with H193's 60 strips as part 1; reply
passes/h373_reply.tsv. Pre-stated: GATE >= 17/20 on the re-read, else CONTROL FAIL (c2 unchanged, nothing decided). If it passes: agreement with the
original c2 over items answered yes/no both times >= 0.85 -> "c2 stands" (H371's read-out stands); else "c2 replaced": the original reply is kept as
passes/h371_reply_c2_orig.tsv, the re-read is copied to passes/h371_reply_c2.tsv (the file H371 scores), and h371_97r_4tri_split.py score is rerun
unchanged. Descriptive.   python3 h373_97r_c2_reread.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
import h370_bowl_97r  # noqa: F401  (same package path as H371)
def gate(ans):
    return sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in rd(f"{HERE}/h193_items.tsv") if r["group"] in ("CP", "AN"))
orig_f = f"{P}/h371_reply_c2_orig.tsv" if os.path.exists(f"{P}/h371_reply_c2_orig.tsv") else f"{P}/h371_reply_c2.tsv"
o = {r["id"]: r["answer"].strip().lower() for r in rd(orig_f)}; n = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h373_reply.tsv")}
g = gate(n); out = [f"re-read control: {g} of 20 (gate >= 17): {'PASS' if g >= 17 else 'CONTROL FAIL'}"]
if g >= 17:
    items = [r["item"] for r in rd(f"{HERE}/h371_items.tsv") if r["chunk"] == "c2"]
    both = [i for i in items if o.get(i) in ("yes", "no") and n.get(i) in ("yes", "no")]; same = sum(o[i] == n[i] for i in both)
    cnt = lambda d: " ".join(f"{a} {sum(d.get(i) == a for i in items)}" for a in ("yes", "no", "n"))
    out.append(f"original c2: {cnt(o)}; re-read: {cnt(n)}; agreement {same}/{len(both)} = {same / max(1, len(both)):.2f}")
    out.append("read-out: " + ("c2 stands" if both and same / len(both) >= 0.85 else "c2 replaced (original kept as h371_reply_c2_orig.tsv)"))
txt = "\n".join(out) + "\n"; res = f"{HERE}/h373_97r_c2_reread_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
