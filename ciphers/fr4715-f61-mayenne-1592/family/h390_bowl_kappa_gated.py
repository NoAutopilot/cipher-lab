#!/usr/bin/env python3
"""H390 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: is the gated bowl reader repeatable on target tokens? 50 of
f.124r's 4TRI tokens already answered yes/no by H359/H360 (seed 390, stratified 25 of each answer so kappa is not driven by the base rate), re-cut
exactly as H359 cut them (their x_native, y_centre from h359/h360_items.tsv; native Gallica btv1b9060543f f256), plus H377's 6 known f.61 strips
(gate 2), shuffled (seed 3901), R01..R56, SCRATCH/h390/. One fresh blind Opus call, H359's prompt verbatim with H193's strips as part 1.
score -- GATE 1 >= 17/20, GATE 2 >= 5/6, else CONTROL FAIL. Pre-stated: Cohen's kappa (yes/no) between the re-read and the original answers:
>= 0.6 'the gated reader is repeatable at this design'; < 0.4 'not repeatable'; else 'moderate'. Descriptive.
python3 h390_bowl_kappa_gated.py tiles SCRATCH NATIVE124 F61REGION | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def rep(f): return {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/{f}")}
def originals():
    out = []; a = rep("h359_reply.tsv")
    for r in rd(f"{HERE}/h359_items.tsv"):
        if r["code"] == "4TRI": out.append((r, a.get(r["item"])))
    for k in range(1, 5):
        a = rep(f"h360_reply_c{k}.tsv"); out += [(r, a.get(r["item"])) for r in rd(f"{HERE}/h360_items.tsv") if r["chunk"] == f"c{k}"]
    return out
def sample():
    o = originals(); rng = random.Random(390); pick = []
    for v in ("yes", "no"): pick += rng.sample([x for x in o if x[1] == v], 25)
    return pick
def tiles(scratch, n124, f61):
    from PIL import Image, ImageDraw
    its = [("T", r["code"], r["line"], r["pos"], int(r["x_native"]), int(r["y_centre"]), a) for r, a in sample()]
    its += [(r["kind"], r["code"], r["line"], r["pos"], int(r["x_native"]), int(r["y_centre"]), r["kind"][1:]) for r in rd(f"{HERE}/h377_items.tsv") if r["kind"].startswith("K")]
    random.Random(3901).shuffle(its); nat = {"T": Image.open(n124).convert("RGB"), "K": Image.open(f61).convert("RGB")}
    os.makedirs(f"{scratch}/h390", exist_ok=True); key = ["item\tkind\tcode\tline\tpos\toriginal"]; ims = []
    for n, (kind, code, line, pos, x, yc, a) in enumerate(its, 1):
        up, dn = (60, 55) if kind == "T" else (45, 92)
        t = nat[kind[0]].crop((x - 150, yc - up, x + 150, yc + dn)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{kind}\t{code}\t{line}\t{pos}\t{a}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h390/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h390_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = rep("h390_reply.tsv"); items = rd(f"{HERE}/h390_items.tsv")
    g1 = sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in rd(f"{HERE}/h193_items.tsv") if r["group"] in ("CP", "AN"))
    g2 = sum(ans.get(r["item"]) == r["original"] for r in items if r["kind"].startswith("K"))
    out = [f"gate 1 (H193 anchors): {g1}/20 (>= 17); gate 2 (known part-2 strips): {g2}/6 (>= 5)"]
    if g1 < 17 or g2 < 5: out.append("CONTROL FAIL -- nothing scored")
    else:
        tg = [r for r in items if r["kind"] == "T"]; ks = [r for r in tg if ans.get(r["item"]) in ("yes", "no")]; n = len(ks)
        po = sum(ans[r["item"]] == r["original"] for r in ks) / n; pa = sum(ans[r["item"]] == "yes" for r in ks) / n; pb = sum(r["original"] == "yes" for r in ks) / n
        pe = pa * pb + (1 - pa) * (1 - pb); k = (po - pe) / (1 - pe)
        cm = {(o, v): sum(r["original"] == o and ans[r["item"]] == v for r in ks) for o in ("yes", "no") for v in ("yes", "no")}
        out.append(f"targets 50, answered both times {n} (re-read n: {sum(ans.get(r['item']) == 'n' for r in tg)}); original yes -> re-read yes {cm[('yes', 'yes')]} / no {cm[('yes', 'no')]}; "
                   f"original no -> re-read yes {cm[('no', 'yes')]} / no {cm[('no', 'no')]}")
        out.append(f"agreement {po:.2f}, kappa {k:.2f} -> " + ("the gated reader is repeatable at this design" if k >= 0.6 else "not repeatable" if k < 0.4 else "moderate"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h390_bowl_kappa_gated_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1], a[2], a[3]) if a[0] == "tiles" else score()
