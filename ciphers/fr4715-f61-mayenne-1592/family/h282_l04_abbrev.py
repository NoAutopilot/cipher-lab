#!/usr/bin/env python3
"""H282 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only: f.61 L04 2 OTHER is 'an S/8-like loop joined to a b/d form, written after
Come; may be a handwriting abbreviation (e.g. S.M.)' (H238; read_call_U pass U2, low confidence). In tools/data/fr16 (normalised as H268), what follows
'comme' / 'come': the share of next tokens that are a majesty formula (sa, sadicte, sadite, s, v, vostre + majeste) against the rest, and the count of
the abbreviations 's m', 'v m', 's a' as tokens anywhere. Descriptive for the OTHER rows of the null-band table; no value.  [--check]"""
import gzip, os, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.abspath(f"{HERE}/../../../tools/data/fr16")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
toks = []
for f in sorted(os.listdir(D)):
    if f.endswith(".gz"): toks += re.findall(r"[a-z]+", norm(gzip.open(f"{D}/{f}", "rt", encoding="utf-8", errors="ignore").read()).replace("'", " "))
nxt = Counter(toks[i + 1] + (" " + toks[i + 2] if toks[i + 1] in ("sa", "sadicte", "sadite", "s", "v", "vostre", "vtre") else "") for i in range(len(toks) - 2) if toks[i] in ("comme", "come"))
n = sum(nxt.values()); maj = sum(v for k, v in nxt.items() if "majest" in k or k in ("s m", "v m"))
abbr = Counter(toks[i] + " " + toks[i + 1] for i in range(len(toks) - 1) if toks[i] in ("s", "v") and toks[i + 1] in ("m", "a"))
rows = [f"'comme/come' + next: {n} cases; majesty formula next {maj} ({maj / n:.3f})" if n else "no 'comme'",
        "top next tokens: " + ", ".join(f"{k} {v}" for k, v in nxt.most_common(12)),
        "abbreviation tokens anywhere: " + ", ".join(f"{k} {v}" for k, v in abbr.most_common()) if abbr else "abbreviation tokens anywhere: none"]
out = "\n".join(rows) + "\n"; p = f"{HERE}/h282_l04_abbrev_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
