#!/usr/bin/env python3
"""H368 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), written before the calls: the bowl question on fr.3983 f.106r (Mayenne's
secretary, f.61's hand, HELD leaf) over rows 1-18, for VERIFY-F61-V11 (PROPOSAL_v8_4tri.md). H231 read only 33 strips of rows 1-6. f.108v is not
re-read: H199 read its 4-family in full (74 strips) and H230 reproduced it (bowl sign = the readers' 4STEM there, 4TRI 0/6).
 targets -- from pass A (passes/f106rall_signsA.tsv rows 1-12 + passes/f106r_signsA_c3.tsv rows 13-18; the passes carry x, the reconciled draft does
   not): EVERY sign pass A coded 4TRI (19) or 4STEM (59), and 20 of its 63 C43 (seed 368) as the no-bowl check; the reconciled draft's 'why'
   (passes/recf106rall18, matched at the same line/position when the sign agrees, else 'unmatched') is carried in the key for reporting only.
 tiles SCRATCH NATIVE106 -- cut exactly as H231/H229 cut f.106r (H199 geometry: 250 native px wide around x = box x0 + x_px/3, box top+20 to bottom+30,
   x1.44, one red triangle above, 370x250 tiles, 20 per sheet); boxes sheets/f106r_bands.json for rows 1-6 and sheets/f106r_b_bands.json for rows
   7-18; native = Gallica btv1b9059406b f191 (sha1 5aa1a799..., as the 15:04 fetch). Shuffled (seed 368), split into two chunks c1/c2 of 49, R01..R49
   per chunk. Key h368_items.tsv. Each chunk is one blind Opus call, H359's prompt verbatim (H193's 60 strips as part 1; part 2 = the chunk's sheets).
   The runner does not look at the H368 sheets (H231's geometry was already checked on this leaf).
 score -- per chunk GATE control >= 17/20 H193 anchors; only passing chunks are used. Pre-stated read-outs over answered items (n left out):
   "f.106r's bowl sign is coded 4TRI" iff 4TRI yes-share >= 0.8 AND C43 no-share >= 0.8; "coded 4STEM" iff 4STEM yes-share >= 0.8 AND C43 no-share
   >= 0.8; "the codes mix" iff C43 no-share >= 0.8 and neither; else "unclear". Also the 4TRI no-share against H362's 0.4 bar (the two-sign 4TRI
   question) and agreement with H231 on shared rows 1-6 positions (same line and pass-A pos). Descriptive; no key, cell or grade changed.
 python3 h368_bowl_106r.py tiles SCRATCH NATIVE106 | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    A = rd(f"{P}/f106rall_signsA.tsv") + rd(f"{P}/f106r_signsA_c3.tsv")
    D = {(r["line"], r["position"]): r for r in rd(f"{P}/recf106rall18/ciphertext_draft.tsv")}
    rng = random.Random(368); c43 = [r for r in A if r["sign"] == "C43"]
    its = [r for r in A if r["sign"] in ("4TRI", "4STEM")] + rng.sample(c43, 20); rng.shuffle(its); out = []
    for r in its:
        d = D.get((r["line"], r["pos"])); why = (d["why"] or "-") if d and d["sign"] == r["sign"] else "unmatched"
        out.append(dict(code=r["sign"], line=r["line"], pos=r["pos"], seg=r["segment"], x_px=int(float(r["x_px"])), why=why))
    return out
def box(line, seg):
    f = "f106r_bands.json" if int(line[1:]) <= 6 else "f106r_b_bands.json"
    return json.load(open(f"{HERE}/sheets/{f}"))["boxes"][f"f106r_{line}_{seg}.jpg"]
def tiles(scratch, native):
    from PIL import Image, ImageDraw
    its = targets(); nat = Image.open(native).convert("RGB"); s = 1.44; key = ["chunk\titem\tcode\tline\tpos\tx_native\twhy"]
    for ci, chunk in enumerate((its[:49], its[49:]), 1):
        os.makedirs(f"{scratch}/h368_c{ci}", exist_ok=True); ims = []
        for n, t in enumerate(chunk, 1):
            bx = box(t["line"], t["seg"]); x = bx[0] + t["x_px"] // 3; y0, y1 = bx[1] + 20, bx[3] + 30
            w = nat.crop((x - 125, y0, x + 125, y1)).resize((360, int((y1 - y0) * s)))
            c = Image.new("RGB", (370, 250), "white"); c.paste(w.crop((0, 0, 360, min(w.height, 225))), (5, 20)); d = ImageDraw.Draw(c); mx = 5 + int(125 * s)
            d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 17)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0)); ims.append(c)
            key.append(f"c{ci}\tR{n:02d}\t{t['code']}\t{t['line']}\t{t['pos']}\t{x}\t{t['why']}")
        for s0 in range(0, len(ims), 20):
            sh = Image.new("RGB", (4 * 370, 5 * 250), "white")
            for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 250))
            sh.save(f"{scratch}/h368_c{ci}/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h368_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "targets", dict(Counter(t["code"] for t in its)))
def score():
    ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}; items = rd(f"{HERE}/h368_items.tsv"); out = []; ok = set(); ans = {}
    for ci in ("c1", "c2"):
        a = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h368_reply_{ci}.tsv")}
        hit = sum((a.get(m) == "yes") == (r["group"] == "CP") and a.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
        out.append(f"{ci} control: {hit} of 20 f.176v anchors (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}")
        if hit >= 17: ok.add(ci); ans.update({(ci, k): v for k, v in a.items() if k.startswith("R")})
    t = defaultdict(Counter); tw = defaultdict(Counter); got = {}
    for r in items:
        if r["chunk"] not in ok: continue
        v = ans.get((r["chunk"], r["item"]), "missing"); t[r["code"]][v] += 1; got[(r["line"], r["pos"])] = v
        tw[f"{r['code']} {'agreed' if r['why'].startswith('agree') else 'other'}"][v] += 1
    fmt = lambda T: "; ".join(f"{c} " + " ".join(f"{k} {v}" for k, v in sorted(T[c].items())) for c in sorted(T))
    out.append("by pass-A code: " + fmt(t)); out.append("by code and draft agreement: " + fmt(tw))
    sh = lambda c, a: t[c][a] / max(1, t[c]["yes"] + t[c]["no"])
    y4, n4, ys, nc = sh("4TRI", "yes"), sh("4TRI", "no"), sh("4STEM", "yes"), sh("C43", "no")
    ro = ("f.106r's bowl sign is coded 4TRI" if y4 >= 0.8 and nc >= 0.8 else "coded 4STEM" if ys >= 0.8 and nc >= 0.8 else
          "the codes mix" if nc >= 0.8 else "unclear")
    out.append(f"read-out: 4TRI yes-share {y4:.2f} (no-share {n4:.2f}; H362 bar 0.4 -> {'4TRI carries the no-bowl sign' if n4 >= 0.4 else 'below the bar'}), "
               f"4STEM yes-share {ys:.2f}, C43 no-share {nc:.2f} -> {ro}")
    h = {r["item"]: r for r in rd(f"{HERE}/h231_items.tsv")}; ha = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h231_reply.tsv")}
    both = same = 0
    for i, r in h.items():
        v = got.get((r["line"], r["pos"])); w = ha.get(i)
        if v in ("yes", "no") and w in ("yes", "no"): both += 1; same += v == w
    out.append(f"H231 agreement on shared rows 1-6 positions: {same}/{both}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h368_bowl_106r_result.txt"
    if "--check" in sys.argv:
        okc = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if okc else "STALE"); sys.exit(0 if okc else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2], sys.argv[3]) if sys.argv[1] == "tiles" else score()
