#!/usr/bin/env python3
"""Grep CSP Domestic William and Mary vol. 1 (and vol. 2) IA djvu full text for SP 8/6/65 (GAPS111, 3 Oct 2026).

Usage: csp_grep.py V1_DJVU.txt [V2_DJVU.txt]
Fetch once: https://archive.org/download/calendarofstatep01grea_2/calendarofstatep01grea_2_djvu.txt
            https://archive.org/download/calendarofstatep02grea_1/calendarofstatep02grea_1_djvu.txt
Prints, per file, hits for: the three names (exact regexes and an OCR-fuzzy token match, edit distance <= 2,
long-s/f and c/e confusions folded), King William's Chest 6 references, and cipher words within 400 chars of any
name. Positive control: p. 387's neighbouring entries (Waldeck to Heinsius; Castanaga) must be found by the same
regex method, else exit 2.
"""
import re, sys

NAMES = {
    "ehrenstein": r"[EB][hb]ren\s?[sf][tl][ec]i[nu]",
    "bernsdorff": r"Bern[sf]?[dt]?or[fp]",
    "guldenstolp": r"G[uy]l[dl]en\s?[sf]tolp",
}
CIPHER = r"\b(?:de)?[cs][iy]ph(?:er|ers|ered|ring)?\b|\bcipher|\bcypher|\bchiffre|\bdecypher|\bdecipher"
CONTROLS = {"waldeck-heinsius": r"Waldeck\s+to\s+(?:Pensionary\s+)?Heinsius", "castanaga": r"Casta[nñ]aga"}

def fold(s):
    return s.lower().replace("f", "s").replace("ſ", "s").replace("c", "e").replace("y", "i")

def lev(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]

def ctx(t, i, w=160):
    return re.sub(r"\s+", " ", t[max(0, i - w): i + w])

def run(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    print(f"== {path} ({len(t)} chars)")
    out = {}
    for k, rx in NAMES.items():
        hits = [m.start() for m in re.finditer(rx, t)]
        out[k] = hits
        print(f"-- {k} regex: {len(hits)}")
        for i in hits:
            print("   ", ctx(t, i))
    for k in NAMES:
        tgt = fold(k)
        fz = []
        for m in re.finditer(r"[A-Za-zſ']{6,14}", t):
            w = fold(m.group().lstrip("d'D'"))
            if w != tgt and abs(len(w) - len(tgt)) <= 2 and lev(w, tgt) <= 2 and not re.match(NAMES[k], m.group().lstrip("d'D'")):
                fz.append((m.start(), m.group()))
        print(f"-- {k} fuzzy (not in regex): {len(fz)}")
        for i, g in fz:
            print("   ", g, "|", ctx(t, i, 100))
    ch = [m.start() for m in re.finditer(r"King\s+William.s\s+Chest,?\s*6\b", t)]
    print(f"-- King William's Chest 6 refs: {len(ch)}")
    allnames = sorted(i for v in out.values() for i in v)
    near = [m.start() for m in re.finditer(CIPHER, t, re.I) if any(abs(m.start() - n) < 400 for n in allnames)]
    print(f"-- cipher words within 400 chars of a name: {len(near)}")
    for i in near:
        print("   ", ctx(t, i))
    print(f"-- cipher words in file total: {len(re.findall(CIPHER, t, re.I))}")
    ok = True
    for k, rx in CONTROLS.items():
        n = len(re.findall(rx, t))
        print(f"-- control {k}: {n}")
        ok &= n > 0
    return ok

if __name__ == "__main__":
    ok = run(sys.argv[1])
    for p in sys.argv[2:]:
        run(p)
    sys.exit(0 if ok else 2)
