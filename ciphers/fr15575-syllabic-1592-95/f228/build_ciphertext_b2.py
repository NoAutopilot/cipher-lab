#!/usr/bin/env python3
"""N8-NV05B: tokenise the reconciled f.228 L05-L08 lines into ciphertext_b2.tsv; report err_2reader (passes A/B).

  python3 build_ciphertext_b2.py [--check]

Tokeniser imported from build_ciphertext.py (PREREG.md rule, unchanged). conf H where the run is as both passes read
it, M where this worker settled an A/B disagreement from the crop (PREREG-ADDENDUM-N8B.md).
"""
import difflib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_ciphertext import toks, runs, passes  # noqa: E402

FINAL = {
 "L05": "57 90 8917n.55.24.5691 ^68y 8324 ^94 pa 7381.34 6517n.17c 9 92:89 965 + 73 ho 4872 2n76",
 "L06": "50 97348 (188025 68y31 /^n n.3461 5961 4.23 66.90:73484031 (7235 nun fos 92 6 n ^ 19.90:",
 "L07": "56 9 24:3283 ^61 92:8623 Vuz fal 57 tim mil 459088 5750 55 56402421 n.81.22 57n.83",
 "L08": "∞o2 1661 18:7345 81.31 ∞o2 91:87: (50 21.23 5655.2476 fo 91e5977n.21 57 , 88705 4224 c15",
}
# runs settled by the worker from the crop (A/B disagreed) -> M
SETTLED = {("L05", "965"), ("L05", "2n76"), ("L05", "6517n.17c"), ("L06", "nun"), ("L06", "6"), ("L06", "n"),
           ("L07", "9"), ("L07", "24:3283"), ("L07", "Vuz"), ("L08", "fo"), ("L08", "88705"), ("L08", "4224"),
           ("L08", ","), ("L08", "c15")}


def main():
    A, B = passes("passA_b2.tsv"), passes("passB_b2.tsv")
    rows = ["line\tpos\tsign\tconf"]; agree = tot = 0
    for ln in sorted(FINAL):
        ta, tb = toks(A[ln]), toks(B[ln])
        sm = difflib.SequenceMatcher(a=ta, b=tb, autojunk=False)
        agree += sum(b.size for b in sm.get_matching_blocks()); tot += max(len(ta), len(tb))
        pos = 0
        for w, ts in runs(FINAL[ln]):
            for t in ts:
                pos += 1
                rows.append(f"{ln}\t{pos}\t{t}\t{'M' if (ln, w) in SETTLED else 'H'}")
    text = "\n".join(rows) + "\n"
    path = os.path.join(HERE, "ciphertext_b2.tsv")
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path, encoding="utf-8").read() == text
        print("ciphertext_b2.tsv up to date" if ok else "ciphertext_b2.tsv is stale"); sys.exit(0 if ok else 1)
    open(path, "w", encoding="utf-8").write(text)
    print(f"tokens {len(rows) - 1}; err_2reader = {tot - agree}/{tot} = {(tot - agree) / tot:.3f}")


if __name__ == "__main__":
    main()
