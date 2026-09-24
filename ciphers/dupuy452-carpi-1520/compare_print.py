#!/usr/bin/env python3
"""Letter agreement between reading.txt and the printed plaintext of the cipher passage (Jacqueton 1892,
P.J. XXXIII, print/jacqueton1892_PJ33.txt), from "du bon tour" to "touchant les affaires" (the editor's
"Commencement/Fin du chiffre" marks). Word signs are removed from both sides; letters are normalised
(accents off, j->i, v->u, y->i, h dropped because the transcription merged the key's y and h).
Reports the longest-common-subsequence letter count. Solver worker, 24 Sept 2026."""
import difflib, os, re, unicodedata
H = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(H, "print/jacqueton1892_PJ33.txt"), encoding="utf-8").read()
p = t[t.index("du  bon  tour  que"):t.index("touchant  les  affaires  (1)") + len("touchant  les  affaires")]
p = re.sub(r"\(1\)\s+Commencement\s+du\s+chiffre\.", "", p)
p = re.sub(r"(\d+\s+)?x+i*\.\s+—\s+25\s+octobre\s+1525(\s+\d+)?", "", p, flags=re.I)
p = unicodedata.normalize("NFD", p.lower())
p = re.sub(r"\b(marquis de pesquere|duc de bar|millan|madame|veniciens|cardinal de come|france)\b", "",
           unicodedata.normalize("NFD", "".join(c for c in p if not unicodedata.combining(c))))
def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if c.isalpha() and ord(c) < 128)
    return s.replace("j", "i").replace("v", "u").replace("y", "i").replace("h", "")
r = "".join(l.split("| ", 1)[1] for l in open(os.path.join(H, "reading.txt"), encoding="utf-8") if "| " in l)
r = re.sub(r"<[^>]*>|\[[^\]]*\]", "", r)
R, P = norm(r), norm(p)
sm = difflib.SequenceMatcher(None, R, P, autojunk=False)
m = sum(b.size for b in sm.get_matching_blocks())
print(f"reading letters {len(R)}, print letters {len(P)}, common {m} ({m/len(P):.1%} of print), ratio {sm.ratio():.3f}")
