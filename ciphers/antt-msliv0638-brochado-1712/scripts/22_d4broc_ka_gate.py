#!/usr/bin/env python3
"""D4-BROC known-answer gate G1 (PREREG-D4-BROC.md): token accuracy of a blind pass on the two appendix decoy
lines against the master transcription, edit-distance aligned, z == 7.
Usage: 22_d4broc_ka_gate.py "<pass tokens carta13 line2>" "<pass tokens carta110 line2>"  (dot-separated, | allowed)"""
import sys
TRUTH = ["13.c.7.18.15.4.5.15.m.c.7.m.5.7.18.y.8.4", "55.x.7.12.18.7.16.15.e.7.2.7.18.8.18"]
norm = lambda s: [t.strip().replace("z", "7") for t in s.replace("|", ".").split(".") if t.strip()]
def matches(a, b):  # number of aligned equal tokens (LCS-style via edit distance DP)
    n, m = len(a), len(b); d = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            d[i+1][j+1] = max(d[i][j] + (a[i] == b[j]), d[i][j+1], d[i+1][j])
    return d[n][m]
if __name__ == "__main__":
    tot = hit = 0
    for t, p in zip(TRUTH, sys.argv[1:3]):
        T, P = norm(t), norm(p); h = matches(T, P); tot += len(T); hit += h
        print(f"{len(T)} truth tokens, {len(P)} read, {h} matched")
    acc = hit / tot; print(f"G1 accuracy {acc:.3f} -> {'PASS' if acc >= 0.85 else 'FAIL'} (gate 0.85)")
    sys.exit(0 if acc >= 0.85 else 1)
