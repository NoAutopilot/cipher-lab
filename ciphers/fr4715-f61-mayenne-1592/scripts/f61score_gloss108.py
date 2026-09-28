#!/usr/bin/env python3
"""F61-GLOSS108-SCORER (campaign step H137, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe): the scorer for ASKS 88,
written and pushed BEFORE the person's gloss of f.108r L04-L06 exists, so nothing in it can be fitted to the answer.

Input (the person's file, format in images/person_pack/README.md): scripts/gloss108_person.tsv with columns
line, word, first_sign, last_sign, note -- first/last_sign in the person pack's numbering (= H34 pass A positions,
scripts/pass108gA_classes.tsv, PLAIN rows included in the count). Rows whose word is '-' or starts with '?' are skipped.

Mapping (fixed here): a pass A position -> the H108 draft position through the reconciliation task (same segment and x in
L04/L05); for L06 (pass A read the half-cut row) the draft sign in the same segment with the nearest x within 90 px, else
unmapped (reported). Each gloss word is placed on the covered signs under its range by f61crib.align (F61-CAL's DP) with
the pairs of the 14-cell map + HASH4 = i/x; at every aligned sign whose pair holds the gloss letter, each prediction is
right or wrong. Predictions scored: H107 (judge, pass A signs), H112 seeds 108 and 109 (judge, H108 draft), H120 (beam,
H108 draft); baselines: always the pair's first letter, and 0.5. Nothing is gated here: H64 reads the numbers.

  python3 scripts/f61score_gloss108.py            -> "waiting" (exit 0) while the gloss file is absent; else
                                                     scripts/f61score_gloss108_result.txt
  python3 scripts/f61score_gloss108.py --selftest -> a synthetic gloss built from H120's own letters must score H120 1.000
"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61hash4_108r as H
from f61crib import align
J, jp = H.J, H.jp
GLOSS = f"{HERE}/gloss108_person.tsv"
def rows(p): return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))
def passA():
    return {L: [r for r in rows(f"{HERE}/pass108gA_classes.tsv") if r["line"] == L] for L in ("L04", "L05", "L06")}
def a_to_draft():
    """(line, pass A pos) -> H108 draft position (1-based), or None."""
    A = passA(); T = rows(f"{HERE}/f61recon108r_task.tsv"); D = rows(f"{HERE}/f61recon108r_draft.tsv"); m = {}
    for L in ("L04", "L05"):
        byxy = {(t["segA"], t["xA"]): int(t["position"]) for t in T if t["line"] == L and t["segA"]}
        kept = [t for t in T if t["line"] == L]   # draft positions renumber after 'none' drops; map task position -> draft order
        dpos = {}; k = 0
        for t in kept:
            if any(d["line"] == L and d["segment"] == (t["segA"] or t["segB"]) and d["x_px"] == (t["xA"] or t["xB"]) for d in D): k += 1; dpos[int(t["position"])] = k
        for r in A[L]:
            tp = byxy.get((r["segment"], r["x_px"])); m[(L, int(r["pos"]))] = dpos.get(tp) if tp else None
    d6 = [(int(d["position"]), d["segment"], float(d["x_px"])) for d in D if d["line"] == "L06"]
    for r in A["L06"]:
        c = [(abs(x - float(r["x_px"])), p) for p, sg, x in d6 if sg == r["segment"] and abs(x - float(r["x_px"])) <= 90]
        m[("L06", int(r["pos"]))] = min(c)[1] if c else None
    return m
def draft_classes():
    return {L: {k + 1: c for k, c in enumerate(seq)} for L, seq in J.lines("f108r_L04_L06_h108").items()}
def covered_positions(seq_by_pos, cells):
    return [p for p in sorted(seq_by_pos) if seq_by_pos[p] in cells]
def predictions():
    """name -> {(line, draft pos): letter}; H107 is on pass A positions, mapped to draft positions."""
    P = {}; D = draft_classes(); m = a_to_draft()
    for name, tag in (("H112 s108", "f108r_L04_L06_h108_s108"), ("H112 s109", "f108r_L04_L06_h108_s109")):
        k = json.load(open(f"{HERE}/f61judge_{tag}_key.json")); cells = k["cells"]
        rd = [l for l in open(f"{HERE}/f61judge_{tag}_result.txt") if l.startswith("target reading")][0].split(":", 1)[1].strip().split(" | ")
        d = {}
        for L, s in zip(("L04", "L05", "L06"), rd):
            for p, ch in zip(covered_positions(D[L], cells), s.replace(" ", "")): d[(L, p)] = jp.fold(ch)
        P[name] = d
    k = json.load(open(f"{HERE}/f61judge_f108r_L04_L06_s107_key.json")); cells = k["cells"]; A = passA()
    rd = [l for l in open(f"{HERE}/f61judge_f108r_L04_L06_s107_result.txt") if l.startswith("target reading")][0].split(":", 1)[1].strip().split(" | ")
    d = {}
    for L, s in zip(("L04", "L05", "L06"), rd):
        cov = [int(r["pos"]) for r in A[L] if r["sign"] in cells]
        for ap, ch in zip(cov, s.replace(" ", "")):
            dp = m.get((L, ap))
            if dp: d[(L, dp)] = jp.fold(ch)
    P["H107"] = d
    d = {}
    for r in rows(f"{HERE}/f61beam_f108r_prediction.txt"):
        if r["beam"] != ".": d[(r["line"], int(r["position"]))] = r["beam"]
    P["H120 beam"] = d
    return P
def score(gloss_rows):
    C = dict(J.cells(), HASH4="i/x"); key = {c: tuple(v.split("/")) for c, v in C.items()}
    D = draft_classes(); m = a_to_draft(); P = predictions()
    res = {n: [0, 0] for n in P}; first = [0, 0]; unm = 0; words = 0
    for g in gloss_rows:
        w = jp.fold(g["word"].strip())
        if not w or w.startswith("?") or w == "-": continue
        L = g["line"].strip(); lo, hi = int(g["first_sign"]), int(g["last_sign"])
        dps = [m.get((L, a)) for a in range(lo, hi + 1)]; unm += sum(1 for x in dps if x is None)
        dps = sorted({x for x in dps if x and D[L].get(x) in C}); seq = [D[L][x] for x in dps]
        if not seq: continue
        words += 1
        for i, j in align(w, seq, key)[1]:
            t = w[i]; pr = tuple(jp.fold(x) for x in C[seq[j]].split("/"))
            if t not in pr: continue
            first[1] += 1; first[0] += pr[0] == t
            for n, d in P.items():
                ch = d.get((L, dps[j]))
                if ch: res[n][1] += 1; res[n][0] += ch == t
    out = [f"gloss words placed {words}; pass A signs in their ranges not mapped to the draft {unm}",
           f"always-first-letter {first[0]}/{first[1]}" + (f" = {first[0] / first[1]:.3f}" if first[1] else "") + "; chance 0.5"]
    out += [f"{n}: {r}/{t}" + (f" = {r / t:.3f}" if t else "") for n, (r, t) in res.items()]
    return "\n".join(out) + "\n"
def selftest():
    d = predictions()["H120 beam"]; m = a_to_draft(); inv = {}
    for (L, a), dp in m.items():
        if dp: inv.setdefault((L, dp), a)
    g = []
    for L in ("L04", "L05", "L06"):
        ps = sorted(p for (l, p) in d if l == L)
        for k in range(0, len(ps) - 3, 4):
            chunk = [p for p in ps[k:k + 4] if (L, p) in inv]
            if len(chunk) < 2: continue
            g.append({"line": L, "word": "".join(d[(L, p)] for p in chunk), "first_sign": str(inv[(L, chunk[0])]), "last_sign": str(inv[(L, chunk[-1])])})
    txt = score(g); line = [l for l in txt.splitlines() if l.startswith("H120 beam")][0]
    r, t = map(int, line.split(":")[1].split("=")[0].strip().split("/"))
    print(txt, end=""); ok = t > 20 and r == t; print("SELFTEST", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
def main():
    if "--selftest" in ARGS: selftest()
    if not os.path.exists(GLOSS): print("waiting: scripts/gloss108_person.tsv not present (ASKS 88)"); sys.exit(0)
    txt = score(rows(GLOSS)); rp = f"{HERE}/f61score_gloss108_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
