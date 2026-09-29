#!/usr/bin/env python3
"""H359 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), written before the call: H358's pointer (on de Diou's fr.3982 f.124r the readers'
4TRI code also carries the no-bowl a/n sign) tested by shape, in H199's design: H193's 60 known-answer strips (f.176v anchors CP/AN + f.176r targets,
regenerated from natives f327/f328, sha1 as H230's, h193_items.tsv byte-identical) as part 1 of the same call, and part 2 = f.124r targets: 50 4TRI
and 20 C43 tokens that both f.124r sign passes wrote at the same reconciled position (passes/recf124r why 'agree' or 'agree-flagged' -- widened from 'agree' before any call, since only 54 4TRI are unflagged; x from pass A where its sign
matches; the held-out s5 crops of passes/f124r_drop.tsv excluded; seed 359), cut from the native (images/3982_f124r.jpg) at H193's strip geometry
(300 native px wide around the sign, row centre -60 to +55 native, x1.2, red triangle ABOVE the strip pointing down, as H199's part 2 -- CHANGED before the call after the runner looked at the top
of target sheet 01 for marker placement: f.124r's gloss sits BELOW its cipher rows, so a marker under the strip would sit under the gloss), shuffled, R01..R70, 20 per sheet. Key h359_items.tsv committed before the call.
One blind Opus call, H199's prompt verbatim (part 2 = h359 sheets, R01-R70).
score: GATE control >= 17/20 H193 anchors in their group's direction, else CONTROL FAIL. Pre-stated read-out: "shape supports H358's pointer" iff
f.124r 4TRI no-share >= 0.25 AND C43 no-share >= 0.8 (n answers left out); "4TRI follows the bowl on f.124r" iff 4TRI yes-share >= 0.8 AND C43 no-share
>= 0.8; else "unclear". Descriptive; no key change.   python3 h359_bowl_124r.py tiles SCRATCH | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    drop = {(r["line"], r["segment"]) for r in rd(f"{P}/f124r_drop.tsv")}; A = {(r["line"], r["pos"]): r for r in rd(f"{P}/f124r_signsA.tsv")}
    B = json.load(open(f"{HERE}/sheets/f124r_bands.json"))["boxes"]; out = []
    for r in rd(f"{P}/recf124r/ciphertext_draft.tsv"):
        if r["sign"] not in ("4TRI", "C43") or not r["why"].startswith("agree"): continue
        a = A.get((r["line"], r["position"]))
        if not a or a["sign"] != r["sign"] or (a["line"], a["segment"]) in drop: continue
        bx = B[f"f124r_{a['line']}_{a['segment']}.jpg"]; out.append((r["sign"], r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + 70))
    rng = random.Random(359); t4 = [t for t in out if t[0] == "4TRI"]; c43 = [t for t in out if t[0] == "C43"]
    its = rng.sample(t4, 50) + rng.sample(c43, 20); rng.shuffle(its); return its, len(t4), len(c43)
def tiles(scratch):
    from PIL import Image, ImageDraw
    its, n4, nc = targets(); nat = Image.open(f"{HERE}/images/3982_f124r.jpg").convert("RGB"); os.makedirs(f"{scratch}/h359", exist_ok=True)
    key = ["item\tcode\tline\tpos\tx_native\ty_centre"]; ims = []
    for n, (code, line, pos, x, yc) in enumerate(its, 1):
        t = nat.crop((x - 150, yc - 60, x + 150, yc + 55)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{code}\t{line}\t{pos}\t{x}\t{yc}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h359/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h359_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "targets from pools 4TRI", n4, "C43", nc)
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h359_reply.tsv")}; ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}
    hit = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
    out = [f"control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        t = defaultdict(Counter)
        for r in rd(f"{HERE}/h359_items.tsv"): t[r["code"]][ans.get(r["item"], "missing")] += 1
        out.append("by code: " + "; ".join(f"{c} " + " ".join(f"{k} {v}" for k, v in sorted(t[c].items())) for c in sorted(t)))
        sh = lambda c, a: t[c][a] / max(1, t[c]["yes"] + t[c]["no"])
        y4, n4, nc = sh("4TRI", "yes"), sh("4TRI", "no"), sh("C43", "no")
        ro = "shape supports H358's pointer" if n4 >= 0.25 and nc >= 0.8 else "4TRI follows the bowl on f.124r" if y4 >= 0.8 and nc >= 0.8 else "unclear"
        out.append(f"read-out: 4TRI yes-share {y4:.2f} no-share {n4:.2f}, C43 no-share {nc:.2f} -> {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h359_bowl_124r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
