#!/usr/bin/env python3
"""H367 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the call: f.61's OWN 4-family tokens bowl-read in H359's design,
for VERIFY-F61-V11 (PROPOSAL_v8_4tri.md: the readers' 4TRI is two signs told apart by a stem-foot bowl).
 targets -- every 4TRI, C43, 4STEM and 4PI of scripts/f61_positions_all.tsv (18 signs; scripts/f61_positions_L10.tsv has none, L04 file empty):
   6 4TRI, 9 C43, 1 4STEM, 2 4PI. H194 already asked the bowl question of 15 of them (L03, L05, L08, L11) in a different design (the reader listed
   the 4-signs of a whole span sheet and the k-th was matched to the k-th code; L01 left out on a count mismatch), so this call is also H194's
   reproduction at fixed positions.
 tiles SCRATCH -- cut from the NATIVE region image images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg (verify_v9's source; sheet-A x
   mapped to native by verify_v9/v9_ca_sort.nat_x), row centre = the midpoint of that x's f61n band (verify_v9/v9_bands.json, v9_ca_sort.band_of),
   at H359's strip geometry (300 native px wide, x1.2, red triangle ABOVE the strip pointing down) but rows centre -45 to +92 -- CHANGED before the
   call from H359's -60/+55 after the runner looked at the sheet for marker placement (markers sat on the intended signs, but the f61n band midpoint
   sits high and the strips clipped every stem below the line, where the bowl is); shuffled (seed 367),
   R01..R18, one sheet. Key h367_items.tsv. Part 1 = H193's 60 strips (regenerated from natives f327/f328, sha1 a2b0d98e / 4a13be67 as H230/H359,
   h193_items.tsv byte-identical). One blind Opus call, H359's prompt verbatim with part 2 = h367/sheet_01.jpg, R01-R18.
 score -- GATE control >= 17/20 H193 anchors in their group's direction, else CONTROL FAIL. Pre-stated read-outs (n answers left out):
   "f.61 4TRI is the bowl sign" iff 4TRI yes-share >= 0.8 AND C43 no-share >= 0.8; "f.61 4TRI mixes the two signs" iff 4TRI no-share >= 0.25 AND
   C43 no-share >= 0.8; else "unclear". Also reported: every 4TRI answered 'no' (a position whose cell would move under PROPOSAL_v8_4tri.md), every
   C43/4STEM/4PI answered 'yes', and agreement with H194's answer on the shared positions ('H194 reproduces' iff >= 0.85 of the items answered
   yes/no both times agree). Descriptive; no key, cell or grade changed (the verifier's).
 python3 h367_bowl_f61.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); P = f"{HERE}/passes"
sys.path.insert(0, f"{T}/verify_v9")
FAM = ("4TRI", "C43", "4STEM", "4PI")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    import v9_ca_sort as v
    B = v.bands(); out = []
    for r in rd(f"{T}/scripts/f61_positions_all.tsv"):
        if r["class"] not in FAM: continue
        x = round(v.nat_x("A", r["line"], int(r["segment"]), int(r["x"]))); b = v.band_of(B, r["line"], x)
        out.append((r["class"], r["line"], r["pos"], x, (b[1] + b[3]) // 2))
    rng = random.Random(367); rng.shuffle(out); return out
def tiles(scratch):
    from PIL import Image, ImageDraw
    its = targets(); nat = Image.open(f"{T}/images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg").convert("RGB")
    os.makedirs(f"{scratch}/h367", exist_ok=True); key = ["item\tcode\tline\tpos\tx_native\ty_centre"]; ims = []
    for n, (code, line, pos, x, yc) in enumerate(its, 1):
        t = nat.crop((x - 150, yc - 45, x + 150, yc + 92)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{code}\t{line}\t{pos}\t{x}\t{yc}")
    sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
    for k, c in enumerate(ims): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
    sh.save(f"{scratch}/h367/sheet_01.jpg", quality=88)
    open(f"{HERE}/h367_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "targets:", dict(Counter(i[0] for i in its)))
def h194():
    """H194's answers by (line, pos): its k-th listed 4-sign of a line matched to the k-th 4-family code of that line (its own result file)."""
    fam = defaultdict(list)
    for r in rd(f"{T}/scripts/f61_positions_all.tsv"):
        if r["class"] in FAM: fam[r["line"]].append(r)
    out = {}
    for l in open(f"{HERE}/h194_bowl_f61_result.txt"):
        f = l.rstrip("\n").split("\t")
        if len(f) == 5 and f[0].startswith("L") and f[1].isdigit():
            r = fam[f[0]][int(f[1]) - 1]; assert r["class"] == f[2], (f, r["class"]); out[(f[0], r["pos"])] = f[3]
    return out
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h367_reply.tsv")}; ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}
    hit = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
    out = [f"control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        items = rd(f"{HERE}/h367_items.tsv"); t = defaultdict(Counter); prev = h194(); same = both = 0
        out.append("item\tcode\tline\tpos\tanswer\th194")
        for r in sorted(items, key=lambda r: (r["line"], int(r["pos"]))):
            a = ans.get(r["item"], "missing"); t[r["code"]][a] += 1; p = prev.get((r["line"], r["pos"]), "-")
            if a in ("yes", "no") and p in ("yes", "no"): both += 1; same += a == p
            out.append(f"{r['item']}\t{r['code']}\t{r['line']}\t{r['pos']}\t{a}\t{p}")
        out.append("by code: " + "; ".join(f"{c} " + " ".join(f"{k} {v}" for k, v in sorted(t[c].items())) for c in sorted(t)))
        sh = lambda c, a: t[c][a] / max(1, t[c]["yes"] + t[c]["no"])
        y4, n4, nc = sh("4TRI", "yes"), sh("4TRI", "no"), sh("C43", "no")
        ro = "f.61 4TRI is the bowl sign" if y4 >= 0.8 and nc >= 0.8 else "f.61 4TRI mixes the two signs" if n4 >= 0.25 and nc >= 0.8 else "unclear"
        out.append(f"read-out: 4TRI yes-share {y4:.2f} no-share {n4:.2f}, C43 no-share {nc:.2f} -> {ro}")
        mv = [f"{r['line']}/{r['pos']}" for r in items if r["code"] == "4TRI" and ans.get(r["item"]) == "no"]
        oth = [f"{r['code']} {r['line']}/{r['pos']}" for r in items if r["code"] != "4TRI" and ans.get(r["item"]) == "yes"]
        out.append(f"4TRI answered no (cell would move under PROPOSAL_v8_4tri.md): {', '.join(sorted(mv)) or 'none'}")
        out.append(f"C43/4STEM/4PI answered yes: {', '.join(sorted(oth)) or 'none'}")
        out.append(f"H194 agreement: {same}/{both} of the positions answered yes/no both times -> "
                   f"{'H194 reproduces' if both and same / both >= 0.85 else 'H194 does not reproduce'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h367_bowl_f61_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
