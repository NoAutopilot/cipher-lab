#!/usr/bin/env python3
"""H259 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): what does Tomokiyo's markup carry at f.61's CA positions inside his five spans?
H256 found CA has the letterform of the scribe's clear a, H63 the cipher hand: is CA (a) a clear letter a left among the signs -- then his markup at
the CA, or an unassigned markup 'a' beside it, should be 'a'; (b) a null -- then his markup at the CA is '-' (or the CA takes no markup char); or
(c) a cipher sign with a value -- then a letter other than a. Alignment: f61cal's local DP (scripts/f61crib.align) of each span's markup against the
line's classes under key v6's f.61 reading (build_key_v6.load_key_v6(f61=True), the current key; CA has no value in it, so a CA can only pair with a
markup char at score 0 or be skipped), the same alignment the known-span scores use. Controls: PHI and C43 at span positions must pair with letters in
their cells. Read-out, fixed before running: 'CA pairs with a' if every in-span CA pairs with markup 'a' or sits next to an unpaired markup 'a';
'CA takes no letter' if every in-span CA pairs with '-' or is skipped by the alignment; else 'mixed', with the per-position table. Descriptive; the
DP's placement of a valueless sign is itself uncertain (a CA and a neighbouring gap can swap at equal score), so this is a lead for the verifier,
not a value.  python3 h259_ca_span.py [--check]"""
import os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
from build_key_v6 import load_key_v6
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
key = load_key_v6(f61=True); lines = split_lines(load_read()); relabel(lines)
rows = ["span\tline\tpos\tclass\tcell\tmarkup"]; summ = Counter(); ctrl = Counter(); ca_rows = []
for s, l, m in load_spans():
    pairs = align(m, lines[l], key)[1]; pj = {j: i for i, j in pairs}; pi = {i: j for i, j in pairs}
    if not pairs: continue
    lo, hi = min(pj), max(pj)
    for j in range(lo, hi + 1):
        c = lines[l][j]; ch = m[pj[j]] if j in pj else "(skipped)"
        rows.append(f"{s}\t{l}\t{j + 1}\t{c}\t{'/'.join(key.get(c, ()))or '-'}\t{ch}")
        if c == "CA":
            near_a = any(m[i] == "a" and i not in pi for i in (pj.get(j, -9) - 1, pj.get(j, -9) + 1) if 0 <= i < len(m)) if j in pj else \
                     any(m[i] == "a" and i not in pi for i in range(len(m)) if abs(i - (pj.get(j - 1, pj.get(j + 1, -9)))) <= 1)
            verdict = "a" if ch == "a" or near_a else ("none" if ch in ("-", "(skipped)") else f"letter {ch}")
            summ[verdict] += 1; ca_rows.append(f"  {s} {l} pos {j + 1}: markup {ch}{' (unpaired a beside it)' if near_a and ch != 'a' else ''} -> {verdict}")
        elif c in ("PHI", "C43") and j in pj: ctrl[c, "letter in cell" if ch in key.get(c, ()) else f"other ({ch})"] += 1
rows += ["", "CA inside the spans:"] + ca_rows + [f"CA verdicts: " + ", ".join(f"{k} {n}" for k, n in sorted(summ.items()))]
rows.append("controls: " + "; ".join(f"{c} {k} {n}" for (c, k), n in sorted(ctrl.items())))
out = "CA pairs with a" if summ and set(summ) == {"a"} else "CA takes no letter" if summ and set(summ) == {"none"} else "mixed"
rows.append(f"read-out: {out}")
txt = "\n".join(rows) + "\n"; res = f"{HERE}/h259_ca_span_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
