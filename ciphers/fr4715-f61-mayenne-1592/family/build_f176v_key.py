#!/usr/bin/env python3
"""H177c (runner 7, 29 Sept 2026): period key rows for fr.3984 f.176v from its separate-sheet decipherment (fol. 177v, then fol. 178r),
kept in a SEPARATE file (key_period_f176v.tsv) while VERIFY-F61-V5 audits key_period_f176.tsv; build_f176_key.py is imported, never
edited. Design = build_f176_key.py's (A/B consensus signs, key v4's letter SETS decide only where signs and letters line up, the
letter comes from the decipherment), fixed before the f.176v passes were read, with two controls instead of one:
 (a) wrong text, other letter: fr.3984 f.184r's clear from word 0, same N (build_f176_key.py's control);
 (b) wrong passage, same decipherment: fol. 177r from its line L01 (f.176r's own clear, same writer, cipher and day), same N.
Clear: fol. 177v lines from --start (default V01; f.176r's 3,095 signs at the 0.8 letters-per-sign rule end near fol. 177r's foot,
2,589 letters) in reading order, then fol. 178r lines (passes/f178r_clearA_*.tsv, R01...), folded as h170_gate.py folds, trimmed to
N = floor(0.8 x signs).
GATE (pre-registered, PROMPTS_f176_f175.md section H177c): true match - max(control a, control b) >= +0.10.
  python3 build_f176v_key.py ROWS [--start V01] [--check]   (ROWS e.g. L01-L08; reads passes/f176v_signs{A,B}_*.tsv)"""
import glob, os, re, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_f176_key as b
g = b.g; P = b.P; LEAF = "fr.3984 f.176v/f.177v-178r"
def pass_rows(tag):
    rows = defaultdict(list)
    for f in sorted(glob.glob(f"{P}/f176v_signs{tag}_*.tsv")):
        for r in g.rd(f):
            s = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"].strip(), r["sign"].strip())
            if s != "PLAIN": rows[r["line"]].append(s)
    return rows
def clear(start):
    lines = {}
    for f in sorted(glob.glob(f"{P}/f177v_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
    order = sorted(lines, key=lambda l: int(l[1:])); order = order[order.index(start):]
    for f in sorted(glob.glob(f"{P}/f178r_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("R" + r["line"].lstrip("LR"), r["text"]); order.append("R" + r["line"].lstrip("LR"))
    order = list(dict.fromkeys(order))
    return "".join(g.fold(lines[l]) for l in order), order
def clear177r():   # control (b): fol. 177r only (L01's salutation dropped as build_f176_key.py drops it); N is capped at its length
    lines = {}
    for f in sorted(glob.glob(f"{P}/f177r_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault(r["line"], r["text"])
    t = ""
    for l in sorted(lines, key=lambda l: int(l[1:])):
        x = lines[l]; t += g.fold(x.split("/", 1)[1] if l == "L01" and "/" in x else x)
    return t
def main():
    a = sys.argv; lo, hi = [int(x) for x in re.findall(r"\d+", a[1])]; want = [f"L{k:02d}" for k in range(lo, hi + 1)]
    start = a[a.index("--start") + 1] if "--start" in a else "V01"
    A, B = pass_rows("A"), pass_rows("B"); missing = [l for l in want if l not in A or l not in B]
    if missing: sys.exit(f"missing rows in the passes: {missing}")
    seq = [s for l in want for s in b.consensus(A[l], B[l])]; key = g.load_key()
    text, order = clear(start); w177r = clear177r(); N = min(len(text), len(w177r), int(0.8 * len(seq)))
    w184 = g.fold(" ".join(r["word"] for r in g.rd(f"{P}/f184r_clear_rec.tsv")))[:N]; w177r = w177r[:N]
    ct, ft = b.run(seq, text[:N], key, "true"); ca, fa = b.run(seq, w184, key, "wrong"); cb, fb = b.run(seq, w177r, key, "wrong")
    marg = ft - max(fa, fb); nc = sum(not s.startswith("?") for s in seq)
    out = [f"rows {want[0]}-{want[-1]} of f.176v: {len(seq)} signs, consensus {nc} ({nc/len(seq):.2f}); clear {order[0]}-{order[-1]}, {len(text)} letters, N {N}",
           f"match: fol. 177v-178r {ft:.3f} vs (a) f.184r {fa:.3f}, (b) fol. 177r from L01 {fb:.3f}; margin {marg:+.3f}; GATE (>= +0.10) {'PASS' if marg >= 0.10 else 'FAIL'}", "",
           "class\tv4 set\ttrue: letters (n)\t(a) f.184r: letters (n)\t(b) fol. 177r: letters (n)\tin-set share true / a / b"]
    fmt = lambda C: " ".join(f"{x}{n}" for x, n in sorted(C.items(), key=lambda t: (-t[1], t[0]))[:6])
    sh = lambda C, vs: (sum(C[x] for x in vs) / sum(C.values())) if sum(C.values()) else 0
    for c in sorted(set(ct) | set(ca) | set(cb), key=lambda c: (-sum(ct[c].values()), c)):
        vs = key.get(c, ())
        out.append(f"{c}\t{'/'.join(vs) or '-'}\t{fmt(ct[c])} ({sum(ct[c].values())})\t{fmt(ca[c])} ({sum(ca[c].values())})\t{fmt(cb[c])} ({sum(cb[c].values())})\t{sh(ct[c], vs):.2f} / {sh(ca[c], vs):.2f} / {sh(cb[c], vs):.2f}")
    out += ["", "disputed columns (A|B) under the true text:"]
    for k, C in sorted(b.DISP["true"].items(), key=lambda t: -sum(t[1].values()))[:10]: out.append(f"{'|'.join(k)}\t{fmt(C)} ({sum(C.values())})")
    rows = ["# key_period_f176v.tsv -- H177c (runner 7), build_f176v_key.py " + a[1] + ": set-anchored DP pairs, consensus signs only; key source period; NOT merged into v4 (a verifier's)", "class\tletter\tn\tleaf\tbands"] + [f"{c}\t{x}\t{n}\t{LEAF}\tDP stage {want[0]}-{want[-1]}" for c in sorted(ct) for x, n in sorted(ct[c].items(), key=lambda t: (-t[1], t[0]))]
    files = {f"{HERE}/build_f176v_key_result.txt": "\n".join(out) + "\n", f"{HERE}/key_period_f176v.tsv": "\n".join(rows) + "\n"}
    if "--check" in a:
        bad = [p for p, s in files.items() if not os.path.exists(p) or open(p).read() != s]
        print("stale: " + ", ".join(bad) if bad else "OK"); sys.exit(1 if bad else 0)
    for p, s in files.items(): open(p, "w").write(s)
    print("\n".join(out[:2]))
if __name__ == "__main__": main()
