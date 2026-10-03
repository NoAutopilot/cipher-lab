#!/usr/bin/env python3
"""Reconcile two blind passes of Krauske's 1893 key table (Loc. 694/10 ff.2-5) into key.tsv and compounds.tsv.

GAPS151 (account-4, 3 Oct 2026). Inputs: table_passes/pass{A,B}_f{2-3,4-5}.tsv (two blind Opus passes over
images/table_crops). Values where the passes agree are taken as read; the reconciler's settlements (RECON below) are
logged with their reason. Grade: C -- Krauske's table is an 1893 archivist's compilation of decipherments
("Einige Chiffre-Aufloesungen"), not the 1712 key sheet; M where the passes split on the value, where a value
carries '?', or where Krauske lists alternatives (value 'a|b'). Null codes (non-valeurs) get value '' (grade M:
Krauske himself marks them "wahrscheinlich"/"?").
  python3 reconcile_table.py           write key.tsv, compounds.tsv
  python3 reconcile_table.py --check   exit 1 if the committed files differ
"""
import csv, re, sys, pathlib
D = pathlib.Path(__file__).resolve().parent
P = D / "table_passes"

# reconciler settlements: code -> (value, grade, reason)
RECON = {
    "259": ("Ilgen", "M", "passes split Ilgen?/Flynn?; Ilgen also in f.2 notes to codes 9, 39, 46 (both passes); Prussian minister H.R. von Ilgen fits Berlin 1712"),
    "260": ("Kameke", "M", "passes split Kameke?/Haacken?; pass A reads Kameke in f.2 note to code 11; Prussian minister P.A. von Kameke fits"),
    "191": ("Stenbock", "M", "passes split Stenbock?/Steenbock?; spelling only; 694/08 f.468 gloss reads Stenbock over 191 (A2-SAX2)"),
    "130": ("Walling", "M", "both passes Walling?; Kurrent, f.2 note to code 3 read Welling/Walling"),
    "217": ("la reine d'Angleterre", "C", "both passes; line-wrap joined"),
    "153": ("der Statthalter Prinz von Fuerstenberg", "C", "both passes; line-wrap joined"),
    "227": ("le roi de Danemark|Danemark", "M", "two values written"),
    "298": ("la France|le roi de France", "M", "two values written"),
    "266": ("Hannover|Electeur de Hanovre", "M", "two values written"),
    "301": ("", "M", "nonvaleur (first word unclear, both passes)"),
    "95": ("te", "M", "value struck through (both passes)"),
}

def load(p):
    out = []
    for r in csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"):
        if r["code"].strip() == "HEAD":
            continue
        out.append({k: (v or "").strip() for k, v in r.items()})
    return out

def norm_code(c):
    return c.replace(" ", "").rstrip(".")

def alts(v):
    v = v.strip().rstrip(".:")
    toks = [t.strip(".:,; ") for t in re.split(r"[ .]+", v) if t.strip(".:,; ")]
    return toks

def build():
    key, comp = [], []
    for grp in ("f2-3", "f4-5"):
        A = {norm_code(r["code"]): r for r in load(P / f"passA_{grp}.tsv")}
        B = {norm_code(r["code"]): r for r in load(P / f"passB_{grp}.tsv")}
        for c in dict.fromkeys(list(B) + list(A)):
            a, b = A.get(c, {}), B.get(c, {})
            va, vb = a.get("value", ""), b.get("value", "")
            # passes sometimes put Krauske's second/third alternative in the note column: join value+note-if-short
            note = b.get("note") or a.get("note", "")
            if c in RECON:
                v, g, why = RECON[c]
            elif not re.fullmatch(r"\d+", c):
                comp.append((c, vb or va, "C" if va == vb else "M"))
                continue
            else:
                ja = " ".join([va] + ([a.get("note", "")] if len(alts(a.get("note", ""))) and all(len(t) <= 3 for t in alts(a.get("note", ""))) else []))
                jb = " ".join([vb] + ([b.get("note", "")] if len(alts(b.get("note", ""))) and all(len(t) <= 3 for t in alts(b.get("note", ""))) else []))
                ta, tb = alts(ja.replace("?", "")), alts(jb.replace("?", ""))
                if not ta and not tb and "valeur" not in note:
                    continue  # no value written by Krauske: left unkeyed
                if not ta and not tb:
                    v, g, why = "", "M", "null (non-valeur): " + note
                elif ta == tb:
                    if len(ta) == 2 and len(ta[0]) <= 3 and ta[1][:1].isupper():
                        v, g, why = ta[0], ("M" if "?" in ja + jb else "C"), "passes agree; example word written beside: " + ta[1]
                    elif all(len(t) <= 3 and t.islower() for t in ta):
                        v = "|".join(ta); g = "M" if ("?" in ja + jb or len(ta) > 1) else "C"; why = "passes agree"
                    else:
                        v = " ".join(ta); g = "M" if "?" in ja + jb else "C"; why = "passes agree"
                else:
                    v = "|".join(dict.fromkeys(ta + tb)); g = "M"; why = f"passes split A={ja!r} B={jb!r}"
            if c in RECON:
                why = "reconciler: " + why
            key.append((c, v, g, "Krauske 1893, Loc. 694/10 f." + (a.get("folio") or b.get("folio")), why + ("; note: " + note if note and "split" not in why and "null" not in why else "")))
    return key, comp

def compound_check(key, comp):
    val = {c: v for c, v, *_ in key}
    rows = []
    for c, word, g in comp:
        parts = [p for p in c.split(".") if p.isdigit()]
        spelled = "".join((val.get(p, "?").split("|")[0]) for p in parts)
        w = re.sub(r"[^a-z]", "", word.lower().replace("ö", "o").replace("ü", "u"))
        ok = w.startswith(spelled.lower()) if "?" not in spelled else False
        rows.append((c, word, g, spelled, "agree" if ok else "disagree"))
    return rows

def render(key, comp):
    k = "code\tvalue\tgrade\tsource\tnote\n" + "".join("\t".join(r) + "\n" for r in key)
    cc = compound_check(key, comp)
    n = sum(r[4] == "agree" for r in cc)
    c = (f"# compound codes (Krauske f.5 R): letter codes spelled through key.tsv vs the word's opening; {n}/{len(cc)} agree\n"
         "compound\tword\tgrade\tspelled_by_key\tcheck\n" + "".join("\t".join(r) + "\n" for r in cc))
    return k, c

if __name__ == "__main__":
    k, c = render(*build())
    files = {D / "key.tsv": k, D / "compounds.tsv": c}
    if "--check" in sys.argv:
        bad = [p.name for p, t in files.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        print("stale: " + ", ".join(bad) if bad else "OK"); sys.exit(1 if bad else 0)
    for p, t in files.items():
        p.write_text(t, encoding="utf-8")
    print(c.splitlines()[0]); print(len(k.splitlines()) - 1, "key rows")
