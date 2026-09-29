#!/usr/bin/env python3
"""H377 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: raise f.97r's N for H374 (16/20 at 78 of 127) and try the
PART-2 fix (H376).
 targets -- every remaining pass-A 4TRI of f.97r L17-L43 (A = the latest chunk's row of passes/f97r3_signsA_c3..c7; drop crops excluded) not already
   in h370/h371_items.tsv: 64 tokens, the ones the reconciled draft does not agree on or that h370's pool left out. Cut exactly as H370 (x = box x0 +
   x_px/2, centre box y0 + 70, f97r4 boxes for L22/L31; H359 geometry, marker above).
 known part-2 strips (the H376 fix) -- 6 f.61 tiles cut exactly as H367 cuts them (its geometry, from the f.61 native region image), chosen (seed 377)
   from the H367 positions where H194 and H367 gave the same answer: 3 answered yes (all 4TRI) and 3 answered no (C43); shuffled in among the 64.
 One blind Opus call, H359's prompt verbatim (part 1 H193's 60 strips; part 2 SCRATCH/h377/sheet_01..04.jpg, R01-R70). Key h377_items.tsv. The
   runner does not look at the sheets.
 score -- GATE 1: >= 17/20 H193 anchors; GATE 2: >= 5/6 known part-2 strips in their known direction; either failing -> CONTROL FAIL, nothing
   scored. Also a one-value check: if every answered target is the same value, report 'one-value chunk: re-read before use' and stop.
   If both pass: (a) no-bowl share of the 64; (b) the enlarged split: H370 + H371(after H373) + H377 answers, relabelling a draft token as C43 only
   where the draft (passes/recf97r) has 4TRI at that (line, position) and the answer is 'no'; H374's comparison on the enlarged pool (the bowl-read
   positions whose draft sign is 4TRI): shape split vs 20 random relabellings of the same count (seed 3770), v7 order gain mean of seeds 342-344.
   Pre-stated as H374 (>= 19/20 'carries order information', <= 9/20 'no better than random', else 'unclear').
 python3 h377_97r_4tri_more.py tiles SCRATCH NATIVE97 F61REGION | score [--check]"""
