#!/usr/bin/env python3
"""H280 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only, after H278's correction (the pronoun phrase l'entendoit is not attested
in fr16): an EXISTENCE check of the object-pronoun construction in the other French corpora on disk -- tools/data/fr16 (1570s-1600s letters), fr18
(1700s memoirs and gazette), fr19 and fr19v (1830-1888 novels and verse). Era-mismatched for fr18/fr19 (CLAUDE.md rule 3's corpus-era lesson), so this
says only whether the construction "<l|m|le|me|se> entend<oit|oient|ait|aient>" exists in French of any period on disk, never how likely it is in
1593. Normalisation as H268 (lower-cased, accents stripped, apostrophes split); the pronoun token must stand alone (so 'il entendoit' is excluded).
Also the enten- forms per corpus. Descriptive; no verdict.  python3 h280_pronoun_phrase.py [--check]"""
import gzip, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); DD = os.path.abspath(f"{HERE}/../../../tools/data")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
PRON = re.compile(r"\b(l|m|le|me|se) (entend(?:oit|oient|ait|aient))\b"); ENTEN = re.compile(r"\benten(?:oit|oient|ait|aient)\b")
rows = []
for d in ("fr16", "fr18", "fr19", "fr19v"):
    txt = " ".join(norm(gzip.open(f"{DD}/{d}/{f}", "rt", encoding="utf-8", errors="ignore").read()) for f in sorted(os.listdir(f"{DD}/{d}")) if f.endswith(".gz"))
    txt = re.sub(r"\s+", " ", txt.replace("'", " ")); hits = PRON.findall(txt); ex = [m.group(0) for m in PRON.finditer(txt)][:4]
    rows.append(f"{d}: pronoun + entend- {len(hits)}" + (f" ({'; '.join(ex)})" if ex else "") + f"; enten- forms {len(ENTEN.findall(txt))}; {len(txt.split())} words")
out = "\n".join(rows) + "\n"; p = f"{HERE}/h280_pronoun_phrase_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
