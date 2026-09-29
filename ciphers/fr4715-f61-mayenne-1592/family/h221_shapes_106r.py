#!/usr/bin/env python3
"""H221 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): bowl and hash forms on fr.3983 f.106r (Mayenne's secretary; six cipher rows, pass
codes on disk; its gloss passes disagreed, so the leaf is HELD and no period letter is used here). Descriptive: do this leaf's pass codes follow shape
(H218's table extended) before any of its counts are pooled into a key? Written before the calls.
 tiles SCRATCH NATIVE106: targets = every draft sign (passes/recf106r/ciphertext_draft.tsv) coded 4TRI/C43/4STEM (bowl call) or HASH4/H24 (hash call),
   with pass A's (segment, x_px) where pass A wrote the same code (else the draft row's own segment/x). Geometry: native (btv1b9059406b f191) window
   x +-60 by the band box (sheets/f106r_bands.json, x = box x0 + x_px/3), extended 30 px below the box (the bowl sits under the line), scaled 3x --
   H222's matched scale. Two sheets sets, shuffled (seeds 2211, 2212), 20 tiles per sheet:
   HASH call <scratch>/h221h/: HASH4 + H24 targets and 10 H212 anchor tiles (A 5, B 5, tile 9 excluded), H224's prompt and five categories.
   BOWL call <scratch>/h221b/: 4-family targets and 10 f.108v anchors from H199's own blind answers (bowl yes 5, no 5, seed 2213; h199_items.tsv
   geometry, cut from images/3983_f108v.jpg at 3x over x +-60), H193's bowl question (yes / no / n).
   Keys h221_items.tsv, committed before the calls; the runner looks at one sheet of each set once for marker geometry only (disclosed).
 score: GATE per call: anchors >= 8 of 10 (HASH: as their H212 group; BOWL: as H199's answer), else that call's targets are not scored.
   Pre-stated read-outs: HASH "f.106r's hash codes follow the forms" iff answered HASH4 are >= 0.8 A AND answered H24 are >= 0.8 D (N left out);
   BOWL "f.106r's 4-family codes follow the bowl" iff answered 4TRI are >= 0.8 yes AND answered C43 are >= 0.8 no (4STEM reported). Else "does not".
   Every target's answer goes to h221_positions.tsv for any later sequence step. No key change.
  python3 h221_shapes_106r.py tiles SCRATCH NATIVE106 | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
FAM = ("4TRI", "C43", "4STEM"); HSH = ("HASH4", "H24")
def targets():
    A = {(r["line"], r["pos"]): r for r in rd(f"{P}/f106r_signsA.tsv")}; out = []
    for r in rd(f"{P}/recf106r/ciphertext_draft.tsv"):
        if r["sign"] not in FAM + HSH: continue
        a = A.get((r["line"], r["position"]))
        seg, x = (a["segment"], a["x_px"]) if a and a["sign"] == r["sign"] else (r.get("segment", ""), r.get("x_px", ""))
        if not seg or not str(x).strip(): continue
        out.append(dict(kind="T", line=r["line"], pos=r["position"], code=r["sign"], seg=seg, x=int(float(x))))
    return out
def tiles(scratch, native):
    from PIL import Image, ImageDraw
    import h212_hash_sort as h212, h199_bowl_108v as h199
    ts = targets(); nat = Image.open(native).convert("RGB"); B = json.load(open(f"{HERE}/sheets/f106r_bands.json"))["boxes"]
    k212 = {r["item"]: r for r in rd(f"{HERE}/h212_items.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    geo = {(t["leaf"], t["line"], t["seg"], t["x"]): t for t in h212.items()}; anc = {"A": [], "B": []}
    for m, r in sorted(k212.items()):
        if m == "T09" or grp.get(m) not in anc: continue
        anc[grp[m]].append(dict(geo[(r["leaf"], r["line"], r["segment"], int(r["x_px"]))], kind="C", ref=m, group=grp[m]))
    rng = random.Random(2213); a199 = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h199_reply.tsv")}
    it199 = [dict(r, ans=a199.get(r["item"])) for r in rd(f"{HERE}/h199_items.tsv")]
    banc = [dict(r, kind="C", ref=r["item"], group=g) for g in ("yes", "no") for r in rng.sample([r for r in it199 if r["ans"] == g], 5)]
    n108 = Image.open(f"{HERE}/images/3983_f108v.jpg").convert("RGB"); B108 = {}
    for j in ("f108v3y_bands.json", "f108v3z_bands.json"): B108.update(json.load(open(f"{HERE}/sheets/{j}"))["boxes"])
    key = ["set\titem\tkind\tref\tline\tpos\tcode\tgroup"]
    for tag, seed, its in (("h221h", 2211, [t for t in ts if t["code"] in HSH] + rng.sample(anc["A"], 5) + rng.sample(anc["B"], 5)),
                           ("h221b", 2212, [t for t in ts if t["code"] in FAM] + banc)):
        random.Random(seed).shuffle(its); os.makedirs(f"{scratch}/{tag}", exist_ok=True); ims = []; pre = "H" if tag == "h221h" else "K"
        for n, t in enumerate(its, 1):
            c = Image.new("RGB", (370, 560), "white"); d = ImageDraw.Draw(c)
            if t["kind"] == "T":
                b = B[f"f106r_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 3
                w = nat.crop((x - 60, b[1], x + 60, b[3] + 30)).resize((360, 3 * (b[3] + 30 - b[1]))); mx = 5 + 180
                key.append(f"{tag}\t{pre}{n:02d}\tT\tf106r\t{t['line']}\t{t['pos']}\t{t['code']}\t-")
            elif tag == "h221h":
                im = Image.open(t["crop"]).convert("RGB"); x0 = max(0, min(im.width - 360, t["x"] - 180))
                w = im.crop((x0, 0, x0 + 360, im.height)); mx = 5 + (t["x"] - x0)
                key.append(f"{tag}\t{pre}{n:02d}\tC\t{t['ref']}\t{t['line']}\t-\tHASH4\t{t['group']}")
            else:
                bx = B108[os.path.basename(h199.crop(t["line"], t["segment"]))]; x = bx[0] + int(t["x_px"]) // 3
                w = n108.crop((x - 60, bx[1], x + 60, bx[3] + 30)).resize((360, 3 * (bx[3] + 30 - bx[1]))); mx = 5 + 180
                key.append(f"{tag}\t{pre}{n:02d}\tC\t{t['ref']}\t{t['line']}\t-\t{t['rec']}\t{t['group']}")
            if w.height > 500: w = w.crop((0, 0, 360, 500))
            c.paste(w, (5, 20)); y = 20 + w.height
            d.polygon([(mx - 8, 2), (mx + 8, 2), (mx, 17)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 18), (mx + 8, y + 18), (mx, y + 3)], fill=(220, 0, 0))
            d.text((330, 4), f"{pre}{n:02d}", fill=(0, 0, 0)); ims.append(c)
        for s0 in range(0, len(ims), 20):
            sh = Image.new("RGB", (4 * 370, 5 * 560), "white")
            for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 560))
            sh.save(f"{scratch}/{tag}/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
        print(tag, len(its), "tiles", Counter(t["kind"] for t in its), Counter(t.get("code") for t in its if t["kind"] == "T"))
    open(f"{HERE}/h221_items.tsv", "w").write("\n".join(key) + "\n")
def score():
    its = rd(f"{HERE}/h221_items.tsv"); out = []; pos = ["set\titem\tline\tpos\tcode\tanswer"]
    for tag, rep, norm, ok_ans in (("h221h", "h221h_reply.tsv", str.upper, None), ("h221b", "h221b_reply.tsv", str.lower, None)):
        ans = {r["id"]: norm(r["answer"].strip()) for r in rd(f"{P}/{rep}")}; rows = [r for r in its if r["set"] == tag]
        C = [r for r in rows if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == norm(r["group"]) for r in C)
        out.append(f"{tag} anchors: {hit} of {len(C)} as expected (gate >= 8): {'PASS' if hit >= 8 else 'CONTROL FAIL'}")
        if hit < 8: continue
        T = [r for r in rows if r["kind"] == "T"]; t = defaultdict(Counter)
        for r in T: t[r["code"]][ans.get(r["item"], "missing")] += 1; pos.append(f"{tag}\t{r['item']}\t{r['line']}\t{r['pos']}\t{r['code']}\t{ans.get(r['item'], 'missing')}")
        out.append(f"{tag} by code: " + "; ".join(f"{c} " + " ".join(f"{k} {v}" for k, v in sorted(t[c].items())) for c in sorted(t)))
        sh = lambda c, a, drop: t[c][a] / max(1, sum(v for k, v in t[c].items() if k not in drop))
        if tag == "h221h":
            a, dd = sh("HASH4", "A", ("N",)), sh("H24", "D", ("N",)); ok = a >= 0.8 and dd >= 0.8
            out.append(f"h221h read-out: HASH4 A-share {a:.2f}, H24 D-share {dd:.2f} -> " + ("f.106r's hash codes follow the forms" if ok else "does not follow") + f"; looped B {sum(t[c]['B'] for c in t)}")
        else:
            y, nn = sh("4TRI", "yes", ("n",)), sh("C43", "no", ("n",)); ok = y >= 0.8 and nn >= 0.8
            out.append(f"h221b read-out: 4TRI yes-share {y:.2f}, C43 no-share {nn:.2f}, 4STEM yes-share {sh('4STEM', 'yes', ('n',)):.2f} -> " + ("f.106r's 4-family codes follow the bowl" if ok else "does not follow"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h221_shapes_106r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); open(f"{HERE}/h221_positions.tsv", "w").write("\n".join(pos) + "\n"); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:4]) if sys.argv[1] == "tiles" else score()
