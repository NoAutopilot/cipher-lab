#!/usr/bin/env python3
"""H392 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: VERIFY-F61-V10 item 6 found the a/n widening LOWERS v7's
order gain on fr.3984 f.188r (Desportes, in-sample, a 'clean-4TRI' leaf). The shape rule predicts f.188r's 4TRI is (nearly) all the bowl sign.
Targets: every draft 4TRI of passes/recf188r with why 'agree*' and pass A (passes/f188r_signsA.tsv) matching -- 66; the draft has no agreed C43 (checked
before writing: 0), so the leaf offers no no-bowl check of its own and gate 2 carries it. Cut at H359's geometry (x = box x0 + x_px/2, scale 2.0;
row centre = box y0 + 58, the bands' 'up'; sheets/f188r_bands.json), marker above; plus H377's 6 known f.61 strips (3 bowl, 3 no-bowl). Shuffled (seed
392), R01..R72, SCRATCH/h392/. One blind Opus call, H359's prompt verbatim (part 1 H193's 60 strips). Native Gallica btv1b9060633d f351 (MANIFEST.tsv).
score -- GATE 1 >= 17/20, GATE 2 >= 5/6, else CONTROL FAIL. Pre-stated: 4TRI yes-share >= 0.8 -> "f.188r's 4TRI is the bowl sign (V10's specificity
result is what the shape rule predicts)"; 4TRI no-share >= 0.4 -> "f.188r also mixes (the specificity result is not explained by shape)"; else
"unclear". Descriptive.   python3 h392_bowl_188r.py tiles SCRATCH NATIVE188 F61REGION | score [--check]"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    A = {(r["line"], r["pos"]): r for r in rd(f"{P}/f188r_signsA.tsv")}; B = json.load(open(f"{HERE}/sheets/f188r_bands.json"))["boxes"]; out = []
    for r in rd(f"{P}/recf188r/ciphertext_draft.tsv"):
        if r["sign"] != "4TRI" or not r["why"].startswith("agree"): continue
        a = A.get((r["line"], r["position"]))
        if not a or a["sign"] != "4TRI": continue
        bx = B[f"f188r_{a['line']}_{a['segment']}.jpg"]; out.append(("T", "4TRI", r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + 58))
    return out
def tiles(scratch, n188, f61):
    from PIL import Image, ImageDraw
    kn = [(r["kind"], r["code"], r["line"], r["pos"], int(r["x_native"]), int(r["y_centre"])) for r in rd(f"{HERE}/h377_items.tsv") if r["kind"].startswith("K")]
    its = targets() + kn; random.Random(392).shuffle(its); nat = {"T": Image.open(n188).convert("RGB"), "K": Image.open(f61).convert("RGB")}
    os.makedirs(f"{scratch}/h392", exist_ok=True); key = ["item\tkind\tcode\tline\tpos\tx_native\ty_centre"]; ims = []
    for n, (kind, code, line, pos, x, yc) in enumerate(its, 1):
        up, dn = (60, 55) if kind == "T" else (45, 92)
        t = nat[kind[0]].crop((x - 150, yc - up, x + 150, yc + dn)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{kind}\t{code}\t{line}\t{pos}\t{x}\t{yc}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h392/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h392_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items:", len(its) - 6, "targets + 6 known")
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h392_reply.tsv")}; items = rd(f"{HERE}/h392_items.tsv")
    g1 = sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in rd(f"{HERE}/h193_items.tsv") if r["group"] in ("CP", "AN"))
    g2 = sum(ans.get(r["item"]) == r["kind"][1:] for r in items if r["kind"].startswith("K"))
    out = [f"gate 1 (H193 anchors): {g1}/20 (>= 17); gate 2 (known part-2 strips): {g2}/6 (>= 5)"]
    if g1 < 17 or g2 < 5: out.append("CONTROL FAIL -- nothing scored")
    else:
        tg = [r for r in items if r["kind"] == "T"]; y = sum(ans.get(r["item"]) == "yes" for r in tg); n = sum(ans.get(r["item"]) == "no" for r in tg)
        ys, ns = y / max(1, y + n), n / max(1, y + n)
        ro = ("f.188r's 4TRI is the bowl sign (V10's specificity result is what the shape rule predicts)" if ys >= 0.8 else
              "f.188r also mixes (the specificity result is not explained by shape)" if ns >= 0.4 else "unclear")
        out.append(f"f.188r 4TRI {len(tg)}: bowl {y}, no bowl {n}, n {len(tg) - y - n}; yes-share {ys:.2f} -> {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h392_bowl_188r_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1], a[2], a[3]) if a[0] == "tiles" else score()
