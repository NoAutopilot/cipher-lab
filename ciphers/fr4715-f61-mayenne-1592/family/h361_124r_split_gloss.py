#!/usr/bin/env python3
"""H361 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: H325/H328's held-gloss count on f.124r
(two-pass agreed gloss letters matched one-to-one into key v7's cells; binned-permutation and frequency-key controls) rerun on H360's SPLIT draft
(passes/recf124r_split: the 202 agreed 4TRI tokens answered no-bowl relabelled C43). Code: h328_124r_freq.py and its h325 prefix executed unchanged
except (1) the draft path -> recf124r_split and (2) H325's pass-A match rule, which keeps a sign only where pass A's sign equals the draft's, now
compares pass A with the ORIGINAL draft's sign at that position (so a relabelled token keeps its pass-A x, and nothing else changes). Pre-stated:
'the split is supported by the gloss' iff the split draft's real count exceeds the original's (148) AND the split real > its binned p95 AND > its
frequency key; else 'not supported by the gloss count'. No reading, no merge.   python3 h361_124r_split_gloss.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]
h325 = open(f"{HERE}/h325_124r_agreed.py").read()
a = 'for r in rd(f"{P}/recf124r/ciphertext_draft.tsv"):\n    a = A.get((r["line"], int(r["position"])))\n    if a and a["sign"] == r["sign"]:'
assert a in h325, "h325 match block changed"
h325 = h325.replace(a, 'ORIG = {(r["line"], r["position"]): r["sign"] for r in rd(f"{P}/recf124r/ciphertext_draft.tsv")}\nfor r in rd(f"{P}/recf124r_split/ciphertext_draft.tsv"):\n    a = A.get((r["line"], int(r["position"])))\n    if a and a["sign"] == ORIG[(r["line"], r["position"])]:')
h328 = open(f"{HERE}/h328_124r_freq.py").read()
h328 = h328.replace('src = open(f"{HERE}/h325_124r_agreed.py").read()', 'src = H325SRC').replace('rd(f"{P}/recf124r/ciphertext_draft.tsv")', 'rd(f"{P}/recf124r_split/ciphertext_draft.tsv")')
h328 = h328[:h328.index('txt = "\\n".join(out)')]
g = {"__file__": f"{HERE}/h328_124r_freq.py", "__name__": "h361", "H325SRC": h325}; sys.argv = [sys.argv[0]]
exec(compile(h328, "h328_on_split", "exec"), g)
out = ["split draft: " + l for l in g["out"]]
real = g["real"]; line_a = g["out"][0]; import re
p95 = int(re.search(r"p95 (\d+)", line_a).group(1)); fk = int(re.search(r"\(b\) frequency key.*?: (\d+)", "\n".join(g["out"])).group(1))
out.append(f"original draft real 148 (H328); split real {real}; split binned p95 {p95}; split frequency key {fk}")
ok = real > 148 and real > p95 and real > fk
out.append("read-out: " + ("the split is supported by the gloss" if ok else "not supported by the gloss count"))
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h361_124r_split_gloss_result.txt"
if "--check" in ARGS:
    ok2 = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok2 else "STALE"); sys.exit(0 if ok2 else 1)
open(rs, "w").write(txt); print(txt, end="")
