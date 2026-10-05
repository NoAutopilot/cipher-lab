#!/usr/bin/env python3
"""DIN-FIRM step 2 (3 Oct 2026): strict-rule regrade of f.130r after the per-occurrence conflict check.

Rule (firm/PREREG.md): VERIFY-DIN2's strict_no_conflict (agree >= 2, no conflicting print alignment, token read H),
except that a row whose every conflict in firm/conflicts.tsv is 'spelling', 'slip' or (look/PREREG.md unit 1, D2-DIN0 5 Oct 2026)
'transcription' (the sign is 0', merged under 0 by the f.128 transcription) counts as conflict-free.
Writes f130/print/key_dk_strict.tsv (key_dk.tsv with the strict grade per row) and firm/result.json.
  python3 ciphers/fr3621-dinteville-1592/firm/firm_grades.py [--check]   (--check: exit 1 if outputs are stale)
"""
import csv, json, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
TGT = HERE.parent
NAME = {"#": "hash"}

kp = {r["sign"]: r for r in csv.DictReader(open(TGT / "f128/print_align/key_print.tsv", encoding="utf-8"), delimiter="\t")}
conf = defaultdict(list)
for r in csv.DictReader(open(HERE / "conflicts.tsv", encoding="utf-8"), delimiter="\t"):
    conf[r["row"]].append(r["class"])
promoted = sorted(s for s, cl in conf.items() if cl and all(c in ("spelling", "slip", "transcription") for c in cl))


def strict_ok(sign):
    k = kp.get(sign)
    if not k:
        return None
    clean = (not k["others"].strip()) or sign in promoted
    return int(k["agree"]) >= 2 and clean


rows = list(csv.reader(open(TGT / "f130/print/key_dk.tsv", encoding="utf-8"), delimiter="\t"))
out_rows = [rows[0]]
for r in rows[1:]:
    s = "#" if r[0] == "hash" else r[0]
    ok = strict_ok(s)
    out_rows.append([r[0], r[1], "C" if ok else "M", r[3] + ("" if ok else " (strict: M)")])
key_txt = "".join("\t".join(r) + "\n" for r in out_rows)

toks = [r for r in csv.DictReader(open(TGT / "f130/print/tokens.tsv", encoding="utf-8"), delimiter="\t") if r["sign"] != "."]
g = Counter()
for r in toks:
    s = "#" if r["sign"] == "hash" else r["sign"]
    ok = strict_ok(s)
    g["U" if ok is None else ("C" if ok and r["conf"] == "H" else "M")] += 1
res = {"conflicts": {k: v for k, v in conf.items()}, "promoted_rows": promoted,
       "strict_grades_before": {"C": 177, "M": 311, "U": 39},
       "strict_grades_after": {k: g[k] for k in ("C", "M", "U")}}
res_txt = json.dumps(res, indent=1) + "\n"
targets = {TGT / "f130/print/key_dk_strict.tsv": key_txt, HERE / "result.json": res_txt}
if "--check" in sys.argv:
    bad = [str(p) for p, t in targets.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
    print(res_txt); print("check: committed outputs match" if not bad else "check: STALE " + ", ".join(bad))
    sys.exit(1 if bad else 0)
for p, t in targets.items():
    p.write_text(t, encoding="utf-8")
print(res_txt)
