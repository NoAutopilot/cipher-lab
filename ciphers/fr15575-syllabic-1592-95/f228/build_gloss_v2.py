#!/usr/bin/env python3
"""N8-NV05: gloss_v2_diplomatic.tsv (reconciled GA/GB read, abbreviations as written) -> gloss_v2.tsv.

  python3 build_gloss_v2.py [--check]

Only the fixed rule of PREREG-ADDENDUM-N8.md: unread [..] spans removed, '?' doubt marks and '^' superscript marks
dropped (letters kept), reader-marked abbreviations expanded by this list only: qe/qȷe -> que, ql/qel/qȷel -> que el,
dho -> dicho, dha -> dicha, V.Md/V.Mg -> V.M. (score_control's table then gives vuestramagestad). Everything else
(norm(), the q/q~/qs/V.M./S.M./duq table) is score_control.py's, applied at scoring time.
--check exits 1 if gloss_v2.tsv is stale (rule 7).
"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EXP = [(r"\bq[ȷ]?e\b", "que"), (r"\bq[ȷ]?e?l\b", "que el"), (r"\bdho\b", "dicho"), (r"\bdha\b", "dicha"),
       (r"\bV\.\s?M[dg]\b\.?", "V.M.")]


def clean(t):
    t = re.sub(r"\[\.\.\]", " ", t).replace("?", "").replace("^", "")
    for pat, rep in EXP:
        t = re.sub(pat, rep, t)
    return re.sub(r"\s+", " ", t).strip()


def build():
    out = ["line\ttext"]
    with open(os.path.join(HERE, "gloss_v2_diplomatic.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            out.append(f"{r['line']}\t{clean(r['text'])}")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    txt, p = build(), os.path.join(HERE, "gloss_v2.tsv")
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p, encoding="utf-8").read() == txt
        print("gloss_v2.tsv up to date" if ok else "gloss_v2.tsv is stale"); sys.exit(0 if ok else 1)
    open(p, "w", encoding="utf-8").write(txt); print(txt, end="")
