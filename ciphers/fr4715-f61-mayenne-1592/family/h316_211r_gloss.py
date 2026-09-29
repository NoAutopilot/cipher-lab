#!/usr/bin/env python3
"""H316 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): the period gloss above fr.3983 f.211r's one cipher run (ASKS 93, open since
28 Sept for a person's reading). Two independent blind Opus reads of the gloss words only (scripts/PROMPTS.md H316) on H315's two segments
(family/sheets/f211r_run_s1/s2.jpg), each word with its x span on the sheet (s2 x + 1480). Gate, fixed before the calls: the passes agree EXACTLY
(case- and accent-folded) on >= 3 words, matched in order by overlapping x span, and each agreed word occurs in tools/data/fr16 (the era corpus);
agreed words are then grade M (S at most) for H317; ASKS 93 stays open for a person's reading either way. H34/H35 found model gloss readers fail on
f.108r's gloss hand, so a FAIL is the expected outcome.  python3 h316_211r_gloss.py [--check]"""
import csv, glob, gzip, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../..")
fold = lambda w: unicodedata.normalize("NFKD", w).encode("ascii", "ignore").decode().lower().strip(".,;:'\"")
def load(tag):
    rows = []
    for n, off in ((1, 0), (2, 1480)):
        for r in csv.DictReader((l for l in open(f"{HERE}/passes/f211r_s{n}_gloss{tag}.tsv") if not l.startswith("#")), delimiter="\t"):
            rows.append((int(float(r["x_from"])) + off, int(float(r["x_to"])) + off, r["word"].strip(), r.get("conf", "").strip()))
    rows.sort(); dd = []
    for r in rows:  # the same word seen in both segments' overlap: keep one
        if dd and r[0] < dd[-1][1] and fold(r[2]) == fold(dd[-1][2]): continue
        dd.append(r)
    return dd
A, B = load("A"), load("B")
words = set()
for f in glob.glob(f"{ROOT}/tools/data/fr16/*.txt.gz") + glob.glob(f"{ROOT}/tools/data/fr16/*.txt"):
    t = (gzip.open(f, "rt", errors="ignore") if f.endswith(".gz") else open(f, errors="ignore")).read()
    words |= {fold(w) for w in re.findall(r"[A-Za-zÀ-ÿ]+", t)}
pairs = [(a, b) for a in A for b in B if min(a[1], b[1]) - max(a[0], b[0]) > 0]
agree = [(a, b) for a, b in pairs if fold(a[2]) == fold(b[2])]
ok = [a for a, b in agree if fold(a[2]) in words]
out = [f"pass A {len(A)} words: " + " | ".join(f"{w} ({x0}-{x1}, {c})" for x0, x1, w, c in A),
       f"pass B {len(B)} words: " + " | ".join(f"{w} ({x0}-{x1}, {c})" for x0, x1, w, c in B),
       f"x-overlapping pairs {len(pairs)}; exact agreements {len(agree)}: " + ", ".join(a[2] for a, _ in agree) + f"; of them in fr16: {len(ok)}",
       "gate: " + ("PASS -- agreed words grade M for H317: " + ", ".join(f"{a[2]} ({a[0]}-{a[1]})" for a in ok) if len(ok) >= 3 else "FAIL (fewer than 3 agreed fr16 words); the gloss stays unread, ASKS 93 open")]
txt = "\n".join(out) + "\n"; res = f"{HERE}/h316_211r_gloss_result.txt"
if "--check" in sys.argv:
    k = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if k else "STALE"); sys.exit(0 if k else 1)
open(res, "w").write(txt); print(txt, end="")
