#!/usr/bin/env python3
"""H207 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026): H193's bowl question on fr.3982 f.101r, whose 4TRI and 4STEM supports mix c/p and
a/n (H203), against the leaf's own period interlinear decipherment. Written before the call.
 tiles NATIVE SCRATCH: pool = rows of passes/f101r_align_v4.tsv (the period-gloss alignment behind key v4/v5's f.101r rows; grade C) whose code is 4TRI
   or 4STEM and whose letter is one of c, p, a, n; idx -> the reconciled draft (passes/recf101r/ciphertext_draft.tsv, DASH dropped, as
   align_period.py builds it; 3075/3075 codes checked equal) -> pass A's row at that position, kept only when pass A wrote the same code (so pass A's
   x marks this sign). Pool: 4TRI c/p 53, a/n 165; 4STEM c/p 9, a/n 13. Sample (seed 207): 10 c/p + 10 a/n under 4TRI, 9 c/p + 10 a/n under 4STEM
   = 39 targets. Each strip: 250 native px wide by the full band box the readers saw (140 px) of the Gallica native (btv1b9060543f f210; box from
   sheets/f101r_bands.json, x = box x0 + x_px/2), scaled 1.1, 30 px gap between cells, the column marked by a red triangle above (pointing down) and one
   below (pointing up), because the rows drift and a marker under the strip alone sat under the next row's gloss; numbered U01.., shuffled, 20 per sheet,
   <scratch>/h207/. Key h207_items.tsv committed before the call. Repeat control = H193's 60 strips.
 score: GATE repeat control >= 17/20, else CONTROL FAIL. Then bowl yes/no vs letter {c,p}/{a,n}, pooled and per code, Fisher exact. Pre-stated
   read-out: "the bowl splits f.101r's mixed 4-family support" iff pooled Fisher p < 0.01 AND bowl-yes answers are >= 0.75 c/p AND bowl-no
   answers are >= 0.75 a/n (n left out). Descriptive, for the verifier; no key change.
  python3 h207_bowl_101r.py tiles NATIVE SCRATCH | score [--check]"""
import csv, json, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool():
    S = defaultdict(list)
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/f101r_signsA.tsv")}; out = defaultdict(list)
    for r in rd(f"{P}/f101r_align_v4.tsv"):
        if r["kind"] != "code" or r["value"] not in ("4TRI", "4STEM") or r["plain_chunk"] not in ("c", "p", "a", "n"): continue
        s = S[r["cipher_line"]][int(r["idx"])]; assert s["sign"] == r["value"]
        a = A.get((r["cipher_line"], int(s["position"])))
        if a and a["sign"] == r["value"]:
            out[(r["value"], "CP" if r["plain_chunk"] in "cp" else "AN")].append(dict(line=r["cipher_line"], idx=r["idx"], code=r["value"], letter=r["plain_chunk"], seg=a["segment"], x=int(a["x_px"])))
    return out
def tiles(native, scratch):
    from PIL import Image, ImageDraw
    pl = pool(); rng = random.Random(207); its = []
    for k, n in ((("4TRI", "CP"), 10), (("4TRI", "AN"), 10), (("4STEM", "CP"), 9), (("4STEM", "AN"), 10)): its += rng.sample(pl[k], n)
    rng.shuffle(its); os.makedirs(f"{scratch}/h207", exist_ok=True); B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]
    nat = Image.open(native).convert("RGB"); ims = []; key = ["item\tline\tidx\tcode\tletter"]
    for n, t in enumerate(its, 1):
        # the full band box the readers saw (140 native px: up 80, down 60 round the row), the column marked by a red triangle above (pointing
        # down) and one below (pointing up), 30 px white gap between cells (prompt part 2 says so)
        b = B[f"f101r_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2; y0, y1 = b[1], b[3]; s = 1.1
        w = nat.crop((x - 125, y0, x + 125, y1)); w = w.resize((int(250 * s), int((y1 - y0) * s)))
        c = Image.new("RGB", (370, 220), "white"); c.paste(w, (5, 18)); d = ImageDraw.Draw(c); mx = 5 + int(125 * s); y = 18 + w.height
        d.polygon([(mx - 8, 1), (mx + 8, 1), (mx, 15)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 16), (mx + 8, y + 16), (mx, y + 2)], fill=(220, 0, 0))
        d.text((300, 4), f"U{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"U{n:02d}\t{t['line']}\t{t['idx']}\t{t['code']}\t{t['letter']}")
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 220), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 220))
        sh.save(f"{scratch}/h207/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h207_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "targets; pool", {k: len(v) for k, v in pl.items()})
def score():
    import h190_4fam as h190
    ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}; ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h207_reply.tsv")}
    hit = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
    out = [f"repeat control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        its = rd(f"{HERE}/h207_items.tsv")
        def tab(rows):
            t = {"yes": [0, 0], "no": [0, 0], "n": [0, 0]}
            for r in rows:
                a = ans.get(r["item"], "n"); t.setdefault(a, [0, 0])[0 if r["letter"] in "cp" else 1] += 1
            return t
        for name, rows in (("4TRI", [r for r in its if r["code"] == "4TRI"]), ("4STEM", [r for r in its if r["code"] == "4STEM"]), ("pooled", its)):
            t = tab(rows); p = h190.fisher(t["yes"][0], t["yes"][1], t["no"][0], t["no"][1])
            out.append(f"{name}: bowl yes c/p {t['yes'][0]} a/n {t['yes'][1]}; bowl no c/p {t['no'][0]} a/n {t['no'][1]}; n c/p {t['n'][0]} a/n {t['n'][1]}; Fisher p {p:.2g}")
        t = tab(its); p = h190.fisher(t["yes"][0], t["yes"][1], t["no"][0], t["no"][1])
        ys = t["yes"][0] / max(1, sum(t["yes"])); ns = t["no"][1] / max(1, sum(t["no"]))
        ok = p < 0.01 and ys >= 0.75 and ns >= 0.75
        out.append(f"read-out: bowl-yes c/p share {ys:.2f}, bowl-no a/n share {ns:.2f}, p {p:.2g} -> " + ("the bowl splits f.101r's mixed 4-family support" if ok else "the bowl does not split f.101r's mixed support by the registered rule"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h207_bowl_101r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2], sys.argv[3]) if sys.argv[1] == "tiles" else score()
