#!/usr/bin/env python3
"""H278 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only: the fr16 contexts behind H268's counts, verbatim, so the verifier reads
the period usage itself. For each of the three source files (Catherine de Medicis t.1-2, Marguerite de Valois; tools/data/fr16/MANIFEST.tsv) every
occurrence of 'entendoit', 'entendoient' and of any enten- imperfect form (entenoit, entenoyt, entenoient), matched on the normalised token (lower-cased, accents
stripped, apostrophes split, punctuation stripped), printed with ten words either side and the file name; the raw (un-normalised) window is given too. Descriptive. Found on the first run (29 Sept 2026): H268's phrase count "l entendoit 5" was the substring of
"il entendoit" (qu'il / s'il entendoit) -- the object-pronoun phrase l'entendoit is not attested here; corrected in NOTES/HYPOTHESES/V9_PAGE.
python3 h278_entendoit_contexts.py [--check]"""
import gzip, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.abspath(f"{HERE}/../../../tools/data/fr16")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
FORMS = ["entendoit", "entendoient", "entenoit", "entenoyt", "entenoient"]
rows = []
for f in sorted(os.listdir(D)):
    if not f.endswith(".gz"): continue
    raw = re.sub(r"\s+", " ", gzip.open(f"{D}/{f}", "rt", encoding="utf-8", errors="ignore").read())
    rt = raw.replace("'", " ").split(" "); nt = [re.sub(r"[^a-z]", "", norm(w)) for w in rt]   # punctuation stripped for the match only
    for i, w in enumerate(nt):
        if w in FORMS:
            rows.append(f"{f.split('_')[0]} | {w} | ... " + " ".join(rt[max(0, i - 10):i + 11]) + " ...")
rows.sort(key=lambda r: (r.split(" | ")[1], r))
out = "\n".join(rows) + f"\n{len(rows)} contexts\n"; p = f"{HERE}/h278_entendoit_contexts_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
