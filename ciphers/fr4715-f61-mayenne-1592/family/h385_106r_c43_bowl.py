#!/usr/bin/env python3
"""H385 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: complete f.106r's shape draft. Pass A (rows 1-18) codes 63
C43 and no 4PI; H368 read 20 C43 (seed 368), H231 some in rows 1-6. Targets: every pass-A C43 not already answered by H231/H368 at that (line, pos), cut
exactly as H368 (H231 geometry, marker above, 370x250 tiles); plus the 6 known f.61 part-2 strips of H377 (same items, cut as H367 cuts them, pasted
into a 370x250 tile). Shuffled (seed 385), R01.., 20 per sheet, SCRATCH/h385/. One blind Opus call, H359's prompt verbatim (part 1 H193's 60 strips).
Key h385_items.tsv. The runner does not look at the sheets.
score -- GATE 1 >= 17/20 H193 anchors; GATE 2 >= 5/6 known strips; else CONTROL FAIL. One-value check: if every answered target is 'no', that is the
expected answer for C43 on every leaf so far (0.95-1.00), so it is reported, not treated as a default-answer fault, when gate 2 has passed (the known
strips include 3 bowl-yes, which a default-'no' reader fails). Then: C43 no-share; and H380's comparison rerun on the completed draft (H231/H368/H385
answers, same usability rule, 20 permuted drafts, seed 385), pre-stated as H380.   python3 h385_106r_c43_bowl.py tiles SCRATCH NATIVE106 F61REGION | score [--check]"""
import csv, json, os, random, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    import h368_bowl_106r as h368
    A = rd(f"{P}/f106rall_signsA.tsv") + rd(f"{P}/f106r_signsA_c3.tsv")
    done = {(r["line"], r["pos"]) for r in rd(f"{HERE}/h231_items.tsv") + rd(f"{HERE}/h368_items.tsv")}
    return [("T", "C43", r["line"], r["pos"], r["segment"], int(float(r["x_px"]))) for r in A if r["sign"] == "C43" and (r["line"], r["pos"]) not in done], h368
def tiles(scratch, n106, f61):
    from PIL import Image, ImageDraw
    tg, h368 = targets(); kn = [(r["kind"], r["code"], r["line"], r["pos"], int(r["x_native"]), int(r["y_centre"])) for r in rd(f"{HERE}/h377_items.tsv") if r["kind"].startswith("K")]
    its = tg + kn; random.Random(385).shuffle(its); N = Image.open(n106).convert("RGB"); F = Image.open(f61).convert("RGB"); s = 1.44
    os.makedirs(f"{scratch}/h385", exist_ok=True); key = ["item\tkind\tcode\tline\tpos"]; ims = []
    for n, it in enumerate(its, 1):
        c = Image.new("RGB", (370, 250), "white"); d = ImageDraw.Draw(c)
        if it[0] == "T":
            _, code, line, pos, seg, xp = it; bx = h368.box(line, seg); x = bx[0] + xp // 3; y0, y1 = bx[1] + 20, bx[3] + 30
            w = N.crop((x - 125, y0, x + 125, y1)).resize((360, int((y1 - y0) * s))); c.paste(w.crop((0, 0, 360, min(w.height, 225))), (5, 20)); mx = 5 + int(125 * s)
        else:
            kind, code, line, pos, x, yc = it; t = F.crop((x - 150, yc - 45, x + 150, yc + 92)); t = t.resize((360, int(t.height * 1.2)))
            c.paste(t.crop((0, 0, 360, min(t.height, 225))), (5, 20)); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 17)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0)); ims.append(c)
        key.append(f"R{n:02d}\t{it[0]}\t{code}\t{line}\t{pos}")
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 250), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 250))
        sh.save(f"{scratch}/h385/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h385_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items:", len(tg), "targets + 6 known")
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h385_reply.tsv")}; items = rd(f"{HERE}/h385_items.tsv")
    g1 = sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in rd(f"{HERE}/h193_items.tsv") if r["group"] in ("CP", "AN"))
    kn = [r for r in items if r["kind"].startswith("K")]; g2 = sum(ans.get(r["item"]) == r["kind"][1:] for r in kn)
    out = [f"gate 1 (H193 anchors): {g1}/20 (>= 17); gate 2 (known part-2 strips): {g2}/6 (>= 5)"]
    if g1 < 17 or g2 < 5: out.append("CONTROL FAIL -- nothing scored")
    else:
        tg = [r for r in items if r["kind"] == "T"]; y = sum(ans.get(r["item"]) == "yes" for r in tg); n = sum(ans.get(r["item"]) == "no" for r in tg)
        out.append(f"C43 targets {len(tg)}: bowl {y}, no bowl {n}, n {len(tg) - y - n}; no-share {n / max(1, y + n):.2f}" + (" (one value; gate 2 passed)" if y == 0 else ""))
        sys.argv = [sys.argv[0], "f97r"]
        import h374_split_randctl as h374, h380_106r_shape_relabel as h380
        lab = h380.answers()
        for r in tg: lab[(r["line"], r["pos"])] = ("C43", ans.get(r["item"]))
        rows = list(open(f"{P}/recf106rall18/ciphertext_draft.tsv")); D = {tuple(l.split("\t")[:2]): l.split("\t")[2] for l in rows[1:]}
        keys = [k for k, (c, a) in sorted(lab.items()) if a in ("yes", "no") and D.get(k) == c]; av = [lab[k][1] for k in keys]
        def write(m, name):
            new = [rows[0]]
            for l in rows[1:]:
                c = l.rstrip("\n").split("\t"); a = m.get((c[0], c[1]))
                if a: c[2] = "4TRI" if a == "yes" else "C43"
                new.append("\t".join(c) + "\n")
            os.makedirs(f"{P}/{name}", exist_ok=True); open(f"{P}/{name}/ciphertext_draft.tsv", "w").write("".join(new))
        rng = random.Random(385); rand = []
        try:
            g0 = h374.gains("recf106rall18"); write(dict(zip(keys, av)), "_h385tmp_shape"); gs = h374.gains("_h385tmp_shape")
            for _ in range(20):
                a = av[:]; rng.shuffle(a); write(dict(zip(keys, a)), "_h385tmp_rand"); rand.append(h374.gains("_h385tmp_rand"))
        finally:
            for t in ("_h385tmp_shape", "_h385tmp_rand"): shutil.rmtree(f"{P}/{t}", ignore_errors=True)
        beat = sum(gs > r for r in rand); ro = "carries order information" if beat >= 19 else "no better than random" if beat <= 9 else "unclear"
        out.append(f"completed draft: {len(keys)} usable tokens (yes {av.count('yes')}, no {av.count('no')}); order gain v7 mean of 3 seeds: as transcribed "
                   f"{g0:.4f}, shape {gs:.4f}; 20 permuted drafts mean {sum(rand) / 20:.4f}, max {max(rand):.4f} -> beats {beat}/20 -> {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h385_106r_c43_bowl_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1], a[2], a[3]) if a[0] == "tiles" else score()
