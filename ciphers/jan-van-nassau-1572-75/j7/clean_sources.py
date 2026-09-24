#!/usr/bin/env python3
"""J7 (24 Sept 2026): cleaned German sources for tools/german_ngram.py.
Writes j7/src_5549_clear.txt (the clear German of 5549 from Groen Suppl. no.45, numeral runs cut out as paragraph
breaks, dbnl note markers removed) and j7/src_cdxliv.txt (Groen IV CDXLIV = WVO 5797, the held-out control text)."""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(H)
R = os.path.dirname(os.path.dirname(T))

def clean(txt, start):
    txt = txt[txt.find(start):] if start in txt else txt
    txt = re.sub(r"Ga naar (voet|marge)noot\S*\s*\[#\d+\]", " ", txt)
    txt = re.sub(r"\[[^\]]*\]\([^)]*\)|\[#[^\]]*\]|\[/[^\]]*\]", " ", txt)
    txt = re.sub(r"(?:\b[0-9ivxlc]+\.?\s*(?:[a-zäöüß]{1,4}\.?\s+)?){1,}(?=\s)", lambda m: "\n\n" if re.search(r"\d", m.group(0)) else m.group(0), txt)
    return txt

g = open(os.path.join(T, "groen", "gpas_lettre45.txt"), encoding="utf-8").read()
open(os.path.join(H, "src_5549_clear.txt"), "w").write(clean(g[:g.find("PS. Nachdem")], "Mein willig dienst sey"))
c = open(os.path.join(R, "ciphers", "lodewijk-van-nassau-1573-74", "groen", "groen_IV_CDXLIV.txt"), encoding="utf-8").read()
c = c[c.find("Gnediger Herr. E.G. schreiben"):]
end = c.find("Verantwoording")
c = c[:end] if end > 0 else c
open(os.path.join(H, "src_cdxliv.txt"), "w").write(clean(c, "Gnediger"))
