"""A2-LAG3 (3 Oct 2026): base-code view of the pooled spec ciphertext for the masc family.
Strips the mark suffix (N^, N^ol, N^lp -> N) and drops the 11 free-standing MARK^ flourishes, which carry no
digit and so cannot be letters under a one-sign-per-letter design (solve_l2.py's base-digit mode makes the same
choice). '07' and '29' are kept as transcribed, distinct from 7 (never silently repaired).
  python3 build_basecode.py [--check]   writes/compares families/basecode_cipher.txt"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(here, "../../specs/la-garde-1577.json"), encoding="utf-8"))
out = []
for line in spec["ciphertext"]:
    toks = [t.split("^")[0] for t in line.split() if not t.startswith("MARK^")]
    if toks:
        out.append(" ".join(toks))
text = "# base codes of specs/la-garde-1577.json, marks stripped, MARK^ dropped (build_basecode.py)\n" + "\n".join(out) + "\n"
p = os.path.join(here, "families/basecode_cipher.txt")
if "--check" in sys.argv:
    sys.exit(0 if open(p, encoding="utf-8").read() == text else 1)
open(p, "w", encoding="utf-8").write(text)
toks = " ".join(out).split()
print(f"N={len(toks)} K={len(set(toks))} lines={len(out)}")
