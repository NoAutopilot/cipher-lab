#!/usr/bin/env python3
"""D2-NOXB2: score read-D2NOXB2.tsv against gloss.tsv per PREREG-D2NOXB2.md (PX-BRODEC normalisation, difflib agreement).

Control lines L07/L09/L10 (unchanged by 4ef591e8c); gate pooled >= 0.80. Exit 0 if the gate passes, 3 if not.
"""
import difflib, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ABBR = {"q": "que", "nre": "nostre", "vre": "vostre", "sr": "seigneur", "mt": "mont", "md": "monseigneur",
        "ms": "messieurs", "sm": "sa majeste", "mte": "majeste", "&": "et"}
CONTROL, GATE = ["L07", "L09", "L10"], 0.80

def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("[?]", " QQQ ").replace("'", " ").replace("&", " et ")
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
        if re.fullmatch(r"L\d\d", f[0]):
            d[f[0]] = f[col]
    return d

def agree(read, ans):
    a, b = norm(read), norm(ans)
    m = sum(x.size for x in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
    return m, len(b)

read, gloss = load(HERE / "read-D2NOXB2.tsv", 2), load(HERE / "gloss.tsv", 1)
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
