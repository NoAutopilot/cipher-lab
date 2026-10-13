#!/usr/bin/env python3
"""VIV-105: word-level agreement between two blind reads of one page, and a merged draft.
Reads are line files: 'S01.1<TAB>text' (VIV-105 strips) or plain text lines (VIV-T's tx/plain_c110_f105r.txt, '#' lines
skipped). Lines are paired by a word-level alignment of the whole page (difflib on normalized words), so the two reads
need not number lines the same way. Normalization: lowercase, u/v->u, i/j->i, y->i, accents and punctuation dropped,
brackets and '?' dropped from [word?]; '{?}' never matches.
Agreement = 2*matched / (words_A + words_B), per page and per line of read A.
Usage: python3 v105/agree.py A.txt B.txt --label f105v [--expand] [--merge OUT] [--check]"""
import argparse, difflib, re, sys, unicodedata
def load(path):
    lines = []
    for raw in open(path, encoding="utf-8"):
        raw = raw.rstrip("\n")
        if not raw.strip() or raw.startswith("#"):
            continue
        lid, txt = (raw.split("\t", 1) if "\t" in raw else (str(len(lines) + 1), raw))
        lines.append((lid.strip(), txt.strip()))
    return lines
EXPAND = {"p.r": "pour", "pr": "pour", "q.": "que", "q.e": "que", "mons.r": "monsieur", "monsr": "monsieur", "s.r": "sieur",
          "ma.te": "maieste", "mate": "maieste", "vre": "vostre", "v.re": "vostre", "catho.": "catholique", "cath.que": "catholique",
          "led.": "ledict", "ambassad.r": "ambassadeur", "&": "et", "m.e": "mesme", "card.": "cardinal"}
EXP = False
def norm(w):
    if EXP and w.lower().strip("[]?") in EXPAND:
        w = EXPAND[w.lower().strip("[]?")]
    if "{?}" in w:
        return None
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    w = re.sub(r"[\[\]?.,;:'\"()^<>/]", "", w).replace("v", "u").replace("j", "i").replace("y", "i")
    return w or None
def words(lines):
    out = []
    for i, (lid, txt) in enumerate(lines):
        for w in txt.split():
            out.append((i, w, norm(w)))
    return out
def compare(a_lines, b_lines):
    A, B = words(a_lines), words(b_lines)
    ka = [n if n is not None else f"\x00a{k}" for k, (_, _, n) in enumerate(A)]
    kb = [n if n is not None else f"\x00b{k}" for k, (_, _, n) in enumerate(B)]
    sm = difflib.SequenceMatcher(None, ka, kb, autojunk=False)
    ops = sm.get_opcodes()
    matched = sum(i2 - i1 for t, i1, i2, _, _ in ops if t == "equal")
    per = {}
    for t, i1, i2, j1, j2 in ops:
        for k in range(i1, i2):
            li = A[k][0]; m, n = per.get(li, (0, 0)); per[li] = (m + (t == "equal"), n + 1)
    return A, B, ops, matched, per
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--label", default="page")
    ap.add_argument("--merge", help="write a merged draft: agreed words plain, disagreements {A|B}")
    ap.add_argument("--check", action="store_true", help="exit 1 if --merge OUT differs from what would be written")
    ap.add_argument("--expand", action="store_true", help="expand common abbreviations and & before matching (PX-BRODEC)")
    o = ap.parse_args()
    global EXP; EXP = o.expand
    al, bl = load(o.a), load(o.b)
    A, B, ops, matched, per = compare(al, bl)
    agr = 2 * matched / max(1, len(A) + len(B))
    print(f"{o.label}\tlines A {len(al)} B {len(bl)}\twords A {len(A)} B {len(B)}\tmatched {matched}\tagreement {agr:.3f}")
    print(f"{o.label}\tillegible {{?}}: A {sum(1 for x in A if x[2] is None)} B {sum(1 for x in B if x[2] is None)}")
    for li, (lid, _) in enumerate(al):
        m, n = per.get(li, (0, 0))
        print(f"{o.label}\t{lid}\t{m}/{n}\t{(m / n if n else 0):.2f}")
    if o.merge:
        out_lines = {}
        for t, i1, i2, j1, j2 in ops:
            if t == "equal":
                for k in range(i1, i2):
                    out_lines.setdefault(A[k][0], []).append(A[k][1])
            else:
                aw = " ".join(A[k][1] for k in range(i1, i2)); bw = " ".join(B[k][1] for k in range(j1, j2))
                li = A[i1][0] if i2 > i1 else (A[i1 - 1][0] if i1 > 0 else 0)
                out_lines.setdefault(li, []).append("{" + aw + "|" + bw + "}")
        text = "".join(f"{al[li][0]}\t{' '.join(out_lines.get(li, []))}\n" for li in range(len(al)))
        if o.check:
            sys.exit(0 if open(o.merge, encoding="utf-8").read() == text else 1)
        open(o.merge, "w", encoding="utf-8").write(text)
main()
