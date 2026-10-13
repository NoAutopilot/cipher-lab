#!/usr/bin/env python3
"""LAG-HIRES (13 Oct 2026): settle LAG-MARKS' doubt cells from the WVO PDF's embedded scan of 6179 (pp.2-3, 2237x3142 and
2208x3189 px, ~288 ppi, about 1.8x the 150-dpi renders in images/) and carry them forward, never silently.
Writes (1) lag_hires_look.tsv: lag_marks_look.tsv with the re-looked cells replaced, plus a provenance column;
(2) ciphertext_6179_v3.tsv: ciphertext_6179_v2.tsv with the settled tokens set to conf H, plus a provenance column.
v2 is left untouched (the committed family runs were built on it). 6467's two doubt cells are not re-looked: the WVO PDF
of 6467 embeds only an 831x1244 gray scan (~113 ppi), below the existing render.
  python3 build_v3.py [--check]    --check exits 1 if either output is stale."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PROV = "LAG-HIRES 13 Oct 2026: WVO 06179.pdf embedded scan ~288 ppi, blind Sonnet look + reconciler by eye"
# cell -> (settled, look, evidence); look 'sure' = settled at native resolution, 'doubt' = still not separable
CELLS = {
    "p2L22.10": ("10", "doubt", "second figure loop with rising stroke: 0 with tilde, 6 or an 8 (this hand's looped 8) not separable"),
    "p2L22.15": ("3", "sure", "bare 3; the stroke before it runs on into the b of 'bien' on the next line"),
    "p2L24.8": ("2", "sure", "bare 2; slash before it is a descender from the line above"),
    "p2L24.12": ("29^", "doubt", "bar above clear; second figure closed loop with descender, 4 vs 9 not separable in this hand"),
    "p2L24.21": ("11", "sure", "no bar above the 11 (the 11 two groups earlier has one)"),
    "p2L26.6": ("18", "sure", "second figure is this hand's looped 8 with ascender, unlike the round 0 of nearby 10s"),
    "p2L27.8": ("[mark]16", "doubt", "loop and long stem before the 16: ring-on-stem mark or a descender from the line above"),
    "p2L27.13": ("18", "sure", "looped 8 with ascender, same shape as p2L26.6; the 10 later in the line is a round 0"),
    "p2L27.16": ("[mark]12", "sure", "ring-on-stem mark with crossbar between the 16 and the 12"),
    "p2L27.28": ("16^", "sure", "bar above; second figure is the 6 with top stroke, as the 16 after 23^ in the same line"),
    "p2L28.20": ("4^", "sure", "distinct straight bar above the final 4"),
    "p3L7.4": ("[mark]15", "sure", "ring-on-stem mark between the 2 and the 15 (v2 already carries it as its own token)"),
    "p3L8.7": ("10", "doubt", "short stroke near the top of the 10 may be the following mark's crossbar"),
    "p3L9.13": ("[mark]11", "sure", "ring-and-slash mark between the 14 and the 11 (v2 already carries it as its own token)"),
}
# v2 tokens changed or confirmed by the sure settles: (line, pos) -> group
V3 = {("p2L22", "15"): "3", ("p2L24", "8"): "2", ("p2L24", "21"): "11", ("p2L26", "6"): "18", ("p2L27", "13"): "18",
      ("p2L27", "15"): "[mark]", ("p2L27", "16"): "12", ("p2L27", "28"): "16^", ("p2L28", "20"): "4^",
      ("p3L7", "3"): "[mark]", ("p3L7", "4"): "15", ("p3L9", "12"): "[mark]", ("p3L9", "13"): "11"}
def rl(f):
    return open(os.path.join(HERE, f), encoding="utf-8").read().splitlines()
out = {}
L = rl("lag_marks_look.tsv")
o = [L[0] + "\tprovenance"]
seen = set()
for l in L[1:]:
    c = l.split("\t")
    if c[0] == "6179" and c[1] in CELLS:
        s, lk, ev = CELLS[c[1]]
        o.append("\t".join([c[0], c[1], s, lk, ev, PROV + f"; was {c[2]} {c[3]} (LAG-MARKS)"])); seen.add(c[1])
    else:
        o.append(l + "\tLAG-MARKS 9 Oct 2026 (150-dpi render)")
assert seen == set(CELLS), set(CELLS) - seen
out["lag_hires_look.tsv"] = "\n".join(o) + "\n"
L = rl("ciphertext_6179_v2.tsv")
o = [L[0] + "\tprovenance"]
hit = set()
for l in L[1:]:
    c = l.split("\t")
    k = (c[0], c[1])
    if k in V3:
        was = f"{c[2]} {c[3]}"
        c[2], c[3] = V3[k], "H"
        c += [""] * (6 - len(c))
        c[4] = ""
        o.append("\t".join(c[:6]) + f"\t{PROV}; v2 was {was}"); hit.add(k)
    else:
        o.append(l + "\t" * (5 - l.count("\t")) + "\tv2")
assert hit == set(V3), set(V3) - hit
out["ciphertext_6179_v3.tsv"] = "\n".join(o) + "\n"
stale = 0
for f, t in out.items():
    p = os.path.join(HERE, f)
    if "--check" in sys.argv:
        stale |= not (os.path.exists(p) and open(p, encoding="utf-8").read() == t)
    else:
        open(p, "w", encoding="utf-8").write(t); print("wrote", f)
sys.exit(1 if stale else 0)
