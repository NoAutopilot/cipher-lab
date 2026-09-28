#!/usr/bin/env python3
"""F61-FAMILY-4 (28 Sept 2026): generate the per-call prompt files passes/prompts_f4/<call>.txt from passes/PROMPTS_undec.md.
The atlas is the f.101r one (PROMPTS_f101r.md's atlas block, taken verbatim from that file)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
src = open(f"{P}/PROMPTS_undec.md").read()
sec = {m.group(1): m.group(2).strip() for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", src, re.S | re.M)}
f101 = open(f"{P}/PROMPTS_f101r.md").read()
atlas = f101[f101.index("Atlas (code TAB shape):\n") + len("Atlas (code TAB shape):\n"):f101.index("\n\nRead the {ni} images")]
os.makedirs(f"{P}/prompts_f4", exist_ok=True)
def w(name, text): open(f"{P}/prompts_f4/{name}.txt", "w").write(text + "\n")
def fmt(t, **kw):
    for k, v in kw.items(): t = t.replace("{" + k + "}", str(v))
    return t
chunks = {"c1": range(1, 9), "c2": range(9, 17), "c3": range(17, 25), "c4": range(25, 33), "c5": range(33, 41), "c6": range(41, 46)}
for ck, rng in chunks.items():
    bands = [f"L{i:02d}" for i in rng]; paths = [f"{HERE}/sheets/f124r/f124r_{b}_s{s}.jpg" for b in bands for s in range(1, 6)]
    for pas in "AB":
        w(f"f124r_signs{pas}_{ck}", fmt(sec["Sign pass template (f.124r)"], nb=len(bands), bands=", ".join(bands), atlas=atlas, ni=len(paths), paths="\n".join(paths), out=f"{P}/f124r_signs{pas}_{ck}.tsv"))
        w(f"f124r_gloss{pas}_{ck}", fmt(sec["Gloss pass template (f.124r)"], nb=len(bands), bands=", ".join(bands), ni=len(paths), paths="\n".join(paths), out=f"{P}/f124r_gloss{pas}_{ck}.tsv"))
# sign-only leaves: generated when their bands exist (sheets/<pre>_bands.json), chunks of 8
import json
for pre, desc in (("f97r", "BnF fr.3982 f.97r, de Diou to president Jeannin, Rome, 27 October 1592"), ("f186r", "BnF fr.3984 f.186r, Desportes to Pietro Aldobrandini, Paris, 22 July 1593"), ("f189r", "BnF fr.3984 f.189r, Desportes to Hieronimo Frachetta, Paris, 22 July 1593")):
    bj = f"{HERE}/sheets/{pre}_bands.json"
    if not os.path.exists(bj): continue
    b = json.load(open(bj)); names = sorted(b["boxes"]); lines = sorted({n.split("_")[1] for n in names}); ns = max(int(n.split("_s")[1].split(".")[0]) for n in names)
    from PIL import Image
    im = Image.open(f"{HERE}/sheets/{pre}/{names[0]}")
    for k in range(0, len(lines), 8):
        bands = lines[k:k + 8]; paths = [f"{HERE}/sheets/{pre}/{pre}_{ln}_s{s}.jpg" for ln in bands for s in range(1, ns + 1) if os.path.exists(f"{HERE}/sheets/{pre}/{pre}_{ln}_s{s}.jpg")]
        for pas in "AB":
            w(f"{pre}_signs{pas}_c{k // 8 + 1}", fmt(sec["Sign pass template (leaves without gloss: f.97r, f.186r, f.189r)"], leafdesc=desc, nb=len(bands), bands=", ".join(bands), ns=ns, segw=im.width, segh=im.height, atlas=atlas, ni=len(paths), paths="\n".join(paths), out=f"{P}/{pre}_signs{pas}_c{k // 8 + 1}.tsv"))
print("written", len(os.listdir(f"{P}/prompts_f4")))
