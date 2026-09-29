#!/usr/bin/env python3
"""VERIFY-CEPPO-D2-2 step 3 (29 Sept 2026): do the endorsed f.21v / f.87 passages survive without the I signs and
without the double-barred-oval = r reading?
Per line, four decodes of the verifier's D (verify_d2/<folio>/passD.tsv) under Tomokiyo's printed values:
  AUD   as the first audit read (X_THETA2 = r, S60 = printed r, X_POUND/X_NEW unkeyed)
  NOOV  no override: X_THETA2 and every S60 position (all are the double-barred oval) unkeyed '_', pound unkeyed
  STRICT NOOV, and also every letter not graded S (both raw passes and D agree at H) masked '.'
and the two raw blind passes A and B decoded alone (NOOV values). For each endorsed passage: present in each
decode (exact substring, '_' and '.' count as a miss), and in A/B the best alignment (letters matching, sliding
window). Usage: override_d2.py  (both folios)"""
import csv, json, glob
from pathlib import Path
H = Path(__file__).resolve().parent.parent
m = {e["id"]: e["value"] for e in json.load(open(H / "sign_id_map.json"))}
PASS = {"f21v": {"L01": ["tuttoda"], "L03": ["questacarica", "diqua"], "L04": ["credolene"],
                 "L05": ["cederuiuendoetseruend"], "L09": ["tantodi", "indiuerse"], "L11": ["fatto", "fadificu"]},
        "f87": {"L04": ["ungiornoauanti"], "L05": ["neandosecre", "amente"]}}

def val(s, mode):
    if mode != "AUD" and s in ("X_THETA2", "S60"): return "_"
    if mode == "AUD" and s == "X_THETA2": return "r"
    v = m.get(s)
    return "_" if v is None else ("" if v == "null" else ("et" if v == "et" else v))

def dec_rows(rows, mode):
    out = ""
    for r in rows:
        t = val(r["sign_id"].strip(), mode)
        if mode == "STRICT" and t and not (r.get("conf") == "H" and r.get("src") == "AB"): t = "." * len(t)
        out += t
    return out

def best(sub, text):
    b = (0, "")
    for i in range(0, max(1, len(text) - len(sub) + 1)):
        w = text[i:i + len(sub)]; k = sum(a == c for a, c in zip(sub, w))
        if k > b[0]: b = (k, w)
    return b

for fo, want in PASS.items():
    D = {}
    for r in csv.DictReader(open(H / "verify_d2" / fo / "passD.tsv"), delimiter="\t"):
        D.setdefault(r["passage"], []).append(r)
    raw = {}
    for tag in "AB":
        raw[tag] = {}
        for f in sorted(glob.glob(str(H / fo / f"pass{tag}*.tsv"))):
            for r in csv.DictReader(open(f), delimiter="\t"):
                raw[tag].setdefault(r["passage"], []).append(r)
    print(f"== {fo}")
    for ln, subs in want.items():
        dd = {md: dec_rows(D[ln], md) for md in ("AUD", "NOOV", "STRICT")}
        ab = {t: dec_rows(raw[t].get(ln, []), "NOOV") for t in "AB"}
        for md in ("AUD", "NOOV", "STRICT"): print(f"  {ln} {md:6} {dd[md]}")
        for t in "AB": print(f"  {ln} raw{t}   {ab[t]}")
        for s in subs:
            res = [f"{md}:{'Y' if s in dd[md] else 'n'}" for md in ("AUD", "NOOV", "STRICT")]
            strict_best = best(s, dd["STRICT"]); noov_best = best(s, dd["NOOV"])
            rb = [f"raw{t} {best(s, ab[t])[0]}/{len(s)} '{best(s, ab[t])[1]}'" for t in "AB"]
            print(f"   * {s:22} {' '.join(res)}  NOOV {noov_best[0]}/{len(s)} '{noov_best[1]}'  STRICT "
                  f"{strict_best[0]}/{len(s)} '{strict_best[1]}'  {'  '.join(rb)}")
