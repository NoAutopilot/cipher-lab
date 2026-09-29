#!/usr/bin/env python3
"""H370 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: fr.3982 f.97r (de Diou, HELD leaf with an order signal
for v7, H342/H344) carries 233 agreed 4TRI but only 44 agreed C43 in passes/recf97r -- the f.124r pattern before H360 found 75% of its 4TRI to be the
no-bowl sign. H359's design on f.97r's recut rows L17-L43 (the first cut L01-L16 was superseded, NOTES.md F61-FAMILY-5).
 targets -- draft tokens 4TRI/C43 with why 'agree' or 'agree-flagged' whose pass-A sign at the same (line, position) matches (pass A = the latest
   chunk's row of passes/f97r3_signsA_c3..c7, as undec_pipeline.py pools them); crops of passes/f97r_drop.tsv excluded; boxes
   sheets/f97r4/f97r4_bands.json for L22/L31 (hand-set recut), else sheets/f97r3/f97r3_bands.json; native x = box x0 + x_px/2 (scale 2.0), row
   centre = box y0 + 70 (up 70, as f.124r's bands). Seeded sample (370): 50 4TRI + 20 C43, shuffled, R01..R70, 20 per sheet, cut exactly as H359
   (300 native px wide, centre -60 to +55, x1.2, red triangle ABOVE). Native: Gallica btv1b9060543f canvas 202 (MANIFEST.tsv). Key h370_items.tsv.
   One blind Opus call, H359's prompt verbatim (part 1 H193's 60 strips; part 2 h370/sheet_01..04.jpg, R01-R70). The runner does not look at the sheets.
 score -- GATE control >= 17/20, else CONTROL FAIL. Pre-stated (as H362): 4TRI no-share >= 0.4 AND C43 no-share >= 0.8 -> "f.97r's 4TRI mixes the
   no-bowl sign: run H371 (full split + order gain)"; 4TRI yes-share >= 0.8 AND C43 no-share >= 0.8 -> "f.97r's 4TRI is the bowl sign: H371 dropped";
   else "unclear". Descriptive; no key change.   python3 h370_bowl_97r.py tiles SCRATCH NATIVE | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool():
    A = {}
    for c in (3, 4, 5, 6, 7):
        for r in rd(f"{P}/f97r3_signsA_c{c}.tsv"): A[(r["line"], r["pos"])] = r
    drop = {(r["line"], r["segment"]) for r in rd(f"{P}/f97r_drop.tsv")}
    B3 = json.load(open(f"{HERE}/sheets/f97r3/f97r3_bands.json"))["boxes"]; B4 = json.load(open(f"{HERE}/sheets/f97r4/f97r4_bands.json"))["boxes"]; out = []
    for r in rd(f"{P}/recf97r/ciphertext_draft.tsv"):
        if int(r["line"][1:]) < 17 or r["sign"] not in ("4TRI", "C43") or not r["why"].startswith("agree"): continue
        a = A.get((r["line"], r["position"]))
        if not a or a["sign"] != r["sign"] or (a["line"], a["segment"]) in drop: continue
        bx = B4[f"f97r4_{a['line']}_{a['segment']}.jpg"] if a["line"] in ("L22", "L31") else B3[f"f97r3_{a['line']}_{a['segment']}.jpg"]
        out.append((r["sign"], r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + 70))
    return out
def targets():
    out = pool(); rng = random.Random(370); t4 = [t for t in out if t[0] == "4TRI"]; c43 = [t for t in out if t[0] == "C43"]
    its = rng.sample(t4, 50) + rng.sample(c43, 20); rng.shuffle(its); return its, len(t4), len(c43)
def tiles(scratch, native):
    from PIL import Image, ImageDraw
    its, n4, nc = targets(); nat = Image.open(native).convert("RGB"); os.makedirs(f"{scratch}/h370", exist_ok=True)
    key = ["item\tcode\tline\tpos\tx_native\ty_centre"]; ims = []
    for n, (code, line, pos, x, yc) in enumerate(its, 1):
        t = nat.crop((x - 150, yc - 60, x + 150, yc + 55)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{code}\t{line}\t{pos}\t{x}\t{yc}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h370/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h370_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "targets from pools 4TRI", n4, "C43", nc)
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h370_reply.tsv")}; ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}
    hit = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
    out = [f"control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        t = defaultdict(Counter)
        for r in rd(f"{HERE}/h370_items.tsv"): t[r["code"]][ans.get(r["item"], "missing")] += 1
        out.append("by code: " + "; ".join(f"{c} " + " ".join(f"{k} {v}" for k, v in sorted(t[c].items())) for c in sorted(t)))
        sh = lambda c, a: t[c][a] / max(1, t[c]["yes"] + t[c]["no"])
        y4, n4, nc = sh("4TRI", "yes"), sh("4TRI", "no"), sh("C43", "no")
        ro = ("f.97r's 4TRI mixes the no-bowl sign: run H371 (full split + order gain)" if n4 >= 0.4 and nc >= 0.8 else
              "f.97r's 4TRI is the bowl sign: H371 dropped" if y4 >= 0.8 and nc >= 0.8 else "unclear")
        out.append(f"read-out: 4TRI yes-share {y4:.2f} no-share {n4:.2f}, C43 no-share {nc:.2f} -> {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h370_bowl_97r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2], sys.argv[3]) if sys.argv[1] == "tiles" else score()
