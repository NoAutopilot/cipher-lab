#!/usr/bin/env python3
"""A2-F61R (2 Oct 2026): score two blind passes of f.61r's clear text.

  python3 scripts/f61r_clear_score.py passA.tsv passB.tsv [--out scripts/f61r_clear_score.txt]

Gates (pre-registered in NOTES.md, step A2-F61R):
  KA  each pass reads >= 10 of the 12 known words of f.108r's clear line (line id K);
  WA  pooled word agreement between the passes on f.61r lines 01-11 >= 0.80 and above the maximum of a
      line-shuffled control (pass A line i vs pass B line j, i != j) -- word agreement depends on which lines are
      paired, so the control can differ from the target on this statistic.
Normalisation: lowercase, accents stripped, u=v, i=j=y, punctuation dropped, [#]/[?] and '?' letters removed.
Agreement = matched words / max(len A, len B), from a Needleman-Wunsch word alignment.
"""
import sys, unicodedata, re, argparse

KNOWN = "Et pour cela je vous laisse a juger quel contentement je debvois avoir"


def norm_word(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    w = w.replace("v", "u").replace("j", "i").replace("y", "i")
    return re.sub(r"[^a-z]", "", w)


def words(text):
    text = re.sub(r"\[[#?]\]", " ", text)
    out = []
    for w in text.split():
        if "?" in w:
            continue  # unsure-letter words never count as agreement
        n = norm_word(w)
        if n:
            out.append(n)
    return out


def nw_matches(a, b):
    n, m = len(a), len(b)
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + (a[i - 1] == b[j - 1]))
    return s[n][m]


def align(a, b):
    """Return list of (wordA or None, wordB or None) by LCS traceback."""
    n, m = len(a), len(b)
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + (a[i - 1] == b[j - 1]))
    i, j, out = n, m, []
    while i or j:
        if i and j and a[i - 1] == b[j - 1] and s[i][j] == s[i - 1][j - 1] + 1:
            out.append((a[i - 1], b[j - 1])); i -= 1; j -= 1
        elif i and (not j or s[i - 1][j] >= s[i][j - 1]):
            out.append((a[i - 1], None)); i -= 1
        else:
            out.append((None, b[j - 1])); j -= 1
    return out[::-1]


def load(path):
    d = {}
    for line in open(path, encoding="utf-8"):
        if "\t" in line:
            k, v = line.rstrip("\n").split("\t", 1)
            k = k.strip()
            if k.upper() == "K":
                k = "K"
            elif k.isdigit():
                k = "%02d" % int(k)
            d[k] = v
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--out")
    o = ap.parse_args()
    A, B = load(o.a), load(o.b)
    lines = ["%02d" % i for i in range(1, 12)]
    rep = []
    kw = words(KNOWN)
    ka_ok = True
    for name, P in (("A", A), ("B", B)):
        got = nw_matches(kw, words(P.get("K", "")))
        ok = got >= 10
        ka_ok &= ok
        rep.append(f"KA pass {name}: {got}/{len(kw)} known words -> {'PASS' if ok else 'FAIL'}")
    tm = tl = 0
    for l in lines:
        a, b = words(A.get(l, "")), words(B.get(l, ""))
        m, L = nw_matches(a, b), max(len(a), len(b))
        tm += m; tl += L
        rep.append(f"line {l}: A {len(a)} B {len(b)} agree {m} ({m / L if L else 0:.3f})")
    real = tm / tl if tl else 0
    ctrl = []
    for li in lines:
        for lj in lines:
            if li != lj:
                a, b = words(A.get(li, "")), words(B.get(lj, ""))
                L = max(len(a), len(b))
                ctrl.append(nw_matches(a, b) / L if L else 0)
    cmax, cmean = max(ctrl), sum(ctrl) / len(ctrl)
    wa_ok = real >= 0.80 and real > cmax
    rep.append(f"WA pooled f.61r word agreement {tm}/{tl} = {real:.3f}; line-shuffled control (110 pairs) mean {cmean:.3f} max {cmax:.3f} -> {'PASS' if wa_ok else 'FAIL'}")
    rep.append(f"GATES: KA {'PASS' if ka_ok else 'FAIL'}, WA {'PASS' if wa_ok else 'FAIL'}")
    txt = "\n".join(rep)
    print(txt)
    if o.out:
        open(o.out, "w").write(txt + "\n")
    return 0 if (ka_ok and wa_ok) else 3


if __name__ == "__main__":
    sys.exit(main())
