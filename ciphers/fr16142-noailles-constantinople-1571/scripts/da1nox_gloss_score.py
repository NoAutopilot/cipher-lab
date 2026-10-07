#!/usr/bin/env python3
"""DA1-NOX: score a blind word-level read of the c262 gloss against gloss.tsv per PREREG-DA1NOX.md.

usage: da1nox_gloss_score.py READ.tsv   (columns: line, read; '#' lines ignored)
Normalisation = scripts/d2noxb2_score.py's (PX-BRODEC) except that an apostrophe is dropped without splitting the word
(j'ay = jay, s'aller = saller), registered in PREREG-DA1NOX.md before any pass was scored.
Control L07, L10, L11, L12 (unchanged by DEF1-NOXG and R7A-NOX262); gate pooled >= 0.80. Exit 0 PASS, 3 FAIL.
"""
import difflib, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ABBR = {"q": "que", "nre": "nostre", "vre": "vostre", "sr": "seigneur", "mt": "mont", "md": "monseigneur",
        "ms": "messieurs", "sm": "sa majeste", "mte": "majeste", "&": "et"}
CONTROL, GATE = ["L07", "L10", "L11", "L12"], 0.80

def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("[?]", " QQQ ").replace("'", "").replace("’", "").replace("&", " et ")
    s = re.sub(r"[^a-zQ ]", " ", s)
    s = s.replace("v", "u").replace("j", "i").replace("y", "i")
    out = []
    for t in s.split():
        out.extend(ABBR.get(t, t).split())
    return out

def load(p, col):
    d = {}
    for ln in Path(p).read_text(encoding="utf-8").splitlines():
        if ln.startswith("#") or not ln.strip():
            continue
        f = ln.split("\t")
        if re.fullmatch(r"L\d\d", f[0]) and len(f) > col:
            d[f[0]] = f[col]
    return d

def agree(read, ans):
    a, b = norm(read), norm(ans)
    m = sum(x.size for x in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
    return m, len(b)

if __name__ == "__main__":
    read, gloss = load(sys.argv[1], 1), load(HERE / "gloss.tsv", 1)
    tot = [0, 0]
    for L in sorted(read):
        m, n = agree(read[L], gloss.get(L, ""))
        role = "control" if L in CONTROL else "target"
        if role == "control":
            tot[0] += m; tot[1] += n
        print(f"{L}\t{role}\t{m}/{n}\t{m/n if n else 0:.3f}\tread={' '.join(norm(read[L]))}\tgloss={' '.join(norm(gloss.get(L,'')))}")
    p = tot[0] / tot[1] if tot[1] else 0
    print(f"CONTROL pooled {tot[0]}/{tot[1]} = {p:.3f} gate {GATE} -> {'PASS' if p >= GATE else 'FAIL'}")
    sys.exit(0 if p >= GATE else 3)
