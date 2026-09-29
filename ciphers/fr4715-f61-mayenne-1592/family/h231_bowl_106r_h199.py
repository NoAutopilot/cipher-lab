#!/usr/bin/env python3
"""H231 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): f.106r's 4-family bowl in H199's own design, since H230 showed the bowl answers need
H193's f.176v strips in the same call. Written before the call.
 tiles SCRATCH NATIVE106: the 33 f.106r 4-family targets of H221/H229 (h229_items.tsv T rows), cut at H199 geometry exactly as h229_bowl_106r.py cuts
   them, one triangle above; shuffled (seed 231), numbered R01..R33, 20 per sheet, <scratch>/h231/. Part 1 = H193's regenerated strips
   (<scratch>/h193/, h193_items.tsv byte-identical, H230). Key h231_items.tsv committed before the call; the runner does not look at the sheets.
 One blind Opus call, H199's verbatim prompt with part 2 = <h231/sheet_01..02.jpg> (R01-R33).
 score: GATE control >= 17/20 (H193 anchors). Read-out as H221: "f.106r's 4-family codes follow the bowl" iff answered 4TRI >= 0.8 yes AND answered
   C43 >= 0.8 no; 4STEM reported. Descriptive, no key change.  python3 h231_bowl_106r_h199.py tiles SCRATCH NATIVE106 | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def tiles(scratch, native):
    from PIL import Image, ImageDraw
    import h221_shapes_106r as h221
    T = {(t["line"], t["pos"]): t for t in h221.targets()}; B = json.load(open(f"{HERE}/sheets/f106r_bands.json"))["boxes"]
    its = [r for r in rd(f"{HERE}/h229_items.tsv") if r["kind"] == "T"]; random.Random(231).shuffle(its)
    nat = Image.open(native).convert("RGB"); os.makedirs(f"{scratch}/h231", exist_ok=True); ims = []; key = ["item\tline\tpos\tcode"]; s = 1.44
    for n, r in enumerate(its, 1):
        t = T[(r["line"], r["pos"])]; bx = B[f"f106r_{t['line']}_{t['seg']}.jpg"]; x = bx[0] + t["x"] // 3
        y0, y1 = bx[1] + 20, bx[3] + 30; w = nat.crop((x - 125, y0, x + 125, y1)).resize((360, int((y1 - y0) * s)))
        c = Image.new("RGB", (370, 250), "white"); c.paste(w.crop((0, 0, 360, min(w.height, 225))), (5, 20)); d = ImageDraw.Draw(c); mx = 5 + int(125 * s)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 17)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0)); ims.append(c)
        key.append(f"R{n:02d}\t{r['line']}\t{r['pos']}\t{r['code']}")
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 250), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 250))
        sh.save(f"{scratch}/h231/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h231_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "targets", Counter(r["code"] for r in its))
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h231_reply.tsv")}; ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}
    hit = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
    out = [f"control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        t = defaultdict(Counter)
        for r in rd(f"{HERE}/h231_items.tsv"): t[r["code"]][ans.get(r["item"], "missing")] += 1
        out.append("by code: " + "; ".join(f"{c} " + " ".join(f"{k} {v}" for k, v in sorted(t[c].items())) for c in sorted(t)))
        sh = lambda c, a: t[c][a] / max(1, t[c]["yes"] + t[c]["no"])
        ok = sh("4TRI", "yes") >= 0.8 and sh("C43", "no") >= 0.8
        out.append(f"read-out: 4TRI yes-share {sh('4TRI', 'yes'):.2f}, C43 no-share {sh('C43', 'no'):.2f}, 4STEM yes-share {sh('4STEM', 'yes'):.2f} -> " + ("f.106r's 4-family codes follow the bowl" if ok else "does not follow"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h231_bowl_106r_h199_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:4]) if sys.argv[1] == "tiles" else score()
