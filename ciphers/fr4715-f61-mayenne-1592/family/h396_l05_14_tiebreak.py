#!/usr/bin/env python3
"""H396 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: f.61 L05/14 is the one conflicted target token (H194
bowl, H367 no-bowl; Tomokiyo prints c; VERIFY-F61-V11 keeps it c/p M). Items: L05/14 cut at three windows -- W1 H367's (centre -45/+92), W2 H359's
(-60/+55), W3 wider (-70/+110, pasted at the same scale, cropped to the tile) -- and the other 17 f.61 4-family tiles at H367's window (h367_items.tsv
x/y), shuffled (seed 396), R01..R20, one sheet SCRATCH/h396/sheet_01.jpg. Gate 2 = the 6 of the 17 where H194 and H367 agree (H377's known set).
One fresh blind Opus call, H359's prompt verbatim with H193's 60 strips as part 1.
score -- GATE 1 >= 17/20, GATE 2 >= 5/6, else CONTROL FAIL. Pre-stated: the majority of W1-W3 is recorded as the tie-break ('bowl' or 'no-bowl',
with the split, e.g. 2-1); 'n' answers are not votes; a tie or all-n is 'undecided'. Also the other 11 non-known tiles' agreement with H367.
No grade or key change (V11's).   python3 h396_l05_14_tiebreak.py tiles SCRATCH F61REGION | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def rep(f): return {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/{f}")}
def items():
    known = {(r["line"], r["pos"]): r["kind"][1:] for r in rd(f"{HERE}/h377_items.tsv") if r["kind"].startswith("K")}
    a367 = rep("h367_reply.tsv"); out = []
    for r in rd(f"{HERE}/h367_items.tsv"):
        k = (r["line"], r["pos"]); x, y = int(r["x_native"]), int(r["y_centre"])
        if k == ("L05", "14"):
            out += [("W1", r["code"], *k, x, y, 45, 92, ""), ("W2", r["code"], *k, x, y, 60, 55, ""), ("W3", r["code"], *k, x, y, 70, 110, "")]
        else:
            out.append(("K" if k in known else "O", r["code"], *k, x, y, 45, 92, known.get(k, a367.get(r["item"]))))
    random.Random(396).shuffle(out); return out
def tiles(scratch, f61):
    from PIL import Image, ImageDraw
    its = items(); F = Image.open(f61).convert("RGB"); os.makedirs(f"{scratch}/h396", exist_ok=True); key = ["item\tkind\tcode\tline\tpos\tref"]; ims = []
    for n, (kind, code, line, pos, x, yc, up, dn, ref) in enumerate(its, 1):
        t = F.crop((x - 150, yc - up, x + 150, yc + dn)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{kind}\t{code}\t{line}\t{pos}\t{ref}")
    sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
    for k, c in enumerate(ims): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
    sh.save(f"{scratch}/h396/sheet_01.jpg", quality=88)
    open(f"{HERE}/h396_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = rep("h396_reply.tsv"); it = rd(f"{HERE}/h396_items.tsv")
    g1 = sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in rd(f"{HERE}/h193_items.tsv") if r["group"] in ("CP", "AN"))
    g2 = sum(ans.get(r["item"]) == r["ref"] for r in it if r["kind"] == "K")
    out = [f"gate 1 (H193 anchors): {g1}/20 (>= 17); gate 2 (known f.61 strips): {g2}/6 (>= 5)"]
    if g1 < 17 or g2 < 5: out.append("CONTROL FAIL -- nothing scored")
    else:
        w = {r["kind"]: ans.get(r["item"], "missing") for r in it if r["kind"].startswith("W")}; y = sum(v == "yes" for v in w.values()); n = sum(v == "no" for v in w.values())
        ro = f"bowl ({y}-{n})" if y > n else f"no-bowl ({n}-{y})" if n > y else "undecided"
        out.append(f"L05/14 windows: W1 {w.get('W1')}, W2 {w.get('W2')}, W3 {w.get('W3')} -> tie-break: {ro} (H194 bowl, H367 no-bowl, Tomokiyo c)")
        o = [r for r in it if r["kind"] == "O" and ans.get(r["item"]) in ("yes", "no") and r["ref"] in ("yes", "no")]
        out.append(f"other f.61 tiles vs H367: {sum(ans[r['item']] == r['ref'] for r in o)}/{len(o)} agree")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h396_l05_14_tiebreak_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1], a[2]) if a[0] == "tiles" else score()
