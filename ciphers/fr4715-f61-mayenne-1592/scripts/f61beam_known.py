#!/usr/bin/env python3
"""F61-BEAM-KNOWN (campaign step H116, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only, no model call.
AUDIT.md (VERIFY-F61-V4 sec. 6 item 1): f.61r's two-way choices need an instrument with a control. The H114/H115 4-gram
beam (scripts/f61hash4_108r.py resolve: fr16 4-gram, width 400) ranks the fitted 14-cell map 1-2 on the known span lines,
but its within-pair letter choices were never scored against the known answer. Here they are.

Method, fixed before the first run: the known_h51 lines (f61judge108v.lines, the H85/H94 control text) are resolved line by
line under the 14-cell map; Tomokiyo's markup (scripts/tomokiyo_spans.tsv) is placed on each line by f61crib.align (F61-CAL's
DP) with the 14-cell map's pairs as the key; at every aligned position whose sign is covered and whose true letter (folded,
i=j, u=v) is one of its pair's two letters, the beam's choice is right or wrong.
  (ii) choice accuracy = right / such positions; baselines: always the pair's first letter, and 0.5.
  (i)  letters matched at the aligned positions, fitted map vs the same count under 200 permuted maps (seed 116), each
       resolved by the same beam (positions fixed by the fitted alignment -- circular for (i), stated; (ii) is the test).
GATE H116: (ii) >= 0.75 AND (i) above the permuted p95.   -> scripts/f61beam_known_result.txt [--check]
"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61hash4_108r as H
from f61crib import load_spans, align
J, jp = H.J, H.jp
def resolved(seq, m):
    idx = [k for k, c in enumerate(seq) if c in m]
    pairs = [tuple(jp.fold(x) for x in m[seq[k]].split("/")) for k in idx]
    s, _, _ = H.resolve(pairs); return dict(zip(idx, s)), dict(zip(idx, pairs))
F108 = "--f108r" in ARGS   # H121 (28 Sept 2026): the same method on Tomokiyo's overlay of f.108r L02/L03 (84 letters), lines as f61joint builds them, H51 relabel
def load108():
    import f61joint, f61qo2
    L = f61joint.f108_lines(); f61qo2.relabel(L)
    spans = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{HERE}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    return {k: L[k] for k in ("F108_L02", "F108_L03")}, spans
def main():
    C = J.cells(); L, spans = load108() if F108 else (J.lines("known_h51"), load_spans())
    key = {c: tuple(v.split("/")) for c, v in C.items()}
    placed = []   # (line, seq index, true letter)
    for s, line, markup in spans:
        _, prs = align(markup, L[line], key)
        for i, j in prs:
            ch = markup[i]
            if ch != "-": placed.append((line, j, jp.fold(ch)))
    res = {line: resolved(L[line], C) for line in L}
    right = inpair = first = 0
    for line, j, t in placed:
        ch, pr = res[line][0].get(j), res[line][1].get(j)
        if pr and t in pr:
            inpair += 1; right += ch == t; first += pr[0] == t
    def matched(m):
        r = {line: resolved(L[line], m)[0] for line in L}
        return sum(1 for line, j, t in placed if r[line].get(j) == t)
    fit = matched(C); labs = sorted(C); rng = random.Random(116); null = []
    for _ in range(200):
        v = [C[l] for l in labs]; rng.shuffle(v); null.append(matched(dict(zip(labs, v))))
    null.sort(); p95 = null[int(0.95 * 200)]
    acc = right / inpair if inpair else 0
    out = [f"aligned known letters {len(placed)}; covered with the true letter in the pair {inpair}",
           f"(ii) beam choice accuracy {right}/{inpair} = {acc:.3f}; always-first-letter {first}/{inpair} = {first / inpair:.3f}; chance 0.5",
           f"(i) letters matched: fitted {fit}; permuted median {null[100]}, p95 {p95}, max {null[-1]} (200 maps, seed 116; positions from the fitted alignment)",
           f"GATE H116 ((ii) >= 0.75 and (i) > p95): {'PASS' if acc >= 0.75 and fit > p95 else 'FAIL'}"]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61beam_known{'_108r' if F108 else ''}_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
