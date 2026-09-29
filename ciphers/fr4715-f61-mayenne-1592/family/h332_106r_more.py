#!/usr/bin/env python3
"""H332 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), written before the four calls returned: fr.3983 f.106r (Mayenne's secretary,
f.61's hand; HELD leaf) rows 7-12 (bands L07..L12, sheets/f106r_b, prompts passes/prompts_h332) read by two blind Opus sign passes and two blind
Opus gloss passes (passes/f106r_{signs,gloss}{A,B}_c2.tsv). Steps: (1) normalise the c2 passes exactly as f106r_pipeline.py does; (2) reconcile the
c2 sign passes with tools/reconcile_passes.py (nw) into passes/recf106r_c2/; (3) report sign agreement and gloss word agreement for c2 (the
pipeline's 60% gate, reported, not used to drop data -- H329 already ran on the HELD rows); (4) pool rows 1-6 (passes/f106r_*.tsv, recf106r) and
rows 7-12 into passes/f106rall_* and passes/recf106rall/ciphertext_draft.tsv; (5) run H329's count and controls unchanged (h329_106r_agreed.py's
code with 'f106r' -> 'f106rall'). Pre-stated as H329: 'consistent with key v7 on a held leaf in f.61's hand' iff real > binned p95 AND real >
frequency key; else 'no signal beyond frequency'; and untestable if fewer than 40 signs sit under agreed words (H329's 12 was untestable).
No reading, no merge.  python3 h332_106r_more.py [--check]"""
import csv, difflib, os, subprocess, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); P = f"{HERE}/passes"
def norm(path, kind):
    rows = []
    for line in open(path):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#") or line.startswith("line\t"): continue
        c = line.split("\t"); n = 7 if kind == "signs" else 8; c += [""] * (n - len(c)); k = 3 if kind == "signs" else 4
        v = c[k].strip().lower(); c[k] = {"high": "h", "medium": "m", "med": "m", "low": "l"}.get(v, v[:1] if v[:1] in "hml" else "m"); rows.append(c[:n])
    hdr = "line\tpos\tsign\tconf\tsegment\tx_px\tnote" if kind == "signs" else "line\tpos\tkind\tword\tconf\tsegment\tx0_px\tx1_px"
    return hdr, rows
out = []
for kind in ("signs", "gloss"):
    for pas in "AB":
        hdr, rows = norm(f"{P}/f106r_{kind}{pas}_c2.tsv", kind)
        open(f"{P}/f106r_{kind}{pas}_c2.tsv", "w").write(hdr + "\n" + "\n".join("\t".join(r) for r in rows) + "\n")
        _, r1 = norm(f"{P}/f106r_{kind}{pas}.tsv", kind)
        open(f"{P}/f106rall_{kind}{pas}.tsv", "w").write(hdr + "\n" + "\n".join("\t".join(r) for r in r1 + rows) + "\n")
os.makedirs(f"{P}/recf106r_c2", exist_ok=True)
subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{P}/f106r_signsA_c2.tsv", f"{P}/f106r_signsB_c2.tsv", "--out-dir", f"{P}/recf106r_c2", "--method", "nw"], capture_output=True, text=True, check=True)
ag = tot = 0
for row in csv.DictReader(open(f"{P}/recf106r_c2/agreement.tsv"), delimiter="\t"):
    a, t = int(row["agree"]), int(row["columns"]); ag += a; tot += t; out.append(f"{row['line']}: signs A {row['signs_A']} B {row['signs_B']} agree {a}/{t}")
out.append(f"c2 SIGN AGREEMENT {ag}/{tot} = {ag / tot if tot else 0:.3f}")
G = {}
for pas in "AB":
    d = defaultdict(list)
    for c in norm(f"{P}/f106r_gloss{pas}_c2.tsv", "gloss")[1]:
        if c[2].strip().lower() == "dash" or c[3].strip() in ("-", "--"): continue
        d[c[0]].append(c[3].strip().lower())
    G[pas] = d
m = na = nb = 0
for band in sorted(set(G["A"]) | set(G["B"])):
    wa, wb = G["A"].get(band, []), G["B"].get(band, []); sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
    k = sum(i2 - i1 for t, i1, i2, j1, j2 in sm.get_opcodes() if t == "equal"); m += k; na += len(wa); nb += len(wb)
    out.append(f"{band}: gloss words A {len(wa)} B {len(wb)} identical {k}")
gf = 2 * m / (na + nb) if na + nb else 0
out.append(f"c2 GLOSS WORD AGREEMENT {m} of A {na} / B {nb} = {gf:.3f} (pipeline gate 60%: {'HELD' if gf < 0.60 else 'PASS'})")
os.makedirs(f"{P}/recf106rall", exist_ok=True)
lines = [l for l in open(f"{P}/recf106r/ciphertext_draft.tsv")] + [l for l in open(f"{P}/recf106r_c2/ciphertext_draft.tsv") if not l.startswith("line\t")]
open(f"{P}/recf106rall/ciphertext_draft.tsv", "w").write("".join(lines))
src = open(f"{HERE}/h329_106r_agreed.py").read().replace('"f106r")', '"f106rall")').replace("h329_106r_agreed_result", "h332_106r_count_tmp").replace("recf106r/", "recf106rall/")
src = src[:src.index('txt = "\\n".join(out)')]
g = {"__file__": f"{HERE}/h329_106r_agreed.py", "__name__": "h332"}; _argv = sys.argv; sys.argv = sys.argv[:1]; exec(compile(src, "h329_on_f106rall", "exec"), g); sys.argv = _argv
out.append("POOLED ROWS 1-12 (H329's count, controls unchanged):"); out += g["out"]
nsig = g["nsig"]
if nsig < 40: out.append(f"pre-stated floor: {nsig} signs under agreed words < 40 -> untestable at this N (not a negative)")
txt = "\n".join(out) + "\n"; res = f"{HERE}/h332_106r_more_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
