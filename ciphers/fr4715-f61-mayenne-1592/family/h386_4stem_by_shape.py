#!/usr/bin/env python3
"""H386 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, for VERIFY-F61-V11: does the readers' 4STEM code split by the bowl the
way 4TRI does? Letters exist for 4STEM only on f.101r (H207, key-row positions, period gloss; the 4STEM counts line of its result); f.108v (H199) and
f.106r (H368) have bowl answers for 4STEM but no letters. Reports, per source: 4STEM bowl yes/no and, where letters exist, the c/p vs a/n cross-tab and
agreement beside 4TRI's in the same call; plus v7's pooled and f.61-reading 4STEM cells. Descriptive, a pointer for a 4STEM clause.
python3 h386_4stem_by_shape.py [--check]"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_key_v7 as b
def line(f, start): return next(l for l in open(f"{HERE}/{f}") if l.startswith(start)).strip()
out = [f"v7 4STEM cell: pooled {'/'.join(sorted(b.load_key_v7(ebr='B')['4STEM']))}, f.61 reading {'/'.join(sorted(b.load_key_v7(ebr='B', f61=True)['4STEM']))}"]
for code in ("4TRI", "4STEM"):
    t = line("h207_bowl_101r_result.txt", f"{code}:"); m = list(map(int, re.findall(r"(?:c/p|a/n) (\d+)", t)))[:4]
    n = sum(m); out.append(f"f.101r H207 {code}: bowl&c/p {m[0]} bowl&a/n {m[1]} no&c/p {m[2]} no&a/n {m[3]}; agreement {(m[0] + m[3]) / n:.2f} (n {n})")
out.append("f.108v H199 4STEM (no letters): " + re.search(r"4STEM yes (\d+) no (\d+) n (\d+)", line("h199_bowl_108v_result.txt", "by rec code")).expand(r"bowl \1, no \2, n \3"))
out.append("f.106r H368 4STEM (no letters): " + re.search(r"4STEM (n \d+ no \d+ yes \d+)", line("h368_bowl_106r_result.txt", "by pass-A code")).group(1))
txt = "\n".join(out) + "\n"; res = f"{HERE}/h386_4stem_by_shape_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