import csv, json, os, random, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    A = {}
    for c in (3, 4, 5, 6, 7):
        for r in rd(f"{P}/f97r3_signsA_c{c}.tsv"): A[(r["line"], r["pos"])] = r
    drop = {(r["line"], r["segment"]) for r in rd(f"{P}/f97r_drop.tsv")}
    done = {(r["line"], r["pos"]) for r in rd(f"{HERE}/h370_items.tsv") + rd(f"{HERE}/h371_items.tsv")}
    B3 = json.load(open(f"{HERE}/sheets/f97r3/f97r3_bands.json"))["boxes"]; B4 = json.load(open(f"{HERE}/sheets/f97r4/f97r4_bands.json"))["boxes"]; out = []
    for k, a in sorted(A.items()):
        if a["sign"] != "4TRI" or k in done or (a["line"], a["segment"]) in drop: continue
        bx = B4[f"f97r4_{a['line']}_{a['segment']}.jpg"] if a["line"] in ("L22", "L31") else B3[f"f97r3_{a['line']}_{a['segment']}.jpg"]
        out.append(("T", "4TRI", a["line"], a["pos"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + 70))
    return out
def known():
    it = {(r["line"], r["pos"]): r for r in rd(f"{HERE}/h367_items.tsv")}; ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h367_reply.tsv")}
    import h367_bowl_f61 as h; prev = h.h194(); ok = {"yes": [], "no": []}
    for k, r in sorted(it.items()):
        a = ans.get(r["item"])
        if a in ok and prev.get(k) == a: ok[a].append(r)
    rng = random.Random(377); pick = [("K" + a, r) for a in ("yes", "no") for r in rng.sample(ok[a], 3)]
    return [(kind, r["code"], r["line"], r["pos"], int(r["x_native"]), int(r["y_centre"])) for kind, r in pick]
def tiles(scratch, n97, f61):
    from PIL import Image, ImageDraw
    its = targets() + known(); random.Random(3771).shuffle(its); nat = {"T": Image.open(n97).convert("RGB"), "K": Image.open(f61).convert("RGB")}
    os.makedirs(f"{scratch}/h377", exist_ok=True); key = ["item\tkind\tcode\tline\tpos\tx_native\ty_centre"]; ims = []
    for n, (kind, code, line, pos, x, yc) in enumerate(its, 1):
        up, dn = (45, 92) if kind != "T" else (60, 55)       # H367's f.61 window / H359's f.97r window
        t = nat[kind[0]].crop((x - 150, yc - up, x + 150, yc + dn)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{kind}\t{code}\t{line}\t{pos}\t{x}\t{yc}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h377/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h377_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items:", sum(i[0] == "T" for i in its), "targets + 6 known")
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h377_reply.tsv")}; items = rd(f"{HERE}/h377_items.tsv")
    ctl = rd(f"{HERE}/h193_items.tsv")
    g1 = sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in ctl if r["group"] in ("CP", "AN"))
    kn = [r for r in items if r["kind"].startswith("K")]; g2 = sum(ans.get(r["item"]) == r["kind"][1:] for r in kn)
    out = [f"gate 1 (H193 anchors): {g1}/20 (>= 17); gate 2 (known part-2 strips): {g2}/6 (>= 5)"]
    tg = [r for r in items if r["kind"] == "T"]; vals = {ans.get(r["item"]) for r in tg} - {"n", None, "missing"}
    if g1 < 17 or g2 < 5: out.append("CONTROL FAIL -- nothing scored")
    elif len(vals) < 2: out.append("one-value chunk: re-read before use")
    else:
        y = sum(ans.get(r["item"]) == "yes" for r in tg); n = sum(ans.get(r["item"]) == "no" for r in tg)
        out.append(f"targets {len(tg)}: bowl {y}, no bowl {n}, n {len(tg) - y - n}; no-share {n / max(1, y + n):.2f}")
        import h374_split_randctl as h374
        lab = {}
        for f, fi in (("h370_reply.tsv", "h370_items.tsv"),):
            a = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/{f}")}
            for r in rd(f"{HERE}/{fi}"):
                if r["code"] == "4TRI": lab[(r["line"], r["pos"])] = a.get(r["item"], "missing")
        for ch in ("c1", "c2"):
            a = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h371_reply_{ch}.tsv")}
            for r in rd(f"{HERE}/h371_items.tsv"):
                if r["chunk"] == ch: lab[(r["line"], r["pos"])] = a.get(r["item"], "missing")
        for r in tg: lab[(r["line"], r["pos"])] = ans.get(r["item"], "missing")
        rows = list(open(f"{P}/recf97r/ciphertext_draft.tsv")); d4 = {tuple(l.split("\t")[:2]) for l in rows[1:] if l.split("\t")[2] == "4TRI"}
        pool = sorted(k for k in lab if k in d4); no = {k for k in pool if lab[k] == "no"}
        def write(pick, name):
            new = [rows[0]]
            for l in rows[1:]:
                c = l.rstrip("\n").split("\t")
                if c[2] == "4TRI" and (c[0], c[1]) in pick: c[2] = "C43"
                new.append("\t".join(c) + "\n")
            os.makedirs(f"{P}/{name}", exist_ok=True); open(f"{P}/{name}/ciphertext_draft.tsv", "w").write("".join(new))
        write(no, "recf97r_split2"); gs = h374.gains("recf97r_split2"); g0 = h374.gains("recf97r"); rng = random.Random(3770); rand = []
        try:
            for _ in range(20): write(set(rng.sample(pool, len(no))), "_h377tmp"); rand.append(h374.gains("_h377tmp"))
        finally:
            shutil.rmtree(f"{P}/_h377tmp", ignore_errors=True)
        beat = sum(gs > r for r in rand); ro = "carries order information" if beat >= 19 else "no better than random" if beat <= 9 else "unclear"
        out.append(f"enlarged pool (bowl-read, draft 4TRI): {len(pool)}, relabelled {len(no)}; order gain v7 mean of 3 seeds: as transcribed {g0:.4f}, "
                   f"shape split {gs:.4f}; 20 random relabellings mean {sum(rand) / 20:.4f}, max {max(rand):.4f} -> beats {beat}/20 -> {ro}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h377_97r_4tri_more_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]; sys.argv = [sys.argv[0], "f97r"]
    tiles(a[1], a[2], a[3]) if a[0] == "tiles" else score()
