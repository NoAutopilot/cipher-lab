#!/usr/bin/env python3
"""H362 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), written before the call: H359's design and prompt unchanged on fr.3982 f.101r (in-sample;
its period gloss built v7's 4TRI c/p/t; 4TRI scored 0.84 there in H355): 50 agreed 4TRI + 20 agreed C43 tokens (passes/recf101r, x from
passes/f101r_signsA.tsv, sheets/f101r_bands.json, scale 2, row centre = box top + 80), seed 362, cut from the native images/3982_f101r.jpg exactly as
H359 cuts; H193's 60 strips as part 1; one blind Opus call; reply passes/h362_reply.tsv. f.97r is not run: its draft is built from several cuts
(sheets/f97r, f97r3, f97r4) and its 4TRI scored 0.94 (H349). GATE control >= 17/20. Pre-stated: f.101r 4TRI no-share >= 0.4 (with C43 no-share >= 0.8)
-> a full split row is written; else none. Descriptive; no key change. Code below is H359's with the leaf swapped (its docstring kept after this).
  python3 h362_bowl_101r.py tiles SCRATCH | score [--check]
"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    drop = set(); A = {(r["line"], r["pos"]): r for r in rd(f"{P}/f101r_signsA.tsv")}
    B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]; out = []
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        if r["sign"] not in ("4TRI", "C43") or not r["why"].startswith("agree"): continue
        a = A.get((r["line"], r["position"]))
        if not a or a["sign"] != r["sign"] or (a["line"], a["segment"]) in drop: continue
        bx = B[f"f101r_{a['line']}_{a['segment']}.jpg"]; out.append((r["sign"], r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + 80))
    rng = random.Random(362); t4 = [t for t in out if t[0] == "4TRI"]; c43 = [t for t in out if t[0] == "C43"]
    its = rng.sample(t4, 50) + rng.sample(c43, 20); rng.shuffle(its); return its, len(t4), len(c43)
def tiles(scratch):
    from PIL import Image, ImageDraw
    its, n4, nc = targets(); nat = Image.open(f"{HERE}/images/3982_f101r.jpg").convert("RGB"); os.makedirs(f"{scratch}/h362", exist_ok=True)
    key = ["item\tcode\tline\tpos\tx_native\ty_centre"]; ims = []
    for n, (code, line, pos, x, yc) in enumerate(its, 1):
        t = nat.crop((x - 150, yc - 60, x + 150, yc + 55)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{code}\t{line}\t{pos}\t{x}\t{yc}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h362/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h362_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "targets from pools 4TRI", n4, "C43", nc)
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h362_reply.tsv")}; ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}
    hit = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
    out = [f"control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        t = defaultdict(Counter)
        for r in rd(f"{HERE}/h362_items.tsv"): t[r["code"]][ans.get(r["item"], "missing")] += 1
        out.append("by code: " + "; ".join(f"{c} " + " ".join(f"{k} {v}" for k, v in sorted(t[c].items())) for c in sorted(t)))
        sh = lambda c, a: t[c][a] / max(1, t[c]["yes"] + t[c]["no"])
        y4, n4, nc = sh("4TRI", "yes"), sh("4TRI", "no"), sh("C43", "no")
        ro = "f.101r's 4TRI mixes the no-bowl sign: write the full split row" if n4 >= 0.4 and nc >= 0.8 else "no full split for f.101r" 
        out.append(f"read-out: 4TRI yes-share {y4:.2f} no-share {n4:.2f}, C43 no-share {nc:.2f} -> {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h362_bowl_101r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
