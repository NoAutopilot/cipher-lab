#!/usr/bin/env python3
"""Build a wordcode cipher file (one run per transcript line, space-separated, a mark written base^mark) from a sign TSV.
R14-KAL12, 6 Oct 2026. Convention A (ciphertext_signs.tsv): x' -> x^a, ê -> e^c, ö -> o^u, ü -> u^u; reproduces
families/r13_kal10/cipher_marked.txt (--check-a). Convention B (ciphertext_signs_B.tsv): the free-standing apostrophe -> ap^a,
ê/ö/ü as in A; so the marked (code-capable) types are the apostrophe and the three diacritic letters.
Usage: python3 make_cipher_marked.py A|B OUT  [--check-a]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(HERE))
DIA = {"ê": "e^c", "ö": "o^u", "ü": "u^u"}

def name(s, conv):
    if s in DIA:
        return DIA[s]
    if conv == "B" and s == "'":
        return "ap^a"
    if conv == "A" and len(s) == 2 and s[1] == "'":
        return s[0] + "^a"
    if "'" in s or "^" in s:
        raise SystemExit(f"unmapped sign {s!r}")
    return s

def build(conv):
    f = "ciphertext_signs.tsv" if conv == "A" else "ciphertext_signs_B.tsv"
    lines = {}
    for row in open(os.path.join(T, f), encoding="utf-8").read().splitlines()[1:]:
        ln, s = row.split("\t")
        lines.setdefault(int(ln), []).append(name(s, conv))
    return "".join(" ".join(lines[k]) + "\n" for k in sorted(lines))

if __name__ == "__main__":
    conv, out = sys.argv[1], sys.argv[2]
    txt = build(conv)
    if "--check-a" in sys.argv:
        ref = open(os.path.join(T, "families", "r13_kal10", "cipher_marked.txt"), encoding="utf-8").read()
        print("convention A rebuild matches r13_kal10/cipher_marked.txt:", build("A") == ref)
    open(out, "w", encoding="utf-8").write(txt)
    toks = txt.split()
    marked = [t for t in toks if "^" in t]
    print(f"conv {conv}: lines {txt.count(chr(10))} N {len(toks)} K {len(set(toks))} marked types {sorted(set(marked))} tokens {len(marked)}")
