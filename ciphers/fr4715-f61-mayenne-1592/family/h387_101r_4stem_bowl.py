#!/usr/bin/env python3
"""H387 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: does the readers' 4STEM on fr.3982 f.101r (the in-sample
leaf with a period gloss) split by the bowl the way its 4TRI does (H365: agreement 0.83)? H386 found 0.71 at n 17 (H207). Targets: every draft 4STEM
of passes/recf101r with why 'agree*' and pass A's sign matching (f101r_signsA.tsv), cut exactly as H365 cuts f.101r (sheets/f101r_bands.json, row
centre box top + 80, H359 geometry, marker above); plus H377's 6 known f.61 part-2 strips (H367 geometry) as gate 2. Shuffled (seed 387), R01..,
20 per sheet, SCRATCH/h387/. One blind Opus call, H359's prompt verbatim (part 1 H193's 60 strips). Native Gallica btv1b9060543f f210 (sha1 313f92b3).
score -- GATE 1 >= 17/20, GATE 2 >= 5/6, else CONTROL FAIL. Then (a) H364's cross-tab (period letter by bowl, the same letter map h364 builds from
f101r_align.tsv) for the 4STEM answers; pre-stated as H364: agreement >= 0.75 'tracks', < 0.6 'does not', else 'between'; (b) H374's comparison
for 4STEM: relabel answered 4STEM tokens bowl -> 4TRI, no -> C43 in recf101r vs 20 drafts with the same answers permuted (seed 3870), v7 order gain
mean of seeds 342-344; pre-stated as H374.   python3 h387_101r_4stem_bowl.py tiles SCRATCH NATIVE101 F61REGION | score [--check]"""
import csv, json, os, random, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    A = {(r["line"], r["pos"]): r for r in rd(f"{P}/f101r_signsA.tsv")}; B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]; out = []
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        if r["sign"] != "4STEM" or not r["why"].startswith("agree"): continue
        a = A.get((r["line"], r["position"]))
        if not a or a["sign"] != "4STEM": continue
        bx = B[f"f101r_{a['line']}_{a['segment']}.jpg"]; out.append(("T", "4STEM", r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + 80))
    return out
def tiles(scratch, n101, f61):
    from PIL import Image, ImageDraw
    kn = [(r["kind"], r["code"], r["line"], r["pos"], int(r["x_native"]), int(r["y_centre"])) for r in rd(f"{HERE}/h377_items.tsv") if r["kind"].startswith("K")]
    its = targets() + kn; random.Random(387).shuffle(its); nat = {"T": Image.open(n101).convert("RGB"), "K": Image.open(f61).convert("RGB")}
    os.makedirs(f"{scratch}/h387", exist_ok=True); key = ["item\tkind\tcode\tline\tpos\tx_native\ty_centre"]; ims = []
    for n, (kind, code, line, pos, x, yc) in enumerate(its, 1):
        up, dn = (60, 55) if kind == "T" else (45, 92)
        t = nat[kind[0]].crop((x - 150, yc - up, x + 150, yc + dn)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{kind}\t{code}\t{line}\t{pos}\t{x}\t{yc}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h387/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h387_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items:", len(its) - 6, "targets + 6 known")
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h387_reply.tsv")}; items = rd(f"{HERE}/h387_items.tsv")
    g1 = sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in rd(f"{HERE}/h193_items.tsv") if r["group"] in ("CP", "AN"))
    kn = [r for r in items if r["kind"].startswith("K")]; g2 = sum(ans.get(r["item"]) == r["kind"][1:] for r in kn)
    out = [f"gate 1 (H193 anchors): {g1}/20 (>= 17); gate 2 (known part-2 strips): {g2}/6 (>= 5)"]
    if g1 < 17 or g2 < 5: out.append("CONTROL FAIL -- nothing scored")
    else:
        tg = [r for r in items if r["kind"] == "T"]; lab = {(r["line"], r["pos"]): ans.get(r["item"], "missing") for r in tg}
        out.append(f"4STEM targets {len(tg)}: " + " ".join(f"{a} {sum(v == a for v in lab.values())}" for a in ("yes", "no", "n")))
        h364 = open(f"{HERE}/h364_101r_bowl_letter.py").read(); h364 = h364[:h364.index("ans = {r")]
        gl = {"__file__": f"{HERE}/h364_101r_bowl_letter.py", "__name__": "h387l"}; exec(compile(h364, "h364_prefix", "exec"), gl); letter = gl["letter"]
        cls = lambda L: "c/p/t" if L in ("c", "p", "t") else "a/n" if L in ("a", "n") else "other"; tab = {}
        for k, a in lab.items():
            L = letter.get(k); kk = (a, cls(L) if L else "none"); tab[kk] = tab.get(kk, 0) + 1
        out.append("period letter by bowl (4STEM): " + " ".join(f"{a}:{c} {v}" for (a, c), v in sorted(tab.items())))
        ag = tab.get(("yes", "c/p/t"), 0) + tab.get(("no", "a/n"), 0); nn = sum(v for (a, c), v in tab.items() if a in ("yes", "no") and c in ("c/p/t", "a/n"))
        r_ = ag / nn if nn else 0; out.append(f"bowl-letter agreement over 4STEM {ag}/{nn} = {r_:.2f} -> " + ("tracks" if r_ >= 0.75 else "does not" if r_ < 0.6 else "between"))
        sys.argv = [sys.argv[0], "f97r"]
        import h374_split_randctl as h374
        rows = list(open(f"{P}/recf101r/ciphertext_draft.tsv")); keys = [k for k, a in sorted(lab.items()) if a in ("yes", "no")]; av = [lab[k] for k in keys]
        def write(m, name):
            new = [rows[0]]
            for l in rows[1:]:
                c = l.rstrip("\n").split("\t"); a = m.get((c[0], c[1]))
                if c[2] == "4STEM" and a: c[2] = "4TRI" if a == "yes" else "C43"
                new.append("\t".join(c) + "\n")
            os.makedirs(f"{P}/{name}", exist_ok=True); open(f"{P}/{name}/ciphertext_draft.tsv", "w").write("".join(new))
        rng = random.Random(3870); rand = []
        try:
            g0 = h374.gains("recf101r"); write(dict(zip(keys, av)), "_h387tmp_shape"); gs = h374.gains("_h387tmp_shape")
            for _ in range(20):
                a = av[:]; rng.shuffle(a); write(dict(zip(keys, a)), "_h387tmp_rand"); rand.append(h374.gains("_h387tmp_rand"))
        finally:
            for t in ("_h387tmp_shape", "_h387tmp_rand"): shutil.rmtree(f"{P}/{t}", ignore_errors=True)
        beat = sum(gs > r for r in rand); ro = "carries order information" if beat >= 19 else "no better than random" if beat <= 9 else "unclear"
        out.append(f"4STEM relabelled by shape ({len(keys)} tokens): order gain v7 as transcribed {g0:.4f}, shape {gs:.4f}; 20 permuted drafts mean "
                   f"{sum(rand) / 20:.4f}, max {max(rand):.4f} -> beats {beat}/20 -> {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h387_101r_4stem_bowl_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1], a[2], a[3]) if a[0] == "tiles" else score()
