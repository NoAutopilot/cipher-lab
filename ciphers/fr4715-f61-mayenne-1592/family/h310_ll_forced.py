#!/usr/bin/env python3
"""H310 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): a different instrument for f.61's LL after the free letterform sort was retired
(H302/H304/H309, rule 3(c), HYPOTHESES.md): a per-tile FORCED CHOICE on H309's own sheet (<scratch>/h309/sheet_01.jpg, key family/h309_items.tsv,
16 tiles Y01..Y16) -- ONE (one tall ascender stroke), TWO (two tall ascender strokes side by side), NEITHER, or unclear -- by a fresh blind Opus reader.
Known answers: the 5 doubled l's are TWO, the 5 single l's ONE, PHI/C43 NEITHER.
Gate, fixed before the call: >= 9 of the 10 text l's answered correctly AND 4/4 PHI/C43 NEITHER, else CONTROL FAIL (nothing read out).
Read-out if the gate passes: LL's and the L02 mark's answers as given ('LL has two ascender strokes, like the clear ll' iff LL = TWO); n = 1 + 1,
flagged; descriptive, for the verifier's null-band wording; no value, no count change.  python3 h310_ll_forced.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
its = {r["item"]: r for r in rd(f"{HERE}/h309_items.tsv")}
ans = {r["tile"].strip(): r["answer"].strip().upper() for r in rd(f"{HERE}/passes/h310_forced.tsv")}
want = {"TEXT_A": "TWO", "TEXT_X": "ONE", "CIPHER": "NEITHER"}
out = []
for kind in ("TEXT_A", "TEXT_X", "CIPHER"):
    ms = [m for m, r in its.items() if r["kind"] == kind]
    out.append(f"{kind} ({want[kind]} expected): " + " ".join(f"{m}={ans.get(m, '-')}" for m in ms) + f"; correct {sum(ans.get(m) == want[kind] for m in ms)}/{len(ms)}")
tl = sum(ans.get(m) == want[r["kind"]] for m, r in its.items() if r["kind"] in ("TEXT_A", "TEXT_X"))
ci = sum(ans.get(m) == "NEITHER" for m, r in its.items() if r["kind"] == "CIPHER")
ll = [ans.get(m, "-") for m, r in its.items() if r["kind"] == "LL"][0]; dp = [ans.get(m, "-") for m, r in its.items() if r["kind"] == "DISP"][0]
if tl < 9 or ci < 4: out.append(f"gate: CONTROL FAIL (text l's {tl}/10, PHI/C43 NEITHER {ci}/4); nothing read out")
else:
    out.append(f"gate passes (text l's {tl}/10, PHI/C43 NEITHER {ci}/4)")
    out.append(f"read-out: LL = {ll}" + (" -- LL has two ascender strokes, like the clear ll" if ll == "TWO" else "") + f"; L02 mark = {dp} (n = 1 + 1, flagged)")
txt = "\n".join(out) + "\n"; res = f"{HERE}/h310_ll_forced_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
