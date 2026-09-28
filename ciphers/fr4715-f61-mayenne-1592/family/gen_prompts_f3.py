#!/usr/bin/env python3
"""F61-FAMILY-3 (28 Sept 2026): generate the per-call prompt files passes/prompts_f3/<call>.txt from passes/PROMPTS_f188_f184_f106.md."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; ROOT = os.path.abspath(f"{HERE}/../../..")
src = open(f"{P}/PROMPTS_f188_f184_f106.md").read()
sec = {m.group(1): m.group(2).strip() for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", src, re.S | re.M)}
atlas = "\n".join(l.rstrip("\n") for l in open(f"{HERE}/../scripts/f61_atlas.tsv") if not l.startswith("#") and not l.startswith("code\t"))
atlas += "\nH24\ta 2-like curl joined to a crossed 4 (the '24' sign); distinct from HASH4, the plain dense crossed-4/hash cluster\nLOOPS\ta chain of two or more small loops written side by side with NO stem and NO bar (like 'oo' or 'ooo'); a chain that sits on a vertical stem is PHI, not LOOPS\nZBAR\ta z-like or 2-like zigzag stroke with a horizontal bar through or under it and no stems; distinct from ZHOOK (a 7/Z hook over two slanted stems)\nRSIGN\ta small r-like or 5-like sign, a short stem with a hook to the right, no loop"
os.makedirs(f"{P}/prompts_f3", exist_ok=True)
def w(name, text): open(f"{P}/prompts_f3/{name}.txt", "w").write(text + "\n")
def fmt(t, **kw):
    for k, v in kw.items(): t = t.replace("{" + k + "}", str(v))
    return t
chunks = {"c1": range(1, 9), "c2": range(9, 17), "c3": range(17, 24)}
for ck, rng in chunks.items():
    bands = [f"L{i:02d}" for i in rng]; paths = [f"{HERE}/sheets/f188r/f188r_{b}_s{s}.jpg" for b in bands for s in range(1, 6)]
    for pas in "AB":
        t = sec["f.188r sign pass template (Desportes' hand, no gloss on the leaf: the clear words are INSIDE the rows)"]
        w(f"f188_signs{pas}_{ck}", fmt(t, nb=len(bands), bands=", ".join(bands), atlas=atlas, ni=len(paths), paths="\n".join(paths), out=f"{P}/f188r_signs{pas}_{ck}.tsv"))
paths = [f"{HERE}/sheets/f184r/f184r_S{k:02d}_h{h}.jpg" for k in range(1, 13) for h in (1, 2)]
for pas in "AB":
    t = sec["f.184r clear-text pass template (the separate-sheet decipherment of f.188, plain French, one hand)"]
    w(f"f184_clear{pas}", fmt(t, paths="\n".join(paths), out=f"{P}/f184r_clear{pas}.tsv"))
paths = [f"{HERE}/sheets/f106r/f106r_L{b:02d}_s{s}.jpg" for b in range(1, 7) for s in range(1, 8)]
for pas in "AB":
    t = sec["f.106r sign pass template (Mayenne's secretary, dense, sparse gloss, heavy bleed-through)"]
    w(f"f106_signs{pas}", fmt(t, atlas=atlas, paths="\n".join(paths), out=f"{P}/f106r_signs{pas}.tsv"))
    t = sec["f.106r gloss pass template"]
    w(f"f106_gloss{pas}", fmt(t, paths="\n".join(paths), out=f"{P}/f106r_gloss{pas}.tsv"))
print("written", sorted(os.listdir(f"{P}/prompts_f3")))
