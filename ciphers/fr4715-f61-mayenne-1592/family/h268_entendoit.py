#!/usr/bin/env python3
"""H268 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): Tomokiyo's span S5 on f.61 L11 is 'melente-noit' (tomokiyo_spans.tsv), the dash at
L11 8 (4STEM, f.61 reading cell a/n) and his n at L11 9 (the 4-over-Pi, V8: a/n grade M on his letter alone). Read as French, 'me l'ente?noit' has no
word for '?' + 'noit' ('entenoit' is not a form), but 'me l'entendoit' (entendre, imperfect) fits if L11 8 = n and L11 9 = d. Count, in the period
corpus tools/data/fr16 (Catherine de Medicis t.1-2 and Marguerite de Valois, gz, lower-cased, accents stripped), whole-word forms: entendoit /
entendoyt / entendoient / entendois / entendoy (the entend- stem) against entenoit / entenoyt / entenoient (the enten- stem), plus the phrases
"l'entendoit" and "entendoit tant" (H253: the clear word after L11's run is 'tant'). Pre-stated read-out: 'entendoit is the word' iff entendoit
(any listed entend- imperfect form) >= 5 and the enten- forms = 0. A plaintext lead (grade I) on two f.61 tokens for the verifier; it stands against
one published letter (his n at L11 9), so it is reported as a candidate correction to a published reading, never as a value.  [--check]"""
import gzip, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.abspath(f"{HERE}/../../../tools/data/fr16")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
txt = " ".join(norm(gzip.open(f"{D}/{f}", "rt", encoding="utf-8", errors="ignore").read()) for f in sorted(os.listdir(D)) if f.endswith(".gz"))
txt = re.sub(r"\s+", " ", txt)
FORMS = {"entend-": ["entendoit", "entendoyt", "entendoient", "entendois", "entendoy"], "enten-": ["entenoit", "entenoyt", "entenoient", "entenois"]}
rows = []; tot = {}
for stem, fs in FORMS.items():
    cs = {f: len(re.findall(rf"\b{f}\b", txt)) for f in fs}; tot[stem] = sum(cs.values())
    rows.append(f"{stem} forms: " + ", ".join(f"{f} {n}" for f, n in cs.items()) + f" (total {tot[stem]})")
for ph in ["l'entendoit", "l entendoit", "entendoit tant", "me l'entendoit", "l'entend"]:
    rows.append(f"phrase '{ph}': {len(re.findall(re.escape(ph), txt))}")
rows.append(f"corpus: {len(txt.split())} words")
ok = tot["entend-"] >= 5 and tot["enten-"] == 0
rows.append("read-out: " + ("entendoit is the word" if ok else "not settled by the corpus"))
out = "\n".join(rows) + "\n"; res = f"{HERE}/h268_entendoit_result.txt"
if "--check" in sys.argv:
    good = os.path.exists(res) and open(res).read() == out; print("check", "OK" if good else "STALE"); sys.exit(0 if good else 1)
open(res, "w").write(out); print(out, end="")
