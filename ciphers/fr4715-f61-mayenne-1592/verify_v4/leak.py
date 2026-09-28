#!/usr/bin/env python3
"""VERIFY-F61-V4 step 2 (28 Sept 2026): which f.61 known-span positions key v4 matches, which cells carry them, and the
v3 -> v4 difference position by position; ablations that remove the cells whose f.61-side class boundary was motivated
by a test scored on Tomokiyo's own letters (H13/H15 VBAR split, H26 SBS split) and the SBS 'e' (a sort-error artefact
per KEY.md). Writes verify_v4/leak_result.txt.   python3 verify_v4/leak.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.abspath(f"{HERE}/../family"); sys.path.insert(0, FAM)
chk = "--check" in sys.argv
def keyof(kf):
    sys.argv = ["x", "--key", f"{FAM}/{kf}", "--collapse-ebr", "--min", "2", "--frac", "0.1"]
    import importlib, test_period_key as T; importlib.reload(T); return T, T.load_key()
T, k4 = keyof("key_period_v4.tsv"); _, k3 = keyof("key_period_v3.tsv")
from sbs_relabel import relabel
L0 = T.split_lines(T.load_read()); L0.update(T.f108_lines())
Ls = {l: list(s) for l, s in L0.items()}; relabel(Ls)
spans = T.load_spans(); out = []
def detail(key, lines, tag):
    rows = []; tot = 0
    for s, line, m in spans:
        mt, pairs = T.align(m, lines[line], key); tot += mt
        for i, j in pairs:
            c = lines[line][j]; ok = m[i] != "-" and m[i] in key.get(c, ())
            rows.append((s, line, j + 1, m[i], c, "/".join(key.get(c, ())) or "-", ok))
    return tot, rows
t3, r3 = detail(k3, L0, "v3"); t4, r4 = detail(k4, Ls, "v4")
out.append(f"v3 (no --sbs) {t3}/55; v4 (--sbs) {t4}/55")
out.append("v4 matched positions by class: " + " ".join(f"{c}:{n}" for c, n in sorted(__import__('collections').Counter(r[4] for r in r4 if r[6]).items())))
out.append("v4 aligned known letters NOT matched: " + "; ".join(f"{r[0]} {r[1]}/{r[2]} '{r[3]}' {r[4]}={r[5]}" for r in r4 if not r[6] and r[3] != "-"))
s3 = {(r[1], r[2], r[3]) for r in r3 if r[6]}; s4 = {(r[1], r[2], r[3]) for r in r4 if r[6]}
out.append("matched under v4 only: " + "; ".join(f"{l}/{p} '{c}'" for l, p, c in sorted(s4 - s3)))
out.append("matched under v3 only: " + "; ".join(f"{l}/{p} '{c}'" for l, p, c in sorted(s3 - s4)))
def perm_p(key, lines, seed=20260928, N=2000):
    mt = T.score(key, lines, spans)[0]; labs = sorted(key); vals = [key[l] for l in labs]; rng = random.Random(seed); cs = []
    for _ in range(N):
        v = list(vals); rng.shuffle(v); cs.append(T.score(dict(zip(labs, v)), lines, spans)[0])
    cs.sort(); return f"{mt}/55 = {mt/55:.3f}; perm p95 {cs[int(.95*N)-1]/55:.3f} max {cs[-1]/55:.3f}, >= {sum(c >= mt for c in cs)}/{N}"
# ablation A: no SBS relabel on f.61 (SBS signs stay PHI/DBL); key v4 as is
out.append("A  v4 key, f.61 WITHOUT the --sbs relabel: " + perm_p(k4, L0))
# ablation B: SBS without its sort-artefact e
kb = dict(k4); kb["SBS"] = tuple(x for x in k4["SBS"] if x != "e"); out.append("B  v4, SBS = b/o (artefact e removed): " + perm_p(kb, Ls))
# ablation C: VBAR split undone on both sides (f.61 VBAR_A/VBAR_B -> VBAR; key VBAR = union)
Lc = {l: [("VBAR" if c.startswith("VBAR") else c) for c in s] for l, s in Ls.items()}
kc = {c: v for c, v in k4.items() if not c.startswith("VBAR")}; kc["VBAR"] = tuple(sorted(set(k4.get("VBAR_A", ())) | set(k4.get("VBAR_B", ()))))
out.append("C  v4, VBAR_A/B merged (f.61 and key): " + perm_p(kc, Lc))
# ablation D: every cell whose f.61 boundary was tested against Tomokiyo letters removed from the key (VBAR_A, VBAR_B, SBS)
kd = {c: v for c, v in k4.items() if c not in ("VBAR_A", "VBAR_B", "SBS")}; out.append("D  v4 minus VBAR_A, VBAR_B, SBS cells: " + perm_p(kd, Ls))
txt = "\n".join(out) + "\n"; path = f"{HERE}/leak_result.txt"
if chk: ok = os.path.exists(path) and open(path).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(path, "w").write(txt); print(txt, end="")
